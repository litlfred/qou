#!/usr/bin/env python3
"""
Jet-level scaling: iterated tower with ℏ_q^{2n} damping per level.

The mass-endomorphism-jet-tower formula writes

    m = m^(0) + Σ_{n=1}^N m^(n)

with level-n contributions bounded by prop:delta-max-uniform-bound:

    |m^(n)| ≤ Δ_max · ℏ_q^{2n}

If the actual contributions sit at a fraction α of the bound
(empirically 'within a factor of 2' for light atoms, from the
paper's numerical scale), the series sums as

    m ≈ m^(0) · Σ_{n=0}^N (α ℏ_q²)^n = m^(0) · (1 − (α ℏ_q²)^{N+1}) / (1 − α ℏ_q²)

with SIGN determined by whether the level-n correction adds or
subtracts.  For the proton level-0 overshoots → jet correction must
subtract, i.e.

    m_p ≈ m^(0) · (1 − α ℏ_q²)    (truncated at level 1)
    m_p ≈ m^(0) · (1 − α ℏ_q²)(1 − β ℏ_q⁴)    (through level 2)

with α, β, ... ratios of actual-to-bound at each level.

We fit α (and β) on the proton CODATA and report:
  - what α is needed to match m_p = 938.272 MeV
  - whether the same α applied to m_n improves or breaks neutron
  - truncation-error prediction at each N

Output: jet-level-geometric-series.witness.json
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
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder


def Phi_q(v, max_iter=2000, tol=1e-16):
    if abs(v) >= float(Q0):
        return float('inf')
    prod = 1.0
    qi_val = float(QI_NUM)
    coef = qi_val
    for k in range(1, max_iter + 1):
        term = 1.0 - coef * v
        if abs(term) < 1e-300:
            return float('inf')
        prod /= term
        if abs(coef * v) < tol:
            break
        coef *= qi_val
    return prod


def tower_level0(V_list, z_val):
    """Level-0 tower: |ΠV| + Σ Φ_q(|V_i|) + z² Σ_{i<j} Φ_q(|V_iV_j|).

    All-pairs form (not adjacent-only), per mass-endomorphism-jet-tower
    §P_n is full set of pairs.
    """
    n = len(V_list)
    abs_V = [abs(v) for v in V_list]
    prod = 1.0
    for v in V_list:
        prod *= v
    prod = abs(prod)
    m = prod + sum(Phi_q(v) for v in abs_V)
    for i in range(n):
        for j in range(i + 1, n):
            m += z_val ** 2 * Phi_q(abs_V[i] * abs_V[j])
    return m


def geometric_jet_series(m0, alpha, hbar_q_sq, N):
    """m^(N) = m^(0) · Σ_{n=0}^N (−α ℏ_q²)^n   (alternating-sign for
    overshooting level 0; replace sign if undershoot)."""
    s = 0.0
    r = 1.0
    for n in range(N + 1):
        s += r
        r *= (-alpha * hbar_q_sq)
    return m0 * s


def main():
    w = WitnessBuilder("jet-level-geometric-series",
                        engine="tower+geometric-series")
    w.set_description(
        "Geometric-series ansatz for the jet-tower expansion: "
        "m_total = m^(0) · Σ (−α ℏ_q²)^n.  Fit α to proton CODATA, "
        "test universality on neutron."
    )

    q = float(Q_NUM)
    h = float(H_A_VAL)
    z_val = float(Z_MARKOV)
    hbar_q_sq_A = ((q - 1) / q) ** 2      # 0.00982
    hbar_q_sq_B = (h / q) ** 2             # 0.03547

    # Level-0 exact
    V_e = vertex_volume([(1.0, 0.0)] * 3)
    Vp0 = vertex_volume(_PROTON_G0)
    Vp1 = vertex_volume(_PROTON_G1)
    Vn0 = vertex_volume(_NEUTRON_G0)
    Vn1 = vertex_volume(_NEUTRON_G1)

    m_e_L0 = abs(V_e) + Phi_q(abs(V_e))
    m_p_L0 = tower_level0([Vp0, Vp1], z_val)
    m_n_L0 = tower_level0([Vn0, Vn1], z_val)

    m_p_L0_MeV = (m_p_L0 / m_e_L0) * M_E_MEV
    m_n_L0_MeV = (m_n_L0 / m_e_L0) * M_E_MEV

    print("=" * 100)
    print("JET-LEVEL GEOMETRIC SERIES + p/n ERROR BREAKDOWN")
    print("=" * 100)
    print(f"  q_0 = {q:.10f}   ℏ_q²(A) = (1−1/q)² = {hbar_q_sq_A:.6f}")
    print(f"                  ℏ_q²(B) = (H_A/q)² = {hbar_q_sq_B:.6f}")
    print(f"                  z = {z_val:.6f}")
    print()
    print(f"  Level-0 predictions:")
    print(f"    m_e^(0) = {m_e_L0:.4f} Hecke = {M_E_MEV:.4f} MeV (reference)")
    print(f"    m_p^(0) = {m_p_L0:.4f} Hecke = {m_p_L0_MeV:.4f} MeV "
          f"(CODATA 938.272, err {(m_p_L0_MeV-M_P_MEV)/M_P_MEV*100:+.3f}%)")
    print(f"    m_n^(0) = {m_n_L0:.4f} Hecke = {m_n_L0_MeV:.4f} MeV "
          f"(CODATA 939.565, err {(m_n_L0_MeV-M_N_MEV)/M_N_MEV*100:+.3f}%)")
    print()

    # ─────────────────────────────────────────────────────────────
    # Fit α to proton CODATA
    # ─────────────────────────────────────────────────────────────
    target_p_frac = M_P_MEV / m_p_L0_MeV
    # target_p_frac = Σ (−α·ℏ_q²)^n → for large N, = 1/(1 + α·ℏ_q²)
    # → α·ℏ_q² = 1/target_p_frac − 1
    alpha_times_h = 1.0 / target_p_frac - 1.0
    alpha_A = alpha_times_h / hbar_q_sq_A
    alpha_B = alpha_times_h / hbar_q_sq_B
    print("=" * 100)
    print("FIT α to proton CODATA (infinite-series limit):")
    print("=" * 100)
    print(f"  m_p / m_p^(0) = 1/(1 + α·ℏ_q²)  →  α·ℏ_q² = {alpha_times_h:.6f}")
    print(f"    if ℏ_q² = ℏ_q²(A) = {hbar_q_sq_A:.6f}  →  α = {alpha_A:.4f}  "
          f"(near [2]_q = {q + 1/q:.4f})")
    print(f"    if ℏ_q² = ℏ_q²(B) = {hbar_q_sq_B:.6f}  →  α = {alpha_B:.4f}")
    print()

    # Test: apply the fitted α to neutron — is α universal?
    print("=" * 100)
    print("TEST universality: apply α = {:.4f} (form A) to m_n".format(alpha_A))
    print("=" * 100)
    m_p_geom_A = m_p_L0_MeV / (1 + alpha_A * hbar_q_sq_A)
    m_n_geom_A = m_n_L0_MeV / (1 + alpha_A * hbar_q_sq_A)
    print(f"  m_p = m_p^(0) / (1 + α·ℏ_q²) = {m_p_geom_A:.4f} MeV "
          f"(err {(m_p_geom_A-M_P_MEV)/M_P_MEV*100:+.3f}% = CODATA by construction)")
    print(f"  m_n = m_n^(0) / (1 + α·ℏ_q²) = {m_n_geom_A:.4f} MeV "
          f"(err {(m_n_geom_A-M_N_MEV)/M_N_MEV*100:+.3f}%)")
    print()

    # ─────────────────────────────────────────────────────────────
    # Truncation table
    # ─────────────────────────────────────────────────────────────
    print("=" * 100)
    print("TRUNCATION BY LEVEL N (proton, α = [2]_q = 2.011)")
    print("=" * 100)
    alpha_use = q + 1/q  # [2]_q as structural candidate
    hbar = hbar_q_sq_A
    print(f"  Using α = [2]_q = {alpha_use:.4f}, ℏ_q²(A) = {hbar:.6f}")
    print()
    print(f"  {'N (levels)':<12} {'m_p (MeV)':>14} {'err':>10} {'ppm':>10}")
    print("  " + "-" * 50)
    rows = []
    for N_trunc in range(0, 8):
        m_pred = geometric_jet_series(m_p_L0_MeV, alpha_use, hbar, N_trunc)
        err = (m_pred - M_P_MEV) / M_P_MEV * 100
        ppm = err * 1e4
        print(f"  N = {N_trunc:<8} {m_pred:>14.6f} {err:>+9.4f}% {ppm:>+9.1f}")
        rows.append({"N": N_trunc, "m_p_pred": m_pred,
                     "err_pct": err, "err_ppm": ppm})

    # ─────────────────────────────────────────────────────────────
    # p/n error breakdown
    # ─────────────────────────────────────────────────────────────
    print()
    print("=" * 100)
    print("p/n ERROR SOURCES (level-0 only)")
    print("=" * 100)
    print()
    print("  PROTON error (+1.83%) decomposition:")
    print(f"    proton g0 chain: {len(_PROTON_G0)} factors →  V̂_0 = {Vp0:+.6f}")
    print(f"    proton g1 chain: {len(_PROTON_G1)} factors →  V̂_1 = {Vp1:+.6f}")
    print(f"    Φ_q(V̂_0) = {Phi_q(abs(Vp0)):.2f} (DOMINANT, 57%)")
    print(f"    Φ_q(V̂_1) = {Phi_q(abs(Vp1)):.2f} (36%)")
    print(f"    z²Φ_q(V̂_0·V̂_1) = {z_val**2 * Phi_q(abs(Vp0*Vp1)):.2f} (7%)")
    print(f"    The +1.83% residual = missing level-≥1 jet contributions")
    print(f"                           = ~17 MeV out of 955 MeV total")
    print()
    print("  NEUTRON error (−55%) decomposition:")
    print(f"    neutron g0 chain: {len(_NEUTRON_G0)} factors →  V̂_0 = {Vn0:+.6f}")
    print(f"    neutron g1 chain: {len(_NEUTRON_G1)} factors →  V̂_1 = {Vn1:+.6f}")
    print(f"    Φ_q(V̂_0) = {Phi_q(abs(Vn0)):.2f} (V̂_0 far from Φ_q pole; 8%)")
    print(f"    Φ_q(V̂_1) = {Phi_q(abs(Vn1)):.2f} (DOMINANT, 91%)")
    print(f"    z²Φ_q(V̂_0·V̂_1) = {z_val**2 * Phi_q(abs(Vn0*Vn1)):.2f} (1%)")
    print(f"    ERROR SOURCE: V̂_0(n) = {Vn0:.4f} is much further from q_0 = {q:.4f}")
    print(f"                   than V̂_0(p) = {Vp0:.4f}; Φ_q growth near pole is")
    print(f"                   extremely sensitive, so neutron gets 18× less T2 weight.")
    print(f"    STRUCTURAL CAUSE: neutron has 2 ud-halves in g0 vs proton's 1.")
    print(f"                       The paper formula as written doesn't account for")
    print(f"                       this asymmetry — the geometric correction α·ℏ_q²")
    print(f"                       (fit from proton) CANNOT close the neutron gap")
    print(f"                       because α·ℏ_q² is ~2% but neutron needs −54%.")

    w.add_data("level_0", {
        "m_e_Hecke": m_e_L0, "m_p_Hecke": m_p_L0, "m_n_Hecke": m_n_L0,
        "m_p_MeV": m_p_L0_MeV, "m_n_MeV": m_n_L0_MeV,
        "V_hat_proton": (Vp0, Vp1),
        "V_hat_neutron": (Vn0, Vn1),
    })
    w.add_data("fit_alpha_from_proton", {
        "alpha_times_hbar_q_sq": alpha_times_h,
        "alpha_A": alpha_A, "alpha_B": alpha_B,
        "twoQ": q + 1/q,  # [2]_q
    })
    w.add_data("geometric_series_p", {
        "m_p_pred_MeV": m_p_geom_A, "by_construction": True,
    })
    w.add_data("geometric_series_n_with_same_alpha", {
        "m_n_pred_MeV": m_n_geom_A,
        "m_n_err_pct": (m_n_geom_A - M_N_MEV) / M_N_MEV * 100,
    })
    w.add_data("truncation_table_alpha_is_two_q", rows)
    w.save()


if __name__ == "__main__":
    main()
