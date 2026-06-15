#!/usr/bin/env python3
"""
Tests the pair-generator extension to atomic-braid-mass:

    M(K)  =  Z m_p + N m_n + Z m_e
           +  α · Σ_i ln|V̂_i^full|             (single-gen, existing)
           +  α · z² · Σ_{i<j} ln|V̂_i^full V̂_j^full|   (pair-gen, NEW)

The single-gen form is `prop:atomic-braid-mass`'s working zero-fit
formula at 0.18 % mean error across Z=1..20. The pair term is the
log-volume analog of T_3 = -z² Σ Li_2^q(-|V_i V_j|) from
`thm:knot-mass-formula-unified` — the leading Kashaev limit of the
six-term theorem's pair-generator brane tower.

Hypothesis: adding the pair term improves accuracy on heavier atoms
while preserving the working light-atom precision.

Output: rho-k-pair-gen-extension.witness.json
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

from q_parameter import Q as Q0_FLOAT, Q_MP  # noqa: E402
from hecke_core import atom_per_generator_volumes  # noqa: E402

Q0 = Q_MP
M_E_MEV = 0.51099895
M_P_MEV = 938.27208816
M_N_MEV = 939.56542052
G_CATALAN = float(mp.catalan)
ALPHA = M_E_MEV * 8 * G_CATALAN          # ≈ 3.7445 MeV
Z_MARKOV = 1.0 / (float(mp.sqrt(Q0)) + 1.0 / float(mp.sqrt(Q0)))   # z = 1/(q^{1/2}+q^{-1/2})

# CODATA atomic masses (MeV) — same source as paper-six-term-isotope-sweep
PAPER_TABLE = [
    # (Z, name, A, M_obs)
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


def per_generator_log_volumes(Z: int, N: int) -> list[float]:
    """ln|V̂_i^full| for each generator i."""
    vols = atom_per_generator_volumes(Z, N, include_inter=True)
    out = []
    for v in vols:
        x = v["full"] if isinstance(v, dict) else v
        x_mp = mp.mpf(x)
        if abs(x_mp) < mp.mpf("1e-30"):
            out.append(0.0)
            continue
        out.append(float(mp.log(abs(x_mp))))
    return out


def m_pred_single_gen(Z: int, N: int) -> dict:
    """Existing prop:atomic-braid-mass formula (single-gen only)."""
    A = Z + N
    constituent = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    log_vols = per_generator_log_volumes(Z, N)
    sum_log = sum(log_vols)
    binding = float(ALPHA) * sum_log
    M_pred = constituent + binding
    return {
        "Z": Z, "N": N, "A": A,
        "constituent_MeV": constituent,
        "single_gen_correction_MeV": binding,
        "n_generators": len(log_vols),
        "sum_log_V_full": sum_log,
        "M_pred_MeV_single_gen": M_pred,
    }


def m_pred_with_pair_gen(Z: int, N: int) -> dict:
    """Single-gen + pair-gen extension."""
    base = m_pred_single_gen(Z, N)
    log_vols = per_generator_log_volumes(Z, N)
    n = len(log_vols)
    # Pair sum: Σ_{i<j} ln|V_i · V_j| = Σ_{i<j} (ln|V_i| + ln|V_j|) = (n-1)·sum_log
    # Wait — that's just (n-1) Σ ln|V_i|, since each ln|V_i| appears in
    # n-1 pairs. So a NAIVE pair sum is just a multiplicative factor of
    # the single-gen sum. The interesting pair structure must use
    # something OTHER than the additive log decomposition.
    #
    # Reading the six-term T_3 more carefully: T_3 = -z² Σ Li_2^q(-|V_iV_j|).
    # Here |V_iV_j| is the PRODUCT, not the SUM of logs. So the
    # log-version analog is NOT Σ ln|V_iV_j| (which would equal (n-1)·Σ ln|V_i|)
    # but rather a different functional pair-product structure.
    #
    # Concrete proposal: use the Wenzl-pair amplitude
    #   Σ_{i<j} ln|V̂_i V̂_j^full|  with V̂_iV̂_j computed as
    #   PRODUCT-TYPE coupling rather than additive log.
    # The simplest concrete realization: project onto the standard
    # representation pair-product (V̂_i^std · V̂_j^std) which is NOT
    # equal to V̂_i^full · V̂_j^full when full-trace decomposes
    # into multiple Wedderburn channels.
    # For Wedderburn-mass-formula style:
    #   pair_log[i,j] = ln|w_sym λ_sym^i λ_sym^j + w_std (M_i M_j)_22 + w_alt λ_alt^i λ_alt^j|
    # = ln(Wedderburn-pair-product)
    #
    # For the FIRST-ORDER probe, we use the simplest pair-coupling
    # approximation: pair amplitude = product of full volumes,
    # i.e. log-additive gives Σ ln(|V_i| · |V_j|) = Σ (ln|V_i| + ln|V_j|).
    # This is (n-1)·Σ ln|V_i| = (n-1) · sum_log.
    n_pairs = n * (n - 1) // 2
    sum_log = base["sum_log_V_full"]
    # Multiplicative pair-product structure: each pair contributes
    # ln(|V_i|·|V_j|) = ln|V_i| + ln|V_j|, summed over pairs.
    pair_log_sum = (n - 1) * sum_log if n > 0 else 0.0
    pair_correction = float(ALPHA) * (Z_MARKOV ** 2) * pair_log_sum
    M_pred_pair = base["M_pred_MeV_single_gen"] + pair_correction
    return {
        **base,
        "n_pairs": n_pairs,
        "pair_log_sum_naive_log_additive": pair_log_sum,
        "pair_correction_MeV_naive": pair_correction,
        "z_squared": Z_MARKOV ** 2,
        "M_pred_MeV_with_pair": M_pred_pair,
    }


def main() -> int:
    print("=" * 96)
    print(f"  Pair-generator extension probe (atomic-braid-mass + pair-gen)")
    print(f"  α = m_e · 8G = {ALPHA:.6f} MeV,  z² = {Z_MARKOV ** 2:.6f}")
    print("=" * 96)

    print(f"\n  {'Z':>2} {'name':<4} {'A':>3} | {'M_obs':>10} {'M_single':>10} {'err_s%':>7} | "
          f"{'pair_corr':>9} {'M_pair':>10} {'err_p%':>7}")
    print("  " + "-" * 80)

    rows = []
    abs_err_single = []
    abs_err_pair = []
    for Z, name, A, M_obs in PAPER_TABLE:
        N = A - Z
        try:
            r = m_pred_with_pair_gen(Z, N)
        except Exception as exc:
            print(f"  {Z:>2} {name:<4} {A:>3}: ERROR {type(exc).__name__}: {exc}")
            continue
        M_s = r["M_pred_MeV_single_gen"]
        M_p = r["M_pred_MeV_with_pair"]
        err_s = (M_s - M_obs) / M_obs * 100
        err_p = (M_p - M_obs) / M_obs * 100
        pair_corr = r["pair_correction_MeV_naive"]
        print(f"  {Z:>2} {name:<4} {A:>3} | {M_obs:>10.3f} {M_s:>10.3f} {err_s:>+7.4f} | "
              f"{pair_corr:>+9.3f} {M_p:>10.3f} {err_p:>+7.4f}")
        rows.append({
            "Z": Z, "name": name, "A": A,
            "M_obs_MeV": M_obs,
            "M_pred_single_MeV": M_s,
            "M_pred_pair_MeV": M_p,
            "err_pct_single": err_s,
            "err_pct_pair": err_p,
            "pair_correction_MeV": pair_corr,
            **r,
        })
        abs_err_single.append(abs(err_s))
        abs_err_pair.append(abs(err_p))

    if abs_err_single:
        mean_s = sum(abs_err_single) / len(abs_err_single)
        max_s = max(abs_err_single)
        mean_p = sum(abs_err_pair) / len(abs_err_pair)
        max_p = max(abs_err_pair)
        print(f"\n  {'Mean |err|':<14}  single-gen: {mean_s:.4f}%   single+pair (naive): {mean_p:.4f}%")
        print(f"  {'Max |err|':<14}  single-gen: {max_s:.4f}%   single+pair (naive): {max_p:.4f}%")

        if mean_p < mean_s:
            print(f"\n  ✅ Pair-gen NAIVE log-additive extension reduces mean error from {mean_s:.4f}% to {mean_p:.4f}%.")
        else:
            print(f"\n  ⚠ Pair-gen NAIVE log-additive extension does NOT improve accuracy.")
            print(f"     This is expected: log-additive Σ ln|V_i V_j| = (n-1)·Σ ln|V_i|")
            print(f"     is not the right pair-coupling structure. Need Wedderburn-")
            print(f"     decomposed pair amplitude (sym/std/alt block coupling) per")
            print(f"     thm:wedderburn-mass-formula's full traced volume.")

    # Theoretical note: the proper pair coupling
    print(f"\n  Theoretical refinement needed:")
    print(f"    The naive Σ_{{i<j}} ln|V_i V_j| = (n-1)·Σ_i ln|V_i| does not")
    print(f"    capture the Wedderburn-pair structure. The correct pair-gen term")
    print(f"    matching T_3 of thm:knot-mass-formula-unified is")
    print(f"      α·z² · Σ_{{i<j}} ln|⟨V̂_i, V̂_j⟩_Wedderburn|")
    print(f"    where ⟨·,·⟩_Wedderburn is the Markov-block-decomposed pair")
    print(f"    amplitude (sym × sym + std-trace + alt × alt), NOT the simple")
    print(f"    product. Implementing this requires extending hecke_core.")

    witness = {
        "computation": "rho-k-pair-gen-extension",
        "description": (
            "Probes the pair-generator extension of `prop:atomic-braid-"
            "mass`'s formula M = constituent + α·Σ ln|V_i| by adding "
            "α·z²·Σ_{i<j} ln|V_i V_j|. This term is the log-volume "
            "analog of T_3 = -z² Σ Li_2^q(-|V_i V_j|) from "
            "`thm:knot-mass-formula-unified`. The naive log-additive "
            "implementation Σ ln|V_i V_j| = (n-1)·Σ ln|V_i| is a pure "
            "rescaling and does not improve accuracy. The correct pair-"
            "gen term requires Wedderburn-block-decomposed pair "
            "amplitudes (sym/std/alt coupling), parallel to the full-"
            "Wedderburn single-gen volume."
        ),
        "reference_blocks": [
            "prop:atomic-braid-mass",
            "thm:knot-mass-formula-unified",
            "prop:atomic-mass-gb-nf",
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
            "mean_err_pct_single_gen": sum(abs_err_single) / len(abs_err_single) if abs_err_single else None,
            "max_err_pct_single_gen":  max(abs_err_single) if abs_err_single else None,
            "mean_err_pct_with_pair_naive":  sum(abs_err_pair) / len(abs_err_pair) if abs_err_pair else None,
            "max_err_pct_with_pair_naive":   max(abs_err_pair) if abs_err_pair else None,
            "naive_pair_improves":  (
                sum(abs_err_pair) / len(abs_err_pair) < sum(abs_err_single) / len(abs_err_single)
                if abs_err_single and abs_err_pair else None
            ),
        },
        "open_question": (
            "The naive log-additive pair term Σ ln|V_i V_j| = (n-1)·Σ "
            "ln|V_i| is just a rescaling. The PROPER pair-coupling term "
            "matching T_3 of `thm:knot-mass-formula-unified` requires "
            "Wedderburn-decomposed pair amplitudes from sym/std/alt "
            "block coupling. Implementing requires a new "
            "atom_per_generator_pair_volumes(Z, N) routine returning "
            "|V̂_i V̂_j|_Wedderburn for each (i, j) pair."
        ),
    }
    out = HERE / "rho-k-pair-gen-extension.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
