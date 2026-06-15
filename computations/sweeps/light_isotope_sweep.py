#!/usr/bin/env python3

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

# DEPRECATION-CANDIDATE: witness was moved to folio-assistant/computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Light-isotope sweep: Schur-Weyl + Frobenius pipeline for A = 2..4.

Generalizes deuteron_first_principles.py.  For each isotope (Z, N)
on A = Z+N nucleons:

  1. Build atomic braid word via atomic_braid_to_crossings
  2. For each partition λ ⊢ 3A, compute seminormal Hoefsmit matrix
     of the braid word, take trace → χ_λ(T_w)
  3. Weight by w_λ = dim_q(λ)²/[3A]_q!
  4. Sum: tr_M(T_w) = Σ_λ w_λ · χ_λ / dim(λ)

β-decay calibration: E_0 = 0.78233341 MeV / |tr_M(n) - tr_M(p)|.
Binding: B = E_0 · (|tr_M(free)| - |tr_M(atom)|).

Frobenius correction per prop:partition-sum-proton-residual and
thm:frobenius-codim-universal:
  Δ_Frob = m_e · (2 + 1/[2]_q) ≈ 1.276 MeV (universal, n=3)

Tests whether adding Δ_Frob closes the binding gap for A = 2, 3, 4.

Scope: A=2 (D), A=3 (T, ³He), A=4 (⁴He).
  - A=2: n=6, max f^λ = 16, runs in <1s
  - A=3: n=9, max f^λ = 42, runs in seconds
  - A=4: n=12, max f^λ = 132, runs in ~a minute

