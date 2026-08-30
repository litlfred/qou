#!/usr/bin/env python3
"""Route 13 -- two of the ladder's hypotheses are FALSE for the corpus's `LiTwo`.

Bean `qou-rhyp` (item 2), parent `qou-0yqu`.

`QOU/QBeta/FiveTwoLevelSevenLadder.lean` proves the three level-7 numerators from
twelve hypotheses about an abstract `L`. `qou-rhyp` graded the inversion and
Landen ones as "real analysis, not yet in the corpus -- each is a one-variable
identity provable the same way `LiTwo_reflection'` is."

That grading is wrong. This probe shows it, and shows the repair.

WHAT THE CORPUS ACTUALLY DEFINES
--------------------------------
`QOU/Archimedean/DilogarithmArchimedeanLimit.lean:63`

    noncomputable def LiTwo (x : R) : R := sum' k, x ^ (k + 1) / ((k : R) + 1) ^ 2

summable exactly on [-1, 1].  Off it, Lean's `tsum` returns its **junk value 0**
(`tsum_eq_zero_of_not_summable`), and Mathlib's `Real.log` is **even**
(`Real.log_neg_eq_log`, Log/Basic.lean:114).  So a Rogers `L` built on `LiTwo` is,
for |x| > 1, the function  log|x| * log|1 - x| / 2 -- not the dilogarithm.

The ladder evaluates `hinv1` at w1 = 2.2469796... > 1 and `hlan1` at -w1 < -1.
Both land in the junk region.  G3 measures the damage; it is a **refutation
gate** and passes when the failure is confirmed.

WHY NO EARLIER PROBE CAUGHT IT
------------------------------
`qbeta_5two_route11_fiveterm_certificate_probe.py` evaluated the same targets
with mpmath's `polylog`, i.e. the genuine analytic continuation with principal
branches, and got the right answer.  It was testing the mathematics, not the
Lean semantics.  Both were fine on their own terms; the gap was between them.

THE BRANCH TRAP, FOURTH INSTANCE
--------------------------------
The first draft of this probe modelled `Real.log` with mpmath's `log`, which is
complex on negative reals.  Residuals came back with imaginary parts in a
statement about a real-valued function.  `rlog` below is the fix: Mathlib's
`Real.log` is EVEN, and `Real.log 0 = 0`.  Principal-vs-real/continuous `log` has
now produced a spurious result four separate times in this lane (see `qou-trns`,
`qou-rstq`).  It remains the single most reliable source of false alarms here.

WHAT THIS PROBE DOES NOT SHOW
-----------------------------
That the piecewise extension IS the analytic continuation of Li_2.  G7 checks
they agree numerically at the six points in play, which is evidence, not proof.
The 5_2 sum rule remains **verified to 80 dps, unproved**.
"""

import json
import pathlib

from mpmath import fabs, log, mp, mpf, nstr, pi, polylog, polyroots, re

TOL = mpf(10) ** -40


def rlog(x):
    """Mathlib's `Real.log`: EVEN, real-valued, and `Real.log 0 = 0`."""
    x = mpf(x)
    return mpf(0) if x == 0 else log(fabs(x))


def li_two_lean(x):
    """The corpus definition verbatim, including Lean's junk value off [-1, 1]."""
    x = mpf(x)
    return mpf(0) if fabs(x) > 1 else re(polylog(2, x))


def rogers_lean(x):
    """Rogers `L` built directly on the corpus `LiTwo`. Junk for |x| > 1."""
    return li_two_lean(x) + rlog(x) * rlog(1 - mpf(x)) / 2


def rogers_unit(x):
    """Rogers `L` on [0, 1], where `LiTwo` is the honest dilogarithm."""
    x = mpf(x)
    return re(polylog(2, x)) + rlog(x) * rlog(1 - x) / 2


def rogers_ext(x, l1):
    """The extended real Rogers dilogarithm (Zagier, *The dilogarithm function*,
    SS I.3) -- exactly what `QOU/QBeta/FiveTwoRogersExtend.lean` `extend` does."""
    x = mpf(x)
    if x > 1:
        return 2 * l1 - rogers_unit(1 / x)
    if x < 0:
        return -rogers_unit(x / (x - 1))
    return rogers_unit(x)


def rogers_principal(x):
    """Re of the analytic Rogers L via mpmath's principal-branch polylog --
    the convention every earlier probe in this lane used."""
    x = mpf(x)
    return re(polylog(2, x) + log(x) * log(1 - x) / 2)


