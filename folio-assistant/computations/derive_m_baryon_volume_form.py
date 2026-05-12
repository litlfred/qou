#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-mpmath consumer of topological
# invariants (Vol(B_3), Vol(4_1)) and CAL-1+CAL-2 only.
"""Derive m_p / m_n via the canonical Borromean-baryon topological mass
formula at 50 dps — Option B implementation per PR #640 follow-up
2026-05-11.

Per [`borromean-baryon-interpretation.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-interpretation.md)
(introduced by PR #487) and [`topological-mass-trefoil.md`](../../content/quantum-observable-universe/braids-and-knots/topological-mass-trefoil.md):

  Leptons (single knot K with hyperbolic volume):
      m(K) = m_e · Vol(K) / ℏ_q²

  Baryons (Borromean linking ℬ_3):
      m(B) = m_e · [ Vol(ℬ_3) / ℏ_q² · λ_scale  +  S(B) ]

where:
  * Vol(ℬ_3) = 7.32772475... (8 · Cl_2(π/3); hyperbolic volume of the
    Borromean-link complement) — substrate constant
  * ℏ_q = (q − 1)/q (CAL-2) — substrate-derived from q_0
  * λ_scale — common Borromean-baryon scale; substrate-derivable in
    principle (open; closure target ≈ 2.460 from empirical m_p/m_e)
  * S(B) = Skein correction from orientation partition (p, n)
    (Borromean baryons with (k positive, 3−k negative) components)

This script:

  (a) Computes Vol(K)/ℏ_q² at 50 dps for the cross-check K = 4_1
      (figure-8, the muon Higgs-coupling knot) — should reproduce
      m_μ/m_e ≈ 206.7682830 (CODATA, CAL-2 anchor) to all digits.  # noqa: P31 — docstring narrative; CAL-2 anchor lives in q_parameter.MASS_RATIO_MU_E_STR

  (b) Computes Vol(ℬ_3)/ℏ_q² at 50 dps — the "common Borromean factor"
      ≈ 746.42 (dimensionless).

  (c) Derives the empirical closure targets for λ_scale (proton) and
      λ_scale (neutron) from CODATA m_p, m_n (validation-only — NOT
      injected as substrate input).

  (d) Records the SUBSTRATE-DERIVABLE Skein difference:
      ΔS(n − p) = (Q_β + m_e) / m_e · ℏ_q² / Vol(ℬ_3)
      uses CAL-1 m_e, CAL-2 q_0 (via Q_β closed form), and the
      topological constant Vol(ℬ_3). No m_p, m_n input.

Outputs `m-baryon-volume-form.witness.json`.

This is the **canonical** topological mass-formula path; the
T1+T4 cat-units chain (build_proton/neutron_mass_50dps_chain.py)
is the **legacy "operator-sum" path** which has the implicit
ansatz "cat-units ratio = mass ratio" (off by ~1570× at q_0).
The Vol form is the path the paper actually documents
(`topological-mass-trefoil`, `borromean-baryon-interpretation`,
`skein-mass-from-linking`).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# CAL-1 + CAL-2 only — no CODATA m_p / m_n injection (validation values
# loaded separately and stored under data.validation).
from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 50


def _q_0_50dps() -> mp.mpf:
    """CAL-2 q_0 at 50 dps from the canonical pinning witness."""
    import json
    with (HERE / "q-pinning-50-digit.witness.json").open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def _q_beta_closed_form(q: mp.mpf) -> mp.mpf:
    """Q_β predicted from CAL-1 m_e + CAL-2 q_0 alone (per
    `derived_masses.q_beta_predicted_mev`, single-wrap symbolic form
    from `prop:neutron-qvalue-symbolic`)."""
    return M_E_MEV * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


# Hyperbolic-volume topological constants (50-dps values from
# SnapPy / Hoste–Thistlethwaite tables, identical to
# `binding_canonical.py`):
#   Vol(4_1)  = 2 · Cl_2(π/3) where Cl_2 is the Clausen function
#               (figure-8 knot complement, 2 ideal tetrahedra).
#   Vol(ℬ_3) = 8 · G          where G is Catalan's constant
#               (Borromean rings complement, 8 ideal octahedra).
# Both are standard hyperbolic-volume identities; the closed forms
# match the SnapPy numerical values to 50 dps.
VOL_4_1 = mp.mpf("2.02988321281930725004240510854904057483004159909893")
VOL_BORROMEAN = mp.mpf("7.32772475587766148235147121870981010907842498879866")


def derive_m_baryon_volume_form() -> dict:
    """Topological-mass formula at 50 dps; substrate-only inputs."""
    q = _q_0_50dps()
    hbar_q = (q - 1) / q
    hbar_q2 = hbar_q ** 2

    # (a) muon cross-check via Vol(4_1)/ℏ_q²
    m_mu_over_m_e_via_volume = VOL_4_1 / hbar_q2
    m_mu_codata_over_m_e = mp.mpf("206.7682830")  # CODATA, validation only

    # (b) Borromean common factor
    vol_borromean_over_hbar2 = VOL_BORROMEAN / hbar_q2

    # (c) Empirical closure for λ_scale per particle (validation only —
    # these are EMPIRICAL targets, NOT inputs to the derivation).
    m_p_over_m_e_codata = M_P_MEV_VALIDATION / M_E_MEV
    m_n_over_m_e_codata = M_N_MEV_VALIDATION / M_E_MEV
    lambda_scale_p_target = m_p_over_m_e_codata / vol_borromean_over_hbar2
    lambda_scale_n_target = m_n_over_m_e_codata / vol_borromean_over_hbar2

    # (d) Substrate-derivable Skein-correction difference:
    # ΔS(n − p) = (m_n − m_p)/m_e / (Vol(ℬ_3)/ℏ_q²)
    #           = (Q_β + m_e) / (m_e · Vol(ℬ_3)/ℏ_q²)
    # Uses CAL-1 (m_e), CAL-2 (q_0 → Q_β via closed form), and the
    # topological constant Vol(ℬ_3). No CODATA m_p, m_n input.
    q_beta_pred = _q_beta_closed_form(q)
    delta_skein_n_minus_p_derived = (
        (q_beta_pred + M_E_MEV) / M_E_MEV / vol_borromean_over_hbar2
    )

    # Validation: ΔS_target = λ_scale(n) − λ_scale(p)
    delta_skein_target = lambda_scale_n_target - lambda_scale_p_target

    return {
        "q_0_50dps": str(q),
        "hbar_q_50dps": str(hbar_q),
        "hbar_q_squared_50dps": str(hbar_q2),
        "muon_cross_check": {
            "Vol_4_1_50dps": str(VOL_4_1),
            "m_mu_over_m_e_via_volume_50dps": str(m_mu_over_m_e_via_volume),
            "m_mu_over_m_e_codata": str(m_mu_codata_over_m_e),
            "agreement_assertion": (
                "Vol(4_1)/ℏ_q² should reproduce CODATA m_μ/m_e exactly "
                "(this IS the CAL-2 q_0 calibration); checks the "
                "topological-mass formula's correctness."
            ),
        },
        "borromean_common_factor": {
            "Vol_Borromean_50dps": str(VOL_BORROMEAN),
            "Vol_Borromean_over_hbar_q_squared": str(vol_borromean_over_hbar2),
            "interpretation": (
                "Dimensionless 'common Borromean factor' shared by all "
                "Borromean baryons; physical baryon mass ratio is this "
                "value times the substrate λ_scale plus Skein correction."
            ),
        },
        "lambda_scale_closure_targets": {
            "proton_empirical_target": str(lambda_scale_p_target),
            "neutron_empirical_target": str(lambda_scale_n_target),
            "interpretation": (
                "Empirical λ_scale value required for the topological-mass "
                "formula to reproduce CODATA m_p / m_n.  THESE ARE "
                "VALIDATION VALUES — NOT inputs to the substrate "
                "derivation.  The substrate-derived λ_scale (from CAL-1 "
                "+ CAL-2 alone) is OPEN; PR #487 introduced the formula "
                "but never defined λ_scale.  Open R&D item — see "
                "docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md."
            ),
        },
        "skein_correction_n_minus_p": {
            "delta_skein_derived_from_CAL_1_CAL_2": str(delta_skein_n_minus_p_derived),
            "delta_skein_empirical_target": str(delta_skein_target),
            "agreement_assertion": (
                "ΔS(n − p) = (Q_β + m_e)/m_e / (Vol(ℬ_3)/ℏ_q²).  "
                "Substrate-derived from CAL-1 (m_e), CAL-2 (q_0 → Q_β "
                "via prop:neutron-qvalue-symbolic), and topological "
                "constant Vol(ℬ_3).  Empirical target is "
                "(m_n − m_p)/m_e / (Vol(ℬ_3)/ℏ_q²); the two should agree "
                "since Q_β = m_n − m_p − m_e by definition."
            ),
        },
        "open_R_and_D": {
            "substrate_lambda_scale": (
                "Derive λ_scale from CAL-1 + CAL-2 + topological invariants "
                "of ℬ_3 alone.  Empirical closure target ≈ 2.460.  "
                "Candidates checked at q_0 (from the candidate sweep in "
                "the linked audit) — none of [n]_q, q^k, m_μ/m_e/84, etc. "
                "matches to better than 0.06%.  Open."
            ),
            "substrate_skein_correction_per_orientation": (
                "Derive S(p), S(n) (not just the difference) from the "
                "Borromean orientation partition (k positive, 3-k negative) "
                "via the Skein polynomial.  Empirical: |S(n) − S(p)| ≈ "
                "0.00339 dimensionless; the difference IS substrate-"
                "derivable per ΔS formula above.  Open: the individual "
                "S(p), S(n) anchored to a common substrate quantity."
            ),
        },
    }


def main() -> int:
    print("=" * 78)
    print(" Topological-mass formula at 50 dps — Borromean baryon path")
    print("=" * 78)
    d = derive_m_baryon_volume_form()

    print(f"\n  q_0  = {mp.nstr(mp.mpf(d['q_0_50dps']), 14)}")
    print(f"  ℏ_q² = {mp.nstr(mp.mpf(d['hbar_q_squared_50dps']), 14)}")

    mu = d["muon_cross_check"]
    print(f"\n  Muon cross-check (CAL-2 anchor):")
    print(f"    Vol(4_1)/ℏ_q² = {mp.nstr(mp.mpf(mu['m_mu_over_m_e_via_volume_50dps']), 14)}")
    print(f"    CODATA m_μ/m_e = {mu['m_mu_over_m_e_codata']}")
    err = abs(mp.mpf(mu['m_mu_over_m_e_via_volume_50dps']) - mp.mpf(mu['m_mu_over_m_e_codata']))
    err_ppm = err / mp.mpf(mu['m_mu_over_m_e_codata']) * mp.mpf("1e6")
    print(f"    Agreement: |Δ| = {mp.nstr(err, 6)}  ({mp.nstr(err_ppm, 4)} ppm)")

    b = d["borromean_common_factor"]
    print(f"\n  Borromean common factor:")
    print(f"    Vol(ℬ_3)/ℏ_q² = {mp.nstr(mp.mpf(b['Vol_Borromean_over_hbar_q_squared']), 14)}")

    ls = d["lambda_scale_closure_targets"]
    print(f"\n  λ_scale closure targets (empirical, NOT substrate input):")
    print(f"    proton  λ_target = {mp.nstr(mp.mpf(ls['proton_empirical_target']), 14)}")
    print(f"    neutron λ_target = {mp.nstr(mp.mpf(ls['neutron_empirical_target']), 14)}")

    ss = d["skein_correction_n_minus_p"]
    print(f"\n  Skein-difference ΔS(n − p):")
    print(f"    derived (from CAL-1+CAL-2+Vol(ℬ_3)) = "
          f"{mp.nstr(mp.mpf(ss['delta_skein_derived_from_CAL_1_CAL_2']), 14)}")
    print(f"    empirical target                  = "
          f"{mp.nstr(mp.mpf(ss['delta_skein_empirical_target']), 14)}")
    delta_err = abs(
        mp.mpf(ss['delta_skein_derived_from_CAL_1_CAL_2'])
        - mp.mpf(ss['delta_skein_empirical_target'])
    )
    print(f"    |Δ| = {mp.nstr(delta_err, 6)}  "
          f"(ppm: {mp.nstr(delta_err / mp.mpf(ss['delta_skein_empirical_target']) * mp.mpf('1e6'), 4)})")

    # WitnessBuilder wrapping
    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        "m-baryon-volume-form",
        {
            "description": (
                "Topological mass formula (Vol(K)/ℏ_q² · λ_scale + Skein) "
                "evaluated at 50 dps for the Borromean baryon channel + "
                "the muon Vol(4_1)/ℏ_q² cross-check.  Substrate-only "
                "inputs: CAL-1 (m_e), CAL-2 (q_0), topological constants "
                "Vol(4_1), Vol(ℬ_3).  Reports the open λ_scale closure "
                "target empirically and verifies that the Skein-correction "
                "DIFFERENCE ΔS(n − p) is substrate-derivable from CAL-1 + "
                "CAL-2 alone (via Q_β closed form)."
            ),
            "auditOnly": (
                "docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md "
                "(motivates this Vol-form chain as Option B per the "
                "user's 'can we use m_e as mass scaling factor' question); "
                "PR #487 (introduced the Borromean-baryon-interpretation "
                "block with the formula and undefined λ_scale)."
            ),
            "owner_directive_2026_05_11": (
                "Re-implement using m_e as scaling factor + Vol(K)/ℏ_q² "
                "as dimensionless multiplier per the canonical "
                "topological-mass formula; expose λ_scale as the single "
                "open derivation needed for 1ppb on individual hadron masses."
            ),
            "data": d,
        },
        script_path=__file__,
        engine="mpmath",
    )
    out_path = builder.save()
    print(f"\n  Wrote {Path(out_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
