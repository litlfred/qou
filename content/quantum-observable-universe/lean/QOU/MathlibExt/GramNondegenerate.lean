import Mathlib.LinearAlgebra.SesquilinearForm.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
# An invertible Gram matrix makes a bilinear form nondegenerate on the span

For a bilinear form `B` and a finite family `v : ι → V`, if the Gram matrix
`(B (v i) (v j))` has nonzero determinant then

  `span k (range v) ⊓ (span k (range v))ᗮ = ⊥`.

**Mathlib does not have this.** It has `LinearMap.BilinForm.Nondegenerate` and
`Submodule.orthogonalBilin`, and it has the Gram matrix of a *basis*
(`LinearMap.BilinForm.toMatrix`), but nothing connecting the determinant of the
Gram matrix of an arbitrary spanning family to triviality of the radical.

## Why it is wanted here

This is the last link of the chain that closes `specht_form_nondegenerate`:

* `MathlibExt.RankMinor` turns linear independence into a nonzero minor;
* `MathlibExt.CauchyBinet` turns a nonzero minor into `det (M Mᵀ) ≠ 0` over any
  characteristic-zero field;
* this file turns `det Gram ≠ 0` into `W ⊓ Wᗮ = ⊥`.

Nothing in it mentions Specht modules, tabloids, or `ℤ` — it is the general
statement, and the Specht application supplies `v` and the determinant.

## Note on which side the form is evaluated

`Submodule.orthogonalBilin N B` is the **left** complement: `x ∈ Nᗮ` means
`B n x = 0` for every `n ∈ N` (Mathlib flags the chirality explicitly). The
proof below therefore reads the Gram matrix rows-first — `gramMatrix B v j i`
is `B (v j) (v i)` — so that orthogonality gives `mulVec`, not `vecMul`. For a
symmetric form the distinction is invisible, but the theorem does not assume
symmetry and this is the side that works without it.
-/

namespace QOU.MathlibExt.GramNondegenerate

open Matrix

variable {k V ι : Type*} [Field k] [AddCommGroup V] [Module k V]

/-- The **Gram matrix** of a family of vectors under a bilinear form:
`gramMatrix B v i j = B (v i) (v j)`. -/
def gramMatrix (B : V →ₗ[k] V →ₗ[k] k) (v : ι → V) : Matrix ι ι k :=
  fun i j => B (v i) (v j)

@[simp] theorem gramMatrix_apply (B : V →ₗ[k] V →ₗ[k] k) (v : ι → V) (i j : ι) :
    gramMatrix B v i j = B (v i) (v j) := rfl

/-- **The radical is trivial when the Gram matrix is invertible.**

`x` in both the span and its orthogonal complement is a combination `∑ cᵢ vᵢ`
whose coefficient vector is killed by the Gram matrix; a nonzero determinant
makes `mulVec` injective, so `c = 0` and `x = 0`. -/
theorem span_inf_orthogonalBilin_eq_bot [Fintype ι] [DecidableEq ι]
    (B : V →ₗ[k] V →ₗ[k] k) (v : ι → V) (hdet : (gramMatrix B v).det ≠ 0) :
    Submodule.span k (Set.range v) ⊓
        (Submodule.span k (Set.range v)).orthogonalBilin B = ⊥ := by
  refine le_antisymm (fun x hx => ?_) bot_le
  obtain ⟨hxW, hxperp⟩ := hx
  obtain ⟨c, hc⟩ := (Submodule.mem_span_range_iff_exists_fun k).mp hxW
  -- orthogonality against each `v j` says the Gram matrix kills `c`
  have hzero : (gramMatrix B v).mulVec c = 0 := by
    funext j
    have hj : B (v j) x = 0 := hxperp (v j) (Submodule.subset_span ⟨j, rfl⟩)
    rw [← hc, map_sum] at hj
    simpa [Matrix.mulVec, dotProduct, mul_comm] using hj
  -- a nonzero determinant makes `mulVec` injective, so `c = 0`
  have hunit : IsUnit (gramMatrix B v) :=
    (Matrix.isUnit_iff_isUnit_det _).mpr (isUnit_iff_ne_zero.mpr hdet)
  have hc0 : c = 0 :=
    Matrix.mulVec_injective_iff_isUnit.mpr hunit (by rw [hzero, Matrix.mulVec_zero])
  rw [Submodule.mem_bot, ← hc, hc0]
  simp

/-- The same statement against a submodule already known to be that span — the
shape a caller has when `W` is *defined* as `Submodule.span k (Set.range v)`. -/
theorem inf_orthogonalBilin_eq_bot [Fintype ι] [DecidableEq ι]
    (B : V →ₗ[k] V →ₗ[k] k) (v : ι → V) (W : Submodule k V)
    (hW : Submodule.span k (Set.range v) = W)
    (hdet : (gramMatrix B v).det ≠ 0) :
    W ⊓ W.orthogonalBilin B = ⊥ := by
  rw [← hW]
  exact span_inf_orthogonalBilin_eq_bot B v hdet

/-! ## Diagonal Gram ⇒ linear independence

The other thing a Gram matrix is good for. Nondegeneracy above needs the whole
matrix invertible; independence needs only that it is **diagonal with nonzero
diagonal**, which is what an orthogonality relation delivers without any
normalisation of the diagonal entries.

This is the step that lets the Specht completeness count avoid
`[IsAlgClosed k]`: `FDRep.char_orthonormal` pins the diagonal to `1` and needs
algebraic closure to do it, but a *bound* only needs the diagonal nonzero. -/

/-- **A family with a diagonal, nonvanishing Gram matrix is linearly
independent.** No symmetry, no nondegeneracy of `B` elsewhere. -/
theorem linearIndependent_of_gram_diagonal {ι : Type*} [Fintype ι]
    (B : V →ₗ[k] V →ₗ[k] k) (v : ι → V)
    (hoff : ∀ i j, i ≠ j → B (v i) (v j) = 0)
    (hdiag : ∀ i, B (v i) (v i) ≠ 0) :
    LinearIndependent k v := by
  classical
  refine Fintype.linearIndependent_iff.mpr (fun c hc j => ?_)
  -- pair the relation with `v j`: every cross term dies
  have h0 : B (∑ i, c i • v i) (v j) = 0 := by rw [hc]; simp
  rw [map_sum, LinearMap.sum_apply] at h0
  simp only [map_smul, LinearMap.smul_apply, smul_eq_mul] at h0
  rw [Finset.sum_eq_single j (fun i _ hij => by rw [hoff i j hij, mul_zero])
    (fun hj => absurd (Finset.mem_univ j) hj)] at h0
  exact (mul_eq_zero.mp h0).resolve_right (hdiag j)

end QOU.MathlibExt.GramNondegenerate
