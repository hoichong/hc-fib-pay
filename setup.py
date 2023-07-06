from setuptools import find_packages, setup

setup(

    name="hc_fib_pay",

    version="0.0.1",

    author="HC",

    author_email="chonghoiyuen@gmail.com",

    description="Calculates a Fibonacci number",

    long_description="A basic library that calculates Fibonacci numbers",

    long_description_content_type="text/markdown",

    url="https://github.com/hoichong/hc-fib-pay",

    install_requires=[],

    packages=find_packages(exclude=("tests",)),

    classifiers=[

        "Development Status :: 4 - Beta",

        "Programming Language :: Python :: 3",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3',

    tests_require=['pytest'],

)
