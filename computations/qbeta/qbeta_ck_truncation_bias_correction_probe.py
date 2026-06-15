#!/usr/bin/env python3
"""qbeta_ck_truncation_bias_correction_probe.py — probe 6.a from
the c_k generating-function scoping doc.

PR #1824 follow-on. The scoping doc
`docs/audits/2026-06-04-ck-generating-function-derivation-chain-
scope.md` predicts: if the c_k are Taylor coefficients of a single
generating function F(u), then finite-rung joint-fit extraction
introduces a CROSS-TALK BIAS:

  Δc_k ≈ c_{k+1} · u  (leading order)

For c_2: this predicts Δc_2 = c_3_extracted · u
                              = -2.010 · 0.00852
                              ≈ -0.01713
The observed c_2_extracted - c_2_canonical = -1.0171 - (-1) = -0.0171
MATCHES to 4 sig figs.

This probe tests the **bias-correction self-consistency** across
multiple rungs: compute the predicted leading bias Δc_k = c_{k+1}·u
for each k, subtract to get bias-corrected c_k_corr, and check
whether c_k_corr looks more structural.

**Predictions if the generating function hypothesis holds**:
  c_2_corr = -1.000 EXACTLY (matches proved canonical)
  c_3_corr = ? (should be closer to -2 if c_3 = -J_Hopf(1) is the
              true algebraic value with the SDP cross-talk removed)
  c_4_corr = ? (the registry calls c_4 a fit; corrected value may
              point to a structural pattern)
  c_5_corr = ? (registry says OPEN; corrected value is the first
              prediction)

**No new claims, just a self-consistency test of the
generating-function hypothesis using existing c_k extraction data.**
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    # Constants defined inside main() per Gemini PR #1824 review.
    U_SUBST = mp.mpf("0.00852")           # ≈ b·ℏ_q² at proton-pinned q_0
    C2_CANONICAL = mp.mpf("-1")           # Lean-proved canonical c_2
    C3_J_HOPF_AT_Q1 = mp.mpf("-2")        # J_Hopf(q=1) — registry near-match

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-truncation-bias-correction-probe",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Probe 6.a: tests the c_k generating-function scoping doc's "
        "leading-order truncation-bias prediction Δc_k = c_{k+1}·u. "
        "Computes bias-corrected c_k_corr from witness c_k_extracted "
        "and checks self-consistency: c_2_corr should equal the "
        "proved canonical -1 to extraction precision; c_3_corr should "
        "approach the empirical near-match -2 = J_Hopf(q=1)."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Probe 6.a — c_k truncation-bias correction self-consistency")
    print("=" * 78)
    print()

    # Read c_k from SDP-extracted witness on main
    witness_path = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    with open(witness_path, encoding="utf-8") as f:
        w = json.load(f)
    ck_extracted_raw = w["data"]["c_k_extracted_50dps"]

    ck = {}
    for k_str, v in ck_extracted_raw.items():
        k = int(k_str.replace("c_", "")) if k_str.startswith("c_") else int(k_str)
        ck[k] = mp.mpf(v)
    k_max = max(ck.keys())

    print(f"  u substrate: {mp.nstr(U_SUBST, 8)}")
    print(f"  Extraction range: k = 2..{k_max}")
    print()

    # Apply leading bias correction Δc_k = c_{k+1} · u
    print(f"  {'k':>3} {'c_k extracted':>22} {'predicted Δc_k':>16} {'c_k bias-corrected':>22}")
    print(f"  {'-'*3} {'-'*22} {'-'*16} {'-'*22}")
    ck_corr = {}
    for k in sorted(ck.keys()):
        if (k + 1) in ck:
            delta_pred = ck[k + 1] * U_SUBST
            c_corr = ck[k] - delta_pred
        else:
            delta_pred = None
            c_corr = ck[k]  # no correction possible at boundary
        ck_corr[k] = c_corr
        delta_str = mp.nstr(delta_pred, 8) if delta_pred is not None else "(boundary)"
        print(f"  {k:>3} {mp.nstr(ck[k], 16):>22} "
              f"{delta_str:>16} {mp.nstr(c_corr, 16):>22}")
    print()

    # Self-consistency checks
    print(f"  Self-consistency checks (hypothesis: F(u) generating function exists):")
    print()
    print(f"  Check 1: c_2_corr vs canonical -1")
    c2_corr_error = ck_corr[2] - C2_CANONICAL
    rel_err = c2_corr_error / C2_CANONICAL
    print(f"    c_2_corr = {mp.nstr(ck_corr[2], 16)}")
    print(f"    canonical = {C2_CANONICAL}")
    print(f"    residual = {mp.nstr(c2_corr_error, 8)} ({float(rel_err * 1e6):.2f} ppm)")
    if mp.fabs(rel_err) < mp.mpf("0.001"):
        print(f"    ✓ c_2_corr matches canonical to {float(mp.fabs(rel_err) * 1e6):.0f} ppm —")
        print(f"      STRONG CONFIRMATION of generating-function hypothesis at c_2")
    else:
        print(f"    ✗ c_2_corr does NOT match canonical — generating function")
        print(f"      hypothesis at c_2 not confirmed at leading-bias order")
    print()

    print(f"  Check 2: c_3_corr vs J_Hopf(q=1) = -2 empirical near-match")
    c3_corr_error = ck_corr[3] - C3_J_HOPF_AT_Q1
    rel_err_c3 = c3_corr_error / C3_J_HOPF_AT_Q1
    print(f"    c_3_corr = {mp.nstr(ck_corr[3], 16)}")
    print(f"    J_Hopf(1) = {C3_J_HOPF_AT_Q1}")
    print(f"    residual = {mp.nstr(c3_corr_error, 8)} "
          f"({float(rel_err_c3 * 100):.4f}%)")
    if mp.fabs(rel_err_c3) < mp.mpf("0.001"):
        print(f"    ✓ c_3_corr matches J_Hopf(1) to {float(mp.fabs(rel_err_c3) * 100):.4f}%")
        print(f"      CONFIRMS bias-correction methodology AND the c_3 ↔ J_Hopf(1)")
        print(f"      identification (currently REFUTED at SDP-extraction level)")
    elif mp.fabs(rel_err_c3) < mp.mpf("0.01"):
        print(f"    ~ c_3_corr within 1% of J_Hopf(1) — partial confirmation,")
        print(f"      higher-order biases needed")
    else:
        print(f"    ✗ c_3_corr does NOT match J_Hopf(1) — higher-order bias")
        print(f"      effects matter; leading correction insufficient at c_3")
    print()

    print(f"  Check 3: c_4_corr (registry says c_4 is a FIT)")
    print(f"    c_4_corr = {mp.nstr(ck_corr[4], 16)}")
    print(f"    (no canonical reference yet — observed value for downstream)")
    print()

    print(f"  Check 4: pattern in c_k_corr (the generating function's structural")
    print(f"            'cleaned' values)")
    print(f"    {'k':>3}  {'c_k_corr':>22}  {'c_k_corr / k!':>22}")
    print(f"    {'-'*3}  {'-'*22}  {'-'*22}")
    for k in sorted(ck_corr.keys())[:-1]:  # skip boundary
        c_corr = ck_corr[k]
        kfact = mp.mpf(int(mp.factorial(k)))
        ratio = c_corr / kfact
        print(f"    {k:>3}  {mp.nstr(c_corr, 16):>22}  {mp.nstr(ratio, 12):>22}")
    print(f"    (If c_k = a_k · k!, then c_k/k! → a_k should be BOUNDED.")
    print(f"     Bounded a_k = signature of factorial-growth generating function)")
    print()

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()

    c2_close = mp.fabs((ck_corr[2] - C2_CANONICAL) / C2_CANONICAL) < mp.mpf("0.01")
    c3_close = mp.fabs((ck_corr[3] - C3_J_HOPF_AT_Q1) / C3_J_HOPF_AT_Q1) < mp.mpf("0.01")
    if c2_close and c3_close:
        print(f"  ✓ STRONG EVIDENCE for generating-function hypothesis:")
        print(f"    The leading-order bias correction Δc_k ≈ c_{{k+1}} · u")
        print(f"    brings both c_2 and c_3 to their structural values")
        print(f"    (canonical -1 and J_Hopf(1) = -2 respectively).")
        print(f"    Higher-order bias corrections would refine further.")
    elif c2_close:
        print(f"  ~ PARTIAL CONFIRMATION: c_2 cleanly corrected to canonical -1.")
        print(f"    c_3 correction does not match J_Hopf(1) at leading order;")
        print(f"    either a higher-order bias is needed, OR the c_3 algebraic")
        print(f"    value is not -2 = J_Hopf(1).")
    else:
        print(f"  ? INCONCLUSIVE: leading-order bias correction does not")
        print(f"    cleanly restore canonical c_2 = -1. Either the generating")
        print(f"    function hypothesis is wrong, or the bias is higher-order")
        print(f"    in u, or the SDP-extracted c_k carry additional non-")
        print(f"    truncation contamination.")
    print()

    builder.add_data("ck_extracted", {str(k): mp.nstr(v, 25) for k, v in ck.items()})
    builder.add_data("ck_bias_corrected_leading", {str(k): mp.nstr(v, 25) for k, v in ck_corr.items()})
    builder.add_data("self_consistency", {
        "c_2_corr": mp.nstr(ck_corr[2], 25),
        "c_2_canonical": str(C2_CANONICAL),
        "c_2_residual_ppm": float((ck_corr[2] - C2_CANONICAL) / C2_CANONICAL * 1e6),
        "c_3_corr": mp.nstr(ck_corr[3], 25),
        "c_3_j_hopf_at_q1": str(C3_J_HOPF_AT_Q1),
        "c_3_residual_pct": float((ck_corr[3] - C3_J_HOPF_AT_Q1) / C3_J_HOPF_AT_Q1 * 100),
    })

    # Strong assertion: c_2 bias-corrected matches canonical -1 within 1%
    builder.add_assertion(
        "c2_bias_corrected_matches_canonical_within_1pct",
        computed=1 if c2_close else 0,
        expected=1,
        tolerance=0,
        source=("Probe 6.a's central test: c_2_extracted - c_3_extracted · u "
                "should equal the proved canonical c_2 = -1 within 1% if "
                "the c_k are Taylor coefficients of a single generating "
                "function F(u). This is the SIGNATURE evidence for the "
                "generating-function hypothesis. The size of the residual "
                "after this leading-order correction bounds higher-order "
                "bias effects."),
    )

    builder.save()
    print(f"  Witness: qbeta-ck-truncation-bias-correction-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
