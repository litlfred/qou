#!/usr/bin/env python3
"""
Explore tower residuals for proton and neutron at high precision.

Baseline (proton_mass_tower_derivation.py):
  m_p_level0 = 955.4917 MeV (tower with pair term z²·Φ_q(V̂_0·V̂_1))
  m_p_corrected = m_p_level0 / (1 + [2]_q · ℏ_q²) = 936.99 MeV
  CODATA m_p = 938.27 MeV  →  residual R_p = m_p / m_p_corrected = 1.001369

  m_n_predicted = m_p + Q_β(³H) + m_e = 937.52 MeV
  CODATA m_n = 939.565 MeV  →  residual R_n = 1.002180

Probe 1: scan for simple q-algebraic forms matching R_p, R_n.
Probe 2: compute volume of braid-closure COMPLEMENT (alternative
         S³-manifold candidates; Dehn fillings, double covers, etc.)
Probe 3: try Jones-Ocneanu Markov weights (z = 1/(q^½+q^⁻½) per
         crossing) instead of Plancherel d_q²/[n]_q! — does this shift
         V̂_0, V̂_1 such that m_p residual closes?
"""
from __future__ import annotations

import sys
import json
import itertools
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 50

from q_parameter import (
    Q as Q0_FLOAT, VOL_FIGURE_EIGHT, MASS_RATIO_MU_E,
    Q_MP, Q_INV_MP, vol_4_1_at,
)
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

# Use HP globals from q_parameter directly.  Previously this script
# went `mp.mpf(str(Q0_FLOAT))`, taking the f64 q (~16 dps), turning
# it back into mpmath, and computing everything downstream at
# f64 dressed up as 50 dps — past digit 16 it was trailing noise.
Q0 = Q_MP
QI = Q_INV_MP


def q_int(k):
    return (Q0**k - QI**k) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


HA = Q0 - QI
HBAR_Q = (Q0 - mp.mpf(1)) / Q0         # ℏ_q = (q−1)/q
HBAR_Q_SQ = HBAR_Q * HBAR_Q
B2 = Q0 + QI                            # [2]_q
B3 = Q0**2 + 1 + QI**2                  # [3]_q

# Current residual values (tower formula vs CODATA)
M_P_TOWER_CORRECTED = mp.mpf("936.99424")    # tower·1/(1+[2]_q·ℏ_q²)
M_N_TOWER_VIA_Qbeta = mp.mpf("937.52349")    # m_p+Q_β+m_e

R_P = mp.mpf(str(M_P_MEV)) / M_P_TOWER_CORRECTED
R_N = mp.mpf(str(M_N_MEV)) / M_N_TOWER_VIA_Qbeta


