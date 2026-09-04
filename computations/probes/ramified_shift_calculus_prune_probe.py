#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic q (sympy) and exact integer/rational
# multipliers throughout; audit-only falsifiability probe (compute-author 1.3),
# no witness, no fitted parameter, NO float64 anywhere.
"""Probe: the W1 prune -- derivative-like prolongations of shift 1 or 2 cannot
produce a residue at a ramified pole.  (bean `qou-4g01`)

CONTEXT.  #6462 showed the classical prolongation d/dz = (1/2t)d/dt kills the
residue slot t^-2 at a square-root branch point because its multiplier (e+2)
vanishes at e = -2.  The scoping audit (2026-07-20) names the q-difference
prolongation D_q as research wall W1.  This probe, with the Lean module
`QOU.Mathlib.RamifiedShiftCalculus`, prunes W1 EXACTLY before anything is built.

THE MODEL.  A local Laurent expansion at z = z_c + t^2 is its coefficient
function f : Z -> R.  A SHIFT OPERATOR (shift k, multiplier c) is

    (S_{k,c} f)(e) = c(e) * f(e + k)          -- coefficient at t^e from t^{e+k}

and every derivative-like operator on the chart is one:
    classical d/dz         k = 2,  c(e) = e + 2
    naive q-deformed d/dz  k = 2,  c(e) = [e+2]_q
    Jackson D_{q,t}        k = 1,  c(e) = [e+1]_q
"Annihilates constants" is c(-k) = 0 -- the constant term t^0 lands at slot -k.

WHAT IS CHECKED, exactly:
  (1) the iterate formula  S^n f (e) = prod_{i<n} c(e+ik) * f(e+nk)  against
      direct iteration, on integer-valued multipliers and seeds;
  (2) the composition law  S_{k,c} S_{l,d} = S_{k+l, c(.)*d(.+k)};
  (3) THE PRUNE: for k = 2 with c(-2) = 0, and for k = 1 with c(-1) = 0 on a
      power-series seed, the residue slot S^n f(-2) is 0 for all n -- for the
      classical multiplier and for the q-deformed ones with SYMBOLIC q (both the
      balanced and the geometric q-integer conventions, so the prune does not
      depend on the convention choice);
  (4) PARITY: an even shift commutes with the covering monodromy t -> -t, an odd
      shift ANTI-commutes; so an odd-shift jet tower alternates its monodromy
      eigenvalue as (-1)^n -- the Door-v residual -- while an even one cannot;
  (5) NON-VACUITY: a shift-1 operator that does NOT annihilate constants
      (c(-1) != 0, a zeroth-order / connection term) DOES produce a residue.

CONCLUSION.  Any single-shift prolongation carrying both measured target
properties (nonzero period; (-1)^n residual) must have an ODD shift and a
NON-DERIVATIVE component.  Derived from the local geometry of Sigma and the two
target properties only -- never from the C1 kernel coefficients (W3).  D_q is
NOT constructed; the class is narrowed.

Reproduce:
    PYTHONPATH=computations python3 -u computations/probes/ramified_shift_calculus_prune_probe.py
"""
from __future__ import annotations

import sys
from itertools import product

import sympy as sp

q = sp.Symbol("q", positive=True)
NMAX = 6
E_LO, E_HI = -6, 8          # exponent window for finite checks


# --------------------------------------------------------------------------
# the model
# --------------------------------------------------------------------------
def shift_op(k, c):
    """S_{k,c}: f |-> (e |-> c(e) f(e+k))."""
    return lambda f: (lambda e: c(e) * f(e + k))


def iterate(op, n, f):
    for _ in range(n):
        f = op(f)
    return f


def iterate_formula(k, c, f, n, e):
    prod = sp.Integer(1)
    for i in range(n):
        prod *= c(e + i * k)
    return prod * f(e + n * k)


def mono(f):
    """covering monodromy t -> -t on coefficients: (-1)^e f(e)."""
    return lambda e: f(e) if e % 2 == 0 else -f(e)


