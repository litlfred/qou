import Mathlib.Tactic

/-!
# QOU.MassTheory.InvolutionSelectionRule — what an invariance argument does and does not localise

Bean `qou-bn8e`. The corpus argues in several places that a mass splitting must
be *sourced* by one particular sector, because the splitting breaks an involution
that every other sector respects. The clearest instance is
`rem:isospin-mass-split-em-localisation`
(`content/quantum-observable-universe/mass-theory/`), which concludes that the
mirror-isobar split `m(³H) − m(³He) ≈ 0.529 MeV` *"must therefore be entirely
sourced by the Coulomb term"*, on the grounds that *"the trace tower, co-Casimir,
chirality, and shell-correction functionals all respect these structural
involutions."*

**The valid core of that argument is here, and so is its load-bearing
hypothesis.** The core is a one-line cancellation. What is doing the real work is
the *enumeration* — the claim that the listed sectors are all of them, and that
each is invariant. This file makes the enumeration a `List` in the type, so that
the arity of the claim cannot be lost between the proposition and the prose
(AGENTS.md §"Grep the claim SHAPE, not only the topic").

## What is proved

| declaration | content |
|---|---|
| `split_invariantSector_eq_zero` | an `ι`-invariant sector contributes **zero** to the `ι`-split |
| `split_sum_eq_split_remainder` | a sum of invariant sectors plus a remainder splits **exactly like the remainder** |
| `omitted_sector_breaks_localisation` | **the enumeration is load-bearing**: omit one non-invariant sector and the conclusion is false |

## What this does NOT establish

Three things, and the third is why bean `qou-bn8e` stays open.

1. **Exhaustiveness.** `split_sum_eq_split_remainder` localises the split into
   `G` only for the decomposition it is handed. Nothing here says the corpus's
   four named sectors plus Coulomb exhaust the mass functional, and
   `omitted_sector_breaks_localisation` shows that gap is not cosmetic.
2. **The invariance of each named sector.** Only the shell-correction sector has
   a proved sign-flip invariance in this corpus
   (`prop:crystal-isospin-degeneracy`, and that one is itself conditional on
   `CrystalEigenlineSignBlind`). Surveying the Lean tree turned up **no**
   theorem asserting sign-flip invariance of the trace tower, the co-Casimir or
   the chirality functional. The nearest chirality result,
   `QOU.Resurgence.chiral_sign_cancels`, does not help and is worth reading
   before anyone cites it here: it concerns a **different** involution (diagram
   conjugation, not the generator sign-flip) and states **anti**-invariance,
   `sign (conj μ) = − sign μ`. A sector that is anti-invariant is the one that
   *survives* a split, not one that drops out of it. So the remark's *"all
   respect these structural involutions"* is, at present, one proved case
   generalised to four — and the generalisation crosses at least two distinct
   involutions, which is its own hazard (AGENTS.md §`da-arity-conflation`).
3. **Any magnitude whatsoever.** A selection rule says *where* a quantity may
   live, never *how big* it is. `E_EM` is not derived by this file and is not
   derived anywhere in this corpus.

**Scope, per the (a)/(b) discipline.** Nothing here refutes the localisation
claim — it is very plausibly true. The claim is scope-**(a)**: as currently
supported it does not follow, because two of its premises are unproved. Fixing
that means proving the two missing invariances, not weakening the remark.
-/

namespace QOU.MassTheory.InvolutionSelectionRule

variable {X : Type*} {R : Type*} [AddCommGroup R]

/-- The **`ι`-split** of a functional: its value on a state minus its value on
the involuted state. For `ι` the isospin mirror this is `m(³H) − m(³He)`; for
`ι` the generator sign-flip it is the proton/neutron difference. -/
def split (ι : X → X) (F : X → R) (x : X) : R := F x - F (ι x)

/-- A **sector** of the mass functional, bundled with the invariance claim that
makes it drop out of the split. Bundling is deliberate: an unbundled `F` with the
invariance asserted in prose is exactly the failure mode this file is about. -/
structure InvariantSector (ι : X → X) (R : Type*) [AddCommGroup R] where
  /-- The sector's contribution to the mass. -/
  F : X → R
  /-- Its invariance under `ι` — the premise that must be *proved* per sector. -/
  invariant : ∀ x, F (ι x) = F x

/-- **An invariant sector contributes exactly zero to the split.** The valid core
of every localisation argument of this shape. -/
theorem split_invariantSector_eq_zero (ι : X → X) (s : InvariantSector ι R) (x : X) :
    split ι s.F x = 0 := by
  simp [split, s.invariant x]

