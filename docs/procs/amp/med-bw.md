# Medida del ancho de banda

## Fundamento del método

Para la medida del ancho de banda se debe analizar la [respuesta en frecuencia del amplificador](../../fund/amp-bw.md). Aunque existen intrumentos específicos para realizar esto la medida se puede hacer de forma naual utilizando un generador de funciones y un osciloscopio.

Una forma directa de estudiar la respuesta en frecuencia de un amplificador sería variar la frecuencia con el generador de funciones y medir la ganancia en cada punto. Sin embargo, este barrido completo requiere bastante tiempo y muchas medidas.

Como ya se conoce la forma típica de la respuesta en frecuencia, puede utilizarse un método más sencillo: localizar únicamente la frecuencia de corte inferior y la frecuencia de corte superior.

## Montaje de medida

Para medir el ancho de banda se utiliza el mismo montaje básico empleado para [medir la ganancia de tensión](med-av.md). El generador de funciones aplica una señal senoidal a la entrada del amplificador y el osciloscopio permite observar simultáneamente la señal de entrada v<sub>i</sub> y la señal de salida v<sub>o</sub>.

Durante la medida se mantiene constante la amplitud de la señal de entrada y se modifica únicamente la frecuencia. De esta forma, cualquier cambio apreciable en la amplitud de salida se debe principalmente a la variación de la ganancia del amplificador con la frecuencia.

Figura X. Montaje para la medida del ancho de banda de un amplificador.

## Procedimiento de medida

Se ajusta el generador de funciones para aplicar una señal senoidal de amplitud adecuada, evitando que la salida del amplificador aparezca recortada o distorsionada. 

1. Se selecciona una frecuencia intermedia y se mide la ganancia de tensión en esa condición. Se puede realizar un barrido rápido y localizar una frecuencia a la que la ganancia se mantenga constante.

La ganancia en esta zona se toma como valor de referencia:

$$
A_{vM} = \frac{V_o}{V_i}
$$

donde V<sub>i</sub> y V<sub>o</sub> son las amplitudes pico a pico de la entrada y de la salida, respectivamente. A partir de este valor se calcula la ganancia correspondiente al punto de corte:

$$
A_{vc} = \frac{A_{vM}}{\sqrt{2}}
$$

2. Se disminuye progresivamente la frecuencia del generador, manteniendo constante la amplitud de entrada, hasta que la ganancia medida sea aproximadamente igual a A<sub>vc</sub>. La frecuencia en la que esto ocurre se identifica como frecuencia de corte inferior, f<sub>cL</sub>.

3. Se vuelve a la zona de ganancia media y se aumenta progresivamente la frecuencia hasta que la ganancia vuelva a caer hasta A<sub>vc</sub>. Esa frecuencia se identifica como frecuencia de corte superior, f<sub>cH</sub>.

Finalmente, el ancho de banda se calcula como:

$$
BW = f_{cH} - f_{cL}
$$

La medida solo debe considerarse válida si la señal de salida mantiene una forma senoidal limpia durante todo el procedimiento. Si aparecen recortes, deformaciones o saturación, debe reducirse la amplitud de entrada y repetir la medida.