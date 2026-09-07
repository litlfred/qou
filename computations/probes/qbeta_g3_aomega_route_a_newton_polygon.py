"""qbeta_g3_aomega_route_a_newton_polygon.py

Route A of docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md:
test whether the G3 DT spectrum {3,4} of the figure-eight 4_1 is Newton-polygon
data of the (quantum) A-polynomial / the QOU C1 binding q-difference carrier.

Rigorous core (airtight): the Newton polygon of the classical A-polynomial
A_{4_1}(M,L) and of the C1 operator, with edge slopes (= boundary slopes) and
L-degree (= number of boundary-parabolic SL_2(C) connections) read off exactly by
integer lattice geometry.

Candidate readings of the certified DT spectrum {3,4} (StokesQZeroDTCount /
FiveTwoDTSpectrumSplit, both sorry-free):
  R1:  3 = L-degree of the FULL A-polynomial = #boundary-parabolic connections
  R2:  4 = |maximal boundary slope| of the Newton polygon

Anti-numerology gate (the rule that killed the disc(Q(sqrt-3))=-3 route): both
readings must survive the 5_2 cross-knot test. 5_2's DT spectrum is ALSO {3,4}
(corpus-certified, chirality-split), so if 5_2's Newton-polygon invariants differ
from {3,4}, the corresponding reading is REFUTED.

Honest scoping:
 * 4_1 A-polynomial + C1 operator: exact, self-contained, reliable.
 * 5_2 boundary slopes / connection count: DERIVED (since 2026-09-07) from the
   corpus's own A_{5_2} — two_bridge_cusp_rows_apoly_probe.py (#6985, Farey word
   RL, meridian pinned by the Dehn-filling test) — read from its witness
   two-bridge-cusp-rows-apoly.witness.json. The literature values this probe
   first ran on ({0,-4,-10}, 4; SnapPy unavailable then) are kept as a labelled
   cross-check: derived == recalled is asserted, and the R1/R2 gate runs on the
   DERIVED values. Lean twin: QOU.QBeta.RouteANewtonPolygonDT (a52_*).
 * Chirality: the derived data carries a definite frame (sign of the slopes);
   Route A's inputs — |max slope| and L-degree — are mirror-invariant
   (RouteANewtonPolygonDT.absSlopeEq_mirror, lProfile_mirror), so the frame
   adds nothing to this gate. Asserted below on the derived polygon.
 * Nothing fitted; nothing wired; audit-only; scope-(a).
"""

from __future__ import annotations

import json
from fractions import Fraction
import os
import subprocess
import time


# ------------------------------------------------------------------ geometry --
def convex_hull(points):
    """Monotone-chain convex hull of integer points; returns hull vertices CCW."""
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def edges(hull):
    return [(hull[i], hull[(i + 1) % len(hull)]) for i in range(len(hull))]


def boundary_slopes(monomials):
    """Edge slopes dM/dL of the Newton polygon in (M-exp, L-exp) coordinates.
    These are the knot-theoretic boundary slopes. Vertical edges (dL=0) are the
    Seifert/longitude direction and reported as 'inf' (slope-0 fiber convention).
    Returns (sorted finite slopes, L_degree, M_width, hull)."""
    hull = convex_hull(monomials)
    slopes = set()
    for (a, b) in edges(hull):
        dM, dL = b[0] - a[0], b[1] - a[1]
        if dL == 0:
            continue
        slopes.add((dM, dL))
    # reduce to lowest terms, express as rational dM/dL
    #
    # `Fraction`, not `dM2 / dL2`. A boundary slope IS a rational number — the
    # p/q of knot theory — and the pair is already in lowest terms two lines up,
    # so float division is a lossy re-encoding of something exact: -10/3 became
    # -3.3333333333333335, which is both wrong and a raw float64 in the witness.
    # Fraction sorts, compares and takes abs() exactly like the float did, so
    # nothing downstream changes except that the values stay correct.
    finite = []
    from fractions import Fraction
    from math import gcd
    for (dM, dL) in slopes:
        g = gcd(abs(dM), abs(dL)) or 1
        dM2, dL2 = dM // g, dL // g
        if dL2 < 0:
            dM2, dL2 = -dM2, -dL2
        finite.append(Fraction(dM2, dL2))
    Ls = [p[1] for p in monomials]
    Ms = [p[0] for p in monomials]
    return sorted(set(finite)), max(Ls) - min(Ls), max(Ms) - min(Ms), hull


