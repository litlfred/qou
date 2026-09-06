#!/usr/bin/env python3
"""Yes — the substrate carries fractional twist, from `n = 5` upward, and the
available values are RATIONAL. QCD's colour ratio `2` is hit exactly. The
nuclear `33.7` is not in the set at all.

PARTLY RETRACTED — READ `the_twist_is_absent_where_it_is_needed_probe.py`
------------------------------------------------------------------------
Two things below do not survive.

1. **The cumulative enumeration is not a predictive claim.** The union of
   achievable `t` over `n <= 24` covers `43` of the `45` rationals with
   denominator `<= 12` (`96 %`). Eight exact group-theoretic ratios all "hit"
   it, because almost everything does. The `n <= 12` table below looks sparse
   only because of where it was cut.
2. **The `t = 1/3` hit is withdrawn as evidence.** It is realised at `n = 12`,
   but two quarks are `n = 2`. A colour observable for `3 (x) 3` cannot be
   evaluated at `4He`'s strand count.

And the decisive fact, which this probe did not check: per strand count the
admissible sets are small, and **`n = 2`, `n = 3` and `n = 6` admit none at
all** — so the two-nucleon sector, where the obstruction lives, cannot be
repaired by this mechanism.

**What stands:** the mechanism itself — `c_n^n = Delta^2`, block magnitude
exactly `q^(2 c(lambda)/n)`, fractionality from `n = 5` — and the per-`n`
availability table as a sparse closed-form structure.

THE QUESTION
------------
`the_hull_exit_is_a_fractional_twist_probe` (bean `qou-vlrq`) showed the
`det T = -1` obstruction is broken by a framing scalar `c`, admissible in
`c in (1/q, 1]`, and that the exponent must be **fractional**: one full
crossing's writhe is already too strong. In the substrate's own base that reads

    c = q^-t ,   t in [0, 1) ,   ratio = (1 + t)/(1 - t)

with `t = 1/3` for QCD's colour ratio `2` and `t = 0.942372321950` for the
nuclear `33.7055`. Left open, and named as the one well-posed question
remaining: **can the substrate produce a fractional `t` at all?**

THE MECHANISM IS ALREADY THERE
------------------------------
The Coxeter element `c_n = s_1 s_2 ... s_{n-1}` satisfies `c_n^n = Delta^2`, the
full twist and generator of the centre of `B_n`. So `c_n` is a genuine **n-th
root of a full twist** — a fractional twist by construction, not an imported
device. Verified here: `Delta^2` acts as a scalar on every block at
`n = 3, 4, 5`, and

    |eigenvalue of c_n on block lambda|  =  q^( 2 c(lambda) / n )

exactly, where `c(lambda) = sum over cells of (j - i)` is the content sum. The
twist exponents are therefore **rational with denominator dividing `n`**.

WHERE FRACTIONALITY STARTS
--------------------------
    n = 3   exponents  2, 0, -2                      all integer
    n = 4   exponents  3, 1, 0, -1, -3               all integer
    n = 5   exponents  4, 2, 4/5, 0, -4/5, -2, -4    **fractional at (3,2) and (2,2,1)**

`2 c(lambda)` is always even, so at `n = 3` and `n = 4` it is divisible by `n`
for every partition and the fractional part vanishes. **`n = 5` is the first
strand count that carries a fractional twist**, and it carries `t = 4/5`.

So the answer to the question is **yes** — and it needed no new ingredient. The
n-th roots of the full twist were in the braid group all along; what was missing
was noticing that their block magnitudes are fractional powers of `q` while the
`n = 2` and `n = 3` cases, which the arc had been working in, happen not to be.

(Contrast the ribbon twist read off the content sum directly,
`theta_lambda = q^(2 c(lambda))`: always an integer power, at every `n`. The
fractionality lives specifically in taking a **root** of the twist, not in the
twist itself.)

WHAT VALUES ARE ACTUALLY AVAILABLE
----------------------------------
Requiring `t = -2 c(lambda) / n in (0, 1)` — inside the window — over all
partitions with `n <= 12`:

    t       ratio    first realisation
    2/11    13/9     n=11 (5,2,2,1,1)
    2/9     11/7     n=9  (4,2,2,1)
    2/7     9/5      n=7  (3,2,2)
    1/3     2        n=12 (4,4,2,1,1)      <== QCD colour ratio, EXACTLY
    4/11    15/7     n=11 (4,3,2,2)
    1/2     3        n=8  (3,3,1,1)
    3/5     4        n=10 (4,3,1,1,1)
    2/3     5        n=9  (3,3,2,1)
    8/11    19/3     n=11 (4,3,2,1,1)
    4/5     9        n=5  (2,2,1)
    6/7     13       n=7  (3,2,1,1)
    8/9     17       n=9  (4,2,1,1,1)
    10/11   21       n=11 (5,2,1,1,1,1)

Thirteen distinct twists, and **every achievable ratio is rational** — a direct
consequence of `t` being rational.

THE TWO TARGETS COME OUT OPPOSITE
---------------------------------
**QCD's ratio is hit exactly.** `t = 1/3` gives `(1+t)/(1-t) = 2`, and `2` is
precisely the `3bar / 6` colour-factor ratio from `3 (x) 3` — exact `SU(3)`
group theory with no error bar and nothing fitted on either side. It is realised
at `n = 12` by `(4,4,2,1,1)` and `(4,3,3,2)`, and at no smaller `n`.

**The nuclear ratio is not in the set.** `33.7055` requires `t = 0.942372`; the
nearest available is `10/11` giving `21`. Reaching `21` would need the `np`
`1S0` virtual state at `105.9 keV` against the accepted `~66 keV` — a `60 %`
shift, far outside any uncertainty on that number. No partition at `n <= 12`
supplies it, and the set is rational while the target is not.

READ THIS CAREFULLY
-------------------
The `t = 1/3` hit is exact and unfitted, and that is worth something. But
thirteen rationals is not a sparse set, and `1/3` is not an unlikely member of
it — the coincidence is suggestive, not evidential, and this probe does not
claim otherwise. What **is** established without qualification:

* the substrate carries fractional twist, from `n = 5`, via an object already in
  the braid group;
* the available twists are rational with denominator dividing `n`, hence so are
  the achievable channel ratios;
* an exact group-theoretic target lands inside that set and a measured
  experimental one does not.

That last asymmetry is the finding. A construction whose achievable ratios are
rational can meet a group-theory target and cannot meet a dynamical one — and
the nuclear sector's `33.7` is dynamical, set by how close two shallow states
sit to threshold.

DISCIPLINE
----------
No fit. `Delta^2 = c_n^n` and the scalar action are verified before use; the
magnitude formula `q^(2c/n)` is asserted against the computed spectra rather
than assumed; the enumeration is exhaustive over partitions for `n <= 12`. The
`1/3` coincidence is reported with its own significance assessed downward.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] the_hull_exit_is_a_fractional_twist_probe.py (the question)
-- Ref: [probe] level_three_colour_channel_probe.py (the QCD target)
-- Ref: [probe] isospin_grading_restores_the_sign_probe.py (the nuclear target)
"""
from __future__ import annotations

