#!/usr/bin/env python3
"""CERTIFICATE PROBE for H4-5c-ii(b) — the TILING.

`qou-w3eg` H4-5c-ii(a) (PR #4864) proved the Lambda-sum on the UNION OF THREE
WEDGES and left exactly one step open: that the union IS the inscribed
triangle.  This probe certifies, numerically and *before* the Lean was written,
every algebraic fact the Lean proof of that step rests on, so that the Lean is
transcription rather than search.

WHAT THE LEAN PROOF NEEDS, AND WHAT IS CHECKED HERE.

  (A) The SUBSET direction is one linear identity, not a convexity argument.
      For a wedge at (theta, psi) tested against the chord half-plane of its
      neighbour at (theta+psi+psi', psi'):

          cos(psi) * F  =  sin(psi+psi') * G2  +  cos(psi') * G3

      with  F  = R cos(psi') - w.u_{theta+psi+psi'}   (the goal),
            G2 = -(w.v_{theta+psi})                    (shared-edge slack),
            G3 = R cos(psi) - w.u_theta                (own-chord slack),
            u_phi = (cos phi, sin phi),  v_phi = (-sin phi, cos phi).
      Both coefficients are positive exactly when 0 < psi+psi' < pi.  Checked
      in both orientations (`next`, and the mirror `prev`).
      -> Lean: `wedgeAt_lt_chord_next` / `wedgeAt_lt_chord_prev`.

  (B) The COVERING direction is a sign relation, not a covering computation.
      With x = w.v_t, y = w.v_{t+2g}, z = w.v_{t+2g+2a}:

          sin(2a) * x + sin(2b) * y + sin(2g) * z = 0

      All three coefficients are positive for acute angles, so (x,y,z) is never
      all-positive or all-negative -- which is the whole covering argument.
      -> Lean: `perp_sign_relation`.

  (C) The half-plane triple really is THE triangle with the three named
      vertices.  `inscribedTriangle` is DEFINED as an intersection of three
      chord half-planes, which is where one could quietly assume the geometry.
      The anchor is the incidence pattern: each circle point lies ON exactly
      two of the three chord lines and STRICTLY INSIDE the third half-plane,
      with the predicted gap 2R sin sin.
      -> Lean: `inscribedTriangle_vertex_incidence`.

  (D) The tiling itself, at the SET level: `milnorWedges` membership and
      `inscribedTriangle` membership agree at interior points off the three
      edge lines.  Evaluated independently -- the wedges by the Lean
      definition's own inequalities, the triangle by its three half-plane
      tests -- so agreement is evidence and not a tautology.
      -> Lean: `milnorWedges_ae_eq_inscribedTriangle`.

NOTHING IS FITTED and there is no free parameter.  The parameter grids are
deterministic rationals (no RNG, no float64 literals), R is taken != 1 so that
spurious R-dependence would surface, and t != 0 so that a dropped rotation
would surface.  No q0 appears anywhere: this is pure hyperbolic geometry, so
the muon/proton anchor question does not arise.

SCOPE.  This is numerical evidence for algebraic identities that are now PROVED
in Lean (`QOU/Archimedean/OrthoschemeTiling.lean`, sorry-free); it is a
regression check on the transcription, not the proof, and it wires to nothing.

  -- Ref: [milnor1982] Appendix (the circumcentre subdivision)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [manuscript] beans qou-w3eg (H4-5c-ii(b)), qou-5gai (H4)
"""
from __future__ import annotations

import json
import platform
import sys
import time
from pathlib import Path

import mpmath
from mpmath import mp, mpf, sin, cos, tan, pi

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parent / "substrate"))

from witness_base import WitnessBuilder  # noqa: E402

WITNESS_NAME = "milnor-tiling-certificate-probe"
COMPUTE_DPS = 50
mp.dps = COMPUTE_DPS

# Exact tolerance: identities are exact, so the only error is round-off at
# `COMPUTE_DPS` digits.  A generous margin above it still catches a wrong sign
# or a dropped term by many orders of magnitude.
TOL = mpf(10) ** (-(COMPUTE_DPS - 8))

# R != 1 and t != 0 deliberately (see module docstring).
R_TEST = mpf(13) / mpf(10)
T_TEST = mpf(7) / mpf(10)


