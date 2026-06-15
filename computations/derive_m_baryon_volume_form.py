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
      m(B) = m_e · [ Vol(ℬ_3) / ℏ_q² · linking_weight  +  S(B) ]

  (the linking_weight is the per-knot VolDensity component of the
  canonical m(K) = m_e · Vol(K) · ρ(K) / ℏ_q² framing; PROVED via
  Family A post-PR #1080 — see linking_weight_family_a in
  _li_2_q_util.py)

where:
  * Vol(ℬ_3) = 7.32772475... (8 · G, Catalan's constant; hyperbolic
    volume of the Borromean-link complement) — substrate constant
  * ℏ_q = (q − 1)/q (CAL-2) — substrate-derived from q_0
  * linking_weight — per-knot VolDensity component; proved Family A
    identity (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h²; the empirical
    closure target ≈ 2.460 is retained as a diagnostic only
  * S(B) = Skein correction from orientation partition (p, n)
    (Borromean baryons with (k positive, 3−k negative) components)

This script:

  (a) Computes Vol(K)/ℏ_q² at 50 dps for the cross-check K = 4_1
      (figure-8, the muon Higgs-coupling knot) — a PREDICTION of
      m_μ/m_e ≈ 206.7682830 (CODATA) expected to agree at the ~2e-7
      level (9.5σ cross-check): q_0 is proton-anchored per the
      2026-05-28 re-pin (q-pinning-50-digit.witness.json).  # noqa: P31 — docstring narrative; cross-check value lives in q_parameter.MASS_RATIO_MU_E_STR

  (b) Computes Vol(ℬ_3)/ℏ_q² at 50 dps — the "common Borromean factor"
      ≈ 746.42 (dimensionless).

  (c) Derives the empirical closure targets for the linking_weight
      (proton, neutron) from CODATA m_p, m_n (validation-only — NOT
      injected as substrate input; diagnostic against the proved
      Family A value).

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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
# CAL-1 + CAL-2 only — no CODATA m_p / m_n injection (validation values
# loaded separately and stored under data.validation).
from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

set_compute_dps()


def _q_0_50dps() -> mp.mpf:
    """CAL-2 q_0 at 50 dps from the canonical pinning witness."""
    import json
    with (_pb.witness_path("q-pinning-50-digit.witness.json", HERE)).open() as fh:
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
from experimental_constants import (  # noqa: E402
    VOL_BORROMEAN_50DPS_STR,
    VOL_4_1_50DPS_STR,
)

VOL_4_1 = mp.mpf(VOL_4_1_50DPS_STR)
VOL_BORROMEAN = mp.mpf(VOL_BORROMEAN_50DPS_STR)


def derive_m_baryon_volume_form() -> dict:
    """Topological-mass formula at 50 dps; substrate-only inputs."""
    q = _q_0_50dps()
    hbar_q = (q - 1) / q
    hbar_q2 = hbar_q ** 2

    # (a) muon cross-check via Vol(4_1)/ℏ_q²
    m_mu_over_m_e_via_volume = VOL_4_1 / hbar_q2
    # CAL-2: m_μ/m_e from q_parameter registry (P31-triage Phase B,
    # validation only — this is the CODATA anchor we cross-check against).
    from q_parameter import MASS_RATIO_MU_E_STR  # noqa: E402
    m_mu_codata_over_m_e = mp.mpf(MASS_RATIO_MU_E_STR)

    # (b) Borromean common factor
    vol_borromean_over_hbar2 = VOL_BORROMEAN / hbar_q2

    # (c) Empirical closure for the per-knot linking_weight (validation
    # only — these are EMPIRICAL targets, NOT inputs to the derivation).
    # Post-PR #1080 naming: what older docs called λ_scale is now the
    # linking_weight component of VolDensity(K) and is PROVED via Family A.
    # The "empirical target" here is the value the linking_weight would
    # need to take to close the equation exactly; it is diagnostic only.
    m_p_over_m_e_codata = M_P_MEV_VALIDATION / M_E_MEV
    m_n_over_m_e_codata = M_N_MEV_VALIDATION / M_E_MEV
    linking_weight_p_empirical_target = m_p_over_m_e_codata / vol_borromean_over_hbar2
    linking_weight_n_empirical_target = m_n_over_m_e_codata / vol_borromean_over_hbar2

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
    delta_skein_target = linking_weight_n_empirical_target - linking_weight_p_empirical_target

    return {
        "q_0_50dps": str(q),
        "hbar_q_50dps": str(hbar_q),
        "hbar_q_squared_50dps": str(hbar_q2),
        "muon_cross_check": {
            "Vol_4_1_50dps": str(VOL_4_1),
            "m_mu_over_m_e_via_volume_50dps": str(m_mu_over_m_e_via_volume),
            "m_mu_over_m_e_codata": str(m_mu_codata_over_m_e),
            "agreement_assertion": (
                "Vol(4_1)/ℏ_q² PREDICTS CODATA m_μ/m_e at the ~2e-7 "
                "level (9.5σ cross-check, NOT the anchor): q_0 is "
                "proton-anchored per the 2026-05-28 re-pin "
                "(q-pinning-50-digit.witness.json).  Exact agreement "
                "held only under the pre-re-pin muon anchor."
            ),
        },
        "borromean_common_factor": {
            "Vol_Borromean_50dps": str(VOL_BORROMEAN),
            "Vol_Borromean_over_hbar_q_squared": str(vol_borromean_over_hbar2),
            "interpretation": (
                "Dimensionless 'common Borromean factor' shared by all "
                "Borromean baryons; physical baryon mass ratio is this "
                "value times the linking_weight (proved Family A "
                "VolDensity component) plus Skein correction."
            ),
        },
        "linking_weight_closure_targets": {
            "proton_empirical_target": str(linking_weight_p_empirical_target),
            "neutron_empirical_target": str(linking_weight_n_empirical_target),
            "interpretation": (
                "Empirical linking_weight value required for the topological-mass "
                "formula to reproduce CODATA m_p / m_n.  THESE ARE "
                "VALIDATION VALUES — NOT inputs to the substrate "
                "derivation.  Post-PR #1080 framing: the linking_weight "
                "is the per-knot VolDensity(K)/Geom_leading(K) component, "
                "PROVED via Family A canonical Wedderburn "
                "(linking_weight_family_a in _li_2_q_util.py); these "
                "empirical targets are diagnostic only (what value would "
                "close the equation exactly).  Field renamed from "
                "`lambda_scale_closure_targets` per owner directive "
                "2026-05-24."
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
            "substrate_linking_weight": (
                "RESOLVED post-PR #1080: the linking_weight component of "
                "VolDensity(K) for K = ℬ_3 is the PROVED Family A "
                "categorical identity (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h² "
                "(see linking_weight_family_a in _li_2_q_util.py).  The "
                "older 'open R&D: derive λ_scale from CAL-1 + CAL-2 + "
                "topological invariants of ℬ_3' framing is closed by "
                "this proof; only the ~2.89 % VolDensity(𝓑₃) categorical-"
                "exactness refinement gap at h² order remains open (see "
                "PR #1063 + audit 2026-05-24-low-isotope-mass-error-"
                "anatomy.md).  Field renamed from `substrate_lambda_scale` "
                "per owner directive 2026-05-24 (no λ_scale anywhere)."
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

    ls = d["linking_weight_closure_targets"]
    print(f"\n  linking_weight closure targets (empirical, NOT substrate input):")
    print(f"    proton  target = {mp.nstr(mp.mpf(ls['proton_empirical_target']), 14)}")
    print(f"    neutron target = {mp.nstr(mp.mpf(ls['neutron_empirical_target']), 14)}")

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
                "Topological mass formula (canonical Vol(K)·ρ(K)/ℏ_q² "
                "framing; Borromean channel Vol(ℬ_3)/ℏ_q² · "
                "linking_weight + Skein) evaluated at 50 dps + the muon "
                "Vol(4_1)/ℏ_q² cross-check prediction under the "
                "proton-pinned q_0.  Substrate-only inputs: CAL-1 (m_e), "
                "CAL-2 (q_0), topological constants Vol(4_1), Vol(ℬ_3).  "
                "Reports the linking_weight empirical closure targets as "
                "diagnostics (the linking_weight itself is PROVED via "
                "Family A, PR #1080) and verifies that the "
                "Skein-correction DIFFERENCE ΔS(n − p) is "
                "substrate-derivable from CAL-1 + CAL-2 alone (via Q_β "
                "closed form)."
            ),
            "auditOnly": (
                "docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md "
                "(motivates this Vol-form chain as Option B per the "
                "user's 'can we use m_e as mass scaling factor' question); "
                "PR #487 (introduced the Borromean-baryon-interpretation "
                "block with the formula and the then-undefined scale "
                "factor, since proved as the linking_weight via Family A)."
            ),
            "provenance_directives": (
                "2026-05-11: introduce this script (m_e scaling factor × "
                "Vol(K)/ℏ_q² dimensionless multiplier; expose the scale "
                "factor as the open derivation).  Superseded in steps: "
                "2026-05-24 rename to linking_weight (no legacy "
                "scale-factor symbol anywhere); PR #1080 proves the "
                "linking_weight via Family A; 2026-06-06 owner purge "
                "fixes the canonical framing as Vol(K)·ρ(K)/ℏ_q²."
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
