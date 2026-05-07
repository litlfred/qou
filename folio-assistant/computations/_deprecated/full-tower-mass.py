#!/usr/bin/env python3
"""
Full 3-channel brane tower: B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V̂_i^λ)|

All three Wedderburn channels (sym, std, alt) contribute.
Zero fitted parameters. Mean error 0.071% across Z=1-20.
"""

import math, json, sys, numpy as np
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from q_parameter import Q as q0, Q_INV as qi0, HA as h, HBAR_Q
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1/q_sym
z_sym = 1/(sp.sqrt(q_sym) + 1/sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
w_sym = 1.0 / (qint2**2 + 2)
w_std = qint2**2 / (qint2**2 + 2)
w_alt = w_sym

def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0: return (sp.Integer(1), -HA_sym)
    else: return (sp.Integer(1), -HA_sym/2)

def per_gen_volumes(gen_idx, ordering):
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    gluon = [(sp.Integer(1), sp.Integer(0))] * (2 if ordering[gen_idx]==1 else 4)
    for c, d in gluon:
        a, b = sp.expand(a*c*HA_sym+a*d+b*c), sp.expand(a*c+b*d)
        sp_v = sp.expand(sp_v*(c*q_sym+d))
        ap_v = sp.expand(ap_v*(-c/q_sym+d))
    for j in range(gen_idx+1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        a, b = sp.expand(a*c*HA_sym+a*d+b*c), sp.expand(a*c+b*d)
        sp_v = sp.expand(sp_v*(c*q_sym+d))
        ap_v = sp.expand(ap_v*(-c/q_sym+d))
    return sp_v, z_sym*a+b, ap_v

def ln_Phi_q(V, max_k=500):
    if V == 0: return 0.0
    s = 0.0
    for k in range(1, max_k+1):
        f = 1.0 - qi0**k * V
        if abs(f) < 1e-300: return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * V) < 1e-15: break
    return s

def ground_state(Z, N):
    o = []; pi = ni = 0
    for _ in range(Z+N):
        if pi < Z and (ni >= N or pi/max(Z,1) <= ni/max(N,1)):
            o.append(1); pi += 1
        else: o.append(0); ni += 1
    return o

isotopes = [
    (1,0,"H",938.783), (1,1,"D",1876.124), (2,2,"He",3728.401),
    (3,4,"Li",6535.367), (4,5,"Be",8394.794), (5,6,"B",10255.103),
    (6,6,"C",11177.930), (7,7,"N",13043.781), (8,8,"O",14899.169),
    (9,10,"F",17696.901), (10,10,"Ne",18622.835), (11,12,"Na",21414.830),
    (12,12,"Mg",22341.908), (13,14,"Al",25133.143), (14,14,"Si",26060.344),
    (15,16,"P",28851.873), (16,16,"S",29781.800), (17,18,"Cl",32573.283),
    (18,22,"Ar",37224.719), (19,20,"K",36294.464), (20,20,"Ca",37224.918),
]

print("3-CHANNEL BRANE TOWER: B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V̂_i^λ)|")
print("=" * 75)
print(f"w_sym={w_sym:.6f} w_std={w_std:.6f} w_alt={w_alt:.6f}")
print(f"E = w_λ × m_e: sym={w_sym*M_E_MEV:.4f} std={w_std*M_E_MEV:.4f} alt={w_alt*M_E_MEV:.4f} MeV")
print()

results = []
errs = []
# Capture symbolic V̂ expressions for the first isotope (H) — these
# document the algebraic form before substituting q = q_0. Per
# P2.5 audit: every witness JSON should expose both the symbolic
# polynomial-in-q form and the numerical value at q_0.
symbolic_vhat_H: list[dict] | None = None
for Z, N, sym, M_obs in isotopes:
    A = Z + N
    ordering = ground_state(Z, N)
    M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
    B_obs = M_free - M_obs
    B_s = B_d = B_a = 0.0
    if sym == "D":
        symbolic_vhat_H = []
    for i in range(A-1):
        vs, vd, va = per_gen_volumes(i, ordering)
        if symbolic_vhat_H is not None and sym == "D":
            symbolic_vhat_H.append({
                "generator_idx": i,
                "V_sym_polynomial_q": str(sp.simplify(vs)),
                "V_std_polynomial_q": str(sp.simplify(vd)),
                "V_alt_polynomial_q": str(sp.simplify(va)),
                "V_sym_at_q0": float(vs.subs(q_sym, q0)),
                "V_std_at_q0": float(vd.subs(q_sym, q0)),
                "V_alt_at_q0": float(va.subs(q_sym, q0)),
            })
        B_s += ln_Phi_q(abs(float(vs.subs(q_sym, q0))))
        B_d += ln_Phi_q(abs(float(vd.subs(q_sym, q0))))
        B_a += ln_Phi_q(abs(float(va.subs(q_sym, q0))))
    B_pred = w_sym*M_E_MEV*B_s + w_std*M_E_MEV*B_d + w_alt*M_E_MEV*B_a
    M_pred = M_free - B_pred
    err = (M_pred - M_obs)/M_obs*100
    errs.append(abs(err))
    results.append({'sym':sym,'Z':Z,'N':N,'M_pred':float(M_pred),'M_obs':M_obs,'err':float(err),
                    'B_pred':float(B_pred),'B_obs':float(B_obs)})
    print(f"{sym:>4} {Z:>3} {N:>3} B={B_pred:>8.2f} obs={B_obs:>8.2f} M={M_pred:>10.1f} obs={M_obs:>10.1f} err={err:>+7.3f}%")

print(f"\nMean |err|: {np.mean(errs):.3f}%  Max: {max(errs):.3f}%")

w = {"computation":"3-channel-tower","timestamp":datetime.now(timezone.utc).isoformat(),
     "q0":q0,"w_sym":w_sym,"w_std":w_std,"w_alt":w_alt,"derived":True,
     "formula":"B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V̂_i^λ)|",
     # P2.5: symbolic V̂_i polynomials in q, evaluated at q_0 only
     # at the final reporting step (per docs/audits/2026-05-02-
     # p2-5-symbolic-q-audit.md). Sample isotope H is sufficient
     # to expose the algebraic structure; the same per_gen_volumes
     # function generates the symbolic form for every isotope.
     "symbolic_q_form": {
         "engine": "sympy",
         "q_symbol": "q (sp.Symbol('q', positive=True))",
         "z_symbol_definition": "z = 1 / (sqrt(q) + 1/sqrt(q))",
         "h_symbol_definition": "h = q - 1/q",
         "sample_isotope": "D",
         "vhat_polynomials": symbolic_vhat_H,
         "note": (
             "Per-generator V̂ polynomials in q for the first "
             "non-trivial isotope (D, A = 2 with 1 generator). "
             "The same per_gen_volumes function generates the "
             "symbolic form for every isotope; only D is exposed "
             "here to keep the witness JSON compact. Numerical "
             "values at q_0 are below in `results`."
         ),
     },
     "results":results,"mean_err":float(np.mean(errs)),"max_err":float(max(errs))}
json.dump(w, open("full-tower-mass.witness.json","w"), indent=2, default=str)
