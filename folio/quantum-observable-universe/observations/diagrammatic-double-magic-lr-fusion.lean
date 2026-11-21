import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import QOU.Common.MagicNumbers
import Mathlib.Combinatorics.Young.YoungDiagram


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

## 2026-11-20 — partitions and conjugation are now Mathlib's

`Partition`, `conj` and `conj_conj` were instance fields of `LRFusionData`, so
`Partition := fun _ => Unit`, `conj := id`, `lr := 1` inhabited the
conjecture at every double-magic pair (bean `qou-dx7g`). `Partition n` is now
`{μ : YoungDiagram // μ.card = n}` and `conj` is `YoungDiagram.transpose`, so
the saturated-shell partitions must be genuine self-conjugate Young diagrams
(`not_doubleMagicConjecture_two_two`: none exists at `Z = N = 2`). **Still
free:** the LR coefficient `lr` — neither Mathlib nor the corpus defines
Littlewood–Richardson coefficients, so it is constrained only by `lr_conj`,
and an instance may still set `lr` to the Kronecker delta at a self-conjugate
`ν`. Encoding the rigidity claim needs `lr` defined (LR tableaux count).

-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
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

/-- **Partitions of `n`**, as Mathlib Young diagrams with `n` cells
    (tied to Mathlib 2026-11-20, bean `qou-dx7g`; until then the carrier was
    an instance field `Partition : ℕ → Type*`, so `Partition := fun _ => Unit`
    inhabited the conjecture at every double-magic `(Z, N)`). -/
