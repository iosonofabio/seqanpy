[![Build Status](https://travis-ci.org/iosonofabio/seqanpy.svg?branch=master)](https://travis-ci.org/iosonofabio/seqanpy)

Fast pairwise sequence alignment using SeqAn, in Python.

REQUIREMENTS
============
 - A C++ 11 compiler, e.g. GCC4.8+. Best with a C++ 14 compiler.
 - [Python](https://www.python.org/) 2.7 or 3.3+.
 - [SeqAn](http://www.seqan.de/) 1.4 or later
 - [SWIG](http://www.swig.org/) 3 (there is a [branch](https://github.com/iosonofabio/seqanpy/tree/swig2) for SWIG 2)

INSTALL
=======
Set (export) the environment variable `SEQAN_INCLUDE_PATH` to the parent folder of your seqan include folder. For instance, if your SeqAn headers are in `/usr/local/include/seqan`, set:

```sh
export SEQAN_INCLUDE_PATH=/usr/local/include
```

To install system-wide:

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

Have fun!
