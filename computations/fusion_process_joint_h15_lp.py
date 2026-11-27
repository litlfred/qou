#!/usr/bin/env python3
"""
Joint H_15 operator-selection LP for the fusion process D + T -> 4He + n
(bean qou-dpy1 / qou-t37g — the joint-frame solve the cross-witness probes
could not do).

Both sides of the process embed in H_15 (15 strands = 5 nucleons x 3). For a
split element x (x) y of the parabolic H_a x H_b < H_15, the block characters
branch by Littlewood-Richardson:

    chi^nu_{H15}(x (x) y) = sum_{lam |- a, mu |- b} c^nu_{lam,mu}
                             chi^lam(x) * chi^mu(y)

so the H_15 cost vector t_nu = y_nu * chi^nu needs NO new heavy character
computation: the per-subject block tables (complete: p(6)=11, p(9)=30,
p(12)=77, p(3)=3 — the "partial tables" blocker recorded in audit 4b was
legacy truncation lore, re-measured 2026-08-30) branch through the cached LR
tables, and the H_15 Wedderburn weights y_nu come from pyhecke.

For each side this script solves the SAME bar-fold-reduced operator-selection
LP the per-nucleus producer solves (positive-norm blocks, n_target = cost sum,
diagonal Frobenius Gram), emitting the full LP-dual contract for BOTH solves.
For the first time the two sides' active sets and dual prices are objects of
ONE algebra and directly comparable.

Precision class: per-subject chi/y enter at the same resolution as the
committed per-nucleus witnesses (float64 by construction, bean qou-ftuv);
LR coefficients are exact integers. Backend pinned per the producer's R10
note; if clarabel (pyhecke_native) is unavailable the fallback backend is
recorded in the witness rather than silently substituted.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "substrate"))

import numpy as np  # noqa: E402

from nucleus_real_sdp import load_cost, dim_specht  # noqa: E402
from lr_coefficients import get_lr_table  # noqa: E402
from pyhecke.lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402  (Jones-Markov y_lambda, NOT the Plancherel w_lambda)
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

mp.dps = 60
Q0 = Q_MP

SIDES = {
    "initial": [("deuteron", 6), ("tritium", 9)],
    "final": [("he4", 12), ("neutron", 3)],
}
N15 = 15


def partitions_of(n: int):
    def gen(n, maxp):
        if n == 0:
            yield ()
            return
        for p in range(min(n, maxp), 0, -1):
            for rest in gen(n - p, p):
                yield (p,) + rest
    return list(gen(n, n))


def subject_chi_map(atom):
    parts, y, chi, dims, meta = load_cost(atom)
    assert not meta["partial"], f"{atom} table incomplete: {meta}"
    return {tuple(p): float(c) for p, c in zip(parts, chi)}


def branched_cost(side):
    """H_15 cost vector t_nu = y_nu * chi^nu(W_side) via LR branching."""
    (a1, n1), (a2, n2) = side
    chi1, chi2 = subject_chi_map(a1), subject_chi_map(a2)
    table = get_lr_table(n1, n2)
    nus = partitions_of(N15)
    chi15 = {nu: 0.0 for nu in nus}
    for (lam, mu, nu), c in table.items():
        if c > 0:
            chi15[nu] += c * chi1[lam] * chi2[mu]
    y15_raw = y_lambda_at(N15, q_val=float(Q0))
    y15 = {tuple(k): float(v) for k, v in y15_raw.items()}
    dims15 = {nu: dim_specht(nu) for nu in nus}
    t = {nu: y15[nu] * chi15[nu] for nu in nus}
    frob = {nu: y15[nu] * dims15[nu] for nu in nus}
    return nus, chi15, y15, dims15, t, frob


def solve_side(name, side):
    nus, chi15, y15, dims15, t, frob = branched_cost(side)
    pos = [nu for nu in nus if frob[nu] > 0.0]
    t_pos = np.array([t[nu] for nu in pos])
    G_pos = np.diag(np.array([frob[nu] for nu in pos]))
    n_target = float(t_pos.sum())
    backend_used = "clarabel"
    try:
        lp = solve_operator_selection_lp(t_pos, G_pos, n_target, backend="clarabel")
    except Exception:
        backend_used = "scipy-f64-fallback"
        lp = solve_operator_selection_lp(t_pos, G_pos, n_target, backend="scipy")
    d = lp.to_dict()
    # serialize numerics as strings at f64 resolution (no raw float64 in the
    # witness JSON — the values ARE f64-limited (qou-ftuv), the encoding is not)
    def _s(x):
        from mpmath import mpf as _m, nstr as _n
        return None if x is None else mp.nstr(_m(repr(float(x))), 17)
    for k in ("y0_star", "duality_gap", "primal_obj", "dual_obj", "n_target"):
        if k in d and isinstance(d[k], float):
            d[k] = _s(d[k])
    for k in ("x_star", "y_star"):
        if k in d and isinstance(d[k], list):
            d[k] = [_s(v) for v in d[k]]
    active = [pos[i] for i in d.get("active_set", []) if i < len(pos)]
    return {
        "side": name,
        "subjects": [a for a, _ in side],
        "n_pos_blocks": len(pos),
        "n_blocks_total": len(nus),
        "n_target": mp.nstr(mpf(repr(n_target)), 17),
        "tr15_branched": mp.nstr(mpf(repr(float(sum(t[nu] for nu in nus)))), 17),
        "backend": backend_used,
        "lp": d,
        "active_blocks": [str(nu) for nu in active],
        "y0_star": d.get("y0_star"),
        "duality_gap": d.get("duality_gap"),
    }


def main() -> int:
    res = {name: solve_side(name, side) for name, side in SIDES.items()}
    ri, rf = res["initial"], res["final"]
    act_i = set(ri["active_blocks"])
    act_f = set(rf["active_blocks"])

    print("JOINT H_15 OPERATOR-SELECTION LP — D + T vs 4He + n (one frame)")
    for r in (ri, rf):
        print(f"  {r['side']:8s} pos-blocks {r['n_pos_blocks']}/{r['n_blocks_total']} "
              f"n_target {float(r['n_target']):+.9f}  y0* {float(r['y0_star']):+.9f}  "
              f"gap {float(r['duality_gap']):.3e}  active {len(r['active_blocks'])}  "
              f"[{r['backend']}]")
    inter = act_i & act_f
    print(f"  active overlap: {len(inter)} shared | initial-only {len(act_i - act_f)} "
          f"| final-only {len(act_f - act_i)}")
    print(f"  tr15(branched): initial {float(ri['tr15_branched']):+.9f} "
          f"final {float(rf['tr15_branched']):+.9f}")
    dy = float(rf["y0_star"]) - float(ri["y0_star"])
    print(f"  Delta y0* (final - initial), SAME frame: {dy:+.9f}")

    ok = all(r["lp"].get("duality_gap") is not None and
             abs(float(r["lp"]["duality_gap"])) < 1e-6 for r in (ri, rf))
    # split multiplicativity checks (exact split union, both sides; factors
    # read LIVE from the committed per-subject SDP witnesses, never hardcoded
    # (Copilot review, PR #6129))
    import json as _json
    def _tr(atom):
        w = _json.load(open(os.path.join(HERE, f"nucleus-real-sdp-{atom}.witness.json")))
        return float(w.get("data", w)["tr_M"])
    mult_fin = abs(float(rf["tr15_branched"]) - _tr("he4") * _tr("neutron"))
    mult_init = abs(float(ri["tr15_branched"]) - _tr("deuteron") * _tr("tritium"))

    from qou_substrate.witness import WitnessBuilder
    wb = WitnessBuilder("fusion-process-joint-h15-lp", engine="python", output_dir=HERE)
    wb.set_description(
        "Joint H_15 operator-selection LP for D + T -> 4He + n: both sides' "
        "cost vectors built by LR branching of the complete per-subject block "
        "character tables (chi^nu(x(x)y) = sum c^nu_{lam mu} chi^lam chi^mu), "
        "H_15 Wedderburn weights from pyhecke, bar-fold positive-norm solve "
        "per side with full LP-dual emission. First same-frame comparison of "
        "the process's two sides (bean qou-dpy1). Inputs at the committed "
        "witnesses' float64 resolution (qou-ftuv)."
    )
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("q0Anchor", "proton")
    for r in (ri, rf):
        wb.add_data(f"{r['side']}", {k: v for k, v in r.items() if k != "lp"})
        wb.add_data(f"{r['side']}_lp_dual", r["lp"])
    wb.add_data("active_overlap", sorted(inter))
    wb.add_data("active_final_only", sorted(act_f - act_i))
    wb.add_data("delta_y0_star_same_frame", mp.nstr(mpf(repr(dy)), 17))
    wb.add_caveat(
        "ADJUDICATED 2026-08-30 (bean qou-lzgv): the deuteron witness "
        "disagreement this caveat used to record is resolved — the live trace "
        "gives tr_H6 = 0.57517 (matching the chi table this producer uses), "
        "and nucleus-real-sdp-deuteron.witness.json was regenerated to it. "
        "Both sides of the process are split-multiplicative under the "
        "branching (asserted below)."
    )
    wb.add_assertion("both_sides_strong_duality", "1" if ok else "0", "1",
                     tolerance="0",
                     source="duality_gap < 1e-6 on both joint solves")
    wb.add_assertion("frames_match", str(ri["n_blocks_total"]), str(rf["n_blocks_total"]),
                     tolerance="0", source="both sides branched into p(15)=176 blocks")
    wb.add_assertion("initial_split_multiplicativity",
                     mp.nstr(mpf(repr(mult_init)), 6), "0", tolerance="1e-8",
                     source="tr15(D x T branched) equals tr(2H)*tr(3H) from the regenerated witnesses, f64 accumulation floor")
    wb.add_assertion("final_split_multiplicativity",
                     mp.nstr(mpf(repr(mult_fin)), 6), "0", tolerance="1e-8",
                     source="tr15(4He x n branched) equals tr(4He)*tr(n) from the committed SDP witnesses, at the f64 accumulation resolution of the branching sum (observed 2.5e-9; inputs are f64 by construction, qou-ftuv)")
    wb.add_assertion("active_support_invariant",
                     str(len(act_i & act_f)), str(len(act_i | act_f)),
                     tolerance="0",
                     source="the two sides select the SAME active H_15 channels (overlap = union)")
    wb.save()
    print(f"\nRESULT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
