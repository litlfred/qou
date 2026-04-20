#!/usr/bin/env python3
"""
Pentagon R-factor ascension between confinement levels.

Per [pentagon-ascension-bound](#prop:pentagon-ascension-bound) the
pentagon identity (Faddeev-Kashaev) lifts per-generator V̂ values
from one confinement level to the next:

    R(u, v) = Φ_q(uv) / (Φ_q(u) · Φ_q(v))

If pentagon operates (û·v̂ = q²·v̂·û), R = 1 and V̂ ascends trivially.
Otherwise R carries an O(ℏ_q²) correction that must be propagated.

Multi-level structure:

    quark   ──[R_quark]──>   hadron   ──[R_hadron]──>   nucleus   ──[R_nucleus]──>   atom
    (H_3)                    (per-nucleon V̂)           (per-atom V̂)                (observables)

At each level k:
    V̂^{(k+1)}_i = V̂^{(k)}_i · ∏_{j} R(V̂^{(k)}_i, V̂^{(k)}_j)

The R-factor is log-multiplicative: log|V̂^{(k+1)}| = log|V̂^{(k)}| + Σ_j log|R|.

For the nuclear binding formula B = Σ_λ w_λ m_e ln|Φ_q(V̂^λ)|, pentagon
ascension means that V̂^λ at the nuclear level already includes the
quark-level and hadron-level R-factor corrections.

This module provides:
  R_factor(u, v)       — pentagon R-factor (log form)
  pentagon_ascend(V_list) — ascend list of V̂ by one level
  multi_level_trace(words_per_level, n_strands_per_level)
                       — compute effective V̂ after full ascension chain
"""
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0

z = 1/(math.sqrt(q0) + 1/math.sqrt(q0))
hbar_log = math.log(q0)


def Li2(x, max_k=2000):
    """Real dilogarithm via series + reflection for |x|>1."""
    if x == 1.0: return math.pi**2 / 6
    if x == -1.0: return -math.pi**2 / 12
    if abs(x) < 1:
        s = 0.0
        xk = x
        for k in range(1, max_k+1):
            s += xk / (k*k)
            xk *= x
            if abs(xk/(k*k)) < 1e-18: break
        return s
    if x > 1:
        return -Li2(1.0/x) - math.pi**2/6 - 0.5*math.log(x)**2
    return -Li2(1.0/x) - math.pi**2/3 - 0.5*math.log(-x)**2


def ln_phi_q(v, order=2):
    """log|Φ_q(v)| via Faddeev expansion in ℏ = log q.

      log Φ_q(v) = Li_2(v)/ℏ + ½ log|1-v| + (ℏ/12)·v/(1-v) + O(ℏ³)
    """
    if abs(1 - v) < 1e-14: return float('inf')
    out = Li2(v) / hbar_log + 0.5 * math.log(abs(1 - v))
    if order >= 2:
        out += (hbar_log / 12) * v / (1 - v)
    return out


def ln_R_factor(u: float, v: float) -> float:
    """log|R(u,v)| = log|Φ_q(uv)| - log|Φ_q(u)| - log|Φ_q(v)|.

    At leading order in ℏ_q (pentagon operational):
        R ≈ 1 + ½ · ℏ_q² · (uv log ...)    [O(ℏ²) correction]
    so log|R| ≈ 0.

    At sub-leading order the R-factor carries non-trivial corrections
    that must ascend between levels.
    """
    return ln_phi_q(u*v) - ln_phi_q(u) - ln_phi_q(v)


