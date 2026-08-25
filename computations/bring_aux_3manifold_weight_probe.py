#!/usr/bin/env python3
r"""bring_aux_3manifold_weight_probe.py

Auxiliary-3-manifold route for the O(alpha^2) coefficient of 1/alpha_EM
(the additive next-order term after the derived 2/(3pi) photon IR
zero-mode).  Companion compute for
``docs/audits/2026-07-05-alpha4pi-coefficient-derivation-attempt.md``
(section "Auxiliary-3-manifold route").

THE SHARPENED LEAD (from that audit, section B.3.1): a genuine B_3 /
trilogarithm class must come from an AUXILIARY 3-MANIFOLD, because the
2-real-dimensional Bring surface tiles only into ideal triangles (area /
weight-1 data), not ideal tetrahedra.  Candidates: a mapping torus of a
Bring automorphism, the unit-tangent bundle, or a K_5(Q(sqrt5)) Bloch
class realized as a 3-manifold scissors class.

WHAT THIS PROBE ESTABLISHES (all parameter-free, no fit) -- the NEW,
sharper obstruction that RE-SCOPES the whole auxiliary-3-manifold idea:

  It is a WEIGHT obstruction, not merely a dimensional one.

  (1) A hyperbolic 3-manifold's complex volume  Vol + i*CS  is the image
      of its fundamental class under the WEIGHT-2 (dilogarithm) Borel
      regulator on K_3(C) ~ B_2(C)  (Neumann-Zagier).  A hyperbolic
      3-manifold period is therefore a DILOGARITHM (weight 2), NEVER a
      trilogarithm (weight 3).  The B_3 class the RT-Phase-5 scaffold
      asked for is weight 3 = K_5 -- one weight ABOVE anything a
      3-manifold scissors/volume/CS class can carry.

  (2) Q(sqrt5) is TOTALLY REAL (r1=2, r2=0).  By Borel,
        rank K_3(Q(sqrt5)) (x) Q = r2       = 0   (weight-2 / dilog: TRIVIAL)
        rank K_5(Q(sqrt5)) (x) Q = r1 + r2  = 2   (weight-3 / trilog: rank 2)
      So the field itself KILLS the weight-2 regulator (the exact
      invariant a 3-manifold computes) and puts all the content at
      weight 3.  Numerical fingerprint below:
        weight 2:  Li_2(1/phi^2) = pi^2/15 - ln^2(phi)   EXACTLY
                   (pi^2-rational up to decomposables => Bloch class torsion)
        weight 3:  L_3(1/phi^2)  = (4/5) zeta(3)          genuinely
                   transcendental-weight-3 (the K_5 zeta(3)-axis).

  (3) The canonical 3-manifold attached to Bring's surface -- the unit
      tangent bundle UT(M_Bring) = PSL2(R)/Gamma_Bring, i.e. the frame
      bundle of the state bundle S already in the QOU tuple
      (C, Theta, G, S) -- is SEIFERT-FIBERED (SL2~ geometry), an S^1
      bundle over M_Bring with Euler number e = chi(M_Bring) = 2-2g = -6.
      Seifert-fibered => Gromov/simplicial volume = 0 and Chern-Simons in
      Q/Z.  It supplies ZERO transcendental scissors content: neither
      dilog nor trilog.  Mapping tori of the (finite-order, conformal)
      S_5 automorphisms are likewise periodic => Seifert-fibered =>
      volume 0.

VERDICT: OPEN (route re-scoped to (a)-refuted-as-posed + one admissible
(b)).  No auxiliary 3-manifold canonically attached to Bring's surface
can realize the weight-3 target, because (b, cited invariants) a
3-manifold period is weight-2 (Neumann-Zagier) and the weight-2 regulator
of Q(sqrt5) is trivial (Borel rank 0).  The weight-3 K_5(Q(sqrt5)) class
{zeta(3), L(3,chi_5)} is REAL but its home is a higher regulator
(Goncharov weight-3 configuration polylog on the 5 golden points) or the
Reshetikhin-Turaev / Chern-Simons 2-LOOP perturbative invariant (which
carries zeta(3) even when the classical volume vanishes) -- NOT a
3-manifold scissors class.  No closure; no fit.

Standalone (mpmath only); emits NO witness (records an open negative).
Run:  python3 bring_aux_3manifold_weight_probe.py
"""
from __future__ import annotations