def probe_algebraic_forms():
    """Scan candidate closed-forms in (q, ℏ_q, [2]_q, [3]_q, H_A, …)
    that might match R_p and R_n at 1-ppm precision."""
    print("=" * 100)
    print("PROBE 1 — algebraic forms for tower residuals")
    print("=" * 100)
    print(f"  R_p = m_p_codata / m_p_tower_corrected = {mp.nstr(R_P, 20)}")
    print(f"  R_n = m_n_codata / m_n_Qbeta_predicted = {mp.nstr(R_N, 20)}")
    print(f"  Δ_p = R_p - 1 = {float(R_P - 1):+.10f}  ≈ 1.37e-3")
    print(f"  Δ_n = R_n - 1 = {float(R_N - 1):+.10f}  ≈ 2.18e-3")
    print()

    candidates = [
        ("1 + ℏ_q⁴",                  1 + HBAR_Q_SQ**2),
        ("1 + ℏ_q² · ℏ_q²·[2]_q",     1 + HBAR_Q_SQ * HBAR_Q_SQ * B2),
        ("1 + ℏ_q² / [2]_q",          1 + HBAR_Q_SQ / B2),
        ("1 + ℏ_q² · [2]_q / [3]_q",  1 + HBAR_Q_SQ * B2 / B3),
        ("1 + H_A²/10",               1 + HA*HA/10),
        ("1 + H_A² · ℏ_q²",           1 + HA*HA * HBAR_Q_SQ),
        ("1/(1 - ℏ_q²·[2]_q/10)",     1/(1 - HBAR_Q_SQ * B2 / 10)),
        ("1/(1 - ℏ_q⁴ · 15)",         1/(1 - HBAR_Q_SQ**2 * 15)),
        ("(1+ℏ_q²)·(1+[2]_q·ℏ_q²)/((1+[2]_q·ℏ_q²)²)",
         (1+HBAR_Q_SQ)*(1+B2*HBAR_Q_SQ)/((1+B2*HBAR_Q_SQ)**2)),
        ("(1+[2]_q·ℏ_q⁴)",             1 + B2 * HBAR_Q_SQ**2),
        ("(1+[3]_q·ℏ_q⁴)",             1 + B3 * HBAR_Q_SQ**2),
        ("1 + [2]_q²·ℏ_q⁴",            1 + B2*B2 * HBAR_Q_SQ**2),
        ("ℏ_q" ,                        HBAR_Q),
    ]
    print(f"  {'expression':<42} {'value':>20} {'rel err to R_p':>17} "
          f"{'rel err to R_n':>17}")
    best_p = None; best_n = None
    for name, val in candidates:
        err_p = abs(float(val) - float(R_P))/float(R_P)
        err_n = abs(float(val) - float(R_N))/float(R_N)
        print(f"  {name:<42} {float(val):>20.10f} {err_p:>17.3e} {err_n:>17.3e}")
        if best_p is None or err_p < best_p[0]:
            best_p = (err_p, name, val)
        if best_n is None or err_n < best_n[0]:
            best_n = (err_n, name, val)
    print()
    print(f"  Best R_p match: {best_p[1]:<40} err {best_p[0]:.3e}")
    print(f"  Best R_n match: {best_n[1]:<40} err {best_n[0]:.3e}")
    return candidates, best_p, best_n


def probe_volumes():
    """Look at q-rational multiples of Vol(4_1) as candidate residual
    contributors.  These are the hyperbolic volumes of Dehn fillings
    or related manifolds."""
    print()
    print("=" * 100)
    print("PROBE 2 — rational-of-V(4_1) contributions")
    print("=" * 100)
    V_fig8 = vol_4_1_at(50)
    print(f"  Vol(4_1) = V_fig8 = {mp.nstr(V_fig8, 25)}")
    print(f"  ℏ_q² = V_fig8 / m_μ/m_e = {mp.nstr(HBAR_Q_SQ, 20)}")
    print()
    # Residual of m_p as a fraction of total mass:
    # Δm_p = m_p - m_p_corrected ≈ 1.28 MeV.
    # As a fraction of m_e: Δm_p/m_e = 2.50
    # Check: is 2.50 ≈ V_fig8 / something?
    dmp = mp.mpf(str(M_P_MEV)) - M_P_TOWER_CORRECTED
    dmn = mp.mpf(str(M_N_MEV)) - M_N_TOWER_VIA_Qbeta
    me = mp.mpf(str(M_E_MEV))
    print(f"  Δm_p = {mp.nstr(dmp, 15)} MeV   /m_e = {float(dmp/me):.6f}")
    print(f"  Δm_n = {mp.nstr(dmn, 15)} MeV   /m_e = {float(dmn/me):.6f}")
    print()
    print("  Check Δ/m_e against vol-based expressions:")
    for name, expr in [
        ("V_fig8",                V_fig8),
        ("V_fig8 / [2]_q",        V_fig8 / B2),
        ("V_fig8 / [3]_q",        V_fig8 / B3),
        ("V_fig8 · [2]_q",        V_fig8 * B2),
        ("V_fig8 / m_μ/m_e",      HBAR_Q_SQ),  # = ℏ_q² by definition
        ("V_fig8 / π",            V_fig8 / mp.pi),
        ("2·ℏ_q²·m_μ/m_e",         2*V_fig8),
        ("V_fig8 · (q−1)",        V_fig8 * (Q0-1)),
    ]:
        print(f"    {name:<26} = {float(expr):>14.6f}   "
              f"Δm_p/m_e ratio = {float(dmp/me/expr):.4f}   "
              f"Δm_n/m_e ratio = {float(dmn/me/expr):.4f}")


