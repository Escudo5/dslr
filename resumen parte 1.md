# Resumen de Exploración y Visualización de Datos (Parte 1)

Este documento reúne los conceptos de ciencia de datos y programación en Python aplicados en los tres primeros scripts del proyecto (`histogram.py`, `scatter_plot.py` y `pair_plot.py`) para preparar la selección de variables (*features*) antes de entrenar la regresión logística.

---

## 1. Los tres gráficos y sus conclusiones

| Script | Tipo de gráfico | Qué compara | Pregunta que responde | Hallazgo en Hogwarts |
| :--- | :--- | :--- | :--- | :--- |
| **`histogram.py`** | Histograma | 1 asignatura dividida por las 4 casas | ¿Qué asignatura tiene una distribución homogénea? | **Arithmancy** y **Care of Magical Creatures** |
| **`scatter_plot.py`** | Dispersión (puntos) | 2 asignaturas entre sí (eje X vs. eje Y) | ¿Qué dos asignaturas son similares o redundantes? | **Astronomy** y **Defense Against the Dark Arts** |
| **`pair_plot.py`** | Matriz de dispersión ($13 \times 13$) | Todas las asignaturas contra todas, coloreadas por casa | ¿Qué asignaturas elegimos para entrenar el modelo? | Descartamos las homogéneas y una de las dos gemelas |

### Detalle de cada análisis

* **Histograma (`histogram.py`):** Muestra cuántas notas caen en cada rango de valores para cada casa.
  * **Asignaturas no homogéneas:** En *Astronomy*, por ejemplo, Ravenclaw y Slytherin se agrupan alrededor de $-500$, mientras que Gryffindor y Hufflepuff se concentran cerca de $+500$. Al estar separadas, sirven para distinguir casas.
  * **Asignaturas homogéneas:** En **Arithmancy** y **Care of Magical Creatures**, las cuatro curvas caen unas encima de otras con prácticamente la misma distribución. Como todas las casas sacan notas similares, **no aportan información útil** para clasificar alumnos.
* **Gráfico de dispersión (`scatter_plot.py`):** Cada punto representa a un alumno cruzando dos asignaturas.
  * Si no tienen relación, forman nubes dispersas.
  * **Astronomy** y **Defense Against the Dark Arts** dibujan una **línea recta diagonal perfecta** (con pendiente negativa: una es literalmente la otra dividida entre $-100$). Esto indica **correlación o redundancia**: saber una nota permite calcular la otra al instante, por lo que basta con darle una sola al modelo.
* **Matriz de dispersión (`pair_plot.py`):** Combina histogramas por casa en la diagonal principal y *scatter plots* coloreados por casa en el resto de casillas.
  * **Variables descartadas:** `Arithmancy` y `Care of Magical Creatures` (por ser homogéneas), una de entre `Astronomy` o `Defense Against the Dark Arts` (por información duplicada), y columnas sin valor predictivo como `Index` o los nombres.
  * **Variables elegidas para el modelo:** Asignaturas donde los grupos de colores de las casas aparecen bien separados en «islas» limpias, como **Herbology**, **Divination**, **Muggle Studies**, **Ancient Runes**, **Charms** o **Flying**.

---

## 2. Librerías de Python utilizadas

* **`pandas` (Manipulación de tablas):**
  * `pd.read_csv(ruta)`: Carga el archivo CSV en un *DataFrame* (tabla).
  * **Filtrado condicional:** Permite aislar filas y columnas específicas respetando mayúsculas y minúsculas exactas (por ejemplo: `df[df["Hogwarts House"] == "Slytherin"]["Astronomy"]`).
  * **`.dropna()`:** Elimina filas con valores vacíos (`NaN`). En los *scatter plots* es fundamental limpiar las dos columnas juntas (`df[["Col1", "Col2"]].dropna()`) para que ambos ejes conserven exactamente el mismo número de alumnos emparejados.
* **`matplotlib.pyplot` (`plt` — Gráficos base):**
  * `plt.hist(..., alpha=0.5, bins=30, color=..., label=...)`: Dibuja histogramas. `alpha=0.5` aplica semitransparencia para ver barras superpuestas y `bins=30` divide los datos en 30 barras finas para apreciar mejor la forma de la distribución.
  * `plt.scatter(x, y, alpha=0.5)`: Dibuja nubes de puntos entre dos variables.
  * **Etiquetado:** `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.legend()` y `plt.show()`.
* **`seaborn` (`sns` — Visualización estadística):**
  * `sns.pairplot(datos_limpios, hue="Hogwarts House")`: Genera automáticamente toda la cuadrícula de cruces entre variables, usando el parámetro `hue` para colorear cada punto según la casa del alumno.

---

## 3. Conceptos de programación aplicados

* **Automatización con listas y bucles `for`:** En lugar de repetir código 13 veces para explorar cada asignatura, se guardan los nombres en una lista (`subjects`) y se recorren con `for element in subjects:`. Dentro del bucle se usa la variable sin comillas (`df[element]`) en lugar de un texto fijo (`df["Astronomy"]`).
* **Sangría (indentación):** En Python, los espacios a la izquierda (4 u 8 espacios) definen qué instrucciones pertenecen a una función, a un bucle `for` o a un bloque `try / except`. Si `plt.show()` queda fuera de la sangría del bucle, todos los gráficos se dibujan amontonados en una sola ventana.
* **Argumentos por terminal (`sys.argv` y `sys.exit()`):** Permite pasar la ruta del dataset al ejecutar el script (`python3 histogram.py dataset_train.csv`) leyendo `sys.argv[1]`. Se comprueba `len(sys.argv) < 2` sin forzar un nombre fijo de ruta para que el programa funcione aunque el archivo esté en otra carpeta.
* **Manejo de errores (`try / except Exception`):** Actúa como red de seguridad al abrir el CSV; si el usuario escribe mal el nombre del archivo, captura el fallo, muestra un aviso limpio por pantalla y cierra el programa ordenadamente con `sys.exit()`.