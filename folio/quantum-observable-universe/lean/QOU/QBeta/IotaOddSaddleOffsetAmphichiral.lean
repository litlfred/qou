import Mathlib.Tactic
import Mathlib.LinearAlgebra.Prod
import Mathlib.Algebra.Group.Invertible.Basic
import Mathlib.Algebra.GroupWithZero.Invertible
import QOU.QBeta.FiveTwoDTSpectrumSplit

/-!
# QOU.QBeta.IotaOddSaddleOffsetAmphichiral — the saddle offset vanishes iff amphichiral

**Formalize-first structural GATE for the owner's saddle-vector picture.**
A knot-particle is pictured as a *vector* (angle + magnitude) attached to a
saddle point of Bring's surface.  At `q = 1` the bar-involution `q ↔ q⁻¹` acts
trivially, the two chirality-conjugate saddle contributions coincide, and the
vector is **origin-centred**.  For `q > 1` the bar-involution is nontrivial, the
two contributions split, and the vector acquires an **offset** — and the claim
is that the offset is precisely the **ι-odd** (bar-odd, `q ↔ q⁻¹`
antisymmetric) component of the saddle vector.

This file proves the honest gate for that picture: **the ι-odd saddle offset
vanishes iff the knot is (ι-fixed) amphichiral.**  It is deliberately not a
`True`-placeholder; the discriminating content is threefold.

## The involution `ι` and the offset

Let `M` be a module over a commutative ring `R` in which `2` is invertible, and
let `ι : M →ₗ[R] M` be an `R`-linear **involution** (`ι ∘ ι = id`) — the
chirality / mirror involution, i.e. the bar-involution `q ↔ q⁻¹` acting at the
observable (saddle-vector) level.  Decompose any `v` into its ι-even and ι-odd
parts
$$\mathrm{even}(v) = \tfrac12\,(v + ι v),\qquad
   \mathrm{offset}(v) = \mathrm{odd}(v) = \tfrac12\,(v - ι v).$$

## What is proved (non-vacuous — three certified facts)

* `even_add_odd` — `even(v) + offset(v) = v`: a genuine direct-sum
  decomposition (uses `Invertible 2`; false without the `½`).
* `iota_offset_odd` — `ι(offset v) = -offset v`: the offset genuinely lands in
  the `(-1)`-eigenspace of `ι`, i.e. it really **is** the ι-odd component (uses
  `ι` linear + `ι∘ι = id`; false for a non-involution).
* `offset_eq_zero_iff_iotaFixed` — **the headline gate**:
  `offset v = 0 ↔ ι v = v`.  The offset vanishes exactly on the ι-fixed
  (amphichiral) locus.

## Grounding in the certified 5₂ / 4₁ Stokes data (the anti-vacuity anchor)

Modelling the saddle vector as the ordered pair of chirality-conjugate leading
Stokes constants `v_K = (S⁺-const, S⁻-const)` with `ι` the chirality **swap**
`(a,b) ↦ (b,a)` (the amphichiral involution of `BarOddAntisymOffDiagonal`, here
acting on the two chirality labels), the certified merged data of
`FiveTwoDTSpectrumSplit` gives:

* `offset_fourone_zero` — `4₁` is **amphichiral**: its two chirality constants
  coincide (`Splus0_41 0 1 = 3`, one member), so `v_{4₁} = (3,3)` is ι-fixed
  and `offset(4₁) = 0`.
* `offset_fivetwo_ne_zero` — `5₂` is **chiral**: its constants split
  (`Splus0 0 1 = 4`, `Sminus0 0 2 = 3`), so `v_{5₂} = (4,3)` is **not** ι-fixed
  and `offset(5₂) ≠ 0`.
* `fivetwo_offset_numerator_eq_chiralityOdd` — the offset's antisymmetric
  numerator is exactly the certified ι-odd datum
  `chiralityOdd 4 3 = 1` (cast to ℚ): the offset is sourced by the merged
  5₂ chirality-split datum, not a freshly-invented number.

Hence the picture's **structural premise holds**: the ι-odd offset is a genuine
eigencomponent of a real decomposition, it vanishes exactly on the ι-fixed
locus, and on the certified knot data that locus is realised by the amphichiral
`4₁` (offset `0`) and missed by the chiral `5₂` (offset `1/2`, numerator `1`).

## Scope (honest)

