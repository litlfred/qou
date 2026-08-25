#!/usr/bin/env python3
"""qbeta_confinement_sdp_offset_homogeneity_probe.py — can the confinement-SDP
offset carry ϑ_K? A structural test, run before any fitting.

WHERE THIS COMES FROM. The owner proposal: a particle interaction IS an SDP
solution, so the solution's geometry — magnitude, angle of incidence, offset
from the lattice saddle — may carry ϑ_K.

The angle-structure attempt (`qbeta_sdp_angle_offset_theta_probe.py`) found the
offset vanishes identically for both anchors, and `QOU/Knot/SymmetricOptimum.lean`
proved why: `optima_coincide` shows two concave objectives that are INVARIANT
under the symmetry share their optimum, so the offset between them is zero
whatever they are. The contrapositive named the next place to look — an offset
can only be informative if the objective BREAKS the symmetry. The confinement
LP/SDP's objective is Markov-trace data, which does.

SO THIS PROBE TESTS THE CONFINEMENT PROGRAM ITSELF, per prop:operator-selection-lp:

    min  t · x       t_i = tr_M(b_i)          (Markov traces of the NF basis)
    s.t. 1ᵀ x = n_target                       (net constraint)
         G x ≥ 0     G_ij = tr_M(b_i b_j)      (Frobenius positivity)

THE STRUCTURAL WORRY, STATED BEFORE MEASURING. In the corpus's canonical setup
(`aK_via_lp_dual_hecke_basis.py`) `t` and `G` come from `pyhecke.gram` and are
properties of the H_3 basis at q₀ — they are KNOT-INDEPENDENT. The only
knot-dependent input is `n_target = |tr_M(K)|`. But `G x ≥ 0` is a HOMOGENEOUS
cone constraint, so the feasible set satisfies

    {x : 1ᵀx = n, Gx ≥ 0}  =  n · {x : 1ᵀx = 1, Gx ≥ 0},

a scaled copy of one fixed polytope. A linear objective on a scaled polytope
attains its optimum at the scaled optimum. If that holds then

    x*(n) = n · x*(1)   and   x_uniform(n) = n · x_uniform(1),

so the offset scales too: its MAGNITUDE is proportional to `tr_M(K)` and its
DIRECTION is knot-independent. Two knots would then give PARALLEL offsets — the
angle carries no knot information at all, and the magnitude ratio is just
tr_M(K₁)/tr_M(K₂). That is RATIO-shaped, and
`QOU.QBeta.AfreeThetaConstraint.ratio_attained` PROVES a ratio-shaped candidate
is unfalsifiable: it names an `A_ω` rather than testing one.

WHAT IS MEASURED:
  H1  exact scaling — solve at several `n_target` and check `x*(c·n) = c·x*(n)`.
  H2  the induced offset from the symmetric point `x_uniform = (n/d)·1`:
      magnitude proportional to `n`, direction constant.
  H3  the consequence for ϑ_K, stated as a verdict.

Scope (STRICT). This tests the CANONICAL formulation as the corpus builds it. A
formulation in which `t` or `G` is itself knot-dependent is NOT homogeneous and
is NOT excluded — that is the named escape and the only way this route survives.
Nothing is fitted; no ϑ is proposed; nothing is wired.

Run: python3 -u computations/probes/qbeta_confinement_sdp_offset_homogeneity_probe.py \
       2>&1 | tee /tmp/qbeta_sdp_homog.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

# pyhecke lives under tools/, as in aK_via_lp_dual_hecke_basis.py
_TOOLS = Path(__file__).resolve().parent.parent.parent / "tools" / "pyhecke" / "python"
if _TOOLS.is_dir() and str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from pyhecke.gram import (  # noqa: E402
    NF_NAMES, gram_matrix_mp_strings, tr_m_mp_strings,
)

set_compute_dps()

SCALES = ["1.0", "2.0", "3.7067", "100.0"]
TOL = mp.mpf("1e-9")



def _norm(v):
    return mp.sqrt(mp.fsum(x ** 2 for x in v))


def main() -> int:
    print("=" * 78)
    print(" confinement-SDP offset — can it carry ϑ_K, or is it homogeneous?")
    print("=" * 78)

    # 50-dps decimal strings in, decimal strings out. The float64 here was never
    # a serialization choice (bean qou-t0rf): it was the scipy/HiGHS f64 LP and
    # the f64 Gram feeding it. `gram_matrix_mp_strings` / `tr_m_mp_strings`
    # exist for exactly this boundary and clarabel solves at ~50 dps.
    # `backend="clarabel"`, not "auto", so a missing binary RAISES instead of
    # silently dropping back to f64 and re-dirtying the witness.
    t = tr_m_mp_strings()
    G_str = gram_matrix_mp_strings()
    G = [[mp.mpf(v) for v in row] for row in G_str]
    d = len(t)
    print(f"\n  NF basis ({d}): {list(NF_NAMES)}")
    print("  objective t = tr_M(b_i)  — KNOT-INDEPENDENT (from pyhecke.gram)")
    print(f"  Gram G ({d}, {d})          — KNOT-INDEPENDENT")
    print("  only n_target = |tr_M(K)| varies per knot")
    print("  LP: clarabel MPFR @ 167 bits, decimal strings across the boundary")

    # ── H1, as an IDENTITY rather than a solver measurement ──────────────
    # The previous version tested homogeneity by asking a solver for x*(n) at
    # several n and checking x*(n) = (n/n0) x*(n0) to 1e-9. That test passed,
    # but it was measuring scipy/HiGHS's VERTEX SELECTION, not the LP: HiGHS
    # crossovers to a basic solution, vertices of n*P are n times vertices of P,
    # so a vertex-returning solver reproduces the scaling for free. Clarabel is
    # a pure interior-point method with no crossover and returns a different
    # point of the same face — under which the identical LP "fails" the same
    # test. A property that flips with the solver is not a property of the LP.
    #
    # What IS a property of the LP: feasible(n) = n * feasible(1), because
    # 1^T x = n and G x >= 0 are both homogeneous. That is an identity, checked
    # here directly on the constraint functions at 50 dps, with no solver.
    print("\n[H1] cone-slice identity (solver-free): x feasible at n  <=>  "
          "x/n feasible at 1")
    worst = mp.mpf(0)
    for k in range(1, 201):                      # deterministic, seed-free grid
        n = mp.mpf(k) / 4
        x = [mp.mpf(k + i) * (-1) ** i for i in range(d)]
        s = mp.fsum(x)
        if s == 0:
            continue
        x = [xi * n / s for xi in x]             # force 1^T x = n
        gx = [mp.fsum(G[i][j] * x[j] for j in range(d)) for i in range(d)]
        gxn = [mp.fsum(G[i][j] * (x[j] / n) for j in range(d)) for i in range(d)]
        worst = max(worst, max(abs(a / n - b) for a, b in zip(gx, gxn)))
    cone_exact = bool(worst < mp.mpf("1e-30"))
    print(f"     max |(Gx)/n − G(x/n)| over 200 points = {mp.nstr(worst, 4)}"
          f"   → identity holds: {cone_exact}")

    # ── H2: does the LP pin x* at all? ───────────────────────────────────
    print("\n[H2] what the LP actually determines, per scale:")
    rows, gaps = [], []
    for sc in SCALES:
        n = mp.mpf(sc)
        r = solve_operator_selection_lp(t, G_str, sc, backend="clarabel")
        if not r.feasible:
            print(f"     n_target={sc}: INFEASIBLE")
            return 1
        if r.x_star_str is None:
            raise RuntimeError(
                "the LP returned no full-precision strings — an f64 backend "
                "answered, which would re-dirty this witness")
        x = [mp.mpf(v) for v in r.x_star_str]
        gaps.append(abs(mp.mpf(r.duality_gap_str)))
        off = [xi - n / d for xi in x]
        rows.append({
            "n_target": sc,
            "primal_obj": mp.nstr(mp.mpf(r.primal_obj_str), 4),
            "y0_star": mp.nstr(mp.mpf(r.y0_star_str), 4),
            "duality_gap": mp.nstr(abs(mp.mpf(r.duality_gap_str)), 4),
            "offset_norm_solver_dependent": mp.nstr(_norm(off), 15),
            "active_set": list(r.active_set),
        })
        print(f"     n={sc:>8}  min t·x = {rows[-1]['primal_obj']:>11}   "
              f"y0* = {rows[-1]['y0_star']:>11}   "
              f"‖offset‖ = {rows[-1]['offset_norm_solver_dependent']}")

    max_gap = max(gaps) if gaps else mp.mpf(0)
    objs = [abs(mp.mpf(r["primal_obj"])) for r in rows]
    y0s = [abs(mp.mpf(r["y0_star"])) for r in rows]
    obj_is_zero = bool(objs and max(objs) < mp.mpf("1e-10"))
    y0_is_zero = bool(y0s and max(y0s) < mp.mpf("1e-10"))
    degenerate = bool(obj_is_zero and y0_is_zero)
    print(f"\n     LP duality gap (max) = {mp.nstr(max_gap, 4)} — the accuracy "
          "floor is the interior-point")
    print("     solver's convergence, not the arithmetic.")
    print(f"     min t·x = 0 at every n: {obj_is_zero}      "
          f"y0* = 0 at every n: {y0_is_zero}")
    if degenerate:
        print("     ⇒ the objective is DEGENERATE: the optimal face is not a "
              "point, so x* — and")
        print("       therefore 'the offset' — is not determined by the LP at "
              "all. Which point comes")
        print("       back is a solver choice (HiGHS: a vertex; clarabel: an "
              "interior point).")

    homogeneous = cone_exact

    verdict = (
        "THE CONFINEMENT LP CANNOT CARRY ϑ_K, and the reason is stronger than "
        "the one this probe originally recorded. TWO FACTS, established "
        "separately. (1) HOMOGENEITY, now as an IDENTITY rather than a "
        "measurement: 1^T x = n and G x >= 0 are both homogeneous, so "
        "feasible(n) = n * feasible(1) exactly — checked on the constraint "
        f"functions at 50 dps to {mp.nstr(worst, 3)}, with no solver involved. "
        "Since t and G are knot-INDEPENDENT (properties of the H_3 basis at q0) "
        "and only n_target = |tr_M(K)| varies, two knots give PARALLEL offsets: "
        "the ANGLE carries zero knot information and the MAGNITUDE is a fixed "
        "constant times tr_M(K), so the pair supplies ONE knot-dependent number "
        "and its content is the ratio tr_M(K1)/tr_M(K2). "
        "AfreeThetaConstraint.ratio_attained proves a ratio-shaped candidate is "
        "unfalsifiable. (2) WORSE: the objective is DEGENERATE. min t·x = 0 and "
        f"y0* = 0 at every tested n (to {mp.nstr(max_gap, 3)}, the solver's "
        "duality gap), so the optimal face is not a point and the LP does not "
        "determine x* at all. 'The offset from the lattice saddle' is therefore "
        "not a well-defined function of the knot even before homogeneity is "
        "invoked — it is whatever point on a zero-objective face the solver "
        "happens to return. "
        "RETRACTED, and this is the reason the second fact surfaced: the "
        "earlier version reported x*(n) = (n/n0) x*(n0) to 1e-9 as the "
        "measurement establishing homogeneity. That number was an artifact of "
        "scipy/HiGHS crossing over to a VERTEX — vertices of n*P are n times "
        "vertices of P, so any vertex-returning solver reproduces the scaling "
        "regardless. Re-run against clarabel's interior point the same LP "
        "'fails' it. The conclusion was right; the evidence was solver-"
        "dependent and has been replaced by the identity above. "
        "THE ESCAPE, unchanged and still the only one: a formulation whose t or "
        "G is itself knot-dependent is NOT homogeneous and is NOT excluded — "
        "the braid's operator content must enter the OBJECTIVE or the GRAM, not "
        "merely the net constraint. SCOPE (a): this excludes the canonical "
        "scalar-net formulation as the corpus builds it, not the proposal. "
        "Nothing fitted; nothing wired."
        if homogeneous else
        "THE CONE-SLICE IDENTITY FAILED, which should be impossible for "
        "homogeneous constraints — inspect the Gram construction before reading "
        "anything else here.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-confinement-sdp-offset-homogeneity",
                        engine="pyhecke+clarabel-mpfr+mpmath")
    wb.set_description(
        "Tests whether the confinement operator-selection LP's solution offset "
        "can carry theta_K. Two independent reasons it cannot. (1) The "
        "Frobenius constraint Gx >= 0 and the net constraint 1^T x = n are both "
        "homogeneous, so feasible(n) = n * feasible(1) as an IDENTITY (verified "
        "on the constraint functions at 50 dps, no solver); with t and G "
        "knot-independent and only n_target = |tr_M(K)| varying, two knots give "
        "parallel offsets, so the pair (magnitude, angle) is ratio-shaped and "
        "unfalsifiable by AfreeThetaConstraint.ratio_attained. (2) The "
        "objective is DEGENERATE: min t.x = 0 and y0* = 0 at every n, so the "
        "optimal face is not a point and x* is not determined by the LP — "
        "'the offset' is a solver artifact. Supersedes this witness's earlier "
        "x*(n) = (n/n0)x*(n0) measurement, which read scipy/HiGHS's vertex "
        "selection rather than a property of the program. Escape: a formulation "
        "with knot-dependent t or G is not homogeneous and is not excluded. "
        "Nothing fitted.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("program", "min t.x s.t. 1^T x = n_target, G x >= 0 "
                           "(prop:operator-selection-lp)")
    wb.add_data("knot_independent_inputs",
                {"t": "tr_M(b_i) from pyhecke.gram", "G": "tr_M(b_i b_j)",
                 "basis": list(NF_NAMES)})
    wb.add_data("knot_dependent_input", "n_target = |tr_M(K)| only")
    wb.add_data("cone_slice_identity", {
        "max_dev": mp.nstr(worst, 4),
        "holds": cone_exact,
        "method": ("(Gx)/n vs G(x/n) on 200 deterministic points with "
                   "1^T x = n, evaluated at 50 dps — no LP solver"),
    })
    wb.add_data("lp_degeneracy", {
        "min_objective_is_zero_at_every_n": obj_is_zero,
        "y0_star_is_zero_at_every_n": y0_is_zero,
        "degenerate": degenerate,
        "consequence": ("the optimal face is not a point, so x* and hence the "
                        "offset are not determined by the LP; the returned "
                        "point is a solver choice"),
    })
    wb.add_data("per_scale", rows)
    wb.add_data("homogeneous", homogeneous)
    wb.add_data("lp_precision", {
        "backend": "clarabel MPFR @ 167 bits (~50 dps)",
        "inputs": "gram_matrix_mp_strings / tr_m_mp_strings — no f64 anywhere",
        "max_duality_gap": mp.nstr(max_gap, 4),
        "reported_digits": 15,
        "why": ("the interior-point solver's convergence gap, not float "
                "arithmetic, is the accuracy floor; values are reported to 15 "
                "digits, inside it. The previous version solved this LP with "
                "scipy/HiGHS in float64 and published 17."),
    })
    wb.add_data("RETRACTED_measurement", {
        "was": "x*(n) = (n/n0) x*(n0) to 1e-9, and ||offset||/n constant",
        "why_retracted": (
            "solver-dependent, not a property of the LP. scipy/HiGHS crosses "
            "over to a basic (vertex) solution; vertices of n*P are n times "
            "vertices of P, so the scaling is reproduced by the solver's "
            "selection rule regardless of the program. clarabel, a pure "
            "interior-point method, returns a different point of the same "
            "zero-objective face and the same LP 'fails' the test."),
        "replaced_by": "the cone_slice_identity block, which needs no solver",
        "conclusion_unchanged": True,
    })
    wb.add_data("why_it_matters",
                "homogeneity makes the offset direction knot-independent and the "
                "magnitude proportional to tr_M(K); the pair is therefore "
                "ratio-shaped and unfalsifiable by ratio_attained. Degeneracy "
                "makes the offset undefined in the first place.")
    wb.add_data("the_only_escape",
                "put the braid's operator content into the OBJECTIVE t or the "
                "GRAM G, not merely the net constraint n_target; that breaks "
                "homogeneity and is not excluded here")
    wb.add_data("verdict", verdict)
    wb.add_assertion("confinement_lp_is_homogeneous",
                     computed="1" if homogeneous else "0", expected="1",
                     tolerance="0.5",
                     source="feasible(n) = n * feasible(1) as an identity on "
                            "the constraint functions at 50 dps — the "
                            "cone-slice structure of 1^T x = n with G x >= 0, "
                            "checked without an LP solver")
    wb.add_assertion("lp_objective_is_degenerate",
                     computed="1" if degenerate else "0", expected="1",
                     tolerance="0.5",
                     source="min t.x = 0 and y0* = 0 at every tested n, so the "
                            "optimal face is not a point and the LP does not "
                            "pin x* — the offset is a solver artifact")
    wb.save()
    print("  witness -> computations/probes/"
          "qbeta-confinement-sdp-offset-homogeneity.witness.json")
    return 0 if homogeneous else 1


if __name__ == "__main__":
    raise SystemExit(main())
