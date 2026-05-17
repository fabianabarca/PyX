import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    **Universidad de Costa Rica** | Escuela de Ingeniería Eléctrica

    *IE0405 - Modelos Probabilísticos de Señales y Sistemas*

    ### `PyX` - Serie de tutoriales de Python para el análisis de datos

    # `Py3` - *Librería de manipulación y análisis de datos Pandas*

    > **Pandas** es una útil y popular librería de manipulación de datos que ofrece estructuras de datos para el análisis de tablas numéricas y series de tiempo. Por sus capacidades, es comparable con Excel u otras hojas de cálculo, pero de forma *programática*. Esta es una introducción al objeto `DataFrame` y sus características básicas.

    *Fabián Abarca Calderón* \
    *Jonathan Rojas Sibaja*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Librería Pandas

    Para trabajar con una gran cantidad de datos, es deseable un conjunto de herramientas que nos permitan efectuar operaciones comunes de forma intuitiva y eficiente. Pandas, es la solución por defecto para hacerlo en Python, y es parte del ecosistema de SciPy. Viene instalado con Anaconda.

    **Nota 0**: La documentación oficial está en [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/).

    Esta guía está basada en "[Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)".

    **Nota 1**: Para toda esta guía se hará la siguiente importación de librerías.

    **Nota 2**: Por convención, el *alias* de Pandas es `pd`.
    """)
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import datetime

    return np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Estructuras de datos de Pandas

    Pandas permitirá la creación de las nuevas estructuras de datos `Series` y `DataFrame`, que son clases optimizadas para manipulación de datos. Aunque son similares en su forma a estructuras de Python como listas y diccionarios, en realidad incorporan una gran cantidad de nuevos atributos y métodos:

    | Clase       | Atributos | Métodos |
    |-------------|-----------|---------|
    | `Series`    | 20+       | 180+    |
    | `DataFrame` | 10+       | 210+    |

    - [Documentación](https://pandas.pydata.org/docs/reference/series.html) de `Series`
    - [Documentación](https://pandas.pydata.org/docs/reference/frame.html) de `DataFrame`
    ---
    ## 3.1. - `Series`

    En Python, las `Series` corresponden a un arreglo de **una** dimensión que admite diversos tipos de datos (números enteros, palabras, números flotantes, objetos de Python, etc.) y que además están etiquetados mediante un índice que el usuario puede definir o permitir que Python lo cree por defecto.

    Para crear listas o `Series` de valores se utiliza la siguiente sintaxis:

    ```python
    pandas.Series(data=None, index=None,
                  dtype=None, name=None, copy=False, fastpath=False)
    ```

    donde `data` es una secuencia o estructura de datos iterable de Python, como una lista, una tupla, un diccionario, un rango, etc. El siguiente ejemplo tiene indexado automático.
    """)
    return


@app.cell
def _(np, pd):
    s = pd.Series([1, 3, 5, np.nan, "modelos", 8.5])

    # Ver objeto Series
    print(s)

    # Utilizar atributo .count
    print('Número de elementos no nulos: {}.'.format(s.count()))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Utilizado el comando de NumPy `random.randn` es posible generar datos aleatorios para la lista. También es posible agregar índices distintos a los numéricos, utilizando el argumento `index` y una lista de índices del mismo tamaño que los datos.
    """)
    return


@app.cell
def _(np, pd):
    s_1 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    print(s_1)
    p = pd.Series([1, '!', 5, '?', 'hola', 13], index=[6, 5, 4, 3, 2, 1])
    print(p)
    q = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'e'])
    print(q)
    return q, s_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Es posible hacer una inspección a los atributos y métodos de los objetos `Series` creados anteriormente con la función `dir()` de Python, y podrán apreciarse descriptores estadísticos como la correlación o la media.
    """)
    return


