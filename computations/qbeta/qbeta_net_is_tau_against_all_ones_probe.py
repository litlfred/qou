#!/usr/bin/env python3
"""
qbeta_net_is_tau_against_all_ones_probe.py — qou-xzrj: `net` is the symmetrizing
trace paired against the ALL-ONES element, which derives the Schur-element factor
and reduces the whole gap to one identity between two canonical elements.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: computations/qbeta/qbeta_mu_is_block_invariants_probe.py

WHERE THIS PICKS UP. mu = dim / (-c_(2,1) y_(2,1)(z)) had every FACTOR named --
block dimension, Schur element, Markov weight -- but the COMBINATION was still
an identification. This derives most of it.

## `net` has an intrinsic form

The canonical symmetrizing trace `tau(T_w) = delta_{w,e}` picks the identity
coefficient. So pairing against the ALL-ONES element sums the coordinates, which
is exactly what `net` does:

    Omega := sum_w T_w  = [1,1,1,1,1,1]
    net(x) = tau(x * Omega)                              for every x      [N1]

Solved rather than assumed: the tau-representative system is rank 6/6, so Omega
is the UNIQUE such element, and the solve returns all-ones.

## which derives the Schur-element factor

With `tau = sum_lambda chi^lambda / c_lambda` and x in sl_2 (where only the
(2,1) block survives),

    net(x) = chi^(2,1)(x * Omega_(2,1)) / c_(2,1)

so the representative against the UNSCALED block form is `Omega_(2,1)/c_(2,1)`.
**The 1/c_(2,1) is not an identification at all -- it is the Schur element in
tau's own decomposition.**

## and reduces the gap to ONE identity

    comm(Omega) = -dim(V_(2,1)) * dC                                      [N3]

NAMING, corrected in the follow-up probe: this is Omega's COMMUTATOR part,
not its (2,1)-component. `chi^(2,1)(Omega) = 2h` is NONZERO, so the two
differ. The identity is unaffected.

exact, ratio exactly -2. So the entire remaining content of the representation is
this: **the all-ones element's traceless part is minus the block dimension times
Delta's traceless part.** Two explicit, canonical elements. No constants left.

## A GUESS THAT FAILED, kept because it was the obvious one

I first tried `Omega = sum_w T_w^{-1}`, reasoning that {T_{w^-1}} is the
tau-dual basis. It is NOT, in this normalisation: `net(x) = tau(x * sum T_w^{-1})`
FAILS on 5 of the 6 basis elements. The inverse-sum has coordinates like
`(q^2-q-1)^2/q^2`; the correct element is plain all-ones. Recorded because the
dual-basis reflex is exactly what makes this look like a one-line fact when it
is not, and because solving beat guessing here on the second attempt.

## What is still NOT derived

N3. Nothing here explains WHY Delta's commutator part is parallel to the
all-ones element's, nor why the ratio is the dimension. That is the whole gap
now. It is also NOT unique to Delta -- `e_minus` = w_0 aligns too (measured in
the companion probe), so any derivation must explain a small family, not a
singleton. Scope-(a); step 8's postulate is not closed.
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

    def bv(i):
        v = sp.zeros(N, 1)
        v[i] = 1
        return v

    def net(v):
        return sp.simplify(sum(v[i] for i in range(N)))

    def tau(v):
        return sp.simplify(v[0])

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
    print(" qou-xzrj — net is tau against the all-ones element")
    print("=" * 78)

    # --- N0: the guess that failed, kept as a control
    Ominv = sp.zeros(N, 1)
    for i in range(N):
        Ominv += sp.simplify(REG[i].inv() * bv(0))
    bad_inv = [NAMES[i] for i in range(N)
               if sp.simplify(sp.together(tau(mul(bv(i), Ominv))
                                          - net(bv(i)))) != 0]
    check("CONTROL_the_inverse_sum_is_NOT_the_representative", len(bad_inv) == 5,
          f"net(x) = tau(x * sum_w T_w^-1) FAILS on {len(bad_inv)} of 6 "
          f"({','.join(bad_inv)}). The dual-basis reflex is wrong here; kept "
          f"because it is the obvious guess and it cost a run")

    # --- N1: solve for the representative (rank-checked first)
    cs = sp.symbols("w0:6")
    Wv = sp.Matrix(list(cs))
    sysm = [sp.Eq(sp.expand(tau(mul(bv(i), Wv))), sp.expand(net(bv(i))))
            for i in range(N)]
    Am, bm = sp.linear_eq_to_matrix(sysm, list(cs))
    check("tau_representative_system_is_FULL_rank_6", Am.rank() == N,
          f"rank {Am.rank()}/6, so the representative is UNIQUE")
    Om = sp.Matrix([sp.simplify(s) for s in
                    list(sp.linsolve((Am, bm), list(cs)))[0]])
    allones = sp.Matrix([1] * N)
    check("N1_net_is_tau_paired_against_the_ALL_ONES_element",
          all(sp.simplify(Om[i] - 1) == 0 for i in range(N)),
          "Omega = sum_w T_w = [1,1,1,1,1,1] -- tau picks the identity "
          "coefficient, so pairing against all-ones sums the coordinates, "
          "which is what `net` does")

    # --- N2: the Schur element, from tau's own decomposition
    a_, b_, c_ = sp.symbols("a b c")
    eqs = [sp.Eq(sp.expand(tau(bv(i))),
                 sp.expand(a_ * chi3(bv(i)) + b_ * chi21(bv(i))
                           + c_ * chi13(bv(i)))) for i in range(N)]
    Aq, Bq = sp.linear_eq_to_matrix(eqs, [a_, b_, c_])
    check("schur_system_is_FULL_rank_3", Aq.rank() == 3, f"rank {Aq.rank()}/3")
    c21 = sp.simplify(1 / list(sp.linsolve((Aq, Bq), [a_, b_, c_]))[0][1])
    check("c_2_1_equals_bracket_three",
          sp.simplify(sp.together(c21 - qbr(3))) == 0,
          "c_(2,1) = [3]_q, the hook formula")

    # --- N3: Omega's (2,1) part vs dC
    comms = [REG[i] * bv(j) - REG[j] * bv(i) for i in range(N) for j in range(N)]
    cb = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * bv(i) - REG[i] * L[0] * bv(0)),
                           sp.simplify(L[1] * bv(i) - REG[i] * L[1] * bv(0)))
          for i in range(N)]
    ctr = sp.Matrix.hstack(*zc).nullspace()
    Pm = sp.Matrix.hstack(*(list(ctr) + list(cb)))
    Pinv = Pm.inv()

    def comm_part(v):
        cc = Pinv * v
        return sp.simplify(sum((cc[3 + k] * cb[k] for k in range(3)),
                               sp.zeros(N, 1)))

    proton = sp.expand(L[0] * (L[1] - (h / 2) * ONE) * bv(0))
    neutron = sp.expand((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * bv(0))
    dC = comm_part(sp.expand(neutron - proton))
    Om21 = comm_part(allones)
    nz = next(i for i in range(N) if sp.simplify(dC[i]) != 0)
    ratio = sp.simplify(sp.factor(Om21[nz] / dC[nz]))
    check("N3_all_ones_COMMUTATOR_part_is_MINUS_DIM_times_dC",
          all(sp.simplify(sp.together(Om21[i] - ratio * dC[i])) == 0
              for i in range(N)) and sp.simplify(ratio + 2) == 0,
          f"comm(Omega) = {ratio} * dC = -dim(V_(2,1)) * dC, exact (COMMUTATOR "
          f"part, not the (2,1)-component -- chi^(2,1)(Omega) = 2h != 0). "
          f"WHOLE remaining content -- two explicit canonical elements, no "
          f"constants left in it")

    # --- N4: the chain closes on the unscaled representative
    cs2 = sp.symbols("v0:3")
    Wsym = sp.expand(sum((cs2[k] * cb[k] for k in range(3)), sp.zeros(N, 1)))
    sysW = [sp.Eq(sp.expand(chi21(mul(cb[k], Wsym))), sp.expand(net(cb[k])))
            for k in range(3)]
    Aw, bw = sp.linear_eq_to_matrix(sysW, list(cs2))
    check("unscaled_representative_system_is_FULL_rank_3", Aw.rank() == 3,
          f"rank {Aw.rank()}/3")
    W = sp.expand(sum((sp.simplify(list(sp.linsolve((Aw, bw), list(cs2)))[0][k])
                       * cb[k] for k in range(3)), sp.zeros(N, 1)))
    check("N4_W_equals_Omega_21_over_the_schur_element",
          all(sp.simplify(sp.together(W[i] - Om21[i] / c21)) == 0
              for i in range(N)),
          "W = Omega_(2,1) / c_(2,1) -- so the 1/c_(2,1) in mu is NOT an "
          "identification: it is the Schur element in tau's own decomposition")

    qv = Q_MP
    print(f"\n  chain, at the proton pin:")
    print(f"    net(x) = tau(x * Omega),  Omega = sum_w T_w = all-ones")
    print(f"    tau    = sum_lambda chi^lambda / c_lambda")
    print(f"    =>  W  = Omega_(2,1) / c_(2,1)")
    print(f"    and Omega_(2,1) = -dim * dC          <-- the only step left")

    wb = WitnessBuilder("qbeta-net-is-tau-against-all-ones", engine="sympy+mpmath")
    wb.set_description(
        "qou-xzrj: `net` is the canonical symmetrizing trace paired against the "
        "ALL-ONES element Omega = sum_w T_w (rank 6/6, unique). With tau = "
        "sum_lambda chi^lambda/c_lambda this DERIVES the Schur-element factor in "
        "mu -- W = Omega_(2,1)/c_(2,1) -- rather than identifying it. The whole "
        "remaining gap collapses to one identity between explicit canonical "
        "elements: Omega_(2,1) = -dim(V_(2,1)) * dC. Also records a failed "
        "guess: sum_w T_w^{-1} is NOT the representative (fails 5 of 6). "
        "Scope-(a); step 8 not closed.")
    wb.add_data("Omega", [str(sp.simplify(x)) for x in allones])
    wb.add_data("Omega_21_over_dC", str(ratio))
    wb.add_data("c_2_1", str(sp.factor(c21)))
    wb.add_data("inverse_sum_failures", str(len(bad_inv)))
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
