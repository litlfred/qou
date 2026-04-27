#!/usr/bin/env python3
"""Neutron-gap probes — Sprint B follow-up.

PR #450 (3-term Wedderburn upgrade) eliminated the empirical mixing
parameter α* and the n→p calibration constant α₄. After single-point
proton calibration, the canonical V_3term + brane-tower assembly
reproduces the proton mass exactly (by construction) but produces
the neutron mass at ≈411.79 MeV vs CODATA 939.57 MeV — a −56.17%
residual. The user's hypothesis space (verbatim):

    "λ_alt sign-flip / [2]_q std weight / Term 2 vs Term 5 for n/p split"

This script implements three CANONICAL probe variants and reports
the resulting neutron prediction for each. **No fitting is done.**
Each variant either has a content-block-cited justification, or it
is rejected.

H1: λ_alt sign flip.
    The current `λ_alt(σ_i) = -q⁻¹` follows the standard sign-rep
    convention. Try the opposite-sign convention `λ_alt(σ_i) = +q⁻¹`
    (or equivalently, |λ_alt|) to see whether the chirality channel
    enters the brane tower with the canonical relative sign.

H2: std weight uses [2]_q rather than dim_q([2,1])².
    The current `W_STD = (q²+1)² / D = dim_q([2,1])² / D` follows the
    Plancherel `dim_q²/D` convention. The std rep at n=3 is
    2-dimensional; an alternative `(q²+1)·[2]_q / D` weighting
    accounts for [2]_q (the q-integer 2) in the multiplicity rather
    than dim_q. Re-normalise the weights so they sum to 1 by scaling
    sym/alt proportionally.

H3: chirality enters Term 5, not Term 1 (per-channel V).
    The six-term formula puts chirality in Term 5 (`a_K · 𝒞_K`),
    NOT inside the per-vertex V that feeds the brane tower. Try
    dropping `λ_alt` from `V_3term` and applying it as a separate
    multiplicative factor `a_K` on the tower output.

Output: `neutron-gap-probes.witness.json` with proton/neutron
prediction for baseline and each H1/H2/H3, plus a verdict.
"""
from __future__ import annotations
import json
import sys
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp

# Import the canonical baseline machinery from PR #450.
# Note: alpha_blend_tower's import-time `mp.mp.dps = 50` side effect
# is what we rely on for module-level precision; we do not import the
# `abt` module name itself (per Copilot review: drop unused imports).
from alpha_blend_tower import (
    Q0, QI, D, W_SYM, W_STD, W_ALT,
    lam_sym, lam_alt, V_std, V_3term, tower, _DPS,
)
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1
from experimental_constants import M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder

WITNESS_OUT = HERE / "neutron-gap-probes.witness.json"


def _calibrate_and_predict(mp_v, mn_v):
    """Calibrate energy scale on the proton (single point, no fit) and
    predict the neutron mass. Returns (mp_pred, mn_pred, neutron_err_ppb).

    Per Copilot review: tuple-based `chirality_factor` API was unused
    (H3 already pre-multiplies tower outputs by `a_p`/`a_n` before
    calling). Simplified to a single calibration path."""
    if mp_v == 0:
        return None, None, None
    with mp.workdps(_DPS):
        E0 = mp.mpf(str(M_P_MEV)) / mp_v
        mp_pred = float(mp_v * E0)
        mn_pred = float(mn_v * E0)
    err_n_ppb = ((mn_pred - M_N_MEV) / M_N_MEV) * 1e9
    return mp_pred, mn_pred, err_n_ppb


# ── Baseline (current PR #450 V_3term) ────────────────────────────

def predict_baseline():
    """Current V_3term as merged in PR #450."""
    Vp0 = V_3term(_PROTON_G0)
    Vp1 = V_3term(_PROTON_G1)
    Vn0 = V_3term(_NEUTRON_G0)
    Vn1 = V_3term(_NEUTRON_G1)
    mp_v = tower([Vp0, Vp1])
    mn_v = tower([Vn0, Vn1])
    mp_pred, mn_pred, err = _calibrate_and_predict(mp_v, mn_v)
    return {
        "name": "baseline",
        "description": "current PR #450 V_3term (W_SYM·λ_sym + W_ALT·λ_alt + W_STD·V_std)",
        "proton_pred_MeV": mp_pred,
        "neutron_pred_MeV": mn_pred,
        "neutron_codata_MeV": M_N_MEV,
        "neutron_err_ppb": err,
    }


