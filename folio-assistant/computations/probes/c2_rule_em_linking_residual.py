"""C=2 selection-rule lead for the PR #1777 EM-linking-invariant slot.

Companion to:
  - per_knot_lambda_component_selection_rule.py (the rule itself, PR #1765)
  - docs/audits/2026-06-03-c2-rule-em-linking-coulomb-residual.md
  - PR #1777 "Derive the two-like-charge EM-linking invariant"

EXPLORATORY.  No production wiring.  No fit.

## What this probe tests

PR #1775 / `docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md`
derives the categorical pp-Coulomb piece of the T-vs-³He AME binding
split:

    derived_Coulomb · [open EM-linking invariant]  =  AME split (0.7638 MeV)
       0.2377 MeV   ·       3.2137×                =  0.7638 MeV

The 3.2137× factor is the per-interface "EM-linking invariant" gate —
the OPEN derivation from PR #1777.  This probe asks whether PR #1765's
zero-parameter c=2 selection rule

    lw(c=2) = (1/3) Σ_{λ⊢3} dim_q V_λ = (q+1)²/(3q)

(the natural per-link scalar for the 2-component-link case = two
protons) fits the slot.

## Result (run on 2026-06-03)

  lw_c2(q₀) at q₀ = 1.1099786 :   1.336965 622235707...
  residual         = 3.21370 / 1.336966 = 2.40372458...

Two structural candidates for the residual:

  (a) classical 12/5 = dim H_4 / I(4) = 24/10 at q=1 :  off −0.155 %
  (b) q-deformed Σdim_q²(H_4)/Σdim_q(H_4) at q₀     :  off +1.448 %

(a) lands closer.  Best full prediction:

    predicted_split  =  0.2377 · lw_c2(q₀) · (12/5)
                     =  0.7630 MeV    vs AME 0.7638 MeV    →  −0.11 % off

The 12/5 carries suggestive structural meaning: regular-rep dimension
(Σ dim²) over Gelfand-model dimension (Σ dim) at the *next* Wedderburn
rank above c=2 (= H_4, the proton's own rank).  But:

  • 0.11 % is NOT derivation-tight (Δ_λ-gate / 1ppQ-level work needs
    ppm or better, not ppt).
  • The classical-limit 12/5 mixed with the q-deformed lw_c2(q₀)
    has no a-priori categorical justification — the natural symmetric
    q-deformation (candidate b) lands worse (1.45 % off).

So this is a 0.1 %-level LEAD, not a derivation.  The c=2 selection
rule sits in the right ballpark for PR #1777's open slot, but closing
the residual to derivation precision needs either (i) a categorical
derivation of why 12/5 appears un-q-deformed in this factorisation,
or (ii) a different residual identification.

q-usage discipline (CLAUDE.md §7c): all symbolic work is at fibre
level; q₀ enters only at the final archimedean evaluation
(Im(q₀) = 0).  No |q|=1 step.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: F401, E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402


# ── Canonical inputs (provenance: charge-coulomb-tn3he-derived.witness
# .json on `origin/main`, commit a4abea28e6).  Inlined so this probe is
# branch-clean; values must be kept in sync with that witness.
DERIVED_COULOMB_DHE_MEV = mp.mpf("0.23767018758225714")
AME_SPLIT_MEV = mp.mpf("0.7638")
B_PP_STRONG_MEV = mp.mpf("2.2860879768761904")
COULOMB_STRONG_RATIO = mp.mpf("0.10396371005241013")  # tanh(ln q₀)
REMAINING_FACTOR = mp.mpf("3.213697131179528")        # AME_SPLIT / DERIVED
Q_PP = mp.mpf(1)


def part1_compute_lw_c2() -> dict:
    q = sp.symbols("q", positive=True)
    lw_c2 = sp.cancel((q + 1) ** 2 / (3 * q))
    # at q=1 (classical limit): (1+1)²/3 = 4/3 = I(3)/3
    lw_c2_q1 = sp.nsimplify(lw_c2.subs(q, 1))
    # at q₀:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    lw_c2_q0 = mp.mpf(str(lw_c2.subs(q, sp.Float(str(q0), 50))))
    return {
        "rule": "lw(c=2) = (1/3) Σ_{λ⊢3} dim_q V_λ = (q+1)²/(3q)",
        "closed_form": str(lw_c2),
        "classical_limit_q1": str(lw_c2_q1),
        "value_at_q0": mp.nstr(lw_c2_q0, 30),
    }, lw_c2_q0


def part2_residual_candidates(lw_c2_q0: mp.mpf) -> dict:
    """Candidate identifications for the residual = REMAINING_FACTOR / lw_c2."""
    residual = REMAINING_FACTOR / lw_c2_q0
    q = sp.symbols("q", positive=True)

    def qint(n):
        return sp.cancel((q ** n - q ** (-n)) / (q - 1 / q))

    qdim_h4 = {
        "(4)": sp.Integer(1),
        "(3,1)": qint(3),
        "(2,2)": sp.cancel(qint(4) / qint(2)),
        "(2,1,1)": qint(3),
        "(1,1,1,1)": sp.Integer(1),
    }
    sum_dim_q = sp.cancel(sum(qdim_h4.values()))         # Gelfand H_4
    sum_dim_q_sq = sp.cancel(sum(d ** 2 for d in qdim_h4.values()))  # regular H_4
    ratio_q = sp.cancel(sum_dim_q_sq / sum_dim_q)
    q0 = mp.mpf(Q_50_DIGIT_STR)
    ratio_q_at_q0 = mp.mpf(str(ratio_q.subs(q, sp.Float(str(q0), 50))))

    candidates = {
        "12_over_5_classical_regular_over_gelfand_H4": {
            "structural_meaning": (
                "dim H_4 / I(4) = 24/10 = 12/5 at q=1 — regular-rep "
                "dimension over Gelfand-rep dimension at the proton's "
                "Wedderburn rank H_4 (one above c=2's rank H_3)."),
            "value": mp.mpf(12) / 5,
            "rel_diff_pct": mp.nstr(
                (mp.mpf(12) / 5 - residual) / residual * 100, 8),
        },
        "ratio_q_def_H4": {
            "structural_meaning": (
                "Σ dim_q² / Σ dim_q at H_4 — the natural symmetric "
                "q-deformation of 12/5."),
            "value": ratio_q_at_q0,
            "rel_diff_pct": mp.nstr(
                (ratio_q_at_q0 - residual) / residual * 100, 8),
        },
    }

    return {
        "residual_measured": mp.nstr(residual, 30),
        "target_factor": mp.nstr(REMAINING_FACTOR, 30),
        "candidates": {
            k: {
                "structural_meaning": v["structural_meaning"],
                "value": mp.nstr(v["value"], 16),
                "rel_diff_pct_vs_residual": v["rel_diff_pct"],
            }
            for k, v in candidates.items()
        },
        "best_candidate": "12_over_5_classical_regular_over_gelfand_H4",
    }


def part3_predicted_split(lw_c2_q0: mp.mpf) -> dict:
    twelve_fifths = mp.mpf(12) / 5
    predicted = DERIVED_COULOMB_DHE_MEV * lw_c2_q0 * twelve_fifths
    rel_diff = (predicted - AME_SPLIT_MEV) / AME_SPLIT_MEV
    return {
        "factorization": "derived_Coulomb · lw_c2(q₀) · (12/5)",
        "values": {
            "derived_Coulomb_MeV": mp.nstr(DERIVED_COULOMB_DHE_MEV, 14),
            "lw_c2_q0": mp.nstr(lw_c2_q0, 14),
            "twelve_fifths": "2.4",
        },
        "predicted_split_MeV": mp.nstr(predicted, 14),
        "ame_split_MeV": mp.nstr(AME_SPLIT_MEV, 6),
        "rel_diff_pct": mp.nstr(rel_diff * 100, 8),
    }


def main() -> int:
    mp.mp.dps = 60
    print("=" * 72)
    print(" c=2 selection-rule lead for PR #1777 EM-linking-invariant slot")
    print("=" * 72)

    p1, lw_c2_q0 = part1_compute_lw_c2()
    print("\n── Part 1: c=2 selection rule (PR #1765) ──")
    print(f"  closed form    = {p1['closed_form']}")
    print(f"  classical limit = {p1['classical_limit_q1']}")
    print(f"  at q₀          = {p1['value_at_q0'][:30]}…")

    p2 = part2_residual_candidates(lw_c2_q0)
    print("\n── Part 2: residual = target / lw_c2 ──")
    print(f"  measured residual = {p2['residual_measured'][:18]}")
    for name, c in p2["candidates"].items():
        print(f"  {name}:")
        print(f"    value         = {c['value']}")
        print(f"    rel diff      = {c['rel_diff_pct_vs_residual']} %")

    p3 = part3_predicted_split(lw_c2_q0)
    print("\n── Part 3: predicted T-³He split via 12/5 factorisation ──")
    print(f"  factorisation     = {p3['factorization']}")
    print(f"  predicted split   = {p3['predicted_split_MeV']} MeV")
    print(f"  AME split          = {p3['ame_split_MeV']} MeV")
    print(f"  rel diff           = {p3['rel_diff_pct']} %")

    print("\n  VERDICT: 0.11% off is SUGGESTIVE (right ballpark), NOT")
    print("           derivation-tight (needs ppm or better).")
    print("           Concrete candidate for PR #1777's open slot.")

    out_path = HERE.parent / "c2-rule-em-linking-residual.witness.json"
    out = {
        "computation": "c2-rule-em-linking-residual",
        "description": (
            "Tests whether PR #1765's c=2 selection rule lw_c2 = "
            "(q+1)²/(3q) fits PR #1777's open EM-linking-invariant "
            "slot. Result: 0.11% near-match via lw_c2 · (12/5) — "
            "suggestive lead, NOT a derivation. EXPLORATORY."),
        "inputs_provenance": (
            "charge-coulomb-tn3he-derived.witness.json on origin/main "
            "(commit a4abea28e6); values inlined so this probe is "
            "branch-clean."),
        "part1_lw_c2": p1,
        "part2_residual_candidates": p2,
        "part3_predicted_split": p3,
        "discipline": {
            "fit": "none (zero parameters in selection rule + 12/5 = "
                   "structural ratio dim H_4 / I(4))",
            "delta_lambda_gate": "compliant (selection rule, not AME fit)",
            "verdict": "0.1%-level lead, not derivation; reported as "
                       "exploratory candidate for PR #1777, not wired",
        },
    }
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWitness: {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
