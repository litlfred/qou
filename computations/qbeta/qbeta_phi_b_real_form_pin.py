#!/usr/bin/env python3
"""qbeta_phi_b_real_form_pin.py — pin the REAL-integral representation of the
Faddeev Φ_b on the fibre saddle (real b, real z) against the validated contour
evaluator (phi_b_evaluator.py, battery-gated, Hikami math/0604094-verified).

INFRASTRUCTURE (no c_k values, no wiring, no fits). This is the measurement
that backs the Lean *construction* of Φ_b
(QOU.MathlibExt.FaddeevPhiBRealIntegral): on the fibre saddle the contour
integral collapses to a REAL single integral plus explicit Gaussian/constant
terms — the "combinatorial/real evaluation" route that needs no contour
machinery. The pinned identity (signs MEASURED against the evaluator, not
remembered — anti-self-deception design):

    log Φ_b(z) = i·( −J(z,b)/2 + π z²/2 + π (b² + b⁻²)/24 ),

    J(z,b) = ∫_0^∞ [ sin(2zt) / (t·sinh(bt)·sinh(t/b)) − 2z/t² ] dt.

Derivation sketch (verified numerically below, gate P1): split the Faddeev
contour ℝ+iδ at the triple pole w = 0 into the principal-value of the odd part
(the −i·sin piece → −J/2 after regularizing the 1/w² subtraction) plus the
half-residue at 0 (Laurent a₋₁ = −z²/2 − (b²+b⁻²)/24, giving the +iπz²/2 and
+iπ(b²+b⁻²)/24 terms). J is REAL for real (z,b): the representation makes the
pure-phase property |Φ_b| = 1 (prop:phi-b-unitary-bar-odd) definitional.

NUMERICAL HARDENING (why the naive quadrature mis-pins): tanh-sinh nodes reach
t ~ 1e-100 where both sin(2zt)−2zt and 1/(sinh·sinh)−1/t² suffer catastrophic
cancellation (relative eps on 1/t² ⇒ absolute garbage ~1e+150). Both integrand
factors therefore switch to explicit series branches for small t. A first
un-hardened run showed exactly this: maxdegree-10 quadrature gave a spurious
z-linear residual ~1e-5 at b ≠ 1 that VANISHED at maxdegree 6 (whose nodes
stay in the safe zone) — the residual was quadrature noise, not a missing
term.

PIN BATTERY (pre-stated gates; run as __main__):
  P1  identity          : |Im log Φ_b(z) − model(z,b)| ≤ 1e-25 on the (z,b) grid
  P2  pure phase        : |Re log Φ_b(z)| ≤ 1e-25 on the grid (fibre saddle)
  P3  self-duality of J : |J(z,b) − J(z,1/b)| ≤ 1e-30 (integrand symmetric)
  P4  z-parity of J     : |J(−z,b) + J(z,b)| ≤ 1e-30 (integrand odd in z)

P3/P4 are the numerical twins of the sorry-free Lean theorems
(PhiB_selfDual / phaseIntegral parity) in FaddeevPhiBRealIntegral.lean.

C14 anti-fitting: nothing here is compared to c_k, S, Φ₁, the residue A, or
any physical constant; the (z,b) grid is a generic mathematical test grid.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from phi_b_evaluator import log_phi_b  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = set_compute_dps()

# Generic mathematical test grid (NOT anchored to any physical value).
Z_GRID = ("0.05", "0.20", "0.35")
B_GRID = ("0.6", "0.8", "1.0", "1.3", "2.0")


def _sin_minus_linear(x):
    """sin(x) − x, cancellation-free for small |x| (series branch)."""
    if mp.fabs(x) >= mp.mpf(1) / 2:
        return mp.sin(x) - x
    # sin(x) − x = Σ_{k≥1} (−1)^k x^{2k+1}/(2k+1)!
    s = mp.mpf(0)
    term = -x**3 / 6
    k = 1
    while mp.fabs(term) > mp.mpf(10) ** (-mp.mp.dps - 5):
        s += term
        k += 1
        term *= -x**2 / ((2 * k) * (2 * k + 1))
    return s


def _sinhsinh_reg(b, t):
    """t² − sinh(bt)·sinh(t/b), cancellation-free for small t.

    Via product-to-sum: sinh(bt)sinh(t/b) = (cosh(rt) − cosh(dt))/2 with
    r = b + 1/b, d = b − 1/b (r² − d² = 4), so
    t² − sinh(bt)sinh(t/b) = −Σ_{k≥2} (r^{2k} − d^{2k}) t^{2k} / (2·(2k)!).
    """
    r, d = b + 1 / b, b - 1 / b
    if r * t >= mp.mpf(1) / 2:
        return t**2 - mp.sinh(b * t) * mp.sinh(t / b)
    s = mp.mpf(0)
    rk, dk = (r * t) ** 2, (d * t) ** 2
    # k-th term: (r^{2k} − d^{2k}) t^{2k} / (2·(2k)!)
    fact = mp.mpf(2)  # (2k)! running, starts at 2! for k=1
    rpow, dpow = rk, dk
    k = 1
    while True:
        k += 1
        rpow *= rk
        dpow *= dk
        fact *= (2 * k - 1) * (2 * k)
        term = (rpow - dpow) / (2 * fact)
        s -= term
        if mp.fabs(term) < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
    return s


def J(z, b):
    """J(z,b) = ∫_0^∞ [ sin(2zt)/(t·sinh(bt)·sinh(t/b)) − 2z/t² ] dt (real).

    Split (both pieces separately regular at 0, hardened by series branches):
      J = ∫ [sin(2zt) − 2zt]/(t·sinh(bt)·sinh(t/b)) dt
        + 2z·∫ [1/(sinh(bt)·sinh(t/b)) − 1/t²] dt.
    """
    z, b = mp.mpmathify(z), mp.mpmathify(b)
    rate = b + 1 / b
    T = (mp.mp.dps * mp.log(10) + 25) / rate

    def f1(t):
        if t == 0:
            return mp.mpf(0)
        return _sin_minus_linear(2 * z * t) / (t * mp.sinh(b * t) * mp.sinh(t / b))

    def f2(t):
        if t == 0:
            return -(b**2 + 1 / b**2) / mp.mpf(6)
        ss = mp.sinh(b * t) * mp.sinh(t / b)
        # 1/ss − 1/t² = (t² − ss)/(t²·ss)
        return _sinhsinh_reg(b, t) / (t**2 * ss)

    I1 = mp.quad(f1, [0, 1, 3, T])
    I2 = mp.quad(f2, [0, 1, 3, T]) - 1 / T  # exact tail of −1/t² beyond T
    return I1 + 2 * z * I2


def model(z, b):
    """Im log Φ_b(z) per the pinned real form."""
    return -J(z, b) / 2 + mp.pi * z**2 / 2 + mp.pi * (b**2 + 1 / b**2) / 24


def main() -> int:
    print("=" * 78)
    print(" Φ_b real-integral form pin — fibre saddle (real b, real z)")
    print("=" * 78)
    wb = WitnessBuilder("qbeta-phi-b-real-form-pin", engine="mpmath")
    wb.set_description(
        "Pins the real-integral representation log Φ_b(z) = i(−J/2 + πz²/2 + "
        "π(b²+b⁻²)/24), J = ∫_0^∞ [sin(2zt)/(t·sinh(bt)·sinh(t/b)) − 2z/t²]dt, "
        "against the validated contour evaluator (phi_b_evaluator.py) on a "
        "generic (z,b) grid. Backs the Lean construction "
        "QOU.MathlibExt.FaddeevPhiBRealIntegral (PhiB): P3/P4 are the numeric "
        "twins of the sorry-free self-duality and z-parity theorems. "
        "Infrastructure only — no c_k, no S comparison, no fits (C14)."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    p1 = p2 = p3 = p4 = mp.mpf(0)
    rows = []
    for bs in B_GRID:
        b = mp.mpf(bs)
        for zs in Z_GRID:
            z = mp.mpf(zs)
            L = log_phi_b(z, b)
            m = model(z, b)
            e1 = mp.fabs(mp.im(L) - m)
            e2 = mp.fabs(mp.re(L))
            p1, p2 = max(p1, e1), max(p2, e2)
            rows.append({"z": zs, "b": bs,
                         "im_log_phi": mp.nstr(mp.im(L), 30),
                         "model": mp.nstr(m, 30),
                         "abs_diff": mp.nstr(e1, 3)})
            print(f"  z={zs:5s} b={bs:4s}:  |Im logΦ − model| = {mp.nstr(e1, 3)}"
                  f"   |Re logΦ| = {mp.nstr(e2, 3)}")
    # P3/P4 on a sub-grid (J-only, no contour evaluation needed)
    for bs in ("0.6", "1.3"):
        b = mp.mpf(bs)
        z = mp.mpf("0.20")
        p3 = max(p3, mp.fabs(J(z, b) - J(z, 1 / b)))
        p4 = max(p4, mp.fabs(J(-z, b) + J(z, b)))
    print(f"\n  P1 identity max      : {mp.nstr(p1, 3)}")
    print(f"  P2 pure-phase max    : {mp.nstr(p2, 3)}")
    print(f"  P3 self-duality max  : {mp.nstr(p3, 3)}")
    print(f"  P4 z-parity max      : {mp.nstr(p4, 3)}")

    wb.add_data("grid", rows)
    wb.add_data("evaluator", "computations/qbeta/phi_b_evaluator.py (battery-gated)")
    wb.add_data("lean_construction",
                "QOU.MathlibExt.FaddeevPhiBRealIntegral (PhiB; sorry-free "
                "self-duality/unitarity/inversion/zero-argument theorems)")
    wb.add_assertion("P1_real_form_identity", computed=float(p1), expected=0.0,
                     tolerance=1e-25,
                     source="Im log Φ_b = −J/2 + πz²/2 + π(b²+b⁻²)/24 on grid")
    wb.add_assertion("P2_pure_phase", computed=float(p2), expected=0.0,
                     tolerance=1e-25,
                     source="Re log Φ_b = 0 at real b, real z (fibre saddle)")
    wb.add_assertion("P3_J_self_dual", computed=float(p3), expected=0.0,
                     tolerance=1e-30, source="J(z,b) = J(z,1/b)")
    wb.add_assertion("P4_J_odd_in_z", computed=float(p4), expected=0.0,
                     tolerance=1e-30, source="J(−z,b) = −J(z,b)")

    ok = p1 < mp.mpf("1e-25") and p2 < mp.mpf("1e-25") \
        and p3 < mp.mpf("1e-30") and p4 < mp.mpf("1e-30")
    print(f"\n  PIN BATTERY: {'ALL OK' if ok else 'FAILURES PRESENT'}")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
