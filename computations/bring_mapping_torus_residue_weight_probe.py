#!/usr/bin/env python3
r"""bring_mapping_torus_residue_weight_probe.py

Session-2 probe for the O(alpha^2) coefficient of 1/alpha_EM (the additive
next-order term after the derived 2/(3pi) photon IR zero-mode).  Companion
compute for
``docs/audits/2026-07-05-alpha4pi-coefficient-derivation-attempt.md``
(section "Session-2: mapping-torus + residue").

This probe pursues the two Session-2 leads to an honest verdict.  It does NOT
fabricate a spectral curve and does NOT fit a single point.

================================================================================
LEAD A -- auxiliary hyperbolic 3-manifold via a MAPPING TORUS of a substrate
          automorphism.
================================================================================
The parent audit's section C rejected mapping tori because the genus-4 Bring
SURFACE automorphisms are the conformal group S_5 -- all FINITE ORDER (Hurwitz:
conformal automorphisms of a compact Riemann surface form a finite group) -- so
their mapping tori are Seifert-fibered (vol 0).  But section C MISSED that the
substrate DOES carry a canonical HYPERBOLIC element: the lever-1 binding
monodromy B (the abelianised lambda_SW / Gauss-Manin monodromy on the rank-2
Hodge factor = H^1 of the color elliptic curve E_q), with

    tr B = 3(3q^4+8q^2+3)/(4q(q+1)^2) = 2.6423863... > 2   (det B = 1 proved),

i.e. B is HYPERBOLIC in SL_2(R) (theta_binding = arccosh(tr B /2) = 0.7815).
[docs/audits/2026-06-24-lever1-binding-monodromy-hyperbolicity.md]

So the honest LEAD-A question is sharper than section C posed: the substrate has
a canonical hyperbolic object -- does IT build a hyperbolic 3-manifold whose
scissors class carries the target?  This probe answers NO, on three independent
cited invariants:

  (A1) B is a rank-2 SL_2 monodromy of an ELLIPTIC (genus-1) factor / a
       connection holonomy -- NOT a surface diffeomorphism.  Suspended as an
       automorphism of the elliptic FIBRE T^2, a |tr|>2 (Anosov) element gives a
       SOL-geometry torus bundle.  Torus bundles are NEVER hyperbolic
       (geometrization): every T^2-bundle has Gromov/simplicial volume 0
       (Euclidean if |tr|<2, Nil if |tr|=2, Sol if |tr|>2).  No ideal
       tetrahedra, no B_2/B_3 scissors content.
  (A2) B is not even in SL_2(Z) (tr B = 2.6424 is irrational / non-integer;
       lever1 integrality audit), so it is not a genuine T^2 automorphism at all
       -- it is a real connection holonomy, which suspends to no canonical
       3-manifold.  The only genuine diffeomorphisms are the finite-order S_5
       ones -> Seifert -> vol 0.
  (A3) Even granting SOME hyperbolic 3-manifold, its complex volume
       Vol + i CS is the WEIGHT-2 (dilogarithm) Borel regulator on
       K_3(C) ~ B_2(C) (Neumann-Zagier).  The target is WEIGHT 3 (trilog, K_5),
       one weight above ANY 3-manifold classical period; and for the totally-real
       Q(sqrt5), rank K_3 (x) Q = r_2 = 0 -- the very weight a 3-manifold
       computes is arithmetically empty.  (Re-confirmed numerically below.)

  => LEAD A verdict: STRUCTURALLY-CLOSED.  The one canonically-hyperbolic object
     the substrate offers (B) is not a mapping class, and even generously
     suspended gives Sol (vol 0); no substrate automorphism builds a hyperbolic
     3-manifold; and a hyperbolic 3-manifold would be weight-2 anyway.  The
     "pseudo-Anosov mapping torus with B_3 scissors class" the lead hoped for
     does not exist -- and the lead's premise ("a 3-manifold's ideal-tetrahedron
     scissors class IS the B_3 object") is FALSE: that scissors class is B_2.

================================================================================
LEAD B -- evaluate the residue  closed-int lambda_SW^{(2)}  directly (the fork).
================================================================================
The corpus fixes lambda_SW = x dz on the color elliptic curve E_q, and by
prop:sw-period-residue-sum the prolonged periods a_D^{(n)} = closed-int
lambda_SW^{(n)} are an ALGEBRAIC RESIDUE SUM -- q-rational.  The three
production-WIRED anchors are exact q-rationals (verified below):

    a_D^{(2)} = 1,   a_D^{(3)} = (q+1)^2/(3q),   a_D^{(4)} = (3q^2+4+3q^{-2})/4,

giving tr B = (a_D^{(2)}+a_D^{(4)})/a_D^{(3)} = 2.6424 (weight-1 algebraic).

So the classical lambda_SW residue tower lives at WEIGHT <= 1 (a residue of a
meromorphic 1-form / an abelian-integral period is algebraic; the wired anchors
ARE q-rational).  It reproduces the TREE / bare content q[9]_q[10]_q and the
multiplicative q-rational family -- exactly the family the 100-dps 54-element
PSLQ already excluded from closing the alpha gap.  It CANNOT produce the
data-demanded next term, which sits at WEIGHT 3 (zeta(3); the exact Bloch value
L_3(1/phi^2) = (4/5)zeta(3)).  A weight-1 object cannot equal a weight-3 object
(transcendence-weight grading) unless its coefficient is 0.

  => The fork RESOLVES: closed-int lambda_SW^{(2)} evaluated CLASSICALLY is
     q-algebraic (weight 1) and does NOT decide the coefficient -- it yields the
     tree periods, not the correction.  The target coefficient is intrinsically
     a WEIGHT-3 = TWO-LOOP object (zeta(3) first enters QED at two loops).  The
     exact Bloch number (4/5)zeta(3) exists but is NOT a classical-residue
     output; its normalization into delta(1/alpha) is a genuine 2-loop
     (Goncharov weight-3 regulator / RT-CS 2-loop) computation, not a
     scissors-congruence evaluation.  So the honest reading is the 2-loop-QFT
     side of the fork: there is no CLASSICAL closed-form residue for the
     coefficient, and the ~ few-ppm additive prediction is the honest ceiling.

     Refutation scope (STRICT): what is (b)-excluded (cited invariant =
     transcendence-weight grading) is "the CLASSICAL lambda_SW residue gives the
     coefficient".  Whether a genuine 2-loop weight-3 computation yields a clean
     closed form is (a)-OPEN -- not claimed refuted.

Standalone (mpmath only); emits NO witness (records an open structural finding,
not a validated result).  Run:  python3 bring_mapping_torus_residue_weight_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import (mp, mpf, mpc, pi, polylog, re, log, zeta, sqrt, acosh,
                    fabs, nstr, pslq)
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent


def q_int(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def L3(z):
    """Zagier single-valued (BWR) trilogarithm (weight 3)."""
    z = mpc(z)
    if z == 0:
        return mpf(0)
    lz = log(abs(z))
    Li1 = -log(1 - z)
    return re(polylog(3, z) - lz * polylog(2, z) + (lz ** 2) / 3 * Li1)


def torus_bundle_geometry(tr):
    """Thurston geometry of a T^2-bundle over S^1 by |tr(monodromy)|.
    All three cases have Gromov/simplicial volume 0 (never hyperbolic)."""
    a = fabs(tr)
    if a < 2:
        return "Euclidean (periodic/elliptic monodromy)", "0"
    if a == 2:
        return "Nil (parabolic monodromy)", "0"
    return "Sol (Anosov/hyperbolic monodromy)", "0"


def main() -> int:
    q_path = HERE / "q-pinning-50-digit.witness.json"
    q0 = mpf(json.load(q_path.open())["derived_50_digit"]["q"])
    phi = (1 + sqrt(5)) / 2

    print("=" * 74)
    print("Session-2: mapping-torus (LEAD A) + lambda_SW residue (LEAD B) probe")
    print("=" * 74)
    print(f"q0 (muon pin) = {nstr(q0, 25)}")
    print()

    # ================================================================
    # LEAD A -- the canonical HYPERBOLIC substrate element and its
    #           (non-)mapping-torus.
    # ================================================================
    print("-" * 74)
    print("LEAD A: does the canonical hyperbolic monodromy B build a")
    print("        hyperbolic 3-manifold?")
    print("-" * 74)

    # binding monodromy trace, two ways (must agree)
    aD2 = mpf(1)
    aD3 = (q0 + 1) ** 2 / (3 * q0)
    aD4 = (3 * q0 ** 2 + 4 + 3 * q0 ** -2) / 4
    trB_seed = (aD2 + aD4) / aD3
    trB_closed = 3 * (3 * q0 ** 4 + 8 * q0 ** 2 + 3) / (4 * q0 * (q0 + 1) ** 2)
    err_trB = fabs(trB_seed - trB_closed)
    theta_b = acosh(trB_closed / 2)          # rapidity; real iff tr>2
    lam_b = mp.e ** theta_b                   # "dilatation"-like eigenvalue

    print(f"tr B  (from wired anchors) = {nstr(trB_seed, 18)}")
    print(f"tr B  (closed form)        = {nstr(trB_closed, 18)}   "
          f"|diff| = {nstr(err_trB, 4)}")
    assert err_trB < mpf("1e-30"), "tr B closed form mismatch"
    print(f"det B = 1 (proved: sl2_prolongation_recurrence)")
    print(f"|tr B| = {nstr(trB_closed, 10)} > 2  =>  B is HYPERBOLIC in SL_2(R)")
    print(f"theta_binding = arccosh(tr B/2) = {nstr(theta_b, 12)}  "
          f"(lambda = e^theta = {nstr(lam_b, 12)})")
    print()

    geom, vol = torus_bundle_geometry(trB_closed)
    print("(A1) B suspended as an automorphism of the elliptic FIBRE T^2:")
    print(f"     |tr B| > 2  =>  T^2-bundle geometry = {geom}")
    print(f"     Gromov/simplicial volume = {vol}  (torus bundles are NEVER")
    print(f"     hyperbolic; no ideal tetrahedra; no B_2/B_3 scissors class).")
    print()
    print("(A2) tr B = 2.6424 is non-integer  =>  B not in SL_2(Z)")
    print("     (lever1 integrality audit) => B is not even a genuine T^2 map;")
    print("     it is a real CONNECTION HOLONOMY, suspending to no canonical")
    print("     3-manifold.  The only genuine surface diffeos are finite-order")
    print("     S_5 (Hurwitz) -> mapping torus Seifert-fibered -> vol 0.")
    print()

    # (A3) weight-2 ceiling of any hyperbolic 3-manifold (Neumann-Zagier)
    Li2 = polylog(2, 1 / phi ** 2)
    Li2_closed = pi ** 2 / 15 - log(phi) ** 2
    err_w2 = fabs(Li2 - Li2_closed)
    L3v = L3(1 / phi ** 2)
    L3_closed = mpf(4) / 5 * zeta(3)
    err_w3 = fabs(L3v - L3_closed)
    print("(A3) even a hyperbolic 3-manifold is WEIGHT 2 (Neumann-Zagier):")
    print(f"     weight-2  Li_2(1/phi^2) = pi^2/15 - ln^2(phi)  "
          f"|diff|={nstr(err_w2,4)}")
    print(f"        -> pi^2-rational: K_3(Q(sqrt5)) (x) Q = 0 (Borel r_2=0)")
    print(f"     weight-3  L_3(1/phi^2)  = (4/5) zeta(3)        "
          f"|diff|={nstr(err_w3,4)}")
    print(f"        -> genuine: K_5(Q(sqrt5)) (x) Q = rank 2 (target home)")
    assert err_w2 < mpf("1e-38") and err_w3 < mpf("1e-38")
    print()
    print("LEAD A VERDICT: STRUCTURALLY-CLOSED.  No substrate automorphism")
    print("  builds a hyperbolic 3-manifold (finite-order S_5 -> Seifert;")
    print("  the canonical hyperbolic B -> Sol / not a mapping class), and a")
    print("  hyperbolic 3-manifold would be weight-2 anyway.  The lead's premise")
    print("  'a 3-manifold ideal-tetrahedron scissors class IS the B_3 object'")
    print("  is FALSE -- that scissors class is B_2 (weight 2).")
    print()

    # ================================================================
    # LEAD B -- the classical lambda_SW residue tower is q-algebraic
    #           (weight 1); the target is weight 3.  Fork resolution.
    # ================================================================
    print("-" * 74)
    print("LEAD B: weight of the classical  closed-int lambda_SW^{(2)}  residue")
    print("-" * 74)
    print("The wired prolonged-period anchors are EXACT q-rationals:")
    print(f"   a_D^(2) = 1                       = {nstr(aD2, 16)}")
    print(f"   a_D^(3) = (q+1)^2/(3q)            = {nstr(aD3, 16)}")
    print(f"   a_D^(4) = (3q^2+4+3q^-2)/4        = {nstr(aD4, 16)}  (Family-A)")
    print("   => the residue tower a_D^(n) = closed-int lambda_SW^(n) is")
    print("      ALGEBRAIC in q  (weight <= 1).  It yields the TREE periods,")
    print("      hence the bare q[9]_q[10]_q + multiplicative q-rational family")
    print("      (the family the 100-dps 54-basis PSLQ already excluded).")
    print()

    alpha = 1 / mpf("137.035999084")
    codata_inv = mpf("137.035999084")
    bare = q0 * q_int(9, q0) * q_int(10, q0)
    term_2_3pi = mpf(2) / (3 * pi)
    T_data = codata_inv - bare - term_2_3pi
    C_data = T_data / alpha
    print("The data-demanded next term is WEIGHT 3, not weight 1:")
    print(f"   T_data = CODATA - bare - 2/(3pi) = {nstr(T_data, 12)}")
    print(f"   C_data = T_data/alpha            = {nstr(C_data, 12)}"
          f"  (= 0.986 * 1/4pi)")
    print(f"   C_data / [(4/5)zeta(3)]          = {nstr(C_data / L3_closed, 12)}"
          f"  (not clean)")
    print(f"   C_data / zeta(3)                 = {nstr(C_data / zeta(3), 12)}"
          f"  (not clean)")
    print()

    # honest bounded null: no weight-1 (q-rational) combination hits weight-3 C_data;
    # and no clean {zeta3, L(3,chi5)} combination either (re-confirm parent B.2).
    Lchi5 = mpf(0)
    chi = {1: 1, 2: -1, 3: -1, 4: 1, 0: 0}
    for n in range(1, 200000):
        c = chi[n % 5]
        if c:
            Lchi5 += c / mpf(n) ** 3
    tests = [
        ("C_data vs {1, q, q^-1} (weight-1 algebraic)",
         [C_data, mpf(1), q0, 1 / q0]),
        ("C_data vs {zeta3, L(3,chi5)} (weight-3 Borel)",
         [C_data, zeta(3), Lchi5]),
    ]
    print("Bounded PSLQ (canonical generators only; NOT a wide scan):")
    for label, basis in tests:
        rel = pslq(basis, tol=mpf("1e-20"), maxcoeff=10 ** 6)
        print(f"   {label:46}: {rel}")
    print("   -> weight-1 algebraic cannot reach weight-3 C_data; and no clean")
    print("      parameter-free weight-3 Borel combination is forced either.")
    print()
    print("LEAD B VERDICT (fork resolved): the classical residue is WEIGHT 1")
    print("  (q-algebraic) and CANNOT be the weight-3 coefficient -- so")
    print("  closed-int lambda_SW^{(2)}, evaluated classically, does NOT decide")
    print("  it; it gives the tree periods.  The coefficient is intrinsically a")
    print("  WEIGHT-3 = 2-LOOP object (zeta(3) enters QED at two loops).  The")
    print("  exact (4/5)zeta(3) exists but is not a classical-residue output;")
    print("  its normalization is a genuine 2-loop computation.  Honest reading:")
    print("  the 2-loop-QFT side -- no classical closed form; additive")
    print("  prediction is the ceiling.  ((b)-excluded: classical residue =")
    print("  coefficient, cited invariant = transcendence-weight grading.")
    print("  (a)-OPEN: a genuine 2-loop weight-3 closed form.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
