#!/usr/bin/env python3
"""SCOPE PROBE — is the obtuse case a failure of Milnor's IDENTITY, or only of
his SUBDIVISION ARGUMENT?

The `qou-w3eg` / `qou-5gai` H4 tier has carried Milnor's restriction

    "if all three angles are acute"                    [milnor1982, Appendix]

as "the flagged place to go wrong" for H4-3/H4-5, in wording that repeatedly
reads as though the RESULT

    \\int\\int_{ABC} dA / (2(R^2 - x^2 - y^2))  =  Lambda(a)+Lambda(b)+Lambda(g)

were in doubt when the triangle is obtuse.  It is not.  This probe separates
the two readings, because they imply different amounts of remaining work:

  * if the IDENTITY failed for obtuse triangles, H4-5 would need a different
    theorem (a signed Lambda-sum) and the tier's target statement is wrong;
  * if only the SUBDIVISION degenerates -- the circumcentre leaves the
    triangle, so one of the three wedges must enter with a minus sign -- then
    the target statement is uniform and H4-5 needs a signed ASSEMBLY of the
    same pieces.

WHAT IS COMPUTED.  Both sides, independently:

  LHS  polar quadrature of the base integral over the inscribed triangle.  The
       radial integral is taken in CLOSED FORM
           int_lo^hi r dr / (2(R^2-r^2)) = -1/4 log((R^2-hi^2)/(R^2-lo^2)),
       deliberately, not by nested quadrature: at a vertex direction the ray
       reaches the circle, R^2-r^2 vanishes, and nested quadrature divides by
       zero there.  The resulting log singularity in the angle is integrable.
       The ray is CLIPPED to the triangle (entry AND exit), which is what makes
       the obtuse case -- circumcentre outside, so the ray enters at r > 0 --
       computed correctly rather than silently mis-integrated from r = 0.

  RHS  Lambda(a)+Lambda(b)+Lambda(g) with Lambda the Lobachevsky function
       Lambda(x) = -int_0^x log|2 sin t| dt.

Nothing here is fitted: there is no free parameter.  The triangle is determined
by (a,b,g) with a+b+g = pi, placed on the circle by the inscribed-angle theorem
(arc BC = 2a, etc.), and R is set to a value != 1 so that any spurious
R-dependence would show up.

ALSO CHECKED, as a control: the WEDGE value Lambda(psi), i.e. that one isoceles
wedge (apex at the circumcentre, apex angle 2psi) integrates to Lambda(psi).
This is now PROVED in Lean -- `hypVolume_chimney_wedge` (H4-5b) -- so it is a
regression check on the probe's own quadrature, not new evidence.

SCOPE OF THE CONCLUSION (per AGENTS.md "Before declaring refuted / ruled out"):
this probe supports a scope-(a) statement -- "Milnor's circumcentre subdivision,
AS AN ARGUMENT, does not apply unchanged to obtuse triangles" -- and REFUTES the
stronger reading that the identity itself is acute-only.  It is numerical
evidence about a target statement, NOT a proof of the identity, and it wires to
nothing.

  -- Ref: [milnor1982] Appendix
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [manuscript] beans qou-w3eg (H4-5), qou-5gai (H4)
"""
from __future__ import annotations

import json
import math
import platform
import sys
import time
from pathlib import Path

from mpmath import mp, mpf, quad, sin, cos, log, pi

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parent / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402

COMPUTE_DPS = 30
mp.dps = COMPUTE_DPS

WITNESS_NAME = "milnor-subdivision-obtuse-scope-probe"

# Agreement floor.  The LHS quadrature integrates through three integrable log
# singularities (one per vertex, where the ray meets the circle), so it is not
# expected to reach full working precision; 1e-12 is far below any plausible
# structural discrepancy and far above the quadrature's own noise.
TOL = mpf("1e-12")


def Lob(x):
    """Lobachevsky Lambda(x) = -int_0^x log|2 sin t| dt."""
    return -quad(lambda t: log(abs(2 * sin(t))), [0, x])


def radial(R, lo, hi):
    """int_lo^hi r dr / (2(R^2 - r^2)), in closed form (see module docstring)."""
    num = R**2 - hi**2
    den = R**2 - lo**2
    floor = mpf(10) ** (-(mp.dps + 10))
    if num < floor:          # a vertex direction: ray reaches the circle
        num = floor
    return -mpf(1) / 4 * log(num / den)


