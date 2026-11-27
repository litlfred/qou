#!/usr/bin/env python3
"""The braid defect of the pre-fix YSN family is INVISIBLE to any character.

Companion to
`docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md`
(bean `qou-4m9u`).  That document reports a braid defect of 0.7315 in the
matrices `_build_ysn_matrices` used to produce.  This probe establishes why
the corpus never noticed: every consumer on the binding path
(`unified_iterative_correction`, `atom_character_raw`) takes a **trace**, and

    Tr(ABA) - Tr(BAB) = Tr(B) - Tr(A) = 0

follows from the QUADRATIC relation alone, for any dimension.  Derivation,
using A^2 = hA + I and B^2 = hB + I:

    Tr(ABA) = Tr(A^2 B) = h*Tr(AB) + Tr(B)
    Tr(BAB) = Tr(B^2 A) = h*Tr(AB) + Tr(A)

and both generators of a seminormal family have trace h in the 2-dim irrep.
So a character-level check CANNOT fire on this defect -- the audit that found
it had to compare matrices.

Everything here is exact-arithmetic mpmath at 50 dps.  The production builder
is float64 (`math.sqrt`, `1.0` literals); that is a separate defect, tracked
as `qou-sv7h` step 3, and is deliberately NOT reproduced here -- carrying the
two families at MPFR is what lets this probe distinguish a real cancellation
from float64 rounding, which the production path cannot.

Exit 0 when every assertion holds.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

from mpmath import mp                                    # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP                   # noqa: E402

mp.dps = 50

Q = Q_MP
H = Q - 1 / Q                       # h = q - 1/q


def q_int(n):
    """[n]_q = (q^n - q^-n)/(q - q^-1), exact in mpmath."""
    return (Q ** n - Q ** (-n)) / (Q - 1 / Q)


def family(a):
    """The 2-dim irrep of H_3(q) with sigma_1 = diag(q, -1/q) and
    sigma_2 = [[a, b], [b, h-a]], b fixed by det = -1  =>  b^2 = a(h-a)+1.

    Both implementations agree on sigma_1 exactly; `a` is the single entry
    they disagree about.
    """
    b = mp.sqrt(a * (H - a) + 1)
    s1 = mp.matrix([[Q, 0], [0, -1 / Q]])
    s2 = mp.matrix([[a, b], [b, H - a]])
    return s1, s2


# The axial distance of the single off-diagonal pair of the 2-dim irrep of
# H_3(q).  It is NEGATIVE, and the sign is load-bearing: [-2]_q = -[2]_q, so
# the legacy formula lands on -h/[2]_q rather than +h/[2]_q.  A first version
# of this probe used rho = +2 and measured a family the code never built
# (a = +0.1039, matrix defect 1.0269 instead of the reported 0.7315).
RHO = -2

# What `_build_ysn_matrices` computed before the fix: h over a q-integer of
# the axial distance.  Kept inline, parameterised by RHO, rather than read
# from git, so this probe survives the merge that removes the line.
A_LEGACY = H / q_int(RHO)
# The fix: h / (1 - q^(-2 rho)).  Equal to the -1/(q(q^2+1)) of the audit's
# SETTLED section at this rho -- asserted below rather than assumed.
A_FIXED = H / (1 - Q ** (-2 * RHO))

I2 = mp.matrix([[1, 0], [0, 1]])


def norm(M):
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def report(tag, a):
    s1, s2 = family(a)
    quad = max(norm(s * s - H * s - I2) for s in (s1, s2))
    braid = norm(s1 * s2 * s1 - s2 * s1 * s2)
    tr_braid = abs(mp.fsum((s1 * s2 * s1)[i, i] for i in range(2))
                   - mp.fsum((s2 * s1 * s2)[i, i] for i in range(2)))
    print(f"  {tag:8s} a = {mp.nstr(a, 12):>16s}"
          f"   quadratic {mp.nstr(quad, 3):>10s}"
          f"   MATRIX braid {mp.nstr(braid, 5):>12s}"
          f"   TRACE braid {mp.nstr(tr_braid, 3):>10s}")
    return quad, braid, tr_braid


def main():
    print(f"q0 = {mp.nstr(Q, 20)}   h = {mp.nstr(H, 20)}   dps = {mp.dps}\n")

    q_fix, br_fix, tr_fix = report("fixed", A_FIXED)
    q_leg, br_leg, tr_leg = report("legacy", A_LEGACY)
    print()

    tol = mp.mpf(10) ** -45
    checks = [
        ("both families satisfy the quadratic relation",
         q_fix < tol and q_leg < tol),
        ("the fixed family satisfies the MATRIX braid relation",
         br_fix < tol),
        ("the legacy family does NOT -- defect is O(0.1), not noise",
         br_leg > mp.mpf("0.5")),
        ("the legacy TRACE braid defect vanishes anyway (the blindness)",
         tr_leg < tol),
        ("so does the fixed one -- the trace never discriminated",
         tr_fix < tol),
        ("h - a = z_D = q^3/(q^2+1) for the fixed family",
         abs((H - A_FIXED) - Q ** 3 / (Q ** 2 + 1)) < tol),
        ("the fixed a agrees with the audit's closed form -1/(q(q^2+1))",
         abs(A_FIXED - (-1 / (Q * (Q ** 2 + 1)))) < tol),
        ("the legacy a reproduces the value recorded in the audit",
         abs(A_LEGACY - mp.mpf("-0.1039637101")) < mp.mpf("1e-9")),
        ("the legacy MATRIX defect reproduces the recorded 0.7315",
         abs(br_leg - mp.mpf("0.7315")) < mp.mpf("1e-3")),
    ]
    ok = True
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok &= bool(passed)

    print(f"\n  legacy: matrix braid defect {mp.nstr(br_leg, 6)}"
          f"  vs trace braid defect {mp.nstr(tr_leg, 3)}")
    print("  A trace consumer cannot tell the two families apart.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
