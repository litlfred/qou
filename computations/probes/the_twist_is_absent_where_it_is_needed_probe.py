#!/usr/bin/env python3
"""The fractional twist exists — but not at the strand counts where the physics
lives. `n = 2`, `n = 3` and `n = 6` admit **none**, and that retires both
targets and most of my own previous claim.

WHAT THIS CORRECTS
------------------
`can_the_substrate_carry_a_fractional_twist_probe` (bean `qou-bq9l`) answered
"can the substrate carry a fractional twist?" with yes, exhibited the mechanism
(`c_n^n = Delta^2`, block magnitude `q^(2c(lambda)/n)`), enumerated the
achievable values for `n <= 12`, and observed that QCD's colour ratio `2` is hit
exactly at `t = 1/3`. It flagged that hit as suggestive rather than evidential.

**That flag was not strong enough, and the enumeration was over the wrong
object.** Both are fixed here, and the result reverses.

FIRST CORRECTION: THE CUMULATIVE SET IS DENSE
---------------------------------------------
Taking the union of achievable `t` over all `n` up to a cutoff:

    n <= 5     1 distinct t     2 % of the rationals with denominator <= 12
    n <= 8     4               9 %
    n <= 12   13              29 %
    n <= 16   32              51 %
    n <= 20   57              69 %
    n <= 24   86              96 %      (43 of 45; only 4/9 and 7/8 missing)

By `n <= 24` essentially every small-denominator rational is achievable, so a
"the substrate can only produce rational ratios" prediction has **no
discriminating power** in cumulative form. Tested against eight exact
group-theoretic ratios — QCD `3bar/6 = 2`, QCD singlet/octet `= 8`, `piN` at the
`Delta` `9` and `9/2`, quark-model `|mu_p/mu_n| = 3/2` and `g_A = 5/3`, `4`, and
`25/9` — **all eight "hit"**, because almost everything does. A test that
everything passes is not a test.

SECOND CORRECTION: CUMULATIVE IS THE WRONG OBJECT
-------------------------------------------------
A physical system has a **fixed** strand count. Two quarks are `n = 2`. A
nucleon is `n = 3`. A two-nucleon system is `n = 6`. `4He` is `n = 12`. The
union over all `n` describes nothing. Per `n` the sets are small:

    n    A    admissible t in (0,1)                          count
    3    1    NONE                                               0
    6    2    NONE                                               0
    9    3    2/9, 2/3, 8/9                                      3
    12   4    1/3, 1/2, 2/3                                      3
    15   5    2/15, 4/15, 2/5, 2/3, 4/5, 14/15                   6
    18   6    1/9, 2/9, 1/3, 5/9, 2/3, 7/9, 8/9                  7

So the quantisation *is* sharply constraining — just not in the form the
previous probe stated it.

THE RESULT: NOTHING AT THE STRAND COUNTS THAT MATTER
----------------------------------------------------
`t in (0,1)` requires `-2c(lambda)/n in (0,1)`, i.e. `c(lambda)` strictly
between `-n/2` and `0`. At `n = 6` the achievable content sums are

    {-15, -9, -5, -3, 0, 3, 5, 9, 15}

and the window needs `c in {-1, -2}`. **Neither exists.** The same at `n = 3`.
At `n = 2` the only negative content sum is `-1`, giving `t = 1` exactly — the
**excluded boundary**, where the `T = 0` channel unbinds and the ratio diverges.

Consequently:

* **The two-nucleon sector cannot be repaired by this mechanism.** That sector
  is `n = 6`, it is where `qou-v3u2` proved the impossibility lives, and it
  admits no admissible twist at all.
* **The `t = 1/3` QCD hit was at the wrong strand count.** It is realised at
  `n = 12`, but two quarks are `n = 2`, and `n = 2` offers only the excluded
  boundary. A colour observable for `3 (x) 3` cannot be evaluated at `4He`'s
  strand count. That hit is withdrawn as evidence.

WHAT SURVIVES
-------------
`qou-bq9l`'s mechanism stands: `c_n` is genuinely an `n`-th root of the full
twist, its block magnitude is exactly `q^(2c(lambda)/n)`, and fractional values
do occur from `n = 5`. The per-`n` availability table is a real and falsifiable
structure — sparse, computable, and closed-form.

What does not survive is the use I put it to. The twist exists in the substrate
and is absent at every strand count where this arc's two open questions are
posed. The honest summary of the last two probes together is: **the missing
ingredient was correctly identified, and the substrate does not supply it where
it is needed.**

DISCIPLINE
----------
This probe exists to test a claim of mine and it fails it. The coverage
measurement is the primary result and was computed before any target was
checked; the eight group-theoretic targets are reported as a demonstration that
the cumulative test has no power, not as matches.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] can_the_substrate_carry_a_fractional_twist_probe.py (corrected here)
-- Ref: [probe] the_hull_exit_is_a_fractional_twist_probe.py (why the twist is needed)
-- Ref: [probe] two_nucleon_pattern_is_unreachable_probe.py (the n=6 obstruction)
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

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

DENOM = 12
TARGETS = {
    "QCD 3bar/6": Fraction(2),
    "QCD singlet/octet": Fraction(8),
    "piN at Delta (9:1)": Fraction(9),
    "piN (9:2)": Fraction(9, 2),
    "quark model |mu_p/mu_n|": Fraction(3, 2),
    "quark model g_A": Fraction(5, 3),
    "width ratio 4": Fraction(4),
    "SU(6) 25/9": Fraction(25, 9),
}


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


def t_at(n):
    """admissible fractional twists at exactly n strands"""
    return sorted({Fraction(-2 * content(l), n) for l in partitions(n)
                   if 0 < Fraction(-2 * content(l), n) < 1})


def main() -> int:
    assertions = []
    print("t7qv — the twist exists, but not where the physics is")

    # ── A1. the cumulative set is dense ────────────────────────────────
    print("\n  1. FIRST CORRECTION: the cumulative set is dense")
    allr = sorted({Fraction(p, r) for r in range(2, DENOM + 1)
                   for p in range(1, r)})
    seen: set = set()
    cov = {}
    for N in (5, 8, 12, 16, 20, 24):
        for n in range(2, N + 1):
            seen |= set(t_at(n))
        c = len([t for t in allr if t in seen])
        cov[N] = (len(seen), c)
        print(f"     n <= {N:>2d}: {len(seen):>3d} distinct t, "
              f"{c:>2d}/{len(allr)} of the denominator-<= {DENOM} rationals "
              f"({100 * c / len(allr):.0f} %)")
    missing = [t for t in allr if t not in seen]
    print(f"     by n <= 24 only {len(missing)} are missing: "
          f"{[str(x) for x in missing]}")
    ok = cov[24][1] / len(allr) > 0.9
    print(f"     so a 'the substrate only produces rational ratios' prediction")
    print(f"     has NO discriminating power in cumulative form.")
    assertions.append(("A1_cumulative_set_is_dense", ok,
                       f"{cov[24][1]}/{len(allr)} = "
                       f"{100 * cov[24][1] / len(allr):.0f}% coverage by n<=24"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. every target trivially hits ────────────────────────────────
    print("\n  2. and so every group-theoretic target trivially 'hits'")
    print(f"     {'target':<26s} {'R':>7s} {'t':>8s}  in cumulative set?")
    hits = 0
    for k, R in TARGETS.items():
        t = (R - 1) / (R + 1)
        h = t in seen
        hits += h
        print(f"     {k:<26s} {str(R):>7s} {str(t):>8s}  {h}")
    ok = hits == len(TARGETS)
    print(f"     {hits}/{len(TARGETS)} hit. A test everything passes is not a test.")
    assertions.append(("A2_all_targets_trivially_hit_cumulatively", ok,
                       f"{hits}/{len(TARGETS)} group-theoretic targets in the "
                       f"cumulative set"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. per-n is the right object, and is sparse ───────────────────
    print("\n  3. SECOND CORRECTION: a physical system has a FIXED n")
    print(f"     two quarks are n=2; a nucleon n=3; two nucleons n=6; 4He n=12.")
    print(f"     {'n':>3s} {'A':>3s}  admissible t in (0,1)")
    per = {}
    for n in (2, 3, 6, 9, 12, 15, 18):
        ts = t_at(n)
        per[n] = ts
        s = ", ".join(str(t) for t in ts) if ts else "NONE"
        print(f"     {n:>3d} {n // 3:>3d}  {s}")
    ok = all(len(per[n]) <= 7 for n in per) and len(per[9]) == 3
    print(f"     per n the sets are SMALL — the quantisation is sharply")
    print(f"     constraining, just not in the form qou-bq9l stated it.")
    assertions.append(("A3_per_n_sets_are_sparse", ok,
                       "; ".join(f"n={n}: {len(per[n])}" for n in sorted(per))))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. nothing at n = 2, 3, 6 ─────────────────────────────────────
    print("\n  4. THE RESULT: nothing at the strand counts that matter")
    cs6 = sorted({content(l) for l in partitions(6)})
    cs3 = sorted({content(l) for l in partitions(3)})
    cs2 = sorted({content(l) for l in partitions(2)})
    print(f"     t in (0,1) needs c(lambda) strictly between -n/2 and 0.")
    print(f"     n=6: achievable content sums {cs6}")
    print(f"          window needs c in {{-1, -2}} — NEITHER EXISTS")
    print(f"     n=3: achievable content sums {cs3}")
    print(f"          window needs c in {{-1}} — does not exist")
    print(f"     n=2: achievable content sums {cs2}")
    print(f"          c = -1 gives t = 1 EXACTLY, the excluded boundary where")
    print(f"          the T=0 channel unbinds and the ratio diverges")
    ok = per[2] == [] and per[3] == [] and per[6] == [] \
        and not any(-3 < c < 0 for c in cs6)
    assertions.append(("A4_no_admissible_twist_at_n_2_3_6", ok,
                       f"n=2,3,6 all admit none; n=6 content sums {cs6} miss "
                       f"the required {{-1,-2}}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. so both targets are out of reach at their own n ────────────
    print("\n  5. so both targets are unreachable AT THEIR OWN STRAND COUNT")
    third = Fraction(1, 3)
    at12 = third in per[12]
    print(f"     the two-nucleon sector is n=6, which is where qou-v3u2 proved")
    print(f"     the impossibility lives — and it admits NO twist. The mechanism")
    print(f"     cannot repair it.")
    print(f"     the t=1/3 QCD hit is at n=12 ({at12}), but two quarks are n=2,")
    print(f"     and n=2 offers only the excluded boundary. A colour observable")
    print(f"     for 3(x)3 cannot be evaluated at 4He's strand count.")
    print(f"     THAT HIT IS WITHDRAWN AS EVIDENCE.")
    ok = at12 and third not in per[2] and third not in per[3]
    assertions.append(("A5_both_targets_unreachable_at_their_own_n", ok,
                       "n=6 admits none so the nuclear sector is unrepairable; "
                       "t=1/3 exists only at n=12 while two quarks are n=2"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. what survives ──────────────────────────────────────────────
    print("\n  6. what survives of qou-bq9l")
    print(f"     STANDS: c_n is genuinely an n-th root of the full twist; its")
    print(f"       block magnitude is exactly q^(2c(lambda)/n); fractional")
    print(f"       values do occur, from n = 5; and the per-n availability table")
    print(f"       is a real, sparse, closed-form falsifiable structure.")
    print(f"     WITHDRAWN: the cumulative enumeration as a predictive claim,")
    print(f"       and the t = 1/3 coincidence as evidence for anything.")
    print(f"     NET: the missing ingredient was correctly identified, and the")
    print(f"       substrate does not supply it where it is needed.")
    ok = True
    assertions.append(("A6_scope_of_the_correction_is_stated", ok,
                       "mechanism stands; cumulative claim and 1/3 hit "
                       "withdrawn"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  This probe tests a claim of mine and it fails it, twice.")
    print("  The cumulative achievable set is dense — 96 % of the")
    print("  denominator-<=12 rationals by n <= 24 — so 'the substrate only")
    print("  produces rational ratios' has no discriminating power, and all")
    print("  eight group-theoretic targets trivially hit it.")
    print("  But cumulative was the wrong object: a physical system has a fixed")
    print("  strand count, and per n the sets are small. The decisive fact is")
    print("  that n = 2, n = 3 and n = 6 admit NO admissible fractional twist at")
    print("  all — at n=6 the content sums are {-15,-9,-5,-3,0,...} and the")
    print("  window needs {-1,-2}. The two-nucleon sector, where the whole")
    print("  obstruction lives, cannot be repaired by this mechanism; and the")
    print("  t = 1/3 QCD hit sits at n = 12 while two quarks are n = 2, so it is")
    print("  withdrawn as evidence.")
    print("  The mechanism from qou-bq9l stands. The use I put it to does not.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "Tests and largely retracts qou-bq9l's use of the fractional-twist "
            "mechanism. TWO CORRECTIONS. First, the cumulative achievable set is "
            "dense: the union of t over n <= 24 covers 43 of the 45 rationals "
            "with denominator <= 12 (96%, only 4/9 and 7/8 missing), so a "
            "'substrate only produces rational ratios' prediction has no "
            "discriminating power, and all eight exact group-theoretic targets "
            "tested (QCD 3bar/6 = 2, QCD singlet/octet = 8, piN 9 and 9/2, "
            "quark-model 3/2 and 5/3, 4, SU(6) 25/9) trivially hit it. Second "
            "and decisive, cumulative is the wrong object: a physical system has "
            "a FIXED strand count — two quarks n=2, a nucleon n=3, two nucleons "
            "n=6, 4He n=12 — and per n the admissible sets are small (n=9: 3 "
            "values; n=12: 3; n=15: 6; n=18: 7). At n=2, n=3 and n=6 there is NO "
            "admissible fractional twist at all: t in (0,1) needs c(lambda) "
            "strictly between -n/2 and 0, and at n=6 the achievable content sums "
            "are {-15,-9,-5,-3,0,3,5,9,15} while the window needs {-1,-2}; at "
            "n=2 the only candidate gives t = 1 exactly, the excluded boundary. "
            "CONSEQUENCES: the two-nucleon sector, which is n=6 and is where "
            "qou-v3u2 proved the impossibility lives, cannot be repaired by this "
            "mechanism; and the t = 1/3 QCD hit is realised at n=12 while two "
            "quarks are n=2, so it is withdrawn as evidence. What stands from "
            "qou-bq9l is the mechanism itself — c_n^n = Delta^2, block magnitude "
            "exactly q^(2c(lambda)/n), fractional values from n=5, and a sparse "
            "closed-form per-n availability table.")
        wb.add_data("cumulative_coverage",
                    {str(N): {"distinct_t": cov[N][0],
                              "covered_of_45": cov[N][1],
                              "pct": f"{100 * cov[N][1] / len(allr):.1f}"}
                     for N in cov})
        wb.add_data("cumulative_missing",
                    [str(x) for x in missing])
        wb.add_data("targets_all_hit_cumulatively",
                    {k: {"R": str(R), "t": str((R - 1) / (R + 1)),
                         "in_cumulative_set": (R - 1) / (R + 1) in seen}
                     for k, R in TARGETS.items()})
        wb.add_data("per_n_admissible",
                    {str(n): [str(t) for t in per[n]] for n in sorted(per)})
        wb.add_data("content_sums",
                    {"n=2": cs2, "n=3": cs3, "n=6": cs6,
                     "n6_window_requires": [-1, -2],
                     "n6_window_satisfied": False})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THIS PROBE RETRACTS PART OF qou-bq9l, WHICH IS MINE. Its mechanism "
            "(c_n^n = Delta^2, magnitude q^(2c/n), fractionality from n=5) is "
            "re-verified and stands. Its cumulative enumeration as a predictive "
            "claim, and its t = 1/3 coincidence as evidence, do not. Anyone "
            "quoting that probe should quote this one alongside it.")
        wb.add_caveat(
            "THE PER-n ANALYSIS ASSUMES A SYSTEM'S TWIST MUST COME FROM ITS OWN "
            "STRAND COUNT. That is the natural reading — the Coxeter element of "
            "B_n is defined on n strands — but a construction could in principle "
            "embed a subsystem in a larger braid and inherit a twist from there. "
            "Nothing here rules that out; it would need the embedding exhibited, "
            "and the resulting object would no longer be the n-strand system's "
            "own Coxeter element.")
        wb.add_caveat(
            "The eight group-theoretic ratios are used ONLY to demonstrate that "
            "the cumulative test has no power. They are not claimed as "
            "predictions, matches, or targets the substrate should meet, and no "
            "per-n check against them is offered — at the strand counts where "
            "they would be posed (n=2, n=3) there is nothing to check against.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
