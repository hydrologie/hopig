import os
from setuptools import find_packages, setup

here = os.path.dirname(__file__)
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


install_requires = [
    "dask[array]",
    "zarr",
]
doc_requires = [
    "sphinx",
    "sphinxcontrib-srclinks",
    "numpydoc",
    "IPython",
    "nbsphinx",
]

extras_require = {
    "complete": ["dask[array]", "zarr", "pyyaml", "fsspec"],
    "docs": doc_requires,
}
extras_require["dev"] = extras_require["complete"] + [
    "pytest",
    "pytest-cov",
    "hypothesis",
    "flake8",
    "black",
    "codecov",
]

setup(
    name="hopig",
    description="HOPIG",
    url="https://github.com/hydrologie/hopig",
    author="Sebastien Langlois",
    author_email="sebastien.langlois62@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["doc", "tests", "tests.*", "doc.*"]),
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
