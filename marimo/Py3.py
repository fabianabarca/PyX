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

    # `Py2` - *Librerías de computación científica*

    > Con librerías externas es posible acceder a poderosas herramientas computacionales que hacen a Python comparable con otros programas de cálculo numérico, como Matlab, R, Mathematica y otros.

    *Fabián Abarca Calderón*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Librerías especializadas

    Además de las librerías vistas en PyX anteriores, y que pertenecen a [The Python Standard Library](https://docs.python.org/3/library/), existen otras librerías de aplicación específica que personas y organizaciones externas han creado. Entre ellas, algunas útiles para el estudio de la probabilidad, la estadística y el análisis de datos. Específicamente estudiaremos NumPy, SciPy y Matplotlib aquí.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2.1 - NumPy

    Según su [página oficial](https://numpy.org/),

    > NumPy es el paquete fundamental para la computación científica con Python.

    <img src="https://numpy.org/images/logo.svg" width="150">

    * NumPy está diseñado para ser veloz, y por eso es parte de aplicaciones críticas en análisis de datos. Parte de la razón de esto es que la librería está escrita en Python y también en **C**.
    * Provee muchas herramientas para funciones matemáticas comunes.
    * Es la base de muchas otras librerías de Python, incluyendo SciPy.
    * Está orientado al manejo de matrices, tal como Matlab.

    ### 2.1.1. - Importar NumPy

    Por convención, NumPy se importa bajo el alias `np`.

    ```python
    import numpy as np
    ```

    NumPy viene con la instalación usual de [Anaconda](https://www.anaconda.com/products/individual). De otro modo, se puede instalar con la [guía](https://numpy.org/install/) de instalación.

    **Nota**: En Python, los *alias* son un nombre alternativo para referirse a la misma librería, de forma que las siguientes expresiones serían equivalentes, pero claramente una más abreviada:

    ```python
    # Sin el alias
    matplotlib.pyplot.plot()

    # Con el alias
    plt.plot()
    ```

    ### 2.1.2. - El contenedor `array`

    NumPy no utiliza listas, tuplas o diccionarios genéricos de Python. En cambio, la estructura de datos usual de NumPy es el `array`, que permite almacenar *valores numéricos* (exclusivamente) y efectuar operaciones eficientes sobre estos en la forma de matrices, como lo haría Matlab. Su sintaxis de creación es:

    ```python
    np.array([lista de numeros, separados, por, coma])
    ```

    El `array` es un contenedor **mutable**, y por tanto tiene los mismos métodos: inserción de elementos, eliminación, anexión, concatenación, etc.
    """)
    return


@app.cell
def _():
    import numpy as np
    _arr = np.array([1, 2, 3, 4, 5, 6])
    # Creacción del array
    suma = np.sum(_arr)
    base2 = np.exp2(_arr)
    # Operación sobre todos los elementos
    print('Arreglo:          ', _arr)
    print('Tipo de dato:     ', type(_arr))
    # Operación sobre cada elemento
    print('Primer elemento:  ', _arr[0])
    print('Último elemento:  ', _arr[-1])
    print('Suma de elementos:', suma)
    print('2^(cada elemento):', base2)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.3. - Generalización de los objetos *n*-dimensionales

    #### Crear un objeto NumPy `ndarray`

    NumPy crea `array` multidimensionales que representan matrices y son llamados `ndarray`.

    Es posible crear un objeto `ndarray` de NumPy utilizando la función `array()`.
    """)
    return


@app.cell
def _(np):
    nd1 = np.array([1, 2, 3, 4, 5, 6])
    nd2 = np.array([[1, 2, 3], [4, 5, 6]])
    # Matriz unidimensional (vector)
    nd3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print('Matriz unidimensional\n', nd1, '\n')
    # Matriz bidimensional
    print('Matriz bidimensional\n', nd2, '\n')
    # Matriz tridimensional
    print('Matriz tridimensional\n', nd3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ¿Cómo podríamos interpretar o visualizar este último arreglo tridimensional? Trate de imaginar que `1, 2, ..., 8` son los vértices de un cubo.

    NumPy `array` proporciona el atributo `ndim`, que retorna un entero con el número de dimensiones de la matriz.
    """)
    return


@app.cell
def _(np):
    _a = np.array(42)
    _b = np.array([1, 2, 3, 4, 5])
    _c = np.array([[7, 7, 7], [6, 6, 6]])
    _d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print('nd(a) =', _a.ndim)
    print('nd(b) =', _b.ndim)
    print('nd(c) =', _c.ndim)
    print('nd(d) =', _d.ndim)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.4. - Acceso a los elementos de una matriz

    Es posible acceder a un elemento de la matriz haciendo referencia a su número de **índice**. Para *n* dimensiones, los índices de un arreglo se referencian como:

    ```python
    arr[i_1, i_2, ..., i_n]
    ```

    **Nota**: Los índices en las matrices NumPy (como en Python) comienzan con 0.

    En el siguiente ejemplo se desea acceder al tercer elemento de la segunda matriz de la primera matriz de la primera dimensión. Esto se logra, para un arreglo tridimensional `arr`, con:

    ```python
    arr[0, 1, 2]
    ```

    Para el ejemplo a continuación:

    * El primer número representa la primera dimensión, que contiene dos matrices. Al escribir 0 se elige la primera matriz.
    * El segundo número representa la segunda dimensión, que también contiene dos matrices. Al elegir 1 se elige la segunda matriz.
    * El tercer número representa la tercera dimensión, que contiene tres valores. Con 2 se elige el tercer valor.
    """)
    return


@app.cell
def _(np):
    _arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print('Matriz tridimensional: \n', _arr)
    print('Primer elemento de la primera dimensión: \n', _arr[0])
    print('Segundo elemento del primer elemento de la primera dimensión: \n', _arr[0, 1])
    print('Tercer elemento del segundo elemento del primer elemento de la primera dimensión: \n', _arr[0, 1, 2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.5. - Operaciones en un `array` de NumPy

    De la [multitud](https://numpy.org/doc/stable/reference/) de funciones (rutinas) que ejecuta NumPy, estas pueden operar:

    * Sobre cada elemento (*element-wise*), retornando un `array` del mismo tamaño que esa dimensión.
    * Sobre todos los elementos en una dimensión, retornando uno solo o un conjunto de valores del mismo tamaño que esa dimensión.
    * Entre dos o más `array`, que puede retornar un solo valor o un vector, dependiendo de la operación.

    #### Operaciones sobre cada elemento de un `array`

    Algunas operaciones son:

    * Funciones trigonométricas, exponenciales, logarítmicas
    * Funciones "misceláneas" como redondeo, parte entera, conversión de grados a radianes, etc.

    En el siguiente ejemplo, `sqrt`, `log10`, `ceil` y `round` son todas de este tipo.
    """)
    return


@app.cell
def _(np):
    _arr = np.array([1, 2, 3, 5, 8, 13])
    _a = np.sqrt(_arr)
    _b = np.log10(_arr)
    print('Raíces:', np.ceil(_a))
    print('Logaritmos:', np.round(_b, 2))
    print('Mismo tamaño:', len(_arr) == len(_a) == len(_b))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operaciones sobre todos los elementos de un `array`

    El ejemplo más usual es el de la suma de los elementos. En un arreglo unidimensional, la operación `sum` suma todos los elementos. En un arreglo *n*-dimensional también, pero tiene la opción de elegir un "eje" (`axis`) sobre el cual sumar.

    Por ejemplo, en esta matriz, una suma sobre el eje 0 (la primera dimensión, las filas) es la suma de los elementos en las columnas, y una suma sobre el eje 1 (la segunda dimensión, las columnas) es la suma de los elementos en las filas.

    | –      | C0     | C1     | C2     | –      |
    |--------|--------|--------|--------|--------|
    | **F0** | *3*    | *8*    | *6*    | **17** |
    | **F1** | *2*    | *4*    | *5*    | **11** |
    | **F2** | *7*    | *1*    | *0*    | **8**  |
    | –      | **12** | **13** | **11** | –      |
    """)
    return


@app.cell
def _(np):
    _arr1 = np.array([-5, -3, 0, 1, 6, 9])
    _arr2 = np.array([[3, 8, 6], [2, 4, 5], [7, 1, 0]])
    _a = np.sum(_arr1)
    _b = np.sum(_arr2)
    _c = np.sum(_arr2, 0)
    _d = np.sum(_arr2, 1)
    print('Suma de todos los elementos:', _a)
    print('Suma de todos los elementos:', _b)
    print('Suma de los elementos en cada columna:', _c)
    print('Suma de los elementos en cada fila:', _d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operaciones entre dos o más `array`

    En el álgebra lineal, por ejemplo, hay operaciones vectoriales y matriciales entre dos o más arreglos, todas ellas presentes en NumPy. Pero también hay otras operaciones "misceláneas".
    """)
    return


@app.cell
def _(np):
    _a = np.array([1, 2, 3])
    _b = np.array([4, 5, 6])
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.add(A, B)
    D = np.multiply(A, B)
    E = np.vdot(_a, _b)
    print('Suma por elemento: \n', C)
    print('Multiplicación por elemento: \n', D)
    print('Producto punto: \n', E)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.6. - Polinomios

    Existen dos formas de tratar con polinomios 1-D en SciPy. El primero es usar la `poly1d` clase de NumPy. Esta clase acepta coeficientes o raíces polinómicas para inicializar un polinomio. El objeto polinomial puede manipularse en expresiones algebraicas, integrarse, diferenciarse y evaluarse. Incluso se imprime como un polinomio.
    """)
    return


@app.cell
def _():
    from numpy import poly1d

    p = poly1d([3,4,5])

    print('Polinomio: \n', p)
    print('Polinomio derivado: \n', p.deriv())
    print('Polinomio integrado: \n', p.integ())
    print('Polinomio al cuadrado: \n', p*p)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.7. - Tipos de datos en NumPy

    A continuación se muestra una lista de todos los tipos de datos en NumPy y los caracteres utilizados para representarlos.

    | Símbolo | Tipo |
    | ------- | ---- |
    | `i`     | entero     |
    | `b`     | booleano     |
    | `u`     | entero sin signo     |
    | `f`     | flotante     |
    | `c`     | flotante complejo     |
    | `m`     | timedelta     |
    | `M`     | fecha y hora     |
    | `O`     | objeto     |
    | `S`     | cadena de caracteres    |
    | `U`     | cadena unicode     |
    | `V`     | fragmento de memoria |

    **Nota**: El objeto de matriz NumPy tiene una propiedad llamada `dtype` que devuelve el tipo de datos de la matriz.
    """)
    return


@app.cell
def _(np):
    _arr1 = np.array([[1, 2, 3, 4], [9, 8, 7, 6]])
    _arr2 = np.array(['manzana', 'banano', 'fresa'])
    _arr3 = np.array([1.0, 2.0])
    print(_arr1.dtype)
    print(_arr2.dtype)
    print(_arr3.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Conversión de tipo de datos en matrices existentes

    La mejor manera de cambiar el tipo de datos de una matriz existente es hacer una copia de la matriz con el método `astype()`, que permite especificar el tipo de datos como parámetro.
    """)
    return


@app.cell
def _(np):
    _arr1 = np.array([1.4, 2.5, 3.6])
    _arr2 = _arr1.astype(str)
    _arr3 = _arr1.astype(int)
    print(_arr1, _arr1.dtype)
    print(_arr2, _arr2.dtype)
    print(_arr3, _arr3.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## 2.2 - SciPy

    Según su [página oficial](https://www.scipy.org/),

    > SciPy es un ecosistema de software de código abierto en Python para matemáticas, ciencias e ingeniería. SciPy está basado en NumPy, y para todas las necesidades básicas de manejo de arreglos se puede usar las funciones de NumPy.

    <img src="https://scipy.org/images/logo.svg" width="150px">

    SciPy ofrece módulos especializados en varios temas de ciencia e ingeniería, entre ellos:

    * Funciones básicas - (usando NumPy)
    * Funciones especiales - `scipy.special`
    * Integración - `scipy.integrate`
    * Optimización - `scipy.optimize`
    * Interpolación - `scipy.interpolate`
    * Transformadas de Fourier - `scipy.fft`
    * Procesamiento de señales - `scipy.signal`
    * Álgebra lineal - `scipy.linalg`
    * Estructuras de datos espaciales y algoritmos - `scipy.spatial`
    * **Estadísticas** - `scipy.stats`
    * Procesamiento de imágenes multidimensional - `scipy.ndimage`
    * Escritura y lectura de archivos - `scipy.io`

    El paquete `scipy.stats` será muy importante para el curso, y será abordado en otro PyX.

    **Nota**: Las estructuras (o contenedores) de datos son las mismas que NumPy, como `array`, y aplican todas las manipulaciones vistas anteriormente.

    ### 2.2.1 - Importar SciPy

    Para importar todo un módulo

    ```python
    from scipy import algun_modulo

    # Código aquí...

    algun_modulo.alguna_funcion()
    ```

    o bien solo funciones de un módulo

    ```python
    from scipy.algun_modulo import una_funcion, otra_funcion

    # Código aquí...

    una_funcion()
    otra_funcion()
    ```

    ### 2.2.2. - Integración

    Para hacer el cálculo numérico de una integral (definida o indefinida) es posible usar las siguientes dos (de varias) funciones de SciPy:

    * `quad`: integración de propósito general, conocida la función y los límites de integración.
    * `trapz`: integración de una muestra de datos con la regla trapezoidal.

    A continuación, el cálculo de la integral

    $$
    R = \int_{a}^{b} (rx^3 + s) ~ \mathrm{d}x
    $$

    utilizando

    ```python
    (resultado, error) = quad(funcion, lim_inf, lim_sup, args=())
    ```
    """)
    return


@app.cell
def _():
    from scipy.integrate import quad

    def paraintegrar(x, r, s):
        return r * _x ** 3 + s
    _a = 0
    _b = 2
    r = 1
    s = 0
    _R = quad(paraintegrar, _a, _b, args=(r, s))
    print(_R)
    print('Resultado:', _R[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cuando, en cambio, se tiene una muestra de datos de pares ordenados $(x, y)$ entonces se utiliza `trapz` para hacer una integración trapezoidal.

    La precisión de la aproximación depende del número de muestras en el intervalo de interés:

    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Trapezium2.gif" width="400">

    En el siguiente ejemplo observar que:

    * Los datos no son necesariamente `array` (en la documentación se les conoce como *array-like*, e incluye listas o tuplas).
    * Los puntos en el eje $x$ no están necesariamente uniformemente espaciados.
    * Los pares ordenados son extraídos de la misma función $rx^3 + s$ utilizada arriba, de forma que se sabe que con los límites de integración a = 0, b = 2 y parámetros r = 1, s = 0, el resultado de la integración es 4.
    """)
    return


@app.cell
def _():
    from scipy.integrate import trapz
    _x = (0.0, 0.5, 0.9, 1.2, 1.7, 2.0)
    _y = (0.0, 0.125, 0.729, 1.728, 4.913, 8.0)
    _R = trapz(_y, _x)
    print('Resultado:', _R)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2.3 - Matplotlib

    Según su [página oficial](https://matplotlib.org/),

    > Matplotlib es una biblioteca completa para crear visualizaciones estáticas, animadas e interactivas en Python.

    <img src="https://matplotlib.org/_static/images/documentation.png" width="150">

    En esta primera aproximación a Matplotlib, estudiaremos gráficas bidimensionales estáticas.

    ### 2.3.1. - Pyplot

    Pyplot es una interfaz "que hace a Matplotlib funcionar como Matlab", y en este primer acercamiento a Matplotlib será el módulo a utilizar.

    Según el [tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html) oficial:

    > Cada función `pyplot` realiza algún cambio en una figura: por ejemplo, crea una figura, crea un área de trazado (lienzo) en una figura, traza algunas líneas en un área de trazado, decora la trama con etiquetas, etc.

    Para importar Pyplot utilizamos:

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    ```

    ### 2.3.2. - Primer gráfico

    **Nota**: Es posible agregar código de $\mathrm{\LaTeX}$ con las etiquetas con `'$...$'`.
    """)
    return


@app.cell
def _(np):
    import matplotlib.pyplot as plt
    _x = np.linspace(0, 4 * np.pi, 60)
    _y = np.cos(_x)
    plt.plot(_x, _y)
    plt.ylabel('$\\cos(\\omega)$')
    plt.xlabel('$\\omega$')
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En el ejemplo anterior, `np.linspace(start, stop, num)` es una función que crea una secuencia uniformemente espaciada de `num` elementos entre `start` y `stop` pero sin incluir este último, es decir $[start, stop)$. Es necesario para crear un dominio, o conjunto de números en que la función (en el caso anterior, coseno) será evaluada. La cantidad `num` se elige según varios criterios, pero en general lo "suficiente" para que se vea "bien" (otras razones tienen que ver con la frecuencia de muestreo de Nyquist).

    Ver a continuación tres eleciones distintas de `num`, es decir, distintos muestreos de la función.

    **Nota**: Aquí se importan únicamente las funciones `pi`, `cos` y `linspace` de NumPy, y por tanto se puede cambiar la notación `np.pi` por `pi`.
    """)
    return


@app.cell
def _(plt):
    from numpy import pi, cos, linspace
    x1 = linspace(0, 2 * pi, 25)
    x2 = linspace(0, 2 * pi, 15)
    x3 = linspace(0, 2 * pi, 5)
    y1 = cos(x1)
    y2 = cos(x2 + pi / 6)
    y3 = cos(x3 + pi / 3)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.title('Gráficas con distinto número de puntos de muestra')
    plt.ylabel('$\\cos(\\omega)$')
    plt.xlabel('$\\omega$')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.3.3. - Gráficas de múltiples funciones

    Combinando las herramientas de NumPy, SciPy y Pyplot, es posible graficar infinidad de formas, incluyendo funciones propias creadas en Python.

    Hay una lista extensísima de funciones matemáticas en NumPy [aquí](https://numpy.org/doc/stable/reference/routines.math.html).
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 2, 100)

    def hola(x):
        _y = np.log(_x + 1)
        return _y
    plt.plot(_x, np.sqrt(_x))
    plt.plot(_x, np.power(_x, 1.2))
    plt.plot(_x, hola(_x))
    plt.title('Algunas funciones')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(left=0, right=2)
    plt.ylim(bottom=0)
    plt.grid()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.3.4. - Modificación de la apariencia de las curvas

    Es posible cambiar el color y el trazado de las funciones con instrucciones sencillas. Para eso, se modifican los argumentos de la función `plt.plot` con cualquiera de los "argumentos por clave" (*keyword arguments* o **\*\*kwargs**) (lista completa [aquí](https://matplotlib.org/tutorials/introductory/pyplot.html#controlling-line-properties)):

    | Propiedad          | Valor                                       |
    |--------------------|---------------------------------------------|
    | `color` o `c`      | cualquier color de Matplotlib               |
    | `label`            | cualquier texto                             |
    | `linestyle` o `ls` | ( '-' o '--' o '-.' o ':' o 'steps' o ...)  |
    | `linewidth` o `lw` | valor decimal de puntos                     |
    | `marker`           | ( '+' o ',' o '.' o '1' o '2' o '3' o '4' ) |

    Las opciones para especificar colores están [aquí](https://matplotlib.org/3.1.0/gallery/color/named_colors.html).

    Al especificar una etiqueta (`label`) para cada curva se puede entonces invocar una "leyenda".
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, np.pi, 100)
    plt.plot(_x, np.sqrt(_x), label='Raíz cuadrada', color='darkmagenta', linestyle='--', linewidth=2.3)
    plt.plot(_x, np.cos(_x), label='Coseno', c='midnightblue', ls='-.', lw=1.6)
    plt.plot(_x, np.sin(_x), label='Seno', c='firebrick', ls=':', lw=3.1)
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.title('Distintas opciones de línea')
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.3.5. - Exportar imágenes

    Ya tenemos gráficos, ¿cómo se pueden utilizar en otras aplicaciones? La forma más sencilla es exportar la imagen en un formato especificado. Los formatos recomendados son:

    * JPG: imagen "rasterizada" (con pérdidas).
    * PNG: imagen "rasterizada" (con pérdidas) que permite transparencias.
    * SVG: archivo vectorial (sin pérdidas) soportado en navegadores web, LaTeX y otros.
    * PDF: archivo vectorial portable no modificable.

    La función de Matplotlib para hacerlo es `savefig`, cuya documentación está [aquí](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.savefig.html).

    Ejemplo:

    ```python
    import matplotlib.pyplot as plt

    # Crear gráfico aquí

    plt.savefig('/imágenes/señales', format='png', transparent=True)
    ```

    donde

    * `/imágenes/` es la carpeta (dentro del directorio actual) donde se va a guardar
    * `señales` es el nombre del archivo
    * `format='png'` es el tipo de archivo
    * `transparent=True` habilita o no las transparencias

    ### 2.3.6. - Exportar imágenes a $\mathrm{\LaTeX}$

    La librería [TikZplotlib](https://anaconda.org/conda-forge/tikzplotlib) es una herramienta para convertir una gráfica de Matplotlib a $\mathrm{\LaTeX}$ vía PGFplots de TikZ. Es fácil de usar, y solamente debe instalarse en la terminal antes con

    ```bash
    $ pip install tikzplotlib
    ```

    Similar al caso de `savefig` discutido, el procedimiento es:

    ```python
    import tikzplotlib

    # Crear gráfico aquí

    tikzplotlib.save('señales.tex')
    ```

    donde

    * `señales.tex` es el nombre del archivo

    El archivo `.tex` generado puede luego ser compilado en un proyecto de $\mathrm{\LaTeX}$, creando gráficas nativas, vectoriales, adaptables que lucen muy bien.

    ### 2.3.7. - Hojas de estilo de Matplotlib

    Matplotlib [permite configurar](https://matplotlib.org/stable/tutorials/introductory/customizing.html) la apariencia de las gráficas con hojas de estilo que modifican los más de 300 [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams).

    Por ejemplo, un archivo `mpss.mplstyle` creado para el curso incluye ciertos ajustes:

    ```python
    lines.linewidth     : 4
    axes.prop_cycle     : cycler('color', ['005DA4', '00C0F3', '6DC067', 'FFE06A'])
    axes.spines.right   : False
    axes.spines.top     : False
    ```

    - el ancho de las líneas a 4 px
    - los colores de la UCR en hexadecimal
    - sin eje derecho
    - sin eje superior

    Finalmente, se ingresa en el código con:

    ```python
    plt.style.use('./mpss.mplstyle')
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Más información

    * [Tutorial de NumPy](https://unipython.com/numpy-algebra/)
    * [Tutorial de SciPy](https://riptutorial.com/es/scipy)
    * [Tutorial de Pyplot](https://pybonacci.org/2012/05/14/manual-de-introduccion-a-matplotlib-pyplot-i/)
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
