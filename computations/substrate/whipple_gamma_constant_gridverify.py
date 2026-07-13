"""Whipple toroidal degree<->order constant — grid-verified EXACT Gamma structure.

Promotion of the one-point numerical DISCOVERY in
`whipple_rotation_involution_probe.py` (assertion 5, the two Gamma-shift ratios
matched at a single (nu, mu) point) to a GRID-VERIFIED exact structural identity
for the full a-independent Whipple constant.

Setup (EXACT conventions copied from the probe, DLMF 14.9.16):

    W(nu, mu, a) := P^{-mu}_{nu-1/2}(coth a) / (sqrt(sinh a) * Q^{nu}_{mu-1/2}(cosh a))

    mpmath calls (type=3 associated Legendre, Whipple/toroidal branch):
        p  = legenp(nu - 1/2, -mu, coth a, type=3)
        qq = legenq(mu - 1/2,  nu, cosh a, type=3)
        W  = p / (sqrt(sinh a) * qq)

The probe established (re-verified here at >=2 (nu,mu) x >=3 a):
    (A) W(nu, mu, a) = c(nu, mu) is INDEPENDENT of a  (the degree<->order
        exchange: P at coth-argument is sqrt(sinh a)-proportional to Q at
        cosh-argument), and
    (B) at ONE point the two Gamma-shift ratios matched
        c(nu, mu+1)/c(nu, mu) = +1/(nu+mu+1/2),
        c(nu+1, mu)/c(nu, mu) = -1/(nu+mu+1/2).

This script upgrades (B) from one point to a GRID of >=8 generic (nu, mu)
points (non-integer AND non-half-integer), then DERIVES and TESTS the closed
form the two first-order recurrences force.

Derivation (solve the two recurrences; s := nu + mu + 1/2):

    mu-recurrence  c(nu, mu+1)/c(nu, mu) = 1/(nu+mu+1/2)
                 = Gamma(nu+mu+1/2) / Gamma(nu+mu+3/2)
        => c(nu, mu) = A(nu) / Gamma(nu+mu+1/2).

    nu-recurrence  c(nu+1, mu)/c(nu, mu) = -1/(nu+mu+1/2).  Substituting the
        mu-solution, [A(nu+1)/A(nu)] * 1/(nu+mu+1/2) = -1/(nu+mu+1/2)
        => A(nu+1)/A(nu) = -1  => A(nu) = C * (-1)^nu, and the analytic
        continuation selected numerically is the lower branch e^{-i*pi*nu}.

    => c(nu, mu) = C * e^{-i*pi*nu} / Gamma(nu + mu + 1/2).

The overall (nu,mu)-independent constant is then read off the grid and
identified: C = sqrt(2/pi) (grid-constant, imaginary part numerically zero).

    ==>  c(nu, mu) = sqrt(2/pi) * e^{-i*pi*nu} / Gamma(nu + mu + 1/2).

TIERED VERDICT: this is a symbolic-exact structural identity for the Whipple
constant, grid-verified (not one-point) to ~1e-40 at generic non-special
points. The full rotation_step <-> Whipple IDENTIFICATION (audit S9;
conjecture class WhippleRotationIntertwining) remains an OPEN LEAD: proving the
Gamma-structure of the constant does NOT prove the categorical identification.
Nothing here wires to production or touches an observable.
"""
import json
import os

import mpmath as mp

mp.mp.dps = 60  # compute margin; 40 sig digits serialized
HALF = mp.mpf(1) / 2
TOL = mp.mpf("1e-40")


def whipple_ratio(nu, mu, a):
    """P^{-mu}_{nu-1/2}(coth a) / (sqrt(sinh a) * Q^{nu}_{mu-1/2}(cosh a)).

    EXACT probe convention (DLMF 14.9.16, type=3)."""
    x = mp.coth(a)
    y = mp.cosh(a)
    p = mp.legenp(nu - HALF, -mu, x, type=3)
    qq = mp.legenq(mu - HALF, nu, y, type=3)
    return p / (mp.sqrt(mp.sinh(a)) * qq)


# ---------------------------------------------------------------- (A) a-indep
A_GRID = [mp.mpf("0.4"), mp.mpf("0.9"), mp.mpf("1.3"), mp.mpf("2.0"), mp.mpf("2.6")]
AINDEP_POINTS = [
    (mp.mpf("2.3"), mp.mpf("0.7")),   # probe point 1
    (mp.mpf("1.6"), mp.mpf("0.25")),  # probe point 2
    (mp.mpf("0.3"), mp.mpf("1.2")),   # extra generic point
]
aindep_spreads = []
for nu, mu in AINDEP_POINTS:
    vals = [whipple_ratio(nu, mu, a) for a in A_GRID]
    spread = max(abs(v - vals[0]) / abs(vals[0]) for v in vals[1:])
    aindep_spreads.append(spread)
