#!/usr/bin/env python3
"""Route 70 -- the 5_2 saddle sum rule is PROVED. This probe is the numerical
control on the statement that was proved, not evidence for it.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Closes the lane
opened at Route 1.

WHAT IS PROVED (Lean, sorry-free, axioms [propext, Classical.choice, Quot.sound])
--------------------------------------------------------------------------------
`QOU/QBeta/FiveTwoComplexPentagon.lean`:

  fiveTwo_saddle_sum_rule -- there are three roots of X^3 - 2X^2 + 3X - 1, one
  real in (0,1) and a conjugate pair, and

      Sum Li_2(y_j) = -pi^2/6 - log^2(y_3)/2 + (2/3)(arg y_1 - pi)^2

  fiveTwoSaddleSumRule_holds -- the same in the form of the corpus's own
  conjecture class QOU.QBeta.FiveTwo.FiveTwoSaddleSumRule, declared there with
  NO instance and the comment "the statement is open". With
  V_j = 3 Li_2(y_j) + (log y_j + b_j pi i)^2 and b = (-1,+1,+1),

      Sum_j V_j = -3 pi^2/2 + 2 pi log(y_3) i     so   Sum_j Re V_j = -3 pi^2/2

WHAT THIS PROBE IS FOR
----------------------
Not evidence -- the theorem does not need any. It is a **control on the
statement**: that the expression proved is the one the corpus recorded as the
target, at the precision the corpus recorded it (80 dps), and that the branch
assignment b = (-1,+1,+1) is the one that works and the alternatives do not.

A proof of the wrong statement is the failure mode that a proof cannot detect,
and this is the check for it.

**The 5_2 sum rule is PROVED.** The 5_2 volume conjecture is untouched.
"""

import json
import pathlib

from mpmath import (arg, conj, fabs, im, log, mp, mpc, mpf, nstr, pi, polylog,
                    polyroots, re)

SADDLE = [1, -2, 3, -1]
A_RECORDED = "0.9717306814686482591277741699"


