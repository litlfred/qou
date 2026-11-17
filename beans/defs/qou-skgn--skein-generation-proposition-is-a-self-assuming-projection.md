---
# qou-skgn
title: prop:skein-generation is a self-assuming projection — the class field IS the conclusion
status: in-progress
type: task
priority: medium
tags:
    - reorg-2026-10-04
    - 8f-decide
created_at: 2026-08-30T08:20:00Z
updated_at: 2026-10-10T07:40:12Z
parent: qou-8lxd
pr: 8229
---

Found on `origin/main` while diffing the `qou-scrx` collision pairs. Not a
q-RH-arc item; recorded because it is load-bearing and because §3b-cond names
this exact shape.

## The defect

`folio/quantum-observable-universe/lean/QOU/Torsion/skein_generation.lean`:

```lean
class SkeinGenerationContext (R Skein FundamentalKnotIndex : Type*) … where
  fundamentalKnot : FundamentalKnotIndex → Skein
  hopfLink : Skein
  generation_top : Algebra.adjoin R (range fundamentalKnot ∪ {hopfLink}) = ⊤

theorem skein_generation … (h : Skein) :
    h ∈ Algebra.adjoin R (range ctx.fundamentalKnot ∪ {ctx.hopfLink}) := by
  rw [ctx.generation_top]
  exact Algebra.mem_top
```

The narrative (`mass-theory/skein-generation.md`) opens: *"The Skein module
`Sk_q` **is generated** as an algebra by the fundamental knot types and the Hopf
link."* That sentence **is** `generation_top`. So the class carries the block's
own conclusion as a field and the theorem projects it — the vacuous
self-assuming projection AGENTS.md §3b-cond item 5 defines, verbatim:

> *"A class that carries the block's own conclusion as a field, with a 'theorem'
> that merely projects it, is a vacuous self-assuming projection — it satisfies
> the propagation audit yet fails `proof-statement-integrity`."*

**The block is `prop:skein-generation`, kind `proposition`** — a provable kind,
not a conjecture. So this is not the sanctioned "open conjecture as a
content-bearing class with no instance" disposition; it is a proposition whose
Lean derives nothing.

## Second, independent problem: the theorem over-claims relative to the prose

The narrative's second claim is *"Every **hadron** admits a terminal Skein
resolution into a finite polynomial in these generators with coefficients in
`ℤ[q^{±1}]`."* The theorem concludes membership for **every** `h : Skein`, with
no hadron restriction, no finiteness, and no coefficient ring. Three of the
four content words in the sentence are absent from the formalisation.

Notably the **scratch** copy `QOU/scratch_skein.lean` — debris in every other
respect, see `qou-scrx` — is closer here: it carries `Hadron : Skein → Prop` and
restricts the conclusion to hadrons. It is still a projection, but of the right
proposition. **Do not delete it before this bean is resolved**, or the corpus
loses its only hadron-restricted statement of the claim.

## Dispositions, and why this needs the author

Three honest routes; picking among them is a judgement about what the
proposition is meant to assert, which is the author's call, not a mechanical
repair:

1. **Demote to `conj:skein-generation`.** Generation of the Skein module by
   torus knots plus the Hopf link is a real mathematical claim about `Sk_q`; if
   it is not proved here, a conjecture carrier is the honest kind. Cascade would
   need measuring (§3b propagation over its `uses[]` consumers).
2. **Keep it a proposition and make the class carry genuine sub-hypotheses** —
   the §3b-cond item-5 remedy: fields encoding the *inputs* (a spanning
   property, a resolution algorithm terminating) from which membership is
   *derived*, rather than a field asserting membership is total.
3. **Restate at the narrative's actual strength** — hadron-restricted, with
   finiteness and the `ℤ[q^{±1}]` coefficient ring — which is a strictly harder
   and more interesting formalisation than either copy has.

Recommendation, marked as my judgement: **(1) now, (3) later.** The claim reads
like a conjecture about the Skein module's structure, and demoting is cheap and
reversible; (2) risks producing another projection with more steps.

**Default if nothing is done:** the proposition stays, the audit family keeps
passing it (it has no `sorry`, no `axiom`, no `True`), and the corpus keeps a
provable-kind block whose Lean asserts its own premise. That is the state today
— nothing breaks, and nothing catches it either.

## Blast radius — unmeasured

I did not measure the `uses[]` consumers of `prop:skein-generation`; route (1)
would need that first, since demoting a proposition propagates. Measure before
acting.


--------

## RESOLVED 2026-09-02 by route (2). My own recommendation of route (1) was WRONG.

