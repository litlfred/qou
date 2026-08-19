"""GSWZ 5_2 symmetrization + Habiro gluing digit — printed (282)/(283)/(286) verified exactly.

Bean qou-9p9y (Habiro attack plan, capstone approach work). Scope-(a);
no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 8/9).

CONTEXT. GSWZ §4.6 (arXiv:2412.04241v2) gives the 5_2 knot's
perturbative series Phi_1(h) = (1/sqrt(delta)) (1 + phi_1 h + phi_2 h^2
+ phi_3 h^3 + ...) with delta = 3*alpha - 2, alpha^3 - alpha^2 + 1 = 0
(eqn (282), exact algebraic coefficients printed to h^3), and the
symmetrized series

    delta * f_1(x) * f_1(-x/(1+x))     (eqn (283), printed to x^4)

where f_1(x) = Phi_1(h)|_{h = log(1+x)}. Since the second argument
x' = -x/(1+x) has 1 + x' = 1/(1+x), i.e. h' = -h, the symmetrization
is delta * (1/delta) * Phi~(h) Phi~(-h) with Phi~ = 1 + phi_1 h + ...
— the same bar-even Phi(h)Phi(-h) structure verified for 4_1 in
gswz_symmetrization_integrality_probe.py, now on the 5_2 with its
cubic trace field.

WHAT THIS CHECKS (exact arithmetic in Q[alpha]/(alpha^3 - alpha^2 + 1)):

(Note: the h-odd cancellation in Phi~(h)Phi~(-h) is an identity for
ANY coefficient values — G(-h) = G(h) by construction — so it is NOT
posed as a check; a vacuous always-true check would violate the
constructed-to-fail discipline. The falsifiable content is the printed
coefficient data below.)

1. Printed (283) x^2 coefficient: expanding G(h(x)) with
   h = log(1+x) gives x^2 coefficient g_2 = 2*phi_2 - phi_1^2;
   the printed value reads (465*alpha^2 - 465*alpha + 54)/23^3
   (pdf "1/233" = 1/23^3 = 1/12167, adjudicated by exact numerator
   match: N(delta) = N(3*alpha-2) = 23 is the 5_2 field's discriminant
   prime, so denominators are 23-powers — GSWZ integrality away from
   Delta, with Delta containing disc = -23).
2. Printed (283) x^3 coefficient: the transcribed value equals
   -(x^2 coefficient), and the math forces exactly that (only the h^2
   term contributes below x^4, and log(1+x)^2 = x^2 - x^3 +
   (11/12)x^4 - ...) — falsifiable against either transcription.
3. Integrality away from 23: the exact g_2 denominator is a power
   of 23 (= |disc| of the trace field) — in particular 5-integral,
   the GSWZ integrality-away-from-Delta statement in miniature.
4. Habiro gluing digit (286): (alpha^2 + 4*alpha)^5 = alpha^2 +
   3*alpha + 2 (mod 5) in F_5[alpha]/(alpha^3 - alpha^2 + 1) —
   the p-power gluing between the zeta_5 fibre (284) and the m=5
   constant term (285), checked in the exact ring.
5. Observation (recorded, not a claim): the printed x^4 coefficient
   determines the h^4 coefficient g_4 = printed_x4 - (11/12)*g_2,
   hence the unprinted phi_4 via g_4 = 2*phi_4 - 2*phi_1*phi_3 +
   phi_2^2 — derived and stored in the witness for downstream use
   ((287) needs the x-expansion machinery).

HONESTY: the (287) Psi-section division test (the module-membership
capstone consuming the full-precision Li_2 layer) and the eps_m units
at m > 1 (no printed GSWZ targets; needs the CGZ [10] data) remain
queued on qou-9p9y.
"""

import json
import pathlib
import sys

import sympy as sp

a = sp.symbols("alpha")
MINPOLY = a**3 - a**2 + 1
h, x = sp.symbols("h x")


def red(e):
    """Reduce a Q[alpha] expression mod the minimal polynomial."""
    return sp.rem(sp.expand(e), MINPOLY, a)


delta = 3 * a - 2

# GSWZ (282): Phi_1(h) = delta^{-1/2} (1 + phi1 h + phi2 h^2 + phi3 h^3 + ...)
phi1 = (765 * a**2 - 1086 * a + 1043) / (24 * delta**3)
phi2 = (1757583 * a**2 - 2956029 * a + 2241964) / (1152 * delta**6)
phi3 = (21285784611 * a**2 - 37166037066 * a + 27969826252) / (414720 * delta**9)

