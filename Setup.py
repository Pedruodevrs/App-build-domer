from setuptools import setup

setup(
    name="domer-lang",
    version="1.0.0",
    description="Interpretador da linguagem DOMER",
    author="Pedruodevrs",
    py_modules=["main"],
    entry_points={
        'console_scripts': [
            'domer=main:run',
        ],
    },
)

