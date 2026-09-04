#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic q (sympy) throughout; audit-only
# falsifiability probe (compute-author 1.3), no witness, no fitted parameter,
# NO float64 anywhere.
"""Probe: can the C1 kernel, read as a shift operator on the jet tower, carry the
Door-v (-1)^m residual -- and does the residual decide between the two
sigma <-> t-shift dictionaries?  (bean `qou-w0tx`)

CONTEXT.  #6582 read L_K = (q^2 x - 1) sigma^2 - (q-1) sigma - (q-1) in the
ramified shift calculus under two dictionaries,
  (a) sigma = unit t-shift, x = q^e:   L_a = (q^{e+2}-1) S_2 - (q-1) S_1 - (q-1) S_0
  (b) double cover, q = u^2, sigma = t-shift 2:
                                        L_b = (u^{2e+4}-1) S_4 - (u^2-1) S_2 - (u^2-1) S_0
and found they disagree on parity: (a) has an odd shift, (b) commutes with the
covering monodromy mono: t -> -t.  The Door-v residual is the demand that the
level-n jet carry monodromy character (-1)^n eps from some level n0 on.  Lean
companion: `QOU.Mass.C1KernelDictionaryParity`.

WHAT IS CHECKED, exactly (symbolic q, u; generic seeds a_0..a_{N-1}):
  (1) Dictionary (b): the monodromy character is transported UNCHANGED level to
      level (commutation), so demanding a flip at two consecutive levels is a
      linear system on the jet whose only solution is the zero jet
      (Lean comm_mono_flip_kills / c1KernelOpCover_residual_kills_tower).
  (2) Dictionary (a): E Y = 0 and E (O Y) = 0 are the same q-recurrence with
      q^{e+2} vs q^{e+1} in the shift-2 weight; (q-1)*a_e + b_e =
      (q-1)^2 q^{e+1} Y(e+2) exactly, so jointly they force Y = 0
      (Lean c1E_zero_c1E_O_zero_imp / c1KernelOp_residual_kills_jet).
  (3) The window is minimal: ONE alternating level is satisfiable in (a) --
      E Y = 0 alone has the q-hypergeometric solution Y(e+2) = Y(e)/[e+2]_q
      (geometric q-integer) with the odd part forced to zero by the e = -1 slot,
      i.e. the q-cosh series in t^2 -- it is the SECOND consecutive alternating
      level that kills.  In (b) one level is likewise
      satisfiable by any fixed-parity seed.
  (4) Sanity: the kernel annihilates its own C1 carrier (b_0 = b_1 = 1,
      [m+2]_q b_{m+2} = b_{m+1} + b_m) as a coefficient sequence -- L_a b = 0
      identically, residue slots included -- so the kernel's tower on the
      carrier is trivial (X, 0, 0, ...).  The Door-v alternation lives on the
      GGM growing solution, not on anything the kernel iterates.

CONCLUSION.  The residual does not decide the dictionary; it kills both.  If
the conjecture's "symbol = L_K" holds and the prolongation IS its symbol, the
(-1)^m twist is not produced by the prolongation's own iteration.  D_q is not
constructed; lower-order corrections to the symbol are not excluded.

Reproduce:
    PYTHONPATH=computations python3 -u computations/probes/c1_kernel_door_v_residual_probe.py
"""
from __future__ import annotations

import sympy as sp

q = sp.Symbol("q", positive=True)
u = sp.Symbol("u", positive=True)
N = 10           # seed window a_0..a_{N-1}
E_LO, E_HI = -6, N + 4


def shift_op(k, c):
    return lambda f: (lambda e: c(e) * f(e + k))


def add_ops(*ops):
    return lambda f: (lambda e: sum((op(f)(e) for op in ops), sp.Integer(0)))


def mono(f):
    return lambda e: f(e) if e % 2 == 0 else -f(e)


def iterate(op, n, f):
    for _ in range(n):
        f = op(f)
    return f


def seed_from(coeffs, lo=0):
    return lambda e: sp.sympify(coeffs[e - lo]) if lo <= e < lo + len(coeffs) else sp.Integer(0)


def qint_geo(m):
    return sp.cancel((q**m - 1) / (q - 1))


def only_zero_solution(eqs, unknowns):
    sol = sp.linsolve([sp.expand(x) for x in eqs if sp.expand(x) != 0], list(unknowns))
    return sol == sp.FiniteSet(tuple(sp.Integer(0) for _ in unknowns))