def wedge_base_integral(R, psi):
    """Base integral over the isoceles wedge of half-angle psi."""
    return quad(lambda phi: radial(R, mpf(0), R * cos(psi) / cos(phi)),
                [-psi, 0, psi])


def triangle_base_integral(R, a, b, g):
    """Base integral over the triangle inscribed in the circle of radius R with
    inscribed angles (a, b, g).  Works for acute AND obtuse: the ray is clipped
    to the triangle at both ends."""
    tA, tB, tC = mpf(0), 2 * g, 2 * g + 2 * a      # arc AB = 2g, BC = 2a, CA = 2b
    V = [(R * cos(t), R * sin(t)) for t in (tA, tB, tC)]
    sides = [(V[0], V[1]), (V[1], V[2]), (V[2], V[0])]
    EPS = mpf(10) ** (-22)

    def ray_hits(phi):
        """Positive distances at which the ray from the circumcentre meets the
        triangle's boundary.  TWO hits when the circumcentre is outside."""
        ux, uy = cos(phi), sin(phi)
        hits = []
        for (p, q) in sides:
            dx, dy = q[0] - p[0], q[1] - p[1]
            den = dx * uy - dy * ux                 # cross(d, u)
            if abs(den) < EPS:
                continue
            t = -(p[0] * uy - p[1] * ux) / den
            if -EPS <= t <= 1 + EPS:
                s = (p[0] + t * dx) * ux + (p[1] + t * dy) * uy
                if s > EPS:
                    hits.append(s)
        return sorted(hits)

    def inner(phi):
        h = ray_hits(phi)
        if not h:
            return mpf(0)
        lo = mpf(0) if len(h) < 2 else h[0]         # inside -> 0; outside -> entry
        hi = h[-1]
        return radial(R, lo, hi) if hi > lo else mpf(0)

    angs = sorted(math.atan2(float(v[1]), float(v[0])) for v in V)
    a0, a1, a2 = angs
    cand = [(a0, a1), (a1, a2), (a2, a0 + 2 * float(pi))]
    pieces = [(p0, p1) for (p0, p1) in cand if ray_hits(mpf((p0 + p1) / 2))]
    return sum(quad(inner, [mpf(p0), mpf(p1)]) for (p0, p1) in pieces)


# ---------------------------------------------------------------- the cases

WEDGES = [mpf("0.3"), mpf("0.7"), mpf("1.0"), mpf("1.4"), pi / 3, pi / 6]

ACUTE = [
    (pi / 3, pi / 3, pi / 3),                       # equilateral
    (mpf("1.2"), mpf("1.0"), pi - mpf("2.2")),
    (mpf("1.4"), mpf("1.1"), pi - mpf("2.5")),
    (mpf("0.9"), mpf("1.3"), pi - mpf("2.2")),
    (mpf("1.5"), mpf("1.5"), pi - mpf("3.0")),      # nearly degenerate, still acute
]

OBTUSE = [
    (mpf("2.0"), mpf("0.7"), pi - mpf("2.7")),
    (mpf("2.5"), mpf("0.4"), pi - mpf("2.9")),
    (mpf("1.8"), mpf("0.9"), pi - mpf("2.7")),
    (pi / 2, mpf("0.8"), pi / 2 - mpf("0.8")),      # RIGHT triangle, the boundary
]


def in_milnor_wedges(R, t, a, b, g, w, tol=mpf("1e-18")):
    """Membership in `milnorWedges R t a b g` -- the Lean definition, evaluated
    literally: the union of three `wedgeAt`s at the axes/half-angles Milnor's
    subdivision produces.

        wedgeAt R theta psi = { <w,u> < R cos psi  and  |<w,v>| < <w,u> tan psi }
        u = (cos theta, sin theta),  v = (-sin theta, cos theta)
    """
    from mpmath import tan
    axes = [(t + g, g), (t + 2 * g + a, a), (t + 2 * g + 2 * a + b, b)]
    for (th, psi) in axes:
        wu = w[0] * cos(th) + w[1] * sin(th)
        wv = -(w[0] * sin(th)) + w[1] * cos(th)
        if wu < R * cos(psi) - tol and abs(wv) < wu * tan(psi) - tol:
            return True
    return False


