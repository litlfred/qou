"""Δ_coupling closed-form: q-Edgeworth ansatz from q-CLT finite-A correction.

Per user direction: "q-CLT is in limit... has finite order. can we use?"

## Hypothesis

The framework's q-CLT (Blitvić + Marsh-Tsallis per
[`conj:q-clt-non-commutative`](#conj:q-clt-non-commutative)) gives the
n → ∞ limit of rescaled Hecke transfer-matrix sums under tr_M as a
q-Gaussian. The MAGIC-SHELL stabilization energy Δ_coupling captures
the over-binding of doubly-magic nuclei beyond the categorical T1-T6
prediction. At finite A, the q-Edgeworth correction to the q-Gaussian
limit provides natural candidates.

The q-Edgeworth expansion of the rescaled centred sum S_n at finite n:

  P_n(x) = p_qG(x) · [1 + κ_3^(q) · H_3(x) / √n + κ_4^(q) · H_4(x) / n + ...]

where κ_k^(q) are q-cumulants of σ_i under tr_M, H_k are q-Hermite
polynomials. The leading finite-n correction is O(1/√n).

For magic-shell binding at A_magic ∈ {2, 4, 8, 20, 28, ...}, the
correction at A = 4 (⁴He) is:

  Δ_coupling^Edgeworth(2, 2) ≈ E_0 · κ_3^(q_0) / √(A-2)
                              = E_0 · κ_3^(q_0) / √2

The q-cumulant κ_3 (q-skewness) is:
  κ_3^(q) = tr_M(σ̃_1^3) - 3·tr_M(σ̃_1)·Var(σ̃_1)
where σ̃_i = σ_i - z·1 is the centred Hecke generator.

## Computed values

  E_0(q_0)          = 4.18598 MeV
  Var(σ̃)(q_0)       = 0.85529   (per prop:centered-hecke-variance-positive)
  κ_3^(q_0)          = computed from tr_M(σ̃_1^3) (this probe)
  (A-2) factor at ⁴He = 2

  Hypothesis 1 (leading-form per PR #644):
    Δ_coupling(2,2) ≈ (A-2) · E_0 · log(1/h(q_0))
                    = 2 · 4.186 · 1.565 = 13.10 MeV   (gap +0.71%)

  Hypothesis 2 (q-Edgeworth — THIS PROBE):
    Δ_coupling(2,2) ≈ E_0 · κ_3^(q_0) / √(A-2)
                    = 4.186 · κ_3^(q_0) / √2

Target: Δ_coupling(2,2) = +13.20 MeV (extracted from AME).

## Output

q-edgeworth-delta-coupling-probe.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 90)
    print("  Δ_coupling closed-form: q-Edgeworth ansatz from finite-A q-CLT correction")
    print("=" * 90)
    print()

    q0 = mp.mpf(Q_50_DIGIT_STR)
    h_q0 = q0 - 1 / q0
    m_e = mp.mpf("0.51099895069")
    E_0 = m_e / (q0 * (q0 - 1))
    z_mark = 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))

    print(f"  q_0     = {mp.nstr(q0, 16)}")
    print(f"  h(q_0)  = {mp.nstr(h_q0, 16)}")
    print(f"  z(q_0)  = {mp.nstr(z_mark, 16)}")
    print(f"  m_e     = {mp.nstr(m_e, 14)} MeV")
    print(f"  E_0     = m_e / (q(q-1)) = {mp.nstr(E_0, 14)} MeV")
    print()

    # ─── q-cumulants of σ_i under tr_M ───
    # σ_1 in H_2: tr_M(σ_1) = z, so centred σ̃_1 has tr_M(σ̃_1) = 0.
    # σ_1^2 = (q-q⁻¹) σ_1 + 1 (Hecke); so tr_M(σ_1^2) = h·z + 1.
    # Var(σ_1) = tr_M(σ̃_1^2) = tr_M(σ_1^2) - z^2 = h·z + 1 - z^2.
    var = h_q0 * z_mark + 1 - z_mark ** 2
    print(f"  Var(σ̃)  = h·z + 1 - z^2 = {mp.nstr(var, 14)}")

    # σ_1^3 via Hecke iteration: σ_1^3 = (q-q⁻¹)·σ_1^2 + σ_1
    #                                = (q-q⁻¹)·((q-q⁻¹) σ_1 + 1) + σ_1
    #                                = ((q-q⁻¹)^2 + 1)·σ_1 + (q-q⁻¹)
    # So tr_M(σ_1^3) = ((q-q⁻¹)^2 + 1)·z + (q-q⁻¹)
    tr_sigma_cubed = (h_q0 ** 2 + 1) * z_mark + h_q0

    # Centred: σ̃_1 = σ_1 - z·1
    # tr_M(σ̃_1^3) = tr_M(σ_1^3) - 3·z·tr_M(σ_1^2) + 3·z^2·tr_M(σ_1) - z^3
    #             = tr_M(σ_1^3) - 3·z·(h·z + 1) + 3·z^3 - z^3
    #             = tr_M(σ_1^3) - 3·h·z^2 - 3·z + 2·z^3
    tr_sigma_tilde_cubed = tr_sigma_cubed - 3 * h_q0 * z_mark ** 2 - 3 * z_mark + 2 * z_mark ** 3
    kappa_3 = tr_sigma_tilde_cubed  # third central moment = third cumulant for a single variable
    print(f"  tr_M(σ_1^3) = (h^2+1)z + h = {mp.nstr(tr_sigma_cubed, 14)}")
    print(f"  κ_3 = tr_M(σ̃_1^3) = {mp.nstr(kappa_3, 14)}")
    print()

    # ─── q-Edgeworth Δ_coupling predictions ───
    A_minus_2 = 2  # for ⁴He doubly-magic anchor (Z=N=2 → A-2 = 2)
    delta_target = mp.mpf("13.20")  # extracted from AME at (2,2)

    print("  Δ_coupling(2,2) candidate forms — checked against extracted +13.20 MeV:")
    print()

    candidates = [
        ("H1: (A-2)·E_0·log(1/h)",
         A_minus_2 * E_0 * mp.log(1 / h_q0)),
        ("H2 (q-Edgeworth leading): E_0·κ_3/√(A-2)",
         E_0 * kappa_3 / mp.sqrt(A_minus_2)),
        ("H3 (q-Edgeworth × A-2): (A-2)·E_0·κ_3",
         A_minus_2 * E_0 * kappa_3),
        ("H4 (variance scaling): E_0·Var(σ̃)·log(1/h)",
         E_0 * var * mp.log(1 / h_q0)),
        ("H5 (cumulant × log): E_0·κ_3·log(1/h)",
         E_0 * kappa_3 * mp.log(1 / h_q0)),
        ("H6 (cumulant × A factor): (A-2)·E_0·κ_3·log(1/h)",
         A_minus_2 * E_0 * kappa_3 * mp.log(1 / h_q0)),
    ]

    results = []
    for name, value in candidates:
        gap_pct = abs(value - delta_target) / delta_target * 100
        within_1_pct = bool(gap_pct < 1.0)
        marker = " <-- WITHIN 1%" if within_1_pct else ""
        print(f"  {name:<60} = {float(value):>+12.6f}   gap = {float(gap_pct):>7.3f}%{marker}")
        results.append({
            "name": name,
            "value_MeV": float(value),
            "gap_pct_vs_13_20": float(gap_pct),
            "within_1_pct": within_1_pct,
        })
    print()
    print(f"  Extracted target:                                     = {float(delta_target):>+12.4f} MeV")
    print()

    builder = (
        WitnessBuilder("q-edgeworth-delta-coupling-probe", engine="mpmath")
        .set_description(
            "Δ_coupling closed-form q-Edgeworth ansatz probe. Tests 6 "
            "candidate forms built from q-cumulants of σ_i under tr_M "
            "(per the q-CLT framework on main, prop:hecke-satisfies-"
            "blitvic-hypothesis + prop:centered-hecke-variance-positive). "
            "H1 reproduces PR #644's leading-form. H2-H6 are new q-"
            "Edgeworth-derived candidates from the κ_3 q-skewness."
        )
        .set_audit_only(
            "docs/audits/2026-05-12-1ppb-implementation-plan.md"
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("delta_coupling_target_MeV", float(delta_target))
        .add_data("E_0_MeV", float(E_0))
        .add_data("h_q0", float(h_q0))
        .add_data("z_mark", float(z_mark))
        .add_data("variance_sigma_tilde", float(var))
        .add_data("kappa_3_skewness", float(kappa_3))
        .add_data("A_minus_2_at_4He_anchor", A_minus_2)
        .add_data("candidates", results)
        .add_assertion(
            name="H1_leading_form_within_1_pct",
            computed=results[0]['within_1_pct'],
            expected=True,
            source="(A-2)·E_0·log(1/h) ≈ 13.10 MeV vs target 13.20 MeV (0.71% gap)",
        )
        .add_caveat(
            "The q-Edgeworth ansatz (H2-H6) tests whether finite-A "
            "corrections to the q-Gaussian CLT limit can produce "
            "Δ_coupling. None of H2-H6 hits <1% in this single-anchor "
            "probe; cross-anchor verification on (2,1) ³He=D+p and (1,2) "
            "T=D+n requires PR #644's Δ_cat data which is not on main. "
            "H1 remains the leading candidate at the (2,2) anchor."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
