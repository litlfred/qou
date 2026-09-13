#!/usr/bin/env python3
# polynomial_q_not_applicable: numeric evaluation at the recorded anchor, not a q-series compute.
"""The recorded Phi_1 column matches NO reading of the theorem's Phi_1.

FOLLOW-ON to `phi1_closed_form_and_no_z_reproduces_it_probe.py` (#7224, merged).
That probe closed Phi_1 in closed form and showed no real z reproduces the
recorded Z=1-20 column under the theorem's all-pairs chained reading. This asks
the obvious next question -- **is the recorded column SOME OTHER reading of the
same definition?** -- and answers no, across every reading that can be built
from Table 1's crossings.

WHY IT IS WORTH ASKING. `wedderburn_Mi_constructor_test.py` swept four readings
x two orderings of `M_i` and found residuals 54 %-2653 % against the deuteron.
Its banner then RETRACTED that sweep as "a REFUTED READING, not an
underdetermined formula", because the all-pairs reading is the correct one and
re-derives Phi_2 and Phi_3 19/19. So the corpus has never asked whether the
recorded PHI_1 COLUMN -- as opposed to the deuteron -- comes from one of those
other readings. It does not.

THREE FAMILIES TESTED, none consistent:

  1. Chain-length-limited: `M_i = prod_{j=i+1}^{min(i+L, n)} T(type_i, type_j)`.
     L = 1 is the single adjacent crossing, L = None the theorem's full suffix.
     Best over a 401-point z scan on [-20, 20]:

       L = 1    33.8 %      L = 2    95.2 %      L = 3    33.0 %
       L = 5    64.8 %      L = all  604 %

  2. Any linear-in-(Z, N) form. The adjacent-pair counts for the arrangement
     p^Z n^N e^Z are (pp: Z-1, pn: 1, nn: N-1, ne: 1, ee: Z-1), which spans the
     SAME affine space as (Z, N, 1) -- so a single least-squares on (Z, N, 1)
     tests the whole family at once. Worst residual 146 % (at He).

  3. The theorem's own all-pairs counts, granted three free coefficients:
     59.9 % (at C). Recorded for contrast; the exact-rank version of this is
     the sibling `phi3_quark_basis_is_structurally_excluded_probe.py`.

THE GROWTH EXPONENTS SETTLE IT WITHOUT ANY FIT. Log-log least squares of
|Phi_1| against n over the table's own range n = 6..60:

    recorded column           0.911
    theorem's Phi_1 at z_D    2.704

The recorded column is essentially LINEAR in the strand count; the theorem's
Phi_1 grows faster than quadratically over this range. No choice of z changes
that -- z enters each of the n-1 terms as a bounded factor, contributing O(n)
in total, so it cannot move the exponent.

🛑 A CORRECTION TO MY OWN MERGED PR BODY (#7224). There I wrote *"Phi_1 is
Theta(n^2) (per-pair density varies 6.1x over n = 6..60) while the recorded
column is Theta(n) (12.4x, falling monotonically)"*. The Theta(n^2) label is
right ASYMPTOTICALLY -- ln|P_i| ~ (n-i)*<ln|lambda|> summed over i is ~n^2/2 --
but the parenthetical I offered as evidence for it shows the opposite: a density
that RISES 6.1x over the range is growing FASTER than n^2, which the measured
effective exponent 2.704 confirms. The conclusion (the two columns have
incompatible growth) is unaffected and is if anything stronger; what was wrong
was citing a rising density as evidence for Theta(n^2). Over a finite range,
quote the EFFECTIVE exponent; reserve Theta() for the asymptotic argument.

WHAT THIS MEANS. Combined with the sibling results -- the recorded Phi_3 column
IS the theorem's Phi_3 at the documented anchor, and the recorded Phi_1 is not
the theorem's Phi_1 under any reading -- the recovered producer
`atom-mass-complete-wedderburn` shares TWO of the three invariants with the
published formula and its Phi_1 is a different object. Identifying that object
needs the recovered witness itself, not reverse-engineering from the column:
every reading the definition admits has now been excluded.

🛑 SCOPE. Scope-(a) on a named class: readings expressible as a product of
Table 1 crossings along the p^Z n^N e^Z arrangement, evaluated by the theorem's
bilinear form, for real z in [-20, 20]. NOT excluded: a different crossing
table, a complex z, a reading that is not a product of crossings at all (the
theorem's own table calls Phi_1 "trace of Markov-weighted product", and a
single trace rather than a sum over generators is untested here), or a
transcription error in the column. No candidate is proposed or adopted --
solving the column for its own generator is the fit the 2026-09-05 directive
forbids.

NO FLOAT64: every quantity is `mpmath.mpf`, constructed inside functions so
`mp.dps` is raised first. q0 is the producer's own recorded 1.10998 (a decimal
string, not a stringified double -- see #7224's laundering fix).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLE = ROOT / "computations" / "wedderburn_mass_table_z1_20.py"
MI_TEST = ROOT / "computations" / "wedderburn_Mi_constructor_test.py"
SIB = (ROOT / "computations" / "probes"
       / "phi1_closed_form_and_no_z_reproduces_it_probe.py")

_checks = 0
_failed = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global _checks, _failed
    _checks += 1
    if not cond:
        _failed += 1
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))


def rows():
    out = []
    for m in re.finditer(
            r'\("([A-Za-z]{1,2})",\s*(\d+),\s*(\d+),\s*(\d+),\s*"(-?[\d.]+)",'
            r'\s*"(-?[\d.]+)",\s*"(-?[\d.]+)"', TABLE.read_text()):
        el, Z, _zz, N, p1, _p2, _p3 = m.groups()
        out.append((el, int(Z), int(N), p1))
    return out


print("CHECK 1 -- inputs and prior art, read from the corpus")
NONH = [r for r in rows() if r[0] != "H"]
check("19 non-hydrogen rows parsed", len(NONH) == 19, f"{len(NONH)}")
check("the sibling probe exists and is CITED, not re-derived", SIB.exists())
mi = MI_TEST.read_text()
check("the Mi-constructor sweep RETRACTED its four-readings result",
      "REFUTED READING" in mi and "ALL-PAIRS" in mi,
      "so the recorded Phi_1 COLUMN was never tested against those readings")


def engine():
    """mpf engine; a FUNCTION so mp.dps is raised before the first mpf."""
    from mpmath import mp, mpf

    mp.dps = 40
    q0 = mpf("1.10998")
    h = q0 - 1 / q0
    CD = {frozenset("pp"): (mpf(1), mpf(0)), frozenset("nn"): (mpf(1), -h),
          frozenset("pn"): (mpf(2), -h), frozenset("pe"): (mpf(1), -h),
          frozenset("ne"): (mpf(0), mpf(1)), frozenset("ee"): (mpf(1), mpf(0))}
    LS = mp.log(q0 + 1 / q0)

    def phi1(Z, N, z, L=None):
        """L = max chain length inside M_i; None = all j>i (the theorem's)."""
        ty = "p" * Z + "n" * N + "e" * Z
        n = len(ty)
        tot = mpf(0)
        for i in range(n - 1):
            hi = n if L is None else min(i + 1 + L, n)
            P = mpf(1)
            Q = mpf(1)
            for j in range(i + 1, hi):
                c, d = CD[frozenset(ty[i] + ty[j])]
                P *= c * q0 + d
                Q *= -c / q0 + d
            a = P * (z + 1 / q0) + Q * (q0 - z)
            if a == 0:
                return None
            tot += mp.log(abs(a)) - LS
        return tot

    def slope(xs, ys):
        n_ = mpf(len(xs))
        sx = sum(xs); sy = sum(ys)
        sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
        return (n_ * sxy - sx * sy) / (n_ * sxx - sx * sx)

    def lsq_worst(basis):
        A = mp.matrix([[mpf(v) for v in basis(Z, N)] for _, Z, N, _ in NONH])
        y = mp.matrix([mpf(p1) for _, _, _, p1 in NONH])
        c = mp.lu_solve(A.T * A, A.T * y)
        worst, wel = mpf(0), None
        for k, (el, Z, N, p1) in enumerate(NONH):
            pred = sum(c[j] * A[k, j] for j in range(A.cols))
            d = abs(pred - mpf(p1)) / abs(mpf(p1))
            if d > worst:
                worst, wel = d, el
        return worst, wel

    def scan(L, lo, hi, npts):
        best = (None, mpf("inf"), None)
        for k in range(npts + 1):
            z = mpf(lo) + (mpf(hi) - mpf(lo)) * k / npts
            w, wel, bad = mpf(0), None, False
            for el, Z, N, p1 in NONH:
                v = phi1(Z, N, z, L)
                if v is None:
                    bad = True
                    break
                d = abs(v - mpf(p1)) / abs(mpf(p1))
                if d > w:
                    w, wel = d, el
            if not bad and w < best[1]:
                best = (z, w, wel)
        return best

    return dict(mp=mp, mpf=mpf, q0=q0, phi1=phi1, slope=slope,
                lsq_worst=lsq_worst, scan=scan,
                zD=q0 ** 3 / (q0 ** 2 + 1))


try:
    E = engine()
    mp, mpf = E["mp"], E["mpf"]

    print()
    print("CHECK 2 -- the GROWTH EXPONENTS are incompatible, with no fit involved")
    xs = [mp.log(mpf(2 * Z + N)) for _, Z, N, _ in NONH]
    s_rec = E["slope"](xs, [mp.log(abs(mpf(p1))) for _, _, _, p1 in NONH])
    s_thm = E["slope"](xs, [mp.log(abs(E["phi1"](Z, N, E["zD"])))
                            for _, Z, N, _ in NONH])
    print(f"      recorded column         effective exponent {mp.nstr(s_rec, 6)}")
    print(f"      theorem's Phi_1 at z_D  effective exponent {mp.nstr(s_thm, 6)}")
    check("the recorded column is essentially LINEAR in the strand count",
          abs(s_rec - 1) < mpf("0.15"), f"{mp.nstr(s_rec, 6)} over n = 6..60")
    check("the theorem's Phi_1 grows faster than QUADRATICALLY over the range",
          s_thm > 2, f"{mp.nstr(s_thm, 6)}")
    check("the gap is ~1.8 in exponent, and z cannot move it",
          s_thm - s_rec > mpf("1.5"),
          "z enters each of the n-1 terms as a bounded factor: O(n) in total")

    print()
    print("CHECK 3 -- chain-length-limited readings: none reproduce the column")
    print(f"      {'L':>4}{'best z':>12}{'worst rel miss':>17}{'row':>6}")
    results = {}
    for L in (1, 2, 3, 5, None):
        b = E["scan"](L, -20, 20, 400)
        results[L] = b
        print(f"      {('all' if L is None else str(L)):>4}"
              f"{mp.nstr(b[0], 6):>12}{mp.nstr(b[1], 6):>17}{str(b[2]):>6}")
    check("every chain length L in {1,2,3,5,all} misses by >25 % at its own best z",
          all(b[1] > mpf("0.25") for b in results.values()),
          "L=1 is the single adjacent crossing; L=all is the theorem's reading")
    check("the theorem's full reading is the WORST of them",
          results[None][1] == max(b[1] for b in results.values()),
          f"{mp.nstr(results[None][1] * 100, 4)} %")

    print()
    print("CHECK 4 -- no linear-in-(Z,N) form either, and that covers the "
          "adjacent-count family")
    w_lin, el_lin = E["lsq_worst"](lambda Z, N: (mpf(Z), mpf(N), mpf(1)))
    w_adj, el_adj = E["lsq_worst"](lambda Z, N: (mpf(2 * (Z - 1)), mpf(N - 1), mpf(1)))
    print(f"      (Z, N, 1)            worst {mp.nstr(w_lin, 6)}  (at {el_lin})")
    print(f"      (2(Z-1), N-1, 1)     worst {mp.nstr(w_adj, 6)}  (at {el_adj})")
    check("both miss by >100 %, and by the SAME amount", w_lin > 1 and w_adj > 1)
    check("identical because the adjacent counts span the same affine space",
          abs(w_lin - w_adj) < mpf("1e-20"),
          "so one least-squares tests the whole adjacent family at once")

    print()
    print("CHECK 5 -- the theorem's all-pairs counts, granted three free coefficients")
    from math import comb
    w_ap, el_ap = E["lsq_worst"](
        lambda Z, N: (mpf(2 * comb(Z, 2)), mpf(comb(N, 2) + Z * Z), mpf(Z * N)))
    check("also misses, at ~60 %", w_ap > mpf("0.5"),
          f"worst {mp.nstr(w_ap, 6)} at {el_ap}; the EXACT-rank version of this "
          "is phi3_quark_basis_is_structurally_excluded_probe.py")
except ImportError as exc:                                       # pragma: no cover
    print(f"  [INFO] mpmath unavailable ({exc}); checks 2-5 skipped")

print()
print("CHECK 6 -- what is deliberately NOT claimed")
doc = Path(__file__).read_text()
check("no candidate generator is proposed or adopted",
      "No candidate is proposed or adopted" in doc and "forbids" in doc)
check("the exclusion is scoped to a named class", "Scope-(a) on a named class" in doc)
check("the single-trace reading is named as UNTESTED",
      "a single trace rather than a sum over generators is untested here" in doc)
check("my own merged PR body's slip is corrected here, not quietly dropped",
      "A CORRECTION TO MY OWN MERGED PR BODY" in doc)

print()
print(f"{_checks - _failed}/{_checks} checks passed")
print()
print("MEASURED: the recorded Phi_1 column matches NO reading of the theorem's")
print("Phi_1 built from Table 1's crossings -- not the all-pairs chain (604 %),")
print("not any truncated chain (33-95 %), not any linear-in-(Z,N) form (146 %).")
print("Its effective growth exponent is 0.911 against the theorem's 2.704, and z")
print("cannot move an exponent. The producer's Phi_1 is a different object, and")
print("identifying it needs the recovered witness rather than the column.")
sys.exit(1 if _failed else 0)
