"""Regression tests for `pyhecke.tl` — the TL_n quotient Markov–Gram form.

Bean `qou-8iru` (the TL_n compute move) / `qou-cds2` (the Gram singularity).

These pin the facts that make the quotient form usable in place of the
`pinv` / rank-one-shift workarounds:

1. the basis is `Catalan(n)` and, at `n = 3`, is the `NF_BASIS` minus its one
   321-pattern word — the reason PR #5572's "first five NF cosets" was the
   right five;
2. the general-`n` Ocneanu recursion reproduces `pyhecke.gram`'s hard-coded
   `TR_M` **exactly**, symbolically, which is a cross-*implementation* check
   and not an internal consistency one;
3. the `n = 3` quotient determinant is PR #5572's closed form;
4. the full form's corank is `n! − Catalan(n)` at `n = 3, 4, 5`;
5. the quotient form has a genuine **inverse** — `G · G⁻¹ = I` with exact 1s
   and 0s — where the full form has only a pseudoinverse.

Everything is exact (`Fraction` over ℚ, sympy over ℚ(q)). No float64 appears
in any assertion; the one mpmath case runs at 60 dps and its tolerance is set
by that arithmetic, not by float64 epsilon.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial

import pytest
import sympy as sp

from pyhecke import gram as _gram
from pyhecke import tl


def _word_to_perm(n: int, word) -> tuple[int, ...]:
    p = tuple(range(1, n + 1))
    for i in word:
        lst = list(p)
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        p = tuple(lst)
    return p


@pytest.mark.parametrize("n", [2, 3, 4, 5, 6, 7])
def test_tl_basis_size_is_catalan(n: int) -> None:
    assert len(tl.tl_basis(n)) == tl.catalan(n)


def test_tl_basis_3_is_nf_basis_minus_the_321_word() -> None:
    """The `n = 3` quotient basis is exactly `gram.NF_BASIS` less `(0,1,0)`.

    `(0,1,0)` is the word for `(3,2,1)`, the sole 321 pattern in `S_3` and the
    generator of the radical.  This is the structural reason the ad-hoc
    "take the first five NF cosets" of PR #5572 worked.
    """
    nf = [_word_to_perm(3, w) for w in _gram.NF_BASIS]
    assert set(tl.tl_basis(3)) == set(nf[:5])
    assert nf[5] == (3, 2, 1)
    assert nf[5] not in tl.tl_basis(3)


def test_ocneanu_trace_reproduces_gram_TR_M_symbolically() -> None:
    """Cross-implementation: a general-`n` recursion vs a hard-coded 6×6 table."""
    q = sp.symbols("q", positive=True)
    one = sp.Integer(1)
    h, z = tl.markov_weights(q, one)
    got = [sp.cancel(tl.markov_trace_basis(_word_to_perm(3, w), 3, h, z, one))
           for w in _gram.NF_BASIS]
    want = [one, z, z, z ** 2, z ** 2, sp.cancel(h * z ** 2 + z)]
    for a, b in zip(got, want):
        assert sp.simplify(a - b) == 0


def test_full_H3_form_is_identically_singular() -> None:
    """`det G = 0` over ℚ(q) — the blocker, not a `q₀` artefact."""
    q = sp.symbols("q", positive=True)
    G = sp.Matrix(tl.full_hecke_gram(3, q, sp.Integer(1)))
    assert sp.simplify(sp.cancel(G.det())) == 0


def test_TL3_determinant_matches_pr_5572() -> None:
    q = sp.symbols("q", positive=True)
    G = sp.Matrix(tl.tl_gram(3, q, sp.Integer(1)))
    want = sp.cancel(-(q ** 4 + 1) * (q ** 2 - q + 1) ** 4
                     * (q ** 2 + q + 1) ** 4 / (q ** 2 + 1) ** 10)
    assert sp.simplify(sp.cancel(G.det()) - want) == 0


@pytest.mark.parametrize("n,corank", [(3, 1), (4, 3 ** 2 + 1 ** 2),
                                      (5, 6 ** 2 + 5 ** 2 + 4 ** 2 + 1 ** 2)])
def test_full_gram_corank_matches_qou_cds2(n: int, corank: int) -> None:
    """Corank `n! − Catalan(n)`: 1, 10, 78 — `qou-cds2`'s accounting, exactly."""
    rank = tl.gram_rank_exact(n)
    assert rank == tl.catalan(n)
    assert factorial(n) - rank == corank


