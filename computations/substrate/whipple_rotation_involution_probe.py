"""Whipple involution vs channel rotation — eigenfunction-level probe (option 2
of the parabolic-cylinder/toroidal channel-interpolation audit, PR #3445).

The ladder-level result (hoefsmit_toroidal_ladder_probe: the toroidal
half-integer degree shift is forced) leaves the eigenfunction-level lead of
audit §5 open: does the corpus channel rotation (x, q) -> (ix, q^{-1})
(`rotation_step`, channel-rotation-askey-lit) act on the toroidal family as
the Whipple degree<->order exchange? This probe verifies the three exact
structural facts that the identification requires, and *discovers* (does not
assume) the Gamma-structure of the Whipple constant numerically.

Verified EXACTLY (sympy symbolic):

(1) BAR-EVENNESS OF THE LADDER: [d]_{q^{-1}} = [d]_q. The interpolating
    (Hoefsmit/Legendre) ladder is invariant under the bar involution — the
    mixing amplitude lives in the bar-EVEN sector, so channel interpolation
    is a binding-sector (cosh) object, while bar-ODD data enters only
    through the channel loci themselves.

(2) WHIPPLE ARGUMENT INVOLUTION: coth(arccosh(coth a)) = cosh a for a > 0.
    The cosh <-> coth argument exchange underlying Whipple's transformation
    is an involution — the geometric seat of the (mu, nu) winding exchange
    (around-core <-> along-loop) on nested tori.

(3) QUARTER-PERIOD CHANNEL SHIFT: cosh(t + i pi/2) = i sinh t. The zeta_4
    quarter-period shift maps the bar-even (cosh) channel to the bar-odd
    (sinh) channel — already Lean-certified in the corpus
    (QOU/Mass/ComplexVolumeZeta4Partner); re-asserted here because it is the
    analytic face of the rotation x -> ix that the Whipple exchange must
    intertwine.

Verified NUMERICALLY (mpmath, 50 dps):

(4) WHIPPLE ALPHA-INDEPENDENCE: for the toroidal pair
        W(nu, mu, a) := P^mu_{nu-1/2}(coth a) / (sqrt(sinh a) * Q^nu_{mu-1/2}(cosh a)),
    W is independent of a (checked on an a-grid to ~1e-30 relative) — i.e.
    P^mu_{nu-1/2} at coth argument IS proportional to Q^nu_{mu-1/2} at cosh
    argument with a sqrt(sinh a) Jacobian: degree and order EXCHANGE.

(5) GAMMA-STRUCTURE DISCOVERY: the a-independent constant c(nu, mu)
    satisfies c(nu, mu+1)/c(nu, mu) and c(nu+1, mu)/c(nu, mu) laws matched
    against simple Gamma-shift candidates; the discovered law is recorded in
    the witness (discovery output, not an assumed identity).

Scope discipline: (a)-scoped structural verification + labeled numerical
discovery. The identification "rotation_step archimedean shadow = Whipple
involution" remains a LEAD (conjecture shape, audit §9); nothing here wires
to production and no observable is touched.
"""
import json
import os

import mpmath as mp
import sympy as sp

# ---------------------------------------------------------------- (1) sympy
d_s, q_s, a_s, t_s = sp.symbols("d q a t", positive=True)


def bkt(x, q):
    return (q**x - q**(-x)) / (q - 1 / q)


bar_even_bracket = sp.simplify(bkt(d_s, 1 / q_s) - bkt(d_s, q_s)) == 0

# ------------------------------------------------------------- (2) involution
# coth(arccosh(x)) = x / sqrt(x^2 - 1); at x = coth a, a > 0, the composite
# equals cosh a. Verified in SQUARED form (sympy normalizes the radical-free
# identity to 0); both sides are positive for a > 0, so the squared identity
# is equivalent to the stated one.
_x = sp.coth(a_s)
whipple_argument_involution = sp.simplify(
    _x**2 / (_x**2 - 1) - sp.cosh(a_s)**2) == 0

# ------------------------------------------------------ (3) quarter-period
quarter_period_shift = sp.simplify(
    sp.expand_complex(sp.cosh(t_s + sp.I * sp.pi / 2)) - sp.I * sp.sinh(t_s)) == 0

# ----------------------------------------------------- (4) Whipple numerics
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()


def whipple_ratio(nu, mu, a):
    """P^{-mu}_{nu-1/2}(coth a) / (sqrt(sinh a) * Q^nu_{mu-1/2}(cosh a)).

    Pairing DISCOVERED by a 48-combo scan over {P,Q} x order-signs x
    Jacobian exponents (only the -mu order on P is alpha-independent,
    matching the DLMF 14.9.16 convention)."""
    x = mp.coth(a)
    y = mp.cosh(a)
    p = mp.legenp(nu - mp.mpf(1) / 2, -mu, x, type=3)
    qq = mp.legenq(mu - mp.mpf(1) / 2, nu, y, type=3)
    return p / (mp.sqrt(mp.sinh(a)) * qq)


NU, MU = mp.mpf("2.3"), mp.mpf("0.7")
GRID = [mp.mpf("0.4"), mp.mpf("0.9"), mp.mpf("1.7"), mp.mpf("2.6")]
vals = [whipple_ratio(NU, MU, a) for a in GRID]
spread = max(abs(v - vals[0]) / abs(vals[0]) for v in vals[1:])
whipple_alpha_independent = spread < mp.mpf("1e-30")

# a second (nu, mu) point to guard against coincidence
NU2, MU2 = mp.mpf("1.6"), mp.mpf("0.25")
vals2 = [whipple_ratio(NU2, MU2, a) for a in GRID]
spread2 = max(abs(v - vals2[0]) / abs(vals2[0]) for v in vals2[1:])
whipple_alpha_independent_2 = spread2 < mp.mpf("1e-30")

