# vim: fdm=marker
'''
author:     Fabio Zanini
date:       26/01/14
content:    Setup file for the Python wrapper of SeqAn.
'''
# Modules
from distutils.command import build_ext
from distutils.core import setup, Extension


# Globals
# NOTE: change this folder to your seqanpy include folder
seqan_path = '/usr/include'

# Extension description
class my_build_ext(build_ext.build_ext):
    def find_swig(self):
        import os
        swig_cmd = os.getenv('SWIG')
        if swig_cmd is not None:
            return swig_cmd
        else:
            return build_ext.build_ext.find_swig(self)

seqan_module = Extension('_seqanpy',
                         sources=['seqanpy.i',
                                  'test.cpp',
                                  'align.cpp'],
                         swig_opts = ['-c++',
                                      '-modern',
                                      '-modernargs',
                                      '-keyword',
                                      '-I'+seqan_path],
                         extra_compile_args=['-std=c++11'],
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
      cmdclass={'build_ext': my_build_ext},
     )

