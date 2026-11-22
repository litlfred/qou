"""Collision-as-gradient probe: Lagrangian relaxation of the gamma-gamma word
selection in H_3, and canonical rounding of the relaxed optimum.

Issue #7895, PR #7896.  Candidates are the vertex powers V^k = (sigma_0
sigma_1^-1)^k, k = 1..kmax (inside H_3 these are all the gamma-gamma words,
Lean gammaGamma_inH3_eq_vertexPow), cost 2k crossings, constraint reading 3
(owner ruling 2026-09-12): chi_lambda(V^k) >= 0 on every block with y_lambda > 0
under convention D, at the proton pin.

What it computes, all in mpmath (no float64 anywhere):
  * the ILP choice (cheapest feasible word);
  * the LP relaxation over mixtures, solved EXACTLY: chi_(3)(V^k) = 1 for all k
    (Lean trivChar_eq_one), so only the (2,1) row can bind, and the optimum is
    the best edge [a, b] (a infeasible, b feasible) of the lower hull, value
    crossVal = (c_a x_b - c_b x_a)/(x_b - x_a);
  * the Lagrangian dual g(mu) = min_k 2k - mu . chi(V^k), whose optimum equals
    the LP value (Geoffrion), with multipliers (shadow prices) and the
    supergradients -chi(V^k) of the words attaining the minimum -- the
    "incidence vectors";
  * the margin condition of Lean QOU.Optimization.RelaxedVertexRounding
    (slope_le_of_margin) with X = 2 (|chi_(2,1)(V^k)| = |2 cos k theta| <= 2,
    det V = 1, Lean GammaGammaVertexOrder), which makes the unique feasible
    vertex of the relaxed optimal face equal the ILP choice;
  * subgradient ascent on mu (multipliers as forces), the sequence of chosen
    words.

No AME/CODATA value is read.  Nothing is fitted.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations",
           "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from pyhecke.wedderburn import partitions_of  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from gamma_gamma_h3_psd_selector_probe import vertex_pow, word_image, trace  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")


def main() -> int:
    t0 = time.time()
    kmax = 10
    for a in sys.argv[1:]:
        if a.startswith("--kmax="):
            kmax = int(a.split("=", 1)[1])
    mp.mp.dps = DPS
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    cache = BlockCacheMP(q, h)
    parts = [tuple(p) for p in partitions_of(3)]
    reps = {lam: seminormal_matrices_mp(lam, cache=cache) for lam in parts}
    y = {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(3, q, 2).items()}
    live = [lam for lam in parts if y[lam] > TOL]

    ks = list(range(1, kmax + 1))
    cost = {k: mp.mpf(2 * k) for k in ks}
    chi = {}
    for k in ks:
        w = vertex_pow(0, k, h)
        chi[k] = {}
        for lam in parts:
            sig, dim, _ = reps[lam]
            chi[k][lam] = trace(word_image(sig, dim, w), dim)
    triv_dev = max(abs(chi[k][(3,)] - 1) for k in ks)
    bound_dev = max(abs(chi[k][(2, 1)]) for k in ks)
    x = {k: chi[k][(2, 1)] for k in ks}
    feas = [k for k in ks if all(chi[k][lam] >= -TOL for lam in live)]
    infeas = [k for k in ks if k not in feas]

    print(f"collision-gradient Lagrangian probe -- proton pin, convention D, {DPS} dps, kmax = {kmax}")
    print(f"  live blocks: {live};  max |chi_(3) - 1| = {mp.nstr(triv_dev, 3)};  max |chi_(2,1)| = {mp.nstr(bound_dev, 10)}")
    for k in ks:
        print(f"  k={k:2d} cost={int(cost[k]):3d} chi_(2,1)={mp.nstr(x[k], 12):>16}  {'feasible' if k in feas else ''}")

    kstar = min(feas, key=lambda k: cost[k])
    ilp = cost[kstar]
    print(f"\n  ILP: k* = {kstar}, cost {int(ilp)}")

    # exact LP over mixtures: best edge (a infeasible, b feasible), or a single feasible word
    def cross(a, b):
        return (cost[a] * x[b] - cost[b] * x[a]) / (x[b] - x[a])
    edges = [(cross(a, b), a, b) for a in infeas for b in feas if x[b] > TOL]
    best = min(edges, key=lambda e: e[0])
    lp_val, a_opt, b_opt = best
    if ilp < lp_val:
        lp_val, a_opt, b_opt = ilp, None, kstar
    mu = (cost[b_opt] - cost[a_opt]) / (x[b_opt] - x[a_opt]) if a_opt else mp.mpf(0)
    lam_a = x[b_opt] / (x[b_opt] - x[a_opt]) if a_opt else mp.mpf(0)
    # dual: g(mu) = min_k cost_k - mu x_k
    g = min(cost[k] - mu * x[k] for k in ks)
    attain = [k for k in ks if abs(cost[k] - mu * x[k] - g) < TOL]
    gap = ilp - lp_val
    print(f"  LP relaxation: {mp.nstr(lam_a, 12)} V^{a_opt} + {mp.nstr(1 - lam_a, 12)} V^{b_opt},  value {mp.nstr(lp_val, 15)}")
    print(f"  Lagrangian dual: mu*_(2,1) = {mp.nstr(mu, 15)}, mu*_(3) = 0, g* = {mp.nstr(g, 15)}, |g* - LP| = {mp.nstr(abs(g - lp_val), 3)}")
    print(f"  integrality gap = {mp.nstr(gap, 15)} crossings")
    print("  incidence vectors (supergradients -chi of the words attaining g*):")
    incid = {}
    for k in attain:
        incid[k] = [-chi[k][lam] for lam in live]
        print(f"    V^{k}: {[mp.nstr(v, 12) for v in incid[k]]}")

    # canonical rounding: unique feasible vertex of the optimal face
    rounded = b_opt
    print(f"  feasible vertex of the optimal face: V^{rounded}  (ILP: V^{kstar})")

    # margin condition of Lean slope_le_of_margin, X = 2
    X = mp.mpf(2)
    others = [j for j in feas if j != kstar]
    delta = (min(cost[j] for j in others) - cost[kstar]) if others else None
    margins = []
    for a in infeas:
        if cost[a] >= cost[kstar]:
            continue  # any mixture with a costs >= cost[kstar]
        lhs = (cost[kstar] - cost[a]) * (X - x[kstar])
        rhs = delta * (x[kstar] - x[a]) if delta is not None else mp.inf
        margins.append({"a": a, "lhs": lhs, "rhs": rhs, "holds": bool(lhs <= rhs)})
        print(f"  margin a=V^{a}: (c_b-c_a)(X-x_b) = {mp.nstr(lhs, 10)} <= delta(x_b-x_a) = {mp.nstr(rhs, 10)}: {lhs <= rhs}")

    # subgradient ascent: multipliers as forces
    m = mp.mpf(0)
    seq = []
    for it in range(1, 61):
        k = min(ks, key=lambda kk: cost[kk] - m * x[kk])
        seq.append(k)
        m = max(mp.mpf(0), m - x[k] / it)
    print(f"  subgradient ascent, chosen words: {seq[:24]} ...")

    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("collision-gradient-lagrangian-probe", engine="python", start_time=t0)
    wb.set_description(
        "Issue #7895: Lagrangian relaxation of the gamma-gamma word selection V^k in H_3 at the "
        "proton pin, convention D, reading 3. Exact LP over mixtures (one binding row), its "
        "Lagrangian dual with shadow prices and supergradient incidence vectors, the integrality "
        "gap, and the margin condition of Lean RelaxedVertexRounding.slope_le_of_margin that makes "
        "the unique feasible vertex of the relaxed optimal face equal the ILP choice. No AME read."
    )
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("convention", "D")
    wb.add_parameter("dps", DPS)
    wb.add_parameter("kmax", kmax)
    wb.add_parameter("cost", "crossing count 2k")
    wb.add_parameter("constraint_reading", "3: chi_lambda >= 0 on y_lambda > 0 blocks")
    wb.add_data("candidates", [{"k": k, "cost": int(cost[k]), "chi_3": fmt(chi[k][(3,)]),
                                "chi_21": fmt(x[k]), "feasible": k in feas} for k in ks])
    wb.add_data("ilp_k", kstar)
    wb.add_data("lp_support", {"a": a_opt, "b": b_opt, "weight_a": fmt(lam_a), "weight_b": fmt(1 - lam_a)})
    wb.add_data("y0_star", fmt(g))
    wb.add_data("y_star", [fmt(mp.mpf(0)), fmt(mu)])
    wb.add_data("y_star_channels", [str(lam) for lam in live])
    wb.add_data("active_set", [1] if mu > TOL else [])
    wb.add_data("primal_obj", fmt(lp_val))
    wb.add_data("dual_obj", fmt(g))
    wb.add_data("duality_gap", fmt(abs(lp_val - g)))
    wb.add_data("integrality_gap", fmt(gap))
    wb.add_data("incidence_vectors", {f"V^{k}": [fmt(v) for v in incid[k]] for k in attain})
    wb.add_data("rounded_feasible_vertex", rounded)
    wb.add_data("margin_checks", [{"a": d["a"], "lhs": fmt(d["lhs"]), "rhs": fmt(d["rhs"]), "holds": d["holds"]} for d in margins])
    wb.add_data("subgradient_sequence", seq)
    wb.add_assertion(name="trivial_block_character_is_one", computed=fmt(triv_dev), expected="0",
                     tolerance="1e-50", source="Lean trivChar_eq_one")
    wb.add_assertion(name="chi21_bounded_by_two", computed=str(int(bound_dev <= 2)), expected="1",
                     tolerance="0", source="det V = 1, |tr V| < 2 (Lean GammaGammaVertexOrder)")
    wb.add_assertion(name="ilp_selects_beta_bor", computed=str(kstar), expected="3", tolerance="0",
                     source="Lean GammaGammaFrobeniusSelection (reading 3 selects k = 3)")
    wb.add_assertion(name="strong_duality_lp_lagrangian", computed=fmt(abs(lp_val - g)), expected="0",
                     tolerance="1e-50", source="Geoffrion: Lagrangian dual = LP over convex hull")
    wb.add_assertion(name="rounded_vertex_equals_ilp", computed=str(rounded), expected=str(kstar),
                     tolerance="0", source="Lean RelaxedVertexRounding.crossVal_le_of_margin")
    wb.add_assertion(name="margin_condition_holds", computed=str(int(all(d["holds"] for d in margins))),
                     expected="1", tolerance="0", source="Lean RelaxedVertexRounding.slope_le_of_margin")
    out = wb.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
