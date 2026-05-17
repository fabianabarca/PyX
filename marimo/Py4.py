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

    # `Py4` - *Introducción al módulo de funciones estadísticas*

    > El módulo **stats** de SciPy ofrece herramientas para manipulación de distribuciones estadísticas. Entre ellas: identificación de parámetros de ajuste para datos, cálculo de probabilidades en un intervalo, graficación de funciones de distribución, generación de datos aleatorios con una distribución particular, etc.

    *Fabián Abarca Calderón*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Módulo `stats`

    ```python
    from scipy import stats
    ```

    > Este módulo contiene una gran cantidad de distribuciones de probabilidad, así como una creciente biblioteca de funciones estadísticas.

    Con más de 100 distribuciones estadísticas diferentes, muy posiblemente la que necesitamos está ahí. Tiene una variedad de:

    * Distribuciones continuas
    * Distribuciones multivariadas
    * Distribuciones discretas
    * Descriptores estadísticos (*summary statistics*)
    * ...

    La documentación oficial está en [Statistical functions (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4.1. - Creación de un "objeto aleatorio"

    Para iniciar la manipulación de las distribuciones, existen *clases* generales de variables aleatorias que son:

    * `rv_continuous`: Una clase de variable aleatoria **continua** genérica.
    * `rv_discrete`: Una clase de variable aleatoria **discreta** genérica.
    * `rv_histogram`: Genera una distribución dada por un histograma.

    (`rv` viene de *random variable*). A su vez, existen **subclases** de estas categorías que representan las distribuciones a utilizar. Por ejemplo:

    ```python
    from scipy import stats

    W = stats.uniform(0,1)  # distribución uniforme
    X = stats.expon(0,1)    # distribución exponencial
    Y = stats.norm(0,1)     # distribución normal
    Z = stats.rayleigh(0,1) # distribución Rayleigh
    ```

    Aquí, `W`, `X`, `Y` y `Z` son objetos que heredan las propiedades de las distribuciones indicadas. También se dice que son una versión "congelada" (*frozen*) de la variable aleatoria.

    La lista completa está en [Statistical functions (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html).
    """)
    return


@app.cell
def _():
    from scipy import stats
    _X = stats.uniform(0, 1)
    print(type(_X))
    return (stats,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4.2. - Generación de datos aleatorios

    A menudo es necesario generar datos aleatorios con una distribución de probabilidad específica. En `stats` el método es `rvs` (de *random variates*), aplicado a un objeto aleatorio predefinido.
    """)
    return


@app.cell
def _(stats):
    _X = stats.uniform(0, 1)
    _a = _X.rvs()
    _b = _X.rvs(5)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4.3. - Funciones de distribución

    Los objetos aleatorios ponen a disposición las dos funciones de distribución asociadas con cada modelo probabilístico.

    Las funciones de distribución son relevantes para el cálculo de probabilidades, cálculo de momentos, y para hacer gráficos, entre otras cosas.

    ### 4.3.1. - Función de densidad de probabilidad

    El método `pdf` entrega la *probability density function* $f_X(x)$, que puede evaluarse para cualquier valor $x$ particular.

    ### 4.3.2. - Función de probabilidad de masa

    El método `pmf` entrega la *probability mass function* $f_X(x) = P_X(x)$ para una variable aleatoria **discreta**, y puede evaluarse en valores $x$ discretos.

    ### 4.3.3. - Función de probabilidad acumulativa

    El método `cdf` entrega la *cumulative distribution function* $F_X(x)$, que puede evaluarse para cualquier valor $x$ particular.

    *Ejemplo*

    Para la distribución [log-normal](https://en.wikipedia.org/wiki/Log-normal_distribution) `stats` [muestra](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html#scipy.stats.lognorm) la siguiente función de densidad de probabilidad:

    $$
    \displaystyle f_X(x,s) = {\frac{1}{s x {\sqrt {2\pi }}}}\ \exp \left(-{\frac {\left(\ln x \right)^{2}}{2 s^{2}}}\right)
    $$

    Una evaluación numérica en $f_X(2,1)$, con parámetro $s = 1$ da como resultado $f_X(2,1) \approx 0.15687$.
    """)
    return


@app.cell
def _(stats):
    _X = stats.lognorm(1)
    _a = _X.pdf(2)
    print(_a)
    Y = stats.norm(0, 1)
    _b = Y.pdf(0)
    c = Y.cdf(0)
    print(_b, c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4.3.4. - Función cuantil

    El método `ppf` entrega la *probability point function* $Q_X(p)$, que puede evaluarse para cualquier valor de probabilidad $0 \leq p \leq 1$.

    La función cuantil es la inversa de la función acumulativa (y por tanto en ocasiones su notación es $F_X^{-1}(p)$) e indica el valor $x$ en el cual $P(X \leq x) = p$. Es útil porque permite saber dónde está el $100p$% de la distribución. $Q_X(0.45)$ se interpreta como "¿en qué valor de $x$ está acumulado el 45% de la probabilidad de la distribución?".

    Se utiliza a menudo al graficar para delimitar apropiadamente el soporte que tiene la curva.

    En el ejemplo a continuación, el 1% de una distribución uniforme entre 0 y 1 claramente está en 0.01, y el 99% en 0.99, pero excepto por este ejemplo, rara vez es tan sencillo saberlo.
    """)
    return


@app.cell
def _(stats):
    import numpy as np
    _X = stats.uniform(0, 1)
    _a = _X.ppf(0.01)
    _b = _X.ppf(0.99)
    print(_a, _b)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 4.3.5. - Función de supervivencia

    El método `sf` entrega la *survival function* $S_X(x)$, que puede evaluarse para cualquier valor $x$ particular.

    La función de supervivencia es el complemento de la función acumulativa,

    $$
    S_X(x) = P(X > x) = 1 - P(X \leq x) = 1 - F_X(x)
    $$
    """)
    return


@app.cell
def _(stats):
    _X = stats.chi(10)
    _a = _X.cdf(3)
    _b = _X.sf(3)
    print(_a, _b, _a + _b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4.4 - Gráficas de las funciones de distribución

    Con la ayuda de Matplotlib es posible y deseable graficar la forma de las funciones de distribución. Por ejemplo, con la función normal y recordando que su distribución está dada por:

    $${\displaystyle f_X(x) = {\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}}$$

    entonces se obtienen las gráficas de la función de densidad y la función acumulativa.
    """)
    return


@app.cell
def _(np, stats):
    import matplotlib.pyplot as plt
    _X = stats.norm(0, 1)
    _x = np.linspace(_X.ppf(0.01), _X.ppf(0.99), 100)
    plt.plot(_x, _X.pdf(_x))
    plt.title('Distribución normal')
    plt.ylabel('$f_X(x)$')
    plt.xlabel('$x$')
    plt.show()
    plt.figure()
    plt.plot(_x, _X.cdf(_x))
    plt.plot(_x, _X.sf(_x))
    plt.title('Distribución normal')
    plt.legend(['$F_X(x)$', '$S_X(x)$'])
    plt.xlabel('$x$')
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4.5 - Modificación de parámetros de la distribución

    Todas las variables aleatorias están definidas por parámetros (con símbolos distintos, como $\lambda$, $\mu$, $\alpha$, etc.). En el módulo `stats`, sin embargo, los parámetros están especificados generalmente como "ubicación" y "escala". Sin cambiar ninguno de estos parámetros, las distribuciones están **normalizadas** o **estandarizadas**. El efecto que tienen los parámetros es:

    * `loc` (*location*) va a desplazar la media de la distribución.
    * `scale` va a "dispersar" la distribución.

    ### 4.5.1 - Ejemplo con la distribución de Rayleigh

    La función de densidad de probabilidad de Rayleigh es

    $${\displaystyle f_X(x) = {\frac {x}{\sigma ^{2}}}e^{-x^{2}/\left(2\sigma ^{2}\right)}}$$

    Para $x \geq 0$. Y normalizada ($\sigma = 1$) es

    $${\displaystyle f_X(x) = {{x}}e^{-x^{2}/2}}$$

    Para modificarlo en `stats` se hace

    * `rayleigh.pdf(x, loc, scale)`, que es equivalente a
    * `rayleigh.pdf(y) / scale` con `y = (x - loc) / scale`

    Es decir,

    $${ \displaystyle f_X(x) = {\frac {(x - \mathsf{loc})}{\mathsf{scale}^2}} e^{\frac{-(x - \mathsf{loc})^{2}}{(2~\cdot~ \mathsf{scale}^2)}} }$$

    Y corresponde en este caso específico que $\sigma$ = `scale`. En ocasiones se utiliza como notación `shift` = `loc` pues es, en efecto, un desplazamiento a $x_0$.
    """)
    return


@app.cell
def _(np, plt, stats):
    locs = range(1, 6)
    scales = range(1, 6)
    plt.figure()
    plt.title('Distribución de Rayleigh con varios parámetros de escala')
    plt.ylabel('$f_X(x)$')
    plt.xlabel('$x$')
    for scale in scales:
        R = stats.rayleigh(0, scale)
        _x = np.linspace(0, 16, 100)
        plt.plot(_x, R.pdf(_x), label='$\\sigma$ = ' + str(scale))
        plt.legend()
    plt.figure()
    plt.title('Distribución de Rayleigh con varios parámetros de ubicación')
    plt.ylabel('$f_X(x)$')
    plt.xlabel('$x$')
    for loc in locs:
        R = stats.rayleigh(loc, 4)
        _x = np.linspace(loc, 20, 100)
        plt.plot(_x, R.pdf(_x), label='$x_0$ = ' + str(loc))
        plt.legend()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4.6. - Cálculo de probabilidades

    Típicamente, el cálculo de probabilidades se hace de dos formas:

    * Con la integración en una región $\mathcal{R}$ de la función de densidad $f_X(x)$.
    * Con la función acumulativa, de la forma $P(a < X < b) = F_X(b) - F_X(a)$.

    ### 4.6.1. - Integración de la función de densidad

    La librería ofrece formas de hacer la integración numérica

    $$
    \int_{\mathcal{R}} f_X(x) ~\mathrm{d}x
    $$

    #### Ejemplo de la probabilidad en una distribución exponencial

    La variable aleatoria exponencial tiene PDF:

    $$
    f_X(x) = \lambda e^{-\lambda x}
    $$

    donde es posible determinar que $E[X] = 1/\lambda$ y también $\sigma_X^2 = 1/\lambda^2$.

    El módulo `integrate` de `scipy` (información [aquí](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html)) realiza integraciones numéricas con distintos métodos, según sean funciones o muestras de datos. El método `quad` realiza integraciones de uso general.
    """)
    return


