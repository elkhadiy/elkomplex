# Toy implementation of a complex number data type in Python

This module is a basic implementation of complex numbers in Python.
The goal is to demonstrate basic know-how in Python packaging,
project managment, documentation and testing.

This package is not in any way, shape or form suitable for production!

## Install

### Development mode

```Bash
$ git clone https://github.com/elkhadiy/elkomplex
$ cd elkomplex
$ python -m venv .pyenv
$ . .pyenv/bin/activate
$ pip install -e .[dev,test]
```

## Example usage

### Create a complex number from real and imaginary parts

```Python
>>> from elkomplex import Komplex
>>> Komplex.from_cartesian(2, 3)
Komplex(re=2.00, im=3.00, r=3.61, th=0.98)
```

### Create a complex number from polar coordinates

```Python
>>> from math import pi
>>> Komplex.from_polar(1, pi / 4)
Komplex(re=0.71, im=0.71, r=1.00, th=0.79)
```
