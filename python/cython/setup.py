from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("cython_mandelbrot.pyx", annotate=True),
    zip_safe=False,
)