aindep_max = max(aindep_spreads)
alpha_independent = aindep_max < TOL


def c(nu, mu):
    """a-independent Whipple constant (read at a reference a; a-independence
    already certified in block (A))."""
    return whipple_ratio(nu, mu, mp.mpf("1.3"))


# -------------------------------------------- (B) grid-verify the shift laws
# >=8 generic points: non-integer AND non-half-integer.
GRID = [(mp.mpf(x), mp.mpf(y)) for x, y in [
    ("0.3", "0.7"), ("0.7", "1.2"), ("1.2", "0.9"), ("1.5", "2.2"),
    ("2.2", "0.3"), ("0.9", "1.8"), ("1.8", "2.6"), ("2.6", "1.5"),
]]

mu_dev = mp.mpf(0)
nu_dev = mp.mpf(0)
for nu, mu in GRID:
    r_mu = c(nu, mu + 1) / c(nu, mu)
    law_mu = 1 / (nu + mu + HALF)
    mu_dev = max(mu_dev, abs(r_mu - law_mu) / abs(law_mu))
    r_nu = c(nu + 1, mu) / c(nu, mu)
    law_nu = -1 / (nu + mu + HALF)
    nu_dev = max(nu_dev, abs(r_nu - law_nu) / abs(law_nu))

mu_law_grid = mu_dev < TOL
nu_law_grid = nu_dev < TOL

# -------------------------------------- (C) derived closed form + constant C
# c(nu, mu) = C * e^{-i pi nu} / Gamma(nu + mu + 1/2); read C off the grid.
C_samples = [c(nu, mu) * mp.gamma(nu + mu + HALF) * mp.exp(mp.mpc(0, 1) * mp.pi * nu)
             for nu, mu in GRID]
C0 = C_samples[0]
C_spread = max(abs(Ci - C0) / abs(C0) for Ci in C_samples[1:])
C_constant = C_spread < TOL

with mp.workdps(60):
    C_SQRT_2_PI = +mp.sqrt(2 / mp.pi)
C_imag_max = max(abs(Ci.imag) / abs(Ci) for Ci in C_samples)
C_matches_sqrt2pi = abs(C0.real - C_SQRT_2_PI) / C_SQRT_2_PI < TOL


def closed_form(nu, mu):
    return C_SQRT_2_PI * mp.exp(-mp.mpc(0, 1) * mp.pi * nu) / mp.gamma(nu + mu + HALF)


# -------------------- (D) test derived closed form vs direct compute on grid
# Extended grid: add two extreme points to stress the closed form.
TEST_GRID = GRID + [(mp.mpf("0.05"), mp.mpf("0.05")), (mp.mpf("3.4"), mp.mpf("2.9"))]
closed_dev = max(abs(c(nu, mu) - closed_form(nu, mu)) / abs(c(nu, mu))
                 for nu, mu in TEST_GRID)
closed_form_matches = closed_dev < TOL

assertions = {
    "alpha_independence_grid": bool(alpha_independent),
    "shift_law_mu_grid": bool(mu_law_grid),
    "shift_law_nu_grid": bool(nu_law_grid),
    "constant_C_grid_independent": bool(C_constant),
    "constant_C_equals_sqrt_2_over_pi": bool(C_matches_sqrt2pi),
    "derived_closed_form_matches_grid": bool(closed_form_matches),
}
all_passed = all(assertions.values())

closed_form_str = "c(nu,mu) = sqrt(2/pi) * exp(-i*pi*nu) / Gamma(nu+mu+1/2)"

