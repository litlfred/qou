#!/usr/bin/env python3
"""Which case of Geom(K) do the atom branches fall into?  Measured.

Bean qou-7p7d.  The design question, answered from inside the framework.

THE RULE THE FRAMEWORK ALREADY STATES
=====================================
`prop:hoefsmit-scattering-pipeline` Stage 3 makes Geom(K) a THREE-WAY CASE SPLIT
on the geometric type of K, with different physical meanings per case:

    Vol(K)/hbar_q^2   for HYPERBOLIC K   -> mass/energy
    CS(K)*hbar_q^2    for TORUS K        -> coupling phase
    0                 for the UNKNOT     -> vacuum

and `predicted-spectra/em-coupling-chern-simons.md` APPLIES it, verbatim: "The
torus knots T_{2,9} and T_{3,5} are non-hyperbolic. Their tau-image geometric
invariant is the Chern-Simons functional, not the hyperbolic volume."

So the framework does not need a new geometric functor for non-hyperbolic
carriers.  It has one, states when to use it, and uses it in the alpha_EM sector.

WHAT THIS MEASURES
==================
atom_branch_hyperbolicity_probe.py established that all 40 branch closures
(proton 4, neutron 4, deuteron 32) are NON-hyperbolic.  Non-hyperbolic is not
the same as torus: by Nielsen-Thurston a non-hyperbolic closure is torus OR
reducible/satellite, and a CONNECTED SUM is in NEITHER -- Stage 3 has no case
for it.  So which is it?

This runs SnapPy's `deconnect_sum` on every branch and reports the number of
prime summands.  One summand -> prime, so torus is available and the CS case
applies.  More than one -> composite, and Stage 3 as written has NO case at all.

CALIBRATION, both directions, asserted before anything is reported:
  * a KNOWN composite -- the granny knot, trefoil # trefoil -- must split;
  * a KNOWN prime -- the trefoil -- must not.
Without both, a "everything is prime" or "everything is composite" table would
be a property of the detector.

EXPLORATORY / audit-only.  No volumes are computed or serialised here; the
verdict is a summand COUNT, an integer.
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
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import HA_MP  # noqa: E402 — exact mpf, not the f64 twin

import snappy  # noqa: E402

H = HA_MP
TOL = mp.mpf("1e-9")


def summands(braid):
    """Number of prime summands of the closure, or None on failure."""
    try:
        return len(snappy.Link(braid_closure=list(braid)).deconnect_sum())
    except Exception:                                        # noqa: BLE001
        return None


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
    # ---- calibration -----------------------------------------------------
    granny = summands([1, 1, 1, 3, 3, 3])      # trefoil # trefoil in B_4
    trefoil = summands([1, 1, 1])              # prime
    calib = {"composite_control": {"braid": "granny = trefoil # trefoil",
                                   "summands": granny, "expected": "> 1"},
             "prime_control": {"braid": "trefoil s1^3", "summands": trefoil,
                               "expected": "1"}}
    assert granny is not None and granny > 1, (
        f"COMPOSITE control failed (granny -> {granny} summands) -- the "
        "detector cannot see a connected sum, so a table of 1s below would be "
        "an artefact")
    assert trefoil == 1, (
        f"PRIME control failed (trefoil -> {trefoil}) -- the detector splits a "
        "prime knot, so a table of >1s would be an artefact")

    rows = []
    for name, Z, N in [("proton", 1, 0), ("neutron", 0, 1), ("deuteron", 1, 1)]:
        sl = branch_slots(atom_braid_word_3A(Z, N))
        counts = []
        for combo in itertools.product(*sl):
            counts.append(summands([x for x, _ in combo]))
        ok = [c for c in counts if c is not None]
        rows.append({
            "isotope": name, "A": Z + N, "branches": len(counts),
            "resolved": len(ok), "failed": len(counts) - len(ok),
            "prime_branches": sum(1 for c in ok if c == 1),
            "composite_branches": sum(1 for c in ok if c > 1),
            "max_summands": max(ok) if ok else None,
            "summand_histogram": {str(k): ok.count(k) for k in sorted(set(ok))},
        })
        print(f"  {name:9s} A={Z+N}  {len(counts):3d} branches   "
              f"prime={rows[-1]['prime_branches']:3d}  "
              f"composite={rows[-1]['composite_branches']:3d}  "
              f"summands={rows[-1]['summand_histogram']}")

    assert all(r["failed"] == 0 for r in rows), (
        "a branch failed to resolve; the sweep is incomplete and must not be "
        "reported as a clean classification")

    total_comp = sum(r["composite_branches"] for r in rows)
    total_prime = sum(r["prime_branches"] for r in rows)

    wb = WitnessBuilder("atom-branch-geom-case", engine="snappy")
    wb.set_description(
        "Classifies every atom-element branch closure by number of prime "
        "summands, to decide WHICH case of the Stage-3 Geom(K) split applies. "
        "The branches are already measured non-hyperbolic; non-hyperbolic is "
        "torus OR reducible, and a connected sum is in neither -- Stage 3 has "
        "no case for a composite. Carries a composite control (granny knot must "
        "split) and a prime control (trefoil must not).")
    wb.add_data("the_rule_the_framework_states", {
        "stage_3": ("Geom(K) = Vol(K)/hbar_q^2 for HYPERBOLIC K (mass/energy); "
                    "CS(K)*hbar_q^2 for TORUS K (coupling phase); 0 for the "
                    "UNKNOT (vacuum)"),
        "applied_in_alpha_EM": ("predicted-spectra/em-coupling-chern-simons.md: "
                                "'The torus knots T_{2,9} and T_{3,5} are "
                                "non-hyperbolic. Their tau-image geometric "
                                "invariant is the Chern-Simons functional, not "
                                "the hyperbolic volume.'"),
        "not_applied_in_mass": ("the mass path applies Vol(K)/hbar_q^2 "
                                "unconditionally, with Vol(B_3) substituted, to "
                                "carriers measured non-hyperbolic"),
    })
    wb.add_data("calibration", calib)
    wb.add_data("per_isotope", rows)
    wb.add_data("totals", {"prime": total_prime, "composite": total_comp})
    wb.set_audit_only(
        "docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md")

    wb.add_assertion(
        name="composite_control_splits", computed=granny, expected=2,
        tolerance=0, unit="summands",
        source="Granny knot = trefoil # trefoil; without this a table of 1s is an artefact.")
    wb.add_assertion(
        name="prime_control_does_not_split", computed=trefoil, expected=1,
        tolerance=0, unit="summands",
        source="Trefoil is prime; without this a table of >1s is an artefact.")
    wb.add_assertion(
        name="every_branch_resolved",
        computed=sum(r["resolved"] for r in rows),
        expected=sum(r["branches"] for r in rows), tolerance=0, unit="count",
        source="An unresolved branch makes the classification incomplete.")
    out = wb.save()
    print(f"\ncalibration: granny -> {granny} summands, trefoil -> {trefoil}")
    print(f"TOTALS: prime {total_prime}, composite {total_comp}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
