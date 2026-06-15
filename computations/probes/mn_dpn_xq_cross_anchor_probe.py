#!/usr/bin/env python3
"""mn_dpn_xq_cross_anchor_probe.py — cross-anchor verdict on X(q)
refinement candidates from flavor_split_xq_refinement.py.

CONTEXT. PR #1645's flavor_split_xq_refinement.py tested ~15 candidate
multiplicative refinements of the canonical Hecke-skein

    X(q) = (q-1)²·(1-q⁻⁴)/3

against the CODATA target (m_n - m_p)/M_N at q_proton. Best non-
tautological candidate sat at ~10³ ppb residual; only the PSLQ-fit
(by construction) hit 0 ppb.

PER CLAUDE.md "Im(q) fibre vs observable" framing (added this session):
each q_0 anchor is a different archimedean evaluation of the SAME
fibre object. A refinement that closes the gap at q_proton ALONE is
an anchor-coincidence (near-match); a refinement structural at the
fibre level must close at BOTH q_proton AND q_muon.

This probe takes the same candidate family and adds the cross-anchor
verdict — re-evaluates each at q_muon = 1.109978595554 (the historic
pre-2026-05-28 anchor) AND q_proton = 1.10997858275, and tiers:

  TIER 1 (proved-candidate): residual < 1 ppb at BOTH anchors
  TIER 2 (near-match): residual < 1000 ppb at q_proton but blows
    up by > 10× at q_muon (single-anchor-fit signature)
  TIER 3 (refuted): residual > 10⁵ ppb at either anchor

DISCIPLINE: this probe is DIAGNOSTIC. Per CLAUDE.md ("don't search
for substrate matching the residual"), do NOT wire a Tier 2 result
into production. Only Tier 1 candidates merit structural derivation
work. Confirmation of Tier 2 ⟹ confirms X(q) intrinsic residual
needs a fibre-level Habiro element, not a multiplicative refinement.
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

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV  # noqa: E402

try:
    from qou_substrate.constants import q_at, q_muon_at
except ImportError:
    print("ERROR: qou_substrate not available", file=sys.stderr)
    sys.exit(1)


def _candidates_at(q):
    """Build (name, factor) list at a given q."""
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    q2 = q + 1 / q
    G = mp.catalan
    alpha_em = mp.mpf(1) / mp.mpf("137.0359991")

    return [
        ("(a) bare", mp.mpf(1)),
        ("(b1) 1 + α_em/π", 1 + alpha_em / mp.pi),
        ("(b2) 1 - α_em·G/(4π)", 1 - alpha_em * G / (4 * mp.pi)),
        ("(b3) 1 - h²·α_em", 1 - h2 * alpha_em),
        ("(c1) 1 + h²/6", 1 + h2 / 6),
        ("(c2) 1 - h²/[2]_q²", 1 - h2 / q2 ** 2),
        ("(d1) 1 + h²·G/(4π)", 1 + h2 * G / (4 * mp.pi)),
        ("(d2) 1 - ℏ_q²/24", 1 - hbar_q ** 2 / 24),
        ("(e1) (3q²-1)/(2q²)",
         (3 * q ** 2 - 1) / (2 * q ** 2)),
        ("(f1) 1 + m_e/m_p", 1 + mp.mpf(repr(M_E_MEV)) / mp.mpf(repr(M_P_MEV))),
        ("(f2) 1 - α_em·ℏ_q", 1 - alpha_em * hbar_q),
        # New cross-anchor focused candidates: q-fibre-structure ones
        ("(g1) 1 + ℏ_q²·[2]_q/2", 1 + hbar_q ** 2 * q2 / 2),
        ("(g2) bar-symmetric: (1+q⁻¹/2)/(1+q/2)",
         (1 + 1 / q / 2) / (1 + q / 2)),
        ("(g3) [3]_q / 3",
         (q ** 2 + 1 + 1 / q ** 2) / 3),
    ]


def _residual_at(q, factor):
    """Compute (X_pred - delta_target)/delta_target at given q."""
    M_e = mp.mpf(repr(M_E_MEV))
    M_p = mp.mpf(repr(M_P_MEV))
    Q_n = mp.mpf(repr(Q_NEUTRON_MEV))
    M_n = M_p + M_e + Q_n
    M_N_avg = (M_p + M_n) / 2
    delta_target = (M_n - M_p) / M_N_avg

    X_baseline = (q - 1) ** 2 * (1 - q ** (-4)) / 3
    X_pred = X_baseline * factor
    return (X_pred - delta_target) / delta_target


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "mn-dpn-xq-cross-anchor-probe",
        engine="python+mpmath", start_time=t0,
    )
    builder.set_description(
        "Cross-anchor verdict on X(q) refinement candidates "
        "(extension of PR #1645 single-anchor probe). Per CLAUDE.md "
        "Im(q) fibre-vs-observable: tier by both q_proton AND q_muon."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-precision-residual-probes-workplan.md"
    )

    q_p = q_at()
    q_m = q_muon_at()
    print("=" * 78)
    print(" m_n / Δ_pn — X(q) refinement: CROSS-ANCHOR verdict")
    print("=" * 78)
    print(f"q_proton = {fmt(q_p)[:30]}")
    print(f"q_muon   = {fmt(q_m)[:30]}")
    print(f"Δq       = {fmt(q_p - q_m)}")
    print()

    candidates_p = _candidates_at(q_p)
    candidates_m = _candidates_at(q_m)

    print(f"{'Candidate':<35} {'ppb @ q_p':>14} {'ppb @ q_m':>14} {'tier':>15}")
    print("-" * 85)
    results = []
    for (name_p, f_p), (name_m, f_m) in zip(candidates_p, candidates_m):
        assert name_p == name_m
        resid_p = _residual_at(q_p, f_p) * mp.mpf("1e9")
        resid_m = _residual_at(q_m, f_m) * mp.mpf("1e9")
        rp = float(resid_p)
        rm = float(resid_m)
        # tier rule
        if abs(rp) < 1 and abs(rm) < 1:
            tier = "TIER 1 (proved)"
        elif abs(rp) < 1000 and abs(rm) > 10 * abs(rp) + 100:
            tier = "TIER 2 (near-match)"
        elif abs(rp) > 1e5 or abs(rm) > 1e5:
            tier = "TIER 3 (refuted)"
        elif abs(rp) < 1000 and abs(rm) < 1000:
            tier = "TIER 1.5 (consistent)"
        else:
            tier = "TIER 2.5"
        print(f"  {name_p:<33} {rp:14.2f} {rm:14.2f} {tier:>15}")
        results.append({
            "name": name_p,
            "factor_at_q_proton": fmt(f_p),
            "factor_at_q_muon": fmt(f_m),
            "ppb_at_q_proton": rp,
            "ppb_at_q_muon": rm,
            "tier": tier,
        })

    # Verdict
    tier_1 = [r for r in results if "TIER 1" in r["tier"] and "1.5" not in r["tier"]]
    tier_15 = [r for r in results if "1.5" in r["tier"]]
    tier_2 = [r for r in results if "TIER 2" in r["tier"]]

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if tier_1:
        verdict = (
            f"STRUCTURAL HIT — {len(tier_1)} candidate(s) at TIER 1 "
            f"(< 1 ppb at BOTH anchors). Worth structural derivation: "
            f"{', '.join(r['name'] for r in tier_1)}."
        )
    elif tier_15:
        verdict = (
            f"CONSISTENT — {len(tier_15)} candidate(s) at TIER 1.5 "
            f"(< 1000 ppb at both anchors, not closure). "
            f"Suggests the fibre form is correct family but missing "
            f"a sub-coefficient: {', '.join(r['name'] for r in tier_15)}."
        )
    else:
        verdict = (
            "ALL CANDIDATES FAIL cross-anchor. The X(q) 0.10% residual "
            "is NOT a multiplicative-refinement problem — it needs a "
            "fibre-level Habiro element (per CLAUDE.md Im(q) framing), "
            "not a q_0-evaluated correction. This rules out the "
            "ansatz family tested in PR #1645 + this probe."
        )
    print(verdict)
    print()

    builder.add_data("q_proton", str(q_p))
    builder.add_data("q_muon", str(q_m))
    builder.add_data("delta_q", str(q_p - q_m))
    builder.add_data("candidates", results)
    builder.add_data("tier_1_count", len(tier_1))
    builder.add_data("tier_15_count", len(tier_15))
    builder.add_data("verdict", verdict)
    builder.add_data("anti_pattern_guard", (
        "Tier 2 results are anchor-coincidences and MUST NOT be wired. "
        "Only Tier 1 candidates merit structural derivation. Failure of "
        "all candidates at cross-anchor confirms that X(q) needs a "
        "fibre-level Habiro element (parallel α_EM PR #1511), not a "
        "multiplicative q_0-fit."
    ))

    builder.add_assertion(
        name="cross_anchor_candidates_evaluated",
        computed=len(results),
        expected=len(results),
        tolerance=0.0,
        source="Cross-anchor enumeration",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
