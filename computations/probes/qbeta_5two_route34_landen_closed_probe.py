#!/usr/bin/env python3
"""Route 34 -- Landen's identity is CLOSED on the negative reals, in Lean.

Bean `qou-rstq` item 4. Pairs with the extended
  QOU/MathlibExt/ComplexDilogarithmLanden.lean
which is sorry-free, lake-verified, axioms [propext, Classical.choice, Quot.sound]:

  landenCombo_ofReal_eq_zero : forall {t : R}, t < 0 -> landenCombo (t : C) = 0

  landenCombo z := cLiTwoExt z + cLiTwoExt (z/(z-1)) + log(1-z)^2 / 2

WHAT CHANGED SINCE ROUTE 33
---------------------------
Route 33 G5 recorded the Landen leg as needing exactly one thing: "the
connectedness step from zero derivative to the identity". That step is now
taken. G3/G4 of Route 33 measured the zero derivative and that the constant is
0; this probe checks the THEOREM AS STATED, plus the two design choices the
proof turns on, plus what it still does not reach.

THE DESIGN CHOICE WORTH CHECKING (G3)
-------------------------------------
The constant is pinned at the LIMIT t -> 0-, not at t = -1. That is not a
stylistic preference: at t = -1 the combination is
Li2(-1) + Li2(1/2) + log(2)^2/2, so pinning there needs Li2(1/2), which Mathlib
does not have. G3 checks that each of those three pieces is INDIVIDUALLY
NONZERO -- i.e. the special value really would have been needed, and "we avoided
it" is a claim about the proof rather than decoration.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import fabs, findroot, im, log, mp, mpc, mpf, nstr, pi, polylog, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def landen_combo(z):
    """The Lean `landenCombo`, evaluated with mpmath's principal branches."""
    return polylog(2, z) + polylog(2, z / (z - 1)) + log(1 - z) ** 2 / 2


def in_not_cut(w):
    """Lean's `notCut = {w | Im w != 0 or Re w < 1}` -- Li2's cut is [1, inf)."""
    return (im(w) != 0) or (re(w) < 1)


