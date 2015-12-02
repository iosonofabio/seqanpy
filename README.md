SWIG Python wrapper for a few functions in SeqAn.

REQUIREMENTS
============
 - A C++ compiler
 - [Python](https://www.python.org/) 2.7. Python 3 is not tested but probably trivial to adapt for seqanpy. Open an issue if you need that.
 - [SeqAn](http://www.seqan.de/) 1.4 or later
 - [SWIG](http://www.swig.org/) 2. If you have SWIG 3, there is a branch for that too.

INSTALL
=======
If necessary, edit the `seqan_path` variable in `setup.py` to your SeqAn include folder.

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
