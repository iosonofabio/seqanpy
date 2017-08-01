[![Build Status](https://travis-ci.org/iosonofabio/seqanpy.svg?branch=master)](https://travis-ci.org/iosonofabio/seqanpy)
[![PyPI version](https://badge.fury.io/py/seqanpy.svg)](https://pypi.org/project/seqanpy)

Fast pairwise sequence alignment using SeqAn, in Python.

# REQUIREMENTS
 - [Python](https://www.python.org/) 2.7 or 3.3+.
 - A C++ 11 compiler, e.g. GCC 4.8+. If you are using SeqAn 2.2+ (see below), then you need a C++ 14 compiler, e.g. GCC 5.2+.
 - [SeqAn](http://www.seqan.de/) 1.4 or later. If you are using SeqAn 2.2+, then you need a C++ 14 compiler, e.g. GCC 5.2+.
 - [SWIG](http://www.swig.org/) 3 (there is a [branch](https://github.com/iosonofabio/seqanpy/tree/swig2) for SWIG 2)

# INSTALL
Export the environment variable `SEQAN_INCLUDE_PATH` to the parent folder of your seqan include folder. For instance, if your SeqAn headers are in `/usr/local/include/seqan`, set:

```sh
export SEQAN_INCLUDE_PATH=/usr/local/include
```

If your SWIG 3 is not executed by the standard `swig` command, e.g. because it is called `swig3` or because it is not in the `PATH`, just export another environment variable called `SWIG`, e.g.:

```sh
export SWIG=swig3
```

Now you can use one of the following methods to install `seqanpy`.

## Pip
```sh
pip install seqanpy
```

## Setup.py (development version)
Clone the github repo. To install system-wide:

```sh
python2.7 setup.py install
```

To install in the current folder:

```sh
python2.7 setup.py install --install-lib .
```

Remember to add the current folder to your `PYTHONPATH`.

To install to a specific folder, put your destination folder
after the --install-lib option. Remember to add that to your
`PYTHONPATH`

# USAGE
```python
import seqanpy
print(seqanpy.align_global('ACCGGT', 'CCG'))
```
