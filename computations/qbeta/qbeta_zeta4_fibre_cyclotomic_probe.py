#!/usr/bin/env python3
"""qbeta_zeta4_fibre_cyclotomic_probe.py — bean 0zr0, fibre-Laurent leg:
the ζ₄-residue route tested at the level where it is NOT vacuous.

The companion probe (`qbeta_zeta4_faithful_odd_probe.py`,
`docs/audits/2026-07-04-fixed-ring-vacuity-ladder-membership.md`) proved
that at the s-adic / formal-disk level the ζ₄ / odd-degree grading is
VACUOUS (Fix(σ) = ℚ(√3)[[ũ]] = ℚ(√3)[[h²]]; ĥ = q+q⁻¹ ∈ ℚ[[h²]]). The
verdict there: "genuine ζ₄-faithfulness must be imposed at the
Laurent/Habiro level where odd-degree support is a real constraint."

This probe does exactly that, on the actual Q_β carrier — the bar-odd
part (under q ↦ q⁻¹) of the net decay-width Laurent polynomial
Δ_net(q) = Δ(neutron) − Δ(proton):

    Δ_odd(q) = ½(Δ_net(q) − Δ_net(q⁻¹)) = num(q) / (4 q⁷).

Two exact, falsifiable questions (no fit, no s-expansion — pure Laurent
polynomial algebra in q):

  (Q1) ζ₄-faithful GRADING: is Δ_odd supported on odd powers of q (the
       ±i isotypes of the ζ₄ action q ↦ ζ₄q)? Equivalently num(q) even
       in q, i.e. num(−q) = num(q).

  (Q2) ζ₄-RESIDUE sharpening (the descent audit's specific claim that the
       shared ζ₄=i residue is Φ₄ = q²+1): does Φ₄ divide num(q)?

Result (recorded as assertions):
  (Q1) TRUE  — num is a polynomial in q²; with the q⁷ denominator the
       carrier is odd-q-degree supported. The grading holds.
  (Q2) FALSE — num factors as (q−1)(q+1)·R₁₂ over ℚ; the only cyclotomic
       divisors are Φ₁, Φ₂ (⇒ q²−1), NOT Φ₄. The Φ₄-residue sharpening
       is refuted. This is a scope-(b) STRUCTURAL exclusion: the cited
       invariant is the exact ℚ[q] factorisation (an exact-arithmetic
       impossibility, not a numerical miss).

The substance of the odd carrier is the non-cyclotomic palindromic
degree-12 factor R₁₂ = q¹²−4q¹⁰+6q⁸−10q⁶+6q⁴−4q²+1 — recorded as the open
object where any residual fibre-level ζ₄/Habiro structure would have to
live (its relation to the underlying 14-strand net braid's knot invariant
is not pursued here).

All exact (ℤ[q]); audit-only; no wiring; nothing fitted.

Emits `qbeta-zeta4-fibre-cyclotomic.witness.json`.

Usage:
    python3 -u qbeta/qbeta_zeta4_fibre_cyclotomic_probe.py 2>&1 | tee /tmp/zeta4_fibre.log
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp  # noqa: E402
from sympy import cyclotomic_poly  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta_ck_sseries_exact_rational import q, load_net_symbolic  # noqa: E402


def main() -> int:
    print("=" * 74)
    print(" 0zr0 fibre leg — ζ₄ grading (Q1) + Φ₄ residue (Q2) on the Q_β carrier")
    print("=" * 74)

    dnet = sp.cancel(sp.simplify(load_net_symbolic("neutron"))
                     - sp.simplify(load_net_symbolic("proton")))
    dbar = dnet.subs(q, 1 / q)
    odd = sp.cancel((dnet - dbar) / 2)
    num, den = sp.fraction(sp.cancel(odd))
    num = sp.Poly(sp.expand(num), q)
    print(f"  Δ_odd = ({sp.expand(num.as_expr())}) / ({sp.expand(den)})")

    # (Q1) ζ₄-faithful grading: carrier on odd powers of q.
    # num even in q  AND  den = const·q^odd  ⇒  carrier odd-q-degree supported.
    num_even = sp.simplify(num.as_expr().subs(q, -q) - num.as_expr()) == 0
    den_q_exp = sp.Poly(sp.fraction(sp.cancel(1 / den))[1], q).degree() \
        if den != 0 else 0
    # den is 4*q^7 → the q-exponent is 7 (odd)
    den_deg = sp.degree(sp.denom(sp.cancel(odd)), q)
    carrier_odd_support = bool(num_even and (den_deg % 2 == 1))
    print(f"  (Q1) num(−q)=num(q): {bool(num_even)};  den q-degree {den_deg} "
          f"(odd) ⇒ carrier odd-q-degree supported: {carrier_odd_support}")

    # (Q2) Φ₄ = q²+1 residue + full cyclotomic content.
    phi4 = q**2 + 1
    phi4_divides = sp.rem(num.as_expr(), phi4, q) == 0
    cyclo = [n for n in range(1, 2 * num.degree() + 2)
             if sp.rem(num.as_expr(), cyclotomic_poly(n, q), q) == 0]
    res = num.as_expr()
    for n in cyclo:
        Phi = cyclotomic_poly(n, q)
        while (sp.rem(res, Phi, q) == 0
               and sp.degree(res, q) >= sp.degree(Phi, q)):
            res = sp.quo(res, Phi, q)
    res = sp.factor(res)
    print(f"  (Q2) Φ₄ | num: {bool(phi4_divides)};  cyclotomic divisors: "
          f"Φ_{cyclo};  non-cyclotomic residual: {res}")
    print(f"       full factorisation: {sp.factor(num.as_expr())}")

    w = WitnessBuilder("qbeta-zeta4-fibre-cyclotomic", engine="sympy")
    w.set_description(
        "Bean 0zr0 fibre-Laurent leg: the Q_beta (bar-odd) carrier of the "
        "net decay-width Laurent polynomial has ζ₄-faithful odd-q-degree "
        "support (Q1 TRUE) but is NOT divisible by Φ₄=q²+1 (Q2 FALSE) — the "
        "ζ₄-residue sharpening is refuted (scope b, exact factorisation).")
    w.add_parameter("carrier", "Δ_odd = ½(Δ_net(q) − Δ_net(1/q)), Δ_net = neutron − proton")
    w.add_data("odd_numerator", str(sp.expand(num.as_expr())))
    w.add_data("odd_denominator", str(sp.expand(den)))
    w.add_data("full_factorisation", str(sp.factor(num.as_expr())))
    w.add_data("cyclotomic_divisors", cyclo)
    w.add_data("non_cyclotomic_residual", str(res))
    w.add_data("phi4_divides", bool(phi4_divides))
    w.add_data("verdict",
               "Q1 (ζ₄ grading / odd-q-degree support): TRUE. "
               "Q2 (Φ₄=q²+1 residue): FALSE — only Φ₁,Φ₂ divide (⇒ q²−1); "
               "the ζ₄-residue route is refuted at the fibre level "
               "(scope b: proved exact-arithmetic impossibility). Open "
               "residue: the non-cyclotomic palindromic R₁₂.")
    w.add_assertion(
        name="carrier_zeta4_odd_degree_supported",
        computed=1.0 if carrier_odd_support else 0.0,
        expected=1.0, tolerance=0.0,
        unit="bool (1 = Δ_odd supported on odd powers of q)",
        source="num(−q)=num(q) and den=4q⁷ (odd q-exponent).")
    w.add_assertion(
        name="phi4_does_not_divide_carrier",
        computed=1.0 if not phi4_divides else 0.0,
        expected=1.0, tolerance=0.0,
        unit="bool (1 = Φ₄=q²+1 does NOT divide num) — the ζ₄-residue refutation",
        source="exact ℤ[q] division; cyclotomic content is Φ₁·Φ₂ only.")
    w.set_audit_only(
        "docs/audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md")
    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