# ── H1: λ_alt sign flip ──────────────────────────────────────────

def V_h1(chain):
    """H1: negate the alt contribution."""
    return W_SYM * lam_sym(chain) - W_ALT * lam_alt(chain) + W_STD * V_std(chain)


def predict_h1():
    Vp0 = V_h1(_PROTON_G0); Vp1 = V_h1(_PROTON_G1)
    Vn0 = V_h1(_NEUTRON_G0); Vn1 = V_h1(_NEUTRON_G1)
    mp_v = tower([Vp0, Vp1]); mn_v = tower([Vn0, Vn1])
    mp_pred, mn_pred, err = _calibrate_and_predict(mp_v, mn_v)
    return {
        "name": "h1_alt_sign_flip",
        "description": ("V = W_SYM·λ_sym − W_ALT·λ_alt + W_STD·V_std "
                        "(negate the chirality contribution)"),
        "justification_check": (
            "λ_alt(σ_i) = -q⁻¹ from sign-rep convention. Flipping the "
            "sign in V is equivalent to using λ_alt(σ_i) = +q⁻¹, which "
            "would correspond to a different choice of antipode "
            "convention. Not standard — flagged as exploratory."
        ),
        "proton_pred_MeV": mp_pred,
        "neutron_pred_MeV": mn_pred,
        "neutron_codata_MeV": M_N_MEV,
        "neutron_err_ppb": err,
    }


# ── H2: std weight = (q²+1)·[2]_q / D, re-normalise ───────────────

def predict_h2():
    """H2: alternative std-weight normalisation."""
    with mp.workdps(_DPS):
        q2_q = Q0 + QI                                    # [2]_q = q + q⁻¹
        # Alternative: w_std uses dim_q([2,1]) · [2]_q / D rather than
        # dim_q([2,1])² / D. Numerator: (q² + 1) · (q + q⁻¹).
        W_STD_h2 = (Q0**2 + 1) * q2_q / D
        # Sym/alt are uncorrupted in this convention; re-scale sym + alt
        # proportionally so the three weights still sum to 1 exactly.
        leftover = mp.mpf(1) - W_STD_h2
        sym_alt_total = W_SYM + W_ALT                     # unchanged ratio
        scale = leftover / sym_alt_total
        W_SYM_h2 = W_SYM * scale
        W_ALT_h2 = W_ALT * scale

    def V_h2(chain):
        return (W_SYM_h2 * lam_sym(chain)
                + W_ALT_h2 * lam_alt(chain)
                + W_STD_h2 * V_std(chain))

    Vp0 = V_h2(_PROTON_G0); Vp1 = V_h2(_PROTON_G1)
    Vn0 = V_h2(_NEUTRON_G0); Vn1 = V_h2(_NEUTRON_G1)
    mp_v = tower([Vp0, Vp1]); mn_v = tower([Vn0, Vn1])
    mp_pred, mn_pred, err = _calibrate_and_predict(mp_v, mn_v)
    return {
        "name": "h2_std_weight_q2_q",
        "description": (
            "W_STD = (q²+1) · [2]_q / D where [2]_q = q + q⁻¹; "
            "sym/alt re-scaled so weights sum to 1."
        ),
        "weights": {
            "W_SYM_h2": float(W_SYM_h2),
            "W_STD_h2": float(W_STD_h2),
            "W_ALT_h2": float(W_ALT_h2),
            "sum": float(W_SYM_h2 + W_STD_h2 + W_ALT_h2),
        },
        "justification_check": (
            "Plancherel weights are dim_q(λ)²/[n]_q!; replacing "
            "dim_q([2,1])² with dim_q([2,1])·[2]_q breaks the standard "
            "Wedderburn convention. Probe is exploratory — would only "
            "be canonical if [wedderburn-trace-identity.md] is reread "
            "with a different normalization."
        ),
        "proton_pred_MeV": mp_pred,
        "neutron_pred_MeV": mn_pred,
        "neutron_codata_MeV": M_N_MEV,
        "neutron_err_ppb": err,
    }


