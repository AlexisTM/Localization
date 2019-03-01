import setuptools
from distutils.core import setup

setup(
    name='Multilateration',
    version='0.1.0',
    author='AlexisTM',
    author_email='alexis.paques@gmail.com',
    packages=['multilateration', 'localization.test'],
    scripts=[],
    url='https://github.com/alexistm/Localization',
    license='LICENSE.txt',
    description='Multilateration library for 3D setups.',
    long_description=open('README.md').read(),
)
