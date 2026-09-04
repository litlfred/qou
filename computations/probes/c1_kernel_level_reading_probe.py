#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic q (sympy) throughout; audit-only
# falsifiability probe (compute-author 1.3), no witness, no fitted parameter,
# NO float64 anywhere.
"""Probe: the LEVEL reading of the C1 kernel -- L_K as a recurrence on the residue
tower r_n = (D^n X)(-2) across jet levels n, not as a t-shift operator on one
jet.  (bean `qou-col1`; corrects the axis of #6582 / #6610)

CONTEXT.  conj:qdifference-kernel-prolongation-symbol writes x = q^m with m the
BODY ORDER, which prop:sw-period-residue-sum identifies with the JET DEGREE.
So sigma: x -> qx is the level step and L_K = (q^2 x - 1) sigma^2 - (q-1) sigma
- (q-1) is the second-order recurrence [n+2]_q r_{n+2} = r_{n+1} + r_n that the
level-indexed residues of D's jet tower must satisfy.  #6582/#6610 read sigma
as a shift in the t-exponent of a single jet -- the pure-shift-1 special case.
Lean companion: `QOU.Mass.C1KernelLevelReading`.

WHAT IS CHECKED, exactly (symbolic q; symbolic weights c1(e), c2(e); generic
seed a_0..a_{N-1}):
  (1) r_0 = 0 on any power-series seed for ANY shift-sum operator, so the
      residue tower cannot equal a carrier with b_0 != 0.  The corpus carrier
      b_n = f_n/[n]_q! (f = q-involution numbers) has b_0 = b_1 = 1 and DOES
      satisfy C1 (sanity on the carrier itself).
  (2) Two-term operator: r_1 = c2(-2) a_0 (Lean twoOp_residueSeq_one).  A
      derivative-like shift-2 term (c2(-2) = 0) gives r_0 = r_1 = 0, and C1
      from level 0 then forces r == 0 (c1Rec_zero_of_init_zero).
  (3) Derivative-only tower: r_{m+2} = kappa * s_m with s_m = (D^m X)(1),
      kappa = c1(-2) c2(-1); and the identity
        [m+4]_q r_{m+4} - r_{m+3} - r_{m+2} = kappa ([m+4]_q s_{m+2} - s_{m+1} - s_m)
      holds exactly, so C1 from level 2 on the residues <=> index-shifted C1 on
      the t^1-coefficient sequence (twoOp_c1RecFrom_two_iff).
  (4) MEASUREMENT: for the Jackson + q-d/dz tower (balanced and geometric
      q-integer weights) impose the shifted C1 on s_m for m = 0..M-1 and solve
      for the seed: how many seed coefficients does it fix, and is a_0
      (the branch value) among them?  Reported, not interpreted.
  (5) Locking: a constant-weight pure shift-1 tower has r_n = c^n a_{n-2} --
      level and t-exponent lock, which is the sense in which the t-shift
      reading was a special case.

Reproduce:
    PYTHONPATH=computations python3 -u computations/probes/c1_kernel_level_reading_probe.py
"""
from __future__ import annotations

import sympy as sp

q = sp.Symbol("q", positive=True)
N = 12
E_LO, E_HI = -6, N + 4


def shift_op(k, c):
    return lambda f: (lambda e: c(e) * f(e + k))


def add_ops(*ops):
    return lambda f: (lambda e: sum((op(f)(e) for op in ops), sp.Integer(0)))


def iterate(op, n, f):
    for _ in range(n):
        f = op(f)
    return f


def seed_from(coeffs, lo=0):
    return lambda e: sp.sympify(coeffs[e - lo]) if lo <= e < lo + len(coeffs) else sp.Integer(0)


def qint_geo(m):
    # closed form, valid for NEGATIVE m too ([-1]_q = -1/q); the finite sum
    # sum_{i<m} q^i is 0 for m < 0 and would silently kill c1(-2) = [-1]_q
    return sp.cancel((q**m - 1) / (q - 1))


