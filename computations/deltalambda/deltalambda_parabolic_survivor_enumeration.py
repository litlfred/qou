#!/usr/bin/env python3
"""deltalambda_parabolic_survivor_enumeration.py — enumerate the survivor class
that the two-anchor no-go handed off, and check whether ANY member closes.

WHAT THIS FOLLOWS ON FROM (do not re-run the closed parts)
    `docs/audits/2026-07-25-deltalambda-perpair-bond-scalar.md` (PR #4300) already
    PROVED, sorry-free:
      (S) step-lock       [4]_q >= 4 for all q >= 1  (AME-independent)
      (M) monotonicity    rho_grad(3), rho_grad(4) both increase in q
      (N) two-anchor no-go  reaching rho_strong(3) forces overshooting
                            rho_strong(4), margin 2.2196
      + SU(4) row restriction l(lambda) <= 4 is VACUOUS for A <= 4.
    So the single-knob q-scaled family [A]_q! is closed, and the W5 workplan item
    "Lean-state the invariant" is DONE. Nothing here re-derives any of that.

    That audit closes by naming the surviving candidate class:
      "parabolic / skew quotients of [A]_q! whose truncation level is A-locked by
       a stated principle (not a fitted knob)".
    This script enumerates that class exhaustively at the fixed substrate q0 and
    reports what it can and cannot do.

THE CONSTRAINT ANY CLOSURE MUST SATISFY (from the no-go, restated numerically)
    Targets (DERIVED-ELSEWHERE comparison constants, isospin/Coulomb-corrected
    AME, #3986/#3990 -- used only as comparison bounds, never inverted):
        rho_strong(3) = 3.8128        rho_strong(4) = 13.0316
        => required step  rho(4)/rho(3) = 3.4181
    Determinant cap (Lean, lower side): rho_3 <= 3, rho_4 <= 6 -- a closure must
    lie ABOVE these, else it falls back into the machine-excluded det family.

WHY THE ENUMERATION IS FINITE AND DECISIVE
    The substrate q is NOT a free knob: production is pinned to the experimental
    proton anchor q0 = 1.1099785827513808 (AGENTS.md owner directive 2026-08-07).
    At fixed q, a parabolic quotient of [A]_q! is determined by a composition mu
    of A, and there are 2^(A-1) compositions of A. So the whole class at A <= 4 is
    4 + 8 = 12 objects (plus 2 at A=2), and every candidate family is a choice of
    one composition per A. That is a finite table, not a search.

No fit, no AME inversion, nothing wired. Comparison constants are bounds only.
"""
from __future__ import annotations

import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "substrate"))
sys.path.insert(0, str(HERE.parent))

from mpmath import mpf, nstr  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was a hardcoded PROTON
# literal -- the right VALUE by the wrong MECHANISM: it cannot follow the
# anchor, and it is invisible to the retired-pin drain because it never
# matched. Spellings across this family ran 13 to 60 digits for one pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

# Experimental / Physical-Observations pin (proton). AGENTS.md §q0-anchor:
# "ALL AGENTS AND ALL PRODUCTION CODE DEFAULT TO THE EXPERIMENTAL (PROTON) ANCHOR."
Q0 = Q_MP
RHO_STRONG_3 = mpf("3.8128")
RHO_STRONG_4 = mpf("13.0316")
DET_CAP = {2: 1, 3: 3, 4: 6}          # C(A,2)


def q_int(k: int, q: mpf) -> mpf:
    """[k]_q = 1 + q + ... + q^{k-1}."""
    return sum((q ** j for j in range(k)), mpf(0))


def q_fact(k: int, q: mpf) -> mpf:
    """[k]_q! = prod_{j=1..k} [j]_q."""
    out = mpf(1)
    for j in range(1, k + 1):
        out *= q_int(j, q)
    return out


def compositions(n: int):
    """All ordered compositions of n."""
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def parabolic(mu, q: mpf) -> mpf:
    """q-multinomial [A]_q! / prod_i [mu_i]_q!  — the Poincare polynomial of the
    partial flag variety, i.e. the parabolic quotient W^P."""
    A = sum(mu)
    den = mpf(1)
    for part in mu:
        den *= q_fact(part, q)
    return q_fact(A, q) / den


