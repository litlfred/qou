import QOU.MathlibExt.OctonionDerivationsBound
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.Tactic

set_option maxHeartbeats 2000000
set_option maxRecDepth 16000

/-!
# QOU.MathlibExt.OctonionDerivationsUpperBound — `dim Der(𝕆) ≤ 14`, closing `dim = 14`

The residual upper bound from `OctonionDerivationsBound`: `finrank Der𝕆 ≤ 14`, i.e. the
Leibniz-defect operator `L` has `rank ≥ 50`. We exhibit 50 endomorphisms `Hfam 0 .. 49`
(integer matrices; rational combinations of the 50 pivot matrix-units, scaled by 2) whose
defect images `L (Hfam s)`, projected onto 50 fixed output coordinates (`rowProj`), are
`2 · (standard basis of ℚ⁵⁰)` (`hrows`, machine-checked by `decide` over ℤ). Hence
`rowProj ∘ L` is surjective, so `rank L ≥ 50` and `finrank Der𝕆 ≤ 14`; with the lower bound
`octDer_finrank_ge` this gives **`octonion_derivation_dim : dim Der(𝕆) = 14`**, sorry-free.

The row-projection identities are proved over `ℤ` (which kernel-reduces under `decide`,
unlike `ℚ`) via a cast bridge `key`; the 50×50 certificate was produced by exact rational
Gaussian elimination on the 512×64 defect matrix. Reference: [baez2002] §4.1.
-/

namespace QOU.MathlibExt.OctonionDerivations

open Matrix QOU.MathlibExt.DerivationRankNullity

/-- Integer basis vector `eₓ`. -/
def ebz (x : Fin 8) : Fin 8 → ℤ := Pi.single x 1

/-- Octonion product over ℤ (same structure constants as `octMul`). -/
def octMulZ (u v : Fin 8 → ℤ) : Fin 8 → ℤ :=
  ![u 0 * v 0 - u 1 * v 1 - u 2 * v 2 - u 3 * v 3 - u 4 * v 4 - u 5 * v 5 - u 6 * v 6 - u 7 * v 7, u 0 * v 1 + u 1 * v 0 + u 2 * v 4 + u 3 * v 7 - u 4 * v 2 + u 5 * v 6 - u 6 * v 5 - u 7 * v 3, u 0 * v 2 - u 1 * v 4 + u 2 * v 0 + u 3 * v 5 + u 4 * v 1 - u 5 * v 3 + u 6 * v 7 - u 7 * v 6, u 0 * v 3 - u 1 * v 7 - u 2 * v 5 + u 3 * v 0 + u 4 * v 6 + u 5 * v 2 - u 6 * v 4 + u 7 * v 1, u 0 * v 4 + u 1 * v 2 - u 2 * v 1 - u 3 * v 6 + u 4 * v 0 + u 5 * v 7 + u 6 * v 3 - u 7 * v 5, u 0 * v 5 - u 1 * v 6 + u 2 * v 3 - u 3 * v 2 - u 4 * v 7 + u 5 * v 0 + u 6 * v 1 + u 7 * v 4, u 0 * v 6 + u 1 * v 5 - u 2 * v 7 + u 3 * v 4 - u 4 * v 3 - u 5 * v 1 + u 6 * v 0 + u 7 * v 2, u 0 * v 7 + u 1 * v 3 + u 2 * v 6 - u 3 * v 1 + u 4 * v 5 - u 5 * v 4 - u 6 * v 2 + u 7 * v 0]

/-- The concrete integer Leibniz defect of a matrix `G` at basis pair `(x,y)`, coord `k`. -/
def defCZ (G : Matrix (Fin 8) (Fin 8) ℤ) (x y k : Fin 8) : ℤ :=
  (G.mulVec (octMulZ (ebz x) (ebz y))) k - (octMulZ (G.mulVec (ebz x)) (ebz y)) k
    - (octMulZ (ebz x) (G.mulVec (ebz y))) k

/-- Rational basis vector `eₓ`. -/
def eb (x : Fin 8) : Fin 8 → ℚ := Pi.single x 1