def main() -> int:
    mp.dps = 60
    gates = []

    # ---- G1: the roots, and which arguments leave the disc of convergence ----
    rts = sorted(re(r) for r in polyroots([1, -2, -1, 1], maxsteps=300, extraprec=300))
    w3, w2, w1 = rts
    l1 = pi ** 2 / 6
    outside = [nm for nm, v in [("w1", w1), ("-w1", -w1), ("w2", w2), ("-w2", -w2),
                                ("w3", w3), ("-w3", -w3)] if fabs(v) > 1]
    gates.append({
        "gate": "G1",
        "claim": "roots of w^3-2w^2-w+1; exactly w1 and -w1 leave [-1,1]",
        "w1": nstr(w1, 24), "w2": nstr(w2, 24), "w3": nstr(w3, 24),
        "outside_unit_interval": outside,
        "pass": outside == ["w1", "-w1"],
    })

    # ---- G2: the series really does diverge there ----
    def partial(x, n):
        return sum(mpf(x) ** (k + 1) / (mpf(k) + 1) ** 2 for k in range(n))

    growth = [nstr(fabs(partial(w1, n)), 8) for n in (20, 40, 80)]
    diverges = fabs(partial(w1, 80)) > fabs(partial(w1, 40)) > fabs(partial(w1, 20))
    gates.append({
        "gate": "G2",
        "claim": "the LiTwo power series diverges at w1, so Lean's tsum returns 0",
        "partial_sums_at_w1_n20_n40_n80": growth,
        "pass": bool(diverges and li_two_lean(w1) == 0 and li_two_lean(-w1) == 0),
    })

    # the argument dictionary the ladder uses
    q = (-w1) / (-w1 - 1)
    r = (-w2) / (-w2 - 1)
    s = -w3

    # ---- G3 (REFUTATION): hinv1 and hlan1 FAIL under literal Lean semantics ----
    res_inv = rogers_lean(w1) + rogers_lean(1 / w1) - 2 * l1
    res_lan = rogers_lean(-w1) + rogers_lean((-w1) / (-w1 - 1))
    gates.append({
        "gate": "G3",
        "claim": "REFUTATION: hinv1 and hlan1 are FALSE for a Rogers L built on the corpus LiTwo",
        "hinv1_residual": nstr(res_inv, 12),
        "hlan1_residual": nstr(res_lan, 12),
        "note": "gate passes when both failures are confirmed, i.e. residuals are NOT small",
        "pass": bool(fabs(res_inv) > mpf("0.1") and fabs(res_lan) > mpf("0.1")),
    })

    # ---- G4: the other seven hypotheses DO hold under the same semantics ----
    others = {
        "hlan2": rogers_lean(-w2) + rogers_lean(r),
        "hlan3": rogers_lean(w3) + rogers_lean(w3 / (w3 - 1)),
        "refl_w2": rogers_lean(w2) + rogers_lean(1 - w2) - l1,
        "refl_q": rogers_lean(q) + rogers_lean(1 - q) - l1,
        "refl_r": rogers_lean(r) + rogers_lean(1 - r) - l1,
        "refl_s": rogers_lean(s) + rogers_lean(1 - s) - l1,
    }
    worst4 = max(fabs(v) for v in others.values())
    gates.append({
        "gate": "G4",
        "claim": "the failure is localised: every hypothesis whose arguments stay in [-1,1] holds",
        "residuals": {k: nstr(v, 8) for k, v in others.items()},
        "worst": nstr(worst4, 8),
        "pass": bool(worst4 < TOL),
    })

    # ---- G5: the definitional extension repairs both ----
    rep = {
        "hinv1": rogers_ext(w1, l1) + rogers_ext(1 / w1, l1) - 2 * l1,
        "hlan1": rogers_ext(-w1, l1) + rogers_ext(q, l1),
        "hlan2": rogers_ext(-w2, l1) + rogers_ext(r, l1),
        "hlan3": rogers_ext(w3, l1) + rogers_ext(w3 / (w3 - 1), l1),
    }
    worst5 = max(fabs(v) for v in rep.values())
    gates.append({
        "gate": "G5",
        "claim": "under `extend` all four reduction hypotheses hold -- by construction, not by analysis",
        "residuals": {k: nstr(v, 8) for k, v in rep.items()},
        "worst": nstr(worst5, 8),
        "pass": bool(worst5 < TOL),
    })

    # ---- G6: reflection survives the extension ----
    refl = {nm: rogers_ext(v, l1) + rogers_ext(1 - v, l1) - l1
            for nm, v in [("w2", w2), ("q", q), ("r", r), ("s", s)]}
    worst6 = max(fabs(v) for v in refl.values())
    gates.append({
        "gate": "G6",
        "claim": "reflection is unchanged by the extension (both arguments stay in the middle branch)",
        "residuals": {k: nstr(v, 8) for k, v in refl.items()},
        "worst": nstr(worst6, 8),
        "pass": bool(worst6 < TOL),
    })

    # ---- G7: the extension agrees with the principal-branch analytic Rogers L ----
    agree = {nm: rogers_ext(v, l1) - rogers_principal(v)
             for nm, v in [("w1", w1), ("-w1", -w1), ("w2", w2),
                           ("-w2", -w2), ("w3", w3), ("-w3", -w3)]}
    worst7 = max(fabs(v) for v in agree.values())
    gates.append({
        "gate": "G7",
        "claim": "the piecewise extension agrees with Re of the principal-branch analytic Rogers L "
                 "at all six points -- EVIDENCE that the repair is the right one, not a proof",
        "residuals": {k: nstr(v, 8) for k, v in agree.items()},
        "worst": nstr(worst7, 8),
        "pass": bool(worst7 < TOL),
    })

    # ---- G8: end to end -- the numerators, from the extension alone ----
    targets, per = [], []
    for k, (w, m) in enumerate(zip([w1, w2, w3], [17, 5, -1]), 1):
        t = 2 * rogers_ext(w, l1) + rogers_ext(-w, l1)
        targets.append(t)
        per.append({"k": k, "value": nstr(t, 24), "m": m,
                    "abs_err": nstr(fabs(t - mpf(m) * l1 / 7), 8)})
    worst8 = max(fabs(t - mpf(m) * l1 / 7) for t, m in zip(targets, [17, 5, -1]))
    sum_err = fabs(sum(targets) - 3 * l1)
    gates.append({
        "gate": "G8",
        "claim": "from `extend` alone the numerators are (17,5,-1)/7 and the sum is 3*L1 = pi^2/2",
        "per_k": per,
        "sum": nstr(sum(targets), 24), "sum_target": nstr(3 * l1, 24),
        "sum_abs_err": nstr(sum_err, 8), "worst": nstr(worst8, 8),
        "pass": bool(worst8 < TOL and sum_err < TOL),
    })

    out = {
        "probe": "qbeta_5two_route13_rogers_extension",
        "bean": "qou-rhyp",
        "parent_bean": "qou-0yqu",
        "dps": mp.dps,
        "lean_file": "QOU/QBeta/FiveTwoRogersExtend.lean",
        "gates": gates,
        "verdict": {
            "correction": "qou-rhyp graded inversion and Landen as hard-but-provable analysis. Two of "
                          "them (hinv1, hlan1) are instead FALSE for a Rogers L built on the corpus's "
                          "LiTwo, because their arguments w1 = 2.2469796... and -w1 leave the disc of "
                          "convergence, where Lean's tsum is the junk value 0 and Real.log is even.",
            "repair": "definitional, not analytic: extend by inversion above 1 and Landen below 0 "
                      "(Zagier SS I.3). All four reduction hypotheses then hold by construction. "
                      "Formalised sorry-free in QOU/QBeta/FiveTwoRogersExtend.lean, generic in f and c, "
                      "axioms [propext, Classical.choice, Quot.sound].",
            "what_the_repair_costs": "the Lean object is a piecewise function, NOT proved equal to the "
                                     "analytic continuation of Li_2. G7 checks they agree at the six "
                                     "points in play. Agreement is evidence, not identification.",
            "net_effect": "of the twelve hypotheses numerators_original_form takes, four reduction ones "
                          "are now discharged for any f, and reflection transports through the "
                          "extension. The genuinely open input is exactly the three five-term "
                          "instances hA, hB, hC.",
            "why_missed": "route11's probe used mpmath polylog -- the true analytic continuation -- so "
                          "it was testing the mathematics, not the Lean semantics. Both were right on "
                          "their own terms; the gap was between them.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route13-rogers-extension.witness.json")
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
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:88]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: hinv1/hlan1 were FALSE, not hard. `extend` repairs them by construction;")
    print("         the three five-term instances are now the only open input to the numerators.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
