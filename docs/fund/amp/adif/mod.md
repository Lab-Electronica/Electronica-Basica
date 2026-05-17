# Teoría básica del amplificador diferencial

## 1. Concepto general

Un **amplificador diferencial** es un circuito cuya función principal es amplificar la **diferencia entre dos señales de entrada**. A diferencia de un amplificador convencional de una sola entrada, que amplifica una señal medida respecto a masa, el amplificador diferencial compara dos tensiones de entrada y responde principalmente a la diferencia entre ellas.

Si las tensiones aplicadas a sus entradas son \(v_1\) y \(v_2\), la señal diferencial de entrada se define como:

\[
v_d = v_1 - v_2
\]

El amplificador diferencial ideal produce una salida proporcional a esa diferencia:

\[
v_o = A_d(v_1-v_2)
\]

donde \(A_d\) es la **ganancia diferencial**.

Por tanto, si ambas entradas son iguales, es decir, si \(v_1=v_2\), entonces:

\[
v_d = v_1-v_2 = 0
\]

y en un amplificador diferencial ideal la salida debida a esa señal sería nula:

\[
v_o = 0
\]

Esta propiedad es fundamental, porque permite rechazar señales que aparecen de forma común en ambas entradas, como ruido, interferencias o perturbaciones externas.

## 2. Señal diferencial y señal de modo común

Cualquier pareja de señales \(v_1\) y \(v_2\) puede descomponerse en dos componentes: una **componente diferencial** y una **componente común**. Esta descomposición facilita el desarrollo de las expresiones matemáticas necesarias para analizar el circuito. 

La **señal diferencial** se define como:

\[
v_d = v_1 - v_2
\]

La **señal de modo común** se define como el valor medio de las dos entradas:

\[
v_c = \frac{v_1+v_2}{2}
\]

A partir de estas dos magnitudes, las entradas originales pueden escribirse como:

\[
v_1 = v_c + \frac{v_d}{2}
\]

\[
v_2 = v_c - \frac{v_d}{2}
\]

Con estas expresiones se puede estudiar por separado la respuesta del amplificador ante una diferencia entre entradas y ante una señal común aplicada simultáneamente a ambas. La bondad de estas respuestas nos permiten evaluar la calidad de un amplificador diferencial y se podrá estudiar su comportamiento si necesidad de conocer cómo están construídos internamente.

## 3. Excitación diferencial

Se dice que el amplificador recibe una **excitación diferencial** cuando las dos entradas se mueven en sentidos opuestos respecto a un valor común. En el caso más simétrico:

\[
v_1 = +\frac{v_d}{2}
\]

\[
v_2 = -\frac{v_d}{2}
\]

En esta situación, el valor medio de las entradas es cero:

\[
v_c = \frac{v_1+v_2}{2}=0
\]

y toda la excitación aplicada es diferencial.

En un amplificador diferencial ideal, esta es la señal que debe ser amplificada.

## 4. Excitación en modo común

Se dice que el amplificador recibe una **excitación en modo común** cuando las dos entradas reciben exactamente la misma señal:

\[
v_1 = v_2 = v_c
\]

En ese caso, la señal diferencial es nula:

\[
v_d = v_1-v_2 = 0
\]

Un amplificador diferencial ideal no debería responder a esta excitación, porque no hay diferencia entre sus entradas. Por tanto, idealmente, la ganancia en modo común debería ser cero:

\[
A_c = 0
\]

En un circuito real, sin embargo, siempre aparece una pequeña respuesta en modo común debido a las no idealidades de los componentes y a la falta de simetría perfecta.

## 5. Modelo general de salida

En un amplificador diferencial real, la salida puede depender tanto de la señal diferencial como de la señal común. De forma general, puede escribirse:

\[
v_o = A_d v_d + A_c v_c
\]

donde:

- \(A_d\) es la **ganancia diferencial**.
- \(A_c\) es la **ganancia en modo común**.
- \(v_d\) es la señal diferencial de entrada.
- \(v_c\) es la señal común de entrada.

En un amplificador ideal se desea que:

\[
A_d \text{ sea grande}
\]

y que:

\[
A_c \text{ sea lo más pequeña posible}
\]

Idealmente:

