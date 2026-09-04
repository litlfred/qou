#!/usr/bin/env python3
"""Is the Descartes shape parameter z_q in the upper half plane?  Yes -- and it
is forced, not fitted: the Descartes cubic has NEGATIVE discriminant at both
anchors, so its Legendre lambda-invariant cannot be real.

WHY THIS IS ASKED.  `conj:crossing-graded-mass-expansion` builds the depth
scalar xi(q) = D(z_q)/hbar_q^2 on "the universal shape parameter z_q from the
Descartes elliptic curve", D being Bloch-Wigner.  D VANISHES IDENTICALLY ON THE
REALS (a real shape is a flat/degenerate ideal tetrahedron -- the corpus records
this as the reason `Lob_zero`/`Lob_pi` make D vanish on real-shape tetrahedra).
So if z_q were real, xi would be identically 0 and the whole crossing-graded
expansion would collapse to its n=0 term, the flat Groebner-Shirshov baseline.
The conjecture is therefore vacuous unless Im z_q != 0.

It is also the hypothesis of `AngleTriple.ofShape`
(QOU/Archimedean/IdealTetrahedronShapeBridge.lean), which needs Im z > 0 before
the ideal-tetrahedron concavity results apply at z_q.

WHICH z_q -- the symbol is overloaded, so this is pinned deliberately.  Three
distinct objects share the glyph in this corpus:
  * `z = s - 1/s` (s = sqrt q), the "spacetime ratio" at which
    descartes-elliptic-curve.md takes the color elliptic fibre.  REAL.
  * `z_q`, the information-theory partition function.  Unrelated.
  * `z_q = lambda(E_q)`, the LEGENDRE INVARIANT of the Descartes curve.  This is
    the one the conjecture means -- crossing-graded-mass-expansion.lean says so
    explicitly: "xi(q) = D(lambda(E_q)) / hbar_q^2 ... lambda the Legendre
    invariant of the Descartes elliptic curve".
Reading the .md alone would have picked the REAL `s - 1/s` and concluded the
conjecture was vacuous.  It is the .lean that disambiguates.

THE ARGUMENT.  For y^2 = x^3 + px + r the discriminant is -4p^3 - 27r^2.  It is
negative at both anchors, so the cubic has one real root and a complex-conjugate
pair; the Legendre lambda -- a cross-ratio of the three roots -- is then
necessarily non-real.  This is a SIGN fact, not a numerical coincidence: no
fitting, no anchor-inversion.

SCOPE.  Scope-(a).  What is established: Im z_q != 0 at both anchors, so the
degeneracy that would make the conjecture vacuous does not occur, and the
`ofShape` hypothesis is satisfiable.  What is NOT established: that the
crossing-graded expansion is CORRECT, that xi is the right depth scalar, or any
mass/binding claim.  Nothing here is wired to production; the canonical
absolute-mass route (computations/canonical_mass.py) does not use xi at all.

auditOnly: no witness emitted -- this is a consistency/non-degeneracy check, not
a new production number.
"""
import cmath
import math

