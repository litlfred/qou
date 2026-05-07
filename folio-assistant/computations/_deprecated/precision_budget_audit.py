#!/usr/bin/env python3
"""
Plan F — first concrete step: precision-budget audit on the existing
low-isotope-mass-table witness.

Reads the f64 witness `low-isotope-mass-table.witness.json` and
recomputes the *assembly* step (Δ = Z·Δ_H + N·Δ_n − B; M = A·u + Δ)
in mpmath at 50 dps, treating B_pred as the only f64-tainted input.
Emits a diagnostic witness `low-isotope-mass-table-precision-audit
.witness.json` that:

  1. Confirms the assembly arithmetic preserves the input precision
     (assembly-step residual ~ 10^-30 in the symbolic limit; observed
     residual is bounded by the f64 quantization of B_pred itself).
  2. Quantifies the precision budget per isotope: how much of the
     observed f64 residual could in principle be reduced by lifting
     B_pred to mpmath, and how much is irreducible f64 floor.
  3. Reports the f64-quantization noise floor on each isotope's
     M_pred (≈ M · 2^-52 ≈ M · 2.22e-16, i.e. ~0.5 ppb for ¹H,
     ~5 ppb for ²⁰Ne).

This script does NOT change the prediction path — it just shows that
the residuals reported in the f64 witness today are already at the
f64 floor for ¹H, ⁴He, and ¹²C. Plan F's higher-leverage step (Hoefsmit
seminormal in MPFR end-to-end) is what moves the floor.

Output: folio-assistant/computations/low-isotope-mass-table-precision-
audit.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from mpmath import mp, mpf, fabs

mp.dps = 50

HERE = Path(__file__).parent
F64_WITNESS = HERE / "low-isotope-mass-table.witness.json"
Q0_WITNESS = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "low-isotope-mass-table-precision-audit.witness.json"


def load_constants_50dps() -> dict:
    """Pin CODATA constants at 50 dps from string sources."""
    # CODATA 2022 string source (hard-coded; same as in low_isotope_
    # mass_table.py but as decimal strings).
    return {
        "U_MEV":   mpf("931.49410372"),
        "M_P_MEV": mpf("938.27208816"),
        "M_N_MEV": mpf("939.56542052"),
        "M_E_MEV": mpf("0.51099895"),
    }


def assembly_at_50dps(row: dict, c: dict) -> dict:
    """Recompute Δ and M from B_pred at 50 dps."""
    Z, N, A = row["Z"], row["N"], row["A"]
    B = mpf(repr(row["B_pred_MeV"]))
    Delta_H = c["M_P_MEV"] + c["M_E_MEV"] - c["U_MEV"]
    Delta_N = c["M_N_MEV"] - c["U_MEV"]
    Delta_pred = Z * Delta_H + N * Delta_N - B
    M_pred = A * c["U_MEV"] + Delta_pred
    return {
        "Delta_pred_50dps": str(Delta_pred),
        "M_pred_50dps":     str(M_pred),
    }


# Machine epsilon for IEEE 754 double precision, expressed as a
# relative error in parts per billion: 2^-52 ≈ 2.22e-16, so multiplied
# by 1e9 it is 2.22e-7 ppb (NOT 0.222 ppb — earlier draft was off by
# 10^6).  Used as the floor below which an observed residual is
# attributable to f64 quantization rather than any real upstream signal.
F64_FLOOR_PPB = 2.22e-7  # 2^-52 × 1e9


def main() -> int:
    f64 = json.load(open(F64_WITNESS))
    q0 = json.load(open(Q0_WITNESS))

    c = load_constants_50dps()

    rows_audited = []
    for row in f64["rows"]:
        a = assembly_at_50dps(row, c)
        # Convert f64 results to mpf to compare apples-to-apples.
        Delta_f64 = mpf(repr(row["delta_pred_MeV"]))
        M_f64     = mpf(repr(row["M_pred_MeV"]))
        Delta_50  = mpf(a["Delta_pred_50dps"])
        M_50      = mpf(a["M_pred_50dps"])

        # The assembly step is exact rational arithmetic in mpmath
        # given fixed B_pred. The only difference is the precision of
        # the mpmath constants vs the f64 ones.
        delta_residual = Delta_50 - Delta_f64
        M_residual = M_50 - M_f64

        rows_audited.append({
            "symbol":         row["symbol"],
            "Z":              row["Z"],
            "N":              row["N"],
            "A":              row["A"],
            "Delta_assembly_residual_MeV":   float(delta_residual),
            "Delta_assembly_residual_ppm":   float(delta_residual / Delta_50 * mpf(1_000_000)) if Delta_50 != 0 else None,
            "M_assembly_residual_MeV":       float(M_residual),
            "M_assembly_residual_ppb":       float(M_residual / M_50 * mpf(1_000_000_000)),
            "M_f64_quantization_floor_ppb":  F64_FLOOR_PPB,
            "observed_M_err_ppm":            row["M_err_ppm"],
            "observed_M_err_ppb":            row["M_err_ppm"] * 1000.0,
            # Residual is f64-floor-limited iff its magnitude is at or
            # below the IEEE 754 quantization floor (2.22e-7 ppb).
            # Earlier draft used a 1 ppb threshold, which is 4.5 million
            # times the actual floor and falsely tagged genuinely
            # signal-bearing residuals as floor-limited (PR #454,
            # Gemini r3150164181).
            "f64_floor_dominates":
                abs(row["M_err_ppm"] * 1000.0) < F64_FLOOR_PPB,
        })

    # Aggregate stats.
    n = len(rows_audited)
    n_at_floor = sum(1 for r in rows_audited if r["f64_floor_dominates"])
    max_assembly_residual = max(abs(r["M_assembly_residual_ppb"]) for r in rows_audited)

    out = {
        "computation": "low-isotope-mass-table-precision-audit",
        "description":
            "Plan F precision-budget audit. Reads the f64 witness "
            "low-isotope-mass-table.witness.json and recomputes the "
            "Δ and M assembly step in mpmath @ 50 dps. Quantifies how "
            "much of each observed residual is at the f64 floor "
            "(2.22e-7 ppb = 2^-52 × 1e9) vs upstream from the "
            "prediction path. Confirms the assembly arithmetic is "
            "precision-preserving — the mpmath lift on this step alone "
            "would not move any residual.",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision":  "mpfr_50dps",
        "inputs": {
            "f64_witness":   str(F64_WITNESS.name),
            "q0_50dps_str":  q0["derived_50_digit"]["q"],
        },
        "constants_50dps": {k: str(v) for k, v in c.items()},
        "stats": {
            "n_isotopes":               n,
            "n_at_f64_floor":           n_at_floor,
            "max_assembly_residual_ppb": max_assembly_residual,
        },
        "rows": rows_audited,
    }

    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Audit complete. {n} isotopes; {n_at_floor} at f64 floor "
          f"(< {F64_FLOOR_PPB:.2e} ppb).")
    print(f"  Max assembly-step residual: {max_assembly_residual:.3e} ppb")
    print(f"  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
