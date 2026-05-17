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

    # `Py7` - *Graficación estadística*

    > La visualización de resultados es fundamental en el análisis de datos. Python tiene librerías complementarias como **Matplotlib** y **Seaborn**, entre otras, que ofrecen herramientas avanzadas para muchos tipos de gráficos comúnmente utilizados en muchos contextos académicos y profesionales.

    *Fabián Abarca Calderón*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tipos de gráficos

    Para empezar, haremos un repaso de tipos de gráficos usuales en estadística y análisis de datos.

    [Seaborn](https://seaborn.pydata.org/tutorial/function_overview.html) clasifica sus gráficos de la siguiente forma:

    <img src="https://seaborn.pydata.org/_images/function_overview_8_0.png" width="350">
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Gráficos relacionales

    Mapeo de la relación entre dos variables en un plano cartesiano.

    - **Gráfico de dispersión** (*scatter plot*): diagrama que muestra la relación de dos variables como pares ordenados en un plano cartesiano.

    <img src="https://seaborn.pydata.org/_images/scatterplot_5_0.png" width="300">

    - **Gráfico de línea** (*line chart, line plot*): diagrama que muestra la relación de dos variables como pares ordenados en un plano cartesiano, conectados por una línea para denotar una sucesión.

    <img src="https://seaborn.pydata.org/_images/lineplot_9_0.png" width="300">
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Gráficos de distribución

    Representación de la distribución de un conjunto de valores a lo largo de un eje.

    - **Histograma** (*histogram*): diagrama que agrupa valores numéricos dentro de pequeños rangos de valores (*bins*) y que muestra la distribución del número de veces que aparece un valor dentro de cada intervalo, creando una densidad de probabilidad aproximada.

    <img src="https://seaborn.pydata.org/_images/histplot_1_0.png" width="300">

    - **Gráfico de estimación de densidad kernel** (*KDE plot*): como el histograma, es útil para una estimación de la distribución de ocurrencia de valores muestra, pero mediante la estimación $\hat{f}_h(x)$ de la función de densidad de probabilidad $f_X(x)$, a través de un "[kernel](https://en.wikipedia.org/wiki/Kernel_(statistics))".

    <img src="https://seaborn.pydata.org/_images/kdeplot_5_0.png" width="300">

    - **Función de distribución acumulativa empírica** (*ECDF plot*): es una aproximación de la función de distribución acumulativa (CDF) que representa la proporción o conteo de observaciones ubicadas por debajo de cada valor en un conjunto de datos.

    <img src="https://seaborn.pydata.org/_images/ecdfplot_1_0.png" width="300">

    - **Gráfico de alfombra** (*rug plot*): es una visualización de la distribución marginal de los datos en un eje real, como un gráfico de dispersión unidimensional.

    <img src="https://seaborn.pydata.org/_images/rugplot_1_0.png" width="300">
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Gráficos categóricos

    Representación de la distribución de un conjunto de valores a lo largo de un eje para distintas variables categóricas.

    - **Gráfico de franjas** (*strip plot*): es un diagrama de dispersión donde una variable es categórica.

    <img src="https://seaborn.pydata.org/_images/seaborn-stripplot-2.png" width="300">

    - **Gráfico de enjambre** (*swarm plot*): es un diagrama de dispersión donde una variable es categórica, similar a un gráfico de franjas, pero los puntos no se traslapan.

    <img src="https://seaborn.pydata.org/_images/seaborn-swarmplot-2.png" width="300">

    - **Gráfico de caja o de caja y bigotes** (*box plot*, *box-and-whisker plot*): es una visualización de grupos de datos categóricos por medio de sus *cuartiles*: el mínimo y el mayor valor son los "bigotes", la mediana es la línea dentro de la caja, y el primer cuartil y tercer cuartil son los bordes de la caja. Siguiendo ciertos criterios se excluyen los valores atípicos (*outliers*), aquí mostrados como puntos.

    <img src="https://seaborn.pydata.org/_images/seaborn-boxplot-2.png" width="300">

    - **Gráfico de violín** (*violin plot*): tiene un rol similar al gráfico de caja en mostrar la distribución de datos numéricos por cuartiles en una categoría, pero lo combina con un gráfico KDE para representar además la distribución de ocurrencias.

    <img src="https://seaborn.pydata.org/_images/seaborn-violinplot-2.png" width="300">

    - **Gráfico de punto** (*point plot*): el punto representa la media (u otro estimador) de los datos de una variable categórica y la línea horizontal es un intervalo de confianza para la estimación. Aporta menos información que los gráficos anteriores pero puede ser útil para representar los cambios de las medidas de tendencia central (la media, la mediana o la moda) entre una variable categórica y otra.

    <img src="https://seaborn.pydata.org/_images/seaborn-pointplot-5.png" width="300">

    - **Gráfico de barras** (*bar plot*): muestra una información similar a la del gráfico de punto: la media (u otra medida de tendencia central) y el intervalo de confianza de la estimación, pero la magnitud de la media es una barra.

    <img src="https://seaborn.pydata.org/_images/seaborn-barplot-1.png" width="300">
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Seaborn

    Según su [página oficial](https://seaborn.pydata.org/),

    > Seaborn es una biblioteca de visualización de datos de Python basada en Matplotlib y compatible con las estructuras de datos de Pandas. Proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos e informativos.

    <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" width="350">

    **Nota**: Los aspectos básicos de Matplotlib ya fueron cubiertos en `Py2` y subsiguientes.

    Con los tipos de gráficos mostrados en la sección anterior, Seaborn tiene la posibilidad de configurar una [gran variedad](https://seaborn.pydata.org/examples/index.html) de alternativas. Aquí mostraremos algunos ejemplos básicos.

    Seaborn se importa por convención como

    ```python
    import seaborn as sns
    ```

    A continuación hay algunos ejemplos utilizando conjuntos de datos incluidos con la librería.
    """)
    return


@app.cell
def _():
    # Import seaborn
    import seaborn as sns

    # Apply the default theme
    sns.set_theme()

    # Load an example dataset
    tips = sns.load_dataset("tips")

    # Create a visualization
    sns.relplot(
        data=tips,
        x="total_bill", y="tip", col="time",
        hue="smoker", style="smoker", size="size",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Más información

    * [Página web](https://www.google.com/)
    * Libro o algo
    * Tutorial [w3schools](https://www.w3schools.com/python/)
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
