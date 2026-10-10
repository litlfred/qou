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

## 2026-09-03 — self-conjugacy was free, and is now derived

Two defects, and the second is the one that matters.

**`SelfConjugate` was an unconstrained predicate field.**
`LRFusionData` carried `SelfConjugate : ∀ {n}, Partition n → Prop` as data,
so an instance could take `SelfConjugate := fun _ => True` and satisfy
`lambdaZ_selfConj`, `muN_selfConj` and `nuZN_selfConj` with `trivial`. All
three self-conjugacy hypotheses of the conjecture were therefore vacuous as
encoded — the same shape as a bound variable that never occurs in the body.
It is now *defined*, `SelfConjugate λ ↔ conj λ = λ`, over a conjugation
operation with `conj_conj` making it an involution, so the three hypotheses
constrain something.

**`nu_selfConjugate` returned `c.nuZN_selfConj`**, and its docstring said
"self-conjugacy is *preserved by the LR rigidity*" — a derivation from
rigidity that did not happen, contradicted by its own next sentence ("one of
the conditions of the conjecture itself, lifted to a callable theorem").

It is now **proved**, and this is the §3b-cond item-5 remedy rather than a
re-adjudication: the class carries genuine sub-hypotheses and the theorem
composes them. `lr_conj` — the Littlewood–Richardson conjugation symmetry
`c^ν_{λμ} = c^{ν'}_{λ'μ'}`, a *theorem of LR theory* and not conjecture
content — belongs on `LRFusionData` beside `lr`. With `λ' = λ` and `μ' = μ`
it gives `c^{ν'}_{λμ} = c^ν_{λμ} = 1 ≠ 0`, and `nu_unique` then forces
`ν' = ν_{ZN}`.

So `nuZN_selfConj` is **removed from the conjecture**: the conjecture is
strictly weaker than before — one fewer thing assumed — and the `.md`, which
still states self-conjugacy of `ν` as part of the claim, is now *stronger*
than the Lean rather than the other way round. That direction is the safe one
and is recorded rather than silently taken.

Zero consumers: the two other `.lean` files naming `DoubleMagicConjecture`
refer to `QOU.Interactions.LRFusion.DoubleMagicConjecture`, a **different**
class of the same name in the library tree (repaired separately 2026-08-31),
and to a docstring cross-reference to it.

-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
-- Ref: [ariki1996] Ariki, "On the decomposition numbers of the Hecke algebra of G(m, 1, n)," J. Math. Kyoto Univ. 36 (1996)
-- Ref: [ram1991]     title: — see folio/schema/references.ts
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
  /-- Conjugation (transpose) of a Young diagram, `λ ↦ λ'`. -/
  conj : ∀ {n : ℕ}, Partition n → Partition n
  /-- Conjugation is an involution, `λ'' = λ`. -/
  conj_conj : ∀ {n : ℕ} (l : Partition n), conj (conj l) = l
  /-- The Specht module attached to a partition (abstract carrier). -/
  Specht : ∀ {n : ℕ}, Partition n → Type*
  /-- The LR coefficient `c^ν_{λ μ}` as a natural number. -/
  lr : Partition Z → Partition N → Partition (Z + N) → ℕ
  /-- **LR conjugation symmetry**, `c^ν_{λ μ} = c^{ν'}_{λ' μ'}`.

      A theorem of Littlewood–Richardson theory, not part of the conjecture:
      it holds for the actual LR coefficients and is recorded here because
      this carrier abstracts them. It is what makes `nu_selfConjugate`
      derivable instead of assumed. -/
  -- Ref: [geckpfeiffer2000] Geck & Pfeiffer, LMS Monographs 21, OUP 2000
  lr_conj : ∀ (l : Partition Z) (m : Partition N) (n : Partition (Z + N)),
    lr (conj l) (conj m) (conj n) = lr l m n

/-- **Self-conjugacy**, `λ' = λ`.

    A *definition* over `conj`, not a free predicate field. As a field an
    instance could take `SelfConjugate := fun _ => True` and discharge every
    self-conjugacy hypothesis of the conjecture with `trivial`; here the
    hypotheses constrain the partition. -/
def LRFusionData.SelfConjugate {Z N : ℕ} (d : LRFusionData Z N) {n : ℕ}
    (l : d.Partition n) : Prop :=
  d.conj l = l

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
  /-- It is self-conjugate, `λ' = λ`.  Written as the equation rather than
      via `LRFusionData.SelfConjugate`, which needs a `LRFusionData` term this
      class body does not yet have; the two are definitionally equal. -/
  lambdaZ_selfConj : conj lambdaZ = lambdaZ
  /-- The unique saturated-shell partition at level `N`. -/
  muN : Partition N
  /-- It is self-conjugate, `μ' = μ`. -/
  muN_selfConj : conj muN = muN
  /-- The unique fused partition at level `Z + N`. -/
  nuZN : Partition (Z + N)
  -- Its self-conjugacy was a field here until 2026-09-03. It is now DERIVED
  -- (`nu_selfConjugate` below) from `lambdaZ_selfConj`, `muN_selfConj`,
  -- `lr_conj` and the two rigidity fields, so the conjecture assumes one
  -- thing fewer. Do not restore it.
  /-- LR-rigidity at the fused partition: multiplicity one. -/
  lr_unique_at_nu : lr lambdaZ muN nuZN = 1
  /-- LR-rigidity off the fused partition: multiplicity zero. -/
  lr_vanishes_off : ∀ ν : Partition (Z + N), ν ≠ nuZN → lr lambdaZ muN ν = 0

open scoped Classical in
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

open scoped Classical in
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

/-- **Self-conjugacy of the fused partition is preserved by the LR rigidity**
    — and now this docstring is true.

    Until 2026-09-03 the body was `c.nuZN_selfConj`, a field of the class, so
    nothing was preserved by anything; the sentence above and the body
    disagreed.

    The derivation: LR conjugation symmetry gives
    `c^{ν'}_{λ' μ'} = c^ν_{λ μ}`, and `λ' = λ`, `μ' = μ` by the two
    saturated-shell hypotheses, so `c^{ν'}_{λ μ} = c^{ν}_{λ μ} = 1 ≠ 0`. LR
    rigidity off the fused partition then forces `ν' = ν_{ZN}` — which is
    self-conjugacy. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion §"Statement"
-- Ref: [geckpfeiffer2000] Geck & Pfeiffer, LMS Monographs 21, OUP 2000
theorem nu_selfConjugate
    (Z N : ℕ) [c : DoubleMagicConjecture Z N] :
    LRFusionData.SelfConjugate c.toLRFusionData c.nuZN := by
  have hsym := c.lr_conj c.lambdaZ c.muN c.nuZN
  rw [c.lambdaZ_selfConj, c.muN_selfConj, c.lr_unique_at_nu] at hsym
  exact nu_unique Z N (c.conj c.nuZN) (by rw [hsym]; exact one_ne_zero)

end QOU.LRFusion
