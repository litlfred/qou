#!/usr/bin/env python3
# polynomial_q_not_applicable: per-generator volumes are numerical
# scalars at q = q_0, not symbolic-in-q polynomials.
"""Brane-tower m_p / m_n with the DERIVED "std" V̂_i vs the production "full".

Acts on the merged item-2 audit
[`docs/audits/2026-06-01-vhat-per-crossing-transfer-chain.md`] (verdict A
+ RED finding): the brane tower
(`derive_m_p_hecke_full_tower_50dps.derive_full_tower`) consumes the
W-weighted 3-channel ``"full"`` Wedderburn average
``w_sym·λ_sym + w_std·V_std + w_alt·λ_alt`` — which is NOT
`thm:markov-trace-product`'s per-generator factor V̂_i = z·a_i + b_i (the
``"std"`` channel, whose product reproduces tr_M to 4e-6).

This script runs the FULL tower (T1 + T2 + T3 + T4 + T5 + T6) for both
channels at MPFR @ 50 dps, with ZERO tuning, and reports the RAW m_p /
m_n in MeV for each, plus the delta vs CODATA.  No channel weight is
tuned; no correction is hard-coded.  Production default in
`derive_m_p_hecke_full_tower_50dps.py` stays ``"full"`` — this is a
comparison/diagnostic only, OWNER-GATED before any default flip.

Output: ``vhat-std-vs-full-tower-compare.witness.json``.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV_RAW,
    M_P_MEV_VALIDATION as M_P_MEV_CODATA,
    M_N_MEV_VALIDATION as M_N_MEV_CODATA,
)
from witness_base import WitnessBuilder, load_and_hash_upstream  # noqa: E402
from _li_2_q_util import load_q_50dps  # noqa: E402
from derive_m_p_hecke_full_tower_50dps import (  # noqa: E402
    derive_full_tower, PER_GEN_WITNESS,
)

M_E_MEV = mp.mpf(str(_M_E_MEV_RAW))


def _predict(channel: str, per_gen_w: dict, q0, qi, z) -> dict:
    """Run the full tower for proton + neutron in the given channel and
    return RAW m_p / m_n in MeV (m_e × m_X/m_e) plus per-term breakdown.

    m_e is the CAL-1 anchor (the electron is not in the per-gen witness
    post-rebase), so m_X = (m_X_hecke / m_e_hecke) × m_e ≡ m_X_hecke ×
    m_e / m_e_hecke; with m_e_hecke ≡ m_e (CAL-1) this is m_X_hecke ×
    (m_e / m_e_hecke).  Mirrors the production main() exactly.
    """
    p = derive_full_tower("proton",  per_gen_w, Z=1, N=0, knot_type="none",
                          q0=q0, qi=qi, z=z, channel=channel)
    n = derive_full_tower("neutron", per_gen_w, Z=0, N=1, knot_type="none",
                          q0=q0, qi=qi, z=z, channel=channel)
    try:
        e = derive_full_tower("electron", per_gen_w, Z=0, N=0, knot_type="none",
                              q0=q0, qi=qi, z=z, channel=channel)
        m_e_hecke = mp.mpf(e["m_hecke_50dps"])
    except KeyError:
        # CAL-1 anchor fallback (electron not in per-gen witness post-rebase).
        m_e_hecke = M_E_MEV

    m_p_hecke = mp.mpf(p["m_hecke_50dps"])
    m_n_hecke = mp.mpf(n["m_hecke_50dps"])
    ratio_pe = m_p_hecke / m_e_hecke
    ratio_ne = m_n_hecke / m_e_hecke
    m_p_MeV = ratio_pe * M_E_MEV
    m_n_MeV = ratio_ne * M_E_MEV

    rel_p = (m_p_MeV - M_P_MEV_CODATA) / M_P_MEV_CODATA
    rel_n = (m_n_MeV - M_N_MEV_CODATA) / M_N_MEV_CODATA

    return {
        "channel": channel,
        "proton_terms": {
            "T1_descended": p["T1_descended_50dps"],
            "T2_single": p["T2_single_Li2q_50dps"],
            "T3_pair": p["T3_pair_Li2q_50dps"],
            "T4_Frobenius": p["T4_Frobenius_50dps"],
            "T5_chirality": p["T5_chirality_BW_50dps_cat_units"],
            "T6_Habiro": p["T6_Habiro_residue_50dps_cat_units"],
            "m_hecke": p["m_hecke_50dps"],
            "vhat_i": p["wedderburn_vols_full_50dps"],
        },
        "neutron_terms": {
            "T1_descended": n["T1_descended_50dps"],
            "T2_single": n["T2_single_Li2q_50dps"],
            "T3_pair": n["T3_pair_Li2q_50dps"],
            "T4_Frobenius": n["T4_Frobenius_50dps"],
            "T5_chirality": n["T5_chirality_BW_50dps_cat_units"],
            "T6_Habiro": n["T6_Habiro_residue_50dps_cat_units"],
            "m_hecke": n["m_hecke_50dps"],
            "vhat_i": n["wedderburn_vols_full_50dps"],
        },
        "m_p_MeV": str(m_p_MeV),
        "m_n_MeV": str(m_n_MeV),
        "rel_diff_p": str(rel_p),
        "rel_diff_p_percent": str(rel_p * 100),
        "rel_diff_n": str(rel_n),
        "rel_diff_n_percent": str(rel_n * 100),
    }


def main() -> int:
    start_time = time.monotonic()
    per_gen_w, per_gen_hash = load_and_hash_upstream(PER_GEN_WITNESS)
    q0, qi, z = load_q_50dps()

    print("=" * 78)
    print("BRANE-TOWER m_p / m_n: DERIVED 'std' V̂_i vs production 'full'")
    print("=" * 78)
    print(f"  MPFR @ {mp.mp.dps} dps   source: {PER_GEN_WITNESS.name}")
    print()

    res_full = _predict("full", per_gen_w, q0, qi, z)
    res_std = _predict("std", per_gen_w, q0, qi, z)

    def _row(tag: str, r: dict) -> None:
        m_p = mp.mpf(r["m_p_MeV"])
        m_n = mp.mpf(r["m_n_MeV"])
        print(f"  [{tag:>4}]  m_p = {mp.nstr(m_p, 12):>16} MeV  "
              f"({mp.nstr(mp.mpf(r['rel_diff_p_percent']), 6):>10} %)   "
              f"m_n = {mp.nstr(m_n, 12):>16} MeV  "
              f"({mp.nstr(mp.mpf(r['rel_diff_n_percent']), 6):>10} %)")

    print(f"  CODATA   m_p = {mp.nstr(M_P_MEV_CODATA, 12):>16} MeV"
          f"                   m_n = {mp.nstr(M_N_MEV_CODATA, 12):>16} MeV")
    _row("full", res_full)
    _row("std", res_std)
    print()

    m_p_full = mp.mpf(res_full["m_p_MeV"])
    m_p_std = mp.mpf(res_std["m_p_MeV"])
    delta_mp = m_p_std - m_p_full
    abs_full = mp.fabs(mp.mpf(res_full["rel_diff_p"]))
    abs_std = mp.fabs(mp.mpf(res_std["rel_diff_p"]))
    verdict = "IMPROVES" if abs_std < abs_full else ("REGRESSES" if abs_std > abs_full else "UNCHANGED")
    print(f"  Δ m_p (std − full) = {mp.nstr(delta_mp, 8)} MeV")
    print(f"  |rel_p| full = {mp.nstr(abs_full, 8)}   |rel_p| std = {mp.nstr(abs_std, 8)}")
    print(f"  VERDICT: switching to derived 'std' channel {verdict} m_p accuracy")
    print()

    builder = WitnessBuilder("vhat-std-vs-full-tower-compare", engine="mpmath")
    builder.set_description(
        "RAW brane-tower m_p / m_n (full T1..T6 endomorphism tower @ "
        "MPFR 50 dps) computed with BOTH per-generator V̂_i channels: "
        "(a) production 'full' = W-weighted 3-channel Wedderburn average; "
        "(b) DERIVED 'std' = thm:markov-trace-product factor V̂_i = z·a_i "
        "+ b_i whose product reproduces tr_M to 4e-6 (item-2 audit "
        "2026-06-01-vhat-per-crossing-transfer-chain.md, verdict A + RED). "
        "ZERO tuning: no channel weight fitted, no correction hard-coded; "
        "only CAL-1 (m_e) + CAL-2 (q_0) consumed. Reports m_p/m_n in MeV "
        "and rel-diff vs CODATA for each channel and the std−full delta. "
        "Production default in derive_m_p_hecke_full_tower_50dps stays "
        "'full' — this is a diagnostic for the owner-gated wiring decision."
    )
    builder._upstream_hashes.append(per_gen_hash)
    builder.add_parameter("q_0_50dps", str(per_gen_w["parameters"]["q_0_50dps"]))
    builder.add_parameter("M_E_MEV_CAL1", str(M_E_MEV))
    builder.add_parameter("production_default_channel", "full")
    builder.add_data("full_channel", res_full)
    builder.add_data("std_channel", res_std)
    builder.add_data("comparison", {
        "m_p_full_MeV": res_full["m_p_MeV"],
        "m_p_std_MeV": res_std["m_p_MeV"],
        "delta_m_p_std_minus_full_MeV": str(delta_mp),
        "rel_diff_p_full": res_full["rel_diff_p"],
        "rel_diff_p_std": res_std["rel_diff_p"],
        "abs_rel_p_full": str(abs_full),
        "abs_rel_p_std": str(abs_std),
        "m_n_full_MeV": res_full["m_n_MeV"],
        "m_n_std_MeV": res_std["m_n_MeV"],
        "rel_diff_n_full": res_full["rel_diff_n"],
        "rel_diff_n_std": res_std["rel_diff_n"],
        "m_p_codata_MeV": str(M_P_MEV_CODATA),
        "m_n_codata_MeV": str(M_N_MEV_CODATA),
        "std_vs_full_m_p_verdict": verdict,
    })
    builder.set_content_block("prop:mass-endomorphism-tower")
    out = builder.save()
    print(f"  Witness: {Path(out).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
