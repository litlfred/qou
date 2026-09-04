#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic q (sympy) throughout; audit-only
# falsifiability probe (compute-author 1.3), no witness, no fitted parameter,
# NO float64 anywhere.
"""Probe: can a DERIVATIVE-ONLY mixed-shift D_q have the C1 kernel as its symbol?
(bean `qou-33hb`)

CONTEXT.  #6474/#6498/#6523 narrowed the prolongation operator D_q from the two
target properties and left one class alive at the low body orders: a mixed-shift
sum of DERIVATIVE-LIKE terms (every multiplier vanishes at e = -k), e.g. Jackson
[e+1]_q sigma + q-d/dz [e+2]_q sigma^2.  The conjecture says D_q's symbol is the
C1 kernel  L_K = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1).  This probe reads L_K
in the same calculus, in the two natural dictionaries, and tests the class
against it.  Lean companion: `QOU.Mass.C1KernelAsShiftSum`.

  (a) sigma = unit t-shift, x = q^e:   L = (q^{e+2}-1) S_2 - (q-1) S_1 - (q-1) S_0
  (b) double cover, x^{1/2} = u^e, q = u^2, sigma = t-shift 2:
                                       L = (u^{2e+4}-1) S_4 - (u^2-1) S_2 - (u^2-1) S_0

WHAT IS CHECKED, exactly (symbolic q, u):
  (1) L in dictionary (a) reproduces the corpus recurrence [m+2]_q b_{m+2} =
      b_{m+1} + b_m in the GEOMETRIC q-integer (qint of
      qlift_normalized_kernel_exists), up to the factor (q-1).
  (2) THE INVARIANT: a derivative-only sum kills the constant seed t^0; L does
      not (value -(q-1) at e = 0 in (a), -(u^2-1) in (b)).  Checked on the two
      derivative-only candidates (balanced and geometric q-integer conventions)
      and on L in both dictionaries.  Consequence: no derivative-only sum equals
      L -- and the only way to make L's shift-1 multiplier vanish at -1 is q = 1.
  (3) Where L sits in the #6474 class under (a): shift-2 term derivative-like
      (c2(-2) = 0), shift-1 term NOT (c1(-1) = -(q-1)); residue dead at level 1,
      alive at level 2 with L^2 f(-2) = (q-1)^2 (a0 - a1) on a power-series seed.
      Compared with the derivative-only candidate's level-2 residue -a1.
  (4) Under (b): all shifts even, L commutes with the covering monodromy
      (no odd component); residue alive at level 1, L f(-2) = -(u^2-1) a0.

CONCLUSION.  If the conjecture holds, D_q is NOT derivative-only: the kernel's
own zeroth-order term forces a non-derivative component -- the #6474 clause by
a third route, independent of the residue and the residual.  D_q is not
constructed; the dictionary sigma <-> t-shift (W2) is still open, and the two
dictionaries disagree on parity.

Reproduce:
    PYTHONPATH=computations python3 -u computations/probes/derivative_only_dq_vs_c1_kernel_probe.py
"""
from __future__ import annotations

import sympy as sp

q = sp.Symbol("q", positive=True)
u = sp.Symbol("u", positive=True)
E_LO, E_HI = -8, 10


def shift_op(k, c):
    return lambda f: (lambda e: c(e) * f(e + k))


def add_ops(*ops):
    return lambda f: (lambda e: sum((op(f)(e) for op in ops), sp.Integer(0)))


def mono(f):
    return lambda e: f(e) if e % 2 == 0 else -f(e)


def qint_bal(m):
    return sp.cancel((q**m - q**(-m)) / (q - 1 / q))


def qint_geo(m):
    return sp.cancel((q**m - 1) / (q - 1))


def const_seed(e):
    return sp.Integer(1) if e == 0 else sp.Integer(0)


def seed_from(coeffs, lo=0):
    return lambda e: sp.sympify(coeffs[e - lo]) if lo <= e < lo + len(coeffs) else sp.Integer(0)


