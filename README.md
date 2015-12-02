SWIG Python wrapper for a few functions in SeqAn.

REQUIREMENTS
============
 - SeqAn 1.4 or later
 - SWIG 2. If you have SWIG 3, there is a branch for that too.

INSTALL
=======
If necessary, edit the `seqan_path` variable in `setup.py` to your SeqAn include folder.

To install system-wide:

python2.7 setup.py install

To install in the current folder:

python2.7 setup.py install --install-lib . 

Remember to add the current folder to your `PYTHONPATH`.

To install to a specific folder, put your destination folder
after the --install-lib option. Remember to add that to your
`PYTHONPATH`

Have fun!
