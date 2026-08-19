"""GSWZ membership harness v1 — layers assembled + the Bloch-group decomposition verified mod 5^3.

Bean qou-9p9y (T3 of the Habiro attack plan). Scope-(a); no fit;
nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 7).

WHAT THIS IS. The first end-to-end assembly of the GSWZ
module-membership layers built across this program (symmetrization
integrality, Hensel Frobenius, Teichmuller, mod-p finite-polylog dilog)
into one harness, PLUS one genuinely new module-side verification:

**THE BLOCH-GROUP DECOMPOSITION CHECK (GSWZ eqns (271)/(273)/(274),
Theorem 9 in action).** Example 4.3 decomposes the 5_2 knot's Bloch
element xi = [z1]+[z2]+[z3] in K3 of the 5-adic field over
root-of-unity symbols:

    D5(xi) = c1*D5(zeta24) + c2*D5(zeta24^2) + c3*D5(zeta24^6)

with printed 5-adic coefficients c1 = 1+4*5+..., c2 = 3+5+...,
c3 = 1+5+... and printed D5(xi) = (3*5^2+...)a^2 + (5^2+...)a +
(2*5^2+...). Every ingredient on the right is computable mod 5^3 from
OUR layers alone (Prop 3.2 finite-polylog values give each D5(zeta)
mod 5^3; the c_i enter mod 5 since D5(zeta) = 0 mod 25), so the
decomposition is verifiable mod 5^3 with no Coleman integration:

    sum_i (c_i mod 5) * (D5(zeta_i)/25 mod 5)  =?=  D5(xi)/25 mod 5.

This is the module-side (epsilon_m-class) layer of the membership test
exercised on printed data — the knot's K3 class expressed in the
root-of-unity basis that the Habiro-module leading terms live in.

WHAT THIS CHECKS:

1. Layer self-tests (rerun of the merged layers' key invariants):
   Frobenius lift root property; Teichmuller exact order 24;
   li_{2,5}(1) = 0 mod 5.
2. THE DECOMPOSITION: c1*D5(zeta24) + c2*D5(zeta24^2) + c3*D5(zeta24^6)
   = D5(xi) mod 5^3, all sides from printed data + Prop 3.2 values.
3. Harness pass/fail demo on the candidate interface: a Z[q,1/q]
   candidate (the n=4 binding tail) PASSES integrality + bar checks; a
   rationally perturbed clone FAILS — the gate discriminates without
   anchor comparison.

MISSING INGREDIENT (named, single): full-precision Coleman Li2 requires
the Besser-de Jeu overconvergent expansion (their reference [8]) which
is NOT among the uploaded sources; until it lands, the dilog layer is
mod-5^3-exact only. epsilon_m units at full precision are queued with
it. Bean qou-9p9y stays in-progress for that layer.
"""

import json
import pathlib
import sys

D = 6
MOD = 5**D


def mul(a, b):
    prod = [0] * 5
    for i in range(3):
        for j in range(3):
            prod[i + j] = (prod[i + j] + a[i] * b[j]) % MOD
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
    r = [coeffs_desc[0] % MOD, 0, 0]
    for c in coeffs_desc[1:]:
        r = mul(r, a)
        r = [(r[0] + c) % MOD, r[1], r[2]]
    return r


def inv_unit(u):
    seed = None
    for c0 in range(5):
        for c1 in range(5):
            for c2 in range(5):
                t = mul(u, [c0, c1, c2])
                if t[0] % 5 == 1 and t[1] % 5 == 0 and t[2] % 5 == 0:
                    seed = [c0, c1, c2]
                    break
            if seed:
                break
        if seed:
            break
    assert seed is not None, "not a unit"
    inv = seed
    for _ in range(4):
        t = mul(u, inv)
        inv = mul(inv, [(-t[0] + 2) % MOD, (-t[1]) % MOD, (-t[2]) % MOD])
    return inv


def li25(z):
    total = [0, 0, 0]
    for k in range(1, 5):
        zk = pw(z, k)
        ki = pow(k * k, -1, MOD)
        total = [(total[m] + zk[m] * ki) % MOD for m in range(3)]
    return total


def d5_over_25_mod5(zeta_input):
    """Prop 3.2: D5(zeta_input^5)/25 mod 5 = li_{2,5}(zeta_input)/(zeta_input-1)^5."""
    num = li25(zeta_input)
    den = pw([(zeta_input[0] - 1) % MOD, zeta_input[1], zeta_input[2]], 5)
    return [c % 5 for c in mul(num, inv_unit(den))]