theorem octMul_cast (u v : Fin 8 → ℤ) (k : Fin 8) :
    octMul (fun i => (u i : ℚ)) (fun j => (v j : ℚ)) k = (octMulZ u v k : ℚ) := by
  fin_cases k <;> simp only [octMul, octMulZ, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.head_cons, Matrix.cons_val, Matrix.cons_val_fin_one] <;> push_cast <;> ring

theorem octMul_cast_fun (u v : Fin 8 → ℤ) :
    octMul (fun i => (u i : ℚ)) (fun j => (v j : ℚ)) = fun k => ((octMulZ u v k : ℤ) : ℚ) :=
  funext (octMul_cast u v)

theorem mulVec_cast (H : Matrix (Fin 8) (Fin 8) ℤ) (v : Fin 8 → ℤ) (a : Fin 8) :
    ((H.map (Int.cast)).mulVec (fun i => (v i : ℚ))) a = ((H.mulVec v) a : ℚ) := by
  simp only [Matrix.mulVec, dotProduct, Matrix.map_apply, Fin.sum_univ_eight]; push_cast; ring

theorem mulVec_cast_fun (H : Matrix (Fin 8) (Fin 8) ℤ) (v : Fin 8 → ℤ) :
    (H.map (Int.cast)).mulVec (fun i => (v i : ℚ)) = fun a => ((H.mulVec v) a : ℚ) :=
  funext (mulVec_cast H v)

theorem eb_cast (x : Fin 8) : eb x = (fun i => ((ebz x i : ℤ) : ℚ)) := by
  funext i; simp only [eb, ebz, Pi.single_apply]; split <;> simp

/-- The concrete rational Leibniz defect of a matrix `G`. -/
def defCq (G : Matrix (Fin 8) (Fin 8) ℚ) (x y k : Fin 8) : ℚ :=
  (G.mulVec (octMul (eb x) (eb y))) k - (octMul (G.mulVec (eb x)) (eb y)) k
    - (octMul (eb x) (G.mulVec (eb y))) k

theorem defC_eq (G : Matrix (Fin 8) (Fin 8) ℚ) (x y k : Fin 8) :
    leibnizDefect octMulₗ (Matrix.mulVecLin G) (eb x) (eb y) k = defCq G x y k := by
  rw [defCq]
  simp only [leibnizDefect_apply, octMulₗ_apply, Matrix.mulVecLin_apply, Pi.sub_apply]

theorem defCq_cast (H : Matrix (Fin 8) (Fin 8) ℤ) (x y k : Fin 8) :
    defCq (H.map (Int.cast)) x y k = ((defCZ H x y k : ℤ) : ℚ) := by
  simp only [defCq, defCZ, eb_cast, mulVec_cast_fun, octMul_cast_fun, octMul_cast]
  push_cast; ring

/-- **Cast bridge:** the abstract ℚ defect equals the concrete ℤ defect (cast). -/
theorem key (H : Matrix (Fin 8) (Fin 8) ℤ) (x y k : Fin 8) :
    leibnizDefect octMulₗ (Matrix.mulVecLin (H.map (Int.cast))) (eb x) (eb y) k
      = ((defCZ H x y k : ℤ) : ℚ) := by
  rw [defC_eq, defCq_cast]

/-- Output-coordinate selectors for the 50-dimensional row projection (the pivot rows of the
Gaussian elimination of the 512×64 defect matrix). -/
def rx : Fin 50 → Fin 8 := ![0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 4, 2, 3, 3, 3, 0, 1, 1, 1, 2, 0, 2, 2, 0, 3]
def ry : Fin 50 → Fin 8 := ![0, 1, 2, 3, 2, 5, 5, 3, 1, 1, 1, 3, 1, 3, 3, 3, 2, 3, 2, 3, 2, 5, 5, 3, 3, 2, 2, 3, 2, 5, 5, 3, 4, 3, 3, 3, 2, 1, 1, 2, 5, 2, 5, 5, 3, 6, 3, 3, 6, 3]
def rk : Fin 50 → Fin 8 := ![0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 4, 1, 1, 0, 2, 0, 5, 4, 4, 2, 4, 2, 2, 0, 5, 7, 7, 3, 7, 3, 3, 0, 6, 6, 0, 0, 0, 1, 0, 0, 6, 6, 5, 7, 0, 5, 3, 2, 0]

