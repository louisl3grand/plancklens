py = import('python').find_installation(pure: false)

# Adds all python sources in the current directory to the python installation
python_sources = [
    '__init__.py',
    'cmbs.py',
    'maps.py',
    'phas.py',
    'planck2018_sims.py',
    'utils.py',
]

py.install_sources(
    python_sources,
    subdir: 'plancklens/sims'
)
