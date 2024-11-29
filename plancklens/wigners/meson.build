
# Libraries
fc = meson.get_compiler('fortran')
fortran_m_dep = fc.find_library('m', required: true)

# # Directories
# library_install_dir = py.get_install_dir() / 'plancklens'


if host_machine.system() == 'darwin'
    openmp_args = ['-Xpreprocessor', '-fopenmp']
    openmp_link_args = ['-lgomp']
else
    openmp_args = ['-fopenmp']
    openmp_link_args = ['-lgomp']
endif

# Includes

# Need to massage these into relative paths to keep meson happy.
# It does not allow for absolute paths.
incdir_numpy = run_command(
    py,
    ['-c', 'import numpy; import os; print(os.path.relpath(numpy.get_include()))'],
    check: true
).stdout().strip()

incdir_f2py = run_command(
    py,
    ['-c', 'import numpy.f2py; import os; print(os.path.relpath(numpy.f2py.get_include()))'],
    check: true
).stdout().strip()

# Build fortran extensions

fortran_include = include_directories(incdir_numpy, incdir_f2py)
add_project_arguments('-Wno-tabs', language : 'fortran')
add_project_arguments('-Wno-conversion', language : 'fortran')



# Fortran extension: wigners
# f2py -c -m wigners wigners.f90

f2py_output = custom_target(
    input: 'wigners.f90',
    output: 'wigners',
    # command: [py, '-m', 'numpy.f2py', '@INPUT@', '-m', module_name, '--lower'],
    command: [py, '-m', 'numpy.f2py', '-c', '-m', 'wigners', '@INPUT@'],
    # install_dir: 'plancklens' / 'wigners',
    # install_dir: 'plancklens',
    # install_dir: py.purelib_install_path('plancklens/wigners'),
    # install:true,
)

wigners_module = py.extension_module(
    'plancklens.wigners.wigners',
    sources : ['wigners.f90', f2py_output],
    include_directories: fortran_include,
    fortran_args : openmp_args,
    link_args : openmp_link_args,
    install: true,
    # output: ['plancklens.wigners.wigners.f90', 'plancklens.wigners.wignersmodule.c'],
    # command: [py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'plancklens.wigners.wigners', '--lower'],
)