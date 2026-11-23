import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Order.Hom.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination

/-!
# A strange strand: the `sl_n` Jimbo braiding restricted to two flavours, and the forced wall

Level-`n` Jimbo braiding `Ř` on `Cⁿ ⊗ Cⁿ`, `h = q - q⁻¹`, basis `eᵢ ⊗ eⱼ`:

* `Ř (eᵢ ⊗ eᵢ) = q · eᵢ ⊗ eᵢ`,
* `Ř (eᵢ ⊗ eⱼ) = eⱼ ⊗ eᵢ` for `i < j`,
* `Ř (eᵢ ⊗ eⱼ) = eⱼ ⊗ eᵢ + h · eᵢ ⊗ eⱼ` for `j < i`.

For `n = 2` this is the braiding of `NucleonWeightSpaceTraces` (`e₁ = u`, `e₂ = d`); for `n = 3`
the third flavour is `e₃ = s`.

## Results

1. `jimbo_entry_ne_zero`: `Ř` only ever sends `eᵢ ⊗ eⱼ` into `span(eᵢ ⊗ eⱼ, eⱼ ⊗ eᵢ)`. So the span
   of any set of flavours, on every strand, is preserved.
2. `jimbo_submatrix_orderEmbedding`: restricted to any two flavours `a < b` (an order embedding
   `Fin 2 ↪o Fin n`), `Ř` **is** the `sl₂` braiding. In particular the `(u, s)` and `(d, s)`
   restrictions of the `sl₃` braiding are literally the `(u, d)` one. Consequence for the octet:
   the weight spaces of `Σ⁺ = uus`, `Σ⁻ = dds` carry the proton-type matrices and
   `Ξ⁰ = uss`, `Ξ⁻ = dss` the neutron-type ones. This file proves the two-strand statement;
   the three-strand weight-space consequence (and with it equal plain traces of every braid word
   on the two members of each isospin pair, via `NucleonWeightSpaceTraces.trace_word_eq`) is
   checked by exact computation in the accompanying probe, not yet in Lean.
3. `reflection_diag_iff`: for a diagonal boundary matrix `K = diag(a, b, c)` on the first strand,
   the constant reflection equation `Ř K₁ Ř K₁ = K₁ Ř K₁ Ř` holds iff
   `b (a - b) = 0`, `c (a - c) = 0` and `c (b - c) = 0` (for `q ≠ 0`, `q² ≠ 1`).
4. `strange_entry_forced`: if the wall treats `u` and `d` alike (`a = b`) and is not a
   scalar (`c ≠ a`), then `c = 0`. The reflection equation forces the boundary to annihilate `s`.

No numerical value enters.
-/

namespace QOU.BraidsAndKnots.StrangeStrandOctet

open Matrix
open scoped Kronecker

variable {R : Type*} [Field R]

/-- The level-`n` Jimbo braiding on `Cⁿ ⊗ Cⁿ`, as a matrix indexed by (output, input). -/
def jimbo (n : ℕ) (q : R) : Matrix (Fin n × Fin n) (Fin n × Fin n) R :=
  fun x y =>
    if y.1 = y.2 then (if x = y then q else 0)
    else (if x = (y.2, y.1) then 1 else 0) + (if y.2 < y.1 ∧ x = y then q - q⁻¹ else 0)

/-- **Flavour sets are preserved.** A nonzero entry of `Ř` from `eᵢ ⊗ eⱼ` lands on `eᵢ ⊗ eⱼ`
or on `eⱼ ⊗ eᵢ`. -/
theorem jimbo_entry_ne_zero {n : ℕ} (q : R) (x y : Fin n × Fin n) (h : jimbo n q x y ≠ 0) :
    x = y ∨ x = (y.2, y.1) := by
  unfold jimbo at h
  by_cases hy : y.1 = y.2
  · rw [if_pos hy] at h
    by_cases hx : x = y
    · exact Or.inl hx
    · rw [if_neg hx] at h; exact absurd rfl h
  · rw [if_neg hy] at h
    by_cases hx : x = (y.2, y.1)
    · exact Or.inr hx
    · rw [if_neg hx, zero_add] at h
      by_cases hc : y.2 < y.1 ∧ x = y
      · exact Or.inl hc.2
      · rw [if_neg hc] at h; exact absurd rfl h

/-- **Two-flavour restriction is the `sl₂` braiding.** For any order embedding
`f : Fin 2 ↪o Fin n` (two flavours `f 0 < f 1`), restricting `Ř` to those flavours on both
strands gives exactly the level-2 Jimbo braiding. -/
theorem jimbo_submatrix_orderEmbedding {n : ℕ} (q : R) (f : Fin 2 ↪o Fin n) :
    (jimbo n q).submatrix (Prod.map f f) (Prod.map f f) = jimbo 2 q := by
  ext ⟨a, b⟩ ⟨i, j⟩
  simp only [submatrix_apply, Prod.map_apply, jimbo, Prod.mk.injEq, f.injective.eq_iff,
    f.lt_iff_lt]