@app.cell
def _(np):
    from scipy.integrate import quad

    def exponencial(x, lbd):
        return lbd * np.exp(-lbd * _x)
    _a, _ = quad(exponencial, 1, 3, args=0.5)
    _b, _ = quad(exponencial, 4, np.inf, args=0.5)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Alternativamente, con la [función](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapz.html) `trapz` se puede integrar una función $f(x)$ sobre $x$, utilizando así las funciones de densidad de `stats`.

    **Nota**: no confundir `trapz` la integración de `scipy.integrate` con `trapz` la distribución de probabilidad de `scipy.stats`.
    """)
    return


@app.cell
def _(np, stats):
    from scipy import trapz
    _X = stats.expon(0, 1 / 0.5)
    _x = np.linspace(1, 3, 100)
    _a = trapz(_X.pdf(_x), _x)
    _x = np.linspace(4, _X.ppf(0.999), 100)
    _b = trapz(_X.pdf(_x), _x)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### 4.6.2. - Resta de la función de probabilidad acumulativa

    Conociendo que

    $$P(a < X < b) = F_X(b) - F_X(a)$$

    es fácil hacer la evaluación con las herramientas de `stats`.
    """)
    return


@app.cell
def _(np, stats):
    _X = stats.expon(0, 1 / 0.5)
    _a = _X.cdf(3) - _X.cdf(1)
    _b = _X.cdf(np.inf) - _X.cdf(4)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Más información

    * [Statistical functions (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html)
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
