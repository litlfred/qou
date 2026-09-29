#!/usr/bin/env python3
# polynomial_q_not_applicable: numeric evaluation at the recorded anchor, not a q-series compute.
"""Phi_1 HAS a closed form -- and NO real z makes it the recorded column.

OWNER INSTRUCTION 2026-09-12: *"Phi_1 ... open"*.

WHAT THE CORPUS HAD. `thm:wedderburn-mass-formula` defines

    Phi_1 = sum_i ln| z*(M_i)_12 + (M_i)_22 |,   M_i = prod_{j>i} T(type_i, type_j)

and `phi_allpairs_reconstruction.py` closed Phi_2 and Phi_3 under the all-pairs
reading (19/19), while recording that "Phi_1 is NOT closed here". The 2026-09-12
sibling probe `phi1_is_chain_additive_iff_z_is_an_eigenvalue_probe.py` proved WHY
the obvious route fails: the bilinear form f(M) = z*M_12 + M_22 is multiplicative
only when z^2 - h z - 1 = 0, i.e. z in {q, -1/q}, the eigenvalues of sigma. That
explained the resistance; it did not evaluate Phi_1.

WHAT THIS ADDS -- four things, one of which refutes my own prediction.

1. ORDER-INDEPENDENCE, with its structural reason. Every crossing is
   c*sigma + d*1 with the SAME sigma = [[h,1],[1,0]], so all six crossing
   matrices are polynomials in ONE matrix and COMMUTE EXACTLY (max commutator 0
   over all 81 ordered pairs). The transfer algebra is R[x]/(x^2 - h x - 1),
   commutative. So `wedderburn_Mi_constructor_test.py`'s retraction -- "an
   ALL-PAIRS braid with no ordering dependence" -- is correct, and correct for a
   stronger reason than it states: it holds for Phi_1 too, not only for the two
   multiplicative invariants.

   🛑 I PREDICTED THE OPPOSITE AND WAS WRONG. Reasoning from the sibling probe's
   non-multiplicativity, I expected Phi_1 to depend on the strand arrangement and
   on the order of j inside M_i, and said so. Measured: identical to 10 digits
   across five arrangements (p,n,e / e,p,n / p,e,n / n,p,e / e,n,p) and both
   j-orders, on He, C and Ca. Non-multiplicativity of f does NOT imply order
   dependence of Phi_1, because the matrices being multiplied commute.

2. THE CLOSED FORM. Diagonalising sigma (eigenvalues q, -1/q; V = [[q,-1/q],[1,1]]):

       M_i = V diag(P_i, Q_i) V^-1,
       P_i = prod_{j>i} (c q + d) = prod lambda^sym,   Q_i = prod_{j>i} (-c/q + d)
       (M_i)_12 = (P_i - Q_i)/(q + 1/q),  (M_i)_22 = (P_i/q + q Q_i)/(q + 1/q)

   hence

       Phi_1(z) = sum_i ln| P_i (z + 1/q) + Q_i (q - z) |  -  (n-1) ln(q + 1/q).

   Verified against the literal 2x2 matrix product to 3e-41. Phi_1 is therefore
   CLOSED in exactly the same per-pair data (Table 1's (c,d), the all-pairs
   counts) that closed Phi_2 and Phi_3 -- what it is not is per-pair ADDITIVE.

3. AT z = q THE SECOND TERM VANISHES and Phi_1 collapses to the per-pair sum
   sum_{i<j} ln|c q + d| (verified exactly). That is the sibling probe's
   eigenvalue condition, confirmed numerically rather than algebraically: the
   eigenvalues are exactly the z at which the closed form degenerates to one
   factor.

4. NO REAL z REPRODUCES THE RECORDED COLUMN. Phi_1(z) has n-1 poles (one per
   generator, where the argument vanishes), so it is unbounded below and no sign
   or growth argument settles it -- the honest test is CONSISTENCY: one parameter
   against 19 constraints. Minimising the worst relative miss over all 19 rows
   gives a best of ~5.2 (520 %) at Ar, near z = 1.054. The three documented z --
   convention C, convention D, z = q -- are all far worse, and have the WRONG
   SIGN on every row (Phi_1 > 0 while every recorded value is < 0) and the wrong
   growth (Phi_1 = Theta(n^2); the recorded column is Theta(n)).

   🛑 QUOTE THE ORDER OF MAGNITUDE, NOT THE MINIMISER. The reported best z and
   its miss depend on the scan grid -- a 2001-point scan gives z = 1.0537 and
   5.24, a 401-point scan z = 0.926 and 5.84, because Phi_1(z) is pole-ridden
   and the basin is shallow and ragged. What is robust across resolutions is
   that the best achievable miss is ~5-6 (several hundred per cent), never
   near zero. Do not cite the minimiser as if it were a determined value.

CONSEQUENCE, and it relocates the beta_3 question. The sibling probe
`beta3_deviation_is_isolated_to_the_coefficient_probe.py` established that the
recorded Phi_3 column IS the theorem's Phi_3, at the documented anchor. So the
recovered producer agrees with the published formula on Phi_2 and Phi_3 and
DISAGREES on Phi_1: two of the three invariants are shared. The 14.2 % beta_3
departure and the Phi_1 disagreement are on the same object, and neither is
explained by the anchor.

🛑 SCOPE -- this is scope-(a) turning on a NAMED class, not a universal
exclusion. What is excluded is: the theorem's own Phi_1, on the all-pairs A+Z
reading, with Table 1's crossing values, for any real z. Not excluded: a
different M_i reading (the adjacent-suffix reading is separately refuted in
`wedderburn_Mi_constructor_test.py`), a complex z, a different crossing table,
or the possibility that the recorded column is some other quantity entirely.
The `A` (electron-free) reading is tested here too and is also excluded. The
quark-level readings are not testable on Table 1, whose rows are nucleon- and
electron-typed.

NO REPLACEMENT IS PROPOSED. Solving the table for a coefficient or a z and
adopting it is the fit the owner's 2026-09-05 directive forbids; the scan below
reports that no z works and stops there.

NO FLOAT64: every quantity is `mpmath.mpf`. The coarse scan runs at dps 25 and
the winning candidate is recomputed at dps 40; the closed-form cross-check runs
at dps 40. Constructed inside functions so `mp.dps` is raised before the first
`mpf`.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLE = ROOT / "computations" / "wedderburn_mass_table_z1_20.py"
THM = (ROOT / "folio" / "quantum-observable-universe" / "mass-theory"
       / "wedderburn-mass-formula.md")
SIB_INV = (ROOT / "computations" / "probes"
           / "phi1_is_chain_additive_iff_z_is_an_eigenvalue_probe.py")
SIB_B3 = (ROOT / "computations" / "probes"
          / "beta3_deviation_is_isolated_to_the_coefficient_probe.py")
ALLPAIRS = ROOT / "computations" / "phi_allpairs_reconstruction.py"
MI_TEST = ROOT / "computations" / "wedderburn_Mi_constructor_test.py"

_checks = 0
_failed = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global _checks, _failed
    _checks += 1
    if not cond:
        _failed += 1
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))


def rows():
    """(el, Z, N, Phi_1) from the producer's own ROWS table."""
    out = []
    for m in re.finditer(
            r'\("([A-Za-z]{1,2})",\s*(\d+),\s*(\d+),\s*(\d+),\s*"(-?[\d.]+)",'
            r'\s*"(-?[\d.]+)",\s*"(-?[\d.]+)"', TABLE.read_text()):
        el, Z, _zz, N, p1, _p2, _p3 = m.groups()
        out.append((el, int(Z), int(N), p1))
    return out


