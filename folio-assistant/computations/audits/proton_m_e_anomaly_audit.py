#!/usr/bin/env python3


# polynomial_q_not_applicable: pure-numeric audit, no symbolic-q output.
"""
Audit: the proton 544k ppb defect IS the missing electron-rest anchor.

Documents the empirical observation that
`proton-mass-50dps.derivation.json`'s predicted m_p sits exactly at
`m_p_codata - m_e_codata` (within 472 ppb), and traces it to the
placeholder literals `M_HECKE_PIPELINE_AT_Q0` in
`derivation_chain.py:73-76`.

This script is **diagnostic-only**.  It does NOT modify the chain or the
literals — applying a `+1` to the Hecke ratio would be algebraic
cancellation hiding a fitting (warned against by repo owner).

Output: `proton-m_e-anomaly-audit.witness.json`.

See `docs/audits/2026-05-09-proton-m_e-anomaly.md` for the full audit and
resolution options A-E.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from derivation_chain import M_HECKE_PIPELINE_AT_Q0_LEGACY as M_HECKE_PIPELINE_AT_Q0  # noqa: E501  the documented placeholders, NOT the production Path A values (per Copilot review: audit script must pin the placeholder values it is documenting)
# CODATA anchors via the canonical mp.mpf-string source
# (per Copilot review on PR #621 — single source of truth).
from codata_constants import M_E_MEV as _M_E_MP, M_P_MEV_VALIDATION as _M_P_MP
M_E_MEV = float(_M_E_MP)
M_P_MEV = float(_M_P_MP)  # validation-only comparator (audit script)
from witness_base import WitnessBuilder


def main() -> int:
    # Construct WitnessBuilder up-front so durationMs reflects actual
    # end-to-end runtime (per Copilot review on PR #621).
    w = WitnessBuilder("proton-m_e-anomaly-audit", engine="python")
    w.set_audit_only("docs/audits/2026-05-09-proton-m_e-anomaly.md")

    M_E_HECKE = M_HECKE_PIPELINE_AT_Q0["e"]
    M_P_HECKE = M_HECKE_PIPELINE_AT_Q0["p"]

    ratio_predicted = M_P_HECKE / M_E_HECKE
    ratio_codata = M_P_MEV / M_E_MEV
    ratio_codata_minus_one = (M_P_MEV - M_E_MEV) / M_E_MEV

    m_p_predicted = ratio_predicted * M_E_MEV
    ppb_vs_codata = (m_p_predicted - M_P_MEV) / M_P_MEV * 1e9
    ppb_vs_minus_m_e = (m_p_predicted - (M_P_MEV - M_E_MEV)) / M_P_MEV * 1e9

    ratio_diff_to_codata = ratio_codata - ratio_predicted
    ratio_diff_to_codata_minus_one = ratio_codata_minus_one - ratio_predicted

    print("=" * 90)
    print("PROTON m_e ANOMALY AUDIT (diagnostic-only, no fix)")
    print("=" * 90)
    print(f"  Placeholder literals (derivation_chain.py:73-76):")
    print(f"    M_HECKE_PIPELINE_AT_Q0['e'] = {M_E_HECKE}")
    print(f"    M_HECKE_PIPELINE_AT_Q0['p'] = {M_P_HECKE}")
    print(f"  Predicted m_p_Hecke / m_e_Hecke = {ratio_predicted:.10f}")
    print(f"  CODATA  m_p / m_e               = {ratio_codata:.10f}")
    print(f"  CODATA (m_p - m_e) / m_e        = {ratio_codata_minus_one:.10f}")
    print()
    print(f"  Ratio diff to CODATA m_p/m_e          = {ratio_diff_to_codata:+.6f}")
    print(f"  Ratio diff to CODATA (m_p-m_e)/m_e    = {ratio_diff_to_codata_minus_one:+.6f}")
    print()
    print(f"  Predicted m_p (MeV)             = {m_p_predicted:.10f}")
    print(f"  CODATA m_p (MeV)                = {M_P_MEV}")
    print(f"  CODATA m_p - m_e (MeV)          = {M_P_MEV - M_E_MEV:.10f}")
    print(f"  Predicted ppb vs CODATA m_p     = {ppb_vs_codata:+.0f}")
    print(f"  Predicted ppb vs (m_p - m_e)    = {ppb_vs_minus_m_e:+.0f}")
    print()
    print("FINDING:")
    print("  The placeholder literals give a Hecke ratio sitting at exactly")
    print("  (m_p - m_e)/m_e + (~1 ppm noise), NOT m_p/m_e.  The 544,145 ppb")
    print("  defect = the missing electron rest anchor.  An algebraic +1 patch")
    print("  would cancel to CODATA m_p but would be fitting, not derivation.")
    print()
    print("  Resolution options A-E in docs/audits/2026-05-09-proton-m_e-anomaly.md.")

    w.set_description(
        "Diagnostic-only audit of the proton 544k ppb defect.  Documents "
        "that the placeholder literals M_HECKE_PIPELINE_AT_Q0['p']=1.4283 "
        "and ['e']=0.0007783 in derivation_chain.py:73-76 give a Hecke "
        "ratio matching (m_p - m_e)/m_e to ~470 ppb, NOT m_p/m_e.  The "
        "544,145 ppb error in proton-mass-50dps.derivation.json is "
        "structurally the missing electron-rest anchor.  This audit does "
        "NOT apply a fix: a `+1` patch on the Hecke ratio would hit CODATA "
        "by algebraic cancellation but would be fitting, not derivation.  "
        "Resolution options enumerated in docs/audits/2026-05-09-proton-m_e-anomaly.md "
        "(Options A-E).  Recommended: D (relabel-then-derive) or E (defer "
        "and focus 1ppb work on T1 / binding-energy chains that don't "
        "consume these placeholders)."
    )
    w.set_content_block("prop:full-pole-structure-mass-trace")
    w.add_parameter("M_E_HECKE_placeholder", M_E_HECKE)
    w.add_parameter("M_P_HECKE_placeholder", M_P_HECKE)
    w.add_parameter("M_E_MEV_codata", M_E_MEV)
    w.add_parameter("M_P_MEV_codata", M_P_MEV)
    w.add_data("ratio_predicted", ratio_predicted)
    w.add_data("ratio_codata_m_p_over_m_e", ratio_codata)
    w.add_data("ratio_codata_m_p_minus_m_e_over_m_e", ratio_codata_minus_one)
    w.add_data("ratio_diff_to_codata", ratio_diff_to_codata)
    w.add_data("ratio_diff_to_codata_minus_one", ratio_diff_to_codata_minus_one)
    w.add_data("m_p_predicted_MeV", m_p_predicted)
    w.add_data("ppb_vs_codata_m_p", ppb_vs_codata)
    w.add_data("ppb_vs_codata_m_p_minus_m_e", ppb_vs_minus_m_e)
    w.add_data("finding", (
        "Hecke ratio sits at (m_p - m_e)/m_e to ~470 ppb. Not a Phi_q precision "
        "issue, not a convention bug, not a q_0 drift. Placeholders calibrated "
        "to wrong target (or upstream missing rest-mass anchor). NO FIX APPLIED."
    ))
    w.add_data("resolution_options", {
        "A_relabel_only": "Demote chain step to PLACEHOLDER; flag literals' provenance",
        "B_recompute_from_6term": "Assemble m_p from mass-formula-6term-mpfr-50dps witness; needs unit reconciliation + A=1 brane-tower extension + T5 sign audit + T6 unit clarification",
        "C_audit_upstream_provenance": "Find or refute the claimed 'rounded summary' upstream for 1.4283 / 0.0007783",
        "D_recommended_A_then_B": "Two-PR sequence: relabel first, then derive",
        "E_defer": "Treat 544k ppb as known-floor; focus 1ppb work on T1 / binding-energy chains that don't consume these literals",
    })
    w.add_assertion(
        "predicted_matches_m_p_minus_m_e_within_1000_ppb",
        computed=abs(ppb_vs_minus_m_e),
        expected=0,
        tolerance=1000,
    )
    w.add_assertion(
        "predicted_diverges_from_codata_m_p_by_more_than_100k_ppb",
        computed=bool(abs(ppb_vs_codata) > 100_000),
        expected=True,
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
