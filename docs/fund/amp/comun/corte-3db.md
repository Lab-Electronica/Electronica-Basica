# Criterio de −3 dB
## Definición

El criterio de −3 dB se utiliza para definir puntos de corte en la respuesta de un circuito electrónico, especialmente en amplificadores y filtros.

Este criterio no es arbitrario. Se adopta porque indica el punto en el que la potencia entregada se reduce a la mitad respecto a un valor de referencia del circuito, manteniendo constantes las demás condiciones de medida.

## Valor de referencia
Para aplicar este criterio es necesario definir primero cuál es el valor de referencia.

En un amplificador, ese valor suele ser la ganancia de la zona donde la respuesta es aproximadamente constante. En un filtro, suele tomarse como referencia el valor máximo de la respuesta en la banda de paso.

A partir de ese valor de referencia, se considera que una frecuencia es de corte cuando la potencia se ha reducido a la mitad.

## Relación con la tensión
En muchos casos de laboratorio no se mide directamente la potencia, sino la tensión. Por eso es útil relacionar el criterio de media potencia con una caída de tensión.

La potencia en una resistencia puede expresarse como:

$$
P = \frac{V^2}{R}
$$

Si la tensión cae a un valor \(1/\sqrt{2}\) del valor inicial, la potencia queda:

$$
P = \frac{\left(\frac{V}{\sqrt{2}}\right)^2}{R} = \frac{V^2}{2R}
$$

Por tanto, la potencia se ha reducido a la mitad.

Como:

$$
\frac{1}{\sqrt{2}} \approx 0{,}707
$$

el punto de −3 dB corresponde aproximadamente al 70,7 % del valor de tensión de referencia.

## Interpretación
Por esta razón, las frecuencias de corte también se denominan **frecuencias de media potencia** o **puntos de −3 dB**.

En la práctica, si se está midiendo una tensión de salida, el punto de corte se identifica cuando dicha tensión cae hasta aproximadamente el 70,7 % del valor de referencia.

## Utilización de la unidad decibelio
El decibelio, dB, es una forma logarítmica de expresar relaciones entre magnitudes. En electrónica se utiliza mucho porque permite representar cómodamente variaciones muy grandes o muy pequeñas de ganancia, atenuación o potencia.

Cuando se comparan dos potencias, la relación en decibelios se calcula como:

$$
G_{dB} = 10 \log_{10}\left(\frac{P_2}{P_1}\right)
$$

donde \(P_1\) es la potencia de referencia y \(P_2\) es la potencia considerada.

En el punto de media potencia se cumple:

$$
P_2 = \frac{P_1}{2}
$$

Por tanto:

$$
G_{dB} = 10 \log_{10}\left(\frac{P_1/2}{P_1}\right)  = 10 \log_{10}\left(\frac{1}{2}\right) \approx -3{,}01\ \text{dB}
$$

Por este motivo, el punto en el que la potencia cae a la mitad se denomina habitualmente **punto de −3 dB**.

## Relación entre −3 dB y la tensión
Cuando se trabaja sobre la misma resistencia, la potencia es proporcional al cuadrado de la tensión:

$$
P = \frac{V^2}{R}
$$

Si la potencia se reduce a la mitad, la tensión no se reduce a la mitad, sino a:

$$
V_2 = \frac{V_1}{\sqrt{2}}
$$

Por tanto, la relación entre tensiones es:

$$
\frac{V_2}{V_1} = \frac{1}{\sqrt{2}}
$$

Si se expresa esta relación de tensiones en decibelios, se utiliza:

$$
G_{dB} = 20 \log_{10}\left(\frac{V_2}{V_1}\right)
$$

Sustituyendo:

$$
G_{dB} = 20 \log_{10}\left(\frac{1}{\sqrt{2}}\right) \approx -3{,}01\ \text{dB}
$$

Por eso, en una medida de tensión, el punto de −3 dB se identifica cuando la amplitud cae hasta \(V_1/\sqrt{2}\), es decir, aproximadamente el 70,7 % del valor de referencia.
