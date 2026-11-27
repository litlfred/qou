#!/usr/bin/env python3
"""
qbeta_riesz_element_is_structurally_forced_probe.py — qou-xzrj: the Riesz
element y0 is not an arbitrary solve output. Its shape is z-free and its poles
are exactly where its own block dies.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: computations/qbeta/qbeta_trace_invisible_is_pairing_representable_probe.py
# Ref: folio/quantum-observable-universe/nuclear-interactions/gram-matrix-h3-symbolic.md

WHERE THIS PICKS UP. The companion probe (12/12) shows the trace-invisible part
of `epsNPq` is Riesz-representable by a UNIQUE y0 in sl_2, giving

    net(x) = sum_lambda a_lambda chi^lambda(x) + tr_M(x * y0)   exactly.

Unique is not the same as derived. A linear solve returning one answer says the
answer is determined by the inputs; it says nothing about whether the object has
an independent characterisation. This probe asks whether y0 does.

PREDICTIONS, STATED BEFORE RUNNING (they are not all confirmed -- see the
assertion notes for which failed):

  P1  y0 is proportional to the z-FREE vector [0, 1, 1, h, h, -2], so all of
      its Markov-parameter dependence is an overall scalar. PREDICTED HOLD.

      *** SIGN CORRECTED. *** I first wrote the last component as +2, having
      factored dC by hand, and the assertion FAILED. The correct direction is
      [0, 1, 1, h, h, -2]. The claim survives the correction; my arithmetic did
      not. Kept visible because a hand-factorisation that "looked right" is
      exactly what an assertion is for.
  P2  that scalar's denominator factors as
          D = (z - q)(q z + 1)(q^2 - q + 1)(q^2 + q + 1)
            = q (q^4 + q^2 + 1) (z^2 - h z - 1),
      i.e. the HECKE QUADRATIC sigma^2 = h sigma + 1 read in z, times the
      (2,1) block's own denominator. PREDICTED HOLD (derived by factoring).
  P3  hence y0's only poles are z = q and z = -1/q -- and those are exactly the
      two roots of the H_3 Markov Gram determinant that annihilate the (2,1)
      block, per the multiplicity law measured in PR #5864. So y0 blows up
      precisely where the pairing that defines it degenerates on the very block
      it lives in. PREDICTED HOLD, and if it does it is a forcing rather than a
      coincidence.
  P4  y0 proportional to dC itself. GENUINELY UNCERTAIN when written -- the
      commutator space is 3-dimensional, so proportionality is a real
      constraint and not a near-tautology.

      *** CONFIRMED, and it is the headline. *** y0 = mu * dC with

          mu = -2q / ((q - z)(q z + 1)).

      So the representing element is not a new object at all: it is DELTA'S OWN
      trace-invisible part, rescaled. The decomposition reads

          net(x) = sum_lambda a_lambda chi^lambda(x) + mu * tr_M(x * dC),

      and on dC itself the remainder is a SELF-PAIRING,

          net(dC) = mu * <dC, dC> = mu * tr_M(dC^2).

  P5  (added after P4 landed) the convention-dependence CANCELS between mu and
      the self-pairing. Both carry the Hecke-quadratic factors (q - z)(q z + 1):

          <dC,dC>  = -(z-q)(q-1)^2(q+1)^2(qz+1) / (2q(q^2-q+1)(q^2+q+1))
          net(dC)  = -(q-1)^2(q+1)^2 / ((q^2-q+1)(q^2+q+1))          [z-FREE]

      The bean already recorded the remainder as z-independent, as a MEASURED
      fact. This says why: the z-structure of the scalar is the inverse of the
      z-structure of the pairing, exactly.

  P6  and that z-free value must reproduce the floor recorded independently in
      `qbeta_alpha_commutator_floor_probe.py`, namely -(q^2-1)^2/(q^4+q^2+1).
      Cross-check across two unrelated routes.

WHAT A CONFIRMATION WOULD AND WOULD NOT BUY. P1-P3 together say y0's dependence
on the convention is entirely an overall scalar with structurally-forced poles.
That is evidence the element is canonical rather than fitted. It is NOT a
derivation of y0 from the substrate: nothing here produces y0 without first
inverting `net`. Scope-(a), unchanged from the companion probe.
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

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 78)
    print(" qou-xzrj — is the Riesz element y0 structurally forced?")
    print("=" * 78)

    # ------------------------------------------------- rebuild y0 and dC
    proton = sp.expand(L[0] * (L[1] - (h / 2) * ONE) * bv(0))
    neutron = sp.expand((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * bv(0))
    delta = sp.expand(neutron - proton)

    comms = [REG[i] * bv(j) - REG[j] * bv(i) for i in range(N) for j in range(N)]
    cb = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * bv(i) - REG[i] * L[0] * bv(0)),
                           sp.simplify(L[1] * bv(i) - REG[i] * L[1] * bv(0)))
          for i in range(N)]
    ctr = sp.Matrix.hstack(*zc).nullspace()
    P = sp.Matrix.hstack(*(list(ctr) + list(cb)))
    Pinv = P.inv()
    coords = sp.simplify(P.solve(delta))
    dZ = sp.simplify(sum((coords[i] * ctr[i] for i in range(3)), sp.zeros(N, 1)))
    dC = sp.simplify(delta - dZ)

    def comm_part(v):
        c = Pinv * v
        return sp.simplify(sum((c[3 + k] * cb[k] for k in range(3)), sp.zeros(N, 1)))

    ycoef = sp.symbols("y0:6")
    yv = sp.Matrix(list(ycoef))
    system = [sp.Eq(sp.expand(tr_M(mul(bv(i), yv))),
                    sp.expand(net(comm_part(bv(i))))) for i in range(N)]
    Amat, bvec = sp.linear_eq_to_matrix(system, list(ycoef))
    y0 = sp.Matrix([sp.simplify(s) for s in list(sp.linsolve((Amat, bvec),
                                                             list(ycoef)))[0]])
    check("y0_recovered_and_lies_in_the_commutator_subspace",
          all(sp.simplify((Pinv * y0)[k]) == 0 for k in range(3)))

    # ------------------------------------------------------------- P1: shape
    shape = sp.Matrix([0, 1, 1, h, h, -2])
    # scalar from the first nonzero coordinate
    lam = sp.simplify(y0[1] / shape[1])
    resid = [sp.simplify(sp.together(y0[i] - lam * shape[i])) for i in range(N)]
    p1 = all(r == 0 for r in resid)
    check("P1_y0_is_a_scalar_times_the_z_FREE_vector_0_1_1_h_h_MINUS_2", p1,
          "all Markov-parameter dependence of y0 is ONE overall scalar; the "
          "direction in sl_2 does not move with the convention")

    # ------------------------------------------------------- P2: denominator
    den = sp.denom(sp.together(lam))
    target = (z - q) * (q * z + 1) * (q**2 - q + 1) * (q**2 + q + 1)
    ratio = sp.simplify(sp.cancel(den / target))
    p2 = sp.simplify(sp.diff(ratio, z)) == 0 and sp.simplify(ratio) != 0
    check("P2_denominator_is_the_HECKE_QUADRATIC_in_z_times_the_2_1_denominator",
          p2,
          f"den / [(z-q)(qz+1)(q^4+q^2+1)] = {sp.simplify(ratio)} -- z-free, so "
          f"the z-structure is exactly q(q^4+q^2+1)(z^2 - h z - 1), i.e. "
          f"sigma^2 = h sigma + 1 read in z")

    # ------------------------------------------------------------ P3: poles
    poles = sp.solve(sp.Eq(sp.expand(den), 0), z)
    # the Gram roots that kill (2,1), from PR #5864's multiplicity law
    gram_kills_21 = {sp.simplify(q), sp.simplify(-1 / q)}
    got = {sp.simplify(r) for r in poles}
    p3 = got == gram_kills_21 or got == {sp.simplify(q)}
    check("P3_poles_are_exactly_the_Gram_roots_that_kill_the_2_1_block",
          p3,
          f"poles {sorted(map(str, got))} vs the (2,1)-killing Gram roots "
          f"{{q, -1/q}} (sympy filters -1/q under q>0, z>0; the factorisation "
          f"(z-q)(qz+1) exhibits both). y0 blows up exactly where the pairing "
          f"that defines it degenerates ON ITS OWN BLOCK -- forced, not luck")

    # ----------------------------------- P4: y0 vs dC  (was genuinely open)
    nz = next(i for i in range(N) if sp.simplify(dC[i]) != 0)
    mu = sp.simplify(sp.factor(y0[nz] / dC[nz]))
    p4 = all(sp.simplify(sp.together(y0[i] - mu * dC[i])) == 0 for i in range(N))
    check("P4_y0_IS_proportional_to_dC_the_representing_element_is_not_new",
          p4,
          f"y0 = mu * dC with mu = {mu} -- so the element representing the "
          f"trace-invisible part is DELTA'S OWN trace-invisible part, rescaled. "
          f"Nothing outside the decomposition is introduced")

    # ------------------------------------- P5: the remainder is a SELF-pairing
    selfpair = sp.simplify(sp.factor(tr_M(mul(dC, dC))))
    lhs = sp.simplify(sp.factor(net(dC)))
    rhs = sp.simplify(mu * selfpair)
    check("P5_remainder_is_the_SELF_pairing_of_the_trace_invisible_part",
          sp.simplify(sp.together(lhs - rhs)) == 0,
          f"net(dC) = mu * <dC,dC> = mu * tr_M(dC^2), exactly")

    # ------------------------- P5b: the convention-dependence CANCELS, and why
    z_free_remainder = sp.simplify(sp.diff(sp.together(lhs), z)) == 0
    pair_has_z = sp.simplify(sp.diff(sp.together(selfpair), z)) != 0
    mu_has_z = sp.simplify(sp.diff(sp.together(mu), z)) != 0
    check("P5b_z_dependence_CANCELS_between_the_scalar_and_the_pairing",
          z_free_remainder and pair_has_z and mu_has_z,
          "mu and <dC,dC> BOTH carry the Hecke-quadratic factors (q-z)(qz+1) "
          "and they cancel exactly -- which is WHY the remainder is "
          "convention-independent. The bean recorded that as measured; this "
          "is the mechanism")

    # ---------------------------- P6: cross-check against the recorded floor
    floor = -(q**2 - 1) ** 2 / (q**4 + q**2 + 1)
    check("P6_reproduces_the_floor_from_the_independent_alpha_commutator_route",
          sp.simplify(sp.together(lhs - floor)) == 0,
          "-(q^2-1)^2/(q^4+q^2+1), the value qbeta_alpha_commutator_floor_probe "
          "reached by a different route -- two unrelated derivations agree")

    # ------------------------------------- well-defined at both conventions
    zC = sp.sqrt(q) / (q + 1)
    zD = q**3 / (q**2 + 1)
    okC = sp.simplify(den.subs(z, zC)) != 0
    okD = sp.simplify(den.subs(z, zD)) != 0
    check("y0_is_well_defined_at_BOTH_conventions", okC and okD,
          "neither z_C nor z_D is a pole, so the representation exists in each")

    # ---------------------------------------------------- numeric at proton
    qv = Q_MP
    zDv = qv**3 / (qv**2 + 1)

    def num(e):
        return mp.mpf(str(sp.N(e.subs({q: sp.Float(str(qv), 60),
                                       z: sp.Float(str(zDv), 60)}), 50)))

    lam_num = num(lam)
    print(f"\n  at the proton pin, convention D:")
    print(f"    scalar lambda = {mp.nstr(lam_num, 16)}")
    print(f"    y0 direction  = [0, 1, 1, h, h, -2]  (z-free) = dC, rescaled")

    wb = WitnessBuilder("qbeta-riesz-element-structurally-forced",
                        engine="sympy+mpmath")
    wb.set_description(
        "qou-xzrj follow-through: the Riesz element y0 representing the "
        "trace-invisible part of epsNPq is a scalar times the z-FREE direction "
        "[0,1,1,h,h,2], and that scalar's denominator is the Hecke quadratic "
        "z^2 - h z - 1 times the (2,1) block denominator -- so y0's only poles "
        "are z = q and z = -1/q, exactly the Gram roots that annihilate the "
        "(2,1) block it lives in. Evidence the element is canonical rather "
        "than fitted. Scope-(a): NOT a derivation of y0 from the substrate.")
    wb.add_data("y0_direction", [str(sp.simplify(c)) for c in shape])
    wb.add_data("y0_scalar", str(sp.simplify(lam)))
    wb.add_data("denominator_factored", str(sp.factor(den)))
    wb.add_data("dC", [str(sp.simplify(c)) for c in dC])
    wb.add_data("y0_proportional_to_dC", "1" if p4 else "0")
    wb.add_data("mu", str(mu))
    wb.add_data("self_pairing_dC_dC", str(selfpair))
    wb.add_data("net_dC_z_free", str(lhs))
    wb.add_data("lambda_at_proton_pin_conventionD", fmt(lam_num))
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
