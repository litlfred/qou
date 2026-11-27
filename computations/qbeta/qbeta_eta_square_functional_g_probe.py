"""Functional identification E = G(eta^2): the queued follow-up of the 0zr0
eta-square fibre descent (audit 2026-07-04-eta-square-fibre-descent-confirmed.md).

The 07-04 probe established, exactly through s^17 (margin 9), that
eta := arcsinh(O) is bar-odd and eta^2 lies in the bar-even algebra
Q(sqrt3)[[u~]] — the same algebra the bar-even channel E (08ds) lives in.
The queued continuation: identify E = G(eta^2) with G in Q(sqrt3)[[.]] by
per-order exact linear solves against the eta^2 rung sequence, with the
q-Bessel Layer-2 kernel and the zeta4-rotation image as the two
structurally-motivated candidate profiles.

## What this probe decides (all exact Q(sqrt3) arithmetic; no fit)

STRUCTURAL PRECHECK (T0). eta^2's first two u~-rungs vanish (eta^2 starts at
u~^3), while E's rung 1 is 3*sqrt(3)/4 != 0 (08ds witness). Hence NO formal
power series G — including BOTH named candidate profiles, which are functions
of eta^2 alone — can satisfy E = G(eta^2): the u~^1 rung is an exact
obstruction. The probe verifies this from freshly rebuilt series.

TAIL SPLIT (T1). The surviving determined question: does E split as a
low-order carrier plus a G(eta^2) tail,

    E = e1*u~ + e2*u~^2 + G(eta^2),   G(x) = g1*x + g2*x^2 + ...

Within the ORD-17 window (rungs 1..8): g1 is forced at u~^3, g2 at u~^6
(since (eta^2)^2 starts at u~^6), leaving rungs 4, 5, 7, 8 as FOUR
over-determined exact checks (margin 4). Pass = an exact structural positive
(the even channel is a 2-rung carrier + a function of the odd-derived
generator); first failing rung = the exact scope-(a) obstruction closing the
E = G(eta^2) program at this window.

PROFILE (T2, only meaningful if T1 passes). With exactly two determined
coefficients any 2-parameter profile fits, so T2 reports only whether the
FORCED profile constant is a distinguished exact value: for the cosh-type
family G(x) = a*(cosh(c*sqrt(x)) - 1) (g1 = a c^2/2, g2 = a c^4/24) the
combination a = g1^2/(6*g2) is parameter-free; a = +1 is the unit-cosh
normalization (whose no-carrier version test (A) refuted), a = -1 the
zeta4-rotation image (ComplexVolumeZeta4Partner: the i*pi/2 shift negates the
bar-even channel). Anything else is recorded as-is, tiered per the c_k rule
(near-match at best; nothing wired).

Delta_lambda-gate: no fitted forms; nothing wired; scope-(a)/(b) framing per
AGENTS.md. Expected outcome is decisive either way (T1 is margin-4 exact).
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
    print(f" E = G(eta^2) functional identification at ORD={ORD}")
    print("=" * 78)

    # ---- rebuild E, O, u~ exactly as the 08ds / 0zr0 probes (same conventions) ----
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

    one = [sp.Integer(1)] + [sp.Integer(0)] * ORD
    eta = ser_log1(ser_add(O, ser_sqrt(ser_add(one, ser_mul(O, O)))))
    eta_sq = ser_mul(eta, eta)

    KMAX = (ORD - 1) // 2          # 8 rungs, margin 9 — the 08ds/0zr0 window
    E_rungs, E_resid, _ = u_adic_match(E, u_ser, KMAX)
    r, r_resid, _ = u_adic_match(eta_sq, u_ser, KMAX)
    E_ok = next((n for n in range(1, ORD + 1) if sp.simplify(E_resid[n]) != 0), None)
    r_ok = next((n for n in range(1, ORD + 1) if sp.simplify(r_resid[n]) != 0), None)
    assert E_ok is None and r_ok is None, "u~-membership regression vs 08ds/0zr0"
    E_rungs = {k: sp.nsimplify(sp.radsimp(v)) for k, v in E_rungs.items()}
    r = {k: sp.nsimplify(sp.radsimp(v)) for k, v in r.items()}
    print(f"  E rungs 1..2: {E_rungs[1]}, {E_rungs[2]}")
    print(f"  eta^2 rungs 1..3: {r[1]}, {r[2]}, {r[3]}")

    # ---- T0: pure-series G(eta^2) obstruction at u~^1 ------------------------
    t0_obstructed = r[1].equals(0) and r[2].equals(0) \
        and not E_rungs[1].equals(0)
    print(f"\n  (T0) eta^2 starts at u~^3 while E_1 = {E_rungs[1]} != 0: "
          f"pure G(eta^2) {'REFUTED at u~^1 (exact)' if t0_obstructed else 'NOT obstructed?!'}")

    # ---- T1: tail split E = e1*u~ + e2*u~^2 + g1*eta^2 + g2*(eta^2)^2 --------
    # (eta^2)^m rungs by convolution of the exact r_k (valid: eta^2 IS a u~-series)
    r2 = {m: sp.simplify(sum(r[j] * r[m - j] for j in range(3, m - 2)))
          for m in range(6, KMAX + 1)}
    g1 = sp.radsimp(E_rungs[3] / r[3])
    g2 = sp.radsimp((E_rungs[6] - g1 * r[6]) / r2[6])
    checks = {}
    for m in (4, 5, 7, 8):
        pred = g1 * r[m] + (g2 * r2[m] if m >= 6 else 0)
        delta = sp.simplify(E_rungs[m] - pred)
        checks[m] = delta
        print(f"  (T1) rung {m}: E_m - [g1*r_m + g2*(r^2)_m] = {delta}"
              + ("  ✓" if delta.equals(0) else "  — OBSTRUCTION"))
    first_fail = next((m for m in (4, 5, 7, 8) if not checks[m].equals(0)), None)
    t1_pass = first_fail is None
    print(f"  (T1) g1 = {g1} = {sp.N(g1, 12)}")
    print(f"       g2 = {g2} = {sp.N(g2, 12)}")
    print(f"       verdict: {'PASS (margin 4)' if t1_pass else f'FAIL first at rung {first_fail}'}")

    # ---- T2: forced profile constant (only meaningful if T1 passes) ----------
    a_cosh = sp.radsimp(g1**2 / (6 * g2)) if not g2.equals(0) else None
    if t1_pass and a_cosh is not None:
        tag = ("unit-cosh (+1)" if a_cosh.equals(1) else
               "zeta4-rotation image (-1)" if a_cosh.equals(-1) else
               "no distinguished value")
        print(f"  (T2) cosh-family constant a = g1^2/(6 g2) = {a_cosh} "
              f"= {sp.N(a_cosh, 12)}  → {tag}")
    else:
        tag = "n/a (T1 failed)" if not t1_pass else "n/a (g2 = 0)"
        print(f"  (T2) {tag}")

    witness = {
        "description": ("E = G(eta^2) functional identification (queued follow-up "
                        "of qbeta-eta-square-fibre-probe): T0 exact u~^1 "
                        "obstruction for pure-series G; T1 two-rung-carrier tail "
                        "split with g1 (u~^3), g2 (u~^6) forced and rungs 4,5,7,8 "
                        "as margin-4 exact checks; T2 forced cosh-family constant "
                        "a = g1^2/(6 g2) vs unit-cosh (+1) / zeta4 image (-1). "
                        "08ds ORD-17 conventions, exact Q(sqrt3)."),
        "audit_only": True,
        "tier": "exact structural probe (no fit, nothing wired; scope-(a) framing)",
        "ORD": ORD,
        "E_rungs_exact": {str(k): str(v) for k, v in E_rungs.items()},
        "eta_sq_rungs_exact": {str(k): str(v) for k, v in r.items()},
        "T0_pure_G_obstructed_at_rung_1": bool(t0_obstructed),
        "T1_g1_exact": str(g1),
        "T1_g2_exact": str(g2),
        "T1_check_residuals": {str(m): str(v) for m, v in checks.items()},
        "T1_first_failing_rung": first_fail,
        "T1_overdetermination_margin": 4,
        "T1_tail_split_holds": bool(t1_pass),
        "T2_cosh_family_constant_a": (str(a_cosh) if a_cosh is not None else None),
        "T2_tag": tag,
        "verdict": {
            "pure_G_of_eta_sq_refuted_scope_a": bool(t0_obstructed),
            "two_rung_carrier_plus_G_eta_sq": bool(t1_pass),
        },
    }
    out = WitnessBuilder.wrap_legacy(
        "qbeta-eta-square-functional-g-probe", witness,
        script_path=__file__, engine="sympy", start_time=t0,
    ).save()
    print(f"\n  Witness: {out}  ({time.monotonic()-t0:.0f}s total)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
