#!/usr/bin/env python3
"""qbeta_fmap_parity_stability_probe.py — parity predicts anchor-stability.

Sharp, falsifiable consequence of the two-saddle geometry
(docs/scope/2026-07-06-qbeta-fmap-torus-knot-cs-phase-geometry.md):

  bar-EVEN c_k  <->  torus / Rogers / REAL-q saddle       ->  ANCHOR-STABLE
  bar-ODD  c_k  <->  hyperbolic / Faddeev / root-of-unity ->  ANCHOR-DEPENDENT

Parities are TAKEN FROM the corpus (not re-derived here — the u-variable is
not bar-invariant, u -> q^2 u, so re-deriving parity by hand is error-prone;
the established assignments are used):
  * c_2 = -1  bar-EVEN  (Kashiwara f~_1^2; registry / state-of-play §1)
  * c_3       bar-ODD   (a_1 = -c_3 bar-antisymmetric; #1887 Reeb-sinh, §2)
  * Q_β overall bar-ODD (= Im 𝔙 = sinh/CS face; conj:binding-qbeta-complex-volume §8)

Anchor-stability is TAKEN FROM the c_3 cross-anchor verdict
(docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md):
  * c_2 identical at both anchors (exact)
  * c_3 swings 2.375% (proton -2.0693 / muon -2.0202)

This probe records the correlation and its consequence; it does not fit
anything. Only 2 rungs currently have BOTH a reliable parity and reliable
stability datum, so the higher-rung predictions are stated, not tested.
"""
from __future__ import annotations

# (rung, parity, corpus source, anchor-stable?, stability datum)
ROWS = [
    ("c_2", "bar-even", "Kashiwara f~_1^2 (registry)", True,
     "identical both anchors (proved exact)"),
    ("c_3", "bar-odd", "a_1=-c_3, #1887 Reeb-sinh", False,
     "swings 2.375% (p -2.0693 / mu -2.0202)"),
]

# geometry's rule: bar-even -> stable (real-q saddle); bar-odd -> unstable.
PREDICT = {"bar-even": True, "bar-odd": False}


def main() -> int:
    print("=" * 78)
    print(" Q_β f-map — parity predicts anchor-stability (two-saddle consequence)")
    print("=" * 78)
    print(f"  {'rung':5} {'parity':9} {'predict stable':15} {'observed stable':16} {'match':6}")
    all_match = True
    for rung, parity, src, stable, datum in ROWS:
        pred = PREDICT[parity]
        match = pred == stable
        all_match = all_match and match
        print(f"  {rung:5} {parity:9} {str(pred):15} {str(stable):16} {'OK' if match else 'FAIL'}")
        print(f"        parity src: {src}")
        print(f"        stability : {datum}")
    print()
    print("  RULE (geometry): bar-even <-> real-q/Rogers saddle -> anchor-STABLE;")
    print("                   bar-odd  <-> root-of-unity/Faddeev -> anchor-DEPENDENT.")
    print(f"  Confirmed on all rungs with reliable data: {all_match}  (2/2)")
    print()
    print("  CONSEQUENCE for F(q): the ladder splits by parity into")
    print("    F(q) = F_even(q)  x  F_odd(q)")
    print("  with F_even a REAL-q (Rogers, bar-even, anchor-stable) factor and")
    print("  F_odd a ROOT-OF-UNITY (Faddeev, bar-odd, anchor-dependent) factor.")
    print("  This refines the self-dual-Higgs 'one bar-even-multiplier recurrence")
    print("  yields both parity ladders': the two ladders live on the two saddles.")
    print()
    print("  PREDICTIONS (untested — need reliable higher c_k):")
    print("    * every bar-even c_k is anchor-stable / real-q-exact;")
    print("    * every bar-odd  c_k is anchor-dependent (only F_odd carries it);")
    print("    * a bar-even c_k that swings, or a bar-odd c_k that is anchor-exact,")
    print("      would FALSIFY the two-saddle assignment.")
    print()
    print("  NOT fit: no c_k value proposed, no root-of-unity value picked.")
    return 0 if all_match else 1


if __name__ == "__main__":
    raise SystemExit(main())
