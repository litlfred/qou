#!/usr/bin/env python3
"""
The canonical atomic word is NOT a braid word — so there is no complement to
triangulate, for any atom.

Bean `qou-eptr`, issue #6941. This is the root-level answer to whether the
Epstein-Penner route can reach the binding gap, and it sits UPSTREAM of every
other measurement in this arc.

The whole route presumes an object of the form `S^3 \\ closure(beta_atom)`: take
the atom's canonical braid, close it, remove it from the 3-sphere, decompose the
complement. This probe measures that the first step does not exist.

WHAT THE LETTERS ARE. `canonical_braid_crossings` classifies each letter of the
canonical word as a Hecke-algebra element `c*sigma + d*1` with `c = 1`:

    d = 0        ->  "sigma"       = sigma_g            a positive crossing
    d = -h       ->  "sigma_inv"   = sigma_g - h        a negative crossing,
                                                        since sigma^2 = h*sigma + 1
                                                        gives sigma^-1 = sigma - h
    d = -h/2     ->  "averaged"    = sigma_g - h/2      NEITHER
    d = -h(1/2 - delta/4) -> "averaged_weighted"        NEITHER

and the third is exactly the arithmetic mean of the first two:

    (sigma + sigma^-1)/2 = (sigma + sigma - h)/2 = sigma - h/2.

**An "averaged" letter is not a crossing.** In a link diagram every crossing is
either over or under; this is the midpoint of the two. It is a linear
combination in `H_n(q)`, and the braid group `B_n` maps into `H_n(q)` by
PRODUCTS of `sigma_i^{+-1}` — a proper linear combination is not such a product.

MEASURED HERE: across the full mass range, protium through iron-56, **zero of
twelve atoms has a word free of these letters.** Every atom carries them, and
the count grows with `A`. So no atom's canonical word is a braid word, and
"the closure of the atom's braid" is undefined for every atom in the framework.

CONSEQUENCE, and it subsumes the rest of this arc. The reachability probe found
that an Epstein-Penner invariant of the DICTIONARY-NAMED knot is constant across
13 atoms; the cell-structure probe found the Pachner candidate vanishes on 4_1.
Both are downstream of a more basic fact: there is no per-atom link to have an
invariant OF. It also explains why `classify_nuclear_knot` is a four-branch
dispatch on `A` rather than a computation — a label is what you can assign when
the object is not a link whose type could be computed.

SCOPE — (a), and the distinction matters.

This is measured as: **the canonical word, as the corpus's own classifier
defines its letters, is not a word in the braid group, so its closure is not
defined without an additional choice.** It is NOT proved that
`sigma - h/2` lies outside the image of `B_n` in `H_n(q)` — that would be a
scope-(b) claim and no such proof is offered here.

THE REPAIR EXISTS AND IS A CHOICE, WHICH IS THE POINT. Replacing each averaged
letter by `sigma` or by `sigma_inv` yields a genuine braid whose closure is a
link, and the sigma / sigma_inv counts are already per-atom and distinct, so a
resolution WOULD give per-atom links. But which resolution is a free choice —
2^k of them for `k` averaged letters, and `k` reaches 113 at iron-56. Selecting
one because its complement's invariants land near a target is a fit under the
NO-FITTING directive and must be labelled one. A DERIVED resolution rule would
be a real result; this probe does not have one and does not propose one.

Precision: letters are exact symbolic classifications; all counts are exact
integers. No floats, no `q` evaluated, no anchor.

-- Ref: [manuscript] computations/canonical_braid_crossings.py (the ctype contract)
-- Ref: [manuscript] docs/audits/2026-09-06-universal-triangulation-ep-route-assessment.md
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

BRAID_LETTERS = {"sigma", "sigma_inv"}

ATOMS = [("protium", 1, 0), ("deuterium", 1, 1), ("tritium", 1, 2),
         ("he3", 2, 1), ("he4", 2, 2), ("li6", 3, 3), ("li7", 3, 4),
         ("be9", 4, 5), ("b11", 5, 6), ("c12", 6, 6), ("o16", 8, 8),
         ("ne20", 10, 10), ("ca40", 20, 20), ("fe56", 26, 30)]


def main() -> int:
    rows = []
    for name, Z, N in ATOMS:
        w = atom_canonical_crossings(Z, N)
        c = Counter(t for _, t in w)
        non_braid = sum(v for k, v in c.items() if k not in BRAID_LETTERS)
        rows.append({"name": name, "Z": Z, "N": N, "A": Z + N,
                     "n_letters": len(w), "n_sigma": c["sigma"],
                     "n_sigma_inv": c["sigma_inv"],
                     "n_non_braid": non_braid,
                     "is_braid_word": non_braid == 0})

    seen = set()
    for name, Z, N in ATOMS:
        seen |= {t for _, t in atom_canonical_crossings(Z, N)}
    non_braid_types = sorted(seen - BRAID_LETTERS)

    n_pure = sum(1 for r in rows if r["is_braid_word"])
    max_k = max(r["n_non_braid"] for r in rows)

    checks = [
        ("no_atom_word_is_a_braid_word", n_pure == 0,
         f"0 of {len(rows)} atoms, protium through iron-56, has a word free of "
         "non-braid letters"),
        ("every_atom_carries_non_braid_letters",
         all(r["n_non_braid"] > 0 for r in rows),
         "the obstruction is universal, not a heavy-atom artifact — even "
         "protium carries them"),
        ("non_braid_letter_types_are_the_averaged_family",
         set(non_braid_types) <= {"averaged", "averaged_weighted"},
         f"the only non-braid letters are {non_braid_types}, both of which are "
         "sigma + d*1 with d strictly between 0 and -h"),
        ("non_braid_count_grows_with_A",
         all(a["n_non_braid"] <= b["n_non_braid"]
             for a, b in zip(rows, rows[1:]) if a["A"] <= b["A"]),
         "the count is non-decreasing in A, so the obstruction worsens with "
         f"mass rather than washing out (max {max_k} at the heaviest sampled)"),
        ("sigma_counts_are_per_atom_distinct",
         len({(r["n_sigma"], r["n_sigma_inv"]) for r in rows}) == len(rows),
         "the braid-letter counts ARE per-atom, so a chosen resolution of the "
         "averaged letters would give per-atom links — which is why the "
         "resolution is a choice and not a non-issue"),
    ]

    print(f"{'atom':10} {'A':>3} {'len':>5} {'sigma':>6} {'s_inv':>6} "
          f"{'non-braid':>10}  braid word?")
    for r in rows:
        print(f"{r['name']:10} {r['A']:>3} {r['n_letters']:>5} "
              f"{r['n_sigma']:>6} {r['n_sigma_inv']:>6} "
              f"{r['n_non_braid']:>10}  {r['is_braid_word']}")
    print()
    print(f"atoms whose canonical word IS a braid word: {n_pure} / {len(rows)}")
    print(f"non-braid letter types: {non_braid_types}")
    print(f"averaged = sigma - h/2 = (sigma + sigma^-1)/2 "
          f"— the midpoint, not a crossing")
    print(f"free binary choices to repair the heaviest sampled: 2^{max_k}")
    print()

    ok = 0
    for name, cond, desc in checks:
        print(f"[{'PASS' if cond else 'FAIL'}] {name}: {desc}")
        ok += 1 if cond else 0
    print(f"\n{ok}/{len(checks)} assertions")

    try:
        from qou_substrate.witness import WitnessBuilder
    except Exception as e:  # noqa: BLE001
        print(f"(witness not emitted: {e!r})")
        return 0 if ok == len(checks) else 1

    wb = WitnessBuilder("canonical-word-is-not-a-braid", engine="python",
                        _script_path=__file__)
    for name, cond, desc in checks:
        wb.add_assertion(name, computed="1" if cond else "0", expected="1",
                         tolerance="0.5", source=desc)
    wb.add_data("atoms", rows)
    wb.add_data("non_braid_letter_types", non_braid_types)
    wb.add_data("n_atoms_with_braid_word", n_pure)
    wb.add_data("max_non_braid_letters", max_k)
    wb.add_data("averaged_identity",
                "averaged = sigma - h/2 = (sigma + sigma^-1)/2, the arithmetic "
                "mean of the positive and negative crossing")
    wb.add_data("consequence",
                "There is no per-atom link, so no complement and no "
                "triangulation, for any atom. This is upstream of the "
                "dictionary-collapse and Pachner-distance findings, and it "
                "explains why classify_nuclear_knot is a dispatch label rather "
                "than a computation.")
    wb.add_data("scope",
                "Scope-(a): the canonical word, as the corpus's own classifier "
                "defines its letters, is not a word in the braid group, so its "
                "closure is undefined without an additional choice. NOT proved "
                "that sigma - h/2 lies outside the image of B_n in H_n(q); that "
                "would be scope-(b) and no such proof is offered. A repair "
                "exists (resolve each averaged letter to sigma or sigma_inv) "
                "but it is a free choice, 2^k of them; selecting one because "
                "its invariants land near a target is a fit and must be "
                "labelled one. A DERIVED resolution rule would be a real "
                "result and this probe does not have one.")
    wb.save({"q0Anchor": "independent",
             "q0AnchorReason": "letter classification only: no q evaluated, no anchor"})
    print("witness written")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