This is a **structural gate**, scope-(a), not a bridge or derivation.  The
identification *amphichiral ⟺ ι-fixed saddle vector* is the modelling
convention — backed by the certified `4₁` collapse and `5₂` split — not an
independently re-proved knot-theory theorem.  The file derives no physical
number from the 13 categorical drivers, wires no `c_k`, and inverts no
`Q_β`/CODATA value.  It formalises exactly the claim in the owner's picture:
that the saddle offset is the bar-odd component and vanishes at the amphichiral
(q=1-like) locus.

## Base ring (§7c)

The general theory is stated over a generic `{R : Type*} [CommRing R]
[Invertible (2 : R)]` and `{M : Type*} [AddCommGroup M] [Module R M]` — the
substrate→archimedean wall is not crossed (no ordering, no `Real.*`, no `q₀`).
The concrete grounding uses `R = ℚ` (a field with `2` invertible; **not** `ℝ` —
no archimedean construct is required), reusing the *integer* certified Stokes
data of `FiveTwoDTSpectrumSplit` by casting `ℤ → ℚ`.

-- Ref: [leitner2026] docs/audits/2026-08-02-fivetwo-crossknot-34-resolution.md
-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (5₂ DT spectrum, eqs 96/97/98)
-/

namespace QOU.QBeta.IotaOddSaddleOffsetAmphichiral

/-! ## General theory: the ι-odd offset over a generic module -/

section General

variable {R : Type*} [CommRing R] [Invertible (2 : R)]
variable {M : Type*} [AddCommGroup M] [Module R M]

/-- The ι-**even** component of a saddle vector, `½ (v + ι v)`. -/
def evenPart (ι : M →ₗ[R] M) (v : M) : M := ⅟(2 : R) • (v + ι v)

/-- The **saddle offset** — the ι-**odd** component `½ (v − ι v)`.  This is the
vector's displacement from the ι-fixed (origin-centred, `q = 1`) locus. -/
def offset (ι : M →ₗ[R] M) (v : M) : M := ⅟(2 : R) • (v - ι v)

/-- **Genuine decomposition.** The ι-even part and the offset sum to `v` — so
`offset` is the honest odd summand of a direct-sum splitting, not an ad-hoc
object.  (Uses `Invertible 2`; the identity is false without the `½`.) -/
theorem even_add_odd (ι : M →ₗ[R] M) (v : M) :
    evenPart ι v + offset ι v = v := by
  simp only [evenPart, offset]
  rw [← smul_add]
  have h : (v + ι v) + (v - ι v) = (2 : R) • v := by
    rw [two_smul]; abel
  rw [h, smul_smul, invOf_mul_self, one_smul]

/-- **The offset is genuinely ι-odd.** `ι (offset v) = − offset v`: the offset
lands in the `(-1)`-eigenspace of `ι`, certifying it really is *the* ι-odd
component.  This is where the involution hypothesis `ι ∘ ι = id` is used — the
statement is false for a non-involution `ι`. -/
theorem iota_offset_odd (ι : M →ₗ[R] M) (hι : ∀ v, ι (ι v) = v) (v : M) :
    ι (offset ι v) = - offset ι v := by
  simp only [offset]
  rw [map_smul, map_sub, hι]
  rw [← smul_neg, neg_sub]

/-- **The headline gate.** The saddle offset vanishes **iff** the vector is
ι-fixed (amphichiral).  The `½` is essential in the `⇒` direction (cancelled by
`Invertible 2`); the `⇐` direction is immediate. -/
theorem offset_eq_zero_iff_iotaFixed (ι : M →ₗ[R] M) (v : M) :
    offset ι v = 0 ↔ ι v = v := by
  simp only [offset]
  constructor
  · intro h
    have h2 : (2 : R) • (⅟(2 : R) • (v - ι v)) = (2 : R) • (0 : M) := by rw [h]
    rw [smul_smul, mul_invOf_self, one_smul, smul_zero, sub_eq_zero] at h2
    exact h2.symm
  · intro h
    rw [h, sub_self, smul_zero]

end General

/-! ## Concrete grounding: the certified 5₂ / 4₁ chirality-split saddle data

The saddle vector is the ordered pair of chirality-conjugate leading Stokes
constants `(S⁺-const, S⁻-const) : ℚ × ℚ`, and `ι` is the chirality **swap**.
We reuse the *integer* certified data of `FiveTwoDTSpectrumSplit` by casting
`ℤ → ℚ`. -/

section Concrete

open FiveTwoDTSpectrumSplit

