# vim: fdm=marker
'''
author:     Fabio Zanini
date:       26/01/14
content:    Setup file for the Python wrapper of SeqAn.
'''
# Modules
from distutils.core import setup, Extension


# Globals
seqan_path = '/ebio/ag-neher/share/programs/include'

# Extension description
seqan_module = Extension('_seqanpy',
                         sources=['seqanpy.i',
                                  'test.cpp',
                                  'align_overlap.cpp'],
                         swig_opts = ['-c++',
                                      '-modern',
                                      '-modernargs',
                                      '-keyword',
                                      '-I'+seqan_path],
                         include_dirs=[seqan_path],
                        )


setup (name = 'seqanpy',
       version = '0.1',
       author      = "Fabio Zanini",
       description = """Python wrapper of some SeqAn functions""",
       ext_modules = [seqan_module],
       py_modules = ["seqanpy"],
       )