# ── H3: chirality as Term-5 factor on tower output ────────────────

def predict_h3():
    """H3: drop alt from V_3term, apply chirality as multiplicative
    factor a_K on the tower output (per Term 5 of six-term formula)."""
    def V_h3(chain):
        # Per-vertex V WITHOUT the chirality channel.
        # Re-normalise so sym + std weights sum to 1.
        with mp.workdps(_DPS):
            denom = W_SYM + W_STD
            w_sym_h3 = W_SYM / denom
            w_std_h3 = W_STD / denom
        return w_sym_h3 * lam_sym(chain) + w_std_h3 * V_std(chain)

    def chirality_factor(g0_chain, g1_chain):
        """a_K from the chirality content average — proxy via product
        of λ_alt over the chain (per chirality-from-frobenius-self-pairing.md
        the chirality factor for an atomic braid is built from the
        per-crossing λ_alt contributions). Use product as multiplicative."""
        return lam_alt(g0_chain) * lam_alt(g1_chain)

    Vp0 = V_h3(_PROTON_G0); Vp1 = V_h3(_PROTON_G1)
    Vn0 = V_h3(_NEUTRON_G0); Vn1 = V_h3(_NEUTRON_G1)
    mp_tower = tower([Vp0, Vp1])
    mn_tower = tower([Vn0, Vn1])
    a_p = chirality_factor(_PROTON_G0, _PROTON_G1)
    a_n = chirality_factor(_NEUTRON_G0, _NEUTRON_G1)
    # Apply chirality as multiplicative factor; calibrate on proton.
    mp_v = mp_tower * a_p
    mn_v = mn_tower * a_n
    mp_pred, mn_pred, err = _calibrate_and_predict(mp_v, mn_v)
    return {
        "name": "h3_chirality_as_factor",
        "description": (
            "V_per_vertex without alt channel; chirality factor "
            "a_K = λ_alt(g0)·λ_alt(g1) applied multiplicatively to "
            "the tower output (per Term 5 of six-term-mass-formula)."
        ),
        "chirality_factors": {
            "a_p": float(a_p),
            "a_n": float(a_n),
            "ratio_n_over_p": float(a_n / a_p) if a_p != 0 else None,
        },
        "justification_check": (
            "Per six-term-mass-formula-complete.md, Term 5 (a_K · 𝒞_K) "
            "is a multiplicative chirality factor applied to the tower "
            "mass, not summed inside the per-vertex V. This probe "
            "factors the structure that way, using the per-crossing "
            "λ_alt product as a proxy for a_K. If neutron lands close "
            "to CODATA, this is the canonical structural decomposition; "
            "otherwise the chirality content needs a different "
            "construction (cf. ribbon_content_average.content_average)."
        ),
        "proton_pred_MeV": mp_pred,
        "neutron_pred_MeV": mn_pred,
        "neutron_codata_MeV": M_N_MEV,
        "neutron_err_ppb": err,
    }


