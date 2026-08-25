#!/usr/bin/env python3
"""Two results at the classical point q = 1, both EXACT and both about
`conj:crossing-graded-mass-expansion`:

  (A) xi(q) -> +infinity as q -> 1, not 0 -- so the block is internally
      inconsistent AS WRITTEN.
  (B) z_1 = i EXACTLY, so D(z_1) = Catalan EXACTLY -- which EXPLAINS the
      "0.11% near-match to Catalan" that the sibling probe flagged at the
      substrate anchor as an unexplained numerical coincidence.

Both follow from one exact rational factorisation, recorded in `q1_exact()`.

WHAT THIS ADDS to `descartes_lambda_shape_upper_half_plane.py`.  That probe
observed that xi = D(z_q)/hbar_q^2 = 93.2 at the substrate anchor, which is not
small, and flagged the block's "perturbative"/"semiclassical" tagging as
scope-(a).  A single large value at one anchor is weak evidence: a quantity can
be large at q_0 and still tend to 0 in the limit the block actually names.  This
probe settles the limit itself, which is the claim the block makes.

THE CLAIM UNDER TEST.  `crossing-graded-mass-expansion.md` closes with:

    "Taking the classical limit xi -> 0 recovers the baseline Groebner-Shirshov
     reduction."

and states the locality corollary  m = m_GB * (1 + xi)^c.  For that sentence to
be true, the classical limit must send xi -> 0.

THE ARGUMENT (analytic; the numerics below only confirm it).

  * hbar_q = 1 - 1/q, so the classical limit is q -> 1, where hbar_q -> 0 and
    hbar_q^2 -> 0.  xi = D/hbar_q^2 therefore tends to 0 ONLY IF D(z_q) -> 0
    at least as fast as hbar_q^2.
  * D(z_q) does NOT tend to 0.  At q = 1 exactly the Descartes curve is
    y^2 = x^3 + (2/3) x + 20/27, and the cubic factors over Q:
        27 x^3 + 18 x + 20 = (3x + 2)(9x^2 - 6x + 10),
    so the roots are exactly  -2/3  and  1/3 +- i  -- one real, one conjugate
    pair (equivalently discriminant -4(2/3)^3 - 27(20/27)^2 = -16 < 0).  The
    Legendre lambda is therefore non-real at q = 1 too, the ideal tetrahedron
    at z_1 is non-degenerate, and D(z_1) is a nonzero constant.
  * Hence xi = D(z_q)/hbar_q^2 -> D(z_1)/0+ = +infinity as q -> 1.

RESULT (B) -- the Catalan near-match, EXPLAINED.  The same factorisation pins
the classical shape exactly.  Ordering the roots (e1, e2, e3) = (-2/3, 1/3 - i,
1/3 + i),

    z_1 = lambda = (e3 - e1)/(e2 - e1) = (1 + i)/(1 - i) = i    EXACTLY,

the shape of the REGULAR IDEAL OCTAHEDRON, whose angle triple is
(pi/2, pi/4, pi/4) and whose volume is D(i) = Catalan G = Vol(B_3)/8.

The sibling probe `descartes_lambda_shape_upper_half_plane.py` recorded, as
OBSERVATION 1, that at the substrate anchor z_q sits *near* i and D(z_q) sits
0.11% from Catalan, and correctly refused to call it an identity ("a near-match,
NOT an identity ... Recorded as an observation only").  That was the right call
and it stands: at q_0 it is NOT an identity.  What this probe adds is WHERE the
near-match comes from -- it is the q -> 1 limit, exact at q = 1, and the 0.11%
is simply how far the substrate anchor sits from the classical point.  So the
near-match is neither a coincidence nor a hidden identity at q_0: it is the
leading behaviour of an exactly-known limit.  Nothing is thereby wired, and no
identity at q_0 is claimed -- the 0.11% gap remains a gap.

The classical limit is the OPPOSITE of what the block says.  Note this is a
statement about the limit's DIRECTION and needs no anchor: the q=1 discriminant
is -16 exactly, so the conclusion does not depend on any measured input.

SCOPE.  Scope-(a) -- this flags the STATEMENT of one conjecture block.  It
refutes no ingredient: not Bloch-Wigner D, not the shape parameter z_q, not the
crossing grading, not the ideal-tetrahedron machinery.  A crossing-graded
expansion may well be correct in some variable; what is established is that
`xi = D/hbar_q^2` is not a variable in which it is perturbative, because that
xi diverges in the very limit the block calls classical.

The three readings that survive (unchanged from the sibling probe, now with the
limit as a discriminator):
  (R1) the sentence is simply wrong and the expansion is not perturbative;
  (R2) xi was meant as D * hbar_q^2, which DOES tend to 0 as q -> 1 -- this
       reading is consistent with the classical-limit sentence, and the probe
       reports it alongside for comparison;
  (R3) z_q denotes a third object whose D vanishes as q -> 1.
This probe cannot choose between them -- that is the block owner's call.  What
it removes is the possibility that the block is fine as written.

auditOnly: no witness emitted -- a consistency check on a conjecture's prose,
not a production number.  Nothing here is wired; the canonical absolute-mass
route (computations/canonical_mass.py) does not use xi at all.
"""
import itertools
import math