def pentagon_ascend(V_list: list[float]) -> list[float]:
    """Ascend V̂ values from level k to level k+1 via pentagon R-factor.

    For each i: log|V̂^{(k+1)}_i| = log|V̂^{(k)}_i| + Σ_{j≠i} z² log|R(V̂_i, V̂_j)|

    Factor of z² is the Markov weight of the pair crossing at this level.
    """
    n = len(V_list)
    V_next = []
    for i, vi in enumerate(V_list):
        if abs(vi) < 1e-300:
            V_next.append(0.0); continue
        log_abs_vi = math.log(abs(vi))
        sign_vi = 1.0 if vi >= 0 else -1.0
        # Sum pentagon R-factor corrections from all pair partners
        log_correction = 0.0
        for j, vj in enumerate(V_list):
            if j == i: continue
            log_correction += (z**2) * ln_R_factor(abs(vi), abs(vj))
        log_abs_next = log_abs_vi + log_correction
        V_next.append(sign_vi * math.exp(log_abs_next) if log_abs_next < 700 else sign_vi * float('inf'))
    return V_next


def ascension_residual_ppm(V_list: list[float]) -> float:
    """Measure the magnitude of pentagon correction on level-ascent.

    Returns mean |ΔlogV̂ / logV̂| in ppm across all entries.
    If pentagon operates perfectly (R=1), residual → 0.
    """
    V_after = pentagon_ascend(V_list)
    if not V_list: return 0.0
    devs = []
    for v, va in zip(V_list, V_after):
        if abs(v) < 1e-300: continue
        d = abs(math.log(abs(va)/abs(v))) if abs(va) > 0 else 0.0
        devs.append(d / abs(math.log(abs(v))) if abs(math.log(abs(v))) > 1e-10 else d)
    return float(np.mean(devs)) * 1e6 if devs else 0.0


def hbar_orders_needed_for_ppm(v: float, target_ppm: float = 1.0) -> int:
    """How many orders of ℏ_q expansion are needed for target precision?

    For ℏ_q ≈ 0.1, order n suffices if ℏ_q^n < target_ppm/1e6.
    target_ppm=1 → ℏ_q^n < 1e-6 → n > 6·log(10)/log(1/ℏ_q) ≈ 6.
    """
    hbar_q = (q0 - 1) / q0
    n = 1
    ratio = 1.0
    while ratio > target_ppm / 1e6 and n < 20:
        ratio *= hbar_q
        n += 1
    return n


if __name__ == "__main__":
    print("="*80)
    print("Pentagon ascension infrastructure — self-test")
    print("="*80)
    print(f"q₀ = {q0:.6f}")
    print(f"ℏ = log(q) = {hbar_log:.6f}")
    print(f"ℏ_q = (q-1)/q = {(q0-1)/q0:.6f}")
    print(f"z = 1/(√q + 1/√q) = {z:.6f}")
    print(f"z² = {z**2:.6f}")

    # ℏ_q orders needed for 1 ppm
    n_orders = hbar_orders_needed_for_ppm(0.5, 1.0)
    print(f"\nℏ_q expansion orders needed for 1 ppm: {n_orders}")

    # Test R-factor on commuting case (pentagon fully operational)
    print(f"\nR-factor tests:")
    for u, v in [(0.3, 0.4), (0.5, 0.5), (0.8, 0.2), (0.1, 0.9)]:
        r = ln_R_factor(u, v)
        print(f"  u={u}, v={v}:  log|R| = {r:+.6e}")

    # Test ascension on a 3-quark V̂ list (proton-like)
    print(f"\nPentagon ascension of [0.3, 0.4, 0.5] (3-quark analog):")
    V_pre = [0.3, 0.4, 0.5]
    V_post = pentagon_ascend(V_pre)
    for v_pre, v_post in zip(V_pre, V_post):
        delta_ppm = (v_post - v_pre)/v_pre * 1e6
        print(f"  {v_pre:.4f} → {v_post:.6f}  (Δ = {delta_ppm:+.1f} ppm)")

    # Verify: if R ≈ 1 (pentagon operational) the ascension is trivial
    residual = ascension_residual_ppm(V_pre)
    print(f"\nMean ascension residual: {residual:.1f} ppm")
    if residual < 100:
        print("  [PASS] Pentagon ≈ operational — R-factor is small")
    else:
        print("  [FAIL] Pentagon not operational — large R-factor correction")
