#!/usr/bin/env python3
"""Probe: frobenius-gram-matrix (`prop:frobenius-gram-matrix`).

Verifies the structural properties of the Markov-trace Gram matrix

    G_{ij}  =  tr_M(b_i · b_j),

with NF basis b ∈ {γ = 𝟙, σ_0, σ_1, L_+ = σ_0σ_1, L_- = σ_1σ_0,
e^- = σ_0σ_1σ_0} of H_3(R, q):

  (1) **Single-element traces** match the corrected closed forms
      (post-Markov-bug fix per audit 2026-05-19-trm5-markov-bug):
        tr_M(𝟙) = 1
        tr_M(σ_0) = tr_M(σ_1) = z
        tr_M(L_+) = tr_M(L_-) = z²
        tr_M(e^-) = h z² + z         (NOT z³ — that was the bug)
      where z = 1/(√q + 1/√q), h = q − q⁻¹.

  (2) **Gram matrix is symmetric**: G_{ij} = G_{ji} (by cyclicity
      of tr_M).

  (3) **Gram matrix is non-degenerate**: det G ≠ 0 at q_0.

  (4) **Gram matrix has indefinite signature**: eigenvalues are
      not all of the same sign (i.e., G is NOT positive definite).

Emits `frobenius-gram-matrix-probe.witness.json`.
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

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from markov_trace_recursive import (  # noqa: E402
    markov_trace_of_word, q as Q_SYM,
)


# NF basis as 1-indexed signed words.  The proposition uses
# σ_0, σ_1 (0-indexed); the recursive reducer uses 1-indexed
# generators σ_1, σ_2.  Translation: σ_0 ↔ index 1, σ_1 ↔ index 2.
NF_BASIS_WORDS: list[tuple[str, list[int]]] = [
    ("γ = 𝟙",                []),
    ("σ_0",                   [1]),
    ("σ_1",                   [2]),
    ("L_+ = σ_0 σ_1",         [1, 2]),
    ("L_- = σ_1 σ_0",         [2, 1]),
    ("e^- = σ_0 σ_1 σ_0",     [1, 2, 1]),
]


def _eval_at_q0(expr) -> "mp.mpf":
    """Evaluate sympy expression at q = q_0 with 50 dps."""
    q_sympy = sp.Float(Q_50_DIGIT_STR, 50)
    return mp.mpf(str(sp.N(expr.subs(Q_SYM, q_sympy), 40)))


def main() -> int:
    builder = WitnessBuilder(
        "frobenius-gram-matrix-probe",
        engine="sympy+mpmath",
    )
    mp.dps = 50

    q_sympy = sp.Float(Q_50_DIGIT_STR, 50)
    z_sym = 1 / (sp.sqrt(Q_SYM) + 1 / sp.sqrt(Q_SYM))
    h_sym = Q_SYM - 1 / Q_SYM
    z = _eval_at_q0(z_sym)
    h = _eval_at_q0(h_sym)

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
    for (label, word), (lbl, expected) in zip(NF_BASIS_WORDS,
                                                expected_traces):
        sym_expr = markov_trace_of_word(3, word)
        got = _eval_at_q0(sym_expr)
        residue = float(mp.fabs(got - expected))
        max_single_residue = max(max_single_residue, mp.mpf(residue))
        single_trace_results.append({
            "basis_element": label,
            "expected_closed_form": str(sp.cancel(
                sym_expr.subs(Q_SYM,
                              sp.symbols("q", positive=True)))),
            "expected_at_q0": float(expected),
            "computed_at_q0": float(got),
            "residue": residue,
        })

    # (2)–(4) Gram matrix.
    n_basis = len(NF_BASIS_WORDS)
    G = mp.matrix(n_basis, n_basis)
    for i, (li, wi) in enumerate(NF_BASIS_WORDS):
        for j, (lj, wj) in enumerate(NF_BASIS_WORDS):
            # b_i · b_j  in the Hecke algebra (concatenate words).
            combined = wi + wj
            sym = markov_trace_of_word(3, combined)
            G[i, j] = _eval_at_q0(sym)

    # Symmetry: G_{ij} − G_{ji} = 0.
    symmetry_resid = mp.mpf(0)
    for i in range(n_basis):
        for j in range(i + 1, n_basis):
            symmetry_resid = max(symmetry_resid,
                                  mp.fabs(G[i, j] - G[j, i]))

    # Non-degeneracy: det G ≠ 0.
    det_G = mp.det(G)

    # Signature: count positive vs negative eigenvalues.
    eigs = mp.eig(G)[0]
    eig_floats = [float(e) for e in eigs]
    n_positive = sum(1 for e in eig_floats if e > 1e-30)
    n_negative = sum(1 for e in eig_floats if e < -1e-30)
    n_zero = n_basis - n_positive - n_negative
    is_indefinite = (n_positive > 0 and n_negative > 0)
    is_nondegenerate = (n_zero == 0) and (abs(float(det_G)) > 1e-30)

    (
        builder
        .set_description(
            "I1 probe for prop:frobenius-gram-matrix.  Verifies the "
            "6×6 Markov-trace Gram matrix G_{ij} = tr_M(b_i · b_j) "
            "over the NF basis {𝟙, σ_0, σ_1, L_+, L_-, e^-} of "
            "H_3(R, q): (1) the six single-element traces match the "
            "corrected closed forms (1, z, z, z², z², hz² + z) at "
            "q_0; (2) G is symmetric to ~1e-40; (3) det G ≠ 0 "
            "(non-degenerate); (4) signature is indefinite (G has "
            "both positive and negative eigenvalues).  Reproduces "
            "the corrected Gram-matrix structure after the "
            "Markov-bug fix in audit 2026-05-19-trm5-markov-bug "
            "(stale `tr_M(e^-) = z³` replaced by `hz² + z`)."
        )
        .set_content_block("prop:frobenius-gram-matrix")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("z_at_q0", float(z))
        .add_parameter("h_at_q0", float(h))
        .add_parameter("max_single_trace_residue",
                       float(max_single_residue))
        .add_parameter("symmetry_residue", float(symmetry_resid))
        .add_parameter("det_G_at_q0", float(det_G))
        .add_parameter("num_positive_eigenvalues", n_positive)
        .add_parameter("num_negative_eigenvalues", n_negative)
        .add_parameter("num_zero_eigenvalues", n_zero)
        .add_parameter("is_indefinite", is_indefinite)
        .add_parameter("is_nondegenerate", is_nondegenerate)
        .add_data("single_element_traces", single_trace_results)
        .add_data("gram_matrix_eigenvalues", eig_floats)
        .add_data("notes", {
            "errata_fix_propagated":
                "tr_M(e^-) corrected from stale z³ to canonical hz² + z",
            "audit_reference":
                "docs/audits/2026-05-19-trm5-markov-bug.md",
        })
        .add_assertion(
            name="single_element_traces_match_closed_forms",
            computed=float(max_single_residue),
            expected=0.0, tolerance=1e-30,
            unit=(
                "max over {𝟙, σ_0, σ_1, L_+, L_-, e^-} of "
                "|tr_M(b) − closed_form(b)|"
            ),
            source="Ocneanu-Wenzl recursion + Hecke quadratic + Markov axiom.",
        )
        .add_assertion(
            name="gram_matrix_symmetric",
            computed=float(symmetry_resid),
            expected=0.0, tolerance=1e-30,
            unit="max over (i,j) of |G_{ij} − G_{ji}|",
            source="Cyclicity of the Markov trace tr_M(ab) = tr_M(ba).",
        )
        .add_assertion(
            name="gram_matrix_nondegenerate",
            computed=0.0 if is_nondegenerate else 1.0,
            expected=0.0, tolerance=0.0,
            unit="boolean (0 = non-degenerate, 1 = degenerate)",
            source=(
                "Frobenius self-duality A ≅ A^∨ implies the Markov-"
                "trace pairing is non-degenerate at generic q."
            ),
        )
        .add_assertion(
            name="gram_matrix_indefinite_signature",
            computed=0.0 if is_indefinite else 1.0,
            expected=0.0, tolerance=0.0,
            unit=(
                "boolean (0 = has both positive AND negative eigvals, "
                "1 = same-sign)"
            ),
            source=(
                "Proposition states G has indefinite signature, "
                "NOT positive definite — confirmed empirically."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"z at q_0 = {float(z):.12f},  h at q_0 = {float(h):.12f}")
    print()
    print("Single-element traces:")
    print(f"{'basis':<25} {'expected':<20} {'computed':<20} {'residue':<10}")
    for r in single_trace_results:
        print(f"  {r['basis_element']:<23} "
              f"{r['expected_at_q0']:<20.12f} "
              f"{r['computed_at_q0']:<20.12f} "
              f"{r['residue']:.2e}")
    print()
    print("Gram matrix properties:")
    print(f"  symmetry residue: {float(symmetry_resid):.2e}")
    print(f"  det G = {float(det_G):.6f}")
    print(f"  eigenvalues: {sorted(eig_floats)}")
    print(f"  signature: ({n_positive} positive, {n_negative} negative,"
          f" {n_zero} zero) — indefinite: {is_indefinite}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
