# Respuesta en frecuencia de un amplificador

## Introducción

En artículos anteriores se ha estudiado algunos parámetros básicos del amplificador como la ganancia de tensión, la impedancia de entrada y la impedancia de salida. Otro parámetro importante que caracteriza su respuesta en frecuencia es el **ancho de banda**.  Este parámetroindica el margen de frecuencias en el que el amplificador puede trabajar de forma adecuada.

Idealmente, un amplificador tendría el mismo valor de ganancia A<sub>v</sub> para cualquier frecuencia. Sin embargo, en un amplificador real la ganancia no es constante. Su valor depende de la frecuencia de la señal aplicada.

Por este motivo, para conocer bien las prestaciones de un amplificador, no basta con medir su ganancia a una sola frecuencia. También es necesario estudiar cómo cambia esa ganancia cuando se modifica la frecuencia.

## Respuesta en frecuencia

Si se representa la frecuencia en el eje horizontal y el valor de la ganancia A<sub>v</sub> en el eje vertical, se obtiene la **respuesta en frecuencia** del amplificador.

En realidad, la ganancia de un amplificador puede cambiar de dos formas:

- puede cambiar su **módulo**, es decir, cuánto amplifica la señal;
- puede cambiar su **fase**, es decir, cuánto se retrasa o adelanta la señal de salida respecto a la de entrada.

En este nivel se estudiará únicamente la variación del módulo de la ganancia. Es decir, nos centraremos en cómo cambia el valor de \(|A_v|\) con la frecuencia.

## Comportamiento de un amplificador real

En muchos amplificadores reales, el módulo de la ganancia disminuye a bajas frecuencias y también a altas frecuencias. Entre ambas zonas suele existir una región intermedia donde la ganancia se mantiene aproximadamente constante, tal como se muestra en la Figura 1.

A esa zona intermedia se la suele denominar **banda media**. En ella, el amplificador trabaja de forma más cercana al comportamiento ideal.

<figure class="figura-lab01">
  <img src="../images/RespFrecuencia.jpg" alt="Respuesta en frecuencia típica de un amplificador" width=100%">
  <figcaption>Figura 1. Respuesta en frecuencia típica de un amplificador.</figcaption>
</figure>

## Frecuencias de corte

Como la ganancia no cae de forma brusca, es necesario establecer un criterio para decidir a partir de qué frecuencias el amplificador deja de comportarse como se espera.

Se definen dos frecuencias importantes:

- la **frecuencia de corte inferior**, que puede representarse como f<sub>cL</sub> o f<sub>L</sub>;
- la **frecuencia de corte superior**, que puede representarse como f<sub>cH</sub> o f<sub>H</sub>.

La frecuencia f<sub>cL</sub> marca el límite inferior de la zona útil de trabajo. Por debajo de ella, la ganancia empieza a disminuir de forma significativa.

La frecuencia f<sub>cH</sub> marca el límite superior de la zona útil de trabajo. Por encima de ella, la ganancia también disminuye de forma significativa.

## Definición de ancho de banda
El **ancho de banda**  de un amplificador se define como la diferencia entre la frecuencia de corte superior y la frecuencia de corte inferior:

$$
BW = f_{cH} - f_{cL}
$$

donde:

- \(BW\) es el ancho de banda (_BW - Bandwidth_);
- \(f_{cH}\) es la frecuencia de corte superior;
- \(f_{cL}\) es la frecuencia de corte inferior.

En muchos amplificadores, la frecuencia de corte superior es mucho mayor que la frecuencia de corte inferior. En esos casos, el valor numérico del ancho de banda queda muy próximo a f<sub>cH</sub>:

$$
BW \approx f_{cH}
$$

Esta aproximación puede ser útil, pero no debe hacer olvidar que también existe una frecuencia de corte inferior. Esa frecuencia es importante cuando se trabaja con señales de baja frecuencia.

## Criterio de corte: punto de −3 dB

Para definir las frecuencias de corte se utiliza habitualmente el criterio de **−3 dB**. Según este criterio, una frecuencia de corte es aquella en la que el módulo de la ganancia cae hasta:

$$
|A_v| = \frac{|A_{vM}|}{\sqrt{2}}
$$

donde \(|A_{vM}|\) es el valor de la ganancia en la banda media.

Como:

$$
\frac{1}{\sqrt{2}} \approx 0{,}707
$$

esto significa que, en las frecuencias de corte, la ganancia vale aproximadamente el 70,7 % de la ganancia de banda media.

En la Figura 2 se muestra la definición del ancho de banda sobre la respuesta en frecuencia del amplificador.  El valor _**A**_ es la ganancia a frecuencias medias. 

Los valores de la curva de ganancia _Av_ del amplificador real para los cuales la ganancia es **\(A/\sqrt{2}\)** definen, en el eje horizontal la frecuencia de corte inferior **\(f_{cL}\)** y superior **\(f_{cH}\)**.  Como se representa en la figura, ese valor está 3 dB por debajo del valor _A_.

<figure class="figura-lab01">
  <img src="../images/AmpBW.jpg" alt="Ancho de banda de un amplificador" width=100%">
  <figcaption>Figura 2. Ancho de banda de un amplificador.</figcaption>
</figure>

