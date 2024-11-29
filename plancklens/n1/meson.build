f2py_output = custom_target(
    input: 'n1f.f90',
    output: 'n1f',
    command: [py, '-m', 'numpy.f2py', '-c', '-m', 'n1f', '@INPUT@'],
)

n1f_module = py.extension_module(
    'n1f',
    sources : ['n1f.f90', f2py_output],
    include_directories: fortran_include,
    fortran_args : openmp_args,
    link_args : openmp_link_args,
)

# Adds all python sources in the current directory to the python installation
python_sources = [
    '__init__.py',
    'n1.py'
]

py.install_sources(
    python_sources,
    subdir: 'plancklens/n1'
)

