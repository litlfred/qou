#!/usr/bin/env python3
"""Exact closed form for the rank-N Ocneanu/Wenzl Markov parameter.

Evidence for the one cited step of
`folio/quantum-observable-universe/lean/QOU/Eightfold/OcneanuRankFamily.lean`:
that the Lean `markovParam N q` IS the Markov parameter of the SU(N) trace.
Mathlib has no hook-content or principal-specialisation API, so that identity
cannot be stated there; it is established here instead, symbolically and
exactly, against the corpus's own producer `y_lambda_su_n`.

## What is checked

1. `z_N := tr_M(sigma) = y_(2)*q - y_(1,1)/q`, evaluated on the hook-content
   weights of `y_lambda_su_n_symbolic(2, q, N)`, equals

       z_N = q^(2N-1) (q^2 - 1) / (q^(2N) - 1) = (q - 1/q) q^(2N) / (q^(2N) - 1)

   identically in q, for N = 1..8.  This is `markovParam` in the Lean.
2. `z_2 = q^3/(q^2+1)` -- registry convention D, the corpus's canonical Markov
   parameter (owner ruling 2026-08-15 R1).  So the production trace is the
   RANK-2 member of the family.  (`markovParam_two`.)
3. `z_1 = q` (`markovParam_one`) and `z_3 = q^5/(q^4+q^2+1)`
   (`markovParam_three`).
4. `z_N - (q - 1/q) = (q - 1/q)/(q^(2N) - 1)`, strictly positive and strictly
   decreasing: the family sits strictly above the Hecke coefficient q - 1/q,
   which is its uncapped N -> oo value.  (`markovParam_sub_hecke`,
   `markovParam_gt_hecke`, `markovParam_strictAnti`.)
5. The row cap: at rank N the surviving Wedderburn blocks are exactly the
   partitions with at most N rows.  This is the trace-side form of
   `Lambda^N W = 1` -- the last block to survive is the single column (1^N),
   which is the volume form, and (1^(N+1)) is the first to die.
   (`rowCapFactor_eq_zero`; and `RowCapObstruction.weyl_dim_alt_eq_zero_iff`
   on the categorical side.)

## Precision

Symbolic throughout (sympy exact rational functions of q); the only numeric
evaluations are mpmath at 50 dps for the registry cross-check.  No float64
anywhere -- per AGENTS.md the NO-FLOAT64 discipline covers probes.

Writes no witness by design: every claim here is an exact symbolic identity
that a reader re-derives by running the file, and the durable carriers are the
Lean declarations named above.
"""
from __future__ import annotations

import sys

import sympy as sp
import mpmath as mp

sys.path.insert(0, __file__.rsplit("/", 1)[0])

from y_lambda_su_n import y_lambda_su_n_symbolic, f_lambda  # noqa: E402

Q = sp.symbols("q", positive=True)

# docs/coordination/trace-convention-registry.md, at the proton pin.
Q0_STR = "1.1099785827513808075916690956107688798744991218736"
# 50 dps, from y_lambda_su_n.REG_ZD (re-emitted 2026-09-04, bean qou-90k2 --
# the previous 17-digit literal was wrong in its last digit).
REG_ZD_STR = "0.61268803714646525159582986394589924802630839154509"

N_MAX = 8


def z_from_weights_symbolic(N: int):
    """tr_M(sigma) on H_2 for the rank-N trace, exact in q."""
    y = y_lambda_su_n_symbolic(2, Q, N)
    return sp.cancel(sp.simplify(y[(2,)] * Q + y[(1, 1)] * (-1 / Q)))


def closed_form(N: int):
    """The Lean `markovParam N q`."""
    return sp.cancel(Q ** (2 * N - 1) * (Q ** 2 - 1) / (Q ** (2 * N) - 1))


