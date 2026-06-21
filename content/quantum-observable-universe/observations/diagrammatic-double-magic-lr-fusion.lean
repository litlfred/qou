import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import QOU.Common.MagicNumbers


/-!
# Diagrammatic double-magic LR-fusion rigidity (Lean class)

The conjecture asserts: when both `Z` and `N` are saturated (lie in
`magicSet`), the Littlewood–Richardson product
`V_{λ_Z} ⊗ V_{μ_N}` collapses to a single self-conjugate Specht
module `V_{ν_{ZN}}` at level `A = Z + N`, with multiplicity one.

We axiomatise the conjecture as a `class` per AGENTS.md §3b.
Downstream double-magic binding-energy predictions become
conditional on `[DoubleMagicConjecture Z N]` instances.

-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
-- Ref: [ariki1996] Ariki, "On the decomposition numbers of the Hecke algebra of G(m, 1, n)," J. Math. Kyoto Univ. 36 (1996)
-- Ref: [ram1991]     title: — see content/schema/references.ts
-- Ref: [geckpfeiffer2000] Geck & Pfeiffer, "Characters of Finite Coxeter Groups and Iwahori-Hecke Algebras," LMS Monographs 21, OUP 2000
-/

namespace QOU.LRFusion

-- Single source of truth: QOU.Common.magicSet (see PR #501
-- review). Re-exported here for local ergonomics.
abbrev magicSet : Finset ℕ := QOU.Common.magicSet

/-- Both `Z` and `N` are saturated. -/
def DoubleMagic (Z N : ℕ) : Prop := Z ∈ magicSet ∧ N ∈ magicSet

/-- Abstract data of an LR-fusion outcome at level `Z + N`.

    Concretely the QOU substrate instantiates `Specht λ` as the
    `H_{|λ|}(q)`-module structure on the Specht module of the
    partition `λ`, and `lrFusion λ μ ν` records the LR-coefficient
    `c^ν_{λ μ}`. The conjecture below asks for collapse to a unique
    `ν` with multiplicity one. -/
class LRFusionData (Z N : ℕ) where
  /-- Abstract carrier for partitions of a given size. -/
  Partition : ℕ → Type*
  /-- Self-conjugacy predicate on a partition (e.g. `λ = λ'`). -/
  SelfConjugate : ∀ {n : ℕ}, Partition n → Prop
  /-- The Specht module attached to a partition (abstract carrier). -/
  Specht : ∀ {n : ℕ}, Partition n → Type*
  /-- The LR coefficient `c^ν_{λ μ}` as a natural number. -/
  lr : Partition Z → Partition N → Partition (Z + N) → ℕ

/-- The conjecture, encoded as a class.

    A `DoubleMagicConjecture Z N` instance asserts that, when both
    `Z` and `N` are saturated and the unique saturated-shell
    partition at each level is self-conjugate, the LR product
    collapses to a unique self-conjugate fused partition with
    multiplicity one. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
class DoubleMagicConjecture (Z N : ℕ) extends LRFusionData Z N where
  /-- Precondition: both `Z` and `N` are magic numbers. -/
  doubleMagic : DoubleMagic Z N
  /-- The unique saturated-shell partition at level `Z` (provided by
      the categorical-neutrality conjecture upstream). -/
  lambdaZ : Partition Z
  /-- It is self-conjugate. -/
  lambdaZ_selfConj : SelfConjugate lambdaZ
  /-- The unique saturated-shell partition at level `N`. -/
  muN : Partition N
  /-- It is self-conjugate. -/
  muN_selfConj : SelfConjugate muN
  /-- The unique fused partition at level `Z + N`. -/
  nuZN : Partition (Z + N)
  /-- It is self-conjugate. -/
  nuZN_selfConj : SelfConjugate nuZN
  /-- LR-rigidity at the fused partition: multiplicity one. -/
  lr_unique_at_nu : lr lambdaZ muN nuZN = 1
  /-- LR-rigidity off the fused partition: multiplicity zero. -/
  lr_vanishes_off : ∀ ν : Partition (Z + N), ν ≠ nuZN → lr lambdaZ muN ν = 0

/-- Conditional theorem: under the double-magic conjecture, the LR
    product is concentrated at the unique fused self-conjugate
    partition. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem lr_concentrated
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : c.Partition (Z + N)) :
    c.lr c.lambdaZ c.muN ν = if ν = c.nuZN then 1 else 0 := by
  by_cases h : ν = c.nuZN
  · simp [h, c.lr_unique_at_nu]
  · simp [h, c.lr_vanishes_off ν h]

/-- Conditional theorem: under the double-magic conjecture, the
    fused partition `ν_{ZN}` is the unique partition with non-zero
    LR coefficient. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem nu_unique
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : c.Partition (Z + N)) (hν : c.lr c.lambdaZ c.muN ν ≠ 0) :
    ν = c.nuZN := by
  by_contra h
  exact hν (c.lr_vanishes_off ν h)

/-- Biconditional characterisation of `ν_{ZN}`: under the
    conjecture, `ν` equals the fused partition iff the LR
    coefficient is non-zero (equivalently, equal to 1). -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem nu_iff_lr_nonzero
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : c.Partition (Z + N)) :
    ν = c.nuZN ↔ c.lr c.lambdaZ c.muN ν ≠ 0 := by
  refine ⟨?_, nu_unique Z N ν⟩
  intro h
  rw [h, c.lr_unique_at_nu]
  exact one_ne_zero

/-- Stronger biconditional: under the conjecture, the LR
    coefficient at any `ν` is exactly `1` if `ν = ν_{ZN}` and `0`
    otherwise. The two cases together fully characterise the LR
    product as a Kronecker delta. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem lr_kronecker
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : c.Partition (Z + N)) :
    c.lr c.lambdaZ c.muN ν = if ν = c.nuZN then 1 else 0 :=
  lr_concentrated Z N ν

/-- Self-conjugacy is preserved by the LR rigidity: under the
    conjecture, the unique fused partition is self-conjugate. This
    is one of the conditions of the conjecture itself, lifted to a
    callable theorem for downstream use. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem nu_selfConjugate
    (Z N : ℕ) [c : DoubleMagicConjecture Z N] :
    c.SelfConjugate c.nuZN :=
  c.nuZN_selfConj

end QOU.LRFusion
