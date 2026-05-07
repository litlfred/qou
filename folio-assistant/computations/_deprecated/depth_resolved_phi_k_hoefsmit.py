#!/usr/bin/env python3
"""
31a-proper: Depth-resolved Φ_k(β) per isotope using existing Hoefsmit
optimisations from hecke_characters.

For each isotope (Z, N) at H_{3A}:
  1. Enumerate partitions λ ⊢ n = 3A
  2. For each λ: build_seminormal_matrices → sigmas (sparse Hoefsmit YSN)
  3. nuclear_braid_character(Z, N, sigmas, dim, n_gens) → χ_λ(β)
  4. Bin by depth k = len(λ) - 1
  5. Φ_k(β) = Σ_{depth=k} w_λ · log|χ_λ(β)|
  6. LSQ fit α_k per rank from {p, n, D, T}
  7. Predict ³He, ⁴He with same α_k

This is the proper implementation — not the fraction-of-tr_M approximation.
"""
from __future__ import annotations
import sys, json, time, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
mp.mp.dps = 25

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    build_seminormal_matrices, nuclear_braid_character,
    partitions_of, dim_q, qfac, q_int
)
qint = q_int

Q0 = Q_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
m_p = mp.mpf("938.27208816"); m_n = mp.mpf("939.56542052")


# AME 2020
AME = {
    "p":   ( 1, 0,   938.78308711,    0.0),
    "n":   ( 0, 1,   939.56542052,    0.0),
    "D":   ( 1, 1,  1876.12393,       2.22456612),
    "T":   ( 1, 2,  2809.43215,       8.481798),
    "3He": ( 2, 1,  2809.41347,       7.718058),
    "4He": ( 2, 2,  3728.40133,      28.29566),
}
ISOS = list(AME.keys())


def Phi_k_per_isotope(Z, N, max_height=8):
    """Compute Φ_k(β_isotope) for each depth k via per-partition Hoefsmit."""
    A = Z + N
    n = 3 * A
    n_gens = max(1, n - 1)

    bins = {}  # depth k -> list of (w_lambda, chi_lambda)
    t0 = time.time()
    n_parts_skipped = 0
    n_parts_done = 0
    for shape in partitions_of(n):
        if len(shape) > max_height:
            n_parts_skipped += 1
            continue

        # Build seminormal matrices (uses sparse + Hoefsmit optimisations)
        try:
            sigmas, dim_lam, _ = build_seminormal_matrices(shape)
        except Exception as e:
            n_parts_skipped += 1
            continue

        if dim_lam == 0:
            continue

        # Compute χ_λ(β) via nuclear_braid_character (with Hoefsmit optimisations)
        try:
            chi = nuclear_braid_character(Z, N, sigmas, dim_lam, n_gens)
        except Exception as e:
            n_parts_skipped += 1
            continue

        # Plancherel weight
        d = dim_q(shape)
        w_lam = float((d * d) / qfac(n))

        k_depth = len(shape) - 1
        bins.setdefault(k_depth, []).append((w_lam, float(chi), shape))
        n_parts_done += 1

    elapsed = time.time() - t0

    # Compute Φ_k = Σ w_λ · log|χ_λ|
    Phi_k = {}
    for k, contribs in bins.items():
        s = 0.0
        for w, chi, shape in contribs:
            if abs(chi) > 1e-30:
                s += w * float(np.log(abs(chi)))
        Phi_k[k] = s
    return Phi_k, n_parts_done, n_parts_skipped, elapsed


print("=" * 110)
print("31a-proper: Per-partition Hoefsmit Φ_k(β) per isotope")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f}")
print()

