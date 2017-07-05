from distutils.core import setup

from setuptools import find_packages

setup(
    name='benchsuite.rest',
    version='2.0.0-dev12',
    packages=find_packages('src'),
    namespace_packages=['benchsuite'],
    package_dir={'': 'src'},
    url='https://github.com/benchmarking-suite/benchsuite-rest',
    license='',
    author='Gabriele Giammatteo',
    author_email='gabriele.giammatteo@eng.it',
    description='',
    install_requires=['benchsuite.controller', 'flask-restplus', 'benchsuite.core']
)