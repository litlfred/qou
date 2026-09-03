#!/usr/bin/env python3
"""Which analytic properties separate the Markov parameter's two conventions?

Bean `qou-lp5d`.  Written because five convention-C sites in the c_k ladder cone
were triaged B4 ("emits a committed witness -- value change") and handed to the
2026-08-25 drain (PR #5754) as migratable work, when substituting
`z_D = q^3/(q^2+1)` into them does not move a value -- it FALSIFIES each file's
own committed assertions.  The B4 label reads as a work item, so without a
recorded reason every future drain picks them up and re-derives this.

This probe records the reason, once, as an exact symbolic fact.

## What is checked

Four properties that `z_C = sqrt(q)/(q+1)` has and `z_D = q^3/(q^2+1)` does not,
each of which is the SUBJECT of at least one of the five sites:

  P1  bar-parity under the fibre involution q -> 1/q.
      z_C is exactly bar-EVEN; z_D is neither even nor odd.
      Subject of qbeta_z_bar_parity_fmap_class_probe (assertion
      `z_bar_even_twist_1`, with the sorry-free Lean companion
      QOU/QBeta/ZBarParity.lean) and of
      qbeta_eval_map_bar_decomposition_probe (the EXACT even/odd split of the
      archimedean evaluation map, confirming epsNP_decomp / trMNP_decomp).

  P2  criticality at q=1.  (z_C - 1/2) vanishes to order exactly 2, i.e.
      dz_C/dq(1) = 0; for z_D the order is 1 and the derivative is 1.
      Subject of qbeta_t3_carrier_q1_order_preflight_probe, whose T3-1 kill
      criterion is precisely "rational functions of z realize only EVEN
      vanishing orders at q=1".

  P3  the pre-archimedean ODE (4 + 6w + 2w^2) z' + w z = 0, w = q - 1.
      Exact for z_C; nonzero residual for z_D.
      Subject of qbeta_prearchimedean_z_recursion.

  P4  rationality.  z_C is the only non-rational ingredient of tau_M(T_beta)
      (that is what makes the holonomic argument in P3 have content); z_D lies
      in Q(q) outright, so `A(q) + B(q) z` collapses.

Reported alongside: both conventions give z(1) = 1/2, which is why a shallow
q=1 check does not separate them -- and the numeric gap at the substrate pin.

## Scope

Scope-(a) and descriptive.  This says the five files' CONCLUSIONS are properties
of z_C, so a z-swap is not a migration for them; it does NOT re-derive anything
under D, and it takes no position on what the D-frame answers are.  That
re-derivation is `qou-cds1`, which AGENTS.md already states is required and
already states is "NOT a z-swap".

Exact symbolic throughout (sympy); the two numeric lines carry mpmath.mpf end to
end and reach `float` nowhere.  Emits no witness -- there is no computed
quantity here that a downstream consumer should pin to, only a recorded reason.
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — experimental (proton) pin

set_compute_dps()

q = sp.symbols("q", positive=True)
w = sp.symbols("w")

Z_C = sp.sqrt(q) / (1 + q)
Z_D = q**3 / (q**2 + 1)


def bar(e):
    """The fibre bar involution q -> 1/q."""
    return sp.simplify(sp.radsimp(e.subs(q, 1 / q)))


def parity(e):
    e = sp.simplify(e)
    if sp.simplify(bar(e) - e) == 0:
        return "even"
    if sp.simplify(bar(e) + e) == 0:
        return "odd"
    return "neither"


def vanishing_order(e, at=1, maxn=6):
    """Order of the first non-vanishing derivative of `e` at q = at."""
    e = sp.simplify(e)
    for n in range(maxn + 1):
        d = sp.simplify(sp.diff(e, q, n).subs(q, at))
        if d != 0:
            return n, d
    return None, None


def main() -> int:
    checks = []

    def check(name, passed, detail=""):
        checks.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}"
              + (f"   {detail}" if detail else ""))

    print("=" * 74)
    print("P1  bar-parity under q -> 1/q")
    print("=" * 74)
    p_c, p_d = parity(Z_C), parity(Z_D)
    print(f"    z_C = {Z_C}   bar -> {bar(Z_C)}   parity = {p_c}")
    print(f"    z_D = {Z_D}   bar -> {bar(Z_D)}   parity = {p_d}")
    check("zC_bar_even", p_c == "even")
    check("zD_bar_neither", p_d == "neither",
          "so -h*z_D is not a bar-odd term and the EXACT even/odd split "
          "of the evaluation map does not survive the swap")

    print()
    print("=" * 74)
    print("P2  criticality at q = 1")
    print("=" * 74)
    n_c, _ = vanishing_order(Z_C - sp.Rational(1, 2))
    n_d, _ = vanishing_order(Z_D - sp.Rational(1, 2))
    d_c = sp.simplify(sp.diff(Z_C, q).subs(q, 1))
    d_d = sp.simplify(sp.diff(Z_D, q).subs(q, 1))
    print(f"    z_C(1) = {sp.simplify(Z_C.subs(q, 1))}   "
          f"ord(z-1/2) = {n_c}   dz/dq(1) = {d_c}")
    print(f"    z_D(1) = {sp.simplify(Z_D.subs(q, 1))}   "
          f"ord(z-1/2) = {n_d}   dz/dq(1) = {d_d}")
    check("zC_critical_at_1_order_2", n_c == 2 and d_c == 0)
    check("zD_not_critical_at_1", n_d == 1 and d_d != 0,
          "so 'rational functions of z realize only EVEN vanishing orders' "
          "is false under D and the T3-1 parity exclusion evaporates")
    check("both_conventions_agree_at_q1",
          sp.simplify(Z_C.subs(q, 1) - Z_D.subs(q, 1)) == 0,
          "both are 1/2 — a shallow q=1 check does NOT separate them")

    print()
    print("=" * 74)
    print("P3  pre-archimedean ODE  (4 + 6w + 2w^2) z' + w z = 0,  w = q - 1")
    print("=" * 74)
    qw = 1 + w
    res = {}
    for nm, z in (("z_C", sp.sqrt(qw) / (1 + qw)), ("z_D", qw**3 / (qw**2 + 1))):
        r = sp.simplify(sp.radsimp(
            (4 + 6 * w + 2 * w**2) * sp.diff(z, w) + w * z))
        res[nm] = r
        print(f"    {nm}: residual = {r}")
    check("ODE_exact_for_zC", res["z_C"] == 0)
    check("ODE_fails_for_zD", res["z_D"] != 0,
          "so the recursion the probe derives is a property of z_C only")

    print()
    print("=" * 74)
    print("P4  rationality in Q(q)")
    print("=" * 74)
    rat_c = sp.simplify(Z_C).is_rational_function(q)
    rat_d = sp.simplify(Z_D).is_rational_function(q)
    print(f"    z_C rational in q: {rat_c}      z_C^2 = {sp.simplify(Z_C**2)}")
    print(f"    z_D rational in q: {rat_d}")
    check("zC_not_rational", not rat_c,
          "it is the ONLY non-rational ingredient — which is what gives the "
          "holonomic argument its content")
    check("zD_rational", rat_d,
          "so A(q) + B(q)*z collapses and there is no holonomic structure left")

    print()
    print("=" * 74)
    print("numeric separation at the substrate proton pin (mpf end to end)")
    print("=" * 74)
    zc = mp.sqrt(Q_MP) / (Q_MP + 1)
    zd = Q_MP**3 / (Q_MP**2 + 1)
    print(f"    z_C(q0) = {mp.nstr(zc, 20)}")
    print(f"    z_D(q0) = {mp.nstr(zd, 20)}")
    print(f"    z_D/z_C - 1 = {mp.nstr((zd - zc) / zc, 10)}")

    n_ok = sum(1 for _, p in checks if p)
    print()
    print(f"VERDICT: {n_ok}/{len(checks)} — the two conventions are separated by "
          f"bar-parity, criticality at q=1, the ODE, and rationality.")
    print("  Scope-(a): a z-swap is not a migration for a file whose SUBJECT is "
          "one of these.\n  It does not re-derive anything under D — that is "
          "qou-cds1, and AGENTS.md already\n  states it is not a z-swap.")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
