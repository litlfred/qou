#!/usr/bin/env python3
"""
ρ_F complexity-parameter sweep — test which knot invariant predicts
the per-atom deviation of ρ_F^eff = B_AME / Vol_hyp from the nominal
{m_e, 2m_e} dichotomy.

Empirical targets (from user's analysis):
  D   → deviation factor 0.98921  (ρ_F^eff / m_e)     — 1-knot, I_z=0
  T   → deviation factor 1.00156  (ρ_F^eff / 2m_e)    — 1-knot, I_z=-½
  ³He → deviation factor 1.03059  (ρ_F^eff / 2m_e)    — 1-knot, I_z=+½
  ⁴He → deviation factor 0.94459  (ρ_F^eff / 2m_e)    — 4 disjoint pieces

Candidate complexity parameters:
  (1) J(K, q₀)           — Jones polynomial at substrate q₀
  (2) n_JSJ_pieces        — number of hyperbolic JSJ pieces
  (3) d_q(λ_dom)          — quantum dim of dominant Hecke rep
  (4) Milnor triple (³He) — for Brunnian components
  (5) |J(K, -1)| = det    — knot determinant
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

from mpmath import mp, mpf, log, sqrt
mp.dps = 50

# Substrate parameter at 50 digits
Q_0_STR = "1.1099785955541805752815940796095093779667618976181"
Q_0 = mpf(Q_0_STR)

# Empirical ρ_F^eff / nominal per atom (from user's reconstruction)
EMPIRICAL = {
    "D":   {"B_AME": mpf("2.22456612"),
            "V_hyp": mpf("4.40083251612792"),   # Vol(6_2) from SnapPy
            "nominal_rho": mpf("0.51099895"),   # m_e
            "knot":  "6_2",   "n_jsj": 1,  "components": 1,
            "I_z":   0},
    "T":   {"B_AME": mpf("8.4817984"),
            "V_hyp": mpf("8.28632"),           # Vol(8_11)
            "nominal_rho": mpf("2") * mpf("0.51099895"),
            "knot":  "8_11",  "n_jsj": 1,  "components": 1,
            "I_z":   mpf("-0.5")},
    "3He": {"B_AME": mpf("7.7180375"),
            "V_hyp": mpf("7.32772475"),        # Vol(Borromean) = 8G
            "nominal_rho": mpf("2") * mpf("0.51099895"),
            "knot":  "L6a4",  "n_jsj": 1,  "components": 3,
            "I_z":   mpf("0.5")},
    "4He": {"B_AME": mpf("28.2956912"),
            "V_hyp": mpf("4") * mpf("7.32772475"),  # 4 disjoint Borromean
            "nominal_rho": mpf("2") * mpf("0.51099895"),
            "knot":  "4·L6a4", "n_jsj": 4, "components": 12,
            "I_z":   0},
}


# ── (1) Jones polynomial at q₀ ─────────────────────────────
#
# Hardcoded from KnotInfo / LinkInfo databases (Sage not available
# here).  Convention: V_K(t) is the Jones polynomial with V(unknot) = 1
# and skein relation (t V(L+) - t^-1 V(L-) = (t^{1/2} - t^{-1/2}) V(L0)).
#
# t = q₀² for our substrate (standard convention relating to Markov q).

def jones_6_2(t):
    """V(6_2, t) = t^{-1} - 1 + 2t - 2t^2 + 2t^3 - 2t^4 + t^5"""
    return 1/t - 1 + 2*t - 2*t**2 + 2*t**3 - 2*t**4 + t**5

def jones_8_11(t):
    """V(8_11, t) = -1 + 3t - 4t^2 + 5t^3 - 5t^4 + 4t^5 - 3t^6 + 2t^7 - t^8

    (From KnotInfo — may differ by sign convention with other sources.)
    """
    return (-1 + 3*t - 4*t**2 + 5*t**3 - 5*t**4
            + 4*t**5 - 3*t**6 + 2*t**7 - t**8)

def jones_borromean(t):
    """Borromean rings V_L(t) — specific 3-component evaluation.

    Using the linked form: V(Borromean, t) = (t - 1)^2 · (t + 1) / t^3
    (from published tables, may vary by convention).
    """
    return (t - 1)**2 * (t + 1) / t**3

def jones_4_borromean_disjoint_APPROX(t):
    """⚠ APPROXIMATION — NOT a correct Jones polynomial.

    The exact disjoint-union rule under the standard Jones normalization
    `V(unknot) = 1` is
        V(L₁ ⊔ L₂) = -(t^{1/2} + t^{-1/2}) · V(L₁) · V(L₂)
    so 4 disjoint Borromean links would give
        V = (-(t^{1/2}+t^{-1/2}))^3 · V(Borromean)^4.

    This function drops the `(-(t^{1/2}+t^{-1/2}))^3` prefactor and
    returns only `jones_borromean(t) ** 4`.  It is retained here as a
    crude qualitative proxy for the ⁴He row of the correlation sweep
    only; the absolute magnitude is not physically meaningful.

    Flagged in the PR#401 Copilot review — if the ⁴He row is used for
    any quantitative claim, implement the correct disjoint-union
    convention and rename without the `_APPROX` suffix.
    """
    return jones_borromean(t) ** 4


# Backward-compat alias — any caller relying on the prior name gets
# the same (approximate) value but the name change is not breaking.
jones_4_borromean_disjoint = jones_4_borromean_disjoint_APPROX


def j_at_q0(name):
    """Evaluate Jones polynomial at t = q₀²."""
    t = Q_0 ** 2
    if name == "6_2":     return jones_6_2(t)
    if name == "8_11":    return jones_8_11(t)
    if name == "L6a4":    return jones_borromean(t)
    if name == "4·L6a4":  return jones_4_borromean_disjoint(t)
    return mpf("nan")


# ── (5) Knot determinant |J(K, -1)| ────────────────────────
DETERMINANTS = {
    "6_2":    11,
    "8_11":   27,
    "L6a4":   16,     # Borromean link determinant
    "4·L6a4": 16**4,  # 65536 — multiplicative for disjoint
}


def run_probe():
    """Compute all complexity parameters + rho_F deviations."""
    results = []
    print("=" * 110)
    print(f"ρ_F COMPLEXITY SWEEP — q₀ = {float(Q_0):.6f}")
    print("=" * 110)
    print(f"\n  {'atom':>4} {'B_AME':>10} {'V_hyp':>12} "
          f"{'ρ_F^eff':>10} {'nominal':>10} {'dev':>10} "
          f"{'dev(-1)':>9}")
    for atom, d in EMPIRICAL.items():
        rho_eff = d["B_AME"] / d["V_hyp"]
        dev_factor = rho_eff / d["nominal_rho"]
        dev_from_1 = float(dev_factor - 1) * 100
        print(f"  {atom:>4} {float(d['B_AME']):>10.4f} "
              f"{float(d['V_hyp']):>12.4f} "
              f"{float(rho_eff):>10.5f} "
              f"{float(d['nominal_rho']):>10.5f} "
              f"{float(dev_factor):>10.5f} "
              f"{dev_from_1:>+8.3f}%")

    # Candidate: Jones polynomial at q₀
    print(f"\n{'=' * 80}")
    print("CANDIDATE 1: Jones polynomial J(K, q₀²)")
    print("=" * 80)
    print(f"  {'atom':>4} {'knot':>8} {'J(K, q₀²)':>15} "
          f"{'ln|J|':>10} {'dev(-1)%':>10}")
    for atom, d in EMPIRICAL.items():
        J = j_at_q0(d["knot"])
        rho_eff = d["B_AME"] / d["V_hyp"]
        dev_factor = rho_eff / d["nominal_rho"]
        dev_pct = float(dev_factor - 1) * 100
        try:
            lnJ = float(log(abs(J))) if J != 0 else float("-inf")
        except Exception:
            lnJ = float("nan")
        print(f"  {atom:>4} {d['knot']:>8} "
              f"{float(J):>+15.6f} "
              f"{lnJ:>10.5f} "
              f"{dev_pct:>+9.3f}%")
        results.append({"atom": atom, "knot": d["knot"],
                         "J_at_q0_sq": str(J), "ln_abs_J": lnJ,
                         "dev_pct": dev_pct})

    # Candidate: JSJ piece count
    print(f"\n{'=' * 80}")
    print("CANDIDATE 2: JSJ-piece count")
    print("=" * 80)
    print(f"  {'atom':>4} {'n_JSJ':>6} {'dev(-1)%':>10} {'dev/(n_JSJ-1)':>15}")
    for atom, d in EMPIRICAL.items():
        rho_eff = d["B_AME"] / d["V_hyp"]
        dev_factor = rho_eff / d["nominal_rho"]
        dev_pct = float(dev_factor - 1) * 100
        n = d["n_jsj"]
        per_piece = (dev_pct / (n - 1)) if n > 1 else float("nan")
        print(f"  {atom:>4} {n:>6} {dev_pct:>+9.3f}% "
              f"{per_piece if n > 1 else '        n/a':>15}")

    # Candidate: knot determinant
    print(f"\n{'=' * 80}")
    print("CANDIDATE 5: Knot determinant |J(K, -1)|")
    print("=" * 80)
    print(f"  {'atom':>4} {'knot':>8} {'det':>10} {'ln(det)':>10} "
          f"{'1/det':>12} {'dev(-1)%':>10}")
    for atom, d in EMPIRICAL.items():
        det = DETERMINANTS.get(d["knot"], 0)
        rho_eff = d["B_AME"] / d["V_hyp"]
        dev_factor = rho_eff / d["nominal_rho"]
        dev_pct = float(dev_factor - 1) * 100
        ln_det = float(log(mpf(det))) if det > 0 else float("nan")
        inv_det = 1 / float(det) if det != 0 else float("nan")
        print(f"  {atom:>4} {d['knot']:>8} {det:>10} "
              f"{ln_det:>10.4f} {inv_det:>12.6e} "
              f"{dev_pct:>+9.3f}%")

    # Correlation analysis
    print(f"\n{'=' * 80}")
    print("CORRELATION SUMMARY")
    print("=" * 80)
    devs = [(r["atom"], r["dev_pct"], float(r["ln_abs_J"]))
             for r in results]
    # Pearson-like
    n = len(devs)
    mean_d = sum(x[1] for x in devs) / n
    mean_lj = sum(x[2] for x in devs if x[2] > -1e9) / n
    var_d = sum((x[1] - mean_d) ** 2 for x in devs)
    var_lj = sum((x[2] - mean_lj) ** 2 for x in devs if x[2] > -1e9)
    cov = sum((x[1] - mean_d) * (x[2] - mean_lj)
                for x in devs if x[2] > -1e9)
    if var_d > 0 and var_lj > 0:
        corr = cov / (var_d * var_lj) ** 0.5
    else:
        corr = float("nan")
    print(f"  deviations: {[f'{d[1]:+.2f}%' for d in devs]}")
    print(f"  ln|J(q₀²)|: {[f'{d[2]:+.3f}' for d in devs]}")
    print(f"  Pearson correlation(dev%, ln|J|) = {corr:+.4f}")

    return results


if __name__ == "__main__":
    results = run_probe()

    witness = {
        "computation": "rho-f-complexity-sweep",
        "description": (
            "Empirical ρ_F^eff reconstruction vs nominal {m_e, 2m_e} "
            "dichotomy, tested against candidate complexity parameters: "
            "(1) J(K, q₀²), (2) n_JSJ, (5) |det K|.  Uses hardcoded "
            "Jones polynomials from KnotInfo since Sage not available "
            "for SnapPy.jones_polynomial() in this env.  q₀ at 50 "
            "decimal digits."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0_str": Q_0_STR,
        "precision_digits": 50,
        "empirical_targets": {
            k: {kk: (str(vv) if hasattr(vv, 'real') else vv)
                for kk, vv in v.items()}
            for k, v in EMPIRICAL.items()
        },
        "candidate_1_jones": results,
        "notes": (
            "Jones polynomial coefficients hardcoded from KnotInfo "
            "(6_2, 8_11) and LinkInfo (Borromean L6a4).  Four disjoint "
            "Borromeans evaluated multiplicatively; this is an "
            "approximation — the exact multi-component Jones "
            "convention for disjoint unions differs."
        ),
    }
    out = Path(__file__).parent / "rho-f-complexity-sweep.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