\[
A_c = 0
\]
## 6. Ganancia diferencial

La **ganancia diferencial** indica cuánto se amplifica la diferencia entre las dos entradas. Se define como:

\[
A_d = \frac{v_o}{v_d}
\]

Si el amplificador tiene salida diferencial, formada por dos salidas \(v_{o1}\) y \(v_{o2}\), la salida diferencial se define como:

\[
v_{od}=v_{o1}-v_{o2}
\]

En ese caso, la ganancia diferencial se define como:

\[
A_d=\frac{v_{od}}{v_d}
\]

donde:

\[
v_d=v_1-v_2
\]

Esta ganancia es la más representativa del funcionamiento del amplificador diferencial, ya que mide la respuesta ante la señal que realmente se desea amplificar.

## 7. Ganancia en modo común

La **ganancia en modo común** mide la respuesta del amplificador cuando las dos entradas reciben la misma señal. Se define como:

\[
A_c=\frac{v_{oc}}{v_c}
\]

donde \(v_c\) es la señal común de entrada y \(v_{oc}\) es la salida asociada al modo común.

Si el amplificador tiene dos salidas, la salida común puede definirse como el promedio de ambas:

\[
v_{oc}=\frac{v_{o1}+v_{o2}}{2}
\]

Por tanto:

\[
A_c=\frac{v_{oc}}{v_c}
\]

En un amplificador ideal:

\[
A_c=0
\]

En la práctica, \(A_c\) es pequeño, pero no nulo.

## 8. Relación de rechazo en modo común

La **relación de rechazo en modo común**, conocida como **CMRR** por sus siglas en inglés, mide la capacidad del amplificador para amplificar señales diferenciales y rechazar señales comunes.

Se define como:

\[
CMRR=\left|\frac{A_d}{A_c}\right|
\]

Cuanto mayor sea el valor de \(CMRR\), mejor será el comportamiento diferencial del amplificador.

También suele expresarse en decibelios:

\[
CMRR_{dB}=20\log_{10}\left|\frac{A_d}{A_c}\right|
\]

Un valor alto de \(CMRR_{dB}\) indica que la ganancia diferencial es mucho mayor que la ganancia en modo común.

---

## 9. Salida simple y salida diferencial

Un amplificador diferencial puede utilizarse de dos formas principales: con **salida simple** o con **salida diferencial**.

### 9.1. Salida simple

En la configuración de salida simple se toma una sola de las salidas respecto a masa. Por ejemplo:

\[
v_o = v_{o1}
\]

o bien:

\[
v_o = v_{o2}
\]

En este caso, la ganancia medida depende de la salida elegida:

\[
A_{v1}=\frac{v_{o1}}{v_d}
\]

\[
A_{v2}=\frac{v_{o2}}{v_d}
\]

Esta forma de uso es sencilla, pero no aprovecha completamente la naturaleza diferencial del circuito.

### 9.2. Salida diferencial

En la configuración de salida diferencial se utiliza la diferencia entre las dos salidas:

\[
v_{od}=v_{o1}-v_{o2}
\]

La ganancia diferencial se calcula entonces como:

\[
A_d=\frac{v_{od}}{v_d}
\]

Esta forma suele proporcionar mayor amplitud de señal útil y mejor rechazo de perturbaciones comunes.

## 10. Signo de las ganancias

En un amplificador diferencial, las dos salidas suelen comportarse de forma complementaria. Si una salida aumenta, la otra tiende a disminuir.

Por ejemplo, si al aumentar \(v_1\) respecto a \(v_2\), la salida \(v_{o1}\) disminuye, entonces la ganancia de esa rama será negativa:

\[
A_{v1}<0
\]

Si al mismo tiempo \(v_{o2}\) aumenta, la ganancia de esa rama será positiva:

\[
A_{v2}>0
\]

Por esta razón, en las medidas experimentales es importante distinguir entre el **módulo** de la ganancia y su **signo**. Cuando se usan amplitudes pico a pico, se obtiene normalmente el módulo:

\[
|A_v|=\frac{V_{o,pp}}{V_{i,pp}}
\]

El signo debe determinarse observando si la salida está en fase o en oposición de fase respecto a la entrada.

