---
title: "Minimización y Reducción de Autómatas"
format: html
editor: visual
---

## 2.2 Minimizando DFAs (Haciendo el autómata más pequeño)

[cite_start]El objetivo principal de esta sección es tomar un Autómata Finito Determinista (DFA) y convertirlo en su versión "única y mínima"[cite: 4]. Es decir, buscamos la versión más simple posible de la máquina que siga haciendo exactamente el mismo trabajo (reconocer el mismo lenguaje).

[cite_start]Para lograr esto, utilizamos un algoritmo que funciona en dos pasos fundamentales[cite: 5, 6]:

1.  **Agrupar (Partición):** Primero, organizamos los estados del autómata en grupos (llamados bloques). [cite_start]La idea es poner en el mismo grupo a los estados que se comportan igual[cite: 5]. [cite_start]A esta organización la llamamos "partición del lenguaje"[cite: 6].
2.  **Fusionar (Cociente):** Una vez que tenemos los grupos listos, fusionamos todos los estados de un mismo grupo para convertirlos en un único "superestado". [cite_start]Esto crea un nuevo autómata donde no hay estados repetidos o redundantes[cite: 6, 7].

A continuación, explicamos cómo se hace la primera parte, que es la más importante.

### 2.2.1 Calculando la Partición del Lenguaje (Creando los grupos)

Para entender cómo agrupar los estados, necesitamos entender qué es una **partición**. [cite_start]Imagina que tienes una caja con todos los estados; una partición es simplemente dividir esos estados en bolsas separadas (bloques) sin que sobre ninguno y sin que un estado esté en dos bolsas a la vez[cite: 11].

[cite_start]El objetivo es separar los estados poco a poco hasta que solo queden juntos aquellos que sean verdaderamente equivalentes[cite: 13, 14].

#### Paso 1: La división inicial (Ganadores vs. Perdedores)
Al principio, hacemos la división más obvia. [cite_start]Separamos los estados en dos grandes grupos[cite: 16]:
* **Grupo 1:** Los estados de aceptación (finales).
* **Grupo 2:** Los estados que no son de aceptación (no finales).

[cite_start]Esto se hace porque un estado que dice "sí acepto la palabra" nunca puede ser igual a uno que dice "no la acepto"[cite: 18]. [cite_start]Si todos los estados fueran finales o todos no finales, tendríamos un solo grupo[cite: 17].

#### Paso 2: Refinar los grupos (La prueba de la separación)
Ahora debemos revisar si los estados que pusimos en el mismo grupo realmente merecen estar juntos. Para ello, los "probamos" con las letras del alfabeto del autómata.

La regla de oro es la siguiente:
[cite_start]Si dos estados ($q_1$ y $q_2$) están en el mismo grupo, pero al recibir una letra (por ejemplo, 'a') se van a grupos diferentes, **entonces no son iguales y deben separarse**[cite: 22].

* **¿Cómo se divide?** Si tenemos un grupo $B$ y lanzamos una letra 'a':
    * Unos estados se van al grupo $B'$ (destino 1).
    * Otros estados se van a un sitio diferente (destino 2).
    * [cite_start]Entonces, el grupo original $B$ se rompe (se divide) en dos nuevos grupos más pequeños[cite: 24, 25, 26].

[cite_start]A esto le llamamos que la partición es "inestable" mientras podamos seguir encontrando diferencias y separando grupos[cite: 27].

#### El Algoritmo (LanPar)
[cite_start]El proceso automático (Algoritmo 4) funciona así[cite: 30, 33]:

1.  [cite_start]Comienza con la división inicial (Finales vs. No Finales)[cite: 38].
2.  [cite_start]Repite el siguiente ciclo mientras sea posible dividir algún grupo[cite: 43]:
    * [cite_start]Busca un grupo y una letra que demuestren que los estados de ese grupo no se comportan igual[cite: 41].
    * [cite_start]Divide ese grupo en dos[cite: 44].
3.  [cite_start]Cuando ya no se pueda dividir más (la partición es estable), el algoritmo termina[cite: 30].

El resultado final es la agrupación perfecta donde los estados en cada grupo son equivalentes. [cite_start]Esto garantiza que hemos encontrado la estructura más simple posible para ese autómata[cite: 53, 87].

> **Ejemplo visual:** Imagina pintar los estados de colores. Al principio pintas los finales de un color y el resto de otro. Luego, si un estado azul va a uno rojo con la letra 'a', pero otro estado azul se queda en azul con la misma letra 'a', significa que esos dos azules son diferentes. Entonces, le cambias el color a uno de ellos. [cite_start]Repites esto hasta que los colores no cambien[cite: 48, 49, 51].