### The blast radius, finally measured — and it kills route (1)

This bean said *"Blast radius — unmeasured … Measure before acting."* Measured now,
by transitive closure over `uses[]` across every `.ts` in the paper:

**437 downstream blocks.** Of those, §3b would force a demotion on:

| kind | count | §3b consequence |
|---|---|---|
| proposition | **63** | must demote |
| theorem | **5** | must demote |
| lemma | **3** | must demote |
| proof | **44** | → `remark` + `interprets:` |

The cone contains `thm:knot-mass-formula-unified`, `prop:categorical-proton-*`,
`prop:markov-trace-*`, `def:three-calibration-discipline`, the α_EM chain and
the whole mass-formula spine.

**So my recommendation in this bean — *"(1) now, (3) later … demoting is cheap
and reversible"* — was wrong**, and it was wrong precisely because I made it
with the blast radius unmeasured and then said so in the same breath. Demoting
one proposition would have demoted ~115 provable blocks. Route (1) is off the
table.

### What was done instead: route (2), the §3b-cond item-5 remedy

`SkeinGenerationContext` no longer carries `generation_top` (the conclusion).
It now carries the **inputs to** generation:

* `complexity : Skein → ℕ` — crossing number in the intended model;
* `base` — complexity `0` ⟹ already in the generated subalgebra;
* `resolve` — positive complexity ⟹ expressible via the generators plus
  **finitely many strictly simpler** elements.

`skein_generation` is now a genuine strong induction on `complexity`
(`mem_adjoin_of_complexity_eq`), and `skein_generation_top` — the `= ⊤`
statement that used to be the *hypothesis* — is now a **consequence**. The
direction of implication is flipped, which is the whole point.

Three declarations, `lean`-direct exit 0, all `#print axioms`-clean
(`[propext, Classical.choice, Quot.sound]`).

**The `Finset` in `resolve` is not incidental** — it encodes the narrative's
*"finite polynomial"*, which the previous encoding dropped entirely.

**Non-vacuity witness added, deliberately as a `def` and NOT an `instance`.**
As an instance it would apply to every `Skein` by resolution, silently
discharging the hypothesis everywhere and re-creating the exact defect being
removed.

### Still open — route (3), and now the only part left

The formalisation carries two of the narrative sentence's four content words.
Still absent:

* **hadron restriction** — conclusion is for every `h : Skein`, prose says
  *"every **hadron**"*. `QOU/scratch_skein.lean` is still the corpus's only
  hadron-restricted statement; **do not delete it** (`qou-scrx`).
* **`ℤ[q^{±1}]` coefficients** — `R` is an arbitrary `CommRing`.

Both are now recorded in the module docstring under "What is still NOT
formalised", so the file no longer reads as stronger than it is.

**No cascade from this change**: the block stays a `proposition`, so nothing
propagates. Its `lean.ref` (`qou:QOU.Torsion.skein_generation`) is unchanged.


## Re-filed `8f-lean` -> `8f-decide` 2026-10-10

The 2026-10-10 front tagging put this in `8f-lean` (mechanical Lean work) on the
strength of its title — "self-assuming projection" reads like a defect to repair.
**Reading the body corrects that.** This bean states, in its own words, that
picking among its three dispositions *"is a judgement about what the proposition
is meant to assert, which is the author's call, not a mechanical repair"*, and it
already carries the three routes plus a recommendation.

So it is owner-gated, and it was making `8f-lean` look one item larger than it
is. Nothing about the diagnosis changes; only where it sits.

**Not actioned, deliberately.** I did not pick among (1) demote to
`conj:skein-generation`, (2) make the class carry genuine sub-hypotheses per
§3b-cond item 5, or (3) restate at the narrative's actual strength
(hadron-restricted, finite, `Z[q^{+-1}]` coefficients). The prior agent's
recommendation — (1) now, (3) later — stands as the thing to approve or overrule.

Also still live from the body: **do not delete `QOU/scratch_skein.lean` before
this resolves.** It is debris in every other respect (`qou-scrx`) but it is the
corpus's only hadron-restricted statement of the claim.

## Implementation Note (PR #8229)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/SkeinResolutionQuarkWritheBalanceWorpitzkyDecupletOrderedContentAndGenerationFilters.lean` and `computations/probes/skein_resolution_quark_writhe_balance_worpitzky_decuplet_ordered_content_and_generation_filters_probe.py` (witness `computations/probes/skein-resolution-quark-writhe-balance-worpitzky-decuplet-ordered-content-and-generation-filters.witness.json`, `f1cdc284e299c69db7b5cdefc55f5ba3d747a9ab`).
