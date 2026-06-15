#!/usr/bin/env python3
# polynomial_q_not_applicable: pure integer combinatorics on nucleon
# orderings + d-value classification of the canonical braid word; no
# q-polynomial arithmetic.
"""Canonical-braid interface composition sweep (Layer 3 producer).

Emits `canonical-braid-interface-composition.witness.json` for
`def:canonical-braid-interface-composition`.

For each atom (Z, N) in the known table, this probe computes the
inter-nucleon interface composition (n_pp, n_pn, n_nn) two ways and
cross-checks them:

  1. **Closed form** — `interface_composition(Z, N, ordering='pppnnn')`
     from `interface_composition.py`:

         n_pp = max(0, Z − 1)
         n_nn = max(0, N − 1)
         n_pn = 1 if Z ≥ 1 and N ≥ 1 else 0
         total = n_pp + n_pn + n_nn = A − 1

  2. **From the canonical braid word** — `atom_braid_word_3A(Z, N)`
     (the authoritative producer `mass_at_3A_proper`) is inspected at
     the inter-nucleon interface positions σ_{3k+2}; each interface
     generator is classified by its content `d`:

         d = 0     → pp interface (bare σ)
         d = −h/2  → pn interface (averaged Δ_I = σ − h/2)
         d = −h    → nn interface (σ⁻¹)

The witness records, for every atom, the (n_pp, n_pn, n_nn) triple and
asserts the two derivations agree exactly. This makes the closed-form
definition checkable against the producing braid word.

NOTE ON THE ⁴He NARRATIVE TABLE: the empirical table (Table 2) and the
ordering-comparison table (Table 3) in the `.md` list the ⁴He row as
(n_pp, n_pn, n_nn) = (1, 2, 1) with total 4. That contradicts the boxed
closed form AND the canonical word `atom_braid_word_3A(2, 2)`, both of
which give (1, 1, 1) with total A−1 = 3 (one pp at gen 2, one pn at gen
5, one nn at gen 8). This probe records the closed-form / from-word
value (1, 1, 1), which is the authoritative claim; the narrative-table
discrepancy is a separate `.md` content bug, not a compute result.

Helper: `interface_composition.py`
Authoritative word producer: `mass_at_3A_proper.atom_braid_word_3A`
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from interface_composition import (  # noqa: E402
    ATOM_TABLE,
    interface_composition,
    interface_composition_from_ordering,
    interface_composition_from_word,
    pppnnn_ordering,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    w = WitnessBuilder(
        "canonical-braid-interface-composition",
        engine="python",
    )
    w.set_description(
        "Inter-nucleon interface composition (n_pp, n_pn, n_nn) of the "
        "canonical atomic braid β(Z, N) ∈ H_{3A}(q) in pppnnn ordering. "
        "Cross-checks the closed form (n_pp = max(0, Z−1), n_nn = "
        "max(0, N−1), n_pn = 1 if Z≥1,N≥1) against the actual canonical "
        "braid word atom_braid_word_3A(Z, N) classified by interface "
        "content d ∈ {0 → pp, −h/2 → pn, −h → nn}. Total = A − 1."
    )
    w.set_content_block("def:canonical-braid-interface-composition")
    w.add_parameter("ordering", "pppnnn")
    w.add_parameter("interface_positions", "σ_{3k+2}, k = 0..A-2")

    rows = []
    all_match = True
    for atom, (Z, N) in ATOM_TABLE.items():
        A = Z + N
        closed = interface_composition(Z, N, ordering="pppnnn")
        from_ordering = interface_composition_from_ordering(
            pppnnn_ordering(Z, N)
        )
        word = atom_braid_word_3A(Z, N)
        from_word = interface_composition_from_word(word)
        match = (closed == from_ordering == from_word)
        all_match = all_match and match
        total = sum(closed)
        rows.append({
            "atom": atom,
            "Z": Z,
            "N": N,
            "A": A,
            "n_pp": closed[0],
            "n_pn": closed[1],
            "n_nn": closed[2],
            "total": total,
            "total_equals_A_minus_1": (total == A - 1),
            "closed_form": list(closed),
            "from_ordering": list(from_ordering),
            "from_word": list(from_word),
            "all_three_agree": match,
        })
        print(f"  {atom:<5} (Z={Z},N={N}) A={A:<2}  "
              f"closed={closed}  from_word={from_word}  "
              f"total={total} (A-1={A-1})  match={match}")

    w.add_data("rows", rows)
    w.add_data("n_atoms", len(rows))

    # Spot-check assertions on the canonical {D, T, ³He, ⁴He} bench
    # plus a heavy nucleus, recording (closed vs from-word) cross-check.
    spot = {
        "D": (0, 1, 0),
        "T": (0, 1, 1),
        "3He": (1, 1, 0),
        "4He": (1, 1, 1),
        "16O": (7, 1, 7),
    }
    for atom, expected in spot.items():
        Z, N = ATOM_TABLE[atom]
        from_word = interface_composition_from_word(atom_braid_word_3A(Z, N))
        # Encode the (n_pp, n_pn, n_nn) triple as a single integer
        # 100·n_pp + 10·n_pn + n_nn for a scalar assertion.
        def enc(t):
            return 100 * t[0] + 10 * t[1] + t[2]
        w.add_assertion(
            name=f"interface_composition_{atom}",
            computed=enc(from_word),
            expected=enc(expected),
            tolerance=0,
            source=(
                f"{atom} (Z={Z},N={N}): canonical word "
                f"atom_braid_word_3A gives (n_pp,n_pn,n_nn)={from_word}; "
                f"closed form predicts {expected}"
            ),
        )

    # Global assertion: closed form == from-word for ALL atoms.
    w.add_assertion(
        name="closed_form_matches_canonical_word_all_atoms",
        computed=1 if all_match else 0,
        expected=1,
        tolerance=0,
        source=(
            "interface_composition(Z,N) closed form agrees with "
            "interface_composition_from_word(atom_braid_word_3A(Z,N)) "
            f"for all {len(rows)} atoms in ATOM_TABLE"
        ),
    )

    out = w.save()
    print(f"\n  all atoms closed-form == from-word: {all_match}")
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
