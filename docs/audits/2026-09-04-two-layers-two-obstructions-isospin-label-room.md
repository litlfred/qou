# Two layers, two obstructions: the pair-layer isospin impossibility does not close the six-strand channel

**Date:** 2026-09-04 · **Bean:** `qou-brng`, arc `bk-crossing-mass-binding`
**Type:** scope boundary of an existing corpus proof + exact combinatorics.
No fit, no search, no production change. **Does not close the binding gap.**

## VERDICT (one line)

**`PairIsospinAssignment`'s impossibility is special to the two-block case
`n = 2` — at the forced six-strand two-nucleon layer `H₆` charge conjugation
leaves `6` independent values for a `C`-invariant total-isospin label, so it
does *not* close that layer. What binds at six strands is the separate
crossing-budget bound (`R ≤ s² = 9`), not charge conjugation.**

## The question

The channel asymmetry needs a label separating **total** isospin `T = 0`
(deuteron ³S₁, bound) from `T = 1` (np ¹S₀, virtual). This is total isospin, not
the projection — both channels sit at `I₃ = 0`, which is precisely why the
linking class is channel-blind
([`two_nucleon_linking_matrix_channel_blind_probe`](../../computations/probes/two_nucleon_linking_matrix_channel_blind_probe.py),
scope-(b)).

The corpus already settles the **pair layer**, negatively.
[`QOU.MassTheory.PairIsospinAssignment`](../../content/quantum-observable-universe/lean/QOU/MassTheory/PairIsospinAssignment.lean):
charge conjugation is tensoring with the sign representation, so
`C : V_λ → V_{λ*}`. At `n = 2` the partitions `(2)` and `(1,1)` are conjugate
**to each other**, so `C` *swaps* the two blocks; total isospin is `C`-invariant
(`C : |T,T₃⟩ → |T,−T₃⟩` fixes `T`); and a `C`-invariant labelling of a
two-element set whose `C` is the swap is **constant**
(`isospin_const_of_conj_invariant`). No `T`-label can give one block `T = 1` and
the other `T = 0`.

**It is tempting to read that as closing the channel asymmetry outright.** It
does not, and the reason is purely combinatorial: the argument turns on there
being *one* `C`-orbit covering *both* blocks. The physical two-nucleon carrier
is six strands (3 per nucleon, forced — `StrandLayoutForcesChain` / `qou-gwr9`),
i.e. `H₆`, where `C` acts on 11 blocks. A `C`-invariant label is constant on
each **orbit**, not globally.

## Measured (exact; partitions and conjugation only)

[`conjugation_orbit_isospin_room_probe.py`](../../computations/probes/conjugation_orbit_isospin_room_probe.py),
reading fixed before counting (`orbits = 1` ⇒ C closes the layer; `orbits ≥ 2`
⇒ it does not):

| layer | blocks | `C`-orbits | self-conjugate | `C`-invariant `T` forced constant? |
|---|--:|--:|--:|---|
| pair `H₂` | 2 | **1** | 0 | **yes** |
| two-nucleon `H₆` | 11 | **6** | 1 — `(3,2,1)` | **no** |

`H₆` orbits: `(6)↔(1⁶)`, `(5,1)↔(2,1⁴)`, `(4,2)↔(2,2,1,1)`,
`(4,1,1)↔(3,1,1,1)`, `(3,3)↔(2,2,2)`, and the self-conjugate `(3,2,1)`.

The `n = 2` row **reproduces `PairIsospinAssignment` independently** (1 orbit ⇒
constant ⇒ impossible), which is the check that the method is reading the same
structure the Lean does. The `n = 6` row is the new content: **6 independent
values available**, so charge conjugation alone does not force a constant
labelling there.

## Consequence — do not over-extend either result

This is an instance of the standing rule that attributes do not transfer across
layers merely because they share a name:

- **`PairIsospinAssignment` closes the pair layer and only the pair layer.** It
  must **not** be cited as closing the six-strand channel question. Its
  mechanism (a single `C`-orbit) is absent at `n = 6`.
- **The six-strand layer is bound by a different obstruction** — the crossing
  budget: with `s = 3` forced, a block exchange has `c = s² = 9` inter-nucleon
  crossings and the achievable asymmetry is `R ≤ 9` against nature's `33.7055`
  ([`channel_asymmetry_crossing_budget_bound_probe`](../../computations/probes/channel_asymmetry_crossing_budget_bound_probe.py),
  [audit](2026-09-04-channel-asymmetry-crossing-budget-class-bound.md)).
  Charge conjugation has nothing to do with that bound.

**Two layers, two different obstructions, and neither subsumes the other.** The
pair layer cannot *label* the distinction; the six-strand layer can label it but
cannot *reach the magnitude*. Reporting either as "the" closure would be wrong
in both directions.

## What this does NOT claim

- **NOT** that a `T`-labelling of `H₆` blocks exists — only that `C` does not
  forbid one. Six orbits is room, not a construction.
- **NOT** a refutation of `PairIsospinAssignment`, which stands exactly as
  proved at `n = 2`.
- **NOT** that the binding gap or the channel asymmetry is closed. Neither is.

## Cross-references

- [`PairIsospinAssignment.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/PairIsospinAssignment.lean) — the `n = 2` impossibility.
- [`2026-09-04-channel-asymmetry-crossing-budget-class-bound.md`](2026-09-04-channel-asymmetry-crossing-budget-class-bound.md) — the six-strand budget bound.
- [`two_nucleon_linking_matrix_channel_blind_probe.py`](../../computations/probes/two_nucleon_linking_matrix_channel_blind_probe.py) — both channels at `I₃ = 0`.
- [`StrandLayoutForcesChain.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/StrandLayoutForcesChain.lean) / `qou-gwr9` — `s = 3` forced.
