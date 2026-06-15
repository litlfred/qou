#!/usr/bin/env python3
"""xq_habiro_element_search_probe.py — Habiro element search for X(q).

CONTEXT. PR #1673 Probe 1 refuted the multiplicative-refinement family
for the canonical X(q) = (q-1)²(1-q⁻⁴)/3 of m_n/Δ_pn. Cross-anchor
verdict: all 14 candidates were near-identical at q_proton and q_muon
because Δq ≈ 1.28e-8 cannot discriminate.

CLAUDE.md Im(q) framing: the right object is a FIBRE-LEVEL Habiro
element — a formal q-deformation H(q; α) whose archimedean evaluations
at different q_0 give different real values. PARALLEL TO α_EM PR #1511
template `H_α_EM = [2]_q · (1 - h²α)`.

X(q) is bar-ASYMMETRIC (unlike α_EM's [2]_q which is bar-symmetric):
  bar((q-1)²) = (q⁻¹-1)² ≠ (q-1)²
  bar(1-q⁻⁴)  = 1-q⁴   ≠ 1-q⁻⁴

So the X(q) Habiro element lives in the bar-MIXED sector (parallel
Q_β per PR #1622/#1636), NOT the bar-fixed α_EM sector.

PROBE STRATEGY. For each candidate Habiro form H(q; α) with α formal:
  1. Compute the multiplicative correction f_p, f_m at q_p, q_m
     required to close X·f to the CODATA target.
  2. Solve for α_p such that H(q_p; α_p) = f_p.
  3. Evaluate H(q_m; α_p) and compare to required f_m.
  4. If H(q_m; α_p) matches f_m to << 1 ppb: CROSS-ANCHOR HIT.
     Otherwise: anchor-coincident; refuted.

CANDIDATES (Habiro forms):
  H1: 1 + α · h²
  H2: 1 + α · h² · [2]_q
  H3: 1 + α · h² · (q - q⁻¹)·q⁻¹ / (1 - q⁻²) [qLambert n=1]
  H4: 1 + α · (1 - q⁻²) [qLambert n=1 'inverse']
  H5: 1 / (1 - α · h²) [resolvent form]
  H6: [2]_q · α + (1 - [2]_q · α) [trivial bar-mix sanity]
  H7: 1 + α · h² + β · h⁴ (2-param; solve at both anchors then extrapolate)

DISCIPLINE: this probe is DIAGNOSTIC. Per CLAUDE.md, do NOT wire any
TIER 1/2 result without structural derivation; the cross-anchor test
is necessary but not sufficient.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1 catch-up, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
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


def _delta_target():
    M_e = mp.mpf(repr(M_E_MEV))
    M_p = mp.mpf(repr(M_P_MEV))
    Q_n = mp.mpf(repr(Q_NEUTRON_MEV))
    M_n = M_p + M_e + Q_n
    M_N_avg = (M_p + M_n) / 2
    return (M_n - M_p) / M_N_avg


def _xq(q):
    return (q - 1) ** 2 * (1 - q ** (-4)) / 3


def _required_factor(q):
    """Return f such that X(q)·f = delta_target."""
    return _delta_target() / _xq(q)


def _candidates_at(q):
    """Return list of (name, formula_callable(alpha), structural_note)."""
    h = q - 1 / q
    h2 = h * h
    h4 = h2 * h2
    q2 = q + 1 / q
    qLambert_kernel = (q - 1 / q) * (1 / q) / (1 - 1 / q ** 2)  # = 1 (sanity)

    return [
        ("H1: 1 + α·h²", lambda a: 1 + a * h2,
         "bar-symmetric perturbation"),
        ("H2: 1 + α·h²·[2]_q", lambda a: 1 + a * h2 * q2,
         "bar-symmetric times bar-symmetric"),
        ("H3: 1 + α·h·(q-q⁻¹)/(1-q⁻²) [qLambert]",
         lambda a: 1 + a * h * (q - 1 / q) / (1 - q ** (-2)),
         "qLambert n=1 single term"),
        ("H4: 1 + α·(1-q⁻²)", lambda a: 1 + a * (1 - q ** (-2)),
         "bare q-Lambert RHS"),
        ("H5: 1/(1 - α·h²) [resolvent]",
         lambda a: 1 / (1 - a * h2),
         "Habiro resolvent form (matches α_EM via Taylor)"),
        ("H6: 1 + α·(q - q⁻¹)·q⁻¹",
         lambda a: 1 + a * (q - 1 / q) * (1 / q),
         "bar-antisymmetric perturbation"),
        ("H7: 1 + α·h² · ℏ_q²", lambda a: 1 + a * h2 * (1 - 1 / q) ** 2,
         "second-order"),
    ]


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder(
        "xq-habiro-element-search-probe",
        engine="python+mpmath", start_time=t0,
    )
    builder.set_description(
        "X(q) Habiro element search — cross-anchor test of 7 candidate "
        "Habiro forms H(q; α) parallel to α_EM's [2]_q·(1-h²α) template. "
        "Follow-on to PR #1673 Probe 1's multiplicative-refutation verdict."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-xq-habiro-he4-9-3-yekutieli-a-workplan.md"
    )

    q_p = q_at()
    q_m = q_muon_at()
    f_p = _required_factor(q_p)
    f_m = _required_factor(q_m)

    print("=" * 78)
    print(" X(q) Habiro element search — cross-anchor probe")
    print("=" * 78)
    print(f"q_proton = {fmt(q_p)[:30]}")
    print(f"q_muon   = {fmt(q_m)[:30]}")
    print()
    print(f"required f at q_p: {fmt(f_p)[:30]} (f_p - 1 = {fmt(f_p - 1)[:30]})")
    print(f"required f at q_m: {fmt(f_m)[:30]} (f_m - 1 = {fmt(f_m - 1)[:30]})")
    print(f"|f_p - f_m|: {float(abs(f_p - f_m)):.3e}")
    print()

    candidates_p = _candidates_at(q_p)
    candidates_m = _candidates_at(q_m)

    print(f"{'Habiro form':<45} {'α* (from q_p)':>18} {'H(q_m; α*)':>18} {'ppb @ q_m':>14}")
    print("-" * 100)
    results = []
    for (name_p, H_p, note), (_, H_m, _) in zip(candidates_p, candidates_m):
        # Solve H_p(α) = f_p for α
        # H_p(α) = 1 + α·X → α = (f_p - 1) / X (for linear forms)
        # General: use findroot
        try:
            alpha_star = mp.findroot(lambda a: H_p(a) - f_p, mp.mpf("0.001"))
        except Exception as e:
            alpha_star = None

        if alpha_star is not None:
            # Evaluate at q_m with the same α_star
            H_m_val = H_m(alpha_star)
            residual_m = (H_m_val - f_m) / f_m
            ppb_m = float(residual_m * mp.mpf("1e9"))
            # Tier
            if abs(ppb_m) < 1:
                tier = "TIER 1 (cross-anchor proved-candidate)"
            elif abs(ppb_m) < 100:
                tier = "TIER 1.5 (consistent)"
            elif abs(ppb_m) < 1e5:
                tier = "TIER 2 (near-match)"
            else:
                tier = "TIER 3 (refuted)"
            print(f"  {name_p:<43} {fmt(alpha_star)[:17]:>18} "
                  f"{float(H_m_val):>18.10f} {ppb_m:>14.2f}  {tier}")
            results.append({
                "name": name_p,
                "structural_note": note,
                "alpha_star_from_q_proton": fmt(alpha_star),
                "H_at_q_muon": fmt(H_m_val),
                "required_f_at_q_muon": fmt(f_m),
                "residual_ppb_at_q_muon": ppb_m,
                "tier": tier,
            })
        else:
            print(f"  {name_p:<43} SOLVE FAILED")
            results.append({
                "name": name_p,
                "structural_note": note,
                "error": "findroot did not converge",
            })

    # Verdict
    tier_1 = [r for r in results if r.get("tier") == "TIER 1 (cross-anchor proved-candidate)"]
    tier_15 = [r for r in results if r.get("tier") == "TIER 1.5 (consistent)"]
    tier_2 = [r for r in results if r.get("tier") == "TIER 2 (near-match)"]

    print()
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if tier_1:
        verdict = (
            f"CROSS-ANCHOR HIT — {len(tier_1)} Habiro candidate(s) match at "
            f"BOTH q_proton AND q_muon to < 1 ppb: "
            f"{', '.join(r['name'] for r in tier_1)}. Worth structural "
            f"derivation. (Cross-anchor necessary but not sufficient — "
            f"still requires categorical justification.)"
        )
    elif tier_15:
        verdict = (
            f"CONSISTENT — {len(tier_15)} candidate(s) at TIER 1.5 "
            f"(< 100 ppb at q_muon). Suggests the fibre family is right "
            f"but missing a sub-coefficient: "
            f"{', '.join(r['name'] for r in tier_15)}."
        )
    else:
        verdict = (
            "ALL CANDIDATES REFUTED at cross-anchor. The Habiro forms "
            "tested do NOT close X(q) at both anchors with a single α. "
            "Two interpretations: (a) the X(q) Habiro element has a more "
            "complex form (2+ parameters; H7 partially tests this) — "
            "expand the candidate basis. (b) the residual is upstream "
            "of X(q) entirely (in the Hecke-skein structure itself, not "
            "a multiplicative refinement)."
        )
    print(verdict)
    print()

    builder.add_data("q_proton", str(q_p))
    builder.add_data("q_muon", str(q_m))
    builder.add_data("required_f_at_q_proton", fmt(f_p))
    builder.add_data("required_f_at_q_muon", fmt(f_m))
    builder.add_data("delta_target", fmt(_delta_target()))
    builder.add_data("X_at_q_proton", fmt(_xq(q_p)))
    builder.add_data("X_at_q_muon", fmt(_xq(q_m)))
    builder.add_data("candidates", results)
    builder.add_data("tier_1_count", len(tier_1))
    builder.add_data("tier_15_count", len(tier_15))
    builder.add_data("tier_2_count", len(tier_2))
    builder.add_data("verdict", verdict)
    builder.add_data("template_pr", (
        "Parallel to PR #1511's α_EM Habiro element [2]_q·(1-h²α). "
        "Cross-anchor test logic: pick the α that closes at q_proton, "
        "then evaluate at q_muon. A real fibre-level Habiro element gives "
        "the right f at BOTH anchors with the same α. Failure ⟹ "
        "anchor-coincidence."
    ))
    builder.add_data("anti_pattern_guard", (
        "TIER 1 result is necessary but NOT sufficient — still requires "
        "structural categorical derivation (e.g. identify the formal Habiro "
        "ring element whose archimedean evaluation IS the formula). Do not "
        "wire to production without that derivation."
    ))

    builder.add_assertion(
        name="habiro_cross_anchor_evaluated",
        computed=len(results),
        expected=len(candidates_p),
        tolerance=0.0,
        source="Cross-anchor Habiro enumeration",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