@app.cell
def _(s_1):
    print(dir(s_1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Una vez creado el objeto `Series` se pueden ejecutar operaciones vectoriales con la misma o agregar otros atributos, como un nombre.
    """)
    return


@app.cell
def _(pd, q):
    _d = pd.Series(q + q, name='suma')
    print(_d)
    e = pd.Series(q ** 2, name='potencia')
    print(e)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.2. - `DataFrame`

    En Pandas, un `DataFrame` corresponde a un arreglo etiquetado de **dos dimensiones**, semejante a concatenar varias `Series`. También admite varios tipos de datos.

    > Un `DataFrame` tiene una funcionalidad equivalente a una hoja de cálculo o una tabla SQL y permite manipular datos de forma versátil y eficiente.

    La sintaxis de creación de un `DataFrame` es:

    ```python
    pandas.DataFrame(data=None, index=None,
                     columns=None, dtype=None, copy=None)
    ```

    donde `data` es típicamente un diccionario en el que cada llave/valor describe una columna. Sin embargo, se puede crear de varias otras maneras, como desde archivos JSON o CSV importados.

    La asignación de las etiquetas puede ser decidida por el usuario y Python hará coincidir los valores, en caso de diferencias en los tamaños de las listas agregadas, rellenará esos espacios siguiendo reglas de sentido común.

    A continuación un ejemplo de dos `Series` de diferentes tamaños. Observar las diferencias en el orden de los índices.
    """)
    return


@app.cell
def _(pd):
    # Creación de un diccionario con las series indexadas
    _d = {'esta': pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']), 'otra': pd.Series([1.0, 2.0, 3.0, 4.0], index=['c', 'a', 'd', 'b'])}
    df = pd.DataFrame(_d)
    # Creación del DataFrame a partir del diccionario
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Con `dir()` también es posible consultar atributos y métodos disponibles de `DataFrame`.

    ##### Ejemplo con índice tipo "timestamp"

    Los índices podrían ser una estampa de tiempo (*timestamp*). Este es un caso útil en el que, por ejemplo, se lleva un registro de varias variables (las columnas) en una sucesión de momentos distintos (el índice):
    """)
    return


@app.cell
def _(np, pd):
    # Creación de un rango de fechas
    fechas = pd.date_range('20200101', periods=6)
    df_1 = pd.DataFrame(np.random.randn(6, 4), index=fechas, columns=list('ABCD'))
    # Creación de un DataFrame con las fechas como índices
    df_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Ejemplo con distintos tipos de datos

    Como en las `Series`, los `DataFrame` pueden utilizar diferentes tipos de datos en cada columna y asignarse como diccionarios.
    """)
    return


@app.cell
def _(np, pd):
    df_2 = pd.DataFrame({'A': 1.0, 'B': pd.Timestamp('20200101'), 'C': pd.Series(1, index=list(range(4))), 'D': np.array([3] * 4, dtype='int32'), 'E': pd.Categorical(['norte', 'sur', 'este', 'oeste']), 'F': 'hola'})
    df_2
    return (df_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Modificaciones al `DataFrame`

    Una vez incializado el `DataFrame`, se pueden ejecutar acciones como extraer, eliminar e insertar columnas, con una sintaxis similar a la de los [diccionarios](https://www.w3schools.com/python/python_dictionaries.asp).
    """)
    return


@app.cell
def _(df_2):
    # Extraer una columna
    df_2['E']
    return


@app.cell
def _(df_2):
    # Eliminar columna 'F'
    del df_2['F']
    # Mostrar nuevo DataFrame sin columna 'F'
    df_2
    return


@app.cell
def _(df_2, np, pd):
    # Asignar nuevos datos a la columna 'A'
    df_2['A'] = pd.Series(np.random.randn(4), index=list(range(4)))
    df_2
    return


@app.cell
def _(df_2):
    # Crear nueva columna 'A+' y agregar valores según criterio
    df_2['A+'] = df_2['A'] > 0
    # Mostrar nuevo DataFrame
    df_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.3. - Inspeccionar los datos

    Es posible (y útil) "echar un vistazo" a los primeros y últimos datos. Por ejemplo, del `DataFrame` llamado `df` se pueden ver las primeras ***N*** filas de datos con el comando `head`.
    """)
    return


@app.cell
def _(df_2):
    df_2.head(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Si solamente se desea visualizar las útimas tres líneas se utiliza el comando `tail`:
    """)
    return


@app.cell
def _(df_2):
    df_2.tail(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para visualizar los índices, se utiliza:
    """)
    return


@app.cell
def _(df_2):
    df_2.index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Ejemplo de convertir a NumPy

    Cuando sea deseable, se puede transformar el `DataFrame` a un `array` de NumPy.
    """)
    return


@app.cell
def _(df_2):
    df_2.to_numpy()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Lo anterior tanto si el `DataFrame` tiene un solo tipo o diversos tipos de datos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Ejemplo de manipulación para un solo tipo de datos

    Si todos los elementos son del mismo tipo, se pueden ejecutar algunas funciones de análisis y manipulación específicas, especialmente si son datos numéricos.

    A continuación se crea un `DataFrame` tipo matriz 6$\times$4 de números aleatorios.
    """)
    return


@app.cell
def _(np, pd):
    df_num = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"), index=['a', 'b', 'c', 'd', 'e', 'f'])

    df_num
    return (df_num,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Es posible obtener un resumen de los principales descriptores estadísticos de cada columna, en este caso: el conteo de elementos, la media, la desviación estándar, el valor mínimo, el primer, segundo y tercer cuartil, y el valor máximo.
    """)
    return


@app.cell
def _(df_num):
    df_num.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Reordenar datos

    Es común desear reordenar los datos con alguna columna de referencia:
    """)
    return


@app.cell
def _(df_num):
    df_num.sort_values(by='B')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.4. - Seleccionar datos

    > En Python, la selección (o búsqueda) de datos utilizando Pandas es más eficiente que las expresiones para seleccionar y obtener datos en NumPy.

    Por ejemplo, para ubicar una **fila** de datos, se puede utilizar el comando  `loc`, que tiene muchas opciones para buscar índices, según la [documentación](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html).
    """)
    return


@app.cell
def _(df_2):
    df_2.loc[2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    También se pueden seleccionar un rango de filas (registros) al mismo tiempo:
    """)
    return


