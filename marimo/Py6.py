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

    # `Py6` - *Intercambio de datos con servicios web*

    > Las interfaces de programación de aplicaciones **API** permiten la adquisición y modificación de datos de servidores externos. En el contexto del curso, esta es una herramienta útil para trabajar con la inmensa cantidad de datos disponibles en internet, muchos de los cuales están disponibles en la forma de *RESTful APIs* y son accesibles con Python.

    *Fabián Abarca Calderón*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Servicios web de datos

    Con la filosofía de "datos abiertos" u otras motivaciones similares, existen muchos servicios en internet que ofrecen acceso público a sus datos –de forma gratuita o no, con registro o no– en áreas tan diversas como datos ambientales, datos de gobierno, datos de salud, etc. Algunos ejemplos son:

    - **DataHub**: tiene una gran cantidad de [colecciones](https://datahub.io/collections) de datos incluyendo indicadores económicos, cambio climático, cine y televisión, demografía, fútbol y otros datos de referencia como listas de países, de ciudades, de idiomas, entre otros.
    - **Urban Observatory**: es "la mayor [colección](https://urbanobservatory.ac.uk/) de datos urbanos en tiempo real en el Reino Unido", con más de 50 tipos de datos de sensores, incluyendo calidad del aire, radiación solar, ruido, tiempo atmosférico y tráfico de vehículos y personas.
    - **RECOPE**: tiene algunos [datos](https://datosabiertos.recope.go.cr/servicio-api) de interés relacionados con hidrocarburos, como el precio internacional del petróleo y los precios al consumidor de cada producto comercializado en Costa Rica, esto es, gasolina súper, gasolina plus 91 ("regular"), diesel y keroseno.

    **Nota**: Esta guía está basada en "[Python and REST APIs: Interacting With Web Services](https://realpython.com/api-integration-in-python/)".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 6.1 - API con arquitectura REST

    Una interfaz de programación de aplicaciones (**API**, *Application Programming Interface*) permite operaciones realizadas entre un **cliente** (por ejemplo, un programa en Python) y un **servidor** remoto, en la cual el servidor procesa una **solicitud** (*request*) del cliente relacionada con sus **recursos** (*resources*) y devuelve una **respuesta** (*response*). Esta solicitud puede ser de consulta, creación, actualización o eliminación de datos (**CRUD**, *Create, Read, Update, Delete*), entre otros.

    En este contexto, un "recurso" es un documento con datos identificado por una URL (dirección web).

    #### REST (transferencia de estado representacional)

    > ...es un **estilo de arquitectura de software** que define un patrón para las comunicaciones de cliente y servidor a través de una red. REST proporciona un conjunto de restricciones para que la arquitectura de software promueva el rendimiento, la escalabilidad, la simplicidad y la confiabilidad en el sistema ([Real Python](https://realpython.com/api-integration-in-python/)). Una API web que obedece a las restricciones REST se describe informalmente como **RESTful**. Las API web RESTful generalmente se basan en métodos HTTP para acceder a los recursos a través de *parámetros codificados en URL* y el uso de JSON o XML para transmitir datos ([Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)).

    #### ¿Qué nos permite hacer una API entonces?

    Hay decenas o cientos de servicios disponibles. Ejemplos:

    - Obtener información de la temperatura ambiental medida en una estación cercana
    - Obtener información de música de Spotify
    - Averiguar la ubicación de la Estación Espacial Internacional
    - Predecir datos con algoritmos de inteligencia artificial
    - Conocer datos de terremotos en tiempo real

    Esta [lista](https://github.com/public-apis/public-apis) de API públicos es inmensa.

    ### 6.1.1. Métodos HTTP

    La comunicación entre el cliente y el servidor con una API sucede típicamente vía protocolo **HTTP** (*Hypertext Transfer Protocol*), el cual permite las siguientes solicitudes:

    | Método HTTP | Descripción                                   |
    |-------------|-----------------------------------------------|
    | `GET`       | Extraer un recurso disponible.                |
    | `POST`      | Crear un nuevo recurso.                       |
    | `PUT`       | Actualizar un recurso existente.              |
    | `PATCH`     | Actualizar parcialmente un recurso existente. |
    | `DELETE`    | Eliminar un recurso existente.                |

    Y [otros](https://developer.mozilla.org/es/docs/Web/HTTP/Methods).

    ### 6.1.2. Códigos de estado HTTP

    Las respuestas del servidor a las solicitudes del cliente se dividen en varias categorías:

    | Código | Categoría          |
    |--------|--------------------|
    | 1XX    | Información        |
    | 2XX    | Operación exitosa  |
    | 3XX    | Redireción         |
    | 4XX    | Error del cliente  |
    | 5XX    | Error del servidor |

    Algunos ejemplos típicos son:

    | Código  | Significado             | Descripción                                                    |
    |---------|-------------------------|----------------------------------------------------------------|
    | 200     | `OK`                    | La acción solicitada fue realizada con éxito.                  |
    | 201     | `Created`               | Un nuevo recurso fue creado.                                   |
    | 204     | `No Content`            | La solicitud fue exitosa pero la respuesta no tiene contenido. |
    | 401     | `Unauthorized`          | El cliente no está autorizado a realizar la acción solicitada. |
    | **404** | `Not Found`             | El recurso solicitado no fue encontrado.                       |
    | 500     | `Internal Server Error` | El servidor devolvió un error cuando procesaba la solicitud.   |

    <img src="https://media0.giphy.com/media/jkZtSdwKOx05BOlapR/giphy.gif?cid=ecf05e47zpqivnrg65ywkr5luxl2hqk1n34qzoqbi3rbsg46&rid=giphy.gif&ct=g" width="250">

    La [lista completa](https://es.wikipedia.org/wiki/Anexo:C%C3%B3digos_de_estado_HTTP) es de más de 50 códigos.

    ### 6.1.3. API *endpoints*

    > Una API REST expone un conjunto de **URL públicas** que las aplicaciones clientes utilizan para acceder a los **recursos** de un servicio web. Estas URL, en el contexto de una API, son llamadas ***endpoints*** ([Real Python](https://realpython.com/api-integration-in-python/)).

    ##### Ejemplo de una API hipotética en la UCR

    Supongamos que la Universidad de Costa Rica tuviera una API con la información de los cursos que imparte y sus profesores. Sus *endpoints* podrían ser:

    - URL base:

    ```http
    https://api.ucr.ac.cr/
    ```

    | Método HTTP | *Endpoint*        | Descripción                          |
    |-------------|-------------------|--------------------------------------|
    | `GET`       | `cursos`         | Lista de cursos y sus datos básicos. |
    | `POST`      | `cursos`         | Crear un nuevo curso.                |
    | `GET`       | `cursos/<sigla>` | Información de un curso específico.  |
    | `PUT`       | `cursos/<sigla>` | Actualizar un curso específico.      |
    | `DELETE`    | `cursos/<sigla>` | Eliminar un curso específico.        |
    | `GET`       | `profesores`     | Lista de profesores.                 |

    de modo que la eliminación de un curso específico, por ejemplo, se puede hacer con la URL:

    ```http
    DELETE https://api.ucr.ac.cr/cursos/AB1234
    ```

    *Solicitudes específicas*

    Asumiendo que cada curso tiene la información del código de carrera, se podría hacer una solicitud del tipo

    ```http
    GET https://api.ucr.ac.cr/cursos?carrera=420201
    ```

    que devuelve una lista de los cursos que pertenecen a la carrera de código 420201 (Ingeniería Eléctrica).

    ##### Ejemplo en un navegador y en la terminal de comandos

    Es posible consultar la temperatura en El Cairo con la API de [Open-Meteo](https://open-meteo.com/en/docs), utilizando la URL:

    ```http
    https://api.open-meteo.com/v1/forecast?latitude=30.0571&longitude=31.2272&hourly=temperature_2m
    ```

    de las siguientes formas:

    - En la terminal de comandos (CLI Unix) con `$ curl <URL>`.
    - En la barra de navegación de un navegador cualquiera, ingresando `<URL>` (la información será difícil de leer).
    - Con un cliente API de pruebas en línea, como [ReqBin](https://reqbin.com/).

    Más adelante se estudiará cómo hacer esto con Python de forma programática.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 6.2. Formatos de intercambio de datos

    > ¿Cómo se envía la información de una solicitud, considerando que entre clientes y servidores existe una gran heterogeneidad de lenguajes de programación, sistemas operativos, idiomas, etc.?

    Para esto existen varios formatos usuales, entre ellos **JSON** y **CSV**, que son los más utilizados y casi *de facto*. Pero es posible también utilizar **XML** (*Extensible Markup Language*), **XLSX** (*MS Office Excel*), **ODS** (*OpenDocument Spreadsheet*), **HDF** (*Hierarchical Data Format*), **SHP** (*ESRI Shapefile* para datos espaciales en sistemas de información geográfica) e incluso **DataFrame** de Pandas.

    ### 6.2.1. JSON

    La inmensa mayoría de API ofrecen JSON como uno de sus formatos de descarga.

    > La "notación de objetos de JavaScript" **JSON** (*JavaScript Object Notation*) es un formato ligero de intercambio de datos. Leerlo y escribirlo es simple para humanos, mientras que para las máquinas es simple interpretarlo y generarlo ([JSON.org](https://www.json.org/json-es.html)).

    El formato está [estandarizado](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf): **ECMA-404** *The JSON Data Interchange Standard*.

    #### Cómo crear un objeto

    <img src="https://www.json.org/img/object.png" width="450">

    ##### Ejemplos de objetos JSON

    - En blanco

    ```json
    { }
    ```

    - Un par llave/valor

    ```json
    { "nombre" : "Modelos Probabilísticos de Señales y Sistemas" }
    ```

    - Un conjunto de pares llave/valor

    ```json
    {
        "nombre" : "Modelos Probabilísticos de Señales y Sistemas",
        "sigla" : "IE0405",
        "créditos" : 3,
        "carrera" : 420201
    }
    ```

    #### Cómo crear un arreglo

    <img src="https://www.json.org/img/array.png" width="450">

    El valor (*value*) puede ser una cadena de caracteres con comillas dobles, o un número, o `true` o `false` o `null`, o un objeto o un arreglo. Estas estructuras pueden anidarse ([JSON.org](https://www.json.org/json-es.html)).

    ##### Ejemplos de arreglos JSON

    - Un conjunto de objetos anidados

    ```json
    [
        {
            "nombre" : "Modelos Probabilísticos de Señales y Sistemas",
            "sigla" : "IE0405",
            "créditos" : 3,
            "carrera" : 420201,
            "temas" : {
                "tema_1" : "Introducción a la probabilidad",
                "tema_2" : "Variables aleatorias",
                "tema_3" : "Variables aleatorias múltiples",
                "tema_4" : "Procesos aleatorios",
                "tema_5" : "Cadenas de Markov"
            },
            "obligatorio" : true,
            "laboratorio" : false
        },
        {
            "nombre" : "Circuitos Lineales I",
            "sigla" : "IE0309",
            (...)
        }
    ]
    ```

    #### Librería `json`

    Python provee herramientas para manipular estructuras de datos y convertirlos a o desde JSON. El formato de JSON es similar a la de un diccionario de Python (un rasgo de sintaxis que comparte con JavaScript).
    """)
    return


@app.cell
def _():
    import json
    _d = {'título': 'Don Quijote de La Mancha', 'autor': 'Miguel de Cervantes'}
    # Crear un diccionario de Python
    _j = json.dumps(_d)
    # Convertir a JSON
    print(_j)
    return (json,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Observar que las tildes se transforman y las comillas simples se convierten en comillas dobles.

    **Nota**: Existen páginas para dar formato a textos JSON, como [JSON Formatter](https://jsonformatter.curiousconcept.com/).

    También es posible convertir un JSON en forma de *string* a un objeto de Python
    """)
    return


@app.cell
def _(json):
    _j = '{ "sigla" : "IE0405" }'
    _d = json.loads(_j)
    print(type(_d))
    print(_d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Observar el cambio de convenciones en las comillas y los espacios alrededor de `:`, `{` y `}`.

    Para introducir *strings* de múltiples líneas con `'''` se hace:
    """)
    return


@app.cell
def _(json):
    _j = '\n    { \n        "nombre" : "Modelos Probabilísticos de Señales y Sistemas",\n        "sigla" : "IE0405",\n        "créditos" : 3,\n        "carrera" : 420201\n    }\n\n'
    _d = json.loads(_j)
    print(type(_d))
    print(_d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Cómo extraer información de JSON

    Debido a que un archivo JSON puede tener estructuras complejas de datos, la indexación para solicitar un dato merece especial cuidado.

    ##### Ejemplo de los datos de cursos de la UCR

    En este ejemplo, el JSON tiene un arreglo con dos objetos: `[ { }, { } ]`, y cada objeto a su vez tiene otros objetos y arreglos anidados. Para extraer, por ejemplo, el `"tema_2"` del curso de Circuitos Lineales I es necesario hacer:
    """)
    return


@app.cell
def _(json):
    _cursos = '\n    [\n        { \n            "nombre" : "Modelos Probabilísticos de Señales y Sistemas",\n            "sigla" : "IE0405",\n            "créditos" : 3,\n            "carrera" : 420201,\n            "temas" : {\n                "tema_1" : "Introducción a la probabilidad",\n                "tema_2" : "Variables aleatorias",\n                "tema_3" : "Variables aleatorias múltiples",\n                "tema_4" : "Procesos aleatorios",\n                "tema_5" : "Cadenas de Markov"\n            },\n            "obligatorio" : true,\n            "laboratorio" : false\n        },\n        { \n            "nombre" : "Circuitos Lineales I",\n            "sigla" : "IE0309",\n            "créditos" : 3,\n            "carrera" : 420201,\n            "temas" : {\n                "tema_1" : "Introducción",\n                "tema_2" : "Análisis de circuitos resistivos",\n                "tema_3" : "Técnicas para el análisis de los circuitos lineales",\n                "tema_4" : "Elementos almacenadores de energía",\n                "tema_5" : "El circuito de primer orden",\n                "tema_6" : "El circuito de segundo orden"\n            },\n            "obligatorio" : true,\n            "laboratorio" : false\n        }\n    ]\n'
    _a = json.loads(_cursos)
    _q = _a[1]['temas']['tema_2']
    print(type(_a))
    print('Tema:', _q)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    donde `[1]` hace referencia al segundo objeto (Circuitos Lineales I) y `['temas']` y `['tema_2']` son los índices o "llaves" en los pares llave/valor (*key/value*) buscados.

    Es posible modificar ligeramente el JSON para hacer la búsqueda más intuitiva, al crear dos objetos identificados por la sigla del curso, de forma tal que la petición es ahora, por ejemplo:

    ```python
    a['IE0405']['temas']['tema_3']
    ```
    """)
    return


@app.cell
def _(json):
    _cursos = '\n    {\n        "IE0405" : { \n            "nombre" : "Modelos Probabilísticos de Señales y Sistemas",\n            "créditos" : 3,\n            "carrera" : 420201,\n            "temas" : {\n                "tema_1" : "Introducción a la probabilidad",\n                "tema_2" : "Variables aleatorias",\n                "tema_3" : "Variables aleatorias múltiples",\n                "tema_4" : "Procesos aleatorios",\n                "tema_5" : "Cadenas de Markov"\n            },\n            "obligatorio" : true,\n            "laboratorio" : false\n        },\n        "IE0309" : { \n            "nombre" : "Circuitos Lineales I",\n            "sigla" : "IE0309",\n            "créditos" : 3,\n            "carrera" : 420201,\n            "temas" : {\n                "tema_1" : "Introducción",\n                "tema_2" : "Análisis de circuitos resistivos",\n                "tema_3" : "Técnicas para el análisis de los circuitos lineales",\n                "tema_4" : "Elementos almacenadores de energía",\n                "tema_5" : "El circuito de primer orden",\n                "tema_6" : "El circuito de segundo orden"\n            },\n            "obligatorio" : true,\n            "laboratorio" : false\n        }\n    }\n'
    _a = json.loads(_cursos)
    _q = _a['IE0405']['temas']['tema_3']
    print('Tema:', _q)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 6.2.2. CSV

    Otro formato popular para intercambio de datos es **CSV** o valores separados por coma (*Comma-Separated Values*). Esto representa a una tabla con columnas y registros y que se escribe de la forma más compacta posible:

    - Cada columna está separada por una coma o tabulación.
    - Cada registro está separado por una nueva línea.

    ##### Ejemplo de información de cursos

    *Como tabla*

    |curso                                        |sigla |créditos|carrera|
    |---------------------------------------------|------|--------|-------|
    |Modelos Probabilísticos de Señales y Sistemas|IE0405|3       |420201 |
    |Circuitos Lineales I                         |IE0309|3       |420201 |
    |Análisis de Sistemas                         |IE0409|3       |420201 |

    *Como CSV*

    ```
    curso,sigla,créditos,carrera
    Modelos Probabilísticos de Señales y Sistemas,IE0405,3,420201
    Circuitos Lineales I,IE0309,3,420201
    Análisis de Sistemas,IE0409,3,420201
    ```

    **Nota 1**: No es posible "anidar" tablas dentro de otras, sino que deben ser planas. CSV, por tanto, no permite estructuras de datos tan complejas como JSON.

    **Nota 2**: Cuando una columna incluye una coma se utilizan comillas alrededor de todo el contenido, por ejemplo:

    ```
    curso,sigla,créditos,carrera
    "Cultura, Sociedad y Economía",CS0605,3,254986
    "Spinoza, Descartes y los Racionalistas",VM0339,3,302145
    ```

    **Nota 3**: Editores de hojas de cálculo como Microsoft Excel, Google Spreadsheets o LibreOffice Calc permiten editar y exportar en CSV pero, por su naturaleza, sin ningún tipo de formato ni fórmulas, solo los valores.

    #### Librería `csv`

    Python también tiene herramientas estándar para crear o leer archivos CSV.
    """)
    return


@app.cell
def _():
    import csv
    from os.path import getmtime
    import time
    _lista = [['curso', 'sigla', 'créditos', 'carrera'], ['Modelos Probabilísticos de Señales y Sistemas', 'IE0405', 3, 420201], ['Circuitos Lineales I', 'IE0309', 3, 420201], ['Análisis de Sistemas', 'IE0409', 3, 420201]]
    # Crear lista con los datos de cursos
    with open('archivo.csv', 'w', newline='') as CSV:
        w = csv.writer(CSV)
        for _i in _lista:
            w.writerow(_i)
    _lapso = time.time() - getmtime('archivo.csv')
    # Crear "archivo.csv" y escribir cada una de las líneas de la lista
    # Prueba de creación de archivo
    print('Archivo fue creado hace {} segundos.'.format(_lapso))
    return getmtime, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Manipulación de CSV con Pandas

    Generalmente será preferible utilizar Pandas para gestionar estos documentos, por la sencillez y versatilidad de sus métodos. Para hacer lo mismo que en el caso anterior:
    """)
    return


@app.cell
def _(getmtime, time):
    import pandas as pd
    _lista = [['curso', 'sigla', 'créditos', 'carrera'], ['Modelos Probabilísticos de Señales y Sistemas', 'IE0405', 3, 420201], ['Circuitos Lineales I', 'IE0309', 3, 420201], ['Análisis de Sistemas', 'IE0409', 3, 420201]]
    # Crear lista con los datos de cursos
    df = pd.DataFrame(_lista)
    df.to_csv('pandas.csv', index=False)
    _lapso = time.time() - getmtime('pandas.csv')
    # Convertir en DataFrame de Pandas
    # Crear archivo "pandas.csv" desde el DataFrame
    # Prueba de creación de archivo
    print('Archivo fue creado hace {} segundos.'.format(_lapso))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 6.3 - Librería `requests`

    Esta es la herramienta de Python más popular para el manejo de API. No es estándar pero, según su documentación,

    > …el módulo `urllib2` que se encuentra en el estándar de Python, ofrece la mayoría de las funcionalidades necesarias para HTTP, pero su API está completamente rota. Fue construida para otra época –y una web diferente–. Requiere una gran cantidad de trabajo (incluso reimplementar métodos) para ejecutar las tareas más sencillas. Las cosas no deberían ser así. No en Python.

    **Nota 1**: La documentación oficial de `requests` está en [https://docs.python-requests.org/](https://docs.python-requests.org/es/latest/).

    **Nota 2**: Es necesario verificar la presencia de la librería `requests` con `$ pip list` e instalar con `$ pip install requests` si no está.

    ##### Ejemplo de datos de usuario en GitHub

    GitHub pone a disposición un API con información de las personas usuarias. Se puede utilizar aquí para demostrar algunas acciones típicas.
    """)
    return


@app.cell
def _():
    import requests
    usuario = 'fabianabarca'
    # Usuario(a) de GitHub
    api_url = 'https://api.github.com/users/' + usuario
    _r = requests.get(api_url)
    # Construir la URL
    datos = _r.json()
    # Hacer la solicitud GET y guardar un "Response" en la variable r
    # Convertir la información obtenida en JSON
    # Extraer y mostrar algún dato particular con la llave "company"
    print('Compañía:', datos['company'])
    return (requests,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para ver toda la información obtenida, basta con hacer

    ```python
    info.json()
    ```

    Otros datos disponibles en este objeto de respuesta son: "login", "url", "name", "bio", de 32 en total.

    ### 6.3.1. *Schemas* y parámetros de solicitudes (*queries*)

    > Al recibir una respuesta de una API con datos, ¿cómo sabemos cuáles categorías están presentes, como en el caso anterior con "login", "url", "name", "bio", "company" y otras?

    Es necesario consultar la documentación de la API, que generalmente tiene un esquema de su información.

    La estructura de una base de datos puede ser descrita formalmente por un *schema* (esquema), que es una especie de mapa de los datos incluidos.

    Por ejemplo, en el caso hipotético de la API de la UCR, se definen los siguientes campos (*fields*) en el *endpoint* `cursos`:

    - "nombre"
    - "sigla"
    - "créditos"
    - "carrera"
    - "temas"
    - "obligatorio"
    - "laboratorio".

    Esta información es importante conocerla de antemano para saber qué encontrar y cómo extraer datos específicos de la respuesta de la API.

    #### Solicitudes de subconjuntos

    Asimismo, las API establecen reglas para la selección de **subconjuntos** (*subsets*) de sus datos, clasificados según alguno o varios parámetros, por ejemplo, según `carrera=420201`, como se vio. Es necesario conocer con cuáles se puede clasificar, pues no son todos, eso depende de cada API. Estas peticiones o *queries* tienen una sintaxis como la de ejemplo:

    ```http
    GET https://api.ucr.ac.cr/cursos?carrera=420201&laboratorio=true
    ```

    que devuelve los cursos que son de la carrera de Ingeniería Eléctrica **y** que son de laboratorio.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6.4 Datos de *Urban Observatory*

    La inmensa cantidad de datos disponible en Urban Observatory de Newcastle University puede ser accesada con su [API](https://newcastle.urbanobservatory.ac.uk/api_docs/). La información es extraída en varios formatos: JSON, CSV, XLSX y otros. Existen las siguientes categorías, o *endpoints*:

    - La URL base:

    ```http
    http://uoweb3.ncl.ac.uk/api/v1.1/
    ```

    | *Endpoint*                   | Descripción                        |
    |------------------------------|------------------------------------|
    | `sensors`                    | Lista de sensores                  |
    | `sensors/types`              | Tipos de sensores                  |
    | `sensors/data`               | Datos crudos de sensores           |
    | `sensors/{sensor_name}`      | Sensores individuales              |
    | `sensors/{sensor_name}/data` | Datos de los sensores individuales |
    | `variables`                  | Nombres de las variables medidas   |
    | `themes`                     | Clasificación temática             |

    Así, por ejemplo, para obtener la lista con la clasificación temática (***themes***) de los sensores utilizados, es necesaria la URL donde está esta información, seguida de la especificación del formato deseado:

    ```http
    GET http://uoweb3.ncl.ac.uk/api/v1.1/themes/json/
    ```

    Implementado con `requests` esto es:
    """)
    return


@app.cell
def _(requests):
    api_url_1 = 'http://uoweb3.ncl.ac.uk/api/v1.1/themes/json/'
    _r = requests.get(api_url_1)
    _r.json()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Ejemplo de solicitud de variables por tema

    Como fue visto antes, es posible hacer solicitudes específicas según categorías, modificando la URL. Por ejemplo, en ***variables***, estos son los datos incluidos (su *schema*):

    ```json
    {
        'Upper Limit': [],
        'Lower Limit': [],
        'Units': [],
        'Name': [],
        'Theme': []
    }
    ```

    Se puede entonces solicitar una respuesta solamente con las variables dentro del tema `Soil`, por ejemplo. Para esto, se debe modificar la URL de la solicitud con los parámetros específicos:

    ```http
    GET http://uoweb3.ncl.ac.uk/api/v1.1/variables/json/?theme=Soil
    ```

    En Python, esto se puede hacer así:
    """)
    return


@app.cell
def _(requests):
    api_url_2 = 'http://uoweb3.ncl.ac.uk/api/v1.1/variables/json/?theme=Soil'
    _r = requests.get(api_url_2)
    _r.json()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### ¿Cuáles subconjuntos se pueden obtener?

    En el ejemplo anterior se obtuvieron resultados de ***variables*** clasificados por ***theme***.

    > Cada API define cuáles subconjuntos se pueden obtener en las solicitudes. Por ejemplo, en Urban Observatory se pueden clasificar sus ***variables*** solamente según ***theme***. Por otra parte, ***sensors*** (que son miles) se puede clasificar por ***sensor_type***, ***theme*** y otros, o una combinación de ellos.

    Con `requests`, es posible solicitar información creando un diccionario de parámetros, lo que simplifica la construcción de la URL.

    ##### Ejemplo de selección de sensores

    Para la selección de sensores la API define los siguientes campos:

    - `sensor_type`
    - `theme`
    - `broker`
    - `polygon_wkb`
    - rectángulo de coordenadas dentro de las que está el sensor
    - región (código postal).

    En el siguiente ejemplo se solicita los sensores de **velocidad del viento**, del tema de **calidad del aire** y del fabricante **AURN Sensor**.
    """)
    return


@app.cell
def _(requests):
    api_url_3 = 'http://uoweb3.ncl.ac.uk/api/v1.1/sensors/json/'
    _parametros = {'sensor_type': 'Wind Speed', 'theme': 'Air Quality', 'broker': 'AURN Sensor'}
    _r = requests.get(api_url_3, _parametros)
    print('La URL consultada es:\n{}'.format(_r.url))
    _r.json()
    return (api_url_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ahora se puede hacer una nueva búsqueda de sensores de **velocidad del viento**, del tema de **calidad del aire** y que están **dentro de un rectángulo de coordenadas** de latitud y longitud (en las cercanías de Newcastle upon Tyne, Inglaterra).
    """)
    return


@app.cell
def _(api_url_3, requests):
    import pprint
    _parametros = {'sensor_type': 'Wind Speed', 'theme': 'Air Quality', 'bbox_p1_x': -1.62, 'bbox_p1_y': 54.9, 'bbox_p2_x': -1.61, 'bbox_p2_y': 55.1}
    _r = requests.get(api_url_3, _parametros)
    print('La URL consultada es:\n{}\n'.format(_r.url))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(_r.json())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6.5. Bonus APIs

    Algunas solicitudes de datos.
    """)
    return


@app.cell
def _(requests):
    _r = requests.get('https://api.chucknorris.io/jokes/random')
    joke = _r.json()['value']
    print('----\nJoke\n----')
    print(joke + '\n')
    word = 'random'
    _r = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
    definition = _r.json()
    print('----------\nDefinition\n----------')
    print('{}: {}\n'.format(word, definition[0]['meanings'][0]['definitions'][0]['definition']))
    api_key = '095Vm6CuWfIGTCfhYyoo4ibDhZGg2Ge6'
    api_url_4 = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key='
    _r = requests.get(api_url_4 + api_key)
    news = _r.json()
    num_results = news['num_results']
    print('----\nNews\n----')
    for _i in range(num_results):
        print('- ', news['results'][_i]['title'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para un chiste desde una terminal Unix (posiblemente haya que instalar `jq`, un procesador de JSON en la línea de comandos):

    ```bash
    curl -s https://api.chucknorris.io/jokes/random | jq -C '.value'
    ```

    o bien

    ```bash
    curl -H "Accept: text/plain" https://icanhazdadjoke.com/
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Más información

    - Documentación de [`requests`](https://docs.python-requests.org/es/latest/)
    - [Urban Observatory](https://newcastle.urbanobservatory.ac.uk/)
    - Herramienta de pruebas de API [ReqBin](https://reqbin.com/)
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
