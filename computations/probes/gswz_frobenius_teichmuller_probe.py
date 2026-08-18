"""GSWZ Frobenius-lift + Teichmuller probe — Example 4.3 verified in exact arithmetic.

Bean qou-1hlh (membership-gate v2: the Frobenius layer). Scope-(a); no
fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 4).

CONTEXT. The GSWZ gluing (arXiv:2412.04241v2 Def 1.1, uploaded at
uploads/2412.04241v2.pdf) is Frobenius-twisted: f_m(x + zeta_pm -
zeta_m) = (phi_p f_pm)(x). Testing membership of a candidate
Habiro-module element over a number field therefore REQUIRES the
Frobenius endomorphism phi_p of R_p^wedge in executable form. GSWZ
§4.4 gives the constructive Hensel algorithm (their eqns (263)-(267))
and prints concrete 5-adic data for the 5_2 trace field
K = Q(alpha)/(alpha^3 - alpha^2 + 1) in Example 4.3 — including the
Teichmuller root of unity zeta_24 = lim alpha^{5^{2s}} with printed
digits (their eqn (272)):

    zeta_24 = (4*5^2 + ...)alpha^2 + (1 + ...)alpha + (3*5 + ...).

WHAT THIS CHECKS (exact Z/5^d arithmetic in (Z/5^d)[x]/(P), d = 6):

1. The Hensel lift phi_5(alpha): P(phi_5(alpha)) = 0 mod 5^6 and
   phi_5(alpha) = alpha^5 mod 5 — the defining Frobenius properties,
   computed by the GSWZ induction (263)-(267).
2. Teichmuller stabilization: alpha^{5^{2s}} stabilizes mod 5^6 and the
   limit zeta has EXACT multiplicative order 24.
3. Printed-digit match (272): the alpha^2-coordinate is 4*5^2 mod 5^3,
   the alpha-coordinate is 1 mod 5, the constant coordinate is 3*5
   mod 5^2.
4. Frobenius-Teichmuller equivariance: phi_5(zeta_24) = zeta_24^5
   mod 5^6 — the ring-hom extension of the lift acts on the Teichmuller
   subgroup exactly as q -> q^p, i.e. the vertical-edge action the
   gluing applies.

HONESTY: this implements and verifies the FROBENIUS layer of the GSWZ
toolkit against their printed data. The p-adic dilogarithm layer
(Besser-de Jeu, their eqn (268), needed for the module-side epsilon_m
corrections) is NOT implemented here and stays queued on bean qou-1hlh.
"""

import json
import pathlib
import sys

D = 6
MOD = 5**D
# P(x) = x^3 - x^2 + 1; reduction: x^3 = x^2 - 1
P = [1, -1, 0, 1]  # coefficients of x^3 - x^2 + 1, degree-descending


def mul(a, b):
    """Multiply two elements of (Z/5^D)[x]/(x^3 - x^2 + 1); coords
    ascending [c0, c1, c2]."""
    prod = [0] * 5
    for i in range(3):
        for j in range(3):
            prod[i + j] = (prod[i + j] + a[i] * b[j]) % MOD
    # reduce x^4 = x^3 - x = (x^2 - 1) - x + ... : do x^4 first then x^3
    # x^3 = x^2 - 1 ; x^4 = x*x^3 = x^3 - x = x^2 - 1 - x
    c4, c3 = prod[4], prod[3]
    prod[2] = (prod[2] + c4 + c3) % MOD
    prod[1] = (prod[1] - c4) % MOD
    prod[0] = (prod[0] - c4 - c3) % MOD
    return prod[:3]


def pw(a, n):
    r = [1, 0, 0]
    b = a[:]
    while n:
        if n & 1:
            r = mul(r, b)
        b = mul(b, b)
        n >>= 1
    return r


def poly_eval(coeffs_desc, a):
    """Evaluate an integer polynomial at ring element a."""
    r = [coeffs_desc[0] % MOD, 0, 0]
    for c in coeffs_desc[1:]:
        r = mul(r, a)
        r = [(r[0] + c) % MOD, r[1], r[2]]
    return r


alpha = [0, 1, 0]

checks = {}