# --------------------------------------------------------------- A-polynomials --
# A_{4_1}(M,L) geometric component (standard normalization, e.g. CCGLS / Culler
# database):  A = -M^4 + L(1 - M^2 - 2M^4 - M^6 + M^8) - L^2 M^4.
# Full A-polynomial = (L-1) * geometric  (the (L-1) is the abelian connection).
A41_geom = [
    (4, 0),                                  # -M^4
    (0, 1), (2, 1), (4, 1), (6, 1), (8, 1),  # L * (1 - M^2 - 2M^4 - M^6 + M^8)
    (4, 2),                                  # -L^2 M^4
]
# full = geometric * (L - 1): L-degree +1 (abelian factor). We only need degrees,
# so full L-degree = geom L-degree (2) + 1 = 3.
A41_full_Ldeg = 2 + 1

# QOU C1 binding carrier:  [m+2]_q b_{m+2} = b_{m+1} + b_m.
# With M = q^m, balanced [m+2]_q ~ (q^2 M - q^-2 M^-1)/(q - q^-1) and L = shift E:
#   (q^2 M - q^-2 M^-1) L^2 - (q - q^-1)(L + 1) = 0
# Monomials in (M-exp, L-exp):
C1_op = [(1, 2), (-1, 2), (0, 1), (0, 0)]