/-- Projection of a trilinear defect value onto its 50 pivot output coordinates. -/
def rowProj : ((Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)) →ₗ[ℚ] (Fin 50 → ℚ) where
  toFun g := fun i => g (eb (rx i)) (eb (ry i)) (rk i)
  map_add' g h := by funext i; simp [eb]
  map_smul' c g := by funext i; simp [eb]

@[simp] theorem rowProj_apply (g) (i : Fin 50) :
    rowProj g i = g (eb (rx i)) (eb (ry i)) (rk i) := rfl

/-- `2 · (standard basis vector s)` of `ℚ⁵⁰`. -/
def twoSingle (s : Fin 50) : Fin 50 → ℚ := fun i => if i = s then 2 else 0

/-- **Generic finrank plumbing.** A family of integer endomorphisms whose defect
row-projections are `2 · (standard basis)` forces `finrank (ker L) ≤ 14`. -/
theorem finrank_le_of_rows
    (Hfam : Fin 50 → Matrix (Fin 8) (Fin 8) ℤ)
    (hrows : ∀ s, rowProj (leibnizDefect octMulₗ (Matrix.mulVecLin ((Hfam s).map (Int.cast))))
      = twoSingle s) :
    Module.finrank ℚ (LinearMap.ker (leibnizDefect octMulₗ)) ≤ 14 := by
  set G : (Fin 50 → ℚ) →ₗ[ℚ] ((Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)) :=
    ∑ s, (LinearMap.proj s).smulRight (Matrix.mulVecLin ((Hfam s).map (Int.cast))) with hG
  have hGe : ∀ s, G (Pi.single s 1) = Matrix.mulVecLin ((Hfam s).map (Int.cast)) := by
    intro s
    simp only [hG, LinearMap.sum_apply, LinearMap.smulRight_apply, LinearMap.proj_apply]
    rw [Finset.sum_eq_single s (fun b _ hb => by simp [Pi.single_apply, hb]) (by simp)]
    simp [Pi.single_apply]
  set LG := (leibnizDefect octMulₗ).comp G with hLG
  have hsec : rowProj.comp LG = (2 : ℚ) • LinearMap.id := by
    apply (Pi.basisFun ℚ (Fin 50)).ext
    intro s
    simp only [LinearMap.comp_apply, hLG, LinearMap.smul_apply, LinearMap.id_apply,
      Pi.basisFun_apply]
    rw [hGe s, hrows s]
    funext i
    simp only [twoSingle, Pi.smul_apply, Pi.single_apply, smul_eq_mul]
    split <;> simp
  have hsurj : Function.Surjective (rowProj.comp (leibnizDefect octMulₗ)) := by
    have hcomp : (rowProj.comp (leibnizDefect octMulₗ)).comp G = (2 : ℚ) • LinearMap.id := by
      rw [LinearMap.comp_assoc, ← hLG]; exact hsec
    have hsc : Function.Surjective ((rowProj.comp (leibnizDefect octMulₗ)).comp G) := by
      rw [hcomp]; intro y; exact ⟨(2⁻¹ : ℚ) • y, by simp⟩
    exact Function.Surjective.of_comp hsc
  have hmaptop : Submodule.map rowProj (LinearMap.range (leibnizDefect octMulₗ)) = ⊤ := by
    rw [← LinearMap.range_comp]; exact LinearMap.range_eq_top.mpr hsurj
  have h50 : 50 ≤ Module.finrank ℚ (LinearMap.range (leibnizDefect octMulₗ)) := by
    have hle := Submodule.finrank_map_le rowProj (LinearMap.range (leibnizDefect octMulₗ))
    rw [hmaptop, finrank_top] at hle
    simpa using hle
  have h64 := octCarrier_finrank_ker_add_finrank_range octMulₗ
  have hle : Module.finrank ℚ (LinearMap.ker (leibnizDefect octMulₗ)) + 50 ≤ 64 :=
    h64 ▸ Nat.add_le_add_left h50 _
  omega

