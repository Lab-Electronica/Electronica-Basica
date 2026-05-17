# Amplificador diferencial NMOS con espejo de corriente

## 1. Idea general del circuito

Un **amplificador diferencial NMOS** es un circuito formado por dos transistores de entrada, \(M_1\) y \(M_2\), cuyas fuentes están unidas en un nodo común. Este nodo se polariza mediante una fuente de corriente, que en este caso se implementa con un **espejo de corriente NMOS**, formado por \(M_3\) y \(M_4\).

La función principal del amplificador diferencial es amplificar la diferencia entre dos señales de entrada. Si las tensiones aplicadas a las puertas de \(M_1\) y \(M_2\) son \(v_{g1}\) y \(v_{g2}\), la señal diferencial de entrada se define como \(v_{id}=v_{g1}-v_{g2}\).

El circuito idealmente responde a esta diferencia y rechaza las señales comunes, es decir, aquellas que aparecen simultáneamente y con el mismo valor en ambas entradas.

En reposo, si el circuito es simétrico, la corriente de cola \(I_T\) fijada por el espejo de corriente se reparte aproximadamente por igual entre las dos ramas: \(I_{D1}=I_{D2}=I_T/2\).

Las salidas se toman normalmente en los drenadores de \(M_1\) y \(M_2\), y se denominan \(v_{o1}\) y \(v_{o2}\). Estas dos salidas son complementarias: cuando una sube, la otra tiende a bajar.

## 2. Papel del espejo de corriente

El espejo de corriente formado por \(M_3\) y \(M_4\) se utiliza para fijar la corriente total que circula por el par diferencial. En un espejo ideal, la corriente de referencia generada en \(M_3\) se copia en \(M_4\), de forma que \(M_4\) actúa como fuente de corriente de cola.

En un circuito real, la corriente copiada no es exactamente igual a la de referencia porque los transistores tienen resistencia de salida finita. Esta no idealidad influye especialmente en la **ganancia en modo común**, ya que una fuente de corriente no ideal permite que el nodo común de las fuentes varíe con la señal común de entrada.

## 3. Parámetros básicos del transistor MOS

Para un NMOS en saturación, despreciando inicialmente la modulación de canal, la corriente de drenador puede aproximarse mediante:

\[
I_D \approx \frac{1}{2}\beta (V_{GS}-V_{TH})^2
\]

Donde \(\beta\) depende del proceso tecnológico y de las dimensiones del transistor:

\[
\beta=K_p\frac{W}{L}
\]

La tensión de sobreexcitación o sobretensión de puerta se define como:

\[
V_{OV}=V_{GS}-V_{TH}
\]

Con esta definición, la corriente puede escribirse como:

\[
I_D \approx \frac{1}{2}\beta V_{OV}^2
\]

La transconductancia del transistor es:

\[
g_m=\frac{\partial I_D}{\partial V_{GS}}
\]

Para el modelo cuadrático ideal:

\[
g_m=\beta V_{OV}
\]

También puede expresarse como:

\[
g_m=\frac{2I_D}{V_{OV}}
\]

O bien:

\[
g_m=\sqrt{2\beta I_D}
\]

Si se considera la modulación de longitud de canal, aparece una resistencia de salida \(r_o\), aproximadamente:

\[
r_o=\frac{1}{\lambda I_D}
\]

Donde \(\lambda\) es el parámetro de modulación de canal.

La resistencia equivalente de carga en cada rama de salida suele ser:

\[
R_D'=R_D \parallel r_o
\]

Si \(r_o\) es mucho mayor que \(R_D\), puede aproximarse:

\[
R_D' \approx R_D
\]

## 4. Ganancia diferencial

La señal diferencial de entrada es \(v_{id}=v_{g1}-v_{g2}\). La salida diferencial se define como:

\[
v_{od}=v_{o1}-v_{o2}
\]

La ganancia diferencial es:

\[
A_d=\frac{v_{od}}{v_{id}}
\]

Si se aplica una excitación diferencial simétrica, es decir, \(v_{g1}=+v_{id}/2\) y \(v_{g2}=-v_{id}/2\), entonces las ganancias de cada salida respecto a la entrada diferencial son aproximadamente:

