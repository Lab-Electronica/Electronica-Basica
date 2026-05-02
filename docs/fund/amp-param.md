# Amplificadores: Parámetros básicos

## Modelo básico de amplificador

El interior de un amplificador se puede **modelar eléctricamente** de una forma muy simplificada que refleja cómo un circuito externo "percibe" la entrada o la salida. 
En la figura siguiente se muestra ese modelo, en su versión más simplificada, como los elementos eléctricos equivalentes que describen su comportamiento.
La tensión v<sub>i</sub> representa la tensión aplicada a los terminales de entrada del amplificador y la tensión v<sub>o</sub> es la tensión que el amplificador entrega en sus terminales de salida.  
<figure class="figura-lab01">
  <img src="../images/Modelo.jpg" alt="Modelo básico de amplificador" width=100%">
  <figcaption>Figura 1. Modelo básico de amplificador.</figcaption>
</figure>

## Impedancia de entrada Z<sub>i</sub>

La **entrada** del bloque se puede modelar simplemente como una **impedancia Z<sub>i</sub>** que indica cómo “carga” el amplificador a la etapa o instrumento que le entrega la señal. 
Cuanto mayor sea Z<sub>i</sub>, menor corriente tomará el amplificador desde la fuente que lo excita y menor perturbación introducirá sobre ella. En una situación real, una impedancia de entrada alta suele ser deseable porque facilita que la señal aplicada al circuito sea próxima a la que el generador pretendía entregar.

## Ganancia e impedancia de salida Z<sub>o</sub>

La **salida** del bloque se puede modelar con una **fuente de tensión controlada A<sub>v</sub> v<sub>i</sub>**.  Esto representa la tensión equivalente que genera internamiento el amplificador, proporcional a la tensión de entrada V<sub>i</sub>.
El nombre del factor A<sub>v</sub> representa la **ganancia de tensión** del amplificador, es decir el factor por el que se multiplica la tensión de entrada en el modelo ideal.  La letra **A** se usa por el concepto de "Amplificación", y  el subiíndice **v** indica que se trata de una ganancia de tensión (en realidad es el comienzo de la parabra voltaje).
La fuente de tensión controlada se complementa con una impedancia de salida Z<sub>o</sub>, que indica cómo se comporta la salida del amplificador cuando se conecta una carga. Cuanto menor sea Z<sub>o</sub>, más fácil será mantener la tensión de salida al conectar distintos receptores o cargas. En términos prácticos, una impedancia de salida baja permite que el amplificador entregue señal sin que esta caiga excesivamente al alimentar el siguiente bloque.

## Obtención de los parámetros eléctricos del modelo

Para calcular los parámetros eléctricos del modelo de un amplificador real, se analiza el circuito desde sus terminales externos. En la **entrada**, se obtiene la **impedancia equivalente de entrada** Z<sub>i</sub>, es decir, la impedancia vista por la fuente de señal al mirar hacia el amplificador. En la **salida**, se sustituye el circuito por su **equivalente de Thévenin**, formado por una tensión equivalente de salida en vacío A<sub>v</sub> v<sub>i</sub> y una impedancia equivalente vista desde los terminales de salida, que se identifica con la **impedancia de salida** Z<sub>o</sub>. De esta forma, el amplificador queda representado externamente mediante su impedancia de entrada, su ganancia y su impedancia de salida, tal como se puede observar en la figura siguiente.

<figure class="figura-lab01">
  <img src="../images/Cuadripolo.jpg" alt="Modelo cuadripolo de amplificador" width=100%">
  <figcaption>Figura 2. Modelo de cuadripolo con los tres parámetros básicos.</figcaption>
</figure>

## Limitaciones del modelo básico

Este modelo es muy útil, pero hay que entenderlo como una idealización válida dentro de ciertos límites. Los componentes reales que forman el interior de la etapa amplificadora hacen que el comportamiento no sea exactamente constante en cualquier circunstancia.
Por ejemplo, la ganancia puede variar si la frecuencia cambia mucho, si la señal aplicada es demasiado grande o si la carga conectada a la salida no es la prevista.  En cursos más avanzados se estudian con detalle otros parámetros relevantes, como la respuesta con la frecuencia, el rango dinámico, la distorsión, el ruido o la estabilidad.
