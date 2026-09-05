"""Hoefsmit eigencolumn → toroidal-Legendre ladder probe (P1 of the
parabolic-cylinder / toroidal channel-interpolation audit, PR #3445).

Question (audit §6 P1): does the Hoefsmit 2×2 channel-mixing structure
degenerate, under q → 1 with the content/axial-distance variable playing the
role of the Legendre argument index, to the contiguous/ladder structure of the
toroidal Legendre family P^μ_{ν−1/2} — i.e. is the HALF-INTEGER DEGREE SHIFT
(the toroidal signature) derived rather than fitted?

What is verified symbolically (sympy, exact):

(1) CLASSICAL LAYER (q = 1, Young orthogonal form). The adjacent-transposition
    block at axial distance d is
        M(d) = [[1/d, s], [s, -1/d]],   s = sqrt(d^2-1)/d,
    with eigenvectors (sqrt(d+1), sqrt(d-1)) ↔ +1 and
    (sqrt(d-1), -sqrt(d+1)) ↔ -1. The channel-mixing amplitude is s.

(2) TOROIDAL LOCUS. The associated-Legendre order-ladder factor is
    L(n, μ)^2 = (n-μ)(n+μ+1). Matching (d^2-1) = (n-μ)(n+μ+1) IDENTICALLY in
    d, with n = d+α and μ = β constants, forces
        α = -1/2  (half-integer DEGREE shift — the toroidal ν-1/2),
        β = 1/2   (up to the Legendre reflection β ↦ -β-1).
    So the toroidal half-integer degree is DERIVED from the Hoefsmit mixing
    structure, not imposed.

(3) q-LAYER (corpus convention, frobenius-lepton-meson-bridge). With
    a_ρ = h/(1-q^{-2ρ}), h = q - q^{-1}, the binding amplitude satisfies
        b^2 = a_ρ a_{-ρ} + 1 = ([ρ-1][ρ+1])/[ρ]^2 = ([ρ]^2 - 1)/[ρ]^2,
    the exact q-deformation of s^2 = (d^2-1)/d^2. The bracket identity
    [d-1][d+1] = [d]^2 - 1 holds, and the uniqueness computation of (2)
    q-deforms verbatim: [d+α-β][d+α+β+1] = [d]^2 - 1 identically in d forces
    q^{2α+1} = 1 (α = -1/2) and q^{2β+1} + q^{-(2β+1)} = q^2 + q^{-2}
    (β = 1/2 up to reflection). The half-integer shift SURVIVES q-deformation.

Scope discipline: this is a LADDER-COEFFICIENT identification — a structural
(a)-scoped match, NOT a full eigenfunction transform and NOT a numerical fit.
No archimedean evaluation, no q_0, no observables.
"""
import json
import os

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

# ---------------------------------------------------------------- (1) classical
d = sp.symbols("d", positive=True)
# factored radical form sqrt(d-1)*sqrt(d+1) (== sqrt(d^2-1) for d > 1) so that
# sympy combines the products in the eigencolumn check exactly
s = sp.sqrt(d - 1) * sp.sqrt(d + 1) / d
M = sp.Matrix([[1 / d, s], [s, -1 / d]])

v_plus = sp.Matrix([sp.sqrt(d + 1), sp.sqrt(d - 1)])
v_minus = sp.Matrix([sp.sqrt(d - 1), -sp.sqrt(d + 1)])

eig_plus_ok = sp.simplify(M * v_plus - v_plus) == sp.zeros(2, 1)
eig_minus_ok = sp.simplify(M * v_minus + v_minus) == sp.zeros(2, 1)
mixing_sq = sp.simplify(s**2 - (d**2 - 1) / d**2) == 0

# ------------------------------------------------- (2) toroidal locus uniqueness
alpha, beta = sp.symbols("alpha beta", real=True)
n = d + alpha
ladder_sq = (n - beta) * (n + beta + 1)
# require ladder_sq == d^2 - 1 identically in d
diff_poly = sp.expand(ladder_sq - (d**2 - 1))
coeffs = sp.Poly(diff_poly, d).all_coeffs()
sols = sp.solve(coeffs, [alpha, beta], dict=True)
# expected: alpha = -1/2, beta in {1/2, -3/2} (Legendre reflection pair)
sols_set = {(sp.nsimplify(sol[alpha]), sp.nsimplify(sol[beta])) for sol in sols}
expected_set = {(sp.Rational(-1, 2), sp.Rational(1, 2)),
                (sp.Rational(-1, 2), sp.Rational(-3, 2))}
toroidal_locus_forced = sols_set == expected_set

# verify the locus explicitly: (d^2 - 1) = (n - 1/2)(n + 3/2) at n = d - 1/2
locus_check = sp.simplify(
    (d - sp.Rational(1, 2) - sp.Rational(1, 2))
    * (d - sp.Rational(1, 2) + sp.Rational(1, 2) + 1) - (d**2 - 1)) == 0

# ------------------------------------------------------------------ (3) q-layer
q, rho = sp.symbols("q rho", positive=True)
h = q - 1 / q


def bkt(x):
    """q-bracket [x] = (q^x - q^-x)/(q - q^-1)."""
    return (q**x - q**(-x)) / (q - 1 / q)


a_rho = h / (1 - q**(-2 * rho))
a_neg = h / (1 - q**(2 * rho))
b_sq = sp.simplify(a_rho * a_neg + 1)

corpus_b_eq_bracket = sp.simplify(
    b_sq - (bkt(rho)**2 - 1) / bkt(rho)**2) == 0
