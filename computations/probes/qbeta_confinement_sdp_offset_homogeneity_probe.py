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

import numpy as np
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
from pyhecke.gram import TR_M, NF_NAMES, gram_matrix  # noqa: E402

set_compute_dps()

SCALES = ["1.0", "2.0", "3.7067", "100.0"]
TOL = 1e-9


def main() -> int:
    print("=" * 78)
    print(" confinement-SDP offset — can it carry ϑ_K, or is it homogeneous?")
    print("=" * 78)

    t = np.asarray([float(v) for v in TR_M], dtype=float)
    G = gram_matrix()
    G = np.asarray([[float(v) for v in row] for row in G], dtype=float)
    d = len(t)
    print(f"\n  NF basis ({d}): {list(NF_NAMES)}")
    print(f"  objective t = tr_M(b_i)  — KNOT-INDEPENDENT (from pyhecke.gram)")
    print(f"  Gram G {G.shape}          — KNOT-INDEPENDENT")
    print(f"  only n_target = |tr_M(K)| varies per knot\n")

    base = None
    rows, scale_ok = [], True
    for s in SCALES:
        n = float(s)
        r = solve_operator_selection_lp(t, G, n, backend="scipy")
        x = np.asarray(r.x_star, dtype=float)
        if not r.feasible:
            print(f"  n_target={s}: INFEASIBLE")
            scale_ok = False
            continue
        uni = np.full(d, n / d)
        off = x - uni
        mag = float(np.linalg.norm(off))
        unit = (off / mag).tolist() if mag > TOL else None
        if base is None:
            base = (n, x.copy(), off.copy(), mag)
            dev = 0.0
            angdev = 0.0
        else:
            # H1: does x*(n) equal (n/n0) x*(n0) ?
            dev = float(np.max(np.abs(x - (n / base[0]) * base[1])))
            # H2: is the offset direction unchanged?
            b_off = base[2]
            cos = float(off @ b_off / (np.linalg.norm(off) * np.linalg.norm(b_off))) \
                if mag > TOL and np.linalg.norm(b_off) > TOL else 1.0
            angdev = float(np.arccos(max(-1.0, min(1.0, cos))))
        scale_ok = scale_ok and dev < TOL and angdev < 1e-7
        rows.append({"n_target": s, "offset_norm": mag,
                     "offset_norm_over_n": mag / n,
                     "max_dev_from_scaled": dev,
                     "angle_dev_from_base_rad": angdev})
        print(f"    n_target={s:>8}   ‖offset‖ = {mag:.12g}   "
              f"‖offset‖/n = {mag / n:.12g}")
        print(f"    {'':>8}          max|x*(n) − (n/n₀)x*(n₀)| = {dev:.3g}   "
              f"angle drift = {angdev:.3g} rad")

    ratios = [r["offset_norm_over_n"] for r in rows]
    const = (max(ratios) - min(ratios)) < 1e-9 if ratios else False
    print(f"\n  H1/H2: ‖offset‖/n constant across scales: {const}")
    print(f"         exact scaling x*(n) = (n/n₀)·x*(n₀): {scale_ok}")

    homogeneous = bool(const and scale_ok)
    verdict = (
        "THE CONFINEMENT LP IS HOMOGENEOUS, SO ITS OFFSET CANNOT CARRY ϑ_K — a "
        "structural exclusion of the canonical formulation, established before "
        "any fitting. The Frobenius constraint G x >= 0 is a CONE, so the "
        "feasible set at net n_target is exactly n_target times the fixed "
        "polytope at 1. Measured: x*(n) = (n/n0) x*(n0) to "
        f"{max((r['max_dev_from_scaled'] for r in rows), default=0):.2g} and the "
        "offset direction is constant to "
        f"{max((r['angle_dev_from_base_rad'] for r in rows), default=0):.2g} rad, "
        "with ||offset||/n constant. Since t and G are knot-INDEPENDENT "
        "(properties of the H_3 basis at q0) and only n_target = |tr_M(K)| "
        "varies, two knots produce PARALLEL offsets: the ANGLE carries zero "
        "knot information — it is literally the same number for every knot — "
        "and the MAGNITUDE is a fixed constant times tr_M(K). So the pair "
        "(magnitude, angle) supplies ONE knot-dependent number, not two, and "
        "its knot-to-knot content is the ratio tr_M(K1)/tr_M(K2). "
        "AfreeThetaConstraint.ratio_attained proves a ratio-shaped candidate is "
        "unfalsifiable — it names an A_omega rather than testing one. This "
        "route, in this formulation, therefore cannot clear the falsifiability "
        "bar. THE ESCAPE, and it is the only one: a formulation whose t or G is "
        "itself knot-dependent is NOT homogeneous and is NOT excluded. That "
        "means the braid's own operator content must enter the OBJECTIVE or the "
        "GRAM, not merely the net constraint. SCOPE (a): this excludes the "
        "canonical scalar-net formulation as the corpus builds it, not the "
        "proposal. Nothing fitted; nothing wired."
        if homogeneous else
        "NOT HOMOGENEOUS on the tested scales — the offset direction or the "
        "normalised magnitude moved. Inspect the table: if real, the offset "
        "does carry scale-dependent structure and the route is still live.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-confinement-sdp-offset-homogeneity", engine="scipy+mpmath")
    wb.set_description(
        "Tests whether the confinement operator-selection LP's solution offset "
        "can carry theta_K. The Frobenius constraint Gx >= 0 is a homogeneous "
        "cone, so the feasible set at net n_target is n_target times a fixed "
        "polytope; with t and G knot-independent (pyhecke.gram) and only "
        "n_target = |tr_M(K)| varying, the optimum and hence the offset scale "
        "exactly. Verified numerically. Consequence: two knots give PARALLEL "
        "offsets — the angle is knot-independent and the magnitude is "
        "proportional to tr_M(K), so the pair supplies one number, not two, and "
        "is ratio-shaped. AfreeThetaConstraint.ratio_attained proves such a "
        "candidate unfalsifiable. Escape: a formulation with knot-dependent t "
        "or G is not homogeneous and is not excluded. Nothing fitted.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("program", "min t.x s.t. 1^T x = n_target, G x >= 0 "
                           "(prop:operator-selection-lp)")
    wb.add_data("knot_independent_inputs",
                {"t": "tr_M(b_i) from pyhecke.gram", "G": "tr_M(b_i b_j)",
                 "basis": list(NF_NAMES)})
    wb.add_data("knot_dependent_input", "n_target = |tr_M(K)| only")
    wb.add_data("scaling_table", rows)
    wb.add_data("homogeneous", homogeneous)
    wb.add_data("why_it_matters",
                "homogeneity makes the offset direction knot-independent and the "
                "magnitude proportional to tr_M(K); the pair is therefore "
                "ratio-shaped and unfalsifiable by ratio_attained")
    wb.add_data("the_only_escape",
                "put the braid's operator content into the OBJECTIVE t or the "
                "GRAM G, not merely the net constraint n_target; that breaks "
                "homogeneity and is not excluded here")
    wb.add_data("verdict", verdict)
    wb.add_assertion("confinement_lp_is_homogeneous",
                     computed=1.0 if homogeneous else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="x*(n) = (n/n0) x*(n0) and ||offset||/n constant "
                            "across the tested net values — the cone-slice "
                            "structure of G x >= 0")
    wb.save()
    print("  witness -> computations/probes/"
          "qbeta-confinement-sdp-offset-homogeneity.witness.json")
    return 0 if homogeneous else 1


if __name__ == "__main__":
    raise SystemExit(main())
