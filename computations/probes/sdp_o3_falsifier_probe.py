#!/usr/bin/env python3
"""O3 falsifier: the block-PSD program is ALSO degenerate -- by a different route.

Runs the test stated in
docs/proposals/2026-09-05-operator-selection-objective-replacement.md Sec 8:
"O3 is wrong if the block-PSD program is also degenerate."

IT FIRES -- and the mechanism is not the one predicted, which is why the result
is constructive rather than merely negative.

WHAT IS FIXED. The LP's defect (S1: the objective duplicates the i=1 constraint,
so the optimum is identically 0 at six vertices) genuinely does NOT reproduce.
All six LP-optimal vertices from
docs/audits/2026-08-24-operator-selection-lp-objective-defect.md are excluded by
the PSD constraint, and not marginally -- minimum eigenvalues -7.33 and -3.85.

WHAT BREAKS INSTEAD. Solving for the Markov weights from the six basis traces
(6 equations, 3 unknowns, so consistency is itself the validation) gives

    y_(3)       = 0.50540422650393
    y_(2,1)     = 0.24729788674803
    y_(1,1,1)   = 1.45e-17        <-- ZERO

which is the SU(2) specialisation: at convention-D z the Markov weight vanishes
for partitions with more than 2 rows. A zero-weight block does not enter the
objective at all, so a Phi supported ONLY there is PSD (1x1, entry +1 > 0), has
objective 0, and has sum x_i = 0.0202 != 0 -- hence scales to ANY n_target.
The SDP's optimum is therefore also identically 0, attained on a ray.

AND THE RAY IS ALREADY NAMED. It is the q-antisymmetriser
RADICAL = (1, -1/q, -1/q, 1/q^2, 1/q^2, -1/q^3), matched here to a relative
spread of 2.9e-6 (limited by the 6-digit vertex data, not by the arithmetic).
That is the known radical of the Frobenius form under convention D, for which
the corpus already ships G_PINV / gram_quotient_inverse.

SO THE REPAIR IS THE QUOTIENT, NOT A NEW OBJECT. Posing the block-PSD program on
H_3 / radical -- equivalently, over the partitions with NONZERO Markov weight
(<= 2 rows for SU(2)) -- removes the degenerate direction. There the objective is
sum_lambda y_lambda tr(Phi_lambda) with every y_lambda > 0, so PSD feasibility
forces objective >= 0 with equality only at Phi = 0, which the net constraint
excludes. That is option O3' and it is what the proposal should recommend.

NOT CLAIMED: that O3' SELECTS anything. The scope-(b) exclusion (no linear
objective selects B_3) and the relative-interior finding both concern the
feasible geometry and are untouched by re-posing the program.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged. Gap qou-sv7h OPEN.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402
import pyhecke_native as PHN  # noqa: E402

from pyhecke.gram import NF_BASIS, NF_NAMES, TR_M  # noqa: E402
from hecke_core import partitions_of, partition_dimension  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

# The six LP-optimal vertices, from the 2026-08-24 audit's table.
VERTICES = {
    "(1,2,3)": [-1.3148, -1.4594, -1.4594, +3.2482, -1.6199, +3.6054],
    "(1,2,4)": [-1.3148, -1.4594, -1.4594, -1.6199, +3.2482, +3.6054],
    "(1,3,5)": [-0.6174, -0.6853, +1.8520, +2.0557, -0.7607, -0.8443],
    "(1,4,5)": [-0.6174, -0.6853, +1.8520, -0.7607, +2.0557, -0.8443],
    "(2,3,5)": [-0.6174, +1.8520, -0.6853, +2.0557, -0.7607, -0.8443],
    "(2,4,5)": [-0.6174, +1.8520, -0.6853, -0.7607, +2.0557, -0.8443],
}
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))


def main() -> int:
    set_compute_dps()
    q = Q_MP
    parts = [tuple(p) for p in partitions_of(3)]
    dims = [partition_dimension(p) for p in parts]

    def gens(lam):
        raw = PHN.seminormal_matrices_mpfr(list(lam), Q_50_DIGIT_STR, 50)
        d = partition_dimension(lam)
        out = []
        for g in raw:
            M = mp.zeros(d, d)
            for i, row in enumerate(g):
                for (j, s) in row:
                    M[i, j] = mp.mpf(s)
            out.append(M)
        return out

    G = {lam: gens(lam) for lam in parts}

    def rho(lam, word):
        M = mp.eye(partition_dimension(lam))
        for g in word:
            M = M * G[lam][g]
        return M

    print("=" * 74)
    print("  O3 falsifier: is the partition-block SDP degenerate too?")
    print("=" * 74)
    print()

    # ---- solve for the Markov weights; consistency IS the validation ------
    A = mp.matrix(6, 3); b = mp.matrix(6, 1)
    for i, word in enumerate(NF_BASIS):
        for k, lam in enumerate(parts):
            M = rho(lam, word)
            A[i, k] = sum(M[j, j] for j in range(partition_dimension(lam)))
        b[i] = mp.mpf(str(TR_M[i]))
    y = mp.lu_solve(A.T * A, A.T * b)
    resid = A * y - b
    mx = max(abs(resid[i]) for i in range(6))
    print("  Markov weights solved from the six basis traces (6 eqns, 3 unknowns):")
    for k, lam in enumerate(parts):
        print(f"     {str(lam):<12} d={dims[k]}   y = {mp.nstr(y[k], 14)}")
    print(f"     max residual {mp.nstr(mx, 6)}   sum y*d = "
          f"{mp.nstr(sum(y[k] * dims[k] for k in range(3)), 12)}")
    # TR_M in pyhecke.gram is a float64 array, so float64 eps IS exact here.
    # A first pass demanded < 1e-30 and wrongly reported INCONSISTENT.
    check("the block decomposition reproduces tr_M at float64 input precision",
          mx < mp.mpf("1e-13"), f"residual {mp.nstr(mx, 4)}")
    check("normalisation sum y_lambda d_lambda = 1",
          abs(sum(y[k] * dims[k] for k in range(3)) - 1) < mp.mpf("1e-13"))
    zero_w = [parts[k] for k in range(3) if abs(y[k]) < mp.mpf("1e-13")]
    check("exactly one partition has ZERO Markov weight (the SU(2) vanishing)",
          zero_w == [(1, 1, 1)], "3 rows > 2, so invisible to the objective")

    # ---- the LP's degeneracy does NOT reproduce --------------------------
    print()
    print("  the LP's six optimal vertices, under the PSD constraint:")
    verts = []
    for name, xv in VERTICES.items():
        mins = []
        for lam in parts:
            d = partition_dimension(lam)
            Phi = mp.zeros(d, d)
            for i, word in enumerate(NF_BASIS):
                Phi += mp.mpf(str(xv[i])) * rho(lam, word)
            Phi = (Phi + Phi.T) / 2
            ev = mp.eigsy(Phi, eigvals_only=True) if d > 1 else [Phi[0, 0]]
            mins.append(min(ev))
        m = min(mins)
        verts.append({"vertex": name, "min_eigenvalue": fmt(m), "psd": bool(m >= 0)})
        print(f"     {name:>9}  min eig = {mp.nstr(m, 12):>16}   "
              f"{'PSD' if m >= 0 else 'NOT PSD -> excluded'}")
    check("every LP-optimal vertex is EXCLUDED by the PSD constraint",
          not any(v["psd"] for v in verts),
          "so the objective-duplicates-constraint defect does not reproduce")

    # ---- but a zero-weight block is free: the falsifier fires -------------
    print()
    print("  the zero-weight block is unconstrained by the objective:")
    rows, rhs = [], []
    for lam in parts:
        d = partition_dimension(lam)
        for a in range(d):
            for c in range(d):
                rows.append([rho(lam, w)[a, c] for w in NF_BASIS])
                rhs.append(mp.mpf(1) if (lam == (1, 1, 1) and a == 0 and c == 0)
                           else mp.mpf(0))
    xr = mp.lu_solve(mp.matrix(rows), mp.matrix(rhs))
    sx = sum(xr[i] for i in range(6))
    rad = [mp.mpf(1), -1 / q, -1 / q, 1 / q ** 2, 1 / q ** 2, -1 / q ** 3]
    ratios = [xr[i] / rad[i] for i in range(6)]
    spread = (max(ratios) - min(ratios)) / abs(sum(ratios) / 6)
    print(f"     Phi supported only on (1,1,1):  sum x_i = {mp.nstr(sx, 12)}"
          f"   objective = {mp.nstr(sum(y[k] * (1 if parts[k] == (1,1,1) else 0) for k in range(3)), 6)}")
    print(f"     matches the known RADICAL (q-antisymmetriser) to spread "
          f"{mp.nstr(spread, 6)}")
    check("that direction has NONZERO net, so it scales to any n_target",
          abs(sx) > mp.mpf("1e-12"),
          "PSD, objective 0 -> the SDP optimum is identically 0 on a ray")
    check("the degenerate ray IS the known radical, not a new object",
          spread < mp.mpf("1e-4"),
          "so the repair is the existing quotient (G_PINV / gram_quotient_inverse)")

    print()
    print("  VERDICT: falsifier FIRES. The SDP fixes the LP's defect and acquires")
    print("  a different one -- the SU(2) zero-weight block. The repair is O3':")
    print("  pose the program on the QUOTIENT by the radical, i.e. over the")
    print("  partitions with nonzero Markov weight. There every y_lambda > 0, so")
    print("  PSD feasibility forces objective > 0 away from Phi = 0.")

    w = WitnessBuilder("sdp-o3-falsifier", engine="python+mpmath+rust")
    w.set_description(
        "O3 falsifier for the operator-selection replacement. The partition-block "
        "SDP DOES fix the LP's objective-duplicates-constraint defect (all six "
        "LP-optimal vertices excluded, min eig -7.33/-3.85) but is degenerate by a "
        "different route: the SU(2) specialisation gives y_(1,1,1) = 0, so a Phi "
        "supported on that block is PSD with objective 0 and nonzero net, making "
        "the optimum identically 0 on a ray. That ray is the known q-antisymmetriser "
        "radical, so the repair is the existing quotient (O3')."
    )
    w.set_audit_only("docs/proposals/2026-09-05-operator-selection-objective-replacement.md")
    w.add_parameter("q0", fmt(q))
    w.add_data("markov_weights",
               [{"partition": str(parts[k]), "dim": dims[k], "y": fmt(y[k])}
                for k in range(3)])
    w.add_data("lp_vertices_under_psd", verts)
    w.add_data("degenerate_ray",
               {"net_sum": fmt(sx), "radical_match_spread": fmt(spread)})
    for nm, ok in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="sdp_o3_falsifier_probe")
    print(f"\n  witness: {w.save()}")
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed")
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
