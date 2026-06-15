"""silver_ratio_utils.py — shared Pell-Lucas / silver-ratio primitives.

Centralised utilities for testing whether a rational value at the
silver ratio $q = 1 + \\sqrt{2}$ lies in the closure of Pell-Lucas
numbers under powers and powers-of-2.

This module exists so the sector classifier, the SDP-extended c_k
extractor, the silver-ratio Pell-Lucas benchmark, and any future
silver-ratio probe share one canonical `is_pell_lucas_clean`
implementation — instead of each script reimplementing slightly-
different acceptance rules. Per the Gemini review of
`folio-assistant/computations/ck_sector_classifier.py` on PR #816.

Public surface
--------------
- `PELL_LUCAS` : prefix of the Pell-Lucas (companion-to-Pell)
  sequence `a_n` defined by `a_0 = a_1 = 1`,
  `a_{n+1} = 2·a_n + a_{n-1}`: `1, 1, 3, 7, 17, 41, 99, 239, ...`.
- `PELL`       : prefix of the Pell sequence `P_n` defined by
  `P_0 = 0`, `P_1 = 1`, `P_{n+1} = 2·P_n + P_{n-1}`:
  `0, 1, 2, 5, 12, 29, 70, 169, 408, ...`.
- `pell_lucas_up_to(bound)` : Pell-Lucas values up to and including
  the first one ≥ `bound`. Generates on demand.
- `is_pell_lucas_clean(value)` : True iff the reduced numerator
  (in absolute value) has the form `a_n^j · 2^t` for some
  Pell-Lucas number `a_n > 1`, `j ∈ {0, 1, ..., 4}`, `t ≥ 0`. The
  `j = 0` case collapses to a bare power of 2.

Status: structural utility, no compute side-effects.
"""
from __future__ import annotations

from fractions import Fraction


def pell_lucas_up_to(bound: int) -> list[int]:
    """Generate Pell-Lucas numbers `a_n` with `a_0 = a_1 = 1`,
    `a_{n+1} = 2 a_n + a_{n-1}`, up to (and including) the first
    value ≥ `bound`.

    Returns `[]` for `bound ≤ 0`. The bound is on Pell-Lucas
    magnitude, not on rung k — callers pass the numerator they
    want to factor against.
    """
    if bound <= 0:
        return []
    a, b = 1, 1
    out = [a]
    while a < bound:
        a, b = b, 2 * b + a
        out.append(a)
    return out


# Convenience snapshots for self-test display and downstream
# introspection. `is_pell_lucas_clean` uses `pell_lucas_up_to(num)`
# rather than these so it scales to numerators beyond the snapshot.
PELL_LUCAS = pell_lucas_up_to(10_000)
PELL: list[int] = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378]


def is_pell_lucas_clean(value: Fraction) -> bool:
    """Test if a rational value is Pell-Lucas-clean at silver ratio.

    The reduced numerator (in absolute value) is considered clean
    iff it has the form `a_n^j · 2^t` for some Pell-Lucas number
    `a_n > 1`, exponent `j ∈ {0, 1, ..., 4}`, and `t ≥ 0`. The
    `j = 0` case collapses to a bare power of 2.

    Empirically the c_k closed forms observed so far all sit in
    this shape; `j > 4` has not yet been needed but the bound is
    easy to lift if a future c_k pushes past it.

    Examples
    --------
    >>> is_pell_lucas_clean(Fraction(-2))         # power of 2
    True
    >>> is_pell_lucas_clean(Fraction(-49, 32))    # 49 = a_3^2
    True
    >>> is_pell_lucas_clean(Fraction(-11, 8))     # 11 not Pell-Lucas
    False
    >>> is_pell_lucas_clean(Fraction(7, 2))       # 7 = a_3
    True
    >>> is_pell_lucas_clean(Fraction(343, 128))   # 343 = a_3^3
    True
    >>> is_pell_lucas_clean(Fraction(98, 1))      # 98 = a_3^2 · 2
    True
    """
    num = abs(value.numerator)
    if num == 0:
        return True
    # Power of 2 (covers num = 1 = 2^0 as well; j = 0 case)
    if (num & (num - 1)) == 0:
        return True
    # (Pell-Lucas number)^j times (power of 2), for j ∈ 1..4.
    # Generate Pell-Lucas on demand up to `num` so the test stays
    # valid for c_k whose numerators exceed any pre-stored prefix.
    for pl in pell_lucas_up_to(num):
        if pl <= 1:
            continue
        p_pow = 1
        for _j in range(1, 5):
            p_pow *= pl
            if p_pow > num:
                break
            if num % p_pow == 0:
                quotient = num // p_pow
                if quotient != 0 and (quotient & (quotient - 1)) == 0:
                    return True
    return False


if __name__ == "__main__":
    print("Pell-Lucas (a_n):", PELL_LUCAS[:12])
    print("Pell        (P_n):", PELL[:12])
    tests = [
        (Fraction(-2), True, "power of 2"),
        (Fraction(-49, 32), True, "a_3^2"),
        (Fraction(-11, 8), False, "11 not Pell-Lucas"),
        (Fraction(7, 2), True, "a_3"),
        (Fraction(-7), True, "a_3"),
        (Fraction(-8), True, "2^3"),
        (Fraction(49, 16), True, "a_3^2"),
        (Fraction(343, 128), True, "a_3^3"),
        (Fraction(98, 1), True, "a_3^2 · 2"),
    ]
    for v, expected, why in tests:
        got = is_pell_lucas_clean(v)
        mark = "✓" if got == expected else "✗"
        print(f"  {mark} {str(v):>10}  expect={expected}  got={got}  ({why})")