import sys
import warnings
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

from hecke_characters import build_seminormal_matrices  # noqa: E402
from q_parameter import q_at  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
_Q = q_at(mp.mp.dps)
LQ = float(mp.log(_Q))
NMAX = 12
B_DEUT = AME_B_DEUTERON_MEV_VALIDATION
B_VIRT = mp.mpf("0.066")
R_NUC = B_DEUT / B_VIRT
T_NUC = float((R_NUC - 1) / (R_NUC + 1))


def partitions(n):
    out = []

    def rec(r, mx, cur):
        if r == 0:
            out.append(tuple(cur))
            return
        for p in range(min(r, mx), 0, -1):
            rec(r - p, p, cur + [p])
    rec(n, n, [])
    return out


def content(l):
    return sum(j - i for i, r in enumerate(l) for j in range(r))


def coxeter_spectrum(n, lam):
    """(is Delta^2 scalar, sorted distinct q-exponents of |eig(c_n)|)"""
    S = [np.asarray(m, dtype=float)
         for m in build_seminormal_matrices(list(lam))[0]]
    d = S[0].shape[0]
    C = np.eye(d)
    for g in range(n - 1):
        C = C @ S[g]
    F = np.linalg.matrix_power(C, n)
    scalar = np.allclose(F, F[0, 0] * np.eye(d), atol=1e-8)
    ks = sorted({round(float(np.log(abs(z)) / LQ), 8)
                 for z in np.linalg.eigvals(C)})
    return scalar, ks


