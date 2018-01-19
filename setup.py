from distutils.core import setup
import matcensor.main

setup(
    name='matcensor',
    version=matcensor.main.__version__,
    packages=['matcensor'],
    url='https://github.com/Ar4ikov/matcensore',
    license='Apache 2.0',
    author='Nikita Archikov',
    author_email='bizy18588@gmail.com',
    description='A simple censor checker in string for python (3.5 or newer)',
    keywords='mav, rugaming, python, ar4ikov, censor, matsensor'

)
