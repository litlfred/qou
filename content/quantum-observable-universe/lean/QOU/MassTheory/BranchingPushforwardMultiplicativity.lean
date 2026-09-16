/-
# Branching data: the free composite is the pushforward of the product measure, and the binding is the y-weighted deviation from it

Bean `qou-hlbx` (session `qou-qt8b`, 2026-09-16). Generic companion to
`BlockMeasureFromFrobeniusPairing.lean`.

Two Frobenius pairings `D₁` on `A₁` (blocks `Λ₁`) and `D₂` on `A₂` (blocks `Λ₂`)
sit inside a third `D` on `A` (blocks `Λ`) through a "disjoint-union" map
`tensor : A₁ → A₂ → A` (in the corpus, `H_n ⊗ H_m ↪ H_{n+m}` on disjoint strand
blocks). Two hypotheses are carried, both **checkable on committed data**:

* `branching` — the restriction rule `χ_λ(a ⊗ b) = Σ_{μ,ν} c^λ_{μν} χ_μ(a) χ_ν(b)`
  with branching multiplicities `c : Λ₁ → Λ₂ → Λ → ℕ` (Littlewood–Richardson
  coefficients for `S_{n+m} ⊃ S_n × S_m`, unchanged for the Hecke algebra at
  generic `q`);
* `weight_branching` — the weight identity `Σ_λ y_λ c^λ_{μν} = y_μ y_ν`.

## What is proved

* `trM_tensor` — **disjoint-union multiplicativity** `tr_M(a ⊗ b) = tr_M(a) tr_M(b)`
  follows from the two hypotheses. The conclusion is already in the corpus by two
  other routes — `QOU.MathlibExt.MarkovTraceMultiplicative` (`markovTrace_juxtapose`,
  from `Matrix.trace_kronecker`) and `QOU.MathlibExt.DisjointBlockTraceLaw`
  (`TwoSidedMarkov → DisjointBlockMultiplicative`) — and numerically
  (`tr_M(W) = tr_M(p)²`, bean `qou-ales` step 10). What this route adds is the
  **characterisation through the weights**: on the block side, multiplicativity is
  the LR-compatibility of `y`. Scope, per those files: this is the *disjoint-union*
  (Kronecker) statement, not a connected-sum one (bean `qou-bsfg`), and it fails
  for *interleaved* blocks (`QOU.MathlibExt.MarkovTraceInterleavedCrossTerm`,
  bean `qou-ls86`) — which is exactly why a bound composite's trace differs from the
  free product by the deviation term below.
* `blockMass_tensor_char` — the composite's characters on a free product are the
  pushforward of the two marginals' characters along `c`; hence the free composite is
  "unentangled": nothing in its block data goes beyond the two inputs.
* `trM_eq_tensor_add_weighted_deviation` — for any element `atom` of the composite,
  `tr_M(atom) = tr_M(a) tr_M(b) + Σ_λ y_λ δ_λ` with `δ_λ := χ_λ(atom) − χ_λ(a ⊗ b)`
  the **entangled deviation**. So every binding form built from
  `tr_M(atom)/tr_M(free)` is a function of the `y`-weighted deviation alone.
* `weighted_deviation_eq_zero_of_entangledSupp_empty` — the deviation vanishes off
  the entangled support of `BlockMeasureFromFrobeniusPairing.lean`.

## What is NOT claimed

The converse (multiplicativity ⇒ weight identity) needs linear independence of the
products `χ_μ ⊗ χ_ν` and is not stated. Nothing here selects a word, an operator
`K`, or a weight family; `c` is data, not derived.

-- Ref: [manuscript] prop:frobenius-pairing; def:markov-axioms-primitive;
   QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import QOU.MassTheory.BlockMeasureFromFrobeniusPairing

namespace QOU.MassTheory.BlockMeasure

open Finset

/-- Branching data: two Frobenius pairings embedded in a third through a
disjoint-union map, with branching multiplicities `c` and the weight identity. -/
structure BranchingData (R : Type*) [CommRing R]
    (A₁ A₂ A : Type*) [Ring A₁] [Ring A₂] [Ring A]
    (Λ₁ Λ₂ Λ : Type*) [Fintype Λ₁] [Fintype Λ₂] [Fintype Λ] where
  /-- The pairing on the first factor. -/
  D₁ : FrobeniusPairingData R A₁ Λ₁
  /-- The pairing on the second factor. -/
  D₂ : FrobeniusPairingData R A₂ Λ₂
  /-- The pairing on the composite. -/
  D : FrobeniusPairingData R A Λ
  /-- The disjoint-union embedding `a ⊗ b`. -/
  tensor : A₁ → A₂ → A
  /-- Branching multiplicities `c^λ_{μν}`. -/
  c : Λ₁ → Λ₂ → Λ → ℕ
  /-- The restriction rule for characters on a free product. -/
  branching : ∀ (a : A₁) (b : A₂) (l : Λ),
    D.χ l (tensor a b) = ∑ μ, ∑ ν, (c μ ν l : R) * (D₁.χ μ a * D₂.χ ν b)
  /-- The weight identity `Σ_λ y_λ c^λ_{μν} = y_μ y_ν`. -/
  weight_branching : ∀ (μ : Λ₁) (ν : Λ₂), ∑ l, D.y l * (c μ ν l : R) = D₁.y μ * D₂.y ν

