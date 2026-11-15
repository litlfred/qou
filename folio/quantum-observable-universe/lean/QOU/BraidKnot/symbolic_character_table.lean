import QOU.BraidKnot.SytSmallShapeCounts
import QOU.BraidKnot.SytSmallShapeCountsLarger

/-!
# QOU.BraidKnot.symbolic_character_table — `χ_λ(σ₁) = c_λ · h`  (concrete, sorry-free)

**Proposition** ([`prop:symbolic-character-table`](../../../quantum-observable-universe/mass-theory/symbolic-character-table.md)).

*For each self-conjugate partition `λ ∈ {[2,1], [3,1,1], [3,2,1], [4,1,1,1]}`, the
single-generator seminormal character `χ_λ(σ₁)` is `c_λ · h` where `h = q − q⁻¹`
and `c_λ = #SYT(λ)/2 ∈ {1, 3, 8, 10}`.*

## Disposition (integrity) — the `sorry` is now discharged

Earlier revisions carried an **opaque** `chiSigma` class field and left the
proposition as `sorry` + citation: the seminormal-form summation `a_ρ = h/(1 −
q^{−2ρ})` over standard Young tableaux was *not in Mathlib*, so `χ_λ(σ)` could not
be computed. That apparatus now exists in-repo:

- `SeminormalCharacterConnector.sigmaOneCharacter_eq_card_mul` proves
  `χ_λ(σ₁) = |R_row| · h` for **every** self-conjugate `μ` (the off-diagonal class
  is empty for a single generator; `|R_row| = |R_col|` by the conjugate-transpose
  bijection);
- the per-shape counts `card_rowClass_mu{21,311,321,4111}` (via the hook-length /
  enumeration count `#SYT`) give `|R_row| = c_λ ∈ {1, 3, 8, 10}`.

