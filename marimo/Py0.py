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

    ### `PyX` - Serie de tutoriales de Python para el análisis de datos

    # `Py0` - *Introducción a Python*

    > Python es un lenguaje de programación de uso general, en la actualidad el más popular para análisis de datos. Su sintaxis fue pensada desde el inicio para ser más legible.

    *Fabián Abarca Calderón*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Instalación

    Existen varias formas de ejecución de Python. Puede ser ejecutado en la propia computadora o bien en alguna de las varias plataformas en línea que existen, como [Google Colab](https://colab.research.google.com/) o [molab](https://molab.marimo.io/notebooks). En la máquina local es necesario instalar Python y un admninistrador de paquetes en cualquier plataforma (Linux, Windows, macOS).

    - La instalación recomendada de Python y sus paquetes es con [uv](https://docs.astral.sh/uv/).
    - También es posible la instalación de [Anaconda](https://www.anaconda.com/).

    Una vez instalado alguno de estas herramientas, se pueden "correr" *scripts* con la extensión `.py` desde la terminal (también llamada línea de comandos, consola o CLI, de *Command Line Interface*).

    * Ejecutando el código fuente con Python:

    ```bash
    $ python script.py
    ```

    * O usarlo en modo interactivo en la CLI:

    ```bash
    $ python
    >>> print('Hola')
    Hola
    ```

    o desde cualquiera de los muchos **IDE** (entornos de desarrollo integrado, *Integrated Development Environments*) disponibles, como:

    * [Visual Studio Code](https://code.visualstudio.com/)
    * [Cursor](https://cursor.com/)
    * [Antigravity](https://antigravity.google/)
    * [Eclipse](https://www.eclipse.org/ide/)
    * [PyCharm](https://www.jetbrains.com/es-es/pycharm/)
    * [Sublime](https://www.sublimetext.com/)

    ### Más información

    La información más precisa sobre los aspectos básicos del lenguaje Python están en el [manual de referencia](https://docs.python.org/3/library/) de la _Librería Estándar_ de Python. Sin embargo, es posible encontrar muchas otras buenas referencias en internet, desde cursos en línea, páginas de referencia (ver final del documento), preguntas en foros y hasta el muy buen [Wikibook de Python](https://en.wikibooks.org/wiki/Python_Programming).

    #### Antes de empezar...

    **Nota 0**: Para ejecutar una celda de código en este _notebook_ se utilizan las teclas `shift` + `enter`, o "Run" en el panel superior cuando la celda está seleccionada.

    **Nota 1**: La función `print()` muestra el resultado de la evaluación de su(s) argumento(s).

    **Nota 2**: Los comentarios en el código fuente de Python se hacen con `#` en una sola línea o con `''' (comentario) '''` en varias líneas.

    **Nota 3**: En Python el índice comienza en 0.

    **Nota 4**: Como lenguaje orientado a objetos, Python utiliza la "notación del punto": `objeto.atributo` o bien `objeto.método()`, que son *variables* y *funciones* asociadas con un objeto.

    **Nota 5**: La forma "pitónica" de programar en Python (*the Pythonic way*) son convenciones que hacen el código más legible y sencillo.

    **Nota 6**: La _guía de estilo_ para la escritura de código en Python es [PEP 8](https://peps.python.org/pep-0008/), la cual establece las buenas prácticas (obligatorias en este curso) para mejorar la legibilidad y darle consistencia al código.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.1 - Variables

    En Python, la asignación de un dato a una variable **no** requiere la indicación explícita del *tipo de dato*.

    **Nota**: Esto es conocido como lenguaje "dinámicamente tipado", que comprueba el tipo de dato en tiempo de ejecución.

    Por tanto, basta con escribir lo siguiente para asignar números o caracteres o cualquier otro objeto de Python a una variable:
    """)
    return


@app.cell
def _():
    number = 12
    string = 'hola'
    n1, n2, n3 = (1, 2, 3)
    print(number, string, n1 + n2 + n3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.2 - Valores _booleanos_ y comparaciones

    Los dos valores lógicos (_booleanos_) en Python son `True` (o `1`) y `False` (o `0`), sobre los cuales se aplican las operaciones lógicas `or`, `and` y `not`.
    """)
    return


@app.cell
def _():
    i = True and (not False)
    j = 0 or 0 or (not 0)
    print(i, j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Comparaciones entre números

    La evaluación de las comparaciones retorna `True` o `False`.

    | Operación   | Significado                 |
    |-------------|-----------------------------|
    |     `<`     | es estrictamente menor que  |
    |     `<=`    | es menor o igual que        |
    |     `>`     | es estrictamente mayor que  |
    |     `>=`    | es mayor o igual que        |
    |     `==`    | es igual a                  |
    |     `!=`    | no es igual a               |
    |     `is`    | identidad                   |
    |   `is not`  | identidad negada            |

    **Nota 1**: `=` es de asignación, `==` es de comparación.

    **Nota 2**: las operaciones pueden concatenarse, por ejemplo: `x < y < z`
    """)
    return


@app.cell
def _():
    print(12 < 24)
    print(2023 != 2024)
    print(34 >= 21 > 13 > 8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.3 - Tipos de datos numéricos y sus operadores

    En Python hay tres tipos distintos de datos numéricos:

    * `int`: número entero, positivo o negativo
    * `float`: número de punto flotante (decimal) positivo o negativo
    * `complex`: números con una "parte real" y una "parte imaginaria" de punto flotante

    **Nota 1**: Las funciones respectivas `int()`, `float()` y `complex(a, b)` permiten convertir de un tipo a otro.

    **Nota 2**: La función `type()` permite corroborar el tipo de dato numérico o de cualquier dato de una variable en Python.
    """)
    return


@app.cell
def _():
    # Definición
    n_int = 2
    print(n_int, 'es', type(n_int))
    n_float = 3.0
    print(n_float, 'es', type(n_float))
    n_complex = 5 + 8j
    print(n_complex, 'es', type(n_complex))

    # Conversión de tipo de dato
    new_int = int(n_float)
    new_float = float(n_int)
    new_complex = complex(new_int, new_float)
    print(new_int, new_float, new_complex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operaciones básicas sobre datos numéricos

    | Operación         | Resultado                         |
    |-------------------|-----------------------------------|
    | `x + y`           | suma de `x` y `y`                 |
    | `x - y`           | resta de `x` y `y`                |
    | `x * y`           | producto de `x` y `y`             |
    | `x / y`           | cociente de `x` y `y`             |
    | `x // y`          | piso del cociente de `x` y `y`    |
    | `x % y`           | residuo de `x / y`                |
    | `-x`              | `x` negativo                      |
    | `+x`              | `x` sin cambio de signo           |
    | `abs(x)`          | magnitud de `x`                   |
    | `int(x)`          | `x` convertido a entero           |
    | `float(x)`        | `x` convertido a punto flotante   |
    | `complex(re, im)` | número complejo                   |
    | `c.conjugate()`   | conjugado del número complejo `c` |
    | `divmod(x, y)`    | el par `(x // y, x % y)`          |
    | `pow(x, y)`       | `x` a la potencia de `y`          |
    | `x ** y`          | `x` a la potencia de `y`          |
    """)
    return


@app.cell
def _():
    print(10 / 3)
    print(10 // 3)
    print(10 % 3)
    m, n = divmod(10, 3)
    print(m, n, 3 * m + n)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.4 - Números binarios, octales, hexadecimales y sus operaciones

    Para declarar un número **binario** se inicia con `0b`, para declarar un número **octal** se inicia con `0o`, para declarar un número **hexadecimal** se inicia con `0x`. Para convertir entre un tipo y otro y también `int` se utilizan las funciones `bin()`, `oct()`, `hex()` e `int()`.
    """)
    return


@app.cell
def _():
    a = 42
    b = 2020
    c = 25
    print(bin(a))
    print(hex(a))
    print(int(b))
    print(int(c))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operaciones binarias (bit a bit) sobre números enteros

    | Operación   | Resultado                       |
    |-------------|---------------------------------|
    | `x [barra] y`^    | **OR** de `x` y `y`                 |
    | `x ^ y`     | **XOR** de `x` y `y`                |
    | `x & y`     | **AND** de `x` y `y`                |
    | `x << n`    | Desplazamiento izquierdo de `x` en `n` bits        |
    | `x >> n`    | Desplazamiento derecho de `x` en `n` bits |
    | `~x`        | **NOT** (inversión) de `x`          |

    ^ `[barra]` es |
    """)
    return


@app.cell
def _():
    a = 21 & 10
    b = ~a
    c = 13 | 21
    d = 74 << 2
    print(a, b, c, d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.5 - Tipos de secuencias de datos y sus operadores

    Las variables del tipo "secuencia" permiten almacenar **grupos de datos**. También son llamados "contenedores".

    En Python hay varios tipos:

    * `list`: secuencia **mutable** (*que puede cambiar*) típicamente utilizada para almacenar elementos *homogéneos* (de un mismo tipo de datos o secuencias).
    * `tuple`: secuencia **inmutable** (*que **no** puede cambiar*) típicamente utilizada para almacenar elementos *heterogéneos* (de diferente tipo).
    * `range`: secuencia **inmutable** de **números** típicamente utilizada para iterar en un bucle.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.5.1 Cómo crear secuencias

    #### 0.5.1.1 Creación de listas

    Todas estas opciones crean listas:

    * `[]` (lista vacía)
    * `[a]`, `[a, b, c]`
    * `[x for x in iterable]` (*list comprehension*)
    * `list()` o `list(iterable)`

    **Nota**: Como en algunos lenguajes de computación científica (Matlab, R...), las listas pueden ser utilizadas para crear "vectores" y "matrices".
    """)
    return


@app.cell
def _():
    L1 = ['ha']
    L2 = L1 * 3
    L3 = ['alpha', 'beta', 'gamma']
    L4 = [x for x in range(6)]
    L5 = [x for x in range(6) if x % 3 != 0]
    L6 = [[1,2,3],[4,5,6],[7,8,9]]

    print(L1, L2, L3)
    print(L4)
    print(L5)
    print(L6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 0.5.1.2 Creación de tuplas

    * `()` (tupla vacía)
    * `a`, o `(a,)`
    * `a, b, c` o `(a, b, c)`
    * `tuple()` o `tuple(iterable)`
    """)
    return


@app.cell
def _():
    T1 = (1,)
    T2 = 1, 2, 3
    T3 = ('In', 'a', 'galaxy', 'far', 'far', 'away')
    T4 = tuple([x for x in range(3)])

    print(type(T1))
    print(T2, T3, T4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 0.5.1.3 Creación de rangos

    * `range(stop)` (empieza en 0 y **no** incluye a `stop`)
    * `range(start, stop[, step])` (como en `start:step:stop`)
    """)
    return


@app.cell
def _():
    range(1000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.5.2 Operaciones sobre secuencias

    | Operación              | Resultado                                                                                         |
    |------------------------|---------------------------------------------------------------------------------------------------|
    | `x in s`               | `True` si un elemento de `s` es igual a `x` , de lo contrario `False`                             |
    | `x not in s`           | `False` si un elemento de `s` es igual a `x` , de lo contrario `True`                             |
    | `s + t`                | la concatenación de `s` y `t`                                                                     |
    | `s * n` o `n * s`      | equivalente a agregar `s` a sí mismo `n` veces                                                    |
    | `s[i]`                 | `i`-ésimo elemento de `s` , origen en 0                                                          |
    | `s[i:j]`               | rebanada de `s` de `i` a `j`                                                                      |
    | `s[i:j:k]`             | rebanada de s de `i` a `j` con el paso `k`                                                        |
    | `len(s)`               | longitud de `s`                                                                                   |
    | `min(s)`               | elemento más pequeño de `s`                                                                       |
    | `max(s)`               | elemento más grande de `s`                                                                        |
    | `s.index(x[, i[, j]])` | índice de la primera aparición de `x` en `s` (en o después del índice `i` y antes del índice `j`) |
    | `s.count(x)`           | número total de ocurrencias de `x` en `s`                                                         |

    **Nota**: La forma "pitónica" de acceder al último elemento de la secuencia es con el índice `-1`, es decir, `s[-1]`. De esta forma no hay que conocer *a priori* la cantidad de elementos en `s`.
    """)
    return


@app.cell
def _():
    start = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    continuation = 55, 89, 144, 233
    sequence = start + continuation

    print(sequence)
    print(sequence[4])
    print(sequence[0:-1:2])
    print(sequence.count(1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.5.3 Operaciones sobre secuencias *mutables*

    | Operación             | Resultado                                                                                 |
    |-----------------------|-------------------------------------------------------------------------------------------|
    | `s[i] = x`            | el elemento `i` de `s` se reemplaza por `x`                                               |
    | `s[i:j] = t`          | una porción de `s` de `i` a `j` se reemplaza por el contenido de la `t` iterable          |
    | `del s[i:j]`          | igual que `s[i:j] = []`                                                                   |
    | `s[i:j:k] = t`        | los elementos de `s[i:j:k]` son reemplazados por los de `t`                               |
    | `del s[i:j:k]`        | elimina los elementos `s[i:j:k]` de la lista                                              |
    | `s.append(x)`         | agrega `x` al final de la secuencia (igual que `s[len(s):len(s)] = [x]`)                 |
    | `s.clear()`           | elimina todos los elementos de `s` (igual que `del s[:]`)                                |
    | `s.copy()`            | crea una copia superficial de `s` (igual que `s[:]`)                                      |
    | `s.extend(t) o s += t`| extiende `s` con el contenido de `t` (en su mayor parte igual que) `s[len(s):len(s)] = t` |
    | `s *= n`              | actualiza `s` con su contenido repetido `n` veces                                         |
    | `s.insert(i, x)`      | inserta `x` en `s` en el índice dado por `i` (igual que ) `s[i:i] = [x]`                  |
    | `s.pop([i])`          | recupera el elemento en `i` y también lo elimina de `s`                                   |
    | `s.remove(x)`         | eliminar el primer elemento de `s` donde `s[i]` es igual a `x`                            |
    | `s.reverse()`         | invierte los elementos de `s` en su lugar                                                 |
    """)
    return


@app.cell
def _():
    phrase = ['all', 'you', 'need', 'is', 'love']
    print(phrase)

    need = 'food'
    phrase[-1] = need
    print(phrase)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.6 - Secuencias de texto (*strings*) y sus operadores

    Las "cadenas" de texto o *strings* `str` son secuencias inmutables de caracteres alfanuméricos.

    ### 0.6.1 Creación de secuencias de texto

    * `'hola'` (puede tener comillas dobles adentro)
    * `"hola"` (puede tener comillas sencillas adentro)
    * `'''hola'''` u `\"\"\"hola\"\"\"` (múltiples líneas)
    * Con la función `str()` a partir de otro tipo de dato

    **Nota**: Las secuencias de texto permiten todas las operaciones aplicadas sobre secuencias, pero es inmutable entonces no admite las operaciones sobre secuencias mutables (como las sustituciones o la remoción de elementos).
    """)
    return


@app.cell
def _():
    print('Hello "world"' + ", " + '''greetings.''')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.6.2 Algunas funciones ("métodos") sobre hileras de caracteres

    Es posible hacer operaciones específicas de texto sobre un `str`. La lista completa de métodos está disponible [aquí](https://docs.python.org/3/library/stdtypes.html#string-methods).

    * `str.capitalize()`: Regresa una copia de la cadena con su primer carácter en mayúscula y el resto en minúscula.
    * `str.endswith( sufijo [ , inicio [ , fin ] ] )`: Regresa `True` si la cadena termina con el sufijo especificado, de lo contrario regresa `False`.
    * `str.lower()`: Regresa una copia de la cadena con todos los caracteres en mayúsculas convertidos a minúsculas.
    """)
    return


@app.cell
def _():
    text = 'hElLo, gOoD mOrnInG'

    print(text)
    print(text.capitalize())
    print(text.lower().endswith('ing'))
    print(text.upper())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.6.3 Dar formato al texto al imprimir

    Un [método](https://docs.python.org/3/library/string.html#formatstrings) importante aplicado en hileras de caracteres permite insertar valores en un texto, con ciertas especificaciones.

    * `str.format(*args, **kwargs)`: Realiza una operación de formateo de la cadena. La cadena para la que se llama a este método puede contener texto literal o **campos de reemplazo** delimitados por llaves `{}`. Cada campo de reemplazo contiene el índice numérico de un argumento posicional o el nombre de un argumento de palabra clave. `str.format` devuelve una copia de la cadena donde cada campo de reemplazo se reemplaza con el valor de cadena del argumento correspondiente.

    **Nota 1**: `*args` es un número variable de argumentos que se pasan a una función. Por ejemplo, una función `multiplicar(*args)` que multiplica todos los argumentos que se le pasan puede ser `multiplicar(3,3,2,7)` o `multiplicar(2,3)`. Los `*args` son _posicionales_, es decir, deben estar en el orden exacto en el que los requiere la función. Por ejemplo:

    ```python
    c = dividir(a, b)
    # c = a/b
    ```

    **Nota 2**: ``**kwargs`` es un número variable de argumentos del tipo `clave=argumento`. Los `**kwargs` no son posicionales, pueden ser ingresadas en cualquier posición.

    ```python
    c = dividir(den=b, num=a)
    # c = a/b
    ```

    #### Recomendación: *f-strings*

    Una sintaxis alternativa para incorporar variables en un texto es por medio de la notación de *f-strings*, que es del tipo:

    ```python
    a = 1600
    texto = f'En los años {a}...'
    ```
    """)
    return


@app.cell
def _():
    word = 'world'
    x, y = (5, 3)
    z = x / y
    w = 1600
    print('Hello {}!'.format(word))
    print('{} entre {} es cerca de {:0.2f}'.format(x, y, z))
    print(f'En los años {w}...')
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.7 - Diccionarios

    Un diccionario es un tipo especial de secuencia mutable que hace un *mapeo* de valores a una clave, del tipo `clave: valor` (usualmente en inglés como `key: value`). El nombre es una analogía con los diccionarios que tienen pares **palabra: definición**.

    ### 0.7.1 Creación de diccionarios

    * Los diccionarios se pueden crear colocando una lista de pares separados por comas entre llaves `{}`.
    * Con el constructor `dict()`.

    **Nota**: El orden de los pares no importa. Si dos o más diccionarios comparten exactamente los mismos pares (aunque hayan sido creados en diferente orden) entonces son iguales.
    """)
    return


@app.cell
def _():
    # Con las llaves
    a = {'uno': 1, 'dos': 2, 'tres': 3}
    b = dict(uno=1, dos=2, tres=3)

    # Con la función dict()
    c = dict(zip(['uno', 'dos', 'tres'], [1, 2, 3]))
    d = dict([('dos', 2), ('uno', 1), ('tres', 3)])

    # Con la función zip() que "parea" dos listas
    e = dict({'tres': 3, 'uno': 1, 'dos': 2})
    print(a == b == c == d == e)

    # Con una lista de tuplas (distinto orden)
    # Creación redundante, con dict({})
    # Verificar igualdad
    # Mostrar alguno de los diccionarios
    print(c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.7.2 Algunas funciones útiles en diccionarios

    * `list(d)`: Regresa una lista de todas las claves utilizadas en el diccionario `d`.

    * `len(d)`: Regresa el número de elementos en el diccionario `d`.

    * `d[key]`: Regresa el artículo de `d` con la clave `key`. Genera una clave `KeyError` si no está en el mapa (diccionario).
    """)
    return


@app.cell
def _():
    d = {'IE0247': 'Señales y Sistemas I', 'IE0347': 'Señales y Sistemas II', 'IE0405': 'Modelos Probabilísticos de Señales y Sistemas'}
    print(list(d))
    print(len(d))
    print(d['IE0405'])
    print('MA1001' in d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.8 - Controles de flujo

    Los controles de flujo determinan las acciones del programa ante la evaluación de "declaraciones" tales como comparaciones. La documentación [oficial](https://docs.python.org/3/tutorial/controlflow.html) explica sus detalles.

    ### 0.8.1 Controles de flujo `if` - `elif` - `else`

    Posiblemente el más importante o conocido, `if` evalúa una declaración y prosigue con líneas de ejecución distintas según el resultado. En Python su sintaxis es:

    ```python
    if <declaracion>:
         <accion cuando es verdadero>
    ```

    Cuando el resultado es `False` puede haber otra acción posible, y la sintaxis es:

    ```python
    if <declaracion>:
        <accion cuando es verdadero>
    else:
        <accion cuando es falso>
    ```

    Si al evaluarse la primera declaración hay otras posibilidades entonces deben evaluarse otras declaraciones con la sintaxis:

    ```python
    if <declaracion_1>:
        <accion cuando 1 es verdadero>
    elif <declaracion_2>:
        <accion cuando 1 es falso y 2 es verdadero>
    else:
        <accion cuando 1 y 2 son falsos>
    ```

    **Nota**: la *indentación* es **obligatoria** en Python, y es también suficiente para delimitar qué está contenido dentro de un curso de acción. Por ejemplo, en el siguiente fragmento, `print(a)` está dentro del `if` y `print(b)` no.

    ```python
    if a < b:
        print(a)

    print(b)
    ```

    **Nota**: este ejemplo incluye una **librería** de Python (`datetime`) para conocer la hora actual. El uso e importación de librerías es presentado en `Py1`.
    """)
    return


@app.cell
def _():
    import datetime

    # Hora actual
    H = datetime.datetime.now().hour

    # Saludo según la hora del día
    if H < 12:
        print('Buenos días')
    elif H < 18:
        print('Buenas tardes')
    else:
        print('Buenas noches')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.8.2 Controles de flujo `try` - `except` para manejo de errores

    Python termina la ejecución de un programa cuando encuentra un error. Esto a diferencia de un lenguaje compilado (como C y C++) que no ejecutan el programa hasta descartar errores en una compilación previa.

    A menudo es necesario evitar que el programa **no** se detenga cuando hay un error. Cuando una instrucción puede contener un error con cierta probabilidad, es posible hacer una prueba con la instrucción `try`.

    El comando `except` permite actuar en caso de error.

    Otras opciones con `else` y `finally` pueden encontrarse [aquí](https://www.w3schools.com/python/python_tryexcept.asp).
    """)
    return


@app.cell
def _(x):
    # x = 3

    # Si la definición de x está "comentada"
    try:
        print(f'La variable sí existe y es {x}.')
    except:
        print('¡Suave! La variable no existe')

    # Ahora se puede probar "descomentando" x
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.8.3 Control de flujo `match - case`

    Una alternativa para usar una lógica `if` en el caso en que hay varias opciones posibles, es la comparación de una variable de interés con sus valores posibles y ejecutar acciones para cada caso, como:

    ```python
    match variable:
        case "a":
            print("It's a!")
        case "b":
            print("It's b!")
        case "c":
            print("It's c!")
        case _:
            print("It was something else")
    ```
    """)
    return


@app.cell
def _():
    variable = "a"

    match variable:
        case "a":
            print("It's 'a'!")
        case "b":
            print("It's 'b''!")
        case "c":
            print("It's 'c'!")
        case _:
            print("It was something else")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.9 - Bucles

    Un tipo especial de controles de flujo son los que **repiten** una acción en "bucle" o "lazo" (*loop*).

    ### 0.9.1 Bucle `while`

    Repite una operación **indefinidamente** mientras una condición se cumpla.

    ```python
    while <declaracion>:
        <accion siempre que sea verdadero>
    ```

    ### 0.9.2 Bucle `for`

    Repite una operación por **un número determinado de veces**, al iterar *sobre* una secuencia de datos.

    ```python
    for i in (a, b, c, d, e, f):
        <accion para i = a, luego i = b, despues i = c...>
    ```

    **Nota 1**: la secuencia `range()` es útil cuando se quiere iterar sobre una larga consecución de números (por ejemplo, desde 10 hasta 100).

    **Nota 2**: El operador `a += n` es equivalente a `a = a + n`. También existen `-=` y `*=`.
    """)
    return


@app.cell
def _():
    print('Primero:')
    i = 1
    while i % 5 != 0:
        print(i)
        i += 1

    print('Segundo:')
    for j in (8, 13, 21, 34):
        print(j)

    print('Tercero:')
    for k in range(5):
        print(k)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Otros comandos especiales

    * `break`: Sale del ciclo actual.
    * `yield`: Continúa con la siguiente iteración del bucle.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.10 - Algunas funciones nativas

    Ya son conocidas algunas funciones de la [Librería Estándar de Python](https://docs.python.org/3/library/functions.html) como `print()`, `type()`, `int()`, `len()`, `list()`. Algunas otras funciones útiles de interés son:

    * `abs(a)`: Valor absoluto de un número.
    * `all()`: `True` si todos los elementos de una secuencia son `True`.
    * `enumerate(iterable[, start=n])`: "adhiere" numeración a una secuencia iterable, empezando en `start=n` (por defecto `start=0`).
    * `help()`: Invoca la ayuda de un objeto (función o comando o variable).
    * `input([prompt])`: Habilita el ingreso de datos con un texto `[prompt]` cuando el programa es ejecutado en una terminal de comandos o aquí en Jupyter también.
    * `map(función, iterable)`: Aplica la `función` sobre cada elemento de `iterable`.
    * `round(n[, dígitos])`: Redondea `n` con una precisión de `dígitos`.
    * `zip(*iterables)`: Crea un nuevo iterador con la unión de tantos `*iteradores` como se agreguen. El `i`-ésimo elemento de `zip(*iterables)` es una tupla con los `i`-ésimos elementos de cada argumento iterable.

    **Nota**: Jupyter algunas veces no despliega el ingreso de datos. Para eso puede probar en el menú Kernel > Restart (se borrarán las variables almacenadas).
    """)
    return


@app.cell
def _():
    name = input('Digite su nombre: ')

    print('Hi {}.'.format(name))
    print('This is the help for function "abs":\n')
    help(abs)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### ¡Esto es todo por ahora!

    Los conceptos vistos hasta ahora en Py0 son poderosos y permiten la programación de soluciones para una gran cantidad de problemas computacionales. Aun en tareas mucho más complejas en el futuro, estas bases seguirán siendo esenciales.

    Sin embargo, el verdadero secreto de Python son los muchos paquetes que le dan "poderes especiales" para casi todo tipo de asignaciones, desarrollados por una comunidad activa alrededor del mundo.

    El resto de los PyX serán una guía introductoria para algunas de estas herramientas en [computación científica](https://es.wikipedia.org/wiki/Computaci%C3%B3ncient%C3%ADfica).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Filosofía de Python

    *Tim Peters*

    Este "zen" es una colección de principios de programación (¿o de vida?) que guían las buenas prácticas en Python.

    - Bello es mejor que feo.
    - Explícito es mejor que implícito.
    - Simple es mejor que complejo.
    - Complejo es mejor que complicado.
    - Plano es mejor que anidado.
    - Disperso es mejor que denso.
    - La legibilidad importa.
    - Los casos especiales no son tan especiales como para quebrantar las reglas.
    - Lo práctico gana a lo puro.
    - Los errores nunca deberían dejarse pasar silenciosamente.
    - A menos que hayan sido silenciados explícitamente.
    - Frente a la ambigüedad, rechace la tentación de adivinar.
    - Debería haber una —y preferiblemente solo una— manera obvia de hacerlo.
    - Aunque esa manera puede no ser obvia al principio a menos que usted sea holandés.
    - Ahora es mejor que nunca.
    - Aunque nunca es a menudo mejor que ya mismo.
    - Si la implementación es difícil de explicar, es una mala idea.
    - Si la implementación es fácil de explicar, puede que sea una buena idea.
    - Los espacios de nombres (*namespaces*) son una gran idea, ¡hagamos más!

    **Nota**: Un *namespace* es una forma de asegurarse de que no hay nombres de variables o funciones o métodos repetidos entre el *script* y las librerías y módulos utilizados.
    """)
    return


@app.cell
def _():
    # Estos principios están escondidos aquí:
    import this

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Más información

    * [Documentación oficial de Python](https://docs.python.org/3/)
    * [RealPython](https://realpython.com/)
    * [w3schools](https://www.w3schools.com/python/)
    * [Wikibook de Python](https://en.wikibooks.org/wiki/Python_Programming)
    * (...muchas otras referencias en la web y libros...)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **Universidad de Costa Rica** | Facultad de Ingeniería | Escuela de Ingeniería Eléctrica

    &copy; 2020 - 2026

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
