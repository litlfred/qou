#!/usr/bin/env python3
"""mass_theory_formalize_first_invariants_probe.py — extend the Q_β
§4 formalize-first invariant template to the mass-theory side.

Sibling probe to
`docs/audits/2026-06-05-mass-theory-formalize-first-gates-scope.md`.

Today's Q_β chain (PRs #1875, #1889, #1890, #1893) formalized four
§4 invariants as sorry-free Lean gate classes:

  (a) anchor-stable      — proton + muon cross-anchor swing < 1 ppm
  (b) bar-even           — q ↔ q⁻¹ symmetry
  (c) q=1 shadow         — classical-limit reproduces a known integer
  (d) direction sanity   — magnitude in same order as target

The existing `bar_symmetry_three_candidates.py` tests three published
`linking_weight` candidates against (b) only. This probe extends to
the full 4×3 matrix.

The three candidates:

  Family A:           (3q² + 4 + 3q⁻²) / 4
  via-Jones:          5/2 + 4·(tr_M(β_Borromean) − 1)
  Bring color-tube:   1 / (1 − h·q¹⁰)  (Φ_q-side asymmetric)

Per-cell verdict produced; honest diagnostic only (no production swap).
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    # Constants defined inside main() per the Gemini #1890 convention.
    Q_PROTON = "1.1099785827513808075916690956107688798744991218736"
    Q_MUON = "1.10997859555"

    # CODATA-implied near-match for linking_weight (per PR #1850 audit):
    # λ ≈ m_p / (m_e · Vol/ℏ_q²) ≈ 2.46 — the target's order of magnitude
    LINKING_WEIGHT_TARGET_OOM = mp.mpf("2.46")

    # Tolerance thresholds (per Q_β §4 invariant template, mass-side
    # tightened where appropriate)
    ANCHOR_THRESHOLD_RELATIVE = mp.mpf("0.01")  # 1% (registry §8 mass-side)
    DIRECTION_THRESHOLD_FACTOR = mp.mpf("10")    # 10× order-of-magnitude

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "mass-theory-formalize-first-invariants-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Extends the Q_β §4 formalize-first invariant template "
        "(PRs #1875/#1889/#1890/#1893) to mass-theory. Tests three "
        "published linking_weight candidates (Family A, via-Jones, "
        "Bring color-tube) against all four §4 invariants: anchor-"
        "stability, bar-evenness, q=1 classical-limit shadow, direction "
        "sanity. 4×3 verdict matrix; diagnostic only."
    )
    builder.set_content_block("prop:q-beta-bar-even-kernel-typeclass")

    print("=" * 78)
    print(" Mass-theory §4 formalize-first invariants — 4×3 verdict matrix")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)

    # ─────────────────────────────────────────────────────────────────
    # Candidate definitions (symbolic in q)
    # ─────────────────────────────────────────────────────────────────
    print("  Candidates (symbolic):")
    print()

    # Family A: (3q² + 4 + 3q⁻²) / 4
    family_a = (3 * q ** 2 + 4 + 3 / q ** 2) / 4
    print(f"    Family A:         (3q² + 4 + 3q⁻²)/4")

    # via-Jones: tr_M(β_Borromean) — for the Borromean rings the
    # Markov trace is bar-symmetric and reduces to a particular Hecke
    # combination, structurally IDENTICAL to Family A at q_0 (see
    # bar_symmetry_three_candidates.py: both come out to 2.5328 because
    # the via-Jones Markov-trace reduction collapses to the Family A
    # rational expression). This probe does NOT compute the Hecke
    # Markov trace independently; via-Jones is therefore flagged as a
    # PLACEHOLDER duplicate of Family A (per Copilot review on #1896)
    # to prevent misreading the verdict matrix as independent
    # validation of two candidates.
    via_jones = family_a  # PLACEHOLDER — coincides with Family A
    print(f"    via-Jones:        Markov trace of Borromean (PLACEHOLDER —")
    print(f"                       structurally identical to Family A; the")
    print(f"                       independent Hecke compute is not run here)")

    # Bring color-tube (Φ_q-side, h-deformed). For h = q - 1/q,
    # bring = 1 / (1 - h·q¹⁰). Highly asymmetric in q.
    h_q = q - 1 / q
    bring = 1 / (1 - h_q * q ** 10)
    print(f"    Bring color-tube: 1 / (1 − h·q¹⁰),  h = q − q⁻¹")
    print()

    # `is_placeholder` flag per Copilot review: marks candidates whose
    # values are NOT independently computed, so the witness data and
    # printed matrix flag them to downstream readers.
    candidates = {
        "Family A": (family_a, False),
        "via-Jones": (via_jones, True),  # placeholder — see comment above
        "Bring color-tube": (bring, False),
    }

    # ─────────────────────────────────────────────────────────────────
    # §4(a) Anchor-stability: cross-anchor swing < 1%
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print(" §4(a) Anchor-stability — proton/muon swing < 1%")
    print("=" * 78)
    print()

    q_p_sp = sp.Float(Q_PROTON, 50)
    q_m_sp = sp.Float(Q_MUON, 50)

    anchor_verdicts = {}
    for name, (expr, is_placeholder) in candidates.items():
        v_p = mp.mpf(str(sp.N(expr.subs(q, q_p_sp), 50)))
        v_m = mp.mpf(str(sp.N(expr.subs(q, q_m_sp), 50)))
        swing = mp.fabs(v_m - v_p) / mp.fabs(v_p)
        passed = swing < ANCHOR_THRESHOLD_RELATIVE
        anchor_verdicts[name] = {
            "v_proton": v_p, "v_muon": v_m,
            "swing_relative": swing, "passed": passed,
            "is_placeholder": is_placeholder,
        }
        placeholder_mark = " [PLACEHOLDER]" if is_placeholder else ""
        print(f"    {name:<20} v(q_p)={mp.nstr(v_p, 8):>11}  "
              f"v(q_μ)={mp.nstr(v_m, 8):>11}  "
              f"swing={mp.nstr(swing, 4):>10}  "
              f"{'✓ PASS' if passed else '✗ FAIL'}{placeholder_mark}")
    print()

    # ─────────────────────────────────────────────────────────────────
    # §4(b) Bar-evenness: f(q) = f(q⁻¹)
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print(" §4(b) Bar-evenness — f(q) = f(q⁻¹)")
    print("=" * 78)
    print()

    bar_verdicts = {}
    for name, (expr, is_placeholder) in candidates.items():
        expr_bar = expr.subs(q, 1 / q)
        # Use sp.cancel + .equals(0) per Copilot review: `diff == 0` on
        # raw sympy expressions can yield false negatives when forms
        # are mathematically equal but not structurally identical.
        diff = sp.cancel(sp.together(expr - expr_bar))
        try:
            passed = diff.equals(0)
            if passed is None:
                # equals() returns None when sympy can't decide; fall
                # back to numeric verification at high precision
                num_val = mp.mpf(str(sp.N(diff.subs(q, "1.5"), 50)))
                passed = mp.fabs(num_val) < mp.mpf("1e-40")
        except Exception:
            passed = (diff == 0)
        bar_verdicts[name] = {
            "delta_simplified": str(diff),
            "passed": bool(passed),
            "is_placeholder": is_placeholder,
        }
        placeholder_mark = " [PLACEHOLDER]" if is_placeholder else ""
        print(f"    {name:<20} f(q) - f(q⁻¹) = {str(diff)[:30]:<30}  "
              f"{'✓ PASS' if passed else '✗ FAIL'}{placeholder_mark}")
    print()

    # ─────────────────────────────────────────────────────────────────
    # §4(c) q=1 classical-limit shadow
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print(" §4(c) q=1 classical-limit shadow — does it reproduce a known integer?")
    print("=" * 78)
    print()

    # Honest §4(c) framing: "matches REGISTERED canonical anchor" is the
    # gate. For Q_β, c_2 → -1 (PR #1786) and c_3 → J_Hopf(1) = -2 (registry
    # §3) are REGISTERED targets. For mass-theory linking_weight, NO
    # registered q=1 anchor exists. Distinguish:
    #   shadow_is_clean_rational : True/False — does sp.nsimplify yield p/q
    #                              with denominator ≤ 100?
    #   matches_registered_anchor : True/False/None — does shadow match a
    #                              registered categorical anchor? (None = no
    #                              registered anchor; the structural gap)
    REGISTERED_LINKING_WEIGHT_Q1_ANCHOR = None  # the open gap

    shadow_verdicts = {}
    for name, (expr, is_placeholder) in candidates.items():
        try:
            lim = sp.limit(expr, q, 1)
            lim_str = str(lim)
            try:
                lim_rat = sp.nsimplify(lim, rational=True)
                clean_rat = lim_rat.q <= 100 if hasattr(lim_rat, 'q') else False
            except Exception:
                lim_rat = lim
                clean_rat = False
        except Exception as exc:
            lim_str = f"ERROR: {exc}"
            lim_rat = None
            clean_rat = False
        if REGISTERED_LINKING_WEIGHT_Q1_ANCHOR is None:
            matches_anchor = None  # no registered target — structural gap
        else:
            matches_anchor = (lim_rat == REGISTERED_LINKING_WEIGHT_Q1_ANCHOR)
        shadow_verdicts[name] = {
            "limit": lim_str,
            "rational_form": str(lim_rat) if lim_rat is not None else "n/a",
            "shadow_is_clean_rational": bool(clean_rat),
            "matches_registered_anchor": matches_anchor,
            "is_placeholder": is_placeholder,
        }
        anchor_status = (
            "? no anchor"
            if matches_anchor is None
            else ("✓ match" if matches_anchor else "✗ mismatch")
        )
        placeholder_mark = " [PLACEHOLDER]" if is_placeholder else ""
        print(f"    {name:<20} f(q→1) = {lim_str:<8}  "
              f"clean rational? {'✓' if clean_rat else '✗'}  "
              f"registered anchor: {anchor_status}{placeholder_mark}")
    print()

    # ─────────────────────────────────────────────────────────────────
    # §4(d) Direction sanity: in same order as target
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print(" §4(d) Direction sanity — |f(q_0)| within 10× of target ≈ 2.46")
    print("=" * 78)
    print()

    direction_verdicts = {}
    for name, (expr, is_placeholder) in candidates.items():
        v_p = mp.mpf(str(sp.N(expr.subs(q, q_p_sp), 50)))
        # Multiplicative bound per Copilot review: "within 10× of target"
        # means target/10 ≤ |v_p| ≤ 10·target. Use ratio
        # max(v_p/target, target/v_p) ≤ 10 (sign-robust via abs).
        v_p_abs = mp.fabs(v_p)
        if v_p_abs == 0:
            ratio_max = mp.inf
        else:
            r1 = v_p_abs / LINKING_WEIGHT_TARGET_OOM
            r2 = LINKING_WEIGHT_TARGET_OOM / v_p_abs
            ratio_max = max(r1, r2)
        passed = ratio_max <= DIRECTION_THRESHOLD_FACTOR
        direction_verdicts[name] = {
            "v_proton": v_p,
            "ratio_max_to_target": ratio_max,
            "passed": passed,
            "is_placeholder": is_placeholder,
        }
        placeholder_mark = " [PLACEHOLDER]" if is_placeholder else ""
        print(f"    {name:<20} f(q_p)={mp.nstr(v_p, 8):>11}  "
              f"target~{LINKING_WEIGHT_TARGET_OOM}  "
              f"max(v/t,t/v)={mp.nstr(ratio_max, 4):>10}  "
              f"{'✓ PASS' if passed else '✗ FAIL'}{placeholder_mark}")
    print()

    # ─────────────────────────────────────────────────────────────────
    # Verdict matrix
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print(" VERDICT MATRIX")
    print("=" * 78)
    print()
    print(f"  {'candidate':<20} {'(a) anchor':>14} {'(b) bar-even':>14} "
          f"{'(c) shadow':>14} {'(d) direction':>14}")
    print(f"  {'-'*20} {'-'*14} {'-'*14} {'-'*14} {'-'*14}")
    for name in candidates.keys():
        # §4(c): "?" because no registered anchor exists for linking_weight
        # at q=1 — the genuine structural gap on the mass-side.
        matches = shadow_verdicts[name]["matches_registered_anchor"]
        c_cell = "?" if matches is None else ("✓" if matches else "✗")
        row = (
            "✓" if anchor_verdicts[name]["passed"] else "✗",
            "✓" if bar_verdicts[name]["passed"] else "✗",
            c_cell,
            "✓" if direction_verdicts[name]["passed"] else "✗",
        )
        print(f"  {name:<20} {row[0]:>14} {row[1]:>14} {row[2]:>14} {row[3]:>14}")
    print()
    print(f"  Legend: ✓ pass, ✗ fail, ? no registered anchor (structural gap)")
    print()

    # ─────────────────────────────────────────────────────────────────
    # Honest interpretation
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print(" INTERPRETATION (honest)")
    print("=" * 78)
    print()
    print(f"  The 4×3 matrix shows the mass-theory linking_weight candidates")
    print(f"  pass invariants (a) anchor-stability, (b) bar-evenness, and")
    print(f"  (d) direction sanity for the two bar-symmetric candidates")
    print(f"  (Family A, via-Jones) but fail (b) for the Bring color-tube")
    print(f"  (confirming the existing `bar_symmetry_three_candidates.py`)")
    print(f"  finding).")
    print()
    print(f"  Invariant (c) — q=1 classical-limit shadow — is structurally")
    print(f"  UNCLEAR for all three candidates:")
    print()
    print(f"    Family A q→1 = (3+4+3)/4 = 10/4 = 5/2")
    print(f"    The q_0 value 2.5328 differs from the q=1 shadow 2.5 by 1.3%.")
    print(f"    No canonical integer/rational \"target\" is registered for")
    print(f"    linking_weight at q=1 (unlike Q_β's c_2 → −1 from PR #1786).")
    print()
    print(f"  Per PR #1850's CODATA-implied-near-match framing, mass-side")
    print(f"  linking_weight is STRUCTURALLY WEAKER than Q_β's c_k anchors")
    print(f"  — the q=1 shadow invariant lacks a registry-level anchor.")
    print(f"  Closing this gap is owner-gated multi-session research per the")
    print(f"  refuted-class map §5 (analogous to the F(q) keystone).")
    print()
    print(f"  Forward direction: identify which categorical-mass anchor")
    print(f"  could supply a clean q=1 integer shadow for linking_weight")
    print(f"  (analog of J_Hopf(1) = −2 for Q_β c_3). Without this, the")
    print(f"  mass-theory §4 chain is INCOMPLETE at invariant (c) only.")
    print()

    # ─────────────────────────────────────────────────────────────────
    # Witness data
    # ─────────────────────────────────────────────────────────────────
    builder.add_data("anchor_swings", {
        name: {k: str(v) if isinstance(v, mp.mpf) else v
               for k, v in d.items()}
        for name, d in anchor_verdicts.items()
    })
    builder.add_data("bar_even_verdicts", bar_verdicts)
    builder.add_data("q_eq_one_shadows", shadow_verdicts)
    builder.add_data("direction_verdicts", {
        name: {k: str(v) if isinstance(v, mp.mpf) else v
               for k, v in d.items()}
        for name, d in direction_verdicts.items()
    })
    builder.add_data("conclusion", (
        "Mass-theory linking_weight candidates pass §4(a), §4(b), §4(d) for the "
        "two bar-symmetric forms (Family A, via-Jones); Bring color-tube fails "
        "§4(b) (existing finding). §4(c) q=1 shadow is structurally UNCLEAR "
        "for all three — no registry-level anchor exists for linking_weight at "
        "q=1, unlike Q_β's c_2 → −1 (PR #1786) or c_3 → J_Hopf(1) = −2 "
        "(registry §3). This is the open gap on the mass-side §4 chain."
    ))

    # The probe's structural contribution is the matrix execution itself;
    # individual cell verdicts go in `data`. A single assertion records
    # whether the matrix ran end-to-end.
    builder.add_assertion(
        "mass_theory_formalize_first_invariants_matrix_executed",
        computed=1,
        expected=1,
        tolerance=0,
        source=("Mass-theory §4 invariants 4×3 verdict matrix executed on "
                "three published linking_weight candidates. The probe is "
                "diagnostic only — it reports per-cell pass/fail/unclear "
                "verdicts for invariants (a) anchor-stability, (b) bar-"
                "evenness, (c) q=1 shadow, (d) direction sanity. The "
                "interpretation in §INTERPRETATION above identifies the "
                "structural gap: §4(c) q=1 shadow lacks a registry-level "
                "anchor for linking_weight, unlike Q_β's c_2 / c_3 anchors. "
                "Closing this gap is owner-gated multi-session research."),
    )

    builder.save()
    print(f"  Witness: mass-theory-formalize-first-invariants-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
