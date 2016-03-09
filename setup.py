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
seqan_path = '/usr/include'

# Extension description
_seqanpy = Extension('_seqanpy',
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


setup(name='seqanpy',
      version='0.1',
      author="Fabio Zanini",
      description="""Python wrapper of some SeqAn functions (for now pairwise alignments)""",
      ext_modules=[_seqanpy],
      py_modules=["seqanpy"],

      # metadata for upload to PyPI
      author_email="fabio.zanini@fastmail.fm",
      license="BSD/2-clause",
      keywords="alignment sequence pairwise C++",
      url="https://github.com/iosonofabio/seqanpy",
     )

