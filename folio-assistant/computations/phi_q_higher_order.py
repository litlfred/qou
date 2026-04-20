#!/usr/bin/env python3
"""
Higher-order ℏ_q expansion of log Φ_q(v) + matrix-level Φ_q.

Bernoulli expansion from the exact series:

  log Φ_q(v) = Σ_{m≥1} v^m / [m(q^m - 1)]

Using  1/(e^{mℏ} - 1) = 1/(mℏ) · Σ_n B_n (mℏ)^n / n!,  we get

  log Φ_q(v) = (1/ℏ) · Li_2(v)                      [classical]
             + (1/2) · log(1-v)                       [ℏ⁰]
             + (ℏ/12) · v/(1-v)                       [ℏ¹]
             − (ℏ³/720) · v(1+v)/(1-v)³               [ℏ³]
             + (ℏ⁵/30240) · v(1+11v+11v²+v³)/(1-v)⁵   [ℏ⁵]
             − (ℏ⁷/1209600) · ...                      [ℏ⁷]

Odd-power terms vanish by the Bernoulli recurrence (B_{2k+1}=0 for k≥1).

For ℏ = log(q₀) ≈ 0.104, each successive even-order correction is
~ ℏ² ≈ 0.011, so 7 orders brings residual to ~10⁻⁶ = 1 ppm.

EIGENVALUE-LEVEL Φ_q:
Rather than project T_i onto scalar V̂ = χ/dim, evaluate Φ_q on
every eigenvalue of T_i in irrep λ. The Markov trace becomes

  tr_λ(Φ_q(T_i)) = Σ_k Φ_q(eigenvalue_k)

which differs from Φ_q(tr T_i / dim_λ) whenever the irrep is
non-scalar. Captures matrix-level information the scalar formula
collapses.
"""
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0

hbar_log = math.log(q0)


def Li2(x, max_k=2000):
    if x == 1.0: return math.pi**2 / 6
    if x == -1.0: return -math.pi**2 / 12
    if abs(x) < 1:
        s = 0.0
        xk = x
        for k in range(1, max_k+1):
            s += xk / (k*k)
            xk *= x
            if abs(xk/(k*k)) < 1e-20: break
        return s
    if x > 1:
        return -Li2(1.0/x) - math.pi**2/6 - 0.5*math.log(x)**2
    return -Li2(1.0/x) - math.pi**2/3 - 0.5*math.log(-x)**2


# Bernoulli numbers B_0=1, B_1=-1/2, B_2=1/6, B_3=0, B_4=-1/30,
# B_5=0, B_6=1/42, B_7=0, B_8=-1/30, ...
# Only B_{2k} for k≥1 contribute to Faddeev expansion.
B2k = {
    2: 1/6,
    4: -1/30,
    6: 1/42,
    8: -1/30,
    10: 5/66,
    12: -691/2730,
    14: 7/6,
}


def sum_m_p_vm(p: int, v: float, max_m=500) -> float:
    """Closed form for Σ_{m≥1} m^p · v^m (|v|<1)."""
    if p == 0:
        return v / (1 - v)
    if p == 1:
        return v / (1 - v)**2
    if p == 2:
        return v * (1 + v) / (1 - v)**3
    if p == 3:
        return v * (1 + 4*v + v**2) / (1 - v)**4
    if p == 4:
        return v * (1 + 11*v + 11*v**2 + v**3) / (1 - v)**5
    if p == 5:
        return v * (1 + 26*v + 66*v**2 + 26*v**3 + v**4) / (1 - v)**6
    if p == 6:
        return v * (1 + 57*v + 302*v**2 + 302*v**3 + 57*v**4 + v**5) / (1 - v)**7
    # Fallback: direct summation for general p
    s = 0.0
    vm = v
    for m in range(1, max_m+1):
        s += m**p * vm
        vm *= v
        if abs(m**p * vm) < 1e-20: break
    return s


