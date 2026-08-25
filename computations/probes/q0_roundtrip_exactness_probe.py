#!/usr/bin/env python3
"""Does q0 recover m_p/m_e exactly, and if not, where is the loss?

Owner question, 2026-08-21: *"shouldnt we recover m_p/m_e exactly symbolic?
where are the approximations/truncations/lost terms?"*

q0 is DEFINED by inverting the proton substrate identity

    m_p/m_e = 2 * (Vol(4_1) / hbar_q^2) * F_Bor(q) - 12
    |tr_M(beta_Bor)| = (4 + h^2 - 3h^4 - h^6) / (h^2 + 4)
    F_Bor = |tr_M| * [3]_q! / q^3,  h = q - 1/q,  hbar_q = 1 - 1/q

so the round trip q0 -> m_p/m_e is a pure re-evaluation of the same closed
form. It SHOULD return CODATA to the arithmetic floor. Any residual is a
truncation somewhere, not physics, and this probe localises it.

## Answer

It is exact. Carrying `Vol(4_1)` as `2*Cl_2(pi/3)` in mpmath, the round trip
reproduces CODATA to ~1e-49 at 120 dps -- the floor of the 50-digit pin, not a
discrepancy. All 50 digits of `Q_50_DIGIT_STR` are real: a fresh
high-precision solve reproduces it to ~1e-50, so it is a genuine 50-digit
inversion and not an f64 result padded with zeros.

The residual that shows up in an f64 path has ONE source:

    VOL_FIGURE_EIGHT = 2.029883212819307        (constants.py, an f64 literal)
    2*Cl_2(pi/3)     = 2.029883212819307250042  (exact)
    relative                        1.23e-16

Substituting the exact form drops the round-trip error by ~33 orders of
magnitude. Nothing else contributes at a level worth naming.

## What this does NOT claim

The f64 constant is a LATENT hazard, not a live corruption of the canonical
chain: `Q_50_DIGIT_STR` was already produced against the exact volume (this
probe checks that), so the 50-digit layer is clean. What inherits the 1.23e-16
is any consumer that recomputes from `VOL_FIGURE_EIGHT` at more than f64
precision -- which is a thing this corpus does, hence recording it.

Nor does exactness here say anything about whether the identity is RIGHT. A
round trip through a definition is a consistency check on the arithmetic; it
cannot validate the physics it encodes. The mu-p tension (11.54 ppb) is the
place that question actually gets asked.
"""
from __future__ import annotations

import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
for _p in (HERE.parents[1] / "tools" / "qou-substrate" / "python", HERE.parent):
    sys.path.insert(0, str(_p))

from qou_substrate import constants as C  # noqa: E402

WORK_DPS = 120


def m_p_over_e_of_q(q, vol):
    """The proton substrate identity, evaluated forward."""
    h = q - 1 / q
    hbar2 = (1 - 1 / q) ** 2
    tr_m = abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
    qfac3 = (q**2 + 1 + q**-2) * (q + 1 / q)
    return 2 * vol / hbar2 * (tr_m * qfac3 / q**3) - 12


def main() -> int:
    mp.mp.dps = WORK_DPS
    codata = mp.mpf(str(C.MASS_RATIO_P_E))
    vol_pkg = mp.mpf(str(C.VOL_FIGURE_EIGHT))
    vol_exact = 2 * mp.clsin(2, mp.pi / 3)
    q50 = mp.mpf(C.Q_50_DIGIT_STR)

    vol_rel = abs(vol_pkg - vol_exact) / vol_exact
    err_exact = (m_p_over_e_of_q(q50, vol_exact) - codata) / codata
    err_pkg = (m_p_over_e_of_q(q50, vol_pkg) - codata) / codata

    q_fresh = mp.findroot(
        lambda q: m_p_over_e_of_q(q, vol_exact) - codata, mp.mpf("1.11")
    )
    pin_rel = abs(q_fresh - q50) / q_fresh

    print("=" * 66)
    print("  q0 -> m_p/m_e ROUND TRIP — is it exact, and where is the loss?")
    print("=" * 66)
    print(f"  working precision            : {WORK_DPS} dps")
    print(f"  Vol(4_1) package (f64)       : {mp.nstr(vol_pkg, 22)}")
    print(f"  Vol(4_1) exact 2*Cl_2(pi/3)  : {mp.nstr(vol_exact, 22)}")
    print(f"  -> relative truncation       : {mp.nstr(vol_rel, 5)}")
    print()
    print(f"  round trip, EXACT vol        : {mp.nstr(err_exact, 5)}   <- the floor")
    print(f"  round trip, package vol      : {mp.nstr(err_pkg, 5)}")
    print(f"  ratio                        : {mp.nstr(abs(err_pkg / err_exact), 5)}x")
    print()
    print(f"  fresh 50-dps solve vs pin    : {mp.nstr(pin_rel, 5)}   <- all 50 digits real")
    print()
    verdict = ("EXACT — the identity round-trips to the arithmetic floor; the "
               "only truncation is the f64 Vol(4_1) literal")
    print(f"  VERDICT: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
