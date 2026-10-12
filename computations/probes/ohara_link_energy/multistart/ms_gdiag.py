#!/usr/bin/env python3
"""Diagnostic (pre-registered §6): does the discrete flow functional E_poly(N) track the
spectral (continuum) energy of the SAME smooth curve? Usage: ms_gdiag.py curve.npz [...]"""
import sys, json
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
import ms_lib as S
L = S.L
def load_npz(p):
    d = np.load(p); return [d[k] for k in sorted(d.files, key=lambda s: int(s.split("_")[1]))]
out = {}
for f in sys.argv[1:]:
    X = load_npz(f)
    smooth = [L.fourier_resample(c, 8192) for c in X]
    Espec = L.link_energy_spectral([L.fourier_resample(c, 16 * len(c)) for c in X])["total"]
    row = dict(E_spectral=Espec, N={})
    for N in (128, 256, 512, 1024):
        P = [L.resample_equal_arclength(c, N, dense=8192) for c in smooth]
        fl = L.LinkFlow(P, 0)
        Ep = fl.E_poly(P)[2]
        Es = L.link_energy_spectral([L.fourier_resample(c, 8 * N) for c in P])["total"]
        _, dres = L.guard_distances(P) if N <= 512 else (None, None)
        row["N"][N] = dict(E_poly=float(Ep), E_spec_of_resampled=float(Es), poly_minus_spec=float(Ep - Espec),  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
                           res_ratio=None if dres is None else float(dres))  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        print(f, N, f"Epoly={Ep:.4f} Espec(resampled)={Es:.4f} Espec(orig)={Espec:.4f} diff={Ep-Espec:+.4f} res={dres}", flush=True)
    out[f] = row
json.dump(out, open(sys.argv[0].replace(".py", "") + "_out.json", "w"), indent=1)