def in_triangle(R, t, a, b, g, w, tol=mpf("1e-18")):
    """Membership in the OPEN triangle inscribed in the circle of radius R with
    inscribed angles (a,b,g) and first vertex at angle t -- by the three
    half-plane tests, independent of the wedge description."""
    tA, tB, tC = t, t + 2 * g, t + 2 * g + 2 * a
    V = [(R * cos(x), R * sin(x)) for x in (tA, tB, tC)]
    cx = sum(p[0] for p in V) / 3
    cy = sum(p[1] for p in V) / 3
    for (p, q) in [(V[0], V[1]), (V[1], V[2]), (V[2], V[0])]:
        dx, dy = q[0] - p[0], q[1] - p[1]
        d = dx * (w[1] - p[1]) - dy * (w[0] - p[0])
        dc = dx * (cy - p[1]) - dy * (cx - p[0])
        if d * dc <= tol:
            return False
    return True


def wedges_vs_triangle_mismatches(R, t, a, b, g, n=120):
    """Sample the disk on a polar grid and count points where membership in
    `milnorWedges` and membership in the open triangle DISAGREE.

    This is the ONE step of H4-5c-ii still unproved in Lean
    (`milnorWedges = the inscribed triangle`, up to the null spines).  Checking
    it at the SET level -- not merely that the two have equal measure, which the
    Lambda-sum already gives -- is what tells the next agent the lemma is true
    before they invest in proving it.

    Points within `skin` of the triangle's boundary or of a spine (the segments
    from the circumcentre to the vertices) are skipped: those are exactly the
    null exceptional set, where open-vs-closed disagreement is expected and
    carries no information.
    """
    skin = mpf("1e-6")
    tA, tB, tC = t, t + 2 * g, t + 2 * g + 2 * a
    spines = [tA, tB, tC]
    bad = 0
    checked = 0
    for i in range(1, n):
        phi = -pi + 2 * pi * mpf(i) / n
        # skip rays that graze a spine direction
        if any(abs(((phi - s + pi) % (2 * pi)) - pi) < skin * 1000 for s in spines):
            continue
        for j in range(1, n):
            r = R * mpf(j) / n
            w = (r * cos(phi), r * sin(phi))
            inW = in_milnor_wedges(R, t, a, b, g, w, tol=skin)
            inT = in_triangle(R, t, a, b, g, w, tol=skin)
            # skip the boundary skin, where open/closed disagreement is expected
            if in_milnor_wedges(R, t, a, b, g, w, tol=-skin) != inW:
                continue
            if in_triangle(R, t, a, b, g, w, tol=-skin) != inT:
                continue
            checked += 1
            if inW != inT:
                bad += 1
    return bad, checked


