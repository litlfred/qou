#!/usr/bin/env python3
"""
31a: Depth-resolved Φ_k(β) per isotope + per-rank α_k fit.

Implementation approximation (full Hoefsmit per partition is heavy):
  Use the per-isotope Markov trace from pyhecke (Markov-invariant)
  and APPROXIMATE the depth decomposition by Plancherel-weight
  fractions per rank:

    Φ_k(β) ≈ (W_k_total / W_total) · log|tr_M(β)|

  where W_k_total = Σ_{depth(λ)=k} w_λ at H_{3A}.

  Then fit α_k per rank from {p, n, D, T} bindings and predict
  ³He, ⁴He using same α_k.

This is a SIMPLIFICATION — the exact form requires Hoefsmit χ_λ(β)
per partition.  But it demonstrates the per-rank structural recipe
without the heavy per-partition computation.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
m_p = mp.mpf("938.27208816"); m_n = mp.mpf("939.56542052")
G = mp.catalan


def qint(n): return (Q0**n - QI**n)/(Q0 - QI)
def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n+1): p *= qint(k)
    return p
def hook_lengths(shape):
    rows = len(shape); out = []
    for i in range(rows):
        for j in range(shape[i]):
            arm = shape[i] - j - 1
            leg = sum(1 for r in range(i+1, rows) if shape[r] > j)
            out.append(arm + leg + 1)
    return out
def dim_q_partition(shape, n):
    h_prod = mp.mpf(1)
    for hk in hook_lengths(shape): h_prod *= qint(hk)
    return qfac(n) / h_prod
def partitions_of(n):
    if n == 0:
        yield (); return
    def gen(rem, mxp):
        if rem == 0: yield (); return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem-p, p):
                yield (p,) + rest
    yield from gen(n, n)


def per_rank_W(n, max_height=8):
    """Plancherel weights binned by depth k = len(λ) - 1."""
    bins = {}
    for shape in partitions_of(n):
        if len(shape) > max_height: continue
        d = dim_q_partition(shape, n)
        if abs(d) < mp.mpf("1e-30"): continue
        w = d*d / qfac(n)
        k = len(shape) - 1
        bins[k] = bins.get(k, mp.mpf(0)) + w
    return bins


# Canonical Markov trace per isotope
canon = json.load(open(Path(__file__).parent / "canonical-isospin-pyhecke.witness.json"))
canon_results = canon["results"]
def get_canon_tr(iso):
    sup = {"3He": "³He", "4He": "⁴He"}
    target = sup.get(iso, iso)
    for k in canon_results:
        if k.startswith(target + " ") or k == target:
            return mp.mpf(str(canon_results[k]["tr_M_q0"]))
    return None

# AME 2020
AME = {
    "p":   ( 1, 0,   938.78308711,    0.0),
    "n":   ( 0, 1,   939.56542052,    0.0),
    "D":   ( 1, 1,  1876.12393,       2.22456612),
    "T":   ( 1, 2,  2809.43215,       8.481798),
    "3He": ( 2, 1,  2809.41347,       7.718058),
    "4He": ( 2, 2,  3728.40133,      28.29566),
}
ISOS = ["p", "n", "D", "T", "3He", "4He"]


# Compute Φ_k per isotope per rank (approximation)
print("=" * 110)
print("31a: Depth-resolved Φ_k(β) per isotope (approximation: w_k fraction × log|tr_M|)")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f}")
print()
isotope_phi = {}
for iso in ISOS:
    Z, N, M_AME, B_AME = AME[iso]
    A = Z + N; n = 3*A
    tr_M = get_canon_tr(iso)
    if tr_M is None:
        print(f"  {iso}: no tr_M (skip)")
        continue
    log_tr = float(mp.log(abs(tr_M))) if tr_M != 0 else 0
    Wk = per_rank_W(n)
    W_total = sum(Wk.values())
    Phi_k = {k: float(w/W_total * log_tr) for k, w in Wk.items()}
    isotope_phi[iso] = {
        "A": A, "n": n, "B_AME": B_AME,
        "tr_M": float(tr_M), "log_tr_M": log_tr,
        "Wk": {k: float(w) for k, w in Wk.items()},
        "Phi_k": Phi_k
    }
    Phik_str = "  ".join(f"k={k}:{v:+.4f}" for k, v in sorted(Phi_k.items()))
    print(f"  {iso:<5} A={A} n={n} log|tr_M|={log_tr:+.4f}  Φ_k: {Phik_str}")

print()
# Fit α_k per rank by LSQ over {p, n, D, T}
calib = ["p", "n", "D", "T"]
# Find max rank present across calib isotopes
max_rank = max(max(isotope_phi[iso]["Phi_k"].keys()) for iso in calib)
all_ranks = list(range(max_rank + 1))

# Set up matrix:  B = α · Φ
# Each row: B(iso) = Σ_k α_k · Φ_k(iso)
A_matrix = []
b_vec = []
for iso in calib:
    d = isotope_phi[iso]
    row = [d["Phi_k"].get(k, 0.0) for k in all_ranks]
    A_matrix.append(row)
    b_vec.append(d["B_AME"])
A_arr = np.array(A_matrix); b_arr = np.array(b_vec)

# Solve LSQ
print(f"Calibration: {calib}, ranks 0..{max_rank}")
print(f"  Φ matrix shape: {A_arr.shape}")
alpha_lsq, _resid, _rank, _sv = np.linalg.lstsq(A_arr, b_arr, rcond=None)
print(f"  Fitted α_k per rank: " + ", ".join(f"α_{k}={a:+.4f}" for k, a in enumerate(alpha_lsq)))
print()

# Predict
print("=" * 110)
print(f"  {'iso':<5} {'B_AME':>10} {'B_pred':>10} {'err %':>9} {'role':>20}")
print("-" * 110)
results = []
for iso in ISOS:
    if iso not in isotope_phi: continue
    d = isotope_phi[iso]
    B_pred = sum(alpha_lsq[k] * d["Phi_k"].get(k, 0.0) for k in all_ranks)
    err = (B_pred - d["B_AME"])/d["B_AME"]*100 if d["B_AME"] != 0 else 0
    role = "calibration" if iso in calib else "PREDICTION"
    print(f"  {iso:<5} {d['B_AME']:>10.4f} {B_pred:>10.4f} {err:>+9.4f}% {role:>20}")
    results.append({
        "iso": iso, "A": d["A"], "B_AME": d["B_AME"], "B_pred": B_pred,
        "err_pct": err, "role": role
    })

print()
print("=" * 110)
print(f"FINDING: depth-approximated unified formula with {len(all_ranks)} per-rank α_k")
print("=" * 110)
print(f"""
Calibrated from {{{', '.join(calib)}}} ({len(calib)} observables, {len(all_ranks)} unknowns).
Predictions on ³He, ⁴He are with the SAME α_k — no per-isotope refit.

Approximation: depth fraction of total Markov trace.  True per-rank
distribution requires Hoefsmit χ_λ(β) per partition (heavy).

If the 31c approximation gives ³He, ⁴He within 5%, the per-rank
structural recipe works.  If not, the depth fraction approximation
is too coarse and the full Hoefsmit per partition is required.
""")

out = {
    "computation": "depth-resolved-phi-k-test",
    "description": ("31a: Depth-resolved Φ_k per isotope.  APPROXIMATES "
                    "depth-decomposition by Plancherel-weight fraction × "
                    "log|tr_M|.  Fits α_k per rank from {p, n, D, T} via "
                    "LSQ and predicts ³He, ⁴He using same α_k. "
                    "Tests whether per-rank structural recipe gives universal "
                    "predictions even with the coarse depth approximation."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "max_rank": max_rank,
    "fitted_alpha_k": [float(a) for a in alpha_lsq],
    "calibration_isotopes": calib,
    "results": results
}
out_path = Path(__file__).parent / "depth-resolved-phi-k-test.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
