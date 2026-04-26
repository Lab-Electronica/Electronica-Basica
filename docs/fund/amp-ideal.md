# Amplificadores: modelo básico
## Concepto

Un amplificador puede entenderse, en una primera aproximación, como un bloque con una entrada y una salida.  A la entrada se aplica una señal eléctrica de pequeña amplitud, y a la salida se obtiene otra señal relacionada con la de entrada, pero normalmente de mayor amplitud. 
Desde este punto de vista, resulta útil representar el amplificador como un bloque con dos terminales de entrada, dos terminales de salida y una relación entre la señal aplicada y la señal obtenida tal y como se muestra en la siguiente figura.
<figure markdown="span">
  <img src="../images/CuadripoloSimple.jpg" alt="Modelo cuadripolo de amplificador" width=100%">
  <figcaption>Figura 1. Modelo de amplificador como cuadripolo.</figcaption>
</figure>
El modelo representa un "cuadripolo" porque tiene cuatro polos o terminales.

## Ganancia de un amplificador

El parámetro más inmediato para describir su funcionamiento es la ganancia.  De forma intuitiva, la ganancia indica cuánto “crece” la señal al atravesar la etapa amplificadora. En estos apartados trabajaremos, en particular, con la ganancia de tensión, ya que es la magnitud más sencilla de observar en el laboratorio con un generador de funciones y un osciloscopio. Por ello, a la entrada representamos la señal como v<sub>i</sub> y a la salida como v<sub>o</sub>. 

## Conversión de energía en amplificación

Conviene, no obstante, hacer una precisión conceptual importante. Un amplificador no “crea” energía a partir de la señal de entrada.  La energía que permite obtener una señal de salida mayor procede de la alimentación del circuito, por eso es imprescindible que los componentes que forman el amplificador estén adecuadamente polarizados y se compruebe que su punto de trabajo es el correcto. 
En esta situación, la señal de entrada actúa, por así decirlo, como una señal de control que gobierna cómo la etapa utiliza la energía suministrada por la fuente de alimentación.  Esta idea ayuda a entender por qué,  mediante los dispositivos adecuados, se puede tomar una señal pequeña y entregar una señal de mayor amplitud a la salida.

## Implementación de un amplificador

Un amplificador se puede implementar con diversas tecnologías y de una manera más o menos compleja. No obstante, se le puede estudiar como una "caja negra", es decir, sin importar lo que hay en su interior. Este enfoque funcional, permite hace una labor de diseño a un nivel superior, sin preocuparse todavía de los detalles y luego, en base a las necesidades concretas, hacer la selección de la tecnología y la concreción de los dispositivos a utilizar.
