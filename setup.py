# vim: fdm=marker
'''
author:     Fabio Zanini
date:       26/01/14
content:    Setup file for the Python wrapper of SeqAn.
'''
# Modules
import os
import sys
from distutils.command import build_ext
from distutils.core import setup, Extension
from distutils.cmd import Command
from distutils.log import INFO as logINFO


# Globals
py_maj = sys.version_info[0]

# Use this env variable to set your SeqAn include folder
seqan_path = os.getenv('SEQAN_INCLUDE_PATH',
                       '/usr/include').rstrip(os.path.sep)
seqan_path = os.path.join(seqan_path, "seqan")
seqan_cpp_std = 'c++11'
if os.path.isdir(seqan_path):
    with open(seqan_path+'/seqan/version.h', 'rt') as f:
        for line in f:
            if 'define SEQAN_VERSION_MAJOR' in line:
                seqan_vma = int(line.rstrip('\n').split(' ')[-1])
            if 'define SEQAN_VERSION_MINOR' in line:
                seqan_vmi = int(line.rstrip('\n').split(' ')[-1])
        if (seqan_vma > 2) or ((seqan_vma == 2) and (seqan_vmi >= 2)):
            print('SeqAn 2.2+ found. Setting C++ standard to c++14.')
            seqan_cpp_std = 'c++14'


class install_seqan(Command):
    '''Install seqan before anything else'''
    description = "check SeqAn installation"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.install_seqan()

    def install_seqan(self):
        from subprocess import check_call
        if py_maj == 2:
            from subprocess import CalledProcessError as SubprocessError
        else:
            from subprocess import SubprocessError

        def c(x): return check_call(x, shell=True)

        def p(x): return self.announce(x, level=logINFO)

        if os.path.isdir(seqan_path+'/seqan'):
            p('SeqAn include folder found. Not installing.')
            return

        raise IOError('SeqAn include folder NOT found. Install it and set the'+
                      ' environment variable SEQAN_INCLUDE_PATH to the parent'+
                      ' of the SeqAn include folder and retry.')


class my_build_ext(build_ext.build_ext):
    def run(self):
        self.run_command('install_seqan')
        build_ext.build_ext.run(self)

    def find_swig(self):
        import os
        swig_cmd = os.getenv('SWIG')
        if swig_cmd is not None:
            return swig_cmd
        else:
            return build_ext.build_ext.find_swig(self)


_seqanpy = Extension('_seqanpy',
                     sources=['seqanpy.i',
                              'test.cpp',
                              'align.cpp'],
                     swig_opts=['-c++',
                                '-modern',
                                '-modernargs',
                                '-keyword',
                                '-I'+seqan_path],
                     extra_compile_args=['-std='+seqan_cpp_std],
                     include_dirs=[seqan_path],
                     )


setup(name='seqanpy',
      version="0.2",
      author="Fabio Zanini",
      description="""Fast pairwise sequence alignment using SeqAn""",
      long_description="""Fast pairwise sequence alignment using SeqAn.

      Instructions and development: https://github.com/iosonofabio/seqanpy
      """,
      ext_modules=[_seqanpy],
      py_modules=["seqanpy"],

      # metadata for upload to PyPI
      author_email="fabio.zanini@fastmail.fm",
      license="BSD/2-clause",
      keywords="alignment sequence pairwise C++",
      url="https://github.com/iosonofabio/seqanpy",
      cmdclass={
          'install_seqan': install_seqan,
          'build_ext': my_build_ext
          },
      )
