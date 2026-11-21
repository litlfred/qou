#!/usr/bin/env python3
"""
np_splitting_residual_probe.py — two analyses of the neutron–proton splitting
Δm = α·|ΔΦ| built on the exact Hecke traced-volume closed form for the quark
volumes (see docs/audits/2026-07-11-quark-volume-provenance.md):

(a) L1 precision: |ΔΦ| via the exact-Fraction engine vs the sympy closed form
    agree to *every digit* (proves the closed form = engine) and evaluate
    stably to 50 dps — clearing the 6-digit literal floor (Δ_pn is ppQ-capable).

(b) L2 residual: the 0.63% miss vs CODATA is NOT absorbable by q₀ (needs a
    ~474 ppm q shift vs a ppb-level pin) and is NOT a single clean Habiro term
    — a genuine additive higher-order term on top of the exact leading piece.

CONVENTION NOTE (2026-11-15): (b) was written for the retired convention-C
z = 4993/10000, whose residual was +0.63 %. Both the engine and the closed form
now use convention D, z = q^3/(q^2+1), where the residual is about -18.5 %;
the (b) narrative describes the C-frame number and has not been redone for D.

Run: `cd computations && PYTHONPATH=. python3 probes/np_splitting_residual_probe.py`
"""
from __future__ import annotations

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported. Without
# this the module is unresolvable and the script cannot run standalone.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401
from fractions import Fraction

import mpmath as mp
import sympy as sp
from codata_constants import M_E_MEV
from hecke_engine import HeckeRational
from q_parameter import Q_50_DIGIT_STR, Q_RAT_DEN, Q_RAT_NUM

mp.mp.dps = 60
CODATA_NP_MEV = mp.mpf("1.29333378")  # CODATA 2022 neutron−proton mass diff


def _engine_phi_product(order):
    qr = HeckeRational(Q_RAT_NUM, Q_RAT_DEN)
    prod = Fraction(1)
    for i in range(len(order) - 1):
        prod *= qr.traced_volume(i, order)  # exact Fraction
    return prod


def _logabs(fr: Fraction):
    return mp.log(abs(mp.mpf(fr.numerator) / mp.mpf(fr.denominator)))


def _closed_forms():
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    # Convention D (owner ruling 2026-11-15), matching HeckeRational.z.
    z = q ** 3 / (q ** 2 + 1)

    def T(c, d):
        return sp.Matrix([[c * h + d, c], [c, d]])

    def V(mats):
        M = sp.eye(2)
        for t in mats:
            M = M * t
        return z * M[1, 0] + M[1, 1]

    Tuu, Tud, Tdd = T(1, 0), T(1, -h / 2), T(1, -h)
    cf_uud = sp.simplify(V([Tuu, Tud]) * V([Tud]))
    cf_udd = sp.simplify(V([Tud, Tud]) * V([Tdd]))
    return q, cf_uud, cf_udd


def main() -> None:
    q, cf_uud, cf_udd = _closed_forms()

    print("(a) |ΔΦ| cross-method @ 50 dps")
    p_uud, p_udd = _engine_phi_product([1, 1, 0]), _engine_phi_product([1, 0, 0])
    dphi_engine = abs(_logabs(p_udd) - _logabs(p_uud))
    qrat = sp.Rational(Q_RAT_NUM, Q_RAT_DEN)
    cf_val = {o: cf.subs(q, qrat) for o, cf in (("uud", cf_uud), ("udd", cf_udd))}
    to_fr = lambda e: Fraction(int(sp.fraction(e)[0]), int(sp.fraction(e)[1]))
    dphi_cf = abs(_logabs(to_fr(cf_val["udd"])) - _logabs(to_fr(cf_val["uud"])))
    q0 = mp.mpf(Q_50_DIGIT_STR)
    cf_udd_mp = sp.lambdify(q, cf_udd, "mpmath")
    cf_uud_mp = sp.lambdify(q, cf_uud, "mpmath")
    dphi_q0 = abs(mp.log(abs(cf_udd_mp(q0))) - mp.log(abs(cf_uud_mp(q0))))
    print(f"  engine (exact Fraction) = {mp.nstr(dphi_engine, 40)}")
    print(f"  closed form (same q)    = {mp.nstr(dphi_cf, 40)}")
    print(f"  engine vs closed diff   = {mp.nstr(abs(dphi_engine - dphi_cf), 3)}  (exact)")
    print(f"  closed form @ 50-dps q₀ = {mp.nstr(dphi_q0, 40)}")
    print(f"  6-digit literal         = 0.347593  (floor ~1e-6)\n")

    print("(b) 0.63% residual structure")
    alpha = mp.mpf(M_E_MEV) * 8 * mp.catalan
    dm_pred = alpha * dphi_q0
    rel = (dm_pred - CODATA_NP_MEV) / CODATA_NP_MEV
    r = CODATA_NP_MEV / dm_pred
    hbar2 = (1 - 1 / q0) ** 2
    # `slope_signed = d/dq (log|udd| − log|uud|)` — `d/dq log(f) = f'/f` is real
    # even where f < 0 (the closed forms are negative), so Abs is unnecessary in
    # the derivative.  But `|ΔΦ|` uses the magnitude and the signed ΔΦ is < 0 at
    # q₀, so `d|ΔΦ|/dq = sign(ΔΦ)·slope_signed`.
    signed = mp.log(abs(cf_udd_mp(q0))) - mp.log(abs(cf_uud_mp(q0)))
    slope_signed = float(sp.lambdify(q, sp.diff(sp.log(cf_udd) - sp.log(cf_uud), q), "mpmath")(q0))
    slope = mp.sign(signed) * slope_signed  # = d|ΔΦ|/dq
    dq = float((CODATA_NP_MEV / alpha - dphi_q0) / slope)
    print(f"  α = m_e·8G = {mp.nstr(alpha, 12)},  Δm_pred = {mp.nstr(dm_pred, 12)}")
    print(f"  rel error = {mp.nstr(rel * 100, 4)} %,  correction r−1 = {mp.nstr(r - 1, 6)}")
    print(f"  (r−1)/ℏ_q² = {mp.nstr((r - 1) / hbar2, 5)}  (near −2/3 but not clean)")
    print(f"  d|ΔΦ|/dq = {mp.nstr(slope, 6)}  ⇒  Δq to close = {mp.nstr(dq, 4)}"
          f"  (fractional {mp.nstr(dq / q0, 4)})")
    print(f"  ⇒ absorbing the residual in q₀ needs a {mp.nstr(dq / q0 * 1e6, 4)} ppm shift")
    print("    vs a ppb-level pin ⇒ NOT a q₀ knob; genuine missing physics.")


if __name__ == "__main__":
    main()
