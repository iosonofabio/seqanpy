SWIG Python wrapper for a few functions in SeqAn.

REQUIREMENTS
============
 - A C++ 11 compiler, e.g. GCC4.8+
 - [Python](https://www.python.org/) 2.7 or 3.
 - [SeqAn](http://www.seqan.de/) 1.4 or later
 - [SWIG](http://www.swig.org/) 2.

INSTALL
=======
If necessary, edit the `seqan_path` variable in `setup.py` to your SeqAn include folder.

To install system-wide:

```sh
python setup.py install
```

To install in the current folder:

```sh
python setup.py install --install-lib .
```

Remember to add the current folder to your `PYTHONPATH`.

You can set the environment variable `SWIG` to your SWIG
executable before installing if you have more than one SWIG
version installed, e.g.:
```sh
SWIG=swig2 python setup.py install
```

To install to a specific folder, put your destination folder
after the --install-lib option. Remember to add that to your
`PYTHONPATH`

Have fun!
