import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Obstructions to the essay's "trace observables are triangulation cochains"

Review of an external essay, owner request 2026-11-25
(`docs/coordination/owner-rulings.md`; audit
`docs/audits/2026-11-25-holography-qns-essay-review.md`). Each result below
settles the premise of one verdict there. All are stated over a generic ring
or ordered field (§7c); only `realGtOne_not_rootOfUnity` uses `ℝ`/`ℂ`, because
"root of unity" is a statement about the complex number `q₀`.

1. `hecke_inverse_eq` / `trace_inverse_eq`: from `σ² = hσ + 1` and
   `σ·s = 1`, the inverse is `σ − h`, so any linear trace has
   `tr σ⁻¹ = tr σ − h·tr 1`. Derived, not assumed.
2. `trace_add_inverse_conventionD_pos`: with `tr 1 = 1`, `tr σ = z_D =
   q³/(q²+1)` (convention D) and `h = q − q⁻¹`, `tr σ + tr σ⁻¹ =
   (q⁴+1)/(q(q²+1)) > 0` for every `q > 0`. A 1-cochain must change sign when
   its edge is reversed; a trace of the edge word does not. So
   `e ↦ tr(ψ·w_e)` with `w_ē = w_e⁻¹` is not a cochain.
3. `sum_coboundary_eq_zero` / `const_eq_zero_of_coboundary`: on a closed
   oriented surface (each column of the face–edge incidence sums to zero),
   the total of `dα` over faces vanishes, so a constant face value `c` is a
   coboundary only if `card F • c = 0`. Over a field of characteristic 0 and
   a nonempty face set, `c = 0`.
4. `realGtOne_not_rootOfUnity`: a real `q > 1` is not a root of unity in `ℂ`.
   This is the hypothesis the fusion (finite-rank) quotient of `Rep U_q` needs.
5. `perm3_not_commutative`: `S₃` is nonabelian, so `Vec_{S₃}` has
   `δ_g ⊗ δ_h ≇ δ_h ⊗ δ_g` for some `g, h` and carries no braiding, while
   Turaev–Viro is defined for it. Flip (Pachner 2–2) invariance therefore
   does not use, and is not, a braid relation.
-/

namespace QOU.BringsSurface.TraceCochainObstructions

open scoped BigOperators

section Hecke

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- In an algebra where `σ` satisfies the Hecke quadratic `σ² = h σ + 1` and
has a right inverse `s`, that inverse is `σ − h`. -/
theorem hecke_inverse_eq (σ s : A) (h : R)
    (hquad : σ * σ = h • σ + 1) (hinv : σ * s = 1) :
    s = σ - algebraMap R A h := by
  have h1 : (σ * σ - h • σ) * s = σ - algebraMap R A h := by
    rw [sub_mul, mul_assoc, hinv, mul_one, smul_mul_assoc, hinv, Algebra.smul_def, mul_one]
  have h2 : σ * σ - h • σ = 1 := by rw [hquad, add_sub_cancel_left]
  rw [h2, one_mul] at h1
  exact h1

/-- Consequently any `R`-linear trace satisfies `tr s = tr σ − h · tr 1`. -/
theorem trace_inverse_eq (tr : A →ₗ[R] R) (σ s : A) (h : R)
    (hquad : σ * σ = h • σ + 1) (hinv : σ * s = 1) :
    tr s = tr σ - h * tr 1 := by
  rw [hecke_inverse_eq σ s h hquad hinv, map_sub, Algebra.algebraMap_eq_smul_one,
    map_smul, smul_eq_mul]

end Hecke

