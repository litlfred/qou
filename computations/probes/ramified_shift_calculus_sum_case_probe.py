#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic q (sympy) and exact integer
# multipliers throughout; audit-only falsifiability probe (compute-author 1.3),
# no witness, no fitted parameter, NO float64 anywhere.
"""Probe: the SUM case of the ramified shift calculus.  (bean `qou-60ew`)

CONTEXT.  #6474 (`QOU.Mathlib.RamifiedShiftCalculus`) proved that a SINGLE
derivative-like shift operator of shift 1 or 2 -- one that annihilates constants,
c(-k) = 0 -- has a dead residue slot t^-2 at every jet level on a power-series
seed.  Its audit left the general q-D-module element, a finite sum
Sigma_k c_k sigma^k, open: "could in principle cancel or survive".

The Lean companion `QOU.Mathlib.RamifiedShiftCalculusSum` settles it two ways.
This probe checks every claim there exactly.

  (1) REVIVAL.  For D = S_{2,c2} + S_{1,c1} with BOTH terms annihilating
      constants, the residue slot at level n+2 is
          D^{n+2} f (-2) = c1(-2) * c2(-1) * (D^n f)(1)
      -- the t^1 coefficient of the level-n jet.  Not a cancellation: the word
      (shift 1, then shift 2) JUMPS over the constant slot t^0 where every
      derivative multiplier vanishes.  Checked for the classical pair
      d/dt + (1/t)d/dt (weight -1) and the Jackson + q-d/dz pair (weight
      [-1]_q [1]_q = -1, symbolic q), and against the closed form for the
      whole word expansion at n = 2.
  (2) PARITY TWIST.  mono(E f + O f) = E(mono f) - O(mono f) for E a sum of even
      shifts and O a sum of odd shifts.
  (3) THE RESIDUAL KILLS THE RESIDUE.  If the tower D^n X from a fixed-parity
      power-series seed carries the full (-1)^n residual, then the even part
      annihilates every level, D^n X = O^n X, and the residue slot is dead.
      Checked constructively: on a seed where the residual holds up to level
      n_max, the residue vanishes; and on a generic seed BOTH the residual
      fails and the residue is nonzero -- the two are exclusive, never jointly
      present.
  (4) NON-VACUITY.  A pure shift-2 sum (two even terms) stays dead; the
      revival needs the odd component.  And the revival weight c1(-2) c2(-1)
      really is the only surviving word of length 2.

Reproduce:
    PYTHONPATH=computations python3 -u computations/probes/ramified_shift_calculus_sum_case_probe.py
"""
from __future__ import annotations

from itertools import product

import sympy as sp

q = sp.Symbol("q", positive=True)
NMAX = 5
E_LO, E_HI = -8, 10


def shift_op(k, c):
    return lambda f: (lambda e: c(e) * f(e + k))


def add_ops(*ops):
    return lambda f: (lambda e: sum((op(f)(e) for op in ops), sp.Integer(0)))


def iterate(op, n, f):
    for _ in range(n):
        f = op(f)
    return f


def mono(f):
    return lambda e: f(e) if e % 2 == 0 else -f(e)


def qint_bal(m):
    return sp.cancel((q**m - q**(-m)) / (q - 1 / q))


def seed_from(coeffs):
    return lambda e: sp.sympify(coeffs[e]) if 0 <= e < len(coeffs) else sp.Integer(0)


def word_residue(ops_by_shift, word, f):
    """Residue slot contribution of one word (reading order): position walks
    -2 -> -2+k1 -> ..., weight = product of multipliers met, times f at the end."""
    pos = -2
    w = sp.Integer(1)
    for k in word:
        w *= ops_by_shift[k](pos)
        pos += k
    return w * f(pos)


