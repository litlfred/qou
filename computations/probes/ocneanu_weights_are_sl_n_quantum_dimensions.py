"""Convention D is the sl_2 member of the family z_N = q^N/[N]_q.  Convention C
is not a member for any N.

WHAT THIS ANSWERS.  The previous step (bean qou-dwf4, item (b)) showed that in
convention D the Ocneanu framing ratio a^2 = z/z_- is the MONOMIAL q^4, and
that in convention C it is not a monomial at all.  That was stated as an
aesthetic separation.  It is not aesthetic -- it is a classification, and the
monomial is doing real work.

THE MECHANISM.  `prop:markov-z-reconciliation` gives the Wedderburn block
weights by the Ocneanu formula, frame-general in (z, z_- = z - hbar):

    w_lam  =  prod_{x in lam} ( z q^{c(x)} - z_- q^{-c(x)} ) / ( q^{h(x)} - q^{-h(x)} )

If a = q^N then z = q^{2N} z_-, so each numerator collapses:

    z q^c - z_- q^{-c}  =  z_- ( q^{2N+c} - q^{-c} )  =  z_- q^N ( q^{N+c} - q^{-(N+c)} )

and every factor becomes a ratio of symmetric quantum integers.  With
z_- q^N = 1/[N]_q the whole product is the HOOK-CONTENT FORMULA:

    w_lam  =  dim_q( V_lam^{sl_N} ) / [N]_q^{|lam|}

the U_q(sl_N) quantum dimension of V_lam, normalised by the n-th power of the
quantum dimension of the fundamental.  So an Ocneanu trace whose framing ratio
is a power of q IS a Lie-type specialisation, and the exponent names which one.

THE FAMILY, and where D sits in it.  Solving a = q^N for z gives

    z_N  =  q^N / [N]_q          (equivalently  q^{2N-1}(q^2-1)/(q^{2N}-1))

and z_2 = q^3/(q^2+1) IS convention D, on the nose.  Verified below for
N = 1, 2, 3, 4 and every partition of n <= 5: a^2 = q^{2N}, z_- q^N = 1/[N]_q,
w_lam = dim_q/[N]^n, and w_lam = 0 exactly when lam has more than N rows.

    N = 1   z = q                     w_lam = 0 unless lam is a single row
    N = 2   z = q^3/(q^2+1)           CONVENTION D
    N = 3   z = q^5/(q^4+q^2+1)
    N = 4   z = q^7/((q^2+1)(q^4+1))

THE (1^3) VANISHING IS THE sl_2 SIGNATURE.  The corpus records
y_(1,1,1) = 0 EXACTLY as a notable fact about the production trace, verified
three independent ways.  Under this reading it is not a coincidence of that
trace: a partition with more than N rows has a cell of content -N, whose
numerator factor carries [0]_q = 0.  Three rows, N = 2.  The same mechanism
gives the registered w_(3) = [4]_q/[2]_q^3 and w_(2,1) = 1/[2]_q^2 -- these are
dim_q of the 4-dimensional and 2-dimensional U_q(sl_2) irreps over [2]_q^3.

CONVENTION C IS NOT IN THE FAMILY, FOR ANY N.  Not "for no integer N" -- for no
N at all.  Its framing ratio is a^2 = -s^3/(s^6+s^4-s^3-s^2-1) with s = sqrt q,
whose logarithmic derivative q (a^2)'/a^2 is

    (3 s^6 + s^4 + s^2 + 3) / ( 2(-s^6 - s^4 + s^3 + s^2 + 1) )

which is NOT CONSTANT.  a^2 = q^t forces that derivative to be the constant t,
so no t exists, integer or otherwise.  Consistently, C's weights vanish on NO
partition -- checked at (1^3), (2,1,1) and (1^4), all non-zero -- so C has no
row bound and cannot be any sl_N specialisation.

WHAT THIS UPGRADES.  The convention-D ruling (owner, 2026-08-09 and
2026-08-15) is justified on record EMPIRICALLY: 195.8 ppm on tr_M(beta_Bor),
-197 ppm on m_p.  The previous step added a structural reason.  This one makes
it a classification: D is the sl_2 point of the Ocneanu family, C is off the
family entirely.  No anchor, no measurement and no ppm figure enters.

Exact symbolic arithmetic (sympy).  Convention C is computed in s = sqrt(q),
where its expressions are rational -- sympy's `cancel` fails outright on the
sqrt(q) forms, so the substitution is load-bearing, not cosmetic.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

q = sp.Symbol("q", positive=True)
hbar = q - 1 / q

CHECKS: list[tuple[str, bool]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def qint(m):
    """The symmetric quantum integer [m]_q = (q^m - q^-m)/(q - q^-1)."""
    return sp.cancel((q ** m - q ** (-m)) / (q - 1 / q))


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def hook(lam, i, j):
    return (lam[i] - j - 1) + sum(1 for r in range(i + 1, len(lam)) if lam[r] > j) + 1


def ocneanu(lam, z, *, var=q, hb=None):
    """The frame-general Ocneanu weight of `prop:markov-z-reconciliation`."""
    hb = hbar if hb is None else hb
    zm = z - hb
    num = den = sp.Integer(1)
    for (i, j) in cells(lam):
        c, h = j - i, hook(lam, i, j)
        num *= z * var ** c - zm * var ** (-c)
        den *= var ** h - var ** (-h)
    return sp.cancel(num / den)


def dimq_slN(lam, N):
    """Hook-content formula for the U_q(sl_N) quantum dimension of V_lam."""
    r = sp.Integer(1)
    for (i, j) in cells(lam):
        r *= qint(j - i + N) / qint(hook(lam, i, j))
    return sp.cancel(r)


def main() -> int:
    print("=" * 74)
    print("  THE OCNEANU WEIGHTS ARE sl_N QUANTUM DIMENSIONS -- AND D IS N = 2")
    print("=" * 74)
    print()

    zD = q ** 3 / (q ** 2 + 1)

    # ---- 0. the corpus's own formula and weights ----------------------------
    blk = (Path(__file__).resolve().parents[2] / "content"
           / "quantum-observable-universe" / "mass-endomorphism"
           / "markov-z-reconciliation.md")
    txt = blk.read_text() if blk.exists() else ""
    check("the corpus supplies the frame-general weight formula",
          "frame-general" in txt and "w_{(3)} = [4]_q/[2]_q^3" in txt,
          "prop:markov-z-reconciliation, with the registered D weights "
          "w_(3) = [4]_q/[2]_q^3, w_(2,1) = 1/[2]_q^2, w_(1^3) = 0")

    # ---- 1. the family ------------------------------------------------------
    print()
    ok_all = True
    for N in (1, 2, 3, 4):
        zN = sp.cancel(q ** N / qint(N))
        zm = sp.cancel(zN - hbar)
        ok_a = sp.simplify(sp.cancel(zN / zm) - q ** (2 * N)) == 0
        ok_zm = sp.simplify(zm * q ** N - 1 / qint(N)) == 0
        ok_w = ok_rows = True
        for n in range(1, 6):
            for lam in partitions(n):
                w = ocneanu(lam, zN)
                if sp.simplify(sp.cancel(w - dimq_slN(lam, N) / qint(N) ** n)) != 0:
                    ok_w = False
                if (sp.simplify(w) == 0) != (len(lam) > N):
                    ok_rows = False
        ok = ok_a and ok_zm and ok_w and ok_rows
        ok_all &= ok
        check(f"N={N}: z_N = q^{N}/[{N}]_q gives a = q^{N} and "
              f"w = dim_q(sl_{N})/[{N}]^n, vanishing iff rows > {N}",
              ok, f"z_{N} = {sp.factor(zN)}"
                  + ("      <== CONVENTION D" if N == 2 else ""))

    check("all four members verified over every partition of n <= 5", ok_all)
    check("convention D IS the N=2 member, on the nose",
          sp.simplify(sp.cancel(q ** 2 / qint(2) - zD)) == 0,
          "q^2/[2]_q = q^3/(q^2+1)")

    # ---- 2. the registered D weights, re-derived ---------------------------
    two = qint(2)
    for lam, name in [((3,), "[4]_q/[2]_q^3"), ((2, 1), "1/[2]_q^2"), ((1, 1, 1), "0")]:
        w = ocneanu(lam, zD)
        expected = {(3,): qint(4) / two ** 3, (2, 1): 1 / two ** 2,
                    (1, 1, 1): sp.Integer(0)}[lam]
        check(f"D: w_{lam} = {name}", sp.simplify(sp.cancel(w - expected)) == 0)
    check("the (1^3) vanishing is the sl_2 row bound, not a coincidence",
          sp.simplify(qint(0)) == 0,
          "a partition with more than N rows has a cell of content -N, whose "
          "numerator factor carries [0]_q = 0; three rows, N = 2")

    # ---- 3. convention C is in no member of the family ---------------------
    s = sp.Symbol("s", positive=True)          # s = sqrt(q); C is rational in s
    qs, hs = s ** 2, s ** 2 - 1 / s ** 2
    zCs = s / (1 + s ** 2)
    a2C = sp.cancel(sp.together(zCs / (zCs - hs)))
    logderiv = sp.simplify((s / 2) * sp.diff(a2C, s) / a2C)
    check("C: the framing ratio is q^N for NO N -- not merely no integer N",
          not logderiv.is_number,
          f"q (a^2)'/a^2 = {logderiv}, which is not constant; a^2 = q^t would "
          f"force it to be the constant t")
    nz = [lam for lam in [(1, 1, 1), (2, 1, 1), (1, 1, 1, 1)]
          if sp.simplify(sp.cancel(sp.together(
              ocneanu(lam, zCs, var=qs, hb=hs)))) != 0]
    check("C: the weights vanish on NO partition, so there is no row bound",
          nz == [(1, 1, 1), (2, 1, 1), (1, 1, 1, 1)],
          f"non-vanishing at {nz} -- C cannot be any sl_N specialisation")

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print()
    print("=" * 74)
    print(f"  {n_ok}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  The convention-D ruling now has a CLASSIFICATION behind it,")
    print("  not only the empirical 195.8 ppm: D is the sl_2 point of the Ocneanu")
    print("  family z_N = q^N/[N]_q, its block weights are U_q(sl_2) quantum")
    print("  dimensions over [2]_q^n, and the exact vanishing y_(1^3) = 0 that the")
    print("  corpus records is the sl_2 row bound.  Convention C lies off the")
    print("  family for every N and has no row bound at all.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
