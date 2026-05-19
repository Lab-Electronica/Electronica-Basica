# Fuente de alimentación simétrica

Una **fuente de alimentación simétrica** proporciona dos tensiones de alimentación respecto de un punto común de referencia, normalmente llamado **masa** o **tierra**. En el caso más habitual, las dos tensiones tienen el mismo valor absoluto:

\(+V_{CC}\)   y   \(-V_{CC}\)

Este tipo de alimentación es muy habitual en circuitos analógicos, especialmente en amplificadores operacionales, etapas amplificadoras discretas y circuitos que necesitan trabajar con señales alternas centradas alrededor de cero voltios.

En una fuente simétrica ideal, el punto de tierra se toma como referencia de tensión:

\(V_{GND} = 0\ \text{V}\)

## Fuente simétrica con dos fuentes de tensión

La forma más directa de construir una fuente simétrica consiste en conectar **dos fuentes de tensión continua en serie** y tomar como punto de tierra el nodo situado entre ambas fuentes.

En este montaje, si ambas fuentes tienen el mismo valor \(V_{CC}\), se obtiene:

\(V_{+}  = +V_{CC}\)   y   \(V_{-} = -V_{CC}\)

Las dos fuentes se etiquetan como:

\(E_1 = V_{CC}\)   y   \(E_2 = V_{CC}\)

El punto común entre ambas fuentes se conecta a tierra. Por tanto, la fuente superior proporciona la tensión positiva y la fuente inferior proporciona la tensión negativa respecto de ese punto de referencia.

```schemdraw name="fuente-simetrica-dos-fuentes" title="Fuente simétrica construida con dos fuentes de tensión" alt="Fuente simétrica con dos fuentes de tensión en serie y tierra en el punto medio"
# Fuente simétrica con dos fuentes en serie.
# El nodo central se toma como tierra.

d += elm.Dot()
d += elm.Line().left().length(2).label(" Vcc", loc="right")

d += elm.SourceV().down().reverse().label("E1 = Vcc ", loc="top")
d += elm.Dot()
d.push() # guardamos punto medio

d += elm.Line().right().length(2)
d += elm.Ground().label("GND = 0 V", loc="right")

d.pop() # ovlvemos a punto medio

d += elm.SourceV().down().reverse().label("E2 = Vcc ", loc="top")
d += elm.Line().right().length(2).label(" -Vcc", loc="right")
d += elm.Dot()


```

Una ventaja importante de este montaje es que permite obtener tensiones no simétricas si fuese necesario. Por ejemplo, si un circuito necesitase \(+15\ \text{V}\) y \(-5\ \text{V}\), se podrían ajustar las dos fuentes a valores diferentes: \(E_1 = 15\ \text{V}\) y \(E_2 = 5\ \text{V}\).  En ese caso, la alimentación ya no sería simétrica en valor absoluto, pero seguiría existiendo una tensión positiva y una tensión negativa respecto de la tierra común.

## Fuente simétrica básica con una fuente y dos resistencias

Otra forma sencilla de obtener un punto intermedio de referencia consiste en utilizar una única fuente de tensión continua y un **divisor resistivo** formado por dos resistencias iguales.

En este caso, la fuente total debe tener el doble de la tensión que se desea obtener en cada rama:

\[
E = 2 \cdot V_{CC}
\]

Si se conectan dos resistencias iguales en serie entre el terminal positivo y el terminal negativo de la fuente, el punto medio queda situado aproximadamente a la mitad de la tensión total. Ese punto medio puede tomarse como tierra.

```schemdraw name="fuente-simetrica-divisor-resistivo" title="Fuente simétrica básica obtenida con una fuente y dos resistencias" alt="Fuente simétrica básica con una fuente de tensión y divisor resistivo con tierra en el punto medio"
# Fuente simétrica básica mediante divisor resistivo.
# La tierra se toma en el punto medio entre las dos resistencias.

elm.ResistorIEC()

d += elm.Line().left().length(2).label("Vcc", loc="right")
d.push()
d += elm.ResistorIEC().down().label("R", loc="bottom")
d += elm.Dot()
d.push()
d += elm.Line().right().length(2)
d += elm.Ground().label("GND = 0 V", loc="right")
d.pop()
d += elm.ResistorIEC().down().label("R", loc="bottom")

d += elm.Line().right().length(2).label("-Vcc", loc="right")

# Fuente total entre los extremos del divisor.
d.pop()
d += elm.Line().left().length(2)
d += elm.Line().down().length(1.5)
d += elm.SourceV().down().reverse().label("E = 2 x Vcc ", loc="top")
d += elm.Line().down().length(1.5)
d += elm.Line().right().length(2)
```

