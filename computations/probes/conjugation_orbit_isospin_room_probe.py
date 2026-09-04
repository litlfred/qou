#!/usr/bin/env python3
"""How much room does charge conjugation leave for a total-isospin label — at
the pair layer H_2 versus the two-nucleon layer H_6?

STATUS: exact combinatorics (partitions and conjugation only; no floats, no
fit, no search).  Extends a corpus proof to the layer that matters and, in
doing so, marks the LIMIT of that proof.

-----------------------------------------------------------------------------
WHY THIS EXISTS

Bean `qou-brng`, arc `bk-crossing-mass-binding`.  The two-nucleon channel
asymmetry needs a label distinguishing total isospin T=0 (deuteron 3S1, bound)
from T=1 (np 1S0, virtual).  Note this is TOTAL isospin, not the projection:
both channels sit at I_3 = 0, which is exactly why the linking class is
channel-blind (`two_nucleon_linking_matrix_channel_blind_probe`, scope-(b)).

`QOU.MassTheory.PairIsospinAssignment` settles the PAIR layer, and settles it
negatively.  Charge conjugation is tensoring with the sign representation, so
`C: V_lambda -> V_{lambda*}`.  At n = 2 the partitions are (2) and (1,1), which
are conjugate TO EACH OTHER, so C SWAPS the two blocks.  Total isospin is
C-invariant (C: |T,T_3> -> |T,-T_3>, fixing T).  A C-invariant labelling of a
two-element set whose C is the swap is CONSTANT
(`isospin_const_of_conj_invariant`) -- so no T-label can give one block T=1 and
the other T=0.  The assignment does not merely lack a derivation; it
contradicts the corpus's own C.

THE QUESTION THIS PROBE ANSWERS.  It is tempting to read that as closing the
channel asymmetry outright.  It does not, and the reason is purely
combinatorial: the n=2 argument turns on there being ONE C-orbit covering BOTH
blocks.  The physical two-nucleon carrier is six strands (3 per nucleon, forced
-- `StrandLayoutForcesChain` / `qou-gwr9`), i.e. H_6, where C acts on 11 blocks.
A C-invariant label is constant on each C-ORBIT, not globally; so the honest
question is how many orbits there are.  That count is the number of independent
values a C-invariant T may take, and it is computed here exactly.

PREREGISTERED READING (fixed before the count is taken):
  * orbits == 1  -> a C-invariant T is constant, and C alone closes the layer.
  * orbits >= 2  -> C alone does NOT close the layer; the pair-layer proof is
    special to n=2 and must not be quoted as closing the six-strand layer.
    Whatever binds there binds for another reason.

NO FIT, NO SELECTION: the only inputs are the partitions of n and conjugation.

-- Ref: QOU/MassTheory/PairIsospinAssignment.lean (the n=2 impossibility,
`isospin_const_of_conj_invariant`); shell-schur-weyl-self-duality-proof step 4
(C = tensoring with the sign rep); StrandLayoutForcesChain.lean / qou-gwr9
(s = 3 strands per nucleon, forced); probes/channel_asymmetry_crossing_budget_
bound_probe.py (the R <= s^2 = 9 budget bound at the six-strand layer);
probes/two_nucleon_linking_matrix_channel_blind_probe.py (both channels I_3=0).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from substrate.witness_base import WitnessBuilder  # noqa: E402


def partitions(n: int, cap: int | None = None):
    """All partitions of n as weakly-decreasing tuples."""
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Conjugate (transpose) partition."""
    if not lam:
        return ()
    return tuple(sum(1 for row in lam if row > j) for j in range(lam[0]))


def orbit_structure(n: int):
    """C-orbits on the blocks of H_n, where C: lambda -> lambda*."""
    parts = sorted(partitions(n), reverse=True)
    seen, orbits, self_conj = set(), [], []
    for lam in parts:
        if lam in seen:
            continue
        lc = conjugate(lam)
        if lc == lam:
            orbits.append((lam,))
            self_conj.append(lam)
            seen.add(lam)
        else:
            orbits.append((lam, lc))
            seen.add(lam)
            seen.add(lc)
    return parts, orbits, self_conj


