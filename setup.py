#!/usr/bin/env python
import os.path

from setuptools import find_packages, setup


def read(*parts):
    with open(os.path.join(*parts)) as f:
        return f.read().strip()


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3.9",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
]

VERSION = {}
# version.py defines VERSION and VERSION_SHORT variables.
# We use exec here to read it so that we don't import scispacy
with open("rapida/version.py") as version_file:
    exec(version_file.read(), VERSION)

setup(
    name="rapida_python",
    version=VERSION["VERSION"],
    author_email="code@rapida.ai",
    description="rapidaAi sdk to integrate rapida.ai api's",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=classifiers,
    platforms=["POSIX"],
    url="https://github.com/rapidaai/rapida-python",
    packages=find_packages(exclude=["examples", "*.proto"]),
    install_requires=[
        "aiohappyeyeballs==2.6.1; python_version >= '3.9'",
        "aiohttp==3.12.13; python_version >= '3.9'",
        "aiosignal==1.3.2; python_version >= '3.9'",
        "annotated-types==0.7.0; python_version >= '3.8'",
        "attrs==25.3.0; python_version >= '3.8'",
        "frozenlist==1.7.0; python_version >= '3.9'",
        "grpc-interceptor==0.15.4; python_version >= '3.7' and python_version < '4.0'",
        "grpcio==1.72.1; python_version >= '3.9'",
        "grpcio-tools==1.72.1; python_version >= '3.9'",
        "idna==3.10; python_version >= '3.6'",
        "invoke==2.2.0; python_version >= '3.6'",
        "multidict==6.5.0; python_version >= '3.9'",
        "pillow==11.2.1; python_version >= '3.9'",
        "propcache==0.3.2; python_version >= '3.9'",
        "protobuf==6.31.1; python_version >= '3.9'",
        "pydantic==2.11.7; python_version >= '3.9'",
        "pydantic-core==2.33.2; python_version >= '3.9'",
        "setuptools==80.9.0; python_version >= '3.9'",
        "types-protobuf==6.30.2.20250516; python_version >= '3.9'",
        "typing-extensions==4.14.0; python_version >= '3.9'",
        "typing-inspection==0.4.1; python_version >= '3.9'",
        "yarl==1.20.1; python_version >= '3.9'",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "flake8",
            "black",
            "mypy",
        ],
        "grpcio-tools": ["grpcio-tools==1.72.1; python_version >= '3.9'"],
    },
    tests_require=["pytest", "pytest-cov", "flake8", "black", "mypy"],
    package_data={"rapida-python": ["py.typed"]},
    python_requires=">=3.9",
    include_package_data=True,
)