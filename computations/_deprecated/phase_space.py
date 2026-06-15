"""
Vectorized Fermi beta-decay phase-space integral.

Replaces the 50,000-iteration Python loop in all-nuclei-transfer-matrix.py
and halflife-from-transfer-matrix.py with numpy vectorization (~500x speedup).

Usage:
    from phase_space import fermi_phase_space, half_life

    f = fermi_phase_space(Z_daughter=2, Q_MeV=0.01861)
    t = half_life(Z_daughter=2, Q_MeV=0.01861)  # seconds

The Sommerfeld factor F(η) handles Coulomb corrections for all Z.

@module folio-assistant/computations/phase_space
"""

import math
import numpy as np


def fermi_phase_space(
    Z_daughter: int,
    Q_MeV: float,
    alpha_em: float = 1 / 137.036,
    m_e_MeV: float = 0.51100,
    n_steps: int = 50_000,
) -> float:
    """Vectorized Fermi phase-space integral f(Z, Q).

    Computes ∫₁^W₀ F(η) p_e W (W₀ - W)² dW where:
      W = total electron energy / m_e c²
      p_e = √(W² - 1)
      η = α Z_daughter / β (Sommerfeld parameter)
      F(η) = 2πη / (1 - exp(-2πη))

    Parameters
    ----------
    Z_daughter : int
        Atomic number of the daughter nucleus.
    Q_MeV : float
        Beta-decay Q-value in MeV.
    alpha_em : float
        Fine structure constant (default: CODATA).
    m_e_MeV : float
        Electron mass in MeV.
    n_steps : int
        Number of integration steps (default: 50,000).

    Returns
    -------
    float
        Dimensionless phase-space integral.
    """
    W0 = 1.0 + Q_MeV / m_e_MeV
    if W0 <= 1.0:
        return 0.0

    # Midpoint rule with vectorized evaluation
    W = np.linspace(1.0, W0, n_steps + 1)
    W = 0.5 * (W[:-1] + W[1:])  # midpoints
    dW = (W0 - 1.0) / n_steps

    p_e = np.sqrt(W * W - 1.0)
    beta = p_e / W
    eta = alpha_em * Z_daughter / beta

    # Sommerfeld factor: F(η) = 2πη / (1 - exp(-2πη))
    # Handle η → 0 limit numerically (F → 1)
    two_pi_eta = 2.0 * np.pi * eta
    # Use expm1 for numerical stability when 2πη is small
    with np.errstate(over="ignore", divide="ignore"):
        F = np.where(
            np.abs(eta) > 1e-12,
            two_pi_eta / (-np.expm1(-two_pi_eta)),
            1.0,
        )

    integrand = F * p_e * W * (W0 - W) ** 2
    return float(np.sum(integrand) * dW)


def half_life(
    Z_daughter: int,
    Q_MeV: float,
    alpha_em: float = 1 / 137.036,
    m_e_MeV: float = 0.51100,
    G_F_MeV: float = 1.1664e-11,
    hbar_MeV_s: float = 6.582119569e-22,
    two_q: float = 2.011,
    n_steps: int = 50_000,
) -> float:
    """Compute beta-decay half-life in seconds.

    t_{1/2} = ln(2) / (rate_base × f(Z,Q) × [2]_q)

    Parameters
    ----------
    Z_daughter : int
        Atomic number of daughter.
    Q_MeV : float
        Q-value in MeV.
    alpha_em, m_e_MeV, G_F_MeV, hbar_MeV_s : float
        Physical constants.
    two_q : float
        Quantum integer [2]_q (from q-deformation).
    n_steps : int
        Integration steps.

    Returns
    -------
    float
        Half-life in seconds. Returns inf if Q ≤ 0.
    """
    f_val = fermi_phase_space(Z_daughter, Q_MeV, alpha_em, m_e_MeV, n_steps)
    if f_val <= 0:
        return float("inf")

    rate_base = G_F_MeV**2 * m_e_MeV**5 / (2 * math.pi**3 * hbar_MeV_s)
    gamma = rate_base * f_val * two_q
    if gamma <= 0:
        return float("inf")

    return math.log(2) / gamma


def batch_phase_space(
    nuclei: list[tuple[int, float]],
    alpha_em: float = 1 / 137.036,
    m_e_MeV: float = 0.51100,
    n_steps: int = 50_000,
) -> list[float]:
    """Compute phase-space integrals for multiple nuclei.

    Parameters
    ----------
    nuclei : list of (Z_daughter, Q_MeV) tuples
    alpha_em, m_e_MeV : float
        Physical constants.
    n_steps : int
        Integration steps per nucleus.

    Returns
    -------
    list of float
        Phase-space values, one per nucleus.
    """
    return [
        fermi_phase_space(Z_d, Q, alpha_em, m_e_MeV, n_steps)
        for Z_d, Q in nuclei
    ]


# ── Self-test ────────────────────────────────────────────────────

if __name__ == "__main__":
    import time

    # Benchmark: vectorized vs loop
    Z_d, Q = 2, 0.01861  # Tritium

    # Vectorized
    t0 = time.monotonic()
    for _ in range(100):
        f_vec = fermi_phase_space(Z_d, Q)
    t_vec = (time.monotonic() - t0) / 100

    # Original loop (for comparison)
    t0 = time.monotonic()
    m_e = 0.51100
    alpha = 1 / 137.036
    W0 = 1.0 + Q / m_e
    dW = (W0 - 1.0) / 50000
    total = 0.0
    for k in range(50000):
        W = 1.0 + (k + 0.5) * dW
        p_e = math.sqrt(W * W - 1)
        beta = p_e / W
        eta = alpha * Z_d / beta
        F = 2 * math.pi * eta / (1 - math.exp(-2 * math.pi * eta)) if abs(eta) > 1e-12 else 1.0
        total += F * p_e * W * (W0 - W) ** 2 * dW
    f_loop = total
    t_loop = time.monotonic() - t0

    print(f"Phase-space integral (³H → ³He, Q={Q} MeV):")
    print(f"  Vectorized: f = {f_vec:.6e}  ({t_vec * 1000:.2f} ms)")
    print(f"  Loop:       f = {f_loop:.6e}  ({t_loop * 1000:.2f} ms)")
    print(f"  Speedup:    {t_loop / t_vec:.0f}x")
    print(f"  Agreement:  {abs(f_vec - f_loop) / f_loop:.2e} relative")

    # All 6 verification nuclei
    print("\nAll 6 nuclei:")
    nuclei = [
        (2, 0.01861, "³H"),
        (7, 0.15648, "¹⁴C"),
        (28, 0.31817, "⁶⁰Co"),
        (39, 0.54590, "⁹⁰Sr"),
        (56, 0.51400, "¹³⁷Cs"),
        (84, 1.16270, "²¹⁰Bi"),
    ]
    for Z_d, Q, name in nuclei:
        f = fermi_phase_space(Z_d, Q)
        t = half_life(Z_d, Q)
        print(f"  {name:>6}: f={f:.4e}, t½={t:.4e} s")