/-- **Localisation, stated with its enumeration explicit.** If the mass
functional decomposes as a sum over a *given list* of invariant sectors plus a
remainder `G`, then the split is the split of `G` alone.

The list is the hypothesis. Read `ss` as "the trace tower, the co-Casimir, the
chirality and the shell correction" and `G` as "the Coulomb term", and this is
the remark's argument — with the two things it assumes now visible in the
statement rather than in the prose. -/
theorem split_sum_eq_split_remainder (ι : X → X)
    (ss : List (InvariantSector ι R)) (G : X → R) (x : X) :
    split ι (fun y => ((ss.map (fun s => s.F y)).sum) + G y) x = split ι G x := by
  have hs : ((ss.map (fun s => s.F (ι x))).sum) = ((ss.map (fun s => s.F x)).sum) := by
    induction ss with
    | nil => rfl
    | cons s t ih => simp [List.map_cons, List.sum_cons, s.invariant x, ih]
  simp only [split]
  rw [hs]
  abel

/-- **The enumeration is load-bearing, not bookkeeping.** If a sector that is
*not* invariant is left out of the list, the localisation conclusion is false:
here the remainder `G` has zero split, so the argument would report "the split is
entirely `G`'s, hence zero", while the true split is `2`.

Concretely `ι = (· * -1)` on `ℤ`, the omitted sector is the identity, and `G` is
zero. This is why point 2 above matters: an unproved invariance is
indistinguishable, to this argument, from an omitted sector. -/
theorem omitted_sector_breaks_localisation :
    ∃ (ι : ℤ → ℤ) (F G : ℤ → ℤ) (x : ℤ),
      Function.Involutive ι
        ∧ split ι G x = 0
        ∧ split ι (fun y => F y + G y) x ≠ 0 := by
  refine ⟨fun n => -n, id, fun _ => 0, 1, fun n => by ring, ?_, ?_⟩
  · simp [split]
  · simp [split]

/-! ## Sectors that factor through an invariant of the state

The practical way a sector turns out to be invariant is rarely a computation: it
is that the sector never sees the data the involution moves. The Frobenius
co-Casimir term of the unified mass formula
([`thm:knot-mass-formula-unified`](../../../mass-theory/knot-mass-formula-unified.md))
is the case in point. By
[`thm:frobenius-codim-universal`](../../../mass-theory/frobenius-codim-universal.md),

  `τ(C_dim_q) = Σ_{λ ∈ Â} 1 / dim_q(λ)`,

a sum over the Wedderburn blocks of `H_n(R, q)`. It is a function of `(n, q)`
alone and takes **no braid word as an argument at all**, so a generator sign
flip cannot move it: it factors through `word ↦ (n, q)`, which the flip fixes.
-/

/-- **A sector that factors through an `ι`-invariant of the state contributes
zero to the split.** More useful in practice than checking invariance directly,
because it is usually obvious *by arity* that a sector cannot see what `ι`
moves. -/
theorem split_comp_eq_zero {Y : Type*} (ι : X → X) (π : X → Y) (G : Y → R)
    (hπ : ∀ x, π (ι x) = π x) (x : X) :
    split ι (G ∘ π) x = 0 := by
  simp [split, hπ x]

/-- The sector built from such a factorisation, as an `InvariantSector` — so it
can be dropped straight into the list `split_sum_eq_split_remainder` consumes. -/
def factoringSector {Y : Type*} (ι : X → X) (π : X → Y) (G : Y → R)
    (hπ : ∀ x, π (ι x) = π x) : InvariantSector ι R where
  F := G ∘ π
  invariant x := by simp [hπ x]

/-- **The Frobenius co-Casimir sector is invariant, and the reason is arity.**
Modelled with `Y = ℕ × R` for the pair `(n, q)`: whatever `G` computes from the
block data, the generator sign flip leaves `(n, q)` alone, so the term drops out
of the split. Both mirror isobars sit at `A = 3`, hence at the same `n`, so it
cancels between them exactly rather than approximately.

This supplies **one** of the two premises
`rem:isospin-mass-split-em-localisation` was missing. The other, the trace
tower, is false at the substrate — `QOU.MassTheory.TraceSignFlipRegime`. -/
theorem coCasimir_sector_contributes_zero (ι : X → X) (nq : X → ℕ × R)
    (G : ℕ × R → R) (hnq : ∀ x, nq (ι x) = nq x) (x : X) :
    split ι (G ∘ nq) x = 0 :=
  split_comp_eq_zero ι nq G hnq x

end QOU.MassTheory.InvolutionSelectionRule
