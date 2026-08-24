"""`LaurentQ.from_sympy` must accept a product of sums.

Regression for bean `qou-ls7l`. The `is_Mul` branch of the parser accepts
only Numbers and powers of `q` as factors, so a PRODUCT OF SUMS raised
`ValueError` even when every factor was Laurent and the product plainly was
too — contradicting the method's own docstring ("sums and products of the
above").

The live cost: `habiro_coefficients_extended.py` failed on all four atoms
with `non-Laurent factor -(1 - 1/q**4)*(q - 1)**2/12 + 1/2`, which left the
L1 tr_M cross-check gate consuming a witness nobody could regenerate.

The fix expands and retries once. `sp.expand` is identity-preserving, so
this widens what parses without changing any value — and the genuinely
non-Laurent cases below still raise, which is the half that makes the
widening safe rather than merely permissive.
"""

import sympy as sp

from pyhecke.laurent_q import LaurentQ

q = sp.Symbol("q")


def _roundtrip(expr):
    return sp.simplify(LaurentQ.from_sympy(expr, q).to_sympy(q) - sp.expand(expr))


def test_habiro_product_of_sums_parses():
    """The exact expression that broke habiro_coefficients_extended."""
    expr = (-q + 1 / q) * (-(1 - 1 / q**4) * (q - 1) ** 2 / 12 + sp.Rational(1, 2))
    assert _roundtrip(expr) == 0


def test_simple_product_of_sums_parses():
    assert _roundtrip((q + 1 / q) * (q - 1 / q)) == 0


def test_nested_product_of_sums_parses():
    assert _roundtrip((q + 1) * (q - 1) * (1 / q + 2)) == 0


def test_flat_laurent_still_parses():
    """The fast path is untouched — this never needed expanding."""
    assert _roundtrip(q**2 - 3 + 1 / q) == 0


def test_zero_and_constants():
    assert LaurentQ.from_sympy(sp.Integer(0), q).is_zero()
    assert _roundtrip(sp.Rational(-5, 7)) == 0


def test_genuinely_non_laurent_still_raises():
    """Widening must not become "accepts anything"."""
    for bad in (sp.sqrt(q), q + sp.Symbol("z"), sp.exp(q), q ** sp.Rational(1, 3)):
        try:
            LaurentQ.from_sympy(bad, q)
        except ValueError:
            continue
        raise AssertionError(f"expected ValueError for {bad}")


def test_non_laurent_inside_a_product_still_raises():
    """A product of sums where one factor is not Laurent."""
    try:
        LaurentQ.from_sympy((q + 1 / q) * (sp.sqrt(q) + 1), q)
    except ValueError:
        return
    raise AssertionError("expected ValueError for a product with a sqrt factor")