def main() -> int:
    fail: list[str] = []

    def ok(cond, msg):
        print(f"  [{'OK ' if cond else 'FAIL'}] {msg}")
        if not cond:
            fail.append(msg)

    a = sp.symbols(f"a0:{N}")
    X = seed_from(a)

    # dictionary (a)
    E_a = add_ops(shift_op(2, lambda e: q ** (e + 2) - 1), shift_op(0, lambda e: -(q - 1)))
    O_a = shift_op(1, lambda e: -(q - 1))
    L_a = add_ops(E_a, O_a)
    # dictionary (b)
    L_b = add_ops(shift_op(4, lambda e: u ** (2 * e + 4) - 1),
                  shift_op(2, lambda e: -(u**2 - 1)), shift_op(0, lambda e: -(u**2 - 1)))

    print("=" * 78)
    print("(1) Dictionary (b): character transported unchanged; a flip kills the jet")
    print("=" * 78)
    for n in range(0, 4):
        Y = iterate(L_b, n, X)
        ok(all(sp.simplify(L_b(mono(Y))(e) - mono(L_b(Y))(e)) == 0 for e in range(E_LO, E_HI)),
           f"level {n}: L_b commutes with mono on the level-{n} jet (c1KernelOpCover_comm_mono)")
    # even seed: mono X = X (eps = 1). Residual at levels 0 and 1: mono(L_b X) = -L_b X.
    # With commutation mono(L_b X) = L_b X, so L_b X = 0 -- a linear system on the seed.
    a_even = [a[i] if i % 2 == 0 else sp.Integer(0) for i in range(N)]
    Xe = seed_from(a_even)
    Y1 = L_b(Xe)
    eqs = [mono(Y1)(e) + Y1(e) for e in range(E_LO, E_HI)]        # mono(Y1) = -Y1
    unknowns = [a[i] for i in range(N) if i % 2 == 0]
    ok(only_zero_solution(eqs, unknowns),
       "even seed, flip demanded at level 1: the only solution is the ZERO level-1 jet -> zero seed on the window (comm_mono_flip_kills)")
    # and a fixed-parity seed alone is fine at ONE level (no flip demanded): character 1 at every level
    ok(all(sp.simplify(mono(iterate(L_b, n, Xe))(e) - iterate(L_b, n, Xe)(e)) == 0
           for n in range(0, 4) for e in range(E_LO, E_HI)),
       "even seed: character is +1 at EVERY level -- (b) never alternates, it is a constant character")

    print()
    print("=" * 78)
    print("(2) Dictionary (a): E Y = 0 and E(O Y) = 0 differ by q^{e+2} vs q^{e+1}")
    print("=" * 78)
    Y = X
    ident = True
    for e in range(0, N - 2):
        a_e = E_a(Y)(e)
        b_e = E_a(O_a(Y))(e - 1)
        ident &= sp.simplify((q - 1) * a_e + b_e - (q - 1) ** 2 * q ** (e + 1) * Y(e + 2)) == 0
    ok(ident, "(q-1)*E Y(e) + E(O Y)(e-1) == (q-1)^2 q^{e+1} Y(e+2) for e = 0..%d (the Lean linear_combination)" % (N - 3))
    eqs = [E_a(Y)(e) for e in range(E_LO, E_HI)] + [E_a(O_a(Y))(e) for e in range(E_LO, E_HI)]
    ok(only_zero_solution(eqs, a),
       "E Y = 0 and E(O Y) = 0 jointly: only the ZERO seed on the window (c1E_zero_c1E_O_zero_imp)")

    print()
    print("=" * 78)
    print("(3) The window is minimal: one alternating level is satisfiable")
    print("=" * 78)
    # Impose E Y = 0 only where the window can carry it (e + 2 < N); the upper
    # edge would otherwise force Y = 0 from the top down -- a window artifact.
    eqs1 = [E_a(Y)(e) for e in range(E_LO, N - 2)]
    sol = sp.linsolve([sp.expand(x) for x in eqs1 if sp.expand(x) != 0], list(a))
    (vec,) = list(sol)
    ok(any(v != 0 for v in vec), "E Y = 0 alone has NON-trivial solutions (window edge excluded)")
    ok(all(sp.sympify(vec[i]) == 0 for i in range(1, N, 2)),
       "...but the ODD part is forced to zero: the e = -1 slot reads E Y(-1) = (q-1) Y(1), so Y(1) = 0 propagates")
    fam = all(sp.simplify(sp.sympify(vec[e + 2]) * qint_geo(e + 2) - sp.sympify(vec[e])) == 0 for e in range(0, N - 2))
    ok(fam, "the family is Y(e+2) = Y(e)/[e+2]_q (geometric q-integer): the q-cosh series in t^2, ONE free constant Y(0)")
    Yf = seed_from([sp.sympify(v) for v in vec])
    ok(all(sp.simplify(E_a(Yf)(e)) == 0 for e in range(E_LO, N - 2)), "on that family E Y = 0 (level-1 jet is the pure odd part O Y, so it DOES flip)")
    ok(any(sp.simplify(E_a(O_a(Yf))(e)) != 0 for e in range(E_LO, N - 3)),
       "but E(O Y) != 0 on it: the level-2 flip is what kills -- minimal window is two consecutive levels")

    print()
    print("=" * 78)
    print("(4) Sanity: the kernel annihilates its own C1 carrier")
    print("=" * 78)
    b = [sp.Integer(1), sp.Integer(1)]
    for m in range(0, N):
        b.append(sp.cancel((b[m + 1] + b[m]) / qint_geo(m + 2)))
    B = seed_from(b)
    ok(all(sp.simplify(L_a(B)(e)) == 0 for e in range(E_LO, N)),
       "L_a b == 0 on the window, residue slots e = -2, -1 included (b_0 = b_1 makes the e = -1 slot vanish)")
    print("  so the kernel's tower on the carrier is (b, 0, 0, ...): nothing to alternate.")

    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for m_ in fail:
            print("  -", m_)
        return 1
    print("VERDICT (exact):")
    print("  * The Door-v residual does NOT decide the sigma <-> t-shift dictionary.")
    print("    It kills both: under (b) by monodromy commutation (jet dead one level")
    print("    after alternation starts), under (a) because the two even-part")
    print("    constraints differ by q^{e+2} vs q^{e+1} (jet dead AT the level it starts).")
    print("  * One alternating level is satisfiable in both; the second kills.")
    print("  * If symbol = L_K and D_q is its symbol, the (-1)^m twist is not made by")
    print("    D_q's own iteration.  D_q is NOT constructed; lower-order terms not excluded.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
