#!/usr/bin/env python3
"""80-dps Newton polish of the q0 anchor, with the error carried as a cut.

Bean ``qou-y7ek`` (PPQ-1, L1).  A PRECISION change only: the value of q0 is a
master parameter and is not moved here.  The probe asserts that the polished
root rounds to the published ``Q_50_DIGIT_STR`` and to the 70-digit ``Q_MP``,
and it FAILS if it does not -- a polish that shifted q0 beyond rounding would
be a re-pin, which is the owner's call, not a precision fix.

What it computes
----------------
q0 is DEFINED as the root of the one-term proton substrate identity

    F(q) = 2 (Vol(4_1) / hbar_q^2) |tr_M(beta_Bor)| [3]_q! / q^3 - 12,
    |tr_M(beta_Bor)| = (4 + h^2 - 3h^4 - h^6) / (h^2 + 4),
    h = q - 1/q,  hbar_q = 1 - 1/q,  Vol(4_1) = 2 Cl_2(pi/3),

    F(q0) = (m_p/m_e)_CODATA            (CAL-2 anchor)

1. Explicit Newton on F at ``WORK_DPS`` with a numerical derivative
   (``mp.diff`` at the same precision), iterated until the step is below
   10^-(WORK_DPS - 10).  The step history is recorded so the quadratic
   convergence is visible rather than asserted.
2. The polished root is compared with ``q_at(95)``, ``Q_MP`` (70 digits) and
   ``Q_50_DIGIT_STR`` (50 digits).  Each must agree to its own length.
3. The error is recorded as a two-sided rational cut, not as an epsilon:
   ``lo = floor(q * 10^K) / 10^K`` and ``hi = lo + 10^-K`` with K = 85, and the
   residual F(q) - (m_p/m_e) changes sign across [lo, hi].  Both signs are
   evaluated at two precisions (``WORK_DPS`` and ``2 * WORK_DPS``) and must
   agree.  This is ``QOU.Core.LawvereCut.Cut.ofInterval lo hi`` with width
   10^-85 < 10^-80: a located cut at resolution 10^-80 over Q.  It is a
   numerical certificate (mpmath, two independent precisions), not an
   interval-arithmetic proof; that limit is stated in the witness.
4. Round trip: F(q0) / (m_p/m_e) - 1 at the polished root, and the MeV form
   m_e * F(q0) against the anchor m_e * (m_p/m_e).  Both below 10^-80.
5. The two-term proton pin ``q_proton_two_term_at`` gets the same treatment
   as a NAMED COMPARISON (owner ruling 2026-11-20: never the default).

What it does not claim
----------------------
A round trip through the defining identity is a consistency check on the
arithmetic.  It says nothing about whether the identity is right; the mu-p
tension is where that is asked.  No measured value enters any proof here: the
CODATA ratio is the CAL-2 calibration input of a computation, not a premise of
a theorem.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE = HERE.parent
sys.path.insert(0, str(COMPUTE))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate import constants as C  # noqa: E402
from codata_2022_source import M_E_MEV  # noqa: E402

WORK_DPS = 120
TARGET_DPS = 80
CUT_DIGITS = 85


def _f_one_term(q, vol):
    h = q - 1 / q
    hbar_sq = (1 - 1 / q) ** 2
    tr_m = abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
    qf3 = (q**2 + 1 + q**-2) * (q + 1 / q)
    return 2 * vol / hbar_sq * (tr_m * qf3 / q**3) - 12


def _f_two_term(q, vol):
    q2 = q * q
    return _f_one_term(q, vol) + 2 * (q2 - 1) ** 4 * (q2 * q2 + q2 + 1) / (27 * q2**3)


def _newton(f, ratio, vol, q_start):
    """Explicit Newton; returns (root, list of |step| as strings)."""
    tol = mp.mpf(10) ** (-(mp.mp.dps - 10))
    q = mp.mpf(q_start)
    steps = []
    for _ in range(60):
        g = f(q, vol) - ratio
        dg = mp.diff(lambda x: f(x, vol), q)
        step = g / dg
        q -= step
        steps.append(mp.nstr(abs(step), 5))
        if abs(step) < tol:
            return q, steps
    raise RuntimeError("Newton did not converge in 60 steps")


def _cut(f, q, ratio_str, vol_at):
    """Rational two-sided cut of width 10^-CUT_DIGITS around q, with the sign
    of the residual checked at two precisions."""
    scale = 10**CUT_DIGITS
    with mp.workdps(WORK_DPS + 20):
        lo_num = int(mp.floor(q * scale))
    hi_num = lo_num + 1
    signs = {}
    for dps in (WORK_DPS, 2 * WORK_DPS):
        with mp.workdps(dps):
            vol = vol_at(dps)
            ratio = mp.mpf(ratio_str)
            r_lo = f(mp.mpf(lo_num) / scale, vol) - ratio
            r_hi = f(mp.mpf(hi_num) / scale, vol) - ratio
            signs[dps] = (mp.sign(r_lo), mp.sign(r_hi), mp.nstr(r_lo, 5), mp.nstr(r_hi, 5))
    s = list(signs.values())
    stable = all(x[:2] == s[0][:2] for x in s)
    brackets = stable and s[0][0] * s[0][1] < 0
    return {
        "lo": f"{lo_num}/10^{CUT_DIGITS}",
        "hi": f"{hi_num}/10^{CUT_DIGITS}",
        "width": f"1e-{CUT_DIGITS}",
        "residual_at_lo": {str(k): v[2] for k, v in signs.items()},
        "residual_at_hi": {str(k): v[3] for k, v in signs.items()},
        "sign_change": bool(brackets),
        "signs_stable_across_precisions": bool(stable),
        "lean_shape": "QOU.Core.LawvereCut.Cut.ofInterval lo hi (over Q)",
    }, brackets


def _agree_digits(a, b):
    with mp.workdps(WORK_DPS):
        d = abs(a - b)
        if d == 0:
            return WORK_DPS
        return int(mp.floor(-mp.log10(d / abs(a))))


def main() -> int:
    if os.environ.get("QOU_Q0_SHADOW"):
        print("QOU_Q0_SHADOW is set: this probe certifies the canonical pin only.")
        return 2

    mp.mp.dps = WORK_DPS
    vol = C.vol_4_1_at(WORK_DPS + 10)
    ratio_str = C.MASS_RATIO_P_E_STR
    ratio = mp.mpf(ratio_str)
    m_e = mp.mpf(str(M_E_MEV))

    # 1. Newton polish, one-term (canonical) pin.
    q0, steps = _newton(_f_one_term, ratio, vol, "1.10997858")
    resid_rel = abs(_f_one_term(q0, vol) / ratio - 1)

    # 2. Unchanged-value checks against every published form of q0.
    q_at95 = C.q_at(95)
    q_mp70 = C.Q_MP
    q_50 = mp.mpf(C.Q_50_DIGIT_STR)
    polished80 = mp.nstr(q0, TARGET_DPS, strip_zeros=False)
    rounds_to_50 = mp.nstr(q0, 50, strip_zeros=False) == C.Q_50_DIGIT_STR
    rounds_to_70 = mp.nstr(q0, 70, strip_zeros=False) == mp.nstr(q_mp70, 70, strip_zeros=False)
    agree_q_at95 = _agree_digits(q0, q_at95)

    # 3. Cut.
    cut, brackets = _cut(_f_one_term, q0, ratio_str, C.vol_4_1_at)

    # 4. MeV round trip against the anchor m_e * (m_p/m_e).
    m_p_anchor = m_e * ratio
    m_p_round = m_e * _f_one_term(q0, vol)
    mev_rel = abs(m_p_round / m_p_anchor - 1)
    # The same round trip from the 50-digit string, for comparison: this is
    # the floor every 50-digit consumer inherits.
    resid_rel_50 = abs(_f_one_term(q_50, vol) / ratio - 1)

    # 5. Two-term comparison pin (named comparison only).
    q2t, steps2t = _newton(_f_two_term, ratio, vol, "1.10997859")
    resid2t = abs(_f_two_term(q2t, vol) / ratio - 1)
    q2t_ref = C.q_proton_two_term_at(95)
    cut2t, brackets2t = _cut(_f_two_term, q2t, ratio_str, C.vol_4_1_at)

    tol = mp.mpf(10) ** (-TARGET_DPS)
    print(f"q0 (80 digits)            = {polished80}")
    print(f"Newton steps              = {steps}")
    print(f"round-trip rel residual   = {mp.nstr(resid_rel, 5)}  (50-digit q0: {mp.nstr(resid_rel_50, 5)})")
    print(f"m_p MeV rel vs anchor     = {mp.nstr(mev_rel, 5)}")
    print(f"rounds to Q_50_DIGIT_STR  = {rounds_to_50};  to Q_MP(70) = {rounds_to_70}")
    print(f"agrees with q_at(95) to   = {agree_q_at95} digits")
    print(f"cut                       = [{cut['lo']}, {cut['hi']}], sign change {cut['sign_change']}")
    print(f"two-term (comparison) q   = {mp.nstr(q2t, TARGET_DPS, strip_zeros=False)}")
    print(f"two-term rel residual     = {mp.nstr(resid2t, 5)}, cut sign change {cut2t['sign_change']}")

    w = WitnessBuilder("q0-80dps-anchor-roundtrip", engine="mpmath")
    w.set_description(
        "80-dps Newton polish of the canonical one-term proton pin q0 (bean qou-y7ek). "
        "Precision only: asserts the polished root rounds to Q_50_DIGIT_STR and Q_MP, "
        "so q0 is unchanged. Error recorded as a rational two-sided cut of width 1e-85."
    )
    w.set_audit_only("docs/audits/2026-11-27-q0-80dps-anchor-polish.md")
    w.add_parameter("work_dps", WORK_DPS)
    w.add_parameter("target_dps", TARGET_DPS)
    w.add_parameter("cut_digits", CUT_DIGITS)
    w.add_parameter("anchor", "m_p/m_e (CAL-2), one-term proton substrate identity")
    w.add_parameter("mass_ratio_p_e", ratio_str)
    w.add_data("q0_one_term", {
        "q0_80_digits": polished80,
        "newton_steps_abs": steps,
        "roundtrip_rel_residual": mp.nstr(resid_rel, 5),
        "roundtrip_rel_residual_from_50_digit_string": mp.nstr(resid_rel_50, 5),
        "m_p_MeV_anchor": mp.nstr(m_p_anchor, TARGET_DPS),
        "m_p_MeV_roundtrip": mp.nstr(m_p_round, TARGET_DPS),
        "m_p_MeV_rel_residual_vs_anchor": mp.nstr(mev_rel, 5),
        "rounds_to_Q_50_DIGIT_STR": rounds_to_50,
        "rounds_to_Q_MP_70": rounds_to_70,
        "agree_digits_with_q_at_95": agree_q_at95,
        "cut": cut,
    })
    w.add_data("q_two_term_comparison_only", {
        "status": "NAMED COMPARISON, never the default (owner ruling 2026-11-20)",
        "q_80_digits": mp.nstr(q2t, TARGET_DPS, strip_zeros=False),
        "newton_steps_abs": steps2t,
        "roundtrip_rel_residual": mp.nstr(resid2t, 5),
        "agree_digits_with_q_proton_two_term_at_95": _agree_digits(q2t, q2t_ref),
        "cut": cut2t,
    })
    w.add_assertion("q0_roundtrip_below_1e-80", mp.nstr(resid_rel, 5), "0", f"1e-{TARGET_DPS}")
    w.add_assertion("m_p_MeV_roundtrip_below_1e-80", mp.nstr(mev_rel, 5), "0", f"1e-{TARGET_DPS}")
    w.add_assertion("q0_unchanged_rounds_to_Q_50", str(int(rounds_to_50)), "1", "0")
    w.add_assertion("q0_unchanged_rounds_to_Q_MP_70", str(int(rounds_to_70)), "1", "0")
    w.add_assertion("q0_cut_brackets_root", str(int(brackets)), "1", "0")
    w.add_assertion("q2t_roundtrip_below_1e-80", mp.nstr(resid2t, 5), "0", f"1e-{TARGET_DPS}")
    w.add_assertion("q2t_cut_brackets_root", str(int(brackets2t)), "1", "0")
    w.add_caveat(
        "The cut is a numerical certificate: the residual sign at both rational "
        "endpoints agrees at 120 and 240 dps. It is not an interval-arithmetic proof."
    )
    w.add_caveat(
        "A round trip through the defining identity checks arithmetic, not physics. "
        "The CODATA ratio is the CAL-2 input of this computation and enters no proof."
    )
    w.save({"q0Anchor": "proton",
            "q0AnchorReason": "certifies the canonical one-term proton pin q_at(); the "
                              "two-term pin appears only in the labelled comparison block"})

    ok = (resid_rel < tol and mev_rel < tol and rounds_to_50 and rounds_to_70
          and brackets and resid2t < tol and brackets2t)
    if not (rounds_to_50 and rounds_to_70):
        print("STOP: the polished root does not round to the published q0. "
              "That is a re-pin, not a precision fix; it needs the owner.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
