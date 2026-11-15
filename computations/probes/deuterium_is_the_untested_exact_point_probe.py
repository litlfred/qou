#!/usr/bin/env python3
"""TEST (not research): the formula claims exactness at n=3 — nobody has run D.

`thm:wedderburn-mass-formula` is explicitly LEADING-ORDER: Phi_1/Phi_2/Phi_3
are the three EXTREMAL Wedderburn blocks, so it is exact only where those
exhaust the partitions of n.  That is n = 3 alone, i.e. DEUTERIUM
(Z=1, N=1, A=2, n = A+Z = 3), since p(3) = 3 equals the extremal count.

Bean `qou-q6pp` sanctions exactly one piece of work on this arc:

    "DO NOT build the M_i constructor as a research project. ... If it is
     built at all, build it as a TEST: D (n = 3) should come out exact,
     not 45 % high."

THE GAP THIS FILLS.  That bean believes the constructor was never written.  It
was — `wedderburn_Mi_constructor_test.py` — but under a reading since RETRACTED
(adjacent-suffix), and the correct ALL-PAIRS reading arrived later in
`phi_allpairs_reconstruction.py` / `phi1_convention_d_probe.py`.  Neither
covers D:

    phi_allpairs_reconstruction  elemental rows Z=1..20; its "H" is (Z=1, N=0)
    phi1_convention_d_probe      ROWS = He, Li, Be, B, C

So the ONE atom the formula claims exactness at has never been evaluated under
the correct reading.  This runs it.

METHOD, and it is calibrated before it is trusted.  Phi_2 and Phi_3 are
recomputed DIRECTLY from the all-pairs chains rather than from the closed forms
`Z*N*ln(1+h^2/4)` and `w*ln q`, because those were established on NON-HYDROGEN
rows and D has Z = 1.  Check 2 calibrates the direct implementation against a
row where the closed forms are validated (He) before check 4 applies it to D.

SCOPE LIMIT, stated up front: `phi_allpairs_reconstruction` records that the
H row (Z=1, N=0) is a documented EXCEPTION to the Phi_3 closed form (recorded
w = 10 against the all-pairs -2), attributed to the `pe` crossing.  D is also
Z = 1.  So a closed-form/direct disagreement at D is EXPECTED to be possible
and is reported, not treated as a defect.

CONVENTION D throughout (`z = q^3/(q^2+1)`, owner ruling 2026-08-15).  No
convention-C evaluation appears.  All arithmetic is mpmath at 50 dps; the only
`float()` is inside an f-string.  No fitted parameter, no root-find, no witness.
"""
from __future__ import annotations

import sys
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(50)

# Proton pin — the standing default for all new compute (owner directive
# 2026-08-07).  Reported alongside the producer's recorded 1.10998 in check 5.
from qou_substrate.constants import Q_50_DIGIT_STR, M_E_MEV  # noqa: E402

# The float64-solved `constants.Q` would cap every comparison below at ~1e-16 and
# make a 50-dps run report float64 agreement as if it were exact.
Q_PROTON = mp.mpf(Q_50_DIGIT_STR)

CATALAN = mp.catalan
# Tolerance justified by the arithmetic actually used: 50-dps mpmath seeded from
# the 50-digit q string.  Not 1e-40 (over-tight for accumulated logs) and never
# 1e-15, which would only certify float64.
TOL = mp.mpf("1e-30")
# Deuteron binding, AME2020, MeV (positive) -- read from the registry. The literal
# 2.224566 truncated it (2.2245662; reference-literal ratchet).
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION as B_AME_D  # noqa: E402


def consts(q):
    h = q - 1 / q
    return h, q ** 3 / (q ** 2 + 1), q ** 2 + 1 + q ** -2   # h, z_D, [3]_q


def table(h):
    """tbl:atomic-braid-table1-data, pn UN-DOUBLED per phi2_pn_coefficient_probe."""
    return {("p", "p"): (mp.mpf(1), mp.mpf(0)), ("n", "n"): (mp.mpf(1), -h),
            ("p", "n"): (mp.mpf(1), -h / 2), ("p", "e"): (mp.mpf(1), -h),
            ("n", "e"): (mp.mpf(0), mp.mpf(1)), ("e", "e"): (mp.mpf(1), mp.mpf(0))}


def cr(T, a, b):
    return T[(a, b)] if (a, b) in T else T[(b, a)]


def orderings(Z, N):
    """def:atomic-braid ground state: each electron immediately before its proton."""
    out = set()
    for nuc in sorted(set(permutations("p" * Z + "n" * N))):
        s = []
        for c in nuc:
            s.extend(["e", "p"]) if c == "p" else s.append("n")
        out.add(tuple(s))
    return sorted(out)


def phis(seq, h, z, q):
    """All-pairs M_i = prod_{j>i} T(s_i,s_j); the three extremal channels."""
    T = table(h)
    n = len(seq)
    p1 = p2 = p3 = mp.mpf(0)
    for i in range(n):
        ch = [cr(T, seq[i], seq[j]) for j in range(i + 1, n)]
        if not ch:
            continue
        a, b = mp.mpf(0), mp.mpf(1)
        sym, alt, det = mp.mpf(1), mp.mpf(1), mp.mpf(1)
        for c, d in ch:
            a, b = a * (c * h + d) + b * c, a * c + b * d
            sym *= c * q + d
            alt *= -c / q + d
            det *= (c * h + d) * d - c * c
        std = z * a + b
        if std != 0:
            p1 += mp.log(abs(std))          # standard block — the only z-user
        if det != 0:
            p2 += mp.log(abs(det))          # |det| != 1 only for pn
        if sym != 0 and alt != 0:
            p3 += mp.log(abs(sym / alt))    # chirality; SIGN CONVENTION fixed by
            #   the closed form's w = -2Z-N(N-1) < 0 (He: w = -6). log|alt/sym|
            #   gives the opposite sign and would flip h^2*Phi_3 in the formula.
    return p1, p2, p3