@pytest.mark.parametrize("q", [Fraction(111, 100), Fraction(7, 5)])
@pytest.mark.parametrize("n", [3, 4, 5])
def test_TL_gram_is_nonsingular_exactly(n: int, q: Fraction) -> None:
    """Nonzero at a rational point ⇒ not identically zero over ℚ(q)."""
    assert sp.Matrix(tl.tl_gram_exact(n, q)).det() != 0


@pytest.mark.parametrize("n", [3, 4, 5])
def test_TL_gram_inverse_is_exact(n: int) -> None:
    """A genuine inverse: `G · G⁻¹ = I` entry-by-entry with exact 1s and 0s.

    The object it replaces is `gram.G_PINV`, whose residual on the singular
    6×6 form is `‖G · G_INV − I‖ = 1.64` (measured, `qou-cds2`).
    """
    G = tl.tl_gram_exact(n)
    Gi = tl.tl_gram_inverse_exact(n)
    m = len(G)
    for i in range(m):
        for j in range(m):
            entry = sum(G[i][k] * Gi[k][j] for k in range(m))
            assert entry == (1 if i == j else 0)


def test_full_form_inverse_raises() -> None:
    """Unlike `np.linalg.inv`, the exact path refuses rather than returning noise."""
    with pytest.raises(ZeroDivisionError):
        tl._inverse_exact(tl.full_hecke_gram_exact(3))


def test_tl_gram_exact_rejects_a_float_q() -> None:
    """An "exact" Gram built from a float is a contradiction; refuse it."""
    with pytest.raises(TypeError):
        tl.tl_gram_exact(3, 1.1099785827513808)


def test_tl_gram_mp_inverse_at_substrate_q0() -> None:
    """60-dps mpmath at the proton-pinned `q₀`, no float64 on the path.

    The threshold is set by the *weakest arithmetic used* — 60-dps mpmath with
    `q₀` parsed from its 50-digit decimal string — so 1e-45 is the honest floor.
    A float64-derived `q` would cap agreement near 1e-16 and this would fail,
    which is the point of writing the bound this way.
    """
    import mpmath as mp
    with mp.workdps(60):
        G = mp.matrix(tl.tl_gram_mp(3))
        Gi = tl.tl_gram_inverse_mp(3)
        prod = G * Gi
        resid = max(abs(prod[i, j] - (1 if i == j else 0))
                    for i in range(5) for j in range(5))
        assert resid < mp.mpf(10) ** -45


def test_tl_gram_solve_mp_round_trips() -> None:
    import mpmath as mp
    with mp.workdps(60):
        G = mp.matrix(tl.tl_gram_mp(3))
        rhs = [mp.mpf(1), mp.mpf(2), mp.mpf(3), mp.mpf(4), mp.mpf(5)]
        x = tl.tl_gram_solve_mp(rhs, 3)
        back = G * x
        resid = max(abs(back[i] - rhs[i]) for i in range(5))
        assert resid < mp.mpf(10) ** -45


def test_module_does_not_perturb_gram() -> None:
    """`pyhecke.tl` is additive: importing it changes nothing in `pyhecke.gram`.

    `G_PINV` is computed at *module import*, so a consumer's numbers would move
    the moment that name's meaning changed.  Nothing here touches it.
    """
    assert not hasattr(_gram, "G_INV")
    assert _gram.G_PINV.shape == (6, 6)
    assert _gram.NF_BASIS == [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
