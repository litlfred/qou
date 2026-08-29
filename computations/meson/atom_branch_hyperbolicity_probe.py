#!/usr/bin/env python3
"""Is ANY branch closure of the atom element hyperbolic?  Measured with SnapPy.

Bean qou-7p7d.  This is the single question the convexity bound
(AtomBranchConvexityBound.lean, sorry-free) reduces everything to.

WHY ONE QUESTION
================
tr_M is linear, so the atom element -- which lies OUTSIDE im(rho) and has no
closure -- expands as a weighted sum of genuine braid images,
`atom = sum_b w_b rho(beta_b)`.  Measured (atom_branch_convexity_bound_probe.py):
those weights are a CONVEX combination, so

    |tr_M(atom)| <= max_b |J_{K_b}(q)|          [Lean, sorry-free]

Every branch therefore matters only through the max.  So: is any branch closure
hyperbolic?

WHAT IS NEW HERE
================
The A = 1 carriers (proton, neutron: 4 branches each) have NEVER been checked --
a sibling swept 2H's 32 branches, not these.  This file checks A = 1 and
independently re-runs 2H, so the sibling's 32/32 is corroborated rather than
merely cited.

TWO CALIBRATIONS, BOTH REQUIRED
===============================
"All branches non-hyperbolic" is uninterpretable from a detector that can only
say zero.  So this asserts, before reporting anything:

  * POSITIVE control -- the figure-eight (s1 s2^-1)^2 must come back
    2.029883212819307, so the pipeline can SEE hyperbolic volume;
  * NEGATIVE control -- the trefoil s1^3, a torus knot, must come back
    non-geometric, so a zero is a real zero and not a solver default.

A run failing either asserts rather than reports.

PRECISION, and why no volume is serialised
=========================================
An earlier draft put SnapPy's float64 volumes straight into the witness; the
raw-float64 ratchet flagged 50 fields, correctly.  `fmt()` is NOT the fix -- the
`_precision` docstring says so directly: it "will happily render a 53-bit value
out to the full serialization width, so the number *reads* as measured while
carrying ~15 significant digits", which is what the float64-padding ratchet
exists to catch.  Padding a float64 to 50 digits is laundering, not fixing.

The real fix is that there is nothing to serialise.  Every branch comes back
`degenerate` -- not "volume 0.0" but NO hyperbolic structure at all -- so a `0.0`
float would be storing a non-value.  Branch rows therefore carry the solver
STATUS and the boolean, and no volume field.

The calibration IS a genuine measurement, so it is taken at high precision
(`.high_precision()`, ~212 bits) and serialised with `fmt`, where the digits are
real.

EXPLORATORY / audit-only.
"""

from __future__ import annotations

import itertools
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from _precision import fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import HA_MP  # noqa: E402 — exact mpf, not the f64 twin

import snappy  # noqa: E402

H = HA_MP
TOL = mp.mpf("1e-9")
VOL_41_STR = "2.029883212819307"
CAL_TOL = mp.mpf("1e-9")


def hyp_volume(braid, tries: int = 8, rand: int = 60, hp: bool = False):
    """(status, volume-or-None). status in {geometric, degenerate, error}.

    `volume` is None unless the solution is geometric -- a degenerate solution
    has NO hyperbolic volume, and returning 0.0 would misrepresent that as a
    measured zero.  With `hp`, the volume is computed at ~212 bits so it can be
    serialised honestly; without it, only the status is used.
    """
    if not braid:
        return "empty", None
    try:
        for attempt in range(tries):
            M = snappy.Link(braid_closure=list(braid)).exterior()
            if hp:
                M = M.high_precision()
            if attempt:
                M.randomize()
            st = str(M.solution_type())
            if st.startswith("all tetrahedra positively oriented"):
                return "geometric", mp.mpf(str(M.volume()))
            for _ in range(rand):
                M.randomize()
                if str(M.solution_type()).startswith("all tetrahedra positively"):
                    return "geometric", mp.mpf(str(M.volume()))
        return "degenerate", None
    except Exception as e:                                   # noqa: BLE001
        return f"error:{type(e).__name__}", None


def branch_slots(word):
    out = []
    for (_c, d, g) in word:
        t = -mp.mpf(str(d)) / H
        if abs(t) < TOL:
            out.append([(g + 1, mp.mpf(1))])
        elif abs(t - 1) < TOL:
            out.append([(-(g + 1), mp.mpf(1))])
        else:
            out.append([(g + 1, 1 - t), (-(g + 1), t)])
    return out


