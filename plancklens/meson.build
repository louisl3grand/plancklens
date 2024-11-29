# Adds all python sources in the current directory to the python installation
python_sources = [
    '__init__.py',
    'bandpowers.py',
    'freq_weighting.py',
    'n0s.py',
    'nhl.py',
    'qecl.py',
    'qecl.py',
    'qest.py',
    'qresp.py',
    'shts.py',
    'utils_qe.py',
    'utils_spin.py',
    'utils.py',
]


py.install_sources(
    python_sources,
    subdir: 'plancklens'
)

subdir('wigners')
# subdir('n1')
subdir('filt')
subdir('helpers')
subdir('patchy')
subdir('qcinv')
subdir('sims')
