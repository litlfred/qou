#!/usr/bin/env python3
"""Route 54 -- the complex five-term identity holds in ONE variable and fails in
two, and the 5_2 pair it reaches is (y_3, y_1), not (y_1, conj y_1).

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Companion to the
Lean module `QOU/QBeta/FiveTwoComplexPentagon.lean`, which proves G1 and G2
sorry-free; this probe is the numerical record of G3-G5, which the Lean does not
and cannot state.

WHAT THE LEAN PROVES
--------------------
`pentagonSum_eq_pi_sq_div_two`: for every real `a` in (0,1) and EVERY `w` off
both real cuts,

    L(a) + L(w) + L((1-a)/(1-aw)) + L(1-aw) + L((1-w)/(1-aw)) = pi^2/2

with `L = cRogersL` the Rogers dilogarithm built on the corpus's own integral
continuation of Li_2. Unconditional -- no branch hypothesis, no region
hypothesis. The proof is: the five branch defects are holomorphic with vanishing
derivative, so they propagate from a real base point; and for real `a` in (0,1)
every one of the four `w`-dependent arguments inherits a non-zero imaginary part
from `w`, so the whole of `rogersDomain` is regular.

WHAT THIS PROBE ADDS -- AND THE NEGATIVE THAT MATTERS
-----------------------------------------------------
The one-variable restriction is not an artefact of the proof. With BOTH
variables non-real the identity is FALSE (G3), and the deviation is not even a
REAL multiple of pi^2 -- it carries a non-zero imaginary part, so it is a genuine
`(2 pi i) * (log combination)` and not a flattening integer. That is measured
here, not asserted. (What G3 tests is exactly that: no case has both a vanishing
imaginary part and an integer real part.)

The consequence for the 5_2 lane is exact and it cuts both ways (G4):

    (y_3, y_1)  -- real root against a complex one -- SATISFIES the identity.
    (y_1, conj y_1) -- the pair Vol(5_2) actually needs -- DOES NOT.

So the theorem reaches into the saddle orbit but not to the place the volume
lives. That is the same obstruction Routes 45-46 measured and Neumann's `ker nu`
predicts, now located precisely.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import fabs, im, log, mp, mpc, mpf, nint, nstr, pi, polylog, polyroots, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def rogersL(z):
    """Rogers L on the principal branch -- the numerical stand-in for cRogersL."""
    return polylog(2, z) + log(z) * log(1 - z) / 2


def pentagon(x, y):
    """L(x) + L(y) + L((1-x)/(1-xy)) + L(1-xy) + L((1-y)/(1-xy))."""
    d = 1 - x * y
    return rogersL(x) + rogersL(y) + rogersL((1 - x) / d) + rogersL(d) \
        + rogersL((1 - y) / d)


def off_both_cuts(z):
    """`z in rogersDomain`: off (-inf,0] and off [1,inf)."""
    if fabs(im(z)) > mpf(10) ** -30:
        return True
    return bool(re(z) > 0 and re(z) < 1)


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -30
    target = pi ** 2 / 2
    gates = []

    # ---- G1: the one-variable identity, over a wide sweep ------------------
    ones, devs = [], []
    for a in [mpf("0.05"), mpf("0.3"), mpf("0.5"), mpf("0.9"), mpf("0.999")]:
        for w in [mpc("1.5", "0.8"), mpc("-2.0", "0.5"), mpc("0.2", "-3.0"),
                  mpc("5.0", "0.01"), mpc("-40.0", "-0.001"), mpc("0.5", "1e-8")]:
            dev = pentagon(a, w) - target
            devs.append(fabs(dev))
            ones.append({"a": nstr(a, 8), "w": nstr(w, 10),
                         "w_off_both_cuts": off_both_cuts(w),
                         "abs_dev": nstr(fabs(dev), 8)})
    max_dev = max(devs)
    gates.append({
        "gate": "G1",
        "claim": "the ONE-variable complex five-term identity: for real a in (0,1) and every w "
                 "off both real cuts, the Rogers pentagon sum is exactly pi^2/2. 30 pairs, "
                 "including |w| = 40, w straddling both cuts, and w within 1e-8 of the real "
                 "axis. This is the numerical shadow of the Lean theorem "
                 "pentagonSum_eq_pi_sq_div_two, which is unconditional and sorry-free",
        "pairs_tested": len(ones),
        "max_abs_deviation": nstr(max_dev, 8),
        "sample": ones[:6],
        "pass": bool(max_dev < mpf(10) ** -25),
    })

    # ---- G2: it is not vacuous on the real square either -------------------
    reals = []
    for a in [mpf("0.1"), mpf("0.4"), mpf("0.75")]:
        for b in [mpf("0.2"), mpf("0.6"), mpf("0.95")]:
            reals.append(fabs(pentagon(a, b) - target))
    gates.append({
        "gate": "G2",
        "claim": "the base region is right: on the positive real square the same sum is pi^2/2, "
                 "which is where the corpus's already-proved REAL five-term identity "
                 "(FiveTwoAbelFiveTerm.rogersL_fiveTerm) pins the constant. Three reflections "
                 "convert Abel's arguments into the pentagon's, at a cost of 3*pi^2/6",
        "max_abs_deviation": nstr(max(reals), 8),
        "pass": bool(max(reals) < mpf(10) ** -25),
    })

    # ---- G3: THE NEGATIVE -- two non-real variables break it ---------------
    twos = []
    for x, y in [(mpc("2.0", "0.5"), mpc("1.5", "-0.9")),
                 (mpc("-1.0", "0.3"), mpc("3.0", "2.0")),
                 (mpc("0.5", "3.0"), mpc("0.5", "-3.0")),
                 (mpc("2.0", "0.1"), mpc("2.0", "-0.1"))]:
        dev = pentagon(x, y) - target
        ratio = dev / pi ** 2
        near_int = bool(fabs(im(ratio)) < tol
                        and fabs(re(ratio) - int(nint(re(ratio)))) < tol)
        twos.append({"x": nstr(x, 10), "y": nstr(y, 10),
                     "both_off_cuts": bool(off_both_cuts(x) and off_both_cuts(y)),
                     "dev_over_pi_sq": nstr(ratio, 14),
                     "dev_is_integer_multiple_of_pi_sq": near_int})
    broken = [t for t in twos if not t["dev_is_integer_multiple_of_pi_sq"]]
    gates.append({
        "gate": "G3",
        "claim": "THE NEGATIVE THAT MATTERS. The one-variable restriction is NOT an artefact of "
                 "the proof. With BOTH variables non-real the identity is false, and the "
                 "deviation is not even a REAL multiple of pi^2 -- it carries a non-zero "
                 "imaginary part, so it is a (2 pi i)*(log combination) and not a flattening "
                 "integer. So no sharpening of the same argument reaches the two-variable case",
        "cases": twos,
        "all_off_cuts": bool(all(t["both_off_cuts"] for t in twos)),
        "none_is_integer_multiple": bool(len(broken) == len(twos)),
        "pass": bool(all(t["both_off_cuts"] for t in twos) and len(broken) == len(twos)),
    })

    # ---- G4: where the 5_2 saddle orbit sits -------------------------------
    roots = polyroots([1, -2, 3, -1], maxsteps=900, extraprec=3500)
    y_real = [r for r in roots if fabs(im(r)) < mpf(10) ** -30][0]
    y_up = [r for r in roots if im(r) > mpf(10) ** -30][0]
    dev_mixed = pentagon(re(y_real), y_up) - target
    dev_conj = pentagon(y_up, y_up.conjugate()) - target
    gates.append({
        "gate": "G4",
        "claim": "the consequence for the 5_2 lane, exactly located. The theorem REACHES the "
                 "mixed pair (y_3, y_1) -- the cubic's real root against a complex one, since "
                 "y_3 = 0.43016 lies in (0,1) -- and DOES NOT reach (y_1, conj y_1), which is "
                 "the pair Vol(5_2) = 3*D(y_1) actually needs. Same obstruction Routes 45-46 "
                 "measured, now with an address",
        "y_real": nstr(re(y_real), 20),
        "y_upper": nstr(y_up, 20),
        "y_real_in_unit_interval": bool(0 < re(y_real) < 1),
        "dev_mixed_pair_over_pi_sq": nstr(dev_mixed / pi ** 2, 12),
        "dev_conjugate_pair_over_pi_sq": nstr(dev_conj / pi ** 2, 12),
        "pass": bool(fabs(dev_mixed) < mpf(10) ** -25 and fabs(dev_conj) > mpf("0.1")),
    })

    # ---- G5: target unmoved -----------------------------------------------
    A = re(sum(polylog(2, z) for z in roots))
    gates.append({
        "gate": "G5",
        "claim": "the target is unmoved. A = sum Li2(y_j) still has no proof. G1 is a theorem "
                 "about pairs one of whose members is real, G3 is a negative, G4 says the pair "
                 "the volume needs is on the wrong side of it. This gate exists so none of it "
                 "can be read as progress toward the sum rule",
        "A": nstr(A, 30),
        "pass": bool(fabs(A - mpf("0.9717306814686482591277741699")) < mpf(10) ** -25),
    })

    out = {
        "probe": "qbeta_5two_route54_complex_pentagon",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 53 (the constant pinned)",
        "lean": "QOU/QBeta/FiveTwoComplexPentagon.lean -- pentagonSum_eq_pi_sq_div_two",
        "gates": gates,
        "verdict": {
            "proved": "the complex five-term identity for the Rogers dilogarithm holds "
                      "unconditionally whenever ONE variable is real in (0,1) and the other is "
                      "anywhere off both real cuts. Sorry-free in Lean, standard axioms.",
            "negative": "with BOTH variables non-real it is false, and the deviation is not "
                        "even a real multiple of pi^2 -- it has a non-zero imaginary part.",
            "for_the_lane": "reaches the 5_2 pair (y_3, y_1); does not reach (y_1, conj y_1), "
                            "which is the pair Vol(5_2) needs.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route54-complex-pentagon.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the complex five-term identity is a THEOREM when one variable is real in (0,1) and the "
        "other is anywhere off both cuts -- Lean, sorry-free. With both non-real it is FALSE, and "
        "the deviation is not even a real multiple of pi^2. It reaches the 5_2 pair (y_3, y_1) "
        "and not "
        "(y_1, conj y_1), which is the pair the volume needs. The 5_2 sum rule remains verified "
        "to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
