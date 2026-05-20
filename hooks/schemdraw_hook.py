from __future__ import annotations

import hashlib
import html
import os
import posixpath
import re
import shlex
import shutil
import unicodedata
from pathlib import Path

import schemdraw
import schemdraw.elements as elm
from mkdocs.exceptions import PluginError


SCHEMDRAW_BLOCK_RE = re.compile(
    r"```schemdraw(?P<attrs>[^\n]*)\n(?P<code>.*?)\n```",
    re.DOTALL,
)

# Tema común para los circuitos
SCHEMDRAW_THEME = {
    "wire_color": "#1E5AA8",
    "component_color": "#222222",
    "fill_color": "#F7F9FC",
    "text_color": "#111827",
    "wire_lw": 1.8,
    "component_lw": 1.6,
    "font": "Arial",
    "fontsize": 12,
}


def _slugify(text: str) -> str:
    """
    Convierte un texto en un nombre de archivo seguro.
    """
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text or "circuito"


def _parse_attrs(attrs: str) -> dict[str, str]:
    """
    Permite atributos sencillos en la cabecera del bloque:

    ```schemdraw name="divisor" title="Divisor de tensión" alt="Circuito divisor"
    ...
    ```
    """
    result: dict[str, str] = {}

    attrs = attrs.strip()
    if not attrs:
        return result

    try:
        parts = shlex.split(attrs)
    except ValueError as exc:
        raise PluginError(f"Error leyendo atributos de bloque schemdraw: {exc}") from exc

    for part in parts:
        if "=" in part:
            key, value = part.split("=", 1)
            result[key.strip()] = value.strip()
        else:
            result[part.strip()] = "true"

    return result


def _page_source_dir(page) -> str:
    """
    Carpeta del archivo Markdown dentro de docs/.

    Ejemplo:
    docs/procs/amp/med-av.md -> procs/amp
    docs/index.md            -> ""
    """
    src_path = Path(page.file.src_path)
    parent = src_path.parent.as_posix()
    return "" if parent == "." else parent


def _page_stem(page) -> str:
    """
    Nombre base del Markdown sin extensión.
    """
    return Path(page.file.src_path).stem


def _page_output_dir(page) -> str:
    """
    Carpeta URL desde la que se resolverán las rutas relativas en el HTML final.

    Con use_directory_urls: true:
      procs/amp/med-av.md -> procs/amp/med-av/

    Con use_directory_urls: false:
      procs/amp/med-av.md -> procs/amp/med-av.html
    """
    url = page.file.url or ""

    if url.endswith("/"):
        return url.strip("/")

    return posixpath.dirname(url)


def _relative_url_from_page(page, asset_path: str) -> str:
    """
    Calcula una URL relativa desde la página HTML hasta el SVG.

    asset_path debe ser una ruta relativa a docs/, con separadores '/'.
    """
    page_dir = _page_output_dir(page)

    if not page_dir:
        return asset_path

    rel = posixpath.relpath(asset_path, start=page_dir)
    return rel


def _render_schemdraw_svg(code: str, svg_path: Path) -> None:
    """
    Ejecuta el código SchemDraw y guarda el SVG.

    El código del bloque dispone de:
      - schemdraw
      - elm
      - d

    Ejemplo dentro del Markdown:
      d += elm.Resistor().right().label("R1")
    """
    svg_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        schemdraw.use("svg")

        d = schemdraw.Drawing(show=False, canvas="svg")

        # aplicamos el tema definido para el circuito
        d.config(
            color=SCHEMDRAW_THEME["component_color"],
            lw=SCHEMDRAW_THEME["component_lw"],
            fill=SCHEMDRAW_THEME["fill_color"],
            font=SCHEMDRAW_THEME["font"],
            fontsize=SCHEMDRAW_THEME["fontsize"],
        )

        safe_globals = {
            "__builtins__": {
                "abs": abs,
                "min": min,
                "max": max,
                "round": round,
                "range": range,
                "len": len,
                "float": float,
                "int": int,
                "str": str,
            },
            "schemdraw": schemdraw,
            "elm": elm,
        }

        safe_locals = {
            "d": d,
        }

        exec(code, safe_globals, safe_locals)

        drawing = safe_locals.get("d", d)
        drawing.save(str(svg_path))

    except Exception as exc:
        raise PluginError(
            "Error generando un bloque schemdraw. "
            f"Archivo SVG previsto: {svg_path}. "
            f"Detalle: {exc}"
        ) from exc


def _copy_to_site_dir(config, source_svg: Path, asset_path: str) -> None:
    """
    Copia también el SVG al site_dir.

    Esto evita depender de que MkDocs haya detectado el SVG como archivo estático
    antes de que el hook lo genere.
    """
    site_dir = Path(config["site_dir"])
    target = site_dir / Path(asset_path)

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_svg, target)


def on_page_markdown(markdown: str, page, config, files) -> str:
    """
    Busca bloques ```schemdraw ... ``` en cada página Markdown,
    genera el SVG y sustituye el bloque por una figura HTML.

    La numeración de figuras se reinicia en cada archivo Markdown.
    """
    docs_dir = Path(config["docs_dir"])

    source_dir = _page_source_dir(page)
    page_stem = _page_stem(page)

    figure_counter = 0

    def replace_block(match: re.Match) -> str:
        nonlocal figure_counter

        attrs = _parse_attrs(match.group("attrs"))
        code = match.group("code").strip()

        title = attrs.get("title", "")
        alt = attrs.get("alt", title or "Circuito generado con SchemDraw")
        name = attrs.get("name", title or page_stem or "circuito")
        css_class = attrs.get("class", "schemdraw-figure")
        width = attrs.get("width", "")

        show_caption = attrs.get("caption", "true").lower() != "false"
        numbered = attrs.get("numbered", "true").lower() != "false"

        code_hash = hashlib.sha1(code.encode("utf-8")).hexdigest()[:10]
        file_name = f"{_slugify(page_stem)}-{_slugify(name)}-{code_hash}.svg"

        asset_dir = posixpath.join(source_dir, "images", "svg") if source_dir else "images/svg"
        asset_path = posixpath.join(asset_dir, file_name)

        svg_source_path = docs_dir / Path(asset_path)

        _render_schemdraw_svg(code, svg_source_path)
        _copy_to_site_dir(config, svg_source_path, asset_path)

        img_src = _relative_url_from_page(page, asset_path)

        img_style = ""
        if width:
            img_style = f' style="max-width: {html.escape(width)}; width: 100%; height: auto;"'

        figure = [
            f'<figure class="{html.escape(css_class)}">',
            f'  <img src="{html.escape(img_src)}" alt="{html.escape(alt)}"{img_style}>',
        ]

        if show_caption:
            if numbered:
                figure_counter += 1

                if title:
                    caption_text = f"Figura {figure_counter}. {title}"
                else:
                    caption_text = f"Figura {figure_counter}"
            else:
                caption_text = title

            if caption_text:
                figure.append(f'  <figcaption>{html.escape(caption_text)}</figcaption>')

        figure.append("</figure>")

        return "\n".join(figure)

    return SCHEMDRAW_BLOCK_RE.sub(replace_block, markdown)