def ln_phi_q_high_order(v: float, max_order: int = 7) -> float:
    """log|Φ_q(v)| via Bernoulli expansion to order ℏ^max_order.

    max_order counts the highest power of ℏ retained. Each even k≥2
    contributes via B_k/k! · ℏ^{k-1} · Σ m^{k-2} v^m.
    """
    if abs(1 - v) < 1e-14: return float('inf')
    # Classical + ℏ⁰ + ℏ¹
    out = Li2(v) / hbar_log + 0.5 * math.log(abs(1 - v))
    if max_order >= 1:
        out += (hbar_log / 12) * v / (1 - v)
    # Higher even orders
    for k in [4, 6, 8, 10, 12, 14]:
        if k - 1 > max_order: break
        if k not in B2k: break
        factor = B2k[k] / math.factorial(k) * hbar_log**(k-1)
        # contribution is factor · Σ m^{k-2} v^m · sign (trace the derivation)
        # From 1/(e^x-1) = 1/x + Σ_{n≥1} B_n x^{n-1}/n!, for n=k even, term is
        # B_k x^{k-1}/k! → in log Φ_q this multiplies Σ v^m/m · (mℏ)^{k-1}/k!·B_k
        #                    = ℏ^{k-1} B_k/k! · Σ m^{k-2} v^m
        out += factor * sum_m_p_vm(k-2, v)
    return out


def phi_q_at_matrix_eigvals(T_matrix: np.ndarray, order: int = 7) -> float:
    """Σ_k Φ_q(eigenvalue_k) — matrix-level Markov trace of Φ_q.

    For a Hecke operator T_i in irrep λ, eigenvalues are q (on sym-
    subspace) and -q⁻¹ (on antisym-subspace); Φ_q evaluated on each.
    Sum gives tr_λ(Φ_q(T_i)).
    """
    eigs = np.linalg.eigvals(T_matrix).real  # Hecke is real diagonal-able
    return sum(math.exp(ln_phi_q_high_order(e, max_order=order))
               for e in eigs if abs(1 - e) > 1e-14)


def ln_phi_q_at_matrix_eigvals(T_matrix: np.ndarray, order: int = 7) -> float:
    """log(Σ_k Φ_q(eigenvalue_k))."""
    eigs = np.linalg.eigvals(T_matrix).real
    log_terms = [ln_phi_q_high_order(e, max_order=order)
                 for e in eigs if abs(1 - e) > 1e-14]
    if not log_terms: return -float('inf')
    m = max(log_terms)
    return m + math.log(sum(math.exp(a - m) for a in log_terms))


if __name__ == "__main__":
    from mass_at_3A_proper import _cached_seminormal

    print("="*80)
    print("HIGHER-ORDER ℏ_q expansion of log Φ_q")
    print("="*80)
    print(f"q₀ = {q0}, ℏ = log q = {hbar_log:.6f}")

    # Compare orders at several v values — Euler is ground truth for |v|<q
    def euler_ln_phi_q(v):
        if abs(v) >= q0: return float('nan')
        s = 0; qi = 1/q0
        for k in range(1, 5000):
            f = 1 - qi**k * v
            s -= math.log(abs(f))
            if abs(qi**k * v) < 1e-18: break
        return s

    print(f"\n{'v':>6}  {'Euler':>12}  {'ord=1':>12}  {'ord=3':>12}  {'ord=5':>12}  {'ord=7':>12}")
    for v in [0.1, 0.3, 0.5, 0.7, 0.9, 1.05]:
        eul = euler_ln_phi_q(v)
        o1 = ln_phi_q_high_order(v, max_order=1)
        o3 = ln_phi_q_high_order(v, max_order=3)
        o5 = ln_phi_q_high_order(v, max_order=5)
        o7 = ln_phi_q_high_order(v, max_order=7)
        e_str = f'{eul:+.6f}' if not math.isnan(eul) else '       n/a'
        print(f"{v:>6.2f}  {e_str:>12}  {o1:+.6f}  {o3:+.6f}  {o5:+.6f}  {o7:+.6f}")

    # Test matrix-level Phi_q vs scalar
    print(f"\nMatrix-level vs scalar Φ_q on H_3 seminormal T_0:")
    for shape in [(3,), (2,1), (1,1,1)]:
        sigmas, dim, _ = _cached_seminormal(shape)
        from scipy.sparse import issparse
        T0 = sigmas[0].toarray() if issparse(sigmas[0]) else sigmas[0]
        V_scalar = np.trace(T0) / dim
        ln_scalar = ln_phi_q_high_order(V_scalar, max_order=7)
        ln_matrix = ln_phi_q_at_matrix_eigvals(T0, order=7)
        print(f"  λ={shape} dim={dim}  V̂_scalar={V_scalar:+.4f}  "
              f"ln|Φ|_scalar={ln_scalar:+.4f}  ln|Φ|_matrix={ln_matrix:+.4f}")
