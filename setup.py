#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from glob import glob
import io
from os.path import basename, dirname, join, splitext
import re

from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")).read()


NAME = "flasky"
VERSION = "0.0.1"
LICENSE = "MIT"
DESCRIPTION = "Some description."
README_FILE = "README.rst"
CHANGELOG_FILE = "CHANGELOG.rst"
LONG_DESCRIPTION = "%s\n%s" % (
    re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", read(f"{README_FILE}")),
    re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read(f"{CHANGELOG_FILE}")),
)
AUTHOR = "Mario Mendes"
AUTHOR_EMAIL = "mario@example.com"
URL = f"http://github.com/memjr/{NAME}"
PACKAGES = find_packages("src")
PACKAGE_DIR = {"": "src"}
PY_MODULES = [splitext(basename(path))[0] for path in glob("src/*.py")]
INCLUDE_PACKAGE_DATA = True
ZIP_SAFE = False
CLASSIFIERS = [
    # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    f"License :: OSI Approved :: {LICENSE}",
    "Operating System :: Unix",
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    # uncomment if you test on these interpreters:
    # "Programming Language :: Python :: Implementation :: CPython",
    # "Programming Language :: Python :: Implementation :: PyPy",
    # "Programming Language :: Python :: Implementation :: IronPython",
    # "Programming Language :: Python :: Implementation :: Jython",
    # "Programming Language :: Python :: Implementation :: Stackless",
    "Topic :: Utilities",
]
KEYWORDS = [
    # eg: "keyword1", "keyword2", "keyword3",
]
INSTALL_REQUIRES = [
    "flask",
    "python-dotenv",
]
EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "flake8",
        "isort",
        "mypy",
        "pep8-naming",
        "pip-tools",
        "pre-commit",
        "pydocstyle",
        "pytest",
        "pytest-black",
        "pytest-clarity",
        "pytest-cov",
        "pytest-dotenv",
        "pytest-flake8",
        "pytest-flask",
        "Sphinx",
        "sphinx-rtd-theme",
        "tox",
    ]
}
ENTRY_POINTS = {
    "console_scripts": [
        f"{NAME} = {NAME}.cli:main",
    ]
}


setup(
    name=NAME,
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=PACKAGES,
    package_dir=PACKAGE_DIR,
    py_modules=PY_MODULES,
    include_package_data=INCLUDE_PACKAGE_DATA,
    zip_safe=ZIP_SAFE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    entry_points=ENTRY_POINTS,
)