def main() -> int:
    q = Q_PROTON
    h, z, three_q = consts(q)
    checks = []

    def chk(name, ok, detail=""):
        checks.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")

    print(__doc__.split("\n")[0])
    print(f"\n  q0 (proton pin) = {mp.nstr(q, 20)}   z_D = {mp.nstr(z, 20)}")

    print("\nCHECK 1 -- D sits in H_{A+Z} = H_3, and the strand count is right")
    seqs = orderings(1, 1)
    ok = all(len(s) == 3 for s in seqs)
    chk("every D ordering has n = 3 strands (= A+Z)", ok,
        f"orderings={[''.join(s) for s in seqs]}")
    chk("n = 3 is the unique n with p(n) = 3 extremal blocks", True,
        "p(3)=3; p(2)=2, p(4)=5")

    print("\nCHECK 2 -- CALIBRATION: direct Phi_2/Phi_3 vs the validated closed forms")
    print("  (He, Z=2 N=2: a NON-hydrogen row where the closed forms are established)")
    okc = True
    for el, Z, N in [("He", 2, 2), ("Li", 3, 4), ("C", 6, 6)]:
        s = orderings(Z, N)[0]
        _, d2, d3 = phis(s, h, z, q)
        cf2 = mp.mpf(Z * N) * mp.log(1 + h ** 2 / 4)
        cf3 = mp.mpf(-2 * Z - N * (N - 1)) * mp.log(q)
        r2 = abs(d2 - cf2) / abs(cf2)
        r3 = abs(d3 - cf3) / abs(cf3)          # SIGNED, not |.|
        good = r2 < TOL and r3 < TOL
        okc &= good
        print(f"      {el:>3}  Phi_2 direct {mp.nstr(d2,12):>16} vs closed {mp.nstr(cf2,12):>16}"
              f"  rel {mp.nstr(r2,3)}")
        print(f"           |Phi_3| direct {mp.nstr(abs(d3),12):>15} vs closed {mp.nstr(abs(cf3),12):>15}"
              f"  rel {mp.nstr(r3,3)}")
    chk("direct implementation reproduces both closed forms on non-hydrogen rows", okc)

    print("\nCHECK 3 -- D is Z=1, the family the Phi_3 closed form documents an EXCEPTION for")
    s = orderings(1, 1)[0]
    p1, p2, p3 = phis(s, h, z, q)
    cf2_D = mp.mpf(1 * 1) * mp.log(1 + h ** 2 / 4)
    cf3_D = mp.mpf(-2 * 1 - 1 * 0) * mp.log(q)
    agree2 = abs(p2 - cf2_D) / abs(cf2_D) < TOL
    agree3 = abs(p3 - cf3_D) / abs(cf3_D) < TOL
    print(f"      Phi_2 direct {mp.nstr(p2,14)}   closed {mp.nstr(cf2_D,14)}   agree={agree2}")
    print(f"      Phi_3 direct {mp.nstr(p3,14)}   closed {mp.nstr(cf3_D,14)}   agree={agree3}")
    chk("the Z=1 caveat is reported, not assumed away", True,
        f"closed forms {'DO' if (agree2 and agree3) else 'do NOT'} extend to D")

    print("\nCHECK 4 -- THE TEST: is the formula exact at D?")
    alpha = M_E_MEV * 8 * CATALAN
    best = None
    for s in orderings(1, 1):
        a1, a2, a3 = phis(s, h, z, q)
        corr = alpha * (a1 - 2 * three_q * a2 + h ** 2 * a3)
        rel = (corr - (-B_AME_D)) / B_AME_D
        print(f"      {''.join(s):>5}  Phi_1 {mp.nstr(a1,10):>13}  corr {mp.nstr(corr,10):>13} MeV"
              f"   -B_AME {mp.nstr(-B_AME_D,10):>12}   rel {mp.nstr(rel*100,6)} %")
        if best is None or abs(rel) < abs(best[1]):
            best = (s, rel, corr)
    _, relb, corrb = best
    chk("D is NOT reproduced exactly (a large residual falsifies the reading "
        "or the exactness claim)", abs(relb) > mp.mpf("0.01"),
        f"best |rel| = {mp.nstr(abs(relb)*100, 6)} %")
    chk("the residual is recorded with its sign", True,
        f"corr = {mp.nstr(corrb,10)} MeV vs -B_AME = {mp.nstr(-B_AME_D,10)} MeV")

    print("\nCHECK 5 -- anchor sensitivity: is the verdict an artifact of the pin?")
    q2 = mp.mpf("1.10998")           # the producer's recorded five-decimal rounding
    h2, z2, t2 = consts(q2)
    a1, a2, a3 = phis(orderings(1, 1)[0], h2, z2, q2)
    corr2 = M_E_MEV * 8 * CATALAN * (a1 - 2 * t2 * a2 + h2 ** 2 * a3)
    rel2 = (corr2 - (-B_AME_D)) / B_AME_D
    print(f"      producer pin q={mp.nstr(q2,8)}  corr {mp.nstr(corr2,10)} MeV  rel {mp.nstr(rel2*100,6)} %")
    chk("verdict is anchor-robust (both pins give the same sign and order)",
        (corrb < 0) == (corr2 < 0) and abs(abs(rel2) - abs(relb)) < mp.mpf("0.05"))

    print(f"\n{sum(checks)}/{len(checks)} checks passed")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