# --------------------------------------------------------------------------
# frame helpers -- u_phi = (cos phi, sin phi),  v_phi = (-sin phi, cos phi)
# --------------------------------------------------------------------------
def dot_u(w, phi):
    return w[0] * cos(phi) + w[1] * sin(phi)


def dot_v(w, phi):
    return -(w[0] * sin(phi)) + w[1] * cos(phi)


def in_wedge_at(w, R, theta, psi):
    """Membership by the Lean definition `wedgeAt` -- verbatim."""
    p = dot_u(w, theta)
    q = dot_v(w, theta)
    return p < R * cos(psi) and abs(q) < p * tan(psi)


def in_milnor_wedges(w, R, t, a, b, g):
    """`milnorWedges R t a b g`, verbatim."""
    return (in_wedge_at(w, R, t + g, g)
            or in_wedge_at(w, R, t + 2 * g + a, a)
            or in_wedge_at(w, R, t + 2 * g + 2 * a + b, b))


def chord_slacks(w, R, t, a, b, g):
    """The three `chordHalfplane` slacks; all > 0 iff w is in the triangle."""
    return (R * cos(g) - dot_u(w, t + g),
            R * cos(a) - dot_u(w, t + 2 * g + a),
            R * cos(b) - dot_u(w, t + 2 * g + 2 * a + b))


def in_inscribed_triangle(w, R, t, a, b, g):
    return all(s > 0 for s in chord_slacks(w, R, t, a, b, g))


# --------------------------------------------------------------------------
# deterministic parameter grids (no RNG, no float64)
# --------------------------------------------------------------------------
def acute_triples():
    """(alpha, beta, gamma), all in (0, pi/2), summing to pi -- rationals*pi."""
    out = []
    for i in range(4, 15):
        for j in range(4, 15):
            a = pi * mpf(i) / mpf(32)
            g = pi * mpf(j) / mpf(32)
            b = pi - a - g
            if mpf(0) < b < pi / 2 and a < pi / 2 and g < pi / 2:
                out.append((a, b, g))
    return out


def angle_pairs():
    """(psi, psi') pairs strictly inside (0, pi/2)."""
    return [(pi * mpf(i) / mpf(24), pi * mpf(j) / mpf(24))
            for i in range(1, 12) for j in range(1, 12)]


def sample_points():
    """A deterministic spread of plane points, including large ones."""
    pts = []
    for i in range(-7, 8):
        for j in range(-7, 8):
            pts.append((mpf(i) / mpf(3), mpf(j) / mpf(3)))
    return pts


# --------------------------------------------------------------------------
# (A) the subset identity, both orientations
# --------------------------------------------------------------------------
def check_identity_next():
    worst = mpf(0)
    for psi, psip in angle_pairs():
        for theta in (mpf(0), T_TEST, -pi / mpf(3), pi * mpf(5) / mpf(4)):
            for w in sample_points()[::7]:
                F = R_TEST * cos(psip) - dot_u(w, theta + psi + psip)
                G2 = -dot_v(w, theta + psi)
                G3 = R_TEST * cos(psi) - dot_u(w, theta)
                resid = cos(psi) * F - (sin(psi + psip) * G2 + cos(psip) * G3)
                worst = max(worst, abs(resid))
    return worst


def check_identity_prev():
    worst = mpf(0)
    for psi, psip in angle_pairs():
        for theta in (mpf(0), T_TEST, -pi / mpf(3), pi * mpf(5) / mpf(4)):
            for w in sample_points()[::7]:
                F = R_TEST * cos(psip) - dot_u(w, theta - psi - psip)
                G2 = dot_v(w, theta - psi)
                G3 = R_TEST * cos(psi) - dot_u(w, theta)
                resid = cos(psi) * F - (sin(psi + psip) * G2 + cos(psip) * G3)
                worst = max(worst, abs(resid))
    return worst


