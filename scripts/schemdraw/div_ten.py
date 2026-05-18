import schemdraw
import schemdraw.elements as elm

# Estilo europeo / IEC para resistencias
elm.style(elm.STYLE_IEC)

# Usamos salida SVG directa
schemdraw.use("svg")

with schemdraw.Drawing(
    file="docs/figures/circuitos/div_ten.svg"
) as d:
    d.config(unit=2.5)

    d += elm.SourceV().up().label("$V_i$")
    d += elm.Resistor().right().label("$R_1$")
    d += elm.Dot()
    d += elm.Line().right().label("$V_o$", loc="right")
    d += elm.Line().left()
    d += elm.Resistor().down().label("$R_2$")
    d += elm.Ground()
    d += elm.Line().left()