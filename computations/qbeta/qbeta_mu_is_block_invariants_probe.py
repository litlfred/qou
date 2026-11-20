#!/usr/bin/env python3
"""
qbeta_mu_is_block_invariants_probe.py — qou-xzrj: every factor of mu is a named
invariant of the (2,1) block, and the Hecke quadratic factorises into two of them.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: computations/qbeta/qbeta_mu_normalisation_is_derived_probe.py
# Ref: folio/quantum-observable-universe/lean/QOU/MathlibExt/WenzlSchurElement.lean

WHERE THIS PICKS UP. mu = (-2/[3]_q) / y_(2,1)(z), with the 1/y_(2,1) DERIVED
(the block's pairing normalisation) and -2/[3]_q an identified constant. This
names the two remaining pieces.

## The `2` is the regular-representation multiplicity

On sl_2 = [H,H] only the (2,1) block contributes, and it contributes with
multiplicity dim = 2:

    chi_reg(x y) = 2 * chi^(2,1)(x y)     for x, y in [H,H]      [all 9 pairs]

So writing S for net's representative against the REGULAR form (rank 3/3 inside
sl_2), S = W/2 and S/dC = -1/[3]_q. The 2 is not a free constant: it is the
multiplicity, equivalently the block dimension, equivalently chi^(2,1)(1).

## The `[3]_q` is the block's SCHUR ELEMENT

Solving `tau = sum_lambda chi^lambda / c_lambda` for the canonical symmetrizing
trace `tau(T_w) = delta_{w,e}` (rank 3/3) gives

    c_(3) = (q^2+1)(q^2-q+1)(q^2+q+1)
    c_(2,1) = (q^2-q+1)(q^2+q+1)/q^2  =  [3]_q
    c_(1^3) = (q^2+1)(q^2-q+1)(q^2+q+1)/q^6

and c_(2,1) = [3]_q is exactly the hook formula: the hooks of (2,1) are 3, 1, 1,
so [3]_q [1]_q [1]_q = [3]_q.

## And the two combine into the Hecke quadratic

    c_(2,1) * y_(2,1)(z) = -(z^2 - h z - 1) = -P(z)                  [exact]

The Hecke quadratic FACTORISES into the block's Schur element times its Markov
weight. Hence

    mu = dim(V_(2,1)) / ( - c_(2,1) * y_(2,1)(z) ) = 2 / P(z).

Every factor is now a canonical invariant of one block: its dimension, its Schur
element, its Markov weight.

## CAREFUL — this is NOT the corpus's `schurElement`, and neither is it new

`QOU.MathlibExt.WenzlSchurElement.schurElement Q X lam` is the TWO-VARIABLE
Wenzl form, `Q^n(lam) * prod (1 - X Q^content)/(1 - Q^hook)`, and the corpus
builds `y_lambda` FROM it (`jonesMarkovCoeff = schurElement / wenzlNormalisation`).
What is computed here is the CLASSICAL one-variable symmetrizing-trace Schur
element c_lambda of H_3(q). Same concept, different variables and
normalisation. This probe does NOT claim they are equal under a substitution --
that is a separate question it does not settle -- and does NOT claim c_(2,1) =
[3]_q is a new fact: it is the standard hook formula, verified here rather than
cited, because the value is load-bearing for mu.

## What is still open

Every factor is named; the COMBINATION is still an identification. Nothing here
derives why net's representative should be `-dim/(c_lambda y_lambda)` times dC
rather than something else. Scope-(a); step 8's postulate is not closed.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

E = (0, 1, 2)
S0 = (1, 0, 2)
S1 = (0, 2, 1)


def compose(p, r):
    return tuple(p[r[i]] for i in range(3))


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


BASIS = [E, S0, S1, compose(S0, S1), compose(S1, S0), compose(compose(S0, S1), S0)]
IDX = {w: i for i, w in enumerate(BASIS)}
N = 6


def main() -> int:
    q, z = sp.symbols("q z", positive=True)
    h = q - 1 / q

    def qbr(n):
        return sum(q ** (n - 1 - 2 * k) for k in range(n))

    def left_gen(s):
        M = sp.zeros(N, N)
        for j, w in enumerate(BASIS):
            sw = compose(s, w)
            if length(sw) > length(w):
                M[IDX[sw], j] += 1
            else:
                M[IDX[w], j] += h
                M[IDX[sw], j] += 1
        return M

    L = [left_gen(S0), left_gen(S1)]
    ONE = sp.eye(N)
    REG = [ONE, L[0], L[1], L[0] * L[1], L[1] * L[0], L[0] * L[1] * L[0]]
    TRV = [sp.Integer(1), z, z, z**2, z**2, z * (h * z + 1)]

    def bv(i):
        v = sp.zeros(N, 1)
        v[i] = 1
        return v

    def tr_M(v):
        return sp.simplify(sum(v[i] * TRV[i] for i in range(N)))

    def net(v):
        return sp.simplify(sum(v[i] for i in range(N)))

    def mul(v, w):
        M = sp.zeros(N, N)
        for i in range(N):
            M += v[i] * REG[i]
        return sp.expand(M * w)

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi13(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i])
                               for i in range(N)))

    def chireg(v):
        return sp.simplify(sum(v[i] * sp.trace(REG[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((chireg(v) - chi3(v) - chi13(v)) / 2)

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 78)
    print(" qou-xzrj — mu is built from named (2,1)-block invariants")
    print("=" * 78)

    comms = [REG[i] * bv(j) - REG[j] * bv(i) for i in range(N) for j in range(N)]
    cb = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * bv(i) - REG[i] * L[0] * bv(0)),
                           sp.simplify(L[1] * bv(i) - REG[i] * L[1] * bv(0)))
          for i in range(N)]
    ctr = sp.Matrix.hstack(*zc).nullspace()
    Pm = sp.Matrix.hstack(*(list(ctr) + list(cb)))
    Pinv = Pm.inv()

    def comm_part(v):
        c = Pinv * v
        return sp.simplify(sum((c[3 + k] * cb[k] for k in range(3)),
                               sp.zeros(N, 1)))

    proton = sp.expand(L[0] * (L[1] - (h / 2) * ONE) * bv(0))
    neutron = sp.expand((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * bv(0))
    dC = comm_part(sp.expand(neutron - proton))

    # ---- 1. the 2 is the regular-rep multiplicity
    bad = [(k, l) for k in range(3) for l in range(3)
           if sp.simplify(sp.together(chireg(mul(cb[k], cb[l]))
                                      - 2 * chi21(mul(cb[k], cb[l])))) != 0]
    check("the_2_is_the_regular_rep_MULTIPLICITY_of_the_block", not bad,
          "chi_reg(xy) = 2 chi^(2,1)(xy) on all 9 pairs of the commutator basis "
          "-- only (2,1) contributes there, with multiplicity dim = 2")

    # ---- 2. S against the regular form, INSIDE sl_2 (rank-checked first)
    cs = sp.symbols("s0:3")
    Ssym = sp.expand(sum((cs[k] * cb[k] for k in range(3)), sp.zeros(N, 1)))
    sysS = [sp.Eq(sp.expand(chireg(mul(cb[k], Ssym))), sp.expand(net(cb[k])))
            for k in range(3)]
    As, bs = sp.linear_eq_to_matrix(sysS, list(cs))
    check("regular_form_system_inside_sl2_is_FULL_rank_3", As.rank() == 3,
          f"rank {As.rank()}/3 -- rank-checked BEFORE reading the output, which "
          f"is the lesson from the rank-4/6 trap on the previous probe")
    S = sp.expand(sum((sp.simplify(list(sp.linsolve((As, bs), list(cs)))[0][k])
                       * cb[k] for k in range(3)), sp.zeros(N, 1)))
    nz = next(i for i in range(N) if sp.simplify(dC[i]) != 0)
    rS = sp.simplify(sp.factor(S[nz] / dC[nz]))
    check("S_over_dC_is_minus_one_over_bracket_three",
          all(sp.simplify(sp.together(S[i] - rS * dC[i])) == 0 for i in range(N))
          and sp.simplify(sp.together(rS + 1 / qbr(3))) == 0,
          f"S/dC = {rS} = -1/[3]_q -- so after removing the multiplicity, one "
          f"reciprocal quantum integer remains")

    # ---- 3. [3]_q IS the block's Schur element
    a_, b_, c_ = sp.symbols("a b c")

    def tau(v):
        return sp.simplify(v[0])

    eqs = [sp.Eq(sp.expand(tau(bv(i))),
                 sp.expand(a_ * chi3(bv(i)) + b_ * chi21(bv(i))
                           + c_ * chi13(bv(i)))) for i in range(N)]
    Aq, Bq = sp.linear_eq_to_matrix(eqs, [a_, b_, c_])
    check("schur_element_system_is_FULL_rank_3", Aq.rank() == 3,
          f"rank {Aq.rank()}/3")
    inv = list(sp.linsolve((Aq, Bq), [a_, b_, c_]))[0]
    c21 = sp.simplify(1 / inv[1])
    check("bracket_three_IS_the_2_1_block_SCHUR_ELEMENT",
          sp.simplify(sp.together(c21 - qbr(3))) == 0,
          "c_(2,1) = [3]_q from tau = sum chi^lambda/c_lambda -- and that is the "
          "hook formula, hooks of (2,1) being 3,1,1 so [3][1][1] = [3]_q")

    # ---- 4. Schur element x Markov weight = the Hecke quadratic
    ys = sp.symbols("y3 y21 y13")
    eqs2 = [sp.Eq(sp.expand(tr_M(bv(i))),
                  sp.expand(ys[0] * chi3(bv(i)) + ys[1] * chi21(bv(i))
                            + ys[2] * chi13(bv(i)))) for i in range(N)]
    Ay, By = sp.linear_eq_to_matrix(eqs2, list(ys))
    Y21 = sp.simplify(list(sp.linsolve((Ay, By), list(ys)))[0][1])
    Pz = z**2 - h * z - 1
    check("HECKE_QUADRATIC_FACTORISES_into_schur_element_times_markov_weight",
          sp.simplify(sp.together(c21 * Y21 + Pz)) == 0,
          "c_(2,1) * y_(2,1)(z) = -(z^2 - h z - 1). The Hecke quadratic is the "
          "product of the block's two invariants")

    # ---- 5. so mu is entirely block invariants
    ycoef = sp.symbols("u0:6")
    yv = sp.Matrix(list(ycoef))
    sysY = [sp.Eq(sp.expand(tr_M(mul(bv(i), yv))),
                  sp.expand(net(comm_part(bv(i))))) for i in range(N)]
    Ay2, By2 = sp.linear_eq_to_matrix(sysY, list(ycoef))
    y0 = sp.Matrix([sp.simplify(s) for s in
                    list(sp.linsolve((Ay2, By2), list(ycoef)))[0]])
    mu = sp.simplify(y0[nz] / dC[nz])
    check("MU_IS_DIM_OVER_MINUS_SCHUR_TIMES_MARKOV",
          sp.simplify(sp.together(mu - 2 / (-c21 * Y21))) == 0,
          "mu = dim(V_(2,1)) / (-c_(2,1) y_(2,1)(z)) -- dimension, Schur "
          "element, Markov weight. All three are canonical invariants of the "
          "same block; none is a free constant")

    qv = Q_MP
    zDv = qv**3 / (qv**2 + 1)

    def num(e):
        return mp.mpf(str(sp.N(e.subs({q: sp.Float(str(qv), 60),
                                       z: sp.Float(str(zDv), 60)}), 50)))

    print(f"\n  at the proton pin, convention D:")
    print(f"    dim V_(2,1)   = 2")
    print(f"    c_(2,1)=[3]_q = {mp.nstr(num(c21), 16)}")
    print(f"    y_(2,1)(z_D)  = {mp.nstr(num(Y21), 16)}")
    print(f"    mu            = {mp.nstr(num(mu), 16)}")

    wb = WitnessBuilder("qbeta-mu-is-block-invariants", engine="sympy+mpmath")
    wb.set_description(
        "qou-xzrj: every factor of mu is a named invariant of the (2,1) block. "
        "The 2 is the regular-rep multiplicity (chi_reg = 2 chi^(2,1) on sl_2); "
        "[3]_q is the block's classical Schur element c_(2,1) (hooks 3,1,1); "
        "and c_(2,1)*y_(2,1)(z) = -(z^2 - h z - 1), so the Hecke quadratic "
        "factorises into the block's Schur element times its Markov weight. "
        "Hence mu = dim/(-c_(2,1) y_(2,1)). NOT the corpus's two-variable Wenzl "
        "schurElement -- different normalisation; no equality claimed. The "
        "COMBINATION remains an identification. Scope-(a).")
    wb.add_data("c_2_1_schur_element", str(sp.factor(c21)))
    wb.add_data("y_2_1_of_z", str(sp.factor(Y21)))
    wb.add_data("S_over_dC", str(rS))
    wb.add_data("mu", str(sp.factor(mu)))
    wb.add_data("mu_at_proton_pin_conventionD", fmt(num(mu)))
    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