isotope_phi = {}
for iso in ISOS:
    Z, N, M_AME, B_AME = AME[iso]
    A = Z + N; n = 3 * A
    print(f"  {iso} (Z={Z}, N={N}, A={A}, n=3A={n})...", end=" ", flush=True)
    Phi_k, n_done, n_skip, elapsed = Phi_k_per_isotope(Z, N)
    print(f"done in {elapsed:.1f}s ({n_done} partitions, {n_skip} skipped)")
    print(f"     Φ_k: " + ", ".join(f"k={k}:{v:+.4f}" for k, v in sorted(Phi_k.items())))
    isotope_phi[iso] = {"Z": Z, "N": N, "A": A, "n": n,
                        "B_AME": B_AME, "M_AME": M_AME,
                        "Phi_k": Phi_k}

# LSQ fit α_k from {p, n, D, T}
calib = ["p", "n", "D", "T"]
max_rank = max(max(isotope_phi[iso]["Phi_k"].keys()) for iso in calib)
all_ranks = list(range(max_rank + 1))

A_mat = []
b_vec = []
for iso in calib:
    row = [isotope_phi[iso]["Phi_k"].get(k, 0.0) for k in all_ranks]
    A_mat.append(row)
    b_vec.append(isotope_phi[iso]["B_AME"])
A_arr = np.array(A_mat); b_arr = np.array(b_vec)

print()
print(f"  Calibration LSQ: {len(calib)} observables, {len(all_ranks)} ranks")
alpha_lsq, resid, rank, sv = np.linalg.lstsq(A_arr, b_arr, rcond=None)
print(f"  Fitted α_k:")
for k, a in enumerate(alpha_lsq):
    print(f"    α_{k} = {a:+.6f} MeV")
print()

# Predict
print("=" * 110)
print(f"  {'iso':<5} {'A':>3} {'B_AME':>10} {'B_pred':>10} {'err %':>9} {'role':>15}")
print("-" * 110)
results = []
for iso in ISOS:
    if iso not in isotope_phi: continue
    d = isotope_phi[iso]
    B_pred = sum(alpha_lsq[k] * d["Phi_k"].get(k, 0.0) for k in all_ranks)
    err = (B_pred - d["B_AME"])/d["B_AME"]*100 if d["B_AME"] != 0 else 0
    role = "calibration" if iso in calib else "PREDICTION"
    print(f"  {iso:<5} {d['A']:>3} {d['B_AME']:>10.4f} {B_pred:>10.4f} {err:>+9.4f}% {role:>15}")
    results.append({
        "iso": iso, "A": d["A"], "B_AME": d["B_AME"],
        "B_pred": B_pred, "err_pct": err, "role": role
    })

print()
print("=" * 110)
print("INTERPRETATION")
print("=" * 110)
print(f"""
Per-partition Hoefsmit Φ_k computation uses the FULL nuclear braid
character per partition (not the fraction-of-trace approximation).

If ³He, ⁴He predictions are within a few percent, the per-rank
structural α_k recipe works universally.  Then ⁶Li, ⁷Li (currently
no zero-param rule) get their first structural predictions.

Computational cost: ~1s per H_3, ~10s per H_9, ~minutes per H_12.
For ⁶Li (H_18), ⁷Li (H_21) the partition count blows up (385, 792
respectively); height cap at 8 keeps it tractable.
""")

out = {
    "computation": "depth-resolved-phi-k-hoefsmit",
    "description": ("31a-proper: Per-partition Hoefsmit Φ_k(β) per isotope. "
                    "Uses hecke_characters.nuclear_braid_character with "
                    "build_seminormal_matrices to compute χ_λ(β) for each "
                    "partition.  Depth-bins to Φ_k.  LSQ fits α_k per rank "
                    "from {p, n, D, T} bindings and PREDICTS ³He, ⁴He using "
                    "same α_k."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "max_rank": max_rank,
    "fitted_alpha_k_MeV": [float(a) for a in alpha_lsq],
    "calibration_isotopes": calib,
    "isotope_Phi_k": {iso: {"A": d["A"], "Phi_k": d["Phi_k"]}
                       for iso, d in isotope_phi.items()},
    "predictions": results
}
out_path = Path(__file__).parent / "depth-resolved-phi-k-hoefsmit.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
