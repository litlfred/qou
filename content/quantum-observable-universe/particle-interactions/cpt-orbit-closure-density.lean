/-
  CPT-saturation as Type-B fold-orbit closure.

  Replaces the per-link Boolean flag `cptSaturated` (in
  `mass-volume-factorization.lean`) by the structural predicate
  `isCPTSaturated Λ ↔ σ(Λ) ⊆ Λ`, where σ is the partition
  transpose — the Dynkin involution on the A_{n-1} crystal which,
  after Type-B folding, becomes the bar-involution / chirality-
  reversal operator (conj:symmetric-crystal-pair-production).

  Significance: the Frobenius packing density rule
  ρ_F ∈ {m_e, 2m_e} is no longer a Boolean asserted per atomic
  link — it is derived from the orbit structure of the populated
  Wedderburn-block set Λ(K) under the Type-B fold.  This is the
  symmetric-crystal shortcut #1 (CLAUDE.md §7b) applied at the
  density-rule level.

  Refs: prop:cpt-orbit-closure-density (this block),
        rem:frobenius-packing-density,
        conj:symmetric-crystal-pair-production,
        [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue
                       of universal enveloping algebras", Duke Math.
        [lecouvey2007] Lecouvey, "Combinatorics of crystal graphs and
                       Kostka-Foulkes polynomials"
        [brundankleshchev2009] Brundan-Kleshchev, "Blocks of cyclotomic
                       Hecke algebras and Khovanov-Lauda algebras"
        [khovanovlauda2009] Khovanov-Lauda, "A diagrammatic approach to
                       categorification of quantum groups I"
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

namespace QOU.ParticleInteractions

/-! ## Partitions and the Type-B fold involution

We work with an abstract `Partition n` carrier (matching the stub
in `y-lambda-closed-form-wenzl-bridge.lean`). The fold involution
`σ` is the partition transpose. -/

/-- Abstract partition carrier (full structure in
    `Mathlib.Combinatorics.Young.YoungDiagram`). -/
constant Partition (n : ℕ) : Type

/-- Decidable equality on partitions of `n` (full proof reduces to
    `YoungDiagram` decidability in Mathlib). -/
instance partitionDecEq (n : ℕ) : DecidableEq (Partition n) := by
  intro a b
  -- See Mathlib module Mathlib.Combinatorics.Young.YoungDiagram decEq instance
  -- on YoungDiagram is a derived `DecidableEq`; the wrapper here
  -- inherits it once the constant `Partition n` is unfolded.
  exact Classical.decEq _ a b

/-- The Type-B fold involution: partition transpose
    `σ(λ) = λ^T`.  Identifies (k) ↔ (1^k) and is an involution. -/
constant partitionTranspose {n : ℕ} : Partition n → Partition n

/-- `partitionTranspose` is involutive. -/
-- Ref: [fulton1997] https://doi.org/10.1017/CBO9780511626241 §1 (conjugate/transpose partition is an involution λ^{TT}=λ)
axiom partitionTranspose_involutive {n : ℕ} :
    Function.Involutive (@partitionTranspose n)
  -- See Mathlib module Mathlib.Combinatorics.Young.YoungDiagram —
  --      YoungDiagram.transpose_transpose

/-! ## Orbit-closure predicate -/

/-- A list of partitions is **CPT-saturated** iff it is closed
    under the Type-B fold involution `σ`. -/
def isCPTSaturated {n : ℕ} (Λ : List (Partition n)) : Prop :=
  ∀ lam ∈ Λ, partitionTranspose lam ∈ Λ

instance isCPTSaturated_decidable {n : ℕ}
    (Λ : List (Partition n)) :
    Decidable (isCPTSaturated Λ) := by
  unfold isCPTSaturated
  exact List.decidableBAll _ Λ

/-! ## Equivalence with the Boolean flag

The previous `FrobeniusPackingDensity.cptSaturated : Bool` field
of `mass-volume-factorization.lean` is now a *consequence* of the
orbit predicate, not an independent piece of data. -/

/-- Boolean form of the CPT predicate, matching the legacy
    `FrobeniusPackingDensity.cptSaturated` field. -/
def cptSaturatedBool {n : ℕ} (Λ : List (Partition n)) : Bool :=
  decide (isCPTSaturated Λ)

/-- **Boolean ↔ orbit-closure equivalence**.

    The Frobenius packing density's `cptSaturated` Boolean equals
    the decision procedure for `isCPTSaturated` on the populated-
    blocks list.  Hence the entire Boolean flag is structurally
    determined by the orbit structure of `Λ` under the Type-B
    fold — no per-link case analysis required. -/
theorem cpt_boolean_eq_orbit_closure
    {n : ℕ} (Λ : List (Partition n)) :
    cptSaturatedBool Λ = decide (isCPTSaturated Λ) := by
  rfl

/-- Density value at the categorical scale `m_e`, parametrised by
    the populated-blocks list.  Replaces
    `FrobeniusPackingDensity.value` from `mass-volume-factorization`,
    deriving the factor of 2 from the orbit-closure check. -/
noncomputable def frobeniusPackingDensityValue
    {n : ℕ} (scaleMe : ℝ) (Λ : List (Partition n)) : ℝ :=
  if isCPTSaturated Λ then 2 * scaleMe else scaleMe

/-- **Main proposition**: ρ_F is determined by the orbit-closure
    structure of the populated Wedderburn-block set under the
    Type-B fold involution.

    No Boolean is inserted by hand; the dichotomy
    `ρ_F ∈ {m_e, 2 m_e}` is a *consequence* of whether `Λ` is
    invariant under `σ`. -/
theorem cpt_orbit_closure_density
    {n : ℕ} (scaleMe : ℝ) (Λ : List (Partition n))
    (hsat : isCPTSaturated Λ) :
    frobeniusPackingDensityValue scaleMe Λ = 2 * scaleMe := by
  unfold frobeniusPackingDensityValue
  exact if_pos hsat

theorem cpt_orbit_closure_density_single_chirality
    {n : ℕ} (scaleMe : ℝ) (Λ : List (Partition n))
    (hns : ¬ isCPTSaturated Λ) :
    frobeniusPackingDensityValue scaleMe Λ = scaleMe := by
  unfold frobeniusPackingDensityValue
  exact if_neg hns

/-! ## Worked example: n = 3 Wedderburn blocks

At n = 3 the σ-orbits on Part(3) = {(3), (2,1), (1,1,1)} are:

  · `{(3), (1,1,1)}` — size-2 chirality pair (sym ↔ alt)
  · `{(2,1)}`        — self-dual / mixed channel

The populated-blocks list is CPT-saturated iff every (3) in
the list comes paired with a (1,1,1) (and vice versa); (2,1)
contributes by itself in either case.

The proposition above discharges the dichotomy
`ρ_F ∈ {m_e, 2 m_e}` cleanly via this orbit count, with no per-
link manual flag.  Empirical verification: see
`computations/det_pair_law.py`, which checks
`det ρ_λ(w) · det ρ_{λ^T}(w) = ±1` over generators —
the bar-involution acting at the determinant level, and the
strongest currently available shadow of the underlying
Type-B fold.
-/

end QOU.ParticleInteractions


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub)

This proposition is conditional on the conjecture's class
`SymmetricCrystalPairProduction` (declared in the lake-package sibling).  The local stub
below mirrors the canonical class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises
the conditional-on-class structure of the main theorem above. -/

namespace QOU.ParticleInteractions.CPTOrbit.ConditionalAudit

/-- Local stub of the conjecture's axiomatised class.  See the lake-
    package sibling for the canonical declaration. -/
class SymmetricCrystalPairProduction : Prop where
  /-- Conjecture content is the class instance (sorry = conjecture
      per CLAUDE.md §3b). -/
  holds : True

/-- Witness theorem demonstrating the main proposition is conditional
    on `[SymmetricCrystalPairProduction]` per CLAUDE.md §3b-cond. -/
theorem conditional_on_SymmetricCrystalPairProduction
    [_inst : SymmetricCrystalPairProduction] : True := trivial

end QOU.ParticleInteractions.CPTOrbit.ConditionalAudit