namespace BranchingData

variable {R : Type*} [CommRing R]
variable {A₁ A₂ A : Type*} [Ring A₁] [Ring A₂] [Ring A]
variable {Λ₁ Λ₂ Λ : Type*} [Fintype Λ₁] [Fintype Λ₂] [Fintype Λ]
variable (B : BranchingData R A₁ A₂ A Λ₁ Λ₂ Λ)

/-- **Disjoint-union multiplicativity, derived.** `tr_M(a ⊗ b) = tr_M(a) · tr_M(b)`. -/
theorem trM_tensor (a : A₁) (b : A₂) :
    B.D.trM (B.tensor a b) = B.D₁.trM a * B.D₂.trM b := by
  rw [B.D.pairing, B.D₁.pairing, B.D₂.pairing, sum_mul_sum]
  simp_rw [B.branching]
  -- Σ_l y_l Σ_μ Σ_ν c χ χ  =  Σ_μ Σ_ν (Σ_l y_l c) χ χ
  calc ∑ l, B.D.y l * ∑ μ, ∑ ν, (B.c μ ν l : R) * (B.D₁.χ μ a * B.D₂.χ ν b)
      = ∑ μ, ∑ ν, (∑ l, B.D.y l * (B.c μ ν l : R)) * (B.D₁.χ μ a * B.D₂.χ ν b) := by
        simp_rw [mul_sum, sum_mul]
        rw [sum_comm]
        refine sum_congr rfl fun μ _ => ?_
        rw [sum_comm]
        refine sum_congr rfl fun ν _ => sum_congr rfl fun l _ => ?_
        ring
    _ = ∑ μ, ∑ ν, (B.D₁.y μ * B.D₂.y ν) * (B.D₁.χ μ a * B.D₂.χ ν b) := by
        simp_rw [B.weight_branching]
    _ = ∑ μ, ∑ ν, (B.D₁.y μ * B.D₁.χ μ a) * (B.D₂.y ν * B.D₂.χ ν b) := by
        refine sum_congr rfl fun μ _ => sum_congr rfl fun ν _ => ?_
        ring

/-- The **entangled deviation** of a composite element from the free product of two
marginals, block by block. -/
def deviation (atom : A) (a : A₁) (b : A₂) (l : Λ) : R :=
  B.D.χ l atom - B.D.χ l (B.tensor a b)

/-- **The trace of any composite element is the free product's trace plus the
`y`-weighted entangled deviation.** Every binding form built from
`tr_M(atom) / tr_M(free)` is therefore a function of `Σ_λ y_λ δ_λ` alone. -/
theorem trM_eq_tensor_add_weighted_deviation (atom : A) (a : A₁) (b : A₂) :
    B.D.trM atom = B.D₁.trM a * B.D₂.trM b + ∑ l, B.D.y l * B.deviation atom a b l := by
  rw [← B.trM_tensor, B.D.pairing atom, B.D.pairing (B.tensor a b), ← sum_add_distrib]
  refine sum_congr rfl fun l _ => ?_
  unfold deviation
  ring

/-- The weighted deviation vanishes when no block separates `atom` from the free product. -/
theorem weighted_deviation_eq_zero_of_entangledSupp_empty (atom : A) (a : A₁) (b : A₂)
    (h : B.D.entangledSupp atom (B.tensor a b) = ∅) :
    ∑ l, B.D.y l * B.deviation atom a b l = 0 := by
  have := B.trM_eq_tensor_add_weighted_deviation atom a b
  rw [B.D.trM_eq_of_entangledSupp_empty h, B.trM_tensor] at this
  linear_combination -this

/-- The composite's block masses on a free product are determined by the two marginal
characters through `c`: `y_λ χ_λ(a ⊗ b) = y_λ Σ c^λ_{μν} χ_μ(a) χ_ν(b)`. Stated so a reader
sees that nothing in the free composite's block data goes beyond the inputs. -/
theorem blockMass_tensor_char (a : A₁) (b : A₂) (l : Λ) :
    B.D.y l * B.D.χ l (B.tensor a b)
      = B.D.y l * ∑ μ, ∑ ν, (B.c μ ν l : R) * (B.D₁.χ μ a * B.D₂.χ ν b) := by
  rw [B.branching]

end BranchingData

end QOU.MassTheory.BlockMeasure
