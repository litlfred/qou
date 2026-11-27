#!/usr/bin/env python3
"""Probe: frobenius-gram-matrix (`prop:frobenius-gram-matrix`) — 80-dps mpmath.

Verifies the structural properties of the Convention-D Markov-trace pairings on
the NF basis b in {gamma = 1, sigma_0, sigma_1, L_+ = sigma_0 sigma_1,
L_- = sigma_1 sigma_0, e^- = sigma_0 sigma_1 sigma_0} of H_3(R, q) at z = z_D
= q^3/(q^2 + 1), h = q - q^-1:

  (1) **Single-element traces** match the corrected closed forms
      (post-Markov-bug fix per audit 2026-05-19-trm5-markov-bug):
        tr_M(1) = 1
        tr_M(sigma_0) = tr_M(sigma_1) = z_D
        tr_M(L_+) = tr_M(L_-) = z_D^2
        tr_M(e^-) = h z_D^2 + z_D       (NOT z_D^3 — that was the bug)

  (2) **Symmetry**: G_{ij} = G_{ji} (by cyclicity of tr_M on [K^{otimes 3}, -] = 0).

  (3) **Degeneracy on H_3(q) vs non-degeneracy on TL_3(q)**: under Convention D,
      the (1^3) Wedderburn weight y_{(1^3)} = 0 symbolically, so det G = 0
      identically on 6D H_3(q) with 1D radical spanned by the q-antisymmetriser
      sum_w (-q^-1)^{len(w)} T_w (induced form non-degenerate on 5D TL_3(q)).
      The historical assertion ``gram_matrix_nondegenerate`` records this
      failure on full 6D H_3(q) (matching ``frobenius-gram-matrix.ts``).

  (4) **Bilinear vs Hecke *-Gram signature (TN-9 / qou-v4iw)**:
      - No-star bilinear G_{ij} = tr_M(b_i * b_j) has indefinite signature
        (4+, 1-, 1 zero) with negative mode -0.75270211... on (L_+ - L_-)/sqrt(2)
        and radical at argmin(|w|) (NOT w[0]!).
      - Hecke *-Gram S_{ij} = tr_M(b_i * b_j^*) (T_w^* = T_{w^-1}, swapping
        L_+ <-> L_-) is positive semidefinite of signature (5+, 0-, 1 zero).

Emits `frobenius-gram-matrix-probe.witness.json` at >= 60-dps output precision
(zero float64 casts).
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate import fmt, q_at, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from markov_trace_recursive import (  # noqa: E402
    markov_trace_of_word, q as Q_SYM,
)

WORK_DPS = 80

# NF basis as 1-indexed signed words (sigma_0 <-> 1, sigma_1 <-> 2).
NF_BASIS_WORDS: list[tuple[str, list[int]]] = [
    ("γ = 𝟙",                []),
    ("σ_0",                   [1]),
    ("σ_1",                   [2]),
    ("L_+ = σ_0 σ_1",         [1, 2]),
    ("L_- = σ_1 σ_0",         [2, 1]),
    ("e^- = σ_0 σ_1 σ_0",     [1, 2, 1]),
]


def _eval_at_q0(expr: Any, q_sympy: Any | None = None) -> mp.mpf:
    """Evaluate sympy expression at q = q_0 with 75+ dps (zero float64)."""
    if q_sympy is None:
        q0_mp = q_at(WORK_DPS)
        q_sympy = sp.Float(mp.nstr(q0_mp, WORK_DPS), WORK_DPS)
    return mp.mpf(str(sp.N(expr.subs(Q_SYM, q_sympy), WORK_DPS - 5)))


def main() -> int:
    set_compute_dps(WORK_DPS)
    mp.dps = WORK_DPS

    builder = WitnessBuilder(
        "frobenius-gram-matrix-probe",
        engine="sympy+mpmath",
    )

    q0_mp = q_at(WORK_DPS)
    q_sympy = sp.Float(mp.nstr(q0_mp, WORK_DPS), WORK_DPS)
    z_sym = Q_SYM ** 3 / (Q_SYM ** 2 + 1)
    h_sym = Q_SYM - 1 / Q_SYM
    z = _eval_at_q0(z_sym, q_sympy)
    h = _eval_at_q0(h_sym, q_sympy)

    # (1) Single-element trace check.
    expected_traces = [
        ("γ = 𝟙", mp.mpf(1)),
        ("σ_0", z),
        ("σ_1", z),
        ("L_+", z * z),
        ("L_-", z * z),
        ("e^-", h * z * z + z),
    ]
    single_trace_results = []
    max_single_residue = mp.mpf(0)
    q_pos = sp.symbols("q", positive=True)
    for (label, word), (_, expected) in zip(NF_BASIS_WORDS, expected_traces):
        sym_expr = markov_trace_of_word(3, word)
        got = _eval_at_q0(sym_expr, q_sympy)
        residue = mp.fabs(got - expected)
        if residue > max_single_residue:
            max_single_residue = residue
        single_trace_results.append({
            "basis_element": label,
            "expected_closed_form": str(sp.cancel(sym_expr.subs(Q_SYM, q_pos))),
            "expected_at_q0": fmt(expected),
            "computed_at_q0": fmt(got),
            "residue": fmt(residue),
        })

    # (2)–(4) Bilinear Gram G_{ij} = tr_M(b_i * b_j) and Hecke *-Gram S_{ij} = tr_M(b_i * b_j^*).
    n_basis = len(NF_BASIS_WORDS)
    G = mp.matrix(n_basis, n_basis)
    S = mp.matrix(n_basis, n_basis)
    for i, (_, wi) in enumerate(NF_BASIS_WORDS):
        for j, (_, wj) in enumerate(NF_BASIS_WORDS):
            sym_bil = markov_trace_of_word(3, wi + wj)
            sym_star = markov_trace_of_word(3, wi + list(reversed(wj)))
            G[i, j] = _eval_at_q0(sym_bil, q_sympy)
            S[i, j] = _eval_at_q0(sym_star, q_sympy)

    symmetry_resid = mp.mpf(0)
    for i in range(n_basis):
        for j in range(i + 1, n_basis):
            diff = mp.fabs(G[i, j] - G[j, i])
            if diff > symmetry_resid:
                symmetry_resid = diff

    det_G = mp.det(G)
    det_S = mp.det(S)

    zero_thresh = mp.mpf("1e-50")
    eig_bil = sorted(mp.eigsy(G)[0])
    eig_star = sorted(mp.eigsy(S)[0])

    n_positive = sum(1 for e in eig_bil if e > zero_thresh)
    n_negative = sum(1 for e in eig_bil if e < -zero_thresh)
    n_zero = n_basis - n_positive - n_negative
    is_indefinite = (n_positive > 0 and n_negative > 0)
    is_nondegenerate = (n_zero == 0) and (mp.fabs(det_G) > zero_thresh)

    n_pos_star = sum(1 for e in eig_star if e > zero_thresh)
    n_neg_star = sum(1 for e in eig_star if e < -zero_thresh)
    n_zero_star = n_basis - n_pos_star - n_neg_star
    star_is_psd_5_0_1 = (n_pos_star == 5 and n_neg_star == 0 and n_zero_star == 1)

    # Exact radical vector (-q^-1)^len(w) check under both G and S, and argmin(|w|) index.
    qi0 = mp.mpf(1) / q0_mp
    rad_vec = [(-qi0) ** len(w) for _, w in NF_BASIS_WORDS]
    rad_resid_G = max(
        mp.fabs(mp.fsum(G[r, c] * rad_vec[c] for c in range(n_basis)))
        for r in range(n_basis)
    )
    rad_resid_S = max(
        mp.fabs(mp.fsum(S[r, c] * rad_vec[c] for c in range(n_basis)))
        for r in range(n_basis)
    )
    rad_resid_max = max(rad_resid_G, rad_resid_S)
    idx_null_bil = min(range(n_basis), key=lambda k: mp.fabs(eig_bil[k]))
    idx_null_star = min(range(n_basis), key=lambda k: mp.fabs(eig_star[k]))

    tol_tight = mp.mpf("1e-55")
    zero_mp = mp.mpf(0)
    one_mp = mp.mpf(1)

    (
        builder
        .set_description(
            "I1 probe for prop:frobenius-gram-matrix (80-dps mpmath, zero float64). "
            "Verifies on H_3(R, q) at Convention D (z_D = q^3/(q^2 + 1)): "
            "(1) single-element traces match (1, z, z, z^2, z^2, h z^2 + z); "
            "(2) G is symmetric; "
            "(3) det G = 0 identically on 6D H_3(q) with 1D radical (-q^-1)^len(w) "
            "(non-degenerate on 5D TL_3(q)); "
            "(4) bilinear G_{ij} = tr_M(b_i b_j) has signature (4+, 1-, 1 zero) with "
            "radical at argmin(|w|) = 1 (w[0] = -0.75270211... on (L_+ - L_-)/sqrt(2)), "
            "whereas Hecke *-Gram S_{ij} = tr_M(b_i b_j^*) has PSD signature (5+, 0-, 1 zero)."
        )
        .set_content_block("prop:frobenius-gram-matrix")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("z_at_q0", fmt(z))
        .add_parameter("h_at_q0", fmt(h))
        .add_parameter("max_single_trace_residue", fmt(max_single_residue))
        .add_parameter("symmetry_residue", fmt(symmetry_resid))
        .add_parameter("det_G_at_q0", fmt(det_G))
        .add_parameter("det_S_star_at_q0", fmt(det_S))
        .add_parameter("num_positive_eigenvalues", n_positive)
        .add_parameter("num_negative_eigenvalues", n_negative)
        .add_parameter("num_zero_eigenvalues", n_zero)
        .add_parameter("idx_null_bilinear_argmin_abs", idx_null_bil)
        .add_parameter("idx_null_star_argmin_abs", idx_null_star)
        .add_parameter("star_gram_signature", [n_pos_star, n_neg_star, n_zero_star])
        .add_parameter("is_indefinite", is_indefinite)
        .add_parameter("is_nondegenerate", is_nondegenerate)
        .add_data("single_element_traces", single_trace_results)
        .add_data("gram_matrix_eigenvalues", [fmt(e) for e in eig_bil])
        .add_data("star_gram_matrix_eigenvalues", [fmt(e) for e in eig_star])
        .add_data("radical_annihilation", {
            "radical_formula": "(-q^-1)^len(w) over NF_BASIS_WORDS",
            "max_abs_G_mul_rad": fmt(rad_resid_G),
            "max_abs_S_mul_rad": fmt(rad_resid_S),
        })
        .add_data("notes", {
            "errata_fix_propagated":
                "tr_M(e^-) corrected from stale z^3 to canonical h z^2 + z",
            "pairing_distinction":
                "bilinear tr_M(b_i b_j) is (4+, 1-, 1 zero); Hecke *-Gram tr_M(b_i b_j^*) is PSD (5+, 0-, 1 zero)",
            "audit_reference":
                "docs/audits/2026-05-19-trm5-markov-bug.md",
        })
        .add_assertion(
            name="single_element_traces_match_closed_forms",
            computed=max_single_residue,
            expected=zero_mp,
            tolerance=tol_tight,
            unit="max over {1, sigma_0, sigma_1, L_+, L_-, e^-} of |tr_M(b) - closed_form(b)|",
            source="Ocneanu-Wenzl recursion + Hecke quadratic + Markov axiom.",
        )
        .add_assertion(
            name="gram_matrix_symmetric",
            computed=symmetry_resid,
            expected=zero_mp,
            tolerance=tol_tight,
            unit="max over (i,j) of |G_{ij} - G_{ji}|",
            source="Cyclicity of the Markov trace tr_M(ab) = tr_M(ba).",
        )
        .add_assertion(
            name="gram_matrix_nondegenerate",
            computed=zero_mp if is_nondegenerate else one_mp,
            expected=zero_mp,
            tolerance=zero_mp,
            unit="boolean (0 = non-degenerate, 1 = degenerate)",
            source=(
                "Intentional negative witness on 6D H_3(q): under Convention D "
                "(z = q^3/(q^2 + 1)), y_{(1^3)} = 0 gives a 1D radical so det G = 0 "
                "(non-degenerate only on 5D quotient TL_3(q))."
            ),
        )
        .add_assertion(
            name="gram_matrix_indefinite_signature",
            computed=zero_mp if is_indefinite else one_mp,
            expected=zero_mp,
            tolerance=zero_mp,
            unit="boolean (0 = bilinear G has both positive and negative eigvals, 1 = same-sign)",
            source="Bilinear no-star pairing G_{ij} = tr_M(b_i b_j) has signature (4+, 1-, 1 zero).",
        )
        .add_assertion(
            name="star_gram_psd_5_0_1",
            computed=zero_mp if star_is_psd_5_0_1 else one_mp,
            expected=zero_mp,
            tolerance=zero_mp,
            unit="boolean (0 = Hecke *-Gram S has PSD signature (5+, 0-, 1 zero), 1 = otherwise)",
            source="Hecke *-involution T_w^* = T_{w^-1} swaps L_+ <-> L_- and gives PSD (5+, 0-, 1 zero).",
        )
        .add_assertion(
            name="radical_annihilated_by_both_pairings",
            computed=rad_resid_max,
            expected=zero_mp,
            tolerance=tol_tight,
            unit="max(||G @ rad||_inf, ||S @ rad||_inf)",
            source="3-strand q-antisymmetriser (-q^-1)^len(w) spans the 1D Convention-D radical.",
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"z_D at q_0 = {mp.nstr(z, 18)},  h at q_0 = {mp.nstr(h, 18)}")
    print()
    print("Single-element traces:")
    print(f"{'basis':<25} {'expected':<24} {'computed':<24} {'residue':<12}")
    for r in single_trace_results:
        print(
            f"  {r['basis_element']:<23} "
            f"{r['expected_at_q0'][:20]:<24} "
            f"{r['computed_at_q0'][:20]:<24} "
            f"{r['residue'][:12]}"
        )
    print()
    print("Gram matrix properties (80-dps mpmath):")
    print(f"  symmetry residue: {mp.nstr(symmetry_resid, 6)}")
    print(f"  det G (bilinear) = {mp.nstr(det_G, 6)}   idx_null = {idx_null_bil}")
    print(f"  bilinear eigs: {[mp.nstr(e, 10) for e in eig_bil]}")
    print(f"  bilinear sig : ({n_positive}+, {n_negative}-, {n_zero} zero)")
    print(f"  det S (*-Gram)   = {mp.nstr(det_S, 6)}   idx_null = {idx_null_star}")
    print(f"  *-Gram eigs  : {[mp.nstr(e, 10) for e in eig_star]}")
    print(f"  *-Gram sig   : ({n_pos_star}+, {n_neg_star}-, {n_zero_star} zero)")
    print(f"  max(||G rad||, ||S rad||) = {mp.nstr(rad_resid_max, 6)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
