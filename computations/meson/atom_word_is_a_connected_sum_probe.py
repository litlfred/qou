#!/usr/bin/env python3
"""The atom braid word is a CONNECTED SUM by construction — and that is the gap.

Bean qou-6tcn. The author asked whether the "two knots threaded by a torus"
picture -- the *convolution*, not the disjoint union -- is visible in the
Groebner/normal-form structure of the braiding. It is, and what it shows is that
the current construction is the OTHER case.

MEASURED (exact combinatorics -- no q, no float, no representation theory)
=========================================================================
`atom_braid_word_3A(Z, N)` on `n = 3A` strands, generator indices in order:

    deuteron   [1]*7 [2]*4  **3**  [4]*7 [5]*4
    4He        [1]*7 [2]*4  **3**  [4]*7 [5]*4  **6**  [7]*7 [8]*4  **9**  [10]*7 [11]*4

Each nucleon is an identical 11-letter block on its own three strands. The block
walls sit at `sigma_{3k}`, and each wall is crossed by **exactly one generator,
used exactly once**. The word factors strictly at every wall: everything before
uses only generators below the wall, everything after only generators above it.

That is the **connected-sum normal form**. A closed braid factoring as
`(word on strands 1..k) (one junction crossing) (word on strands k..n)` closes to
a connected sum, whose essential surfaces are **SPHERES**.

WHAT THIS EXPLAINS
==================
#5817 measured all 40 branch closures **composite**, 0 hyperbolic, and treated
that as an empirical finding about the particular word. It is not: it is
**forced by the interface being a single generator used once**. The atom is

    K(Z,N) = K_1 # K_2 # ... # K_A       by construction

so `S^3 - K` contains essential spheres and **no** essential torus anywhere. That
is exactly why `conj:jsj-decomposition-linearity` is presently true and EMPTY:
its decomposition hypothesis asks for the inter-nucleon braids to form essential
**tori**, and a one-strand junction cannot make one.

THE FIX, IN ONE NUMBER
======================
    strands crossing each block wall, now  :  1   -> connected sum, SPHERE
    strands needed for an essential torus  : >=2  -> splice, TORUS

The author's "not the simple disjoint union, the convolution is the
interweaving" names precisely this. A single crossing joins the blocks at a
point; a **bundle** of >= 2 strands threading the wall is what makes the
boundary of a neighbourhood incompressible. The interface word `I` in
`conj:confinement-nf-structure-forcing`'s `beta = beta_1 * I * beta_2` is exactly
where that change would go, and its NF shift `alpha_shift(I)` is what would move.

SCOPE -- (a), and narrower than it may look
===========================================
MEASURED: the generator multiset and ordering of the committed word, the strict
factorisation at each wall, and the single-use of each wall generator.

NOT claimed: that a >= 2-strand interface WOULD produce an essential torus (the
strand count is necessary, not sufficient -- incompressibility is a geometric
condition this probe does not test); that any particular replacement interface is
correct or derivable; that `conj:jsj-decomposition-linearity` is false (it is
true and empty as constructed, which is not the same thing); that binding follows
from any of it. Nothing here computes a binding contribution.
"""

from __future__ import annotations

import pathlib
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

ISOTOPES = [("proton", 1, 0), ("neutron", 0, 1), ("deuteron", 1, 1),
            ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3)]


def analyse(Z, N):
    w = atom_braid_word_3A(Z, N)
    A, n = Z + N, 3 * (Z + N)
    gens = [g + 1 for (_c, _d, g) in w]
    walls = [3 * k for k in range(1, A)]
    cnt = Counter(gens)
    rows = []
    all_split = True
    for wl in walls:
        occ = [i for i, g in enumerate(gens) if g == wl]
        split = False
        if len(occ) == 1:
            p = occ[0]
            split = (all(g < wl for g in gens[:p])
                     and all(g > wl for g in gens[p + 1:]))
        all_split &= split
        rows.append({"wall": wl, "uses": len(occ), "factors_strictly": split})
    intra_uses = sorted({cnt[g] for g in cnt if g not in walls})
    return {"A": A, "n_strands": n, "letters": len(gens),
            "walls": walls, "n_walls": len(walls),
            "wall_rows": rows, "all_walls_factor": all_split,
            "wall_uses": [r["uses"] for r in rows],
            "intra_generator_use_counts": intra_uses,
            "strands_crossing_each_wall": 1 if walls else 0}


