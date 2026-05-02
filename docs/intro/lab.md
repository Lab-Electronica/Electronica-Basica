# El laboratorio de electrónica

## Introducción

El laboratorio de electrónica es el espacio donde se comprueba experimentalmente el comportamiento de los circuitos. En él se montan circuitos reales, se aplican señales, se realizan medidas y se comparan los resultados obtenidos con los valores teóricos y/o simulados.

El trabajo en el laboratorio no consiste únicamente en conectar componentes y leer valores en los instrumentos. También implica interpretar las medidas, detectar errores de montaje, comprobar si un circuito funciona dentro de la zona prevista y justificar las diferencias entre teoría, simulación y realidad.

Esto significa que, trabajando en el laboratorio, se van a desarrollar una serie de habilidades que difieren sustancialmente de las aprendidas en las clases teóricas. Al igual que las desarrolladas en las clases de teoría, es necesario un esfuerzo continuo y un trabajo progresivo.  Es fundamental desarrollar una disciplina y unos procedimientos para poder desempeñarse eficazmente en el laboratorio.

## Instrumentos básicos de laboratorio

En un laboratorio electrónica básica se utilizan varios instrumentos fundamentales. Existen diferentes modelos para cada uno de ellos, con diferentes funcionalidades y facilidades.  En esta documentación se considerarn las formas más básicas para incidir en la comprensión de los conceptos básicos y a algunas funcionalidades más avanzadas que son habituales en los equipos actuales.

### Fuente de alimentación

Todos los aparatos y equipos electrónicos necesitan energía para funcionar. Cuando se comercializan como productos finales, suelen alimentarse mediante pilas, baterías o adaptadores conectados a la red eléctrica.

En la mayoría de circuitos electrónicos se utilizan tensiones continuas porque los dispositivos internos, como transistores, circuitos integrados, sensores o microcontroladores, necesitan valores de tensión estables para polarizarse y trabajar correctamente.

En el laboratorio se prueban circuitos muy distintos, que pueden requerir diferentes tensiones de alimentación. Por eso se utiliza una **fuente de alimentación de laboratorio**, capaz de convertir la tensión de la red eléctrica en una tensión continua regulable, que puede ajustarse según las necesidades de cada montaje.

### Multímetro digital

El multímetro digital, también llamado **polímetro**, permite medir magnitudes eléctricas básicas como tensión, corriente y resistencia. Es uno de los instrumentos más utilizados en el laboratorio, especialmente para comprobar alimentaciones, continuidad, puntos de trabajo y valores de componentes.

### Generador de funciones

El generador de funciones permite aplicar señales eléctricas de prueba a un circuito. Estas señales pueden tener distintas formas, como senoidal, triangular o cuadrada, y se pueden ajustar en amplitud y frecuencia.

Cada forma de señal permite observar aspectos diferentes del comportamiento del circuito. La señal senoidal se utiliza porque es una señal básica y muy común para estudiar cómo responde un circuito a una frecuencia determinada. La señal cuadrada permite comprobar cómo reacciona el circuito ante cambios rápidos de nivel. La señal triangular resulta útil para observar respuestas progresivas y variaciones lineales de la tensión.

En el laboratorio, el generador de funciones se utiliza junto con el osciloscopio para aplicar una señal conocida al circuito y observar cómo se modifica a su paso por él.

### Osciloscopio

El osciloscopio permite visualizar señales eléctricas en función del tiempo. Es esencial para observar la forma de onda, medir amplitudes, periodos, frecuencias, desfases y comprobar si una señal está distorsionada o recortada.

Las versiones más básicas de los osciloscopios tienen la capacidad de visualizar al menos dos señales ya que es muy habitual comparar la entrada con la salida de un circuito y es necesario mostrar las dos a la vez.

## Elementos para el montaje de circuitos

Además de los instrumentos de medida, el laboratorio necesita elementos que permitan montar los circuitos de forma rápida y modificable.

### Placa de prototipos

La placa de prototipos, o *protoboard*, permite montar circuitos sin necesidad de soldar. Es especialmente útil en prácticas de aprendizaje, porque facilita probar circuitos, modificar conexiones y sustituir componentes.

Para utilizarla correctamente es necesario conocer cómo están conectadas internamente sus filas, columnas y líneas de alimentación.

### Cables de conexión

Los cables de conexión se utilizan para unir los distintos puntos del circuito en la placa de prototipos y para conectar el montaje con los instrumentos externos.

Es recomendable utilizar cables adecuados para protoboard, con longitud suficiente pero no excesiva, y mantener el montaje lo más ordenado posible para reducir errores de conexión.

### Componentes electrónicos

En las prácticas se utilizan componentes como resistencias, condensadores, diodos, transistores, circuitos integrados y sensores. Cada componente debe identificarse correctamente antes de montarlo, comprobando su valor, orientación y terminales cuando sea necesario.

## Material auxiliar

Además de los instrumentos principales, puede ser útil disponer de material auxiliar como:

- pinzas y alicates de punta fina;
- cortacables;
- cables con conectores tipo banana;
- sondas de osciloscopio;
- adaptadores BNC;
- resistencias y condensadores de distintos valores;
- hojas de características de componentes;
- ordenador con software de simulación;
- cuaderno o plantilla para anotar medidas.

Este material ayuda a realizar los montajes de forma más cómoda y a documentar correctamente los resultados obtenidos.

## Organización del puesto de trabajo

Un puesto de laboratorio debe organizarse de manera que el montaje sea claro y seguro. Antes de alimentar un circuito, conviene revisar que todos los instrumentos están correctamente conectados y que no existen cortocircuitos evidentes.

Una buena práctica consiste en seguir siempre este orden general:

1. Montar el circuito sin alimentación.
2. Revisar visualmente las conexiones.
3. Ajustar la fuente de alimentación antes de conectarla.
4. Alimentar el circuito.
5. Comprobar tensiones continuas básicas.
6. Aplicar señales de prueba si procede.
7. Medir y registrar los resultados.

Este orden ayuda a evitar daños en los componentes y facilita la localización de errores. Es una de las habilidades básicas, mencionadas anteriormente, que se deben adquirir.

## Registro de medidas

Toda práctica de laboratorio debe ir acompañada de un registro ordenado de las medidas realizadas. No basta con obtener un valor numérico; es necesario indicar qué se ha medido, en qué punto del circuito, con qué instrumento y bajo qué condiciones.

En general, conviene anotar:

- esquema o referencia del montaje;
- valores nominales de los componentes;
- condiciones de alimentación;
- señal aplicada;
- valores medidos;
- observaciones sobre la forma de onda;
- diferencias respecto a los valores teóricos o simulados.

El registro de medidas permite analizar posteriormente el funcionamiento del circuito y justificar los resultados.

## Errores frecuentes en el laboratorio

Algunos errores habituales al comenzar a trabajar en el laboratorio son:

- conectar la alimentación con polaridad incorrecta;
- no unir correctamente la masa común de los equipos;
- confundir filas y columnas de la placa de prototipos;
- medir corriente como si se midiera tensión;
- no comprobar la escala o modo del multímetro;
- usar una amplitud de señal demasiado grande;
- interpretar el valor indicado por un generador sin comprobarlo con el osciloscopio;
- olvidar la impedancia de entrada o salida de los instrumentos.

Reconocer estos errores ayuda a evitarlos y a desarrollar una forma de trabajo más segura y rigurosa.  Esta es otra de las habilidades a adquirir durante el trabajo de laboratorio.