def main() -> None:
    # ---- calibration, before anything is believed -----------------------
    pos_status, pos_vol = hyp_volume([1, -2, 1, -2], hp=True)   # figure-eight
    neg_status, neg_vol = hyp_volume([1, 1, 1])                 # trefoil, torus
    calib = {
        "positive_control": {"braid": "(s1 s2^-1)^2 = 4_1", "status": pos_status,
                             "volume": fmt(pos_vol) if pos_vol is not None else None,
                             "expected": fmt(mp.mpf(VOL_41_STR)),
                             "delta": fmt(abs(pos_vol - mp.mpf(VOL_41_STR)))
                             if pos_vol is not None else None,
                             "precision": "high_precision(), ~212 bits"},
        "negative_control": {"braid": "s1^3 = trefoil (torus)", "status": neg_status,
                             "volume": None,
                             "note": "degenerate: no hyperbolic structure, so no volume"},
    }
    assert pos_status == "geometric" and abs(pos_vol - mp.mpf(VOL_41_STR)) < CAL_TOL, (
        f"POSITIVE control failed ({pos_status}, {pos_vol}) -- this pipeline "
        "cannot see hyperbolic volume, so any 'non-hyperbolic' verdict below "
        "would be an artefact")
    assert neg_status != "geometric", (
        f"NEGATIVE control failed ({neg_status}, {neg_vol}) -- the trefoil is a "
        "torus knot and must not read as geometric")

    rows = []
    for name, Z, N in [("proton", 1, 0), ("neutron", 0, 1), ("deuteron", 1, 1)]:
        sl = branch_slots(atom_braid_word_3A(Z, N))
        branches = list(itertools.product(*sl))
        per = []
        for combo in branches:
            braid = [x for x, _ in combo]
            w = mp.mpf(1)
            for _, p in combo:
                w *= p
            st, vol = hyp_volume(braid)
            # NO volume field: every branch is degenerate, and a 0.0 would
            # misrepresent "no hyperbolic structure" as a measured zero.
            per.append({"braid": braid, "weight": mp.nstr(w, 12), "status": st,
                        "hyperbolic": st == "geometric" and vol is not None
                        and vol > CAL_TOL})
        n_hyp = sum(1 for p in per if p["hyperbolic"])
        rows.append({
            "isotope": name, "A": Z + N, "branches": len(per),
            "hyperbolic_branches": n_hyp,
            "any_hyperbolic": n_hyp > 0,
            "solver_statuses": sorted({p["status"] for p in per}),
            "detail": per,
        })
        print(f"  {name:9s} A={Z+N}  {len(per):4d} branches  hyperbolic: {n_hyp}"
              f"   statuses: {sorted({p['status'] for p in per})}")

    by = {r["isotope"]: r for r in rows}

    assert by["deuteron"]["branches"] == 32, "deuteron branch count is not 32"
    # the finding, whichever way it goes -- assert only that it was MEASURED
    assert all(all(p["status"] != "error" for p in r["detail"]) for r in rows), (
        "a branch errored in SnapPy; the sweep is incomplete and its verdict "
        "must not be reported as a clean negative")

    wb = WitnessBuilder("atom-branch-hyperbolicity", engine="snappy")
    wb.set_description(
        "Measures hyperbolicity of every branch closure of the atom H_n(q) "
        "element at A = 1 (proton, neutron -- never checked before) and A = 2 "
        "(deuteron, independently re-running the sibling's 32). This is the one "
        "question the sorry-free convexity bound reduces everything to: "
        "|tr_M(atom)| <= max_b |J_{K_b}(q)|, so only the largest branch matters. "
        "Carries a positive control (figure-eight must read 2.0298832...) and a "
        "negative control (trefoil must not read geometric), because 'all "
        "non-hyperbolic' is uninterpretable from a detector that can only say "
        "zero.")
    wb.add_data("calibration", calib)
    wb.add_data("per_isotope", rows)
    wb.add_data("scope", {
        "no_branch_volume_is_serialised": ("every branch is DEGENERATE -- no "
                                           "hyperbolic structure, so no volume. "
                                           "Storing 0.0 would misrepresent that "
                                           "as a measured zero, and fmt()-ing a "
                                           "float64 to full width is what the "
                                           "float64-padding ratchet exists to "
                                           "catch. Status strings only."),
        "what_this_does_not_settle": ("whether the mass law SHOULD read a "
                                      "volume off this object at all -- that is "
                                      "the (C) reading, bean qou-7p7d. This "
                                      "measures the branches, not the design."),
    })
    wb.set_audit_only(
        "docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md")

    wb.add_assertion(
        name="positive_control_sees_hyperbolic_volume",
        computed=fmt(pos_vol), expected=fmt(mp.mpf(VOL_41_STR)),
        tolerance=fmt(CAL_TOL), unit="volume",
        source=("Figure-eight at ~212 bits; without this a null result is an "
                "artefact of a blind detector."))
    wb.add_assertion(
        name="negative_control_rejects_a_torus_knot",
        computed=0 if neg_status == "geometric" else 1, expected=1,
        tolerance=0, unit="bool",
        source="Trefoil; without this a zero is a solver default, not a fact.")
    wb.add_assertion(
        name="every_branch_completed",
        computed=sum(1 for r in rows for p in r["detail"] if p["status"] != "error"),
        expected=sum(r["branches"] for r in rows), tolerance=0, unit="count",
        source="A sweep with an error in it is not a clean negative.")
    out = wb.save()
    print(f"\ncalibration: 4_1 -> {mp.nstr(pos_vol, 15)} "
          f"(delta {calib['positive_control']['delta']}), trefoil -> {neg_status}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