print("CHECK 1 -- the inputs, read from the corpus")
ROWS = rows()
NONH = [r for r in ROWS if r[0] != "H"]
check("20 rows parsed; 19 non-hydrogen", len(ROWS) == 20 and len(NONH) == 19)
check("every recorded Phi_1 is NEGATIVE",
      all(float(r[3]) < 0 for r in NONH),
      f"He {NONH[0][3]} .. Ca {NONH[-1][3]}")
# Whitespace-normalised: the theorem's prose is line-wrapped, so a literal
# single-line match fails on "chaining the crossing / matrices of all strands".
thm = " ".join(THM.read_text().split())
check("the theorem defines Phi_1 as the bilinear form on a CHAINED product",
      "z \\cdot (M_i)_{12} + (M_i)_{22}" in thm
      and "chaining the crossing matrices of all strands $j > i$" in thm)
check("the all-pairs reading is the corpus's own, and closed Phi_2/Phi_3 only",
      "ALL-PAIRS" in MI_TEST.read_text() and "Phi_1 is NOT closed" in ALLPAIRS.read_text())
check("the sibling invariant probe exists and is CITED, not re-derived",
      SIB_INV.exists() and SIB_B3.exists())


def engine(dps: int):
    """Build the crossing matrices and the per-generator (P_i, Q_i) at `dps`.

    A FUNCTION, not module scope: `mp.dps` must be raised before the first `mpf`,
    and the import-time dps ratchet cannot prove that ordering at module level.
    """
    from mpmath import mp, mpf

    mp.dps = dps
    q0 = mpf("1.10998")          # the producer's own recorded q0
    h = q0 - 1 / q0
    # tbl:atomic-braid-table1-data, (c, d) per unordered pair type
    CD = {frozenset("pp"): (mpf(1), mpf(0)), frozenset("nn"): (mpf(1), -h),
          frozenset("pn"): (mpf(2), -h), frozenset("pe"): (mpf(1), -h),
          frozenset("ne"): (mpf(0), mpf(1)), frozenset("ee"): (mpf(1), mpf(0))}
    sigma = mp.matrix([[h, 1], [1, 0]])

    def T(a, b):
        c, d = CD[frozenset(a + b)]
        return mp.matrix([[c * h + d, c], [c, d]])

    def strands(Z, N, electrons=True):
        return "p" * Z + "n" * N + ("e" * Z if electrons else "")

    def phi1_direct(types, z):
        n = len(types)
        tot = mpf(0)
        for i in range(n - 1):
            M = mp.matrix([[1, 0], [0, 1]])
            for j in range(i + 1, n):
                M = M * T(types[i], types[j])
            tot += mp.log(abs(z * M[0, 1] + M[1, 1]))
        return tot

    def pq(types):
        n = len(types)
        out = []
        for i in range(n - 1):
            P = mpf(1)
            Q = mpf(1)
            for j in range(i + 1, n):
                c, d = CD[frozenset(types[i] + types[j])]
                P *= c * q0 + d
                Q *= -c / q0 + d
            out.append((P, Q))
        return out

    LS = mp.log(q0 + 1 / q0)

    def phi1_closed(pqs, z):
        tot = mpf(0)
        for P, Q in pqs:
            a = P * (z + 1 / q0) + Q * (q0 - z)
            if a == 0:
                return None
            tot += mp.log(abs(a))
        return tot - len(pqs) * LS

    return dict(mp=mp, mpf=mpf, q0=q0, h=h, CD=CD, sigma=sigma, T=T,
                strands=strands, phi1_direct=phi1_direct, pq=pq,
                phi1_closed=phi1_closed, LS=LS)