# delta is a unit in Q(alpha): exact inverse in the quotient ring
dinv = sp.Poly(sp.invert(sp.Poly(delta, a), sp.Poly(MINPOLY, a)), a).as_expr()
assert sp.simplify(red(delta * dinv)) == 1


def canon(e):
    """Canonical form in Q(alpha): replace 1/delta by dinv, reduce."""
    e = sp.together(sp.expand(e))
    num, den = sp.fraction(e)
    denp = sp.Poly(den, a)
    if denp.degree() == 0:
        return sp.expand(red(num) / den)
    # den is a power of delta times a rational
    q, r = sp.div(sp.Poly(den, a), sp.Poly(delta, a), a)
    k = 0
    dd = sp.Poly(den, a)
    const = None
    while dd.degree() > 0:
        q, r = sp.div(dd, sp.Poly(delta, a), a)
        assert r.is_zero, "denominator not a delta power"
        dd = q
        k += 1
    const = dd.as_expr()
    return sp.expand(red(num * red(dinv**k)) / const)


P1 = canon(phi1)
P2 = canon(phi2)
P3 = canon(phi3)

checks = {}

# G(h) = Phi~(h) Phi~(-h): even in h identically; data lives in g2 (+ g4)
g2 = canon(2 * P2 - P1 * P1)

# (1) printed x^2 coefficient of (283)
printed_x2 = sp.Rational(1, 23**3) * (465 * a**2 - 465 * a + 54)
checks["printed_283_x2_coefficient"] = bool(sp.simplify(canon(g2 - printed_x2)) == 0)

# (2) printed x^3: transcribed (283) x^3 numerator is the negative of the
# x^2 numerator, and the structure forces x^3 = -x^2 exactly
printed_x3 = sp.Rational(1, 23**3) * (-465 * a**2 + 465 * a - 54)
hs = sp.series(sp.log(1 + x), x, 0, 6).removeO()
x3_of_h2 = sp.expand(hs**2).coeff(x, 3)
checks["printed_283_x3_matches_forced_value"] = bool(
    x3_of_h2 == -1 and sp.simplify(canon(printed_x3 - (-g2))) == 0
)

# (4) integrality away from 23 (denominator a 23-power => 5-integral)
den = sp.fraction(sp.together(g2))[1]
denr = sp.Rational(sp.Poly(den, a).as_expr()) if sp.Poly(den, a).degree() == 0 else None
checks["g2_denominator_23_power"] = bool(
    denr is not None and set(sp.factorint(denr).keys()) == {23}
)

# (5) Habiro gluing digit (286) in F_5[alpha]/(alpha^3 - alpha^2 + 1)
lhs286 = red(sp.expand((a**2 + 4 * a) ** 5))
rhs286 = a**2 + 3 * a + 2
diff = sp.Poly(sp.expand(lhs286 - rhs286), a)
checks["gluing_digit_286_mod5"] = bool(
    all(c % 5 == 0 for c in diff.all_coeffs())
)

# (6) derived g4 / phi4 observation from printed x^4
printed_x4 = sp.Rational(1, 23**6) * (4934541 * a**2 - 4934541 * a + 462834)
x4_of_h2 = sp.expand(hs**2).coeff(x, 4)  # 11/12
g4_derived = canon(printed_x4 - x4_of_h2 * g2)
phi4_derived = canon((g4_derived + 2 * P1 * P3 - P2 * P2) / 2)

print(json.dumps(checks, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")
print("g2 =", sp.sstr(sp.simplify(g2)))
print("g4_derived =", sp.sstr(sp.simplify(g4_derived)))

witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_52_symmetrization_probe",
    "beans": ["qou-9p9y"],
    "source": "GSWZ arXiv:2412.04241v2 §4.6 eqns (282)/(283)/(286); uploads/2412.04241v2.pdf",
    "field": "Q(alpha)/(alpha^3 - alpha^2 + 1) (5_2 trace field)",
    "checks": checks,
    "g2_exact": sp.sstr(sp.simplify(g2)),
    "derived_observations": {
        "g4_from_printed_x4": sp.sstr(sp.simplify(g4_derived)),
        "phi4_from_g4": sp.sstr(sp.simplify(phi4_derived)),
        "note": "derived from printed (283) x^4 digit-group; not independently verified (phi4 unprinted in (282))",
    },
    "scope": "scope-(a): 5_2 symmetrization + gluing digit vs printed data; (287) Psi-division capstone and eps_m (m>1) queued",
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_52_symmetrization.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
