#!/usr/bin/env python3
"""
Deuteron (D) audit — sweep every decision knob on the H_A 3-channel
framework and record per-channel contributions to localise the error.

Deuteron: Z=1, N=1, A=2, AME binding = 2.224566 MeV.
Current best pred 4.924 MeV → 121% over-predicts B (0.142% of mass).

Knobs:
  - Gluon count per nucleon: proton ∈ {0,1,2}, neutron ∈ {0,1,2,3,4}
  - m_pn (proton-neutron crossing multiplicity): {1, 2, 3, 4, 5}
  - Kähler lift level: {0, 1, 2}

For D there's only ONE generator (A-1 = 1), so per-gen data is crisp.
Report each variant's V̂^sym, V̂^std, V̂^alt, per-channel ln|Φ_q|,
weighted-sum B, and err vs AME.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV

HBAR_Q = (q0 - 1.0) / q0
q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
W_SYM = 1.0 / (qint2**2 + 2)
W_STD = qint2**2 / (qint2**2 + 2)
W_ALT = W_SYM


def ln_phi_q(v, max_k=500):
    if v == 0:
        return 0.0
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi0**k * v
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15:
            break
    return s


def kahler_lift(V_sym_expr, n_levels):
    """Apply Kähler lift n times to a symbolic V(q)."""
    V = V_sym_expr
    for _ in range(n_levels):
        dV_dq = sp.diff(V, q_sym)
        V = sp.expand(V + (q_sym - 1) * dV_dq)   # ℏ_q · q · dV/dq = (q-1)·dV/dq
    return V


def D_per_gen_volumes(proton_gluon_count, neutron_gluon_count, m_pn, kahler_n):
    """Compute V̂^sym, V̂^std, V̂^alt for D's single generator gen_idx=0
    with configurable gluon counts + m_pn + Kähler level."""
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)

    # Gluon for proton at gen_idx=0 (this nucleon is proton)
    # Each σ₀ has (c, d) = (1, 0)
    c_gluon, d_gluon = sp.Integer(1), sp.Integer(0)
    for _ in range(proton_gluon_count):
        a, b = (sp.expand(a * c_gluon * HA_sym + a * d_gluon + b * c_gluon),
                 sp.expand(a * c_gluon + b * d_gluon))
        sp_v = sp.expand(sp_v * (c_gluon * q_sym + d_gluon))
        ap_v = sp.expand(ap_v * (-c_gluon / q_sym + d_gluon))

    # Inter-nucleon pn crossing: (c=1, d=-h/2)
    c_pn, d_pn = sp.Integer(1), -HA_sym / 2
    for _ in range(m_pn):
        a, b = (sp.expand(a * c_pn * HA_sym + a * d_pn + b * c_pn),
                 sp.expand(a * c_pn + b * d_pn))
        sp_v = sp.expand(sp_v * (c_pn * q_sym + d_pn))
        ap_v = sp.expand(ap_v * (-c_pn / q_sym + d_pn))

    V_sym = kahler_lift(sp_v, kahler_n)
    V_std = kahler_lift(z_sym * a + b, kahler_n)
    V_alt = kahler_lift(ap_v, kahler_n)
    return V_sym, V_std, V_alt


def B_from_volumes(V_sym, V_std, V_alt):
    vs = float(V_sym.subs(q_sym, q0))
    vd = float(V_std.subs(q_sym, q0))
    va = float(V_alt.subs(q_sym, q0))
    ln_sym = ln_phi_q(abs(vs))
    ln_std = ln_phi_q(abs(vd))
    ln_alt = ln_phi_q(abs(va))
    B_sym = W_SYM * M_E_MEV * ln_sym
    B_std = W_STD * M_E_MEV * ln_std
    B_alt = W_ALT * M_E_MEV * ln_alt
    return {
        "V_sym_at_q0": vs, "V_std_at_q0": vd, "V_alt_at_q0": va,
        "ln_Phi_sym": ln_sym, "ln_Phi_std": ln_std, "ln_Phi_alt": ln_alt,
        "B_sym_MeV": B_sym, "B_std_MeV": B_std, "B_alt_MeV": B_alt,
        "B_total_MeV": B_sym + B_std + B_alt,
    }


def main():
    B_AME = 2.224566
    Mtot = 2 * 938.272
    print("=" * 125)
    print(f"DEUTERON AUDIT — H_A 3-channel, single generator")
    print(f"q0 = {q0}, h = {HA_sym.subs(q_sym, q0):.6f}, "
          f"ℏ_q² = {HBAR_Q**2:.6f}, m_e = {M_E_MEV} MeV")
    print(f"w_sym = {W_SYM:.6f}  w_std = {W_STD:.6f}  w_alt = {W_ALT:.6f}")
    print(f"B_AME = {B_AME} MeV (AME2020)")
    print("=" * 125)

    # Knob grid
    configs = []
    for pg in [0, 1, 2]:
        for ng in [0, 2, 4]:  # N=1, ng is for later nucleons, not this one
            for m_pn in [1, 2, 3]:
                for k in [0, 1, 2]:
                    configs.append((pg, ng, m_pn, k))

    # For D there's only 1 gen (proton at gen_idx=0), and neutron is after.
    # Neutron's own gluon doesn't appear in gen_idx=0's V̂ (only this
    # nucleon's gluon + inter-nucleon crossings to later). So ng irrelevant
    # for D's single-gen computation. Reduce grid.
    configs = [(pg, m_pn, k)
                 for pg in [0, 1, 2]
                 for m_pn in [1, 2, 3]
                 for k in [0, 1, 2]]

    print(f"\n  {'pg':>3} {'m_pn':>5} {'k':>2} | "
          f"{'V_sym':>9} {'V_std':>9} {'V_alt':>9} | "
          f"{'lnΦ_sym':>10} {'lnΦ_std':>10} {'lnΦ_alt':>10} | "
          f"{'B_sym':>8} {'B_std':>8} {'B_alt':>8} {'B_tot':>8} "
          f"{'err%':>8}")
    print("  " + "-" * 123)

    results = []
    for (pg, m_pn, k) in configs:
        Vs, Vd, Va = D_per_gen_volumes(pg, 0, m_pn, k)
        r = B_from_volumes(Vs, Vd, Va)
        err = abs(r["B_total_MeV"] - B_AME) / Mtot * 100
        gap = r["B_total_MeV"] - B_AME
        print(f"  {pg:>3} {m_pn:>5} {k:>2} | "
              f"{r['V_sym_at_q0']:>+9.4f} {r['V_std_at_q0']:>+9.4f} {r['V_alt_at_q0']:>+9.4f} | "
              f"{r['ln_Phi_sym']:>10.4f} {r['ln_Phi_std']:>10.4f} {r['ln_Phi_alt']:>10.4f} | "
              f"{r['B_sym_MeV']:>+8.4f} {r['B_std_MeV']:>+8.4f} {r['B_alt_MeV']:>+8.4f} "
              f"{r['B_total_MeV']:>+8.4f} {err:>7.4f}%")
        results.append({
            "pg": pg, "m_pn": m_pn, "kahler_level": k,
            **r,
            "gap_MeV": gap, "err_mass_pct": err,
            "relative_err_vs_AME_pct": abs(gap) / B_AME * 100,
        })

    # Find the combination nearest AME
    valid = [r for r in results if r["B_total_MeV"] > 0]
    best = min(valid, key=lambda r: r["err_mass_pct"])
    print("\n  --- minimum-error configuration ---")
    print(f"  pg={best['pg']}, m_pn={best['m_pn']}, k={best['kahler_level']}: "
          f"B={best['B_total_MeV']:+.4f} MeV  err={best['err_mass_pct']:.4f}%")

    # Channel breakdown for the default (pg=2, m_pn=1, k=0)
    default = next(r for r in results
                    if r["pg"] == 2 and r["m_pn"] == 1 and r["kahler_level"] == 0)
    print("\n  --- default (pg=2, m_pn=1, k=0) channel breakdown ---")
    print(f"  B_sym (w={W_SYM:.4f} × m_e × ln|Φ_q(V_sym={default['V_sym_at_q0']:.4f})|) = "
          f"{default['B_sym_MeV']:+.4f} MeV ({default['B_sym_MeV']/default['B_total_MeV']*100:+.1f}%)")
    print(f"  B_std (w={W_STD:.4f} × m_e × ln|Φ_q(V_std={default['V_std_at_q0']:.4f})|) = "
          f"{default['B_std_MeV']:+.4f} MeV ({default['B_std_MeV']/default['B_total_MeV']*100:+.1f}%)")
    print(f"  B_alt (w={W_ALT:.4f} × m_e × ln|Φ_q(V_alt={default['V_alt_at_q0']:.4f})|) = "
          f"{default['B_alt_MeV']:+.4f} MeV ({default['B_alt_MeV']/default['B_total_MeV']*100:+.1f}%)")
    print(f"  B_total = {default['B_total_MeV']:+.4f} MeV (AME={B_AME})  "
          f"gap = {default['gap_MeV']:+.4f} MeV  "
          f"rel_err = {default['relative_err_vs_AME_pct']:.2f}%")

    out = Path(__file__).parent / "deuteron-audit.witness.json"
    out.write_text(json.dumps({
        "computation": "deuteron-audit",
        "description": (
            "Deuteron B(1,1) parameter sweep on H_A 3-channel framework. "
            "Varies per-proton gluon count, m_pn inter-nucleon multiplicity, "
            "and Kähler lift level. Reports per-channel V_hat and ln|Phi_q| "
            "to localise error contributions."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "M_E_MEV": M_E_MEV, "B_AME_MeV": B_AME,
            "w_sym": W_SYM, "w_std": W_STD, "w_alt": W_ALT,
        },
        "results": results,
        "best": best,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")


if __name__ == "__main__":
    main()