/-- The level-3 braiding with `s` as the third flavour, restricted to `(u, s)`. -/
def usFlavours : Fin 2 ↪o Fin 3 :=
  OrderEmbedding.ofStrictMono ![0, 2] (by intro i j h; fin_cases i <;> fin_cases j <;> simp_all)

/-- The level-3 braiding restricted to `(d, s)`. -/
def dsFlavours : Fin 2 ↪o Fin 3 :=
  OrderEmbedding.ofStrictMono ![1, 2] (by intro i j h; fin_cases i <;> fin_cases j <;> simp_all)

/-- The level-3 braiding restricted to `(u, d)`. -/
def udFlavours : Fin 2 ↪o Fin 3 :=
  OrderEmbedding.ofStrictMono ![0, 1] (by intro i j h; fin_cases i <;> fin_cases j <;> simp_all)

/-- The `(u, s)` sector of the `sl₃` braiding is the `(u, d)` sector: a strange strand paired
with an up strand braids exactly like a down strand paired with an up strand. -/
theorem us_sector_eq_ud_sector (q : R) :
    (jimbo 3 q).submatrix (Prod.map usFlavours usFlavours) (Prod.map usFlavours usFlavours) =
      (jimbo 3 q).submatrix (Prod.map udFlavours udFlavours) (Prod.map udFlavours udFlavours) := by
  rw [jimbo_submatrix_orderEmbedding, jimbo_submatrix_orderEmbedding]

/-- The `(d, s)` sector of the `sl₃` braiding is the `(u, d)` sector. -/
theorem ds_sector_eq_ud_sector (q : R) :
    (jimbo 3 q).submatrix (Prod.map dsFlavours dsFlavours) (Prod.map dsFlavours dsFlavours) =
      (jimbo 3 q).submatrix (Prod.map udFlavours udFlavours) (Prod.map udFlavours udFlavours) := by
  rw [jimbo_submatrix_orderEmbedding, jimbo_submatrix_orderEmbedding]

/-! ## The constant reflection equation for a diagonal wall on `C³` -/

/-- The boundary matrix `K = diag(a, b, c)` acting on the first strand, i.e. `K ⊗ 1`
(diagonal, with entry `![a, b, c] i` on `eᵢ ⊗ eⱼ`). -/
def wall (a b c : R) : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R :=
  Matrix.diagonal fun p => ![a, b, c] p.1

/-- The defect `Ř K₁ Ř K₁ - K₁ Ř K₁ Ř` of the constant reflection equation. -/
def reflectionDefect (q a b c : R) : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R :=
  jimbo 3 q * wall a b c * jimbo 3 q * wall a b c - wall a b c * jimbo 3 q * wall a b c * jimbo 3 q

/-- The middle product `Ř K₁ Ř`. -/
def sandwich (q a b c : R) : Matrix (Fin 3 × Fin 3) (Fin 3 × Fin 3) R :=
  jimbo 3 q * wall a b c * jimbo 3 q

theorem sandwich_apply (q a b c : R) (x y : Fin 3 × Fin 3) :
    sandwich q a b c x y = ∑ z, jimbo 3 q x z * ![a, b, c] z.1 * jimbo 3 q z y := by
  simp only [sandwich, wall]
  rw [Matrix.mul_apply]
  simp only [Matrix.mul_diagonal]

/-- For a diagonal wall the defect factors as `(d_y - d_x) · (Ř K₁ Ř)_{xy}`. -/
theorem reflectionDefect_apply (q a b c : R) (x y : Fin 3 × Fin 3) :
    reflectionDefect q a b c x y =
      (![a, b, c] y.1 - ![a, b, c] x.1) * sandwich q a b c x y := by
  have h2 : wall a b c * jimbo 3 q * wall a b c * jimbo 3 q =
      wall a b c * (jimbo 3 q * wall a b c * jimbo 3 q) := by
    simp only [Matrix.mul_assoc]
  unfold reflectionDefect
  rw [h2, Matrix.sub_apply]
  change (sandwich q a b c * wall a b c) x y - (wall a b c * sandwich q a b c) x y = _
  unfold wall
  rw [Matrix.mul_diagonal, Matrix.diagonal_mul]
  ring