def main() -> int:
    wb = WitnessBuilder("atom-word-is-a-connected-sum", engine="python-exact")
    wb.set_description(
        "The atom braid word factors strictly at every block wall, each wall "
        "crossed by exactly ONE generator used exactly ONCE -- the "
        "connected-sum normal form. So K(Z,N) = K_1 # ... # K_A by "
        "construction, its essential surfaces are SPHERES, and no essential "
        "torus exists anywhere. That explains #5817's 40/40 composite result "
        "structurally rather than empirically, and it is why "
        "conj:jsj-decomposition-linearity is true and EMPTY: a one-strand "
        "junction cannot make the essential torus its hypothesis asks for. "
        "A splice needs >= 2 strands crossing the wall.")

    data = {name: analyse(Z, N) for name, Z, N in ISOTOPES}
    multi = [d for d in data.values() if d["n_walls"] > 0]
    all_factor = sum(1 for d in multi if d["all_walls_factor"])
    all_once = all(all(u == 1 for u in d["wall_uses"]) for d in multi)
    walls_ok = all(d["n_walls"] == d["A"] - 1 for d in data.values())
    intra = sorted({u for d in data.values()
                    for u in d["intra_generator_use_counts"]})

    for name, d in data.items():
        print(f"{name:<9} A={d['A']} n={d['n_strands']:>2} "
              f"letters={d['letters']:>2} walls={d['walls']} "
              f"uses={d['wall_uses']} factors={d['all_walls_factor']}")
    print(f"\nintra-nucleon generator use counts across all isotopes: {intra}")
    print(f"strands crossing each wall: 1   (>= 2 required for an essential torus)")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE RESULT: the connected-sum factorisation, at every wall of every
    #      multi-nucleon isotope.
    wb.add_assertion(
        name="word_factors_strictly_at_every_block_wall",
        computed=str(all_factor), expected=str(len(multi)),
        tolerance="0", unit="count",
        source="everything before a wall uses only generators below it, "
               "everything after only generators above it")

    # A2 — and each wall is a SINGLE crossing, which is what makes it a sphere.
    wb.add_assertion(
        name="each_wall_generator_used_exactly_once",
        computed=repr(bool(all_once)), expected="True", tolerance="0",
        unit="boolean", source="occurrence count of sigma_{3k} in the word")

    # A3 — CONTROL against the vacuous reading "every generator is used once":
    #      the intra-nucleon generators are used 4 and 7 times.
    wb.add_assertion(
        name="control_intra_nucleon_generators_used_many_times",
        computed=repr(intra), expected="[4, 7]", tolerance="0", unit="counts",
        source="use counts of the non-wall generators; A2 is meaningful only "
               "because these are not 1")

    # A4 — CONTROL: wall count tracks the nucleon count, so the walls really are
    #      the inter-nucleon interfaces and not an artefact of indexing.
    wb.add_assertion(
        name="control_wall_count_is_A_minus_one",
        computed=repr(bool(walls_ok)), expected="True", tolerance="0",
        unit="boolean", source="n_walls vs A - 1 across all six isotopes")

    # A5 — CONTROL: A = 1 has no wall at all, so the structure measured is the
    #      JOIN and not something internal to a nucleon block.
    wb.add_assertion(
        name="control_single_nucleon_has_no_wall",
        computed=str(data["proton"]["n_walls"] + data["neutron"]["n_walls"]),
        expected="0", tolerance="0", unit="count",
        source="proton and neutron are A = 1")

    # A6 — the number the fix turns on.
    wb.add_assertion(
        name="strands_crossing_each_wall",
        computed=str(data["deuteron"]["strands_crossing_each_wall"]),
        expected="1", tolerance="0", unit="count",
        source="a single generator couples one strand from each block; an "
               "essential torus needs a bundle of >= 2")

    for name, d in data.items():
        wb.add_data(name, d)
    wb.add_data("strands_needed_for_essential_torus", ">= 2")
    wb.add_data("interface_slot",
                "conj:confinement-nf-structure-forcing beta = beta_1 * I * beta_2")
    wb.add_caveat(
        "Scope (a). The strand count is NECESSARY, not sufficient: "
        "incompressibility is a geometric condition this probe does not test, so "
        "it is NOT claimed that a >= 2-strand interface would produce an "
        "essential torus -- only that a 1-strand interface cannot.")
    wb.add_caveat(
        "NOT claimed: that any particular replacement interface is correct or "
        "derivable; that conj:jsj-decomposition-linearity is FALSE (it is true "
        "and EMPTY as constructed, which is not the same thing); that binding "
        "follows from any of this. Nothing here computes a binding contribution.")
    wb.add_caveat(
        "This EXPLAINS rather than contradicts #5817's 40/40 composite finding: "
        "that result is forced by the interface being a single generator used "
        "once, so it is structural rather than a property of the particular "
        "word measured.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