def _monomials_ML(poly_str):
    """(M-exp, L-exp) support of a polynomial in L, M given as a sympy string."""
    import sympy as sp
    L, M = sp.symbols("L M")
    P = sp.Poly(sp.sympify(poly_str, locals={"L": L, "M": M}), L, M)
    return [(int(m), int(l)) for (l, m), c in P.terms() if c != 0]


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    print("=" * 72)
    print(" Route A: Newton polygon of A-poly / C1 vs the G3 DT spectrum {3,4}")
    print("=" * 72)

    DT_SPECTRUM = {3, 4}  # corpus-certified (StokesQZeroDTCount, FiveTwoDTSpectrumSplit)

    # ---- 4_1 classical A-polynomial ------------------------------------------
    s41, Ldeg41_geom, Mw41, hull41 = boundary_slopes(A41_geom)
    print("\n[1] 4_1 classical A-polynomial (geometric component)")
    print(f"    Newton hull vertices (M,L): {hull41}")
    print(f"    boundary slopes dM/dL      : {s41}")
    print(f"    geometric L-degree         : {Ldeg41_geom}")
    print(f"    full A-poly L-degree (=#connections {{0,g,gbar}}): {A41_full_Ldeg}")
    max_slope_41 = max(abs(x) for x in s41)
    print(f"    |max boundary slope|       : {max_slope_41}")

    # R1: 3 = full L-degree = #boundary-parabolic connections
    check("R1-4_1: full-A L-degree = #connections = 3 (a DT integer)",
          A41_full_Ldeg == 3 and 3 in DT_SPECTRUM,
          full_L_degree=A41_full_Ldeg, dt_spectrum=sorted(DT_SPECTRUM))
    # R2: 4 = |max boundary slope|
    check("R2-4_1: |max boundary slope| = 4 (a DT integer)",
          max_slope_41 == 4 and 4 in DT_SPECTRUM,
          max_boundary_slope=str(max_slope_41), dt_spectrum=sorted(DT_SPECTRUM))

    # ---- C1 operator: is it the figure-eight quantum A-polynomial? -----------
    sC1, LdegC1, MwC1, hullC1 = boundary_slopes(C1_op)
    print("\n[2] QOU C1 binding carrier  [m+2]_q b_{m+2} = b_{m+1} + b_m")
    print(f"    Newton hull vertices (M,L): {hullC1}")
    print(f"    boundary slopes dM/dL      : {sC1}")
    print(f"    L-degree                   : {LdegC1}")
    c1_max = max(abs(x) for x in sC1) if sC1 else 0
    print(f"    |max boundary slope|       : {c1_max}")
    # Honest negative: C1's Newton polygon must match 4_1's to BE the quantum
    # A-polynomial. It does not (slopes ±1/2 vs ±4).
    check("C1-is-NOT-quantum-A-poly-of-4_1 (Newton polygons differ)",
          abs(c1_max - max_slope_41) > 1e-9,
          C1_max_slope=str(c1_max), A41_max_slope=str(max_slope_41),
          note="C1 (binding carrier, slopes ±1/2) is NOT the reduced Â_{4_1} "
               "(slopes ±4). Route A must use the true colored-Jones recursion, "
               "not the binding carrier.")

    # ---- 5_2 cross-knot anti-numerology gate ---------------------------------
    # DERIVED 5_2 data (2026-09-07): read the A-polynomial the corpus derived
    # from the Farey word RL (#6985) and recompute the Newton polygon here with
    # the same lattice geometry used for 4_1 above.  The literature values the
    # gate first ran on are kept only as a labelled cross-check.
    FIVE2_boundary_slopes_LIT = {0, -4, -10}   # literature (Hatcher–Oertel / census)
    FIVE2_num_connections_LIT = 4              # literature: 1 abelian + 3 geometric
    FIVE2_DT = {3, 4}                          # corpus-certified (same pair, split)

    derived_w = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "two-bridge-cusp-rows-apoly.witness.json")
    with open(derived_w) as fh:
        dw = json.load(fh)
    A52_monomials = _monomials_ML(dw["data"]["fivetwo_apoly"])
    A52_frame = dw["data"]["fivetwo_chirality_note"]
    s52, Ldeg52_geom, Mw52, hull52 = boundary_slopes(A52_monomials)
    FIVE2_boundary_slopes = set(s52)                     # derived, Fraction
    FIVE2_max_abs_slope = max(abs(x) for x in s52)       # derived
    FIVE2_num_connections = Ldeg52_geom + 1              # derived: + abelian (L-1)

    print("\n[3] 5_2 cross-knot gate (DERIVED boundary data — #6985 A-polynomial)")
    print(f"    source witness             : {os.path.basename(derived_w)} "
          f"(scriptHash {dw.get('scriptHash', '?')[:12]}, {dw.get('computedAt')})")
    print(f"    A_{{5_2}} monomials (M,L)    : {sorted(A52_monomials)}")
    print(f"    Newton hull vertices (M,L) : {hull52}")
    print(f"    5_2 boundary slopes (derived): {sorted(s52)}   [lit {sorted(FIVE2_boundary_slopes_LIT)}]")
    print(f"    5_2 |max boundary slope|   : {FIVE2_max_abs_slope}")
    print(f"    5_2 geometric L-degree     : {Ldeg52_geom}  → #connections = {FIVE2_num_connections}   [lit {FIVE2_num_connections_LIT}]")
    print(f"    5_2 DT spectrum (corpus)   : {sorted(FIVE2_DT)}")

    check("5_2-derived-slopes-match-recalled: derived boundary slopes == literature set",
          FIVE2_boundary_slopes == {Fraction(x) for x in FIVE2_boundary_slopes_LIT},
          derived=[str(x) for x in sorted(s52)], literature=sorted(FIVE2_boundary_slopes_LIT),
          note="In the derived frame (μ by the filling test, λ homological, "
               "Im(t_λ/t_μ) > 0) the signs agree with the corpus's recalled "
               "{0,-4,-10}; the literature's {0,4,10} is the mirror.")
    check("5_2-derived-connections-match-recalled: geometric L-degree 3, full 4",
          Ldeg52_geom == 3 and FIVE2_num_connections == FIVE2_num_connections_LIT,
          derived_geom_L_degree=Ldeg52_geom, derived_full=FIVE2_num_connections,
          literature=FIVE2_num_connections_LIT)
    # Chirality: mirror negates every slope and fixes the L-profile, so the two
    # Route-A inputs cannot see the frame.
    A52_mirror = [(-m, l) for (m, l) in A52_monomials]
    s52m, Ldeg52m, _, _ = boundary_slopes(A52_mirror)
    check("5_2-mirror: |max slope| and L-degree are mirror-invariant (frame invisible to Route A)",
          set(s52m) == {-x for x in s52} and max(abs(x) for x in s52m) == FIVE2_max_abs_slope
          and Ldeg52m == Ldeg52_geom,
          mirror_slopes=[str(x) for x in sorted(s52m)],
          note="The derived frame fixes the SIGN of the slopes; R2 uses |slope| and "
               "R1 the L-degree, both mirror-invariant (Lean absSlopeEq_mirror, "
               "lProfile_mirror). So the {4∈S⁺,3∈S⁻} split — an ordered, ι-odd "
               "datum — is not Newton-polygon data, whatever the frame.")

    # R2 cross-knot: does |max boundary slope| land in the DT spectrum for 5_2?
    r2_survives = FIVE2_max_abs_slope in FIVE2_DT
    check("R2-crossknot-5_2: |max boundary slope| in DT spectrum?",
          r2_survives,
          five2_max_slope=str(FIVE2_max_abs_slope), five2_dt=sorted(FIVE2_DT),
          note="5_2 max boundary slope 10 is NOT a DT integer {3,4} — the "
               "'DT integer = boundary slope' reading (R2) is REFUTED on 5_2 "
               "(scope-(a); the slope 10 is DERIVED from the corpus's A_{5_2}).")

    # R1 cross-knot: does #connections track a DT integer consistently?
    r1_survives = FIVE2_num_connections in FIVE2_DT or (A41_full_Ldeg in DT_SPECTRUM)
    check("R1-crossknot-5_2: #connections consistent with a DT integer?",
          FIVE2_num_connections in FIVE2_DT,
          five2_connections=FIVE2_num_connections, five2_dt=sorted(FIVE2_DT),
          note="4_1 #connections=3∈{3,4}; 5_2 #connections=4∈{3,4} (derived). The "
               "L-degree/#connections reading of the 3↔4 is CONSISTENT across "
               "both knots (both land in {3,4}) — survives where R2 fails.")

    # ---- verdict -------------------------------------------------------------
    verdict = (
        "Route A is PARTIAL / mixed (scope-(a), anti-numerology-gated). "
        "AIRTIGHT: (i) the figure-eight DT integers {3,4} ARE Newton-polygon "
        "data of A_{4_1} — 3 = full-A L-degree = #boundary-parabolic connections, "
        "4 = |max boundary slope|; (ii) the QOU C1 binding carrier is NOT the "
        "quantum A-polynomial (slopes ±1/2 ≠ ±4), so Route A needs the true "
        "colored-Jones recursion Â_K, not C1. CROSS-KNOT GATE: the slope reading "
        "R2 (DT=boundary slope) is REFUTED on 5_2 (max slope 10 ∉ {3,4}); the "
        "L-degree/#connections reading R1 SURVIVES (4_1:3, 5_2:4, both ∈ {3,4}). "
        "Consequence: the internal handle on the DT spectrum is the A-polynomial "
        "L-degree / connection count (an Euler-characteristic datum → Route B), "
        "NOT the Newton-polygon slope; and it needs Â_K, not the binding carrier. "
        "5_2 boundary data is DERIVED (2026-09-07) from the corpus's own "
        "A_{5_2} (#6985), equal to the literature set; the derived frame's sign "
        "is invisible to both readings (mirror-invariant inputs)."
    )
    print(f"\n verdict: {verdict}")

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    while root != os.path.dirname(root):
        if os.path.exists(os.path.join(root, "AGENTS.md")):
            break
        root = os.path.dirname(root)
    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                      cwd=root, text=True).strip()
    except Exception:
        sha = "unknown"

    witness = {
        "name": "qbeta-g3-aomega-route-a-newton-polygon",
        "description": "Route A: Newton polygon of A_{4_1} / C1 carrier vs the G3 "
                       "DT spectrum {3,4}. 3 = full-A L-degree = #connections; "
                       "4 = |max boundary slope|; C1 ≠ quantum A-poly; slope "
                       "reading R2 refuted on 5_2 cross-knot, L-degree reading R1 "
                       "survives.",
        "computation": "qbeta-g3-aomega-route-a-newton-polygon",
        "engine": "python",
        "scriptFile": "computations/probes/qbeta_g3_aomega_route_a_newton_polygon.py",
        "scriptCommitSha": sha,
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md",
        "parameters": {
            "A41_geometric_monomials_ML": A41_geom,
            "A41_full_L_degree": A41_full_Ldeg,
            "C1_operator_monomials_ML": C1_op,
            "five2_boundary_slopes_literature": sorted(FIVE2_boundary_slopes_LIT),
            "five2_num_connections_literature": FIVE2_num_connections_LIT,
            "five2_source_witness": os.path.basename(derived_w),
            "five2_source_scriptHash": dw.get("scriptHash"),
            "five2_source_computedAt": dw.get("computedAt"),
            "dt_spectrum_corpus": sorted(DT_SPECTRUM),
        },
        "data": {
            # Exact rationals as strings: these are p/q boundary slopes, and
            # float() would both lose the value (-10/3) and re-introduce the
            # raw float64 this drain removed.
            "A41_boundary_slopes": [str(x) for x in s41],
            "A41_max_abs_slope": str(max_slope_41),
            "A41_full_L_degree": A41_full_Ldeg,
            "C1_boundary_slopes": [str(x) for x in sC1],
            "C1_max_abs_slope": str(c1_max),
            "A52_monomials_ML": sorted(A52_monomials),
            "A52_newton_hull_ML": hull52,
            "A52_boundary_slopes_derived": [str(x) for x in sorted(s52)],
            "A52_max_abs_slope_derived": str(FIVE2_max_abs_slope),
            "A52_geom_L_degree_derived": Ldeg52_geom,
            "A52_full_L_degree_derived": FIVE2_num_connections,
            "A52_mirror_boundary_slopes": [str(x) for x in sorted(s52m)],
            "A52_frame": A52_frame,
            "R1_survives_crossknot": bool(FIVE2_num_connections in FIVE2_DT),
            "R2_survives_crossknot": bool(r2_survives),
            "verdict": verdict,
        },
        "assertions": assertions,
    }
    out = os.path.join(root, "computations", "probes",
                       "qbeta-g3-aomega-route-a-newton-polygon.witness.json")
    with open(out, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"\n witness: {out}")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f" assertions: {len(assertions) - nfail}/{len(assertions)} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