if all_passed:
    verdict = (
        "SYMBOLIC-EXACT STRUCTURAL IDENTITY (GRID-VERIFIED, NOT ONE-POINT). The "
        "a-independent Whipple toroidal constant c(nu,mu) := "
        "P^{-mu}_{nu-1/2}(coth a) / (sqrt(sinh a) * Q^{nu}_{mu-1/2}(cosh a)) has "
        "closed form " + closed_form_str + ". Both Gamma-shift laws "
        "c(nu,mu+1)/c(nu,mu)=+1/(nu+mu+1/2) and c(nu+1,mu)/c(nu,mu)=-1/(nu+mu+1/2) "
        "hold to ~1e-40 across a grid of 8 generic (nu,mu) points (non-integer AND "
        "non-half-integer); solving the two first-order recurrences forces "
        "c = C*e^{-i*pi*nu}/Gamma(nu+mu+1/2), and the (nu,mu)-independent constant "
        "is grid-identified as C = sqrt(2/pi) (imaginary part numerically zero). "
        "The derived closed form matches the direct 60-dps compute to ~1e-40 on a "
        "10-point extended grid. SCOPE: this promotes assertion (5) of "
        "whipple_rotation_involution_probe from one-point discovery to a "
        "grid-verified exact identity for the CONSTANT; the full rotation_step <-> "
        "Whipple IDENTIFICATION (audit S9, conjecture class "
        "WhippleRotationIntertwining) stays an OPEN LEAD — proving the constant's "
        "Gamma-structure does NOT prove the categorical identification. Nothing "
        "here wires to production or touches an observable."
    )
else:
    verdict = (
        "GRID VERIFICATION FAILED — the one-point discovery did NOT generalize. "
        "Failing assertions: " + ", ".join(k for k, v in assertions.items() if not v)
        + ". Recorded honestly; no block edit made and no identity claimed."
    )

witness = {
    "computation": "whipple_gamma_constant_gridverify",
    "description": (
        "Grid promotion of the Whipple toroidal degree<->order constant from "
        "one-point numerical discovery to a symbolic-exact structural identity: "
        "reproduces a-independence at >=3 (nu,mu) points, grid-verifies BOTH "
        "Gamma-shift laws across 8 generic non-special (nu,mu) points, derives the "
        "closed form c(nu,mu)=sqrt(2/pi)*e^{-i*pi*nu}/Gamma(nu+mu+1/2) implied by "
        "the two recurrences, and tests it against the direct 60-dps compute on a "
        "10-point grid (~1e-40)."
    ),
    "discipline": (
        "no fit; mpmath 60 dps compute, 40 sig digits serialized as strings; "
        "closed form DERIVED from the two shift recurrences then tested (not "
        "fitted); tiered verdict; (a)-scoped; identification stays a lead."
    ),
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "parameters": {
        "a_grid": [mp.nstr(a, 3) for a in A_GRID],
        "alpha_independence_points": [[mp.nstr(nu, 3), mp.nstr(mu, 3)] for nu, mu in AINDEP_POINTS],
        "shift_law_grid": [[mp.nstr(nu, 3), mp.nstr(mu, 3)] for nu, mu in GRID],
        "tolerance": mp.nstr(TOL, 3),
    },
    "results": {
        "alpha_independence_max_spread": mp.nstr(aindep_max, 5),
        "shift_law_mu_max_rel_dev": mp.nstr(mu_dev, 5),
        "shift_law_nu_max_rel_dev": mp.nstr(nu_dev, 5),
        "constant_C_grid_spread": mp.nstr(C_spread, 5),
        "constant_C_value": mp.nstr(C0.real, 40),
        "constant_C_imag_max": mp.nstr(C_imag_max, 5),
        "constant_C_vs_sqrt_2_over_pi_rel": mp.nstr(abs(C0.real - C_SQRT_2_PI) / C_SQRT_2_PI, 5),
        "sqrt_2_over_pi": mp.nstr(C_SQRT_2_PI, 40),
        "derived_closed_form": closed_form_str,
        "closed_form_max_rel_dev_10pt_grid": mp.nstr(closed_dev, 5),
        "shift_law_mu": "c(nu,mu+1)/c(nu,mu) = 1/(nu+mu+1/2)",
        "shift_law_nu": "c(nu+1,mu)/c(nu,mu) = -1/(nu+mu+1/2)",
    },
    "assertions": assertions,
    "allPassed": bool(all_passed),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "whipple-gamma-constant-gridverify.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

for k, v in assertions.items():
    print(f"  {k}: {'PASS' if v else 'FAIL'}")
print(f"\nallPassed: {all_passed}")
print(f"a-independence max spread : {mp.nstr(aindep_max, 5)}")
print(f"shift-law mu max rel dev  : {mp.nstr(mu_dev, 5)}")
print(f"shift-law nu max rel dev  : {mp.nstr(nu_dev, 5)}")
print(f"constant C                : {mp.nstr(C0.real, 30)}  (sqrt(2/pi)={mp.nstr(C_SQRT_2_PI, 30)})")
print(f"derived closed form       : {closed_form_str}")
print(f"closed-form max rel dev   : {mp.nstr(closed_dev, 5)}  (10-pt grid)")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
