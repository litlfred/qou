---
# qou-mt7r
title: 'GAP: q_real in MarkovTraceContext descendants is untethered from the inherited q'
status: completed
type: task
priority: medium
tags:
    - lean
    - 7c
    - wall
    - markovtrace
created_at: 2026-08-08T18:30:00Z
updated_at: 2026-08-24T06:56:29Z
---

Surfaced while working `qou-mtcx` (PR #4756). Not fixed there — fixing it needs
new structure, not a re-typing, so it is filed rather than guessed at.

## The gap

Three descendants of `QOU.Shared.MarkovTraceContext` correctly live on the
archimedean side of the §7c wall and correctly declare a `q_real : ℝ`:

| file | why it is genuinely `ℝ` |
|---|---|
| `QOU/Information/reeb_operations_per_planck.lean` | `1 < q_real`, `div_pos`, `linarith` |
| `QOU/Information/toffoli_transfer_matrix.lean` | `Real.sqrt q_real` in the `P_{7,7}` closed form |
| `QOU/Observations/strangelet_crossing_energy.lean` | `0 < q_real` hypotheses, `inv_pos`, `linarith` |

**But nothing in any of them relates `q_real` to the inherited `q : R`.** The
docstrings call `q_real` "the specialisation of the generic shared `q : R`",
and the *type* says no such thing: `q_real` is an independent field. A context
instance may set `q_real := 37` while the Hecke algebra it carries is built
over an entirely unrelated `q`, and every one of these propositions still holds
vacuously-consistently.

So the claims are archimedean statements about *a* real number, not about
*this* universe's substrate parameter. This is the same defect class as the
dead shadows removed in `mobius_energy` / `wedderburn_bratteli_recursion` under
`qou-mtcx` — except that in those two the field was unused, so deleting it was
the whole fix. Here the field is load-bearing and cannot simply be dropped.

## Why it was not fixed under qou-mtcx

The honest tie is an **archimedean evaluation** `R → ℝ` — the `τ` fibre functor
/ Archimedean functor of the canonical derivation chain — carried as a context
field with `eval q = q_real` as its coherence law. `MarkovTraceContext` does
not carry one, and inventing a `RingHom R ℝ` field on the shared parent is a
real design decision affecting all 15 descendants, not a mechanical edit. Per
the anti-laundering rule, adding a field that merely *posits* `eval q = q_real`
without the functor being the real archimedean evaluation would be assumption
dressed as structure.

## Candidate routes (none validated)

1. **Extend the parent** with an optional archimedean-evaluation mixin
   (`class ArchimedeanEval extends MarkovTraceContext where eval : R →+* ℝ`),
   and have the three archimedean descendants extend *that* instead, replacing
   `q_real` with `eval q`. Cleanest; touches the shared parent, so it needs the
   blast-radius check `qou-mtcx` taught (read the parent before costing it).
2. **Per-file coherence field** — keep `q_real` but add
   `q_real_eq : eval q = q_real` with a per-file `eval`. Cheaper, duplicates
   the functor three times.
3. **Leave as is, documented.** Currently in force: each of the three files
   carries a §7c note naming this bean. Acceptable only as an interim state.

## Verification note for whoever takes this

`-DautoImplicit=false` is mandatory (it is hardcoded in
`scripts/lean_cone_build.py`, and `LEAN_CONE_EXTRA_ARGS` is appended to it, not
a substitute). Without it a field mentioning `R` auto-binds a fresh implicit
and a no-op change compiles green. Never `lake build`.

## Summary of Changes — 2026-08-24

Route 1, varied: a **sibling mixin** `QOU/Shared/ArchimedeanEval.lean` rather
than extending `MarkovTraceContext`. It carries `eval : R →+* ℝ` and *derives*
`q_real := eval q`; the independent field is deleted from all three
descendants. Commit `de221f5f64`.

`ctx.q_real` reads identically at every call site — dot notation resolves
through the parent exactly as it resolved to the field, the same trick
`qou-6ome` used for `field_pos`.

### What the tie buys, machine-checked

`ArchimedeanEval.q_real_one_of_q_one : q = 1 → q_real = 1`. One line from
`eval` being a ring hom, and **not provable at all** before. It bites hardest in
`toffoli_transfer_matrix`, whose sub-claim (v) *is* a classical limit
(`q_real = 1 → P_flip k = 0`) — previously satisfiable at `q_real = 1` with the
substrate parameter anywhere at all.

### Why not route 1 as written

`MarkovTraceContext` has **15** descendants; only 3 are archimedean. Putting a
map to `ℝ` on the parent gives the other 12 an archimedean field they have no
business carrying — the §7c wall in reverse. The mixin costs the three one word
in `extends` and leaves the twelve untouched. Blast radius: 4 files.

### The anti-laundering rule, respected explicitly

This bean's own warning was that positing `eval q = q_real` without the functor
"would be assumption dressed as structure". So the module says outright that it
is **not** the τ-functor, and `ArchimedeanEval.ofRingHom` machine-checks the
point: an instance is buildable from *any* ring hom — no functoriality, no
naturality, no braided category. Modelled on
`TauFunctorTargetSpec.interface_alone_is_trivially_inhabitable`, which does the
same for its interface.

The distinction that makes this honest rather than laundering: the mixin does
not claim `eval` *is* the archimedean evaluation. It claims `q_real` is *some*
ring-homomorphic image of `q`, which is strictly more than "an unrelated real"
and strictly less than the functor.

### Not a second parallel mechanism

The bean warns the τ should be shared with `qou-6ome`, not duplicated. It is:
the mechanism is `RingHom _ ℝ`, already in Mathlib, and `ArchimedeanEval` is
`MarkovTraceContext` plus one. Recorded in the docstring for whoever does the
`qou-6ome` side, together with the asymmetry that matters there — `R_q` is
`LaurentPolynomial ℤ`, so evaluation at a nonzero real is **constructible**, not
assumed. Here `R` is an opaque `CommRing` and `eval` must be a hypothesis.

### Residue

- **`eval` is still assumed.** The τ-functor that would supply it with
  provenance is open, and remains THE wall (`QOU/Archimedean/TauFunctorTargetSpec.lean`).
- **`qou-6ome`'s side is untouched.** `SubstrateParameter` /
  `ArchimedeanSubstrateField` are still untied. That is the follow-up, and it is
  the easier half because `eval` is constructible there.

### Verification

```
lean-direct-cone     exit 0 on all four modules
run-validate         30 issues, unchanged
mirror drift  @35    exit 0
duplicate decls @57  exit 0
```
