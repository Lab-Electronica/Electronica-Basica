# Práctica 5: Análisis del Amplificador MOSFET ALD1105

Este documento contiene la transcripción completa y detallada de los apuntes de la **Práctica 5**, enfocada en el análisis en corriente continua (DC) y en pequeña señal de un amplificador basado en el MOSFET ALD1105. Las fórmulas están en formato MathJax/LaTeX y los esquemas están guardados en archivos SVG independientes para su descarga.

---

## 1. Especificaciones y Parámetros del Circuito

### Esquema del Circuito en Corriente Continua (DC)
El circuito consta de un espejo de corriente en la parte superior formado por transistores PMOS ($M_2, M_3$) que fijan la corriente de referencia $I_{REF}$ a través de una resistencia de polarización $R_B$. El transistor de amplificación es un NMOS ($M_1$) configurado con una resistencia de realimentación $R_F$ entre drenador y puerta. Las capacidades $C_1$ y $C_2$ sirven como condensadores de acoplo para la entrada $V_i$ y la salida $V_o$ respectivamente.

![Circuito DC](circuito_dc.svg)

### Parámetros de los Transistores (MOSFET ALD1105)
* **Resistencia de Realimentación:** $R_F = 1 \text{ M}\Omega$
* **Transistores NMOS:**
    * $\beta_n = 560 \ \mu\text{A/V}^2$
    * $V_{THn} = 0.6 \text{ V}$
    * $\lambda_n = 0.02 \text{ V}^{-1}$
* **Transistores PMOS:**
    * $\beta_p = 210 \ \mu\text{A/V}^2$
    * $V_{THp} = -0.72 \text{ V} \implies |V_{THp}| = 0.72 \text{ V}$
    * $\lambda_p = 0.04 \text{ V}^{-1}$

---

## 2. Análisis del Punto de Trabajo (Estático / DC)

### Análisis en el Transistor $M_3$ (PMOS del Espejo)
Por la configuración de circuito conectado en modo diodo para $M_3$, se cumple la siguiente relación para las tensiones de los terminales:

$$\begin{aligned}
V_{GS3} &= V_{D3} - V_{CC} = V_{DS3} \implies \\
V_{SG3} &= V_{CC} - V_{D3} = V_{SD3} \quad \text{(ec. 1)}
\end{aligned}$$

La corriente de referencia $I_{REF}$ que circula por la rama izquierda del espejo (y a través de $M_3$ en la zona de saturación) viene dada por:

$$I_{REF} = I_{D3} = \frac{\beta_p}{2} \cdot \left(V_{SG3} - |V_{THp}|\right)^2 \cdot \left(1 + \lambda_p \cdot V_{SD3}\right)$$

Asumiendo una primera aproximación con el efecto de modulación de longitud de canal despreciable ($\lambda_p = 0$), simplificamos la expresión:

$$I_{REF} = \frac{\beta_p}{2} \cdot \left(V_{SG3} - |V_{THp}|\right)^2$$

A partir de esta ecuación, podemos aislar el término de tensión puerta-fuente:

$$\frac{2 \cdot I_{REF}}{\beta_p} = \left(V_{SG3} - |V_{THp}|\right)^2$$

Extrayendo la raíz cuadrada en ambos miembros:

$$\pm\sqrt{\frac{2 \cdot I_{REF}}{\beta_p}} = V_{SG3} - |V_{THp}|$$

Sustituyendo la relación de la **ecuación 1** ($V_{SG3} = V_{CC} - V_{D3}$):

$$\pm\sqrt{\frac{2 \cdot I_{REF}}{\beta_p}} = V_{CC} - V_{D3} - |V_{THp}|$$

Despejando finalmente el valor de la tensión de drenador $V_{D3}$:

$$\boxed{V_{D3} = V_{CC} - |V_{THp}| - \sqrt{\frac{2 \cdot I_{REF}}{\beta_p}}}$$

> **Nota de diseño:** Se exige el signo positivo de la raíz para garantizar la condición de conducción del canal, es decir, que $V_{SG3} > |V_{THp}|$, lo cual define el sobrevoltaje o tensión de overdrive como:
> $$V_{OV3} = V_{SG3} - |V_{THp}|$$

Una vez hallado $V_{D3}$, la resistencia de polarización de la rama del espejo $R_B$ se calcula de forma directa aplicando la ley de Ohm:

$$\boxed{R_B = \frac{V_{D3}}{I_{REF}}}$$

---

### Análisis en el Transistor $M_1$ (NMOS Amplificador)
Analizamos ahora el comportamiento estático de la etapa de amplificación inferior:

1. Debido a que la corriente de puerta en un MOSFET ideal es nula ($I_G \approx 0$), no circula corriente a través de la resistencia de realimentación $R_F$. Por lo tanto, la tensión de puerta y de drenador son idénticas:
   $$V_{G1} = V_{D1}$$
2. Como el terminal de fuente ($S_1$) de $M_1$ está conectado directamente a la masa del circuito (tierra):
   $$\boxed{V_{GS1} = V_{G1} = V_{D1} \quad \text{y} \quad V_{DS1} = V_{D1} \quad \text{(ec. 2)}}$$

La corriente de drenador $I_{D1}$ para el transistor $M_1$ en zona de saturación se define como:

$$I_{D1} = \frac{\beta_n}{2} \cdot \left(V_{DS1} - V_{THn}\right)^2 \cdot \left(1 + \lambda_n \cdot V_{DS1}\right) = \frac{\beta_n}{2} \cdot \left(V_{D1} - V_{THn}\right)^2 \cdot \left(1 + \lambda_n \cdot V_{D1}\right)$$

Si aplicamos nuevamente la aproximación despreciando el efecto Early ($\lambda_n = 0$), obtenemos:

