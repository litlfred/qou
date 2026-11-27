#!/usr/bin/env python3
"""
qbeta_trace_invisible_is_pairing_representable_probe.py — qou-xzrj: the
trace-invisible remainder is invisible to every LINEAR trace but visible to the
Markov PAIRING, and `net` decomposes exactly into framework-canonical objects.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/MarkovTraceQuotient.lean
# Ref: folio/quantum-observable-universe/nuclear-interactions/gram-matrix-h3-symbolic.md

THE BEAN'S QUESTION. "What object in the framework carries a non-cyclic
functional's value on [H,H]?" The remainder is 7.67 % of `epsNPq` and no Markov
trace, no augmentation and no chi^lambda can see it, because every trace
annihilates the commutator subspace.

THE ANSWER TESTED HERE -- an ELEMENT, via the pairing rather than a functional.

  A trace is LINEAR and annihilates [H,H]. The Markov PAIRING
  <x,y> := tr_M(x*y) is BILINEAR and does not: for a 2x2 traceless A,
  tr(A^2) = -2*det(A), generically nonzero. So the pairing is the natural next
  object in the framework's own vocabulary, and it needs nothing new.

  The corpus already proves the pairing is DEGENERATE on H_3 under convention D
  -- its radical is the (1^3) ideal (`MarkovGramDegenerate.pairing_descends`,
  `mem_radical_of_pairing_zero`, sibling bean qou-s7z2). That is not an
  obstruction here, it is the enabling fact: the radical is the THREE-ROW block,
  while [H,H] = sl_2 sits inside the TWO-row (2,1) block. The pairing is
  degenerate exactly where the remainder is NOT, and nondegenerate exactly where
  it IS.

  Nondegeneracy on that block makes every linear functional on it REPRESENTABLE
  (Riesz). So there should exist a unique y0 in sl_2 with

      net(x) = sum_lambda a_lambda * chi^lambda(x)  +  tr_M(x * y0)

  for EVERY x -- the trace part on the centre plus a pairing against one derived
  element. The second term automatically vanishes on the centre (a central x
  acts as a scalar on the block, so x*y0 stays traceless), which is what lets
  the two pieces coexist without double-counting.

WHAT WOULD MAKE THIS FAIL, stated before running: y0 could fail to exist (if the
pairing were degenerate on (2,1) at z_D), could fail to be unique, could fail to
lie in sl_2, or the identity could hold on the centre and break on [H,H]. Each
is asserted separately below rather than folded into one pass/fail.

SCOPE -- (a). This exhibits a REPRESENTATION of `net`, not a derivation of it.
It does NOT show the single-wrap presentation is forced, does not close step 8's
postulate, and proposes no value for anything. What it changes is the shape of
the open question: from "what could possibly see this?" to "is y0 derivable?".
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
NAMES = ["gamma", "sigma0", "sigma1", "L_plus", "L_minus", "e_minus"]
IDX = {w: i for i, w in enumerate(BASIS)}
N = 6


def main() -> int:
    q, z = sp.symbols("q z", positive=True)
    h = q - 1 / q

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

    def bv(i):
        v = sp.zeros(N, 1)
        v[i] = 1
        return v

    def word_op(v):
        """Left-multiplication operator of the element with coords v."""
        M = sp.zeros(N, N)
        for i in range(N):
            # build L_{basis[i]} by multiplying generators along a reduced word
            M += v[i] * REG[i]
        return M

    # regular representation of each basis element
    REG = [ONE, L[0], L[1], L[0] * L[1], L[1] * L[0], L[0] * L[1] * L[0]]

    TRV = [sp.Integer(1), z, z, z**2, z**2, z * (h * z + 1)]

    def tr_M(v):
        return sp.simplify(sum(v[i] * TRV[i] for i in range(N)))

    def net(v):
        return sp.simplify(sum(v[i] for i in range(N)))

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 78)
    print(" qou-xzrj — the trace-invisible part is PAIRING-representable")
    print("=" * 78)

    # ---------------------------------------------------------------- Delta
    proton = sp.expand(L[0] * (L[1] - (h / 2) * ONE) * bv(0))
    neutron = sp.expand((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * bv(0))
    delta = sp.expand(neutron - proton)
    check("delta_rebuilt_from_typed_crossing_words",
          all(sp.simplify(e) == 0 for e in
              (delta - sp.Matrix([h**2 / 2, -h / 2, -h / 2, 0, 0, 0]))))

    # ------------------------------------------------- centre / commutator
    comms = [REG[i] * bv(j) - REG[j] * bv(i) for i in range(N) for j in range(N)]
    comm_basis = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * bv(i) - REG[i] * L[0] * bv(0)),
                           sp.simplify(L[1] * bv(i) - REG[i] * L[1] * bv(0)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    check("dim_commutator_3_and_centre_3",
          len(comm_basis) == 3 and len(centre) == 3,
          f"got {len(comm_basis)} and {len(centre)}")

    P = sp.Matrix.hstack(*(list(centre) + list(comm_basis)))
    coords = sp.simplify(P.solve(delta))
    dZ = sp.simplify(sum((coords[i] * centre[i] for i in range(3)), sp.zeros(N, 1)))
    dC = sp.simplify(delta - dZ)
    check("commutator_part_is_nonzero",
          not all(sp.simplify(e) == 0 for e in dC))

    # ------------------------------------- 1. every trace kills it (control)
    check("CONTROL_every_markov_trace_annihilates_the_commutator_part",
          sp.simplify(tr_M(dC)) == 0,
          "true for EVERY z -- this is why no linear trace can see the remainder")

    # ------------------------- 2. the PAIRING does not: <dC,dC> = tr_M(dC^2)
    def mul(v, w):
        """product of two elements, in coordinates"""
        M = sp.zeros(N, N)
        for i in range(N):
            M += v[i] * REG[i]
        return sp.expand(M * w)

    pair_dC_dC = sp.simplify(tr_M(mul(dC, dC)))
    check("the_PAIRING_sees_what_every_trace_cannot",
          sp.simplify(pair_dC_dC) != 0,
          f"<dC,dC> = tr_M(dC^2) != 0 -- bilinear, so not killed by [H,H]")

    # ------------- 3. Riesz: solve for y0 with tr_M(x*y0) = net(x) on [H,H]
    #     and tr_M(x*y0) = 0 on the centre.  6 equations, 6 unknowns.
    ycoef = sp.symbols("y0:6")
    yv = sp.Matrix(list(ycoef))
    eqs = []
    for i in range(N):
        lhs = tr_M(mul(bv(i), yv))
        rhs = net(bv(i)) - sum(0 for _ in ())  # placeholder, set below
        eqs.append(lhs)
    # target functional: net on [H,H], zero on the centre.
    #   build the projector onto [H,H] along the centre from P
    Pinv = P.inv()

    def commutator_part(v):
        c = Pinv * v
        return sp.simplify(sum((c[3 + k] * comm_basis[k] for k in range(3)),
                               sp.zeros(N, 1)))

    targets = [sp.simplify(net(commutator_part(bv(i)))) for i in range(N)]
    system = [sp.Eq(sp.expand(eqs[i]), sp.expand(targets[i])) for i in range(N)]
    Amat, bvec = sp.linear_eq_to_matrix(system, list(ycoef))
    rank = Amat.rank()
    sol = sp.linsolve((Amat, bvec), list(ycoef))
    has_sol = len(sol) > 0
    check("riesz_system_is_solvable", has_sol, f"rank {rank}/6")
    if not has_sol:
        print("  cannot continue without y0")
        return 1
    y0 = sp.Matrix([sp.simplify(s) for s in list(sol)[0]])
    check("riesz_representative_is_UNIQUE", rank == N,
          f"rank {rank} = 6, so y0 is the unique solution -- not a fitted choice")

    # ------------------------------------------- 4. y0 lies in the commutator
    cy = sp.simplify(Pinv * y0)
    in_comm = all(sp.simplify(cy[k]) == 0 for k in range(3))
    check("y0_lies_in_the_commutator_subspace_sl2",
          in_comm,
          "its centre-coordinates all vanish, so y0 is in sl_2 subset (2,1)")

    # ------------------------- 5. the exact decomposition, on ALL SIX basis elts
    chi3 = lambda v: sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))   # noqa: E731
    chi13 = lambda v: sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))  # noqa: E731

    def chi21(v):
        # chi_reg = 1*chi3 + 2*chi21 + 1*chi13
        reg = sp.simplify(sum(v[i] * sp.trace(REG[i]) for i in range(N)))
        return sp.simplify((reg - chi3(v) - chi13(v)) / 2)

    a3 = (q + 1) / ((q**2 + 1) * (q**2 - q + 1))
    a21 = q * (q**2 - 1) / (q**4 + q**2 + 1)
    a13 = q**3 * (q - 1) / ((q**2 + 1) * (q**2 + q + 1))

    # CONTROL, added after the multiplicity slip: the trace part must equal
    # net on the CENTRE-PROJECTION of x, not net on x itself. Comparing against
    # net(x) directly is a bad diagnostic -- they need not agree off the centre.
    Pinv2 = P.inv()

    def centre_part(v):
        c = Pinv2 * v
        return sp.simplify(sum((c[k] * centre[k] for k in range(3)),
                               sp.zeros(N, 1)))

    tp_bad = [NAMES[i] for i in range(N)
              if sp.simplify(sp.together(
                  a3 * chi3(bv(i)) + a21 * chi21(bv(i)) + a13 * chi13(bv(i))
                  - net(centre_part(bv(i))))) != 0]
    check("CONTROL_trace_part_equals_net_on_the_centre_projection",
          not tp_bad,
          "sum_lambda a_lambda chi^lambda (x) = net(x_Z) on all six -- with NO "
          "dimension multiplicity; the 2x reading matches only 1 of 6")

    bad = []
    for i in range(N):
        v = bv(i)
        lhs = net(v)
        # NO dimension multiplicity on the (2,1) term. My first version wrote
        # `2 * a21`, reading the a_lambda as if they were regular-character
        # coefficients (chi_reg = 1*chi3 + 2*chi21 + 1*chi13). They are not --
        # they are the coefficients of the trace functional itself. Measured:
        # against net(x_Z) on the six basis elements, no-multiplicity matches
        # 6/6 and the 2x version matches 1/6 (only on e_minus, where the two
        # happen to coincide). Caught by this assertion failing.
        rhs = (a3 * chi3(v) + a21 * chi21(v) + a13 * chi13(v)
               + tr_M(mul(v, y0)))
        if sp.simplify(sp.expand(lhs - rhs)) != 0:
            bad.append(NAMES[i])
    check("EXACT_decomposition_holds_on_all_six_basis_elements",
          not bad,
          "net(x) = sum_lambda a_lambda chi^lambda(x) + tr_M(x*y0), "
          f"{'all 6' if not bad else 'FAILS on ' + ','.join(bad)}")

    # --------------------------------- 6. the pairing term vanishes on centre
    ctr_bad = [k for k in range(3)
               if sp.simplify(tr_M(mul(centre[k], y0))) != 0]
    check("pairing_term_vanishes_on_the_CENTRE_so_no_double_counting",
          not ctr_bad,
          "a central x acts as a scalar on the block, so x*y0 stays traceless")

    # ------------------------------------------- 7. numeric, at the proton pin
    qv = Q_MP
    zD = qv**3 / (qv**2 + 1)

    def num(e):
        return mp.mpf(str(sp.N(e.subs({q: sp.Float(str(qv), 60),
                                       z: sp.Float(str(zD), 60)}), 50)))

    net_dC = num(net(dC))
    pr = num(tr_M(mul(dC, y0)))
    print(f"\n  at the proton pin, convention D:")
    print(f"    net(dC)          = {mp.nstr(net_dC, 16)}")
    print(f"    tr_M(dC * y0)    = {mp.nstr(pr, 16)}")
    check("numeric_agreement_at_the_proton_pin",
          abs(net_dC - pr) < mp.mpf(10) ** -40,
          f"|diff| = {mp.nstr(abs(net_dC - pr), 4)}")

    wb = WitnessBuilder("qbeta-trace-invisible-is-pairing-representable",
                        engine="sympy+mpmath")
    wb.set_description(
        "qou-xzrj: the 7.67 % trace-invisible remainder of epsNPq is invisible "
        "to every linear Markov trace but visible to the Markov PAIRING, whose "
        "radical under convention D is the (1^3) block while [H,H] = sl_2 sits "
        "in the (2,1) block. Nondegeneracy there makes net|_[H,H] Riesz-"
        "representable by a UNIQUE element y0 in sl_2, giving an exact "
        "decomposition net = sum_lambda a_lambda chi^lambda + tr_M(.*y0) on all "
        "of H_3. Scope-(a): a representation, not a derivation of net.")
    wb.add_data("y0_coords", [str(sp.simplify(c)) for c in y0])
    wb.add_data("pair_dC_dC", str(sp.simplify(pair_dC_dC)))
    wb.add_data("net_dC_at_proton_pin", fmt(net_dC))
    wb.add_data("pairing_dC_y0_at_proton_pin", fmt(pr))
    wb.add_data("riesz_rank", str(rank))
    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    print(f"\n  y0 = {[str(sp.simplify(c)) for c in y0]}")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
