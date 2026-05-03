# Condensadores de acoplo y desacoplo

## Introducción

En muchos circuitos electrónicos se utilizan condensadores para controlar qué parte de una señal pasa de una zona del circuito a otra. En particular, un condensador permite **bloquear la componente continua y dejar pasar, dentro de ciertos límites, la componente alterna de una señal**.

## Comportamiento básico del condensador

En corriente continua, una vez cargado, un condensador se comporta como un circuito abierto. Por eso impide el paso permanente de corriente continua entre dos puntos del circuito.

En corriente alterna, en cambio, el condensador presenta una impedancia que depende de la frecuencia y de su capacidad:

$$
|Z_C| = \frac{1}{2 \pi f C}
$$

De esta expresión se deduce que la impedancia del condensador disminuye cuando aumenta la frecuencia o cuando aumenta la capacidad. Por tanto, un condensador suficientemente grande puede dejar pasar la señal alterna con poca atenuación, mientras bloquea la componente continua.

## Condensador de acoplo entre etapas

Una de las aplicaciones más habituales es el **acoplo entre etapas**. Al realizar el diseño de un equipo electrónico la funcionalidad se divide en módulos o etapas más sencillas, recibiendo cada una de ellas una señal a su entrada y sirviéndola procesada a su salida.

Para realizar su función, cada etapa puede estar compuesta por diferentes componentes que requerirán su propia polarización para que cada componente esté en su punto de trabajo adecuado.

Si estas etapas se conectasen directamente, la polarización de una etapa podría modificar la polarización de la otra. Para evitarlo, se coloca un condensador de acoplo entre ambas.

De esta forma, la señal variable que se desea transmitir puede pasar de una etapa a la siguiente, mientras que las tensiones continuas de polarización quedan separadas. En electrónica básica se suele hablar de “señal alterna” para referirse a la parte de la señal que cambia con el tiempo. 

Una señal real puede tener una forma compleja, pero puede estudiarse como una combinación de componentes de distintas frecuencias.  Para la funcionalidad requerida se debe tomar **el caso más desfavorable que sería el de la frecuencia más baja**.

## Elección del valor del condensador

El valor del condensador debe elegirse teniendo en cuenta además de la frecuencia mínima de trabajo,  la impedancia con la que se conecta.  

Como criterio práctico inicial, interesa que la impedancia del condensador sea pequeña frente a la resistencia o impedancia relevante del circuito a la frecuencia de trabajo, por ejemplo, la impedancia de entrada de la etapa para el condensador a la entrada o la impedancia de salida para el condensador a la salida.

Una regla sencilla en un primer análisis es escoger el condensador de forma que:

$$
|Z_C| \leq \frac{R}{10}
$$

donde \(R\) representa la resistencia o impedancia relevante asociada al condensador.

Esta regla no es exacta para todos los diseños, pero permite estimar si el condensador tendrá una influencia pequeña sobre la señal alterna en la zona de trabajo prevista.

Dado que la impedancia del condensador disminuye cuando aumenta su capacidad, quizás puede pensarse que se puede resolver de forma definitiva escogiendo el condensador de la mayor capacidad disponible.  Sin embargo, se debe tener en cuenta que cuanto mayor es la capacidad mayor es el tamaño del condencsador.