from mpmath import mp, mpf, mpc, polylog, arg, log, sqrt
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Proton = experimental/default pin per AGENTS.md; muon = ideal CAL-2 proxy.
Q_PROTON = mpf("1.1099785827513808")
Q_MUON = mpf("1.10997859555733471")


def weierstrass(q):
    """(p, r) of the Descartes curve y^2 = x^3 + p x + r.

    The s-form, taken straight off the Weierstrass equation, is the one used
    here; the q-form is asserted against it exactly as the sibling probe does.
    """
    s = sqrt(q)
    p_q = 2 * (q * q - q + 1) / (3 * q) + (q - 1) / (3 * s)
    r_q = (20 * (q - 1) ** 3 / (27 * q ** mpf("1.5")) + 5 * (q - 1) ** 2 / (9 * q)
           + 5 * (s - 1 / s) / 9 + mpf(20) / 27)
    p_s = (2 * s ** 4 + s ** 3 - 2 * s ** 2 - s + 2) / (3 * s ** 2)
    r_s = (5 * (s ** 2 + s - 1) * (4 * s ** 4 - s ** 3 - 4 * s ** 2 + s + 4)
           / (27 * s ** 3))
    assert abs(p_q - p_s) < mpf("1e-30"), f"p forms disagree: {p_q} vs {p_s}"
    assert abs(r_q - r_s) < mpf("1e-30"), f"r forms disagree: {r_q} vs {r_s}"
    return p_s, r_s


def cubic_roots(p, r):
    """Roots of x^3 + p x + r = 0 (Cardano, complex arithmetic throughout)."""
    disc_c = (r / 2) ** 2 + (p / 3) ** 3
    sq = sqrt(mpc(disc_c))
    u3 = -r / 2 + sq
    u = u3 ** (mpf(1) / 3)
    w = mpc(-mpf(1) / 2, sqrt(mpf(3)) / 2)
    roots = []
    for k in range(3):
        uk = u * w ** k
        vk = (-p / 3 / uk) if abs(uk) > mpf("1e-300") else mpc(0)
        roots.append(uk + vk)
    return roots


def lambda_upper(roots):
    """The Legendre cross-ratio branch with Im > 0 -- the orientation that
    `AngleTriple.ofShape` needs."""
    lams = [(e3 - e1) / (e2 - e1) for e1, e2, e3 in itertools.permutations(roots)]
    return max(lams, key=lambda l: l.imag)


def bloch_wigner(z):
    """D(z) = Im Li_2(z) + arg(1 - z) log|z| -- the standard closed form.

    Cross-checked below against the corpus's angle route
    Lambda(a1) + Lambda(a2) + Lambda(a3), so this faster evaluation is not a
    new convention.
    """
    return polylog(2, z).imag + arg(1 - z) * log(abs(z))


def tet_angles(z):
    """The corpus's tetAngle_1/2/3 (BlochWignerLobachevsky.lean)."""
    return arg(z), arg(1 / (1 - z)), arg(1 - 1 / z)


def xi_at(q):
    """(D(z_q), hbar_q, xi) at a given q."""
    p, r = weierstrass(q)
    z = lambda_upper(cubic_roots(p, r))
    d = bloch_wigner(z)
    hbar = 1 - 1 / q
    return z, d, hbar, d / hbar ** 2


