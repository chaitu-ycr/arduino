from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='arduino_uno_do',
    version='0.0.1',
    description='GUI for controlling arduino UNO IO',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['arduino_uno'],
    package_dir={'': 'src'},
    url='https://github.com/chaitanya-ycr/arduino',
    author='chaitanya reddy y',
    author_email='chaitu.ycr@gmail.com',
    license='MIT',
    keywords='arduino UNO digital output'
)