# --------------------------------------------------------------------------
# (B) the sign relation, and the exclusion it buys
# --------------------------------------------------------------------------
def check_sign_relation():
    worst = mpf(0)
    for a, b, g in acute_triples():
        for w in sample_points()[::5]:
            x = dot_v(w, T_TEST)
            y = dot_v(w, T_TEST + 2 * g)
            z = dot_v(w, T_TEST + 2 * g + 2 * a)
            resid = sin(2 * a) * x + sin(2 * b) * y + sin(2 * g) * z
            worst = max(worst, abs(resid))
    return worst


def count_all_same_sign():
    """The relation forbids (+,+,+) and (-,-,-); count violations."""
    bad = 0
    for a, b, g in acute_triples():
        for w in sample_points():
            x = dot_v(w, T_TEST)
            y = dot_v(w, T_TEST + 2 * g)
            z = dot_v(w, T_TEST + 2 * g + 2 * a)
            if (x > 0 and y > 0 and z > 0) or (x < 0 and y < 0 and z < 0):
                bad += 1
    return bad


# --------------------------------------------------------------------------
# (C) vertex incidence -- the anchor on the DEFINITION
# --------------------------------------------------------------------------
def check_vertex_incidence():
    """Each vertex on exactly two chord lines, strictly inside the third.

    Returns (max |on-line residual|, min strict gap, max |gap - predicted|)
    where predicted = 2 R sin(.) sin(.) from the product-to-sum identity that
    the Lean proof (`cos_sub_cos_two_mul_add`) uses.
    """
    worst_on = mpf(0)
    min_gap = None
    worst_pred = mpf(0)
    for a, b, g in acute_triples():
        R, t = R_TEST, T_TEST
        verts = [(t, 0), (t + 2 * g, 1), (t + 2 * g + 2 * a, 2)]
        # side i is the chord line; vertices lying on it:
        on = {0: {0, 1}, 1: {1, 2}, 2: {2, 0}}
        lines = [(t + g, g), (t + 2 * g + a, a), (t + 2 * g + 2 * a + b, b)]
        # opposite vertex -> predicted gap
        pred = {0: 2 * R * sin(a) * sin(b),     # vertex 2 vs side 0
                1: 2 * R * sin(b) * sin(g),     # vertex 0 vs side 1
                2: 2 * R * sin(g) * sin(a)}     # vertex 1 vs side 2
        for i, (th, ps) in enumerate(lines):
            for ang, vi in verts:
                P = (R * cos(ang), R * sin(ang))
                slack = R * cos(ps) - dot_u(P, th)
                if vi in on[i]:
                    worst_on = max(worst_on, abs(slack))
                else:
                    min_gap = slack if min_gap is None else min(min_gap, slack)
                    worst_pred = max(worst_pred, abs(slack - pred[i]))
    return worst_on, min_gap, worst_pred


# --------------------------------------------------------------------------
# (D) the tiling, at the SET level
# --------------------------------------------------------------------------
def check_set_level_tiling():
    """Independent membership tests must agree off the three edge lines."""
    tested = 0
    mismatches = 0
    skin = mpf(10) ** (-20)
    R, t = R_TEST, T_TEST
    for a, b, g in acute_triples()[::3]:
        for w in sample_points():
            # stay off the three edge lines and the three chord lines
            edges = [abs(dot_v(w, t)), abs(dot_v(w, t + 2 * g)),
                     abs(dot_v(w, t + 2 * g + 2 * a))]
            if min(edges) < skin:
                continue
            if min(abs(s) for s in chord_slacks(w, R, t, a, b, g)) < skin:
                continue
            tested += 1
            if in_milnor_wedges(w, R, t, a, b, g) != in_inscribed_triangle(
                    w, R, t, a, b, g):
                mismatches += 1
    return tested, mismatches


