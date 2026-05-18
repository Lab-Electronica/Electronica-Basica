from pathlib import Path
import schemdraw
import schemdraw.elements as elm

# Salida SVG
schemdraw.use("svg")

# Fichero de salida
out_file = Path("docs/figures/circuitos/fuente_sim1.svg")
out_file.parent.mkdir(parents=True, exist_ok=True)

# Longitud de las ramas laterales
L_RAMA = 1.6

d = schemdraw.Drawing()
d.config(unit=2.5, fontsize=12)   # fondo transparente

# -------------------------
# Nodo superior
# -------------------------
d += elm.Dot()

# Rama lateral de Vcc
d.push()
d += elm.Line().right().length(L_RAMA)
d += elm.Dot().label("Vcc", loc="right")
d.pop()

# Fuente superior: + arriba, - abajo
d += elm.SourceV().down().reverse().label("V1 = Vcc", loc="left")

# -------------------------
# Nodo central
# -------------------------
d += elm.Dot()

# Rama lateral de tierra
d.push()
d += elm.Line().right().length(L_RAMA)
d += elm.Ground()
d.pop()

# Fuente inferior: + arriba, - abajo
d += elm.SourceV().down().reverse().label("V2 = Vee", loc="left")

# -------------------------
# Nodo inferior
# -------------------------
d += elm.Dot()

# Rama lateral de -Vee
d.push()
d += elm.Line().right().length(L_RAMA)
d += elm.Dot().label("-Vee", loc="right")
d.pop()

# Guardar
d.save(str(out_file))

print(f"Esquema guardado en: {out_file}")