#!/usr/bin/env python3
"""Calibration gates G1-G3 (preregistration.md section 7)."""
import json, sys, time
import numpy as np  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2]))  # computations/
import ohara_lib as L

out = {}
target = 2 * np.pi ** 2

# ---- G1: corpus integrator on the round Hopf configuration of its own family
import mobius_cross_energy_hopf_calibration as corpus
from mpmath import mp, mpf, sqrt, pi as mpi
g1 = {}
for N in (32, 64, 128):
    e = corpus.cross_energy(mpf(1), sqrt(2), N)
    g1[N] = (mp.nstr(e, 20), mp.nstr(abs(e - 2 * mpi ** 2) / (2 * mpi ** 2), 5))
    print("G1 corpus cross_energy(R=1,c=sqrt2,N=%d) = %s  rel.dev %s" % (N, *g1[N]))
out["G1_corpus_integrator_round_hopf"] = {"R": "1", "c": "sqrt(2)", "by_N": g1,
                                         "target_2pi2": mp.nstr(2 * mpi ** 2, 20)}
g1_pass = float(g1[128][1]) < 1e-8  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
out["G1_pass"] = g1_pass

# ---- G2: my evaluator. Round circle; stereographic Hopf fibres from a generic pole
def circle(M, R=1.7):
    u = np.arange(M) / M * 2 * np.pi
    return np.c_[R * np.cos(u), R * np.sin(u), 0 * u]

g2 = {}
for M in (64, 128, 256):
    e, _ = L.self_energy_spectral(circle(M))
    g2[f"circle_M{M}"] = e
rng = np.random.default_rng(7)
pole = rng.normal(size=4); pole /= np.linalg.norm(pole)
# orthonormal frame with pole as last vector
Qm, _ = np.linalg.qr(np.c_[pole, rng.normal(size=(4, 3))])
Qm = Qm[:, [1, 2, 3, 0]]
if np.dot(Qm[:, 3], pole) < 0: Qm[:, 3] *= -1
def stereo(P):  # P on S^3 (M,4) -> R^3, projecting from 'pole'
    c = P @ Qm
    return c[:, :3] / (1 - c[:, 3:4])
for M in (64, 128, 256, 512):
    u = np.arange(M) / M * 2 * np.pi
    f1 = np.c_[np.cos(u), np.sin(u), 0 * u, 0 * u]
    f2 = np.c_[0 * u, 0 * u, np.cos(u), np.sin(u)]
    X, Y = stereo(f1), stereo(f2)
    r = L.link_energy_spectral([X, Y])
    g2[f"hopf_M{M}"] = dict(E1=r["self"][0], E2=r["self"][1], E12=r["mutual"],
                           rel_dev_E12=abs(r["mutual"] - target) / target)
    print(f"G2 stereographic Hopf M={M}: E1={r['self'][0]:.12f} E2={r['self'][1]:.12f} "
          f"E12={r['mutual']:.12f} reldev={abs(r['mutual']-target)/target:.2e}")
print("G2 circle:", {k: v for k, v in g2.items() if k.startswith('circle')})
g2_pass = (abs(g2["circle_M256"] - 4) < 1e-10 and g2["hopf_M512"]["rel_dev_E12"] < 1e-8
           and abs(g2["hopf_M512"]["E1"] - 4) < 1e-8 and abs(g2["hopf_M512"]["E2"] - 4) < 1e-8)
out["G2_my_evaluator"] = g2; out["G2_pass"] = bool(g2_pass)

# ---- G3: Möbius invariance under a random inversion, on canonical embeddings
def inversion(X, c, rad=1.0):
    D = X - c
    return c + rad ** 2 * D / np.sum(D * D, 1)[:, None]
g3 = {}
for name, w, n in (("hopf_s1^2", [0, 0], 2), ("nuc9", [0, 1] * 3 + [0, 0, 1], 3)):
    rows = {}
    for M in (512, 1024):
        curves = L.closed_braid_curves(w, n, M, R=3.0, a=1.0)
        r0 = L.link_energy_spectral(curves)
        c = np.array([0.7, -2.2, 1.9])  # off the curves  # float64-ok: numerical gradient flow of a discretised curve energy is float64 by design; results are stated as float64 upper bounds, never as identities
        ci = [inversion(C, c, 2.0) for C in curves]
        r1 = L.link_energy_spectral(ci)
        rows[M] = dict(before=dict(E1=r0["self"][0], E2=r0["self"][1], E12=r0["mutual"]),
                       after=dict(E1=r1["self"][0], E2=r1["self"][1], E12=r1["mutual"]),
                       max_rel_change=max(abs(a - b) / abs(a) for a, b in
                                          zip(r0["self"] + [r0["mutual"]], r1["self"] + [r1["mutual"]])))
        print(f"G3 {name} M/pass={M}: before {r0['self']} {r0['mutual']:.10f}  after {r1['self']} {r1['mutual']:.10f}  maxrel={rows[M]['max_rel_change']:.2e}")
    g3[name] = rows
g3_pass = all(r[1024]["max_rel_change"] < 1e-6 for r in g3.values())
out["G3_mobius_invariance"] = g3; out["G3_pass"] = bool(g3_pass)
print("PASS:", g1_pass, g2_pass, g3_pass)
json.dump(out, open("calibration_G1_G3.json", "w"), indent=1, default=str)
