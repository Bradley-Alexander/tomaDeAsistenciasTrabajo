---
title: "04-capitulo"
format: html
---

---
#"Conversión de Autómatas Finitos a Expresiones Regulares"
---

## Introducción

Existen varios métodos para obtener una expresión regular (ER) equivalente a partir de un Autómata Finito (AF), ya sea Determinista (DFA) o No Determinista (NFA). Esto demuestra que los autómatas finitos y las expresiones regulares son equivalentes en poder expresivo: ambos describen exactamente la clase de lenguajes regulares.

Dos de los métodos más comunes son:

1.  **Método de Eliminación de Estados (State Elimination)**
2.  **Uso del Lema de Arden (Método Algebraico)**

---

## 1. Método de Eliminación de Estados

Este método consiste en eliminar iterativamente los estados de un autómata, excepto el inicial y el final, mientras se actualizan las transiciones restantes con expresiones regulares que representan los caminos perdidos.

### Pasos Preliminares (Preparación del Autómata)

Antes de comenzar la eliminación, el autómata debe ser modificado para cumplir con dos condiciones:

1.  **Un único estado inicial:**
    * Crear un **nuevo estado inicial** ($q_i$) sin transiciones entrantes.
    * Añadir una transición-ε (o λ) desde este nuevo estado al estado inicial original del autómata.

2.  **Un único estado final (de aceptación):**
    * Crear un **nuevo estado final** ($q_f$) sin transiciones salientes.
    * Añadir transiciones-ε desde todos los estados finales originales al nuevo estado final.
    * Los estados finales originales dejan de ser finales.

> **Nota:** Si el autómata ya tiene un solo estado inicial sin transiciones entrantes y/o un solo estado final sin transiciones salientes, esos pasos respectivos pueden omitirse. El autómata sobre el que se trabaja se considera un "Autómata Finito Generalizado" (AFG), donde las etiquetas de las transiciones son expresiones regulares, no solo símbolos.

### Proceso de Eliminación

El núcleo del método es eliminar uno por uno todos los estados intermedios (cualquier estado que no sea el $q_i$ ni el $q_f$ nuevos).

Al eliminar un estado $q_k$ (el "estado pivote"), debemos compensar todos los caminos que pasaban a través de él. Para cada par de estados $q_i$ (origen) y $q_j$ (destino), donde había una transición de $q_i$ a $q_k$ y de $q_k$ a $q_j$, actualizamos la transición directa de $q_i$ a $q_j$.

**La Fórmula de Actualización:**

Supongamos que queremos eliminar el estado $q_k$. Para cualquier par de estados $q_i$ y $q_j$ (distintos de $q_k$), la nueva expresión regular $R'(i, j)$ que va de $q_i$ a $q_j$ se calcula así:

$$
R'(i, j) = R(i, j) \quad | \quad ( R(i, k) \cdot (R(k, k))^* \cdot R(k, j) )
$$

* **$R(i, j)$:** La ER de la transición directa actual de $q_i$ a $q_j$. (Si no hay, es $\emptyset$).
* **$R(i, k)$:** La ER de $q_i$ a $q_k$.
* **$R(k, k)$:** La ER del bucle en $q_k$.
* **$R(k, j)$:** La ER de $q_k$ a $q_j$.
* **$| (o +)$:** Representa la unión (alternativa).
* **$\cdot$:** Representa la concatenación.
* **$^*$:** Representa la clausura de Kleene (cero o más repeticiones).



Este proceso se repite hasta que los únicos estados restantes sean el nuevo estado inicial $q_i$ y el nuevo estado final $q_f$. La expresión regular en la única transición que queda de $q_i$ a $q_f$ es la expresión regular equivalente a todo el autómata.

---

## 2. Lema de Arden (Método Algebraico)

Este método trata el autómata como un sistema de ecuaciones lineales, donde las "variables" son los lenguajes aceptados a partir de cada estado, y las "constantes" son los símbolos del alfabeto.

### El Lema de Arden

El lema establece que si tenemos una ecuación de la forma:

$$
X = (P \cdot X) \quad | \quad Q
$$

Donde $P$ y $Q$ son expresiones regulares (o lenguajes) y la expresión regular $P$ **no** contiene la cadena vacía (ε), entonces esta ecuación tiene una única solución para $X$:

$$
X = Q \cdot P^*
$$

Si $P$ puede contener ε, la solución es $X = P^* \cdot Q$. En la práctica, la forma $X = Q \cdot P^*$ es la más utilizada. A veces se ve la ecuación como $X = X \cdot P \quad | \quad Q$, cuya solución es $X = Q \cdot P^*$.

### Pasos del Método

1.  **Asignar variables:** A cada estado $q_i$ del autómata se le asigna una variable $X_i$, que representa la expresión regular del lenguaje aceptado *comenzando desde* ese estado $q_i$.

2.  **Construir el sistema de ecuaciones:** Se crea una ecuación para cada estado $X_i$ (para $i = 0...n$).
    * La ecuación para $X_i$ es la **unión (suma)** de todas las transiciones que *salen* de $q_i$.
    * Si una transición con el símbolo $a$ va de $q_i$ a $q_j$, se añade el término $a \cdot X_j$ a la ecuación de $X_i$.
    * Si $q_i$ es un estado final, se añade **ε** a su ecuación (porque acepta la cadena vacía *desde ese punto*).

    **Ejemplo de Ecuación:**
    Si el estado $q_1$ tiene un bucle con 'a' y una transición con 'b' a $q_2$, y $q_1$ no es final:
    $X_1 = (a \cdot X_1) \quad | \quad (b \cdot X_2)$

    Si $q_1$ fuera también final:
    $X_1 = (a \cdot X_1) \quad | \quad (b \cdot X_2) \quad | \quad \epsilon$

3.  **Resolver el sistema:**
    * El objetivo es encontrar el valor de $X_0$ (la variable del estado inicial).
    * Se utiliza sustitución algebraica (como en un sistema de ecuaciones normal) y el Lema de Arden para despejar las variables.
    * Se empieza resolviendo las ecuaciones para los estados "más lejanos" (a menudo los finales) y se sustituye hacia atrás hasta llegar a $X_0$.
    * Cada vez que se llega a una forma $X_i = (P \cdot X_i) \quad | \quad Q$, se aplica el lema para obtener $X_i = Q \cdot P^*$.

4.  **Resultado:** La expresión regular final es la solución obtenida para la variable $X_0$ (o la variable del estado inicial).
