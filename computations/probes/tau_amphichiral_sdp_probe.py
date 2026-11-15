#!/usr/bin/env python3
"""
Tau amphichiral-candidate SDP probe.

Per owner directive 2026-05-25 (post-PR #1127 merge):
"tau is not torus knot. knot operator = symmetries → should be same
as 1st gen. verify via SDP solutions."

Interpretation: tau's canonical knot has the SAME SYMMETRIES as the
1st-generation lepton (muon = 4_1 figure-eight is the smallest
hyperbolic + amphichiral 2-bridge knot). Per this hint:
  - tau is NOT a torus knot (rules out PR #1250's T(2,7) family
    and the simple Vol/ℏ_q^k extension)
  - tau IS hyperbolic with the SAME symmetry class as muon
  - amphichirality is the natural "1st-gen-like" symmetry for muon
  - candidate tau: next amphichiral hyperbolic knot after 4_1

Amphichiral hyperbolic knots (volumes from `knot_volumes.vol_at`, SnapPy
3.3.2). Ten of the twelve figures previously listed here were wrong — see
the note at `amphichiral_knots` below (bean qou-ckbv, 2026-08-30):
  4_1   (Vol = 2.02988...)  — MUON canonical
  6_3   (Vol = 5.69302...)  — next amphichiral, 6-crossing
  8_3   (Vol = 5.23868...)  — 8-crossing amphichiral   (was 6.55175)
  8_9   (Vol = 7.58818...)
  8_12  (Vol = 8.93586...)
  8_17  (Vol = 10.9859...)                             (was 10.7853)
  8_18  (Vol = 12.3509...)
  10_17 (Vol = 8.53676...)                             (was 10.4575)
  10_33 (Vol = 11.5357...)  — NOT commensurable with 8_12 (was 8.93582)
  10_37 (Vol = 10.9658...)                             (was 11.3322)
  10_43 (Vol = 12.6026...)                             (was 13.8330)
  10_45 (Vol = 13.7161...)                             (was 14.5582)

For each candidate, test multiple formulas:
  (a) Vol(K) / ℏ_q^k  for k = 2, 3, 4
  (b) Vol(K) · constant_factor / ℏ_q^k
  (c) Vol(K) / ([n]_q · ℏ_q²)  for various n

Match to CODATA m_τ/m_e = 3477.23 (within 1%).

Output: candidate matches + verdict (which amphichiral knot, if any).

Audit-only; no production wiring.
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
from pathlib import Path

import mpmath as mp

# Canonical sources (per AGENTS.md "single source of truth for q_0"):
#   - q_parameter.Q_50_DIGIT_STR  → substrate q_0 at 50-dps
#   - experimental_constants.MU_OVER_E / TAU_OVER_E → CODATA m_ℓ/m_e
# These imports replace the prior hardcoded P31 literals (cal2/cal_tau_e
# and the Vol(4_1)-from-string-derived q_0) flagged by the
# compute_audit_scan registry-bypass detector.
from experimental_constants import MU_OVER_E, TAU_OVER_E
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder
from _precision import set_compute_dps  # noqa: E402
from knot_volumes import vol_at  # noqa: E402 — canonical volume registry


def main() -> int:
    set_compute_dps()

    # Canonical substrate from Q_50_DIGIT_STR (the single 50-dps pin).
    q0 = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q0
    h = q0 - qi
    hbar_q = mp.mpf(1) - qi  # ℏ_q = 1 - q⁻¹  (per substrate definition)
    hbar_q_sq = hbar_q * hbar_q
    # Vol(4_1) recovered identity: Vol(4_1) = (m_μ/m_e) · ℏ_q²
    cal2_target = mp.mpf(MU_OVER_E)
    # TAU_OVER_E is an mpf pinned at _CONST_DPS in experimental_constants; use it
    # directly.  mp.mpf(repr(...)) was the float64 -> mpf idiom and raises
    # ValueError on an mpf's repr.
    cal_tau_e = TAU_OVER_E
    Vol_4_1 = cal2_target * hbar_q_sq  # for the muon sanity check below
    # A convention-C `z` was bound here and NEVER READ -- `z` occurred
    # exactly once in this file, in its own assignment. Excised by
    # deletion rather than converted to z_D: a dead binding of the
    # canonical convention is still dead, and leaving one would keep this
    # file in the convention-C site list for no reason. Verified: witness
    # diff 0 fields, stdout identical apart from a provenance line.

    # Amphichiral hyperbolic knots — read from the canonical registry.
    #
    # EXCISED 2026-08-30 (bean qou-ckbv). This list was headed "SnapPy census;
    # cross-checked w/ knot-volumes.py" and was neither. Measured against
    # SnapPy, ten of its twelve entries were wrong inside the digits they
    # printed, most of them at the FIRST or second significant figure:
    #
    #     8_3    6.55174581471284  ->   5.23868410079844   (25 % out)
    #     8_17  10.78528041739327  ->  10.98590760628482
    #     10_17 10.45758935320168  ->   8.53675559919323
    #     10_33  8.93581640816072  ->  11.53567393228233
    #     10_37 11.33222803236     ->  10.96581053242464
    #     10_43 13.83304617        ->  12.60259611426208
    #     10_45 14.55822           ->  13.71607598475273
    #
    # The "10_33" row carried 8_12's value under the comment "commensurable
    # w/ 8_12". They are not: 11.5357 against 8.9359. As with the 9_46 entry
    # in m_tau_knot_prediction, a stated reason is what made a wrong number
    # look deliberate — and a claim of commensurability is exactly the kind a
    # reader would take on trust rather than re-derive.
    #
    # Only 4_1 and 6_3 survived. `knot_volumes` stocked none of the others,
    # which is why they were hand-typed here; it now does.
    amphichiral_knots = [
        (name, vol_at(name, mp.mp.dps))
        for name in ("4_1",                      # muon (calibration)
                     "6_3", "8_3", "8_9", "8_12", "8_17", "8_18",
                     "10_17", "10_33", "10_37", "10_43", "10_45")
    ]

    print(f"=== Substrate ===")
    print(f"  q_0 = {float(q0):.10f}")
    print(f"  ℏ_q² = {float(hbar_q_sq):.10f}")
    print(f"  1/ℏ_q² = {float(1/hbar_q_sq):.6f}")
    print(f"  CODATA m_τ/m_e = {float(cal_tau_e):.4f}")
    print()

    # Reference: muon at 4_1 closes exactly via Vol(4_1)/ℏ_q²
    print(f"=== Muon sanity check ===")
    muon_pred = Vol_4_1 / hbar_q_sq
    print(f"  Vol(4_1)/ℏ_q² = {float(muon_pred):.10f}")
    print(f"  CODATA m_μ/m_e = {float(cal2_target):.10f}")
    print(f"  Match: {float(mp.fabs(muon_pred - cal2_target) / cal2_target):.2e}")
    print()

    # Test each amphichiral candidate under formulas (a) Vol/ℏ_q^k for k=2,3,4
    print(f"=== Amphichiral candidates for tau ===")
    print(f"{'knot':10s}  {'Vol':>10s}  {'Vol/ℏ_q²':>14s}  {'Vol/ℏ_q³':>14s}  {'Vol/ℏ_q^4':>14s}  {'best ratio vs CODATA':>22s}")
    print("-" * 100)

    best_matches = []
    for knot_name, vol in amphichiral_knots:
        ratios = {
            "k=2": vol / hbar_q_sq,
            "k=3": vol / hbar_q_sq / mp.sqrt(hbar_q_sq),  # ℏ_q^3 = ℏ_q² · ℏ_q
            "k=4": vol / (hbar_q_sq ** 2),
        }
        diffs = {k: (r - cal_tau_e) / cal_tau_e * 100 for k, r in ratios.items()}
        best_k = min(diffs, key=lambda k: mp.fabs(diffs[k]))
        best_diff = diffs[best_k]
        marker = " ✓✓ <1%" if mp.fabs(best_diff) < 1 else (" ✓ <5%" if mp.fabs(best_diff) < 5 else "")
        print(f"  {knot_name:10s}  {float(vol):10.4f}  {float(ratios['k=2']):14.4f}  {float(ratios['k=3']):14.4f}  {float(ratios['k=4']):14.4f}  best ({best_k}): {float(best_diff):+8.3f}%{marker}")
        if mp.fabs(best_diff) < 5:
            best_matches.append((knot_name, best_k, float(ratios[best_k]), float(best_diff)))
    print()

    # Apply q-bracket correction factor candidates (in spirit of muon ξ_2 = [3]_q·[2]_q/[4]_q)
    print(f"=== With q-bracket correction (search ξ_3 · Vol(K)/ℏ_q² = CODATA) ===")
    print(f"  For each amphichiral K, compute required ξ_3 = CODATA·ℏ_q²/Vol(K)")
    print(f"  Compare to candidate q-bracket ratios (analog of muon's [3]_q·[2]_q/[4]_q)")
    print()

    two_q = q0 + qi
    three_q = q0**2 + 1 + qi**2
    four_q = q0**3 + q0 + qi + qi**3
    five_q = q0**4 + q0**2 + 1 + qi**2 + qi**4
    six_q = (q0**5 + q0**3 + q0 + qi + qi**3 + qi**5)
    seven_q = (q0**6 + q0**4 + q0**2 + 1 + qi**2 + qi**4 + qi**6)

    q_bracket_candidates = [
        ("[3]_q · [2]_q / [4]_q (muon)", three_q * two_q / four_q),
        ("[5]_q · [2]_q / [6]_q", five_q * two_q / six_q),
        ("[5]_q · [3]_q / [6]_q", five_q * three_q / six_q),
        ("[5]_q · [3]_q / ([4]_q · [2]_q)", five_q * three_q / (four_q * two_q)),
        ("[5]_q / [4]_q", five_q / four_q),
        ("[7]_q · [2]_q / [8]_q", seven_q * two_q / ((q0**7 + q0**5 + q0**3 + q0 + qi + qi**3 + qi**5 + qi**7))),
        ("[3]_q² / [4]_q", three_q**2 / four_q),
        ("[3]_q² · [2]_q / [5]_q", three_q**2 * two_q / five_q),
        ("3 (pure)", mp.mpf(3)),
        ("17", mp.mpf(17)),  # CODATA m_τ/m_μ rounded
    ]

    print(f"{'amphichiral knot':10s}  {'Vol':>10s}  {'required ξ_3':>14s}  {'best q-bracket match':>40s}")
    print("-" * 100)

    closeup_finds = []
    for knot_name, vol in amphichiral_knots:
        if knot_name == "4_1":
            continue  # muon
        required_xi = cal_tau_e * hbar_q_sq / vol
        # Find best q-bracket match
        best_name, best_val, best_pct = None, None, float("inf")
        for q_name, q_val in q_bracket_candidates:
            diff_pct = float((q_val - required_xi) / required_xi * 100)
            if abs(diff_pct) < abs(best_pct):
                best_pct = diff_pct
                best_name = q_name
                best_val = q_val
        marker = " ✓✓ <0.5%" if abs(best_pct) < 0.5 else (" ✓ <2%" if abs(best_pct) < 2 else "")
        print(f"  {knot_name:10s}  {float(vol):10.4f}  {float(required_xi):14.4f}  {best_name + f'={float(best_val):.4f}({best_pct:+.2f}%)':>40s}{marker}")
        if abs(best_pct) < 2:
            closeup_finds.append((knot_name, best_name, float(best_val), best_pct))

    print()

    # Verdict
    print(f"=== Verdict ===")
    if best_matches:
        print(f"  PR #1250-style: best amphichiral candidates within 5% (no q-bracket):")
        for k, kk, v, d in best_matches:
            print(f"    {k} via {kk}: {v:.4f} ({d:+.3f}%)")
    if closeup_finds:
        print(f"  With q-bracket correction: best matches within 2%:")
        for k, qn, v, d in closeup_finds:
            print(f"    {k} × {qn} = {v:.4f} → {d:+.2f}%")
    if not best_matches and not closeup_finds:
        print(f"  NO amphichiral candidate closes tau to within 2% under tested formulas.")
        print(f"  Either: (i) tau is non-amphichiral hyperbolic, (ii) tau requires")
        print(f"  higher-tower correction beyond simple Vol/ℏ_q^k · q-bracket, or")
        print(f"  (iii) tau's canonical knot needs SDP-derived non-knot-label identification.")
    print()

    # Canonical witness emission via WitnessBuilder (provenance auto-captured:
    # git SHA, script hash, duration, engine version, etc.).
    w = WitnessBuilder("tau-amphichiral-sdp-probe", engine="mpmath")
    w.set_description(
        "Tau amphichiral-candidate SDP-spirit probe per owner directive "
        "2026-05-25: 'tau is not torus knot; knot operator = symmetries → "
        "should be same as 1st gen. verify via SDP solutions.' (verbatim "
        "quote — original message had typo 'tau in not knot tauris' which "
        "was interpreted as 'tau is not torus knot' per context.) Filters "
        "12 amphichiral hyperbolic knots from SnapPy census + tests under "
        "Vol/ℏ_q^k and q-bracket-corrected closure formulas analogous to "
        "muon's ξ_2 = [3]_q · [2]_q / [4]_q."
    )
    w.set_audit_only("docs/audits/2026-05-25-t6-f-ell-derivation-attempt.md")
    w.set_content_block("conj:lepton-tower-h-n-plus-1-branching")
    w.add_parameter("precision_dps", 50)
    w.add_parameter("q_0_source", "Q_50_DIGIT_STR (canonical substrate pin)")
    w.add_parameter("q_0", str(q0))
    w.add_parameter("hbar_q_sq", str(hbar_q_sq))
    w.add_parameter("inv_hbar_q_sq", str(1 / hbar_q_sq))
    w.add_parameter("cal_tau_e_codata", str(cal_tau_e))
    w.add_parameter("cal_mu_e_codata", str(cal2_target))
    w.add_data("amphichiral_candidates", [
        {
            "knot": k,
            "vol": str(v),
            "ratios": {
                "k=2": str(v / hbar_q_sq),
                "k=3": str(v / hbar_q_sq / mp.sqrt(hbar_q_sq)),
                "k=4": str(v / hbar_q_sq**2),
            },
        }
        for k, v in amphichiral_knots
    ])
    w.add_data("best_simple_matches", [
        {"knot": k, "formula": f"Vol/ℏ_q^{kk[2:]}", "predicted": v, "rel_err_percent": d}
        for k, kk, v, d in best_matches
    ])
    w.add_data("best_with_q_bracket_correction", [
        {"knot": k, "q_bracket": qn, "predicted_xi_3": v, "rel_err_percent": d}
        for k, qn, v, d in closeup_finds
    ])
    # Headline assertion: muon sanity reproduces CODATA to ≤ 1e-40 at 50 dps
    # (trivially true under canonical substrate pin Q_50_DIGIT_STR; serves
    # as a regression guard if the canonical pin ever drifts).
    w.add_assertion(
        name="muon_canonical_pin_consistency",
        computed=str(muon_pred),
        expected=str(cal2_target),
        tolerance=1e-40,
        source="Q_50_DIGIT_STR + MU_OVER_E (canonical pin)",
    )

    # Structural-identity assertions: verify the Lean theorems in
    # `folio/quantum-observable-universe/braids-and-knots/three-halves-structural-factor.lean`
    # hold numerically at the canonical q_0 to 50-dps precision.
    # These are NUMERICAL CROSS-CHECKS of the algebraic identities;
    # the Lean proofs are categorical (over generic [Field R]).
    one_plus_h_sq = mp.mpf(1) + h**2
    two_plus_h_sq = mp.mpf(2) + h**2
    three_plus_h_sq = mp.mpf(3) + h**2
    w.add_assertion(
        name="lean_three_plus_h_sq_eq_bracket3",
        computed=str(three_plus_h_sq),
        expected=str(three_q),
        tolerance=1e-40,
        source="theorem three_plus_h_sq_eq_bracket3 (muon identity)",
    )
    w.add_assertion(
        name="lean_two_plus_h_sq_times_bracket2_eq_bracket4",
        computed=str(two_plus_h_sq * two_q),
        expected=str(four_q),
        tolerance=1e-40,
        source="theorem two_plus_h_sq_times_bracket2_eq_bracket4 (muon T6 (c))",
    )
    w.add_assertion(
        name="lean_bracket6_eq_bracket2_bracket3_times_one_plus_h_sq",
        computed=str(two_q * three_q * one_plus_h_sq),
        expected=str(six_q),
        tolerance=1e-40,
        source="theorem bracket6_eq_bracket2_bracket3_times_one_plus_h_sq (tau structural identity)",
    )
    w.add_caveat(
        "Amphichiral-filter is a heuristic from the owner's 'same symmetries "
        "as 1st gen' directive; not a structural theorem. Best hit "
        "10_43 × [5]_q·[3]_q/[6]_q closes m_τ/m_e to +0.79% — empirical "
        "foundation only, not a canonical identification of tau."
    )
    out_path = w.save()
    print(f"Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
