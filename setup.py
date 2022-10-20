"""
A setuptools based setup module.
"""

from setuptools import setup
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md")) as f:
    long_description = f.read()


setup(
    name="sqlalchemy_awesome_pagination",
    version="1.0.3",
    description="Python package for implementing sqlalchemy pagination",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["sqlalchemy_awesome_pagination"],
    author="Ivan Djuraki",
    author_email="ivandjuraki@protonmail.com",
    license="Apache 2.0",
    install_requires=[
        "sqlalchemy>=1.1",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
    ],
)
