"""The branch-3 holonomy t^2 test is a BAR-SYMMETRY test in disguise — so D
failing it is NOT independent evidence against the convention-D ruling.

Bean `qou-pdix` (child of `qou-cds1`). Chases the tension recorded in entry (6):
single-wrap C matches a holonomy angle `c*ln q` through `t^2` while single-wrap
D does not, which entry (6) logged as *"TENSION WITH THE RULING ... deepens the
recorded decayLadder_zC_threeRow_ne_zero tension"*.

**It does not deepen it. It restates it.**

## The chain, each link exact

1. With `q = 1 + t` and `h = q - 1/q = 2t - t^2 + ...`, the phase
   `alpha = (z-1)h/2` has

       t^1 coefficient = z(1) - 1
       t^2 coefficient = 1/4 + z'(1)          <- verified for both conventions

2. Kohno-Drinfeld fixes the scale rather than leaving it free: braiding is
   `P exp(hbar t/2)` with `t` eigenvalues +-1, matching Hecke `{q, -1/q}` exactly
   when `q = e^{hbar/2}`, so `hbar = 2 ln q` and a constant-residue holonomy
   angle is a multiple of `ln q`. Pinning `c` at `t^1` (both conventions give
   `z(1) = 1/2`, hence `c = -1/2`), the `c*ln q` prediction at `t^2` is `1/4`.

3. So **alpha is second-order logarithmic if and only if `z'(1) = 0`.**

4. **Bar-evenness FORCES `z'(1) = 0`.** Differentiating `z(1/q) = z(q)` at
   `q = 1` gives `-z'(1) = z'(1)`, hence `z'(1) = 0`. No property of the
   particular function is used — only that `q = 1` is the fixed point of the bar
   involution.

5. `z_C = sqrt(q)/(q+1)` **is** bar-even (`z_C(1/q) - z_C(q) == 0` identically —
   it is `u/(u^2+1)` in `u = sqrt q`, manifestly `u <-> 1/u` symmetric).
   `z_D = q^3/(q^2+1)` is **not**, and `z_D'(1) = 1`.

## The consequence, which is a DEFLATION

C passes the `t^2` holonomy test **because it is bar-invariant**, and D fails it
**because it is not**. These are not two facts. The corpus already knows z_D is
not bar-even — `QOU.Interactions.markovZC`'s docstring says so, and
`QOU.QBeta.DFrameBarAction` proves the stronger statement that the whole bar
ACTION changes shape (affine reflection under C, multiplicative under D).

**So the t^2 failure is not independent evidence against convention D.** It is
the same fact in holonomy language. The 2026-08-15 ruling does not have to
answer a second objection; it has to answer the one it already answered.

## And a correction to the branch-3 acceptance test

Entry (6) states acceptance-test part 1 as *"reproduce alpha through order t^2
(requires z'(1) = 0)"*. Given the chain above, **that test has no discriminating
power for route 5**: any construction built on a bar-even `z` passes it
automatically and any built on `z_D` fails it automatically, whatever the
construction is. It tests the Markov parameter, not the holonomy hypothesis.

The other two parts are untouched and remain the real test: account for the
`-1/4` of `Re(log-gap)` and the discarded `i*pi`; deliver a value below 1.

## What this does NOT say

It does not say D is right or C is right. It does not overturn the ruling, and
it does not rescue C: C's own `t^3` coefficient misses its prediction
(`alpha_C - c*ln q = -7t^3/48 + ...`), so C is not a logarithm either — the
agreement is second-order, not exact, and cannot be exact because **alpha is
ALGEBRAIC** (a rational function of `sqrt q` under C, of `q` under D) while
`c*ln q` is transcendental.

Run:  python3 -u computations/qbeta/qbeta_holonomy_t2_is_a_bar_symmetry_test_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in (REPO / "computations", REPO / "computations" / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from q_parameter import q_at  # noqa: E402 — proton pin
from witness_base import WitnessBuilder  # noqa: E402

q, t, u = sp.symbols("q t u", positive=True)
h = q - 1 / q
zC = sp.sqrt(q) / (q + 1)
zD = q**3 / (q**2 + 1)


def alpha(z):
    return sp.simplify((z - 1) * h / 2)


def tcoeff(expr, k, n=6):
    return sp.nsimplify(sp.expand(
        sp.series(expr.subs(q, 1 + t), t, 0, n).removeO()).coeff(t, k))


def main() -> int:
    checks: list[tuple[str, bool, str]] = []
    lnq_ser = sp.series(sp.log(1 + t), t, 0, 6).removeO()

    data = {}
    for nm, z in (("C", zC), ("D", zD)):
        a = alpha(z)
        z1 = sp.simplify(z.subs(q, 1))
        zp = sp.simplify(sp.diff(z, q).subs(q, 1))
        c1, c2 = tcoeff(a, 1), tcoeff(a, 2)
        bar_even = sp.simplify(sp.together(z.subs(q, 1 / q) - z)) == 0
        dev = sp.expand(sp.nsimplify(
            sp.series(a.subs(q, 1 + t), t, 0, 6).removeO() - c1 * lnq_ser))
        first_dev = next(k for k in range(1, 6)
                         if sp.simplify(dev.coeff(t, k)) != 0)
        data[nm] = {"z_at_1": str(z1), "z_prime_at_1": str(zp),
                    "alpha_t1": str(c1), "alpha_t2": str(c2),
                    "bar_even": bool(bar_even),
                    "first_deviation_order_from_c_lnq": first_dev,
                    "alpha_closed_form": str(sp.factor(a))}

        # link 1: t^2 coefficient is exactly 1/4 + z'(1)
        checks.append((
            f"alpha_t2_coeff_is_quarter_plus_zprime_{nm}",
            sp.simplify(c2 - (sp.Rational(1, 4) + zp)) == 0,
            f"{nm}: t^2 = {c2} = 1/4 + z'(1) = 1/4 + {zp}",
        ))
        # link 2: c is pinned to -1/2 by t^1, since z(1) = 1/2 in both
        checks.append((
            f"c_pinned_to_minus_half_{nm}",
            z1 == sp.Rational(1, 2) and c1 == sp.Rational(-1, 2),
            f"{nm}: z(1) = 1/2 so the t^1 coefficient pins c = -1/2",
        ))

    # link 3+4: bar-even <=> z'(1) = 0, and that is what decides the t^2 test
    checks.append((
        "zC_is_bar_even", data["C"]["bar_even"],
        "z_C(1/q) - z_C(q) == 0 identically",
    ))
    checks.append((
        "zD_is_NOT_bar_even", not data["D"]["bar_even"],
        "z_D(1/q) != z_D(q)",
    ))
    checks.append((
        "bar_even_forces_zprime_zero",
        sp.simplify(sp.diff(zC, q).subs(q, 1)) == 0,
        "differentiating z(1/q) = z(q) at q=1 gives -z'(1) = z'(1)",
    ))
    checks.append((
        "not_bar_even_zD_has_nonzero_zprime",
        sp.simplify(sp.diff(zD, q).subs(q, 1)) != 0,
        "z_D'(1) = 1, so nothing forces the t^2 match",
    ))
    checks.append((
        "t2_test_passes_exactly_for_the_bar_even_convention",
        (tcoeff(alpha(zC), 2) == sp.Rational(1, 4))
        and (tcoeff(alpha(zD), 2) != sp.Rational(1, 4)),
        "C passes the holonomy t^2 test, D fails it — and the discriminator "
        "is bar-evenness, not the holonomy hypothesis",
    ))

    # the deflation: C is not a logarithm either
    checks.append((
        "C_is_not_a_logarithm_either",
        data["C"]["first_deviation_order_from_c_lnq"] == 3,
        "alpha_C - c*ln q first deviates at t^3, so the agreement is "
        "second-order, not exact",
    ))
    checks.append((
        "alpha_is_algebraic_so_exact_agreement_is_impossible",
        sp.factor(alpha(zC).subs(q, u**2)).is_rational_function(u)
        and sp.simplify(alpha(zD)).is_rational_function(q),
        "alpha_C is a rational function of sqrt(q), alpha_D of q; c*ln q is "
        "transcendental, so no exact agreement is possible in either",
    ))

    npass = sum(1 for _, ok, _ in checks if ok)
    for n, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}: {why}")
    print(f"\n{npass}/{len(checks)} assertions pass\n")
    for nm, d in data.items():
        print(f"  {nm}: z(1)={d['z_at_1']}  z'(1)={d['z_prime_at_1']}  "
              f"bar-even={d['bar_even']}  alpha t^1={d['alpha_t1']} "
              f"t^2={d['alpha_t2']}  first dev from c*lnq at "
              f"t^{d['first_deviation_order_from_c_lnq']}")

    w = WitnessBuilder("qbeta-holonomy-t2-is-a-bar-symmetry-test",
                       engine="python+sympy", output_dir=HERE,
                       _script_path=__file__)
    w.set_description(
        "The branch-3 holonomy t^2 acceptance test is a BAR-SYMMETRY test in "
        "disguise. alpha's t^2 coefficient is exactly 1/4 + z'(1); the c*ln q "
        "prediction is 1/4; so alpha is second-order logarithmic iff "
        "z'(1) = 0 — and bar-evenness FORCES z'(1) = 0 (differentiate "
        "z(1/q) = z(q) at the bar fixed point q=1). z_C is bar-even, z_D is "
        "not. So convention D failing the t^2 test is NOT independent evidence "
        "against the 2026-08-15 ruling; it restates the already-known fact that "
        "z_D is not bar-even. Corollary: acceptance-test part 1 has no "
        "discriminating power for route 5, since it tests the Markov parameter "
        "rather than the holonomy hypothesis. Neither convention is a "
        "logarithm: alpha is ALGEBRAIC (rational in sqrt q under C, in q under "
        "D) while c*ln q is transcendental, and alpha_C already deviates at "
        "t^3.")
    w.set_content_block("prop:q-beta-cos-resummation")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_parameter("q0_value", str(q_at()))
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why}
                          for n, ok, why in checks])
    w.add_data("per_convention", data)
    w.add_data("verdict", (
        "DEFLATION. The t^2 tension recorded in qou-pdix entry (6) is not an "
        "independent objection to convention D — it is bar-evenness restated. "
        "Acceptance-test part 1 is therefore not a test of route 5; parts 2 "
        "and 3 (the -1/4 of Re(log-gap) with the discarded i*pi, and a value "
        "below 1) remain the real test."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save()
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
