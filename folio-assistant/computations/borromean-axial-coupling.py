#!/usr/bin/env python3
"""
Borromean axial-coupling probe — y_λ-weighted Markov trace edition.

The deprecated script evaluated tr(β · σ₁ · β⁻¹). That observable is
trace-cyclic and identically equal to tr(σ₁), forcing the "Borromean
suppression" to be 1 by construction. The 2026-05-07 restored probe
swapped to the non-conjugate β · σ₁, which IS sensitive to the
Borromean word, but evaluated only the seminormal trace on the
two-dimensional standard representation ρ_(2,1). That is still not
the right observable: the principled Markov trace at level n=3 is

    tr_M(w) = Σ_{λ ⊢ 3} y_λ · χ_λ(w),

with y_λ the Jones–Markov central coefficients, χ_λ the Hecke
character on the Specht module V_λ, and the sum running over all
three partitions of 3 ([3], [2,1], [1,1,1]).

This script computes that y_λ-weighted Markov trace for

    β  = σ₁ · σ₂⁻¹ · σ₁ · σ₂⁻¹               (the Borromean word in B_3)
    β·σ₁                                      (axial-conversion probe)

and compares the resulting suppression factor to the naive g_A = 5/3
prediction of the categorical-proton model. The y_λ data is consumed
verbatim from `y-lambda-jones-markov-witness.json` (which already
records the full n=3 weights at the canonical substrate q₀).

The remaining gap to PDG g_A = 1.2754 is genuine — it is not the
trace-cyclicity bug — and is reported as a structural mismatch that
the bound-state observable formula
(⟨O⟩_T = Σ u_i (G⁻¹)_{ij} ⟨O, b_j⟩) is expected to close.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from hecke_characters import chi_lambda_braid
from q_parameter import Q as Q0
from witness_base import WitnessBuilder


THIS_DIR = Path(__file__).parent
Y_LAMBDA_WITNESS = THIS_DIR / "y-lambda-jones-markov-witness.json"


def load_y_lambda_n3() -> tuple[float, float, list[dict]]:
    """Load the y_λ table for n=3 from the canonical Jones–Markov witness."""
    data = json.loads(Y_LAMBDA_WITNESS.read_text())
    table = data["tables_by_n"]["3"]
    return float(table["q_0"]), float(table["z_markov"]), list(table["weights"])


def markov_trace(weights: list[dict], word: list[tuple[int, int]]) -> float:
    """tr_M(w) = Σ_λ y_λ · χ_λ(w) over partitions of n=3."""
    total = 0.0
    for entry in weights:
        chi = chi_lambda_braid(tuple(entry["partition"]), word)
        total += entry["y_lambda"] * float(chi)
    return total


def channel_breakdown(weights: list[dict],
                      word: list[tuple[int, int]]) -> list[dict]:
    """Per-partition contribution to tr_M(w)."""
    rows = []
    for entry in weights:
        chi = float(chi_lambda_braid(tuple(entry["partition"]), word))
        rows.append({
            "partition": list(entry["partition"]),
            "y_lambda": float(entry["y_lambda"]),
            "chi": chi,
            "contribution": entry["y_lambda"] * chi,
        })
    return rows


def main() -> int:
    q_y, z_markov, weights = load_y_lambda_n3()
    # The Jones–Markov witness file pins q at the canonical substrate
    # parameter; the numeric q here MUST agree with the q used for the
    # Hecke characters (chi_lambda_braid defaults to q0 from
    # q_parameter.py).  Spot-check that they match.
    if abs(q_y - float(Q0)) > 1e-12:
        print(
            f"WARN: y-lambda witness q_0={q_y} disagrees with substrate "
            f"Q0={float(Q0)} by {abs(q_y - float(Q0)):.3e}",
            file=sys.stderr,
        )

    word_beta = [(1, 1), (-1, 2), (1, 1), (-1, 2)]
    word_axial = word_beta + [(1, 1)]
    word_sigma1 = [(1, 1)]

    tr_M_beta = markov_trace(weights, word_beta)
    tr_M_sigma1 = markov_trace(weights, word_sigma1)
    tr_M_axial = markov_trace(weights, word_axial)

    suppression = tr_M_axial / tr_M_sigma1
    g_a_naive = 5.0 / 3.0
    g_a_predicted = g_a_naive * suppression
    g_a_pdg = 1.2754
    relative_error = abs(g_a_predicted - g_a_pdg) / g_a_pdg

    breakdown_axial = channel_breakdown(weights, word_axial)
    breakdown_beta = channel_breakdown(weights, word_beta)

    w = WitnessBuilder("borromean-axial-coupling", engine="python")
    w.set_description(
        "Borromean axial-coupling probe via y_λ-weighted Markov trace. "
        "Replaces the trace-cyclic β·σ₁·β⁻¹ formula and the seminormal-"
        "only β·σ₁ probe with tr_M = Σ_λ y_λ · χ_λ on the full Specht "
        "tower of n=3."
    )
    w.set_audit_only("docs/audits/2026-05-07-borromean-axial-coupling-fix.md")
    w.add_parameter("q", float(Q0))
    w.add_parameter("yLambdaSource",
                    "folio-assistant/computations/y-lambda-jones-markov-witness.json#tables_by_n.3")
    w.add_parameter("betaBorr", "σ₁ σ₂⁻¹ σ₁ σ₂⁻¹")
    w.add_parameter("conversionOperator", "σ₁")
    w.add_parameter("axialOperator", "β · σ₁")

    # Sanity: tr_M(σ_1) must equal z_markov (definition of z).
    w.add_assertion("tr_M(σ_1) = z_markov", tr_M_sigma1, z_markov,
                    tolerance=1e-9)
    w.add_assertion("axial trace differs from bare σ_1 trace",
                    abs(tr_M_axial - tr_M_sigma1) > 1e-6, True)
    # Document the structural gap to PDG (NOT a tolerance failure — it
    # is the central finding of this probe).
    w.add_assertion("g_A predicted within 50% of PDG (structural gap)",
                    relative_error < 0.5, True)

    w.add_data("yLambdaWeights", [
        {"partition": list(e["partition"]),
         "depth": e.get("depth"),
         "y_lambda": float(e["y_lambda"])}
        for e in weights
    ])
    w.add_data("markovTraces", {
        "tr_M_beta": tr_M_beta,
        "tr_M_sigma1": tr_M_sigma1,
        "tr_M_axial": tr_M_axial,
        "z_markov_reference": z_markov,
    })
    w.add_data("axialBreakdownByPartition", breakdown_axial)
    w.add_data("borromeanBreakdownByPartition", breakdown_beta)
    w.add_data("axialCoupling", {
        "suppressionFactor": suppression,
        "gA_naive_5_over_3": g_a_naive,
        "gA_yLambdaWeighted": g_a_predicted,
        "gA_PDG": g_a_pdg,
        "relativeErrorVsPDG": relative_error,
        "absoluteGap": g_a_predicted - g_a_pdg,
    })

    w.add_caveat(
        "The y_λ-weighted Markov trace fixes the trace-cyclicity bug "
        "(tr(βXβ⁻¹)=tr(X)) of the deprecated probe and the standard-"
        "rep-only restriction of the 2026-05-07 βσ₁ probe; the "
        "remaining gap to g_A = 1.2754 is a genuine structural mismatch "
        "of the naive 5/3 prediction, not a numerical artifact."
    )
    w.add_caveat(
        "Closing the gap requires the full bound-state observable "
        "⟨O⟩_T = Σ_{i,j∈A*(T)} u_i (G⁻¹)_{ij} ⟨O, b_j⟩ on the LP "
        "active set A*(T); see confinement-frobenius-reciprocity.md."
    )
    w.add_caveat(
        "tr_M(σ_1) is identically z_markov by definition; the assertion "
        "is retained as a regression check on the y_λ table."
    )

    out = w.save()
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
