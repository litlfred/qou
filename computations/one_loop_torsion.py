#!/usr/bin/env python3
# polynomial_q_not_applicable: hyperbolic-geometry numeric helper.
"""one_loop_torsion.py — the Dimofte-Garoufalidis 1-loop invariant, done right.

WHY THIS EXISTS

Three implementations of "the 1-loop determinant" exist in this repo and they
disagree. This is the one that is correct, promoted out of a probe so the
others can point at it instead of re-deriving it.

    whitehead_c_sigma_torsion.py     |tau(4_1)| = sqrt(3)     NOT invariant
    probes/one_loop_vs_nu_sdp_probe  |tau(4_1)| = sqrt(3)/2   INVARIANT   <- this
    probes/torsion_nu_sdp_probe.py   |T_mu(4_1)| = 3          Porti convention

`sqrt(3)/2` is Dimofte-Garoufalidis' own worked figure-eight example
(arXiv:1202.6268, eq. 3.2). The `sqrt(3)` in the first is exactly twice it —
the `1/2` that file's docstring claims is unnecessary "because the calibration
reproduces the known value sqrt(3)". See
`docs/audits/2026-08-07-one-loop-fix-impact-analysis.md`.

THE FORMULA (DG Defn 1.2 / Garoufalidis-Yoon 2411.03801 Defn 2.1)

    tau = +- (1/2) det( G_mu diag(zeta) + G'_mu diag(zeta') + G''_mu diag(zeta'') )
                   / prod_j zeta_j^{f_j} zeta'_j^{f'_j} zeta''_j^{f''_j}

with `zeta = 1/z`, `zeta' = 1/(1-z)`, `zeta'' = 1/(z(z-1))`, `G_mu` the edge
gluing matrices with one edge row replaced by the meridian completeness row,
and `(f, f', f'')` a combinatorial flattening:

    f + f' + f'' = 1  per tetrahedron,     G f + G' f' + G'' f'' = 2  on edges

That flattening convention is DG Definition 2.1. It is worth stating because
reasoning from `z z' z'' = -1` suggests `f + f' + f'' = -1`, which has NO
integer solution at all (bean qou-fl4t).

ONE CUSP ONLY — AND THIS RAISES RATHER THAN RETURNING GARBAGE

DG Definition 1.2 is stated for one-cusped manifolds; the multi-cusp case is
their Section 4.5 ("Invariance of the generalized torsion"), which is NOT
implemented here. `G_mu` substitutes ONE meridian row for ONE edge row, which
is right at `c = 1` and wrong for `c >= 2`, where `N - c` edges and `c`
meridians are needed.

The probe this was promoted from silently returns `0` for links — verified:
`|tau(L5a1)| = |tau(L6a4)| = 0.000000`. A zero that means "not implemented" is
indistinguishable from a zero that means "the torsion vanishes", so this module
RAISES instead. That matters: the whole c_sigma arc is c=2 and c=3, so anyone
reaching for this to fix it will hit the guard rather than a plausible number.

PRECISION

Shapes are read at `bits_prec` derived from `mp.mp.dps` and converted through
decimal strings; the determinant is an mpmath determinant. The probe this came
from used `complex(s['rect'])` and `np.linalg.det`, i.e. float64 throughout
(bean qou-t0rf's class). The flattening is solved over the integers with sympy.

VALIDATION

`self_test()` checks `|tau(4_1)| = sqrt(3)/2` against DG's worked example, and
that `L5a1` raises rather than returning 0. Garoufalidis-Yoon prove
1-loop = adjoint torsion for TWO-BRIDGE knots, which covers 4_1, 5_2, 6_2 — so
the one-cusped leg is validated against a theorem, not self-consistency.

-- Ref: [dimofte-garoufalidis2013] arXiv:1202.6268, Defn 1.2, Defn 2.1, eq 3.2
-- Ref: [garoufalidis-yoon] arXiv:2411.03801, Defn 2.1 (symmetric normalization)
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


class MultiCuspNotImplemented(NotImplementedError):
    """Raised for c >= 2: needs DG Section 4.5, which is not implemented."""


def _bits() -> int:
    return int(mp.mp.dps * 3.3219) + 16


def _shapes(M):
    """Tetrahedra shapes as mpc via decimal strings — never through float()."""
    return [mp.mpc(mp.mpf(str(s.real())), mp.mpf(str(s.imag())))
            for s in M.tetrahedra_shapes("rect", bits_prec=_bits())]


def flattening(M):
    """A combinatorial flattening (f, f', f''), DG Defn 2.1, over the integers.

    Free parameters are set to 0. DG prove the invariant is independent of the
    flattening choice (their Section 3.5), so any solution serves.
    """
    N = M.num_tetrahedra()
    R = sp.Matrix([[int(x) for x in r] for r in M.gluing_equations(form="log")])
    G, Gp, Gpp = R[:, 0::3], R[:, 1::3], R[:, 2::3]
    Ge, Gpe, Gppe = G[:N, :], Gp[:N, :], Gpp[:N, :]
    f = sp.symbols(f"f0:{N}")
    fp = sp.symbols(f"fp0:{N}")
    fpp = sp.symbols(f"fpp0:{N}")
    eqs = [sp.Eq(f[i] + fp[i] + fpp[i], 1) for i in range(N)]
    lhs = Ge * sp.Matrix(f) + Gpe * sp.Matrix(fp) + Gppe * sp.Matrix(fpp)
    eqs += [sp.Eq(lhs[i], 2) for i in range(N)]
    sols = list(sp.linsolve(eqs, list(f) + list(fp) + list(fpp)))
    if not sols:
        raise ValueError("no flattening: gluing system inconsistent")
    sol = sols[0]
    free = set()
    for e in sol:
        free |= e.free_symbols
    subs = {s: sp.Integer(0) for s in free}
    v = [sp.nsimplify(e.subs(subs)) for e in sol]
    if not all(x.is_Integer for x in v):
        raise ValueError("flattening not integral at this parameter choice")
    v = [int(x) for x in v]
    return v[:N], v[N:2 * N], v[2 * N:]


def one_loop(M):
    """DG 1-loop invariant tau of a ONE-CUSPED hyperbolic manifold, as mpc.

    Raises MultiCuspNotImplemented for c >= 2 rather than returning a
    meaningless value.
    """
    c = M.num_cusps()
    if c != 1:
        raise MultiCuspNotImplemented(
            f"{M.name() if hasattr(M, 'name') else M}: {c} cusps. DG Defn 1.2 is "
            "one-cusped; multi-cusp needs DG Sec 4.5 (not implemented). The probe "
            "this was promoted from returns 0 here, which is why it raises instead."
        )
    N = M.num_tetrahedra()
    R = [[int(x) for x in r] for r in M.gluing_equations(form="log")]
    G = [[r[0::3][j] for j in range(N)] for r in R]
    Gp = [[r[1::3][j] for j in range(N)] for r in R]
    Gpp = [[r[2::3][j] for j in range(N)] for r in R]
    mer = N                                    # meridian row follows the N edges

    def mu(A):
        B = [list(row) for row in A[:N]]
        B[-1] = list(A[mer])                   # swap last edge row for meridian
        return B

    Gm, Gpm, Gppm = mu(G), mu(Gp), mu(Gpp)
    z = _shapes(M)
    zeta = [1 / x for x in z]
    zetap = [1 / (1 - x) for x in z]
    zetapp = [1 / (x * (x - 1)) for x in z]
    A = mp.matrix(N, N)
    for i in range(N):
        for j in range(N):
            A[i, j] = (Gm[i][j] * zeta[j] + Gpm[i][j] * zetap[j]
                       + Gppm[i][j] * zetapp[j])
    det = mp.det(A)
    fv, fpv, fppv = flattening(M)
    denom = mp.mpc(1)
    for j in range(N):
        denom *= zeta[j] ** fv[j] * zetap[j] ** fpv[j] * zetapp[j] ** fppv[j]
    return det / (2 * denom)


def self_test() -> int:
    import snappy

    ok = True
    tau41 = one_loop(snappy.Manifold("4_1"))
    target = mp.sqrt(3) / 2
    rel = abs(abs(tau41) - target) / target
    good = rel < mp.mpf("1e-20")
    ok &= bool(good)
    print(f"  |tau(4_1)|  = {mp.nstr(abs(tau41), 25)}")
    print(f"  sqrt(3)/2   = {mp.nstr(target, 25)}   rel={mp.nstr(rel, 4)}"
          f"   {'OK (DG eq 3.2)' if good else 'FAIL'}")
    try:
        one_loop(snappy.Manifold("L5a1"))
        print("  L5a1: FAIL — returned a value instead of raising")
        ok = False
    except MultiCuspNotImplemented:
        print("  L5a1: raises MultiCuspNotImplemented   OK (does not return 0)")
    for k in ("5_2", "6_2"):
        print(f"  |tau({k})| = {mp.nstr(abs(one_loop(snappy.Manifold(k))), 20)}")
    print("SELF-TEST", "PASSED" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(self_test())
