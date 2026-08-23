#!/usr/bin/env python3
"""Whipple exchange at the PHYSICAL forced windings (mu = 1/2, nu = d - 1/2).

Evidence for the modeling layer of the Whipple-rotation identification
(content/quantum-observable-universe/mass-endomorphism/whipple-rotation-intertwining.md).

The generic grid-verify
(`whipple-gamma-constant-gridverify.witness.json`) checks the toroidal
degree<->order exchange

    P^{-mu}_{nu-1/2}(coth a) = C(nu, mu) * sqrt(sinh a) * Q^nu_{mu-1/2}(cosh a),
    C(nu, mu) = sqrt(2/pi) * e^{-i pi nu} / Gamma(nu + mu + 1/2),

at GENERIC non-half-integer (nu, mu) points, deliberately dodging the
mu = 1/2 order to avoid Legendre degeneracies. But the PHYSICAL windings
are forced by the Hoefsmit mixing structure to be exactly

    (mu, nu) = (1/2, d - 1/2)          (QOU.BraidsAndKnots.toroidal_locus_forced)

at axial distance d. This probe tests the identification AT those physical
points -- the real test of whether the exchange (hence the even<->odd channel
rotation it shadows) survives at the actual half-integer order. It also
re-verifies, per d, the forcing identity

    (nu - mu)(nu + mu + 1) = d^2 - 1                (order-ladder = mixing numerator).

This is EVIDENCE for a modeling identification (that the bound-vortex windings
are the toroidal-harmonic windings), NOT a proof. auditOnly; nothing wired.

-- Ref: [whipple1917] https://doi.org/10.1112/plms/s2-16.1.301
-- Ref: [lebedev1965] Special Functions and Their Applications (toroidal harmonics)
"""
import json
import os

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

# Exact DLMF 14.9.16 (type=3) conventions, matching
# whipple_rotation_involution_probe.py / whipple_gamma_constant_gridverify.py.
HALF = mp.mpf(1) / 2


def whipple_ratio(nu, mu, a):
    """P^{-mu}_{nu-1/2}(coth a) / (sqrt(sinh a) * Q^{nu}_{mu-1/2}(cosh a))."""
    x = mp.coth(a)
    y = mp.cosh(a)
    p = mp.legenp(nu - HALF, -mu, x, type=3)
    qq = mp.legenq(mu - HALF, nu, y, type=3)
    return p / (mp.sqrt(mp.sinh(a)) * qq)


def gamma_constant(nu, mu):
    """C(nu, mu) = sqrt(2/pi) * e^{-i pi nu} / Gamma(nu + mu + 1/2)."""
    with mp.workdps(60):
        c = +mp.sqrt(2 / mp.pi)
    return c * mp.exp(-mp.mpc(0, 1) * mp.pi * nu) / mp.gamma(nu + mu + HALF)


# Physical axial distances: d = 2 is the meson (b^2 = [3]_q/[2]_q^2), then 3, 4.
# The forced windings are (mu, nu) = (1/2, d - 1/2).
A_GRID = [mp.mpf("0.4"), mp.mpf("0.9"), mp.mpf("1.7"), mp.mpf("2.6")]

per_d = {}
all_exchange_ok = True
all_forcing_ok = True
for d in (2, 3, 4):
    mu = HALF
    nu = mp.mpf(d) - HALF
    # (a) forcing: order-ladder factor == mixing numerator d^2 - 1
    ladder = (nu - mu) * (nu + mu + 1)
    forcing_ok = abs(ladder - (mp.mpf(d) ** 2 - 1)) < mp.mpf("1e-40")
    all_forcing_ok = all_forcing_ok and bool(forcing_ok)
    # (b) exchange: whipple_ratio a-independent AND equal to C(nu, mu)
    Cexpect = gamma_constant(nu, mu)
    ratios = [whipple_ratio(nu, mu, a) for a in A_GRID]
    spread = max(abs(r - ratios[0]) for r in ratios)
    max_dev = max(abs(r - Cexpect) for r in ratios)
    exchange_ok = spread < mp.mpf("1e-30") and max_dev < mp.mpf("1e-30")
    all_exchange_ok = all_exchange_ok and bool(exchange_ok)
    per_d[str(d)] = {
        "windings_mu_nu": [mp.nstr(mu, 5), mp.nstr(nu, 5)],
        "forcing_ladder_value": mp.nstr(ladder, 10),
        "forcing_target_d2_minus_1": d * d - 1,
        "forcing_ok": bool(forcing_ok),
        "a_independence_spread": mp.nstr(spread, 5),
        "max_dev_from_gamma_constant": mp.nstr(max_dev, 5),
        "gamma_constant": mp.nstr(Cexpect, 30),
        "whipple_ratio_point0": mp.nstr(ratios[0], 30),
        "exchange_ok": bool(exchange_ok),
    }

assertions = {
    "physical_forcing_ladder_eq_d2_minus_1_all_d": all_forcing_ok,
    "whipple_exchange_holds_at_physical_half_integer_order_all_d": all_exchange_ok,
}
all_passed = bool(all(assertions.values()))
verdict = (
    "The toroidal degree<->order exchange with the exact Gamma-constant "
    "C(nu,mu) = sqrt(2/pi) e^{-i pi nu}/Gamma(nu+mu+1/2) holds to 1e-30 at the "
    "PHYSICAL forced windings (mu, nu) = (1/2, d-1/2) for d in {2,3,4} -- not "
    "only at the generic grid points -- and the order-ladder factor reproduces "
    "the Hoefsmit mixing numerator d^2-1 at each d. This is numerical EVIDENCE "
    "that the even<->odd channel rotation descends to the physical toroidal "
    "windings as the Whipple exchange; it does NOT prove the modeling "
    "identification (a model validated by observables, not a theorem)."
) if all_passed else (
    "FAIL: the Whipple exchange or the forcing identity does not hold at one or "
    "more physical winding points -- see per_d for the offending d."
)

witness = {
    "computation": "whipple_physical_windings_probe",
    "description": (
        "Whipple degree<->order exchange + Hoefsmit forcing verified AT the "
        "physical forced windings (mu, nu) = (1/2, d-1/2) for axial distances "
        "d in {2,3,4} (meson d=2), at 50 dps. Evidence for the modeling layer "
        "of the Whipple-rotation identification; auditOnly."
    ),
    "discipline": "canonical-derivation / modeling-evidence (not a proof)",
    "auditOnly": True,
    "results": {
        "per_d": per_d,
        "gamma_constant_formula": "sqrt(2/pi) * e^{-i pi nu} / Gamma(nu + mu + 1/2)",
        "lean_cert_forcing": "QOU.BraidsAndKnots.toroidal_locus_forced (sorry-free)",
        "conjecture": "QOU.MassEndomorphism.WhippleRotationIntertwining (open)",
    },
    "assertions": assertions,
    "allPassed": all_passed,
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(
    os.path.dirname(__file__), "whipple-physical-windings-probe.witness.json"
)
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

for k, v in assertions.items():
    print(f"  {k}: {'PASS' if v else 'FAIL'}")
print(f"\nallPassed: {all_passed}")
for d, r in per_d.items():
    print(f"  d={d}: windings={r['windings_mu_nu']} "
          f"exchange_dev={r['max_dev_from_gamma_constant']} "
          f"forcing_ok={r['forcing_ok']}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {out}")