def main() -> None:
    q = Q0
    print("Parabolic/skew quotient survivors of the Delta_lambda two-anchor no-go")
    print(f"substrate q0 = {nstr(q, 17)}  (experimental / proton pin)\n")
    print(f"targets:  rho_strong(3) = {nstr(RHO_STRONG_3, 6)}   "
          f"rho_strong(4) = {nstr(RHO_STRONG_4, 6)}")
    req_step = RHO_STRONG_4 / RHO_STRONG_3
    print(f"required step rho(4)/rho(3) = {nstr(req_step, 6)}")
    print(f"det cap (must exceed):  rho_3 > {DET_CAP[3]}   rho_4 > {DET_CAP[4]}\n")

    table = {}
    for A in (2, 3, 4):
        table[A] = [(mu, parabolic(mu, q)) for mu in compositions(A)]
        print(f"  compositions of {A}:")
        for mu, val in table[A]:
            print(f"    mu = {str(mu):12s}  P = {nstr(val, 10)}")
    print()

    # A family = one composition per A in {2,3,4}; rho(A) := P_A / P_2.
    rows = []
    for mu2, mu3, mu4 in product(table[2], table[3], table[4]):
        (c2, P2), (c3, P3), (c4, P4) = mu2, mu3, mu4
        if P2 == 0:
            continue
        r3, r4 = P3 / P2, P4 / P2
        rows.append({
            "mu2": c2, "mu3": c3, "mu4": c4,
            "rho3": r3, "rho4": r4,
            "err3": (r3 - RHO_STRONG_3) / RHO_STRONG_3 * 100,
            "err4": (r4 - RHO_STRONG_4) / RHO_STRONG_4 * 100,
            "above_cap": (r3 > DET_CAP[3] and r4 > DET_CAP[4]),
        })

    # A survivor must clear the det cap AND land both anchors to within a stated
    # tolerance. 1% is generous -- the no-go margin it must beat is ~17%.
    TOL = mpf("1.0")
    survivors = [r for r in rows if r["above_cap"]
                 and abs(r["err3"]) < TOL and abs(r["err4"]) < TOL]

    print(f"total candidate families: {len(rows)}")
    print(f"families clearing the determinant cap: "
          f"{sum(1 for r in rows if r['above_cap'])}")
    print(f"families landing BOTH anchors within {nstr(TOL, 3)}%: "
          f"{len(survivors)}\n")

    ranked = sorted(rows, key=lambda r: abs(r["err3"]) + abs(r["err4"]))
    print("closest 8 families (by combined |err|):")
    print(f"    {'mu2':>8s} {'mu3':>10s} {'mu4':>12s} {'rho3':>9s} {'err3%':>8s} "
          f"{'rho4':>9s} {'err4%':>8s}  cap")
    for r in ranked[:8]:
        print(f"    {str(r['mu2']):>8s} {str(r['mu3']):>10s} {str(r['mu4']):>12s} "
              f"{nstr(r['rho3'], 6):>9s} {nstr(r['err3'], 4):>8s} "
              f"{nstr(r['rho4'], 6):>9s} {nstr(r['err4'], 4):>8s}  "
              f"{'ok' if r['above_cap'] else 'BELOW'}")

    # The structural reason, independent of the table: the achievable steps.
    print("\nAchievable steps rho(4)/rho(3) over the whole class:")
    steps = sorted({(r["mu3"], r["mu4"], r["rho4"] / r["rho3"]) for r in rows},
                   key=lambda t: t[2])
    lo, hi = steps[0][2], steps[-1][2]
    bracketing = [s for s in steps if abs(s[2] - req_step) / req_step < mpf("0.05")]
    print(f"    min = {nstr(lo, 6)}   max = {nstr(hi, 6)}   "
          f"required = {nstr(req_step, 6)}")
    print(f"    families within 5% of the required step: {len(bracketing)}")
    for mu3, mu4, s in bracketing[:6]:
        print(f"      mu3={str(mu3):10s} mu4={str(mu4):12s} step={nstr(s, 6)}")

    print("\n" + "=" * 74)
    if survivors:
        print(f"{len(survivors)} family/families land both anchors. Each must now be")
        print("justified by an A-LOCKED PRINCIPLE, not selected because it fits --")
        print("selecting on the anchors is the forbidden seventh ansatz.")
    else:
        print("NO parabolic/skew quotient family lands both anchors within 1%.")
        print("The survivor class named by the 2026-07-25 no-go is EMPTY at the")
        print("fixed substrate q0, for A <= 4. This is a scope-(a) negative: the")
        print("class is exhausted as a SINGLE per-A multiplier, not excluded as an")
        print("ingredient inside a larger (e.g. additive) closure.")
    print("=" * 74)

    w = WitnessBuilder("deltalambda-parabolic-survivor-enumeration", engine="mpmath")
    w.add_parameter("q0", str(q))
    w.add_parameter("q0_anchor", "experimental/proton")
    w.add_assertion("survivor_count", len(survivors), 0, tolerance=0,
                    source="No parabolic quotient family lands rho_strong(3) and "
                           "rho_strong(4) simultaneously within 1% at fixed q0.")
    w.add_assertion("class_size_A_le_4", len(rows), 2 * 4 * 8, tolerance=0,
                    source="compositions: 2 of A=2, 4 of A=3, 8 of A=4.")
    w.add_data("targets", {"rho_strong_3": str(RHO_STRONG_3),
                           "rho_strong_4": str(RHO_STRONG_4),
                           "required_step": str(req_step)})
    w.add_data("step_range", {"min": str(lo), "max": str(hi)})
    w.add_data("closest_families", [
        {"mu2": list(r["mu2"]), "mu3": list(r["mu3"]), "mu4": list(r["mu4"]),
         "rho3": str(r["rho3"]), "rho4": str(r["rho4"]),
         "err3_pct": str(r["err3"]), "err4_pct": str(r["err4"]),
         "above_det_cap": r["above_cap"]}
        for r in ranked[:8]])
    w.add_data("verdict", (
        "scope-(a). The parabolic/skew-quotient survivor class named by the "
        "2026-07-25 two-anchor no-go is exhausted at A <= 4 and fixed proton-pin "
        "q0: no member lands both light-nucleus anchors. This closes the class as "
        "a single per-A multiplier. It does NOT exclude these objects as factors "
        "inside a larger closure -- per AGENTS.md, a compositional/additive object "
        "is already many-body and 'insufficient alone' is not 'excluded'."))
    w.add_data("wired_to_production", False)
    w.add_data("fit_performed", False)
    w.add_caveat("rho_strong(3) and rho_strong(4) are DERIVED-ELSEWHERE comparison "
                 "constants used only as bounds; they are never inverted to define "
                 "any quantity here. No composition was selected on the anchors.")
    print(f"\nwitness -> {w.save()}")


if __name__ == "__main__":
    main()
