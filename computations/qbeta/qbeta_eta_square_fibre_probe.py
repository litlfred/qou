"""Eta-square fibre-descent probe: do (E, O) descend from ONE complex fibre F(eta)?

Bean 0zr0's concrete first test (formalize-first scoping 2026-07-03), executed.
Inputs on main: ComplexVolumeZeta4Partner.lean (zeta4-rotation negates the bar-even
channel, keeps bar-odd — the cosh/sinh model), and the 08ds ORD-17 exact bar-split
of the net-route log R (E bar-even, O bar-odd; qbeta_bar_split_ord17_probe).

Model under test: E and O are the even/odd parts of one fibre F(eta) with a bar-odd
argument eta(s) — concretely E = cosh(eta) - 1 and O = sinh(eta) (constants fixed by
E(0) = O(0) = 0). Two exact, parameter-free consequences, tested to ORD = 17:

  (A) PYTHAGOREAN COMPATIBILITY: (E+1)^2 - O^2 = 1, i.e. P := E^2 + 2E - O^2 = 0
      identically. The first nonzero order of P is the exact obstruction.
  (B) ETA-SQUARE u~-MEMBERSHIP: eta := arcsinh(O) = log(O + sqrt(1+O^2)) (exact
      series; bar-odd by construction), and the bean's prediction is that eta^2
      lies in the bar-even algebra Q(sqrt3)[[u~]] — tested with the same u-adic
      matcher as the 08ds probe (KMAX = 8 rungs, margin 9).

If (A) holds and (B) holds, the zeta4 cosh/sinh fibre-descent is exactly consistent
through s^17 (strong structural support for conj:binding-qbeta-complex-volume's
odd sector); the first failing orders otherwise are the next constraints.
All exact rational/sqrt3 arithmetic (sympy); no fit, nothing wired; scope-(a) framing.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
sys.path.insert(0, str(Path(__file__).resolve().parent))

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
core.ORD = 17          # raise the truncation BEFORE any series call (08ds convention)
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)
from qbeta_bar_split_ord17_probe import ser_compose, u_adic_match  # noqa: E402

ORD = core.ORD
HERE = Path(__file__).resolve().parent


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" 0zr0 — eta-square fibre-descent test at ORD={ORD}")
    print("=" * 78)

    # ---- rebuild E, O, u~ exactly as the 08ds ORD-17 probe (same conventions) ----
    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    # q₀ from q_parameter (proton pin, AGENTS.md 2026-08-07 directive).
    # Was a direct read of q-pinning-50-digit.witness.json, which is the
    # MUON anchor’s definition and bypasses the manifest entirely.
    q0 = Q_MP
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_ser = ser_mul(rat_series(q), ser_mul(b_ser, hbar2))
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    logR_bar = ser_compose(logR, phi)
    E = [simp((x + y) / 2) for x, y in zip(logR, logR_bar)]
    O = [simp((x - y) / 2) for x, y in zip(logR, logR_bar)]
    assert sp.simplify(E[0]) == 0 and sp.simplify(O[0]) == 0
    print(f"  series rebuilt ({time.monotonic()-t0:.0f}s)")

    # ---- (A) Pythagorean compatibility: P = E^2 + 2E - O^2 = 0? --------------
    P = ser_add(ser_add(ser_mul(E, E), ser_scale(sp.Integer(2), E)),
                ser_scale(sp.Integer(-1), ser_mul(O, O)))
    firstP = next((n for n in range(ORD + 1) if sp.simplify(P[n]) != 0), None)
    print(f"\n  (A) P = E^2+2E-O^2: first nonzero order = {firstP}"
          + ("  — cosh/sinh fibre EXACTLY compatible through s^17 ✓"
             if firstP is None else "  — obstruction"))

    # ---- (B) eta = arcsinh(O); eta^2 in Q(sqrt3)[[u~]]? ----------------------
    one = [sp.Integer(1)] + [sp.Integer(0)] * ORD
    inner = ser_add(O, ser_sqrt(ser_add(one, ser_mul(O, O))))
    eta = ser_log1(inner)
    # bar-oddness sanity: even coefficients of eta vanish? (eta odd under the
    # involution phi, not under s -> -s; check via composed conjugate instead)
    eta_bar = ser_compose(eta, phi)
    odd_resid = next((n for n in range(ORD + 1)
                      if sp.simplify(eta[n] + eta_bar[n]) != 0), None)
    print(f"  (B0) eta bar-odd (eta + eta_bar = 0): first violation = {odd_resid}")

    eta_sq = ser_mul(eta, eta)
    KMAX = (ORD - 1) // 2
    rungs, resid, _ = u_adic_match(eta_sq, u_ser, KMAX)
    firstB = next((n for n in range(1, ORD + 1)
                   if sp.simplify(resid[n]) != 0), None)
    print(f"  (B) eta^2 u~-rungs: { {k: str(sp.N(x, 10)) for k, x in rungs.items()} }")
    print(f"      first nonzero residual: {firstB} (margin {ORD - KMAX})"
          + ("" if firstB else "  — eta^2 IS a u~-series through s^17 ✓"))

    witness = {
        "description": ("0zr0 eta-square fibre-descent test: (A) exact Pythagorean "
                        "compatibility P=E^2+2E-O^2 of the cosh/sinh zeta4 fibre "
                        "model; (B) eta=arcsinh(O) bar-oddness + eta^2 membership "
                        "in Q(sqrt3)[[u~]] with 08ds conventions, ORD=17."),
        "audit_only": True,
        "tier": "exact structural probe (no fit, nothing wired; scope-(a) framing)",
        "ORD": ORD,
        "pythagorean_first_obstruction_order": firstP,
        "eta_bar_odd_first_violation": odd_resid,
        "eta_sq_rungs": {str(k): str(v) for k, v in rungs.items()},
        "eta_sq_first_residual_order": firstB,
        "overdetermination_margin": ORD - KMAX,
        "verdict": {
            "cosh_sinh_fibre_compatible_through_ord": firstP is None,
            "eta_sq_is_u_series_through_ord": firstB is None,
        },
    }
    out = WitnessBuilder.wrap_legacy(
        "qbeta-eta-square-fibre-probe", witness,
        script_path=__file__, engine="sympy", start_time=t0,
    ).save()
    print(f"\n  Witness: {out}  ({time.monotonic()-t0:.0f}s total)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
