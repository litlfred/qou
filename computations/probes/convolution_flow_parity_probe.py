#!/usr/bin/env python3
"""convolution_flow_parity_probe.py — the convolution flow σ^t and the parity of feasible bridge letters at A = 2.
Bean `qou-jfx8` (owner 2026-10-12: "flow by the knot convolution operator"), refining `qou-8r6b`. Companion to
`QOU/MassTheory/ConvolutionFlowParity.lean`.

On the deuteron composite W_free (production proton and neutron H_3 blocks in H_6), with bridge letter σ = σ₂:
  1. the channel split χ_λ(W σ^m) = q^m χ_λ(W P_S) + (−q⁻¹)^m χ_λ(W P_A), checked against direct evaluation for
     m = −3 … 19 on every positive-weight (convention D) block;
  2. the feasibility of the power letter σ^m under reading 3 (χ_λ ≥ 0 on every block with y_λ > 0), for m = −8 … 20,
     and the threshold where odd powers turn feasible;
  3. the real-t flow, Re χ_λ(W σ^t) = q^t a_S + q^{−t} cos(πt) a_A (branch-independent real part), on a grid.
Evaluator: composition_feasibility_a2_probe's mpmath Hoefsmit evaluator, validated against committed H_6 deuteron
characters to 1e-40 (re-run here). 60 dps, no floats. Nothing fitted; no letter selected.
-- Ref: [manuscript] bean qou-jfx8, qou-8r6b
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
mp.mp.dps = 60
import composition_feasibility_a2_probe as cf  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Q, H = cf.Q, cf.H
QI = 1 / Q


def power_word(m):
    return [(1, mp.mpf(0), 2)] * m if m >= 0 else [(1, -H, 2)] * (-m)


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    TOL = mp.mpf("1e-40")
    P6 = cf.partitions_of(6)
    y6 = cf.load_y(6)
    W = cf.nucleon_word(cf.B_P, 0, 1) + cf.nucleon_word(cf.B_N, 3, 4)
    atom, free, meta = cf.load_atom("d")
    dev = max(abs(cf.chi(l, W) - free[l]) for l in P6)
    check("evaluator_reproduces_committed_H6_deuteron_free_characters", dev < TOL, "atom-chi-rust-d free")
    pos = [l for l in P6 if y6[l] > 0]
    PS = [(1 / (Q + QI), QI / (Q + QI), 2)]
    PA = [(-1 / (Q + QI), Q / (Q + QI), 2)]
    aS = {l: cf.chi(l, W + PS) for l in pos}
    aA = {l: cf.chi(l, W + PA) for l in pos}

    worst = mp.mpf(0)
    for l in pos:
        for m in range(-3, 20):
            worst = max(worst, abs(cf.chi(l, W + power_word(m)) - (Q ** m * aS[l] + (-QI) ** m * aA[l])))
    print("channel split worst deviation:", mp.nstr(worst, 5))
    check("channel_split_matches_direct_for_m_in_-3..19", worst < TOL, "Lean pow_interp_at_q / pow_interp_at_neg_inv")

    feas = {}
    for m in range(-8, 21):
        vals = {l: Q ** m * aS[l] + (-QI) ** m * aA[l] for l in pos}
        feas[m] = all(v >= 0 for v in vals.values())
    print("feasible power letters σ^m:", [m for m, f in feas.items() if f])
    thr = {}
    for l in pos:
        if aS[l] > 0 and aA[l] > 0:
            thr[str(l)] = mp.log(aA[l] / aS[l]) / (2 * mp.log(Q))      # odd m feasible iff m ≥ thr
    print("odd-power thresholds (m ≥ thr feasible):", {k: mp.nstr(v, 8) for k, v in thr.items()})
    check("odd_m_le_15_infeasible_and_odd_m_ge_17_feasible",
          all(not feas[m] for m in range(1, 16, 2)) and all(feas[m] for m in range(17, 21, 2)),
          "Lean odd_power_negative_iff on (5,1): a_A/a_S ≈ 32.1")
    check("all_even_m_ge_0_feasible", all(feas[m] for m in range(0, 21, 2)), "Lean even_power_nonneg")
    check("direct_m17_composite_feasible", all(cf.chi(l, W + power_word(17)) >= 0 for l in pos), "direct evaluation")

    grid = [mp.mpf(k) / 4 for k in range(-24, 81)]
    flow = [{"t": mp.nstr(t, 6), "feasible": all(Q ** t * aS[l] + Q ** (-t) * mp.cos(mp.pi * t) * aA[l] >= 0 for l in pos)}
            for t in grid]

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("convolution-flow-parity", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 read from the committed y-lambda-at-q0 witness string via composition_feasibility_a2_probe",
        "description": ("PROBE (bean qou-jfx8): convolution flow σ^t at A = 2. χ(Wσ^m) = q^m χ(W P_S) + (−q⁻¹)^m χ(W P_A); "
                        "odd powers infeasible up to m = 15 and feasible from m = 17 (block (5,1), a_A/a_S ≈ 32.1); even "
                        "powers feasible; real-t flow feasibility on a grid. Refines qou-8r6b's |m| ≤ 3 parity finding."),
        "weight_family": "markov_y_lambda_convention_D",
        "channel_weights": {str(l): {"aS": mp.nstr(aS[l], 30), "aA": mp.nstr(aA[l], 30)} for l in pos},
        "split_worst_dev": mp.nstr(worst, 5),
        "feasible_power_letters": [m for m, f in feas.items() if f],
        "odd_power_thresholds": {k: mp.nstr(v, 20) for k, v in thr.items()},
        "real_flow_grid": flow,
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