def probe_jones_ocneanu_weights():
    """Switch Plancherel weights d_q²/[n]_q! → Jones-Ocneanu weights
    z = 1/(q^½+q^⁻½) per crossing.  Check how this shifts the
    per-generator V̂_i values and whether the residual closes."""
    print()
    print("=" * 100)
    print("PROBE 3 — Jones-Ocneanu Markov weights")
    print("=" * 100)
    z_JO = mp.mpf(1) / (mp.sqrt(Q0) + mp.sqrt(QI))
    print(f"  z_JO = 1/(q^½+q^⁻½) = {mp.nstr(z_JO, 20)}")
    print(f"  1/z_JO = {mp.nstr(1/z_JO, 20)}")
    print(f"  z_JO²  = {mp.nstr(z_JO*z_JO, 20)}")
    print()

    # Plancherel w_sym = 1/[3]_q!, w_std = [2]_q²/[3]_q!, w_alt = 1/[3]_q!
    nfac = q_fact(3)
    w_sym_P = mp.mpf(1)/nfac
    w_std_P = B2*B2/nfac
    w_alt_P = mp.mpf(1)/nfac
    # Plancherel sum: w_sym + w_std + w_alt = (1 + [2]_q² + 1)/[3]_q!
    S_P = w_sym_P + w_std_P + w_alt_P
    print(f"  Plancherel sum = (2 + [2]_q²)/[3]_q! = {float(S_P):.10f}")
    print(f"  (should be 1; deviates at q ≠ 1 by {float(S_P-1)*100:+.3f}%)")
    print()

    # Jones-Ocneanu analogues.  For H_3(q), Markov weight decomposition
    # is w_λ^JO = (path count of adding boxes in shape λ) · z^boxes
    # For n=3: sym has path 1 → 2 → 3 (product of corresponding z's),
    # alt has path 1 → 1,1 → 1,1,1.  Std (2,1) is: 1 → 2 → 2,1 or 1 → 1,1 → 2,1.
    # Formally: w_λ^JO = d_λ(classical) · z^(n-1) · (sum over paths of q-factors)
    # The simplest consistent formula: w_λ^JO = z^n · dim_q(λ)
    # (Jones-Ocneanu Markov trace with z-weighted crossings).
    w_sym_JO = z_JO**3 * mp.mpf(1)      # d_q(sym) = 1
    w_std_JO = z_JO**3 * B2              # d_q((2,1)) = [2]_q
    w_alt_JO = z_JO**3 * mp.mpf(1)      # d_q(alt) = 1
    S_JO = w_sym_JO + w_std_JO + w_alt_JO
    print(f"  JO w_sym = z³·d_q(sym) = {float(w_sym_JO):.10f}")
    print(f"  JO w_std = z³·d_q(std) = {float(w_std_JO):.10f}")
    print(f"  JO w_alt = z³·d_q(alt) = {float(w_alt_JO):.10f}")
    print(f"  Sum                    = {float(S_JO):.10f}")
    print()
    # Ratio of weights
    r_sym = w_sym_JO / w_sym_P
    r_std = w_std_JO / w_std_P
    r_alt = w_alt_JO / w_alt_P
    print(f"  JO/Plancherel ratios:")
    print(f"    sym: {float(r_sym):.10f}")
    print(f"    std: {float(r_std):.10f}")
    print(f"    alt: {float(r_alt):.10f}")
    print()

    # V̂_i under both conventions
    # V̂_i^λ = w_λ · (character formula for λ at generator i)
    # For the sym (1-dim, χ_sym(σ) = q): V̂^sym = w_sym · q
    # For alt (1-dim, χ_alt(σ) = -1/q):  V̂^alt = w_alt · (-1/q)
    # For std: matrix-valued; use its q-dim as proxy here.
    print(f"  Effect on V̂_i (schematically, single σ):")
    print(f"    V̂^sym_Planck    = w_sym_P · q       = {float(w_sym_P * Q0):.10f}")
    print(f"    V̂^sym_JO        = w_sym_JO · q      = {float(w_sym_JO * Q0):.10f}")
    print(f"    V̂^alt_Planck    = w_alt_P · (-1/q)  = {float(w_alt_P * (-QI)):.10f}")
    print(f"    V̂^alt_JO        = w_alt_JO · (-1/q) = {float(w_alt_JO * (-QI)):.10f}")
    print()

    # Sum: V̂_full_sym_diff = V̂^sym_JO - V̂^sym_Planck
    # If the tower m_p_level0 ≈ 955 uses Plancherel weights and the
    # observed m_p ≈ 938, the "missing" mass is (m_p_Planck - m_p_JO)?
    # Check what shift JO conversion would produce on m_p.
    # This requires running the tower with JO weights — see
    # proton_mass_tower_derivation.py for the level-0 computation.
    # Here we just report the ratio for the user.
    w_total_P = w_sym_P + w_std_P + w_alt_P
    w_total_JO = w_sym_JO + w_std_JO + w_alt_JO
    scale = w_total_JO / w_total_P
    print(f"  Scale factor w_total_JO / w_total_P = {float(scale):.10f}")
    print(f"  Apply to m_p_tower_corrected:")
    m_p_scaled = M_P_TOWER_CORRECTED * scale
    err = (float(m_p_scaled) - M_P_MEV) / M_P_MEV * 100
    print(f"    m_p · scale = {float(m_p_scaled):.6f} MeV  err {err:+.3f}%")
    m_p_over_scale = M_P_TOWER_CORRECTED / scale
    err2 = (float(m_p_over_scale) - M_P_MEV) / M_P_MEV * 100
    print(f"    m_p / scale = {float(m_p_over_scale):.6f} MeV  err {err2:+.3f}%")


