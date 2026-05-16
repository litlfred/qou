#!/usr/bin/env python3
"""
Derive m_n_Hecke via the FULL mass-endomorphism tower at MPFR @ 50 dps.

Mirror of :py:mod:`derive_m_p_hecke_full_tower_50dps` for the
neutron.  Sums T1 (descended) + T2 (single brane tower) + T3 (pair
brane tower) + T4 (Frobenius co-Casimir) from the MPFR-native
per-generator volumes in
``terms-2-3-atom-per-gen-mpfr-50dps.witness.json``.

Per CLAUDE.md three-cal discipline: only CAL-1 (M_E_MEV) and CAL-2
(q_0) consumed.  No CODATA m_p / m_n injection.

Output: ``neutron-mass-full-tower-50dps.witness.json``

Result @ 2026-05-16: m_n_pred = 348.6 MeV vs CODATA 939.57 MeV;
                     residual −62.9 % (−628,824 ppm).

The 62.9 % residual is **NOT** the m_n_chain's "still unclosed"
state — it is the framework's actual prediction at the current
mass-endomorphism tower truncation.  The proton's T1+T2+T3+T4 sum
(via the symmetric uud quark chain plus the gluon self-coupling)
gives m_p / m_e ≈ 1866 (close to CODATA 1836).  The neutron's
analogous sum (udd, with a dd pair giving a σ⁻¹ instead of the uu
pair's σ) produces m_n / m_e ≈ 682 — *less than* m_p / m_e, which
contradicts experiment.  This points at a structural framework gap
(likely missing W± / Z mediation in the neutron's σ⁻¹ branch, or a
sign convention issue with the σ⁻¹ contribution to the brane
tower) that the current truncation does not capture.

¹H is admitted as `derived` under the 2 % threshold (proton 1.63 %
closure); m_n at 62.9 % is far outside the threshold and is
correctly classified `derivation_pending` by
:py:mod:`low_isotope_mass_table` — preserving honest reporting.

See ``docs/audits/2026-05-16-t1-t4-tower-closure-plan.md`` for the
next research steps (T5/T6 closure for the electron is a convention
question, not a code patch; the neutron-brane-tower structural gap
is research-level).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV_RAW, M_N_MEV_VALIDATION as M_N_MEV_CODATA,
)
from witness_base import (  # noqa: E402
    WitnessBuilder, load_and_hash_upstream,
)
from mass_formula_6term_mpfr_50dps import (  # noqa: E402
    term_4_frobenius_mp, f_Zdep_scale,
)
from bw_chirality_isotopes import (  # noqa: E402
    B_bulk, B_Zdep, B_shell, pairing_sign,
)
from term5_v2_chirality import aK_v2  # noqa: E402
from gb_filtration_jet_tracker import reduce_braid  # noqa: E402

M_E_MEV = mp.mpf(str(_M_E_MEV_RAW))


_CANONICAL_BRAID = {
    "neutron":  {"n": 3, "word": [1, -2, 1, -2, 1, -2]},
    "electron": {"n": 2, "word": [1, 1, 1]},
}


def _A_categorical(atom: str) -> int:
    """Max filtration grade of GS normal form (see
    derive_m_p_hecke_full_tower_50dps for the full rationale)."""
    spec = _CANONICAL_BRAID[atom]
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        r = reduce_braid(atom, spec["n"], spec["word"])
    shape = r["filtration_shape"]
    return max(shape.keys()) if shape else 0


def _t5_cat_units_for(A: int, Z: int, N: int) -> mp.mpf:
    """T5 in cat-units at categorical A.  See proton producer."""
    if A == 0:
        return mp.mpf(0)
    a_K = aK_v2(Z, N)
    sign = pairing_sign(Z, N)
    bulk = B_bulk(A, Z, N, sign)
    zdep = B_Zdep(A, Z, N)
    shell = B_shell(A, Z, N) if A >= 4 else mp.mpf(0)
    return (a_K * bulk + f_Zdep_scale * zdep + shell) / M_E_MEV


PER_GEN_WITNESS = HERE / "terms-2-3-atom-per-gen-mpfr-50dps.witness.json"
OUT_PATH = HERE / "neutron-mass-full-tower-50dps.witness.json"


def _sum_full_tower(per_gen_witness: dict, atom: str, Z: int, N: int) -> dict:
    """Sum T1+T2+T3+T4+T5 with categorical A (max GS filtration grade)."""
    A = _A_categorical(atom)
    for r in per_gen_witness["data"]["results"]:
        if r.get("atom") != atom:
            continue
        vols = [mp.mpf(v["full"]) for v in r["wedderburn_vols"]]
        desc = mp.mpf(1)
        for v in vols:
            desc *= v
        t1 = mp.fabs(desc)
        t2 = mp.mpf(r["term2_single_50dps"])
        t3 = mp.mpf(r["term3_pair_50dps"])
        t4 = term_4_frobenius_mp(A)
        t5_cat = _t5_cat_units_for(A, Z, N)
        return {
            "atom": atom,
            "A_categorical_max_grade": A,
            "A_derivation": "max filtration grade of GS normal form",
            "Z": Z,
            "N": N,
            "T1_descended_50dps": str(t1),
            "T2_single_50dps":    str(t2),
            "T3_pair_50dps":      str(t3),
            "T4_Frobenius_50dps": str(t4),
            "T5_chirality_BW_50dps_cat_units": str(t5_cat),
            "m_hecke_50dps":      str(t1 + t2 + t3 + t4 + t5_cat),
            "wedderburn_vols_full_50dps": [str(v) for v in vols],
        }
    raise KeyError(f"atom {atom!r} not found in per-gen witness")


def main() -> int:
    per_gen_w, _ = load_and_hash_upstream(PER_GEN_WITNESS)
    print(f"\n  MPFR @ {mp.mp.dps} dps  —  m_n_pred from full tower (A_categorical)\n")

    n_data = _sum_full_tower(per_gen_w, "neutron",  Z=0, N=1)
    e_data = _sum_full_tower(per_gen_w, "electron", Z=0, N=0)

    m_n_hecke = mp.mpf(n_data["m_hecke_50dps"])
    m_e_hecke = mp.mpf(e_data["m_hecke_50dps"])
    ratio_ne  = m_n_hecke / m_e_hecke
    m_n_pred  = ratio_ne * M_E_MEV
    rel_diff_n = (m_n_pred - M_N_MEV_CODATA) / M_N_MEV_CODATA

    print(f"  m_n_hecke (T1+T2+T3+T4) = {mp.nstr(m_n_hecke, 14)}")
    print(f"  m_e_hecke (T1+T2+T3+T4) = {mp.nstr(m_e_hecke, 14)}")
    print(f"  m_n / m_e (predicted)   = {mp.nstr(ratio_ne, 14)}")
    print(f"  CODATA m_n / m_e        = 1838.6836601")
    print()
    print(f"  m_n_pred (MeV)          = {mp.nstr(m_n_pred, 14)}")
    print(f"  CODATA m_n              = {mp.nstr(M_N_MEV_CODATA, 14)}")
    print(f"  residual                = {mp.nstr(rel_diff_n * 100, 6)} %  "
          f"({mp.nstr(rel_diff_n * mp.mpf('1e6'), 6)} ppm)")
    print()
    print("  NOTE: 62.9 % residual is the framework's actual prediction at")
    print("        this truncation, not a numerical-precision issue.")
    print("        m_n is correctly classified derivation_pending in")
    print("        low_isotope_mass_table.py under the 2 % threshold;")
    print("        the neutron-brane-tower structural gap is research-level")
    print("        (see docs/audits/2026-05-16-t1-t4-tower-closure-plan.md).")

    builder = WitnessBuilder("neutron-mass-full-tower-50dps", engine="mpmath")
    builder.set_description(
        "Full mass-endomorphism tower derivation of m_n at MPFR @ 50 dps. "
        "Sums T1 + T2 + T3 + T4 for the neutron and electron via the "
        "MPFR-native per-generator volumes from "
        "terms-2-3-atom-per-gen-mpfr-50dps.witness.json. m_n prediction "
        "in MeV computed as (m_n_hecke / m_e_hecke) × M_E_MEV. Three-cal "
        "discipline respected: only CAL-1 (M_E_MEV) and CAL-2 (q_0) "
        "consumed; no CODATA m_n injection. The residual (~-62.9 %) is "
        "the framework's actual prediction at this truncation — a real "
        "structural gap in the neutron-brane-tower formula (the udd "
        "quark content with σ⁻¹ pair under-counts the neutron's "
        "Wedderburn-weighted single-generator volume vs the proton's "
        "uud). Documented; not patched."
    )
    builder.add_upstream(PER_GEN_WITNESS)
    builder.add_assertion(
        "m_n_within_2_percent",
        computed=str(mp.fabs(rel_diff_n)),
        expected="0",
        tolerance=0.02,
    )
    builder.add_assertion(
        "m_n_finite",
        computed=mp.isfinite(m_n_pred),
        expected=True,
    )
    builder.add_parameter("q_0_50dps", str(per_gen_w["parameters"]["q_0_50dps"]))
    builder.add_parameter("M_E_MEV_CAL1", str(M_E_MEV))
    builder.add_data("particles", {"neutron": n_data, "electron": e_data})
    builder.add_data("ratios", {
        "m_n_over_m_e_50dps": str(ratio_ne),
    })
    builder.add_data("predictions_MeV", {
        "m_n_pred_50dps": str(m_n_pred),
    })
    builder.add_data("comparisons", {
        "m_n_codata_MeV":  str(M_N_MEV_CODATA),
        "rel_diff_n":      str(rel_diff_n),
        "rel_diff_n_ppm":  str(rel_diff_n * mp.mpf("1e6")),
    })
    builder.set_content_block("prop:mass-endomorphism-tower")
    builder.save()
    print(f"\n  Wrote {OUT_PATH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