def qint_bal(m):
    """balanced q-integer at integer index: (q^m - q^-m)/(q - q^-1)."""
    return sp.cancel((q**m - q**(-m)) / (q - 1 / q))


def qint_geo(m):
    """geometric q-integer, extended to Z the standard way: (q^m - 1)/(q - 1)."""
    return sp.cancel((q**m - 1) / (q - 1))


def power_series_seed(coeffs):
    """seed supported on e >= 0 with given coefficients."""
    return lambda e: sp.Integer(coeffs[e]) if 0 <= e < len(coeffs) else sp.Integer(0)


def main() -> int:
    fail: list[str] = []

    def ok(cond, msg):
        print(f"  [{'OK ' if cond else 'FAIL'}] {msg}")
        if not cond:
            fail.append(msg)

    seed = power_series_seed([3, -1, 4, 1, -5, 9, 2, 6])   # generic, non-zero constant term

    print("=" * 78)
    print("(1) iterate formula vs direct iteration -- integer multipliers, exact")
    print("=" * 78)
    tests = [(2, lambda e: sp.Integer(e + 2)), (1, lambda e: sp.Integer(e + 1)),
             (1, lambda e: sp.Integer(1)), (3, lambda e: sp.Integer(2 * e - 1))]
    all_ok = True
    for k, c in tests:
        op = shift_op(k, c)
        for n in range(0, NMAX + 1):
            it = iterate(op, n, seed)
            for e in range(E_LO, E_HI):
                if sp.simplify(it(e) - iterate_formula(k, c, seed, n, e)) != 0:
                    all_ok = False
    ok(all_ok, f"S^n f(e) == prod_(i<n) c(e+ik) * f(e+nk) on 4 operators, n<={NMAX}, e in [{E_LO},{E_HI})")

    print()
    print("=" * 78)
    print("(2) composition law S_k,c S_l,d = S_(k+l), c(.)*d(.+k)")
    print("=" * 78)
    c = lambda e: sp.Integer(e + 2)
    d = lambda e: sp.Integer(3 * e - 1)
    lhs = shift_op(2, c)(shift_op(1, d)(seed))
    rhs = shift_op(3, lambda e: c(e) * d(e + 2))(seed)
    ok(all(sp.simplify(lhs(e) - rhs(e)) == 0 for e in range(E_LO, E_HI)),
       "composition law holds pointwise (k=2, l=1)")

    print()
    print("=" * 78)
    print("(3) THE PRUNE -- residue slot t^-2 under derivative-like operators")
    print("=" * 78)
    ops = {
        "classical d/dz        (k=2, c=e+2)":        (2, lambda e: sp.Integer(e + 2)),
        "q-deformed d/dz, bal  (k=2, c=[e+2]_q bal)": (2, lambda e: qint_bal(e + 2)),
        "q-deformed d/dz, geo  (k=2, c=[e+2]_q geo)": (2, lambda e: qint_geo(e + 2)),
        "Jackson D_{q,t}, bal  (k=1, c=[e+1]_q bal)": (1, lambda e: qint_bal(e + 1)),
        "Jackson D_{q,t}, geo  (k=1, c=[e+1]_q geo)": (1, lambda e: qint_geo(e + 1)),
    }
    for name, (k, cc) in ops.items():
        ann = sp.simplify(cc(-k))
        print(f"  {name}:  c(-k) = {ann}")
        ok(ann == 0, f"    annihilates constants: c(-{k}) = 0")
        op = shift_op(k, cc)
        dead = all(sp.simplify(iterate(op, n, seed)(-2)) == 0 for n in range(1, NMAX + 1))
        ok(dead, f"    residue slot S^n f(-2) == 0 for n = 1..{NMAX} (symbolic q where present)")
        # and the killing factor is genuinely the one the Lean names
        if k == 2:
            ok(sp.simplify(cc(-2)) == 0, "    killing factor is the i=0 term c(-2)")
        else:
            ok(sp.simplify(cc(-1)) == 0 and seed(-1) == 0 and seed(-2) == 0,
               "    killing factors: seed support at n<=1, the i=1 term c(-1) at n>=2")

    print()
    print("=" * 78)
    print("(4) PARITY -- even shift commutes with t -> -t, odd shift ANTI-commutes")
    print("=" * 78)
    for k in (2, 4):
        op = shift_op(k, lambda e: sp.Integer(e + 2))
        ok(all(op(mono(seed))(e) == mono(op(seed))(e) for e in range(E_LO, E_HI)),
           f"shift {k} (even): S(mono f) == mono(S f)")
    for k in (1, 3):
        op = shift_op(k, lambda e: sp.Integer(e + 1))
        ok(all(op(mono(seed))(e) == -mono(op(seed))(e) for e in range(E_LO, E_HI)),
           f"shift {k} (odd):  S(mono f) == -mono(S f)")
    # eigenvalue alternation along an odd-shift tower from an even seed
    even_seed = power_series_seed([1, 0, 2, 0, -1, 0, 3, 0])   # mono X = +X
    op1 = shift_op(1, lambda e: sp.Integer(1))
    alt = True
    for n in range(0, NMAX + 1):
        jet = iterate(op1, n, even_seed)
        eps = (-1) ** n
        if not all(mono(jet)(e) == eps * jet(e) for e in range(E_LO, E_HI)):
            alt = False
    ok(alt, "odd-shift tower from a bar-even seed has monodromy eigenvalue (-1)^n  (Door-v residual)")
    op2 = shift_op(2, lambda e: sp.Integer(e + 2))
    const = all(all(mono(iterate(op2, n, even_seed))(e) == iterate(op2, n, even_seed)(e)
                    for e in range(E_LO, E_HI)) for n in range(0, NMAX + 1))
    ok(const, "even-shift (classical) tower keeps eigenvalue +1 at every n  (cannot carry (-1)^n)")

    print()
    print("=" * 78)
    print("(5) NON-VACUITY -- an operator that does NOT annihilate constants has a residue")
    print("=" * 78)
    lam = sp.Symbol("lambda")
    # shift 1 with a zeroth-order weight lambda at the constant slot, [e+1]_q elsewhere
    conn = lambda e: lam if e == -1 else qint_bal(e + 1)
    opc = shift_op(1, conn)
    r2 = sp.simplify(iterate(opc, 2, seed)(-2))
    print(f"  shift-1 with c(-1) = lambda:  S^2 f(-2) = {r2}")
    ok(r2 != 0, "residue is a NON-ZERO multiple of lambda -- the prune is about derivative-like operators, not all")
    ok(sp.simplify(r2.subs(lam, 0)) == 0, "  and it vanishes exactly when lambda = 0 (the derivative-only case)")
    r1 = iterate(shift_op(1, lambda e: sp.Integer(1)), 2, seed)(-2)
    ok(r1 == seed(0), f"  constant-weight shift-1: S^2 f(-2) = f(0) = {r1}  (Lean constant_weight_shift_one_residue)")

    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for m in fail:
            print("  -", m)
        return 1
    print("VERDICT (exact):")
    print("  * Derivative-like prolongations of shift 1 or 2 -- classical d/dz, its")
    print("    q-deformation in EITHER q-integer convention, the Jackson operator in")
    print("    the local coordinate -- all annihilate constants and all have a dead")
    print("    residue slot at every jet level.  None can produce the binding period.")
    print("  * Even shifts preserve the monodromy eigenvalue; odd shifts alternate it.")
    print("  * Hence any single-shift D_q carrying both target properties needs an")
    print("    ODD shift and a NON-DERIVATIVE (zeroth-order / connection) component.")
    print("  D_q is NOT constructed; the class is narrowed, with no C1 input (W3).")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
