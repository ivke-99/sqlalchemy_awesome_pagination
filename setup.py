"""
A setuptools based setup module.
"""

from setuptools import setup, find_packages
from os import path
import re

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md")) as f:
    long_description = f.read()


def find_version(*file_paths):
    """
    Reads out software version from provided path(s).
    """
    version_file = open("/".join(file_paths), 'r').read()
    lookup = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                       version_file, re.M)

    if lookup:
        return lookup.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name="SqlAlchemy Awesome Pagination",
    version=find_version("pagination", "module", "__init__.py"),
    description="Python package for implementing sqlalchemy pagination",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["doc"]),
    include_package_data=True,
    namespace_packages=["pagination"],
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