checks = {}

# --- (1) layer self-tests
alpha = [0, 1, 0]
P = [1, -1, 0, 1]
phi = pw(alpha, 5)
for d in range(1, D):
    val = poly_eval(P, phi)
    Pp = poly_eval([3, -2, 0], phi)
    corr = mul(val, inv_unit(Pp))
    phi = [(phi[k] - corr[k]) % MOD for k in range(3)]
checks["layer_frobenius_root"] = all(
    v % MOD == 0 for v in poly_eval(P, phi)
)
z = alpha[:]
prev = None
stabilized = False
for s in range(1, 12):
    z = pw(z, 25)
    if z == prev:
        stabilized = True
        break
    prev = z[:]
assert stabilized
zeta24 = z
checks["layer_teichmuller_order24"] = pw(zeta24, 24) == [1, 0, 0] and all(
    pw(zeta24, 24 // f) != [1, 0, 0] for f in (2, 3)
)
checks["layer_li25_at_1"] = all(c % 5 == 0 for c in li25([1, 0, 0]))

# --- (2) THE BLOCH-GROUP DECOMPOSITION mod 5^3 (GSWZ (271)/(273)/(274))
# D5(zeta)/25 mod 5 via Prop 3.2 (targets reached by 5th-power inputs)
D_z1 = d5_over_25_mod5(pw(zeta24, 5))  # target zeta24
D_z2 = d5_over_25_mod5(pw(zeta24, 10))  # target zeta24^2
D_z6 = d5_over_25_mod5(pw(zeta24, 6))  # target zeta24^6
# printed coefficients of (274) mod 5
c1, c2, c3 = 1, 3, 1
# printed D5(xi) of (271), /25 mod 5, coords (const, alpha, alpha^2):
# (2*5^2+...) const, (5^2+...) alpha, (3*5^2+...) alpha^2
printed_xi = [2, 1, 3]
lhs = [
    (c1 * D_z1[m] + c2 * D_z2[m] + c3 * D_z6[m]) % 5 for m in range(3)
]
checks["bloch_decomposition_274_mod_125"] = lhs == printed_xi

# --- (3) harness candidate interface demo (archimedean gate, sympy)
import sympy as sp

q = sp.symbols("q")
# the n=4 binding tail (corpus, balanced convention): D(4) = (q-1)^2*Phi3/q^2
cand_pass = (q - 1) ** 2 * (q**2 + q + 1) / q**2
cand_fail = cand_pass + sp.Rational(1, 7) * (q - 1) ** 2


def gate(candidate):
    e = sp.cancel(candidate)
    num, den = sp.fraction(sp.together(e))
    pnum = sp.Poly(sp.expand(num), q)
    pden = sp.Poly(sp.expand(den), q)
    if len(pden.terms()) != 1:
        return {"integer_laurent": False, "bar_even": False}
    (dmono, dcoef), = pden.terms()
    ints = all(
        sp.Rational(c, dcoef).q == 1 for (_,), c in pnum.terms()
    )
    bar = sp.simplify(e.subs(q, 1 / q) - e) == 0
    return {"integer_laurent": bool(ints), "bar_even": bool(bar)}


gp = gate(cand_pass)
gf = gate(cand_fail)
checks["harness_pass_case"] = gp["integer_laurent"] and gp["bar_even"]
checks["harness_fail_case_rejected"] = not gf["integer_laurent"]

print(json.dumps(checks, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_membership_harness_v1_probe",
    "beans": ["qou-9p9y"],
    "source": "GSWZ arXiv:2412.04241v2 Example 4.3 eqns (271)/(273)/(274); library/arxiv-2412.04241v2/2412.04241v2.pdf; merged layer probes",
    "checks": checks,
    "bloch_decomposition": {
        "computed_lhs_mod5": lhs,
        "printed_D5_xi_over25_mod5": printed_xi,
        "coefficients_mod5": [c1, c2, c3],
    },
    "missing_ingredient": "Besser-de Jeu overconvergent Li2 expansion (GSWZ ref [8]) — not in library/; dilog layer is mod-5^3-exact until it lands",
    "scope": "scope-(a): harness v1 assembled; Bloch decomposition (Theorem 9 instance) verified mod 5^3 from printed data; full-precision Coleman + eps_m queued",
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_membership_harness_v1.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
