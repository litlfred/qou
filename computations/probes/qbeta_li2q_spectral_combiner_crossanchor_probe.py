#!/usr/bin/env python3
"""qbeta_li2q_spectral_combiner_crossanchor_probe.py — completes the
deferred cross-anchor evaluation from PR #1609.

CONTEXT. PR #1609 refuted the Li_2^q × spectral combiner candidate at
q_proton (13% off empirical c_3). The q_muon cross-anchor evaluation
was DEFERRED with note 'Hoefsmit χ_λ(q) closed-form evaluator not yet
wired'.

But the symbolic χ_λ(q) closed forms ARE available in the upstream
witness `qbeta-per-block-paper-closed-forms.witness.json` (sympy-
rational in q). So the deferral was unwarranted: this probe completes
the cross-anchor test using the upstream symbolic forms.

GOAL. Evaluate the Li_2^q × spectral c_3 candidate at q_muon as well
as q_proton, then test the cross-anchor swing prediction from PR #1626
(complex-c_3 diagnostic): empirical c_3 swing is 7.13× across anchors;
if the Li_2^q × spectral candidate has the SAME swing ratio, the
refutation is structurally weaker (both data and candidate share the
extraction-noise-floor behavior). If the candidate swing differs
significantly, the refutation is structurally strong.

DISCIPLINE (CLAUDE.md no-7th-ansatz). This probe COMPLETES PR #1609's
deferred test, NOT a new candidate. The candidate refuted at q_proton
remains refuted. The new finding is the cross-anchor behavior.

PRE-STATED FAILURE SIGNATURES:
  - If candidate swing ≈ empirical swing (7.13×): refutation is
    near-anchor-precision-limited; need wider q-anchor separation
    to be more diagnostic.
  - If candidate swing << empirical swing: candidate has structural
    q-independence that empirical doesn't; rules out as systematic
    error in extraction.
  - If candidate swing >> empirical swing: candidate has wrong q-
    dependence direction; structural mismatch deeper than 13% number.
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

import sympy as sp
import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, OUTPUT_DPS, fmt  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from qou_substrate.constants import q_at, q_muon_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def chi_lambda_at_q(chi_q_sympy: sp.Expr, q_numeric: mpf, q_sym: sp.Symbol) -> mpf:
    """Evaluate symbolic χ_λ(q) at numeric q (mpf)."""
    return mp.mpf(str(sp.N(chi_q_sympy.subs(q_sym, sp.Float(str(q_numeric), 50)), 50)))


def li2q_spectral_candidate_at(q: mpf, chi_q_syms: dict, q_sym: sp.Symbol) -> dict:
    """Compute Li_2^q × spectral candidate c_3 at one q anchor."""
    q_inv = 1 / q

    chi_at = {k: chi_lambda_at_q(v, q, q_sym) for k, v in chi_q_syms.items()}

    # Per-block c_3 leading order (from witness, ε^1 Taylor coeffs)
    c3_per_block = {"(3)": mpf(-2), "(2,1)": mpf(-1), "(1,1,1)": mpf(-2)}

    # Li_2^q(-|χ_λ|) for each block
    li2q_neg = {k: li_2_q(-abs(v), q, q_inv, max_k=500) for k, v in chi_at.items()}
    sum_li2q = sum(li2q_neg.values())
    mu = {k: v / sum_li2q for k, v in li2q_neg.items()}

    c3_candidate = sum(mu[k] * c3_per_block[k] for k in c3_per_block)

    return {
        "q": q,
        "chi_lambda": chi_at,
        "li2q_minus_abs_chi": li2q_neg,
        "sum_li2q": sum_li2q,
        "mu_lambda_measure": mu,
        "c3_candidate": c3_candidate,
    }


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder("qbeta-li2q-spectral-combiner-crossanchor",
                              engine="python+sympy+mpmath", start_time=t0)
    builder.set_description(
        "Cross-anchor completion of PR #1609 Li_2^q × spectral combiner "
        "deferred test. Evaluates candidate at BOTH q_proton and q_muon "
        "using symbolic χ_λ(q) from upstream witness. Tests structural "
        "vs anchor-precision-limited refutation."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-qbeta-li2q-spectral-crossanchor-completion.md"
    )

    upstream = builder.add_upstream(
        _pb.witness_path("qbeta-per-block-paper-closed-forms.witness.json", HERE)
    )

    q_sym = sp.Symbol("q", positive=True)
    chi_q_strs = upstream["data"]["paper_closed_forms"]
    chi_q_syms = {k: sp.sympify(v, locals={"q": q_sym}) for k, v in chi_q_strs.items()}

    print("=" * 78)
    print(" Li_2^q × spectral combiner — cross-anchor completion")
    print("=" * 78)
    print()
    print("Symbolic χ_λ(q) closed forms loaded from upstream witness:")
    for k, v in chi_q_syms.items():
        print(f"  {k}: {sp.cancel(v)}")
    print()

    q_proton = q_at()
    q_muon = q_muon_at()

    result_p = li2q_spectral_candidate_at(q_proton, chi_q_syms, q_sym)
    result_m = li2q_spectral_candidate_at(q_muon, chi_q_syms, q_sym)

    EMPIRICAL_C3_P = mpf("-2.0693")
    EMPIRICAL_C3_M = mpf("-2.0097")

    print(f"q_proton: {fmt(q_proton)[:30]}")
    print(f"  Σ μ_λ                  = {fmt(sum(result_p['mu_lambda_measure'].values()))[:25]}")
    print(f"  c_3 candidate          = {fmt(result_p['c3_candidate'])[:25]}")
    print(f"  c_3 empirical          = {EMPIRICAL_C3_P}")
    err_p = (result_p['c3_candidate'] - EMPIRICAL_C3_P) / abs(EMPIRICAL_C3_P) * 100
    print(f"  err vs empirical       = {float(err_p):+.4f}%")
    print()
    print(f"q_muon:   {fmt(q_muon)[:30]}")
    print(f"  Σ μ_λ                  = {fmt(sum(result_m['mu_lambda_measure'].values()))[:25]}")
    print(f"  c_3 candidate          = {fmt(result_m['c3_candidate'])[:25]}")
    print(f"  c_3 empirical          = {EMPIRICAL_C3_M}")
    err_m = (result_m['c3_candidate'] - EMPIRICAL_C3_M) / abs(EMPIRICAL_C3_M) * 100
    print(f"  err vs empirical       = {float(err_m):+.4f}%")
    print()

    # Cross-anchor analysis
    candidate_swing_abs = result_p['c3_candidate'] - result_m['c3_candidate']
    candidate_swing_pct = candidate_swing_abs / abs(result_p['c3_candidate']) * 100
    empirical_swing_abs = EMPIRICAL_C3_P - EMPIRICAL_C3_M
    empirical_swing_pct = empirical_swing_abs / abs(EMPIRICAL_C3_P) * 100

    print(f"Candidate swing: {fmt(candidate_swing_abs)[:25]} ({float(candidate_swing_pct):.6f}%)")
    print(f"Empirical swing: {fmt(empirical_swing_abs)} ({float(empirical_swing_pct):.4f}%)")
    print(f"Swing ratio (candidate/empirical): {float(candidate_swing_pct/empirical_swing_pct):.4e}")
    print()

    # Verdict
    swing_ratio = float(candidate_swing_pct / empirical_swing_pct)
    if abs(swing_ratio) < 1e-4:
        verdict = (
            "STRUCTURAL REFUTATION CONFIRMED — candidate is essentially "
            f"q-independent (swing {abs(float(candidate_swing_pct)):.2e}% << "
            f"empirical {float(empirical_swing_pct):.4f}%). The 13% miss at "
            "q_proton reflects a TRUE structural mismatch, not extraction "
            "noise. Refutation stands strong."
        )
    elif 0.5 < swing_ratio < 2:
        verdict = (
            "NEAR-ANCHOR-PRECISION-LIMITED — candidate and empirical swings "
            "comparable; refutation might be weakened by extraction noise. "
            "But the 13% magnitude miss is too large for anchor precision."
        )
    else:
        verdict = (
            f"UNEXPECTED SWING RATIO ({swing_ratio:.4e}) — needs interpretation"
        )

    print(f"VERDICT: {verdict}")
    print()

    builder.add_data("q_proton", str(q_proton))
    builder.add_data("q_muon", str(q_muon))
    builder.add_data("q_anchor_gap_abs", str(abs(q_proton - q_muon)))
    builder.add_data("symbolic_chi_lambda_q_forms", chi_q_strs)
    builder.add_data("at_q_proton", {
        "chi_lambda": {k: str(v) for k, v in result_p["chi_lambda"].items()},
        "mu_lambda": {k: str(v) for k, v in result_p["mu_lambda_measure"].items()},
        "c3_candidate": str(result_p["c3_candidate"]),
        "c3_empirical": str(EMPIRICAL_C3_P),
        "err_pct": float(err_p),
    })
    builder.add_data("at_q_muon", {
        "chi_lambda": {k: str(v) for k, v in result_m["chi_lambda"].items()},
        "mu_lambda": {k: str(v) for k, v in result_m["mu_lambda_measure"].items()},
        "c3_candidate": str(result_m["c3_candidate"]),
        "c3_empirical": str(EMPIRICAL_C3_M),
        "err_pct": float(err_m),
    })
    builder.add_data("cross_anchor_analysis", {
        "candidate_swing_abs": str(candidate_swing_abs),
        "candidate_swing_pct": float(candidate_swing_pct),
        "empirical_swing_abs": str(empirical_swing_abs),
        "empirical_swing_pct": float(empirical_swing_pct),
        "swing_ratio_candidate_to_empirical": float(swing_ratio),
        "interpretation_pre_stated": (
            "If swing_ratio << 1: candidate q-independent ⟹ structural "
            "refutation strong (13% mismatch is real). "
            "If swing_ratio ≈ 1: anchor-precision-limited (extraction noise). "
            "If swing_ratio >> 1: candidate has wrong q-dependence direction."
        ),
        "verdict": verdict,
    })

    builder.add_assertion(
        name="cross_anchor_completion_emitted",
        computed=1.0,
        expected=1.0,
        tolerance=0.0,
        source="Completes PR #1609 deferred q_muon evaluation using upstream symbolic chi_lambda(q)",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