@app.cell
def _(df_2):
    df_2[0:3]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para obtener una posición en específico, se debe indicar la fila y la columna mediante el comando `at`:
    """)
    return


@app.cell
def _(df_2):
    df_2.at[2, 'E']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se puede ubicar ese mismo elemento por medio de la posición y no los índices, utilizando el comando `iloc`:
    """)
    return


@app.cell
def _(df_2):
    df_2.iloc[2, 4]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se pueden ubicar los datos que cumplan con cierta condición booleana:
    """)
    return


@app.cell
def _(df_2):
    df_2[df_2['A'] > 0]
    return


@app.cell
def _(df_2):
    df_2[df_2['E'] == 'sur']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.5. - Operaciones sobre datos

    En Python, las operaciones se ejecutan sobre todos los datos arrojando el valor de salida por filas o columnas.

    Por ejemplo, para calcular la media estadística de los datos de cada columna, se utiliza el comando `mean` que recorre la dimensión `0` (filas) de la siguiente manera:
    """)
    return


@app.cell
def _(df_num):
    df_num.mean(0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Si en cambio se desea conocer la media de los valores por filas, se utiliza la siguiente variación, donde `1` es la dimensión de las columnas:
    """)
    return


@app.cell
def _(df_num):
    df_num.mean(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Ejemplo de conteo de ocurrencias de valores únicos

    Para la siguiente serie de ejemplo:
    """)
    return


@app.cell
def _(np, pd):
    letras = ['a', 'b', 'c', 'd', 'e']
    serie = pd.Series(np.random.choice(letras, size=15))
    serie
    return (serie,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se pueden aplicar operaciones tales como el conteo (o "apariciones de cada uno") sobre `Series` o `DataFrame`, y devuelve un resultado clasificado de mayor a menor número de ocurrencias.
    """)
    return


@app.cell
def _(serie):
    serie.value_counts()
    return


@app.cell
def _(df_2):
    df_2.value_counts(df_2['A+'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Operaciones sobre caracteres

    También existen operaciones que se pueden aplicar sobre `Series` de palabras:
    """)
    return


@app.cell
def _(pd):
    G = pd.Series(['ÁRbOL', 'BLanCO', 'AvE', 'BuRRo'])
    g = G.str.lower()

    pd.DataFrame({'G': G, 'g': g})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.6. - Fusionar datos

    En Pandas, para concatenar datos se utiliza el comando `concat()` donde

    ```python
    pandas.concat(objs, axis=0, join='outer', ignore_index=False,
                  keys=None, levels=None, names=None, verify_integrity=False,
                  sort=False, copy=True)[source]
    ```

    donde `axis=` determine a lo largo de cuál dimensión se concatenan: `0` filas (vertical) y `1` columnas (horizontal) de la siguiente forma:
    """)
    return


@app.cell
def _(np, pd):
    # Crear DataFrame de ejemplo
    df_a = pd.DataFrame(np.random.randn(5,2))
    df_b = pd.DataFrame(np.random.randn(5,2))

    # Extraer fragmentos y concatenarlos
    fragmentos = [df_a[:], df_b[:]]
    pd.concat(fragmentos, axis=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Nota**: Observar que es necesario extraer los fragmentos primero porque no se pueden concatenar `DataFrame` directamente.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.7. - Agrupar datos

    En Pandar, "agrupar" se refiere a:

    - Separar los datos en grupos basándose en un criterio.
    - Aplicar una función a cada grupo independientemente.
    - Combinar los resultados en una estructura de datos.

    A continuación hay un ejemplo de agrupación aplicando una suma a las columnas numéricas asociadas por cierto criterio:
    """)
    return