def main() -> int:
    fail: list[str] = []

    def ok(cond, msg):
        print(f"  [{'OK ' if cond else 'FAIL'}] {msg}")
        if not cond:
            fail.append(msg)

    # dictionary (a)
    cA2 = lambda e: q ** (e + 2) - 1
    cA1 = lambda e: -(q - 1)
    cA0 = lambda e: -(q - 1)
    L_a = add_ops(shift_op(2, cA2), shift_op(1, cA1), shift_op(0, cA0))
    # dictionary (b)
    cB4 = lambda e: u ** (2 * e + 4) - 1
    cB2 = lambda e: -(u**2 - 1)
    cB0 = lambda e: -(u**2 - 1)
    L_b = add_ops(shift_op(4, cB4), shift_op(2, cB2), shift_op(0, cB0))
    # derivative-only candidates
    D_bal = add_ops(shift_op(2, lambda e: qint_bal(e + 2)), shift_op(1, lambda e: qint_bal(e + 1)))
    D_geo = add_ops(shift_op(2, lambda e: qint_geo(e + 2)), shift_op(1, lambda e: qint_geo(e + 1)))

    print("=" * 78)
    print("(1) L in dictionary (a) IS the corpus recurrence (geometric qint), times (q-1)")
    print("=" * 78)
    b = sp.symbols("b0:12")
    bseq = seed_from(b)
    good = all(sp.simplify(L_a(bseq)(m) - (q - 1) * (qint_geo(m + 2) * bseq(m + 2) - bseq(m + 1) - bseq(m))) == 0
               for m in range(0, 9))
    ok(good, "L b (m) == (q-1) * ([m+2]_geo b_{m+2} - b_{m+1} - b_m) for m = 0..8  (Lean c1KernelOp_eq_recurrence)")

    print()
    print("=" * 78)
    print("(2) THE INVARIANT: derivative-only kills the constant seed; the kernel does not")
    print("=" * 78)
    for name, D in (("Jackson+q-d/dz, balanced", D_bal), ("Jackson+q-d/dz, geometric", D_geo)):
        ok(all(sp.simplify(D(const_seed)(e)) == 0 for e in range(E_LO, E_HI)),
           f"{name}: kills t^0 (Lean sumOp_derivativeOnly_const)")
    va = sp.simplify(L_a(const_seed)(0))
    vb = sp.simplify(L_b(const_seed)(0))
    print(f"  L_a(t^0)(0) = {va};   L_b(t^0)(0) = {vb}")
    ok(sp.simplify(va + (q - 1)) == 0, "dictionary (a): kernel on t^0 at e=0 is -(q-1) -- nonzero for q != 1 (c1KernelOp_const_ne_zero)")
    ok(sp.simplify(vb + (u**2 - 1)) == 0, "dictionary (b): kernel on t^0 at e=0 is -(u^2-1) -- nonzero for u^2 != 1 (c1KernelOpCover_const_ne_zero)")
    supp = [e for e in range(E_LO, E_HI) if sp.simplify(L_a(const_seed)(e)) != 0]
    print(f"  support of L_a(t^0): {supp}  (e=-1 from the shift-1 term, e=0 from the zeroth-order term)")
    ok(supp == [-1, 0], "dictionary (a): L(t^0) is supported on exactly {-1, 0} -- both from the NON-derivative terms")
    ok(sp.solve(sp.Eq(cA1(-1), 0), q) == [1], "the only way L's shift-1 multiplier annihilates constants is q = 1")

    print()
    print("=" * 78)
    print("(3) Where L sits in the #6474 class under (a); its residues")
    print("=" * 78)
    ok(sp.simplify(cA2(-2)) == 0, "shift-2 term annihilates constants: c2(-2) = q^0 - 1 = 0 (derivative-like)")
    ok(sp.simplify(cA1(-1)) != 0, "shift-1 term does NOT: c1(-1) = -(q-1) -- the non-derivative odd component #6474 asks for")
    a = sp.symbols("a0:10")
    f = seed_from(a)
    r1 = sp.simplify(L_a(f)(-2))
    r2 = sp.simplify(L_a(L_a(f))(-2))
    print(f"  L f(-2) = {r1};   L^2 f(-2) = {sp.factor(r2)}")
    ok(r1 == 0, "level 1: residue dead on a power-series seed (c1KernelOp_residue_one)")
    ok(sp.simplify(r2 - (q - 1) ** 2 * (a[0] - a[1])) == 0, "level 2: residue = (q-1)^2 (a0 - a1) -- branch value and leading sqrt coefficient (c1KernelOp_residue_two)")
    rd = sp.simplify(D_bal(D_bal(f))(-2))
    ok(sp.simplify(rd + a[1]) == 0, f"for comparison the derivative-only candidate's level-2 residue is -a1 = {rd}: no a0 -- it cannot see the branch value")

    print()
    print("=" * 78)
    print("(4) Dictionary (b): even shifts only")
    print("=" * 78)
    ok(all(sp.simplify(L_b(mono(f))(e) - mono(L_b(f))(e)) == 0 for e in range(E_LO, E_HI)),
       "L_b commutes with the covering monodromy t -> -t: no odd component (c1KernelOpCover_comm_mono)")
    rb1 = sp.simplify(L_b(f)(-2))
    print(f"  L_b f(-2) = {sp.factor(rb1)}")
    ok(sp.simplify(rb1 + (u**2 - 1) * a[0]) == 0, "level 1: residue = -(u^2-1) a0, alive from the branch value (c1KernelOpCover_residue_one)")
    ok(sp.simplify(cB4(-4)) != 0, "the shift-4 term is NOT derivative-like either: c4(-4) = u^-4 - 1")

    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for m_ in fail:
            print("  -", m_)
        return 1
    print("VERDICT (exact):")
    print("  * A derivative-only shift-sum kills the constant seed; the C1 kernel does")
    print("    not, in either dictionary.  So NO derivative-only mixed-shift D_q has the")
    print("    kernel as its symbol.  If the conjecture holds, D_q carries a non-derivative")
    print("    component -- #6474's clause by a third route, independent of the residual.")
    print("  * Under (a) the kernel is exactly the #6474 class (odd shift 1, constant")
    print("    weight), with residue (q-1)^2 (a0 - a1) at level 2.  Under (b) it is even-")
    print("    only, monodromy-commuting, with residue -(u^2-1) a0 at level 1.  The two")
    print("    dictionaries disagree on parity: that disagreement IS the open W2 question.")
    print("  D_q is NOT constructed.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
