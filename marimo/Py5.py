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

    # `Py5` - *Curvas de ajuste de datos*

    > Los modelos para describir un fenómeno y sus parámetros pueden obtenerse a partir de una muestra de datos. Debido a la gran cantidad de modelos probabilísticos disponibles, a menudo es necesario hacer una comparación de ajuste entre muchas de ellas.

    *Fabián Abarca Calderón* \
    *Jonathan Rojas Sibaja*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5.1. Ajuste de modelo con SciPy/Stats

    Los objetos creados con SciPy/Stats tienen varios métodos, entre ellos:

    | Método                | Descripción                                                 |
    |-----------------------|-------------------------------------------------------------|
    | `rvs()`               | Generador de números aleatorios.                            |
    | `pdf(x)`              | Función de densidad de probabilidad                         |
    | `cdf(x)`              | Función de probabilidad acumulativa                         |
    | `stats(moments=’mv’)` | Media(‘m’), varianza(‘v’), inclinación(‘s’), kurtosis(‘k’). |
    | `fit(data)`           | Estimación de parámetros de mejor ajuste.                   |
    | `median()`            | Mediana de la distribución.                                 |
    | `mean()`              | Media de la distribución.                                   |
    | `var()`               | Varianza de la distribución.                                |
    | `std()`               | Desviación estándar de la distribución.                     |

    La función `fit()`, específicamente, encuentra los parámetros de mejor ajuste para un conjunto de datos provistos.

    #### Ejemplo

    A continuación será generada una distribución exponencial de parámetro $\lambda = 2$ y serán obtenidos los parámetros de mejor ajuste para los datos aleatorios.

    **Nota**: SciPy/Stats no siempre usa los mismos parámetros usuales de la teoría. Ejemplo: en la función exponencial dice:

    > A common parameterization for expon is in terms of the rate parameter lambda, such that pdf = lambda * exp(-lambda * x). This parameterization corresponds to using scale = 1 / lambda.

    Por tanto, en este caso el valor $\lambda$ buscado es `lambda = 1/scale`, y así `scale = 1/lambda = 1/2 = 0.5`, para este ejemplo.
    """)
    return


@app.cell
def _():
    from scipy import stats

    # Crear objeto aleatorio de ejemplo
    X = stats.expon(0, 1/2)

    # Generar números aleatorios a partir de X
    data = X.rvs(400)

    # Estimar parámetros de ajuste de datos aleatorios
    params = stats.expon.fit(data)

    print('Los parámetros son: loc = {}, scale = {}.'.format(params[0], params[1]))
    return (stats,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Es posible observar que el valor de `scale` está razonablemente cerca del valor de 0.5 esperado.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5.2. Paquete `fitter`

    El paquete `fitter` automatiza y simplifica la obtención de modelos de mejor ajuste para un conjunto de datos, utilizando todas las distribuciones de SciPy/Stats disponibles (o algunas, según sea la especificación).

    Sea `data` un conjunto de datos con mediciones numéricas de alguna variable de interés. Con

    ```python
    from fitter import Fitter

    f = Fitter(data)
    f.fit()
    ```

    el programa va a recorrer todas las distribuciones de SciPy/Stats y va a encontrar los parámetros de mejor ajuste.

    **Nota**: Como son muchas distribuciones posibles, esto puede tomar un tiempo considerable.

    Luego, con:

    ```python
    f = Fitter(data, distributions=['expon', 'norm', 'gamma'])
    ```

    es posible limitar el ajuste a solo unas cuantas distribuciones.

    Con:

    ```python
    f.summary()
    ```

    es posible obtener una tabla con el ránking de mejor ajuste (según el criterio de la suma del cuadrado del error) y una gráfica de Matplotlib con el histograma de `data` junto con las curvas de las funciones de densidad (PDF) de las distribuciones de la tabla.

    Para obtener los parámetros de estas distribuciones, estos son accesibles vía:

    ```python
    f.fitted_param
    ```

    que es de la forma:

    ```python
    {'expon': (1.5516548212580765, 3.837313054949372), 'norm': (5.388967876207449, 2.6612762163716237), 'gamma': (2.059695507081982, 1.4639030411838343, 1.9056503608256832)}
    ```

    es decir, un diccionario con el nombre de la distribución y sus parámetros de mejor ajuste. Si es necesario obtener los parámetros de una distribución en específico, es posible escribir, por ejemplo:

    ```python
    f.fitted_param['gamma']
    ```

    y obtener:

    ```python
    (2.059695507081982, 1.4639030411838343, 1.9056503608256832)
    ```

    **Nota**: observar que la cantidad de parámetros varía según la distribución. Además, que los parámetros de SciPy/Stats no son necesariamente los mismos que aparecen en la teoría.

    Incluso, es posible obtener los parámetros de la curva de mejor ajuste indicando solamente:

    ```python
    f.get_best()
    ```

    que devuelve el nombre de la distribución con el mejor ajuste y sus parámetros como un diccionario.

    En el siguiente ejemplo será generada una muestra de 1000 puntos con una distribución de ejemplo, para luego utilizar `fitter`, el cuál revisará las más de 80 distribuciones de SciPy y desplegará un resumen con las distribuciones y sus parámetros.
    """)
    return


