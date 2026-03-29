# Dataset Sintético de Abandono Escolar 🎓

Este repositorio contiene un conjunto de datos sintéticos generado en Python diseñado para simular y analizar los factores que influyen en el abandono escolar. El proyecto cumple con los requisitos académicos de generación de datos, inclusión de ruidos (nulos/atípicos) y análisis de variables.

## 📊 Descripción del Conjunto de Datos

El dataset cuenta con **500 registros** y las siguientes variables:

| Variable | Tipo | Descripción | Rango/Valores |
| :--- | :--- | :--- | :--- |
| `id_estudiante` | Entero | Identificador único del alumno. | 1 - 500 |
| `edad` | Entero | Edad cronológica del estudiante. | 17 - 25 años (aprox.) |
| `promedio` | Decimal | Calificación promedio acumulada (GPA). | 1.0 - 5.0 |
| `asistencia_pct` | Entero | Porcentaje de asistencia a clases. | 40% - 100% |
| `ingreso_mensual` | Entero | Ingreso familiar mensual (COP). | Distribución normal |
| `tiene_beca` | Categórica | Indica si el alumno posee apoyo financiero. | Si / No |
| `abandono` | Categórica | **Variable de salida** (Target). | Si / No |

---

## 🛠️ Metodología de Generación

Para que el dataset sea realista y útil para pruebas de limpieza de datos, se aplicaron las siguientes técnicas:

### 1. Introducción de Valores Nulos
Se introdujeron deliberadamente valores nulos (`NaN`) en la columna `promedio`.
* **Método:** Se seleccionaron 15 índices de forma aleatoria mediante `numpy` y se reemplazaron sus valores originales por nulos.
* **Propósito:** Simular errores de captura o falta de información en el sistema académico.

### 2. Valores Atípicos (Outliers)
Se forzaron valores fuera de los rangos lógicos en dos variables clave:
* **Edad:** Se insertaron valores extremos como **5, 85 y 99 años** en 10 registros aleatorios.
* **Ingreso Mensual:** Se asignaron ingresos de **50.000.000** a 5 registros para simular casos atípicos de extrema riqueza o errores de digitación.

### 3. Lógica de la Variable de Salida
La variable `abandono` no es puramente aleatoria. Se utilizó una **función de probabilidad ponderada**:
* Si un estudiante tiene un `promedio` bajo (< 3.0) o una `asistencia` menor al 70%, su probabilidad de abandono sube al **80%**.
* En casos normales, la probabilidad de abandono se mantiene en un **10%**.

---

## 🚀 Cómo ejecutar el generador

Si deseas replicar la generación de los datos, asegúrate de tener instalado `pandas` y `numpy`:

```bash
pip install pandas numpy