@app.cell
def _(np, pd):
    df_foo = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo'],
                           'B': ['uno', 'dos', 'dos', 'tres', 'dos'],
                           'C': np.random.randn(5),
                           'D': np.random.randn(5)})
    df_foo
    return (df_foo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El siguiente resultado agrupa las filas según los elementos en `A` y suma los resultados de las columnas no categóricas (es decir, numéricas), que en este caso son `C` y `D`.
    """)
    return


@app.cell
def _(df_foo):
    df_foo.groupby('A').sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    El siguiente resultado agrupa primero por `A` y luego por `B`, para finalmente sumar las columnas `C` y `D` asociadas.
    """)
    return


@app.cell
def _(df_foo):
    df_foo.groupby(['A', 'B']).sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.8. - Reacomodar datos

    ##### Apilar

    En Pandas, una forma de reacomodar los datos es mediante el comando `stack`:
    """)
    return


@app.cell
def _(df_2):
    pila = df_2.stack()
    pila
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Tabla pivote

    También se puede cambiar la forma de ordenar los datos como tablas pivote:
    """)
    return


@app.cell
def _(np, pd):
    df_piv = pd.DataFrame({'A': ['uno', 'uno', 'dos', 'tres']*3,
                           'B': ['A', 'B', 'C']*4,
                           'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar']*2,
                           'D': np.random.randn(12),
                           'E': np.random.randn(12)})
    df_piv
    return (df_piv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En la siguiente tabla va a sumar los valores en `D` asociados con la agrupación con respecto a `A` y `B`, para cada categoría en `C`. Es una herramienta **poderosa**.
    """)
    return


@app.cell
def _(df_piv, pd):
    v = pd.pivot_table(df_piv, values='D', 
                       index=['A', 'B'], columns=['C'])
    v
    return (v,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ¿Cómo extraer un elemento de una tabla pivote?
    """)
    return


@app.cell
def _(v):
    v['bar']['dos']['B']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.9. - Series de tiempo

    En Pandas, las series de tiempo permiten generar secuencias con una frecuencia fija en un lapso de tiempo, como por ejemplo:
    """)
    return


@app.cell
def _(pd):
    # Tres ciclos horarios que inician el 1 de enero de 2020
    dti = pd.date_range('1-1-2020', periods=3, freq='H')
    dti
    return (dti,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cuya hora se puede convertir a una zona horaria diferente:
    """)
    return


@app.cell
def _(dti):
    dti_1 = dti.tz_localize('America/Costa_Rica')
    dti_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    También se pueden convertir una serie de tiempo a una frecuencia particular:
    """)
    return


@app.cell
def _(pd):
    idx = pd.date_range('2020-01-01', periods=5, freq='H')
    ts = pd.Series(range(len(idx)), index=idx)
    ts
    return (ts,)


@app.cell
def _(ts):
    ts.resample('2H').mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.10. - Gráficas

    En Python, se utiliza la asignación estándar para utilizar los comandos del API de `matplotlib` como métodos de la `Series` y `DataFrame`. Así, por ejemplo, se puede graficar una `Serie` de datos:
    """)
    return


@app.cell
def _(np, pd):
    import matplotlib.pyplot as plt
    plt.close('all')
    ts_1 = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000))
    ts_1 = ts_1.cumsum()
    # Crear serie temporal
    ts_1.plot()
    plt.xlabel('Días')
    # Suma acumulada
    # Método .plot() de Matplotlib sobre la serie temporal
    plt.ylabel('Valor')
    return plt, ts_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    También se pueden graficar arreglos del tipo `DataFrame` de manera que se grafican varias curvas en una misma gráfica como se muestra a continuación:
    """)
    return


@app.cell
def _(np, pd, plt, ts_1):
    # Crear números aleatorias con el mísmo índice de ts
    df_3 = pd.DataFrame(np.random.randn(1000, 4), index=ts_1.index, columns=['A', 'B', 'C', 'D'])
    df_3 = df_3.cumsum()
    plt.figure()
    df_3.plot()
    # Graficar las curvas
    plt.legend(loc='best')
    plt.xlabel('Días')
    plt.ylabel('Valor')
    return (df_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3.11. - Importar y exportar datos

    Pandas es un excelente "manejador" de archivos externos de datos, tipo `.xls` o `.csv`. Por ejemplo, para crear un archivo `modelos.csv` a partir de los datos anteriores:
    """)
    return


@app.cell
def _(df_3):
    df_3.to_csv('modelos')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cuyo contenido se puede "llamar" nuevamente utilizando el comando a continuación, que lo guarda como un `DataFrame`.
    """)
    return


@app.cell
def _(pd):
    pd.read_csv('modelos')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Más información

    * [Página oficial de Pandas](https://pandas.pydata.org/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **Universidad de Costa Rica** | Facultad de Ingeniería | Escuela de Ingeniería Eléctrica

    &copy; 2021

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