def qint_bal(m):
    return sp.cancel((q**m - q**(-m)) / (q - 1 / q))


def qfact_geo(m):
    out = sp.Integer(1)
    for i in range(1, m + 1):
        out *= qint_geo(i)
    return out


def sym_weight(name, lo, hi):
    tab = {e: sp.Symbol(f"{name}_{'m' if e < 0 else ''}{abs(e)}") for e in range(lo, hi)}
    return (lambda e: tab[e]), tab


def main() -> int:
    fail: list[str] = []

    def ok(cond, msg):
        print(f"  [{'OK ' if cond else 'FAIL'}] {msg}")
        if not cond:
            fail.append(msg)

    a = sp.symbols(f"a0:{N}")
    X = seed_from(a)
    c1, c1tab = sym_weight("c1", E_LO - 2, E_HI + 4)
    c2, c2tab = sym_weight("c2", E_LO - 2, E_HI + 4)
    D_gen = add_ops(shift_op(2, c2), shift_op(1, c1))

    def residues(D, X, nmax):
        return [iterate(D, n, X)(-2) for n in range(nmax)]

    def coeff1(D, X, nmax):
        return [iterate(D, n, X)(1) for n in range(nmax)]

    print("=" * 78)
    print("(1) r_0 = 0 always; the corpus carrier has b_0 = 1 and satisfies C1")
    print("=" * 78)
    ok(residues(D_gen, X, 1)[0] == 0, "generic two-term operator, generic power-series seed: r_0 = X(-2) = 0 (residueSeq_zero_of_powerSeries)")
    f = [sp.Integer(1), sp.Integer(1)]
    for n in range(0, N):
        f.append(sp.expand(f[n + 1] + qint_geo(n + 1) * f[n]))
    b = [sp.cancel(f[n] / qfact_geo(n)) for n in range(N)]
    ok(all(sp.simplify(qint_geo(n + 2) * b[n + 2] - b[n + 1] - b[n]) == 0 for n in range(N - 2)),
       "carrier b_n = f_n/[n]_q! satisfies [n+2]_q b_{n+2} = b_{n+1} + b_n (qlift_normalized_kernel_exists)")
    print(f"  b_0 = {b[0]}, b_1 = {b[1]}, b_2 = {sp.factor(b[2])}")
    ok(b[0] != 0, "b_0 = 1 != 0 = r_0: the residue tower can never EQUAL the carrier at level 0 -- offset, or C1 only from a level on")

    print()
    print("=" * 78)
    print("(2) r_1 = c2(-2) a_0; derivative-like shift 2 kills C1-from-0")
    print("=" * 78)
    r = residues(D_gen, X, 4)
    ok(sp.simplify(r[1] - c2tab[-2] * a[0]) == 0, f"r_1 = c2(-2) * a_0  (got {r[1]})  (twoOp_residueSeq_one)")
    # derivative-like shift 2: c2(-2) = 0
    sub = {c2tab[-2]: 0}
    r1d = sp.simplify(r[1].subs(sub))
    ok(r1d == 0, "with c2(-2) = 0: r_1 = 0, so r_0 = r_1 = 0")
    # C1 from level 0 with r_0 = r_1 = 0 -> recursion gives 0 forever
    rr = [sp.Integer(0), sp.Integer(0)]
    for n in range(6):
        rr.append(sp.cancel((rr[n + 1] + rr[n]) / qint_geo(n + 2)))
    ok(all(x == 0 for x in rr), "C1 from level 0 with two zero initial values is the zero sequence (c1Rec_zero_of_init_zero)")

    print()
    print("=" * 78)
    print("(3) derivative-only tower: r_{m+2} = kappa s_m and the C1 transfer identity")
    print("=" * 78)
    subd = {c1tab[-1]: 0, c2tab[-2]: 0}       # derivative-only: c1(-1) = 0, c2(-2) = 0
    D_d = add_ops(shift_op(2, lambda e: c2(e).subs(subd)), shift_op(1, lambda e: c1(e).subs(subd)))
    rd = residues(D_d, X, 8)
    sd = coeff1(D_d, X, 6)
    kappa = c1tab[-2] * c2tab[-1]
    ok(all(sp.simplify(rd[m + 2] - kappa * sd[m]) == 0 for m in range(6)),
       "r_{m+2} = c1(-2) c2(-1) s_m for m = 0..5 (twoOp_residueSeq_add_two / #6498 twoOp_iterate_residue)")
    ident = all(sp.simplify((qint_geo(m + 4) * rd[m + 4] - rd[m + 3] - rd[m + 2])
                            - kappa * (qint_geo(m + 4) * sd[m + 2] - sd[m + 1] - sd[m])) == 0 for m in range(4))
    ok(ident, "[m+4]_q r_{m+4} - r_{m+3} - r_{m+2} == kappa ([m+4]_q s_{m+2} - s_{m+1} - s_m), m = 0..3 (twoOp_c1RecFrom_two_iff)")

    print()
    print("=" * 78)
    print("(4) MEASUREMENT: what shifted-C1 on s_m imposes on the seed, Jackson + q-d/dz")
    print("=" * 78)
    for name, qi in (("balanced", qint_bal), ("geometric", qint_geo)):
        D = add_ops(shift_op(2, lambda e, qi=qi: qi(e + 2)), shift_op(1, lambda e, qi=qi: qi(e + 1)))
        s = coeff1(D, X, 6)
        kap = sp.simplify(qi(-1) * qi(1))     # c1(-2) c2(-1) = [-1]_q [1]_q
        eqs = [sp.expand(qi(m + 4) * s[m + 2] - s[m + 1] - s[m]) for m in range(4)]
        M = sp.Matrix([[sp.diff(eq, ai) for ai in a] for eq in eqs])
        rank = M.rank()
        lows = [min(i for i in range(N) if eqs[m].has(a[i])) for m in range(4)]
        tops = [max(i for i in range(N) if eqs[m].has(a[i])) for m in range(4)]
        print(f"  {name}: kappa = c1(-2) c2(-1) = {kap};  rank of the 4 constraints (m = 0..3) on the seed = {rank}")
        print(f"  {name}: constraint m reads a_{{low}}..a_{{top}} = {list(zip(lows, tops))}  (level m+2 at t^1 reads a_{{m+3}}..a_{{2m+5}})")
        ok(kap != 0, f"{name}: kappa != 0, so the equivalence applies")
        ok(rank == 4, f"{name}: the 4 constraints are independent (rank 4): each new level reaches a new top coefficient a_{{2m+5}}")
        ok(not any(eq.has(a[0]) for eq in eqs), f"{name}: NO constraint mentions the branch value a_0 -- a derivative-only tower never reads it")

    print()
    print("=" * 78)
    print("(5) locking: constant-weight pure shift-1 tower has r_n = c^n a_{n-2}")
    print("=" * 78)
    c = sp.Symbol("c")
    S1 = shift_op(1, lambda e: c)
    ok(all(sp.simplify(iterate(S1, n, X)(-2) - c**n * X(n - 2)) == 0 for n in range(0, 8)),
       "r_n = c^n a_{n-2}, n = 0..7: the level index and the t-exponent lock (shiftOne_const_residueSeq)")

    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for m_ in fail:
            print("  -", m_)
        return 1
    print("VERDICT (exact):")
    print("  * L_K is a recurrence on the residue tower across LEVELS.  r_0 = 0 always,")
    print("    so the tower never equals a carrier with b_0 != 0 at level 0.")
    print("  * A derivative-like shift-2 term cannot carry C1 from level 0 (r_0 = r_1 = 0).")
    print("  * On a derivative-only tower, C1 from level 2 is EXACTLY the shifted C1 on the")
    print("    t^1-coefficients; each level's constraint reaches one new seed slot and the")
    print("    branch value a_0 is never constrained.  D_q is NOT constructed.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
