#!/usr/bin/env python3
"""
qbeta_mu_normalisation_is_derived_probe.py — qou-xzrj: mu splits into a DERIVED
factor and a z-free identified constant. All of mu's convention-dependence is
the derived half.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: computations/qbeta/qbeta_mu_closed_form_and_delta_alignment_probe.py

WHERE THIS PICKS UP. mu = -dim(V_(2,1)) / ([3]_q y_(2,1)(z)) was reached by
IDENTIFICATION -- recognising the factors in a solve output. That left the
honest question: is any of it FORCED, or is the whole closed form a lucky
reading?

THE SPLIT, and it is not 50/50 in importance.

On [H,H] = sl_2 the Markov trace collapses to one block, so for x, w in [H,H]

    tr_M(x w) = y_(2,1)(z) * chi^(2,1)(x w)                    [all 9 pairs]

i.e. the Markov PAIRING is the standard trace form of the block, scaled by that
block's own Markov weight. Nothing is chosen there: it is what the Wedderburn
decomposition gives.

So define W as the representative of net|_[H,H] against the UNSCALED trace form
chi^(2,1)(x w). Then y0 = W / y_(2,1) forced, and

    mu  =  (W / dC) / y_(2,1)(z),         W / dC = -2/[3]_q,   W is z-FREE.

  * the 1/y_(2,1)(z) factor is **DERIVED** -- it is the pairing's normalisation
    on the block, not an identification;
  * the -2/[3]_q residual is z-free and is **still an identification**.

**Consequence: ALL of mu's convention-dependence is now derived.** Whatever is
left to explain is a pure-q constant that does not move with the Markov
parameter. That is what the tranche buys; it does not close step 8.

METHOD NOTE -- an under-determined system that silently returned symbols.
Solving for W over all of H_3 (6 unknowns) gives **rank 4/6**, because
chi^(2,1)(x w) annihilates both 1-dimensional blocks: the pairing cannot see
them, so two coordinates of W are free. The first run of this analysis did
exactly that and produced a "ratio" still containing the free symbols w4, w5 --
an answer-shaped expression that was not an answer. W must be solved INSIDE
sl_2 (3 unknowns against the 3 commutator basis vectors), which is rank 3/3.
Recorded because a rank check is the cheap guard and I did not run it first.
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

    def chi21(v):
        reg = sp.simplify(sum(v[i] * sp.trace(REG[i]) for i in range(N)))
        return sp.simplify((reg - chi3(v) - chi13(v)) / 2)

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 78)
    print(" qou-xzrj — which half of mu is DERIVED")
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

    ys = sp.symbols("y3 y21 y13")
    eqs = [sp.Eq(sp.expand(tr_M(bv(i))),
                 sp.expand(ys[0] * chi3(bv(i)) + ys[1] * chi21(bv(i))
                           + ys[2] * chi13(bv(i)))) for i in range(N)]
    Ay, by = sp.linear_eq_to_matrix(eqs, list(ys))
    Y21 = sp.simplify(list(sp.linsolve((Ay, by), list(ys)))[0][1])

    # -------- 1. the pairing on [H,H] IS the block trace form, scaled by y
    bad = [(k, l) for k in range(3) for l in range(3)
           if sp.simplify(sp.together(tr_M(mul(cb[k], cb[l]))
                                      - Y21 * chi21(mul(cb[k], cb[l])))) != 0]
    check("the_markov_pairing_on_HH_IS_the_block_trace_form_times_y_2_1",
          not bad,
          "tr_M(xw) = y_(2,1) * chi^(2,1)(xw) on all 9 ordered pairs of the "
          "commutator basis -- Wedderburn, nothing chosen")

    # -------- 2. W: representative against the UNSCALED form, solved IN sl_2
    cs = sp.symbols("c0:3")
    Wsym = sp.expand(sum((cs[k] * cb[k] for k in range(3)), sp.zeros(N, 1)))
    sysW = [sp.Eq(sp.expand(chi21(mul(cb[k], Wsym))), sp.expand(net(cb[k])))
            for k in range(3)]
    Aw, bw = sp.linear_eq_to_matrix(sysW, list(cs))
    rankW = Aw.rank()
    check("W_system_restricted_to_sl2_has_FULL_rank_3", rankW == 3,
          f"rank {rankW}/3. Solved over all of H_3 it is rank 4/6 -- "
          f"chi^(2,1)(x w) annihilates both 1-dim blocks, so two coordinates "
          f"stay free and the 'answer' still contains symbols. Rank check "
          f"first; I did not, on the first pass")
    W = sp.expand(sum((sp.simplify(list(sp.linsolve((Aw, bw), list(cs)))[0][k])
                       * cb[k] for k in range(3)), sp.zeros(N, 1)))

    check("W_is_z_FREE_so_all_convention_dependence_sits_in_the_normalisation",
          all(sp.simplify(sp.diff(sp.together(W[i]), z)) == 0 for i in range(N)),
          "the unscaled representative carries no Markov parameter at all")

    # -------- 3. W parallel to dC, ratio = -2/[3]_q
    proton = sp.expand(L[0] * (L[1] - (h / 2) * ONE) * bv(0))
    neutron = sp.expand((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * bv(0))
    dC = comm_part(sp.expand(neutron - proton))
    nz = next(i for i in range(N) if sp.simplify(dC[i]) != 0)
    ratio = sp.simplify(sp.factor(W[nz] / dC[nz]))
    check("W_is_parallel_to_dC_with_ratio_minus_two_over_bracket_three",
          all(sp.simplify(sp.together(W[i] - ratio * dC[i])) == 0
              for i in range(N))
          and sp.simplify(sp.together(ratio + 2 / qbr(3))) == 0,
          f"W/dC = {ratio} = -2/[3]_q -- z-free, and STILL AN IDENTIFICATION")

    # -------- 4. and mu is exactly the quotient
    ycoef = sp.symbols("u0:6")
    yv = sp.Matrix(list(ycoef))
    sysY = [sp.Eq(sp.expand(tr_M(mul(bv(i), yv))),
                  sp.expand(net(comm_part(bv(i))))) for i in range(N)]
    Ay2, by2 = sp.linear_eq_to_matrix(sysY, list(ycoef))
    y0 = sp.Matrix([sp.simplify(s) for s in
                    list(sp.linsolve((Ay2, by2), list(ycoef)))[0]])
    mu = sp.simplify(y0[nz] / dC[nz])
    check("MU_SPLITS_derived_normalisation_times_z_free_identified_constant",
          sp.simplify(sp.together(mu - ratio / Y21)) == 0,
          "mu = (-2/[3]_q) / y_(2,1)(z). The 1/y_(2,1) is DERIVED (the block's "
          "pairing normalisation); only the z-free -2/[3]_q is identified. So "
          "ALL of mu's convention-dependence is now derived")

    qv = Q_MP
    zDv = qv**3 / (qv**2 + 1)

    def num(e):
        return mp.mpf(str(sp.N(e.subs({q: sp.Float(str(qv), 60),
                                       z: sp.Float(str(zDv), 60)}), 50)))

    print(f"\n  at the proton pin, convention D:")
    print(f"    derived factor 1/y_(2,1) = {mp.nstr(1 / num(Y21), 16)}")
    print(f"    identified  -2/[3]_q     = {mp.nstr(num(ratio), 16)}")
    print(f"    mu                       = {mp.nstr(num(mu), 16)}")

    wb = WitnessBuilder("qbeta-mu-normalisation-is-derived", engine="sympy+mpmath")
    wb.set_description(
        "qou-xzrj: mu = (-2/[3]_q) / y_(2,1)(z) splits into a DERIVED factor "
        "and a z-free identified constant. On [H,H] the Markov pairing is the "
        "(2,1) block's trace form scaled by that block's own Markov weight "
        "(verified on all 9 ordered pairs), so the 1/y_(2,1) is forced by "
        "Wedderburn rather than identified. The residual -2/[3]_q is z-free. "
        "Consequence: ALL of mu's convention-dependence is derived; what "
        "remains identified is a pure-q constant. Scope-(a); step 8 not closed.")
    wb.add_data("W_over_dC", str(ratio))
    wb.add_data("y_2_1_of_z", str(sp.factor(Y21)))
    wb.add_data("mu", str(sp.factor(mu)))
    wb.add_data("W_rank_in_sl2", str(rankW))
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
