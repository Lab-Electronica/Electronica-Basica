# Amplificadores

Un amplificador es un circuito electrónico diseñado para **aumentar el nivel de una señal eléctrica**. Según el tipo de circuito, la magnitud amplificada puede ser la **tensión**, la **corriente** o la **potencia**.

En electrónica analógica, los amplificadores se utilizan para adaptar señales procedentes de sensores, aumentar niveles de señal, excitar cargas, acondicionar medidas o formar parte de sistemas más complejos, como filtros activos, osciladores, fuentes de alimentación reguladas o sistemas de adquisición de datos.

Aunque existen muchos tipos de amplificadores, todos comparten una **idea básica**: 

!!! note "En los amplificadores una señal de entrada controla una señal de salida de mayor amplitud, utilizando para ello la energía suministrada por una fuente de alimentación externa"

## Modelo general de amplificador

El estudio de los amplificadores suele comenzar con un modelo general de entrada y salida. En este modelo se analiza el amplificador como un bloque caracterizado por una serie de parámetros básicos:

- ganancia de tensión;
- ganancia de corriente;
- ganancia de potencia;
- impedancia de entrada;
- impedancia de salida;
- respuesta en frecuencia;
- ancho de banda.

Este modelo permite estudiar el comportamiento externo del amplificador sin entrar inicialmente en los detalles internos del circuito.

## Tipos de amplificadores

Existen varias familias de amplificadores especialmente importantes en electrónica básica y analógica.

### Amplificadores básicos

En esta sección llamaremos amplificadores básicos a aquellos circuitos en los que una señal de entrada, tomada respecto a una referencia común, controla una señal amplificada en la salida. 

El análisis se centra en su comportamiento externo, es decir, en la relación entre las señales de entrada y salida. Para ello se emplean parámetros fundamentales como la ganancia, la impedancia de entrada, la impedancia de salida y la respuesta en frecuencia.

### Amplificadores diferenciales

Un amplificador diferencial es un circuito cuya salida depende principalmente de la diferencia entre dos señales de entrada.

### Amplificadores operacionales

El amplificador operacional es un bloque amplificador de alta ganancia que se utiliza habitualmente con realimentación externa.

Aunque internamente puede estar formado por varias etapas, incluyendo una etapa diferencial de entrada, en muchas aplicaciones se estudia como un componente funcional con su propio símbolo eléctrico.

### Amplificadores de potencia

Los amplificadores de potencia están diseñados para entregar energía a una carga, siendo la carga el dispositivo conectado a la salida, como un altavoz, un motor o una resistencia. En ellos no solo interesa la ganancia de tensión, sino también la potencia transferida, el rendimiento y la capacidad de excitar cargas de baja impedancia.

Son especialmente importantes en aplicaciones como audio, etapas de salida, control de actuadores y sistemas donde la señal debe entregar una cantidad significativa de energía.

## Conceptos comunes

Algunos conceptos aparecen en muchos tipos de amplificadores y se estudiarán de forma común para evitar repeticiones.

Entre ellos se encuentran:

- el uso de condensadores de acoplo y desacoplo;
- la respuesta en frecuencia;
- las frecuencias de corte;
- el criterio de caída de ganancia de -3 dB;
- el ancho de banda.

Estos conceptos permiten comprender por qué la respuesta de un amplificador no es constante para todas las frecuencias.
