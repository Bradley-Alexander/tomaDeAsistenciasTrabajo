---
title: "Definición de Ambigüedad en Gramáticas Independientes del Contexto"
author: "Bradley Poma Vera"
date: "2025-12-27"
lang: es
format:
  html:
    theme: flatly
    toc: true
    toc-title: "Índice"
    number-sections: true
    code-fold: true
    self-contained: true
editor: visual
---

## 1. Introducción

En la teoría de lenguajes formales, una **Gramática Independiente del Contexto (GIC)** describe la estructura sintáctica de un lenguaje. 
Sin embargo, ciertas gramáticas presentan un defecto estructural conocido como **ambigüedad**, el cual complica el proceso de análisis sintáctico (*parsing*) en la construcción de compiladores.

Este informe define formalmente la ambigüedad y presenta ejemplos prácticos visualizados mediante árboles de derivación.

## 2. Definición Formal

Sea $G = (V, \Sigma, R, S)$ una gramática independiente del contexto.

Una gramática $G$ se denomina **ambigua** si existe alguna cadena $w$ perteneciente al lenguaje $L(G)$ para la cual se cumple **al menos una** de las siguientes condiciones:

1.  Existen dos o más **árboles de derivación** (análisis sintáctico) distintos para $w$.
2.  Existen dos o más **derivaciones por la izquierda** distintas para $w$.
3.  Existen dos o más **derivaciones por la derecha** distintas para $w$.

### Nota sobre la semántica
La ambigüedad sintáctica suele implicar **ambigüedad semántica**: si un compilador puede construir dos árboles diferentes, puede interpretar el código de dos maneras distintas (por ejemplo, cambiando el orden de ejecución de operaciones matemáticas).

---

## 3. Ejemplo Práctico: Expresiones Aritméticas

Consideremos la siguiente gramática $G$ que genera expresiones de sumas y multiplicaciones:

$$
S \rightarrow S + S \mid S * S \mid a
$$

Analizaremos la cadena de entrada:
$$w = a + a * a$$

Esta cadena es ambigua porque podemos generar dos árboles de análisis sintáctico completamente diferentes.

### Caso A: Interpretación (a + a) * a
En este árbol, la **suma** se evalúa primero (está más abajo en el árbol).

```{mermaid}
%%| label: fig-arbol1
%%| fig-cap: "Árbol 1: La suma tiene precedencia sobre la multiplicación"
graph TD
    Root[S] --> Left[S]
    Root --> Op1[*]
    Root --> Right[S]
    
    Left --> L1[S]
    Left --> Op2[+]
    Left --> L2[S]
    
    L1 --> term1(a)
    L2 --> term2(a)
    Right --> term3(a)

    style Root fill:#f9f,stroke:#333
    style Op1 fill:#ff9,stroke:#333
