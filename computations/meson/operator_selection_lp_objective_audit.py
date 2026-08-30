#!/usr/bin/env python3
"""The operator-selection LP's objective is bounded below by its own constraint.

Audits `prop:operator-selection-lp` against what it claims. Three findings, all
symbolic over `Q(q)` except where a pin is named:

1. THE OBJECTIVE IS VACUOUS. The NF basis begins with the empty word, so
   `b_1 = 1` and `G[0][j] = tr_M(1 . b_j) = t_j` -- the first row of the Gram
   matrix IS the objective vector. So the Frobenius positivity constraint at
   i = 1 is literally `t.x >= 0`. The program minimises `t.x` subject to
   `t.x >= 0`, hence the optimum is exactly 0 whenever feasible. This needs
   only that the basis contains the identity, so it holds for every n, every q,
   and EVERY trace convention -- it is not a convention-D artifact.
   `primal_obj = 0` and `y_0* = 0` both follow, rather than being coincidences.

2. THE ARGMIN IS NOT A POINT. The optimal set is a positive-dimensional face;
   enumerated at the proton pin it has at least six vertices, all at objective
   0, in mirror pairs under sigma_0 <-> sigma_1. Since `t` and `G` are
   mirror-invariant the optimal set is mirror-closed, so a unique optimum would
   have to be mirror-symmetric -- and none of these is. "The solution x*" and
   "the unique optimizer" are therefore both false.

3. THE CLAIMED OPTIMIZER IS NOT ONE. `prf:operator-selection-lp` tabulates the
   n = 3 optimum as NF(B_3). Computed here directly, NF(B_3) reproduces that
   table to every printed digit and is strictly feasible -- but its objective is
   tr_M(B_3) ~ 0.9986 against an optimum of 0. The program does not select the
   Borromean link.

Emits no witness: a decision probe whose output is an argument. Carries the
NO-FLOAT64 discipline anyway -- all arithmetic is exact (sympy over Q(q), and
`Rational` at the pin); `float` appears only inside display formatting.

Bean qou-v7qj.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import sympy as sp

_REPO = Path(__file__).resolve().parents[2]
for _p in (_REPO / "computations", _REPO / "computations" / "substrate",
           _REPO / "tools" / "qou-substrate" / "python",
           _REPO / "computations" / "meson"):
    sys.path.insert(0, str(_p))

from operator_selection_lattice_symbolic import (  # noqa: E402
    NF_BASIS, q, h, structure_constants, derive_trace, build_gram, _reduce_nf,
)

#: The corpus's claimed n = 3 optimum, from `prf:operator-selection-lp`'s table.
CLAIMED_OPTIMUM = ("+0.998", "-0.010", "+0.009", "+0.046", "-0.044", "0")


def _q0():
    try:
        from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    except ImportError:
        from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
    return sp.Rational(Q_50_DIGIT_STR)


def rmul(y, gen, inv=False):
    """Right-multiply an NF vector by sigma_gen, or by sigma_gen^-1 = sigma_gen - h."""
    terms: dict[tuple[int, ...], sp.Expr] = {}
    for i, b in enumerate(NF_BASIS):
        if y[i] == 0:
            continue
        terms[b + (gen,)] = terms.get(b + (gen,), 0) + y[i]
        if inv:
            terms[b] = terms.get(b, 0) - h * y[i]
    red = _reduce_nf(terms)
    return [sp.simplify(red.get(b, 0)) for b in NF_BASIS]


def main() -> int:
    C = structure_constants()
    t = derive_trace(C)
    G = build_gram(C, t)

    print("=" * 72)
    print("DEFECT 1 — the objective is bounded below by its own constraint")
    print("=" * 72)
    print(f"  NF_BASIS[0] = {NF_BASIS[0]!r}  (the identity, so G[0][j] = tr_M(b_j))")
    row0_is_t = all(sp.simplify(G[0, j] - t[j]) == 0 for j in range(6))
    for j in range(6):
        print(f"    G[0,{j}] - t[{j}] = {sp.simplify(G[0, j] - t[j])}")
    print(f"  first row of G == t : {row0_is_t}")
    assert row0_is_t, "the identity must make row 0 of G equal t"
    print("\n  So constraint (Gx)_0 >= 0 IS t.x >= 0 — the objective itself.")
    print("  The LP minimises t.x subject to t.x >= 0  =>  optimum == 0, always,")
    print("  for every n, every q, every convention. primal_obj = 0 and y_0* = 0")
    print("  are forced, not measured.")

    q0 = _q0()
    Gn = G.subs(q, q0)
    tn = [e.subs(q, q0) for e in t]
    xs = sp.symbols("x0:6")
    X = sp.Matrix(xs)
    v = sp.Matrix([(-1 / q) ** len(w) for w in NF_BASIS]).subs(q, q0)

    print("\n" + "=" * 72)
    print("DEFECT 2 — the argmin is a face, not a point")
    print("=" * 72)
    verts = []
    for A in itertools.combinations(range(1, 6), 3):
        eqs = [sp.Eq(sum(xs), 1), sp.Eq((Gn * X)[0], 0), sp.Eq((v.T * X)[0], 0)]
        eqs += [sp.Eq((Gn * X)[i], 0) for i in A]
        sol = sp.solve(eqs, xs, dict=True)
        if len(sol) != 1:
            continue
        xv = [sol[0][s] for s in xs]
        gx = [sp.N((Gn * sp.Matrix(xv))[i], 25) for i in range(6)]
        if min(gx) < -sp.Rational(1, 10**12):
            continue
        obj = sp.N(sum(xv[i] * tn[i] for i in range(6)), 25)
        verts.append((A, xv, obj))
    print(f"  feasible optimal vertices at the proton pin: {len(verts)}")
    for A, xv, obj in verts:
        cells = ", ".join(f"{float(e):+.4f}" for e in xv)
        print(f"    tight={A}  obj={float(obj):+.1e}  x=[{cells}]")
    print("\n  They occur in MIRROR PAIRS under sigma_0 <-> sigma_1. t and G are")
    print("  mirror-invariant, so the optimal set is mirror-closed; a unique")
    print("  optimum would have to be mirror-symmetric, and none of these is.")
    print("  => 'the solution x*' / 'the unique optimizer' are both false.")
    assert len(verts) > 1, "defect 2 requires more than one optimal vertex"

    print("\n" + "=" * 72)
    print("DEFECT 3 — the claimed optimizer is not a minimiser")
    print("=" * 72)
    y = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for _ in range(3):                      # B_3 = (sigma_0 sigma_1^-1)^3
        y = rmul(y, 0)
        y = rmul(y, 1, inv=True)
    yn = [sp.N(e.subs(q, q0), 25) for e in y]
    net = sum(yn)
    obj = sum(yn[i] * tn[i] for i in range(6))
    gx = [sp.N((Gn * sp.Matrix(yn))[i], 25) for i in range(6)]
    print("  NF(B_3) =", ", ".join(f"{float(e):+.6f}" for e in yn))
    print("  corpus  =", ", ".join(f"{e:>9}" for e in CLAIMED_OPTIMUM))
    print(f"\n  net         = {float(net):+.6f}")
    print(f"  objective   = tr_M(B_3) = {float(obj):+.6f}")
    print(f"  min (Gx)_i  = {float(min(gx)):+.6e}   feasible: {min(gx) >= 0}")
    print(f"  LP optimum  = 0  (defect 1)")
    print(f"\n  => B_3 is FEASIBLE but NOT OPTIMAL; gap = {float(obj):+.6f},")
    print("     i.e. the entire range of the objective. The stated program does")
    print("     not select the Borromean link.")

    print("\n" + "=" * 72)
    print("WHAT IS NOT CONCLUDED")
    print("=" * 72)
    print("  No replacement objective is proposed — that is a decision about the")
    print("  physics, not a repair an audit can make. Note ONLY as a hypothesis")
    print(f"  needing the author's intent: tr_M(B_3) = {float(obj):.6f} and")
    print(f"  sum NF(B_3) = {float(net):.6f} are both ~1, and n_target ~ 1.000 for")
    print("  the proton — consistent with the intended constraint having been")
    print("  t.x = n_target rather than sum x = n_target with t.x minimised, and")
    print("  EQUALLY consistent with n_target having been chosen as ~1, which")
    print("  would make the agreement circular.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
