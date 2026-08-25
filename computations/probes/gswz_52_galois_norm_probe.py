"""GZ Galois triple-product integrality for the 5_2 series — exact norm check + E-factor shape match.

Beans qou-xx9f (the (287) normalization gap) + qou-9p9y. Scope-(a);
no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 15).

SOURCE ([26] = GZ "Knots, Perturbative Series and Quantum Modularity",
SIGMA 20 (2024) 055, library/arxiv-2111.06645v3/2111.06645v3.pdf, §9 end):

1. For 4_1: sqrt(3)*Phi(h)*Phi(-h) = -sqrt(-3)*Phi^(1)(h)*Phi^(2)(h)
   lies in Z[1/3][[e^{-h}-1]]; "we expect, and have checked
   numerically, that the same is also true for 5_2 if one multiplies
   all three series Phi^(5_2, sigma_i) (i = 1,2,3)" — the GALOIS
   TRIPLE PRODUCT is integral (away from small primes).
2. The single-series correction factor
   E^(K,sigma)(h) = exp(-sum_{r>=1} |B_{r+1}|/(r+1)! * C_r * h^r)
   makes Phi(h)*E(h) integral WITHOUT the bar partner, and "the
   corrected Phi-series can be seen as the h-deformed versions of the
   units constructed in [10]" (= the CGZ eps-units this program
   computes). Note E(h)E(-h) = 1 (odd Bernoulli structure).

WHAT THIS CHECKS (exact rational arithmetic):

1. THE TRIPLE PRODUCT: N(h) = Norm_{Q(alpha)/Q}(1 + phi1 h + phi2 h^2
   + phi3 h^3) computed exactly as det(I + M(phi1)h + M(phi2)h^2 +
   M(phi3)h^3) over the multiplication-matrix representation, from
   the printed GSWZ (282) coefficients, truncated to h^3. Check:
   every coefficient is 5-INTEGRAL (the falsifiable core for the
   5-adic harness), and the full denominator support is recorded.
   Observed support: exactly {2, 23} — the 3s cancel entirely
   (stronger than the 4_1 Z[1/3] statement) and the 23-powers enter
   per-order from the delta^{3k} normalization, consistent with
   integrality away from Delta since disc = -23.
2. E-FACTOR SHAPE MATCH (structural, recorded): the (287) mismatch
   found on this branch has EXACTLY the E-factor signature — an h^1
   term, NO h^2 term (B_3 = 0; our x^2 matched with the h^1 solve
   alone), and an h^3 residual (B_4 term). The witness records the
   implied C_1 = -12*lambda and the C_3 relation for future
   comparison with GZ §8.1 data. This upgrades xx9f candidate (b)
   from "some unprinted series factor" to "a GZ E-type unit
   deformation factor" — shape-identified, values open.
3. Norm of delta = 3*alpha - 2 equals -23 exactly (odd-degree sign;
   the discriminant-prime bookkeeping used throughout).

HONESTY: check 2 is a recorded structural identification, not a
digit-verified equality (GZ print C_r data for 4_1 in their §8.1,
not for 5_2); extracting 5_2 C_r values from our mismatch digits and
verifying them against independent data remains open on qou-xx9f.
"""

import json
import pathlib
import sys

import sympy as sp

a, h = sp.symbols("alpha h")
MINPOLY = a**3 - a**2 + 1
delta = 3 * a - 2

phi1 = (765 * a**2 - 1086 * a + 1043) / (24 * delta**3)
phi2 = (1757583 * a**2 - 2956029 * a + 2241964) / (1152 * delta**6)
phi3 = (21285784611 * a**2 - 37166037066 * a + 27969826252) / (414720 * delta**9)

checks = {}


def mult_matrix(expr):
    """3x3 rational multiplication matrix of expr in Q[alpha]/(m)."""
    M = sp.zeros(3, 3)
    for k in range(3):
        num, den = sp.fraction(sp.together(sp.expand(expr * a**k)))
        num = sp.rem(sp.expand(num), MINPOLY, a)
        denp = sp.Poly(den, a)
        if denp.degree() > 0:
            dinv = sp.invert(denp, sp.Poly(MINPOLY, a)).as_expr()
        else:
            dinv = sp.Integer(1) / den
        e = sp.rem(sp.expand(num * dinv), MINPOLY, a)
        p = sp.Poly(e, a)
        for i in range(3):
            M[i, k] = p.coeff_monomial(a**i)
    return M


M1 = mult_matrix(phi1)
M2 = mult_matrix(phi2)
M3 = mult_matrix(phi3)

# (3) norm of delta: odd degree gives N(3a-2) = -23 exactly
Nd = sp.Matrix(mult_matrix(delta)).det()
checks["norm_delta_is_minus_23"] = bool(sp.simplify(Nd + 23) == 0)

# (1) triple product = det(I + M1 h + M2 h^2 + M3 h^3), truncate to h^3
A = sp.eye(3) + M1 * h + M2 * h**2 + M3 * h**3
N = sp.expand(A.det())
coeffs = [sp.nsimplify(sp.expand(N).coeff(h, k)) for k in range(4)]
# truncation validity: contributions to h^k for k<=3 only involve
# phi_j with j<=3 — exact.
dens = [sp.fraction(sp.Rational(c))[1] for c in coeffs]
support = set()
for d in dens:
    support |= set(sp.factorint(int(d)).keys())
checks["triple_product_coeffs_rational"] = all(
    sp.Rational(c) == c for c in coeffs
)
checks["triple_product_5_integral_to_h3"] = 5 not in support
# expected support: {2,3} from the 4_1-style statement PLUS 23-powers
# from the per-order delta^{3k} normalization (integrality away from
# Delta, Delta containing disc = -23). Observed: exactly {2, 23} — the
# 3s cancel entirely (stronger than the 4_1 Z[1/3] statement).
checks["triple_product_denominator_support_in_2_3_23"] = support <= {2, 3, 23}
# pin the observed exact support so a silent reappearance of 3 fails
checks["triple_product_support_exactly_2_23"] = support == {2, 23}

print(json.dumps(checks, indent=1))
print("N(h) coefficients:", [str(c) for c in coeffs])
print("denominator support:", sorted(support))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_52_galois_norm_probe",
    "engine": "python3-sympy-exact",
    "scriptFile": "gswz_52_galois_norm_probe.py",
    "commitSha": _sha,
    "beans": ["qou-xx9f", "qou-9p9y"],
    "source": (
        "GZ SIGMA 20 (2024) 055 §9 end (library/arxiv-2111.06645v3/2111.06645v3.pdf); "
        "GSWZ (282) (library/arxiv-2412.04241v2/2412.04241v2.pdf)"
    ),
    "checks": checks,
    "norm_series_coeffs": [str(c) for c in coeffs],
    "denominator_support": sorted(int(x) for x in support),
    "e_factor_shape_identification": {
        "statement": (
            "the (287) quotient mismatch has the GZ E-factor signature: "
            "h^1 present, h^2 absent (B_3 = 0; matches x^2 passing with "
            "the h^1 solve alone), h^3 residual (B_4 term)"
        ),
        "implied_relations": "C_1 = -12*lambda_1; C_3 = 720*mu_3 (up to sign conventions)",
        "status": "shape-identified; values OPEN (GZ print C_r for 4_1 only, their §8.1)",
    },
    "scope": (
        "scope-(a): Galois triple-product integrality of the printed 5_2 "
        "series verified exactly to h^3; E-factor shape identification "
        "recorded for xx9f; C_r value extraction open"
    ),
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_52_galois_norm.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
