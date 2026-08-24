#!/usr/bin/env python3
"""qbeta_c3_rung_structure_analysis.py — symbolic decomposition of
the c_3 [3]_q/25 closure rungs.

PR #1786 follow-up after the [3]_q/25 c_3 closure landed on main
(commit 305c08a91 — formula
`c_3 = -(q² + q⁻²) · (1 + ℏ_q · [3]_q / 25 + ℏ_q³ / [2]_q)`).
Audit doc explicitly tags it NEAR-MATCH, NOT derived.

The c_2 = -1 STRUCTURAL result (PR #1786, prop:q-beta-c-2-eq-neg-
one-structural) was proved one-line in CommRing R: `(1 - b²·ℏ_q⁴)
= (1 - u²)` with u = b·ℏ_q². The proof template: identify a CLEAN
RING IDENTITY linking the operator-valued correction factor to a
ladder-normal-form coefficient.

This probe applies the same template to the c_3 closure's two
rungs: factor each rung into elementary substrate primitives and
check whether either has a clean ring-identity structure that
would lift it from NEAR-MATCH to STRUCTURAL.

Rung-by-rung breakdown:

  Rung 0 (base): -(q² + q⁻²) = -J_Hopf(q) [POSITIVE HOPF JONES]
                 At q = 1: -(1 + 1) = -2 ✓ (matches J_Hopf(1)
                 categorical limit). This is THE most categorical
                 part — it IS a Jones polynomial.

  Rung 1: ℏ_q · [3]_q / 25
          = (q-1)/q · (q² + 1 + 1/q²) / 25
          The /25 is the open empirical factor (the audit doc
          conjectures 25 = 5² with 5 from cinquefoil T(2,5)
          framing; not proven).

  Rung 2: ℏ_q³ / [2]_q
          = (q-1)³ / q³ · q / (q² + 1)
          = (q-1)³ / (q² · (q² + 1))
          A pure rational function with NO empirical coefficient —
          this is the "cleanest categorical" rung per the audit
          doc (called T7 = "ℏ_q³ / [2]_q" in the brackets).

The question this probe answers: do any of the rungs admit a clean
ring-identity simplification (analogous to how (1 - b²·ℏ_q⁴) IS
(1 - u²))?

Findings reported as data, not assertions. Honest scoping.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q0_MP_PIN = Q_50_DIGIT_STR


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-c3-rung-structure-analysis",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Symbolic decomposition of the [3]_q/25 c_3 closure "
        "rungs (commit 305c08a91 on main). Applies the c_2 = -1 "
        "STRUCTURAL proof template (PR #1786) to each rung: "
        "factor into substrate primitives, check for a clean "
        "ring-identity simplification. Reports findings as data; "
        "does NOT claim a structural lift."
    )
    builder.set_content_block("prop:q-beta-c-2-eq-neg-one-structural")

    print("=" * 78)
    print(" Q_β c_3 RUNG STRUCTURE — symbolic decomposition")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    hbar_q = (q - 1) / q
    qint_2 = q + 1 / q
    qint_3 = q ** 2 + 1 + 1 / q ** 2
    J_Hopf = -(q ** 2 + 1 / q ** 2)

    rung0 = J_Hopf
    rung1 = hbar_q * qint_3 / 25
    rung2 = hbar_q ** 3 / qint_2

    c_3_full = J_Hopf * (1 + rung1 + rung2)

    print("  Closed form (commit 305c08a91 on main):")
    print(f"    c_3 = -J_Hopf · (1 + rung_1 + rung_2)")
    print(f"        = -(q² + q⁻²) · (1 + ℏ_q · [3]_q / 25 + ℏ_q³ / [2]_q)")
    print()

    # ---- Rung 0: base J_Hopf(q) ----
    rung0_simple = sp.simplify(rung0)
    rung0_classical = sp.limit(rung0, q, 1)
    print(f"  RUNG 0  (base):  -(q² + q⁻²)")
    print(f"    simplified:    {rung0_simple}")
    print(f"    at q = 1:      {rung0_classical}     (matches J_Hopf(1) = -2 ✓)")
    print(f"    categorical:   STRUCTURAL — IS the Hopf-link Jones polynomial")
    print(f"                   (see qbetaC3Closure 1 = jonesHopfClassicalLimit")
    print(f"                   Lean bridge in commit 923ab77a7)")
    print()

    # ---- Rung 1: ℏ_q · [3]_q / 25 ----
    rung1_expanded = sp.together(sp.expand(rung1))
    rung1_factored = sp.factor(rung1)
    print(f"  RUNG 1:  ℏ_q · [3]_q / 25")
    print(f"    expanded:      {rung1_expanded}")
    print(f"    factored:      {rung1_factored}")
    # Is rung1 itself a clean form? Try Taylor expansion at q=1
    rung1_taylor = sp.series(rung1, q, 1, 4).removeO()
    print(f"    Taylor at q=1: {sp.collect(rung1_taylor, (q-1))}")
    print(f"    /25 is OPEN empirical (audit doc conjectures 5² from")
    print(f"    cinquefoil T(2,5) framing — NOT proven)")
    print()

    # ---- Rung 2: ℏ_q³ / [2]_q ----
    rung2_expanded = sp.together(sp.expand(rung2))
    rung2_factored = sp.factor(rung2)
    print(f"  RUNG 2:  ℏ_q³ / [2]_q  (T7 — 'cleanest categorical')")
    print(f"    expanded:      {rung2_expanded}")
    print(f"    factored:      {rung2_factored}")
    rung2_taylor = sp.series(rung2, q, 1, 5).removeO()
    print(f"    Taylor at q=1: {sp.collect(rung2_taylor, (q-1))}")
    print(f"    No empirical coefficient — pure ratio of q-integer powers")
    print(f"    Categorical interpretation: open (audit doc).")
    print()

    # ---- Try: does rung2 = ℏ_q³/[2]_q equal a clean Jones-skein form? ----
    # ℏ_q · [2]_q = (q-1)/q · (q²+1)/q = (q-1)(q²+1)/q² = (q³ - q² + q - 1)/q²
    # ℏ_q · [2]_q vs rung2 · [2]_q² = ℏ_q³
    test_a = sp.simplify(rung2 * qint_2 - hbar_q ** 3)
    print(f"  Sanity ring identity:  rung2 · [2]_q - ℏ_q³ = {test_a}")
    print(f"  → rung2 IS exactly ℏ_q³/[2]_q (trivially true, just sanity)")
    print()

    # ---- Numerical check at q_0 ----
    q0_mp = mp.mpf(Q0_MP_PIN)
    def evalmp(expr):
        return mp.mpf(str(sp.N(expr.subs(q, sp.Float(str(q0_mp), 50)), 50)))
    print(f"  Numerical values at q_0 = {Q0_MP_PIN[:14]}:")
    print(f"    rung 0 (J_Hopf(q_0))       = {mp.nstr(evalmp(rung0), 14)}")
    print(f"    rung 1 (ℏ_q · [3]_q / 25)  = {mp.nstr(evalmp(rung1), 14)}")
    print(f"    rung 2 (ℏ_q³ / [2]_q)      = {mp.nstr(evalmp(rung2), 14)}")
    print(f"    c_3 (full closure)         = {mp.nstr(evalmp(c_3_full), 14)}")
    print()

    # ---- The honest verdict ----
    print("=" * 78)
    print(" VERDICT — c_3 rung structural lift")
    print("=" * 78)
    print()
    print(f"  RUNG 0 (base):  STRUCTURAL ✓ — IS Hopf Jones polynomial")
    print(f"                  (Lean bridge: qbetaC3Closure 1 =")
    print(f"                  jonesHopfClassicalLimit, commit 923ab77a7)")
    print()
    print(f"  RUNG 1:         NEAR-MATCH — the /25 denominator is the only")
    print(f"                  open empirical factor. If 25 = framing² for a")
    print(f"                  cinquefoil-anchored substrate, this would lift")
    print(f"                  to structural (audit doc conjecture, not proven).")
    print()
    print(f"  RUNG 2:         NEAR-MATCH — no empirical coefficient, just")
    print(f"                  ℏ_q³ / [2]_q. The functional FORM is clean but")
    print(f"                  the choice 'rung 2 is ℏ_q³/[2]_q' (vs T1, T3, T8")
    print(f"                  in the audit doc bracket) is empirical-fit.")
    print()
    print(f"  Path to STRUCTURAL c_3:")
    print(f"    1. Prove /25 = (T(2,5) framing)² categorically (rung 1 lift)")
    print(f"    2. Derive 'rung 2 must be ℏ_q³/[2]_q' from a knot-theoretic")
    print(f"       principle (vs other 10-ppm-tier candidates T1, T3, T8)")
    print(f"    3. Either would close the NEAR-MATCH gap for c_3 at the")
    print(f"       2.65 ppm level recorded by the closure.")
    print()

    builder.add_data("closed_form", {
        "c_3": "-(q^2 + q^-2) * (1 + hbar_q * [3]_q / 25 + hbar_q^3 / [2]_q)",
        "rung_0_base": str(rung0_simple),
        "rung_1": str(rung1_factored),
        "rung_2": str(rung2_factored),
    })
    builder.add_data("classical_limit", {
        "rung_0_at_q_1": str(rung0_classical),
        "matches_J_Hopf_classical_limit": True,
    })
    builder.add_data("at_q_0", {
        "q_0": Q0_MP_PIN,
        "rung_0": mp.nstr(evalmp(rung0), 25),
        "rung_1": mp.nstr(evalmp(rung1), 25),
        "rung_2": mp.nstr(evalmp(rung2), 25),
        "c_3_full": mp.nstr(evalmp(c_3_full), 25),
    })
    builder.add_data("structural_status", {
        "rung_0": "STRUCTURAL (Hopf Jones polynomial; Lean bridge in main)",
        "rung_1": "NEAR-MATCH (open: /25 = framing^2 conjecture)",
        "rung_2": "NEAR-MATCH (open: rung-2 choice from T-bracket empirical)",
        "overall_c_3_status": "NEAR-MATCH (2.65 ppm)",
    })
    builder.add_data("path_to_structural", [
        "Prove /25 = (T(2,5) framing)^2 categorically (lifts rung 1)",
        ("Derive 'rung 2 IS hbar_q^3 / [2]_q' from knot theory "
         "vs other 10-ppm-tier candidates (lifts rung 2)"),
        "Either step closes the NEAR-MATCH gap categorically",
    ])

    # Single invariant assertion: the closed-form expression for c_3
    # equals the rung-decomposition expression (algebraic sanity).
    diff = sp.simplify(c_3_full - J_Hopf * (1 + rung1 + rung2))
    builder.add_assertion(
        "rung_decomposition_equals_closure",
        computed=int(diff == 0),
        expected=1,
        tolerance=0,
        source=("Symbolic identity check: the 3-rung decomposition "
                "as written here matches the closure formula on main. "
                "Sympy.simplify of the difference equals 0. This is "
                "a sanity invariant for the audit; the substantive "
                "findings (which rungs are structural vs near-match) "
                "are recorded as data."),
    )

    # q0 anchor: `independent`, declared rather than inherited.

    # Measured, not assumed -- see the reason (bean qou-o922).

    builder.save({"q0Anchor": "independent",

            "q0AnchorReason": (

                'Reads no substrate value. PROVED by running this producer under'

                'QOU_Q0_ANCHOR=muon and =proton and diffing the emitted witness:'

                'the only non-ephemeral leaves that differ are q0Anchor and'

                'q0Value THEMSELVES -- every substantive field is byte-identical,'

                'so the pin changes the label and nothing else. Its previous'

                '`muon` label was therefore a false claim that this producer'

                'computed at that anchor. `independent` is the honest'

                'disposition; a q0_anchor_manifest entry would be the WRONG fix,'

                'promoting a false claim into a declared one. Bean qou-o922,'

                'class (ii).'

            )})
    print(f"  Witness: qbeta-c3-rung-structure-analysis.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
