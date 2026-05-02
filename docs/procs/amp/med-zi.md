# Medida de la impedancia de entrada

## Fundamento del método

La impedancia de entrada puede determinarse mediante el **método del divisor resistivo**. La idea consiste en introducir una resistencia auxiliar \(R_{aux}\) en serie entre el generador y la entrada del amplificador, de modo que \(R_{aux}\) y \(Z_i\) formen un divisor de tensión.

En un montaje real, el generador de funciones no se comporta como una fuente ideal de tensión ideal, sino que tiene una impedancia interna  que se representa como \(R_g\). Esta impedancia también forma parte del divisor de tensión y debe tenerse en cuenta si su valor no es despreciable frente a \(R_{aux}\) o frente a la impedancia de entrada que se desea medir.

## Comprobación de la impedancia del generador

Antes de realizar la medida, se debe verificar el valor de la impedancia de salida del generador de funciones. Este dato debe consultarse en el manual de instrucciones del equipo. En muchos casos, también aparece serigrafiado junto al borne o conector desde el que se toma la señal de salida.

Los valores habituales son \(50\ \Omega\) y \(600\ \Omega\). Por este motivo, no debe asumirse un valor concreto sin comprobarlo previamente.

## Montaje de medida

<figure class="figura-lab01">
  <img src="../images/MedidaZin.jpg" alt="Medida de la impedancia de entrada de un amplificador" width=100%">
  <figcaption>Figura 1. Medida de la impedancia de entrada de un amplificador: 1) medida de la tensión del generador \(V_g\); 2) intercalación de \(R_{aux}\) y medida de la tensión de entrada \(V_i\)..</figcaption>
</figure>

El procedimiento requiere dos medidas principales.

1.  Se registra la tensión pico a pico del generador, sin conectar todavía la entrada del amplificador. Llamaremos a ese valor \(V_g\). Esta comprobación permite conocer la tensión realmente disponible en la salida del generador antes de conectar el circuito bajo prueba.

No debe confundirse el valor ajustado en el generador con el valor realmente medido en sus terminales. Para el cálculo se utilizará siempre el valor \(V_g\) medido con el osciloscopio.

2.  Se conecta la resistencia auxiliar \(R_{aux}\) entre el generador y la entrada del amplificador. Se mide entonces la tensión \(V_i\), también en pico a pico, presente a la entrada de la etapa.

## Cálculo de la impedancia de entrada

Una vez tomados los dos valores, si el conjunto se modela como un divisor resistivo, se cumple:

$$
V_i = V_g \cdot \frac{Z_i}{R_{aux} + R_g + Z_i}
$$

A partir de esta expresión puede despejarse la impedancia de entrada:

$$
Z_i = \frac{(R_{aux} + R_g)\,V_i}{V_g - V_i}
$$

Esta fórmula es la base del cálculo experimental. Su validez depende de que el amplificador se mantenga en el régimen de funcionamiento previsto, por lo que conviene comprobar también que la señal observada a la salida sigue siendo senoidal y no presenta distorsión.

Aunque se esté determinando \(Z_i\), el estado de la salida sigue siendo un buen indicador de que la etapa no ha sido excitada de forma excesiva y de que los componentes trabajan dentro de la zona para la que el modelo lineal es razonable.

## Elección de la resistencia auxiliar

Desde el punto de vista práctico, el método resulta más sensible cuando \(R_{aux}\) es del mismo orden de magnitud que la impedancia de entrada esperada. Si \(R_{aux}\) fuese muy pequeña frente a \(Z_i\), la caída de tensión en ella sería escasa y el cálculo sería poco preciso. Si fuese excesivamente grande, la tensión aplicada al amplificador disminuiría demasiado.

Por eso, es conveniente tomar un valor de \(R_{aux}\) del mismo orden de magnitud que \(Z_i\). Como criterio práctico, puede elegirse inicialmente:

$$
R_{aux} \approx Z_i
$$

## Consideración de la impedancia interna del generador

El valor de \(R_g\) puede despreciarse si es mucho menor que \(R_{aux}\) y que \(Z_i\). Sin embargo, es prudente considerarlo inicialmente y decidir después si su influencia es despreciable.

Por ejemplo, si \(R_g = 50\ \Omega\) y se utiliza una resistencia auxiliar de varios kiloohmios, la influencia de \(R_g\) puede ser pequeña. En cambio, si \(R_g = 600\ \Omega\) y \(R_{aux}\) tiene un valor comparable, despreciar \(R_g\) puede introducir un error apreciable.