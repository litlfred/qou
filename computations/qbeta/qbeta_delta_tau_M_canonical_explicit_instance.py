"""qbeta_delta_tau_M_canonical_explicit_instance.py
====================================================

Evaluate the *canonical* Δτ_M (with the **explicit √q-bearing instance** of
`CanonicalMarkovWeightsH3` from `QBetaCanonicalMarkovWeightsInstance.lean`,
PR #1764) at substrate q₀, and report the cross-anchor swing.

## Why this script exists

`prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor` is a
§3b-cond conditional theorem: it consumes a `CanonicalMarkovWeightsH3`
instance as `[Instance]` hypothesis. The class has exactly one in-repo
instance — the explicit `√q`-bearing inhabitant

    y_(3)(q)    = z(q) = √q / (1 + q)
    y_(2,1)(q)  = 1/2 - z(q)
    y_(1,1,1)(q) = z(q)

which makes the downstream theorems NON-VACUOUS but is NOT a claim that
this is the canonical Wenzl–Markov instance.

Until now no Python compute realised this instance numerically. This
script closes that gap: it evaluates

    Δτ_M_explicit(q) = z·χ_(3) + (1/2 - z)·χ_(2,1) + z·χ_(1,1,1)

at q_proton (proton-pinned q₀) and q_muon (cross-check anchor), and
compares the result against the previously-recorded *rational surrogate*
Δτ_M from `qbeta_c3_multiblock_recursion_attack.py`.

## What this is NOT

The explicit instance is one valid inhabitant of the class, not THE
canonical Wenzl–Markov instance — see PR #1764 / the .md banner. The
"NEAR-MATCH" terminology that has historically attached to the
*surrogate* swing now also applies, in a parallel fashion, to the
*explicit-instance* swing. The two swings are reported side-by-side so
the relative magnitudes are visible and a reviewer can confirm that
making the y_λ instance √q-bearing does not collapse the swing to zero
(it doesn't — see witness for actual numbers).

No fits, no tuning. Pre-archimedean closed forms only.

## Precision policy

Adopts the canonical `qou_substrate.precision` policy verbatim:
`set_compute_dps()` raises `mp.dps` to COMPUTE_DPS (70), and every
serialized value goes through `fmt()` at OUTPUT_DPS (60), with a
10-digit guard. **Both anchors are derived at the full compute
precision** via `q_at(mp.dps)` (proton) and `q_muon_at(mp.dps)` (muon)
— NOT read from the truncated 50-digit string — so no anchor is the
precision-limiting factor. The witness's `precisionMetadata`
(auto-recorded from the same package constants) therefore matches the
precision actually used, and the `data` block additionally records the
effective anchor / compute / output dps for traceability.

## Outputs

A single witness JSON
``qbeta-delta-tau-m-canonical-explicit-instance.witness.json`` with the
per-anchor Δτ_M values (canonical-explicit + surrogate), the two
cross-anchor swings, and the relative divergence canonical↔surrogate at
each anchor.

Invariants (assertions):

    Δτ_M_canonical_explicit(1) = 0
        (each per-block χ_λ has a (q²−1) factor — verified at q=1.)
    swing_canonical_explicit > 0
        (the cross-anchor swing survives the √q-bearing weights — i.e.
        making the instance non-rational does not collapse the
        NEAR-MATCH diagnostic to zero.)

References:
    Lean class:    QOU.BraidKnot.CanonicalMarkovWeightsH3 (PR #1764)
    Lean instance: QOU.BraidKnot.CanonicalMarkovWeightsH3.explicitInstance
    Lean eval:     QOU.BraidKnot.delta_tau_M_canonical_explicit_eq
                   (this PR) — the Lean lemma this probe mirrors numerically
    Surrogate:     folio-assistant/computations/qbeta/
                       qbeta_c3_multiblock_recursion_attack.py
    Shared utils:  qbeta_utils.py (χ-blocks, markov_parameter, the two
                   Δτ_M evaluators)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import (  # noqa: E402
    delta_tau_M_canonical_explicit,
    delta_tau_M_surrogate,
)


def main() -> None:
    # Adopt the canonical package precision policy: mp.dps = COMPUTE_DPS,
    # serialization via fmt() at OUTPUT_DPS, guard digits as configured.
    eff_dps = set_compute_dps()
    from qou_substrate.precision import OUTPUT_DPS, PRECISION_GUARD

    print("=" * 72)
    print("Δτ_M_canonical at the explicit √q-bearing instance — q₀ evaluation")
    print("=" * 72)
    print(f"effective compute mp.dps = {eff_dps}  (output dps = {OUTPUT_DPS}, "
          f"guard = {PRECISION_GUARD})")

    # ── q anchors, both derived at full compute precision ──
    anchor_dps = mp.dps
    q_proton = q_at(anchor_dps)          # proton-pinned q₀ (current canonical)
    q_muon = q_muon_at(anchor_dps)       # muon cross-check anchor
    print(f"\nq_proton = {mp.nstr(q_proton, 30)}")
    print(f"q_muon   = {mp.nstr(q_muon, 30)}")

    # ── Sanity: Δτ_M_canonical_explicit(1) must vanish ──
    val_at_one = delta_tau_M_canonical_explicit(mpf(1))
    print(f"\nSanity: Δτ_M_canonical_explicit(1) = {mp.nstr(val_at_one, 5)}"
          f"  (must be 0)")

    # ── Δτ_M_canonical_explicit at both anchors ──
    can_p = delta_tau_M_canonical_explicit(q_proton)
    can_m = delta_tau_M_canonical_explicit(q_muon)
    print("\n── Canonical (explicit √q-bearing instance) ──")
    print(f"  Δτ_M_can(q_proton) = {mp.nstr(can_p, 25)}")
    print(f"  Δτ_M_can(q_muon)   = {mp.nstr(can_m, 25)}")
    swing_can = fabs(can_p - can_m)
    print(f"  swing_can          = {mp.nstr(swing_can, 25)}")

    # ── Δτ_M_surrogate at both anchors (re-eval for parity) ──
    sur_p = delta_tau_M_surrogate(q_proton)
    sur_m = delta_tau_M_surrogate(q_muon)
    print("\n── Surrogate (rational y_λ) ──")
    print(f"  Δτ_M_sur(q_proton) = {mp.nstr(sur_p, 25)}")
    print(f"  Δτ_M_sur(q_muon)   = {mp.nstr(sur_m, 25)}")
    swing_sur = fabs(sur_p - sur_m)
    print(f"  swing_sur          = {mp.nstr(swing_sur, 25)}")

    # ── Divergence between canonical-explicit and surrogate at each anchor ──
    div_at_p = fabs(can_p - sur_p) / fabs(sur_p) if sur_p != 0 else mpf("nan")
    div_at_m = fabs(can_m - sur_m) / fabs(sur_m) if sur_m != 0 else mpf("nan")
    print("\n── Divergence canonical_explicit ↔ surrogate ──")
    print(f"  relative |can − sur| / |sur| @ q_proton = {mp.nstr(div_at_p, 8)}")
    print(f"  relative |can − sur| / |sur| @ q_muon   = {mp.nstr(div_at_m, 8)}")

    # ── Sanity: swings non-zero (NEAR-MATCH diagnostic survives) ──
    assert swing_can > 0, (
        "swing_can must be > 0 — the explicit-instance evaluation "
        "should not collapse the cross-anchor swing"
    )
    assert fabs(val_at_one) < mpf(10) ** -(OUTPUT_DPS - 2), (
        f"Δτ_M_canonical_explicit(1) must be 0 (got {val_at_one})"
    )

    # ── Witness ──
    wn = WitnessBuilder(
        "qbeta-delta-tau-m-canonical-explicit-instance",
        engine="mpmath",
    )
    wn.set_description(
        "Evaluation of Δτ_M_canonical at the explicit √q-bearing instance "
        "of CanonicalMarkovWeightsH3 (Lean PR #1764) at substrate q₀, with "
        "side-by-side comparison against the rational Δτ_M surrogate "
        "(qbeta_c3_multiblock_recursion_attack). Closes the conjectural-"
        "to-numerical loop: makes the §3b-cond conditional theorem "
        "prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor "
        "numerically inspectable. Both anchors derived at full compute "
        "precision (q_at / q_muon_at). No fits, no tuning."
    )
    wn.set_content_block(
        "prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor"
    )
    # Explicit precision traceability (in addition to the auto
    # precisionMetadata block, which records the same package constants):
    wn.add_data("anchor_dps", anchor_dps)
    wn.add_data("compute_dps_effective", eff_dps)
    wn.add_data("output_dps", OUTPUT_DPS)
    wn.add_data("q_proton", fmt(q_proton))
    wn.add_data("q_muon", fmt(q_muon))
    wn.add_data(
        "delta_tau_M_canonical_explicit_q_proton", fmt(can_p)
    )
    wn.add_data(
        "delta_tau_M_canonical_explicit_q_muon", fmt(can_m)
    )
    wn.add_data("swing_canonical_explicit", fmt(swing_can))
    wn.add_data("delta_tau_M_surrogate_q_proton", fmt(sur_p))
    wn.add_data("delta_tau_M_surrogate_q_muon", fmt(sur_m))
    wn.add_data("swing_surrogate", fmt(swing_sur))
    wn.add_data("relative_divergence_at_q_proton", fmt(div_at_p))
    wn.add_data("relative_divergence_at_q_muon", fmt(div_at_m))
    wn.add_data(
        "interpretation",
        "The explicit-instance Δτ_M and the surrogate Δτ_M disagree by "
        "the reported relative divergence at each anchor; both have "
        "non-zero cross-anchor swings (NEAR-MATCH diagnostic). Neither "
        "is the canonical Wenzl–Markov instance: the explicit instance "
        "uses y_3 = y_111 = z and y_21 = 1/2 - z (the simplest √q-"
        "bearing choice that satisfies the dimension-normalisation "
        "axiom), while the surrogate uses the rational dimension-shape "
        "y_λ = q^{ℓ(λ)} / ((1+q)(1+q+q²)). Identifying THE canonical "
        "instance — the open math — would close the f-map keystone "
        "for the Q_β c_k ladder."
    )

    # Assertions (real invariants):
    # 1. Δτ_M_canonical_explicit(1) = 0 (q²-1 factor)
    wn.add_assertion(
        "delta_tau_M_canonical_explicit_vanish_at_one",
        computed=float(val_at_one),
        expected=0.0,
        tolerance=float(mpf(10) ** -(OUTPUT_DPS - 2)),
    )
    # 2. Cross-anchor swing of the explicit instance is non-zero
    wn.add_assertion(
        "swing_canonical_explicit_strictly_positive",
        computed=1.0 if swing_can > 0 else 0.0,
        expected=1.0,
    )

    out = wn.save()
    print(f"\nWitness written: {out.name}")


if __name__ == "__main__":
    main()