/-- The 50 explicit range-witness endomorphisms (integer matrices). -/
def Hfam : Fin 50 → Matrix (Fin 8) (Fin 8) ℤ :=
  ![!![-2, 0, 0, 0, 0, 0, 0, 0;
        0, -1, 0, 0, 0, 0, 0, 0;
        0, 0, -1, 0, 0, 0, 0, 0;
        0, 0, 0, -1, 0, 0, 0, 0;
        0, 0, 0, 0, -2, 0, 0, 0;
        0, 0, 0, 0, 0, -2, 0, 0;
        0, 0, 0, 0, 0, 0, -3, 0;
        0, 0, 0, 0, 0, 0, 0, -2],
!![0, -1, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, -1, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, -1, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, -1, 0, 0;
        0, 1, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, -1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 0, -1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 1, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 1, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 0, 0, 1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, -1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, -1, 0, 0, 0, 0, 0, 0;
        2, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, -1, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 1, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 1, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 0, 0, 0, 0, 1],
!![0, 0, 0, 0, -1, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 1, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 2, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, -1, 0, 0, 0, 0, 0;
        0, 0, 0, 0, -2, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, -1, 0, 0;
        0, 1, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, -1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 1, 0, 0;
        0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 2, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        2, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 2, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 2, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        2, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, -2, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 2, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 2, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 2, 0, 0, 0, 0;
        0, 0, -2, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2],
!![0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 0, 0, -1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 2, 0, 0, 0;
        0, 0, 0, -1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 2, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, -2, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        2, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, -2, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 2, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 1, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 1, 0, 0, 0;
        0, 0, 0, 0, 0, 1, 0, 0;
        0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, -1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, -1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, -1;
        0, 0, 0, 0, 0, -1, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, -1, 0, 0;
        0, 0, 0, 0, 0, 0, -1, 0;
        0, 0, 0, 1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 1;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        2, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 2, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, -2, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, -2, 0, 0, 0, 0, 0;
        0, 2, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, -2, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        2, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 2, 0, 0;
        0, 0, 0, 0, 0, 0, 2, 0;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 2, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 2, 0, 0;
        0, -2, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 2;
        0, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        2, 0, 0, 0, 0, 0, 0, 0],
!![0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 1, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 0, 0, 0;
        0, 0, 0, 0, 0, 1, 0, 0;
        0, 0, 0, 0, 0, 0, 1, 0;
        0, 0, 0, 0, 0, 0, 0, 1]]

/-- The defect row-projections of the family are `2 · (standard basis)` — machine-checked
over ℤ. -/
theorem hrows (s : Fin 50) :
    rowProj (leibnizDefect octMulₗ (Matrix.mulVecLin ((Hfam s).map (Int.cast)))) = twoSingle s := by
  have hZ : ∀ s i : Fin 50, defCZ (Hfam s) (rx i) (ry i) (rk i) = (if i = s then (2 : ℤ) else 0) := by
    decide
  funext i
  rw [rowProj_apply, key, hZ s i, twoSingle]
  split <;> simp

/-- **Upper bound (fully proved):** `dim Der(𝕆) ≤ 14`. -/
theorem octDer_finrank_le : Module.finrank ℚ Der𝕆 ≤ 14 :=
  finrank_le_of_rows Hfam hrows

/-- **`dim Der(𝕆) = 14`** — the octonion derivation algebra is the 14-dimensional compact
`𝔤₂`, now fully machine-verified (lower bound `octDer_finrank_ge`, upper bound
`octDer_finrank_le`). -/
theorem octonion_derivation_dim : Module.finrank ℚ Der𝕆 = 14 :=
  le_antisymm octDer_finrank_le octDer_finrank_ge

end QOU.MathlibExt.OctonionDerivations