"""pytest for Jing-Liu hook and two-row closed-form characters.

Verifies that chi_hook_hoefsmit / chi_two_row_hoefsmit agree with
the Hoefsmit seminormal matrix-trace direct computation to 1e-12
across partitions of n = 2..8.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def _min_cycle_word(mu):
    word = []
    offset = 0
    for part in mu:
        for t in range(part - 1):
            word.append(offset + t)
        offset += part
    return tuple(word)


def _chi_direct(lam, mu):
    import numpy as np
    from hecke_characters import build_seminormal_matrices
    sigmas, d, _ = build_seminormal_matrices(lam)
    if d == 0:
        return 0.0
    w = _min_cycle_word(mu)
    prod = np.eye(d)
    for g in w:
        prod = prod @ sigmas[g]
    return float(np.trace(prod))


def test_hook_characters_n2_n6():
    from q_parameter import Q as Q0
    from hecke_characters import partitions_of
    from jing_liu_characters import chi_hook_hoefsmit
    cases = 0
    for n in [2, 3, 4, 5, 6]:
        for mu in partitions_of(n):
            mu = tuple(mu)
            for k in range(1, n + 1):
                lam = (k,) + (1,) * (n - k)
                lam = tuple(x for x in lam if x > 0)
                chi_d = _chi_direct(lam, mu)
                chi_f = chi_hook_hoefsmit(lam, mu, Q0)
                assert abs(chi_d - chi_f) < 1e-12, (
                    f"hook n={n} λ={lam} μ={mu}: "
                    f"direct={chi_d} jing-liu={chi_f}")
                cases += 1
    assert cases > 0


def test_hook_characters_n7_n8():
    from q_parameter import Q as Q0
    from hecke_characters import partitions_of
    from jing_liu_characters import chi_hook_hoefsmit
    cases = 0
    for n in [7, 8]:
        for mu in partitions_of(n):
            mu = tuple(mu)
            for k in range(1, n + 1):
                lam = (k,) + (1,) * (n - k)
                lam = tuple(x for x in lam if x > 0)
                chi_d = _chi_direct(lam, mu)
                chi_f = chi_hook_hoefsmit(lam, mu, Q0)
                assert abs(chi_d - chi_f) < 1e-12
                cases += 1
    assert cases > 0


def test_two_row_characters():
    from q_parameter import Q as Q0
    from hecke_characters import partitions_of
    from jing_liu_characters import chi_two_row_hoefsmit
    cases = 0
    for n in [2, 3, 4, 5, 6, 7, 8]:
        for mu in partitions_of(n):
            mu = tuple(mu)
            for k in range(max(1, (n + 1) // 2), n + 1):
                nk = n - k
                lam = (k, nk) if nk > 0 else (k,)
                chi_d = _chi_direct(lam, mu)
                chi_f = chi_two_row_hoefsmit(lam, mu, Q0)
                assert abs(chi_d - chi_f) < 1e-12, (
                    f"two-row n={n} λ={lam} μ={mu}: "
                    f"direct={chi_d} jing-liu={chi_f}")
                cases += 1
    assert cases > 0


def test_hook_boundary_cases():
    """λ = (n) single row: χ^(n)(T_{γ_n}) = q^{n-1} in Hoefsmit."""
    from q_parameter import Q as Q0
    from jing_liu_characters import chi_hook_hoefsmit

    for n in [2, 3, 4, 5]:
        lam = (n,)
        mu = (n,)  # single n-cycle
        chi = chi_hook_hoefsmit(lam, mu, Q0)
        expected = Q0 ** (n - 1)
        assert abs(chi - expected) < 1e-12, (
            f"λ=(n={n}) μ=(n): χ={chi} vs q^(n-1)={expected}")


def test_column_hook_boundary():
    """λ = (1^n) single column: χ^(1^n)(T_{γ_n}) = (-q^{-1})^{n-1}."""
    from q_parameter import Q as Q0
    from jing_liu_characters import chi_hook_hoefsmit

    for n in [2, 3, 4, 5]:
        lam = (1,) * n
        mu = (n,)
        chi = chi_hook_hoefsmit(lam, mu, Q0)
        expected = (-1.0 / Q0) ** (n - 1)
        assert abs(chi - expected) < 1e-12, (
            f"λ=(1^{n}) μ=(n): χ={chi} vs (-q⁻¹)^(n-1)={expected}")