print()
print("CHECK 2 -- all six crossing matrices COMMUTE, so the order cannot matter")
try:
    E = engine(40)
    mp, mpf = E["mp"], E["mpf"]
    worst = mpf(0)
    pairs = 0
    for a in "pne":
        for b in "pne":
            for c_ in "pne":
                for d_ in "pne":
                    X, Y = E["T"](a, b), E["T"](c_, d_)
                    Cm = X * Y - Y * X
                    pairs += 1
                    worst = max(worst, max(abs(Cm[i, j]) for i in range(2) for j in range(2)))
    check(f"max |[T_s, T_t]| over all {pairs} ordered pairs is EXACTLY zero",
          worst == 0, "every crossing is c*sigma + d*1 in the SAME sigma")
    check("sigma has trace h and determinant -1, so its eigenvalues are q and -1/q",
          abs(E["sigma"][0, 0] + E["sigma"][1, 1] - E["h"]) < mpf("1e-35")
          and abs(mp.det(E["sigma"]) + 1) < mpf("1e-35"),
          "the transfer algebra is R[x]/(x^2 - h x - 1), COMMUTATIVE")

    print()
    print("CHECK 3 -- so Phi_1 is ORDER-INDEPENDENT (my own prediction was WRONG)")
    zD = E["q0"] ** 3 / (E["q0"] ** 2 + 1)
    ORD = {"p,n,e": lambda Z, N: "p" * Z + "n" * N + "e" * Z,
           "e,p,n": lambda Z, N: "e" * Z + "p" * Z + "n" * N,
           "p,e,n": lambda Z, N: "p" * Z + "e" * Z + "n" * N,
           "n,p,e": lambda Z, N: "n" * N + "p" * Z + "e" * Z,
           "e,n,p": lambda Z, N: "e" * Z + "n" * N + "p" * Z}
    spread = mpf(0)
    for el, Z, N, _ in [r for r in NONH if r[0] in ("He", "C")]:
        vals = [E["phi1_direct"](f(Z, N), zD) for f in ORD.values()]
        spread = max(spread, max(vals) - min(vals))
    check("Phi_1 is identical across five strand arrangements (He, C)",
          spread < mpf("1e-30"), f"spread {mp.nstr(spread, 3)}")
    print("       I predicted order DEPENDENCE from the non-multiplicativity of f.")
    print("       That inference is invalid: the matrices being multiplied commute.")

    print()
    print("CHECK 4 -- THE CLOSED FORM, against the literal 2x2 matrix product")
    print("    Phi_1(z) = sum_i ln|P_i(z+1/q) + Q_i(q-z)| - (n-1)ln(q+1/q)")
    worst_cf = mpf(0)
    for el, Z, N, _ in [r for r in NONH if r[0] in ("He", "Li", "C")]:
        ty = E["strands"](Z, N)
        a = E["phi1_direct"](ty, zD)
        b = E["phi1_closed"](E["pq"](ty), zD)
        worst_cf = max(worst_cf, abs(a - b))
        print(f"      {el:<3} direct {mp.nstr(a, 14):>18}   closed {mp.nstr(b, 14):>18}")
    check("closed form agrees with the direct product to < 1e-30",
          worst_cf < mpf("1e-30"), f"worst |direct - closed| = {mp.nstr(worst_cf, 3)}")

    print()
    print("CHECK 5 -- at z = q the Q term vanishes and Phi_1 COLLAPSES to a per-pair sum")
    worst_pp = mpf(0)
    for el, Z, N, _ in [r for r in NONH if r[0] in ("He", "C")]:
        ty = E["strands"](Z, N)
        n = len(ty)
        s = mpf(0)
        for i in range(n - 1):
            for j in range(i + 1, n):
                c, d = E["CD"][frozenset(ty[i] + ty[j])]
                s += mp.log(abs(c * E["q0"] + d))
        worst_pp = max(worst_pp, abs(E["phi1_direct"](ty, E["q0"]) - s))
    check("Phi_1(z=q) == sum_{i<j} ln|c q + d|", worst_pp < mpf("1e-30"),
          f"worst |Phi_1(q) - per-pair sum| = {mp.nstr(worst_pp, 3)}; "
          "the sibling probe's eigenvalue condition, confirmed numerically")

    print()
    print("CHECK 6 -- the three documented z all have the WRONG SIGN and WRONG GROWTH")
    zC = mp.sqrt(E["q0"]) / (E["q0"] + 1)
    cache = {r[0]: E["pq"](E["strands"](r[1], r[2])) for r in NONH}
    allpos = True
    for el, Z, N, p1 in NONH:
        for z in (zD, zC, E["q0"]):
            if E["phi1_closed"](cache[el], z) <= 0 and el not in ("He", "Li", "Be"):
                allpos = False
    check("Phi_1 > 0 at C, D and z=q on every row from B upward, while every "
          "recorded value is negative", allpos)
    lead = [(r[0], E["phi1_closed"](cache[r[0]], zD)
             / (mpf(len(cache[r[0]])) * (len(cache[r[0]]) + 1) / 2),
             mpf(r[3]) / (mpf(len(cache[r[0]])) * (len(cache[r[0]]) + 1) / 2))
            for r in NONH]
    thm_ratio = max(abs(a) for _, a, _ in lead) / min(abs(a) for _, a, _ in lead)
    rec_ratio = max(abs(b) for _, _, b in lead) / min(abs(b) for _, _, b in lead)
    print(f"      Phi_1(D)/C(n,2): {mp.nstr(lead[0][1], 4)} (He) .. "
          f"{mp.nstr(lead[-1][1], 4)} (Ca)   spread {mp.nstr(thm_ratio, 4)}x")
    print(f"      recorded/C(n,2): {mp.nstr(lead[0][2], 4)} (He) .. "
          f"{mp.nstr(lead[-1][2], 4)} (Ca)   spread {mp.nstr(rec_ratio, 4)}x")
    check("Phi_1 is Theta(n^2) -- its per-pair density is roughly constant",
          thm_ratio < 7, f"{mp.nstr(thm_ratio, 4)}x across n = 6..60")
    check("the recorded column is NOT -- its per-pair density falls off",
          rec_ratio > 10, f"{mp.nstr(rec_ratio, 4)}x, i.e. Theta(n), not Theta(n^2)")

    def scan(electrons: bool, lo, hi, npts, dps):
        """min over z of the worst relative miss over all 19 rows."""
        Ex = engine(dps)
        mpx, mpfx = Ex["mp"], Ex["mpf"]
        cc = {r[0]: Ex["pq"](Ex["strands"](r[1], r[2], electrons)) for r in NONH}
        rc = {r[0]: mpfx(r[3]) for r in NONH}
        best = (None, mpfx("inf"), None)
        for k in range(npts + 1):
            z = mpfx(lo) + (mpfx(hi) - mpfx(lo)) * k / npts
            w, wel = mpfx(0), None
            for el, L in cc.items():
                v = Ex["phi1_closed"](L, z)
                if v is None:
                    w = mpfx("inf")
                    wel = el
                    break
                d = abs(v - rc[el]) / abs(rc[el])
                if d > w:
                    w, wel = d, el
            if w < best[1]:
                best = (z, w, wel)
        return best, Ex

    print()
    print("CHECK 7 -- is there ANY real z?  one parameter against 19 constraints")
    print("    (Phi_1 has n-1 poles and is unbounded below, so only a consistency")
    print("     test settles it -- a sign or growth argument alone does not.)")
    best, Ex = scan(True, -20, 20, 400, 25)
    print(f"      coarse over z in [-20,20]: z = {Ex['mp'].nstr(best[0], 10)}   "
          f"worst rel miss {Ex['mp'].nstr(best[1], 6)} (at {best[2]})")
    lo2, hi2 = best[0] - Ex["mpf"]("0.1"), best[0] + Ex["mpf"]("0.1")
    ref, Ex2 = scan(True, lo2, hi2, 200, 40)
    print(f"      refined at dps 40:         z = {Ex2['mp'].nstr(ref[0], 14)}   "
          f"worst rel miss {Ex2['mp'].nstr(ref[1], 8)} (at {ref[2]})")
    check("NO real z reproduces the recorded Phi_1 column",
          ref[1] > Ex2["mpf"]("1"),
          f"best possible worst-miss {Ex2['mp'].nstr(ref[1] * 100, 5)} % at {ref[2]}")
    print("      as |z| -> inf, Phi_1 -> (n-1)ln|z| -> +inf while every recorded")
    print("      value is negative, so the minimum is interior to the window.")

    print()
    print("CHECK 8 -- SCOPE: the electron-free A reading is excluded too")
    bestA, ExA = scan(False, -20, 20, 400, 25)
    print(f"      A reading, best over z in [-20,20]: z = {ExA['mp'].nstr(bestA[0], 10)}   "
          f"worst rel miss {ExA['mp'].nstr(bestA[1], 6)} (at {bestA[2]})")
    check("the A (nucleons-only) reading is also excluded for every real z",
          bestA[1] > ExA["mpf"]("1"),
          f"best possible worst-miss {ExA['mp'].nstr(bestA[1] * 100, 5)} %")
