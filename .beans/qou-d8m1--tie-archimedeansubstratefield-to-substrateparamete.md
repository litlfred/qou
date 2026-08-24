---
# qou-d8m1
title: Tie ArchimedeanSubstrateField to SubstrateParameter — here eval is constructible, unlike qou-mt7r
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T06:57:02Z
updated_at: 2026-08-24T08:34:35Z
---

Follow-up left by `qou-6ome` and `qou-mt7r`.

## The gap

The §7c split (`qou-6ome`) gave the library two layers:

| layer | field |
|---|---|
| `SubstrateParameter M` | `field : M → QOU.GroundRing.R_q` (categorical) |
| `ArchimedeanSubstrateField M` | `field : M → ℝ` (order axioms) |

Nothing relates them. Same defect `qou-mt7r` just closed for the
`MarkovTraceContext` family: the archimedean layer's values are free of the
categorical layer's, so `field_ge_one` and `not_root_of_unity` constrain a real
function unconnected to this universe's substrate parameter.

## Why this half is EASIER than qou-mt7r, and the reason matters

In `qou-mt7r` the coefficient ring `R` is an opaque `CommRing`, so
`eval : R →+* ℝ` had to be **assumed** — see
`QOU/Shared/ArchimedeanEval.lean`, which says so and machine-checks how little
an instance costs (`ofRingHom`).

Here `R_q = LaurentPolynomial ℤ`. Evaluation at a nonzero real is an **ordinary
constructible ring hom**, not a hypothesis. So this side can carry a real
`ι : R_q →+* ℝ, q ↦ q₀` and derive `ArchimedeanSubstrateField.field := ι ∘ sp.field`
rather than positing coherence.

That makes it a genuinely stronger fix than the one `qou-mt7r` could manage,
and it is the reason not to copy that file wholesale.

## Do not build a second mechanism

Both sides want the same thing and it is not a new abstraction: it is
`RingHom _ ℝ`, already in Mathlib. Reuse it; do not invent a parallel notion.

## Still not the τ-functor

Constructibility of `ι` does not touch the archimedean τ-functor wall
(`QOU/Archimedean/TauFunctorTargetSpec.lean`). `ι` is an evaluation of the
ground ring; τ is a functor from the braided category. Do not let the first
being available read as progress on the second.

## Blast radius, not yet measured

20 library modules carry `ArchimedeanSubstrateField`. Whether the tie belongs on
that structure or on a mixin (as `qou-mt7r` chose, to spare 12 pre-archimedean
descendants) needs the same parent-first check before costing it.

## Summary of Changes — 2026-08-24

`QOU/Archimedean/GroundRingEval.lean` (commit `32e0d2f12a6`). The prediction in
this bean held: ι is **constructible** here, so nothing is assumed.

| declaration | what it gives |
|---|---|
| `evalAt (q0 : ℝˣ) : R_q →+* ℝ` | the specialisation, built from `AddMonoidAlgebra.lift ∘ zpowersHom` |
| `evalAt_T` | `T n ↦ q0 ^ n` — it really is substitution, not merely *some* ring hom |
| `evalAt_q_param`, `evalAt_q_inv_param` | the two named generators pinned |
| `evalAt_q_param_mul_inv` | the constructed hom respects `GroundRingCore`'s relation |
| `ArchimedeanRealisation` | categorical `sp` + `q0` + the order axioms *about the realised values* |
| `toArchimedeanSubstrateField` | the archimedean layer **produced**, not posited |
| `realised_one` | `sp.field p = 1 → realised = 1`, for every `q0` |

`evalAt_T` is the load-bearing one. Without it the definition would be
untethered in exactly the way this bean is about — a ring hom with no reason to
be called `q ↦ q₀`.

### The docstring that started it

`ArchimedeanSubstrateField` already *said* it was "obtained by specialising the
categorical field through `ι : R_q → ℝ, q ↦ q₀`". That was prose asserting a
tie the type did not carry. Corrected in place: the bare structure is now
documented as independent by construction, and points at
`ArchimedeanRealisation` for the specialisation the prose meant. A stale "all
four fields are unchanged" went with it — `field_pos` became a theorem under
`qou-6ome`, so there are three.

### `q0 : ℝˣ`, not a real with a side condition

The indeterminate is invertible in `ℤ[q, q⁻¹]`, so any evaluation must send it
to a unit. Taking `ℝˣ` is not a convenience: a plain real with `q0 ≠ 0` would
need the inverse rebuilt at every use, and over a general codomain nonzero
would not even suffice. Same distinction `CategoricalQExtDeriv` hit under
`qou-u87j`.

### Residue — what is still assumed, and correctly

- **The order axioms.** `1 ≤ q0^n` and "not a root of unity" are archimedean
  facts about the chosen `q0`, not consequences of the categorical layer. They
  stay hypotheses; what stopped being a hypothesis is the *field*.
- **Nothing forces existing call sites through the tie.** The bare
  `ArchimedeanSubstrateField` is still constructible directly, and the 20
  modules carrying it were left alone. Migrating them is separate work and
  wants its own measurement — this bean was about making the tie *available*
  and honest, not about sweeping the corpus onto it.
- **Not the τ-functor.** ι evaluates the ground ring; τ is a functor from the
  braided category (`TauFunctorTargetSpec`, still open). ι turning out to be
  constructible says nothing about τ and must not be cited as progress on it.

### Verification

```
lean-direct-cone     exit 0 — GroundRingEval, SubstrateParameter, QuantumObservableUniverse
#print axioms        propext / Classical.choice / Quot.sound only — no sorry, no custom axiom
run-validate         30 issues, unchanged
mirror drift  @35    exit 0
duplicate decls @57  exit 0
```

One process note worth keeping: the first gate run in this container reported a
plausible-looking failure that was actually `exit 2`, module-not-found — the
folio-assistant checkout predated the #132 merge and `>/dev/null 2>&1` hid the
reason. Third time this shape has bitten in this arc: a tool that returns a
status without examining anything is indistinguishable from one that did.