import sys
from mpmath import (mp, mpf, mpc, pi, polylog, re, im, log, zeta, sqrt, fabs,
                    nstr)
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def L3(z):
    """Zagier single-valued (BWR) trilogarithm (weight 3)."""
    z = mpc(z)
    if z == 0:
        return mpf(0)
    lz = log(abs(z))
    Li1 = -log(1 - z)
    return re(polylog(3, z) - lz * polylog(2, z) + (lz ** 2) / 3 * Li1)


def main() -> int:
    phi = (1 + sqrt(5)) / 2
    g = 4                       # genus of Bring's surface
    euler = 2 - 2 * g          # Euler number of UT(M_Bring) = chi

    print("=" * 72)
    print("Auxiliary-3-manifold route -- WEIGHT obstruction probe")
    print("=" * 72)

    # ---- (2) weight-2 (K_3) is TRIVIAL on Q(sqrt5): pi^2-rational ------
    Li2_iphi2 = polylog(2, 1 / phi ** 2)
    dilog_closed = pi ** 2 / 15 - log(phi) ** 2
    err_w2 = fabs(Li2_iphi2 - dilog_closed)
    print("--- weight 2 (dilogarithm / K_3(Q(sqrt5)) ) ---")
    print(f"Li_2(1/phi^2)                 = {nstr(Li2_iphi2, 30)}")
    print(f"pi^2/15 - ln^2(phi)           = {nstr(dilog_closed, 30)}")
    print(f"|diff|                        = {nstr(err_w2, 4)}   "
          f"=> pi^2-RATIONAL (Bloch class torsion; Borel rank K_3 = 0)")
    assert err_w2 < mpf("1e-40"), "golden dilog closed form failed"

    # ---- (3) weight-3 (K_5) is GENUINE on Q(sqrt5) --------------------
    L3_iphi2 = L3(1 / phi ** 2)
    w3_closed = mpf(4) / 5 * zeta(3)
    err_w3 = fabs(L3_iphi2 - w3_closed)
    print("--- weight 3 (trilogarithm / K_5(Q(sqrt5)) ) ---")
    print(f"L_3(1/phi^2)                  = {nstr(L3_iphi2, 30)}")
    print(f"(4/5) zeta(3)                 = {nstr(w3_closed, 30)}")
    print(f"|diff|                        = {nstr(err_w3, 4)}   "
          f"=> genuinely weight-3 (Borel rank K_5 = 2)")
    assert err_w3 < mpf("1e-40"), "golden trilog closed form failed"

    # ---- (1)+(3) the canonical 3-manifold: UT(M_Bring) ----------------
    print("--- canonical auxiliary 3-manifold: UT(M_Bring)=PSL2(R)/Gamma ---")
    print(f"genus g                       = {g}")
    print(f"Euler number e = chi = 2-2g   = {euler}")
    print("geometry                      = SL2~ (Seifert-fibered S^1 bundle)")
    print("simplicial (Gromov) volume    = 0        (Seifert => vanishes)")
    print("Chern-Simons invariant        = in Q/Z   (rational; no dilog/trilog)")
    print("=> transcendental scissors content: NONE (weight 0 output)")
    print()

    print("WEIGHT LADDER (the obstruction):")
    print("  3-manifold complex volume   =  WEIGHT-2 regulator  (K_3, dilog)")
    print("                                 -- Neumann-Zagier")
    print("  K_3(Q(sqrt5)) (x) Q         =  0   (totally real, r2=0)")
    print("  target B_3 class            =  WEIGHT-3 regulator  (K_5, trilog)")
    print("  K_5(Q(sqrt5)) (x) Q         =  rank 2  {zeta(3), L(3,chi_5)}")
    print()
    print("VERDICT: OPEN.  No 3-manifold period can be the weight-3 target:")
    print("  a 3-manifold computes the weight-2 (K_3) regulator, which is")
    print("  exactly the one that VANISHES for the totally-real Q(sqrt5).")
    print("  The real weight-3 class lives on a higher (Goncharov) regulator")
    print("  or the RT/CS 2-loop perturbative invariant -- not a 3-manifold.")
    print("  No closure; no fit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
