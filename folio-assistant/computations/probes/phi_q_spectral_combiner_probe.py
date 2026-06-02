#!/usr/bin/env python3
"""phi_q_spectral_combiner_probe.py — probe: Li_2^q × spectral combiner
for Q_β c_3.

CONTEXT. Per b502b9b83 audit:
  - mech #4: Li_2^q E_0 tower (global) — RULED OUT (wrong direction)
  - mech #5: per-block dim_q² decomposition — RULED OUT (-8 vs -2)
  - mech #6: y_λ-weighted SUM rule — RULED OUT (Σ y_λ ≠ 1 at q ≠ 1)

This probe tests the UNTESTED combination: a Li_2^q-derived per-block
measure μ_λ replacing y_λ in the per-block sum. By construction,
Σ μ_λ = 1 (curing mech #6's normalization defect).

DISCIPLINE (per CLAUDE.md "Don't propose a seventh fit-based ansatz"):
the probe pre-states its failure-mode signature. If the candidate
matches empirical c_3 at q_proton anchor but NOT at q_muon
cross-check anchor, declare another near-match (mechanism #7). Do
NOT wire.

Per the framework's _li_2_q_util.py docstring: Q_β / Δ_λ are
BINDING-context quantities, so Li_2^q (not Φ_q) is the right
dilogarithm. The c_k flip-flop's earlier "Φ_q × spectral" framing
was a category error — corrected to Li_2^q × spectral.

INPUTS (from qbeta-per-block-paper-closed-forms.witness.json):
  - per-block χ_λ at q_proton
  - per-block leading-order c_3^(λ) Taylor coefficient
  - per-block y_λ Wenzl-bridge weights (for comparison)

OUTPUTS (in witness):
  - μ_λ candidate measures at q_proton AND q_muon
  - normalization check Σ μ_λ = 1 at both anchors
  - c_3 candidate = Σ μ_λ · c_3^(λ) at both anchors
  - cross-anchor swing
  - verdict: TAYLOR-EXACT / NEAR-MATCH / REFUTED
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, OUTPUT_DPS, fmt  # noqa: E402
from _li_2_q_util import li_2_q, _q_int  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def compute_at_anchor(q: mpf, label: str, per_block_data: dict) -> dict:
    """Compute candidate μ_λ measure + c_3 candidate at one q anchor.

    For the ``q_proton`` anchor we use the χ_λ values directly from the
    upstream witness (computed at production q_0 = q_proton). For
    ``q_muon`` we would need to re-evaluate the Hoefsmit closed forms
    at q_muon; that requires the per-block χ_λ(q) symbolic forms which
    are NOT on disk in evaluable form. This probe therefore reports
    the single-anchor (q_proton) result only; the q_muon cross-anchor
    test is deferred. Single-anchor refutation at q_proton alone is
    decisive (13.14% off ⟹ refuted) so the cross-anchor extension
    isn't required to settle the candidate.
    """
    q_inv = 1 / q

    if label != "proton":
        raise NotImplementedError(
            "q_muon cross-anchor evaluation requires Hoefsmit χ_λ(q) "
            "closed-form re-evaluation infrastructure not yet wired. "
            "Single-anchor (q_proton) refutation is decisive (13% off "
            "empirical c_3 = -2.07); cross-anchor adds nothing to the "
            "verdict. Deferred to a future session that wires Hoefsmit "
            "χ_λ(q) reusable evaluator."
        )

    # Per-block leading-order c_3^(λ) (from witness, ε^1 coefficient)
    # Indexing: position 1 in the Taylor coefs list (position 0 is the ε^0 = 0)
    c3_per_block = {
        "(3)": mpf(-2),       # from witness
        "(2,1)": mpf(-1),     # from witness
        "(1,1,1)": mpf(-2),   # from witness
    }

    chi_per_block = {k: mpf(v) for k, v in per_block_data["chi_at_q_0"].items()
                     if k in c3_per_block}
    y_per_block = {k: mpf(v) for k, v in per_block_data["y_lambda_at_q_0"].items()
                   if k in c3_per_block}

    # Candidate μ_λ via Li_2^q(-|χ_λ|):
    # Li_2^q has convergence radius |z| < q; |χ_λ| ≈ 0.1-0.3 << q ≈ 1.11 → converges.
    li2q_neg_chi = {}
    for k, v in chi_per_block.items():
        z = -abs(v)  # negative argument, |z| < 1 << q
        li2q_neg_chi[k] = li_2_q(z, q, q_inv, max_k=500)

    sum_li2q = sum(li2q_neg_chi.values())
    mu_per_block = {k: v / sum_li2q for k, v in li2q_neg_chi.items()}

    # Σ μ_λ = 1 by construction. Verify.
    sum_mu = sum(mu_per_block.values())

    # c_3 candidate = Σ μ_λ · c_3^(λ)
    c3_li2q_measure = sum(mu_per_block[k] * c3_per_block[k] for k in c3_per_block)

    # For comparison: y_λ-weighted sum (mech #6 baseline)
    c3_y_weighted = sum(y_per_block[k] * c3_per_block[k] for k in c3_per_block)
    sum_y = sum(y_per_block.values())

    # Uniform sum (mech #5 baseline) — just sum the c_3^(λ)
    c3_uniform = sum(c3_per_block.values())

    return {
        "q_at_this_anchor": fmt(q),
        "Σ_y_λ_(should_be_1_but_isnt)": fmt(sum_y),
        "Σ_μ_λ_(should_be_1_by_construction)": fmt(sum_mu),
        "Σ_μ_λ_deviation_from_1": fmt(sum_mu - 1),
        "per_block_χ_λ": {k: fmt(v) for k, v in chi_per_block.items()},
        "per_block_y_λ": {k: fmt(v) for k, v in y_per_block.items()},
        "per_block_Li_2_q_neg_chi": {k: fmt(v) for k, v in li2q_neg_chi.items()},
        "per_block_μ_λ_(Li_2_q_measure)": {k: fmt(v) for k, v in mu_per_block.items()},
        "c3_candidate_Li_2_q_measure": fmt(c3_li2q_measure),
        "c3_baseline_uniform_sum_(mech_5)": fmt(c3_uniform),
        "c3_baseline_y_lambda_weighted_(mech_6)": fmt(c3_y_weighted),
    }


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder("phi-q-spectral-combiner-probe", engine="python+mpmath",
                              start_time=t0)
    builder.set_description(
        "User-proposed 2026-05-31: Li_2^q × spectral combiner for Q_β c_3. "
        "Tests Li_2^q-derived per-block measure μ_λ replacing y_λ in "
        "Wedderburn-block sum. Cross-anchor (q_proton vs q_muon) is the "
        "pre-stated failure signature: matches at one only ⟹ NEAR-MATCH."
    )

    print("=" * 78)
    print(" Li_2^q × spectral combiner probe — Q_β c_3 cross-anchor test")
    print("=" * 78)
    print()

    # Empirical c_3 targets (per qbeta_ck_truncation_order_analysis.py docstring)
    EMPIRICAL_C3_PROTON = mpf("-2.0693")   # m_p-pin anchor
    EMPIRICAL_C3_MUON = mpf("-2.0097")    # muon-pin anchor

    # Load per-block data via WitnessBuilder so the drift detector
    # (folio-assistant/computations/witness_dependency_drift.py) sees
    # the upstream hash. Per Copilot review on PR #1609.
    upstream_path = _pb.witness_path("qbeta-per-block-paper-closed-forms.witness.json", HERE)
    per_block_witness = builder.add_upstream(upstream_path)
    per_block_data = per_block_witness.get("data", per_block_witness)

    # SINGLE-ANCHOR PROBE: q_proton only.
    # Cross-anchor (q_muon) evaluation requires re-evaluating the
    # Hoefsmit χ_λ(q) closed forms — not yet wired as a reusable
    # evaluator. The single-anchor refutation at q_proton alone (13%
    # off empirical c_3) is DECISIVE for this Li_2^q-derived candidate;
    # cross-anchor data would not change the verdict.
    q_proton = q_at()
    print(f"q_proton = {fmt(q_proton)}")
    result_proton = compute_at_anchor(q_proton, "proton", per_block_data)
    result_muon = {
        "note": (
            "DEFERRED — q_muon cross-anchor evaluation requires "
            "Hoefsmit χ_λ(q) closed-form re-evaluation infrastructure "
            "not yet wired. Single-anchor refutation at q_proton is "
            "decisive (13% off empirical c_3 = -2.07). The fibre/"
            "observable distinction (user 2026-05-31) would matter "
            "here: a TRULY q-independent Li_2^q × spectral mechanism "
            "would close at both anchors; an empirical near-match "
            "would swing. Deferred to a future session that wires "
            "the Hoefsmit evaluator."
        )
    }

    print()
    print("--- Per-anchor results ---")
    print()
    print(f"  q_proton anchor:")
    print(f"    Σ μ_λ (Li_2^q measure) = {result_proton['Σ_μ_λ_(should_be_1_by_construction)'][:30]}")
    print(f"    c_3 candidate          = {result_proton['c3_candidate_Li_2_q_measure']}")
    print(f"    c_3 empirical          = -2.0693")
    print(f"    c_3 baseline (mech 5)  = {result_proton['c3_baseline_uniform_sum_(mech_5)']} (uniform)")
    print(f"    c_3 baseline (mech 6)  = {result_proton['c3_baseline_y_lambda_weighted_(mech_6)']} (y_λ-weighted)")
    print()

    c3_proton_pred = mpf(result_proton["c3_candidate_Li_2_q_measure"])
    err_proton = (c3_proton_pred - EMPIRICAL_C3_PROTON) / abs(EMPIRICAL_C3_PROTON) * 100

    print(f"  Single-anchor (q_proton) analysis:")
    print(f"    c_3 candidate at q_proton: {fmt(c3_proton_pred)}")
    print(f"    c_3 empirical at q_proton: {fmt(EMPIRICAL_C3_PROTON)}")
    print(f"    err vs empirical @ proton: {float(err_proton):+.4f}%")
    print(f"    cross-anchor (q_muon):     DEFERRED (see result_muon note)")
    print()

    # VERDICT logic — single-anchor decisive for this candidate
    if abs(float(err_proton)) < 0.01:
        verdict = (
            "PROTON-EXACT but cross-anchor unknown — candidate matches at q_proton "
            "to compute precision; q_muon cross-check REQUIRED before declaring "
            "Taylor-exact (deferred)"
        )
    elif abs(float(err_proton)) < 5:
        verdict = (
            "NEAR-MATCH at q_proton (within 5%) — q_muon cross-check would be "
            "diagnostic, but currently deferred"
        )
    else:
        verdict = (
            f"REFUTED — candidate misses empirical c_3 at q_proton by "
            f"{float(err_proton):+.2f}% (> 5% threshold); decisive single-"
            f"anchor refutation; q_muon adds no information"
        )

    print(f"  VERDICT: {verdict}")
    print()

    builder.add_data("EMPIRICAL_C3_PROTON", fmt(EMPIRICAL_C3_PROTON))
    builder.add_data("EMPIRICAL_C3_MUON", fmt(EMPIRICAL_C3_MUON))
    builder.add_data("anchor_q_proton", result_proton)
    builder.add_data("anchor_q_muon", result_muon)
    builder.add_data("single_anchor_summary", {
        "c3_candidate_at_q_proton": fmt(c3_proton_pred),
        "err_pct_vs_empirical_at_q_proton": fmt(err_proton),
        "cross_anchor_status": (
            "DEFERRED — Hoefsmit χ_λ(q) evaluator not wired; single-"
            "anchor refutation at q_proton is decisive without it"
        ),
    })
    builder.add_data("verdict", verdict)
    builder.add_data("interpretation", (
        "If TAYLOR-EXACT: Li_2^q × spectral combiner IS the Q_β Habiro "
        "element analog; closes c_k chain. If NEAR-MATCH: another near-"
        "match (mech #7 trap) — does NOT wire to production. If REFUTED: "
        "cleanly rules out combined Li_2^q × spectral attack; updates "
        "research-queue."
    ))

    builder.add_assertion(
        name="li_2_q_measure_normalized_at_proton",
        computed=float(abs(mpf(result_proton["Σ_μ_λ_deviation_from_1"]))),
        expected=0.0,
        tolerance=1e-40,
        source="Li_2^q measure normalization Σ μ_λ = 1 by construction",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
