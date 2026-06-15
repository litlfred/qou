#!/usr/bin/env python3
"""
Fresh p/n derivation — OBSERVABLE only (m_n − m_p), true SDP.

Per user guidance + prior work (see mass-formula-validation.md,
pair-creation-energy.md, hecke-charge-mass-duality.md):

  1. Absolute m_p and m_n are NOT directly derivable from γγ → target
     Hecke-energy distance because entanglement energy (pre-observable
     complex-q sector) is gauged away.
  2. Only DIFFERENCES/RATIOS project to observables.  The clean prior
     result is:
         m_n − m_p = S_dd − S_uu
                   = ((q+q⁻¹)/(q^{1/2}+q^{-1/2})) · (μ_d − μ_u)
     giving < 1 ppm on Δm across isotopes once μ_d − μ_u is
     calibrated from CODATA.

This script:

  A. Runs the existing true SDP (confinement_sdp.solve_sdp) on the
     proton NF net and neutron NF net separately.  Extracts minimum-
     objective (Hecke-energy) for each.
  B. Reports the difference ΔE_SDP = E_sdp(n) − E_sdp(p).
  C. Computes the algebraic prefactor (q+q⁻¹)/(q^{1/2}+q^{-1/2}) and
     μ_d − μ_u = Δm_codata / prefactor; verifies internal consistency
     with the prior result.
  D. Checks whether ΔE_SDP / prefactor matches μ_d − μ_u in Hecke-energy
     units — i.e. whether the SDP minimum correctly captures the same-
     flavor dressing structure.

Caveat: the SDP target_net is a single scalar (total NF basis
coefficient sum).  This captures the OBSERVABLE component only.
Pre-observable / entanglement contributions are absent by construction.
"""
from __future__ import annotations

import sys
import json
import math
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP

# Prior-work nucleon NF nets (nucleon-with-gluons-nf.witness.json)
# at q_0 for bare B_3 (without gluons):
NETS_BARE = {
    "proton (uud)": 0.9991251252427813,
    "neutron (udd)": 0.8108354875878183,
}
# With gluons (B₃+g):
NETS_GLUON = {
    "proton (uud)": 1.845956,
    "neutron (udd)": 1.493885,
}

# Observable: m_n − m_p = 1.293 MeV (CODATA)
DELTA_M_CODATA = M_N_MEV - M_P_MEV


def algebraic_prefactor():
    """(q+q⁻¹) / (q^{1/2} + q^{-1/2}).

    At q=1 reduces to 2/2 = 1.  At q₀ ≈ 1.11 gives ~1.004.
    """
    num = Q0 + QI
    den = mp.sqrt(Q0) + mp.sqrt(QI)
    return num / den


def run_sdp(target_net: float, label: str) -> dict:
    """Call confinement_sdp.solve_sdp on a target net value."""
    # Import lazily to avoid its boot-time LP that silences stdout
    try:
        from confinement_sdp import solve_sdp, solve_lp
    except ImportError as e:
        return {"error": f"SDP module import failed: {e}"}
    out = {"label": label, "target_net": target_net}
    try:
        sdp_res = solve_sdp(target_net)
        out["sdp"] = {
            "status": sdp_res.get("status"),
            "objective": sdp_res.get("objective"),
            "moment_rank": sdp_res.get("moment_rank_numeric"),
        }
    except Exception as e:
        out["sdp_error"] = f"{type(e).__name__}: {e}"
    try:
        lp_res = solve_lp(target_net)
        out["lp"] = {
            "status": lp_res.get("status"),
            "objective": lp_res.get("objective"),
        }
    except Exception as e:
        out["lp_error"] = f"{type(e).__name__}: {e}"
    return out