def in_slit_plane(w):
    """Mathlib's `slitPlane = {w | 0 < Re w or Im w != 0}` -- log's cut is (-inf,0]."""
    return (re(w) > 0) or (im(w) != 0)


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -40
    gates = []

    # ---- G1: the theorem as stated, over the whole negative axis ------------
    worst1 = mpf(0)
    at1 = None
    for i in range(1, 201):
        t = -mpf(i) / 20                       # -0.05 .. -10
        d = fabs(landen_combo(mpc(t, 0)))
        if d > worst1:
            worst1, at1 = d, t
    gates.append({
        "gate": "G1",
        "claim": "landenCombo_ofReal_eq_zero AS STATED: Li2(t) + Li2(t/(t-1)) + log(1-t)^2/2 = 0 "
                 "for every real t < 0. 200 points from -0.05 to -10. This is the Lean theorem's "
                 "exact content, not a nearby identity",
        "n_points": 200, "worst_abs": nstr(worst1, 10),
        "at_t": nstr(at1, 12) if at1 is not None else None,
        "pass": bool(worst1 < tol),
    })

    # ---- G2: the pinning point -- the limit t -> 0- is 0, not merely finite --
    rows2 = []
    ok2 = True
    for k in range(1, 9):
        t = -mpf(10) ** (-k)
        v = landen_combo(mpc(t, 0))
        rows2.append({"t": nstr(t, 6), "abs_combo": nstr(fabs(v), 10)})
        ok2 = ok2 and fabs(v) < tol
    gates.append({
        "gate": "G2",
        "claim": "THE PINNING THE PROOF USES: the combination tends to 0 as t -> 0-, over eight "
                 "decades. The Lean proof takes the constant from the endpoint 0 (where "
                 "cLiTwoExt_zero and log 1 = 0 make every term vanish) and `Ico t 0` excludes "
                 "the one point where the derivative hypotheses fail. If this limit were any "
                 "nonzero constant the theorem would be FALSE, not merely unproved",
        "per_decade": rows2, "pass": bool(ok2),
    })

    # ---- G3: the special value really would have been needed ---------------
    li2_neg1 = polylog(2, mpf(-1))
    li2_half = polylog(2, mpf(1) / 2)
    logterm = log(mpf(2)) ** 2 / 2
    total = li2_neg1 + li2_half + logterm
    li2_half_closed = pi ** 2 / 12 - log(mpf(2)) ** 2 / 2
    gates.append({
        "gate": "G3",
        "claim": "WHY THE BASE POINT IS 0 AND NOT -1, checked rather than asserted. At z = -1 the "
                 "combination is Li2(-1) + Li2(1/2) + log(2)^2/2. Each of the three pieces is "
                 "INDIVIDUALLY NONZERO, so pinning there genuinely needs Li2(1/2) = pi^2/12 - "
                 "log(2)^2/2 -- a value Mathlib does not have (it has hasSum_zeta_two only). "
                 "They cancel to 0 exactly, which is why the identity holds; but the cancellation "
                 "is not available without the special value. Pinning at 0 needs no value at all",
        "Li2_minus_1": nstr(li2_neg1, 20),
        "Li2_half": nstr(li2_half, 20),
        "Li2_half_closed_form": nstr(li2_half_closed, 20),
        "log_term": nstr(logterm, 20),
        "sum": nstr(total, 10),
        "each_piece_nonzero": bool(fabs(li2_neg1) > mpf("0.1") and fabs(li2_half) > mpf("0.1")
                                   and fabs(logterm) > mpf("0.1")),
        "half_matches_closed_form": bool(fabs(li2_half - li2_half_closed) < tol),
        "pass": bool(fabs(total) < tol and fabs(li2_neg1) > mpf("0.1")
                     and fabs(li2_half) > mpf("0.1") and fabs(logterm) > mpf("0.1")),
    })

    # ---- G4: the hypotheses hold SIMULTANEOUSLY at every sampled point ------
    # The failure mode of PR #4701 correction 6: a theorem true and about nothing.
    bad4 = []
    for i in range(1, 201):
        t = -mpf(i) / 20
        z = mpc(t, 0)
        u = z / (z - 1)
        hyps = {
            "z_in_notCut": in_not_cut(z),
            "z_ne_0": z != 0,
            "z_minus_1_ne_0": (z - 1) != 0,
            "u_in_notCut": in_not_cut(u),
            "u_ne_0": u != 0,
            "one_sub_z_in_slitPlane": in_slit_plane(1 - z),
        }
        if not all(hyps.values()):
            bad4.append({"t": nstr(t, 12), "failing": [k for k, v in hyps.items() if not v]})
    gates.append({
        "gate": "G4",
        "claim": "NON-VACUITY: all six hypotheses of hasDerivAt_landenCombo hold SIMULTANEOUSLY at "
                 "every one of the 200 sampled points. This is the gate class that caught "
                 "correction 6 in PR #4701, where a slitPlane hypothesis failed at all 199 arc "
                 "points and made its theorem vacuous. Type-checking would never have found it",
        "n_points": 200, "n_failing": len(bad4), "failures": bad4[:5],
        "pass": bool(len(bad4) == 0),
    })

    # ---- G5: ADVERSARIAL -- the identity FAILS for t > 1 --------------------
    rows5 = []
    all_fail = True
    for t in [mpf(2), mpf(3), mpf(5), mpf("2.24698")]:
        v = landen_combo(mpc(t, 0))
        rows5.append({"t": nstr(t, 12), "abs_combo": nstr(fabs(v), 12),
                      "combo": nstr(v, 12)})
        all_fail = all_fail and fabs(v) > mpf("0.1")
    gates.append({
        "gate": "G5",
        "claim": "ADVERSARIAL ON THE REGIME: for t > 1 the same combination is NOT zero, so the "
                 "restriction to t < 0 is load-bearing rather than a convenience. t = 2.24698 is "
                 "included deliberately -- it is w_1, the one argument `extended_sum` uses that "
                 "lies in the INVERSION regime, and it is exactly the value this theorem does not "
                 "reach. A proof that appeared to cover it would be wrong",
        "per_point": rows5, "all_nonzero": bool(all_fail), "pass": bool(all_fail),
    })

    # ---- G6: OFF the configuration -- complex points near the axis ---------
    worst6 = mpf(0)
    at6 = None
    for i in range(1, 41):
        for eps in [mpf(1) / 10, mpf(1) / 3, mpf(1)]:
            z = mpc(-mpf(i) / 8, eps)
            if not (in_not_cut(z) and in_not_cut(z / (z - 1)) and in_slit_plane(1 - z)):
                continue
            d = fabs(landen_combo(z))
            if d > worst6:
                worst6, at6 = d, z
    gates.append({
        "gate": "G6",
        "claim": "CHECKED OFF THE CONFIGURATION IT WILL BE USED ON: the identity also holds at "
                 "complex points off the real axis, where the Lean theorem says nothing. If it "
                 "held ONLY on the negative reals that would signal the real-restriction had "
                 "smuggled something in; it does not",
        "n_points": 120, "worst_abs": nstr(worst6, 10),
        "at_z": nstr(at6, 12) if at6 is not None else None,
        "pass": bool(worst6 < tol),
    })

    # ---- G7: which of the six `extended_sum` arguments this reaches ---------
    xr = findroot(lambda t: t ** 3 - 2 * t ** 2 - t + 1, mpf("0.55"))
    ws = [1 / (1 - xr), xr, (xr - 1) / xr]
    args = ws + [-w for w in ws]
    reached, not_reached = [], []
    for a in args:
        (reached if a < 0 else not_reached).append(nstr(a, 18))
    gates.append({
        "gate": "G7",
        "claim": "SCOPE, named per argument rather than left in prose. Of the six arguments "
                 "`extended_sum` uses, this theorem reaches exactly those that are NEGATIVE -- the "
                 "Landen regime of `extend`. The non-negative ones are untouched: those in [0,1] "
                 "need nothing (the series already agrees), and w_1 = 2.24698 needs the INVERSION "
                 "leg, which is still open and is the sharper of the two",
        "reached_by_this_theorem": reached,
        "not_reached": not_reached,
        "still_open": "the inversion leg for x > 1: x > 1 lies ON cLiTwoExt's cut (notCut "
                      "excludes real x >= 1), so it needs a boundary value from off the cut, "
                      "not a constant of integration",
        "pass": bool(len(reached) == 3 and len(not_reached) == 3),
    })

    out = {
        "probe": "qbeta_5two_route34_landen_closed",
        "bean": "qou-rstq", "cross_ref": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": ["QOU/MathlibExt/ComplexDilogarithmLanden.lean"],
        "lean_theorem": "landenCombo_ofReal_eq_zero : forall {t : R}, t < 0 -> landenCombo (t:C) = 0",
        "lean_axioms": ["propext", "Classical.choice", "Quot.sound"],
        "gates": gates,
        "verdict": {
            "closed_this_round": "the Landen leg of qou-rstq item 4, on the negative reals. "
                                 "Route 33 G5 named the connectedness step as the only thing "
                                 "missing from this leg; it is now proved, sorry-free and "
                                 "lake-verified, with the constant pinned at the limit t -> 0- "
                                 "so that no special value of Li2 is needed.",
            "still_open": "the INVERSION leg (x > 1), unchanged and still the sharper of the "
                          "two. Exactly one of the six arguments needs it, w_1 = 2.24698, and "
                          "it cannot be avoided. Also unchanged: identifying the corpus's "
                          "PIECEWISE `extend` with Re of the analytic Rogers L still needs the "
                          "real-part bookkeeping on top of these identities.",
            "not_claimed": "this does NOT close qou-rstq item 4, and does not touch the sum "
                           "rule. It closes one of the two analytic legs that item rests on.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route34-landen-closed.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("Landen is CLOSED on the negative reals, in Lean; the inversion leg "
                         "(x > 1, w_1 = 2.24698) is still open."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
