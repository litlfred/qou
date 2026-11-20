#!/usr/bin/env python3
"""
H² concrete-test probe: is the Bring color-tube form `1/(1 − h_q · q_0^10)`
the resummed all-orders form of the additive canonical + Yekutieli
`5/2 + (3/4 − G)·h²` at leading h² order?

Per `docs/audits/2026-05-23-lambda-scale-canonical-unification.md` §"Concrete
test" — informs whether Path B and Path C are the same mechanism truncated
differently (B = leading h² of C-resummed) or independent (need explicit
double-counting subtraction).

The h-expansion is around `q = 1` (i.e. h_q = q − q^{-1} → 0), with q
treated as the natural deformation variable parameterised by h. Both q
and q^10 carry h-dependence — q is a root of `q² − h·q − 1 = 0`, so
q = (h + √(h² + 4))/2, and q^n has its own h-expansion.

We compare the leading h² coefficient of:
  • `5/2 + (3/4)·h²`           (Family A, canonical Wedderburn, PROVED)
  • `5/2 + (3/4 − G)·h²`       (canonical + Yekutieli additive, OPTION B)
  • `1/(1 − h · q^10)`         (Bring color-tube Φ_q pentagon, OPTION C)

via SYMBOLIC Taylor expansion through sympy at high precision, then
sanity-check the q_0 numerical value matches the h² expansion's q_0 truncate.

Expected outcomes (per audit's hypotheses):
  - If the h² coefficient of `1/(1 − h·q^10)` matches `3/4 − G`, then
    Path C IS the resummed Path B at leading order → no double-counting.
  - If they don't match, the two mechanisms are categorically independent.

Also reports the h^4, h^6, h^8 coefficients of `1/(1 − h·q^10)` so the
h⁴ derivation (Option A — derive from 13 drivers) has a concrete target
coefficient to aim for.

Witness: `lambda-scale-h2-concrete-test.witness.json`
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 80


def expand_in_h(expr_q, n_terms: int = 8) -> list:
    """Expand `expr_q` (a sympy expression in symbol q) as a Taylor series
    in h = q − q^{-1} around h = 0.

    Strategy: substitute q = (h + √(h² + 4))/2 (the positive root of
    q² − h·q − 1 = 0, so q − q⁻¹ = h), then series-expand in h around 0.
    """
    q, h = sp.symbols('q h', positive=True)
    # q expressed as a function of h: q² − h·q − 1 = 0  ⇒  q = (h + √(h²+4))/2
    q_of_h = (h + sp.sqrt(h ** 2 + 4)) / 2
    expr_h = sp.simplify(expr_q.subs(q, q_of_h))
    series = sp.series(expr_h, h, 0, n_terms).removeO()
    # Extract coefficients as a list
    poly = sp.Poly(series, h)
    coeffs = poly.all_coeffs()
    coeffs.reverse()  # so coeffs[k] is the h^k coefficient
    return [sp.simplify(c) for c in coeffs]


def main() -> int:
    q, h = sp.symbols('q h', positive=True)
    G_sym = sp.Symbol('G')  # Catalan, left symbolic
    G_mp = mp.catalan
    Q0 = Q_MP
    h0 = Q0 - 1 / Q0
    h0_sq = h0 * h0
    h0_fourth = h0_sq * h0_sq

    # ── Family A canonical: `5/2 + (3/4) h²` ──────────────────────
    # Already in h directly; trivial expansion.
    family_a_coeffs = [sp.Rational(5, 2), 0, sp.Rational(3, 4), 0, 0, 0, 0, 0]

    # ── canonical + Yekutieli additive: `5/2 + (3/4 − G) h²` ─────
    canonical_yek_coeffs = [
        sp.Rational(5, 2), 0, sp.Rational(3, 4) - G_sym, 0, 0, 0, 0, 0
    ]

    # ── Bring color-tube: `1/(1 − h · q^10)` ──────────────────────
    bring_expr = 1 / (1 - h * q ** 10)
    bring_coeffs = expand_in_h(bring_expr, n_terms=9)

    print("=" * 76)
    print("h-expansion of three candidate linking_weight forms")
    print("=" * 76)
    print()
    print(f"{'h^k':<6} {'Family A':<22} {'+Yek (option b)':<24} {'Bring (option c)':<30}")
    print(f"{'---':<6} {'-'*22:<22} {'-'*24:<24} {'-'*30:<30}")
    for k, (a, b, c) in enumerate(zip(family_a_coeffs, canonical_yek_coeffs,
                                     bring_coeffs)):
        print(f"h^{k:<3} {str(a):<22} {str(b):<24} {str(c):<30}")
    print()

    # ── Sanity check at q_0 ──────────────────────────────────────
    print("Numerical check at q_0:")
    fa_val = sp.lambdify((), 5*sp.Rational(1,2) + sp.Rational(3,4)*h0**2)
    bring_val_q0 = float(1 / (1 - h0 * Q0 ** 10))
    print(f"  Family A          @ q_0: {float(mp.mpf('5')/2 + mp.mpf('3')/4 * h0_sq):.15f}")
    print(f"  canonical+Yek     @ q_0: {float(mp.mpf('5')/2 + (mp.mpf('3')/4 - G_mp) * h0_sq):.15f}")
    print(f"  Bring color-tube  @ q_0: {bring_val_q0:.15f}")
    print()

    # ── The MAIN COMPARISON: h² coefficient ──────────────────────
    bring_h2_coeff = bring_coeffs[2]
    canonical_yek_h2 = sp.Rational(3, 4) - G_sym
    family_a_h2 = sp.Rational(3, 4)

    print("=" * 76)
    print("H² COEFFICIENT COMPARISON (the load-bearing concrete test)")
    print("=" * 76)
    print(f"  Family A h² coeff           = {family_a_h2}")
    print(f"  canonical + Yek h² coeff    = {canonical_yek_h2}  ≈ {float(sp.Rational(3,4)) - float(G_mp):.6f}")
    print(f"  Bring color-tube h² coeff   = {bring_h2_coeff}")
    bring_h2_val = float(bring_h2_coeff)
    print(f"                              ≈ {bring_h2_val:.6f}")
    print()
    diff = bring_h2_val - (float(sp.Rational(3, 4)) - float(G_mp))
    print(f"  Bring h² − (Family A + Yek h²) = {diff:+.6f}")
    print()

    bring_eq_family_a_yek = abs(bring_h2_val - (3/4 - float(G_mp))) < 1e-10
    bring_eq_family_a_only = abs(bring_h2_val - 3/4) < 1e-10

    if bring_eq_family_a_yek:
        print("✓ MATCH: Bring h² coeff = (3/4 − G). Path C IS the resummed Path B.")
        print("  → No double-counting; Path C contains canonical + Yekutieli at leading h².")
    elif bring_eq_family_a_only:
        print("✓ MATCH: Bring h² coeff = 3/4 (no Yekutieli). Path C extends Family A only.")
        print("  → Yekutieli per-cell IS independent of Bring color-tube.")
    else:
        print("✗ NO MATCH: Bring color-tube h² coeff differs from canonical + Yekutieli.")
        print("  → They are categorically distinct mechanisms.")
        print(f"  Bring h² coeff = {float(bring_h2_coeff):.10f}")
        print(f"  (3/4 − G) =       {float(sp.Rational(3,4)) - float(G_mp):.10f}")
        print(f"  (3/4) =           {float(sp.Rational(3,4)):.10f}")

    # ── H⁴ COEFFICIENT — concrete target for Option A derivation ──
    bring_h4_coeff = bring_coeffs[4]
    print()
    print("=" * 76)
    print("H⁴ COEFFICIENT — target for Option A categorical derivation")
    print("=" * 76)
    bring_h4_val = float(bring_h4_coeff)
    print(f"  Bring h⁴ coeff (symbolic): {bring_h4_coeff}")
    print(f"  Bring h⁴ coeff (numeric):  {bring_h4_val:.10f}")
    print()
    print("  Empirical residual α (CODATA back-solve − Bring) / h⁴ ≈ 1.011")
    print("  (from lambda_scale_refinement_h4_correction_bring.py — retired empirical fit)")
    print()
    print(f"  Combined target h⁴ coeff = Bring h⁴ + 1.011 = {bring_h4_val + 1.011:.6f}")
    print("  (or 1·h⁴ if we model the residual as an additive +1·h⁴ correction)")
    print()
    print("Categorical drivers (13-driver menu, see")
    print("docs/audits/2026-05-23-lambda-scale-canonical-unification.md):")
    print("  (i)   iterated compact-q-dilog Φ_q(q^k z)/Φ_q(z)")
    print("  (ii)  Φ_q power series expansion")
    print("  (iii) Rogers pentagon Li_2^q")
    print("  (iv)  Yang-Baxter higher-iter")
    print("  (v)   Hexagon equations")
    print("  (vi)  Frobenius reciprocity")
    print("  (vii) 6j Biedenharn-Elliott")
    print("  (viii) Modular dual")
    print("  (ix)  KLR positivity")
    print("  (x)   MacMahon master theorem (partition algebra at H_4)")
    print("  (xi)  Lobachevsky-Catalan")
    print("  (xii) Chern-Simons-Ohtsuki series")
    print("  (xiii) Crystal-graph Kashiwara")
    print()

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder("lambda-scale-h2-concrete-test", engine="sympy+mpmath")
    w.set_description(
        "Concrete test per 2026-05-23-lambda-scale-canonical-unification.md "
        "§'Concrete test': symbolic h-expansion of `1/(1 − h_q · q_0^10)` "
        "around h = 0 (with q = (h + √(h²+4))/2). Compares h² coefficient to "
        "canonical Family A `3/4` and to canonical + Yekutieli additive "
        "`3/4 − G`. Reports h⁴ coefficient as concrete target for Option A "
        "h⁴ categorical derivation. Informs whether Path C (Bring color-tube) "
        "IS the resummed Path B (additive Yekutieli) at leading order."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("dps", 80)
    w.add_parameter("expansion_variable", "h = q − q^{-1} around h = 0")
    w.add_parameter("q_of_h_substitution", "q = (h + √(h²+4))/2")
    w.add_data("family_a_coeffs", [str(c) for c in family_a_coeffs])
    w.add_data("canonical_plus_yek_coeffs", [str(c) for c in canonical_yek_coeffs])
    w.add_data("bring_color_tube_coeffs", [str(c) for c in bring_coeffs])
    w.add_data("bring_h2_coeff_symbolic", str(bring_h2_coeff))
    w.add_data("bring_h2_coeff_numeric", f"{bring_h2_val:.20f}")
    w.add_data("canonical_plus_yek_h2_numeric",
               f"{float(sp.Rational(3,4)) - float(G_mp):.20f}")
    w.add_data("h2_match_canonical_plus_yek", bring_eq_family_a_yek)
    w.add_data("h2_match_family_a_only", bring_eq_family_a_only)
    w.add_data("h2_difference_bring_minus_canonical_yek", f"{diff:.20f}")
    w.add_data("bring_h4_coeff_symbolic", str(bring_h4_coeff))
    w.add_data("bring_h4_coeff_numeric", f"{bring_h4_val:.20f}")
    w.add_data("empirical_residual_alpha_at_h4", "1.011")
    w.add_data("conclusion", (
        "PATH C and PATH B are CATEGORICALLY DISTINCT mechanisms at "
        "leading h² order. The Bring color-tube h² coefficient does "
        "NOT equal (3/4 − G); the two mechanisms cannot be unified by "
        "the simple 'resummed Yekutieli' hypothesis."
        if not (bring_eq_family_a_yek or bring_eq_family_a_only)
        else
        f"Bring h² coeff matches {'(3/4 − G)' if bring_eq_family_a_yek else '3/4'} — "
        "Path C resums Path B (or extends Family A) at leading order. "
        "Higher orders may still differ."
    ))

    w.add_assertion(
        "h2_concrete_test_completed",
        computed=int(bring_eq_family_a_yek or bring_eq_family_a_only),
        expected=1,
        tolerance=None,
        source=(
            "Concrete test of whether Bring color-tube `1/(1 − h·q^10)` "
            "reproduces canonical + Yekutieli at h² order. Passes iff "
            "the leading h² coefficient matches either Family A (3/4) "
            "or canonical+Yekutieli (3/4 − G)."
        ),
    )

    out = w.save()
    print(f"Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
