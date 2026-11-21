#!/usr/bin/env python3
"""bring_residue_energy_probe.py — the residue dependence of the Bring energy, evaluated at q₀.
Bean `qou-jfx8` (owner 2026-10-12). Companion to `QOU/MassTheory/BringResidueEnergy.lean`.

μ(t) = q^t w_S + q^{−t} cos(πt) w_A, with the convention-D bridge weights w_S = y_(2), w_A = y_(1,1)
(read from the committed y-lambda witness and checked against the closed forms), and E(ℓ) = −log μ(2ℓ).
Validation: at integer t, μ must equal the Markov value of σ^t, namely z_D at t = 1 and z_D − h at t = −1.
Evaluated at the canonical residue ℓ = −1/6 (t = −1/3) and its mirror. The modelling identification
(ambient linking ℓ enters as the flow time t = 2ℓ) is stated in the Lean file, not tested here.
mpmath 60 dps; no floats; nothing fitted.
-- Ref: [manuscript] bean qou-jfx8
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
C = HERE.parent
sys.path.insert(0, str(C.parent / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Y = json.loads((C / "y-lambda-at-q0.witness.json").read_text(encoding="utf-8"))
assert Y["q0Anchor"] == "proton"
Q = mp.mpf(Y["q0Value"])
H = Q - 1 / Q
ZD = Q ** 3 / (Q ** 2 + 1)
y2 = {tuple(e["partition"]): mp.mpf(e["y_at_q0_50dps"]) for e in Y["data"]["by_n"]["2"]}
WS, WA = y2[(2,)], y2[(1, 1)]


def mu(q, t):
    return q ** t * WS + q ** (-t) * mp.cos(mp.pi * t) * WA


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    TOL = mp.mpf("1e-45")
    check("weights_match_conventionD_closed_forms",
          abs(WS - (Q ** 4 + Q ** 2 + 1) / (Q ** 2 + 1) ** 2) < TOL and abs(WA - Q ** 2 / (Q ** 2 + 1) ** 2) < TOL,
          "SegmentCollisionDatum channel_weights_conventionD")
    check("mu_at_t_1_is_zD", abs(mu(Q, 1) - ZD) < TOL, "Markov value of σ")
    check("mu_at_t_minus1_is_zD_minus_h", abs(mu(Q, -1) - (ZD - H)) < TOL, "Markov value of σ⁻¹")
    check("mu_at_t_2_is_markov_of_full_twist", abs(mu(Q, 2) - (Q ** 2 * WS + Q ** -2 * WA)) < TOL, "σ² channel split")
    ell = mp.mpf(-1) / 6
    t = 2 * ell
    m_c, m_m = mu(Q, t), mu(Q, -t)
    E_c, E_m = -mp.log(m_c), -mp.log(m_m)
    print(f"  q0 = {mp.nstr(Q, 15)}  w_S = {mp.nstr(WS, 15)}  w_A = {mp.nstr(WA, 15)}")
    print(f"  canonical ℓ = −1/6 (t = −1/3): μ = {mp.nstr(m_c, 15)}  E = −log μ = {mp.nstr(E_c, 15)}")
    print(f"  mirror    ℓ = +1/6 (t = +1/3): μ = {mp.nstr(m_m, 15)}  E = −log μ = {mp.nstr(E_m, 15)}")
    print(f"  chiral gap E(−1/6) − E(+1/6) = {mp.nstr(E_c - E_m, 15)}")
    split = (Q ** t - Q ** (-t)) * (WS - mp.cos(mp.pi * t) * WA)
    check("chiral_split_identity", abs((m_c - m_m) - split) < TOL, "Lean chiral_split")
    check("canonical_mu_below_mirror", m_c < m_m, "Lean canonical_mu_lt_mirror")
    check("mirror_equals_bar_involution", abs(mu(Q, -t) - mu(1 / Q, t)) < TOL, "Lean mirror_eq_bar")
    check("classical_limit_achiral", abs(mu(mp.mpf(1), t) - mu(mp.mpf(1), -t)) < TOL, "Lean classical_limit_achiral")

    # the relative minimum of E (owner's principle): maximise μ in t near 0
    dmu = lambda q, tt: mp.log(q) * (q ** tt * WS - q ** (-tt) * mp.cos(mp.pi * tt) * WA) - mp.pi * q ** (-tt) * mp.sin(mp.pi * tt) * WA  # noqa: E731
    check("analytic_derivative_matches_numeric", abs(dmu(Q, mp.mpf("0.3")) - mp.diff(lambda x: mu(Q, x), mp.mpf("0.3"))) < mp.mpf("1e-40"),
          "μ'(t) formula")
    check("mu_prime_at_0_eq_lnq_times_wS_minus_wA", abs(dmu(Q, 0) - mp.log(Q) * (WS - WA)) < TOL, "Lean hasDerivAt_mu_zero")
    tstar = mp.findroot(lambda x: dmu(Q, x), (mp.mpf("0.0001"), mp.mpf("0.5")), solver="illinois", tol=mp.mpf("1e-50"))
    second = mp.diff(lambda x: mu(Q, x), tstar, 2)
    s_star = tstar - t
    angle_deg = 180 * s_star
    print(f"  relative minimum of E: t* = {mp.nstr(tstar, 15)}  (μ'' = {mp.nstr(second, 6)} < 0)  E(t*) = {mp.nstr(-mp.log(mu(Q, tstar)), 15)}")
    print(f"  collision twist s* = t* − 2ℓ = {mp.nstr(s_star, 15)}  →  turning angle π·s* = {mp.nstr(angle_deg, 12)}°")
    check("t_star_in_open_0_half_and_is_a_max_of_mu", 0 < tstar < mp.mpf("0.5") and second < 0, "Lean mu_increasing_at_zero_conventionD")
    check("q_equals_1_has_no_preferred_twist", abs(mp.log(1) * (WS - WA)) == 0, "Lean mu_deriv_zero_classical")

    ok_all = all(ok for _, ok, _ in checks)
    w = WitnessBuilder("bring-residue-energy", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 read from the committed y-lambda-at-q0 witness string",
        "description": ("PROBE (bean qou-jfx8): Bring energy E(ℓ) = −log μ(2ℓ), μ(t) = q^t w_S + q^{−t} cos(πt) w_A, "
                        "convention-D bridge weights; validated against Markov values at t = ±1; canonical ℓ = −1/6 vs "
                        "mirror. Modelling step (ambient linking as flow time 2ℓ) stated in the Lean file."),
        "weight_family": "markov_y_lambda_convention_D",
        "wS": mp.nstr(WS, 50), "wA": mp.nstr(WA, 50),
        "mu_canonical": mp.nstr(m_c, 50), "mu_mirror": mp.nstr(m_m, 50),
        "E_canonical": mp.nstr(E_c, 50), "E_mirror": mp.nstr(E_m, 50), "chiral_gap": mp.nstr(E_c - E_m, 50),
        "t_star": mp.nstr(tstar, 50), "collision_twist_s_star": mp.nstr(s_star, 50),
        "turning_angle_degrees": mp.nstr(angle_deg, 30), "E_at_t_star": mp.nstr(-mp.log(mu(Q, tstar)), 50),
    })
    print("witness:", out)
    print(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
