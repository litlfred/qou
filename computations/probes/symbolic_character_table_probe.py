#!/usr/bin/env python3
"""Probe: symbolic-character-table (`prop:symbolic-character-table`).

The proposition asserts that for every partition λ of n ≤ 7, the
single-generator character χ_λ(σ) is a rational function of q
expressible as `c_λ · h` where h = q − q⁻¹ and c_λ ∈ ℚ(q²).

For self-conjugate partitions, c_λ is an integer:

| Partition  | χ_λ(σ) / h | Source rep             |
|:----------:|:----------:|:----------------------:|
| (2, 1)     | 1          | standard               |
| (3, 1, 1)  | 3          | H_5 Wigner             |
| (3, 2, 1)  | 8          | H_6 dominant (~36% Pl) |
| (4, 1, 1, 1) | 10       | H_7 self-conjugate     |

The proposition also lists pair characters (for λ = (3, 1, 1) in H_5):

  χ_(3,1,1)(σ_i σ_{i+1})            = h²             (adjacent)
  χ_(3,1,1)(σ_i σ_j),  |i−j| ≥ 2   = h² − 2         (non-adjacent)
  χ_(3,1,1)(σ_i σ_{i+1} σ_{i+2})    = −h             (Coxeter triple)

This probe verifies each of these identities numerically at q = q_0
via the canonical Hoefsmit-seminormal rep.  All residues at ~1e-50
witness the proposition's claims.

Emits `symbolic-character-table-probe.witness.json`.
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
# `build_hoefsmit_mpfr` moved: it lived in
# `_deprecated/probes/probe_staircase_ew_k3_categorical.py`, root-level agent
# scratch untracked wholesale by 0763606e4, so this import has raised
# ModuleNotFoundError and THIS PRODUCER COULD NOT RUN AT ALL since. Recovered
# from history into hecke_character_symbolic, beside the symbolic twin and the
# standard_young_tableaux it is built on.
from hecke_character_symbolic import build_hoefsmit_mpfr  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _trace(M, dim: int) -> "mp.mpf":
    return sum(M[i, i] for i in range(dim))


def _eval_word(sigmas, dim, word: list[tuple[int, int]]):
    M = mp.eye(dim)
    for idx, sgn in word:
        g = sigmas[idx] if sgn > 0 else sigmas[idx] ** (-1)
        M = M * g
    return M


def main() -> int:
    builder = WitnessBuilder(
        "symbolic-character-table-probe",
        engine="mpmath",
    )
    set_compute_dps()

    q = Q_MP
    h = q - 1 / q

    # === Self-conjugate single-generator characters ===
    # Each entry: (partition, expected c_λ).
    SELF_CONJ_CASES: list[tuple[tuple[int, ...], int]] = [
        ((2, 1), 1),
        ((3, 1, 1), 3),
        ((3, 2, 1), 8),
        ((4, 1, 1, 1), 10),
    ]

    self_conj_results: list[dict] = []
    max_self_conj_residue = mp.mpf(0)
    for shape, c_expected in SELF_CONJ_CASES:
        sigmas, dim = build_hoefsmit_mpfr(shape, q)
        M = sigmas[0]  # σ_1
        chi = _trace(M, dim)
        ratio = chi / h
        residue = float(mp.fabs(ratio - mp.mpf(c_expected)))
        max_self_conj_residue = max(max_self_conj_residue, mp.mpf(residue))
        self_conj_results.append({
            "shape": str(shape),
            "dim": dim,
            "chi_lambda_sigma_1": float(chi),
            "chi_over_h": float(ratio),
            "expected_integer": c_expected,
            "residue": residue,
        })

    # === Pair characters for λ = (3, 1, 1) in H_5 ===
    sigmas_311, dim_311 = build_hoefsmit_mpfr((3, 1, 1), q)
    assert dim_311 == 6  # |SYT((3,1,1))| = 6

    # Adjacent σ_i σ_{i+1}: pick (σ_1 σ_2) for i=1.
    M_adj = _eval_word(sigmas_311, dim_311,
                       [(0, +1), (1, +1)])
    chi_adj = _trace(M_adj, dim_311)
    chi_adj_expected = h * h  # h²
    # Keep residue at mp.mpf precision (no float() — flagged by
    # compute_no_mpf_to_float_cast). Downstream comparison works
    # natively with mp.mpf.
    res_adj = mp.fabs(chi_adj - chi_adj_expected)

    # Non-adjacent σ_i σ_j with |i-j| ≥ 2: pick (σ_1 σ_3).
    M_nonadj = _eval_word(sigmas_311, dim_311,
                          [(0, +1), (2, +1)])
    chi_nonadj = _trace(M_nonadj, dim_311)
    chi_nonadj_expected = h * h - mp.mpf(2)
    res_nonadj = mp.fabs(chi_nonadj - chi_nonadj_expected)

    # Coxeter triple σ_i σ_{i+1} σ_{i+2}: σ_1 σ_2 σ_3.
    M_triple = _eval_word(sigmas_311, dim_311,
                          [(0, +1), (1, +1), (2, +1)])
    chi_triple = _trace(M_triple, dim_311)
    chi_triple_expected = -h
    res_triple = mp.fabs(chi_triple - chi_triple_expected)

    pair_results = {
        "lambda": "(3, 1, 1)",
        "adjacent_pair_chi_value": float(chi_adj),
        "adjacent_pair_chi_expected_h2": float(chi_adj_expected),
        "adjacent_pair_residue": res_adj,
        "nonadjacent_pair_chi_value": float(chi_nonadj),
        "nonadjacent_pair_chi_expected_h2_minus_2":
            float(chi_nonadj_expected),
        "nonadjacent_pair_residue": res_nonadj,
        "coxeter_triple_chi_value": float(chi_triple),
        "coxeter_triple_chi_expected_minus_h":
            float(chi_triple_expected),
        "coxeter_triple_residue": res_triple,
    }

    (
        builder
        .set_description(
            "I1 probe for prop:symbolic-character-table.  Verifies "
            "the single-generator character ratios χ_λ(σ)/h for "
            "self-conjugate λ ∈ {(2,1), (3,1,1), (3,2,1), (4,1,1,1)} "
            "are integers {1, 3, 8, 10} respectively, and the three "
            "pair-character identities for λ = (3,1,1) in H_5: "
            "χ(σ_i σ_{i+1}) = h², χ(σ_i σ_j) = h² − 2 for |i−j| ≥ 2, "
            "χ(σ_i σ_{i+1} σ_{i+2}) = −h.  LHS computed via canonical "
            "Hoefsmit-seminormal (mpmath, 50 dps); RHS from the "
            "proposition's symbolic closed forms with h = q − q⁻¹."
        )
        .set_content_block("prop:symbolic-character-table")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("h_at_q0", float(h))
        .add_parameter("max_self_conj_residue",
                       float(max_self_conj_residue))
        .add_data("self_conjugate_single_generator_table",
                  self_conj_results)
        .add_data("pair_character_identities_lambda_311", pair_results)
        .add_assertion(
            name="self_conjugate_chi_over_h_are_integers",
            computed=float(max_self_conj_residue),
            expected=0.0,
            tolerance=1e-40,
            unit=(
                "max over {(2,1), (3,1,1), (3,2,1), (4,1,1,1)} of "
                "|χ_λ(σ_1)/h − c_λ|, c_λ ∈ {1, 3, 8, 10}"
            ),
            source=(
                "Hoefsmit-seminormal single-generator character; "
                "claim that c_λ = χ_λ(σ)/h ∈ ℤ for self-conjugate λ."
            ),
        )
        .add_assertion(
            name="pair_character_311_adjacent_equals_h_squared",
            computed=res_adj,
            expected=0.0, tolerance=1e-40,
            unit="|χ_(3,1,1)(σ_1 σ_2) − h²|",
            source="prop:symbolic-character-table pair-character row.",
        )
        .add_assertion(
            name="pair_character_311_nonadjacent_equals_h_squared_minus_2",
            computed=res_nonadj,
            expected=0.0, tolerance=1e-40,
            unit="|χ_(3,1,1)(σ_1 σ_3) − (h² − 2)|",
            source="prop:symbolic-character-table pair-character row.",
        )
        .add_assertion(
            name="coxeter_triple_311_equals_minus_h",
            computed=res_triple,
            expected=0.0, tolerance=1e-40,
            unit="|χ_(3,1,1)(σ_1 σ_2 σ_3) − (−h)|",
            source="prop:symbolic-character-table Coxeter-triple row.",
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print("Self-conjugate single-generator characters χ_λ(σ_1)/h:")
    print(f"{'shape':<15} {'dim':<5} {'χ/h':<20} {'expected':<10} {'residue':<10}")
    for r in self_conj_results:
        print(f"  {r['shape']:<13} {r['dim']:<5} "
              f"{r['chi_over_h']:<20.15f} {r['expected_integer']:<10} "
              f"{r['residue']:.2e}")
    print()
    print(f"Pair characters for λ = (3,1,1):")
    print(f"  adjacent σ_1 σ_2:      χ = {float(chi_adj):.12f},  expected h² = {float(chi_adj_expected):.12f},  res = {res_adj:.2e}")
    print(f"  non-adj σ_1 σ_3:       χ = {float(chi_nonadj):.12f},  expected h²−2 = {float(chi_nonadj_expected):.12f},  res = {res_nonadj:.2e}")
    print(f"  Coxeter σ_1 σ_2 σ_3:   χ = {float(chi_triple):.12f},  expected −h = {float(chi_triple_expected):.12f},  res = {res_triple:.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
