from __future__ import print_function

import os
import pickle as pk
import numpy as np
import healpy as hp

from plancklens2018 import utils
from plancklens2018 import mpi
from plancklens2018 import sql
from plancklens2018 import qresp

class nhl_lib_simple:
    """Analytical unnormalized N0 library.

    NB: This version only for 4 identical legs
    """
    def __init__(self, lib_dir, ivfs, cls_weight, lmax_qlm):
        self.lmax_qlm = lmax_qlm
        self.cls_weight = cls_weight
        self.ivfs = ivfs
        self.lib_dir = lib_dir
        self.npdb = sql.npdb(lib_dir)
        self.fsky = np.mean(self.ivfs.get_fmask())

    def hashdict(self):
        ret = {k: utils.clhash(self.cls_weight[k]) for k in self.cls_weight.keys()}
        ret['ivfs']  = self.ivfs.hashdict()
        ret['lmax_qlm'] = self.lmax_qlm
        return ret

    def get_nhl(self, idx, k1, k2, recache=False):
        fn = 'anhl_qe_' + k1[1:] + '_qe_' + k2[1:] + ('_G' if k1[0] != 'x' else '_C')
        if self.npdb.get(fn) is None or recache:
            cls_ivfs, lmax_ivf = self.get_cls(idx)
            G, C = qresp.get_nhl(k1, k2, self.cls_weight, cls_ivfs, lmax_ivf, lmax_out=self.lmax_qlm)
            if recache and self.npdb.get(fn) is not None:
                self.npdb.remove('anhl_qe_' + k1[1:] + '_qe_' + k2[1:] + '_G')
                self.npdb.remove('anhl_qe_' + k1[1:] + '_qe_' + k2[1:] + '_C')
            self.npdb.add('anhl_qe_' + k1[1:] + '_qe_' + k2[1:] + '_G', G)
            self.npdb.add('anhl_qe_' + k1[1:] + '_qe_' + k2[1:] + '_C', C)
        return self.npdb.get(fn)

    def get_cls(self, idx):
        ret =  {'tt':  hp.alm2cl(self.ivfs.get_sim_tlm(idx)) / self.fsky,
                'ee':  hp.alm2cl(self.ivfs.get_sim_elm(idx)) / self.fsky,
                'bb':  hp.alm2cl(self.ivfs.get_sim_blm(idx)) / self.fsky,
                'te':  hp.alm2cl(self.ivfs.get_sim_tlm(idx), alms2=self.ivfs.get_sim_elm(idx)) / self.fsky}
        lmaxs = [len(cl) for cl in ret.values()]
        assert np.all(lmaxs == lmaxs[0]), 'not implemented'
        return ret, lmaxs[0]





