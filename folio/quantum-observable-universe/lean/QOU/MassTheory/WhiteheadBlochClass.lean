import QOU.MassTheory.PreArchimedeanBloch

/-!
# The Whitehead link Bloch class `4[ζ]`, `ζ² = −1`

The Whitehead link complement is one regular ideal octahedron, which cuts into four
ideal tetrahedra of shape `i` (Thurston). Its Bloch class is therefore `4[i]`. This
file defines `whiteheadClass ζ = 4[ζ]` over any field and proves it lies in `B(F)`
exactly when `ζ² = −1` and `2 ≠ 0`:

  `δ(4[ζ]) = 4 · (ζ ∧ (1 − ζ)) = ζ⁴ ∧ (1 − ζ) = 1 ∧ (1 − ζ) = 0`.

No `⊗ ℚ` is needed, because `ζ` is a root of unity of order dividing `4`. The
decomposition of the octahedron into four shape-`i` tetrahedra is cited, not
formalised.

Pre-Archimedean: no `ℝ`, `ℂ`, limit or regulator.

-- Ref: [thurston1978] The geometry and topology of three-manifolds
-/

namespace QOU.Archimedean.WhiteheadBloch

open QOU.Archimedean.PreArchimedeanBloch

variable {F : Type*} [Field F] [DecidableEq F]

/-- **The Whitehead class** `4[ζ]`. -/
def whiteheadClass (ζ : F) : PreBloch F := 4 • (QuotientAddGroup.mk (gen ζ) : PreBloch F)

/-- If `ζ² = −1` then `4 · u(ζ) = 0` in `F^×` written additively. -/
theorem four_nsmul_u {ζ : F} (h : ζ ^ 2 = -1) : (4 : ℕ) • u ζ = 0 := by
  have h0 : ζ ≠ 0 := by
    rintro rfl; norm_num at h
  simp only [u, ne_eq, h0, not_false_eq_true, dite_true]
  rw [← ofMul_pow]
  have : (Units.mk0 ζ h0) ^ 4 = 1 := by
    ext
    simp only [Units.val_pow_eq_pow_val, Units.val_mk0, Units.val_one]
    rw [show ζ ^ 4 = (ζ ^ 2) ^ 2 by ring, h]; norm_num
  rw [this, ofMul_one]

/-- **`4[ζ] ∈ B(F)`** when `ζ² = −1` and `2 ≠ 0`. -/
theorem whiteheadClass_mem_blochGroup {ζ : F} (h : ζ ^ 2 = -1) (h2 : (2 : F) ≠ 0) :
    whiteheadClass ζ ∈ BlochGroup F := by
  have h0 : ζ ≠ 0 := by
    rintro rfl; norm_num at h
  have h1 : ζ ≠ 1 := by
    rintro rfl
    apply h2
    linear_combination h
  simp only [whiteheadClass, BlochGroup, AddMonoidHom.mem_ker, map_nsmul, deltaP_mk]
  rw [delta_gen _ h0 h1, ← AddMonoidHom.nsmul_apply, ← map_nsmul, four_nsmul_u h, map_zero,
    AddMonoidHom.zero_apply]

end QOU.Archimedean.WhiteheadBloch
