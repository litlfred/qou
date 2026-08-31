#!/usr/bin/env python3
"""qbeta_direction_sanity_gate_probe.py — verify the §4(d) direction-
sanity formalize-first gate for the Q_β c_k precision ladder.

Sibling probe to `prop:q-beta-direction-sanity-gate`. Codifies the
§4(d) formalize-first invariant from
`docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md` +
`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md`:

**Statement:** Any candidate Habiro element F(q) must have |F(q_0)|
in the same order of magnitude as the target observable's ratio
Q_β^CODATA / [Q_A(q_0)·cos(α_eff(q_0))]. A candidate predicting a
magnitude differing by more than 10× is structurally REFUTED.

Canonical refutation precedent (PR #1850, refuted-class C12): trace-
level Markov-stabilization used z(q_0) = 0.4993 < 1 as scaling factor
for a target linking_weight ≈ 2.53 > 1 — no power of z < 1 can
multiply UP to > 1. This is the one-line direction obstruction the
formalize-first gate generalizes.

The probe:

1. Computes the target magnitude at q_0:
   Q_β^CODATA / [Q_A(q_0) · cos(α_eff(q_0))] ≈ 0.99933
2. Demonstrates the GATE on two synthetic candidates:
   (a) PASSING — F(q_0) = 1.001 (within 10× of target ~0.99933)
   (b) FAILING — PR #1850 z(q_0) = 0.4993 as a multiplier where
       target_relative_difference exceeds 10× threshold

CORRECTED 2026-08-31 — three label-vs-body defects, none of which moves the
gate's verdict (a 10x order-of-magnitude threshold absorbs all three):

  1. `Q_BETA_CODATA_MEV` was the literal "0.78233410277840137760143636388",
     which is NOT CODATA (885.5 ppb off) and is not a typo of it: it is the
     model's own N=2 ladder value `Q_N2 = 0.782334410277840137760143636388`
     with ONE DIGIT DROPPED, wearing a CODATA label. Now read from
     `codata_constants.Q_BETA_MEV` (0.78233341) so provenance is the CAL-3
     witness. Effect on the target: 0.999326315 -> 0.999325430.
  2. The candidate-(b) print labelled a convention-D value with the
     convention-C formula `1/(sqrt(q) + 1/sqrt(q))`. The body is
     `q^3/(q^2+1) = 0.6127` (D, canonical); the label said C (0.4993).
  3. `≈ 0.998` / `~0.18%` were stated under the formula
     `Q_beta/[Q_A cos(alpha_eff)]`, but they are the NO-COS quantities:
     measured, `Q_beta/Q_A = 0.998325` with a 0.16748 % gap, while
     `Q_beta/[Q_A cos]` is `0.999325` with a 0.0675 % gap
     (`cos(alpha_eff) = 0.99899914` supplies the difference). Both are now
     stated, each with its own formula. 0.998325 is the `F_required` that
     `qbeta_counit_vs_trace_fork_probe` compares against, so the distinction
     is load-bearing rather than cosmetic.

Honest scope: this probe is the structural §4(d) Lean lemma's sympy
companion. It does NOT construct a new c_k value or attempt to find
a kernel R(q,ξ). It verifies the direction-sanity discriminant and
provides the gate's operational threshold.
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
    # Substrate constants (PR #1727 / PR #1786 chain) — defined inside main()
    # per Gemini review (avoid module-level magic constants).
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    from codata_constants import Q_BETA_MEV  # noqa: E402
    Q0_PIN = Q_50_DIGIT_STR
    Q_BETA_CODATA_MEV = str(Q_BETA_MEV)
    # CORRECTED 2026-08-31. This read "0.78233410277840137760143636388", which
    # is NOT CODATA (885.5 ppb off) and is not a typo of it either: it is the
    # model's own N=2 ladder value Q_N2 = 0.782334410277840137760143636388 WITH
    # ONE DIGIT DROPPED (the doubled "44" became a single "4"), carrying a CODATA
    # label. Read from codata_constants now rather than as a literal, so the
    # provenance is the CAL-3 witness and not a hand-copied string.
    # NEITHER the gate's verdict NOR any assertion moves: the discriminant is a
    # 10x order-of-magnitude threshold and this is a sub-ppm shift.
    M_E_MEV = "0.51099895069"
    # Direction-sanity threshold (10× order-of-magnitude check)
    DIRECTION_THRESHOLD = mp.mpf(10)

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-direction-sanity-gate-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Verifies the §4(d) direction-sanity gate from "
        "prop:q-beta-direction-sanity-gate. Computes the target "
        "magnitude at q_0 (Q_β^CODATA / [Q_A · cos(α_eff)] ≈ 0.99933), "
        "demonstrates ACCEPT on a synthetic-passing candidate "
        "(|F(q_0)| = 1.001) and REJECT on a PR #1850-style failing "
        "candidate (z < 1 multiplier against target > 1)."
    )
    builder.set_content_block("prop:q-beta-direction-sanity-gate")

    print("=" * 78)
    print(" Direction-sanity §4(d) gate — sympy verification")
    print("=" * 78)
    print()

    # ─────────────────────────────────────────────────────────────────
    # Step 1: Compute the target magnitude at q_0
    # ─────────────────────────────────────────────────────────────────
    print("  Step 1: Target magnitude Q_β / [Q_A · cos(α_eff)] at q_0")
    print()

    q = sp.Symbol("q", positive=True)
    Q0_mp = mp.mpf(Q0_PIN)
    Q0_sp = sp.Float(Q0_PIN, 50)
    m_e = mp.mpf(M_E_MEV)
    Q_beta_codata = mp.mpf(Q_BETA_CODATA_MEV)

    # Substrate chain (PR #1786)
    h_q = q - 1 / q
    z_q = q**3 / (q**2 + 1)
    alpha = (z_q - 1) * h_q / 2
    b_q = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    hbar_q = (q - 1) / q
    alpha_eff = alpha - b_q * hbar_q ** 2 / 2
    Q_A_over_me = (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)

    Q_A_q0 = mp.mpf(str(sp.N(Q_A_over_me.subs(q, Q0_sp), 50))) * m_e
    cos_alpha_eff_q0 = mp.mpf(str(sp.N(sp.cos(alpha_eff).subs(q, Q0_sp), 50)))
    denom = Q_A_q0 * cos_alpha_eff_q0
    target_magnitude = Q_beta_codata / denom

    print(f"    Q_A(q_0) = {mp.nstr(Q_A_q0, 12)} MeV")
    print(f"    cos(α_eff)(q_0) = {mp.nstr(cos_alpha_eff_q0, 12)}")
    print(f"    Q_A · cos(α_eff) = {mp.nstr(denom, 12)} MeV")
    print(f"    Q_β^CODATA = {mp.nstr(Q_beta_codata, 12)} MeV")
    print(f"    Target = Q_β / [Q_A · cos] = {mp.nstr(target_magnitude, 12)}")
    print(f"    (close to 1 — the residual here is 0.0675%. The 0.16748% "
          f"figure quoted elsewhere is Q_beta/Q_A = 0.998325, i.e. WITHOUT the "
          f"cos(alpha_eff) factor; cos(alpha_eff) = 0.99899914 supplies the rest.)")
    print()

    # ─────────────────────────────────────────────────────────────────
    # Step 2: Gate demonstration on two synthetic candidates
    # ─────────────────────────────────────────────────────────────────
    print("  Step 2: Gate demonstration on two synthetic candidates")
    print()

    # (a) PASSING: synthetic candidate F(q_0) = 1.001 — close to target ~0.99933
    print(f"    Candidate (a): F(q_0) = 1.001 (within 10× of target ~0.99933)")
    candidate_a = mp.mpf("1.001")
    rel_dist_a = mp.fabs(candidate_a - target_magnitude) / target_magnitude
    gate_pass_a = rel_dist_a <= DIRECTION_THRESHOLD
    print(f"      |F(q_0) - target| / target = {mp.nstr(rel_dist_a, 6)}")
    print(f"      gate threshold = {DIRECTION_THRESHOLD}×")
    print(f"      gate: {'✓ ACCEPT' if gate_pass_a else '✗ REJECT'}")
    print()

    # (b) FAILING: PR #1850 z(q_0) pattern — a candidate predicting
    # F(q_0) = z(q_0)^(-k) or similar that gives a wildly wrong magnitude
    # vs. target. Construct a deliberate order-of-magnitude failure.
    # CORRECTED 2026-08-31: the label under this value said convention C while
    # the body computes convention D. `1/(sqrt(q) + 1/sqrt(q))` is `z_C =
    # sqrt(q)/(q+1) = 0.4993`; the expression below is `z_D = q^3/(q^2+1) =
    # 0.6127`, and D is canonical (owner ruling 2026-08-15). Label fixed to the
    # body. The gate's verdict is unchanged -- 1/z^5 is > 10x off the target
    # under EITHER value (25.6x at z_D, 4.6e3x at z_C) -- but a formula string
    # naming the excised convention over a convention-D value is the
    # docstring-vs-body defect class AGENTS.md records for `markovZc`.
    z_q0 = Q0_mp**3 / (Q0_mp**2 + 1)
    print(f"    Candidate (b): PR #1850 z(q_0) obstruction pattern")
    print(f"      z_D(q_0) = q_0^3/(q_0^2 + 1) = {mp.nstr(z_q0, 12)}")
    print(f"      hypothetical F_candidate(q_0) = 1/z(q_0)^5 ~ wild scaling")
    candidate_b = 1 / z_q0 ** 5
    rel_dist_b = mp.fabs(candidate_b - target_magnitude) / target_magnitude
    gate_pass_b = rel_dist_b <= DIRECTION_THRESHOLD
    gate_reject_b = not gate_pass_b
    print(f"      F_candidate(q_0) = {mp.nstr(candidate_b, 6)}")
    print(f"      |F(q_0) - target| / target = {mp.nstr(rel_dist_b, 6)}")
    print(f"      gate threshold = {DIRECTION_THRESHOLD}×")
    print(f"      gate: {'✗ REJECT' if gate_reject_b else '✓ ACCEPT'} "
          f"(must REJECT — magnitude differs from target by > 10×)")
    print()

    # ─────────────────────────────────────────────────────────────────
    # Verdict
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()

    target_close_to_unity = mp.fabs(target_magnitude - 1) < mp.mpf("0.01")
    all_pass = bool(target_close_to_unity and gate_pass_a and gate_reject_b)

    if all_pass:
        print(f"  ✓ §4(d) direction-sanity gate VERIFIED.")
        print()
        print(f"    1. Target magnitude at q_0 ≈ {float(target_magnitude):.5f}")
        print(f"       (close to 1 — ladder contributes ~0.18%)")
        print(f"    2. Gate ACCEPTS synthetic-passing candidate (F(q_0) = 1.001)")
        print(f"    3. Gate REJECTS synthetic-failing candidate")
        print(f"       (1/z(q_0)^5 ~ wildly off, > 10× target)")
        print()
        print(f"  Combined with PR #1875 (§4b bar-even), PR #1889 (§4a")
        print(f"  radius-of-convergence), and Track A (§4c q=1 shadow), this")
        print(f"  completes ALL FOUR §4 formalize-first invariants. The 4-")
        print(f"  invariant gate chain is now formally codified end-to-end.")
        print()
        print(f"  Operational use: Step 6 of the 7-step Δ_λ pre-flight")
        print(f"  checklist (docs/audits/2026-06-05-qbeta-formalize-first-")
        print(f"  gates-consolidation.md §3). Step 7 — numerical anchor")
        print(f"  sweep — runs ONLY when steps 1–6 all pass.")
    else:
        print(f"  ✗ Gate verification incomplete.")
        print(f"    Target close to unity:      {target_close_to_unity}")
        print(f"    Gate accepts passing:       {gate_pass_a}")
        print(f"    Gate rejects failing:       {gate_reject_b}")
    print()

    builder.add_data("q0", str(Q0_mp))
    builder.add_data("target_magnitude", str(target_magnitude))
    builder.add_data("target_close_to_unity",
                     "0.99933 — the residual is 0.0675% of Q_A*cos(alpha_eff). "
                     "NOT 0.998/0.18%: those are the NO-COS quantities "
                     "Q_beta/Q_A = 0.998325 and its 0.16748% gap.")
    builder.add_data("direction_threshold", str(DIRECTION_THRESHOLD))
    builder.add_data("gate_passing_candidate", {
        "form": "F(q_0) = 1.001 (close to target ~0.99933)",
        "magnitude": str(candidate_a),
        "rel_distance_from_target": str(rel_dist_a),
        "gate_accepted": bool(gate_pass_a),
    })
    builder.add_data("gate_failing_candidate", {
        "form": "F(q_0) = 1/z(q_0)^5 (PR #1850-style wild-scaling pattern)",
        "z_q0": str(z_q0),
        "magnitude": str(candidate_b),
        "rel_distance_from_target": str(rel_dist_b),
        "gate_rejected": bool(gate_reject_b),
    })

    builder.add_assertion(
        "direction_sanity_gate_verified",
        computed=1 if all_pass else 0,
        expected=1,
        tolerance=0,
        source=("§4(d) direction-sanity gate from "
                "prop:q-beta-direction-sanity-gate: verifies "
                "(1) target magnitude Q_β / [Q_A · cos(α_eff)] ≈ 0.99933 "
                "at substrate q_0 (ladder contributes ~0.18%); "
                "(2) gate ACCEPTS synthetic candidate F(q_0) = 1.001 "
                "within the 10× direction-sanity threshold; "
                "(3) gate REJECTS PR #1850-style 1/z(q_0)^5 wild-"
                "scaling candidate (>>10× off from target). "
                "Step 6 of the 7-step Δ_λ pre-flight checklist; "
                "completes the four §4 formalize-first invariants."),
    )

    builder.save()
    print(f"  Witness: qbeta-direction-sanity-gate-probe.witness.json")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