@app.cell
def _(stats):
    from fitter import Fitter
    data_1 = stats.gamma.rvs(2, loc=1.5, scale=2, size=1000)
    f = Fitter(data_1, distributions=['expon', 'norm', 'rayleigh', 'uniform'])
    # Crear los datos de ejemplo
    f.fit()
    # Definir cuáles distribuciones va a evaluar
    # Realizar el ajuste para las distribuciones seleccionadas
    # Mostrar principales resultados y gráfica
    f.summary()
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Los parámetros de mejor ajuste de todas las distribuciones utilizadas están en:
    """)
    return


@app.cell
def _(f):
    params_1 = f.fitted_param
    print(params_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5.3. Ajustes polinomiales con el módulo `numpy`

    Aunque no son una distribución de probabilidad propiamente, en ocasiones se pueden utilizar funciones polinomiales genéricas para describir unos datos. Esto puede resultar particularmente útil en distribuciones "multimodales", es decir, que tienen más de una concentración de valores, como la siguiente:

    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e2/Bimodal.png" width="300px">

    Con la función `polyfit()` de la librería `numpy` se puede realizar el ajuste de datos experimentales a polinomios de cualquier orden. Esta función devuelve los parámetros de la recta para un modelo lineal de la forma:

    $$
    f(x) = mx + b
    $$

    Esto en el caso de un polinomio de grado 1. Un ejemplo utilizando este método es el siguiente:
    """)
    return


app._unparsable_cell(
    r"""
    from numpy import *
    import matplotlib.pyplot as plt

    # Datos experimentales
    x = array([ 0.,  1.,  2.,  3.,  4.])
    y = array([ 10.2 ,  12.1,  15.5 ,  18.3,  20.6 ])

    # Ajustar a una recta (polinomio de grado 1)
    p = polyfit(x, y, 1)

    # Crear la recta de ajuste obtenida.
    y_ajuste = p[0]*x + p[1]

    # Graficar los datos experimentales
    p_datos, = plt.plot(x, y, 'b.')

    # Agregar la recta de ajuste
    p_ajuste, = plt.plot(x, y_ajuste, 'r-')

    plt.title('Ajuste lineal por minimos cuadrados')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.legend(('Datos experimentales', 'Ajuste lineal'), loc="upper left")
    plt.show()
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5.4. Métricas de desempeño

    **(Opcional)**

    Para evaluar el ajuste de los modelos probabilísticos, se utilizan típicamente uno o varios de las siguientes indicadores de error.

    En las siguientes definiciones, $\hat{x}$ es el dato pronosticado o valor predicho y $x$ es el dato medido o valor verdadero.

    ### Error máximo

    El error máximo (ME) captura el valor absoluto más alto de error entre todas las predicciones y mediciones.

    \begin{equation}
        \mathrm{ME} = \max_{1 \leq i \leq n} \{ | \hat{x}_i - x_i | \}
    \label{E:me}
    \end{equation}

    ### Error medio absoluto

    El error medio absoluto (MAE) encuentra el promedio de la magnitud del error para cada medición.

    \begin{equation}
        \mathrm{MAE} = \frac{1}{n} \sum_{i = 1}^n | \hat{x}_i - x_i |
    \label{E:mae}
    \end{equation}

    ### Error mediano absoluto

    La mediana del error absoluto (MedAE) encuentra el valor central de los valores ordenados de error para cada medición.

    \begin{equation}
        \mathrm{MedAE} = \mathrm{mediana} (| \hat{x}_1 - x_1 |, \ldots, | \hat{x}_i - x_i |)
    \label{E:medae}
    \end{equation}

    ### Error medio absoluto porcentual

    El error medio absoluto porcentual (MAPE), también llamado el error medio relativo \acrdef{mre}, es una modificación del error medio absoluto que se calcula en términos relativos (porcentuales) al valor verdadero.

    \begin{equation}
        \mathrm{MAPE} = \frac{1}{n} \sum_{i = 1}^n \left| \frac{\hat{x}_i - x_i}{x_i} \right|
    \label{E:mape}
    \end{equation}

    ### Error medio absoluto porcentual simétrico

    El error medio absoluto porcentual simétrico (SMAPE) provee resultados entre 0\% y 200\%.

    \begin{equation}
        \mathrm{SMAPE} = \frac{200\%}{n} \sum_{i = 1}^n  \frac{|\hat{x}_i - x_i|}{|\hat{x}_i| + |x_i|}
    \label{E:smape}
    \end{equation}

    ### Error cuadrático medio

    El error cuadrático medio (MSE) es la media aritmética del cuadrado del error. Penaliza con más rigor los errores grandes que los errores pequeños, según el cuadrado de su magnitud.

    \begin{equation}
        \mathrm{MSE} = \frac{1}{n} \sum_{i = 1}^n ( \hat{x}_i - x_i )^2
    \label{E:mse}
    \end{equation}

    ### Raíz del error cuadrático medio

    La raíz del error cuadrático medio (RMSE) es siempre positiva y menos sensible que MSE a valores atípicamente grandes.

    \begin{equation}
        \mathrm{RMSE} = \sqrt{\frac{1}{n} \sum_{i = 1}^n ( \hat{x}_i - x_i )^2}
    \label{E:rmse}
    \end{equation}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Más información

    * [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
    * [Fitter](https://fitter.readthedocs.io/en/latest/index.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **Universidad de Costa Rica** | Facultad de Ingeniería | Escuela de Ingeniería Eléctrica

    &copy; 2022

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