def main() -> int:
    t0 = time.monotonic()
    layers = {}
    for n, label in ((2, "pair layer H_2"), (6, "two-nucleon layer H_6")):
        parts, orbits, self_conj = orbit_structure(n)
        layers[n] = {
            "layer": label,
            "n_blocks": len(parts),
            "n_C_orbits": len(orbits),
            "n_self_conjugate": len(self_conj),
            "self_conjugate_blocks": [str(s) for s in self_conj],
            "orbits": [" <-> ".join(str(x) for x in o) for o in orbits],
            "C_invariant_label_is_constant": len(orbits) == 1,
            "independent_T_values_available": len(orbits),
        }

    pair, six = layers[2], layers[6]
    verdict = (
        f"The pair-layer impossibility does NOT extend. At n=2 there are "
        f"{pair['n_blocks']} blocks in {pair['n_C_orbits']} C-orbit, so a "
        f"C-invariant T is CONSTANT — which is exactly "
        f"PairIsospinAssignment's result, and C alone closes that layer. At "
        f"n=6 (the forced six-strand two-nucleon carrier) there are "
        f"{six['n_blocks']} blocks in {six['n_C_orbits']} C-orbits "
        f"({six['n_self_conjugate']} self-conjugate: "
        f"{', '.join(six['self_conjugate_blocks'])}), so a C-invariant T has "
        f"{six['independent_T_values_available']} independent values available "
        f"and is NOT forced constant. CONSEQUENCE: the n=2 proof is special to "
        f"the two-block case and must NOT be quoted as closing the six-strand "
        f"channel layer. What binds at six strands is the separate crossing-"
        f"budget bound (R <= s^2 = 9 vs nature's 33.7), not charge conjugation. "
        f"Two layers, two different obstructions — neither subsumes the other."
    )

    result = {
        "preregistered_reading": {
            "orbits_eq_1": "C-invariant T constant; C alone closes the layer",
            "orbits_ge_2": "C alone does not close the layer; the n=2 proof is special",
            "fixed_before_counting": True,
        },
        "layers": layers,
        "verdict": verdict,
    }
    payload = {
        "computation": "conjugation-orbit-isospin-room",
        "description": ("Charge-conjugation orbit structure on H_n blocks, "
                        "measuring how many independent values a C-invariant "
                        "total-isospin label may take at the pair layer (n=2) "
                        "versus the forced six-strand two-nucleon layer (n=6). "
                        "Marks the limit of the n=2 impossibility proof. "
                        "Audit-only; exact combinatorics; no fit."),
        "tier": "exploratory (scope boundary of a corpus proof)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "conjugation-orbit-isospin-room", payload,
        script_path=__file__, engine="python",
        engine_version=f"python {platform.python_version()}",
        output_dir=str(_HERE), start_time=t0,
    )
    wb.add_assertion("pair_layer_has_one_orbit_hence_constant",
                     computed=str(pair["n_C_orbits"]), expected="1")
    wb.add_assertion("pair_layer_matches_PairIsospinAssignment",
                     computed=str(pair["C_invariant_label_is_constant"]),
                     expected="True")
    wb.add_assertion("six_strand_layer_not_forced_constant",
                     computed=str(six["C_invariant_label_is_constant"]),
                     expected="False")
    wb.add_assertion("h6_block_count_is_eleven",
                     computed=str(six["n_blocks"]), expected="11")
    wb.save(extra={"auditOnly": True})

    print("=== charge-conjugation room for a total-isospin label ===")
    for n in (2, 6):
        L = layers[n]
        print(f"  {L['layer']}: {L['n_blocks']} blocks, {L['n_C_orbits']} C-orbits, "
              f"{L['n_self_conjugate']} self-conjugate")
        for o in L["orbits"]:
            print(f"      {o}")
        print(f"      C-invariant T forced constant? "
              f"{L['C_invariant_label_is_constant']}")
    print("  " + verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
