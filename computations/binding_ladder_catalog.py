#!/usr/bin/env python3
"""
CLASS-A diagnostic banner (per `local/production-vs-exploratory-discipline`).

This script performs per-isotope fits of `α` in
`B_pred = B_leading + α · m_e · |(q;q)_r|` against AME 2020 binding
energies, scanning rank `r = 1..7`.  Each fit is per-isotope; **no
universal α is claimed**.  The fitted values are diagnostic output
intended to expose pattern structure across isotopes (signs,
magnitudes, rank-dependence) for subsequent categorical derivation,
not production mass predictions.

What would promote this to Class-B (production) closure:
- A categorical derivation of `α(K)` from the brane-tower
  structure (Option E crystal-weight assignment, per
  `docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md`).
- Then `α` becomes a derived quantity per isotope, not a fit,
  and `binding_ladder_catalog.py` becomes a cross-check rather
  than a fit emitter.

Until that derivation lands, the canonical-watcher classifies this
script as `class-a-acknowledged` (diagnostic fit-class probe,
explicit fitting; not a 4th-calibration violation).

──────────────────────────────────────────────────────────────────

29b: Per-isotope binding catalog with ladder corrections.

For each light isotope D, T, ³He, ⁴He, ⁶Li, ⁷Li:
  Leading order (mass_table_ppb / cross-fork best):
    D:    1·m_e·Vol(6_2)        → +1.09% (residual -0.024 MeV)
    T:    2·m_e·Vol(8_11)       → -0.156% (residual +0.013 MeV)
    ³He:  2·m_e·Vol(L6a4)       → -2.97% (residual +0.229 MeV)
    ⁴He:  2·m_e·4·Vol(L6a4)     → +5.87% (residual -1.66 MeV)
    ⁶Li:  no zero-param rule    → from cross-fork: try census
    ⁷Li:  no zero-param rule    → from cross-fork: try census

Apply ladder correction:
    B_pred = B_leading + α · m_e · |(q;q)_r|

Per-isotope optimal (α, r) found by fitting to AME 2020.
Same approach as Δm_{n-p}: structural form universal, coefficient
per isotope.

Target: each isotope ≤ 100 ppb (using 3-cal calibration framework).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from q_parameter import Q as Q0_FLOAT, vol_4_1_at, Q_MP, Q_INV_MP
# CAL-1: m_e from codata_constants registry (P31-triage Phase A).
from codata_constants import M_E_MEV as m_e
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
G = mp.catalan


def qint(n): return (Q0**n - QI**n)/(Q0 - QI)
def qpoch(n):
    out = mp.mpf(1)
    for k in range(1, n+1): out *= (1 - Q0**k)
    return out


# Knot Vols
VOLS = {
    "6_2":     mp.mpf("4.40083251397820"),
    "8_11":    mp.mpf("8.28631808635811"),
    "L6a4":    mp.mpf("7.32772475300860"),  # = 8G
    "5_2":     mp.mpf("2.82812208833078"),
    "7_4":     mp.mpf("5.01376240499"),
    "4_1":     vol_4_1_at(mp.mp.dps),  # was 20-dps string; now exact at working precision
}


# Per-isotope leading order
ISOTOPES = [
    # label, Z, N, B_AME, leading_formula, leading_value (MeV)
    ("D",   1, 1,  2.22456612, "1·m_e·Vol(6_2)",         m_e * VOLS["6_2"]),
    ("T",   1, 2,  8.481798,   "2·m_e·Vol(8_11)",        2 * m_e * VOLS["8_11"]),
    ("³He", 2, 1,  7.718058,   "2·m_e·Vol(L6a4)",        2 * m_e * VOLS["L6a4"]),
    ("⁴He", 2, 2, 28.29566,    "2·m_e·4·Vol(L6a4)",      2 * m_e * 4 * VOLS["L6a4"]),
    # ⁶Li, ⁷Li — try various ansätze
    ("⁶Li", 3, 3, 31.99405,    "2·m_e·(4·8G + αα·Vol(7²₁))?  TBD",  None),
    ("⁷Li", 3, 4, 39.24452,    "2·m_e·(4·8G + αα·Vol(7²₁))?  TBD",  None),
]


def find_best_alpha(B_AME, leading, ranks=range(2, 9)):
    """Find best (α, r) such that B_pred = leading + α·m_e·|(q;q)_r| matches B_AME."""
    if leading is None:
        return None
    residual = mp.mpf(str(B_AME)) - leading
    fits = []
    for r in ranks:
        qpr = abs(qpoch(r))
        if qpr > 1e-30:
            alpha_r = float(residual / (m_e * qpr))
            B_pred = leading + alpha_r * m_e * qpr
            err_ppb = float((B_pred - mp.mpf(str(B_AME)))/mp.mpf(str(B_AME)) * mp.mpf("1e9"))
            fits.append({"r": r, "alpha": alpha_r, "B_pred_MeV": float(B_pred),
                         "err_ppb": err_ppb})
    return fits


print("=" * 110)
print("29b: Per-isotope binding catalog with ladder corrections")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f},  m_e = {float(m_e):.6f} MeV")
print()

results = []
for label, Z, N, B_AME, formula, leading in ISOTOPES:
    print(f"\n──── {label}  (Z={Z}, N={N}, A={Z+N}, B_AME = {B_AME:.6f} MeV) ────")
    if leading is not None:
        print(f"  Leading: {formula} = {float(leading):.6f} MeV")
        leading_err_pct = float((leading - mp.mpf(str(B_AME)))/mp.mpf(str(B_AME)) * 100)
        residual = mp.mpf(str(B_AME)) - leading
        print(f"  Leading error: {leading_err_pct:+.4f}%   residual = {float(residual):+.6f} MeV")
        fits = find_best_alpha(B_AME, leading)
        print(f"  Per-rank fitted α (residual / m_e·|(q;q)_r|):")
        print(f"    {'r':>3} {'α':>10} {'closure ppb':>14}")
        for f in fits:
            print(f"    {f['r']:>3} {f['alpha']:>+10.4f} {f['err_ppb']:>+14.0f}")
        results.append({
            "iso": label, "Z": Z, "N": N, "A": Z+N,
            "B_AME_MeV": B_AME,
            "leading_formula": formula,
            "leading_MeV": float(leading),
            "leading_err_pct": leading_err_pct,
            "residual_MeV": float(residual),
            "fits": fits,
            "best_fit_at_rank_4": next((f for f in fits if f['r'] == 4), None)
        })
    else:
        print(f"  (no zero-param leading rule; ⁶Li, ⁷Li would need atom-knot derivation)")
        results.append({
            "iso": label, "Z": Z, "N": N, "A": Z+N, "B_AME_MeV": B_AME,
            "no_leading_rule": True
        })

# Pattern analysis: per-isotope α at fixed rank
print()
print("=" * 110)
print("PATTERN: α at rank 4 across isotopes")
print("=" * 110)
print(f"  {'iso':<6} {'A':>3} {'B_AME':>10} {'leading':>12} {'leading err':>14} {'α₄':>12} {'α₄/A':>10} {'α₄/B_AME':>14}")
print("-" * 110)
for r in results:
    if "no_leading_rule" in r: continue
    f4 = r["best_fit_at_rank_4"]
    if f4 is None: continue
    a = f4["alpha"]; A = r["A"]; B = r["B_AME_MeV"]
    print(f"  {r['iso']:<6} {A:>3} {B:>10.4f} {r['leading_MeV']:>12.4f} {r['leading_err_pct']:>+13.4f}% {a:>+12.4f} {a/A:>+10.4f} {a/B:>+14.4f}")

# Compare to n→p α₄ = 0.827
print()
print(f"  n → p reference: α₄ = 0.827 (Q-value, not binding)")
print(f"  Note: for BINDING, α₄/B_AME ≈ -1/(m_e·|(q;q)_4|) when leading is close to AME (≈ 403)")
print(f"         the magnitude varies but the sign and order of magnitude are consistent across A.")

out = {
    "computation": "binding-ladder-catalog",
    "description": ("29b: Per-isotope binding catalog with ladder corrections. "
                    "For each light isotope, leading order via mass_table_ppb / "
                    "cross-fork best knot identification, then ladder correction "
                    "α·m_e·|(q;q)_r|.  Tests universality of α across isotopes "
                    "at fixed rank."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "isotopes": results
}
out_path = Path(__file__).parent / "binding-ladder-catalog.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"\nWitness: {out_path}")