def main() -> int:
    print("=" * 100)
    print("FRESH p/n DERIVATION — observable Δm via TRUE SDP")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  CODATA Δm = m_n − m_p = {DELTA_M_CODATA} MeV")
    print()
    K = algebraic_prefactor()
    print(f"  Algebraic prefactor (q+q⁻¹)/(q^½+q^(-½)) = {mp.nstr(K, 25)}")
    # μ_d − μ_u calibrated from CODATA Δm and the prefactor
    mu_diff = mp.mpf(str(DELTA_M_CODATA)) / K
    print(f"  μ_d − μ_u (calibrated) = Δm / K = {mp.nstr(mu_diff, 15)} MeV")
    print()

    print("=" * 100)
    print("A.  SDP on proton, neutron NF nets")
    print("=" * 100)
    sdp_results = {}
    for flavor, net in NETS_BARE.items():
        r = run_sdp(net, label=flavor)
        sdp_results[flavor + " (bare)"] = r
        print(f"\n  {flavor} (bare), target_net = {net:.10f}")
        if "sdp" in r and r["sdp"]["objective"] is not None:
            print(f"    SDP obj = {r['sdp']['objective']:+.10f}  "
                  f"rank={r['sdp']['moment_rank']}")
        else:
            print(f"    SDP failed: {r.get('sdp_error', r.get('sdp'))}")
        if "lp" in r and r["lp"]["objective"] is not None:
            print(f"    LP  obj = {r['lp']['objective']:+.10f}")
        else:
            print(f"    LP failed: {r.get('lp_error', r.get('lp'))}")

    for flavor, net in NETS_GLUON.items():
        r = run_sdp(net, label=flavor)
        sdp_results[flavor + " (with gluons)"] = r
        print(f"\n  {flavor} (with gluons), target_net = {net:.6f}")
        if "sdp" in r and r["sdp"]["objective"] is not None:
            print(f"    SDP obj = {r['sdp']['objective']:+.10f}  "
                  f"rank={r['sdp']['moment_rank']}")
        else:
            print(f"    SDP failed: {r.get('sdp_error', r.get('sdp'))}")
        if "lp" in r and r["lp"]["objective"] is not None:
            print(f"    LP  obj = {r['lp']['objective']:+.10f}")
        else:
            print(f"    LP failed: {r.get('lp_error', r.get('lp'))}")

    print()
    print("=" * 100)
    print("B.  ΔE_SDP = obj(n) − obj(p)")
    print("=" * 100)
    for variant in ["bare", "with gluons"]:
        p_key = f"proton (uud) ({variant})"
        n_key = f"neutron (udd) ({variant})"
        rp = sdp_results.get(p_key, {})
        rn = sdp_results.get(n_key, {})
        p_obj = rp.get("sdp", {}).get("objective")
        n_obj = rn.get("sdp", {}).get("objective")
        if p_obj is not None and n_obj is not None:
            dE_sdp = n_obj - p_obj
            print(f"  variant {variant:<14} ΔE_SDP = "
                  f"{dE_sdp:+.10f} Hecke units")
            # Convert Hecke → MeV via μ_d − μ_u calibration:
            #   m_n − m_p = K · (μ_d − μ_u)
            # If ΔE_SDP equals S_dd − S_uu in Hecke-units, then
            #   m_n − m_p = K · ΔE_SDP · (MeV/Hecke-unit conversion)
            # For now report ΔE_SDP · K and see what absolute scale emerges.
            dE_scaled = float(K * mp.mpf(str(dE_sdp)))
            ratio_to_codata = dE_scaled / DELTA_M_CODATA
            print(f"  variant {variant:<14} K · ΔE_SDP = "
                  f"{dE_scaled:+.6f}  (÷ Δm_CODATA = {ratio_to_codata:+.4e})")
        else:
            print(f"  variant {variant:<14} SDP failed for one or both")

    print()
    print("=" * 100)
    print("C.  Consistency check: algebraic Δm via prior-work formula")
    print("=" * 100)
    dm_alg = K * mu_diff
    print(f"  Δm_algebraic = K · (μ_d − μ_u) = "
          f"{mp.nstr(dm_alg, 15)} MeV")
    print(f"  CODATA        = {DELTA_M_CODATA} MeV")
    print(f"  rel err       = {float((dm_alg - mp.mpf(str(DELTA_M_CODATA))) / mp.mpf(str(DELTA_M_CODATA))):+.3e}  "
          f"(should be ~0 since μ_diff was calibrated from Δm)")

    witness = {
        "computation": "fresh-derivation-pn-true-sdp",
        "description": (
            "True SDP (confinement_sdp.solve_sdp, Lasserre moment "
            "relaxation) applied to proton/neutron NF nets to extract "
            "minimum Hecke-energy; diff gives observable Δm analog.  "
            "Prior-work framing: entanglement energy is non-observable, "
            "only S_dd − S_uu matters.  Algebraic prefactor (q+q⁻¹)/"
            "(q^½+q^(-½)) = [2]_q/z_JO^(-1) = 1.00395... at q₀; "
            "μ_d − μ_u calibrated from CODATA Δm = 1.293 MeV."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "algebraic_prefactor": mp.nstr(K, 30),
        "mu_d_minus_mu_u_MeV": mp.nstr(mu_diff, 30),
        "delta_m_codata_MeV": DELTA_M_CODATA,
        "sdp_results": sdp_results,
    }
    out = Path(__file__).parent / "fresh-derivation-pn-true-sdp.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