/-- `Ř K₁ Ř` only links `eᵢ ⊗ eⱼ` to itself or to `eⱼ ⊗ eᵢ`. -/
theorem sandwich_ne_zero (q a b c : R) (x y : Fin 3 × Fin 3) (h : sandwich q a b c x y ≠ 0) :
    x = y ∨ x = (y.2, y.1) := by
  by_contra hxy
  push_neg at hxy
  apply h
  rw [sandwich_apply]
  refine Finset.sum_eq_zero fun z _ => ?_
  by_cases h1 : jimbo 3 q x z = 0
  · rw [h1, zero_mul, zero_mul]
  by_cases h2 : jimbo 3 q z y = 0
  · rw [h2, mul_zero]
  exfalso
  rcases jimbo_entry_ne_zero q x z h1 with hx | hx <;>
    rcases jimbo_entry_ne_zero q z y h2 with hz | hz
  · exact hxy.1 (hx.trans hz)
  · exact hxy.2 (hx.trans hz)
  · exact hxy.2 (by rw [hx, hz])
  · exact hxy.1 (by rw [hx, hz])

/-- **Diagonal walls.** For `q ≠ 0` and `q² ≠ 1`, `diag(a, b, c)` solves the constant reflection
equation iff `b (a - b) = 0`, `c (a - c) = 0` and `c (b - c) = 0`. -/
theorem reflection_diag_iff (q a b c : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    reflectionDefect q a b c = 0 ↔ b * (a - b) = 0 ∧ c * (a - c) = 0 ∧ c * (b - c) = 0 := by
  have hh : q - q⁻¹ ≠ 0 := by
    intro h
    apply hq2
    have : q * (q - q⁻¹) = 0 := by rw [h, mul_zero]
    field_simp at this
    linear_combination this
  constructor
  · intro h
    have e1 := congrFun (congrFun h (1, 0)) (0, 1)
    have e2 := congrFun (congrFun h (2, 0)) (0, 2)
    have e3 := congrFun (congrFun h (2, 1)) (1, 2)
    rw [Matrix.zero_apply, reflectionDefect_apply, sandwich_apply] at e1 e2 e3
    simp [jimbo] at e1 e2 e3
    refine ⟨?_, ?_, ?_⟩
    · rcases e1 with e | e | e
      · rw [e, mul_zero]
      · exact absurd e hh
      · rw [e, zero_mul]
    · rcases e2 with e | e | e
      · rw [e, mul_zero]
      · exact absurd e hh
      · rw [e, zero_mul]
    · rcases e3 with e | e | e
      · rw [e, mul_zero]
      · exact absurd e hh
      · rw [e, zero_mul]
  · rintro ⟨h1, h2, h3⟩
    have g1 : b = 0 ∨ a = b := by
      rcases mul_eq_zero.mp h1 with e | e
      · exact Or.inl e
      · exact Or.inr (sub_eq_zero.mp e)
    have g2 : c = 0 ∨ a = c := by
      rcases mul_eq_zero.mp h2 with e | e
      · exact Or.inl e
      · exact Or.inr (sub_eq_zero.mp e)
    have g3 : c = 0 ∨ b = c := by
      rcases mul_eq_zero.mp h3 with e | e
      · exact Or.inl e
      · exact Or.inr (sub_eq_zero.mp e)
    ext x y
    rw [Matrix.zero_apply, reflectionDefect_apply]
    by_cases hs : sandwich q a b c x y = 0
    · rw [hs, mul_zero]
    rcases sandwich_ne_zero q a b c x y hs with rfl | rfl
    · rw [sub_self, zero_mul]
    · obtain ⟨i, j⟩ := y
      rw [sandwich_apply]
      fin_cases i <;> fin_cases j <;>
        simp [jimbo, Fintype.sum_prod_type, Fin.sum_univ_three] <;>
        first
        | (rcases g1 with e | e <;> simp [e])
        | (rcases g2 with e | e <;> simp [e])
        | (rcases g3 with e | e <;> simp [e])

/-- **The strange entry is forced.** A diagonal wall that treats `u` and `d` alike
(`a = b`) and is not a scalar (`c ≠ a`) solves the reflection equation only if `c = 0`. -/
theorem strange_entry_forced (q a c : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hca : c ≠ a) (h : reflectionDefect q a a c = 0) : c = 0 := by
  obtain ⟨-, h2, -⟩ := (reflection_diag_iff q a a c hq hq2).mp h
  rcases mul_eq_zero.mp h2 with h | h
  · exact h
  · exact absurd (sub_eq_zero.mp h).symm hca

/-- The isospin-respecting wall `diag(a, a, 0)` does solve the reflection equation. -/
theorem ud_projector_wall_solves (q a : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    reflectionDefect q a a 0 = 0 :=
  (reflection_diag_iff q a a 0 hq hq2).mpr ⟨by ring, by ring, by ring⟩

end QOU.BraidsAndKnots.StrangeStrandOctet
