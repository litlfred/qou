# `S² = id` for the QOU substrate antipode is INDEPENDENT, not open

**Date** 2026-09-14 · **Bean** `qou-qjhc` (parent), `qou-c64q` (this finding)
· **Branch** `claude/duality-sigma-hermitian-derivation-2026-09-14`

## The claim

`def:frobenius-hopf-substrate` contains **no antipode axiom**. The Hopf
condition `μ ∘ (S ⊗ id) ∘ Δ = η ∘ ε` appears nowhere in the block, in either
of its two Lean carriers, or anywhere downstream. `S` is therefore
**free data**: it satisfies no law, so no property of it is derivable — and
none is refutable either.

So the correct answer to *"does `S² = id` hold for the QOU substrate?"* is
neither yes nor no. It is **independent of the definition as it stands**,
which is a different epistemic state from "unproved" and a different one
again from "false".

### I had this wrong, and the correction matters for what to do next

Bean `qou-qjhc` (my own text, 2026-09-13) recommended `S² = id` as *"the
cheapest of the three gaps to settle — a single missing theorem in
`def:frobenius-hopf-substrate`"*. **That is wrong.** It is not a missing
theorem; it is a missing **axiom**. Adding one is a change to a central
definition, which §"ASK THE OWNER BEFORE CHANGING THINGS" reserves to the
owner, and §"Axiomatization is NOT a Proof" forbids doing in order to unblock
a downstream consumer. The gap is not cheap — it is *not an agent's to close
at all*.

## The evidence

### A prior QA reviewer already found this, in prose

The corpus-grep checklist turns up the finding already recorded, in the QA
sidecar of the block itself —
`quantum-observable-universes/frobenius-hopf-substrate.qa.json`, criterion
`trap-nonspeakable`, reviewer `agent:d02`, verbatim:

> **(2) THE ANTIPODE IS UNCONSTRAINED.** S appears in the sextuple and is
> named in axiom 2, but no axiom relates it to anything — the Hopf antipode
> condition `mu . (S tensor id) . Delta = eta . epsilon` is missing, so S is
> free data. What axiom 2 actually states (`epsilon . mu = u . (epsilon
> tensor epsilon)`) is multiplicativity of the counit, not a Hopf
> compatibility involving S.

That reading is confirmed against the block's own text. Axiom 2 of
`frobenius-hopf-substrate.md` reads, verbatim:

> the morphisms `Δ : A → A ⊗ A` and `ε : A → 1` make `A` a coassociative
> counital coalgebra object, **with antipode `S : A → A` satisfying the Hopf
> compatibility `ε ∘ μ = u ∘ (ε ⊗ ε)`**

`S` occurs on the left of "satisfying" and in **neither side** of the equation
that follows it. The sentence reads as though it constrains `S` and does not.

**So this audit is not the discovery.** What is new here is (a) machine-checking
it, (b) finding the same hole in the *library* carrier the categorical
Lagrangian actually consumes, (c) finding that `unit` and `counit` are free
data too, and (d) measuring what assuming `S² = id` would cost.

### Mechanical, both carriers, same answer

[`scripts/lean-structure-field-law-audit.py`](../../scripts/lean-structure-field-law-audit.py)
strips docstrings and comments **first** — so a field described at length in
prose and constrained by nothing scores zero, which is exactly this case —
then counts occurrences of each data field's name in the *types* of the law
fields.

```
$ python3 scripts/lean-structure-field-law-audit.py \
    content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean \
    FrobeniusHopfData
  DATA fields : ['obj','mul','unit','comul','counit','antipode','frobeniusForm','coevaluation']
  LAW  fields : ['pairing_snake_left','pairing_snake_right','frobenius_relation']

    obj              CONSTRAINED          mentions-in-laws=21
    mul              CONSTRAINED          mentions-in-laws=4
    unit             *** FREE DATA ***    mentions-in-laws=0
    comul            CONSTRAINED          mentions-in-laws=2
    counit           *** FREE DATA ***    mentions-in-laws=0
    antipode         *** FREE DATA ***    mentions-in-laws=0
    frobeniusForm    CONSTRAINED          mentions-in-laws=2
    coevaluation     CONSTRAINED          mentions-in-laws=2
```

The content-block sibling
`quantum-observable-universes/frobenius-hopf-substrate.lean`
(`FrobeniusHopfSubstrate`) has a *different* law set — it carries `mul_assoc`,
which the library version does not — and gives the **identical** verdict:
`unit`, `counit`, `antipode` free.

Two carriers, different laws, same three free fields. This is not an artifact
of one file.

### Machine-checked in Lean

