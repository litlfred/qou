#!/usr/bin/env python3
"""
qbeta_where_the_trace_invisible_part_lives_probe.py — qou-xzrj: the 7.67 % lives
in the TRACELESS part of the 2-dimensional block, and convention D does NOT
quotient it away.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: computations/qbeta/qbeta_which_algebra_the_decay_channel_lives_in_probe.py
# Ref: computations/qbeta/qbeta_phase_block_resolution_probe.py

WHAT qou-xzrj ASKS. Step 8's postulate was narrowed to the 7.67 % of `epsNPq`
that no trace can see — the value of the coordinate sum on Delta's commutator
component dC. The bean asks what object carries it. This locates it exactly, and
answers the question the TL result made urgent: does convention D remove it?

THE STRUCTURE, and it unifies four facts that arrived separately. For a split
semisimple algebra (+)M_{n_i}, the commutator subspace is (+)sl_{n_i}, and
sl_1 = 0 — so in H_3(q) = R (+) M_2 (+) R the ENTIRE commutator subspace sits
inside the 2-dimensional block. Measured: e_(3) and e_(1,1,1) both annihilate
[H,H], e_(2,1) acts on it as the identity, and dim [H,H] = 3 = dim sl_2.

Consequences, each verified rather than inferred:

  * dC lies entirely in the (2,1) block;
  * Delta's (2,1)-component IS dC exactly — which is the same statement as
    chi^(2,1)(Delta) = 0, since a block component is traceless precisely when its
    character vanishes. The two facts were found separately and are one fact;
  * the floor is -h * y_(2,1)(1), the (2,1) weight — no longer a coincidence of
    labels but the weight of the block the remainder lives in;
  * so Delta splits as: two 1-dimensional blocks carrying everything a trace can
    see, plus a TRACELESS element of the 2-dimensional block carrying everything
    a trace cannot.

THE ANSWER TO THE URGENT QUESTION. Convention D quotients by the (1,1,1) block.
dC is in the (2,1) block, so e_(1,1,1) . dC = 0 and dC is NONZERO: the
trace-invisible remainder SURVIVES the Temperley-Lieb quotient intact. It is not
what D removes. So qou-xzrj stays live under the canonical convention, and the
7.67 % cannot be disposed of by appealing to the quotient.

NOT CLAIMED: that anything in the framework's vocabulary evaluates a traceless
element of a 2-dimensional block. That is precisely what remains open — this
says where to look, not what to find.

NO fit, NO wiring. Exact symbolic in q. Scope-(a).
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

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS, LEFT, L, R, ONE, basis_vec, vec, net, reg_char, length,
)

set_compute_dps(50)

LABELS = ["(3)", "(2,1)", "(1,1,1)"]
DIMS = [1, 2, 1]


def is_zero(M):
    """`.is_zero_matrix` returns None when sympy cannot decide; decide entrywise."""
    return all(sp.simplify(sp.expand(e)) == 0 for e in M)


def main() -> int:
    w = WitnessBuilder("qbeta-where-trace-invisible-part-lives", engine="sympy+mpmath")
    w.set_description(
        "The trace-invisible 7.67 % of epsNPq lives in the traceless part of "
        "the 2-dimensional block, and survives the convention-D Temperley-Lieb "
        "quotient intact."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]

    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    comm = sp.Matrix.hstack(*[LEFT[i] * basis_vec(j) - LEFT[j] * basis_vec(i)
                              for i in range(N) for j in range(N)]).columnspace()
    check("commutator_subspace_is_three_dimensional_equal_to_dim_sl2",
          len(comm) == 3,
          "(H_3 = R + M_2 + R, so [H,H] = sl_1 + sl_2 + sl_1 = sl_2)")

    cf = sp.symbols("c0 c1 c2")
    E = []
    for lam in range(3):
        gen = sum((cf[i] * centre[i] for i in range(3)), sp.zeros(N, 1))
        s = sp.solve([sp.Eq(CHI[mu](gen), DIMS[mu] if mu == lam else 0)
                      for mu in range(3)], cf, dict=True)[0]
        E.append(sp.simplify(sum((s[cf[i]] * centre[i] for i in range(3)),
                                 sp.zeros(N, 1))))
    Lp = [sum((E[k][i] * LEFT[i] for i in range(N)), sp.zeros(N, N)) for k in range(3)]

    check("the_ENTIRE_commutator_subspace_sits_in_the_2_dim_block",
          all(is_zero(Lp[0] * c) for c in comm)
          and all(is_zero(Lp[2] * c) for c in comm)
          and all(is_zero(Lp[1] * c - c) for c in comm),
          "(e_(3) and e_(1,1,1) annihilate [H,H]; e_(2,1) acts as the identity)")

    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("delta_reproduces_the_corpus_NF_vector",
          is_zero(delta - vec(h**2 / 2, -h / 2, -h / 2, 0, 0, 0)))

    P = sp.Matrix.hstack(*(list(centre) + list(comm)))
    co = sp.simplify(P.solve(delta))
    dZ = sp.simplify(sum((co[i] * centre[i] for i in range(3)), sp.zeros(N, 1)))
    dC = sp.simplify(delta - dZ)
    check("dC_is_nonzero", not is_zero(dC))
    check("dC_lies_entirely_in_the_2_dim_block",
          is_zero(Lp[1] * dC - dC) and is_zero(Lp[0] * dC) and is_zero(Lp[2] * dC))

    check("deltas_2_dim_component_IS_dC_exactly",
          is_zero(Lp[1] * delta - dC),
          "(so Delta's (2,1) part is TRACELESS — the same fact as "
          "chi^(2,1)(Delta) = 0, found separately and now unified)")
    check("and_chi_2_1_of_delta_vanishes_CROSS_REFERENCE",
          sp.simplify(chi21(delta)) == 0)

    # THE question the TL result made urgent
    check("dC_SURVIVES_the_convention_D_TL_quotient",
          is_zero(Lp[2] * dC) and not is_zero(dC),
          "(D quotients the (1,1,1) block; dC is in (2,1), so the "
          "trace-invisible remainder is NOT what D removes — qou-xzrj stays "
          "live under the canonical convention)")

    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    floor = sp.factor(sp.simplify(net(dC)))
    ys = sp.symbols("y0 y1 y2")
    TRz = [sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(1),
           sp.Integer(1), (h + 1)]                     # Ocneanu at z = 1
    solY = sp.solve([sp.Eq(sum(ys[k] * CHI[k](basis_vec(i)) for k in range(3)),
                           TRz[i]) for i in (0, 1, 3)], ys, dict=True)[0]
    check("the_floor_is_minus_h_times_the_2_dim_weight_at_z_equals_one",
          sp.simplify(floor + h * solY[ys[1]]) == 0,
          "(so -h*y_(2,1)(1) is not a coincidence of labels: it is the weight "
          "of the very block the remainder lives in)")

    w.add_data("dim_commutator", len(comm))
    w.add_data("block_containing_the_remainder", "(2,1) — the 2-dimensional one")
    w.add_data("floor_symbolic", str(floor))
    w.add_data("floor_at_q0", fmt(ev(floor)))
    w.add_data("epsNPq_at_q0", fmt(ev(sp.simplify(net(delta)))))
    w.add_data("fraction_trace_invisible",
               fmt(abs(ev(floor)) / abs(ev(sp.simplify(net(delta))))))
    w.add_data("survives_TL_quotient", True)
    w.add_data("markov_convention", "convention-free — no z is specialised")
    w.add_data("assertion_notes", notes)

    verdict = (
        "The trace-invisible remainder lives in the TRACELESS part of the "
        "2-dimensional block, and this unifies four facts that arrived "
        "separately. For H_3 = R + M_2 + R the commutator subspace is "
        "sl_1 + sl_2 + sl_1 = sl_2, so [H,H] sits ENTIRELY in the (2,1) block "
        "(measured: the two 1-dim idempotents annihilate it, e_(2,1) is the "
        "identity on it, dim = 3). Hence dC is in that block; Delta's "
        "(2,1)-component IS dC exactly, which is the SAME statement as "
        "chi^(2,1)(Delta) = 0; and the floor -h*y_(2,1)(1) carries that block's "
        "own weight rather than coincidentally sharing its label. So Delta "
        "splits as two 1-dimensional blocks carrying everything a trace can see, "
        "plus a traceless element of the 2-dimensional block carrying everything "
        "it cannot. AND THE URGENT QUESTION: convention D quotients the (1,1,1) "
        "block, dC is in (2,1), so the remainder SURVIVES the Temperley-Lieb "
        "quotient intact -- it is not what D removes, and qou-xzrj stays live "
        "under the canonical convention. NOT claimed: that anything in the "
        "framework's vocabulary evaluates a traceless element of a 2-dimensional "
        "block. That is what remains open; this says where to look."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