$$I_{D1} = \frac{\beta_n}{2} \cdot \left(V_{DS1} - V_{THn}\right)^2$$

Dado que no se desvía corriente por la resistencia $R_F$ ($I_{RF} = 0$), toda la corriente suministrada por el espejo a través de $M_2$ fluye hacia el drenador de $M_1$. Por simetría y características del espejo ideal, establecemos que:

$$I_{D1} = I_{D2} = I_{REF}$$

Sustituyendo esta igualdad en la ecuación simplificada de $M_1$:

$$I_{REF} = \frac{\beta_n}{2} \cdot \left(V_{DS1} - V_{THn}\right)^2$$

Despejando el término cuadrático:

$$\frac{2 \cdot I_{REF}}{\beta_n} = \left(V_{DS1} - V_{THn}\right)^2$$

Aplicando la raíz cuadrada y sustituyendo los términos según la **ecuación 2**:

$$\pm\sqrt{\frac{2 \cdot I_{REF}}{\beta_n}} = V_{D1} - V_{THn}$$

Despejando la tensión de polarización del nodo $V_{D1}$:

$$\boxed{V_{D1} = V_{GS1} = V_{DS1} = V_{THn} + \sqrt{\frac{2 \cdot I_{REF}}{\beta_n}}}$$

> **Nota:** Seleccionamos el signo positivo de la raíz para asegurar que el transistor $M_1$ se encuentre encendido y no entre en la zona de corte ($V_{GS1} > V_{THn}$).

---

### Resumen de Ecuaciones del Punto de Trabajo ($Q$)

A continuación se recopilan las tensiones y corrientes constitutivas que definen el punto de operación en reposo (DC) del circuito:

$$\begin{aligned}
V_{GS1} &= V_{D1} \\
V_{DS1} &= V_{D1} \\
V_{GS2} &= V_{D3} - V_{CC} \\
V_{DS2} &= V_{D1} - V_{CC} \\
V_{GS3} &= V_{D3} - V_{CC} \\
V_{DS3} &= V_{D3} - V_{CC} \\
I_{D1}  &= \frac{\beta_n}{2} \cdot \left(V_{D1} - V_{THn}\right)^2 \\
R_B     &= \frac{V_{D3}}{I_{REF}}
\end{aligned}$$

![Curvas Características](curvas_caracteristicas.svg)

---

## 3. Modelo de Pequeña Señal (AC)

Para el análisis dinámico en alterna, se linealizan las ecuaciones completas del MOSFET alrededor del punto de trabajo estático $Q$:

$$i_d = g_m \cdot v_{gs} + \frac{v_{ds}}{r_o}$$

Donde los parámetros de pequeña señal se definen mediante las siguientes derivadas parciales evaluadas en el punto $Q$:

$$g_m = \left. \frac{\partial I_D}{\partial V_{GS}} \right|_Q \quad ; \quad \frac{1}{r_o} = \left. \frac{\partial I_D}{\partial V_{DS}} \right|_Q$$

### Cálculo de Parámetros Dinámicos

#### Transconductancia ($g_m$):
$$g_{m1} = \beta_n \cdot \left(V_{GS1Q} - V_{THn}\right) \cdot \left(1 + \lambda_n \cdot V_{DS1Q}ight) \simeq \beta_n \cdot \left(V_{GS1Q} - V_{THn}ight)}$$

#### Resistencia de Salida Dinámica ($r_o$):
$$\boxed{r_{o1} = \frac{1}{\lambda_n \cdot I_{D1Q}}} \quad \text{y} \quad \boxed{r_{o2} = \frac{1}{\lambda_p \cdot I_{D2Q}}}$$

---

### Esquema del Circuito Completo en Pequeña Señal

Sustituyendo los modelos correspondientes de pequeña señal en la topología global de la etapa (con las fuentes de continua pasivadas y los condensadores actuando como cortocircuitos ideales en la banda de paso):

![Circuito Pequeña Señal](circuito_pequena_senal.svg)

A partir de este esquema equivalente, deducimos las siguientes igualdades de tensiones de nodo:

$$v_g = v_i = v_{gs1} \quad ; \quad v_{ds1} = v_{d1} = v_{d2} = v_o$$

---

## 4. Cálculo de las Magnitudes de Pequeña Señal

### 4.1 Ganancia de Tensión ($A_v$)
Aplicamos la **Ley de Corrientes de Kirchhoff (KCL)** en el nodo de salida ($V_o$):

$$\frac{v_o}{r_{o1}} + \frac{v_o}{r_{o2}} + \frac{v_o - v_i}{R_F} + g_{m1} \cdot v_i = 0$$

$$\boxed{A_v = \frac{v_o}{v_i} = - \frac{g_{m1} - \frac{1}{R_F}}{\frac{1}{r_{o1}} + \frac{1}{r_{o2}} + \frac{1}{R_F}}}$$

---

### 4.2 Impedancia de Salida ($Z_o$)
Anulamos la fuente de tensión de entrada ($v_i = 0$), lo que implica que $v_{gs1} = 0 \implies g_{m1}v_{gs1} = 0$:

$$\boxed{Z_o = \left(\frac{1}{r_{o1}} + \frac{1}{r_{o2}} + \frac{1}{R_F}\right)^{-1} = r_{o1} \parallel r_{o2} \parallel R_F}$$

---

### 4.3 Impedancia de Entrada ($Z_i$)
Aplicando el efecto Miller a través de la resistencia de realimentación $R_F$:

$$\boxed{Z_i = \frac{R_F}{1 - A_v}}$$

Como $A_v < 0$, entonces $1 - A_v > 1$, lo que provoca que $\boxed{Z_i < R_F}$.
