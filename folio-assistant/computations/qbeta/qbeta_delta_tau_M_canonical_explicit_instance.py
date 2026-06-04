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

No fits, no tuning. Pre-archimedean closed forms only; mpmath at 60 dps.

## Outputs

A single witness JSON
``qbeta-delta-tau-m-canonical-explicit-instance.witness.json`` with:

    Δτ_M_canonical_explicit @ q_proton
    Δτ_M_canonical_explicit @ q_muon
    Δτ_M_surrogate          @ q_proton (re-evaluated for parity)
    Δτ_M_surrogate          @ q_muon
    swing_canonical_explicit = |Δτ_M_can(q_p) − Δτ_M_can(q_μ)|
    swing_surrogate          = |Δτ_M_sur(q_p) − Δτ_M_sur(q_μ)|
    relative_divergence_at_q_proton = |can − sur| / |sur|
    relative_divergence_at_q_muon   = |can − sur| / |sur|

Invariants:

    Δτ_M_canonical_explicit(1) = 0
        (each per-block χ_λ has a (q²−1) factor — verified at q=1 to
        20 mpmath digits.)
    swing_canonical_explicit > 0
        (the cross-anchor swing survives the √q-bearing weights — i.e.
        making the instance non-rational does not collapse the
        NEAR-MATCH diagnostic to zero.)

Source identities:
    χ_(3)(q)      = -(q²-1)(q²+1)² / (4q)
    χ_(2,1)(q)    = (q²-1)(-q⁴-1) / (4q³)
    χ_(1,1,1)(q)  = -(q²-1)(q²+1)² / (4q⁵)
    z(q)          = √q / (1+q)   (markov_parameter)

References:
    Lean class:    QOU.BraidKnot.CanonicalMarkovWeightsH3 (PR #1764)
    Lean instance: QOU.BraidKnot.CanonicalMarkovWeightsH3.explicitInstance
    Surrogate:     folio-assistant/computations/qbeta/
                       qbeta_c3_multiblock_recursion_attack.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt as mpsqrt, fabs  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS_COMPUTE = 60
DPS_REPORT = 50


# ── Pre-archimedean closed forms (rational in q + Real.sqrt(q) for z) ──

def chi_block_3(q: mpf) -> mpf:
    return -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q)


def chi_block_21(q: mpf) -> mpf:
    return (q ** 2 - 1) * (-(q ** 4) - 1) / (4 * q ** 3)


def chi_block_111(q: mpf) -> mpf:
    return -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q ** 5)


def markov_parameter(q: mpf) -> mpf:
    """z(q) = √q / (1 + q) — the canonical Markov parameter."""
    return mpsqrt(q) / (1 + q)


# ── Δτ_M evaluators ──

def delta_tau_M_canonical_explicit(q: mpf) -> mpf:
    """Canonical Δτ_M with the EXPLICIT √q-bearing instance:
       y_3 = z, y_21 = 1/2 - z, y_111 = z.
    """
    z = markov_parameter(q)
    return (
        z * chi_block_3(q)
        + (mpf("0.5") - z) * chi_block_21(q)
        + z * chi_block_111(q)
    )


def delta_tau_M_surrogate(q: mpf) -> mpf:
    """Rational surrogate from qbeta_c3_multiblock_recursion_attack —
    the y_λ weights are dimensions/((1+q)(1+q+q²)) (no √q)."""
    num = (
        -(q ** 11)
        + q ** 10
        - 2 * q ** 9
        + q ** 8
        + q ** 6
        - q ** 5
        - q ** 3
        + 2 * q ** 2
        - q
        + 1
    )
    den = 4 * q ** 5 * (q ** 2 + q + 1)
    return num / den


# ── Main probe ──

def main() -> None:
    set_compute_dps(DPS_COMPUTE)

    print("=" * 72)
    print("Δτ_M_canonical at the explicit √q-bearing instance — q₀ evaluation")
    print("=" * 72)
    print(f"mpmath dps = {mp.dps}")

    # ── q anchors ──
    q_proton = mpf(Q_50_DIGIT_STR)
    q_muon = q_muon_at(DPS_REPORT)
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
    print(f"  relative |can − sur| / |sur| @ q_proton = {mp.nstr(div_at_p, 6)}")
    print(f"  relative |can − sur| / |sur| @ q_muon   = {mp.nstr(div_at_m, 6)}")

    # ── Sanity: swings non-zero (NEAR-MATCH diagnostic survives) ──
    assert swing_can > 0, (
        "swing_can must be > 0 — the explicit-instance evaluation "
        "should not collapse the cross-anchor swing"
    )
    assert val_at_one == 0 or fabs(val_at_one) < mpf(10) ** -20, (
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
        "numerically inspectable. No fits, no tuning."
    )
    wn.set_content_block(
        "prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor"
    )
    wn.add_data("dps_compute", DPS_COMPUTE)
    wn.add_data("q_proton", mp.nstr(q_proton, DPS_REPORT))
    wn.add_data("q_muon", mp.nstr(q_muon, DPS_REPORT))
    wn.add_data(
        "delta_tau_M_canonical_explicit_q_proton",
        mp.nstr(can_p, DPS_REPORT),
    )
    wn.add_data(
        "delta_tau_M_canonical_explicit_q_muon",
        mp.nstr(can_m, DPS_REPORT),
    )
    wn.add_data(
        "swing_canonical_explicit", mp.nstr(swing_can, DPS_REPORT)
    )
    wn.add_data(
        "delta_tau_M_surrogate_q_proton", mp.nstr(sur_p, DPS_REPORT)
    )
    wn.add_data(
        "delta_tau_M_surrogate_q_muon", mp.nstr(sur_m, DPS_REPORT)
    )
    wn.add_data("swing_surrogate", mp.nstr(swing_sur, DPS_REPORT))
    wn.add_data(
        "relative_divergence_at_q_proton", mp.nstr(div_at_p, 12)
    )
    wn.add_data(
        "relative_divergence_at_q_muon", mp.nstr(div_at_m, 12)
    )
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
        tolerance=1e-20,
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
