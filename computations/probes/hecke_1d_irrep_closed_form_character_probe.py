#!/usr/bin/env python3
"""Probe: hecke-1d-irrep-closed-form-character
(`prop:hecke-1d-irrep-closed-form-character`).

The proposition asserts the universal closed form for the
1-dimensional irrep characters of H_n(q):

    χ^(n)_q(β)    =  q^w(β)        · ([2]_q / 2)^m(β)        (trivial)
    χ^(1^n)_q(β)  =  (-q⁻¹)^w(β)   · (-[2]_q / 2)^m(β)       (sign)

where β is encoded as a typed braid with crossings of three types
    σ_i,  σ_i⁻¹,  σ_i - h/2 · 𝟙       (h = q - q⁻¹)
and

    w(β) = #(σ_i) − #(σ_i⁻¹)        (writhe)
    m(β) = #(σ_i − h/2 · 𝟙)         (averaged crossings)
    [2]_q = q + q⁻¹

This probe verifies the closed form numerically at q = q_0 for a
suite of test braids in B_n (n = 2, 3, 4, 5) covering:
  · pure-positive words (only σ_i): writhe-only case
  · pure-negative words (only σ_i⁻¹): negative-writhe-only case
  · mixed (figure-eight β_{4_1} = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹ in B_3)
  · averaged-crossing case (σ_i - h/2 · 𝟙)
  · zero-writhe symmetric case (Coxeter element σ_1σ_2…σ_{n-1})

For each test, the 1-d irrep character is computed two ways:
  · LHS — direct trace of the H_n Hoefsmit (n)-rep (trivial) and
    (1^n)-rep (sign) at q_0 via canonical `build_hoefsmit_mpfr`.
  · RHS — closed-form q^w · ([2]_q/2)^m with the sign convention
    from the proposition.

Equality witnesses the proposition for the tested braids.  All
residues are at ~1e-50 (mpmath 50 dps).

Emits `hecke-1d-irrep-closed-form-character-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from probe_staircase_ew_k3_categorical import build_hoefsmit_mpfr  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _eval_braid_word_in_rep(sigmas, dim: int, word: list[tuple[int, int]]):
    """Evaluate a typed braid word against canonical Hoefsmit matrices.

    `word` entries are (index, type) where:
      type = +1 → σ_index
      type = −1 → σ_index⁻¹
      type =  0 → σ_index − (q − q⁻¹)/2 · 𝟙  (averaged crossing)
    """
    h_half = (Q_MP - 1 / Q_MP) / 2
    M = mp.eye(dim)
    for idx, t in word:
        if t == +1:
            g = sigmas[idx]
        elif t == -1:
            g = sigmas[idx] ** (-1)
        elif t == 0:
            g = sigmas[idx] - h_half * mp.eye(dim)
        else:
            raise ValueError(f"unknown crossing type {t!r}")
        M = M * g
    return M


def _trace(M, dim: int) -> "mp.mpf":
    return sum(M[i, i] for i in range(dim))


def _closed_form(q, w: int, m: int, alt: bool) -> "mp.mpf":
    """Universal closed form for 1-d irreps.

    `alt = False` → trivial irrep (n).
    `alt = True`  → sign irrep (1^n).
    """
    two_q = q + 1 / q
    half_two_q = two_q / 2
    if alt:
        sigma_eigenvalue = -1 / q
        averaged_eigenvalue = -half_two_q
    else:
        sigma_eigenvalue = q
        averaged_eigenvalue = half_two_q
    return (sigma_eigenvalue ** w) * (averaged_eigenvalue ** m)


# ─────────────────────────────────────────────────────────────────
# Test cases.  Each: (label, n, word).
# ─────────────────────────────────────────────────────────────────
TESTS: list[tuple[str, int, list[tuple[int, int]]]] = [
    # B_2: pure positive σ_1^3 (trefoil braid word)
    ("B_2 σ_1^3 (trefoil)", 2, [(0, +1), (0, +1), (0, +1)]),
    # B_2: pure negative σ_1^-3 (mirror trefoil)
    ("B_2 σ_1^-3 (mirror trefoil)", 2, [(0, -1), (0, -1), (0, -1)]),
    # B_3: figure-eight β_{4_1} = σ_1 σ_2^-1 σ_1 σ_2^-1 (writhe 0)
    ("B_3 β_{4_1} = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹ (writhe 0)",
     3, [(0, +1), (1, -1), (0, +1), (1, -1)]),
    # B_3: pure positive Coxeter σ_1 σ_2 (writhe 2)
    ("B_3 σ_1 σ_2 (writhe 2)",
     3, [(0, +1), (1, +1)]),
    # B_4: full positive Coxeter σ_1 σ_2 σ_3 (writhe 3)
    ("B_4 σ_1 σ_2 σ_3 (writhe 3)",
     4, [(0, +1), (1, +1), (2, +1)]),
    # B_4: mixed (writhe 1, m=0)
    ("B_4 σ_1 σ_2 σ_3⁻¹ σ_2 (writhe 2)",
     4, [(0, +1), (1, +1), (2, -1), (1, +1)]),
    # B_3: single averaged crossing σ_1 - h/2 · 𝟙 (w=0, m=1)
    ("B_3 single averaged σ_1 − h/2 (w=0, m=1)",
     3, [(0, 0)]),
    # B_3: mixed averaged + positive (w=1, m=1)
    ("B_3 σ_1 (σ_2 − h/2) (w=1, m=1)",
     3, [(0, +1), (1, 0)]),
    # B_5: longer chain (writhe = 6 − 2 = 4, m=0)
    ("B_5 σ_1 σ_2 σ_3 σ_4 σ_4⁻¹ σ_3⁻¹ σ_1 σ_2 (writhe 4)",
     5, [(0, +1), (1, +1), (2, +1), (3, +1), (3, -1),
         (2, -1), (0, +1), (1, +1)]),
]


def main() -> int:
    builder = WitnessBuilder(
        "hecke-1d-irrep-closed-form-character-probe",
        engine="mpmath",
    )
    set_compute_dps()

    results: list[dict] = []
    max_residue = mp.mpf(0)

    for label, n, word in TESTS:
        # Build canonical Hoefsmit for trivial (n) and sign (1^n).
        sig_triv, dim_triv = build_hoefsmit_mpfr((n,), Q_MP)
        sig_alt, dim_alt = build_hoefsmit_mpfr((1,) * n, Q_MP)
        assert dim_triv == 1
        assert dim_alt == 1

        # Direct trace.
        M_triv = _eval_braid_word_in_rep(sig_triv, dim_triv, word)
        M_alt = _eval_braid_word_in_rep(sig_alt, dim_alt, word)
        chi_triv_direct = _trace(M_triv, dim_triv)
        chi_alt_direct = _trace(M_alt, dim_alt)

        # Writhe and averaged count.
        w = sum(1 for _, t in word if t == +1) - \
            sum(1 for _, t in word if t == -1)
        m_av = sum(1 for _, t in word if t == 0)

        # Closed-form prediction.
        chi_triv_closed = _closed_form(Q_MP, w, m_av, alt=False)
        chi_alt_closed = _closed_form(Q_MP, w, m_av, alt=True)

        # Keep residues at mp.mpf (was float() then re-bounced via
        # mp.mpf in the max(); flagged by compute_no_mpf_to_float_cast).
        res_triv = mp.fabs(chi_triv_direct - chi_triv_closed)
        res_alt = mp.fabs(chi_alt_direct - chi_alt_closed)
        max_residue = max(max_residue, res_triv, res_alt)

        results.append({
            "label": label,
            "n": n,
            "writhe": w,
            "averaged_count": m_av,
            "chi_n_direct": float(chi_triv_direct),
            "chi_n_closed": float(chi_triv_closed),
            "chi_n_residue": res_triv,
            "chi_1n_direct": float(chi_alt_direct),
            "chi_1n_closed": float(chi_alt_closed),
            "chi_1n_residue": res_alt,
        })

    (
        builder
        .set_description(
            "I1 probe for prop:hecke-1d-irrep-closed-form-character.  "
            "Verifies the universal closed form "
            "χ^(n)(β) = q^w · ([2]_q/2)^m  and  "
            "χ^(1^n)(β) = (-q⁻¹)^w · (-[2]_q/2)^m  "
            "for the two 1-dim irreps of H_n(q), against the direct "
            "trace of the canonical H_n Hoefsmit-seminormal (n) and "
            "(1^n) reps.  9 test braids in B_2…B_5 cover pure-positive, "
            "pure-negative, mixed-writhe, zero-writhe, and "
            "averaged-crossing (σ_i − h/2·𝟙) cases.  All residues "
            "at ~1e-50 (mpmath 50 dps) witness the closed form for "
            "each test."
        )
        .set_content_block("prop:hecke-1d-irrep-closed-form-character")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("num_test_cases", len(TESTS))
        .add_parameter("max_residue_across_tests", float(max_residue))
        .add_data("per_test_results", results)
        .add_data("closed_form_recipe", {
            "trivial_irrep": "χ^(n)(β) = q^w(β) · ((q+q⁻¹)/2)^m(β)",
            "sign_irrep": "χ^(1^n)(β) = (-q⁻¹)^w(β) · (-(q+q⁻¹)/2)^m(β)",
            "writhe_def": "w(β) = #(σ_i) − #(σ_i⁻¹)",
            "averaged_count_def": "m(β) = #(σ_i − h/2·𝟙)",
            "two_q_def": "[2]_q = q + q⁻¹",
            "h_def": "h = q − q⁻¹",
        })
        .add_assertion(
            name="max_residue_across_all_tests_at_q0",
            computed=float(max_residue),
            expected=0.0,
            tolerance=1e-40,
            unit=(
                "max over {trivial, sign} × {9 test braids} of "
                "|χ_direct(β) − χ_closed_form(β)|"
            ),
            source=(
                "Universal closed form for 1-d Hecke irrep characters; "
                "direct LHS via canonical Hoefsmit-seminormal "
                "(`build_hoefsmit_mpfr` at 50 dps), closed-form RHS "
                "from the proposition statement."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'test':<60} {'w':<3} {'m':<3} {'res_(n)':<10} {'res_(1^n)':<10}")
    for r in results:
        print(f"  {r['label']:<58} "
              f"{r['writhe']:<3} {r['averaged_count']:<3} "
              f"{r['chi_n_residue']:<10.2e} {r['chi_1n_residue']:<10.2e}")
    print()
    print(f"max residue across all tests: {float(max_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