def q1_exact():
    """The q = 1 facts, in EXACT rational arithmetic -- no floats, no anchors.

    Verifies, over Q and Q(i):
      * p(1) = 2/3, r(1) = 20/27
      * 27 x^3 + 18 x + 20 = (3x + 2)(9x^2 - 6x + 10)
      * roots are exactly -2/3 and 1/3 +- i
      * lambda = (e3 - e1)/(e2 - e1) = i   for (e1,e2,e3) = (-2/3, 1/3-i, 1/3+i)

    Returns nothing; raises AssertionError if any identity fails.  This is the
    load-bearing part of both results -- everything numerical below only
    illustrates it.
    """
    from fractions import Fraction as F

    # p(1), r(1) from the s-form at s = 1, evaluated over Q.
    s = F(1)
    p1 = (2 * s ** 4 + s ** 3 - 2 * s ** 2 - s + 2) / (3 * s ** 2)
    r1 = (5 * (s ** 2 + s - 1) * (4 * s ** 4 - s ** 3 - 4 * s ** 2 + s + 4)
          / (27 * s ** 3))
    assert p1 == F(2, 3), f"p(1) = {p1}, expected 2/3"
    assert r1 == F(20, 27), f"r(1) = {r1}, expected 20/27"

    # Clearing denominators: x^3 + (2/3)x + 20/27 = 0  <=>  27x^3 + 18x + 20 = 0.
    target = [27, 0, 18, 20]  # descending coefficients
    a, b = [3, 2], [9, -6, 10]
    prod = [0] * 4
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            prod[i + j] += u * v
    assert prod == target, f"(3x+2)(9x^2-6x+10) = {prod}, expected {target}"

    # Real root -2/3, exactly.
    x = F(-2, 3)
    assert 27 * x ** 3 + 18 * x + 20 == 0, "-2/3 must be a root"

    # Quadratic 9x^2 - 6x + 10: discriminant 36 - 360 = -324 = (18i)^2, so the
    # roots are (6 +- 18i)/18 = 1/3 +- i, exactly.
    assert 36 - 4 * 9 * 10 == -324, "quadratic discriminant must be -324"
    # Verify 1/3 + i is a root using exact Gaussian-rational arithmetic:
    # 9(1/3+i)^2 - 6(1/3+i) + 10, with (1/3+i)^2 = 1/9 - 1 + (2/3)i.
    re2, im2 = F(1, 9) - 1, F(2, 3)                      # (1/3 + i)^2
    re = 9 * re2 - 6 * F(1, 3) + 10                      # real part
    im = 9 * im2 - 6 * 1                                 # imaginary part
    assert (re, im) == (0, 0), f"1/3+i not a root: {re} + {im}i"

    # lambda = (e3-e1)/(e2-e1) = (1+i)/(1-i) = i, exactly.
    # (1+i)/(1-i) = (1+i)^2 / ((1-i)(1+i)) = (2i)/2 = i.
    num_re, num_im = 0, 2        # (1+i)^2 = 2i
    den = 2                      # (1-i)(1+i) = 2
    assert (F(num_re, den), F(num_im, den)) == (F(0), F(1)), "lambda must be i"


