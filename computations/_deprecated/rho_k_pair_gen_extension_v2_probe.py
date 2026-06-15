#!/usr/bin/env python3
"""
Pair-generator extension v2: WEDDERBURN-coupled pair volumes.

The v1 probe (`rho_k_pair_gen_extension_probe.py`) used the naive
log-additive form Σ ln|V_i V_j| = (n-1)·Σ ln|V_i|, which collapses
to a pure rescaling and degraded accuracy from 0.25% to 9% mean.

This v2 probe uses the proper Wedderburn-block-decomposed pair
amplitudes (`wedderburn_pair_volumes.py`):

    |V̂_i V̂_j|_Wedderburn
       = w_sym  · λ_i^sym · λ_j^sym
       + w_std  · [z · (M_i M_j)_12 + (M_i M_j)_22]
       + w_alt  · λ_i^alt · λ_j^alt

The std-channel pair coupling is the Markov-traced 2x2 transfer-
matrix product M_i M_j — genuinely different from the product
V_i^std · V_j^std and capturing actual braid-group non-commutativity.

Tests the unified ρ_K formula at A=1..20:

  M(K) = (Z m_p + N m_n + Z m_e)
       + α · Σ_i ln|V̂_i^full|
       + α · z² · Σ_{i<j} ln|V̂_i V̂_j|_Wedderburn
       + (higher-order terms)

Output: rho-k-pair-gen-v2-wedderburn.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_MP  # noqa: E402
from hecke_core import atom_per_generator_volumes  # noqa: E402
from wedderburn_pair_volumes import wedderburn_pair_volumes  # noqa: E402

Q0 = Q_MP
M_E_MEV = 0.51099895
M_P_MEV = 938.27208816
M_N_MEV = 939.56542052
G_CATALAN = float(mp.catalan)
ALPHA = M_E_MEV * 8 * G_CATALAN
Z_MARKOV = 1.0 / (float(mp.sqrt(Q0)) + 1.0 / float(mp.sqrt(Q0)))

PAPER_TABLE = [
    (1,  "H",  1,    938.783),
    (2,  "He", 4,   3728.401),
    (3,  "Li", 7,   6535.367),
    (4,  "Be", 9,   8394.794),
    (5,  "B",  11, 10255.103),
    (6,  "C",  12, 11177.929),
    (7,  "N",  14, 13043.782),
    (8,  "O",  16, 14899.169),
    (9,  "F",  19, 17696.901),
    (10, "Ne", 20, 18622.835),
    (11, "Na", 23, 21414.830),
    (12, "Mg", 24, 22341.908),
    (13, "Al", 27, 25133.143),
    (14, "Si", 28, 26060.344),
    (15, "P",  31, 28851.873),
    (16, "S",  32, 29781.800),
    (17, "Cl", 35, 32573.283),
    (18, "Ar", 40, 37224.719),
    (19, "K",  39, 36294.464),
    (20, "Ca", 40, 37213.777),
]


def per_generator_log_full(Z: int, N: int) -> tuple[list[float], float]:
    """Single-gen log-volume sum α · Σ_i ln|V̂_i^full|."""
    vols = atom_per_generator_volumes(Z, N, include_inter=True)
    log_terms = []
    for v in vols:
        x = mp.mpf(v["full"])
        if abs(x) < mp.mpf("1e-30"):
            log_terms.append(0.0)
            continue
        log_terms.append(float(mp.log(abs(x))))
    return log_terms, sum(log_terms)


def pair_gen_log_wedderburn(Z: int, N: int) -> tuple[float, int]:
    """Wedderburn-coupled pair-gen log-volume sum:

        Σ_{i<j} ln |V̂_i V̂_j|_Wedderburn

    Returns (sum, n_pairs)."""
    pairs = wedderburn_pair_volumes(Z, N)
    log_sum = 0.0
    for p in pairs:
        v = mp.mpf(p["full"])
        if abs(v) < mp.mpf("1e-30"):
            continue
        log_sum += float(mp.log(abs(v)))
    return log_sum, len(pairs)


def main() -> int:
    print("=" * 96)
    print(f"  Pair-gen extension v2: WEDDERBURN-coupled pair volumes")
    print(f"  α = {ALPHA:.6f} MeV,  z² = {Z_MARKOV ** 2:.6f}")
    print("=" * 96)

    print(f"\n  {'Z':>2} {'name':<4} {'A':>3} | {'M_obs':>10} {'M_single':>10} {'err_s%':>7} | "
          f"{'pair_corr':>10} {'M_pair':>10} {'err_p%':>7}")
    print("  " + "-" * 84)

    rows = []
    abs_err_single = []
    abs_err_pair = []
    for Z, name, A, M_obs in PAPER_TABLE:
        N = A - Z
        try:
            log_terms, sum_log = per_generator_log_full(Z, N)
            pair_log_sum, n_pairs = pair_gen_log_wedderburn(Z, N)
        except Exception as exc:
            print(f"  {Z:>2} {name:<4} {A:>3}: ERROR {type(exc).__name__}: {exc}")
            continue

        constituent = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
        single_corr = float(ALPHA) * sum_log
        pair_corr = float(ALPHA) * (Z_MARKOV ** 2) * pair_log_sum
        M_single = constituent + single_corr
        M_pair = constituent + single_corr + pair_corr
        err_s = (M_single - M_obs) / M_obs * 100
        err_p = (M_pair - M_obs) / M_obs * 100

        print(f"  {Z:>2} {name:<4} {A:>3} | {M_obs:>10.3f} {M_single:>10.3f} {err_s:>+7.4f} | "
              f"{pair_corr:>+10.3f} {M_pair:>10.3f} {err_p:>+7.4f}")
        rows.append({
            "Z": Z, "name": name, "A": A,
            "M_obs_MeV": M_obs,
            "constituent_MeV": constituent,
            "single_correction_MeV": single_corr,
            "pair_correction_MeV": pair_corr,
            "n_generators": len(log_terms),
            "n_pairs": n_pairs,
            "sum_log_V_full": sum_log,
            "pair_log_sum_wedderburn": pair_log_sum,
            "M_pred_single": M_single,
            "M_pred_pair": M_pair,
            "err_pct_single": err_s,
            "err_pct_pair": err_p,
        })
        abs_err_single.append(abs(err_s))
        abs_err_pair.append(abs(err_p))

    if abs_err_single:
        mean_s = sum(abs_err_single) / len(abs_err_single)
        max_s = max(abs_err_single)
        mean_p = sum(abs_err_pair) / len(abs_err_pair)
        max_p = max(abs_err_pair)
        print(f"\n  {'Mean |err|':<15} single-gen: {mean_s:.4f}%   single+Wedderburn-pair: {mean_p:.4f}%")
        print(f"  {'Max |err|':<15} single-gen: {max_s:.4f}%   single+Wedderburn-pair: {max_p:.4f}%")
        if mean_p < mean_s:
            improvement = (mean_s - mean_p) / mean_s * 100
            print(f"\n  ✅ Wedderburn pair coupling REDUCES mean |err| from {mean_s:.4f}% to {mean_p:.4f}%")
            print(f"     ({improvement:.1f}% reduction in mean error).")
        elif mean_p < mean_s * 1.1:
            print(f"\n  ≈ Wedderburn pair coupling preserves accuracy (mean err {mean_p:.4f}% vs {mean_s:.4f}%).")
        else:
            print(f"\n  ⚠ Wedderburn pair coupling does not reduce mean error.")
            print(f"     Possibly: α · z² · Σ ln|V_i V_j|_Wedd needs different normalization,")
            print(f"     or the pair coupling structure needs further refinement (Frobenius-")
            print(f"     coupled pair amplitudes per thm:frobenius-codim-universal).")

    witness = {
        "computation": "rho-k-pair-gen-v2-wedderburn",
        "description": (
            "Pair-generator v2 extension using Wedderburn-block-coupled "
            "pair volumes |V̂_i V̂_j|_Wedderburn (`wedderburn_pair_volumes."
            "py`). The std-channel pair amplitude is the Markov-traced "
            "2x2 transfer-matrix product (M_i M_j) rather than the "
            "naive product V_i^std · V_j^std, capturing the actual "
            "braid-group non-commutativity. Tests the unified ρ_K "
            "formula M = constituent + α·Σ ln|V_i| + α·z²·Σ ln|V_iV_j|_Wedd "
            "across Z=1..20."
        ),
        "reference_blocks": [
            "prop:rho-k-graded-expansion",
            "prop:atomic-mass-gb-nf",
            "thm:wedderburn-mass-formula",
            "thm:knot-mass-formula-unified",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
            "alpha_MeV": float(ALPHA),
            "z_markov": Z_MARKOV,
            "z_squared": Z_MARKOV ** 2,
            "Z_range": [1, 20],
        },
        "rows": rows,
        "summary": {
            "mean_err_pct_single_gen": (
                sum(abs_err_single) / len(abs_err_single) if abs_err_single else None
            ),
            "max_err_pct_single_gen": (
                max(abs_err_single) if abs_err_single else None
            ),
            "mean_err_pct_with_wedderburn_pair": (
                sum(abs_err_pair) / len(abs_err_pair) if abs_err_pair else None
            ),
            "max_err_pct_with_wedderburn_pair": (
                max(abs_err_pair) if abs_err_pair else None
            ),
            "wedderburn_pair_improves": (
                sum(abs_err_pair) / len(abs_err_pair) < sum(abs_err_single) / len(abs_err_single)
                if abs_err_single and abs_err_pair else None
            ),
        },
    }
    out = HERE / "rho-k-pair-gen-v2-wedderburn.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
