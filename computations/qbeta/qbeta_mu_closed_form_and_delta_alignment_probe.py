#!/usr/bin/env python3
"""
qbeta_mu_closed_form_and_delta_alignment_probe.py — qou-xzrj: the scalar mu has
a framework-native closed form, and y0's alignment with Delta is NOT generic.

# Ref: .beans/qou-xzrj--gap-the-767-trace-invisible-remainder-of-epsnpq-st.md
# Ref: computations/qbeta/qbeta_riesz_element_is_structurally_forced_probe.py
# Ref: folio/quantum-observable-universe/lean/QOU/BraidKnot/LadderConventionLocalisation.lean

WHERE THIS PICKS UP. The previous probe found y0 = mu * dC with
mu = -2q/((q-z)(qz+1)), and narrowed the whole remaining gap to mu. Two
questions were left, and they pull in opposite directions:

  (A) does mu have a closed form in objects the framework already has, or is it
      just what the solve returned?
  (B) `y0 IS dC up to a scalar` sounds strong -- but how surprising is it?

## (A) mu is framework-native

    (q - z)(q z + 1) = -q (z^2 - h z - 1) = -q P(z),  the HECKE QUADRATIC in z
    P(z) = -(q^4 + q^2 + 1)/q^2 * y_(2,1)(z)
    q^4 + q^2 + 1 = q^2 [3]_q          ([3]_q = q^2 + 1 + q^-2, repo convention)

so, exactly and identically in q AND z:

    mu = - dim(V_(2,1)) / ( [3]_q * y_(2,1)(z) ),      dim(V_(2,1)) = 2.

Block dimension, a quantum integer, and the block's own Markov weight. Nothing
outside the framework, and no free parameter.

**This is an IDENTITY IN TWO FREE SYMBOLS, which is why it is not a fit.** A fit
matches numbers at a point; this holds for every q and every z. There is nothing
to tune. (The bracket convention is the repo's, and matches the sibling's
`b^2 = [3]_q/[2]_q^2` -- checked here rather than assumed.)

## (B) and the alignment is NOT generic -- this is the part that could have

y0 is the Riesz representative of `net` restricted to [H,H]. **Delta appears
NOWHERE in its definition.** So `y0 proportional to dC` is a genuine alignment
between a functional-determined element and Delta's own commutator part, not a
restatement.

The commutator subspace is 3-dimensional, so "parallel" is 2 conditions. If
every element's commutator part were parallel to y0 the claim would be empty.

MEASURED, and the answer is not the clean one I expected: of the five basis
elements with a nonzero commutator part, FOUR are not parallel to y0 and ONE is
-- `e_minus`, the longest element w_0. So the alignment is a real 2-condition
constraint that Delta satisfies, but Delta is NOT the unique element satisfying
it. State it that way. (That w_0 is the one is unlikely to be an accident:
conjugation by w_0 is the diagram automorphism s_0 <-> s_1, already noted in
this bean as what makes `net` take only two values across the six conjugates.)

## What this still does NOT do

It does not derive `net` from the substrate. `mu`'s closed form is reached by
identification -- I recognised the factors -- not by a forward derivation from a
normalisation principle. What changed is that mu is no longer an opaque solve
output: it is `-dim / ([3]_q y_lambda)`, which is the kind of object a forward
derivation could plausibly produce. Scope-(a), unchanged.
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
    print(" qou-xzrj — mu's closed form, and how special the Delta alignment is")
    print("=" * 78)

    comms = [REG[i] * bv(j) - REG[j] * bv(i) for i in range(N) for j in range(N)]
    cb = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * bv(i) - REG[i] * L[0] * bv(0)),
                           sp.simplify(L[1] * bv(i) - REG[i] * L[1] * bv(0)))
          for i in range(N)]
    ctr = sp.Matrix.hstack(*zc).nullspace()
    P = sp.Matrix.hstack(*(list(ctr) + list(cb)))
    Pinv = P.inv()

    def comm_part(v):
        c = Pinv * v
        return sp.simplify(sum((c[3 + k] * cb[k] for k in range(3)),
                               sp.zeros(N, 1)))

    # y0 -- note: Delta does NOT enter here
    ycoef = sp.symbols("y0:6")
    yv = sp.Matrix(list(ycoef))
    system = [sp.Eq(sp.expand(tr_M(mul(bv(i), yv))),
                    sp.expand(net(comm_part(bv(i))))) for i in range(N)]
    Amat, bvec = sp.linear_eq_to_matrix(system, list(ycoef))
    y0 = sp.Matrix([sp.simplify(s) for s in
                    list(sp.linsolve((Amat, bvec), list(ycoef)))[0]])

    proton = sp.expand(L[0] * (L[1] - (h / 2) * ONE) * bv(0))
    neutron = sp.expand((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * bv(0))
    delta = sp.expand(neutron - proton)
    dC = comm_part(delta)

    def parallel(u, v):
        """u, v parallel as vectors over Q(q,z)?  (both assumed nonzero)"""
        nz = next((i for i in range(N) if sp.simplify(v[i]) != 0), None)
        if nz is None:
            return False
        s = sp.simplify(u[nz] / v[nz])
        return all(sp.simplify(sp.together(u[i] - s * v[i])) == 0
                   for i in range(N))

    nz = next(i for i in range(N) if sp.simplify(dC[i]) != 0)
    mu = sp.simplify(y0[nz] / dC[nz])
    check("y0_is_parallel_to_dC_recovered", parallel(y0, dC),
          "restated from the previous probe so this file stands alone")

    # ---------------------------------------- (A) mu's framework-native form
    y3, y21, y13 = sp.symbols("y3 y21 y13")

    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi13(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i])
                               for i in range(N)))

    def chi21(v):
        reg = sp.simplify(sum(v[i] * sp.trace(REG[i]) for i in range(N)))
        return sp.simplify((reg - chi3(v) - chi13(v)) / 2)

    eqs = [sp.Eq(sp.expand(tr_M(bv(i))),
                 sp.expand(y3 * chi3(bv(i)) + y21 * chi21(bv(i))
                           + y13 * chi13(bv(i)))) for i in range(N)]
    Ay, by = sp.linear_eq_to_matrix(eqs, [y3, y21, y13])
    sol = list(sp.linsolve((Ay, by), [y3, y21, y13]))[0]
    Y21 = sp.simplify(sol[1])

    dim21 = sp.Integer(2)
    check("block_dimension_is_the_character_at_the_identity",
          sp.simplify(chi21(bv(0)) - dim21) == 0,
          "chi^(2,1)(1) = 2, so the '2' below is dim V_(2,1), measured not assumed")

    check("bracket_convention_q4_q2_1_equals_q2_times_bracket3",
          sp.simplify(sp.expand(q**2 * qbr(3) - (q**4 + q**2 + 1))) == 0,
          "[3]_q = q^2 + 1 + q^-2 (repo convention), so q^4+q^2+1 = q^2 [3]_q")

    closed = -dim21 / (qbr(3) * Y21)
    check("MU_HAS_A_FRAMEWORK_NATIVE_CLOSED_FORM",
          sp.simplify(sp.together(mu - closed)) == 0,
          "mu = -dim(V_(2,1)) / ([3]_q * y_(2,1)(z)) -- EXACT, identically in q "
          "AND z. An identity in two free symbols cannot be a fit: there is "
          "nothing to tune")

    # cross-check the bracket against the sibling's b^2 = [3]_q/[2]_q^2
    check("bracket_matches_the_siblings_b_squared_convention",
          sp.simplify(qbr(3) / qbr(2) ** 2
                      - (q**4 + q**2 + 1) / (q**2 + 1) ** 2) == 0,
          "same [n]_q as hoefsmitB_sq_eq_bracketThree_div_bracketTwo_sq (#5337)")

    # ------------------------------- (B) is the alignment with Delta generic?
    others = []
    for i in range(N):
        ci = comm_part(bv(i))
        if all(sp.simplify(e) == 0 for e in ci):
            continue
        others.append((NAMES[i], parallel(y0, ci)))
    n_par = sum(1 for _, p in others if p)
    check("the_alignment_is_NOT_generic_other_elements_are_not_parallel",
          n_par < len(others),
          f"of {len(others)} basis elements with a nonzero commutator part, "
          f"{n_par} is/are parallel to y0 (the longest element w_0). The "
          f"commutator space is 3-dimensional so parallelism is 2 conditions: "
          f"Delta satisfies a real constraint, but is NOT the unique element "
          f"that does -- do not over-claim this as 'Delta is special'")
    for nm, p in others:
        print(f"        {nm:9s} commutator part parallel to y0: {p}")

    # ------------------------------------------------------ numeric, proton
    qv = Q_MP
    zDv = qv**3 / (qv**2 + 1)

    def num(e):
        return mp.mpf(str(sp.N(e.subs({q: sp.Float(str(qv), 60),
                                       z: sp.Float(str(zDv), 60)}), 50)))

    print(f"\n  at the proton pin, convention D:")
    print(f"    [3]_q        = {mp.nstr(num(qbr(3)), 16)}")
    print(f"    y_(2,1)(z_D) = {mp.nstr(num(Y21), 16)}")
    print(f"    mu           = {mp.nstr(num(mu), 16)}")

    wb = WitnessBuilder("qbeta-mu-closed-form-and-delta-alignment",
                        engine="sympy+mpmath")
    wb.set_description(
        "qou-xzrj: the scalar mu in the pairing representation of epsNPq has "
        "the framework-native closed form mu = -dim(V_(2,1)) / ([3]_q * "
        "y_(2,1)(z)), exact identically in q AND z -- block dimension, a "
        "quantum integer, and the block's own Markov weight, with no free "
        "parameter. Also establishes that y0's alignment with Delta's "
        "commutator part is NOT generic: y0 is defined without reference to "
        "Delta, and the other basis elements' commutator parts are not "
        "parallel to it. Scope-(a): mu is identified, not forward-derived.")
    wb.add_data("mu_closed_form", str(sp.simplify(closed)))
    wb.add_data("y_2_1_of_z", str(sp.factor(Y21)))
    wb.add_data("bracket_three", str(sp.simplify(qbr(3))))
    wb.add_data("dim_V_21", "2")
    wb.add_data("mu_at_proton_pin_conventionD", fmt(num(mu)))
    wb.add_data("n_other_elements_parallel_to_y0", str(n_par))
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