So `chiSigma` below is now a **concrete `def`** (the σ₁ seminormal character of the
shape), not an opaque field, and `symbolic_character_table` is proved outright — no
`sorry`, no class conclusion field. The manuscript's `[3,1,1]` pair/triple
character polynomials are retained as sorry-free algebraic identities.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/symbolic-character-table.md
-- Ref: [sagan2001] The Symmetric Group, §3.3 (Young's seminormal form)
-/

open QOU.Mathlib
open QOU.BraidKnot.SeminormalCharacterConnector
open QOU.BraidKnot.SytSmallShapeCounts
open QOU.BraidKnot.SytSmallShapeCountsLarger

namespace QOU.BraidKnot

/-! §7c base ring. The whole table is Hecke seminormal-form algebra:
`sigmaOneCharacter` is already generic over `[Field R]`, and
`sigmaOneCharacter_eq_card_mul` additionally wants `(2 : R) ≠ 0` — the same
characteristic condition the `meson-em-sinh-closed-form` port needed. -/
variable {R : Type*} [Field R] [CharZero R]

/-- The four self-conjugate partition labels recorded in the table. -/
inductive SelfConjugatePartition
  | p21
  | p311
  | p321
  | p4111
  deriving DecidableEq, Repr

/-- The `c_λ` coefficient for each self-conjugate partition: integer valued,
    `c_λ = #SYT(λ)/2`. -/
def cCoefficient : SelfConjugatePartition → ℤ
  | .p21   => 1
  | .p311  => 3
  | .p321  => 8
  | .p4111 => 10

/-- The self-conjugate Young diagram of each tabulated partition. -/
def shapeOf : SelfConjugatePartition → YoungDiagram
  | .p21   => mu21
  | .p311  => mu311
  | .p321  => mu321
  | .p4111 => mu4111

/-- **The concrete σ₁ seminormal character** of the self-conjugate shape (purely
    diagonal — the off-diagonal class is empty for the single generator). Replaces
    the former opaque class field. -/
noncomputable def chiSigma (q h : R) (lam : SelfConjugatePartition) : R :=
  sigmaOneCharacter (shapeOf lam) q h

/-- **`|R_row|(shapeOf λ) = c_λ`** — the same-row class count of each tabulated shape
    is its coefficient `{1, 3, 8, 10}`. -/
theorem card_rowClass_shapeOf (lam : SelfConjugatePartition) :
    ((rowClass (shapeOf lam)).card : ℤ) = cCoefficient lam := by
  cases lam
  · simp [shapeOf, cCoefficient, card_rowClass_mu21]
  · simp [shapeOf, cCoefficient, card_rowClass_mu311]
  · simp [shapeOf, cCoefficient, card_rowClass_mu321]
  · simp [shapeOf, cCoefficient, card_rowClass_mu4111]

/-- **Self-conjugate single-generator character factorisation**
    ([`prop:symbolic-character-table`]): `χ_λ(σ₁) = c_λ · h` for every self-conjugate
    partition `λ`, proved concretely (`sorry`-free). The character is the σ₁
    seminormal character `sigmaOneCharacter`; the factorisation follows from
    `|R_row| = |R_col|` (`sigmaOneCharacter_eq_card_mul`) and the per-shape counts
    `|R_row| = c_λ`. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/symbolic-character-table.md
theorem symbolic_character_table (q h : R) (hq : q ≠ 0) (lam : SelfConjugatePartition) :
    chiSigma q h lam = (cCoefficient lam : R) * h := by
  have hsc : (shapeOf lam).transpose = shapeOf lam := by
    cases lam
    · exact mu21_transpose
    · exact mu311_transpose
    · exact mu321_transpose
    · exact mu4111_transpose
  have hge : 2 ≤ (shapeOf lam).cells.card := by
    cases lam
    · exact card_ge_two
    · exact card_ge_two_mu311
    · exact card_ge_two_mu321
    · exact card_ge_two_mu4111
  simp only [chiSigma]
  rw [sigmaOneCharacter_eq_card_mul hsc hge q h hq two_ne_zero]
  have hc : ((rowClass (shapeOf lam)).card : R) = (cCoefficient lam : R) := by
    exact_mod_cast card_rowClass_shapeOf lam
  rw [hc]

/-! ## Concrete `[3,1,1]` pair/triple characters (sorry-free algebra)

The manuscript's exact-in-`q` character values for the self-conjugate partition
`[3,1,1]`, encoded as real polynomials in `h = q − q⁻¹`. -/

/-- Manuscript adjacent-pair character: `χ_{[3,1,1]}(σᵢσ_{i+1}) = h²`. -/
def chi311_adjacentPair (h : R) : R := h ^ 2

/-- Manuscript far-commuting-pair character (`|i − j| ≥ 2`):
    `χ_{[3,1,1]}(σᵢσⱼ) = h² − 2`. -/
def chi311_farPair (h : R) : R := h ^ 2 - 2

/-- Manuscript triple character: `χ_{[3,1,1]}(σᵢσ_{i+1}σ_{i+2}) = −h`. -/
def chi311_triple (h : R) : R := -h

omit [CharZero R] in
/-- **Commutation defect**: the adjacent-pair and far-commuting-pair characters of
    `[3,1,1]` differ by exactly `2` — the braid-relation contribution lost when the
    generators commute. -/
theorem chi311_pair_commutation_defect (h : R) :
    chi311_adjacentPair h - chi311_farPair h = 2 := by
  unfold chi311_adjacentPair chi311_farPair
  ring

omit [CharZero R] in
/-- **Adjacent-pair character is the square of the triple character**:
    `χ(σᵢσ_{i+1}) = χ(σᵢσ_{i+1}σ_{i+2})²` (both `h²`). -/
theorem chi311_adjacent_eq_triple_sq (h : R) :
    chi311_adjacentPair h = (chi311_triple h) ^ 2 := by
  unfold chi311_adjacentPair chi311_triple
  ring

end QOU.BraidKnot
