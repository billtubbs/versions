#!/usr/bin/env python
# ----------------- versions.py -----------------
# Convenience script to check versions of python and
# common packages installed in current environment.

# python
from platform import python_version
print('python: %s' % python_version())

if python_version() < '3.6':
    import_exception = ImportError
else:
    import_exception = ModuleNotFoundError

# numpy
try:
    import numpy
    print('numpy: %s' % numpy.__version__)
except (import_exception, AttributeError):
    print('numpy: not installed')

# scipy
try:
    import scipy
    print('scipy: %s' % scipy.__version__)
except (import_exception, AttributeError):
    print('scipy: not installed')

# matplotlib
try:
    import matplotlib
    print('matplotlib: %s' % matplotlib.__version__)
except (import_exception, AttributeError):
    print('matplotlib: not installed')

# pandas
try:
    import pandas
    print('pandas: %s' % pandas.__version__)
except (import_exception, AttributeError):
    print('pandas: not installed')

# statsmodels
try:
    import statsmodels
    print('statsmodels: %s' % statsmodels.__version__)
except (import_exception, AttributeError):
    print('statsmodels: not installed')

# scikit-learn
try:
    import sklearn
    print('sklearn: %s' % sklearn.__version__)
except (import_exception, AttributeError):
    print('sklearn: not installed')

# Tensorflow
try:
    import tensorflow
    print('tensorflow: %s' % tensorflow.__version__)
except (import_exception, AttributeError):
    print('tensorflow: not installed')

# Keras
try:
    import keras
    print('keras: %s' % keras.__version__)
except import_exception:
    print('keras: not installed')

# PyTorch
try:
    import torch
    print('pytorch: %s' % torch.__version__)
except import_exception:
    print('pytorch: not installed')

# opencv
try:
    import opencv
    print('opencv: %s' % opencv.__version__)
except import_exception:
    print('opencv: not installed')

# Gekko (APMonitor.com)
try:
    import gekko
    print('gekko: %s' % gekko.__version__)
except (import_exception, AttributeError):
    print('gekko: not installed')

# Python-Control
try:
    import control
    print('control: %s' % control.__version__)
except (import_exception, AttributeError):
    print('control: not installed')

# gym (Open AI Gym)
try:
    import gym
    print('gym: %s' % gym.__version__)
except import_exception:
    print('gym: not installed')

# Pygame
try:
    import pygame
except ImportError:
    print('pygame: not installed')
else:
    print('pygame: %s' % pygame.__version__)
