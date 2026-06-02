#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation script; computes electron
# Hecke-cat-unit mass at H_2 from substrate (CAL-1 + CAL-2 only).
"""Workplan 2 Phase 2 — derive `m_e_Hecke` from substrate (no fitting).

The electron is the canonical 2-strand atomic braid in H_2(q): the
identity (zero crossings). Its Markov trace and Frobenius co-
Casimir are computable in closed form from CAL-1 m_e and CAL-2 q_0
alone — no upstream witness needed.

══════════════════════════════════════════════════════════════════
 ELECTRON AT H_2 — CLOSED FORM CONSTRUCTION
══════════════════════════════════════════════════════════════════

T1(e) — descended Markov trace of β_e = 1 (identity in H_2(q)):

    T1(e) = z(q_0) = 1 / (q_0^{1/2} + q_0^{-1/2})
          ≈ 0.49932  (dimensionless, cat-units)

This is the standard Markov parameter z that appears throughout
the Hecke / Skein formalism (per `prop:beta-decay-energy-scale`
and `mass_endomorphism.z_mark`).

T4(e) — Frobenius per-vortex co-Casimir at H_2:

H_2(q) has two irreps:

  * λ = (2) symmetric:    σ_1 ↦ +q,    dim_q = [2]_q = q + q^{-1}
  * λ = (1,1) alternating: σ_1 ↦ -q^{-1}, dim_q = 1

The Frobenius per-vortex co-Casimir tr_M(C_dim_q) at H_2 is

    tr_M(C_dim_q)|_{H_2} = z · ([2]_q · 1 + 1 · 1)
                         = z · ([2]_q + 1)

per the master formula `prop:frobenius-co-casimir-master`. In MeV
the framework defines T4 = m_e · tr_M(C_dim_q), so for the
electron (CAL-1 anchor):

    T4(e) [MeV] = M_E_MEV · z · ([2]_q + 1)

Note that for the proton at H_3 the analogous expression yields
T4(p) = 1.27611... MeV (in mass-formula-6term-mpfr-50dps.witness),
confirming the master-formula instantiation per
`prop:proton-mass-frobenius-co-casimir`.

══════════════════════════════════════════════════════════════════
 DIMENSIONAL CARE
══════════════════════════════════════════════════════════════════

T1 is dimensionless (cat-units). T4 carries an explicit m_e
prefactor and is in MeV. To form the partial `m_e_Hecke` in
consistent units we report two scalings:

  * `m_e_Hecke_cat_units` = T1(e) + T4(e)/M_E_MEV  (in m_e units)
  * `m_e_Hecke_MeV`       = M_E_MEV · T1(e) + T4(e)  (MeV)

The categorical mass formula
`m_K_MeV = ρ_K · m_e · |tr_M(β_K)|` consumes `m_e_Hecke` as the
denominator of the cat-units → MeV ratio (per
`applied_uniqueness_mass_table.categorical_mass_via_ratio`); both
forms above are exposed so the consumer picks the right one.

══════════════════════════════════════════════════════════════════
 NO FITTING ASSERTION
══════════════════════════════════════════════════════════════════

All quantities derive from CAL-1 (M_E_MEV) and CAL-2 (q_0_50dps)
alone. No CODATA m_p, no fitted scale, no algebraic +1.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV  # noqa: E402  (CAL-1)
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

OUT_WITNESS = HERE / "electron-m_e-derivation.witness.json"


def _q_0_50dps() -> mp.mpf:
    """CAL-2 q_0 at 50 dps from the canonical pinning witness."""
    p = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
    with p.open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


def derive_m_e_hecke() -> dict:
    """Closed-form Path A derivation of T1+T4 for the electron at H_2."""
    q = _q_0_50dps()
    sqrt_q = mp.sqrt(q)

    # T1(e) = z = 1 / (q^{1/2} + q^{-1/2})
    z = 1 / (sqrt_q + 1 / sqrt_q)

    # [2]_q = q + q^{-1}
    bracket_2_q = q + 1 / q

    # T4(e) [MeV] = M_E_MEV · z · ([2]_q + 1)
    co_casimir_h2 = z * (bracket_2_q + 1)
    t4_MeV = M_E_MEV * co_casimir_h2

    # m_e_Hecke in two unit conventions
    m_e_hecke_cat_units = z + t4_MeV / M_E_MEV  # in units of m_e
    m_e_hecke_MeV = M_E_MEV * z + t4_MeV

    return {
        "atom": "electron",
        "braid": "β_e = 1 (identity in H_2(q), zero crossings)",
        "q_0_50dps": fmt(q),
        "t1_descended": {
            "value_50dps": fmt(z),
            "formula": "z = 1 / (q^{1/2} + q^{-1/2})",
            "dimensionality": "cat-units (dimensionless)",
        },
        "t4_frobenius_co_casimir": {
            "value_50dps_MeV": fmt(t4_MeV),
            "formula": "M_E_MEV · z · ([2]_q + 1)",
            "irrep_decomposition": {
                "lambda_2_sym": "σ_1 ↦ +q, dim_q = [2]_q",
                "lambda_11_alt": "σ_1 ↦ -q^{-1}, dim_q = 1",
                "co_casimir_h2_dimensionless": fmt(co_casimir_h2),
            },
        },
        "m_e_hecke_partial": {
            "cat_units": fmt(m_e_hecke_cat_units),
            "MeV": fmt(m_e_hecke_MeV),
            "construction": "T1(e) + T4(e); same trustable subset as proton",
        },
        "no_fitting_assertion": (
            "Both T1(e) and T4(e) are closed-form expressions in q_0 "
            "(CAL-2) and M_E_MEV (CAL-1). No upstream witness consumed; "
            "no CODATA m_p / m_n / m_e_other tuning. The construction "
            "is the H_2 instantiation of the master Frobenius co-"
            "Casimir formula proved in QOU.BraidKnot.MassFormulaCategorical."
        ),
    }


def main() -> int:
    print("=" * 72)
    print(" Workplan 2 Phase 2 — derive m_e_Hecke from substrate (closed form)")
    print("=" * 72)

    e = derive_m_e_hecke()
    print(f"\n  Electron (β_e = identity in H_2):")
    print(f"    T1(e) = z = {mp.nstr(mp.mpf(e['t1_descended']['value_50dps']), 14)}")
    print(f"    T4(e) [MeV] = M_E · z · ([2]_q + 1) = {mp.nstr(mp.mpf(e['t4_frobenius_co_casimir']['value_50dps_MeV']), 14)}")
    print(f"    m_e_Hecke (cat-units, partial T1+T4) = {mp.nstr(mp.mpf(e['m_e_hecke_partial']['cat_units']), 14)}")
    print(f"    m_e_Hecke (MeV,       partial T1+T4) = {mp.nstr(mp.mpf(e['m_e_hecke_partial']['MeV']), 14)}")

    out = {
        "computation": "derive-m-e-hecke-path-a",
        "description": (
            "Workplan 2 Phase 2 — closed-form Path A derivation of "
            "m_e_Hecke at 50 dps for the electron at H_2 from CAL-1 "
            "M_E_MEV and CAL-2 q_0_50dps alone. NO FITTING per owner "
            "directive 2026-05-10. Replaces the DEPRECATED placeholder "
            "literal M_HECKE_PIPELINE_AT_Q0['e']=0.0007783. T1(e) is "
            "the standard Markov parameter z; T4(e) is the H_2 "
            "instantiation of the Frobenius co-Casimir master formula. "
            "Partial Path A subset (T1+T4); T2/T3/T5/T6 quarantined "
            "same as the proton derivation (see derive_m_p_hecke_path_a.py)."
        ),
        "auditOnly": "docs/audits/2026-05-10-1ppb-workplan-update.md",
        "owner_directive_2026_05_10": (
            "do workplans 2 phase 2; make sure no fitting; all should be derived"
        ),
        "data": {"electron": e},
    }

    # Migrated to WitnessBuilder.wrap_legacy (#637 deferred Tier-2,
    # adopted in PR #639) — adds scriptHash + staleness metadata.
    saved = WitnessBuilder.wrap_legacy(
        "electron-m_e-derivation", out,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Wrote {saved.name}")
    return 0


# Module-level accessors for derivation_chain.py to consume.
def m_e_hecke_path_a_cat_units_at_q0() -> mp.mpf:
    """Returns m_e_Hecke in cat-units (T1+T4 partial Path A). No fitting."""
    return mp.mpf(derive_m_e_hecke()["m_e_hecke_partial"]["cat_units"])


def m_e_hecke_path_a_MeV_at_q0() -> mp.mpf:
    """Returns m_e_Hecke in MeV (T1+T4 partial Path A). No fitting."""
    return mp.mpf(derive_m_e_hecke()["m_e_hecke_partial"]["MeV"])


if __name__ == "__main__":
    sys.exit(main())