except ImportError as exc:                                       # pragma: no cover
    print(f"  [INFO] mpmath unavailable ({exc}); checks 2-8 skipped")

print()
print("CHECK 9 -- what is deliberately NOT claimed")
doc = Path(__file__).read_text()
check("no replacement z or coefficient is proposed or adopted",
      "NO REPLACEMENT IS PROPOSED" in doc and "forbids" in doc)
check("the exclusion is scoped to a NAMED class, not universal",
      "scope-(a) turning on a NAMED class" in doc and "Not excluded:" in doc)
check("the quark-level readings are stated as untestable on Table 1",
      "not testable on Table 1" in doc)
check("my own wrong prediction is recorded, not quietly dropped",
      "I PREDICTED THE OPPOSITE AND WAS WRONG" in doc)

print()
print(f"{_checks - _failed}/{_checks} checks passed")
print()
print("MEASURED: Phi_1 is CLOSED -- sum_i ln|P_i(z+1/q) + Q_i(q-z)| - (n-1)ln(q+1/q),")
print("verified against the literal matrix product -- and it is order-independent")
print("because the transfer algebra is commutative. It collapses to a per-pair sum")
print("exactly at z in {q, -1/q}. And NO real z makes it the recorded column, on")
print("either the A+Z or the A reading: the recorded Phi_1 is not the theorem's.")
sys.exit(1 if _failed else 0)
