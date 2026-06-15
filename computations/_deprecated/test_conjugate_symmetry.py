"""pytest for Track 2 — conjugate-partition symmetry.

Verifies χ^{λ'}(T_w) = (-1)^{ℓ(w)} · χ^λ(T_w) |_{q → q^{-1}} to 1e-12
across partitions of n = 4..8 and a spread of braid words.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def test_conjugate_partition_involution():
    from conjugate_symmetry import conjugate_partition
    assert conjugate_partition(()) == ()
    assert conjugate_partition((4,)) == (1, 1, 1, 1)
    assert conjugate_partition((2, 2)) == (2, 2)        # self-conjugate
    assert conjugate_partition((3, 1)) == (2, 1, 1)
    # idempotence
    for lam in [(5, 3, 1), (4, 2, 1, 1), (6,), (3, 3, 3)]:
        assert conjugate_partition(conjugate_partition(lam)) == lam


def test_is_self_conjugate():
    from conjugate_symmetry import is_self_conjugate
    assert is_self_conjugate((2, 2))
    assert is_self_conjugate((3, 2, 1))
    assert is_self_conjugate((4, 3, 2, 1))
    assert is_self_conjugate((3, 1, 1))   # symmetric hook L
    assert not is_self_conjugate((4, 1))
    assert not is_self_conjugate((3, 2))


def test_conjugate_pair_representatives_n8():
    """At n=8: p(8)=22 partitions.  Self-conj: (4,2,1,1) only?
    Actually (3,3,1,1), (2,2,2,2)... verify by enumeration."""
    from conjugate_symmetry import (conjugate_pair_representatives,
                                       is_self_conjugate)
    from hecke_characters import partitions_of
    self_conj, pairs = conjugate_pair_representatives(8)
    # Cover every partition exactly once
    covered = set(self_conj)
    for rep, other in pairs:
        assert rep not in covered
        assert other not in covered
        covered.add(rep)
        covered.add(other)
    all_parts = {tuple(p) for p in partitions_of(8)}
    assert covered == all_parts
    # Self-conjugate ones really are self-conjugate
    for lam in self_conj:
        assert is_self_conjugate(lam)


def test_character_formula_at_n4_n6():
    """Direct verification at small n (tight tolerance)."""
    from conjugate_symmetry import (detect_conjugate_formula,
                                       conjugate_partition,
                                       is_self_conjugate)
    from hecke_characters import partitions_of
    from q_parameter import Q as Q0

    # Build exhaustive test cases for n = 4, 6
    test_cases = []
    for n in [4, 5, 6]:
        max_gen = n - 1
        words = [(), (0,), (1,), (0, 1), (1, 0), (1, 2, 1),
                 (0, 1, 2, 1)]
        words = [w for w in words if all(g < max_gen for g in w)]
        for lam in partitions_of(n):
            lam = tuple(lam)
            if is_self_conjugate(lam):
                continue
            if conjugate_partition(lam) < lam:
                continue  # visit each pair once via lex-min rep
            for w in words:
                test_cases.append((lam, w, Q0))
    assert test_cases  # nontrivial

    winner = detect_conjugate_formula(test_cases, tol=1e-12, verbose=False)
    assert winner == "A_q_inv_sign", (
        f"Conjugation formula at n=4..6 is {winner}, not "
        f"A_q_inv_sign.  Convention may differ from Hoefsmit.")


def test_character_formula_at_n7_n8():
    """Extended to n=7,8 with more words per partition."""
    from conjugate_symmetry import (detect_conjugate_formula,
                                       conjugate_partition,
                                       is_self_conjugate)
    from hecke_characters import partitions_of
    from q_parameter import Q as Q0

    test_cases = []
    for n in [7, 8]:
        max_gen = n - 1
        words = [(0, 2), (0, 1, 2, 3), (1, 2, 3, 0, 1),
                 (0, 1, 0, 2, 1), (0, 2, 4, 1, 3), (1, 3, 5)]
        words = [w for w in words if all(g < max_gen for g in w)]
        for lam in partitions_of(n):
            lam = tuple(lam)
            if is_self_conjugate(lam):
                continue
            if conjugate_partition(lam) < lam:
                continue
            for w in words:
                test_cases.append((lam, w, Q0))
    assert test_cases

    winner = detect_conjugate_formula(test_cases, tol=1e-12, verbose=False)
    assert winner == "A_q_inv_sign"


def test_conjugate_character_value_direct():
    """conjugate_character_value(λ, w, q, formula='A_q_inv_sign') agrees
    with directly-computed χ^{λ'}(T_w) to 1e-12 on sample cases."""
    import numpy as np
    from conjugate_symmetry import (_eval_chi_direct,
                                       conjugate_character_value,
                                       conjugate_partition,
                                       is_self_conjugate)
    from hecke_characters import partitions_of
    from q_parameter import Q as Q0

    sample_words = [(), (0,), (0, 1), (0, 1, 2), (0, 1, 2, 3)]
    n_cases = 0
    for n in [4, 5, 6]:
        max_gen = n - 1
        words = [w for w in sample_words if all(g < max_gen for g in w)]
        for lam in partitions_of(n):
            lam = tuple(lam)
            if is_self_conjugate(lam):
                continue
            lp = conjugate_partition(lam)
            for w in words:
                chi_direct = _eval_chi_direct(lp, w, Q0)
                chi_from_formula = conjugate_character_value(
                    lam, w, Q0, formula="A_q_inv_sign")
                assert abs(chi_direct - chi_from_formula) < 1e-12, (
                    f"λ={lam} λ'={lp} w={w}: direct={chi_direct} "
                    f"formula={chi_from_formula}")
                n_cases += 1
    assert n_cases > 0
