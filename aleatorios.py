"""
APA T - 4
Diego Fabelo Marrero

aleatorios.py

El objetivo de este código es la implementación efectiva
de un generador de números pseudoaleatorios basándonos
en el algoritmo de generación lineal congruente (LGC) y
el estándar POSIX.

Test unitarios:
>>> rand = Aleat(m=32, a=9, c=13, x0=11)
>>> for _ in range(4):
...     print(next(rand))
...
16
29
18
15

>>> rand(29)
>>> for _ in range(4):
...     print(next(rand))
...
18
15
20
1

>>> rand = aleat(m=64, a=5, c=46, x0=36)
>>> for _ in range(4):
...     print(next(rand))
...
34
24
38
44

>>> rand.send(24)
38
>>> for _ in range(4):
...     print(next(rand))
...
44
10
32
14

"""
import doctest

class Aleat:
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
       """
       Constructor de la clase Aleat
       Inicializa los parámetros por clave
    
       Tiene como argumentos :
       m -> módulo
       a -> multiplicador
       c -> incremento
       x0 -> semilla
       
       """
       self.m = m
       self.a = a
       self.c = c
       self.x = x0

    def __iter__(self):
       """
        Devuelve el  objeto para usarlo como generador
        
       """
       return self

    def __next__(self):
        """
        Aplica la fórmula LGC para calcular el siguiente valor entero

        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, nSemilla):
        """
        Se reinicia la secuencia con una nueva semilla indicada

        """
        self.x = nSemilla


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función LGC generadora de números aleatorios
    
    """
    x = x0
    while True:
        x = (a * x + c) % m
        recibido = yield x

        if recibido is not None:
            x = recibido


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)