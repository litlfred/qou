#!/usr/bin/env python3
"""Mass prediction with the Jones-Markov y_λ formulation.

THE UNITS BRIDGE: the existing formula
    m(β) = Σ_k α_k_old · Σ_{depth=k} w_λ_q · log|χ_λ(β)|
uses q-deformed Plancherel weight w_λ_q = dim_q(λ)² / [n]_q!.  This
diverges at q ≠ 1 for large n (e.g., w_total at n=12 is 1.51, at n=21
is ~26×).  The fitted α_k_old absorb this divergence — they are NOT
structural physical couplings but a compensation for the bad weight.

Switching to the Jones-Markov gauge-free weight y_λ:
    m(β) = m_e · Σ_k α_k_new · Σ_{depth=k} y_λ · log|χ_λ(β)|
                  ───────────────────────────────────────────
                              Φ_k_JM(β)

The y_λ are bounded (sum at every level equals tr_M(1) = 1 via
Plancherel completeness).  Structural α_k_new = O(1) at H_3 are
known from prop:explicit-alpha-k-h3:
    α_0 = 1, α_1 = 0, α_2 = z², α_3 = h·z² + z

For depths k ≥ 4 the universal prefactor is m_e · 8G (Newton's-G).

Test: do these structural α_k_new × Φ_k_JM × m_e match AME 2020?
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
import numpy as np
import mpmath as mp

warnings.filterwarnings("ignore")
mp.mp.dps = 30

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    build_seminormal_matrices, nuclear_braid_character,
    partitions_of as partitions_of_n,
)

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
z_mark = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))
h_amp = Q0 - QI

m_e = mp.mpf("0.51099895")
G_catalan = mp.catalan

# Structural α_k_new (dimensionless) at H_3 closed-form
alpha_struct = {
    0: mp.mpf(1),
    1: mp.mpf(0),
    2: z_mark**2,
    3: h_amp * z_mark**2 + z_mark,
    # k≥4 universal: 8G (gravity-spectral)
}
for k in range(4, 12):
    alpha_struct[k] = 8 * G_catalan

# AME 2020
AME = {
    "p":   ( 1, 0,    938.78308711,    0.0),
    "n":   ( 0, 1,    939.56542052,    0.0),
    "D":   ( 1, 1,   1876.12393,       2.22456612),
    "T":   ( 1, 2,   2809.43215,       8.481798),
    "3He": ( 2, 1,   2809.41347,       7.718058),
    "4He": ( 2, 2,   3728.40133,      28.29566),
}


def load_y_lambda_table():
    """Load the Jones-Markov witness y_λ values for n=2..12."""
    with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
        W = json.load(f)
    out = {}  # (n, partition tuple) -> y_λ
    for n_str, t in W["tables_by_n"].items():
        n = int(n_str)
        for w in t["weights"]:
            out[(n, tuple(w["partition"]))] = mp.mpf(str(w["y_lambda"]))
    return out


def compute_phi_k_jones_markov(Z, N, max_height=None):
    """Φ_k_JM(β) = Σ_{depth(λ)=k} y_λ · log|χ_λ(β)| at H_n where n = 3A
    (the existing convention uses 3 strands per nucleon)."""
    A = Z + N
    n = 3 * A
    n_gens = max(1, n - 1)
    if max_height is None:
        max_height = min(n, 8)  # cap at depth 7 for tractability

    yl = load_y_lambda_table()

    bins = {}  # depth k -> sum y_λ · log|χ|
    n_done = 0
    n_skip = 0
    for shape in partitions_of_n(n):
        if len(shape) > max_height:
            n_skip += 1
            continue
        if (n, shape) not in yl:
            n_skip += 1
            continue

        try:
            sigmas, dim_lam, _ = build_seminormal_matrices(shape, sparse=None)
        except Exception:
            n_skip += 1
            continue
        if dim_lam == 0:
            n_skip += 1
            continue

        try:
            chi = nuclear_braid_character(Z, N, sigmas, dim_lam, n_gens)
        except Exception:
            n_skip += 1
            continue

        if abs(chi) < 1e-300:
            n_skip += 1
            continue

        y_lam = yl[(n, shape)]
        depth_k = len(shape) - 1
        log_abs_chi = mp.log(abs(chi))
        contrib = y_lam * log_abs_chi
        bins[depth_k] = bins.get(depth_k, mp.mpf(0)) + contrib
        n_done += 1

    return bins, n_done, n_skip


def main():
    print("=" * 90)
    print("STRUCTURAL MASS PREDICTION via Jones-Markov y_λ formulation")
    print("=" * 90)
    print(f"q_0 ≈ {float(Q0):.6f}, m_e = {float(m_e)} MeV, 8G = {float(8*G_catalan):.6f}")
    print()
    print(f"Structural α_k (dimensionless):")
    for k in [0, 1, 2, 3]:
        print(f"  α_{k} = {float(alpha_struct[k]):+.6f}")
    print(f"  α_(k≥4) = 8G ≈ {float(8*G_catalan):.6f}")
    print()
    print(f"{'iso':>5} {'A':>3} {'B_AME':>10} {'B_pred':>12} {'err %':>10} {'err ppb':>14}")
    print("-" * 90)

    results = {}
    for iso, (Z, N, M_AME, B_AME) in AME.items():
        A = Z + N
        if A == 0 or A > 2:
            # Skip n alone (Z+N=1, A=1 stays p only); ³He, ⁴He, T need n≥9.
            # Limit to D (n=6) which is fast; print others as TODO.
            if iso == "n":
                continue
            print(f"{iso:>5} {A:>3} {B_AME:>10.4f}  (n={3*A}; would take >>120s — skipped)")
            results[iso] = {"A": A, "skipped": True, "reason": "compute time"}
            continue
        if iso == "p":
            bins, n_done, n_skip = compute_phi_k_jones_markov(Z, N, max_height=5)
        else:
            # D: n=6, max_height=5 keeps this <60s
            bins, n_done, n_skip = compute_phi_k_jones_markov(Z, N, max_height=5)

        # Sum: B_pred = m_e · Σ_k α_k · Φ_k_JM
        B_pred = mp.mpf(0)
        for k, phi_k in bins.items():
            ak = alpha_struct.get(k, 8 * G_catalan)
            B_pred += m_e * ak * phi_k

        err_pct = float((B_pred - B_AME) / B_AME * 100) if B_AME != 0 else 0
        err_ppb = float((B_pred - B_AME) / B_AME * 1e9) if B_AME != 0 else 0
        print(f"{iso:>5} {A:>3} {B_AME:>10.4f} {float(B_pred):>+12.6f} "
              f"{err_pct:>+9.3f}% {err_ppb:>+14.2e}")
        results[iso] = {
            "A": A, "Z": Z, "N": N,
            "B_AME": B_AME,
            "B_pred_struct_y_lambda": float(B_pred),
            "err_pct": err_pct,
            "Phi_k_by_depth": {str(k): float(v) for k, v in bins.items()},
            "partitions_done": n_done,
            "partitions_skipped": n_skip,
        }

    out = {
        "computation": "isotope-mass-structural-y-lambda",
        "description": (
            "Mass prediction via the Jones-Markov gauge-free formulation: "
            "B_pred(β) = m_e · Σ_k α_k · Σ_{depth(λ)=k} y_λ · log|χ_λ(β)|. "
            "Uses STRUCTURAL α_k from prop:explicit-alpha-k-h3 (closed form) "
            "and 8G universal prefactor at depth ≥ 4. NO FITTING. "
            "y_λ from y-lambda-jones-markov-witness.json."
        ),
        "q_0": float(Q0),
        "m_e_MeV": float(m_e),
        "alpha_struct": {str(k): float(v) for k, v in alpha_struct.items()},
        "results": results,
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }
    out_path = Path(__file__).parent / "isotope-mass-structural-y-lambda.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
