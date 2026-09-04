#!/usr/bin/env python3
"""Gate 2 (bean de0o): toroidal-harmonic (toroidal-Legendre) expansion of the
two-strand Reeb tube-linking kernel — does the pn deformation term
(q0-1)^2/q0 fall out?

VERDICT: PARTIAL (scope-(a); see docs/audits/2026-07-06-toroidal-legendre-gates.md
SS Gate 2 for the derivation and the honest assumption ledger).

Construction (reconstruction — the #3407 attack doc's Routes A/B/C have no
concrete integral artifact, per the #3436 provenance audit): the two strands
of the pn bond are modeled as coaxial circular Reeb orbits (radii r1, r2,
axial separation d) on the color-tube solid tori. The Coulomb/Biot-Savart
kernel between the two rings has the classical toroidal-Legendre azimuthal
decomposition (Heine identity)

    1/|x - x'| = (1/(pi*sqrt(r1*r2))) * sum_m eps_m cos(m psi) Q_{m-1/2}(chi),
    chi = (r1^2 + r2^2 + d^2) / (2 r1 r2),   psi = azimuthal offset,

with eps_0 = 1, eps_m = 2 (m >= 1). Identifications tested (A1 derand;
A2/A3 assumed — see the audit section):

  (A1) radial ratio r1/r2 = q0  <=>  coplanar toroidal separation ln q0
       (geometric-mean gauge r1 r2 = 1: r1 = v = sqrt(q0), r2 = 1/v);
  (A2) axial separation d^2 = r1 r2 (= 1 in gauge);
  (A3) the linking magnitude is the scale-invariant kernel amplitude at the
       exchange (antipodal, psi = pi) configuration:
       g = sqrt(r1 r2) * (1/|x-x'|)|_{psi=pi} = sqrt(r1 r2)/d_max.

Verified identities (all mpmath, 50 dps working + 10 guard, tol 1e-45):

  T1  Delta := (q0-1)^2/q0 = (v - 1/v)^2 = 2(cosh eta0 - 1),  eta0 = ln q0
      (the deformation term is even in eta0 — bar-parity automatic).
  T2  chi = cosh(eta0) + 1/2 under (A1)+(A2) — the toroidal-Legendre
      argument carries the q0 dependence ONLY through cosh(ln q0),
      i.e. only through Delta (SHAPE result, from A1 alone).
  T3  g_landed = 1/sqrt(5 + Delta) = sqrt(r1 r2)/d_max,
      d_max^2 = (r1+r2)^2 + d^2 = 1 + [2]_v^2  (I1 of the #3436 audit).
  T4  Toroidal tower: g = (1/pi) * sum_m eps_m (-1)^m Q_{m-1/2}(chi)
      (Heine at psi = pi) — the landed magnitude IS a toroidal-Legendre
      alternating tower at argument cosh(ln q0) + 1/2.
  T5  Elliptic modulus of the two-ring kernel: k = 2*g exactly, via the
      classical closed form Q_{1/2}(chi) = (2/k - k) K(k) - (2/k) E(k).
  T6  NEGATIVE: the m=1 mode alone (the Neumann / mutual-helicity
      functional proper, i.e. what the helicity integral of two closed
      filaments actually contains) is Q_{1/2}(chi)/pi != g. Coaxial
      parallel circles have Gauss lk = 0; g is NOT the m=1 helicity mode.
  T7  Order: Delta = eta0^2 + O(eta0^4) — leading correction is second
      order in (q0 - 1); headroom 1 - sqrt(5) g = Delta/10 + O(Delta^2).
  T8  Classical limit q -> 1: chi = 3/2, g = 1/sqrt(5) (the ceiling),
      5 = (r1+r2)^2 + d^2 = 2^2 + 1^2 at q = 1.

No fits, no new constants; q0 sourced from the canonical 50-dps string.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "computations" / "substrate"))

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 60  # 50 working + 10 guard

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
# Measured before this fix: TOL was mpf('9.9999999999999998e-46'), not 1e-45
# -- 1.59e-17 relative, ~16 digits kept. Nothing DEPENDED on the missing
# digits (TOL only gates `abs(...) < TOL` assertions, which cannot change at
# that resolution), but the binding was genuinely at dps=15 and the ratchet is
# right to flag it. Unlike this file, `main()` raising dps is too late.
mp.mp.dps = DPS

TOL = mp.mpf("1e-45")
HEINE_TERMS = 300  # ratio e^{-arccosh(chi)} ~ 0.38 => far below 1e-45


def qre(x):
    """Real part of a possibly-mpc legenq result (type=3 on (1,inf) is real)."""
    return x.real if isinstance(x, mp.mpc) else x


def main():
    mp.mp.dps = DPS
    q0 = mp.mpf(Q_50_DIGIT_STR)
    v = mp.sqrt(q0)
    eta0 = mp.log(q0)

    # --- T1: shape identities for the deformation term -------------------
    Delta = (q0 - 1) ** 2 / q0
    assert abs(Delta - (v - 1 / v) ** 2) < TOL, "T1a"
    assert abs(Delta - 2 * (mp.cosh(eta0) - 1)) < TOL, "T1b"

    # --- configuration (A1)+(A2): (r1, r2, d) = (v, 1/v, 1) --------------
    r1, r2, d = v, 1 / v, mp.mpf(1)
    chi = (r1**2 + r2**2 + d**2) / (2 * r1 * r2)
    assert abs(chi - (mp.cosh(eta0) + mp.mpf(1) / 2)) < TOL, "T2"

    # --- T3: the landed magnitude as antipodal chord amplitude -----------
    g_landed = 1 / mp.sqrt(5 + Delta)
    d_max = mp.sqrt((r1 + r2) ** 2 + d**2)
    two_v = v + 1 / v  # [2]_v
    assert abs(g_landed - mp.sqrt(r1 * r2) / d_max) < TOL, "T3a"
    assert abs(d_max**2 - (1 + two_v**2)) < TOL, "T3b (I1)"

    # --- T4: toroidal-Legendre alternating tower sums to g ----------------
    S = qre(mp.legenq(mp.mpf("-0.5"), 0, chi, type=3))
    for m in range(1, HEINE_TERMS):
        S += 2 * (-1) ** m * qre(mp.legenq(m - mp.mpf("0.5"), 0, chi, type=3))
    g_tower = S / mp.pi
    assert abs(g_tower - g_landed) < TOL, "T4"

    # --- T5: elliptic modulus k = 2g via the classical Q_{1/2} form ------
    k = 2 * g_landed
    Q_half = qre(mp.legenq(mp.mpf("0.5"), 0, chi, type=3))
    rhs = (2 / k - k) * mp.ellipk(k**2) - (2 / k) * mp.ellipe(k**2)
    assert abs(Q_half - rhs) < TOL, "T5"

    # --- T6: NEGATIVE — the m=1 (mutual-helicity/Neumann) mode is not g --
    neumann_mode = Q_half / mp.pi
    assert abs(neumann_mode - g_landed) > mp.mpf("0.3"), "T6 (must differ)"

    # --- T7: order of the correction --------------------------------------
    assert abs(Delta - eta0**2) < eta0**4, "T7a (Delta = eta0^2 + O(eta0^4))"
    headroom = 1 - mp.sqrt(5) * g_landed
    assert abs(headroom - Delta / 10) < (Delta / 10) ** 2 * 20, "T7b"

    # --- T8: classical limit ----------------------------------------------
    chi_cl = mp.mpf(3) / 2
    g_cl = 1 / mp.sqrt(5)
    S_cl = qre(mp.legenq(mp.mpf("-0.5"), 0, chi_cl, type=3))
    for m in range(1, HEINE_TERMS):
        S_cl += 2 * (-1) ** m * qre(mp.legenq(m - mp.mpf("0.5"), 0, chi_cl, type=3))
    assert abs(S_cl / mp.pi - g_cl) < TOL, "T8"

    n = lambda x, p=50: mp.nstr(x, p)  # noqa: E731
    print(f"q0                = {n(q0)}")
    print(f"Delta             = {n(Delta)}")
    print(f"chi = cosh(ln q0)+1/2 = {n(chi)}")
    print(f"g = 1/sqrt(5+Delta)   = {n(g_landed)}")
    print(f"toroidal tower sum    = {n(g_tower)}  (T4: {n(abs(g_tower-g_landed), 3)})")
    print(f"k = 2g (elliptic mod) = {n(k)}")
    print(f"m=1 Neumann mode      = {n(neumann_mode)}  (T6: != g)")
    print(f"headroom 1-sqrt5*g    = {n(headroom)} vs Delta/10 = {n(Delta/10)}")
    print("All 12 assertions passed (T1-T8).")

    witness = {
        "computation": "probe_toroidal_reeb_deformation",
        "description": (
            "Gate 2 (bean de0o): toroidal-Legendre (Heine) expansion of the "
            "two-strand coaxial-ring Reeb kernel. VERDICT: PARTIAL, scope-(a). "
            "Shape+order of the deformation term (q0-1)^2/q0 derived from the "
            "radial identification r1/r2 = q0 alone (q-dependence enters only "
            "through chi = cosh(ln q0) + d^2/2); exact coefficient/placement "
            "1/sqrt(5+Delta) requires the assumed d^2 = r1*r2 and the "
            "exchange-point (psi=pi) amplitude reading, jointly equivalent to "
            "the #3436 residual CWF postulate. NEGATIVE: the m=1 mutual-"
            "helicity mode Q_{1/2}(chi)/pi does not produce g."
        ),
        "scriptFile": "computations/probe_toroidal_reeb_deformation.py",
        "verdict": "PARTIAL",
        "scope": "a",
        "inputs": {"q0_50dps": Q_50_DIGIT_STR, "config": "(r1,r2,d)=(sqrt(q0),1/sqrt(q0),1)"},
        "data": {
            "Delta": n(Delta),
            "chi": n(chi),
            "g_landed": n(g_landed),
            "g_toroidal_tower": n(g_tower),
            "elliptic_modulus_k": n(k),
            "neumann_m1_mode": n(neumann_mode),
            "headroom_1_minus_sqrt5_g": n(headroom),
            "Delta_over_10": n(Delta / 10),
            "heine_terms": HEINE_TERMS,
            "tolerance": "1e-45",
        },
        "assertions": {
            "T1_shape": True, "T2_chi": True, "T3_antipodal": True,
            "T4_toroidal_tower": True, "T5_elliptic_k_eq_2g": True,
            "T6_neumann_mode_not_g": True, "T7_order": True,
            "T8_classical_ceiling": True,
        },
        "assumed_not_derived": [
            "A1: strand radial ratio r1/r2 = q0 (bar-conjugate pair v, 1/v)",
            "A2: axial separation d^2 = r1*r2 (maps to the derived pp-nn "
            "asymmetry 1 via the #3436 I2 dictionary, but is un-derived "
            "within the toroidal picture)",
            "A3: magnitude = exchange-point (antipodal) kernel amplitude "
            "(equivalent to the #3436 CWF unit-tangent postulate: chord "
            "direction (r1+r2, d) = ([2]_v, 1) has tan = z, sin = g)",
        ],
    }
    WitnessBuilder.wrap_legacy(
        "probe_toroidal_reeb_deformation", witness, script_path=__file__
    ).save()


if __name__ == "__main__":
    main()
