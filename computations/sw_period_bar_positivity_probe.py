#!/usr/bin/env python3
"""
sw_period_bar_positivity_probe.py — is the q-transfer of the SW-period lower
bound unconditional, or does it need a regime restriction on q?

CONTEXT.  `QOU.Mass.SWPeriodSuperExponential` (PR #6052) proves the q=1 leg of
input (1) of the scope note of `prop:jet-filtration-binding-extensive`: the
classical period `a_D^(n)|_{q=1} = lw(n-1) = I(n)/n` grows at least factorially
(`n! <= I(2n)`), so it leaves every geometric class.  Lifting that bound to the
physical pin needs

    S(n)(q) := sum_{lam |- n} dim_q(lam)  >=  S(n)(1) = I(n)      for q > 0,

which the Lean lemma `barSymmetric_ge_at_one` supplies AS SOON AS S(n) is a
bar-symmetric Laurent polynomial with NON-NEGATIVE coefficients.  Whether it is
was open.  A regime restriction `1 < q0 < phi` was proposed (note that
`q - 1/q = 1` exactly at `q = phi`, so `1 < q < phi` <=> `0 < q - 1/q < 1`).

WHAT THIS MEASURES.  Exactly, symbolically, with the CANONICAL balanced q-integer
`[k]_q = (q^k - q^-k)/(q - q^-1)` and the q-hook dimension
`dim_q(lam) = [n]_q! / prod_{c in lam} [h(c)]_q` — the same convention as
`binding_manybody_jet_filtration.py` and `binding_selection_rule_tau_closure.py`:

  (1) is S(n) a Laurent polynomial (denominator a bare monomial q^k)?
  (2) is it bar-symmetric, S(n)(q) = S(n)(1/q)?
  (3) are its coefficients non-negative?
  (4) does S(n)(1) equal the involution number I(n)?
  (5) does S(n)(q) >= S(n)(1) hold AT and BEYOND phi, or does phi bound it?

PRECISION.  sympy exact symbolic and exact Rational throughout.  `float` is never
called and no floating value is constructed — every comparison is a decision over
Q or over Q(sqrt 5).  q0 enters only as the exact rational 110998/100000, used as
a sample point, never as a computed quantity.

EXPLORATORY — no production wiring, no fitted constant, no witness emitted.
"""
from __future__ import annotations

import sys

import sympy as sp

N_MAX = 9
q = sp.Symbol("q", positive=True)
PHI = (1 + sp.sqrt(5)) / 2


def qint(k: int) -> sp.Expr:
    """Balanced q-integer [k]_q = (q^k - q^-k)/(q - q^-1) — the canonical convention."""
    return sp.cancel((q ** k - q ** (-k)) / (q - q ** (-1)))


def qfac(n: int) -> sp.Expr:
    p = sp.Integer(1)
    for k in range(1, n + 1):
        p *= qint(k)
    return sp.cancel(p)


def partitions(n: int, m: int | None = None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam: tuple[int, ...]) -> list[int]:
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [
        (lam[i] - j - 1) + (conj[j] - i - 1) + 1
        for i in range(len(lam))
        for j in range(lam[i])
    ]


def dim_q(lam: tuple[int, ...]) -> sp.Expr:
    d = qfac(sum(lam))
    for h in hooks(lam):
        d = sp.cancel(d / qint(h))
    return sp.cancel(sp.simplify(d))


def S(n: int) -> sp.Expr:
    return sp.simplify(sp.cancel(sum((dim_q(l) for l in partitions(n)), sp.Integer(0))))


def involution_numbers(upto: int) -> list[int]:
    I = [1, 1]
    for n in range(2, upto + 1):
        I.append(I[n - 1] + (n - 1) * I[n - 2])
    return I


def main() -> int:
    I = involution_numbers(N_MAX + 2)
    failures: list[str] = []

    print("=" * 78)
    print("S(n) = sum_{lam|-n} dim_q(lam):  Laurent? bar-symmetric? coefficients >= 0?")
    print("=" * 78)
    print(f"{'n':>2} {'S(n)|q=1':>9} {'I(n)':>7} {'Laurent':>8} {'bar-sym':>8} {'coeff>=0':>9}")

    for n in range(2, N_MAX + 1):
        Sn = S(n)
        num, den = sp.fraction(sp.cancel(sp.together(Sn)))
        is_laurent = len(sp.Poly(den, q).terms()) == 1
        bar_sym = sp.simplify(Sn - Sn.subs(q, 1 / q)) == 0
        coeffs = sp.Poly(sp.expand(num), q).all_coeffs()
        nonneg = all(c >= 0 for c in coeffs)
        at1 = sp.nsimplify(sp.limit(Sn, q, 1))
        matches_I = sp.simplify(at1 - sp.Integer(I[n])) == 0

        print(f"{n:>2} {str(at1):>9} {I[n]:>7} {str(is_laurent):>8} "
              f"{str(bar_sym):>8} {str(nonneg):>9}")

        for cond, name in ((is_laurent, "Laurent"), (bar_sym, "bar-symmetry"),
                           (nonneg, "coefficient non-negativity"),
                           (matches_I, "S(n)(1) = I(n)")):
            if not cond:
                failures.append(f"n={n}: {name} FAILED")

    print()
    print("=" * 78)
    print("Does the golden ratio bound the transfer?  S(n)(q) >= S(n)(1) at/beyond phi")
    print("=" * 78)
    samples = [
        ("q0 = 110998/100000 (< phi)", sp.Rational(110998, 100000)),
        ("phi                       ", PHI),
        ("2   (> phi)               ", sp.Integer(2)),
        ("5   (>> phi)              ", sp.Integer(5)),
        ("1/2 (< 1, bar image of 2) ", sp.Rational(1, 2)),
    ]
    for n in (4, 6, 8):
        Sn = S(n)
        at1 = sp.nsimplify(sp.limit(Sn, q, 1))
        for label, val in samples:
            holds = sp.simplify(sp.nsimplify(Sn.subs(q, val)) - at1) >= 0
            print(f"  n={n}  q={label}  S(n) >= S(n)(1)?  {holds}")
            if not holds:
                failures.append(f"n={n}, q={label}: transfer FAILED")

    print()
    print("=" * 78)
    if failures:
        print("VERDICT: FAILURES —")
        for f in failures:
            print("  -", f)
        return 1
    print(f"VERDICT (n = 2..{N_MAX}, exact):")
    print("  S(n) IS a bar-symmetric Laurent polynomial with NON-NEGATIVE coefficients,")
    print(f"  and S(n)(1) = I(n) at every n.  So `barSymmetric_ge_at_one` applies and")
    print("  a_D^(n)(q) >= a_D^(n)(1) = I(n)/n  for ALL q > 0.")
    print()
    print("  The proposed restriction 1 < q0 < phi is NOT NEEDED for this transfer:")
    print("  the bound is verified to hold AT phi and at q = 2 and q = 5, well past it.")
    print("  Non-negativity of the coefficients is what does the work, and it carries")
    print("  no regime condition.  (phi remains the point where q - 1/q = 1; that is a")
    print("  real feature of the balanced q-integer, it just does not gate THIS claim.)")
    print()
    print("  NOT PROVED HERE: this is verification at n = 2..9, not a proof for all n.")
    print("  The general statement is the q-hook-length formula")
    print("  [n]_q!/prod[h]_q = sum_{T in SYT(lam)} q^maj(T), which needs the")
    print("  StandardYoungTableau layer Mathlib lacks — the same gap as beans")
    print("  qou-m3xr / qou-jlam.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
