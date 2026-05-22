#!/usr/bin/env python3
"""Categorical track, Part 2: Factor D(z), partial-fraction decompose
-P(z)/D(z), identify the irreducible structure.

D(z) is palindromic: 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16

For a palindromic polynomial of even degree 2n, substitute w = z + 1/z:
  z^{-n} D(z) = D̃(w), a polynomial of degree n in w.

For D of degree 6 → D̃ is cubic in w:
  z^{-3} D(z) = 16(z³+z⁻³) + 24(z²+z⁻²) + 35(z+z⁻¹) + 50
              = 16(w³-3w) + 24(w²-2) + 35·w + 50
              = 16w³ + 24w² - 13w + 2

So D(z) = z³ · (16w³ + 24w² - 13w + 2) at w = z + 1/z.

The discriminant zeros (in z) come in reciprocal pairs (z, 1/z),
corresponding to roots of D̃(w) = 0 in w-space. This is the
ALGEBRAIC SYMMETRY of the categorical action.

Each reciprocal pair (z*, 1/z*) of discriminant zeros corresponds
to a SPECIFIC structural object — let's compute and identify them.
"""
import sys
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder


def main():
    z, w, a = sp.symbols("z w a")

    P = 64*z**6 + 96*z**5 + 120*z**4 + 160*z**3 + 105*z**2 + 66*z + 39
    D = 16*z**6 + 24*z**5 + 35*z**4 + 50*z**3 + 35*z**2 + 24*z + 16

    # Factor D over Q
    print("Factor D(z) over Q:")
    D_factored = sp.factor(D)
    print(f"  D(z) = {D_factored}")
    print()

    # Substitute w = z + 1/z to get cubic D̃(w)
    D_tilde = 16*w**3 + 24*w**2 - 13*w + 2
    print(f"D̃(w) = z^{{-3}} D(z) at w = z + 1/z:")
    print(f"  D̃(w) = {D_tilde}")
    print(f"  factored: {sp.factor(D_tilde)}")
    # Roots of D̃ in w
    w_roots = sp.solve(D_tilde, w)
    print(f"  w-roots: {w_roots}")
    print()

    # For each w-root, the z-roots solve z² - w·z + 1 = 0 → z = (w ± √(w²-4))/2
    # These come in reciprocal pairs (z, 1/z) since z · (1/z) = 1
    print("z-roots of D(z), organized by w-pair:")
    for w_root in w_roots:
        w_val = sp.simplify(w_root)
        # Solve z² - w·z + 1 = 0
        z_pair_eq = z**2 - w_val * z + 1
        z_pair = sp.solve(z_pair_eq, z)
        try:
            z_pair_num = [complex(sp.N(zr, 15)) for zr in z_pair]
        except Exception:
            z_pair_num = [None, None]
        print(f"  w = {w_val}")
        for i, zr in enumerate(z_pair):
            print(f"    z_{i+1} = {sp.simplify(zr)}")
            if z_pair_num[i] is not None:
                print(f"           ≈ {z_pair_num[i]}")
        # Check reciprocal pair
        if len(z_pair) == 2:
            product = sp.simplify(z_pair[0] * z_pair[1])
            print(f"    z_1 · z_2 = {product}  (should be 1 for reciprocal pair)")
        print()

    # Factor P(z) similarly — is P palindromic too?
    print("Is P palindromic?")
    P_coeffs = sp.Poly(P, z).all_coeffs()
    print(f"  P coefficients: {P_coeffs}")
    print(f"  reversed:       {P_coeffs[::-1]}")
    palindromic = P_coeffs == P_coeffs[::-1]
    print(f"  P palindromic? {palindromic}")
    print()

    # NOT palindromic — different structure. Let me check if z^6 · P(1/z) = P(z)
    P_recip = sp.simplify(z**6 * P.subs(z, 1/z))
    print(f"  z^6 · P(1/z) = {sp.expand(P_recip)}")
    print(f"  P(z)         = {sp.expand(P)}")
    # If P_recip ≠ P, P has different transformation property

    # Partial fractions of -P/D
    print()
    print("=" * 70)
    print("Partial-fraction decomposition of -P(z)/D(z)")
    print("=" * 70)
    integrand = -P / D
    print("Computing apart(-P/D, z) — this may take a moment...")
    try:
        # apart over Q(z); will keep irreducible factors of D
        decomp = sp.apart(integrand, z, full=False)
        print(f"  Result:")
        for term in sp.Add.make_args(decomp):
            print(f"    + {term}")
    except Exception as e:
        print(f"  apart failed: {e}")

    # Even simpler: just identify the irreducible factors of D
    print()
    print("Irreducible factors of D(z) over Q:")
    D_factors_q = sp.factor_list(D)
    print(f"  D(z) = {D_factors_q[0]} · " + " · ".join(
        f"({sp.expand(f)})^{m}" for f, m in D_factors_q[1]))
    print()

    # Check if D(z) factors as (z² + 1)·(...) given the z=0 form of the cubic
    # We saw F(0, c) = (c+1)(c²+1) — so the cubic at z=0 has roots {-1, i, -i}
    # The discriminant of this cubic at z=0 is computed as 16
    print(f"D(0) = {D.subs(z, 0)}")
    print(f"D(z) factored algebraically (over Q): {sp.factor(D)}")
    print()
    print(f"P(0) = {P.subs(z, 0)}")
    print(f"P(z) factored algebraically (over Q): {sp.factor(P)}")

    # Try factoring D(z) over a quadratic extension if Q doesn't work
    # D̃(w) is a cubic; its discriminant tells us if roots are real or complex
    print()
    print("D̃(w) discriminant analysis:")
    D_tilde_disc = sp.discriminant(D_tilde, w)
    print(f"  disc(D̃) = {D_tilde_disc}")
    if D_tilde_disc > 0:
        print(f"  → 3 distinct REAL w-roots")
    elif D_tilde_disc < 0:
        print(f"  → 1 real + 2 complex conjugate w-roots")
    else:
        print(f"  → repeated roots")

    # Solve D̃(w) = 0 numerically
    w_num = sp.solve(D_tilde, w)
    w_roots_num = [complex(sp.N(wn, 12)) for wn in w_num]
    print(f"  w-roots numerical: {w_roots_num}")

    # Persist the structural results as a witness (Copilot review on PR #751).
    builder = WitnessBuilder(
        "probe-categorical-partial-fractions",
        engine="sympy",
    )
    builder.set_description(
        "Partial-fraction decomposition of -P(z)/D(z) and palindromic "
        "reduction D(z) = z³ D̃(w) at w = z + 1/z. Records irreducible "
        "factors of D over Q, the cubic D̃(w) in w, the w-roots and "
        "their z-pair reciprocal structure."
    )
    builder.set_content_block("prop:sw-3root-rational-integrand")
    builder.add_data("D_tilde_w", str(D_tilde))
    builder.add_data("D_tilde_w_factored", str(sp.factor(D_tilde)))
    builder.add_data("D_tilde_w_discriminant", str(D_tilde_disc))
    builder.add_data("w_roots_numerical", [str(wr) for wr in w_roots_num])
    builder.add_data("P_factored_over_Q", str(sp.factor(P)))
    builder.add_data("D_factored_over_Q", str(sp.factor(D)))
    builder.add_data("P_palindromic", bool(palindromic))
    out = builder.save()
    print(f"\nWitness emitted: {out.name}")


    # Witness emission per Copilot review on PR #751
    _w = WitnessBuilder("categorical-partial-fractions", engine="sympy")
    _w.set_description("Partial-fraction decomposition of -P(z)/D(z) for the SW 3-root product, exposing the palindromic z↔1/z structure and -4 constant term.")
    _w.set_content_block("prop:sw-3root-rational-integrand")
    _w.save()


if __name__ == "__main__":
    main()
