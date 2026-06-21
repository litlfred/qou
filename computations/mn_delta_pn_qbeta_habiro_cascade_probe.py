#!/usr/bin/env python3
"""mn_delta_pn_qbeta_habiro_cascade_probe.py — does the c_3 [3]_q/25 Habiro
closure cascade to close m_n + Δ_pn?

EXPLORATORY probe (task 3 of the 2026-06-04 Habiro follow-up). NOT a wire
decision — quantifies the cascade the "shared root" audit
(`docs/audits/2026-06-03-m-n-delta-pn-qbeta-cal-anchored-acceptance.md`)
predicts.

## The cascade chain

Both m_n and Δ_pn are derived from Q_β via **Path C**:

    m_n   = m_p(substrate) + Q_β + m_e
    Δ_pn  =                  Q_β + m_e

so any Q_β error propagates 1:1 into both observables' ABSOLUTE error.

## The three Q_β variants compared

The Q_β precision ladder is `Q_β = Q_base · Π_k (1 + c_k · u^k)`, `u = b·ℏ_q²`.

| Variant | c_3 source | tier |
|---------|-----------|------|
| N2 | only c_2 = -1 wired (PROVED) | derived (production headline) |
| N3-cal | c_3 = -2.0693… extracted from CODATA Q_β | cal-anchored (circular) |
| N3-Habiro | c_3 from the 3-rung `[3]_q/25` closure (PR #1781) | NEAR-MATCH (2.65 ppm) |

The N3-Habiro c_3 is computed here from the closed form
`c_3 = -(q²+q⁻²)·(1 + ℏ_q·[3]_q/25 + ℏ_q³/[2]_q)` (matches
`MmuR9V9Closure.lean` `qbetaC3Closure`).

## Question

If the c_3 rung were wired (cal-anchored OR the Habiro near-match),
how far do m_n + Δ_pn move toward their 100× L2 targets? And how close
is the Habiro near-match to the cal-anchored rung (i.e. how much
precision does the 2.65 ppm c_3 residual cost downstream)?

## Δ_λ-gate

No fitted form wired. c_3 stays cal-anchored in production; this probe
only QUANTIFIES the cascade to inform the promotion-path priority.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt  # noqa: E402
from codata_constants import (  # noqa: E402 — canonical CODATA registry
    M_E_MEV,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
)

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# CODATA targets (MeV) + 1σ experimental.
Q_BETA_CODATA = "0.78233341"
Q_BETA_SIGMA = "6.1e-7"
M_E = M_E_MEV                  # 0.51099895069 (codata_constants)
M_P_CODATA = M_P_MEV_VALIDATION  # 938.27208816 (codata_constants)
M_N_CODATA = M_N_MEV_VALIDATION  # 939.56542052 (codata_constants)
M_N_SIGMA = "5.4e-7"
DELTA_PN_SIGMA = "5.4e-7"  # dominated by m_n σ (m_p far better known)

# Q_β ladder rung values from qbeta/qbeta-ck-cache.witness.json.
Q_N2 = "0.782334410277840137760143636388"  # c_2 only, DERIVED
Q_N3_CAL = "0.78233341"                     # c_3 cal-anchored
C3_TARGET = "-2.06934257711516783787971951725"  # cal-anchored c_3


def quantum_int(n: int, q: mpf) -> mpf:
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def c3_habiro(q: mpf) -> mpf:
    """3-rung Habiro closure for c_3 (matches MmuR9V9Closure.qbetaC3Closure)."""
    hbar = (q - 1) / q
    base = -(q ** 2 + q ** (-2))
    rung1 = hbar * quantum_int(3, q) / 25
    rung2 = hbar ** 3 / quantum_int(2, q)
    return base * (1 + rung1 + rung2)


def miss_factor(pred: mpf, codata: mpf, sigma: mpf) -> float:
    target = sigma / 100  # 100× L2 target (absolute)
    return float(abs(pred - codata) / target)


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mn-delta-pn-qbeta-habiro-cascade-probe", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    me = mpf(M_E)
    m_p = mpf(M_P_CODATA)
    q_codata = mpf(Q_BETA_CODATA)
    q_sigma = mpf(Q_BETA_SIGMA)
    m_n_codata = mpf(M_N_CODATA)
    m_n_sigma = mpf(M_N_SIGMA)
    delta_codata = m_n_codata - m_p
    delta_sigma = mpf(DELTA_PN_SIGMA)

    q_n2 = mpf(Q_N2)
    q_n3_cal = mpf(Q_N3_CAL)
    c3_cal = mpf(C3_TARGET)

    # Habiro c_3 + the implied Q_β via the ratio method (no need for u):
    #   Q_N3 = Q_N2 · (1 + c_3·u³);  c_3·u³ = Q_N3_cal/Q_N2 − 1.
    #   Q_N3_habiro = Q_N2 · (1 + (c_3_habiro/c_3_cal)·(Q_N3_cal/Q_N2 − 1)).
    c3_hab = c3_habiro(q)
    c3_residual_ppm = float(abs(c3_hab - c3_cal) / abs(c3_cal) * 1e6)
    c3_rung_factor_cal = q_n3_cal / q_n2 - 1            # = c_3_cal·u³
    q_n3_habiro = q_n2 * (1 + (c3_hab / c3_cal) * c3_rung_factor_cal)

    print("=" * 78)
    print(" m_n + Δ_pn ← Q_β c_3 Habiro cascade probe")
    print("=" * 78)
    print(f"  q₀            = {mp.nstr(q, 14)}")
    print(f"  c_3 cal       = {mp.nstr(c3_cal, 16)}")
    print(f"  c_3 Habiro    = {mp.nstr(c3_hab, 16)}  ({c3_residual_ppm:.3f} ppm)")
    print()
    print(f"  Q_β CODATA    = {mp.nstr(q_codata, 12)} ± {mp.nstr(q_sigma, 3)} MeV")
    print(f"  Q_β N2        = {mp.nstr(q_n2, 16)} MeV")
    print(f"  Q_β N3-cal    = {mp.nstr(q_n3_cal, 16)} MeV")
    print(f"  Q_β N3-Habiro = {mp.nstr(q_n3_habiro, 16)} MeV")
    print(f"  |N3hab − N3cal| = {mp.nstr(abs(q_n3_habiro - q_n3_cal), 4)} MeV")
    print()

    variants = {
        "N2 (c_2 only, DERIVED, production)": q_n2,
        "N3-cal (c_3 cal-anchored)": q_n3_cal,
        "N3-Habiro (c_3 [3]_q/25 near-match)": q_n3_habiro,
    }

    print("─" * 78)
    print(f"  {'Q_β variant':<38} {'Q_β miss':>9} {'m_n miss':>9} {'Δ_pn miss':>10}")
    print("─" * 78)
    results = {}
    for name, q_beta in variants.items():
        m_n_pred = m_p + q_beta + me
        delta_pred = q_beta + me
        q_miss = miss_factor(q_beta, q_codata, q_sigma)
        m_n_miss = miss_factor(m_n_pred, m_n_codata, m_n_sigma)
        d_miss = miss_factor(delta_pred, delta_codata, delta_sigma)
        flag = lambda m: "PASS" if m <= 1.0 else f"{m:.0f}x"  # noqa: E731
        print(f"  {name:<38} {flag(q_miss):>9} {flag(m_n_miss):>9} {flag(d_miss):>10}")
        results[name] = {
            "Q_beta_MeV": mp.nstr(q_beta, 24),
            "Q_beta_miss_factor": q_miss,
            "m_n_pred_MeV": mp.nstr(m_n_pred, 18),
            "m_n_miss_factor": m_n_miss,
            "delta_pn_pred_MeV": mp.nstr(delta_pred, 18),
            "delta_pn_miss_factor": d_miss,
        }

    print()
    print("=" * 78)
    print(" FINDINGS")
    print("=" * 78)

    # Cascade confirmation: Q_β error == m_n abs error == Δ_pn abs error.
    n2 = results["N2 (c_2 only, DERIVED, production)"]
    n3c = results["N3-cal (c_3 cal-anchored)"]
    cascade_ratio_mn = n2["m_n_miss_factor"] / n2["Q_beta_miss_factor"]
    print(f"  1. Cascade is 1:1 — at N2, m_n miss / Q_β miss = "
          f"{cascade_ratio_mn:.3f} (≈ σ_exp ratio, NOT independent error).")
    print(f"  2. c_3 rung closes Q_β from {n2['Q_beta_miss_factor']:.0f}x "
          f"→ {n3c['Q_beta_miss_factor']:.2f}x (cal-anchored).")
    print(f"  3. Habiro c_3 residual {c3_residual_ppm:.2f} ppm costs only "
          f"{mp.nstr(abs(q_n3_habiro - q_n3_cal), 3)} MeV on Q_β "
          f"(≪ σ_exp = {mp.nstr(q_sigma, 3)} MeV).")
    print(f"  4. ⇒ IF the [3]_q/25 c_3 closure were DERIVED (not cal-anchored),")
    print(f"       it would close Q_β + m_n + Δ_pn simultaneously — the")
    print(f"       'shared root' made quantitative.")
    print(f"  CAVEAT: c_3 is cal-anchored (circular: extracted from CODATA Q_β).")
    print(f"  The Habiro near-match is the candidate derivation; promotion is")
    print(f"  gated on the KLR/crystal infra (PR #1791 scaffolds). NO wire here.")

    habiro_vs_cal_q_MeV = float(abs(q_n3_habiro - q_n3_cal))

    wb.add_assertion(
        "habiro_c3_reproduces_calanchored_qbeta_within_sigma",
        computed=habiro_vs_cal_q_MeV < float(q_sigma),
        expected=True,
        source="The 3-rung [3]_q/25 Habiro c_3 (2.65 ppm near-match) must "
               "reproduce the cal-anchored Q_β to within σ_exp, confirming the "
               "c_3 residual is downstream-negligible.",
    )
    wb.add_assertion(
        "cascade_is_one_to_one_mn_vs_qbeta",
        computed=abs(cascade_ratio_mn - 1.0) < 0.5,
        expected=True,
        source="m_n miss factor / Q_β miss factor ≈ 1 (modulo σ_exp ratio) — "
               "confirms m_n absolute error is the propagated Q_β error, not "
               "an independent gap.",
    )

    wb.add_data("q_substrate", mp.nstr(q, 30))
    wb.add_data("c3_cal_anchored", mp.nstr(c3_cal, 30))
    wb.add_data("c3_habiro_3rung", mp.nstr(c3_hab, 30))
    wb.add_data("c3_habiro_residual_ppm", c3_residual_ppm)
    wb.add_data("Q_beta_N2_MeV", mp.nstr(q_n2, 30))
    wb.add_data("Q_beta_N3_cal_MeV", mp.nstr(q_n3_cal, 30))
    wb.add_data("Q_beta_N3_habiro_MeV", mp.nstr(q_n3_habiro, 30))
    wb.add_data("habiro_vs_cal_qbeta_diff_MeV", mp.nstr(abs(q_n3_habiro - q_n3_cal), 30))
    wb.add_data("per_variant_results", results)
    wb.add_data("cascade_ratio_mn_over_qbeta", cascade_ratio_mn)
    wb.add_data("interpretation", (
        "Cascade confirmed 1:1 — Q_β error propagates linearly into m_n + Δ_pn "
        "absolute errors via Path C. The c_3 rung closes Q_β to cal-anchored "
        f"precision; the 3-rung [3]_q/25 Habiro near-match ({c3_residual_ppm:.2f} "
        "ppm on c_3) reproduces it to "
        f"{mp.nstr(abs(q_n3_habiro - q_n3_cal), 3)} MeV (≪ σ_exp). IF derived, "
        "the [3]_q/25 closure would close all three observables. c_3 remains "
        "cal-anchored in production; promotion gated on KLR/crystal infra. "
        "NO fitted form wired."
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"{'all passed' if all(a.passed for a in wb.assertions) else 'FAILURES'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