Para que el punto medio quede centrado, las dos resistencias deben tener el mismo valor:

\[
R_1 = R_2 = R
\]

En esas condiciones, si la fuente total vale:

\[
E = 2 \cdot V_{CC}
\]

cada resistencia soporta una caída de tensión igual a:

\[
V_R = V_{CC}
\]

Por tanto, tomando como referencia el punto medio, se obtienen aproximadamente las dos tensiones:

\[
+V_{CC}
\]

\[
-V_{CC}
\]

## Elección del valor de las resistencias

En este montaje, las dos resistencias forman un divisor de tensión. La corriente que circula por ellas es:

\[
I = \frac{E}{R_1 + R_2}
\]

Como en el caso simétrico se cumple que:

\[
R_1 = R_2 = R
\]

entonces:

\[
I = \frac{2 \cdot V_{CC}}{2R}
\]

y, por tanto:

\[
I = \frac{V_{CC}}{R}
\]

El valor de \(R\) no debe elegirse de forma arbitraria. Si las resistencias son muy pequeñas, circulará una corriente elevada y se disipará mucha potencia. Si son demasiado grandes, el punto medio será muy sensible a la carga conectada y la tensión de referencia puede desplazarse.

Como criterio básico, la corriente del divisor debería ser claramente mayor que la corriente que vaya a circular por la carga conectada al punto medio. Si la carga consume una corriente apreciable, esta solución deja de ser adecuada, porque el punto de tierra ya no permanecerá centrado.

Por eso, esta forma de generar una alimentación simétrica debe entenderse como una solución **muy básica**, útil para cargas pequeñas o como explicación conceptual del punto medio de tensión.

## Potencia disipada en las resistencias

Es imprescindible comprobar la potencia que debe soportar cada resistencia.

En el caso simétrico, cada resistencia tiene aplicada una tensión:

\[
V_R = V_{CC}
\]

La potencia disipada en cada resistencia es:

\[
P_R = \frac{V_{CC}^2}{R}
\]

También puede calcularse mediante:

\[
P_R = I^2 R
\]

donde:

\[
I = \frac{V_{CC}}{R}
\]

Por seguridad, la potencia nominal de cada resistencia debe ser superior a la potencia calculada.  Es más prudente utilizar una resistencia con potencia nominal claramente superior, al menos el doble y ser consciente de que la resistencia va a elevar su temperatura por el efecto de disipación de energía.

## Ejemplo de cálculo

Supongamos que se desea obtener una alimentación simétrica de:

\[
+12\ \text{V}
\]

\[
-12\ \text{V}
\]

mediante una única fuente y dos resistencias.

La fuente total necesaria sería:

\[
E = 2 \cdot V_{CC}
\]

\[
E = 2 \cdot 12\ \text{V}
\]

\[
E = 24\ \text{V}
\]

Si se eligen dos resistencias de:

\[
R = 1\ \text{k}\Omega
\]

la corriente por el divisor será:

\[
I = \frac{V_{CC}}{R}
\]

\[
I = \frac{12\ \text{V}}{1000\ \Omega}
\]

\[
I = 0{,}012\ \text{A}
\]

\[
I = 12\ \text{mA}
\]

La potencia disipada en cada resistencia será:

\[
P_R = \frac{V_{CC}^2}{R}
\]

\[
P_R = \frac{12^2}{1000}
\]

\[
P_R = 0{,}144\ \text{W}
\]

Por tanto, cada resistencia disiparía aproximadamente:

\[
P_R = 144\ \text{mW}
\]

En este caso, una resistencia de \(0{,}25\ \text{W}\) podría funcionar desde el punto de vista teórico, pero estaría relativamente cerca de su límite. Para trabajar con más margen, sería preferible utilizar resistencias de \(0{,}5\ \text{W}\) o superiores.

## Tensiones no simétricas con divisor resistivo

El divisor resistivo también puede utilizarse para obtener tensiones no simétricas, aunque sigue siendo una solución básica y dependiente de la carga.  Suele ser más complicado encontrar los valores necesarios para resistencia de la potencia necesaria por lo que no suele ser una solución práctica. 