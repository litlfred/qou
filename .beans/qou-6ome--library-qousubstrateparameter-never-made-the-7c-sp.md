---
# qou-6ome
title: Library QOU.SubstrateParameter never made the §7c split its own block and siblings made — 22 files, 85 field sites, carries q0
status: todo
type: task
created_at: 2026-08-23T12:48:18Z
updated_at: 2026-08-23T12:48:18Z
---


## The gap

Surfaced while characterising option 3 of [`qou-u87j`](qou-u87j--43-content-block-lean-siblings-redefine-a-library.md)
(mirror drift). Two of that bean's 46 drifted pairs are this one object, and it
is the case that showed the whole "resync the mirrors" plan needed rethinking.

Three statements of the same structure, and the library is the odd one out:

| where | shape |
|---|---|
| **block** `substrate-parameter.md` | "The **substrate parameter** $q \in \mathrm{End}(\mathbf{1})$" — categorical. No ordering, no `q ≥ 1`, no ℝ. |
| **siblings** `quantum-observable-universes/substrate-parameter.lean:72`, `quantum-gauge-group.lean:44` | `structure SubstrateParameter (M) where field : M → R_q` — categorical, one field. Archimedean properties moved to a separate `ArchimedeanSubstrateField`. |
| **library** `lean/QOU/QuantumObservableUniverse/SubstrateParameter.lean:23` | `field : M → ℝ`, `field_pos`, `field_ge_one`, `not_root_of_unity` — single-layer, wholly archimedean. |

The siblings say why, in their own docstring:

> the archimedean properties (`q(p) > 0`, `q(p) ≥ 1`, not a root of unity) live
> on `ArchimedeanSubstrateField` below, **after the substrate→archimedean wall
> (AGENTS.md §7c)**.

So the §7c migration reached the block and the siblings and **never reached the
library**. The block is the authority and the library disagrees with it.

## Why no gate caught it

`check-wall-side` and `check-base-ring` both **PASS** on the library file.
That is correct behaviour and worth understanding before trusting either:
they fire on a file that *mixes* algebraic and archimedean regimes. A file that
is **wholly** on the wrong side of the wall is not mixed, so it passes.

> Passing the wall gate means "not mixed". It does not mean "on the right side
> of the wall".

That is a real hole in §7c enforcement, and it is not specific to this file.
Worth its own thought: a checker that compares a declaration's regime against
its **block's** stated regime would catch it; nothing does that today.

## Blast radius — measured, not estimated

- **22 library files** mention `SubstrateParameter`.
- **85 field-access sites** (`.field`, `.field_pos`, `.field_ge_one`, `.not_root_of_unity`).
- It carries **q₀**. Every mass number in the corpus is downstream, so this
  needs a numerical no-change check, not just a green build.

Heaviest consumers: `Elaboration.lean` (10), `AppendixSurreals/collatz_substrate_link.lean`
(10), `PhotonThreading.lean` (9), `MathConstants.lean` (8), `InformationTheory.lean` (7),
`QuantumObservableUniverse/Propositions.lean` (6), `GaugeFieldFluidDynamics.lean` (6).

## Shape of the fix

The same split already done for `MassIdentity` → `ArchimedeanMassIdentity`
(PR #5458), on a much larger object:

1. `SubstrateParameter M` — categorical core, `field : M → R_q` (or a generic
   `{R : Type*} [CommRing R]`), matching the block and the siblings.
2. `ArchimedeanSubstrateField M` — `field : M → ℝ` plus the classicality bound,
   with `field_pos` and the rest derived where they can be rather than posited.
   The siblings already derive positivity from `field_ge_one`; the library
   posits both.
3. Move every archimedean consumer onto layer 2. `quantumPlanckConstant` and
   its two lemmas are the obvious first ones — they consume `field_ge_one` and
   `field_pos` directly.

**The tie between the layers is the part to get right, not to assume.**
[`qou-mt7r`](qou-mt7r--gap-q-real-in-markovtracecontext-descendants-is-untethered.md)
reaches the same design need from a different direction — an
archimedean-evaluation (τ) field carrying `eval q = q_real` as its law — and
says the thing worth repeating here: *positing the coherence without the functor
would be assumption dressed as structure.* Whatever τ this split introduces
should be the one `qou-mt7r` needs, not a second parallel mechanism.

## Related, and deliberately not merged into

- [`qou-u87j`](qou-u87j--43-content-block-lean-siblings-redefine-a-library.md) —
  parent finding (mirror drift). This is 2 of its 46, and its largest case.
- [`qou-mt7r`](qou-mt7r--gap-q-real-in-markovtracecontext-descendants-is-untethered.md) —
  untied `q_real` in `MarkovTraceContext` descendants. Different structure
  family, same missing τ.
- `qreal` — closed into `qou-mt7r`; kept for its corrected file list.

## Not started

Deliberately. This is a q₀-adjacent refactor of the most load-bearing object in
the corpus; it wants its own branch and a numerical no-change check, and it
should not be started at the tail of a session doing something else.