def main() -> int:
    assertions = []
    print("t7qv — can the substrate carry a fractional twist at all?")

    # ── A1. the Coxeter element is an n-th root of the full twist ──────
    print("\n  1. the mechanism is already in the braid group")
    print(f"     c_n = s_1 s_2 ... s_(n-1) satisfies c_n^n = Delta^2, the full")
    print(f"     twist and centre generator — so c_n is an n-th root of a twist.")
    allscalar = True
    for n in (3, 4, 5):
        for lam in partitions(n):
            sc, _ks = coxeter_spectrum(n, lam)
            allscalar = allscalar and sc
    print(f"     Delta^2 acts as a SCALAR on every block at n = 3, 4, 5: "
          f"{allscalar}")
    ok = allscalar
    assertions.append(("A1_coxeter_is_an_nth_root_of_the_full_twist", ok,
                       "Delta^2 = c_n^n acts as a scalar on every block at "
                       "n=3,4,5"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the magnitude formula ──────────────────────────────────────
    print("\n  2. its block magnitude is exactly q^(2 c(lambda)/n)")
    worst = 0.0
    for n in (3, 4, 5):
        for lam in partitions(n):
            _sc, ks = coxeter_spectrum(n, lam)
            pred = 2 * content(lam) / n
            worst = max(worst, max(abs(k - pred) for k in ks))
    print(f"     c(lambda) = sum over cells of (j - i), the content sum")
    print(f"     worst deviation of any computed exponent from 2c/n: "
          f"{worst:.2e}")
    print(f"     every block has a SINGLE magnitude, so the twist exponent is")
    print(f"     rational with denominator dividing n.")
    ok = worst < 1e-6
    assertions.append(("A2_magnitude_is_q_to_the_2c_over_n", ok,
                       f"worst deviation from q^(2c/n) is {worst:.2e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. fractionality starts at n=5 ────────────────────────────────
    print("\n  3. where fractionality starts")
    first = None
    for n in range(2, 8):
        exps = sorted({Fraction(2 * content(l), n) for l in partitions(n)})
        frac = [e for e in exps if e.denominator != 1]
        tag = f"   FRACTIONAL: {frac}" if frac else "   all integer"
        print(f"     n = {n}: exponents {[str(e) for e in exps]}{tag}")
        if frac and first is None:
            first = n
    print(f"     2c(lambda) is always even, so at n = 3 and n = 4 it is")
    print(f"     divisible by n for every partition. n = {first} is the FIRST")
    print(f"     strand count carrying a fractional twist.")
    print(f"     (the ribbon twist read directly off the content sum,")
    print(f"     theta = q^(2c), is an integer power at every n — the")
    print(f"     fractionality lives in taking a ROOT, not in the twist itself.)")
    ok = first == 5
    assertions.append(("A3_fractional_twist_first_appears_at_n5", ok,
                       f"first fractional exponent at n = {first}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. the achievable set ─────────────────────────────────────────
    print(f"\n  4. what is available, exhaustively for n <= {NMAX}")
    seen: dict = {}
    for n in range(2, NMAX + 1):
        for lam in partitions(n):
            t = Fraction(-2 * content(lam), n)
            if 0 < t < 1:
                seen.setdefault(t, []).append((n, lam))
    print(f"     {'t':>7s} {'ratio':>8s}   first realisation")
    for t in sorted(seen):
        n, lam = seen[t][0]
        r = (1 + t) / (1 - t)
        star = "   <== QCD colour ratio, EXACTLY" if t == Fraction(1, 3) else ""
        print(f"     {str(t):>7s} {str(r):>8s}   n={n} {lam}{star}")
    ratios = sorted((1 + t) / (1 - t) for t in seen)
    ok = len(seen) == 13 and all(isinstance(r, Fraction) for r in ratios)
    print(f"     {len(seen)} distinct twists; EVERY achievable ratio is rational,")
    print(f"     a direct consequence of t being rational.")
    assertions.append(("A4_achievable_twists_are_rational", ok,
                       f"{len(seen)} distinct t in (0,1) for n <= {NMAX}, all "
                       f"rational, hence all ratios rational"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. QCD's ratio is hit exactly ─────────────────────────────────
    print("\n  5. QCD's colour ratio is hit EXACTLY")
    third = Fraction(1, 3)
    has = third in seen
    print(f"     t = 1/3 available: {has}")
    if has:
        print(f"       realisations: {seen[third]}")
        print(f"       smallest n: {min(n for n, _l in seen[third])}")
    print(f"       ratio (1+t)/(1-t) = {(1 + third) / (1 - third)} — exactly the")
    print(f"       3bar/6 colour-factor ratio from 3 (x) 3, which is exact SU(3)")
    print(f"       group theory with no error bar. Nothing fitted on either side.")
    ok = has and (1 + third) / (1 - third) == 2
    assertions.append(("A5_qcd_colour_ratio_is_exactly_available", ok,
                       f"t = 1/3 realised at n = "
                       f"{min(n for n, _l in seen[third]) if has else 'n/a'}, "
                       f"giving ratio exactly 2"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the nuclear ratio is not in the set ────────────────────────
    print("\n  6. the nuclear ratio is NOT in the set")
    closest = min(seen, key=lambda t: abs(float(t) - T_NUC))
    r_close = (1 + closest) / (1 - closest)
    need_virt = B_DEUT / mp.mpf(float(r_close))
    print(f"     nuclear needs t = {T_NUC:.12f}  (ratio {float(R_NUC):.4f})")
    print(f"     nearest available t = {closest} = {float(closest):.12f}, "
          f"ratio {r_close}")
    print(f"     reaching {r_close} would need the np 1S0 virtual state at")
    print(f"     {float(need_virt * 1000):.1f} keV against the accepted ~66 keV —")
    print(f"     a {float(100 * (need_virt / B_VIRT - 1)):.0f} % shift, far outside "
          f"any uncertainty on it.")
    print(f"     The available set is RATIONAL; the target is dynamical, set by")
    print(f"     how close two shallow states sit to threshold, and is not.")
    ok = float(closest) < T_NUC and abs(float(need_virt) / float(B_VIRT) - 1) > 0.4
    assertions.append(("A6_nuclear_ratio_is_not_available", ok,
                       f"nearest t = {closest} gives ratio {r_close}, needing a "
                       f"{float(need_virt * 1000):.1f} keV virtual state vs ~66"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Yes. The Coxeter element c_n = s_1...s_(n-1) is an n-th root of the")
    print("  full twist, its block magnitude is exactly q^(2c(lambda)/n), and")
    print("  from n = 5 that exponent is fractional. The mechanism needed no new")
    print("  ingredient — it was in the braid group all along, and the arc had")
    print("  been working at n = 2 and n = 3 where 2c is divisible by n and the")
    print("  fractional part happens to vanish.")
    print("  The available twists are rational with denominator dividing n, so")
    print("  the achievable channel ratios are rational too. That makes the two")
    print("  targets come out opposite: QCD's colour ratio 2 is hit EXACTLY at")
    print("  t = 1/3, with nothing fitted on either side, while the nuclear")
    print("  33.7055 is not in the set at all — the nearest is 21, which would")
    print("  need a 106 keV virtual state against the accepted 66.")
    print("  The 1/3 hit is exact and unfitted, but thirteen rationals is not a")
    print("  sparse set and 1/3 is not an unlikely member: suggestive, not")
    print("  evidential. The finding is the ASYMMETRY — a construction whose")
    print("  ratios are rational can meet a group-theory target and cannot meet")
    print("  a dynamical one.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="numpy")
        wb.set_description(
            "Answers the question qou-vlrq left open: can the substrate produce "
            "the fractional framing twist that the det T = -1 hull exit "
            "requires? YES, and with no new ingredient. The Coxeter element "
            "c_n = s_1...s_(n-1) satisfies c_n^n = Delta^2, the full twist and "
            "centre generator of B_n, so it is a genuine n-th root of a twist; "
            "Delta^2 is verified to act as a scalar on every block at n=3,4,5, "
            "and the block magnitude of c_n is exactly q^(2 c(lambda)/n) with "
            "c(lambda) the content sum (worst deviation 1e-8 or better). Twist "
            "exponents are therefore rational with denominator dividing n. "
            "Since 2c(lambda) is always even it is divisible by n at n=3 and "
            "n=4, so n = 5 is the FIRST strand count carrying a fractional "
            "twist (t = 4/5 at (3,2) and (2,2,1)) — the arc had been working at "
            "n=2 and n=3 where the fractional part vanishes. Contrast the ribbon "
            "twist read directly off the content sum, theta = q^(2c), which is "
            "an integer power at every n: the fractionality lives in taking a "
            "ROOT of the twist, not in the twist. Exhaustive enumeration over "
            "partitions with n <= 12 gives 13 distinct t in (0,1), and every "
            "achievable channel ratio (1+t)/(1-t) is rational. The two targets "
            "come out opposite. QCD's colour ratio 2 — the exact 3bar/6 "
            "colour-factor ratio from 3(x)3 — is hit EXACTLY at t = 1/3, "
            "realised at n=12 by (4,4,2,1,1) and (4,3,3,2), with nothing fitted "
            "on either side. The nuclear 33.7055 needs t = 0.942372 and is NOT "
            "in the set; the nearest is 10/11 giving 21, which would require the "
            "np 1S0 virtual state at 105.9 keV against the accepted ~66 keV, a "
            "60% shift far outside its uncertainty. The 1/3 coincidence is "
            "reported with its significance assessed downward: 13 rationals is "
            "not a sparse set and 1/3 is not an unlikely member.")
        wb.add_data("mechanism",
                    {"element": "c_n = s_1 s_2 ... s_{n-1}",
                     "relation": "c_n^n = Delta^2 (full twist, centre of B_n)",
                     "block_magnitude": "q^(2 c(lambda) / n)",
                     "worst_deviation": f"{worst:.3e}",
                     "delta2_scalar_on_all_blocks_n345": allscalar})
        wb.add_data("onset_of_fractionality",
                    {str(n): [str(Fraction(2 * content(l), n))
                              for l in partitions(n)]
                     for n in range(2, 7)})
        wb.add_data("available_twists",
                    {str(t): {"ratio": str((1 + t) / (1 - t)),
                              "first_n": seen[t][0][0],
                              "first_partition": str(seen[t][0][1]),
                              "n_realisations": len(seen[t])}
                     for t in sorted(seen)})
        wb.add_data("targets",
                    {"QCD": {"required_t": "1/3", "ratio": "2",
                             "available": has,
                             "smallest_n": min(n for n, _l in seen[third])
                             if has else None},
                     "nuclear": {"required_t": f"{T_NUC:.12f}",
                                 "ratio": f"{float(R_NUC):.6f}",
                                 "available": False,
                                 "nearest_t": str(closest),
                                 "nearest_ratio": str(r_close),
                                 "implied_virtual_state_keV":
                                     f"{float(need_virt * 1000):.2f}",
                                 "accepted_virtual_state_keV": "66"}})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE t = 1/3 HIT IS SUGGESTIVE, NOT EVIDENTIAL. It is exact and "
            "nothing is fitted on either side, which is worth recording. But "
            "the achievable set for n <= 12 has thirteen members and 1/3 is not "
            "an unlikely element of a set of small-denominator rationals. No "
            "significance test is offered and none should be inferred. What is "
            "established without qualification is the ASYMMETRY: a rational set "
            "can meet an exact group-theoretic target and cannot meet a "
            "dynamical one.")
        wb.add_caveat(
            "THIS SHOWS THE TWIST EXISTS, NOT THAT THE CONSTRUCTION USES IT. "
            "The Coxeter element is an n-th root of the full twist and its "
            "block magnitudes are fractional powers of q from n=5. Nothing here "
            "attaches it to a bond, recomputes a binding energy, or exhibits "
            "any reason the physical bond SHOULD carry c_n rather than any other "
            "element. The hull exit needs a framing scalar; this demonstrates "
            "the substrate contains operators supplying fractional ones.")
        wb.add_caveat(
            "The n <= 12 enumeration is exhaustive over partitions but is a "
            "CUTOFF. Larger n supply further rationals with larger "
            "denominators, so 'not in the set' for the nuclear target is a "
            "statement about n <= 12, not a theorem. The substantive point "
            "survives the cutoff: the set is rational at every n while the "
            "nuclear target is a measured ratio of two shallow binding "
            "energies.")
        wb.add_caveat(
            "The nuclear target inherits qou-m896's least certain input, the "
            "np 1S0 virtual state at ~66 keV. That is why A6 is phrased as the "
            "shift REQUIRED (to 105.9 keV, 60%) rather than as a bare "
            "mismatch — the conclusion is robust precisely because the needed "
            "shift is far outside the uncertainty on that number.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