bracket_prod_identity = sp.simplify(
    bkt(rho - 1) * bkt(rho + 1) - (bkt(rho)**2 - 1)) == 0

# q-uniqueness: [d+alpha-beta][d+alpha+beta+1] = [d]^2 - 1 identically in q^d.
# Substitute X = q^d; both sides are Laurent in X with coefficients in q^alpha,
# q^beta; match coefficients of X^2, X^0, X^-2.
X, A, B = sp.symbols("X A B", positive=True)  # A = q^alpha, B = q^beta


def bktX(shift_A_pow, shift_B_pow, extra_q_pow):
    """[d + alpha*shift_A + beta*shift_B + extra] with q^d = X."""
    fac = A**shift_A_pow * B**shift_B_pow * q**extra_q_pow
    return (X * fac - 1 / (X * fac)) / (q - 1 / q)


lhs_q = bktX(1, -1, 0) * bktX(1, 1, 1)          # [d+α-β]·[d+α+β+1]
rhs_q = ((X - 1 / X) / (q - 1 / q))**2 - 1       # [d]^2 - 1
diff_q = sp.together(sp.expand(lhs_q - rhs_q))
num_q = sp.expand(sp.numer(diff_q))
poly_X = sp.Poly(num_q, X)
q_coeff_eqs = [sp.Eq(c, 0) for c in poly_X.all_coeffs() if c != 0]
q_sols = sp.solve(q_coeff_eqs, [A, B], dict=True)
# expected positive-branch solutions: A = q^(-1/2), B in {q^(1/2), q^(-3/2)}
q_expected = {(1 / sp.sqrt(q), sp.sqrt(q)), (1 / sp.sqrt(q), q**sp.Rational(-3, 2))}
q_sols_set = {(sp.powsimp(sol[A]), sp.powsimp(sol[B])) for sol in q_sols
              if sol[A].is_positive is not False}
q_toroidal_locus_forced = all(
    any(sp.simplify(sa - ea) == 0 and sp.simplify(sb - eb) == 0
        for (ea, eb) in q_expected)
    for (sa, sb) in q_sols_set) and len(q_sols_set) >= 1

assertions = {
    "classical_eigencolumn_plus": bool(eig_plus_ok),
    "classical_eigencolumn_minus": bool(eig_minus_ok),
    "classical_mixing_sq_(d2-1)/d2": bool(mixing_sq),
    "toroidal_locus_forced_alpha_-1/2_beta_1/2": bool(toroidal_locus_forced),
    "toroidal_locus_explicit_check": bool(locus_check),
    "corpus_bsq_eq_bracket_ratio": bool(corpus_b_eq_bracket),
    "bracket_identity_[d-1][d+1]=[d]^2-1": bool(bracket_prod_identity),
    "q_toroidal_locus_forced": bool(q_toroidal_locus_forced),
}

verdict = (
    "TOROIDAL HALF-INTEGER DEGREE SHIFT DERIVED, NOT FITTED: matching the "
    "Hoefsmit channel-mixing amplitude sqrt(d^2-1)/d against the associated-"
    "Legendre order-ladder factor sqrt((n-mu)(n+mu+1)) identically in the "
    "axial distance d forces degree n = d - 1/2 (the toroidal nu - 1/2) and "
    "order mu = 1/2, up to the Legendre reflection mu -> -mu-1. The corpus "
    "Hoefsmit convention a_rho = h/(1-q^{-2rho}), b = sqrt(a_rho a_{-rho}+1) "
    "satisfies b^2 = [rho-1][rho+1]/[rho]^2 exactly (h = q - q^{-1}), and the "
    "forcing computation q-deforms verbatim (q^{2alpha+1} = 1). SCOPE (a): "
    "ladder-coefficient identification only — supports the toroidal channel-"
    "interpolation lead structurally; it is NOT a full eigenfunction "
    "transform, NOT wired to production, and licenses no numerical claim."
)

witness = {
    "computation": "hoefsmit_toroidal_ladder_probe",
    "description": (
        "P1 of the parabolic-cylinder/toroidal channel-interpolation audit: "
        "symbolic verification that the Hoefsmit 2x2 channel-mixing structure "
        "forces the toroidal half-integer Legendre degree shift (classical and "
        "q-bracket layers)."
    ),
    "discipline": "no fit; sympy symbolic exact; fibre-level only (no q_0, no observables); (a)-scoped.",
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "classical_block": str(M),
        "eigencolumns": "(sqrt(d+1), sqrt(d-1)) <-> +1; (sqrt(d-1), -sqrt(d+1)) <-> -1",
        "ladder_match_solutions_classical": sorted(str(t) for t in sols_set),
        "ladder_match_solutions_q": sorted(str(t) for t in q_sols_set),
        "b_squared_simplified": str(b_sq),
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "hoefsmit-toroidal-ladder-probe.witness.json")
# Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
# `os.replace` it into position. `open(..., "w")` TRUNCATES before the
# dump runs, so any exception in between leaves the committed witness
# empty or partial -- the shape that emptied 22 witnesses to zero bytes
# in one `producer_importability_audit` run. `os.replace` is atomic on
# POSIX within a filesystem, hence a SIBLING temp file.
_wpath_sidu = out
_wtmp_sidu = str(_wpath_sidu) + ".tmp"
with open(_wtmp_sidu, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

_os_sidu.replace(_wtmp_sidu, _wpath_sidu)
for k, v in assertions.items():
    print(f"  {k}: {'PASS' if v else 'FAIL'}")
print(f"\nallPassed: {witness['allPassed']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