Witness: light-isotope-sweep.witness.json
"""
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
from scipy import sparse as sp_sparse

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from experimental_constants import M_E_MEV
from hecke_characters import (
    partitions_of, build_seminormal_matrices, qfac, dim_q,
)
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings
from chi_sym_alt_closed_form import (
    chi_sym_closed_form, chi_alt_closed_form,
)
# F6 (PR #565 follow-up): BlockCache wiring for numerical-q Hoefsmit.
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
from witness_base import WitnessBuilder  # noqa: E402


M_E = M_E_MEV
Q0 = _Q_CANONICAL
H_VAL = float(Q0 - 1.0 / Q0)
_BLOCK_CACHE = BlockCache(float(Q0), H_VAL)
FROB_N3 = M_E * (2.0 + 1.0 / (Q0 + 1.0 / Q0))  # m_e · (2 + 1/[2]_q)
CLOSED_FORM_USED = True  # use exact 1-dim irrep closed forms for sym/alt


def chi_lambda_numeric(shape, crossings):
    """Evaluate χ^λ_q(T_w) numerically for the atomic braid word."""
    sigmas, dim, _syts = build_seminormal_matrices_cached(
        shape, cache=_BLOCK_CACHE,
    )
    if dim == 0:
        return 0.0, 0

    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        I = sp_sparse.eye(dim, format='csr')
        product = sp_sparse.eye(dim, format='csr')
    else:
        I = np.eye(dim)
        product = np.eye(dim)

    d_for = {"sigma": 0.0, "sigma_inv": -H_VAL, "averaged": -H_VAL / 2}
    for gen_idx, cross_type in crossings:
        if gen_idx < 0 or gen_idx >= len(sigmas):
            raise IndexError(
                f"gen_idx {gen_idx} out of range for shape {shape} "
                f"(n_gens={len(sigmas)})"
            )
        M = sigmas[gen_idx] + d_for[cross_type] * I
        product = product @ M

    chi = (
        float(product.diagonal().sum()) if is_sparse
        else float(np.trace(product))
    )
    return chi, dim


def tr_M_at_q0(Z, N, include_inter, convention="plancherel"):
    """Full tr_M at q_0.

    convention="plancherel" (LEGACY): tr_M = Σ_λ (dim_q²/[n]_q!) · χ_λ / dim_λ_classical
        Use w_λ = dim_q² / [n]_q! and divide by classical dim_λ inside.
        This is the Plancherel-A convention. Some scripts depend on this.

    convention="wenzl-schur" (CANONICAL per prop:y-lambda-recipe-from-partition):
        tr_M = Σ_λ y_λ · χ_λ where y_λ from y-lambda-wenzl-witness.json.
        Per the d_from_scratch diagnostic, this is the right Markov trace.

    Returns (tr_M, per_lambda_breakdown, walltime_sec).
    """
    A = Z + N
    k = 3 * A
    nfac = qfac(k)
    crossings = atomic_braid_to_crossings(Z, N, include_inter=include_inter)

    # Lazy-load Wenzl y_λ if requested
    wenzl_y = None
    if convention == "wenzl-schur":
        import json
        from pathlib import Path
        path = Path(__file__).parent / "y-lambda-wenzl-witness.json"
        with open(path) as f:
            wd = json.load(f)
        table = wd["tables_by_n"].get(str(k))
        if table is None:
            raise ValueError(
                f"y-lambda-wenzl-witness.json has no n={k} table; "
                f"extend the witness or fall back to convention='plancherel'."
            )
        wenzl_y = {tuple(w["partition"]): float(w["y_lambda_numeric"])
                   for w in table["weights"]}

    total = 0.0
    per_lambda = []
    t_total = 0.0
    sym_shape = (k,)
    alt_shape = (1,) * k
    for shape in partitions_of(k):
        t0 = time.time()
        used_closed_form = False
        if CLOSED_FORM_USED and shape == sym_shape:
            chi = chi_sym_closed_form(crossings, Q0)
            d = 1
            used_closed_form = True
        elif CLOSED_FORM_USED and shape == alt_shape:
            chi = chi_alt_closed_form(crossings, Q0)
            d = 1
            used_closed_form = True
        else:
            chi, d = chi_lambda_numeric(shape, crossings)
        dt = time.time() - t0
        t_total += dt
        if d == 0:
            continue
        if convention == "wenzl-schur":
            y = wenzl_y.get(shape, 0.0)
            w = y               # for the breakdown
            contrib = y * chi   # canonical: NO /dim_classical
        else:  # plancherel (legacy)
            d_q_val = dim_q(shape)
            w = float(d_q_val ** 2 / nfac)
            contrib = w * chi / d
        total += contrib
        per_lambda.append({
            "shape": shape, "dim": d, "w_lambda": w,
            "chi_lambda": chi, "contribution": contrib,
            "closed_form": used_closed_form,
        })
    return total, per_lambda, t_total


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--convention",
        choices=["plancherel", "wenzl-schur"],
        default="plancherel",
        help=(
            "Markov-trace weight convention. 'plancherel' (legacy) uses "
            "w_λ = dim_q²/[n]_q! with /dim_λ_classical inside. 'wenzl-schur' "
            "(canonical per prop:y-lambda-recipe-from-partition) uses "
            "y_λ = s_λ(q,q^-1)/H_q(λ) loaded from y-lambda-wenzl-witness.json."
        ),
    )
    args = ap.parse_args()
    CONV = args.convention

    print("LIGHT ISOTOPE SWEEP — Schur-Weyl + Frobenius pipeline")
    print("=" * 96)
    print(f"q_0 = {Q0}")
    print(f"m_e = {M_E} MeV")
    print(f"convention = {CONV}")
    print(f"Universal Frobenius (n=3) per nucleon: "
          f"m_e · (2 + 1/[2]_q) = {FROB_N3:.6f} MeV")
    print()

    # ─── A=1 calibration ──────────────────────────────────────
    print("[calibration] A=1 free p, free n (β-decay)")
    print("-" * 72)
    t = time.time()
    tr_p, _, dt_p = tr_M_at_q0(1, 0, include_inter=False, convention=CONV)
    tr_n, _, dt_n = tr_M_at_q0(0, 1, include_inter=False, convention=CONV)
    Q_cat = tr_n - tr_p
    from experimental_constants import Q_NEUTRON_MEV
    E_0 = float(Q_NEUTRON_MEV) / abs(Q_cat)
    print(f"  |tr_M(p)| = {abs(tr_p):.6e}  (walltime: {dt_p:.2f}s)")
    print(f"  |tr_M(n)| = {abs(tr_n):.6e}  (walltime: {dt_n:.2f}s)")
    print(f"  Q_cat     = {Q_cat:+.6e}")
    print(f"  E_0       = {E_0:.6f} MeV/cat.unit")
    print()

    # ─── Isotope sweep ────────────────────────────────────────
    ISOTOPES = [
        ("D",   1, 1,  2.22457),
        ("T",   1, 2,  8.48180),
        ("3He", 2, 1,  7.71806),
        ("4He", 2, 2, 28.29569),
    ]
    print(f"{'iso':>5} {'A':>3}  {'|tr_free|':>14} {'|tr_atom|':>14} "
          f"{'B_pred (MeV)':>12} {'B_AME':>8} {'err%':>8} "
          f"{'+Frob(n=3)·A?':>16}")
    print("-" * 96)

    rows = []
    for iso, Z, N, B_AME in ISOTOPES:
        A = Z + N
        n = 3 * A
        t = time.time()
        try:
            tr_free, free_lam, dt_free = tr_M_at_q0(
                Z, N, include_inter=False, convention=CONV)
            tr_atom, atom_lam, dt_atom = tr_M_at_q0(
                Z, N, include_inter=True, convention=CONV)
        except Exception as exc:
            print(f"  {iso:>5} {A:>3}  ERROR: {type(exc).__name__}: {exc}")
            continue
        dt = time.time() - t
        B_cat = abs(tr_free) - abs(tr_atom)
        B_pred = E_0 * abs(B_cat)
        err_pct = (B_pred - B_AME) / B_AME * 100

        # Frobenius correction: currently tested at (A-1)·Frob (per-bond)
        # and 1·Frob (per-vortex) and A·Frob (per-nucleon)
        B_plus_frob_per_bond = B_pred + (A - 1) * FROB_N3
        err_per_bond = (B_plus_frob_per_bond - B_AME) / B_AME * 100
        B_plus_frob_per_vortex = B_pred + FROB_N3
        err_per_vortex = (B_plus_frob_per_vortex - B_AME) / B_AME * 100
        B_plus_frob_per_nucleon = B_pred + A * FROB_N3
        err_per_nucleon = (B_plus_frob_per_nucleon - B_AME) / B_AME * 100

        best_opts = [
            ("per-vortex (+1·Frob)", B_plus_frob_per_vortex, err_per_vortex),
            ("per-bond (+(A-1)·Frob)", B_plus_frob_per_bond, err_per_bond),
            ("per-nucleon (+A·Frob)", B_plus_frob_per_nucleon, err_per_nucleon),
        ]
        best = min(best_opts, key=lambda x: abs(x[2]))

        print(f"  {iso:>5} {A:>3}  {abs(tr_free):>14.4e} {abs(tr_atom):>14.4e} "
              f"{B_pred:>12.4f} {B_AME:>8.3f} {err_pct:>+7.3f}% "
              f"{best[0]:>16} → {best[1]:.3f} ({best[2]:+.2f}%)")
        print(f"  {'':>5} {'':>3}  walltime: {dt:.1f}s, "
              f"partitions: free={len(free_lam)}, atom={len(atom_lam)}")

        rows.append({
            "iso": iso, "Z": Z, "N": N, "A": A,
            "tr_free_q0": abs(tr_free),
            "tr_atom_q0": abs(tr_atom),
            "B_pred_MeV": B_pred,
            "B_AME_MeV": B_AME,
            "err_pct_raw": err_pct,
            "plus_frob": {
                "per_vortex": {"value": B_plus_frob_per_vortex,
                               "err_pct": err_per_vortex},
                "per_bond": {"value": B_plus_frob_per_bond,
                             "err_pct": err_per_bond},
                "per_nucleon": {"value": B_plus_frob_per_nucleon,
                                "err_pct": err_per_nucleon},
            },
            "best_frob_scaling": best[0],
            "best_value": best[1],
            "best_err_pct": best[2],
            "walltime_sec": dt,
        })

    print()
    print("Frobenius scaling comparison (per-vortex = universal; the")
    print("per-bond and per-nucleon hypotheses would scale with A):")
    print()
    print(f"{'iso':>5}  {'raw err%':>9}  {'+1·Frob err%':>13}  "
          f"{'+(A-1)·Frob err%':>17}  {'+A·Frob err%':>13}")
    print("-" * 72)
    for r in rows:
        print(f"{r['iso']:>5}  {r['err_pct_raw']:>+8.2f}%  "
              f"{r['plus_frob']['per_vortex']['err_pct']:>+12.2f}%  "
              f"{r['plus_frob']['per_bond']['err_pct']:>+16.2f}%  "
              f"{r['plus_frob']['per_nucleon']['err_pct']:>+12.2f}%")

    witness = {
        "computation": "light-isotope-sweep",
        "convention": CONV,
        "closed_form_used": CLOSED_FORM_USED,
        "description": (
            "Schur-Weyl + Frobenius binding predictions for light "
            "isotopes (D, T, ³He, ⁴He) with β-decay calibration at A=1. "
            "Tests three Frobenius-scaling hypotheses: per-vortex "
            "(universal, +1·Frob), per-bond (+(A-1)·Frob), per-nucleon "
            "(+A·Frob). Per-vortex is the universal interpretation from "
            "thm:frobenius-codim-universal; the others are candidate "
            "scalings to test empirically."
        ),
        "reference_blocks": [
            "prop:schur-weyl-mass-decomposition",
            "thm:frobenius-codim-universal",
            "thm:knot-mass-formula-unified",
            "prop:partition-sum-proton-residual",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0,
            "m_e_MeV": M_E,
            "h_q_val": H_VAL,
            "frobenius_n3_per_vortex_MeV": FROB_N3,
            "E_0_MeV": E_0,
        },
        "A1_calibration": {
            "tr_p_q0": abs(tr_p),
            "tr_n_q0": abs(tr_n),
            "Q_cat": Q_cat,
        },
        "rows": rows,
    }
    suffix = "" if CONV == "plancherel" else f".{CONV}"
    out = (WitnessBuilder.wrap_legacy(
        f"light-isotope-sweep{suffix}", witness,
        script_path=__file__, engine="sympy")
        .save())
    print(f"\nWitness: {out}")
