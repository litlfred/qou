#!/usr/bin/env python3
"""qou-cds1 entry 12 — bar-parity is SILENT on K(delta), the freedom that dominates L2.

Entry 11 proved that under convention D every ladder rung is forced bar-even:
expanding prod(1 + c_k X^k) in the bar-invariant variable X = u*Vhat and applying
bar gives c_k - bar(c_k) = 0 for every k. That is a real constraint on the rungs.

Entry 10c settled N=1 uniqueness in the negative: the three conditions force the
phase shift c(delta) = delta/2 but leave the multiplicative constant K(delta)
free, subject only to K(0) = 1. The gap between the two natural choices --
K == 1 and K = cos(delta/2), the latter being what the midpoint factor M
supplies -- is ~7656x the Q_beta 100x target. That residual, not the k=3 rung,
is the largest single unresolved contribution to L2 at N=1.

The obvious hope after entry 11 is that bar-parity also pins K. THIS PROBE SHOWS
IT DOES NOT, and the reason is structural rather than circumstantial:

    delta = h^2/2   with   h = q - 1/q
    bar: q -> 1/q   sends   h -> -h   so   h^2 -> h^2

so delta is bar-INVARIANT, and therefore K(delta) is bar-even for EVERY K.
Bar-parity is not a weak constraint on K; it is a vacuous one.

WHAT THIS IS. A scope-(a) NEGATIVE, recorded to stop a wrong inference: entry
11's prune does not reach the L2-dominant freedom, and no amount of sharpening
it will, because the quantity it would have to constrain is invariant under the
symmetry the prune is built from. Closing K needs a DIFFERENT input.

WHAT THIS IS NOT. Not a claim that K is underivable -- only that bar-parity is
not the tool. Not a claim that either K == 1 or K = cos(delta/2) is correct;
both satisfy every condition the arc has established. And not a move on L2:
Q_beta is untouched at 1279 ppb.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sympy as sp

Q_PROTON = "1.1099785827513808075916690956107688798744991218736"
TARGET_PPB = sp.Rational(7797, 1000)  # Q_beta 100x target = sigma_exp/100 = 779.7/100
# NB: AGENTS.md quotes this target as "7.8 ppb", which is 7.797 rounded. Entry 10c's
# recorded "7656x" uses 7.797; dividing by the rounded 7.8 gives 7653x. They are ONE
# number under two roundings of the DENOMINATOR, not two measurements -- do not read
# the pair as a discrepancy, and quote 7656 (the unrounded target) when you need one.

_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    _results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def main() -> int:
    q = sp.symbols("q", positive=True)
    bar = lambda e: sp.simplify(e.subs(q, 1 / q))

    h = q - 1 / q
    delta = h**2 / 2

    print("=" * 72)
    print("  qou-cds1 entry 12 — bar-parity says NOTHING about K(delta)")
    print("=" * 72)

    print("\n-- the symmetry, at the level of h")
    check("bar_sends_h_to_minus_h",
          sp.simplify(bar(h) + h) == 0,
          "bar(h) = -h exactly, so h is bar-ODD")

    print("\n-- and therefore delta is bar-INVARIANT, not bar-odd")
    check("delta_is_bar_invariant",
          sp.simplify(bar(delta) - delta) == 0,
          "bar(delta) = delta, because delta = h^2/2 and bar squares away the sign")

    print("\n-- so bar-evenness of K is automatic for EVERY K: the prune is vacuous here")
    K = sp.Function("K")
    F = sp.cos(sp.Symbol("a") - delta / 2) * K(delta)
    check("K_of_delta_is_bar_even_for_ARBITRARY_K",
          sp.simplify(bar(K(delta)) - K(delta)) == 0,
          "no condition on K follows from bar-parity — it is satisfied identically")
    check("entry11_prune_does_not_reach_K",
          sp.simplify(bar(F.subs(sp.Symbol("a"), delta - sp.Symbol("a"))) - F) == 0,
          "the whole N=1 factor stays bar-invariant with K free (entry 10c, re-confirmed)")

    print("\n-- contrast: the rung variable IS constrained, because u is bar-COVARIANT")
    u = (q - 1) ** 2 * sp.sqrt(q**4 + q**2 + 1) / (q**4 + q**2)
    check("u_is_bar_covariant_weight_q_squared",
          sp.simplify(sp.cancel(bar(u) / u) - q**2) == 0,
          "bar(u)/u = q^2 — a graded weight, which is exactly what makes entry 11 bite")

    print("\n-- the size of the freedom bar-parity fails to remove")
    qv = sp.Rational(Q_PROTON)
    d0 = (qv - 1 / qv) ** 2 / 2
    gap = sp.Abs(1 - sp.cos(d0 / 2))
    gap_ppb = sp.N(gap * 10**9, 30)
    ratio = sp.N(gap * 10**9 / TARGET_PPB, 20)
    print(f"     delta(q0)              = {sp.N(d0, 20)}")
    print(f"     |1 - cos(delta/2)|     = {sp.N(gap, 20)}")
    print(f"     in ppb                 = {gap_ppb}")
    print(f"     vs target 7.797 ppb    = {ratio}x")
    check("residual_is_large_and_UNCONSTRAINED_by_bar_parity",
          sp.N(gap * 10**9) > TARGET_PPB,
          f"K == 1 vs K = cos(delta/2) differ by {sp.N(gap*10**9, 6)} ppb "
          f"= {sp.N(ratio, 5)}x the target, and bar-parity separates neither")

    n_pass = sum(1 for _, ok, _ in _results if ok)
    print("\n" + "=" * 72)
    print(f"  {n_pass}/{len(_results)} assertions passed")
    print("  A NEGATIVE, scope (a). Bar-parity is VACUOUS on K because delta is")
    print("  bar-invariant, so entry 11's prune -- real as it is on the rungs --")
    print("  cannot reach the residual that dominates L2 at N=1. Closing K needs")
    print("  a different input. No c_k is produced; Q_beta stays at 1279 ppb.")
    print("=" * 72)
    return 0 if n_pass == len(_results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