\[
\frac{v_{o1}}{v_{id}}\approx -\frac{g_mR_D'}{2}
\]

\[
\frac{v_{o2}}{v_{id}}\approx +\frac{g_mR_D'}{2}
\]

Por tanto, la ganancia diferencial con salida diferencial vale:

\[
A_d=\frac{v_{o1}-v_{o2}}{v_{id}}\approx -g_mR_D'
\]

En valor absoluto:

\[
|A_d|\approx g_mR_D'
\]

El signo depende de cómo se defina la resta de salida y de qué entrada se tome como positiva.

## 5. Ganancia con una sola entrada excitada

En muchos ensayos prácticos se aplica señal a una sola entrada y la otra se conecta a tierra de señal. Por ejemplo, \(v_{g1}=v_{in}\) y \(v_{g2}=0\). En ese caso:

\[
v_{id}=v_{g1}-v_{g2}=v_{in}
\]

Las ganancias de salida simple se definen como:

\[
A_{v1}=\frac{v_{o1}}{v_{in}}
\]

\[
A_{v2}=\frac{v_{o2}}{v_{in}}
\]

En un circuito ideal y equilibrado:

\[
A_{v1}\approx -\frac{g_mR_D'}{2}
\]

\[
A_{v2}\approx +\frac{g_mR_D'}{2}
\]

La salida del lado excitado suele estar invertida respecto a la entrada, mientras que la salida del lado opuesto suele estar en fase. Si se excita la entrada de \(M_2\) y se conecta la entrada de \(M_1\) a tierra de señal, las ganancias se intercambian por simetría.

## 6. Ganancia en modo común

La señal de modo común se define cuando ambas entradas reciben la misma señal:

\[
v_{g1}=v_{g2}=v_{ic}
\]

La salida común se define como el promedio de las dos salidas:

\[
v_{oc}=\frac{v_{o1}+v_{o2}}{2}
\]

La ganancia en modo común es:

\[
A_{cm}=\frac{v_{oc}}{v_{ic}}
\]

En un amplificador diferencial ideal:

\[
A_{cm}=0
\]

Esto significa que una señal igual aplicada a las dos entradas no debería producir señal útil de modo común en la salida.

En un circuito real, \(A_{cm}\) no es exactamente cero. Su valor depende en gran medida de la resistencia de salida de la fuente de corriente de cola. Si dicha resistencia se representa como \(R_{SS}\), una aproximación habitual es:

\[
A_{cm}\approx -\frac{g_mR_D'}{1+2g_mR_{SS}}
\]

Si \(2g_mR_{SS}\gg 1\), entonces:

\[
A_{cm}\approx -\frac{R_D'}{2R_{SS}}
\]

Por tanto, cuanto mayor sea \(R_{SS}\), menor será la ganancia en modo común.

## 7. Relación de rechazo en modo común

La **relación de rechazo en modo común**, o **CMRR**, mide la capacidad del amplificador para amplificar señales diferenciales y rechazar señales comunes. Se define como:

\[
CMRR=\left|\frac{A_d}{A_{cm}}\right|
\]

En decibelios:

\[
CMRR_{dB}=20\log_{10}\left|\frac{A_d}{A_{cm}}\right|
\]

Un valor alto de \(CMRR\) indica que el circuito amplifica bien la diferencia entre entradas y rechaza eficazmente las señales comunes.

## 8. Impedancia de entrada

En un transistor MOS, la puerta está aislada eléctricamente, por lo que la corriente de entrada ideal es prácticamente nula:

\[
I_G\approx 0
\]

Por ello, la impedancia de entrada ideal es muy alta:

\[
R_{in}\approx \infty
\]

En la práctica, la impedancia de entrada queda limitada por las resistencias externas de polarización, las fugas y las capacidades parásitas. Si se utiliza una resistencia de polarización \(R_G\), entonces:

\[
R_{in}\approx R_G
\]

A frecuencias elevadas también deben considerarse las capacidades de entrada, especialmente \(C_{gs}\) y \(C_{gd}\).

## 9. Impedancia de salida

La impedancia de salida de una rama, mirando desde \(v_{o1}\) o \(v_{o2}\), es aproximadamente:

\[
R_{out,simple}\approx R_D \parallel r_o
\]

Si \(r_o\gg R_D\):

\[
R_{out,simple}\approx R_D
\]

Para una salida diferencial tomada entre \(v_{o1}\) y \(v_{o2}\), la impedancia equivalente es aproximadamente el doble:

\[
R_{out,dif}\approx 2(R_D \parallel r_o)
\]

---

## 10. Tensión de salida en reposo

La tensión de salida en reposo de cada rama se obtiene a partir de la caída de tensión en la resistencia de drenador:

\[
V_O=V_{DD}-I_DR_D
\]

En un par diferencial equilibrado:

\[
V_{O1}=V_{O2}=V_{DD}-\frac{I_T}{2}R_D
\]

Esta expresión permite elegir \(R_D\) o \(I_D\) para fijar el punto de trabajo de las salidas.

---

## 11. Rango de modo común de entrada

El rango de modo común indica el intervalo de valores de \(V_{CM}\) para los que el circuito sigue funcionando correctamente, manteniendo los transistores en saturación.

La tensión común de entrada se define como:

\[
V_{CM}=\frac{V_{G1}+V_{G2}}{2}
\]

Para el límite inferior, la fuente de corriente de cola debe mantenerse en saturación. Si \(V_{OV4}\) es la sobretensión del transistor de cola, debe cumplirse aproximadamente:

\[
V_S-V_{SS}\geq V_{OV4}
\]

Como:

\[
V_S=V_{CM}-V_{GS1}
\]

se obtiene aproximadamente:

\[
V_{CM,min}\approx V_{SS}+V_{OV4}+V_{GS1}
\]

Para el límite superior, los transistores de entrada deben permanecer en saturación:

\[
V_{DS1}\geq V_{OV1}
\]

Como \(V_{DS1}=V_D-V_S\), el límite superior se aproxima por:

\[
V_{CM,max}\approx V_D+V_{TH}
\]

donde:

\[
V_D=V_{DD}-I_DR_D
\]

---

## 12. Margen de salida

El margen de salida indica hasta dónde pueden variar las tensiones \(v_{o1}\) y \(v_{o2}\) sin que los transistores abandonen la región de saturación.

El límite superior de la salida se aproxima a \(V_{DD}\), cuando la corriente por la rama disminuye. El límite inferior viene dado por la condición de saturación del transistor de entrada:

\[
V_O \geq V_S+V_{OV}
\]

Por tanto, el margen útil de salida depende de \(V_{DD}\), \(V_{SS}\), la corriente de polarización, las resistencias de drenador y las sobretensiones de los transistores.

---

## 13. Resumen de parámetros habituales

| Parámetro | Expresión aproximada | Comentario |
|---|---:|---|
| Corriente de cola | \(I_T\) | Corriente fijada por el espejo |
| Corriente por rama | \(I_D=I_T/2\) | En reposo y con circuito simétrico |
| Sobretensión MOS | \(V_{OV}=V_{GS}-V_{TH}\) | También llamada tensión de overdrive |
| Transconductancia | \(g_m=2I_D/V_{OV}\) | Parámetro clave de ganancia |
| Transconductancia alternativa | \(g_m=\sqrt{2\beta I_D}\) | Modelo cuadrático |
| Resistencia de salida MOS | \(r_o=1/(\lambda I_D)\) | Por modulación de canal |
| Carga equivalente | \(R_D'=R_D\parallel r_o\) | Resistencia efectiva de salida |
| Ganancia salida simple | \(A_v\approx \pm g_mR_D'/2\) | Una salida respecto a masa |
| Ganancia diferencial | \(A_d\approx -g_mR_D'\) | Para \(v_{od}=v_{o1}-v_{o2}\) |
| Ganancia modo común | \(A_{cm}\approx -g_mR_D'/(1+2g_mR_{SS})\) | Depende de la fuente de cola |
| CMRR | \(CMRR=|A_d/A_{cm}|\) | Rechazo del modo común |
| CMRR en dB | \(CMRR_{dB}=20\log_{10}|A_d/A_{cm}|\) | Expresión logarítmica |
| Impedancia de entrada | \(R_{in}\approx \infty\) | Idealmente muy alta |
| Impedancia de salida simple | \(R_{out}\approx R_D\parallel r_o\) | Mirando una salida |
| Impedancia de salida diferencial | \(R_{out,dif}\approx 2(R_D\parallel r_o)\) | Entre ambas salidas |
| Salida en reposo | \(V_O=V_{DD}-I_DR_D\) | Punto de trabajo de salida |

---

## 14. Interpretación final

El amplificador diferencial NMOS convierte una diferencia de tensión entre dos entradas en dos señales de salida complementarias. La ganancia diferencial depende principalmente de la transconductancia \(g_m\) de los transistores de entrada y de la resistencia equivalente de carga \(R_D'\). La ganancia en modo común, en cambio, depende fuertemente de la calidad de la fuente de corriente de cola; cuanto mayor sea su resistencia de salida \(R_{SS}\), menor será \(A_{cm}\) y mayor será el \(CMRR\). Por ello, el espejo de corriente no solo fija el punto de trabajo, sino que también influye directamente en el rechazo de señales comunes.