[`QOU/QuantumObservableUniverse/AntipodeIndependence.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/AntipodeIndependence.lean)
— `lean`-direct `-DautoImplicit=false -s 65536` **exit 0**, zero warnings,
sorry-free; `#print axioms` on all seven declarations reports no axioms at all
except `propext` on the two that use `simp only`.

| declaration | says |
|---|---|
| `withAntipode` / `withUnit` / `withCounit` | replace the field with **anything**; the same three proofs discharge the same three laws |
| `antipode_property_vacuous` | any property provable of *every* substrate's antipode holds of *every* endomorphism of *every* substrate object |
| `unit_property_vacuous`, `counit_property_vacuous` | likewise |
| `involutive_of_sq_eq_id` | if `S ≫ S = 𝟙` were a theorem, every endomorphism of every Frobenius–Hopf object would be an involution |
| `endo_comm_of_antipode_sq_eq_id` | …hence every such endomorphism monoid would be **commutative** |
| `id_eq_zero_of_antipode_sq_eq_id` | …and, in any ambient category with zero morphisms, `𝟙_A = 0` — every Frobenius–Hopf object would be a **zero object** |

The last row is the decisive one and needs no model: take `g = 0` in
`involutive_of_sq_eq_id`; `0 ≫ 0 = 0`, so `0 = 𝟙_A`. The QOU ambient category
is `k`-linear, hence has zero morphisms. So `S² = id` is not merely
underivable from the present axioms — **it cannot be made derivable by adding
axioms that do not mention `S`.** Any route to it must constrain `S`
specifically.

### The one place the corpus does "prove" `S² = id`, and why it is empty

`braids-and-knots/frobenius-antipode-lean-stub.lean` carries
`QOU.BraidKnot.antipode_involution : antipodeS n q (antipodeS n q a) = a`,
proved `rfl`. It is `rfl` because the file defines

```lean
def antipodeS (_n : ℕ) (_q : ℝ) : HeckeAlgebra _n _q → HeckeAlgebra _n _q := id
```

— the antipode **is** the identity function on a one-real-number model whose
generators are all `0` and whose multiplication is real multiplication. The
file says so itself, and
[`2026-09-06-q-analysis-uniqueness-axioms-are-false.md` §Addendum](2026-09-06-q-analysis-uniqueness-axioms-are-false.md)
already lists it in the vacuous class. **Do not cite it as establishing
`S² = id`.**

Worth noting in passing: that model's multiplication is commutative — exactly
what `endo_comm_of_antipode_sq_eq_id` says `S² = id` forces. The one model in
the corpus where `S² = id` holds is the one where the cost has already been
paid.

## Implications

**For the Lagrangian route.** `qou-qjhc` needed `S² = id` to make
`ψ* = ∫_A ∘ S(ψ)` an involution, which is what would let the categorical
Lagrangian's duality be identified with complex conjugation *intrinsically*
rather than via the archimedean signature argument of
[`2026-09-14-duality-sigma-is-conjugation-derivation.md`](2026-09-14-duality-sigma-is-conjugation-derivation.md).
That route is **not cheap and is not blocked on a proof** — it is blocked on a
definition the owner has not written. The signature argument stands on its own
and is unaffected.

**For `unit` and `counit`.** The same hole, twice more. `def:frobenius-hopf-substrate`
names a Hopf algebra and constrains neither the unit nor the counit — so the
unit laws `η ⊗ id ≫ μ = id` and the counit laws are absent as well. Nothing in
this session depended on them, and they are recorded here rather than acted on.

**Blast radius, named.** The blocks that would move if an antipode axiom were
added are `mass-theory/frobenius-antipode-unifies-chirality-and-tower`,
`mass-theory/frobenius-antipode-neutron-tower-closure`, and
`braids-and-knots/frobenius-antipode-lean-stub.lean`. The first two are the
Term-5 chirality and neutron-tower arcs — the physics side of the corpus, not
merely its call graph. None of them currently derives anything *from* an
antipode law (there is none to derive from); what they would gain is the
ability to.

## What is NOT established here

- **Not** that `S² = id` is false for the intended substrate. It is not
  stated, so it has no truth value in the present formalisation.
- **Not** that it *should* be added. For `U_q(g)` the antipode satisfies
  `S² = ` conjugation by `K_{2ρ}`, which is **not** the identity; and the QOU
  ambient category is braided, not symmetric. So a genuinely `q`-deformed
  substrate would plausibly want `S² ≠ id`. That is an argument for care, not
  a measurement, and it is flagged as such.
- **Not** a proposal to add an axiom to unblock a consumer. §"Axiomatization
  is NOT a Proof" forbids exactly that move, and it is the move the shape of
  this gap invites.

## Precedent for how this gets decided

Bean `qou-t7mt` is the same shape one axiom over: the block's axioms 4–5
presupposed a dual the Lean does not need. It was held as *"not
agent-actionable — needs owner pick, not agent work"* for three weeks, put to
the owner as three explicit rewordings, and resolved by the owner choosing
one. The antipode hole is a larger version of that, and takes the same route.
