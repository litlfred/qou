/-
# The block measure a Frobenius pairing already carries — and where the unit sits in an energy-ranked filtration

Bean `qou-jfx8` (session `qou-0nrt`, 2026-09-16). Formalize-first scaffold for the
owner's "q-distribution on phase space weighted by the LP-dual shadow prices"
picture. Everything here is **derived** from three facts the corpus already
states about the Markov trace: the Frobenius pairing `tr_M = Σ_λ y_λ χ_λ`
(`prop:frobenius-pairing`), `χ_λ(1) = dim V_λ`, and the Markov axiom M1
`tr_M(1) = 1` (`def:markov-axioms-primitive`). No substrate value, no solver
output, no fit enters.

## What is proved

* `blockMass_sum_eq_one` — the masses `y_λ · dim V_λ` sum to `1`. This is the
  normalisation the "q-distribution on the block space" needs, and it is **not**
  an extra hypothesis: it is M1 read through the pairing. (`MarkovNormalisation`
  proves the `n = 2, 3` convention-D instances by hand; this is the general
  statement.)
* `trM_eq_expectation` — the Markov trace is the `blockMass`-expectation of the
  **normalised** characters `χ_λ(x) / dim V_λ`.
* `trM_le_of_normalised_le` — with non-negative weights the trace is a convex
  combination, hence bounded by the sup of the normalised characters. This is
  the falsifiable content of calling the weights a *probability*: it fails for a
  weight family that does not sum to `1` (the quantum Plancherel `w_λ(q)`, which
  sums to `≈ 1.51` at `n = 12`, `docs/audits/2026-09-04-plancherel-convention-gap.md`).
* `trM_eq_of_entangledSupp_empty` — if a bound word and its free constituent
  product have the same character on every block, their traces agree, so every
  `log(tr_M(atom)/tr_M(free))` binding form vanishes
  (`bindingForm_eq_zero_of_entangledSupp_empty`, in the archimedean companion
  `BlockMeasureBindingFormArchimedean.lean`, per §7c). The contrapositive is the
  one-line formal content of "the entangled phase space is what carries the
  binding": a nonzero binding **forces** a block on which the two characters
  differ.
* `level_one_eq_top` / `level_le_top` — for the energy-ranked level
  `ℓ(x) = max{E(λ) : λ ∈ supp x}`, which is the shape of `def:confinement-level`,
  the **unit has the maximal level of any element**. This is the abstract form
  of the unit-coefficient exclusion
  (`docs/audits/2026-08-26-the-unit-coefficient-excludes-gs-definable-filtrations.md`):
  the trivial closure is at the top, not at level `0`, so the ladder
  "quark = 0, nucleon = 1, atom = 2" of `def:confined-particle` is **not** this
  level.

## What is NOT claimed

Nothing here selects a weight family, a braid word, an operator `K`, or a
relative Reeb angle; nothing identifies `y_λ` with a solver dual. Positivity of
the convention-D weights is carried as a hypothesis (`IsProbability`), not
derived — the corpus measures it (`sdp_o3prime_weight_positivity_probe.py`,
`n = 3..12`) and proves the two-row vanishing
(`QOU.MassTheory.TwoRowCapDerived.massWeight_eq_zero_of_three_rows_of_wenzl`),
but a general-`n` positivity theorem is not in the tree.

`charSupp` is the **character** support, a lower bound for the block support
(a nonzero traceless block is invisible to it). The unit theorem needs only
`x = 1`, where the two coincide.

-- Ref: [leitner2026] prop:frobenius-pairing; def:markov-axioms-primitive; def:confinement-level
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp

namespace QOU.MassTheory.BlockMeasure

open Finset

/-- Abstract Frobenius-pairing data for a Markov trace on a finite block set `Λ`:
`trM x = ∑ λ, y λ * χ λ x`, with `χ λ 1 = dim λ` and the Markov axiom M1
`trM 1 = 1`. The characters are carried as functions `A → R`; nothing about
their linearity or class-function property is needed below. -/
structure FrobeniusPairingData (R : Type*) [CommRing R] (A : Type*) [Ring A]
    (Λ : Type*) [Fintype Λ] where
  /-- The Markov trace. -/
  trM : A → R
  /-- The Markov (Frobenius-pairing) weight of each block. -/
  y : Λ → R
  /-- The character of each block. -/
  χ : Λ → A → R
  /-- The dimension of each block. -/
  dim : Λ → ℕ
  /-- The Frobenius pairing `tr_M = Σ_λ y_λ χ_λ`. -/
  pairing : ∀ x, trM x = ∑ l, y l * χ l x
  /-- A character at the unit is the dimension. -/
  χ_one : ∀ l, χ l 1 = (dim l : R)
  /-- Markov axiom M1. -/
  trM_one : trM 1 = 1

namespace FrobeniusPairingData

section CommRing

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] {Λ : Type*} [Fintype Λ]
variable (D : FrobeniusPairingData R A Λ)

/-- The mass the pairing assigns to a block: `y_λ · dim V_λ`. -/
def blockMass (l : Λ) : R := D.y l * D.dim l

/-- **Normalisation.** The block masses sum to `1` — Markov axiom M1 read
through the Frobenius pairing at `x = 1`. -/
theorem blockMass_sum_eq_one : ∑ l, D.blockMass l = 1 := by
  have h := D.trM_one
  rw [D.pairing 1] at h
  simpa [blockMass, D.χ_one] using h

/-- Blocks on which two elements have different characters — the block set a
bound word `a` and its free constituent product `b` do **not** share. -/
noncomputable def entangledSupp (a b : A) : Finset Λ :=
  open Classical in univ.filter fun l => D.χ l a ≠ D.χ l b

