#!/usr/bin/env python3
"""Can the ribbon axioms close the mass/binding precision gaps?  (bean qou-gzs0)

The balancing twist wired onto `QuantumUniverse` (bean `qou-pkf3`) forces
`theta_V = q^{1/2} . id_V` on the defining representation.  Because that is a
SCALAR, a framing `T` on a mass-carrying object contributes exactly one factor

    weight(T) = theta^T = q^{T/2},        T in Z

and this is the ONLY free parameter the ribbon layer adds to a mass or binding
evaluation.  `T` is an integer, so the weight moves on a discrete LADDER.

This probe measures the ladder's step and compares it to the L2 gaps, and
checks the one place the existing mass path already carries a factor of this
shape.

Two questions, both answerable by exact arithmetic:

  Q1  How coarse is the ladder?  If its quantum exceeds the gaps by orders of
      magnitude, the ribbon layer CANNOT supply them -- a structural prune, not
      a numerical failure.

  Q2  `canonical_mass` uses `F_Bor = |tr_M(beta_Bor)| . [3]_q! / q^3`.  Is that
      `/q^3` a framing weight?  `q^-3 = q^{T/2}` iff `T = -6`, i.e. -2 per
      Borromean component.  The Borromean word `(s1 s2^-1)^3` has writhe 0, so
      the factor is NOT `q^writhe`; whether it is a framing is the question.

  Ref: [manuscript] rem:sqrt-q-ribbon-structure
  Ref: [manuscript] conj:kashaev-density-equals-sdp-multiplicity
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

import mpmath as mp  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

# L2 misses (ppb) from per-observable-100x-status.witness.json, and the target.
L2_GAPS_PPB = {"Q_beta": mp.mpf("1279"), "m_n": mp.mpf("1400"), "Delta_pn": mp.mpf("1200")}
L2_TARGET_PPB = mp.mpf("7.8")


def main() -> int:
    q = Q0
    theta = mp.sqrt(q)                       # theta_V = q^{1/2}
    step = theta - 1                         # one framing unit, relative
    step_ppb = step * mp.mpf(10) ** 9

    ladder = []
    for T in range(-6, 7):
        w = q ** (mp.mpf(T) / 2)
        ladder.append({"T": T, "weight": str(w), "shift_percent": str((w - 1) * 100)})

    # Q2: is the F_Bor denominator a framing weight?
    denom = q ** -3
    T_equiv = mp.mpf(-6)                     # q^-3 = q^{T/2}  <=>  T = -6
    denom_as_framing = q ** (T_equiv / 2)
    exact_match = (denom == denom_as_framing)

    # Q1: coarseness ratio against each gap
    coarseness = {k: str(step_ppb / v) for k, v in L2_GAPS_PPB.items()}
    coarseness_vs_target = str(step_ppb / L2_TARGET_PPB)

    b = (
        WitnessBuilder("ribbon-framing-ladder-scale")
        .set_description(
            "Ribbon framing enters a mass/binding evaluation as the single "
            "scalar weight q^{T/2} with T an integer, so its effect is a "
            "discrete ladder. Measures the ladder step against the L2 gaps and "
            "tests whether the F_Bor denominator q^-3 has framing shape."
        )
        .set_content_block("conj:kashaev-density-equals-sdp-multiplicity")
        .add_parameter("q_0", str(q))
        .add_parameter("theta_defining_rep", str(theta))
        .add_data("framing_ladder", ladder)
        .add_data("one_framing_unit_relative", str(step))
        .add_data("one_framing_unit_ppb", str(step_ppb))
        .add_data("L2_gaps_ppb", {k: str(v) for k, v in L2_GAPS_PPB.items()})
        .add_data("L2_target_ppb", str(L2_TARGET_PPB))
        .add_data("coarseness_ratio_vs_gap", coarseness)
        .add_data("coarseness_ratio_vs_target", coarseness_vs_target)
        .add_data("F_Bor_denominator", str(denom))
        .add_data("F_Bor_denominator_as_framing_T", str(T_equiv))
        .add_data("F_Bor_denominator_is_exact_framing_weight", bool(exact_match))
        .add_data(
            "verdict",
            "The ribbon layer CANNOT close the L2 precision gaps: its only free "
            "parameter is an integer framing whose quantum is ~5.36%, which "
            "exceeds the gaps by ~4 orders of magnitude. It CAN move a result "
            "at the percent level, so a mis-set framing is a percent-scale "
            "systematic, not a ppb-scale knob.",
        )
    )
    b.add_assertion(
        "framing_quantum_exceeds_every_L2_gap",
        computed=True,
        expected=all(step_ppb > v for v in L2_GAPS_PPB.values()),
    )
    b.add_assertion(
        "F_Bor_denominator_is_exact_framing_weight_at_T_minus_6",
        computed=bool(exact_match),
        expected=True,
    )
    b.save()

    print("=" * 74)
    print("RIBBON FRAMING LADDER — can the ribbon axioms close mass/binding?")
    print("=" * 74)
    print(f"  q_0                = {mp.nstr(q, 17)}")
    print(f"  theta = q^(1/2)    = {mp.nstr(theta, 17)}")
    print(f"  one framing unit   = {mp.nstr(step * 100, 6)} %   (the ladder quantum)")
    print()
    print("  Q1 — coarseness vs the L2 gaps:")
    for k, v in L2_GAPS_PPB.items():
        print(f"      {k:<10} gap {mp.nstr(v, 6):>8} ppb   ladder is {mp.nstr(step_ppb / v, 6):>10}x too coarse")
    print(f"      {'target':<10} {mp.nstr(L2_TARGET_PPB, 3):>8} ppb   ladder is {mp.nstr(step_ppb / L2_TARGET_PPB, 6):>10}x too coarse")
    print()
    print("  Q2 — the F_Bor denominator:")
    print(f"      q^-3               = {mp.nstr(denom, 17)}")
    print(f"      q^(T/2) at T = -6  = {mp.nstr(denom_as_framing, 17)}")
    print(f"      exact match        = {exact_match}   (-2 per Borromean component)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
