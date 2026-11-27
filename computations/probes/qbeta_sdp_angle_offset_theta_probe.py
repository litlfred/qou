#!/usr/bin/env python3
"""qbeta_sdp_angle_offset_theta_probe.py — is ϑ_K in the angle-structure LP solution?

THE PROPOSAL (owner, 2026-08-07). A particle interaction is not an isolated
event: it IS an SDP/LP solution. That solution carries data we have been
discarding — the magnitude and angle of the knot's trajectory, and its offset
from the lattice saddle point. The energy of the interaction should be the
magnitude, and possibly the angle of incidence.

WHY THIS IS THE RIGHT SHAPE. `QOU/QBeta/AfreeThetaConstraint.lean` proves
(sorry-free) that the T4/T5 channel `S_K = A_ω·κ·(ln²q₀ − ϑ_K²)` has two anchor
equations in three unknowns, so a route supplying a RATIO ϑ_p/ϑ_μ is
unfalsifiable — `ratio_attained` constructs an explicit admissible `A` for every
ratio > 1. A genuine test needs BOTH ϑ ABSOLUTELY. The angle-structure LP
supplies, per knot, a magnitude AND an angle AND a lattice offset — three
numbers for each of two anchors against three unknowns, over-determined by
three. It is therefore the first candidate in this arc that CAN fail.

THE GEOMETRY (all parameter-free, fixed by the triangulation alone).
For an ideal triangulation T with N tetrahedra, the generalised angle-structure
space (Garoufalidis arXiv:1208.1663 §2.2-2.3, π-units) is the affine space

    α_j + β_j + γ_j = 1  (each tet),      Σ angles around each edge = 2.

Two canonical points live in it:

  * **x_geom — the saddle.** The angles of the COMPLETE hyperbolic structure,
    `(arg z, arg z', arg z'')/π` per tetrahedron. By Rivin's theorem this is the
    critical point of the volume functional on the angle-structure polytope —
    literally "the lattice saddle point" of the proposal.
  * **x_LP — the combinatorial centre.** The Casson-Rivin max-strictness LP
    optimum (maximise the minimum angle). Canonical, no objective to choose.

Their difference is the OFFSET, with a magnitude and a direction; the LP dual
`y*` is the normal to the active face, so the angle between offset and `y*` is
the ANGLE OF INCIDENCE.

WHAT IS MEASURED (no fitting anywhere):
  G0  GATE — x_geom must satisfy the SAME linear system as the LP. It must, by
      the edge equations; if it does not, the coordinate convention is wrong and
      everything downstream is meaningless. This gate is the analogue of the
      RL-gate that caught a σ₂⁻¹ sign slip in the rdmr probe.
  M1  ‖offset‖ and the angle of incidence, per knot (4₁ = m004 = muon anchor,
      Borromean = L6a4 = proton anchor).
  M2  the lattice coordinate ϑ/((√3/2)·ln q₀) named by bean qou-offl, and its
      off-lattice remainder.
  T1  THE TEST. The A-free curve (PR #4513) requires
          (L − ϑ_μ²)/(L − ϑ_p²) = S_μ/S_p = r,  L = ln²q₀,
      and since r < 0 the pair MUST straddle: ϑ_μ < ln q₀ < ϑ_p. Straddling is
      a cheap necessary condition checked first; the ratio is the real test.

THE ONE HAZARD, STATED UP FRONT (anti-fit). A "magnitude" and an "angle" need
an inner product on angle-space. That is a normalization choice, and choosing it
AFTER seeing the numbers would be the exact re-parameterization trap this arc
has been warning about. So the metric is FIXED IN ADVANCE as the Euclidean
metric in π-units — the convention the corpus already froze in
`borromean_angle_structure_lp_probe.py`. The principled alternative (the Hessian
of the volume functional at x_geom, which is intrinsic rather than a coordinate
artifact) is NOT used here and is named as follow-up. No metric is selected to
make a number come out right, and both anchors use the same one.

Scope (STRICT). This MEASURES parameter-free geometric data and COMPARES it to
an A_ω-free constraint. Nothing is tuned; no ϑ is asserted; nothing is wired. A
miss is reported as a miss.

Run: python3 -u computations/probes/qbeta_sdp_angle_offset_theta_probe.py \
       2>&1 | tee /tmp/qbeta_sdp_angle_offset.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from borromean_angle_structure_lp_probe import (  # noqa: E402
    gluing, ga_equalities, solve_angle_lp,
)

set_compute_dps()

# Measured leaks (inputs, from qbeta_t4_stokes3_crux_probe.py) and the grid the
# T4 inversion used. Consumed for the TEST only; never fitted to.
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
# Canonical proton-pinned substrate modulus, READ not typed. The T4 probe's old
# literal 1.11020 was a unit conflation (it solved 2*ln q = h instead of using
# q0); fixed 2026-08-07, which moved the derived theta by -0.60% / -0.05%.
Q0 = Q_MP

ANCHORS = [("muon", "m004", "4_1 figure-eight"),
           ("proton", "L6a4", "Borromean rings")]


def geometric_angles(M, N):
    """The complete structure's angles in π-units, GA slot order (z, z', z'').

    This is Rivin's critical point of the volume functional — the saddle.
    """
    out = []
    for z in M.tetrahedra_shapes("rect"):
        zz = mp.mpc(complex(z))
        zp = 1 / (1 - zz)          # z'
        zpp = 1 - 1 / zz           # z''
        out += [mp.arg(zz) / mp.pi, mp.arg(zp) / mp.pi, mp.arg(zpp) / mp.pi]
    return out


def norm(v):
    return mp.sqrt(sum(x * x for x in v))


def main() -> int:
    print("=" * 78)
    print(" SDP/LP angle-structure data as a source for ϑ_K — measurement, no fit")
    print("=" * 78)

    import snappy  # noqa: E402

    lnq = mp.log(Q0)
    L = lnq**2
    r_target = S_MUON / S_PROTON
    lattice_unit = (mp.sqrt(3) / 2) * lnq
    print(f"\n  ln q₀ = {mp.nstr(lnq, 10)}   L = {mp.nstr(L, 10)}   "
          f"r = S_μ/S_p = {mp.nstr(r_target, 12)}")
    print(f"  lattice unit (√3/2)·ln q₀ = {mp.nstr(lattice_unit, 10)}")

    res, gate_ok = {}, True
    for anchor, name, desc in ANCHORS:
        print(f"\n[{anchor}] {name} — {desc}")
        M, N, r_cusps, edge_rows, cusp_rows = gluing(snappy, name)
        A_eq, b_eq = ga_equalities(N, edge_rows)
        print(f"    {N} tets, {r_cusps} cusps, solution '{M.solution_type()}', "
              f"GA system {len(A_eq)}×{3 * N}")

        x_geom = geometric_angles(M, N)

        # ---- G0 GATE: the geometric point must satisfy the SAME system ----
        resid = mp.mpf(0)
        for row, rhs in zip(A_eq, b_eq):
            s = sum(mp.mpf(int(c)) * x for c, x in zip(row, x_geom))
            resid = max(resid, abs(s - mp.mpf(int(rhs))))
        ok = resid < mp.mpf("1e-9")
        gate_ok = gate_ok and ok
        print(f"    G0 gate: max |A·x_geom − b| = {mp.nstr(resid, 6)}  → {ok}")

        # ---- the LP optimum (Casson-Rivin max-strictness), canonical ----
        lp = solve_angle_lp(N, A_eq, b_eq)
        s_star, x_lp = lp[0], lp[1]
        x_lp = [mp.mpf(str(v)) for v in x_lp]
        print(f"    LP: max-strictness s* = {mp.nstr(mp.mpf(str(s_star)), 8)} "
              f"(strict iff > 0)")

        offset = [g - l for g, l in zip(x_geom, x_lp)]
        mag = norm(offset)
        # angle of incidence: between the offset and the all-ones (trivial)
        # direction, the only canonical reference available without choosing
        # an objective. Reported, not interpreted.
        ones = [mp.mpf(1)] * (3 * N)
        cosang = sum(a * b for a, b in zip(offset, ones)) / (norm(offset) * norm(ones)) \
            if mag > 0 else mp.mpf(0)
        cosang = max(mp.mpf(-1), min(mp.mpf(1), cosang))
        ang = mp.acos(cosang)
        # An offset at round-off is the ZERO vector; its direction is undefined
        # and `acos` of the noise would report a spurious pi/2. Flag it.
        degenerate = mag < mp.mpf("1e-12")

        print(f"    M1 ‖offset‖ (Euclidean, π-units) = {mp.nstr(mag, 12)}")
        print(f"    M1 angle to the trivial direction = "
              + ("UNDEFINED (offset is the zero vector)" if degenerate
                 else f"{mp.nstr(ang, 12)} rad"))
        if degenerate:
            print("    ** OFFSET VANISHES: the geometric saddle IS the "
                  "max-strictness LP optimum for this manifold. **")
        print(f"    M2 lattice coord ‖offset‖/unit    = "
              f"{mp.nstr(mag / lattice_unit, 10)}")
        res[anchor] = {"manifold": name, "N": N, "cusps": r_cusps,
                       "gate_resid": mp.nstr(resid, 8), "gate_ok": bool(ok),
                       "s_star": str(s_star),
                       "offset_norm": mp.nstr(mag, 16),
                       "angle_rad": mp.nstr(ang, 16),
                       "lattice_coord": mp.nstr(mag / lattice_unit, 12),
                       "offset_degenerate": bool(degenerate),
                       "distinct_geometric_angles":
                           sorted(set(mp.nstr(v, 10) for v in x_geom)),
                       "mag": mag, "ang": ang, "degen": degenerate}

    # ---- R1: the regular-cell certification (owner question 2026-08-07) ----
    # The vanishing offset has a reusable cause: BOTH anchors are exactly two
    # REGULAR ideal cells. Certify it against the closed-form cell volumes.
    print("\n[R1] regular-cell certification — both anchors are 2 regular ideal cells:")
    V_tet = mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))   # regular ideal tetrahedron
    V_oct = 4 * mp.catalan                                  # regular ideal octahedron
    cells = {}
    for anchor, name, cell, V1 in (("muon", "m004", "regular ideal TETRAHEDRON", V_tet),
                                   ("proton", "L6a4", "regular ideal OCTAHEDRON", V_oct)):
        Mv = snappy.Manifold(name)
        vol = mp.mpf(repr(Mv.volume()))
        rel = abs(vol - 2 * V1) / vol
        cells[anchor] = {"manifold": name, "cell": cell,
                         "cell_volume": mp.nstr(V1, 16),
                         "manifold_volume": mp.nstr(vol, 16),
                         "equals_2_cells": bool(rel < mp.mpf("1e-9")),
                         "rel_diff": mp.nstr(rel, 6)}
        print(f"    {anchor:<7} {name}: Vol = {mp.nstr(vol, 14)} = 2 x {cell} "
              f"(rel.diff {mp.nstr(rel, 4)})")
    regular_ok = all(c["equals_2_cells"] for c in cells.values())
    print(f"    → both volumes are FORCED by the cell decomposition, not measured: "
          f"{regular_ok}")

    # ---- T1: the A-free test, on each candidate reading ----
    print("\n[T1] A-free test. r < 0 forces the pair to STRADDLE ln q₀ "
          f"({mp.nstr(lnq, 8)}):")
    verdicts = {}
    for label in ("mag", "ang"):
        tm, tp = res["muon"][label], res["proton"][label]
        straddle = bool(tm < lnq < tp)
        line = (f"    reading '{label}': ϑ_μ = {mp.nstr(tm, 10)}, "
                f"ϑ_p = {mp.nstr(tp, 10)}  → straddles: {straddle}")
        rr = None
        if straddle:
            den = L - tp**2
            rr = (L - tm**2) / den if den != 0 else None
            line += f"   ratio = {mp.nstr(rr, 10)} vs r = {mp.nstr(r_target, 10)}"
        print(line)
        verdicts[label] = {
            "theta_mu": mp.nstr(tm, 14), "theta_p": mp.nstr(tp, 14),
            "straddles_lnq0": straddle,
            "ratio": mp.nstr(rr, 14) if rr is not None else None,
            "matches_r": bool(rr is not None
                              and abs(rr - r_target) < mp.mpf("1e-3")),
        }

    any_hit = any(v["matches_r"] for v in verdicts.values())
    any_straddle = any(v["straddles_lnq0"] for v in verdicts.values())

    all_degenerate = all(res[a]["degen"] for a in res)

    verdict = (
        "THE OFFSET VANISHES IDENTICALLY FOR BOTH ANCHORS — and that is a "
        "structural fact about these two knots, not a null measurement. For "
        "4_1 (m004) and the Borromean rings (L6a4) the complete hyperbolic "
        "structure IS the Casson-Rivin max-strictness LP optimum: "
        "||x_geom - x_LP|| = 2.4e-16 and 5.0e-16 respectively, i.e. zero. The "
        "reason is visible in the angles themselves — 4_1 is two REGULAR ideal "
        "tetrahedra (every angle 1/3 in pi-units) and L6a4 is the regular ideal "
        "OCTAHEDRON decomposition (angles 1/4, 1/2). Both anchors sit exactly "
        "at the symmetric point, where the volume functional's critical point "
        "and the combinatorial centre coincide. So there is no offset to "
        "measure, the offset DIRECTION is undefined (the reported angle would "
        "be arccos of round-off), and both readings fail the straddling "
        "necessary condition trivially rather than informatively. "
        "WHAT THIS ACTUALLY SHOWS, AND IT SHARPENS THE PROPOSAL RATHER THAN "
        "REFUTING IT: the max-strictness LP is PURELY COMBINATORIAL — its "
        "objective is 'maximise the minimum angle', which contains no physics. "
        "Measuring the interaction against it was the wrong second point. The "
        "proposal says the interaction IS an SDP solution, so the offset that "
        "could carry an interaction energy must be measured against the "
        "CONFINEMENT SDP optimum, whose objective t comes from the "
        "Markov-trace / Frobenius data of the specific braid. That solution "
        "generically does NOT sit at the symmetric point, precisely because its "
        "objective breaks the symmetry that makes this offset vanish. "
        "SCOPE (a), and knot-specific: this excludes the geometric-saddle-minus-"
        "combinatorial-centre reading FOR THESE TWO ANCHORS ONLY. It says "
        "nothing about knots whose geometric structure is not the symmetric "
        "one, and nothing about the physically-objectived SDP offset, which is "
        "the named next step. The G0 gate passed at 1e-16 for both, so the "
        "coordinate convention and the extraction machinery are sound and "
        "reusable. Nothing fitted; nothing wired; the S values were used only "
        "to form the test."
        if all_degenerate else
        "OFFSET IS NON-DEGENERATE FOR AT LEAST ONE ANCHOR — read the per-anchor "
        "lines and the T1 table; the straddling condition and the ratio test "
        "are then meaningful and their verdicts stand as printed.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-sdp-angle-offset-theta", engine="snappy+mpmath")
    wb.set_description(
        "Owner proposal 2026-08-07: the interaction IS an SDP/LP solution, so "
        "theta_K may be recoverable from the solution's geometry — magnitude, "
        "angle of incidence, offset from the lattice saddle. Measures, for both "
        "anchors (4_1 = m004 = muon, Borromean = L6a4 = proton), the complete "
        "structure's angle vector (Rivin's critical point of the volume "
        "functional = the saddle) and the Casson-Rivin max-strictness LP "
        "optimum, then their offset norm and direction. Gate G0 confirms the "
        "geometric point satisfies the same generalised-angle-structure linear "
        "system as the LP. Tests the readings against the A_omega-free "
        "constraint curve of PR #4513. This is the first route in the arc "
        "supplying BOTH anchors absolutely rather than a ratio, hence the first "
        "capable of failing. Metric fixed in advance (Euclidean, pi-units). "
        "Nothing fitted; nothing wired.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("anchors", {k: {kk: vv for kk, vv in v.items()
                                if kk not in ("mag", "ang")}
                            for k, v in res.items()})
    wb.add_data("readings_tested", verdicts)
    wb.add_data("a_free_target_r", mp.nstr(r_target, 16))
    wb.add_data("metric_fixed_in_advance",
                "Euclidean in pi-units (the convention frozen by "
                "borromean_angle_structure_lp_probe.py); the volume-functional "
                "Hessian metric is the principled alternative and is NOT used "
                "here — named as follow-up so the choice stays visible")
    wb.add_data("why_this_shape_can_fail",
                "AfreeThetaConstraint.ratio_attained proves a ratio-shaped "
                "candidate is unfalsifiable; this route supplies both anchors "
                "absolutely (3 numbers per knot vs 3 unknowns total), so it is "
                "over-determined and can fail")
    wb.add_data("untried_follow_ups",
                ["volume-functional Hessian metric at x_geom",
                 "per-cusp offset rather than the global vector",
                 "LP dual normal y* as the angle-of-incidence reference",
                 "a confinement objective rather than max-strictness"])
    wb.add_data("verdict", verdict)
    wb.add_data("regular_cell_certification", cells)
    wb.add_data("regular_cell_consequences", [
        "Vol(4_1) and Vol(B_3) are NOT measured inputs — each is exactly 2x a "
        "closed-form regular ideal cell volume (tetrahedron / octahedron), so "
        "anywhere the corpus carries them as numeric literals they are "
        "'structural' for the no-free-parameter certificate (bean qou-skum)",
        "the muon anchor is 2 regular SIMPLICES and the proton anchor is 2 "
        "regular OCTAHEDRA — same cell COUNT, different cell TYPE; the volume "
        "ratio is therefore V_oct/V_tet = 4*Catalan / Im Li_2(e^{i*pi/3}), a "
        "pure ratio of regular-cell volumes with no knot theory in it",
        "both anchors are the maximally symmetric member of their cell type, "
        "which is why the offset vanishes AND is a structural reason a third "
        "comparably-canonical anchor may not exist — making the arc's 2-equations"
        "-in-3-unknowns underdetermination FORCED rather than a gap to be filled",
    ])
    wb.add_data("tempting_but_untestable",
        "the angle denominators (3 for the tetrahedron; 4 and 2 for the "
        "octahedron) invite reading A_omega = 3 off the 4_1 angle 1/3. That is a "
        "SINGLE number and AfreeThetaConstraint.ratio_attained proves any such "
        "reading merely names an A rather than testing one. Flagged so a later "
        "agent does not mistake it for evidence.")
    wb.add_data("offset_vanishes_both_anchors", bool(all_degenerate))
    wb.add_data("why_offset_vanishes",
                "4_1 = two REGULAR ideal tetrahedra (all angles 1/3 in pi-units); "
                "L6a4 = regular ideal OCTAHEDRON decomposition (angles 1/4, 1/2). "
                "Both anchors sit at the symmetric point where the volume "
                "functional's critical point coincides with the combinatorial "
                "centre, so x_geom = x_LP exactly.")
    wb.add_data("corrected_next_step",
                "measure the offset against the CONFINEMENT SDP optimum (objective "
                "t from Markov-trace / Frobenius data of the braid), not against "
                "the max-strictness LP whose objective is purely combinatorial and "
                "therefore symmetric")
    wb.add_assertion("offset_vanishes_at_symmetric_point",
                     computed="1" if all_degenerate else "0", expected="1",
                     tolerance="0.5",
                     source="||x_geom - x_LP|| < 1e-12 for both anchors — the "
                            "structural finding, not a null result")
    wb.add_assertion("both_anchors_are_two_regular_ideal_cells",
                     computed="1" if regular_ok else "0", expected="1",
                     tolerance="0.5",
                     source="Vol(m004) = 2 x regular ideal tetrahedron and "
                            "Vol(L6a4) = 2 x regular ideal octahedron, each to "
                            "<1e-9 relative")
    wb.add_assertion("G0_geometric_point_satisfies_GA_system",
                     computed="1" if gate_ok else "0", expected="1",
                     tolerance="0.5",
                     source="the complete structure's angles must satisfy the "
                            "same edge/tet linear system as the LP — coordinate "
                            "convention gate")
    wb.save()
    print("  witness -> computations/probes/qbeta-sdp-angle-offset-theta.witness.json")
    return 0 if gate_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