def main() -> int:
    print("=" * 100)
    print("TOWER RESIDUAL PROBE for m_p, m_n")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  m_p_tower (corrected) = {float(M_P_TOWER_CORRECTED):.4f} MeV")
    print(f"  m_p_CODATA             = {M_P_MEV} MeV")
    print(f"  residual R_p           = {float(R_P):.10f}  (Δ_p = {float(R_P-1)*100:+.4f}%)")
    print(f"  residual R_n           = {float(R_N):.10f}  (Δ_n = {float(R_N-1)*100:+.4f}%)")
    print()

    candidates, best_p, best_n = probe_algebraic_forms()
    probe_volumes()
    probe_jones_ocneanu_weights()

    witness = {
        "computation": "residual-probe-pn",
        "description": (
            "Probe proton/neutron tower residuals against three "
            "strategies: (1) q-algebraic closed forms, (2) rational-"
            "of-V(fig8) Dehn-filling analogues, (3) switching from "
            "Plancherel to Jones-Ocneanu Markov weights."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "R_p": mp.nstr(R_P, 25),
        "R_n": mp.nstr(R_N, 25),
        "best_alg_R_p": {"name": best_p[1], "val": mp.nstr(best_p[2], 25),
                           "err": best_p[0]},
        "best_alg_R_n": {"name": best_n[1], "val": mp.nstr(best_n[2], 25),
                           "err": best_n[0]},
    }
    out = Path(__file__).parent / "residual-probe-pn.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
