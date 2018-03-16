'''
Creditos:
Tutorial PyAr http://docs.python.org.ar/tutorial/3/index.html
'''
def fib(n):  # escribe la serie de Fibonacci hasta n
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end = ', ')
        a, b = b, a + b
    print()
      
# Ahora llamamos a la funcion que acabamos de definir:
fib(2000)
