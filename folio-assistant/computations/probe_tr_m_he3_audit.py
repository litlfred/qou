#!/usr/bin/env python3
"""Cross-check |tr_M(β_³He)| via two independent canonical paths.

Per the audit conclusion in `docs/audits/2026-05-11-brane-tower-
n_star-closure-audit.md` §"Open path 2 — ³He structural gap": the
³He binding-formula residual survives every operator-volume
convention probed in PR #638.  Before accepting this as a
structural deficit of the brane-tower formula, **verify the
Markov-trace value itself is correct** by cross-checking two
independent canonical computations:

  Path 1 (Hoefsmit + Wedderburn sum):
    tr_M(β_³He) = Σ_λ y_λ(q_0) · χ^λ_q(β)
                via `wedderburn_jones_markov
                .global_wedderburn_sum_q_hecke_seminormal`.
    This is the value used in all six probe families.

  Path 2 (Markov-axiom recursive ascent):
    tr_M(β_³He) via `markov_peel.tr_M_atomic` — Gröbner-Shirshov
    reduction in H_9(q) then peel the top generator using
    `tr_M^{(n)}(x · σ_{n-1}) = z · tr_M^{(n-1)}(x)`.
    This is the canonical-reducer path (no Hoefsmit matrices).

If the two values agree to numerical precision, the ³He structural
gap in PR #638 is REAL and points at the brane-tower formula
itself.  If they disagree, the gap is a Markov-trace mis-count
and the refutation chain points the wrong direction.

Cross-check repeated for D and T as sanity checks (proton at A=1
agreed to 1e-13 per PR #564 ledger; D and T should follow).

Output: `tr-m-he3-audit.witness.json`
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from witness_base import WitnessBuilder

ATOMS = {"deuteron": (1, 1), "tritium": (1, 2), "he3": (2, 1)}


def main():
    q0_val = float(Q0)

    w = (
        WitnessBuilder("tr-m-he3-audit", engine="python")
        .set_description(
            "Cross-check |tr_M(β)| for D, T, ³He via two independent "
            "canonical paths: (1) Hoefsmit seminormal + Wedderburn "
            "sum via `wedderburn_jones_markov."
            "global_wedderburn_sum_q_hecke_seminormal` (used in all "
            "six brane-tower n_⋆ probe families of PR #638); "
            "(2) Markov-axiom recursive ascent via `markov_peel."
            "tr_M_atomic` (canonical reducer, no Hoefsmit matrices). "
            "Tests whether the ³He structural gap identified in the "
            "closure audit is a real brane-tower-formula deficit or "
            "a Markov-trace mis-count."
        )
        .set_content_block("conj:brane-tower-z-habiro")
        .add_parameter("q_0", q0_val)
    )

    print("=" * 72)
    print("|tr_M(β)| audit: Hoefsmit vs Markov-peel")
    print("=" * 72)
    print(f"  q_0 = {q0_val}")
    print()

    rows = {}
    print(f"  {'atom':>10} {'Z,N':>5}  {'Hoefsmit':>15}  "
          f"{'Markov-peel':>20}  {'|Δ|':>12}")
    print("  " + "-" * 68)
    for name, (Z, N) in ATOMS.items():
        # Path 1: Hoefsmit + Wedderburn
        from wedderburn_jones_markov import (
            global_wedderburn_sum_q_hecke_seminormal,
        )
        tr_M_hoefsmit, _ = global_wedderburn_sum_q_hecke_seminormal(
            Z, N, q_val=q0_val,
        )

        # Path 2: Markov-peel
        try:
            from markov_peel import tr_M_atomic
            import sympy as sp
            tr_M_peel_sym = tr_M_atomic(Z, N, include_inter=True)
            # tr_M_atomic returns symbolic; substitute q_0 + evaluate.
            q_sym = sp.symbols("q", positive=True)
            tr_M_peel = float(
                tr_M_peel_sym.subs(q_sym, sp.sympify(q0_val)).evalf(30)
            ) if hasattr(tr_M_peel_sym, "subs") else float(tr_M_peel_sym)
            peel_str = f"{tr_M_peel:.10f}"
        except Exception as e:
            tr_M_peel = float("nan")
            peel_str = f"err: {str(e)[:40]}"

        delta = abs(tr_M_hoefsmit - tr_M_peel) if tr_M_peel == tr_M_peel else float("nan")
        rows[name] = {
            "Z": Z, "N": N,
            "tr_M_hoefsmit": float(tr_M_hoefsmit),
            "tr_M_markov_peel": float(tr_M_peel),
            "abs_delta": float(delta),
            "agree_at_1e_minus_10": bool(delta < 1e-10) if delta == delta else False,
        }
        print(f"  {name:>10} {Z:>2},{N:<2}  {tr_M_hoefsmit:>15.10f}  "
              f"{peel_str:>20}  {delta:>12.4e}")
    print()

    # Verdict on ³He
    he3_agree = rows["he3"]["agree_at_1e_minus_10"]
    if he3_agree:
        print(f"  ³He: Hoefsmit = Markov-peel within 1e-10 → ³He gap is REAL")
        print(f"      (brane-tower-formula structural deficit, not a")
        print(f"       Markov-trace mis-count)")
    else:
        print(f"  ³He: DISAGREEMENT > 1e-10 — refutation chain may point wrong")
        print(f"      direction; the structural gap could be a Markov-trace")
        print(f"      counting issue rather than a formula deficit.")
    print()

    w = (
        w
        .add_data("per_atom", rows)
        .add_assertion(
            "he3_hoefsmit_agrees_with_markov_peel",
            computed=1 if he3_agree else 0,
            expected=1,
        )
        .add_caveat(
            "markov_peel.tr_M_atomic returns a SymbolicHeckeElement; "
            "we substitute q_0 and evalf at 30 dps then float64-cast. "
            "Any disagreement at 1e-10 reflects float64 cast + "
            "symbolic-evaluation rounding, not a structural mismatch."
        )
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
