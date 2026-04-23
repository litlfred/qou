#!/usr/bin/env python3
"""
Low-isotope mass + Q-value table — predicted vs AME2020 observed.

Uses the binding-energy predictions from low_isotope_binding_sweep.py
to compute the atomic mass excess Δ(Z, N) and the total atomic mass
M(Z, N) for all stable isotopes with Z ≤ 10, and compares against
AME2020.

    Δ(Z, N)  =  Z · Δ_H  +  N · Δ_n  -  B(Z, N)
    M(Z, N)  =  A · u  +  Δ(Z, N)

where Δ_H = m_p + m_e - u and Δ_n = m_n - u are single-particle
mass excesses.  Since M(Z, N) ~ A · u, percentage errors on total
mass are parts-per-million even for multi-MeV binding errors —
the useful comparison is on the mass excess Δ (MeV scale) or
directly on B.

Outputs:
    low-isotope-mass-table.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from low_isotope_binding_sweep import (
    AME, predict, M_E_MEV, Q0,
)

# ── CODATA 2022 ─────────────────────────────────────────────────
U_MEV    = 931.49410372      # atomic mass unit, MeV
M_P_MEV  = 938.27208816      # proton
M_N_MEV  = 939.56542052      # neutron

DELTA_H  = M_P_MEV + M_E_MEV - U_MEV    # ≈  7.2890 MeV  (¹H mass excess)
DELTA_N  = M_N_MEV - U_MEV               # ≈  8.0714 MeV  (neutron mass excess)


# ── AME2020 observed mass excesses (MeV, atomic) ────────────────
AME_DELTA = {
    "1H":     7.28897,
    "2H":    13.13572,
    "3H":    14.9498,
    "3He":   14.9312,
    "4He":    2.42492,
    "6Li":   14.0869,
    "7Li":   14.9081,
    "8Be":    4.94167,
    "9Be":   11.3484,
    "10Be":  12.6070,
    "10B":   12.0507,
    "11B":    8.6680,
    "12C":    0.00000,   # AME definition
    "13C":    3.1250,
    "14N":    2.8634,
    "15N":    0.10144,
    "16O":   -4.73700,
    "17O":   -0.80931,
    "18O":   -0.78196,
    "19F":   -1.48740,
    "20Ne":  -7.04193,
    "21Ne":  -5.73175,
    "22Ne":  -8.02466,
}


def predict_mass_excess(symbol: str, Z: int, N: int) -> tuple[float, float, str]:
    """Return (B_pred, Delta_pred, strategy)."""
    B_pred, tag = predict(symbol, Z, N)
    delta_pred = Z * DELTA_H + N * DELTA_N - B_pred
    return B_pred, delta_pred, tag


def main() -> int:
    print(f"\n  Substrate q_0 = {Q0:.6f}")
    print(f"  u = {U_MEV:.4f} MeV,  m_p = {M_P_MEV:.4f},  m_n = {M_N_MEV:.4f}")
    print(f"  Δ_H = {DELTA_H:.4f} MeV,  Δ_n = {DELTA_N:.4f} MeV\n")

    header = (
        f"  {'atom':>6} {'A':>3} "
        f"{'Δ_obs':>9} {'Δ_pred':>9} {'ΔΔ':>8} {'err_%':>7}  "
        f"{'M_obs':>11} {'M_pred':>11}  strategy"
    )
    print(header)
    print("  " + "-" * (len(header) - 2))

    rows = []
    for symbol, Z, N, B_ame in AME:
        A = Z + N
        delta_obs = AME_DELTA.get(symbol)
        if delta_obs is None:
            continue
        B_pred, delta_pred, tag = predict_mass_excess(symbol, Z, N)

        # Total masses (MeV)
        M_obs  = A * U_MEV + delta_obs
        M_pred = A * U_MEV + delta_pred
        ddelta = delta_pred - delta_obs
        # For atoms where delta_obs is zero by AME definition (e.g. ¹²C),
        # a residual-as-percentage-of-Δ is ill-defined.  Use the absolute
        # residual divided by total mass (in ppm) as the meaningful metric
        # and emit a sentinel for the Δ-fractional column.
        if abs(delta_obs) > 1e-9:
            err_pct = 100.0 * ddelta / abs(delta_obs)
        else:
            err_pct = None   # undefined (AME-zero Δ); see M_err_ppm column

        err_pct_str = f"{err_pct:>+7.2f}" if err_pct is not None else f"{'—':>7}"
        print(
            f"  {symbol:>6} {A:>3} "
            f"{delta_obs:>+9.3f} {delta_pred:>+9.3f} "
            f"{ddelta:>+8.3f} {err_pct_str}  "
            f"{M_obs:>11.3f} {M_pred:>11.3f}  {tag}"
        )

        rows.append({
            "symbol": symbol,
            "Z": Z,
            "N": N,
            "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_MeV": B_pred,
            "delta_obs_MeV": delta_obs,
            "delta_pred_MeV": delta_pred,
            "delta_residual_MeV": ddelta,
            "delta_err_pct": err_pct,
            "M_obs_MeV": M_obs,
            "M_pred_MeV": M_pred,
            "M_err_ppm": 1e6 * (M_pred - M_obs) / M_obs if M_obs > 0 else 0.0,
            "strategy": tag,
        })

    # Summary: Q-values for α-decay chain (showcasing the framework)
    print("\n  α-decay Q-values along the α-chain (MeV):")
    alpha_chain = ["4He", "8Be", "12C", "16O", "20Ne", "22Ne"]
    for sym in alpha_chain:
        r = next((x for x in rows if x["symbol"] == sym), None)
        if r is None:
            continue
        # Q_α(parent → daughter + α) = Δ(parent) - Δ(daughter) - Δ(α)
        # For simplicity show Δ (not full Q); downstream readers can difference.
        print(f"    {r['symbol']:>6}  Δ_obs={r['delta_obs_MeV']:>+8.3f}  "
              f"Δ_pred={r['delta_pred_MeV']:>+8.3f}  "
              f"ΔΔ={r['delta_residual_MeV']:>+7.3f}")

    # Stats on Δ (mass excess)
    delta_errs = [abs(r["delta_residual_MeV"]) for r in rows if r["delta_obs_MeV"] != 0]
    mean_abs = sum(delta_errs) / len(delta_errs) if delta_errs else 0
    max_abs  = max(delta_errs) if delta_errs else 0
    m_ppms = [abs(r["M_err_ppm"]) for r in rows if r["M_obs_MeV"] > 0]
    print(f"\n  Δ (mass excess) stats: mean|ΔΔ|={mean_abs:.3f} MeV, max|ΔΔ|={max_abs:.3f} MeV")
    print(f"  M (total mass) stats:  mean|δM|={sum(m_ppms)/len(m_ppms):.1f} ppm, "
          f"max|δM|={max(m_ppms):.1f} ppm")

    witness = {
        "name": "low-isotope-mass-table",
        "description": (
            "Low-isotope mass + mass-excess table (Z ≤ 10) from the "
            "mass-volume binding framework.  Delta = Z·Δ_H + N·Δ_n "
            "- B_pred, M = A·u + Delta."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "constants": {
            "q_0": Q0,
            "U_MEV": U_MEV,
            "M_P_MEV": M_P_MEV,
            "M_N_MEV": M_N_MEV,
            "M_E_MEV": M_E_MEV,
            "DELTA_H_MEV": DELTA_H,
            "DELTA_N_MEV": DELTA_N,
        },
        "rows": rows,
        "stats": {
            "delta_mean_abs_MeV": mean_abs,
            "delta_max_abs_MeV": max_abs,
            "M_mean_abs_ppm": sum(m_ppms)/len(m_ppms) if m_ppms else 0,
            "M_max_abs_ppm": max(m_ppms) if m_ppms else 0,
        },
    }

    out_path = Path(__file__).parent / "low-isotope-mass-table.witness.json"
    out_path.write_text(json.dumps(witness, indent=2))
    print(f"\n  Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
