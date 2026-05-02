# Medida de la impedancia de salida

## Fundamento del método

La impedancia de salida puede determinarse mediante el **método del  divisor resistivo**. Se debe analizar cómo cambia la tensión de salida del amplificador cuando se conecta una resistencia de carga R<sub>L</sub>.

Si la salida del amplificador se representa mediante una fuente equivalente de tensión y una impedancia de salida Z<sub>o</sub> en serie, la resistencia de carga R<sub>L</sub> forma con Z<sub>o</sub> un divisor de tensión.

## Montaje de medida

<figure class="figura-lab01">
  <img src="../images/MedidaZout.jpg" alt="Medida de la impedancia de salida de un amplificador" width=100%">
  <figcaption>Figura 1. Medida de la impedancia de salida de un amplificador: 1) medida de la tensión de salida en vacío V<sub>oc</sub>; 2) conexión de la resistencia de carga R<sub>L</sub> y medida de la tensión V<sub>L</sub>.</figcaption>
</figure>

El procedimiento se realiza, tal como se muestra en la Figura 1, en dos pasos.

1. Se aplica la señal de prueba a la entrada del amplificador y se mide la tensión de salida en vacío, es decir, sin conectar resistencia de carga. Llamaremos a este valor V<sub>oc</sub>, siguiendo la idea de tensión en circuito abierto (_**o**open **c**ircuit_).

2. Se conecta una resistencia R<sub>L</sub> entre la salida y la referencia del circuito, y se mide de nuevo la tensión de salida. Llamaremos a este valor V<sub>L</sub>.

## Cálculo de la impedancia de salida

Con los valores anotados, si se representa la salida del amplificador mediante una fuente equivalente de tensión V<sub>oc</sub> y una impedancia de salida Z<sub>o</sub> en serie, se cumple:

$$
V_L = V_{oc} \cdot \frac{R_L}{Z_o + R_L}
$$

A partir de esta expresión puede despejarse la impedancia de salida:

$$
Z_o = R_L \cdot \left( \frac{V_{oc}}{V_L} - 1 \right)
$$

Esta expresión permite calcular la impedancia de salida a partir de una resistencia conocida y de dos medidas de tensión: la tensión de salida en vacío V<sub>oc</sub> y la tensión de salida con carga V<sub>L</sub>.

## Elección de la resistencia de carga

Para que la medida sea precisa, interesa escoger una resistencia R<sub>L</sub> del mismo orden de magnitud que la impedancia de salida esperada.

Como criterio práctico, puede elegirse inicialmente:

$$
R_L \approx Z_o
$$

Si R<sub>L</sub> fuese muy grande frente a Z<sub>o</sub>, la caída de tensión al conectar la carga sería muy pequeña y el resultado tendría peor precisión. Si R<sub>L</sub> fuese demasiado pequeña, la carga podría alterar en exceso el funcionamiento normal de la etapa e incluso provocar una señal de salida deformada o recortada.

## Comprobación de la forma de onda

No debe olvidarse comprobar que la señal de salida conserva una forma senoidal adecuada antes y después de conectar la carga.

Si al conectar R<sub>L</sub> aparecen deformaciones, recortes o achatamientos en la señal de salida, el modelo lineal deja de describir correctamente la etapa y el valor calculado de Z<sub>o</sub> deja de tener el significado buscado.

Por tanto, la medida de impedancia de salida solo debe considerarse válida si el amplificador sigue trabajando dentro de su zona normal de funcionamiento.