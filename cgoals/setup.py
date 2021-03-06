import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
# from Cython.Build import cythonize


# Removing -Wstring-prototype warning. Hackish.
import os
from distutils.sysconfig import get_config_vars
(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(flag for flag in opt.split() if flag != '-Wstrict-prototypes')
# end of that


ext_modules = [Extension(
    name="cgoals",
    sources=["cgoals.pyx", "c_tseries.cpp"],
    # extra_objects=["fc.o"],  # if you compile fc.cpp separately
    include_dirs = [numpy.get_include()],  # .../site-packages/numpy/core/include
    language="c++",
    # libraries=
    extra_compile_args = "-O4".split(),
    #extra_link_args = "-lflann".split()
    )]

setup(
    name = 'cgoals',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    # ext_modules = cythonize(ext_modules)  ? not in 0.14.1
    version='1.0'
    # description=
    # author=
    # author_email=
    )