/-- If no block separates `a` from `b`, their Markov traces agree. -/
theorem trM_eq_of_entangledSupp_empty {a b : A} (h : D.entangledSupp a b = ∅) :
    D.trM a = D.trM b := by
  classical
  rw [D.pairing, D.pairing]
  refine sum_congr rfl fun l _ => ?_
  have hl : D.χ l a = D.χ l b := by
    by_contra hne
    have hmem : l ∈ D.entangledSupp a b := by
      simp [entangledSupp, hne]
    rw [h] at hmem
    simp at hmem
  rw [hl]

/-- Character support of `x`: the blocks on which its character is nonzero.
A lower bound for the block support (a nonzero traceless block is invisible). -/
noncomputable def charSupp (x : A) : Finset Λ :=
  open Classical in univ.filter fun l => D.χ l x ≠ 0

/-- The energy-ranked level of `x` for an energy ranking `E : Λ → ℕ` of the
blocks: the rank of the most expensive block in the (character) support. This
is the shape of `def:confinement-level`, `ℓ(K, q) = min{ℓ : T_w ∈ J^ℓ(q)}` with
`J^ℓ` spanned by the blocks of rank `≤ ℓ`. -/
noncomputable def level (E : Λ → ℕ) (x : A) : ℕ := (D.charSupp x).sup E

/-- Every level is at most the top rank. -/
theorem level_le_top (E : Λ → ℕ) (x : A) : D.level E x ≤ univ.sup E :=
  Finset.sup_mono (subset_univ _)

end CommRing

section Field

variable {R : Type*} [Field R] {A : Type*} [Ring A] {Λ : Type*} [Fintype Λ]
variable (D : FrobeniusPairingData R A Λ)

/-- **The trace is an expectation.** With every block of nonzero dimension, the
Markov trace is the `blockMass`-weighted sum of the normalised characters. -/
theorem trM_eq_expectation (hdim : ∀ l, (D.dim l : R) ≠ 0) (x : A) :
    D.trM x = ∑ l, D.blockMass l * (D.χ l x / D.dim l) := by
  rw [D.pairing]
  refine sum_congr rfl fun l _ => ?_
  unfold blockMass
  field_simp [hdim l]

/-- At the unit, the character support is everything: `χ_λ(1) = dim V_λ ≠ 0`. -/
theorem charSupp_one (hdim : ∀ l, (D.dim l : R) ≠ 0) : D.charSupp 1 = univ := by
  classical
  ext l
  simp [charSupp, D.χ_one, hdim l]

/-- **The unit sits at the top level.** For any energy ranking of the blocks, the
trivial closure has the maximal level — so an energy-ranked level cannot place the
identity (or a free constituent product's neutral element) at level `0`. -/
theorem level_one_eq_top (hdim : ∀ l, (D.dim l : R) ≠ 0) (E : Λ → ℕ) :
    D.level E 1 = univ.sup E := by
  rw [level, D.charSupp_one hdim]

/-- Consequently the unit's level dominates every other element's level. -/
theorem level_le_level_one (hdim : ∀ l, (D.dim l : R) ≠ 0) (E : Λ → ℕ) (x : A) :
    D.level E x ≤ D.level E 1 := by
  rw [D.level_one_eq_top hdim E]
  exact D.level_le_top E x

end Field

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
variable {A : Type*} [Ring A] {Λ : Type*} [Fintype Λ]
variable (D : FrobeniusPairingData R A Λ)

/-- Non-negative weights: the block masses form a probability vector
(non-negative, summing to `1` by `blockMass_sum_eq_one`). Carried as a
hypothesis; the corpus measures it for convention D and does not yet prove it at
general `n`. -/
def IsProbability : Prop := ∀ l, 0 ≤ D.y l

theorem blockMass_nonneg (hy : D.IsProbability) (l : Λ) : 0 ≤ D.blockMass l :=
  mul_nonneg (hy l) (Nat.cast_nonneg _)

/-- **Convexity bound.** Under a probability block measure the Markov trace is a
convex combination of the normalised characters, hence bounded by any common
upper bound of them. This fails for a weight family that does not sum to `1`. -/
theorem trM_le_of_normalised_le (hy : D.IsProbability) (hdim : ∀ l, (D.dim l : R) ≠ 0)
    {x : A} {M : R} (hM : ∀ l, D.χ l x / D.dim l ≤ M) : D.trM x ≤ M := by
  rw [D.trM_eq_expectation hdim x]
  calc ∑ l, D.blockMass l * (D.χ l x / D.dim l)
      ≤ ∑ l, D.blockMass l * M :=
        sum_le_sum fun l _ => mul_le_mul_of_nonneg_left (hM l) (D.blockMass_nonneg hy l)
    _ = M := by rw [← sum_mul, D.blockMass_sum_eq_one, one_mul]

/-- The mirror lower bound. -/
theorem le_trM_of_le_normalised (hy : D.IsProbability) (hdim : ∀ l, (D.dim l : R) ≠ 0)
    {x : A} {m : R} (hm : ∀ l, m ≤ D.χ l x / D.dim l) : m ≤ D.trM x := by
  rw [D.trM_eq_expectation hdim x]
  calc m = ∑ l, D.blockMass l * m := by rw [← sum_mul, D.blockMass_sum_eq_one, one_mul]
    _ ≤ ∑ l, D.blockMass l * (D.χ l x / D.dim l) :=
        sum_le_sum fun l _ => mul_le_mul_of_nonneg_left (hm l) (D.blockMass_nonneg hy l)

end Ordered

end FrobeniusPairingData

end QOU.MassTheory.BlockMeasure
