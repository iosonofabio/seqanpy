# vim: fdm=marker
'''
author:     Fabio Zanini
date:       26/01/14
content:    Setup file for the Python wrapper of SeqAn.
'''
# Modules
from distutils.core import setup, Extension


# Globals
# NOTE: change this folder to your seqanpy include folder
seqan_path = '/ebio/ag-neher/share/programs/include'

# Extension description
seqan_module = Extension('_seqanpy',
                         sources=['seqanpy.i',
                                  'test.cpp',
                                  'align.cpp'],
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
       description = """Python wrapper of some SeqAn functions (for now just pairwise alignments)""",
       ext_modules = [seqan_module],
       py_modules = ["seqanpy"],

       # metadata for upload to PyPI
       author_email = "fabio.zanini@tuebingen.mpg.de",
       license = "BSD/2-clause",
       keywords = "alignment sequence pairwise C++",
       url = "http://example.com/HelloWorld/",
       )

