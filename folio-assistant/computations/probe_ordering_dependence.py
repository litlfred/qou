#!/usr/bin/env python3
"""probe_ordering_dependence.py — crystal shift vs nucleon ordering.

The closed form `shift(Z, N) = 18Z + 21N + 1` is proved for the
canonical pppnnn ordering (`prop:per-nucleon-shift-additive-linearity`,
PR #539).  This probe tests whether shift is ORDERING-INVARIANT or
DEPENDS ON the nucleon ordering by building atomic braids for several
orderings of fixed (Z, N) and computing crystal q-pole + Habiro shift.

Expected outcomes:
  - If shift is ordering-invariant: all orderings give 18Z + 21N + 1
  - If shift is ordering-dependent: the closed form is canonical-
    specific; non-canonical orderings give different shifts (revealing
    structural information about the interface composition)

Tested orderings for ⁴He (Z=N=2):
  ppnn (canonical), pnpn (alternating), pnnp, nppn (reflections)

Output: ordering-dependence.witness.json
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from typing import List, Tuple

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from crystal_shift_nf_atomic import (  # noqa: E402
    crystal_shift_nf, closed_form_cancellation, habiro_shift_via_crystal,
)
from mass_at_3A_proper import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1, h  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def atom_braid_word_custom(ordering: str) -> Tuple[List, int]:
    """Build atomic braid word for an arbitrary nucleon ordering.

    Mirrors `mass_at_3A_proper.atom_braid_word_3A` but accepts an
    explicit ordering string like "ppnn", "pnpn", "ppnpnn", etc.

    Returns (word, n_strands) where n_strands = 3·len(ordering).
    """
    A = len(ordering)
    n_strands = 3 * A
    word = []
    for k, nuc in enumerate(ordering):
        intra_g0 = _PROTON_G0 if nuc == "p" else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == "p" else _NEUTRON_G1
        base_g0 = 3 * k
        base_g1 = 3 * k + 1
        for c, d in intra_g0:
            word.append((float(c), float(d), base_g0))
        for c, d in intra_g1:
            word.append((float(c), float(d), base_g1))
        if k < A - 1:
            i_inter = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == "p" and next_nuc == "p":
                inter = (1.0, 0.0)
            elif nuc == "n" and next_nuc == "n":
                inter = (1.0, -h)
            else:  # pn or np
                inter = (1.0, -h / 2)
            word.append((float(inter[0]), float(inter[1]), i_inter))
    return word, n_strands


def main() -> int:
    print("=" * 90)
    print("  Crystal shift vs nucleon ordering (closed form is for pppnnn)")
    print("=" * 90)
    print()

    # ⁴He = (Z=2, N=2) orderings — full enumeration of 4!/(2!2!) = 6 orderings
    # (but some are equivalent under reversal symmetry)
    he4_orderings = ["ppnn", "pnpn", "pnnp", "nppn", "npnp", "nnpp"]
    # T = (Z=1, N=2) — 3 orderings: pnn, npn, nnp
    t_orderings = ["pnn", "npn", "nnp"]
    # 3He = (Z=2, N=1) — 3 orderings: ppn, pnp, npp
    he3_orderings = ["ppn", "pnp", "npp"]

    all_targets = []
    all_targets.extend(("4He", o, 2, 2) for o in he4_orderings)
    all_targets.extend(("T",   o, 1, 2) for o in t_orderings)
    all_targets.extend(("3He", o, 2, 1) for o in he3_orderings)

    print(f"  {'atom':<6} {'ordering':<8} {'(Z,N)':>6} {'n_pp':>5} {'n_pn':>5} {'n_nn':>5} "
          f"{'q-pole':>8} {'cancel':>8} {'bridge':>8}  {'canonical':>10}")
    print("  " + "-" * 90)
    results = []
    for atom, ordering, Z, N in all_targets:
        word, n_strands = atom_braid_word_custom(ordering)
        # Count interface types
        n_pp = sum(1 for i in range(len(ordering) - 1)
                   if ordering[i] == "p" and ordering[i + 1] == "p")
        n_nn = sum(1 for i in range(len(ordering) - 1)
                   if ordering[i] == "n" and ordering[i + 1] == "n")
        n_pn = len(ordering) - 1 - n_pp - n_nn
        t0 = time.monotonic()
        res = crystal_shift_nf(word, n_strands)
        elapsed = time.monotonic() - t0
        qpole = res["shift_nf"]
        cancellation = closed_form_cancellation(Z, N)
        bridge = habiro_shift_via_crystal(Z, N, qpole)
        # Canonical for comparison
        canonical = 18 * Z + 21 * N + 1
        print(f"  {atom:<6} {ordering:<8} {f'({Z},{N})':>6} {n_pp:>5} {n_pn:>5} {n_nn:>5} "
              f"{qpole:>8} {cancellation:>8.1f} {bridge:>8}  {canonical:>10}  ({elapsed:.1f}s)")
        results.append({
            "atom": atom, "ordering": ordering,
            "Z": Z, "N": N, "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
            "n_strands": n_strands, "word_length": len(word),
            "q_pole_crystal": qpole,
            "cancellation_closed_form": cancellation,
            "bridge_shift": bridge,
            "canonical_shift_18Z_21N_1": canonical,
            "matches_canonical": bool(bridge == canonical),
            "compute_time_seconds": elapsed,
        })
    print()

    # Analyze ordering dependence
    print("  Ordering-dependence analysis:")
    by_atom = {}
    for r in results:
        by_atom.setdefault(r["atom"], []).append(r)
    for atom, rows in by_atom.items():
        shifts = {r["ordering"]: r["bridge_shift"] for r in rows}
        unique = set(shifts.values())
        invariant = len(unique) == 1
        print(f"    {atom}: shifts = {shifts}")
        print(f"      ORDERING-INVARIANT: {invariant} "
              f"({'all paths give same shift' if invariant else f'{len(unique)} distinct values'})")
    print()

    # Total verifications
    n_match = sum(1 for r in results if r["matches_canonical"])
    print(f"  Of {len(results)} orderings tested, {n_match} match canonical 18Z+21N+1.")
    print()

    builder = (
        WitnessBuilder("ordering-dependence", engine="python")
        .set_description(
            "Crystal q-pole + Habiro shift across non-canonical nucleon "
            "orderings of ⁴He, T, ³He.  Tests whether the closed form "
            "shift(Z, N) = 18Z + 21N + 1 is ordering-invariant or "
            "depends on nucleon ordering.  If invariant, the closed "
            "form is structural; if dependent, non-canonical orderings "
            "have different shifts revealing interface-composition "
            "structure (n_pp, n_pn, n_nn counts)."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-sublemma-2-1-h9-multi-interface-extension.md"
        )
        .add_data("orderings_tested", results)
        .add_data("n_orderings", len(results))
        .add_data("n_match_canonical", n_match)
        .add_data("invariance_by_atom", {
            atom: {
                "shifts": {r["ordering"]: r["bridge_shift"] for r in rows},
                "invariant": len(set(r["bridge_shift"] for r in rows)) == 1,
            }
            for atom, rows in by_atom.items()
        })
        .add_caveat(
            "Habiro bridge formula uses `cancellation = 3Z + 1.5N − 1.5` "
            "which was empirically derived for canonical pppnnn (PR "
            "#539, per_nucleon_shift_derivation).  For non-canonical "
            "orderings the cancellation may be different — this probe's "
            "`bridge_shift` may not be the true Habiro shift if the "
            "cancellation formula is ordering-dependent.  The crystal "
            "q-pole IS computed correctly (combinatorial primitive); "
            "interpreting it as Habiro-shift requires the canonical "
            "cancellation."
        )
    )
    out = builder.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
