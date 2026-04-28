#!/usr/bin/env python3
"""
Jet-prolonged Hecke rep + residual structure search.

Target: m_p^(0) tower = 955.49 MeV vs CODATA 938.27 MeV.
        Required correction Δ = −17.22 MeV = −1.802% of m_p^(0).

Two approaches:

(A) Implement V̂_i^(1) via Jucys–Murphy jet prolongation.
    The recursive brane tower A_{n+1} = A_n ⊗ Ω¹(A_n) has Hecke-algebra
    realisation where Ω¹ is spanned by Jucys–Murphy elements L_k that
    commute with H_{n-1}(q) and encode jet-direction information.
    We compute V̂_i^(1) = V̂_i^(0) acting through L_k-conjugated braid
    factors to get the level-1 contribution explicitly.

(B) Residual-structure search over candidate formulas.
    Test whether −1.80% = f(q_0) for any natural f drawn from the
    framework: ℏ_q², H_A, z, V̂_0, V̂_1, [k]_q, etc.  Report best fits.

Output: jet-level-1-and-residual-search.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np

from hecke_core import (
    _PROTON_G0, _PROTON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    W_SYM, W_STD, W_ALT, vertex_volume,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV
from witness_base import WitnessBuilder


def Phi_q(z: float, max_iter: int = 2000, tol: float = 1e-16) -> float:
    if abs(z) >= float(Q0):
        return float('inf')
    prod = 1.0
    qi_val = float(QI_NUM)
    coef = qi_val
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * z
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * z) < tol:
            break
        coef *= qi_val
    return prod


def q_int(k: int, q: float) -> float:
    """[k]_q = (q^k − q^{-k})/(q − q^{-1})."""
    if k == 0:
        return 0.0
    qi = 1.0 / q
    return (q ** k - qi ** k) / (q - qi)


def level0_tower(V0: float, V1: float) -> float:
    absV0, absV1 = abs(V0), abs(V1)
    prodV = abs(V0 * V1)
    return (prodV + Phi_q(absV0) + Phi_q(absV1)
             + float(Z_MARKOV) ** 2 * Phi_q(prodV))


def jucys_murphy_prolonged_vhat(chain, k_index: int) -> float:
    """V̂_i^(1) via Jucys–Murphy-style prolongation: conjugate each factor
    by the k-th JM element, recompute vertex_volume.

    Approximation: at the sym/alt block level, L_k acts as scalar q^{-ct}
    with content ct depending on position.  Here we pick a phenomenological
    ansatz: multiply (c, d) in the chain by q^{ct_k} for a fixed content.

    NOT a full categorical brane-tower prolongation — but captures the
    L_k-shift structure and gives a SIGN-CORRECT estimate.
    """
    q = float(Q_NUM)
    # Content of position k (Young-diagram diagonal): use k itself for proton
    ct = k_index
    phase = q ** ct
    new_chain = [(c * phase, d * phase) for c, d in chain]
    return vertex_volume(new_chain)


def full_jet_level1_correction(chain_g0, chain_g1):
    """Compute a candidate level-1 correction as (V̂^(1) − V̂^(0)) · level-0.

    Uses JM-prolonged V̂'s and subtracts level-0.  Sign depends on whether
    the shift increases or decreases V̂ toward the Φ_q pole.
    """
    V0_lvl0 = vertex_volume(chain_g0)
    V1_lvl0 = vertex_volume(chain_g1)
    m_lvl0 = level0_tower(V0_lvl0, V1_lvl0)

    # Try different content indices for gen 0 and gen 1
    best = None
    for ct0 in [-2, -1, 0, 1, 2]:
        for ct1 in [-2, -1, 0, 1, 2]:
            V0_1 = jucys_murphy_prolonged_vhat(chain_g0, ct0)
            V1_1 = jucys_murphy_prolonged_vhat(chain_g1, ct1)
            if abs(V0_1) >= float(Q_NUM) or abs(V1_1) >= float(Q_NUM):
                continue
            m_1 = level0_tower(V0_1, V1_1)
            delta_frac = (m_1 - m_lvl0) / m_lvl0
            entry = {"ct0": ct0, "ct1": ct1,
                     "V0_1": V0_1, "V1_1": V1_1,
                     "m_1": m_1, "delta_frac_pct": delta_frac * 100}
            if best is None or abs(delta_frac + 0.0180) < abs(best["delta_frac_pct"]/100 + 0.0180):
                best = entry
    return m_lvl0, best


def main():
    w = WitnessBuilder("jet-level-1-and-residual-search",
                        engine="JM-prolongation + residual-search")
    w.set_description(
        "Two-pronged: (A) JM-prolonged V̂^(1) attempt for proton level-1 "
        "correction; (B) residual-structure search over candidate "
        "closed-form expressions in (q, H_A, z, V̂_i) matching the "
        "required −1.802% correction on m_p^(0) = 955.49 MeV."
    )
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("H_A", float(H_A_VAL))
    w.add_parameter("z_markov", float(Z_MARKOV))

    q = float(Q_NUM)
    qi = float(QI_NUM)
    h = float(H_A_VAL)
    z = float(Z_MARKOV)

    # Level-0 baseline
    V_e = vertex_volume([(1.0, 0.0)] * 3)
    V0_p = vertex_volume(_PROTON_G0)
    V1_p = vertex_volume(_PROTON_G1)
    m_e_Hecke = abs(V_e) + Phi_q(abs(V_e))
    m_p_Hecke_lvl0 = level0_tower(V0_p, V1_p)
    m_p_MeV_lvl0 = (m_p_Hecke_lvl0 / m_e_Hecke) * M_E_MEV
    required_delta_frac = (M_P_MEV - m_p_MeV_lvl0) / m_p_MeV_lvl0
    required_delta_pct = required_delta_frac * 100

    print("=" * 100)
    print("JET-LEVEL-1 + RESIDUAL STRUCTURE SEARCH")
    print("=" * 100)
    print(f"  m_p^(0) level-0 tower = {m_p_MeV_lvl0:.4f} MeV "
          f"(err +{(m_p_MeV_lvl0-M_P_MEV)/M_P_MEV*100:.3f}%)")
    print(f"  Required correction Δ = {required_delta_pct:+.4f}% = {M_P_MEV - m_p_MeV_lvl0:+.4f} MeV")
    print()

    # ═══════════════════════════════════════════════════════════════
    # (A) JM-prolonged V̂^(1) attempt
    # ═══════════════════════════════════════════════════════════════
    print("─" * 100)
    print("(A) Jucys–Murphy prolongation search")
    print("─" * 100)
    _, best_JM = full_jet_level1_correction(_PROTON_G0, _PROTON_G1)
    print(f"  Best content (ct0, ct1) = ({best_JM['ct0']}, {best_JM['ct1']})")
    print(f"    V̂_0^(1) = {best_JM['V0_1']:+.6f} "
          f"(V̂_0^(0) = {V0_p:+.6f})")
    print(f"    V̂_1^(1) = {best_JM['V1_1']:+.6f} "
          f"(V̂_1^(0) = {V1_p:+.6f})")
    print(f"    m^(1) Hecke  = {best_JM['m_1']:.2f}  "
          f"(level-0: {m_p_Hecke_lvl0:.2f})")
    print(f"    Δ = (m^(1) − m^(0))/m^(0) = {best_JM['delta_frac_pct']:+.4f}%")
    print(f"    Target: {required_delta_pct:+.4f}%")
    print(f"    Match : {'✓ close' if abs(best_JM['delta_frac_pct']-required_delta_pct) < 0.2 else '✗ diverges'}")
    print()

    # ═══════════════════════════════════════════════════════════════
    # (B) Residual structure search
    # ═══════════════════════════════════════════════════════════════
    print("─" * 100)
    print("(B) Residual-structure search — candidate closed forms")
    print("─" * 100)

    hbar_q_A = ((q - 1) / q) ** 2
    hbar_q_B = (h / q) ** 2
    candidates = [
        ("ℏ_q² form A = (1−1/q)²",          hbar_q_A),
        ("ℏ_q² form B = (H_A/q)²",          hbar_q_B),
        ("H_A²/4",                           h * h / 4),
        ("H_A²/2",                           h * h / 2),
        ("H_A²",                             h * h),
        ("(q−1)²",                           (q - 1) ** 2),
        ("(q−1)²/q",                         (q - 1) ** 2 / q),
        ("z²",                               z * z),
        ("z² · ℏ_q²(A)",                     z * z * hbar_q_A),
        ("2 · ℏ_q²(A)",                      2 * hbar_q_A),
        ("3 · ℏ_q²(A)",                      3 * hbar_q_A),
        ("ℏ_q²(A) + ℏ_q²(B)",                hbar_q_A + hbar_q_B),
        ("(1 + z²) · ℏ_q²(A)",               (1 + z * z) * hbar_q_A),
        ("[2]_q · ℏ_q²(A)",                  (q + qi) * hbar_q_A),
        ("|V̂_0 V̂_1| · ℏ_q²(A)",            abs(V0_p * V1_p) * hbar_q_A),
        ("log(1 + H_A²/4)",                  math.log(1 + h * h / 4)),
        ("2 log(1 + H_A²/4)",                2 * math.log(1 + h * h / 4)),
        ("(1 − |V̂_0 V̂_1|) / 1",             1 - abs(V0_p * V1_p)),
        ("(1 − |V̂_0|)",                     1 - abs(V0_p)),
        ("(1 − |V̂_1|)",                     1 - abs(V1_p)),
        ("(1 − |V̂_0|)(1 − |V̂_1|)",         (1 - abs(V0_p)) * (1 - abs(V1_p))),
        ("ℏ_q²(A) / (1 − |V̂_0 V̂_1|)",      hbar_q_A / (1 - abs(V0_p * V1_p))),
    ]

    target = abs(required_delta_frac)
    print(f"  target |Δ/m_p^(0)| = {target*100:.4f}%")
    print(f"  {'formula':<38} {'value':>14} {'|Δ−f|%':>10} {'ratio f/Δ':>10}")
    print(f"  {'-'*76}")
    scored = []
    for name, val in candidates:
        ratio = val / target if target > 0 else 0.0
        err_pct = abs(val - target) * 100
        scored.append({"name": name, "value": val,
                        "target_match_err_pct": err_pct, "ratio": ratio})
        print(f"  {name:<38} {val:>14.6f} {err_pct:>9.4f}% {ratio:>9.4f}")

    # Best matches
    scored.sort(key=lambda r: r["target_match_err_pct"])
    print()
    print("  TOP 5 BEST MATCHES to target −1.802%:")
    for r in scored[:5]:
        print(f"    {r['name']:<38} {r['value']:>12.6f}  "
              f"(ratio f/target = {r['ratio']:.4f})")
    print()

    # Test: apply each candidate as a multiplicative correction
    print("  Test as multiplicative correction m_p^(0) · (1 − f):")
    print(f"  {'formula':<38} {'m_p corrected':>14} {'err%':>8} {'ppm':>8}")
    print(f"  {'-'*78}")
    for r in scored[:8]:
        m_corr = m_p_MeV_lvl0 * (1 - r["value"])
        err = (m_corr - M_P_MEV) / M_P_MEV * 100
        ppm = err * 1e4
        print(f"  {r['name']:<38} {m_corr:>14.4f} {err:>+7.3f}% {ppm:>+7.1f}")
    print()

    # Test additive correction m_p^(0) − α · f · m_p^(0)  with α ∈ {0.5, 1, 2}
    print("  Test: m_p = m_p^(0) · (1 − α·f) for α ∈ {0.5, 1, 2} on top-1 candidate:")
    top = scored[0]
    for alpha in [0.5, 1.0, 2.0]:
        m_corr = m_p_MeV_lvl0 * (1 - alpha * top["value"])
        err = (m_corr - M_P_MEV) / M_P_MEV * 100
        print(f"    α={alpha}  m_p = {m_corr:.4f}  err = {err:+.3f}%")

    w.add_data("level0", {
        "V0_proton": V0_p, "V1_proton": V1_p,
        "m_p_Hecke": m_p_Hecke_lvl0, "m_p_MeV": m_p_MeV_lvl0,
        "required_delta_frac_pct": required_delta_pct,
    })
    w.add_data("JM_prolongation_best", best_JM)
    w.add_data("residual_candidates", scored)
    w.save()


if __name__ == "__main__":
    main()