def main() -> int:
    fail: list[str] = []

    def ok(cond, msg):
        print(f"  [{'OK ' if cond else 'FAIL'}] {msg}")
        if not cond:
            fail.append(msg)

    # generic power-series seed with a nonzero t^1 coefficient (a square-root branch)
    a = sp.symbols("a0:8")
    seed = seed_from(a)

    print("=" * 78)
    print("(1) REVIVAL: D = S_2 + S_1 with both annihilating constants")
    print("=" * 78)
    pairs = {
        "classical d/dt + (1/t)d/dt": (lambda e: sp.Integer(e + 1), lambda e: sp.Integer(e + 2)),
        "Jackson [e+1]_q + q-d/dz [e+2]_q": (lambda e: qint_bal(e + 1), lambda e: qint_bal(e + 2)),
    }
    for name, (c1, c2) in pairs.items():
        ok(sp.simplify(c1(-1)) == 0 and sp.simplify(c2(-2)) == 0, f"{name}: both terms annihilate constants")
        D = add_ops(shift_op(2, c2), shift_op(1, c1))
        weight = sp.simplify(c1(-2) * c2(-1))
        print(f"  {name}: weight c1(-2)*c2(-1) = {weight}")
        ok(weight == -1, "    weight is -1")
        ok(sp.simplify(iterate(D, 0, seed)(-2)) == 0 and sp.simplify(iterate(D, 1, seed)(-2)) == 0,
           "    levels 0, 1: residue slot dead (seed support)")
        good = True
        for n in range(0, NMAX + 1):
            lhs = sp.simplify(iterate(D, n + 2, seed)(-2))
            rhs = sp.simplify(weight * iterate(D, n, seed)(1))
            if sp.simplify(lhs - rhs) != 0:
                good = False
        ok(good, f"    D^(n+2) f(-2) == c1(-2) c2(-1) * (D^n f)(1) for n = 0..{NMAX}")
        r2 = sp.simplify(iterate(D, 2, seed)(-2))
        print(f"    level-2 residue = {r2}")
        ok(sp.simplify(r2 + a[1]) == 0, "    level 2: residue = -a1, the leading square-root coefficient -- NONZERO for a genuine branch")
        # word expansion at n = 2
        ops_by_shift = {1: c1, 2: c2}
        words = {w: sp.simplify(word_residue(ops_by_shift, w, seed)) for w in product((1, 2), repeat=2)}
        print(f"    words: {words}")
        ok(all(v == 0 for w, v in words.items() if w != (1, 2)), "    every word other than (1 then 2) lands on t^0 and dies")
        ok(sp.simplify(words[(1, 2)] - r2) == 0, "    the single surviving word (1,2) is the whole residue -- a jump, not a cancellation")

    print()
    print("=" * 78)
    print("(2) PARITY TWIST: mono(E f + O f) = E(mono f) - O(mono f)")
    print("=" * 78)
    E = add_ops(shift_op(2, lambda e: sp.Integer(e + 2)), shift_op(4, lambda e: sp.Integer(3 * e - 1)))
    O = add_ops(shift_op(1, lambda e: sp.Integer(e + 1)), shift_op(3, lambda e: sp.Integer(e * e + 2)))
    D = add_ops(E, O)
    ok(all(sp.simplify(mono(D(seed))(e) - (E(mono(seed))(e) - O(mono(seed))(e))) == 0 for e in range(E_LO, E_HI)),
       "parity twist holds pointwise for a 2-even + 2-odd sum")

    print()
    print("=" * 78)
    print("(3) THE RESIDUAL KILLS THE RESIDUE (two-term derivative-like D)")
    print("=" * 78)
    c1 = lambda e: qint_bal(e + 1)
    c2 = lambda e: qint_bal(e + 2)
    S2, S1 = shift_op(2, c2), shift_op(1, c1)
    D = add_ops(S2, S1)

    def residual_holds(X, eps, nmax):
        for n in range(0, nmax + 1):
            J = iterate(D, n, X)
            if not all(sp.simplify(mono(J)(e) - (-1) ** n * eps * J(e)) == 0 for e in range(E_LO, E_HI)):
                return False
        return True

    # (a) generic bar-even seed: residual FAILS already at n = 2, residue is NONZERO
    even_seed = seed_from([1, 0, 2, 0, -1, 0, 3, 0])
    ok(all(mono(even_seed)(e) == even_seed(e) for e in range(E_LO, E_HI)), "generic seed is bar-even (eps = +1)")
    ok(not residual_holds(even_seed, 1, 2), "  generic seed: the (-1)^n residual FAILS by level 2 (E does not kill the tower)")
    r = sp.simplify(iterate(D, 4, even_seed)(-2))
    print(f"  generic seed: level-4 residue = {r}")
    ok(r != 0, "  generic seed: residue is NONZERO -- residual absent, residue present")
    # (b) a seed on which E kills the whole S1-tower: X supported so that [e+2]_q X(e+2) = 0 along the tower.
    #     The only way with [k]_q != 0 for k != 0 is X(e+2) = 0 wherever the tower is nonzero:
    #     take X = t^0 (constant). Then S1 X = [1]_q t^-1 ... wait: S1 reads slot e from e+1, so
    #     S1 X (e) = [e+1]_q X(e+1): nonzero only at e = -1 with weight [0]_q = 0. So the S1-tower
    #     of a constant is X, 0, 0, ...; E X = S2 X = [e+2]_q X(e+2): nonzero only at e = -2, weight [0]_q = 0.
    const = seed_from([1])
    ok(residual_holds(const, 1, NMAX), "  constant seed: the (-1)^n residual holds at every level (tower is X, 0, 0, ...)")
    ok(all(sp.simplify(iterate(D, n, const)(-2)) == 0 for n in range(0, NMAX + 1)),
       "  constant seed: residue slot dead at every level -- residual present, residue absent")
    ok(all(all(sp.simplify(S2(iterate(S1, n, const))(e)) == 0 for e in range(E_LO, E_HI)) for n in range(0, NMAX + 1)),
       "  constant seed: the even part S2 annihilates every level of the S1-tower (Lean residual_tower_is_odd_part)")
    ok(all(all(sp.simplify(iterate(D, n, const)(e) - iterate(S1, n, const)(e)) == 0 for e in range(E_LO, E_HI)) for n in range(0, NMAX + 1)),
       "  constant seed: D^n X == S1^n X at every level (the tower is the odd part's)")
    # (c) exclusivity on a family: for seeds a0 + a1 t with symbolic a0, a1, the residual at level 1
    #     forces E X = 0, i.e. a1 = 0 wherever [e+2]_q != 0 -- and then the residue is 0.
    fam = seed_from([a[0], a[1]])
    J1 = D(fam)
    viol = [sp.simplify(mono(J1)(e) + J1(e)) for e in range(E_LO, E_HI)]
    print(f"  family a0 + a1 t: level-1 residual defect = {[v for v in viol if v != 0]}")
    sols = sp.solve([v for v in viol if v != 0], [a[1]], dict=True)
    ok(sols == [{a[1]: 0}], "  level-1 residual on a0 + a1 t forces a1 = 0 exactly (E X = 0)")
    ok(sp.simplify(iterate(D, 2, fam)(-2).subs(a[1], 0)) == 0, "  and with a1 = 0 the level-2 residue vanishes")
    ok(sp.simplify(iterate(D, 2, fam)(-2)) != 0, "  while with a1 free it is -a1 != 0")

    print()
    print("=" * 78)
    print("(4) NON-VACUITY")
    print("=" * 78)
    Deven = add_ops(shift_op(2, lambda e: qint_bal(e + 2)), shift_op(2, lambda e: sp.Integer(e + 2)))
    ok(all(sp.simplify(iterate(Deven, n, seed)(-2)) == 0 for n in range(1, NMAX + 1)),
       "a sum of two shift-2 derivatives stays dead: the revival needs the ODD component")
    # a shift-1 derivative alone is dead (the #6474 result), so the residue is genuinely a SUM effect
    ok(all(sp.simplify(iterate(S1, n, seed)(-2)) == 0 for n in range(0, NMAX + 1)),
       "the shift-1 derivative alone is dead (#6474); the residue in (1) is a genuine sum effect")

    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for m in fail:
            print("  -", m)
        return 1
    print("VERDICT (exact):")
    print("  * Two derivative-like terms of shifts 1 and 2 -- classical or q-deformed --")
    print("    REVIVE the residue slot: level n+2 reads the t^1 coefficient of level n")
    print("    with weight -1.  A jump over the constant slot, not a cancellation.")
    print("  * The (-1)^n residual forces the even part off the tower, leaving the")
    print("    pure shift-1 tower, whose residue is dead.  Residue and residual are")
    print("    mutually exclusive for derivative-like sums of shifts <= 2.")
    print("  * So the #6474 conclusion -- odd shift AND a non-derivative component --")
    print("    survives for sums, by a different mechanism.  D_q is NOT constructed.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
