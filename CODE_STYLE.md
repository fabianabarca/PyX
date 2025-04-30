# Guía de estilo para el código en Python

![Static Badge](https://img.shields.io/badge/Black-000000)

> [!Note]
> El código de Python utiliza PEP 8 con la versión de [Black](https://black.readthedocs.io/en/stable/).

## Algunos consejos de la *Guía de estilo para código de Python* (PEP 8)

PEP 8 es una guía para que el código escrito en Python tenga una consistencia agradable a la vista. Pueden hacer lectura completa en la página oficial de [PEP 8](https://www.python.org/dev/peps/pep-0008/).

Aquí mostraremos solamente la síntesis de unas cuantas recomendaciones que serán **regla** para el curso.

### Cosas que fastidian (*pet peeves*)

* Evitar espacios en blanco en medio de paréntesis redondos o cuadrados, o llaves.

:white_check_mark: **Correcto**
```python
spam(ham[1], {eggs: 2})
```
:x: ***Incorrecto***
```
spam( ham[ 1 ], { eggs: 2 } )
```

* Evitar espacios en blanco entre una coma final y un paréntesis cerrado siguiente:

:white_check_mark: **Correcto**
```python
foo = (0,)
```
:x: ***Incorrecto***
```
bar = (0, )
```

* Evitar espacios en blanco inmediatamente antes de una coma, punto y coma o dos puntos:

:white_check_mark: **Correcto**
```python
if x == 4: print x, y; x, y = y, x
```
:x: ***Incorrecto***
```
if x == 4 : print x , y ; x , y = y , x
```

* A pesar de lo anterior, en un segmento los dos puntos actúan como un operador binario y debe tener cantidades iguales en ambos lados:

:white_check_mark: **Correcto**
```python
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
```
:x: ***Incorrecto***
```
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

* Evitar espacios en blanco inmediatamente antes del paréntesis abierto que inicia la lista de argumentos de una llamada de función:

:white_check_mark: **Correcto**
```python
spam(1)
```
:x: ***Incorrecto***
```
spam (1)
```

* Evitar espacios en blanco inmediatamente antes del paréntesis abierto que comienza una indexación o corte:

:white_check_mark: **Correcto**
```python
dct['key'] = lst[index]
```
:x: ***Incorrecto***
```
dct ['key'] = lst [index]
```

* Evitar más de un espacio alrededor de un operador de asignación (u otro) para alinearlo con otro:

:white_check_mark: **Correcto**
```python
x = 1
y = 2
long_variable = 3
```
:x: ***Incorrecto***
```
x             = 1
y             = 2
long_variable = 3
```

#### Otras recomendaciones

* Evitar dejar espacios en blanco en cualquier lugar. Debido a que generalmente es invisible, puede ser confuso para algunos editores de texto.

* Siempre rodear estos operadores binarios con un solo espacio a cada lado: asignación (`=`), la asignación aumentada (`+=`, `-=`, etc.), las comparaciones (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), Booleans (`and`, `or`, `not`).

* Si se utilizan operadores con diferentes prioridades, considerar agregar espacios en blanco alrededor de los operadores con las prioridades más bajas:

:white_check_mark: **Correcto**
```python
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
:x: ***Incorrecto***
```
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

* No usar espacios alrededor del signo `=` cuando se usa para indicar un argumento de palabra clave, o cuando se usa para indicar un valor predeterminado para un parámetro de función:

:white_check_mark: **Correcto**
```python
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```
:x: ***Incorrecto***
```
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

* Las declaraciones compuestas (declaraciones múltiples en la misma línea) generalmente no se aconsejan:

:white_check_mark: **Correcto**
```python
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```
:x: ***Incorrecto***
```
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```

### Comentarios

El código, desde un inicio, estará comentado ampliamente.

Los comentarios tendrán el siguiente formato:

* Una línea en blanco encima (excepto si siguen la norma de *docstrings*)
* Un espacio entre \# y la primera letra
* Primera letra mayúscula
* Texto en español con toda la puntuación y acentos necesarios (el código fuente de Python acepta UTF-8, entre otras codificaciones internacionales)

**Ejemplo**

```python
import numpy as np
from scipy import stats

# Número de muestras
N = 500

# ¿Variable aleatoria de la simulación?
X = stats.norm(0, 1)
```