def main() -> int:
    fails = 0

    # (1) the closed form, N = 1..N_MAX
    zs = {}
    for N in range(1, N_MAX + 1):
        z = z_from_weights_symbolic(N)
        zs[N] = z
        if sp.simplify(z - closed_form(N)) != 0:
            print(f"FAIL (1) N={N}: {sp.factor(z)} != {sp.factor(closed_form(N))}")
            fails += 1
    print(f"(1) closed form z_N = q^(2N-1)(q^2-1)/(q^(2N)-1) for N=1..{N_MAX}: "
          f"{'PASS' if fails == 0 else 'FAIL'}")

    # (2) N = 2 is registry convention D
    okD = sp.simplify(zs[2] - Q ** 3 / (Q ** 2 + 1)) == 0
    print(f"(2) z_2 == q^3/(q^2+1)  [convention D]: {'PASS' if okD else 'FAIL'}")
    fails += 0 if okD else 1

    mp.mp.dps = 50
    q0 = mp.mpf(Q0_STR)
    z2 = sp.lambdify(Q, zs[2], "mpmath")(q0)
    z3 = sp.lambdify(Q, zs[3], "mpmath")(q0)
    okReg = mp.fabs(z2 - mp.mpf(REG_ZD_STR)) < mp.mpf("1e-40")
    print(f"    z_2(q0) = {mp.nstr(z2, 50)}\n    registry REG_ZD = {REG_ZD_STR}"
          f"  -> {'PASS' if okReg else 'FAIL'}")
    print(f"    z_3(q0) = {mp.nstr(z3, 20)}   (the rank-3 / flavour value)")
    fails += 0 if okReg else 1

    # (3) the two named specialisations
    ok1 = sp.simplify(zs[1] - Q) == 0
    ok3 = sp.simplify(zs[3] - Q ** 5 / (Q ** 4 + Q ** 2 + 1)) == 0
    print(f"(3) z_1 == q: {'PASS' if ok1 else 'FAIL'};  "
          f"z_3 == q^5/(q^4+q^2+1): {'PASS' if ok3 else 'FAIL'}")
    fails += (0 if ok1 else 1) + (0 if ok3 else 1)

    # (4) excess over the Hecke coefficient, and strict antitonicity
    hecke = Q - 1 / Q
    okE = all(
        sp.simplify((zs[N] - hecke) - hecke / (Q ** (2 * N) - 1)) == 0
        for N in range(1, N_MAX + 1)
    )
    print(f"(4) z_N - (q - 1/q) == (q - 1/q)/(q^(2N)-1) for all N: "
          f"{'PASS' if okE else 'FAIL'}")
    fails += 0 if okE else 1
    vals = [sp.lambdify(Q, zs[N], "mpmath")(q0) for N in range(1, N_MAX + 1)]
    okMono = all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
    hval = q0 - 1 / q0
    print(f"    strictly decreasing at q0: {'PASS' if okMono else 'FAIL'}"
          f"   z_1={mp.nstr(vals[0], 12)} ... z_{N_MAX}={mp.nstr(vals[-1], 12)}"
          f"  -> q - 1/q = {mp.nstr(hval, 12)}")
    fails += 0 if okMono else 1

    # (5) the row cap == the volume-form degree
    print("(5) row cap at n=5: surviving blocks are exactly ell(lambda) <= N")
    okCap = True
    for N in range(1, 6):
        y = y_lambda_su_n_symbolic(5, Q, N)
        surv = sorted(k for k, v in y.items() if sp.simplify(v) != 0)
        want = sorted(k for k in y if len(k) <= N)
        if surv != want:
            okCap = False
            print(f"    FAIL N={N}: {surv} != {want}")
        else:
            top = tuple([1] * N)
            note = "  (top = the volume form (1^N))" if top in surv else ""
            print(f"    N={N}: max rows surviving = {max(len(k) for k in surv)}"
                  f"{note}")
    fails += 0 if okCap else 1

    print()
    print("VERDICT:", "all checks PASS" if fails == 0 else f"{fails} FAILURE(S)")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
