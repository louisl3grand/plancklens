# Main build file for plancklens, helping with building the fortran,
# extensions.
project(
    'plancklens', 'fortran', 'c', version : '0.0.1'
)

py = import('python').find_installation(pure: false)

# Dependencies
py_dep = py.dependency()
# omp_dep = dependency('openmp')

# # Libraries
# fc = meson.get_compiler('fortran')
# fortran_m_dep = fc.find_library('m', required: true)

# # Directories
# library_install_dir = py.get_install_dir() / 'plancklens'


# if host_machine.system() == 'darwin'
#     openmp_args = ['-Xpreprocessor', '-fopenmp']
#     openmp_link_args = ['-lgomp']
# else
#     openmp_args = ['-fopenmp']
#     openmp_link_args = ['-lgomp']
# endif

# # Includes

# # Need to massage these into relative paths to keep meson happy.
# # It does not allow for absolute paths.
# incdir_numpy = run_command(
#     py,
#     ['-c', 'import numpy; import os; print(os.path.relpath(numpy.get_include()))'],
#     check: true
# ).stdout().strip()

# incdir_f2py = run_command(
#     py,
#     ['-c', 'import numpy.f2py; import os; print(os.path.relpath(numpy.f2py.get_include()))'],
#     check: true
# ).stdout().strip()

# # Build fortran extensions

# fortran_include = include_directories(incdir_numpy, incdir_f2py)
# add_project_arguments('-Wno-tabs', language : 'fortran')
# add_project_arguments('-Wno-conversion', language : 'fortran')



# Fortran extension: wigners
# f2py -c -m wigners wigners.f90

# f2py_output = custom_target(
#     input: 'plancklens/wigners/wigners.f90',
#     output: 'wigners',
#     # command: [py, '-m', 'numpy.f2py', '@INPUT@', '-m', module_name, '--lower'],
#     command: [py, '-m', 'numpy.f2py', '-c', '-m',  'wigners', '@INPUT@'],
#     install_dir: get_option('libdir') / 'wigners',
#     install:true,
# )

# wigners_module = py.extension_module(
#     'plancklens.wigners.wigners',
#     ['plancklens/wigners/wigners.f90', f2py_output],
#     # incdir_f2py / 'fortranobject.c',
#     include_directories: fortran_include,
#     dependencies: [py_dep, omp_dep, fortran_m_dep],
#     install: true,
#     subdir: 'plancklens'
# )

# wigners_module = py.extension_module(
#     'plancklens.wigners.wigners',
#     ['plancklens/wigners/wigners.f90', f2py_output],
#     incdir_f2py / 'fortranobject.c',
#     include_directories: fortran_include,
#     fortran_args : openmp_args,
#     link_args : openmp_link_args,
#     # output: ['plancklens.wigners.wigners.f90', 'plancklens.wigners.wignersmodule.c'],
#     # command: [py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'plancklens.wigners.wigners', '--lower'],
# )

# # Fortran extension: n1f
# n1f_module = py.extension_module(
#     'plancklens.n1.n1f',
#     sources : 'plancklens/n1/n1f.f90',
#     include_directories: fortran_include,
#     fortran_args : openmp_args,
#     link_args : openmp_link_args,
#     # output: ['plancklens/n1/n1f.f90', 'plancklens/n1/n1fmodule.c'],
#     # command: [py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'plancklens/n1/n1f', '--lower'],
# )

# fortran_sources = {
#     'plancklens/wigners/wigners.f90': 'plancklens.wigners.wigners',
#     # 'plancklens/n1/n1f.f90': 'plancklens.n1.n1f',
# }
# foreach source_name, module_name : fortran_sources
#     f2py_output = custom_target(
#         input: source_name,
#         output: [module_name + '.f90', module_name + 'module.c'],
#         command: [py, '-m', 'numpy.f2py', '-c', '-m', module_name, '@INPUT@', '--lower'],
#     )

#     py.extension_module(
#         module_name,
#         [source_name, f2py_output],
#         incdir_f2py / 'fortranobject.c',
#         include_directories: fortran_include,
#         dependencies: [py_dep, omp_dep, fortran_m_dep],
#         install: true,
#         subdir: 'plancklens'
#     )
# endforeach


# Libraries
# fc = meson.get_compiler('fortran')
# fortran_m_dep = fc.find_library('m', required: true)

# # # Directories
# # library_install_dir = py.get_install_dir() / 'plancklens'

# if host_machine.system() == 'darwin'
#     openmp_args = ['-Xpreprocessor', '-fopenmp']
#     openmp_link_args = ['-lgomp']
# else
#     openmp_args = ['-fopenmp']
#     openmp_link_args = ['-lgomp']
# endif

# # Includes
# # Need to massage these into relative paths to keep meson happy.
# # It does not allow for absolute paths.
# incdir_numpy = run_command(
#     py,
#     ['-c', 'import numpy; import os; print(os.path.relpath(numpy.get_include()))'],
#     check: true
# ).stdout().strip()

# incdir_f2py = run_command(
#     py,
#     ['-c', 'import numpy.f2py; import os; print(os.path.relpath(numpy.f2py.get_include()))'],
#     check: true
# ).stdout().strip()

# # Build fortran extensions

# fortran_include = include_directories(incdir_numpy, incdir_f2py)
# add_project_arguments('-Wno-tabs', language : 'fortran')
# add_project_arguments('-Wno-conversion', language : 'fortran')


# install_subdir('plancklens', install_dir: library_install_dir)
subdir('plancklens')