section ConventionD

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Closed form of `2 z_D − h` with `z_D = q³/(q²+1)` and `h = q − q⁻¹`. -/
theorem twice_zD_sub_h (q : K) (hq : 0 < q) :
    2 * (q ^ 3 / (q ^ 2 + 1)) - (q - q⁻¹) = (q ^ 4 + 1) / (q * (q ^ 2 + 1)) := by
  have hq0 : q ≠ 0 := hq.ne'
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **Edge reversal is not a sign flip for the trace.** For a linear trace with
`tr 1 = 1`, `tr σ = z_D` and the Hecke relation at `h = q − q⁻¹`, the sum
`tr σ + tr σ⁻¹` is strictly positive for every `q > 0`, so it is never `0`. -/
theorem trace_add_inverse_conventionD_pos {A : Type*} [Ring A] [Algebra K A]
    (tr : A →ₗ[K] K) (σ s : A) (q : K) (hq : 0 < q)
    (hquad : σ * σ = (q - q⁻¹) • σ + 1) (hinv : σ * s = 1)
    (hone : tr 1 = 1) (hz : tr σ = q ^ 3 / (q ^ 2 + 1)) :
    0 < tr σ + tr s := by
  rw [trace_inverse_eq tr σ s (q - q⁻¹) hquad hinv, hone, mul_one, hz]
  have : q ^ 3 / (q ^ 2 + 1) + (q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹))
      = (q ^ 4 + 1) / (q * (q ^ 2 + 1)) := by
    rw [← twice_zD_sub_h q hq]; ring
  rw [this]
  positivity

end ConventionD

section Stokes

variable {R : Type*} [CommRing R] {F E : Type*} [Fintype F] [Fintype E]

/-- **Discrete Stokes on a closed oriented surface.** If every edge appears in
the face boundaries with total signed multiplicity zero, the face-sum of any
coboundary `dα` vanishes. -/
theorem sum_coboundary_eq_zero (d : F → E → R) (hclosed : ∀ e, ∑ f, d f e = 0)
    (α : E → R) : ∑ f, ∑ e, d f e * α e = 0 := by
  rw [Finset.sum_comm]
  simp [← Finset.sum_mul, hclosed]

/-- A constant face value `c` that is a coboundary satisfies `card F • c = 0`. -/
theorem card_smul_eq_zero_of_coboundary (d : F → E → R) (hclosed : ∀ e, ∑ f, d f e = 0)
    (α : E → R) (c : R) (hconst : ∀ f, ∑ e, d f e * α e = c) :
    (Fintype.card F : R) * c = 0 := by
  have := sum_coboundary_eq_zero d hclosed α
  simp only [hconst, Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at this
  exact this

/-- Over a field of characteristic zero with at least one face, the only
constant coboundary is `0`. -/
theorem const_eq_zero_of_coboundary {K : Type*} [Field K] [CharZero K]
    [Nonempty F] (d : F → E → K) (hclosed : ∀ e, ∑ f, d f e = 0)
    (α : E → K) (c : K) (hconst : ∀ f, ∑ e, d f e * α e = c) : c = 0 := by
  have h := card_smul_eq_zero_of_coboundary d hclosed α c hconst
  have hF : (Fintype.card F : K) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  exact (mul_eq_zero.mp h).resolve_left hF

end Stokes

/-- A real `q > 1` is not a root of unity in `ℂ`: `(q : ℂ) ^ n ≠ 1` for `n ≥ 1`. -/
theorem realGtOne_not_rootOfUnity (q : ℝ) (hq : 1 < q) (n : ℕ) (hn : n ≠ 0) :
    (q : ℂ) ^ n ≠ 1 := by
  intro h
  have h' : ((q ^ n : ℝ) : ℂ) = 1 := by rw [Complex.ofReal_pow]; exact h
  have : q ^ n = 1 := Complex.ofReal_eq_one.mp h'
  exact (one_lt_pow₀ hq hn).ne' this

/-- `S₃` is not commutative, so `Vec_{S₃}` admits no braiding. -/
theorem perm3_not_commutative : ∃ g h : Equiv.Perm (Fin 3), g * h ≠ h * g :=
  ⟨Equiv.swap 0 1, Equiv.swap 1 2, by decide⟩

end QOU.BringsSurface.TraceCochainObstructions