/-- `2` is invertible in `ℚ` (a field) — the concrete base ring is `ℚ`, **not**
`ℝ`; no archimedean construct is used (§7c). -/
noncomputable local instance invTwoRat : Invertible (2 : ℚ) :=
  invertibleOfNonzero (by norm_num)

/-- The chirality **swap** involution `(a,b) ↦ (b,a)` on `ℚ × ℚ`, as a
`ℚ`-linear map.  This is the amphichiral involution `ι` acting on the two
chirality labels of the saddle vector. -/
def swapLM : (ℚ × ℚ) →ₗ[ℚ] (ℚ × ℚ) where
  toFun p := (p.2, p.1)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

@[simp] theorem swapLM_apply (p : ℚ × ℚ) : swapLM p = (p.2, p.1) := rfl

/-- `swapLM` is an involution. -/
theorem swapLM_involutive (p : ℚ × ℚ) : swapLM (swapLM p) = p := rfl

/-- The `5₂` saddle vector: the pair of certified chirality-conjugate leading
Stokes constants `(Splus0 0 1, Sminus0 0 2)`, cast `ℤ → ℚ`. -/
def saddleFiveTwo : ℚ × ℚ :=
  (((Splus0 0 1 : ℤ) : ℚ), ((Sminus0 0 2 : ℤ) : ℚ))

/-- The `4₁` saddle vector: amphichiral, so both chirality constants are the
**same** certified single member `Splus0_41 0 1 = 3` — the vector is diagonal
`(3,3)`, ι-fixed by construction. -/
def saddleFourOne : ℚ × ℚ :=
  (((Splus0_41 0 1 : ℤ) : ℚ), ((Splus0_41 0 1 : ℤ) : ℚ))

/-- The `5₂` saddle vector evaluates to `(4,3)` (the certified split). -/
theorem saddleFiveTwo_eq : saddleFiveTwo = ((4 : ℚ), (3 : ℚ)) := by
  simp only [saddleFiveTwo, splus0_carries_four, sminus0_carries_three]
  norm_num

/-- The `4₁` saddle vector evaluates to `(3,3)` (the certified single member). -/
theorem saddleFourOne_eq : saddleFourOne = ((3 : ℚ), (3 : ℚ)) := by
  simp only [saddleFourOne, fourone_carries_three]
  norm_num

/-- **`4₁` is amphichiral: its saddle offset vanishes.** The two chirality
constants coincide, so the saddle vector is ι-fixed and `offset = 0` (via the
headline gate). -/
theorem offset_fourone_zero : offset swapLM saddleFourOne = 0 := by
  rw [offset_eq_zero_iff_iotaFixed]
  rw [saddleFourOne_eq]
  rfl

/-- **`5₂` is chiral: its saddle offset is nonzero.** The two chirality
constants split (`4 ≠ 3`), so the saddle vector is not ι-fixed and
`offset ≠ 0` (via the headline gate). -/
theorem offset_fivetwo_ne_zero : offset swapLM saddleFiveTwo ≠ 0 := by
  rw [Ne, offset_eq_zero_iff_iotaFixed, saddleFiveTwo_eq]
  simp only [swapLM_apply, Prod.mk.injEq]
  norm_num

/-- **The 5₂ offset is sourced by the certified ι-odd datum.** The offset's
antisymmetric numerator `v.1 − (ι v).1` equals the merged certified chirality
datum `chiralityOdd (Splus0 0 1) (Sminus0 0 2) = 1`, cast `ℤ → ℚ`.  The offset
is `½` of this, i.e. `1/2` — exactly the bar-odd `{4} − {3}` split, not a fresh
number. -/
theorem fivetwo_offset_numerator_eq_chiralityOdd :
    (saddleFiveTwo - swapLM saddleFiveTwo).1
      = ((chiralityOdd (Splus0 0 1) (Sminus0 0 2) : ℤ) : ℚ) := by
  rw [chirality_odd_datum_eq_one, saddleFiveTwo_eq]
  simp only [swapLM_apply, Prod.fst_sub]
  norm_num

/-- **The saddle offset itself is `1/2` for 5₂** — a nonzero displacement whose
size is half the certified ι-odd datum `1`. -/
theorem offset_fivetwo_eq : offset swapLM saddleFiveTwo = ((1 / 2 : ℚ), (-1 / 2 : ℚ)) := by
  rw [offset, saddleFiveTwo_eq]
  simp only [swapLM_apply, invTwoRat]
  norm_num [Prod.ext_iff]

end Concrete

end QOU.QBeta.IotaOddSaddleOffsetAmphichiral
