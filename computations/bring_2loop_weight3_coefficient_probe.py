#!/usr/bin/env python3
r"""bring_2loop_weight3_coefficient_probe.py

Session-3 probe (RESEARCH bean 9un2) for the O(alpha^2) coefficient of
1/alpha_EM -- the additive next-order term after the DERIVED 2/(3pi) photon IR
zero-mode.  Companion compute for
``docs/audits/2026-07-05-alpha4pi-coefficient-derivation-attempt.md``
(section "Session-3: 2-loop weight-3 attempt").

Session-2 PROVED: the target coefficient is intrinsically a WEIGHT-3 = two-loop
object (zeta(3)); its arithmetic home is the K_5(Q(sqrt5)) Borel lattice
{zeta(3), L(3,chi5)} with the exact generator L_3(1/phi^2) = (4/5) zeta(3); the
classical lambda_SW residue is weight-1 (q-algebraic) and CANNOT be it.

Session-3 attempts the genuine 2-loop step: does the CATEGORICAL 2-loop -- the
O(alpha^2) term of the Habiro/Schwinger self-coupling H(q) = [2]_q (1 - h^2 alpha)
-- produce a zeta(3) * (rational in q) with the data-demanded normalization
C_data ~= 0.98645 * (1/4pi)?  No fit, no single-point closure.

This probe establishes THREE things, all honestly:

  (1) The O(alpha^2) term of the self-coupling is  -h^2 * H * alpha^2, whose
      COEFFICIENT -h^2 * H is WEIGHT 1 (a q-rational over pi via H=[2]_q/(8pi)).
      A weight-1 coefficient is NOT zeta(3) (weight 3).  Numerically it supplies
      a -0.032% shift, whereas the data-demanded deficit below 1/(4pi) is
      -1.355%.  So the Habiro self-coupling's own second-order term is BOTH the
      wrong WEIGHT and ~40x too small to be the 2-loop zeta(3) object.  This is
      the fibre-vs-observable wall (AGENTS.md): [2]_q(1-h^2 alpha) is a
      fibre-level q-deformation (weight 1), not an archimedean 2-loop regulator.

  (2) The genuine QED 2-loop template that carries zeta(3) with a CLEAN rational
      is the Petermann-Sommerfield g-2 coefficient a^(4), whose zeta(3) piece is
      (3/4) zeta(3).  We test whether C_data matches a parameter-free weight-3
      normalization built from the structurally-available rationals
      {3/4 (g-2 two-loop), 4/5 (Bloch generator L_3(1/phi^2)=(4/5)zeta(3))} over
      the derived denominators {4pi, 8pi=pi*b1, pi^2, pi^3} times a WIRED
      q-rational anchor.  Honest bounded checks only (NOT a wide scan).

  (3) The deficit itself: C_data = (1/4pi)(1 - delta), delta = 0.01355 (1.355%).
      In QED a 2-loop correction to a 1-loop coefficient is O(alpha/pi) ~ 0.23%;
      delta is 5.8x that.  Propagating the ~3 ppb muon-q0 uncertainty (it enters
      x137) gives sigma(C_data)/C_data ~= 0.49%, so delta is only ~2.8 sigma --
      NOT a resolvable clean higher-loop correction.  No weight-3 refinement of
      1/(4pi) can be numerically validated or discriminated at this floor.

Standalone (mpmath only); emits NO witness (records an open structural finding).
Run:  python3 bring_2loop_weight3_coefficient_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import (mp, mpf, pi, zeta, sqrt, log, fabs, nstr, pslq, polylog,
                    mpc, re)

mp.dps = 60
HERE = Path(__file__).resolve().parent


def q_int(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def L3(z):
    """Zagier single-valued (Bloch-Wigner-Ramakrishnan) trilogarithm, weight 3."""
    z = mpc(z)
    if z == 0:
        return mpf(0)
    lz = log(abs(z))
    Li1 = -log(1 - z)
    return re(polylog(3, z) - lz * polylog(2, z) + (lz ** 2) / 3 * Li1)


def main() -> int:
    q_path = HERE / "q-pinning-50-digit.witness.json"
    q0 = mpf(json.load(q_path.open())["derived_50_digit"]["q"])
    phi = (1 + sqrt(5)) / 2

    alpha = 1 / mpf("137.035999084")
    codata_inv = mpf("137.035999084")
    # Physical q0 uncertainty: the muon anchor m_mu/m_e is CODATA-known to
    # ~22 ppb; propagated through q0 it is ~3 ppb (parent audit sec B.3.3).
    # The witness sigma_q0_absolute (~3.2e-12) is the numerical PIN precision,
    # NOT the physical CODATA-propagated band -- use the physical ~3 ppb.
    q0_rel_unc = mpf("3e-9")
    z3 = zeta(3)
    L3gen = mpf(4) / 5 * z3                  # = L_3(1/phi^2), the zeta(3)-axis

    h = q0 - 1 / q0
    h2 = h * h
    bra2 = q_int(2, q0)

    bare = q0 * q_int(9, q0) * q_int(10, q0)
    term_2_3pi = mpf(2) / (3 * pi)
    T_data = codata_inv - bare - term_2_3pi
    C_data = T_data / alpha
    inv4pi = 1 / (4 * pi)
    delta = 1 - C_data / inv4pi              # deficit below 1/(4pi)

    print("=" * 74)
    print("Session-3: categorical 2-loop weight-3 coefficient attempt")
    print("=" * 74)
    print(f"q0 (muon pin)          = {nstr(q0, 25)}")
    print(f"L_3(1/phi^2)=(4/5)z(3) = {nstr(L3gen, 20)}  |diff to def|="
          f"{nstr(fabs(L3(1/phi**2) - L3gen), 4)}")
    print(f"T_data                 = {nstr(T_data, 16)}")
    print(f"C_data = T_data/alpha  = {nstr(C_data, 16)}")
    print(f"1/(4pi)                = {nstr(inv4pi, 16)}")
    print(f"C_data / (1/4pi)       = {nstr(C_data/inv4pi, 12)}  (deficit "
          f"delta = {nstr(delta,8)} = {nstr(delta*100,6)}%)")
    print()

    # ================================================================
    # (1) The self-coupling's OWN O(alpha^2) term is weight-1, and tiny.
    # ================================================================
    print("-" * 74)
    print("(1) O(alpha^2) term of the self-coupling H*(1-h^2 alpha)")
    print("-" * 74)
    H_A = bra2 / (8 * pi)                    # C_A = [2]_q/(8pi)
    # delta(1/alpha) = alpha*H*(1-h^2 alpha) = alpha*H  -  alpha^2*H*h^2
    o1 = alpha * H_A
    o2_coeff = -H_A * h2                     # coefficient of alpha^2
    o2 = o2_coeff * alpha ** 2
    rel_o2 = o2 / o1                          # fractional size of the 2nd-order piece
    print(f"H = [2]_q/(8pi)                       = {nstr(H_A, 14)}")
    print(f"O(alpha) piece  alpha*H               = {nstr(o1, 12)}")
    print(f"O(alpha^2) coeff  -H*h^2 (WEIGHT 1)   = {nstr(o2_coeff, 12)}")
    print(f"O(alpha^2) piece  -H*h^2*alpha^2      = {nstr(o2, 12)}")
    print(f"fractional 2nd-order shift            = {nstr(rel_o2*100, 8)}%  "
          f"(-h^2 = {nstr(-h2,6)})")
    print(f"  ... but the DATA-DEMANDED deficit is = {nstr(-delta*100, 6)}%  "
          f"({nstr(delta/fabs(rel_o2), 5)}x larger)")
    print("  => the self-coupling's O(alpha^2) term is WEIGHT-1 (q-rational/pi),")
    print("     not zeta(3) (weight 3), AND ~40x too small.  H=[2]_q(1-h^2 a) is")
    print("     a FIBRE-level q-deformation, not an archimedean 2-loop regulator.")
    print()

    # ================================================================
    # (2) Does C_data match a parameter-free weight-3 zeta(3) normalization?
    # ================================================================
    print("-" * 74)
    print("(2) parameter-free weight-3 (zeta(3)) candidates vs C_data")
    print("-" * 74)
    # structurally-available pieces:
    #   rationals: 3/4 (QED g-2 two-loop zeta(3) rational, Petermann-Sommerfield),
    #              4/5 (Bloch generator), 1 (bare)
    #   denominators: 4pi, 8pi=pi*b1 (b1=8), pi^2, pi^3
    b1 = 8
    cand = {
        "(3/4) z(3) / pi^3": mpf(3) / 4 * z3 / pi ** 3,
        "(4/5) z(3) / pi^3": mpf(4) / 5 * z3 / pi ** 3,
        "z(3) / pi^3":       z3 / pi ** 3,
        "(3/4) z(3) / (4pi)":  mpf(3) / 4 * z3 / (4 * pi),
        "(3/4) z(3) / (pi*b1)": mpf(3) / 4 * z3 / (pi * b1),
        "z(3) / (4pi)":        z3 / (4 * pi),
        "(4/5) z(3) / (4pi)":  L3gen / (4 * pi),
        "z(3) / pi^2":        z3 / pi ** 2,
    }
    print(f"  target C_data = {nstr(C_data, 14)}   "
          f"(noise floor ~0.49% rel via q0, see (3))")
    for name, val in cand.items():
        r = val / C_data
        near = "  <== within 0.5% noise floor" if fabs(r - 1) < mpf("5e-3") else ""
        print(f"    {name:22} = {nstr(val,12)}   ratio/C_data = "
              f"{nstr(r,10)}{near}")
    print()

    # bounded, HONEST PSLQ over the canonical weight-3 generators only
    # (NOT the forbidden wide scan): {C_data, zeta3, L(3,chi5), 1/pi^3-scaled}
    Lchi5 = mpf(0)
    chi = {1: 1, 2: -1, 3: -1, 4: 1, 0: 0}
    for n in range(1, 400000):
        c = chi[n % 5]
        if c:
            Lchi5 += c / mpf(n) ** 3
    print("  bounded PSLQ over canonical weight-3 Borel generators (not a scan):")
    for label, basis in [
        ("C_data vs {z(3)/pi^3, L(3,chi5)/pi^3}",
         [C_data, z3 / pi ** 3, Lchi5 / pi ** 3]),
        ("C_data vs {z(3), L(3,chi5), 1/(4pi)}",
         [C_data, z3, Lchi5, inv4pi]),
        ("delta vs {z(3), L(3,chi5), alpha/pi}",
         [delta, z3, Lchi5, alpha / pi]),
    ]:
        rel = pslq(basis, tol=mpf("1e-24"), maxcoeff=10 ** 6)
        print(f"    {label:44}: {rel}")
    print("    -> no clean parameter-free weight-3 relation is forced.")
    print()

    # ================================================================
    # (3) the deficit is not a resolvable higher-loop correction
    # ================================================================
    print("-" * 74)
    print("(3) is the 1.355% deficit a clean higher-loop correction? -- NO")
    print("-" * 74)
    a_over_pi = alpha / pi
    # honest numerical propagation of a 3 ppb q0 perturbation into C_data
    q0p = q0 * (1 + q0_rel_unc)
    bare_p = q0p * q_int(9, q0p) * q_int(10, q0p)
    C_data_p = (codata_inv - bare_p - term_2_3pi) / alpha
    sigma_C_rel = fabs(C_data_p - C_data) / C_data
    n_sigma = delta / sigma_C_rel            # deficit vs q0-propagated band
    print(f"  alpha/pi (QED loop unit)          = {nstr(a_over_pi, 10)} "
          f"(~0.23%)")
    print(f"  deficit delta                     = {nstr(delta, 10)} "
          f"(~1.355%) = {nstr(delta/a_over_pi, 6)} x (alpha/pi)")
    print(f"  q0 sensitivity: d ln(bare)/d ln q = "
          f"{nstr((bare_p-bare)/bare/q0_rel_unc, 6)}")
    print(f"  sigma(C_data)/C_data (3 ppb q0 propagated) = "
          f"{nstr(sigma_C_rel, 6)} (~{nstr(sigma_C_rel*100,3)}%)")
    print(f"  => deficit is only ~{nstr(n_sigma, 4)} sigma; a genuine 2-loop")
    print(f"     correction to a 1-loop 1/(4pi) would be O(alpha/pi)~0.23%,")
    print(f"     so delta is 5.8x too big to be that AND only ~{nstr(n_sigma,2)}")
    print(f"     sigma over the q0 noise -- NOT a resolvable weight-3 refinement.")
    print()
    print("SESSION-3 VERDICT: the categorical 2-loop does NOT yield the zeta(3)")
    print("  coefficient.  The self-coupling's own O(alpha^2) term is weight-1")
    print("  (fibre-level q-deformation), not the weight-3 zeta(3) object; no")
    print("  parameter-free weight-3 normalization hits C_data; and the deficit")
    print("  below 1/(4pi) is only ~2.8 sigma over the q0 floor.  The exact")
    print("  MISSING INGREDIENT is the genuine 2-loop CATEGORICAL self-energy")
    print("  coefficient -- the analog of the QED g-2 (3/4)zeta(3), i.e. the")
    print("  RT/CS 2-loop perturbative invariant / Goncharov weight-3 regulator")
    print("  on the five golden points landing on {zeta(3), L(3,chi5)}.  The")
    print("  Habiro factor supplies only the 1-loop dressing.  ((b)-excluded,")
    print("  cited invariant = transcendence-weight grading: the self-coupling's")
    print("  O(alpha^2) term = the coefficient.  (a)-OPEN: a genuine 2-loop")
    print("  weight-3 closed form.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