def main() -> int:
    print("=" * 100)
    print("NEUTRON-GAP PROBES — Sprint B follow-up")
    print("=" * 100)
    print(f"  q_0 = {float(Q0):.10f}")
    print(f"  m_p (CODATA) = {M_P_MEV} MeV")
    print(f"  m_n (CODATA) = {M_N_MEV} MeV")
    print()

    results = []
    with mp.workdps(_DPS):
        results.append(predict_baseline())
        results.append(predict_h1())
        results.append(predict_h2())
        results.append(predict_h3())

    # Markdown table
    print(f"  {'name':<28} {'mp_pred':>12} {'mn_pred':>12} {'mn_err_ppb':>16}")
    print(f"  {'-' * 28} {'-' * 12} {'-' * 12} {'-' * 16}")
    for r in results:
        mp_p = f"{r['proton_pred_MeV']:>12.4f}" if r['proton_pred_MeV'] is not None else f"{'—':>12}"
        mn_p = f"{r['neutron_pred_MeV']:>12.4f}" if r['neutron_pred_MeV'] is not None else f"{'—':>12}"
        err = f"{r['neutron_err_ppb']:>+16.4e}" if r['neutron_err_ppb'] is not None else f"{'—':>16}"
        print(f"  {r['name']:<28} {mp_p} {mn_p} {err}")
    print()

    # Verdict
    THRESHOLD_PPB = 1e7  # i.e. <1% residual
    closes_gap = [
        r for r in results[1:]                # exclude baseline
        if r['neutron_err_ppb'] is not None
        and abs(r['neutron_err_ppb']) < THRESHOLD_PPB
    ]
    verdict = closes_gap[0]['name'] if closes_gap else "none"
    if closes_gap:
        rec = (f"Promote {closes_gap[0]['name']} canonically — "
               f"neutron err = {closes_gap[0]['neutron_err_ppb']:+.2e} ppb "
               f"(< {THRESHOLD_PPB:.0e} threshold).")
    else:
        # Find the smallest-magnitude residual to recommend the next probe direction
        ranked = sorted(
            [r for r in results[1:] if r['neutron_err_ppb'] is not None],
            key=lambda r: abs(r['neutron_err_ppb'])
        )
        if ranked:
            rec = (f"None of H1/H2/H3 closes the gap below {THRESHOLD_PPB:.0e} ppb. "
                   f"Smallest residual: {ranked[0]['name']} at "
                   f"{ranked[0]['neutron_err_ppb']:+.2e} ppb. Next probe should "
                   f"investigate combinations or higher-order corrections "
                   f"(e.g. Term 4 Frobenius co-Casimir, brane-tower per-vertex "
                   f"spectral-sequence higher pages).")
        else:
            rec = "All probes returned None (proton calibration failed)."
    print(f"  VERDICT: {verdict}")
    print(f"  RECOMMENDATION: {rec}")
    print()

    # Emit the witness via WitnessBuilder so it conforms to the
    # ComputationWitness schema (folio-assistant/schemas/types.ts) —
    # `engine`, `engineVersion`, `assertions`, `allPassed`,
    # `computedAt` etc. are all populated automatically.
    w = (
        WitnessBuilder("neutron-gap-probes", engine="mpmath")
        .set_description(
            "Three canonical probes (H1: λ_alt sign flip; H2: [2]_q "
            "std weight; H3: chirality as Term-5 multiplicative factor) "
            "investigating PR #450's −56% neutron-mass residual. No "
            "fitting; each variant has a content-block-cited rationale "
            "or is explicitly flagged as exploratory. Read-only "
            "investigation: does NOT modify alpha_blend_tower.py or "
            "any existing test."
        )
        .set_content_block("prop:joint-tower-sdp-confinement")
        .add_parameter("q_0", float(Q0))
        .add_parameter("m_p_codata_MeV", M_P_MEV)
        .add_parameter("m_n_codata_MeV", M_N_MEV)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("threshold_ppb", THRESHOLD_PPB)
        .add_data("results", results)
        .add_data("verdict", verdict)
        .add_data("recommendation", rec)
    )
    # Sanity-style assertions: proton calibrates exactly by construction
    # for every variant (single-point calibration).
    for r in results:
        if r.get("proton_pred_MeV") is not None:
            w.add_assertion(
                f"proton_calibration_exact_{r['name']}",
                computed=r["proton_pred_MeV"],
                expected=M_P_MEV,
                tolerance=1e-6,
                source="single-point proton calibration (E0 = m_p / mp_v)",
            )
        if r.get("neutron_err_ppb") is not None:
            # Neutron residual is reported but NOT asserted — this is
            # an investigation, not a verification.
            w.add_data(f"neutron_err_ppb_{r['name']}", r["neutron_err_ppb"])
    w.add_data("attestation", {
        "used_fitting": False,
        "used_root_find": False,
        "modifies_baseline_alpha_blend_tower_py": False,
    })
    out_path = w.save()  # auto-derives path from name → neutron-gap-probes.witness.json
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
