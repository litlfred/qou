# Searching for a flavour-versus-colour discriminator

**Date:** 2026-08-26
**Branch:** `claude/8-fold-way-qou-k4e8ch` (PR #5819)
**Bean:** `qou-8pl3`, gap (ii)
**Lean:** `content/quantum-observable-universe/lean/QOU/Eightfold/FlavourColourDiscriminator.lean`

## The question

Open-problem item 4 asks whether the octonionic (colour) `SU(3)` and the
eightfold-way (flavour) `SU(3)` are the same, different, or related by a
groupoid-level duality. Two invariants have been tried and **both are proved
blind**:

| Invariant | Blindness | Proved in |
|---|---|---|
| `Sym²` gate | at dim 3, passing ⟺ complex type, so any two passing triples get the same verdict | `gate_does_not_separate_two_triples` |
| `ℤ/3` triality grading | `2` is a unit in `ℤ/3`, so every verdict survives the identification | `identification_invisible_to_selection_rule` |

Item 4 concluded *"Whatever separates flavour from colour lies elsewhere."*
This is the search for the elsewhere.

## Result 1 — the two blindnesses are one blindness, and it is a class

Both gates read only **object-level** data: a dimension, a Frobenius–Schur type,
a triality class. On that data the two triples **coincide**, and by two
genuinely different routes:

| | colour | flavour |
|---|---|---|
| origin | the `ℂ³` of `Im(𝕆) = ℝ ⊕ ℂ³` | the fundamental, Dynkin label `(1,0)` |
| dimension | `(7−1)/2 = 3` | Weyl: `2·1·3/2 = 3` |
| FS type | complex *(Günaydin–Gürsey, cited)* | complex *(derived: triality `1 ≠ 0`)* |
| triality | `1` | `1` |

`no_object_gate_separates` turns this into a **scope-(b) structural exclusion of
a class of discriminators**: no gate reading only object data separates them.
The invariant is named — equal data, equal verdict. So the two observed failures
were never repairable, and there is no third gate of that kind to look for.

**Verified non-vacuous by mutation.** Perturbing the octonion dimension
`(7−1)/2 → (7−1)/3`, or the flavour FS type `complex → real`, makes `decide`
prove the data equality **false**. The `decide` is computing, not rubber-stamping.

### What the class exclusion forecloses

`tensor_cube_gates_also_blind` makes it concrete. After `Sym²` fails, the
instinct is the next tensor functor — `Sym³`, or `Λ³`, which looks especially
promising because its singlet *is* the colour `ε_{abc}`. Both dimensions are
functions of `dim V` alone (`Sym³` gives `10` for both triples, `Λ³` gives `1`
for both), so a gate reading either is a gate reading `ObjectData`, already
covered. **The whole "try another tensor construction on `V`" family is dead
without running any of it.**

### One claim deliberately NOT made

This does **not** say the two triples are isomorphic. That would beg item 4's
question — they are a priori representations of two different groups, and
whether those groups are identified is exactly what is open. The claim is only
that *the data these gates read* coincides, which is weaker and sufficient.

## Result 2 — where a discriminator can live

The obstruction lifts as soon as a gate may read one more thing: **which
Young-symmetry channel of `V ⊗ V ⊗ V` carries the physical state.**

| role | channel | `S₃`-irrep |
|---|---|---|
| colour | `λ = (1³)`, totally antisymmetric (`ε_{abc}`) | sign |
| flavour, decuplet | `λ = (3)`, symmetric | trivial |
| flavour, octet | `λ = (2,1)`, mixed | standard |

These are distinct irreps, and `some_channel_gate_separates` exhibits a gate
that tells them apart — a construction, not an existence claim. Note the colour
channel differs from **both** flavour channels, so the separation is not an
artefact of which multiplet is picked.

### The corpus already knew this, in the wrong place

**Items 4 and 7 are the same question.** Item 4 says the answer lies elsewhere;
item 7 — seven items down, filed as a selection-rule problem — names the
elsewhere: *"colour antisymmetric and spin symmetric force flavour symmetric."*
Neither item cited the other. Both now do.

This also raises item 7's stakes: deriving the colour-antisymmetry constraint
would settle more than the Young symmetriser — it would supply the one input
item 4 is missing.

## The circularity this does not escape

Assigning colour the antisymmetric channel is an **input, not a derivation**.
Item 7 states plainly that the chapter derives neither the spin factor nor the
colour antisymmetry. So Result 2 does not establish that flavour and colour
differ; it establishes that *if* the channel assignment is supplied, a gate can
see the difference, whereas no amount of object data ever could.

**The discriminator is located, not established.** Result 1 — the negative — is
what is actually settled, and it is the half that redirects the search.

## A second candidate, named but not pursued

**The symmetry-breaking spectrum.** Flavour `SU(3)` is broken and the corpus
already carries the breaking relations as Lean (`GellMannOkuboIdentity`,
`ColemanGlashowIdentity`, `DecupletEqualSpacing`); colour `SU(3)` is exact and
has no analogue, so a "breaking defect" invariant is nonzero for one and
identically zero for the other. Like the channel, this is data about the role
rather than the object, so Result 1 does not forbid it.

Not pursued here, and it carries the same hazard: the exactness of colour would
be an input unless derived. Recorded so the next agent has two locations rather
than one.

## Verification

- `lean`-direct **exit 0** against the real import cone (3403 Mathlib oleans;
  `Sym2GateFSTrichotomy.olean` and `TrialitySelectionRule.olean` from the merged
  branch).
- `#print axioms` on all seven declarations: `[propext, Classical.choice,
  Quot.sound]`, and `colourChannel_ne_flavourChannels` depends on none — no
  `sorryAx`.
- Zero `sorry`, zero `axiom`, no `native_decide`.
- Three mutation tests, each expected to fail and each failing.