def Partition (n : ℕ) : Type := {μ : YoungDiagram // μ.card = n}

/-- Transposing a Young diagram preserves its number of cells. -/
theorem card_transpose (μ : YoungDiagram) : μ.transpose.card = μ.card := by
  simp [YoungDiagram.card, YoungDiagram.transpose]

/-- **Conjugation** `λ ↦ λ'`: Mathlib's `YoungDiagram.transpose`. -/
def conj {n : ℕ} (l : Partition n) : Partition n :=
  ⟨l.1.transpose, (card_transpose l.1).trans l.2⟩

/-- Conjugation is an involution, `λ'' = λ`. -/
theorem conj_conj {n : ℕ} (l : Partition n) : conj (conj l) = l :=
  Subtype.ext (YoungDiagram.transpose_transpose l.1)

/-- **Self-conjugacy**, `λ' = λ`, for genuine Young diagrams. -/
def SelfConjugate {n : ℕ} (l : Partition n) : Prop := conj l = l

/-- **No partition of `2` is self-conjugate** (`(2)' = (1,1)`): the
    double-magic pair `Z = N = 2` therefore has **no** instance of the
    conjecture below, whereas the pre-2026-11-20 carrier (with `Partition`
    a free field) admitted the one-point model there. -/
theorem not_selfConjugate_two (l : Partition 2) : ¬ SelfConjugate l := by
  intro hl
  obtain ⟨μ, hc⟩ := l
  have hT : μ.transpose = μ := congrArg Subtype.val hl
  have hsym : ∀ c : ℕ × ℕ, c ∈ μ → c.swap ∈ μ := fun c hc' => by
    rw [← hT] at hc'; exact YoungDiagram.mem_transpose.mp hc'
  have hcard : μ.cells.card = 2 := hc
  obtain ⟨x, hx, hx0⟩ := Finset.exists_mem_ne (by omega : 1 < μ.cells.card) ((0 : ℕ), (0 : ℕ))
  have hx' : x ∈ μ := (YoungDiagram.mem_cells _).mp hx
  have h10 : ((1 : ℕ), (0 : ℕ)) ∈ μ ∧ ((0 : ℕ), (1 : ℕ)) ∈ μ := by
    by_cases h1 : 1 ≤ x.1
    · have a : ((1 : ℕ), (0 : ℕ)) ∈ μ := μ.up_left_mem h1 (Nat.zero_le _) hx'
      exact ⟨a, hsym _ a⟩
    · have h2 : 1 ≤ x.2 := by
        rcases x with ⟨i, j⟩; simp at h1 hx0 ⊢; omega
      have a : ((0 : ℕ), (1 : ℕ)) ∈ μ := μ.up_left_mem (Nat.zero_le _) h2 hx'
      exact ⟨hsym _ a, a⟩
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ μ := μ.up_left_mem (Nat.zero_le _) le_rfl h10.1
  have hsub : ({(0, 0), (1, 0), (0, 1)} : Finset (ℕ × ℕ)) ⊆ μ.cells := by
    intro c hc'
    simp only [Finset.mem_insert, Finset.mem_singleton] at hc'
    rcases hc' with rfl | rfl | rfl
    · exact (YoungDiagram.mem_cells _).mpr h00
    · exact (YoungDiagram.mem_cells _).mpr h10.1
    · exact (YoungDiagram.mem_cells _).mpr h10.2
  have := Finset.card_le_card hsub
  rw [hcard] at this
  simp at this

/-- Abstract data of an LR-fusion outcome at level `Z + N`.

    `lrFusion λ μ ν` records the LR-coefficient `c^ν_{λ μ}` of genuine
    partitions.  **Still free** (GAP): neither Mathlib nor the corpus defines
    Littlewood–Richardson coefficients, so `lr` is instance data constrained
    only by the conjugation symmetry `lr_conj`.  `Specht` is an uninterpreted
    label for the Specht module and is used by nothing. -/
class LRFusionData (Z N : ℕ) where
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

/-- The conjecture, encoded as a class.

    A `DoubleMagicConjecture Z N` instance asserts that, when both
    `Z` and `N` are saturated and the unique saturated-shell
    partition at each level is self-conjugate, the LR product
    collapses to a unique self-conjugate fused partition with
    multiplicity one. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
class DoubleMagicConjecture (Z N : ℕ) extends LRFusionData Z N where
  /-- Precondition: both `Z` and `N` are magic numbers. -/
  doubleMagic : DoubleMagic Z N
  /-- The unique saturated-shell partition at level `Z` (provided by
      the categorical-neutrality conjecture upstream). -/
  lambdaZ : Partition Z
  /-- It is self-conjugate, `λ' = λ` (Young-diagram transpose). -/
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

/-- **The one-point model is gone.**  At `Z = N = 2` (both magic) no
    instance exists, because no Young diagram with two cells is
    self-conjugate.  Before 2026-11-20 `Partition := fun _ => Unit`
    inhabited the conjecture here (triage `qou-dx7g`, rank 51). -/
theorem not_doubleMagicConjecture_two_two (c : DoubleMagicConjecture 2 2) : False :=
  not_selfConjugate_two c.lambdaZ c.lambdaZ_selfConj

open scoped Classical in
/-- Conditional theorem: under the double-magic conjecture, the LR
    product is concentrated at the unique fused self-conjugate
    partition. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem lr_concentrated
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : Partition (Z + N)) :
    c.lr c.lambdaZ c.muN ν = if ν = c.nuZN then 1 else 0 := by
  by_cases h : ν = c.nuZN
  · simp [h, c.lr_unique_at_nu]
  · simp [h, c.lr_vanishes_off ν h]

/-- Conditional theorem: under the double-magic conjecture, the
    fused partition `ν_{ZN}` is the unique partition with non-zero
    LR coefficient. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem nu_unique
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : Partition (Z + N)) (hν : c.lr c.lambdaZ c.muN ν ≠ 0) :
    ν = c.nuZN := by
  by_contra h
  exact hν (c.lr_vanishes_off ν h)

/-- Biconditional characterisation of `ν_{ZN}`: under the
    conjecture, `ν` equals the fused partition iff the LR
    coefficient is non-zero (equivalently, equal to 1). -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem nu_iff_lr_nonzero
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : Partition (Z + N)) :
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
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion §"Statement"
theorem lr_kronecker
    (Z N : ℕ) [c : DoubleMagicConjecture Z N]
    (ν : Partition (Z + N)) :
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
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion §"Statement"
-- Ref: [geckpfeiffer2000] Geck & Pfeiffer, LMS Monographs 21, OUP 2000
theorem nu_selfConjugate
    (Z N : ℕ) [c : DoubleMagicConjecture Z N] :
    SelfConjugate c.nuZN := by
  have hsym := c.lr_conj c.lambdaZ c.muN c.nuZN
  rw [c.lambdaZ_selfConj, c.muN_selfConj, c.lr_unique_at_nu] at hsym
  exact nu_unique Z N (conj c.nuZN) (by rw [hsym]; exact one_ne_zero)

end QOU.LRFusion
