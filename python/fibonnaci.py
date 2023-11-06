import functools

import numpy as np


def loop_fibonnaci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a

def recursive_fibonnaci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonnaci(n - 1) + recursive_fibonnaci(n - 2)
    
@functools.lru_cache(maxsize=None)
def memoized_fibonnaci(n):
    if n <= 1:
        return n
    else:
        return memoized_fibonnaci(n - 1) + memoized_fibonnaci(n - 2)

def closed_form_fibonnaci(n):
    from decimal import Decimal
    sqrt5 = Decimal(5).sqrt()
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    return int((phi ** n - psi ** n) / sqrt5)



def matrix_exponentiation_fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = np.array([[1, 1], [1, 0]])
        return np.linalg.matrix_power(matrix, n - 1)[0][0]
    
def time_function(f, n):
    import time
    start = time.time()
    f(n)
    end = time.time()
    return end - start

def display_results(data, title, xlabel, ylabel, legend,loglog=False):
    import matplotlib.pyplot as plt
    if loglog:
        plt.loglog()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        for i in range(len(data)):
            plt.plot(data[i][0], data[i][1], label=legend[i])
        plt.legend()
        plt.show()
    else:
        plt.figure()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        for i in range(len(data)):
            plt.plot(data[i][0], data[i][1], label=legend[i])
        plt.legend()
        plt.show()



def main():
    import numpy as np
    import sys

    # Set the recursion limit to 1000000
    sys.setrecursionlimit(1000000)



    # Plot the time taken for each function on a log-log scale
    # Display each graph on it's own before showing a combined graph

    loop_input = [0,10,100,1000,1000000]
    loop_timings = [time_function(loop_fibonnaci, i) for i in loop_input]
    display_results([(loop_input, loop_timings)], 'Loop Fibonnaci', 'n', 'time', ['loop'])
    recursive_input = [0,10, 20, 30,40]
    recursive_timings = [time_function(recursive_fibonnaci, i) for i in recursive_input]
    display_results([(recursive_input, recursive_timings)], 'Recursive Fibonnaci', 'n', 'time', ['recursive'])
    memoized_input = [0, 10, 100, 1000, 2000]
    memoized_timings = [time_function(memoized_fibonnaci, i) for i in memoized_input]
    display_results([(memoized_input, memoized_timings)], 'Memoized Fibonnaci', 'n', 'time', ['memoized'])
    closed_form_input = [0,10,100,1000,1000000]
    closed_form_timings = [time_function(closed_form_fibonnaci, i) for i in closed_form_input]
    display_results([(closed_form_input, closed_form_timings)], 'Closed Form Fibonnaci', 'n', 'time', ['closed form'])
    matrix_exponentiation_input = [0,10,100,1000,1000000, 1000000000]
    matrix_exponentiation_timings = [time_function(matrix_exponentiation_fibonnaci, i) for i in matrix_exponentiation_input]
    display_results([(matrix_exponentiation_input, matrix_exponentiation_timings)], 'Matrix Exponentiation Fibonnaci', 'n', 'time', ['matrix exponentiation'])

    display_results([(loop_input, loop_timings), (recursive_input, recursive_timings), (memoized_input, memoized_timings), (closed_form_input, closed_form_timings), (matrix_exponentiation_input, matrix_exponentiation_timings)], 'Fibonnaci', 'n', 'time', ['loop', 'recursive', 'memoized', 'closed form', 'matrix exponentiation'])
    # display all results log-log scale
    display_results([(loop_input, loop_timings), (recursive_input, recursive_timings), (memoized_input, memoized_timings), (closed_form_input, closed_form_timings), (matrix_exponentiation_input, matrix_exponentiation_timings)], 'Fibonnaci', 'n', 'time', ['loop', 'recursive', 'memoized', 'closed form', 'matrix exponentiation'], loglog=True)





if __name__ == '__main__':
    main()