"""
probe_mu_d_minus_mu_u_categorical.py — derive (μ_d − μ_u) from
V_(2,1) Hoefsmit substrate, not CODATA Δm fit.

Per owner: research item 1 from m_n investigation.

The current `m_n_difference_formula.py` fits (μ_d − μ_u) to
CODATA Δm = 1.293 MeV (1-parameter calibration).  To make m_n
genuinely substrate-derived, (μ_d − μ_u) must come from the
categorical structure of the V_(2,1) Hoefsmit substrate.

The V_(2,1) Hoefsmit matrix entries are:
  d_1 = q³ / (q² + 1)      (≈ +0.613 at q_0)
  d_2 = −q⁻¹ / (q² + 1)    (≈ −0.404 at q_0)
  b² = d_1 · d_2 + 1       (≈ +0.753 at q_0)
  b  ≈ +0.868

These encode CHIRALITY (d_1 > 0 right-handed, d_2 < 0 left-handed).
The natural identification:
  μ_u → "up-flavor" mass scale, related to d_1 (right-handed)
  μ_d → "down-flavor" mass scale, related to d_2 (left-handed)

This probe tests CATEGORICAL CANDIDATES for (μ_d − μ_u) and
compares to CODATA Δm = 1.293 MeV.  The target value in m_e units:
  Δm_cat = 1.293 / 0.511 = 2.531

Per the difference formula:
  Δm = ((q + q⁻¹) / (q^{1/2} + q^{-1/2})) · (μ_d − μ_u)
     = [2]_q · z · (μ_d − μ_u)  ≈  1.003 · (μ_d − μ_u)
     ≈  (μ_d − μ_u)             (since prefactor ≈ 1 at q_0)

So target (μ_d − μ_u) ≈ 1.293 MeV (in MeV) or 2.531 (in m_e units).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

Q_WIT = HERE / "q-pinning-50-digit.witness.json"
q = mpf(json.load(Q_WIT.open())["derived_50_digit"]["q"])
q_inv = mpf(1) / q
h_q = q - q_inv
z_mark = mpf(1) / (mp.sqrt(q) + mp.sqrt(q_inv))

M_E_MEV = mpf("0.51099895069")
DELTA_M_CODATA_MEV = mpf("1.293332")  # m_n - m_p (CODATA 2018)

# V_(2,1) Hoefsmit substrate
d_1 = q ** 3 / (q ** 2 + 1)
d_2 = -q_inv / (q ** 2 + 1)
b_sq = d_1 * d_2 + 1
b = mp.sqrt(b_sq)

# Difference-formula prefactor (≈ 1 at q_0)
prefactor = (q + q_inv) / (mp.sqrt(q) + mp.sqrt(q_inv))


def main() -> int:
    print("=" * 78)
    print("  Categorical candidates for (μ_d − μ_u) from V_(2,1) Hoefsmit")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(q, 16)}")
    print(f"  d_1 = q³/(q²+1)    = {mp.nstr(d_1, 10)}")
    print(f"  d_2 = −q⁻¹/(q²+1)  = {mp.nstr(d_2, 10)}")
    print(f"  b² = d_1·d_2 + 1   = {mp.nstr(b_sq, 10)}")
    print(f"  b  = √b²           = {mp.nstr(b, 10)}")
    print()
    print(f"  Target: Δm_CODATA  = {DELTA_M_CODATA_MEV} MeV")
    print(f"  Target in m_e:     = {mp.nstr(DELTA_M_CODATA_MEV / M_E_MEV, 10)}")
    print(f"  Difference-formula prefactor [2]_q·z = {mp.nstr(prefactor, 10)} (≈ 1)")
    print(f"  Target (μ_d − μ_u) ≈ Δm / prefactor = "
          f"{mp.nstr(DELTA_M_CODATA_MEV / prefactor, 10)} MeV")
    print(f"  In m_e units:                       = "
          f"{mp.nstr(DELTA_M_CODATA_MEV / (prefactor * M_E_MEV), 10)}")
    print()

    target_cat = DELTA_M_CODATA_MEV / (prefactor * M_E_MEV)

    candidates = [
        ("|d_1|",                     mp.fabs(d_1)),
        ("|d_2|",                     mp.fabs(d_2)),
        ("|d_1| − |d_2|",             mp.fabs(d_1) - mp.fabs(d_2)),
        ("d_1 − d_2",                 d_1 - d_2),
        ("|d_1| + |d_2|",             mp.fabs(d_1) + mp.fabs(d_2)),
        ("b",                         b),
        ("b²",                        b_sq),
        ("|d_1| · 4",                 mp.fabs(d_1) * 4),
        ("(q²−1)/(q²+1)",             (q ** 2 - 1) / (q ** 2 + 1)),
        ("h_q · 4",                   h_q * 4),
        ("[2]_q · b",                 (q + q_inv) * b),
        ("|d_1| · [2]_q",             mp.fabs(d_1) * (q + q_inv)),
        ("h_q · [2]_q · b",           h_q * (q + q_inv) * b),
        ("[3]_q − 1",                 (q**3 - q_inv**3) / h_q - 1),
        ("2 · b",                     2 * b),
        ("(d_1 − d_2) · q",           (d_1 - d_2) * q),
        ("(d_1 − d_2) · z",           (d_1 - d_2) * z_mark),
    ]

    print(f"  {'candidate':35} {'value (m_e units)':>20} {'value (MeV)':>16} {'residual %':>14}")
    print("  " + "-" * 88)
    results = []
    for name, val in candidates:
        val_mev = val * M_E_MEV * prefactor  # m_e times difference-formula prefactor → Δm in MeV
        ratio = val / target_cat
        residual_pct = (val - target_cat) / target_cat * 100
        marker = " ← BEST" if mp.fabs(residual_pct) < 5 else ""
        print(f"  {name:35} {mp.nstr(val, 12):>20} "
              f"{mp.nstr(val_mev, 10):>16} {mp.nstr(residual_pct, 10):>13}%{marker}")
        results.append({
            "name": name,
            "value_m_e_units": str(val),
            "value_MeV": str(val_mev),
            "residual_pct": str(residual_pct),
        })

    print()

    # Find best
    best = min(candidates, key=lambda x: float(mp.fabs(x[1] - target_cat)))
    print(f"  CLOSEST: {best[0]} = {mp.nstr(best[1], 12)} "
          f"vs target {mp.nstr(target_cat, 12)}")
    print(f"  residual: {mp.nstr((best[1] - target_cat) / target_cat * 100, 8)} %")
    print()

    # Check if any candidate gets within 1%
    any_close = any(mp.fabs((v - target_cat) / target_cat) < mpf("0.01")
                    for _, v in candidates)
    if any_close:
        print("  *** AT LEAST ONE CANDIDATE WITHIN 1% — substrate derivation possible ***")
    else:
        print("  *** No single-formula candidate within 1% — (μ_d − μ_u)")
        print("      needs a categorical combination beyond simple Hoefsmit entries ***")

    # Witness
    w = (WitnessBuilder("probe-mu-d-minus-mu-u-categorical", engine="python+mpmath")
         .set_description("Test categorical candidates for (μ_d − μ_u) from V_(2,1) Hoefsmit"))
    w.add_data("q_pinned", str(q))
    w.add_data("hoefsmit_substrate", {"d_1": str(d_1), "d_2": str(d_2),
                                       "b_sq": str(b_sq), "b": str(b)})
    w.add_data("target", {
        "delta_m_CODATA_MeV": str(DELTA_M_CODATA_MEV),
        "prefactor": str(prefactor),
        "target_mu_d_minus_mu_u_m_e_units": str(target_cat),
    })
    w.add_data("candidates_tested", results)
    w.add_data("best_candidate", {
        "name": best[0],
        "value": str(best[1]),
        "residual_pct": str((best[1] - target_cat) / target_cat * 100),
    })
    w.add_assertion(
        "any_candidate_within_1_pct",
        computed=1.0 if any_close else 0.0,
        expected=1.0,
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
