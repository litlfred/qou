import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.Sum
import Mathlib.Data.Fintype.Prod
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.QuantumObservableUniverses.NSymHostStructure

Structural facts bearing on the open composition rule of
`conj:g-action-on-substrate` (does `𝒩_sym = tr_F(e_sym^EW · e_H)` compose
the electroweak hosts by `⊗` or by `⊕`?).  Audit:
`docs/audits/2026-11-20-nsym-host-corpus-route.md`.

Everything is stated over a generic commutative ring or field (AGENTS.md §7c).
Nothing here selects a reading by comparison with the back-solved anchor
`𝒩_sym(q₀) ≈ 213.11`.

1. **Sum vs product of slot weights.** A weighted trace (`dim_q`) is additive
   over a direct sum (`Sum` index type) and multiplicative over a tensor product
   of slots (`Prod` index type).  These are the two readings (b) and (a).
2. **Orthogonal summands kill the composite.** Idempotents supported on
   different summands of a direct sum compose to zero, so a non-zero
   `tr_F(e_sym^EW · e_H)` needs the two idempotents on different tensor factors.
3. **`W⁺` and `W⁻` are one line, not two hosts.** In the sector realisation of
   `thm:electroweak-triplet-charge-spin-from-involution`, `W⁻` carries the
   swap-image `(a⁻¹, a)` of `W⁺`'s carrier vector `(a, a⁻¹)`.  Their σ-odd
   projections are negatives of each other, so they span a single line: they
   cannot be two independent direct summands or two tensor factors.
4. **The Hoefsmit slot object is `V ⊗ V`, with `dim_q = [2]_q² = [3]_q + [1]_q`.**
-/

namespace QOU.QuantumObservableUniverses.NSymHostStructure

open scoped BigOperators

/-! ### 1. Additive over `⊕`, multiplicative over `⊗` -/

section Weights
variable {R : Type*} [CommRing R]

/-- `dim_q` of a direct sum of two weighted bases is the sum (reading (b)). -/
theorem qdim_sum {ι κ : Type*} [Fintype ι] [Fintype κ] (f : ι → R) (g : κ → R) :
    (∑ x : ι ⊕ κ, Sum.elim f g x) = (∑ i, f i) + ∑ j, g j :=
  Fintype.sum_sum_type _

/-- `dim_q` of a tensor product of two weighted bases is the product (reading (a)). -/
theorem qdim_tensor {ι κ : Type*} [Fintype ι] [Fintype κ] (f : ι → R) (g : κ → R) :
    (∑ x : ι × κ, f x.1 * g x.2) = (∑ i, f i) * ∑ j, g j := by
  rw [Fintype.sum_prod_type, Finset.sum_mul_sum]

/-- Three tensor slots (the disjoint strand pairs `σ₁, σ₃, σ₅`): the full
    weighted trace factors as the product of the three slot traces. -/
theorem qdim_three_slots (a b c : Fin 2 → R) :
    (∑ x : (Fin 2 × Fin 2) × Fin 2, a x.1.1 * b x.1.2 * c x.2)
      = (∑ i, a i) * (∑ j, b j) * ∑ k, c k := by
  rw [qdim_tensor (fun y : Fin 2 × Fin 2 => a y.1 * b y.2) c, qdim_tensor a b]

/-- The joint projector `E_{abc}` of the three slots has weighted trace equal to
    the product of the three per-slot block weights. -/
theorem qdim_joint_projector (a b c : Fin 2 → R) (i j k : Fin 2) :
    (∑ x : (Fin 2 × Fin 2) × Fin 2,
        (if x = ((i, j), k) then (1 : R) else 0) * (a x.1.1 * b x.1.2 * c x.2))
      = a i * b j * c k := by
  simp

end Weights

/-! ### 2. Idempotents on orthogonal summands compose to zero -/

section Orthogonal
variable {R : Type*} [CommRing R] {ι κ : Type*}

/-- Diagonal idempotent supported on the left summand. -/
def leftProj (e : ι → R) : ι ⊕ κ → R := Sum.elim e 0

