#!/usr/bin/env python3
"""
Isolate the proton and neutron mass error term-by-term.

For each of the two nucleons we have the tower formula

    m_nuc = T_1 + T_2 + T_3 + T_4
         = |V̂_0 V̂_1|
         + Φ_q(|V̂_0|)
         + Φ_q(|V̂_1|)
         + z² · Φ_q(|V̂_0 V̂_1|)

with a geometric-series level-≥1 correction

    m_nuc_corrected = m_nuc^(0) / (1 + α ℏ_q²),   α = [2]_q
                                                        (fitted from proton)

This script walks term by term:

  1. T_1, T_2, T_3, T_4 for (proton, neutron) in Hecke units and MeV
  2. Absolute contributions and percentage-of-total
  3. Asymmetry: (T_i(n) − T_i(p)) per term, isolating which term
     is responsible for the neutron under-prediction
  4. Effect of applying the proton's α to the neutron (shows that
     a universal α cannot close the gap)

Output: p-n-error-isolate.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import (
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    h as H_A_VAL, q0 as Q_NUM, qi as QI_NUM, z as Z_MARKOV,
    vertex_volume,
)
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV, Q_TRITIUM_MEV
from witness_base import WitnessBuilder


def Phi_q(v, max_iter=2000, tol=1e-16):
    if abs(v) >= float(Q0):
        return float('inf')
    prod = 1.0
    qi = float(QI_NUM)
    coef = qi
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * v
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * v) < tol:
            break
        coef *= qi
    return prod


def tower_terms(V0: float, V1: float, z: float) -> dict:
    absV0, absV1 = abs(V0), abs(V1)
    prod = abs(V0 * V1)
    T1 = prod
    T2 = Phi_q(absV0)
    T3 = Phi_q(absV1)
    T4 = z * z * Phi_q(prod)
    return {"T1": T1, "T2": T2, "T3": T3, "T4": T4,
            "sum": T1 + T2 + T3 + T4,
            "V0": V0, "V1": V1, "abs_prod": prod}


def main():
    w = WitnessBuilder("p-n-error-isolate",
                        engine="tower-term-breakdown")
    w.set_description(
        "Term-by-term breakdown of the proton and neutron tower masses, "
        "showing which tower term drives the neutron −55% undershoot "
        "and why a single geometric-series α cannot close it."
    )

    q = float(Q_NUM)
    hbar_q_sq = ((q - 1) / q) ** 2
    two_q = q + 1 / q
    z_val = float(Z_MARKOV)

    # Level-0 inputs
    V_e = vertex_volume([(1.0, 0.0)] * 3)
    m_e_H = abs(V_e) + Phi_q(abs(V_e))

    V0_p = vertex_volume(_PROTON_G0)
    V1_p = vertex_volume(_PROTON_G1)
    V0_n = vertex_volume(_NEUTRON_G0)
    V1_n = vertex_volume(_NEUTRON_G1)

    p = tower_terms(V0_p, V1_p, z_val)
    n = tower_terms(V0_n, V1_n, z_val)

    # Hecke → MeV conversion
    def H2M(x):
        return (x / m_e_H) * M_E_MEV

    print("=" * 100)
    print("PROTON/NEUTRON ERROR ISOLATION — term-by-term")
    print("=" * 100)
    print(f"  q_0 = {q:.10f}   ℏ_q² = (1-1/q)² = {hbar_q_sq:.8f}")
    print(f"  [2]_q = q + 1/q = {two_q:.6f}")
    print(f"  z = {z_val:.6f}   m_e(Hecke) = {m_e_H:.4f}")
    print(f"  m_e = {M_E_MEV} MeV → 1 Hecke = {M_E_MEV/m_e_H:.6e} MeV")
    print()

    # ─────────────────────────────────────────────────────────────
    # Section 1: level-0 V̂_i values
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("SECTION 1: Level-0 per-generator V̂_i^full")
    print("─" * 100)
    print(f"  {'':<8} {'V̂_0':>12} {'V̂_1':>12} {'|V̂_0 V̂_1|':>14}")
    print(f"  {'proton':<8} {V0_p:>+12.6f} {V1_p:>+12.6f} {p['abs_prod']:>14.6f}")
    print(f"  {'neutron':<8} {V0_n:>+12.6f} {V1_n:>+12.6f} {n['abs_prod']:>14.6f}")
    print(f"  {'Δ(n-p)':<8} {V0_n-V0_p:>+12.6f} {V1_n-V1_p:>+12.6f} "
          f"{n['abs_prod']-p['abs_prod']:>+14.6f}")
    print()
    print(f"  Key: V̂_0(p) − V̂_0(n) = {V0_p-V0_n:+.4f}")
    print(f"       V̂_0(p) is close to q_0 = {q:.4f} (pole of Φ_q)")
    print(f"       V̂_0(n) is {q-V0_n:.3f} away from pole → Φ_q suppressed")
    print()

    # ─────────────────────────────────────────────────────────────
    # Section 2: term breakdown side-by-side
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("SECTION 2: Tower terms T_1..T_4 (Hecke units and MeV)")
    print("─" * 100)
    terms = ['T1', 'T2', 'T3', 'T4']
    labels = {
        'T1': '|V̂_0 V̂_1|',
        'T2': 'Φ_q(|V̂_0|)',
        'T3': 'Φ_q(|V̂_1|)',
        'T4': 'z² Φ_q(|V̂_0 V̂_1|)',
    }
    print(f"  {'term':<22} {'proton (Hecke)':>18} {'neutron (Hecke)':>18} "
          f"{'n/p ratio':>12} {'% of m_p':>10} {'% of m_n':>10}")
    print("  " + "-" * 90)
    for t in terms:
        ratio = n[t] / p[t] if p[t] > 1e-30 else float('inf')
        pct_p = p[t] / p['sum'] * 100
        pct_n = n[t] / n['sum'] * 100
        print(f"  {labels[t]:<22} {p[t]:>18.2f} {n[t]:>18.2f} "
              f"{ratio:>12.4f} {pct_p:>9.2f}% {pct_n:>9.2f}%")
    print("  " + "-" * 90)
    print(f"  {'sum (Hecke)':<22} {p['sum']:>18.2f} {n['sum']:>18.2f}")
    m_p_L0 = H2M(p['sum'])
    m_n_L0 = H2M(n['sum'])
    err_p_L0 = (m_p_L0 - M_P_MEV) / M_P_MEV * 100
    err_n_L0 = (m_n_L0 - M_N_MEV) / M_N_MEV * 100
    print(f"  {'sum (MeV)':<22} {m_p_L0:>18.4f} {m_n_L0:>18.4f}")
    print(f"  {'CODATA (MeV)':<22} {M_P_MEV:>18.4f} {M_N_MEV:>18.4f}")
    print(f"  {'err (level-0)':<22} {err_p_L0:>+17.3f}% {err_n_L0:>+17.3f}%")
    print()

    # ─────────────────────────────────────────────────────────────
    # Section 3: which term drives the neutron error?
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("SECTION 3: Which term drives the neutron −55% error?")
    print("─" * 100)
    delta_T = {t: n[t] - p[t] for t in terms}
    delta_sum = sum(delta_T.values())
    print(f"  {'term':<22} {'Δ = n-p (Hecke)':>18} {'Δ (MeV)':>14} "
          f"{'% of total Δ':>14}")
    for t in terms:
        dmev = H2M(delta_T[t])
        pct = delta_T[t] / delta_sum * 100 if abs(delta_sum) > 1e-30 else 0
        print(f"  {labels[t]:<22} {delta_T[t]:>18.2f} {dmev:>+14.2f} "
              f"{pct:>+13.2f}%")
    print("  " + "-" * 70)
    print(f"  {'sum Δ':<22} {delta_sum:>18.2f} {H2M(delta_sum):>+14.2f}")
    print()

    # ─────────────────────────────────────────────────────────────
    # Section 4: geometric-series correction with same α on both
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("SECTION 4: Effect of [2]_q·ℏ_q² geometric-series correction")
    print("─" * 100)
    alpha = two_q
    factor = 1 / (1 + alpha * hbar_q_sq)
    m_p_corr = m_p_L0 * factor
    m_n_corr = m_n_L0 * factor
    err_p_corr = (m_p_corr - M_P_MEV) / M_P_MEV * 100
    err_n_corr = (m_n_corr - M_N_MEV) / M_N_MEV * 100
    print(f"  α = [2]_q = {alpha:.4f}, ℏ_q² = {hbar_q_sq:.6f}")
    print(f"  correction factor = 1/(1 + α·ℏ_q²) = {factor:.6f}")
    print()
    print(f"  {'nucleon':<10} {'pred^(0)':>12} {'corrected':>12} {'CODATA':>12} "
          f"{'err^(0)':>10} {'err corrected':>14}")
    print(f"  {'-'*75}")
    print(f"  {'p':<10} {m_p_L0:>12.4f} {m_p_corr:>12.4f} {M_P_MEV:>12.4f} "
          f"{err_p_L0:>+9.3f}% {err_p_corr:>+13.3f}%")
    print(f"  {'n':<10} {m_n_L0:>12.4f} {m_n_corr:>12.4f} {M_N_MEV:>12.4f} "
          f"{err_n_L0:>+9.3f}% {err_n_corr:>+13.3f}%")
    print()
    print("  Conclusion: the same α reduces proton error from +1.8% → -0.14%")
    print("  but the neutron stays at ~-56% because the asymmetry lives in")
    print("  T2 = Φ_q(|V̂_0|), not in a missing level-≥1 correction.")
    print()

    # ─────────────────────────────────────────────────────────────
    # Section 5: structural cause of T_2 asymmetry
    # ─────────────────────────────────────────────────────────────
    print("─" * 100)
    print("SECTION 5: Structural cause of T_2 asymmetry")
    print("─" * 100)
    print("  Proton g0 chain (7 factors):  [B_3: 3 σ] + [uu pair: 1 σ] + "
          "[ud pair: 1 ud-half] + [2 gluon σ]")
    print(f"    → {len(_PROTON_G0)} factors, 6 σ + 1 ud-half, V̂_0 = {V0_p:+.4f}")
    print("  Neutron g0 chain (7 factors): [B_3: 3 σ] + "
          "[ud pair: 1 ud-half] + [ud pair: 1 ud-half] + [2 gluon σ]")
    print(f"    → {len(_NEUTRON_G0)} factors, 5 σ + 2 ud-halves, V̂_0 = {V0_n:+.4f}")
    print()
    print("  The extra ud-half in neutron's g0 (2 vs proton's 1) shifts V̂_0")
    print("  away from the q_0 = 1.110 pole of Φ_q.  Φ_q rises steeply near")
    print("  the pole, so this 0.135 shift in V̂_0 drops Φ_q(|V̂_0|) by factor 19×")
    print("  (671,221 → 36,048), accounting for the bulk of the neutron gap.")
    print()
    print("  Closing the neutron error from -55% requires NEW physics:")
    print("    (a) α that depends on V̂_0 (breaking the proton-only fit), OR")
    print("    (b) a different tower formula for neutrons, OR")
    print("    (c) a jet-prolongation V̂_i^(n) that compensates via level ≥ 1.")

    # Save everything
    w.add_data("level_0", {
        "V_e": V_e, "m_e_Hecke": m_e_H,
        "proton": {"V0": V0_p, "V1": V1_p, "tower": p,
                   "m_MeV": m_p_L0, "err_pct": err_p_L0},
        "neutron": {"V0": V0_n, "V1": V1_n, "tower": n,
                     "m_MeV": m_n_L0, "err_pct": err_n_L0},
    })
    w.add_data("per_term_asymmetry", {
        labels[t]: {"p_Hecke": p[t], "n_Hecke": n[t],
                    "delta_Hecke": delta_T[t],
                    "delta_MeV": H2M(delta_T[t])}
        for t in terms
    })
    w.add_data("geometric_series_correction", {
        "alpha": alpha, "hbar_q_sq": hbar_q_sq, "factor": factor,
        "m_p_L0": m_p_L0, "m_p_corrected": m_p_corr, "m_p_err_pct": err_p_corr,
        "m_n_L0": m_n_L0, "m_n_corrected": m_n_corr, "m_n_err_pct": err_n_corr,
    })
    w.save()


if __name__ == "__main__":
    main()
