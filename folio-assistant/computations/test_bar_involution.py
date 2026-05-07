"""pytest for bar_involution kernel.

Verifies the bar involution Z/2Z action on polynomials and on
H_n(q) elements written as {word: coeff} dicts, the S^1 / root-of-
unity dials, and the Kashiwara-graph BFS over partition addable cells.
"""
import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from bar_involution import (  # noqa: E402
    bar_antisymmetric_part,
    bar_coeff_dict,
    bar_polynomial,
    bar_symmetric_part,
    bar_T_word,
    crystal_path_count,
    crystal_paths,
    is_bar_invariant,
    is_bar_invariant_poly,
    root_of_unity_truncate,
    s1_phase,
    unitary_q,
)
from bar_involution import q as q_sym  # noqa: E402


# ── 1.  bar on polynomials in q ─────────────────────────────

def test_bar_polynomial_q_inverse():
    assert sp.simplify(bar_polynomial(q_sym) - 1 / q_sym) == 0


def test_bar_polynomial_invariant_q_plus_qinv():
    assert is_bar_invariant_poly(q_sym + 1 / q_sym)


def test_bar_polynomial_invariant_q_squared_plus_qinv_squared():
    assert is_bar_invariant_poly(q_sym ** 2 + 1 / q_sym ** 2)


def test_bar_polynomial_not_invariant_pure_q():
    assert not is_bar_invariant_poly(q_sym)
    assert not is_bar_invariant_poly(1 / q_sym)


def test_bar_polynomial_idempotent():
    P = q_sym ** 3 - 2 * q_sym + 5 / q_sym
    assert sp.simplify(bar_polynomial(bar_polynomial(P)) - P) == 0


# ── 2.  bar on T_w  ────────────────────────────────────────

def test_bar_T_word_inverts_word():
    inv, _ = bar_T_word((0, 1, 2, 1))
    assert inv == (1, 2, 1, 0)


def test_bar_T_word_prefactor_lusztig():
    # Lusztig sign: (-q)^{-L}
    _, pref = bar_T_word((0, 1, 2))
    assert sp.simplify(pref - (-q_sym) ** -3) == 0


def test_bar_T_word_identity():
    inv, pref = bar_T_word(())
    assert inv == ()
    assert sp.simplify(pref - 1) == 0


# ── 3.  bar on coefficient dicts  ──────────────────────────

def test_bar_coeff_dict_inverts_words():
    elem = {(0, 1): sp.S.One}
    barred = bar_coeff_dict(elem)
    assert (1, 0) in barred


def test_sym_plus_antisym_equals_original():
    elem = {(0,): q_sym, (1, 0): sp.S.One, (2, 1, 0): q_sym ** 2}
    sym = bar_symmetric_part(elem)
    asym = bar_antisymmetric_part(elem)
    keys = set(elem) | set(sym) | set(asym)
    for k in keys:
        original = sp.expand(elem.get(k, sp.S.Zero))
        rebuilt = sp.expand(sym.get(k, sp.S.Zero) + asym.get(k, sp.S.Zero))
        assert sp.simplify(original - rebuilt) == 0, \
            f"sym+asym ≠ original at {k}: orig={original}, rebuilt={rebuilt}"


def test_bar_invariant_element_detected():
    # T_e (identity) with constant coefficient is bar-invariant.
    assert is_bar_invariant({(): sp.S.One})


def test_bar_symmetric_part_is_bar_invariant():
    elem = {(0,): q_sym, (1, 0): sp.S(2)}
    sym = bar_symmetric_part(elem)
    assert is_bar_invariant(sym)


def test_bar_antisymmetric_part_is_bar_antisymmetric():
    # bar(asym) should equal -asym
    elem = {(0,): q_sym, (1, 0): sp.S(2)}
    asym = bar_antisymmetric_part(elem)
    barred = bar_coeff_dict(asym)
    keys = set(asym) | set(barred)
    for k in keys:
        a = sp.expand(asym.get(k, sp.S.Zero))
        b = sp.expand(barred.get(k, sp.S.Zero))
        assert sp.simplify(a + b) == 0, \
            f"bar(asym) ≠ -asym at {k}: asym={a}, bar(asym)={b}"


# ── 4.  S^1 unitarity dial ────────────────────────────────

def test_s1_phase_unit_modulus():
    for theta in (sp.pi / 6, sp.pi / 4, sp.pi / 3, sp.pi):
        z = complex(s1_phase(theta))
        assert abs(abs(z) - 1) < 1e-12


def test_unitary_q_equals_identity_at_two_pi():
    val = complex(unitary_q(q_sym, 2 * sp.pi))
    assert abs(val - 1) < 1e-10


def test_unitary_q_evaluates_polynomial():
    # (q + q^-1) at q = i is 0
    val = complex(unitary_q(q_sym + 1 / q_sym, sp.pi / 2))
    assert abs(val) < 1e-10


# ── 5.  root-of-unity truncation ──────────────────────────

def test_root_of_unity_returns_one():
    for k in (2, 3, 4, 5, 6, 8, 12):
        val = complex(root_of_unity_truncate(q_sym ** k, k))
        assert abs(val - 1) < 1e-9, f"q^{k} at primitive {k}-th root ≠ 1"


def test_root_of_unity_q_squared():
    # q^2 at primitive 4-th root (q = i) = -1
    val = complex(root_of_unity_truncate(q_sym ** 2, 4))
    assert abs(val - (-1)) < 1e-10


def test_root_of_unity_invalid_k():
    import pytest
    with pytest.raises(ValueError):
        root_of_unity_truncate(q_sym, 0)
    with pytest.raises(ValueError):
        root_of_unity_truncate(q_sym, -3)


# ── 6.  Crystal-graph BFS  ────────────────────────────────

def test_crystal_paths_depth_zero():
    paths = crystal_paths((), 0)
    assert paths == [((),)]


def test_crystal_paths_depth_one_from_empty():
    paths = crystal_paths((), 1)
    assert len(paths) == 1
    assert paths[0] == ((), (1,))


def test_crystal_path_count_matches_oeis_a000085():
    """Paths from ∅ at depth d count the involutions in S_d
    (sum over partitions λ ⊢ d of #SYT(λ)).  OEIS A000085."""
    expected = [1, 1, 2, 4, 10, 26, 76, 232]
    actual = [crystal_path_count((), d) for d in range(len(expected))]
    assert actual == expected, \
        f"Crystal path counts disagree with OEIS A000085: {actual}"


def test_crystal_paths_match_count():
    for d in range(5):
        assert len(crystal_paths((), d)) == crystal_path_count((), d)


def test_crystal_paths_invalid_depth():
    import pytest
    with pytest.raises(ValueError):
        crystal_paths((), -1)


def test_crystal_paths_from_nonempty_partition():
    """From λ = (2, 1) at depth 1, addable cells are at row 0 (→ (3,1)),
    row 1 (→ (2,2)), and a new bottom row (→ (2,1,1)).  All three are
    valid partitions."""
    paths = crystal_paths((2, 1), 1)
    children = sorted(p[-1] for p in paths)
    assert children == [(2, 1, 1), (2, 2), (3, 1)]