/-- Diagonal idempotent supported on the right summand. -/
def rightProj (e : κ → R) : ι ⊕ κ → R := Sum.elim 0 e

/-- `e_sym^EW · e_H = 0` when the two act on different summands of `(G-1)`. -/
theorem orthogonal_summands_compose_zero (e : ι → R) (f : κ → R) :
    leftProj (κ := κ) e * rightProj (ι := ι) f = 0 := by
  funext x; cases x <;> simp [leftProj, rightProj]

end Orthogonal

/-! ### 3. `W⁻` is the negative of `W⁺` in the σ-odd sector -/

section Sector
variable {R : Type*} [Field R]

/-- σ-odd projection of a two-block carrier vector (half the swap-difference). -/
def oddPart (p : R × R) : R × R := ((2 : R)⁻¹ * (p.1 - p.2), (2 : R)⁻¹ * (p.2 - p.1))

/-- The σ-odd vectors of `W⁺ = (a, a⁻¹)` and `W⁻ = (a⁻¹, a)` are negatives. -/
theorem oddPart_Wminus_eq_neg_Wplus (a : R) :
    oddPart (a⁻¹, a) = -oddPart (a, a⁻¹) := by
  ext <;> simp [oddPart] <;> ring

/-- Hence they are linearly dependent: `1 • v₊ + 1 • v₋ = 0`. -/
theorem Wplus_Wminus_dependent (a : R) :
    oddPart (a, a⁻¹) + oddPart (a⁻¹, a) = 0 := by
  rw [oddPart_Wminus_eq_neg_Wplus]; exact add_neg_cancel _

/-- …and the line is non-zero exactly when `a² ≠ 1` (the theorem's hypothesis),
    given `2 ≠ 0` and `a ≠ 0`. -/
theorem oddPart_ne_zero (a : R) (h2 : (2 : R) ≠ 0) (ha : a ≠ 0) (hsq : a ^ 2 ≠ 1) :
    oddPart (a, a⁻¹) ≠ 0 := by
  intro h
  have h1 := congrArg Prod.fst h
  simp only [oddPart, Prod.fst_zero] at h1
  have hd : a - a⁻¹ = 0 := by
    rcases mul_eq_zero.mp h1 with h' | h'
    · exact absurd (inv_eq_zero.mp h') h2
    · exact h'
  apply hsq
  have : a = a⁻¹ := sub_eq_zero.mp hd
  calc a ^ 2 = a * a := by ring
    _ = a * a⁻¹ := by rw [← this]
    _ = 1 := mul_inv_cancel₀ ha

end Sector

/-! ### 4. `dim_q (V ⊗ V) = [2]_q² = [3]_q + [1]_q` -/

section QDim
variable {R : Type*} [Field R]

/-- Symmetric `[2]_q = q + q⁻¹`. -/
def q2 (q : R) : R := q + q⁻¹

/-- Symmetric `[3]_q = q² + 1 + q⁻²`. -/
def q3 (q : R) : R := q ^ 2 + 1 + q⁻¹ ^ 2

/-- Symmetric `[4]_q = q³ + q + q⁻¹ + q⁻³`. -/
def q4 (q : R) : R := q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3

/-- Clebsch–Gordan at the level of `dim_q`: `V_{1/2} ⊗ V_{1/2} = V_1 ⊕ V_0`.
    The two-strand Hoefsmit slot carries `[2]_q² = [3]_q + 1`, not `[4]_q`. -/
theorem q2_sq_eq_q3_add_one (q : R) (hq : q ≠ 0) : q2 q ^ 2 = q3 q + 1 := by
  unfold q2 q3; field_simp; ring

/-- `[4]_q = [2]_q · [3]_q − [2]_q`, i.e. `V_{1/2} ⊗ V_1 = V_{3/2} ⊕ V_{1/2}`:
    `[4]_q` is `dim_q V_{3/2}`, a spin not present in Table 1 of the block. -/
theorem q4_eq (q : R) (hq : q ≠ 0) : q4 q = q2 q * q3 q - q2 q := by
  unfold q2 q3 q4; field_simp; ring

end QDim

end QOU.QuantumObservableUniverses.NSymHostStructure