def main() -> int:
    mp.dps = 80
    tol = mpf(10) ** -60
    gates = []
    I = mpc(0, 1)

    roots = polyroots(SADDLE, maxsteps=2000, extraprec=9000)
    t = re([r for r in roots if fabs(im(r)) < mpf(10) ** -60][0])
    a = [r for r in roots if im(r) > mpf(10) ** -60][0]
    b = conj(a)
    th, L = arg(a), log(t)

    # ---- G1: the roots are as the theorem's witnesses describe them --------
    gates.append({
        "gate": "G1",
        "claim": "the witnesses exist and are as stated: one real root in (0,1) and a conjugate "
                 "pair, all three roots of X^3-2X^2+3X-1. In Lean the real root comes from the "
                 "intermediate value theorem (f(0) = -1 < 0 < 1 = f(1)) and the pair from an "
                 "explicit square root, the residual quadratic having discriminant "
                 "-(3t^2-4t+8) < 0 unconditionally",
        "t": nstr(t, 30), "t_in_unit_interval": bool(0 < t < 1),
        "a": nstr(a, 30), "im_a_positive": bool(im(a) > 0),
        "b_is_conj_a": bool(fabs(b - conj(a)) < tol),
        "max_cubic_residual": nstr(max(fabs(z ** 3 - 2 * z ** 2 + 3 * z - 1)
                                       for z in (mpc(t), a, b)), 10),
        "pass": bool(0 < t < 1 and im(a) > 0
                     and max(fabs(z ** 3 - 2 * z ** 2 + 3 * z - 1)
                             for z in (mpc(t), a, b)) < tol),
    })

    # ---- G2: the proved closed form is the recorded target -----------------
    A = polylog(2, a) + polylog(2, b) + polylog(2, t)
    closed = -pi ** 2 / 6 - L ** 2 / 2 + mpf(2) / 3 * (th - pi) ** 2
    gates.append({
        "gate": "G2",
        "claim": "THE CONTROL THAT MATTERS. The expression proved is the one the corpus recorded "
                 "as the target: Sum Li_2(y_j) = -pi^2/6 - log^2(y_3)/2 + (2/3)(arg y_1 - pi)^2, "
                 "and it agrees with the recorded value of A at 80 dps. A proof of the WRONG "
                 "statement is the failure a proof cannot catch, so this gate exists",
        "A_computed": nstr(re(A), 40),
        "A_recorded_in_corpus": A_RECORDED,
        "closed_form": nstr(closed, 40),
        "residual_vs_closed_form": nstr(fabs(A - closed), 10),
        "residual_vs_recorded": nstr(fabs(re(A) - mpf(A_RECORDED)), 10),
        "pass": bool(fabs(A - closed) < tol
                     and fabs(re(A) - mpf(A_RECORDED)) < mpf(10) ** -27),
    })

    # ---- G3: the V-form, and that b = (-1,+1,+1) is the one that works -----
    def V(y, bj):
        return 3 * polylog(2, y) + (log(y) + bj * pi * I) ** 2

    good = V(a, -1) + V(b, 1) + V(t, 1)
    alternatives = {}
    for lab, bs in {"(-1,+1,+1)": (-1, 1, 1), "(+1,-1,0)": (1, -1, 0),
                    "(+1,-1,+1)": (1, -1, 1), "(-1,+1,0)": (-1, 1, 0),
                    "(0,0,0)": (0, 0, 0)}.items():
        s = re(V(a, bs[0]) + V(b, bs[1]) + V(t, bs[2]))
        alternatives[lab] = {"sum_re_V": nstr(s, 25),
                             "hits_target": bool(fabs(s + 3 * pi ** 2 / 2) < tol)}
    hits = [k for k, v in alternatives.items() if v["hits_target"]]
    gates.append({
        "gate": "G3",
        "claim": "the branch assignment is pinned, not chosen: b = (-1,+1,+1) on "
                 "(y_1, y_2, y_3) is the ONLY one of five tried that reaches -3 pi^2/2, and the "
                 "others miss by 9.87 to 25.9. Both halves are elementary -- the real part is the "
                 "corpus's conjecture, the imaginary part is 2 pi log(y_3)",
        "sum_V": nstr(good, 30),
        "predicted": nstr(-3 * (pi ** 2 / 2) + 2 * pi * L * I, 30),
        "residual": nstr(fabs(good - (-3 * (pi ** 2 / 2) + 2 * pi * L * I)), 10),
        "alternatives": alternatives,
        "assignments_hitting_target": hits,
        "pass": bool(fabs(good - (-3 * (pi ** 2 / 2) + 2 * pi * L * I)) < tol
                     and hits == ["(-1,+1,+1)"]),
    })

    # ---- G4: what is NOT proved --------------------------------------------
    D = lambda z: im(polylog(2, z)) + arg(1 - z) * log(fabs(z))
    galois_D = D(a) + D(b) + D(t)
    gates.append({
        "gate": "G4",
        "claim": "the scope, stated so it cannot be overread. The 5_2 VOLUME conjecture is "
                 "untouched: Vol(5_2) = 3 D(y_1) with D the Bloch-Wigner function, and D cancels "
                 "identically on the Galois sum (checked here) -- which is exactly why the sum "
                 "rule could be proved without touching the volume. Nothing in this lane speaks "
                 "to Vol(5_2)",
        "galois_sum_of_D": nstr(fabs(galois_D), 10),
        "D_cancels_on_the_orbit": bool(fabs(galois_D) < mpf(10) ** -50),
        "volume_conjecture_proved": False,
        "pass": bool(fabs(galois_D) < mpf(10) ** -50),
    })

    out = {
        "probe": "qbeta_5two_route70_sum_rule_proved",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "lean": "QOU/QBeta/FiveTwoComplexPentagon.lean -- fiveTwo_saddle_sum_rule, "
                "fiveTwoSaddleSumRule_holds",
        "gates": gates,
        "verdict": {
            "proved": "the 5_2 saddle sum rule, sorry-free, standard axioms: "
                      "Sum Li_2(y_j) = -pi^2/6 - log^2(y_3)/2 + (2/3)(arg y_1 - pi)^2, "
                      "equivalently Sum_j Re V_j = -3 pi^2/2, which instantiates the corpus's "
                      "own conjecture class.",
            "role_of_this_probe": "a control on the STATEMENT, not evidence for it.",
            "not_proved": "the 5_2 volume conjecture. D cancels on the Galois sum.",
            "sum_rule_status": "PROVED",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route70-sum-rule-proved.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the 5_2 saddle sum rule is PROVED -- sorry-free, standard axioms, and the statement "
        "proved is the one the corpus recorded, checked here at 80 dps. The branch assignment "
        "b = (-1,+1,+1) is the only one of five that reaches the target. The 5_2 VOLUME "
        "conjecture is untouched."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
