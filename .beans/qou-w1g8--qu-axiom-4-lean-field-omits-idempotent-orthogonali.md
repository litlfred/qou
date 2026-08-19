---
# qou-w1g8
title: QU axiom 4 Lean field omits idempotent orthogonality + completeness (needs Preadditive)
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T00:23:28Z
updated_at: 2026-08-16T12:56:04Z
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
