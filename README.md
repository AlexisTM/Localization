# Localization

## Introduction

This library is based out of [kamalshadi/Localization](https://github.com/kamalshadi/Localization).

This fork has the same 2D/3D implementations but aim (not done yet) to provide a 2.5D implementation with one or more axis fixed.

## Installation

The package has been tested with python2.7 and python3.6. Use pip to install the package:

```bash
pip install multilateration
# or before being published on Pypi;
sudo -H python setup.py install
# or for development
pip install -e .
```

## Usage

```python
import multilateration
from math import sqrt

P = multilateration.Project(goal=[None, None, 0.0])
P.add_anchor('anchore_A',(1,0,1))
P.add_anchor('anchore_B',(-1,0,1))
P.add_anchor('anchore_C',(-1,-1,1))

t = P.add_target()
t.add_measure('anchore_A',1)
t.add_measure('anchore_B',1)
t.add_measure('anchore_C',sqrt(2))
P.solve()

print(t.ID, str(t.loc))

```

## Changes from the [original library](https://github.com/kamalshadi/Localization)

The library has been cleaned:

- Remove unused dependencies
- Keep only the LSE method
- Added the 2D5 model
- Removed Earth1 model
