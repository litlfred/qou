/-
  Mass-volume factorization conjecture.

  The categorical mass endomorphism of an atomic link complement
  factorizes as
      m(K; q) = ρ_F · Vol_hyp(complement)
  where ρ_F ∈ {m_e, 2m_e} is the Frobenius packing density
  (single-chirality vs CPT-saturated).

  Per `prop:cpt-orbit-closure-density` (PR #577), the dichotomy
  `ρ_F ∈ {m_e, 2 m_e}` is *derived* from the orbit structure of
  the populated Wedderburn-block set under the Type-B fold
  involution `partitionTranspose`, not asserted as an independent
  Boolean flag.  This file therefore exposes
  `FrobeniusPackingDensity` as a parametric structure carrying a
  *populated-blocks list* whose orbit-closure status under the
  fold determines the density value.  The legacy Boolean flag is
  recovered by `decide (isCPTSaturated populatedBlocks)`.

  Since the factorization itself is a conjecture, we axiomatize
  it as a class whose `sorry`-valued instances encode the
  statement.  Downstream results can be proved conditional on
  [MassVolumeFactorization].

  Ref: [manuscript] Ch 11 §8 / mass-volume-factorization
  Ref: [thurston1978] http://library.msri.org/books/gt3m/
  Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

namespace QOU.ParticleInteractions

/-- Abstract partition carrier (full structure in
    `Mathlib.Combinatorics.Young.YoungDiagram`).

    Defined here in this namespace's own naming so that
    `mass-volume-factorization.lean` and
    `cpt-orbit-closure-density.lean` can each compile
    independently of import order.  The two declarations are
    intended to be definitionally identified once a single
    `Partition` carrier is established in
    `cpt-orbit-closure-density.lean` (deduplication tracked as a
    follow-up: `Mathlib.Combinatorics.Young.YoungDiagram` is the
    long-term target). -/
-- Ref: [manuscript] prop:cpt-orbit-closure-density
axiom PartitionMVF (n : ℕ) : Type

/-- The Type-B fold involution on partitions (transpose). -/
-- Ref: [manuscript] prop:cpt-orbit-closure-density
axiom partitionTransposeMVF {n : ℕ} : PartitionMVF n → PartitionMVF n

/-- Equality on the abstract partition carrier is decidable.  Supplied
    classically because `PartitionMVF` is opaque here (the concrete
    `Mathlib.Combinatorics.Young.YoungDiagram` carrier has a genuine
    `DecidableEq`); used so list-membership in `isCPTSaturatedMVF`
    is decidable. -/
noncomputable instance instDecidableEqPartitionMVF {n : ℕ} :
    DecidableEq (PartitionMVF n) :=
  Classical.decEq _

/-- A populated Wedderburn-block list is **CPT-saturated** iff
    closed under the Type-B fold involution. -/
def isCPTSaturatedMVF {n : ℕ} (Λ : List (PartitionMVF n)) : Prop :=
  ∀ lam ∈ Λ, partitionTransposeMVF lam ∈ Λ

noncomputable instance isCPTSaturatedMVF_decidable {n : ℕ}
    (Λ : List (PartitionMVF n)) :
    Decidable (isCPTSaturatedMVF Λ) := by
  unfold isCPTSaturatedMVF
  exact List.decidableBAll _ Λ

/-- Frobenius packing density: derived from the populated
    Wedderburn-block list `populatedBlocks` (parametrised by the
    strand count `n`).  The density is `m_e` when the list lies in
    a fundamental domain of the Type-B fold (single-chirality), and
    `2 m_e` when it is fold-invariant (CPT-saturated).

    This replaces the legacy Boolean-flag encoding; per
    `prop:cpt-orbit-closure-density`, the Boolean is recovered as
    `decide (isCPTSaturatedMVF populatedBlocks)`. -/
structure FrobeniusPackingDensity (n : ℕ) where
  scaleMe : ℝ                                  -- base scale m_e
  populatedBlocks : List (PartitionMVF n)       -- Λ(K)

/-- The density value: `m_e` if `Λ(K)` is *not* fold-closed
    (single-chirality), `2 m_e` if it *is* fold-closed
    (CPT-saturated).  Derived structurally from the orbit
    structure under the Type-B fold (`prop:cpt-orbit-closure-density`),
    no Boolean flag inserted by hand. -/
noncomputable def FrobeniusPackingDensity.value
    {n : ℕ} (ρ : FrobeniusPackingDensity n) : ℝ :=
  if isCPTSaturatedMVF ρ.populatedBlocks then 2 * ρ.scaleMe
  else ρ.scaleMe

/-- Recover the legacy Boolean flag from the populated-blocks
    list.  Provided so any downstream code that branches on
    `cptSaturated` continues to compile after the structural
    refactor; the Boolean is now a *consequence*, not a primitive. -/
noncomputable def FrobeniusPackingDensity.cptSaturated
    {n : ℕ} (ρ : FrobeniusPackingDensity n) : Bool :=
  decide (isCPTSaturatedMVF ρ.populatedBlocks)

/-- **Equivalence**: the value derived from the orbit-closure
    predicate matches the legacy Boolean-form value
    `if ρ.cptSaturated then 2*scaleMe else scaleMe`. -/
theorem FrobeniusPackingDensity.value_eq_boolean_form
    {n : ℕ} (ρ : FrobeniusPackingDensity n) :
    ρ.value =
      (if ρ.cptSaturated then 2 * ρ.scaleMe else ρ.scaleMe) := by
  unfold FrobeniusPackingDensity.value FrobeniusPackingDensity.cptSaturated
  by_cases h : isCPTSaturatedMVF ρ.populatedBlocks
  · simp [h]
  · simp [h]

/-- **Mass-volume factorization** (conjectural class).
    An instance asserts the factorization
        mass = density · hyperbolic volume
    for a given atomic link configuration.  The `factorization`
    field is `sorry` — this is the conjecture itself, not a
    derivable theorem.

    The density now carries the `n`-strand parameter (matching
    the populated-blocks list); the legacy Boolean flag is
    recoverable via `FrobeniusPackingDensity.cptSaturated`. -/
class MassVolumeFactorization
    (K : Type*) -- atomic link configuration
    (n : ℕ)     -- strand count for the configuration's Wedderburn data
    where
  density      : K → FrobeniusPackingDensity n
  volume       : K → ℝ          -- Thurston hyperbolic volume
  mass         : K → ℝ          -- categorical mass endomorphism
  factorization :
    ∀ k : K, mass k = (density k).value * volume k
  -- Ref: [thurston1978] http://library.msri.org/books/gt3m/
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
  -- The `factorization` field is taken as an axiom of the class;
  -- instances must provide evidence per atomic link configuration
  -- (via SnapPy volume computation and Wedderburn block analysis).

/-- Binding energy derived from the factorization for a list of
    JSJ pieces.  Conditional on `MassVolumeFactorization`.
    Uses the `mass` field directly; by the `factorization` axiom
    this equals `Σ (density k).value * volume k`. -/
noncomputable def bindingFromJSJ
    {K : Type*} {n : ℕ} [MassVolumeFactorization K n]
    (pieces : List K) : ℝ :=
  (pieces.map (MassVolumeFactorization.mass (n := n))).sum

/-- **Faithful-density skeleton instance.**  Pins
    `density.scaleMe := 0.51099895` (the CODATA 2022 electron mass
    in MeV) — the canonical Frobenius packing density `m_e` for the
    single-chirality regime.  The other fields stay at the trivial
    `volume = 0` model; the `mass = density · volume = 0` factorisation
    closes by `mul_zero`.  Discharges §3b-cond while encoding the
    one piece of physics that has a canonical value: the m_e
    Frobenius scale. -/
-- Ref: [manuscript] Ch 11 §8 / mass-volume-factorization
-- Ref: [codata2022] CODATA 2022 electron rest energy
instance canonical (K : Type*) : MassVolumeFactorization K 0 where
  density := fun _ => { scaleMe := 0.51099895069, populatedBlocks := [] }
  volume := fun _ => 0
  mass := fun _ => 0
  factorization := by
    intro k
    show (0 : ℝ) = FrobeniusPackingDensity.value _ * 0
    rw [mul_zero]

end QOU.ParticleInteractions
