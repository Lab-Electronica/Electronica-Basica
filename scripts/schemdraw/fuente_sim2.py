from pathlib import Path

import schemdraw
import schemdraw.elements as elm

# Usar salida SVG
schemdraw.use("svg")

# Estilo IEC / europeo para resistencias
elm.style(elm.STYLE_IEC)

# Fichero de salida
out_file = Path("docs/figures/circuitos/fuente_sim2.svg")
out_file.parent.mkdir(parents=True, exist_ok=True)

# Crear dibujo
d = schemdraw.Drawing()
d.config(unit=2.4, fontsize=12, bgcolor="white")

# -----------------------------
# Rama izquierda: fuente única
# -----------------------------
d += elm.SourceV().up().label("V")
d += elm.Dot().label("Vcc", loc="left")

# Línea horizontal superior hacia la rama de resistencias
d += elm.Line().right().length(3)

# -----------------------------
# Rama derecha: divisor resistivo
# -----------------------------
d.push()

d += elm.Resistor().down().label("R1")
d += elm.Dot()

# Tierra en el punto medio
d.push()
d += elm.Line().right().length(1.2)
d += elm.Ground()
d.pop()

d += elm.Resistor().down().label("R2")
d += elm.Dot().label("Vee", loc="right")

# -----------------------------
# Cierre inferior del circuito
# -----------------------------
d += elm.Line().left().length(3)
d += elm.Line().up().length(0)   # mantiene el punto de conexión
d += elm.Line().left().length(0)

# Volver al terminal inferior de la fuente
d += elm.Line().left().length(0)
d += elm.Line().up().length(0)

# Para cerrar de forma limpia, dibujamos la línea inferior hasta la fuente
d += elm.Line().left().length(0)

# Guardar dibujo
d.save(str(out_file))

print(f"Esquema guardado en: {out_file}")