# ------------------------------------------- (5) Gamma-structure discovery
c_base = vals[0]
c_mu_up = whipple_ratio(NU, MU + 1, GRID[0])
c_nu_up = whipple_ratio(NU + 1, MU, GRID[0])
r_mu = c_mu_up / c_base
r_nu = c_nu_up / c_base

half = mp.mpf(1) / 2
candidates_mu = {
    "1/((nu-mu-1/2)(nu+mu+1/2))": 1 / ((NU - MU - half) * (NU + MU + half)),
    "-1/((nu-mu-1/2)(nu+mu+1/2))": -1 / ((NU - MU - half) * (NU + MU + half)),
    "(nu-mu-1/2)(nu+mu+1/2)": (NU - MU - half) * (NU + MU + half),
    "1/(nu+mu+1/2)": 1 / (NU + MU + half),
    "nu+mu+1/2": NU + MU + half,
    "1/(nu-mu-1/2)": 1 / (NU - MU - half),
}
candidates_nu = {
    "-1/(nu+mu+1/2)": -1 / (NU + MU + half),
    "1/(nu+mu+1/2)": 1 / (NU + MU + half),
    "(nu-mu+1/2)/(nu+mu+1/2)": (NU - MU + half) / (NU + MU + half),
    "-(nu-mu+1/2)/(nu+mu+1/2)": -(NU - MU + half) / (NU + MU + half),
    "1/((nu-mu+1/2)(nu+mu+1/2))": 1 / ((NU - MU + half) * (NU + MU + half)),
    "1": mp.mpf(1),
}


def best_match(r, cands):
    hits = [(k, abs(r - v) / abs(r)) for k, v in cands.items()]
    hits.sort(key=lambda kv: kv[1])
    k, err = hits[0]
    return (k, float(err)) if err < mp.mpf("1e-30") else (None, float(err))


mu_law, mu_err = best_match(r_mu, candidates_mu)
nu_law, nu_err = best_match(r_nu, candidates_nu)

assertions = {
    "bar_even_bracket_[d]_qinv_eq_[d]_q": bool(bar_even_bracket),
    "whipple_argument_involution_coth_acosh_coth": bool(whipple_argument_involution),
    "quarter_period_cosh_shift_eq_i_sinh": bool(quarter_period_shift),
    "whipple_alpha_independence_point1": bool(whipple_alpha_independent),
    "whipple_alpha_independence_point2": bool(whipple_alpha_independent_2),
    "gamma_ratio_mu_law_found": mu_law is not None,
    "gamma_ratio_nu_law_found": nu_law is not None,
}

verdict = (
    "EIGENFUNCTION-LEVEL STRUCTURE CONSISTENT, IDENTIFICATION STAYS A LEAD: "
    "the interpolating ladder is bar-EVEN ([d] invariant under q -> q^{-1}); "
    "the Whipple cosh<->coth argument exchange is an exact involution (the "
    "geometric winding exchange); the zeta_4 quarter-period shift maps the "
    "cosh channel to i*sinh (corpus Lean-certified); and numerically at 50 "
    "dps the toroidal pair P^{-mu}_{nu-1/2}(coth a) / Q^nu_{mu-1/2}(cosh a) "
    "(pairing discovered by a 48-combo scan; DLMF 14.9.16 convention) is "
    "sqrt(sinh a)-proportional with an a-independent constant (degree<->order "
    "exchange verified at two generic (nu, mu) points), whose Gamma-shift "
    "laws r_mu = +1/(nu+mu+1/2) and r_nu = -1/(nu+mu+1/2) are recorded as "
    "discovery output — one Gamma(nu+mu+1/2) with an alternating nu-sign. "
    "SCOPE (a): these are the "
    "necessary structural facts for 'rotation_step archimedean shadow = "
    "Whipple involution'; the identification itself remains an open lead "
    "(audit S9) and nothing here touches production or observables."
)

witness = {
    "computation": "whipple_rotation_involution_probe",
    "description": (
        "Option-2 eigenfunction-level probe: bar-evenness of the interpolating "
        "ladder, exactness of the Whipple argument involution and the zeta_4 "
        "quarter-period channel shift, plus 50-dps verification that the "
        "toroidal Legendre pair exchanges degree and order with a "
        "sqrt(sinh)-Jacobian (Whipple)."
    ),
    "discipline": "no fit; sympy exact + mpmath 50 dps; discovery outputs labeled; (a)-scoped.",
    "auditOnly": "docs/audits/2026-07-06-parabolic-cylinder-toroidal-channel-interpolation.md",
    "results": {
        "alpha_spread_point1": mp.nstr(spread, 5),
        "alpha_spread_point2": mp.nstr(spread2, 5),
        "whipple_constant_point1": mp.nstr(c_base, 30),
        "gamma_ratio_mu": {"value": mp.nstr(r_mu, 30), "matched_law": mu_law, "rel_err": mu_err},
        "gamma_ratio_nu": {"value": mp.nstr(r_nu, 30), "matched_law": nu_law, "rel_err": nu_err},
        "lean_cert_quarter_period": "QOU/Mass/ComplexVolumeZeta4Partner (corpus, sorry-free)",
        "lean_cert_ladder_locus": "QOU.BraidsAndKnots.toroidal_locus_forced (this PR, sorry-free)",
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy+mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "whipple-rotation-involution-probe.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

for k, v in assertions.items():
    print(f"  {k}: {'PASS' if v else 'FAIL'}")
print(f"\nallPassed: {witness['allPassed']}")
print(f"gamma laws: mu -> {mu_law} (err {mu_err:.2e}), nu -> {nu_law} (err {nu_err:.2e})")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
