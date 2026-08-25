"""The correct q-analogue of  sum_lam (f^lam)^2 = n!  -- and why Z(n) != 1.

Companion to `wlambda_normalisation_census.py`. That script measures the
sub-normalisation Z(n) = sum_lam w_lam(q) of the q-deformed Wedderburn weights
w_lam(q) = d_q(lam)^2 / [n]_q!. This one identifies what the correct graded
identity actually is, which explains why Z(n) was never going to be 1.

Everything is EXACT and SYMBOLIC in q (sympy). No float anywhere -- these are
polynomial identities, so exact arithmetic is both the correct tool and strictly
stronger than any numerical check (AGENTS.md NO-FLOAT64; probes are not exempt).

RESULT (verified n = 2..7, both conventions):

  standard  [m]_q = 1 + q + ... + q^(m-1):
      sum_lam  f^lam * R_lam(q)            == [n]_q!      where R_lam = q^n(lam) d_q(lam)
  balanced  [m]_q = (q^m - q^-m)/(q - q^-1)   <- the CORPUS convention:
      sum_lam  f^lam * q^(-kappa_lam) * d_q(lam)  == [n]_q!

  and in BOTH conventions:
      sum_lam  d_q(lam)^2                  != [n]_q!      (this is the Z(n) defect)

R_lam(q) is the FAKE DEGREE: the graded multiplicity of V_lam in the coinvariant
algebra C[V]/(invariants), whose Poincare polynomial is prod_i [d_i]_q = [n]_q!
for W = S_n. So the identity is the graded regular representation, i.e. standard
representation theory (Chevalley/Steinberg) -- not a new result. What is new here
is the DIAGNOSIS: the corpus's sum d_q^2 q-deforms BOTH factors of (f^lam)^2 and
squares, where the graded identity deforms exactly ONE into the graded
multiplicity and keeps the other classical.

kappa_lam = sum_x c(x) = n(lam') - n(lam) is the content statistic. Note it is
also exactly the statistic the notation register names as separating y_lam from
w_lam(q) ("the Wenzl-bridge identity y_lam = w_lam(q) holds on the self-conjugate
stratum only, where kappa_lam = 0") -- and q^(-kappa_lam) is 1 precisely there.
"""
import sympy as sp
from sympy.utilities.iterables import partitions as _parts

q = sp.symbols('q')


def partitions_of(n):
    out = []
    for p in _parts(n):
        lam = []
        for k in sorted(p, reverse=True):
            lam += [k] * p[k]
        out.append(tuple(lam))
    return sorted(out, reverse=True)


def conj(lam):
    if not lam:
        return ()
    return tuple(sum(1 for x in lam if x >= j) for j in range(1, lam[0] + 1))


def hooks(lam):
    lc = conj(lam)
    return [row - j + lc[j] - i - 1
            for i, row in enumerate(lam) for j in range(row)]


def contents(lam):
    return [j - i for i, row in enumerate(lam) for j in range(row)]


def n_stat(lam):
    """n(lam) = sum_i (i-1) lam_i."""
    return sum(i * l for i, l in enumerate(lam))


def qint_std(m):
    return sp.simplify(sum(q ** k for k in range(m)))


def qfact_std(n):
    return sp.prod([qint_std(m) for m in range(1, n + 1)])


def qint_bal(m):
    return sp.simplify((q ** m - q ** (-m)) / (q - q ** (-1)))


def qfact_bal(n):
    return sp.prod([qint_bal(m) for m in range(1, n + 1)])


def dq(lam, qint, qfact):
    """q-hook-length dimension  [n]_q! / prod_cells [h]_q."""
    return sp.simplify(qfact(sum(lam)) / sp.prod([qint(h) for h in hooks(lam)]))


def f_lam(lam):
    """Classical #SYT via the hook length formula."""
    import math
    pr = 1
    for h in hooks(lam):
        pr *= h
    return math.factorial(sum(lam)) // pr


def main(nmax=7):
    failures = []

    print("=" * 72)
    print("A. standard convention:  sum_lam f^lam * R_lam(q) == [n]_q! ?")
    print("=" * 72)
    for n in range(2, nmax + 1):
        P = partitions_of(n)
        lhs = sp.simplify(sum(f_lam(l) * q ** n_stat(l) * dq(l, qint_std, qfact_std) for l in P))
        ok = sp.simplify(lhs - qfact_std(n)) == 0
        print(f"  n={n}: {ok}")
        if not ok:
            failures.append(("A", n))

    print()
    print("=" * 72)
    print("B. balanced (corpus):  sum_lam f^lam * q^(-kappa_lam) * d_q(lam) == [n]_q! ?")
    print("=" * 72)
    for n in range(2, nmax + 1):
        P = partitions_of(n)
        lhs = sum(f_lam(l) * q ** (-sum(contents(l))) * dq(l, qint_bal, qfact_bal) for l in P)
        ok = sp.simplify(sp.together(sp.simplify(lhs) - qfact_bal(n))) == 0
        print(f"  n={n}: {ok}")
        if not ok:
            failures.append(("B", n))

    print()
    print("=" * 72)
    print("C. the corpus's object:  sum_lam d_q(lam)^2 == [n]_q! ?  (expect False)")
    print("=" * 72)
    for n in range(2, nmax + 1):
        P = partitions_of(n)
        for tag, qi, qf in (("std", qint_std, qfact_std), ("bal", qint_bal, qfact_bal)):
            bad = sp.simplify(sum(dq(l, qi, qf) ** 2 for l in P) - qf(n)) == 0
            print(f"  n={n} [{tag}]: identity holds? {bad}")
            if bad:
                failures.append(("C", n, tag))

    print()
    print("=" * 72)
    print("D. structure:  R_lam has N-coeffs, R_lam(1)=f^lam, kappa=n(lam')-n(lam)")
    print("=" * 72)
    for n in range(2, min(nmax, 6) + 1):
        for l in partitions_of(n):
            R = sp.Poly(sp.simplify(q ** n_stat(l) * dq(l, qint_std, qfact_std)), q)
            checks = (all(c >= 0 and c == int(c) for c in R.all_coeffs()),
                      R.eval(1) == f_lam(l),
                      sum(contents(l)) == n_stat(conj(l)) - n_stat(l))
            if not all(checks):
                failures.append(("D", n, l, checks))
    print(f"  all lam |- 2..{min(nmax,6)}: {'PASS' if not any(f[0]=='D' for f in failures) else 'FAIL'}")

    print()
    if failures:
        print(f"FAILURES: {failures}")
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