# --- (1) Hensel lift of Frobenius: phi_5(alpha) with P(phi) = 0,
# phi = alpha^5 mod 5, by the GSWZ induction (263)-(267).
phi = pw(alpha, 5)  # alpha^5, the seed: P(alpha^5) = 0 mod 5
for d in range(1, D):
    pd = 5**d
    val = poly_eval(P, phi)
    assert all(v % pd == 0 for v in val), "induction invariant broken"
    # beta = -P(phi)/(p^d P'(phi)) mod 5 ; P'(x) = 3x^2 - 2x
    Pp = poly_eval([3, -2, 0], phi)
    # invert P'(phi) mod 5^D via unit power (order of unit group divides
    # 5^(D-1)*(5^3-1)... use generic: u^-1 = u^(lambda-1) with
    # lambda = |(R/5^D R)^x| divisor; simpler: Hensel-invert via pow of
    # the ring: brute force with extended trick — use pow to
    # 5^(D-1)*(5**3 - 1)*(5-1)... safest: Newton inversion.
    inv = [1, 0, 0]
    # Newton: x_{k+1} = x_k (2 - u x_k); seed = inverse mod 5 by search
    seed = None
    for c0 in range(5):
        for c1 in range(5):
            for c2 in range(5):
                t = mul(Pp, [c0, c1, c2])
                if t[0] % 5 == 1 and t[1] % 5 == 0 and t[2] % 5 == 0:
                    seed = [c0, c1, c2]
                    break
            if seed:
                break
        if seed:
            break
    assert seed is not None, "P'(phi) not a unit — ramified?"
    inv = seed
    for _ in range(4):
        t = mul(Pp, inv)
        two_minus = [(-t[0] + 2) % MOD, (-t[1]) % MOD, (-t[2]) % MOD]
        inv = mul(inv, two_minus)
    corr = mul(val, inv)
    phi = [(phi[k] - corr[k]) % MOD for k in range(3)]

val = poly_eval(P, phi)
checks["hensel_lift_root_of_P_mod_5^6"] = all(v % MOD == 0 for v in val)
a5 = pw(alpha, 5)
checks["hensel_lift_is_alpha^5_mod_5"] = all((phi[k] - a5[k]) % 5 == 0 for k in range(3))

# --- (2) Teichmuller zeta_24 = lim alpha^{5^{2s}}
z = alpha[:]
prev = None
stabilized = False
for s in range(1, 12):
    z = pw(z, 25)
    if z == prev:
        stabilized = True
        break
    prev = z[:]
zeta24 = z
checks["teichmuller_stabilizes"] = stabilized
ord24 = pw(zeta24, 24)
checks["zeta24_pow_24_eq_one"] = bool(ord24 == [1, 0, 0])
proper = all(pw(zeta24, 24 // q) != [1, 0, 0] for q in (2, 3))
checks["zeta24_exact_order_24"] = proper

# --- (3) printed digits of eqn (272)
c0, c1, c2 = zeta24
checks["digit_alpha2_is_4x25_mod_125"] = c2 % 125 == 100
checks["digit_alpha_is_1_mod_5"] = c1 % 5 == 1
checks["digit_const_is_15_mod_25"] = c0 % 25 == 15

# --- (4) Frobenius acts on Teichmuller as q -> q^5:
# phi_5 extends to the ring hom alpha -> phi; apply to zeta24's
# polynomial expression: phi_5(zeta24) = sum c_k phi^k
phz = [zeta24[0] % MOD, 0, 0]
t1 = mul([zeta24[1] % MOD, 0, 0], phi)
t2 = mul([zeta24[2] % MOD, 0, 0], mul(phi, phi))
phz = [(phz[k] + t1[k] + t2[k]) % MOD for k in range(3)]
z5 = pw(zeta24, 5)
checks["frobenius_teichmuller_equivariance"] = bool(phz == z5)

print(json.dumps(checks, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_frobenius_teichmuller_probe",
    "beans": ["qou-1hlh"],
    "source": "GSWZ arXiv:2412.04241v2 §4.4 eqns (263)-(267), (272); uploads/2412.04241v2.pdf",
    "field": "Q(alpha)/(alpha^3 - alpha^2 + 1) (5_2 trace field), p = 5, precision 5^6",
    "checks": checks,
    "zeta24_coords_const_alpha_alpha2": [c0, c1, c2],
    "scope": "scope-(a): Frobenius/Teichmuller layer verified vs printed Example 4.3; p-adic dilog layer queued on qou-1hlh",
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_frobenius_teichmuller.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