## 11. Medida de la ganancia con una sola entrada excitada

Una forma práctica de medir la ganancia consiste en aplicar una señal a una entrada y conectar la otra a tierra de señal.

Si se aplica:

\[
v_1=v_{in}
\]

\[
v_2=0
\]

entonces la entrada diferencial vale:

\[
v_d=v_1-v_2=v_{in}
\]

Si el amplificador tiene dos salidas, pueden medirse:

\[
A_{v1}=\frac{v_{o1}}{v_{in}}
\]

\[
A_{v2}=\frac{v_{o2}}{v_{in}}
\]

En términos de amplitudes pico a pico:

\[
|A_{v1}|=\frac{V_{o1,pp}}{V_{in,pp}}
\]

\[
|A_{v2}|=\frac{V_{o2,pp}}{V_{in,pp}}
\]

El signo de cada ganancia se determina observando la fase relativa entre la entrada y la salida.

## 12. Medida de la ganancia diferencial con salida diferencial

Si se desea medir la ganancia diferencial completa, se debe obtener la diferencia entre las dos salidas:

\[
v_{od}=v_{o1}-v_{o2}
\]

La ganancia diferencial será:

\[
A_d=\frac{v_{od}}{v_{in}}
\]

cuando la segunda entrada está conectada a tierra de señal y la entrada diferencial coincide con \(v_{in}\).

En términos de amplitudes pico a pico:

\[
|A_d|=\frac{V_{od,pp}}{V_{in,pp}}
\]

donde \(V_{od,pp}\) debe obtenerse a partir de la señal diferencial \(v_{od}=v_{o1}-v_{o2}\), no restando directamente las amplitudes pico a pico de \(v_{o1}\) y \(v_{o2}\).

## 13. Medida de la ganancia en modo común

Para medir la ganancia en modo común se aplica la misma señal a las dos entradas:

\[
v_1=v_2=v_c
\]

La salida común se obtiene como:

\[
v_{oc}=\frac{v_{o1}+v_{o2}}{2}
\]

La ganancia en modo común se calcula como:

\[
A_c=\frac{v_{oc}}{v_c}
\]

En términos de amplitudes pico a pico:

\[
|A_c|=\frac{V_{oc,pp}}{V_{c,pp}}
\]

Si el amplificador fuese ideal, \(V_{oc,pp}\) sería cero. En un circuito real será pequeño, pero medible.

## 14. Interpretación de las señales

El comportamiento deseado de un amplificador diferencial puede resumirse así:

- Si las entradas son diferentes, el amplificador debe producir una salida apreciable.
- Si las entradas son iguales, el amplificador debe producir una salida nula o muy pequeña.
- Cuanto mayor sea la ganancia diferencial \(A_d\), mejor amplifica la señal útil.
- Cuanto menor sea la ganancia en modo común \(A_c\), mejor rechaza las perturbaciones comunes.
- Cuanto mayor sea el \(CMRR\), mejor es el comportamiento diferencial global.

## 15. Parámetros básicos de un amplificador diferencial

| Parámetro | Expresión | Significado |
|---|---:|---|
| Entrada diferencial | \(v_d=v_1-v_2\) | Diferencia entre entradas |
| Entrada común | \(v_c=(v_1+v_2)/2\) | Valor medio de las entradas |
| Salida diferencial | \(v_{od}=v_{o1}-v_{o2}\) | Diferencia entre salidas |
| Salida común | \(v_{oc}=(v_{o1}+v_{o2})/2\) | Valor medio de las salidas |
| Ganancia diferencial | \(A_d=v_{od}/v_d\) | Amplificación de la señal diferencial |
| Ganancia en modo común | \(A_c=v_{oc}/v_c\) | Respuesta a señales comunes |
| CMRR | \(CMRR=|A_d/A_c|\) | Rechazo del modo común |
| CMRR en dB | \(CMRR_{dB}=20\log_{10}|A_d/A_c|\) | CMRR expresado en decibelios |
| Ganancia salida simple 1 | \(A_{v1}=v_{o1}/v_d\) | Ganancia usando una salida |
| Ganancia salida simple 2 | \(A_{v2}=v_{o2}/v_d\) | Ganancia usando la otra salida |