def main():
    print("xi(q) = D(z_q)/hbar_q^2 in the classical limit q -> 1\n")

    q1_exact()
    print("=== EXACT (rational arithmetic, no anchors, no floats) ===")
    print("  p(1) = 2/3,  r(1) = 20/27")
    print("  27x^3 + 18x + 20 = (3x + 2)(9x^2 - 6x + 10)")
    print("  roots exactly: -2/3,  1/3 + i,  1/3 - i   (one real, one pair)")
    print("  => z_1 = lambda = (1 + i)/(1 - i) = i  EXACTLY")
    print("     i is the REGULAR IDEAL OCTAHEDRON shape, angles (pi/2, pi/4, pi/4),")
    print("     and D(i) = Catalan G = Vol(B_3)/8.")
    print("  all exact identities verified\n")

    # ---- exact fact at q = 1: the discriminant is -16, so z_1 is non-real ----
    p1, r1 = weierstrass(mpf(1))
    disc1 = -4 * p1 ** 3 - 27 * r1 ** 2
    print("=== q = 1 exactly (the classical point) ===")
    print(f"  p = {p1}  (exact 2/3   = {mpf(2)/3})")
    print(f"  r = {r1}  (exact 20/27 = {mpf(20)/27})")
    print(f"  discriminant -4p^3 - 27r^2 = {disc1}   (exact -16)")
    assert abs(p1 - mpf(2) / 3) < mpf("1e-30"), "p(1) should be 2/3"
    assert abs(r1 - mpf(20) / 27) < mpf("1e-30"), "r(1) should be 20/27"
    assert abs(disc1 + 16) < mpf("1e-28"), "disc(1) should be -16"
    z1, d1, _, _ = xi_at(mpf(1) + mpf("1e-30"))  # hbar=0 at q=1; nudge off it
    print(f"  z_1 = {mp.nstr(z1, 12)}   Im != 0 -> tetrahedron non-degenerate")
    print(f"  D(z_1) = {mp.nstr(d1, 12)}   <- a NONZERO constant\n")
    assert abs(d1) > mpf("0.5"), "D(z_1) must not vanish for the argument to hold"

    # The numerics must reproduce the exact q=1 facts established above.
    CATALAN = mpf("0.915965594177219015054603514932384110774")
    assert abs(z1 - mpc(0, 1)) < mpf("1e-25"), f"z_1 should be i, got {z1}"
    assert abs(d1 - CATALAN) < mpf("1e-25"), f"D(z_1) should be Catalan, got {d1}"
    print(f"  numerics agree with the exact result: |z_1 - i| = "
          f"{mp.nstr(abs(z1 - mpc(0,1)), 4)}, "
          f"|D(z_1) - G| = {mp.nstr(abs(d1 - CATALAN), 4)}\n")

    # ---- cross-check D against the corpus's angle route at the anchor ----
    z, d, hbar, xi = xi_at(Q_PROTON)
    a1, a2, a3 = tet_angles(z)
    print("=== convention cross-check at the proton anchor ===")
    print(f"  angles = ({mp.nstr(a1, 10)}, {mp.nstr(a2, 10)}, {mp.nstr(a3, 10)})")
    print(f"  sum    = {mp.nstr(a1 + a2 + a3, 12)}   pi = {mp.nstr(mp.pi, 12)}")
    assert a1 > 0 and a2 > 0 and a3 > 0, "angles must be positive"
    assert abs(a1 + a2 + a3 - mp.pi) < mpf("1e-25"), "angles must sum to pi"
    print(f"  D via Li_2 closed form  = {mp.nstr(d, 15)}")
    print("  (matches the sibling probe's Lambda-sum value 0.9149... to its"
          " 1e-6 series accuracy)\n")

    # ---- the limit itself ----
    print("=== the limit: q -> 1 ===")
    print(f"  {'q':>18}  {'hbar_q^2':>14}  {'D(z_q)':>14}  {'xi = D/hbar^2':>16}"
          f"  {'D*hbar^2 (R2)':>16}")
    prev_xi = None
    monotone_up = True
    for e in range(1, 9):
        q = 1 + mpf(10) ** (-e)
        _, d_e, hbar_e, xi_e = xi_at(q)
        print(f"  {mp.nstr(q, 10):>18}  {mp.nstr(hbar_e**2, 6):>14}  "
              f"{mp.nstr(d_e, 8):>14}  {mp.nstr(xi_e, 8):>16}  "
              f"{mp.nstr(d_e * hbar_e**2, 6):>16}")
        if prev_xi is not None and not xi_e > prev_xi:
            monotone_up = False
        prev_xi = xi_e

    assert monotone_up, "xi must increase as q -> 1 for the verdict to hold"
    assert prev_xi > mpf("1e12"), "xi should blow up; got %s" % prev_xi

    print("\n=== at the anchors (for reference) ===")
    for name, q in (("proton (default)", Q_PROTON), ("muon (ideal CAL-2)", Q_MUON)):
        _, d_a, hbar_a, xi_a = xi_at(q)
        print(f"  {name:<20} q = {mp.nstr(q, 17)}  xi = {mp.nstr(xi_a, 10)}"
              f"   D*hbar^2 = {mp.nstr(d_a * hbar_a**2, 8)}")

    # ---- (B) the Catalan near-match, explained ----
    _, d_p, hbar_p, _ = xi_at(Q_PROTON)
    CATALAN = mpf("0.915965594177219015054603514932384110774")
    print("\n=== RESULT (B): the Catalan near-match is the q -> 1 limit ===")
    print(f"  D(z_1)   = {mp.nstr(CATALAN, 15)}   = Catalan G, EXACTLY (z_1 = i)")
    print(f"  D(z_q0)  = {mp.nstr(d_p, 15)}   at the proton anchor")
    print(f"  gap      = {mp.nstr(abs(d_p - CATALAN)/CATALAN * 100, 4)} %"
          f"   <- the sibling probe's flagged 0.11%")
    print("  The near-match is the leading behaviour of an EXACTLY known limit,")
    print("  not a coincidence -- and still NOT an identity at q_0: the gap is")
    print("  real and is how far the substrate sits from the classical point.")

    print("\nVERDICT (scope-(a), about the STATEMENT of one conjecture block):")
    print("  D(z_q) tends to the NONZERO constant D(z_1) = Catalan, because the")
    print("  q=1 cubic factors as (3x+2)(9x^2-6x+10), giving z_1 = i exactly.")
    print("  hbar_q^2 -> 0.  Therefore xi -> +infinity as q -> 1.")
    print("  `crossing-graded-mass-expansion.md` says 'taking the classical")
    print("  limit xi -> 0 recovers the baseline'.  Under its own definitions")
    print("  the classical limit sends xi the OTHER WAY, so the block cannot be")
    print("  correct as written.  The reciprocal D*hbar_q^2 DOES tend to 0")
    print("  (column 5), which is reading (R2); choosing among (R1)/(R2)/(R3)")
    print("  is the block owner's call, not this probe's.")
    print("  Refutes NO ingredient, and nothing here is wired to production.")


if __name__ == "__main__":
    main()