def main() -> int:
    t0 = time.time()
    assertions = []

    def record(name, computed, passed, detail):
        assertions.append({"name": name, "computed": str(computed),
                           "passed": bool(passed), "detail": detail})

    rn = check_identity_next()
    record("subset_identity_next_residual", mp.nstr(rn, 8), rn < TOL,
           "cos(psi)F = sin(psi+psi')G2 + cos(psi')G3, next orientation "
           "(Lean: wedgeAt_lt_chord_next)")

    rp = check_identity_prev()
    record("subset_identity_prev_residual", mp.nstr(rp, 8), rp < TOL,
           "same identity, mirror orientation (Lean: wedgeAt_lt_chord_prev)")

    rs = check_sign_relation()
    record("sign_relation_residual", mp.nstr(rs, 8), rs < TOL,
           "sin(2a)x + sin(2b)y + sin(2g)z = 0 (Lean: perp_sign_relation)")

    bad = count_all_same_sign()
    record("all_same_sign_violations", bad, bad == 0,
           "the relation forbids (+,+,+) and (-,-,-); this is the covering "
           "argument (Lean: inscribedTriangle_subset_milnorWedges_of_ne)")

    won, gap, wpred = check_vertex_incidence()
    record("vertex_on_line_residual", mp.nstr(won, 8), won < TOL,
           "each vertex lies ON its two chord lines")
    record("vertex_strict_min_gap", mp.nstr(gap, 8), gap > 0,
           "each vertex lies STRICTLY inside the third half-plane")
    record("vertex_gap_matches_2Rsinsin", mp.nstr(wpred, 8), wpred < TOL,
           "the gap equals the predicted 2 R sin sin "
           "(Lean: cos_sub_cos_two_mul_add, inscribedTriangle_vertex_incidence)")

    tested, mism = check_set_level_tiling()
    record("tiling_points_tested", tested, tested > 1000,
           "interior points, off the edge and chord lines")
    record("tiling_set_level_mismatches", mism, mism == 0,
           "milnorWedges membership == inscribedTriangle membership "
           "(Lean: milnorWedges_ae_eq_inscribedTriangle)")

    all_passed = all(a["passed"] for a in assertions)

    payload = {
        "name": WITNESS_NAME,
        "description": (
            "Certificate probe for H4-5c-ii(b): every algebraic fact the Lean "
            "tiling proof rests on -- the two subset identities, the sign "
            "relation and the all-same-sign exclusion it buys, the vertex "
            "incidence anchoring the triangle's definition, and the set-level "
            "tiling itself."
        ),
        "assertions": assertions,
        "allPassed": all_passed,
        "parameters": {
            "R": str(R_TEST),
            "t": str(T_TEST),
            "acute_triples": len(acute_triples()),
            "angle_pairs": len(angle_pairs()),
            "sample_points": len(sample_points()),
        },
        "precisionMetadata": {
            "compute_dps": COMPUTE_DPS,
            "output_dps": 20,
            "guard_digits": 8,
            "truncation_bound": f"{float(TOL):.0e}",
        },
        "verdict": (
            "Every ingredient of the H4-5c-ii(b) tiling proof checks. The "
            "subset direction is a single positive-coefficient linear identity "
            "in both orientations; the covering direction follows from one sign "
            "relation whose positive coefficients forbid the two sign patterns "
            "that would leave a triangle point in no sector; the three circle "
            "points sit on the chord lines in the incidence pattern that pins "
            "the half-plane definition to the intended triangle, with the "
            "predicted 2 R sin sin gap; and the two memberships agree at the "
            "SET level off the null lines. All of these are now PROVED in Lean "
            "(OrthoschemeTiling.lean, sorry-free), so this is a regression "
            "check on the transcription rather than evidence for an open claim."
        ),
        "wiredTo": None,
        "notes": (
            "No free parameter; nothing fitted; touches no production. "
            "Deterministic rational parameter grids -- no RNG and no float64 "
            "literals. R = 13/10 != 1 and t = 7/10 != 0 so that a spurious "
            "R-dependence or a dropped rotation would surface. No q0 anywhere: "
            "pure hyperbolic geometry, so the muon/proton anchor question does "
            "not arise."
        ),
    }
    # Provenance via WitnessBuilder so the witness does not land as
    # PROV_MISSING -- check-sidecars P30.
    #
    # `stamp_staleness_metadata`, NOT `wrap_legacy().save()`: this payload
    # carries a flat `assertions`/`allPassed` pair, and wrap_legacy builds its
    # own (empty) assertion list which silently REPLACES it -- every assertion
    # vanishes while the rest of the file still looks well-formed.  That trap
    # was found and recorded by the H4-5c-ii(a) session; do not "simplify" this
    # back to wrap_legacy.
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
        print(f"  {flag} {a['name']:<36} {a['computed']}")
    print(f"witness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