def main() -> int:
    t0 = time.time()
    assertions = []
    R = mpf("1.3")                                   # != 1 on purpose

    # (0) control: the wedge value, now Lean-proved (H4-5b)
    for psi in WEDGES:
        got = wedge_base_integral(mpf("1.7"), psi)
        want = Lob(psi)
        assertions.append({
            "name": f"wedge_value_psi_{float(psi):.5f}",
            "computed": mp.nstr(got, 20),
            "expected": mp.nstr(want, 20),
            "passed": bool(abs(got - want) <= TOL),
            "tolerance": f"{float(TOL):.0e}",  # string: a bare float64 here trips the raw-float64 ratchet
            "source": "CONTROL (regression on the probe's own quadrature): the "
                      "isoceles wedge of half-angle psi integrates to Lambda(psi). "
                      "PROVED in Lean as hypVolume_chimney_wedge (H4-5b).",
        })

    # (1) the acute case -- Milnor's stated hypothesis
    for (a, b, g) in ACUTE:
        got = triangle_base_integral(R, a, b, g)
        want = Lob(a) + Lob(b) + Lob(g)
        assertions.append({
            "name": f"acute_{float(a):.3f}_{float(b):.3f}_{float(g):.3f}",
            "computed": mp.nstr(got, 20),
            "expected": mp.nstr(want, 20),
            "passed": bool(abs(got - want) <= TOL),
            "tolerance": f"{float(TOL):.0e}",  # string: a bare float64 here trips the raw-float64 ratchet
            "source": "ACUTE (Milnor's stated hypothesis): base integral over the "
                      "inscribed triangle vs Lambda(a)+Lambda(b)+Lambda(g).",
        })

    # (2) the obtuse case -- THE POINT OF THE PROBE
    for (a, b, g) in OBTUSE:
        got = triangle_base_integral(R, a, b, g)
        want = Lob(a) + Lob(b) + Lob(g)
        assertions.append({
            "name": f"obtuse_{float(a):.3f}_{float(b):.3f}_{float(g):.3f}",
            "computed": mp.nstr(got, 20),
            "expected": mp.nstr(want, 20),
            "passed": bool(abs(got - want) <= TOL),
            "tolerance": f"{float(TOL):.0e}",  # string: a bare float64 here trips the raw-float64 ratchet
            "source": "OBTUSE / RIGHT (circumcentre OUTSIDE the triangle, where "
                      "Milnor's subdivision needs a signed piece): the IDENTITY "
                      "still holds. Scope-(a): the argument degenerates, not the "
                      "statement.",
        })

    # (3) the ONE step of H4-5c-ii still unproved: milnorWedges = the triangle.
    #     Set-level, not measure-level -- see wedges_vs_triangle_mismatches.
    for (a, b, g) in ACUTE:
        bad, checked = wedges_vs_triangle_mismatches(R, mpf("0.37"), a, b, g)
        assertions.append({
            "name": f"wedges_eq_triangle_{float(a):.3f}_{float(b):.3f}_{float(g):.3f}",
            "computed": str(bad),
            "expected": "0",
            "passed": bool(bad == 0 and checked > 1000),
            "tolerance": "0",
            "source": f"SET-LEVEL check of the one remaining H4-5c-ii step: "
                      f"membership in milnorWedges vs membership in the open "
                      f"inscribed triangle, over {checked} interior sample "
                      f"points (boundary/spine skin excluded). 0 mismatches = "
                      f"the unproved Lean lemma is TRUE, worth proving.",
        })

    all_passed = all(a["passed"] for a in assertions)

    import mpmath
    payload = {
        "assertions": assertions,
        "allPassed": all_passed,
        "computation": WITNESS_NAME,
        "scriptFile": HERE.name,
        "precisionMetadata": {
            "compute_dps": COMPUTE_DPS,
            "output_dps": 20,
            "guard_digits": 10,
            "truncation_bound": f"{float(TOL):.0e}",
        },
        "verdict": (
            "The Lambda-sum identity holds for OBTUSE and RIGHT inscribed "
            "triangles as well as acute ones. Milnor's 'if all three angles are "
            "acute' restricts his SUBDIVISION ARGUMENT (the circumcentre leaves "
            "the triangle, so one wedge must enter with a minus sign), NOT the "
            "identity. Scope-(a): a statement about a proof route. H4-5's target "
            "statement is uniform in the three angles; what the obtuse case needs "
            "is a SIGNED assembly of the same wedges, not a different theorem."
        ),
        "wiredTo": None,
        "notes": (
            "No free parameter; nothing fitted; touches no production. R = 1.3 "
            "(!= 1) so spurious R-dependence would surface. The base integral is "
            "R-independent by H2 dilation invariance, and the wedge control "
            "uses R = 1.7 to exercise that. No q0 anywhere: this is pure "
            "hyperbolic geometry, so the muon/proton anchor question does not "
            "arise."
        ),
    }
    # Provenance via WitnessBuilder so the witness does not land as
    # PROV_MISSING in the provenance audit -- check-sidecars P30.
    #
    # `stamp_staleness_metadata`, NOT `wrap_legacy().save()`: this payload
    # carries a flat `assertions`/`allPassed` pair, and wrap_legacy builds its
    # own (empty) assertion list, which silently replaces it -- all 20
    # assertions vanish from the emitted witness while every other key survives,
    # so the file still looks well-formed. That is the split the P30 message
    # means by "(assertion-free payloads)" vs "(payloads carrying a flat
    # 'assertions'/'allPassed')".
    payload["durationMs"] = int((time.time() - t0) * 1000)
    WitnessBuilder.stamp_staleness_metadata(
        payload,
        script_path=HERE,
        engine="mpmath",
        engine_version=f"mpmath {mpmath.__version__}",
    )
    payload["environment"] = {
        "python": platform.python_version(),
        "mpmath": mpmath.__version__,
        "platform": platform.platform(),
    }
    out_path = HERE.parent / f"{WITNESS_NAME}.witness.json"
    out_path.write_text(json.dumps(payload, indent=2) + "\n")

    print(f"assertions: {sum(a['passed'] for a in assertions)}/{len(assertions)} passed")
    for a in assertions:
        flag = "ok  " if a["passed"] else "FAIL"
        print(f"  {flag} {a['name']:<44} {a['computed']}")
    print(f"witness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
