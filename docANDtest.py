import doctest

def cuadrado(x):
    """
    Devuelve el cuadrado de un número.
    >>> cuadrado(4)
    16
    >>> cuadrado(-3)
    9
    """

    return x * x


def cubo(x):
    """
    Devuelve el cubo de un número.
    >>> cubo(3)
    27
    >>> cubo(-2)
    -8"""

    return x * x * x


def raiz_cuadrada(x):
    """
    Devuelve la raíz cuadrada de un número.
    >>> raiz_cuadrada(16)
    4.0
    >>> raiz_cuadrada(9)
    3.0
    """

    if x >= 0:
        return x ** 0.5
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."


def raiz_cubica(x):
    """
    Devuelve la raíz cúbica de un número.
    >>> raiz_cubica(27)
    3.0
    >>> raiz_cubica(-8)
    -2.0
    """

    if x >= 0:
        return x ** (1/3)
    else:
        return -(-x) ** (1/3)
    

if __name__ == "__main__":
    doctest.testmod()