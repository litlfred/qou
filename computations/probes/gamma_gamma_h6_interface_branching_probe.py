#!/usr/bin/env python3
"""
qou-ales step 6 — the H_6 interface bond is selected through branching: numerical
cross-check of `QOU/Mass/GammaGammaH6Interface.lean` against the step-3 witness.

The Lean file states the branching rule as a hypothesis (`InterfaceBranching`):
on the interface bond G^m = (sigma_2 sigma_3^-1)^m, each H_6 block character is

    chi_lam(G^m) = a_lam + b_lam . chi_(2,1)(V^m) + c_lam,

with (a, b, c) the multiplicities of (3), (2,1), (1^3) in V_lam restricted to the
parabolic H_3 = <sigma_2, sigma_3>, computed in Lean as Young-lattice path counts
(branchOf_six .. branchOf_threeThree: (1,0,0), (3,1,0), (3,3,0), (1,2,0)).

This probe does NOT re-derive the selection. It checks, at the proton pin:

  * the path counts, recomputed here by an independent Young-lattice recursion,
    equal the Lean table for all 11 partitions of 6, and f^lam = a + 2b + c;
  * the branched formula reproduces the step-3 witness `h6_bond_candidates[*]
    .chi_by_block` on the four two-row blocks for m = 0..5 (24 values) — the
    step-3 probe computed those from the full Hoefsmit H_6 matrices on the
    MIDDLE strands, so this is the numerical content of the branching
    hypothesis, middle-strand embedding included;
  * the convention-D Markov weight y_lam (two-row truncation, SU(2)) is
    positive exactly on (6), (5,1), (4,2), (3,3) and zero elsewhere — the
    `twoRow` support hypothesis of the Lean theorems;
  * the pin lies in the Lean interval (1 < q <= 23/20, h^2 <= 1/12) and the
    (3,3) sign condition 1 + 2 chi_m has the pattern (-,-,+,-,-) for m = 1..5.

Informational (no assertion): the root x* of 1 + 2 chi_5(x) = 0 on (0, 1/10],
which is why the H_6 interval is 1/12 and not step 4's 1/10.

## Precision
mpmath at 60 dps end to end; q_0 is the proton pin `Q_50_DIGIT_STR`; the (2,1)
characters are the Lean closed forms in x = h^2. Nothing here reads AME2020,
CODATA masses beyond the pin, or a census.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations/substrate",
           "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")
STEP3_WITNESS = _ROOT / "computations/probes/gamma-gamma-h3-psd-selector-probe.witness.json"

PARTS6 = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1), (3, 1, 1, 1), (2, 2, 2),
          (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]
TWO_ROW = [(6,), (5, 1), (4, 2), (3, 3)]
LEAN_BRANCH = {(6,): (1, 0, 0), (5, 1): (3, 1, 0), (4, 2): (3, 3, 0), (3, 3): (1, 2, 0)}


# ------------------------------------------------------- Young's lattice ----
def covers(mu: tuple) -> list[tuple]:
    """Partitions obtained from mu by adding one box (independent of the Lean coding:
    add to row i whenever the result stays weakly decreasing)."""
    out = []
    for i in range(len(mu) + 1):
        nu = list(mu) + [0]
        nu[i] += 1
        if all(nu[j] >= nu[j + 1] for j in range(len(nu) - 1)):
            out.append(tuple(x for x in nu if x > 0))
    return out


def path_count(mu: tuple, lam: tuple) -> int:
    if sum(mu) > sum(lam):
        return 0
    if mu == lam:
        return 1
    return sum(path_count(nu, lam) for nu in covers(mu))


def chi21(m: int, x):
    """The Lean closed forms trace_vtx_pow_one..five in x = h^2 (m = 0: dim 2)."""
    return {0: mp.mpf(2), 1: -1 - x, 2: x ** 2 + 2 * x - 1, 3: 2 - 3 * x ** 2 - x ** 3,
            4: x ** 4 + 4 * x ** 3 + 2 * x ** 2 - 4 * x - 1,
            5: -x ** 5 - 5 * x ** 4 - 5 * x ** 3 + 5 * x ** 2 + 5 * x - 1}[m]


def main() -> int:
    t0 = time.time()
    q = Q_MP
    h = q - 1 / q
    x = h ** 2
    print(f"qou-ales step 6 probe — H_6 interface branching (proton pin, {DPS} dps)")
    print(f"  q_0 = {mp.nstr(q, 20)}   h^2 = {mp.nstr(x, 20)}")

    # 1. path counts vs the Lean table; f^lam = a + 2b + c; Burnside
    branch = {lam: (path_count((3,), lam), path_count((2, 1), lam), path_count((1, 1, 1), lam))
              for lam in PARTS6}
    fdim = {lam: path_count((), lam) for lam in PARTS6}
    dim_ok = all(fdim[lam] == a + 2 * b + c for lam, (a, b, c) in branch.items())
    burnside = sum(f * f for f in fdim.values())
    lean_ok = all(branch[lam] == LEAN_BRANCH[lam] for lam in TWO_ROW)
    print(f"\n  {'lam':>18}{'f':>4}   (a,b,c) = mult of (3),(2,1),(1^3)")
    for lam in PARTS6:
        print(f"  {str(lam):>18}{fdim[lam]:>4}   {branch[lam]}")
    print(f"  f = a + 2b + c on all 11: {dim_ok};  sum f^2 = {burnside};  two-row table = Lean: {lean_ok}")

    # 2. branched formula vs the step-3 witness chi_by_block (middle-strand H_6 matrices)
    step3 = json.loads(STEP3_WITNESS.read_text())["data"]
    rows = {r["bond"]: r for r in step3["h6_bond_candidates"] if r["bond"].startswith("G^")}
    dev_max = mp.mpf(0)
    n_checked = 0
    print(f"\n  {'bond':>6}{'block':>10}{'witness chi':>28}{'a + b chi_m + c':>28}{'dev':>10}")
    for m in range(0, 6):
        r = rows[f"G^{m}"]
        for lam in TWO_ROW:
            a, b, c = branch[lam]
            got = mp.mpf(r["chi_by_block"][str(lam)])
            pred = a + b * chi21(m, x) + c
            dev = abs(got - pred)
            dev_max = max(dev_max, dev)
            n_checked += 1
            print(f"  {'G^' + str(m):>6}{str(lam):>10}{mp.nstr(got, 18):>28}{mp.nstr(pred, 18):>28}{mp.nstr(dev, 3):>10}")
    print(f"  {n_checked} values, max |dev| = {mp.nstr(dev_max, 3)}")

    # 3. convention-D weight support at n = 6
    y6 = {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(6, q, 2).items()}
    pos = [lam for lam in PARTS6 if y6.get(lam, mp.mpf(0)) > TOL]
    zero_off = max(abs(y6.get(lam, mp.mpf(0))) for lam in PARTS6 if lam not in TWO_ROW)
    support_ok = (pos == TWO_ROW) and zero_off < TOL
    print(f"\n  y_lambda (D, SU(2)) > 0 on {pos}; max |y| off two-row = {mp.nstr(zero_off, 3)}")
    for lam in TWO_ROW:
        print(f"    y{lam} = {mp.nstr(y6[lam], 20)}")

    # 4. interval and the (3,3) sign condition
    in_q = bool(1 < q <= mp.mpf(23) / 20)
    in_x = bool(0 < x <= mp.mpf(1) / 12)
    cond = {m: 1 + 2 * chi21(m, x) for m in range(1, 6)}
    signs = "".join("+" if cond[m] > 0 else "-" for m in range(1, 6))
    print(f"\n  1 < q_0 <= 23/20: {in_q};  0 < h^2 <= 1/12: {in_x}")
    for m in range(1, 6):
        print(f"    1 + 2 chi_{m} = {mp.nstr(cond[m], 18)}")
    print(f"  sign pattern: {signs}   (Lean h6_signs_of_small + chi_signs_of_small)")

    # informational: where 1 + 2 chi_5 changes sign
    root = mp.findroot(lambda t: 1 + 2 * chi21(5, t), mp.mpf("0.09"))
    print(f"  informational: 1 + 2 chi_5(x) = 0 at x* = {mp.nstr(root, 12)}  (> 1/12 = 0.0833, < 1/10)")

    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gamma-gamma-h6-interface-branching-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales step 6: the H_6 interface bond G^m = (sigma_2 sigma_3^-1)^m is decided by the H_3 "
        "(2,1) character through the branching rule. Cross-checks QOU/Mass/GammaGammaH6Interface.lean: "
        "Young-lattice path counts (independent recursion) equal the Lean table; the branched formula "
        "a + b chi_m + c reproduces the step-3 witness chi_by_block on the four two-row blocks for "
        "m = 0..5; the convention-D weight is supported exactly on the two-row blocks; the pin lies "
        "in the Lean interval and the (3,3) condition 1 + 2 chi_m has signs (-,-,+,-,-). No AME/CODATA "
        "binding value or census is read.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (two-row truncation; SU(2) Markov weight y_lambda_su_n(6, q, 2))")
    w.add_parameter("dps", DPS)
    w.add_parameter("tolerance", fmt(TOL))
    w.add_parameter("step3_witness", str(STEP3_WITNESS.relative_to(_ROOT)))
    w.add_data("h_sq", fmt(x))
    w.add_data("branching_table", {str(lam): list(branch[lam]) for lam in PARTS6})
    w.add_data("f_lambda", {str(lam): fdim[lam] for lam in PARTS6})
    w.add_data("burnside_sum_f_sq", burnside)
    w.add_data("y_lambda_two_row", {str(lam): fmt(y6[lam]) for lam in TWO_ROW})
    w.add_data("y_lambda_positive_support", [str(lam) for lam in pos])
    w.add_data("three_three_condition_1_plus_2chi", {str(m): fmt(cond[m]) for m in range(1, 6)})
    w.add_data("three_three_condition_signs", signs)
    w.add_data("root_of_1_plus_2chi5_informational", fmt(root))
    w.add_assertion(name="path_counts_match_lean_table", computed=str(int(lean_ok)), expected="1",
                    tolerance="0", source="Lean branchOf_six..branchOf_threeThree (decide)")
    w.add_assertion(name="dim_eq_branch_all_eleven", computed=str(int(dim_ok)), expected="1",
                    tolerance="0", source="Lean dim_eq_branch")
    w.add_assertion(name="burnside_720", computed=str(burnside), expected="720", tolerance="0",
                    source="Lean fDim_sq_sum")
    w.add_assertion(name="branched_formula_matches_step3_h6_characters", computed=fmt(dev_max),
                    expected="0", tolerance="1e-40",
                    source="step-3 witness h6_bond_candidates[*].chi_by_block vs Lean InterfaceBranching")
    w.add_assertion(name="convention_D_weight_supported_on_two_row", computed=str(int(support_ok)),
                    expected="1", tolerance="0", source="Lean H6Block.twoRow hypothesis")
    w.add_assertion(name="pin_inside_lean_interval", computed=str(int(in_q and in_x)), expected="1",
                    tolerance="0", source="Lean h_sq_le_twelfth_of_q_le: 1 < q <= 23/20 => h^2 <= 1/12")
    w.add_assertion(name="three_three_sign_pattern", computed=signs, expected="--+--", tolerance="0",
                    source="Lean h6_signs_of_small; interface_frobenius_table")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
