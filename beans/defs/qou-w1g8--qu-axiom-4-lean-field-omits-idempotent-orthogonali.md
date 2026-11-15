---
# qou-w1g8
title: QU axiom 4 Lean field omits idempotent orthogonality + completeness (needs Preadditive)
status: completed
type: task
priority: normal
created_at: 2026-08-15T00:23:28Z
updated_at: 2026-09-05T19:43:34Z
---


## What is and is not encoded

`QuantumUniverse.blocks/centralIdem/frobWeight/dimQ` (landed #5021) encodes:
finitely many blocks, an idempotent endomorphism per block, non-vanishing
Frobenius weight and quantum dimension.

It does NOT encode mutual orthogonality of the idempotents
(`b ≠ b' → p_b ≫ p_b' = 0`) or completeness of their sum (`Σ p_b = 𝟙`).
`QuantumUniverse` carries neither prerequisite, but **the two gaps cost
differently** and should not be worked as one:

| gap | needs | cost |
|---|---|---|
| orthogonality `p_b ≫ p_b' = 0` | `HasZeroMorphisms` — a zero morphism, nothing more | cheap |
| completeness `Σ p_b = 𝟙` | `Preadditive` — `AddCommGroup (X ⟶ Y)` for the finite sum | needs the decision below |

Orthogonality is addable on its own and is the larger share of what
"semisimple" is doing here. (Caught by Copilot on #5047; the first draft of
this bean, and the Lean docstrings merged in #5021, conflated the two.)

So the field as written is satisfied by a structure with idempotents that
overlap and do not span. That is weaker than "semisimple" and the docstring says
so, but the gap is real: the axiom's NAME promises Wedderburn and its TYPE
delivers less.

## The fix has a prerequisite
Adding `[Preadditive C]` to `QuantumUniverse` is the obvious route and is a
bigger decision than this bean — it changes what a quantum universe is, and the
paper's `R`-linear phrasing may already imply it (check `def:rigid-monoidal-category`
§"We say C is R-linear ..."). Do not add the instance without deciding that
question first.

## Cheap half DONE (2026-08-15)

`centralIdem_orthogonal : ∀ b b', b ≠ b' → p_b ≫ p_b' = 0` added to all three
synced copies, with `[zeroInst : HasZeroMorphisms C]` as the enabling instance
field. `lean`-direct exit 0 on each; no `sorry`.

This was the half Copilot's review on #5047 unblocked — the original bean text
claimed both halves were gated on the `Preadditive` decision, which was wrong
and would have left the valuable half unclaimed.

## Remaining: completeness only

`Σ p_b = 𝟙` still not encoded. It needs `Preadditive` (`AddCommGroup (X ⟶ Y)`
for the finite sum), which changes what a quantum universe *is*. Prerequisite
question unchanged: does the paper's `R`-linear phrasing already imply it?
See `def:rigid-monoidal-category` §"We say **C** is *R*-linear …". Do not add
the instance without settling that.

Note the axiom is now meaningfully stronger than it was: with orthogonality,
the blocks genuinely do not mix. What is missing is only that they *span*.

QUEUED-BLOCKED 2026-08-15 (session qou-pq8k): blocked on owner's Preadditive decision per the originating discussion. Not dispatched.


CAVEAT ANSWERED 2026-08-16 (bean qou-btq3): 'will existing instances still
typecheck under Preadditive/Linear' has no force — there are NO constructions of
QuantumUniverse. Existence is an axiom; QuantumObservableUniverse's is a cited
sorry. Both absorb a new structure field for free, with no proof obligation and
no checker firing. So the decision is not about breakage, it is about
strengthening an axiomatised existence claim silently. Also recorded there: the
structure ALREADY leans on k-linearity it does not carry (frobWeight/dimQ land
in k 'via the standard identification of End(1) with the ground ring of a
k-linear category'), so the gap is load-bearing today, independent of the
completeness question.


## 2026-08-16 — the prerequisite question is ANSWERED, and it is `Linear`, not `Preadditive`

This bean has been blocked since 2026-08-15 on: *"does the paper's `R`-linear
phrasing already imply it? See `def:rigid-monoidal-category` §'We say **C** is
*R*-linear …'. Do not add the instance without settling that."*

Read it. `rigid-monoidal-category.md`:

> We say **C** is *R-linear* for a commutative ring $R$ [without quasi-zeros]
> if **every hom-set is an $R$-module and composition is $R$-bilinear**.

Mathlib, `CategoryTheory/Linear/Basic.lean:43`:

    class Linear (R : Type w) [Semiring R] (C : Type u) [Category.{v} C]
        [Preadditive C] where
      homModule : ∀ X Y : C, Module R (X ⟶ Y)
      smul_comp : ...   -- composition is R-bilinear
      comp_smul : ...

That is the same sentence. So **yes, the paper's phrasing implies it**, and
`quantum-universe.md:3` applies it directly — *"an `R`-linear braided monoidal
category **C**"*.

### The framing "Preadditive vs Linear" is wrong — they are a stack, not rivals

`Linear R C` takes `[Preadditive C]` as a **prerequisite instance**. There is no
choice between them: picking `Linear` gives `Preadditive` for free, and picking
`Preadditive` alone lands strictly *below* what the paper states. Since the whole
point of this bean is that the Lean under-encodes the axiom, stopping at
`Preadditive` would repeat the defect one level up.

### The larger finding: `k` is not connected to `C` at all

Measured over the structure body (lines 133–228 of `CategoricalFoundations.lean`),
`k` occurs in the **type** at exactly two places:

    frobWeight : blocks → k
    dimQ       : blocks → k

plus the binder `(k : Type*) [Field k]`. There is no `Linear k C`, no
`Module k _`, nothing relating `k` to `C`. So a model may take `k = ℚ` and `C`
anything, with `frobWeight` an arbitrary function into ℚ.

Two docstrings assert linearity the types do not carry:

1. `frobWeight`/`dimQ` "land in `k` **via the standard identification of
   `End(𝟙)` with the ground ring of a `k`-linear category**" — there is no
   `k`-linear structure, so this identification is prose only.
2. `fibreFunctor` — "An exact faithful **`k`-linear** monoidal functor",
   typed `Functor C (Type*)`. Not exactness, not faithfulness, not
   `k`-linearity, not monoidality; and the paper says `τ : C → Vect_R`.

This reframes the decision. `[Field k]` has survived not because it is right but
because it is **inert** — it constrains nothing, so nothing has ever failed
against it. Cf. `qou-btq3`: nothing constructs `QuantumUniverse` either.

### The `End(𝟙) ≅ R` step is a second, separate assumption

`Linear R C` supplies a ring map `R → End(𝟙_C)` (`r ↦ r • 𝟙`). It does **not**
supply an iso — that needs 𝟙 simple / the category connected. So landing block
data in `R` rather than in `End(𝟙_C)` presumes something beyond `R`-linearity.
Two honest designs:

- **(a)** `frobWeight : blocks → End(𝟙_C)` — canonical, no extra hypothesis.
- **(b)** `frobWeight : blocks → R` plus an explicit `unitEndEquiv : R ≃+* End(𝟙_C)`.

The current code is (b) **with the equiv missing**, which is the unstated axiom.

### Composes with the `IsUnit` finding on `qou-omuz`

Under `[CommRing R]` the prose's *"invertible in R"* is `IsUnit`, not `≠ 0`
(2 ≠ 0 in ℤ, 2 not a unit). So the target shape for axiom 4 is
`dimQ_isUnit : ∀ b, IsUnit (dimQ b)` — in `R` under design (b), or in the ring
`End(𝟙_C)` under (a).

### Recommendation (NOT applied — owner's call)

`[CommRing R] [Preadditive C] [Linear R C]`, `IsUnit` in place of `≠ 0`, and the
`End(𝟙) ≅ R` identification made an explicit field. Then `Σ p_b = 𝟙` — the
remaining half of this bean — is expressible.

**The risk to name before doing it** (from `qou-btq3`): existence of a
`QuantumUniverse` is an `axiom`, and `QuantumObservableUniverse`'s is a cited
`sorry`. Both absorb new structure fields **for free**. So this strengthens an
axiomatised existence claim with no proof obligation and no checker firing — it
is not a refactor, it is asserting more. That is exactly why it is the owner's
decision and not an idle-drain.


## The prerequisite question has an answer, and it is in the paper (measured 2026-09-05)

This bean holds the completeness half (`Σ p_b = 𝟙`) behind a question it states
as *"does the paper's R-linear phrasing already imply it? … Do not add the
instance without settling that."* Settled, by reading the two blocks it names:

1. **`def:quantum-universe` item 1 ASSERTS it.** *"an $R$-linear braided
   [monoidal category](#def:rigid-monoidal-category) $\mathbf{C}$ over a
   commutative ring $R$"*. So $R$-linearity is an **axiom of every quantum
   universe**, not merely a predicate the corpus defines somewhere. This is the
   discriminator: a defined-but-unasserted predicate would leave the question
   genuinely open, and it is not one.
2. **`def:rigid-monoidal-category:31` DEFINES it as Preadditive plus an
   $R$-action.** *"We say $\mathbf{C}$ is $R$-linear for a commutative ring $R$
   … if every hom-set is an $R$-module and composition is $R$-bilinear."* An
   $R$-module is in particular an `AddCommGroup`; $R$-bilinear composition is in
   particular biadditive. That is Mathlib's `Preadditive` verbatim — and
   `CategoryTheory.Linear R C` is *declared* `[Preadditive C]`, so the
   implication is the library's own, not an argument of mine.

**So adding `[Preadditive C]` to the Lean `QuantumUniverse` does not change what
a quantum universe IS.** The Lean is currently *weaker* than the paper; the fix
is claim-**alignment**, not a claim change, and the caveat this bean raised
against it does not apply.

Reclassifying accordingly: this is agent-actionable Lean work under the paper's
existing axiom, not an owner ruling. It stays open as *work*, and comes off the
owner-gated queue.

What is still true and worth keeping: the two gaps cost differently
(orthogonality needed only `HasZeroMorphisms` and is DONE), and the axiom's name
still promises more than its type delivers until completeness lands.


## ✅ DONE ON MAIN — and my own note above ("still open as work") was wrong

Checked the tree rather than the bean, and this is fully landed. All four
`QuantumUniverse` carriers now have it:

- `quantum-universes/quantum-universe.lean`
- `quantum-observable-universes/quantum-observable-universe.lean`
- `lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean`
- `lean/QOU/QuantumObservableUniverse/TrivialWitness.lean` (field **and** its
  instance, so the completeness axiom is discharged by a witness rather than
  merely stated)

What is in the class now:

```lean
[preInst : @CategoryTheory.Preadditive C catInst]
[linInst : @CategoryTheory.Linear R _ C catInst preInst]
…
centralIdem_orthogonal : ∀ b b', b ≠ b' → centralIdem b ≫ centralIdem b' = 0
centralIdem_complete   : ∑ b, centralIdem b = 𝟙 frobHopf.obj
frobWeight_isUnit      : ∀ b, IsUnit (frobWeight b)
```

`Preadditive` **replaces** the bare `HasZeroMorphisms` rather than sitting
beside it — the docstring records why, and it is a real hazard: two
`HasZeroMorphisms` instances on `C` would have made `p_b ≫ p_b' = 0`
ambiguous. `frobWeight_isUnit` also took this bean's other recommendation,
`IsUnit` over `≠ 0`, with the reason stated (they differ over a ring — `2 ≠ 0`
in `ℤ` and `2` is not a unit; they coincide only over a field, which is why
`≠ 0` survived while the base ring was one).

The completeness docstring cites this bean by name and states the gap in this
bean's own terms: *"This is the field the axiom's NAME promised and its TYPE
did not deliver."*

**🛑 My reclassification note directly above is wrong and is retracted.** It
said *"Off the owner-gated queue, still open as agent work."* The first clause
stands — the `Preadditive` prerequisite really was answered by
`def:quantum-universe` axiom 1, and this bean really did not need an owner
ruling. The second clause was asserted without looking at the tree, on a bean
whose own last update was 2026-08-16. Landed 2026-08-29. Closing.
