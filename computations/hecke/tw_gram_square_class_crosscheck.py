#!/usr/bin/env python3
"""Cross-check the T_w Gram square-class theorem against the measured determinants.

Bean `qou-kwoa`.  Companion to `tw_gram_determinant_probe.py`, which MEASURED

    n = 1   det =            [2]_q^2
    n = 2   det = -   2^4  . q^2  . [2]_q^2  . [3]_q^6
    n = 3   det = - 2^4.3^18 . q^22 . [2]_q^28 . [3]_q^6 . [4]_q^20

by factoring exact symbolic determinants of the regular representation.

`QOU.Hecke.TwBasis.twGram_det_eq_sq_mul_prod` (Lean, sorry-free) proves

    det(twGram) = (det P)^2 * prod_lambda sign(prodComm) * d_lambda^(d_lambda^2)

with `IsUnit (det P)`, `d_lambda` the number of standard Young tableaux of shape
lambda.  Since P is a change of basis and the block factors are the only
non-square part, that makes TWO predictions the probe can test, neither of which
was used in deriving it:

  (A) SIGN.  `prodComm` on `J x J` with `|J| = d` fixes the d diagonal pairs and
      swaps the remaining d(d-1)/2 pairs, so its signature is (-1)^(d(d-1)/2),
      and the sign of the determinant is the product over blocks.

  (B) SQUARE CLASS.  All q-dependence sits inside `(det P)^2`, so after dividing
      out the signed integer constant the remainder must be a PERFECT SQUARE in
      Q(q) -- every irreducible factor to an even power.

Prediction (B) is the substantive one.  It is not implied by the shape of the
measured answer: an arbitrary determinant of this size has no reason for every
exponent to be even, and a single odd exponent anywhere would refute the
theorem's claim that the Wedderburn isomorphism contributes no factor.

**Exact arithmetic only** (AGENTS.md, PROBES ARE NOT EXEMPT).  Every quantity is
a Python int or a sympy expression in the indeterminate q.  There is no float
here and none is admissible: a float would make the "is it a perfect square"
test meaningless, since every positive float is a square.

Run: python3 computations/hecke/tw_gram_square_class_crosscheck.py
"""

from __future__ import annotations

import sys
from math import factorial

import sympy as sp

q = sp.symbols("q")


def q_int(k: int):
    """[k]_q = 1 + q + ... + q^(k-1), exact."""
    return sum(q**i for i in range(k))


def partitions(n: int, mx: int | None = None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def syt_count(lam: tuple[int, ...]) -> int:
    """Standard Young tableaux of shape lam, by the hook-length formula (exact)."""
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    hooks = 1
    for i, row in enumerate(lam):
        for j in range(row):
            hooks *= (row - j) + (conj[j] - i) - 1
    assert factorial(n) % hooks == 0, "hook product must divide n!"
    return factorial(n) // hooks


# The measured determinants, transcribed from tw_gram_determinant_probe.py.
MEASURED = {
    1: q_int(2) ** 2,
    2: -(2**4) * q**2 * q_int(2) ** 2 * q_int(3) ** 6,
    3: -(2**4) * 3**18 * q**22 * q_int(2) ** 28 * q_int(3) ** 6 * q_int(4) ** 20,
}


def block_sign(d: int) -> int:
    """Signature of the transpose involution on a d x d index set."""
    return (-1) ** (d * (d - 1) // 2)


def is_perfect_square(expr):
    """Exact test: unit leading coefficient and every irreducible exponent even."""
    coeff, factors = sp.factor_list(sp.together(sp.cancel(expr)))
    if sp.nsimplify(coeff) != 1:
        return False, None
    if any(e % 2 for _, e in factors):
        return False, None
    root = sp.prod([base ** (e // 2) for base, e in factors])
    return True, sp.factor(root)


def main() -> int:
    ok = True
    for n in (1, 2, 3):
        dims = [syt_count(lam) for lam in partitions(n + 1)]
        sign = 1
        const = 1
        for d in dims:
            sign *= block_sign(d)
            const *= d ** (d * d)

        det = sp.expand(MEASURED[n])
        q_part = sp.cancel(det / (sign * const))
        square, root = is_perfect_square(q_part)

        # (A) The sign test IS the leading coefficient of the quotient: if the
        # predicted sign were wrong, dividing by it would leave -1 out front.
        # There is no separate sign computation to do, and an earlier draft of
        # this probe had one that was overwritten before use -- it looked like a
        # test and was not.
        sign_ok = sp.factor_list(q_part)[0] == 1

        print(f"n = {n}   block dims = {dims}")
        print(f"  (A) sign   predicted {sign:+d}   "
              f"constant predicted {sign * const}   matches: {sign_ok}")
        print(f"      measured det / predicted constant = {sp.factor(q_part)}")
        print(f"  (B) perfect square in Q(q)? {square}")
        if square:
            print(f"      sqrt = {root}")
        else:
            print("      REFUTED: an odd exponent survives -- the Wedderburn "
                  "isomorphism would have to contribute a non-square factor.")
            ok = False
        if not sign_ok:
            print(f"      REFUTED: leading coefficient {sp.factor_list(q_part)[0]} != 1, "
                  "so the predicted sign is wrong.")
            ok = False
        print()

    print("RESULT:", "all ranks confirm both predictions" if ok else "REFUTED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