# The MUON leg read BY NAME (bean qou-9ugp, 2026-09-04). It was the literal
# 1.1099785955573347..., the RETIRED self-certified pin A -- retired 2026-08-22
# when the muon anchor was re-derived to the CODATA-2022 lepton ratio. This is a
# DELIBERATE two-pin comparison, so the fix is the live MUON value, not proton:
# swapping in the proton pin would delete the comparison this probe exists for.
# The stale leg understated the mu-p separation by 0.67% (11.5371 vs 11.6141
# ppb) -- the fourth instance of that class found in this drain.
import sys as _sys_qm  # noqa: E402
from pathlib import Path as _Path_qm  # noqa: E402
for _p_qm in (_Path_qm(__file__).resolve().parent,
              _Path_qm(__file__).resolve().parent.parent,
              _Path_qm(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qm) not in _sys_qm.path:
        _sys_qm.path.insert(0, str(_p_qm))
from q_parameter import q_muon_at as _q_muon_at  # noqa: E402
Q_MUON_LIVE_STR = str(_q_muon_at(50))

# Anchors.  Proton is the experimental/default pin per AGENTS.md; muon is the
# ideal-layer CAL-2 proxy pin.  Both are checked so the conclusion is not
# anchor-specific.
ANCHORS = [
    ("proton (experimental, default)", 1.1099785827513808),
    ("muon (ideal CAL-2 proxy)", float(Q_MUON_LIVE_STR)),
]


def weierstrass(q):
    """(p, r) of the Descartes curve y^2 = x^3 + p x + r, both forms."""
    s = math.sqrt(q)
    p_q = 2 * (q * q - q + 1) / (3 * q) + (q - 1) / (3 * s)
    r_q = (20 * (q - 1) ** 3 / (27 * q ** 1.5) + 5 * (q - 1) ** 2 / (9 * q)
           + 5 * (s - 1 / s) / 9 + 20 / 27)
    # independent form in s, straight off the Weierstrass equation
    p_s = (2 * s ** 4 + s ** 3 - 2 * s ** 2 - s + 2) / (3 * s ** 2)
    r_s = (5 * (s ** 2 + s - 1) * (4 * s ** 4 - s ** 3 - 4 * s ** 2 + s + 4)
           / (27 * s ** 3))
    assert abs(p_q - p_s) < 1e-12, f"p forms disagree: {p_q} vs {p_s}"
    assert abs(r_q - r_s) < 1e-12, f"r forms disagree: {r_q} vs {r_s}"
    return p_q, r_q


def cubic_roots(p, r):
    """Roots of x^3 + p x + r = 0 (Cardano, complex arithmetic throughout)."""
    disc_c = (r / 2) ** 2 + (p / 3) ** 3
    sq = cmath.sqrt(complex(disc_c))
    u3, v3 = -r / 2 + sq, -r / 2 - sq
    u = u3 ** (1 / 3) if abs(u3) > 0 else 0
    w = complex(-0.5, math.sqrt(3) / 2)
    roots = []
    for k in range(3):
        uk = u * w ** k
        vk = (-p / 3 / uk) if abs(uk) > 1e-300 else 0
        roots.append(uk + vk)
    return roots


def lambda_invariants(roots):
    """The six Legendre cross-ratios (e3-e1)/(e2-e1) over root orderings."""
    import itertools
    out = []
    for e1, e2, e3 in itertools.permutations(roots):
        out.append((e3 - e1) / (e2 - e1))
    return out


def clausen2(theta, terms=2_000_000):
    """Cl_2(theta) = sum_{k>=1} sin(k theta)/k^2 -- the Lobachevsky primitive."""
    theta = math.fmod(theta, 2 * math.pi)
    total = 0.0
    for k in range(1, terms + 1):
        total += math.sin(k * theta) / (k * k)
    return total


def lob(t):
    """Lobachevsky Lambda(t) = Cl_2(2t)/2 -- the corpus's normalisation."""
    return clausen2(2 * t) / 2


def bloch_wigner_via_angles(z):
    """D(z) as the ideal-tetrahedron volume Lambda(a)+Lambda(b)+Lambda(c),
    using exactly the corpus's tetAngle_1/2/3 (BlochWignerLobachevsky.lean)."""
    a1 = cmath.phase(z)
    a2 = cmath.phase(1 / (1 - z))
    a3 = cmath.phase(1 - 1 / z)
    return a1, a2, a3, lob(a1) + lob(a2) + lob(a3)


def main():
    print("Descartes shape parameter: is z_q = lambda(E_q) in the upper half plane?\n")
    all_nonreal = True
    for name, q in ANCHORS:
        p, r = weierstrass(q)
        disc = -4 * p ** 3 - 27 * r ** 2
        roots = cubic_roots(p, r)
        n_real = sum(1 for e in roots if abs(e.imag) < 1e-9)
        print(f"=== {name}:  q = {q}")
        print(f"    p = {p:.12f}   r = {r:.12f}   (q-form and s-form agree)")
        print(f"    discriminant -4p^3 - 27r^2 = {disc:.10f}  -> "
              f"{'NEGATIVE' if disc < 0 else 'POSITIVE'}")
        print(f"    roots: {n_real} real, {3 - n_real} complex")
        for e in roots:
            print(f"      {e.real:+.12f} {e.imag:+.12f}i")

        lams = lambda_invariants(roots)
        ims = [l.imag for l in lams]
        max_im = max(ims)
        nonreal = min(abs(i) for i in ims) > 1e-9
        all_nonreal &= nonreal
        print(f"    six Legendre lambdas: all non-real = {nonreal}; "
              f"max Im = {max_im:.12f}")

        # canonical branch: Im lambda > 0, the orientation `ofShape` needs
        z = max(lams, key=lambda l: l.imag)
        a1, a2, a3, vol = bloch_wigner_via_angles(z)
        hbar_q = 1 - 1 / q
        print(f"    z_q (Im>0 branch) = {z.real:+.12f} {z.imag:+.12f}i")
        print(f"    tet angles: {a1:.9f}, {a2:.9f}, {a3:.9f}  "
              f"(sum = {a1 + a2 + a3:.9f}, pi = {math.pi:.9f})")
        assert a1 > 0 and a2 > 0 and a3 > 0, "angles must be positive"
        assert abs(a1 + a2 + a3 - math.pi) < 1e-9, "angles must sum to pi"
        print(f"    D(z_q) = Vol = {vol:.10f}")
        print(f"    hbar_q = {hbar_q:.12f}   xi(q) = D/hbar_q^2 = "
              f"{vol / hbar_q ** 2:.10f}\n")

    assert all_nonreal, "a lambda came out real -- conclusion would flip"
    print("VERDICT: Im z_q != 0 at both anchors, FORCED by disc < 0.")
    print("  => the ideal tetrahedron at z_q is non-degenerate, D(z_q) != 0,")
    print("     so conj:crossing-graded-mass-expansion is not vacuous, and the")
    print("     AngleTriple.ofShape hypothesis is satisfiable at z_q.")
    print("  NOT established: that the expansion is correct, or any mass claim.")

    # ---------------------------------------------------------------- #
    # Two observations that fall out, both labelled, NEITHER wired.
    # ---------------------------------------------------------------- #
    q = ANCHORS[0][1]
    p, r = weierstrass(q)
    z = max(lambda_invariants(cubic_roots(p, r)), key=lambda l: l.imag)
    a1, a2, a3, vol = bloch_wigner_via_angles(z)
    hbar_q = 1 - 1 / q
    xi = vol / hbar_q ** 2

    # Catalan G = Vol of the (pi/4, pi/4, pi/2) tetrahedron, since Lambda(pi/2)=0
    # and Lambda(pi/4) = G/2.  That triple is the regular ideal OCTAHEDRON's,
    # i.e. L6a4's unique symmetric point (L6a4AngleStructure), and Vol(B_3)=8G.
    G = 0.915965594177219015054603514932
    print("\n--- OBSERVATION 1 (NEAR-MATCH, not an identity, NOT wired) ---")
    print(f"  z_q            = {z.real:+.9f} {z.imag:+.9f}i   (near i, not i)")
    print(f"  tet angles     = ({a1:.9f}, {a2:.9f}, {a3:.9f})")
    print(f"  octahedral     = ({math.pi/2:.9f}, {math.pi/4:.9f}, {math.pi/4:.9f})")
    print(f"  angle deltas   = ({a1-math.pi/2:+.2e}, {a2-math.pi/4:+.2e}, "
          f"{a3-math.pi/4:+.2e})")
    print(f"  D(z_q)         = {vol:.10f}")
    print(f"  Catalan G      = {G:.10f}     (= Vol of the octahedral triple)")
    print(f"  rel deviation  = {abs(vol-G)/G:.6e}  ({abs(vol-G)/G*100:.4f} %)")
    print("  => z_q sits NEAR the regular-ideal-octahedron shape i, and D(z_q)")
    print("     NEAR Catalan (= Vol(B_3)/8).  0.11% is FAR outside both the")
    print("     numerical error (~1e-6) and any L2 precision target, so this is")
    print("     a near-match, NOT an identity.  Recorded as an observation only.")

    print("\n--- OBSERVATION 2 (a problem with the conjecture AS WRITTEN) ---")
    print(f"  hbar_q^2 = {hbar_q**2:.10f}, so xi = D/hbar_q^2 = {xi:.6f}")
    print("  The block tags this expansion 'perturbative' / 'semiclassical' and")
    print("  says 'taking the classical limit xi -> 0 recovers the baseline'.")
    print(f"  But xi = {xi:.1f} >> 1.  Under the locality corollary")
    print("  m = m_GB * (1 + xi)^c that is a growth factor per crossing of")
    for c in (1, 3, 6):
        print(f"      c = {c:>2}:  (1 + xi)^c = {(1+xi)**c:.4e}")
    print("  so the series is not a perturbation of anything.  Either the")
    print("  conjecture is wrong as stated, or xi is meant as D * hbar_q^2")
    print(f"  (= {vol*hbar_q**2:.6e}, genuinely small), or z_q is a third object.")
    print("  Scope-(a): this flags the STATEMENT, and refutes no ingredient.")


if __name__ == "__main__":
    main()
