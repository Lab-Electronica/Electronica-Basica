# Medida de la ganancia de tensión

## Montaje de medida

Para determinar la ganancia de tensión en el laboratorio se aplica a la entrada del amplificador una señal de prueba procedente de un generador de funciones y se observan simultáneamente la entrada y la salida con un osciloscopio de dos canales, tal como se muestra en la Figura 1. La señal utilizada será una onda senoidal de frecuencia inicial igual a 1 kHz.

<figure class="figura-lab01">
  <img src="../images/MedidaAv.jpg" alt="Medida de la ganancia de tensión de un amplificador" width=100%">
  <figcaption>Figura 1.Medida de la ganancia de tensión de un amplificador .</figcaption>
</figure>

## Elección de la señal de prueba

La elección de una señal senoidal responde a varios motivos. Por una parte, una senoide es una señal simple, fácil de generar y de observar con claridad en el osciloscopio. Por otra parte, permite comprobar con facilidad si la etapa está trabajando de forma aproximadamente lineal: cuando el amplificador funciona en la zona prevista, la salida conserva aproximadamente la forma senoidal.

La elección de una frecuencia de 1 kHz es habitual en prácticas de laboratorio porque suele situarse en la banda media de funcionamiento de muchos amplificadores de baja frecuencia. A esta frecuencia, normalmente se reducen los efectos asociados a los condensadores de acoplo o desacoplo que pueden aparecer a bajas frecuencias, y todavía no suelen dominar las limitaciones debidas a capacidades parásitas, ancho de banda del dispositivo o efectos de alta frecuencia. Por ello, 1 kHz permite realizar una primera medida sencilla de la ganancia, antes de estudiar con más detalle la respuesta en frecuencia del amplificador.

## Cálculo de la ganancia

En la práctica calcularemos la ganancia a partir de las amplitudes de entrada y salida medidas en valor pico a pico. Si la forma de onda es senoidal y no está distorsionada, la relación entre valores pico, pico a pico o eficaces es fija. Por tanto, el cociente entre la amplitud de salida y la de entrada es el mismo cualquiera que sea la magnitud utilizada, siempre que se use la misma en ambos casos. Se suele utilizar el valor pico a pico porque es el más directo de leer en el osciloscopio.

Así, si \(V_i\) es la amplitud pico a pico de la señal de entrada y \(V_o\) la amplitud pico a pico de la señal de salida, la ganancia de tensión se obtiene como:

$$
A_v = \frac{V_o}{V_i}
$$

## Ganancia con inversión de fase

Si la salida aparece invertida respecto a la entrada, puede indicarse además que existe un desfase aproximado de \(180^\circ\). En ese caso, desde el punto de vista físico, sigue siendo correcto afirmar que el módulo de la ganancia vale:

$$
|A_v| = \frac{V_o}{V_i}
$$

y que la etapa es inversora.

## Comprobación de la forma de onda

Es muy importante no limitarse a leer dos amplitudes y aplicar una fórmula. Antes de anotar los valores debe comprobarse que la señal de salida mantiene una forma senoidal limpia. Si se observan recortes, achatamientos o deformaciones, la etapa ya no está trabajando en la zona de funcionamiento para la que el modelo lineal resulta válido.

Esto suele ocurrir cuando la señal de entrada es demasiado grande y, al ser amplificada, obliga al transistor a salir de la región de funcionamiento prevista por el diseño. En esa situación, el cociente entre amplitudes deja de representar correctamente la ganancia lineal de la etapa.