/-
  `σ₀σ₁σ₀` is not a scalar multiple of a two-photon product in the corpus's
  concrete Iwahori–Hecke algebra `H₃`.

  `QOU.BraidKnot.LongestWordNotTwoPhoton.photon_mul_photon_ne_smul_longest`
  proves the claim in any `K`-algebra carrying two elements `x, y` with
  `x² = h x + 1`, `y² = h y + 1`, `xyx = yxy`, `y` a unit, and
  `1, x, y, xy, yx, xyx` linearly independent. This module discharges those
  hypotheses in `QOU.Hecke.IwahoriHecke K q 2`, the corpus's own `RingQuot`
  presentation of the three-strand Hecke algebra.

  **The normalisation, and the one hypothesis it costs.** `QOU.Hecke.IwahoriHecke`
  is presented with `T_i² = (q − 1) T_i + q`, i.e. `(T_i − q)(T_i + 1) = 0`. The
  photon is written in the corpus normalisation `σ_i² = (t − t⁻¹) σ_i + 1`
  (AGENTS.md §7a). The two agree under `σ_i = t⁻¹ T_i` exactly when `q = t²`, so
  the bridge is stated on `IwahoriHecke K (t^2) 2` for a nonzero `t ∈ K`. That
  is a choice of square root of the presentation parameter, not an assumption
  about the algebra: every `q` that has a square root in `K` is covered, and over
  an algebraically closed field every nonzero `q` is. When `q` has no square root
  in `K` the rescaled generator does not exist in `H₃` over `K`, and this module
  says nothing about that case.

  **Independence.** The six words are independent by
  `QOU.Hecke.TwBasis.orbitMap_TwOf`: the cyclic representation on `K[S₃]` sends
  the product of the `T_i` along a reduced word to the basis vector of its
  permutation. Reducedness of the six words is checked through
  `QOU.Hecke.Inversions.length_eq_invCount`. No basis theorem and no Matsumoto
  is used, and nothing here depends on the value of `t` beyond `t ≠ 0`; in
  particular roots of unity and `t² = −1` are not exceptional.

  Generic field `K` (§7c); no ordering, no Real construct.

  -- Ref: [leitner2026] predicted-spectra, def:photon;
  --      docs/audits/2026-11-21-electron-word-gs-interactions.md §C2c, §8
-/
import QOU.BraidKnot.LongestWordNotTwoPhoton
import QOU.Hecke.TwIndependent
import QOU.Hecke.PermLength
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas

namespace QOU.BraidKnot.LongestWordNotTwoPhotonHecke

open QOU.Photon QOU.Hecke QOU.Hecke.IwahoriHecke QOU.Hecke.TwBasis
open QOU.Hecke.Inversions QOU.Hecke.SymmetricCoxeter

/-! ## The six standard words are independent (any commutative ring) -/

section Words

variable (K : Type*) [CommRing K] (q : K)

/-- The six reduced words of `S₃`, read so that `TwOf` gives
    `1, T₀, T₁, T₀T₁, T₁T₀, T₀T₁T₀` (`TwOf` multiplies on the left). -/
def words : Fin 6 → List (Fin 2) :=
  ![[], [0], [1], [1, 0], [0, 1], [0, 1, 0]]

/-- Their permutations, as products of adjacent transpositions. -/
def perms : Fin 6 → Equiv.Perm (Fin 3) :=
  ![1, Equiv.swap 0 1, Equiv.swap 1 2, Equiv.swap 1 2 * Equiv.swap 0 1,
    Equiv.swap 0 1 * Equiv.swap 1 2, Equiv.swap 0 1 * Equiv.swap 1 2 * Equiv.swap 0 1]

theorem wordProd_words (k : Fin 6) :
    (permCoxeterSystem 2).wordProd (words k) = perms k := by
  fin_cases k <;>
    simp [words, perms, CoxeterSystem.wordProd, permCox_simple, s_eq_swap, mul_assoc]

theorem perms_injective : Function.Injective perms := by
  decide

theorem words_isReduced (k : Fin 6) : (permCoxeterSystem 2).IsReduced (words k) := by
  show (permCoxeterSystem 2).length _ = _
  rw [wordProd_words, length_eq_invCount]
  fin_cases k <;> decide

theorem TwOf_words :
    (fun k => TwOf K q 2 (words k))
      = ![(1 : IwahoriHecke K q 2), σ K q 2 0, σ K q 2 1, σ K q 2 0 * σ K q 2 1,
          σ K q 2 1 * σ K q 2 0, σ K q 2 0 * σ K q 2 1 * σ K q 2 0] := by
  funext k
  fin_cases k <;> simp [TwOf, words, mul_assoc]

/-- **The six words `1, T₀, T₁, T₀T₁, T₁T₀, T₀T₁T₀` are linearly independent in
    `H₃(q)`**, over any commutative ring and for every `q`. -/
theorem linearIndependent_six :
    LinearIndependent K
      ![(1 : IwahoriHecke K q 2), σ K q 2 0, σ K q 2 1, σ K q 2 0 * σ K q 2 1,
        σ K q 2 1 * σ K q 2 0, σ K q 2 0 * σ K q 2 1 * σ K q 2 0] := by
  rw [← TwOf_words]
  refine LinearIndependent.of_comp (orbitMap K q 2) ?_
  have hcomp : (orbitMap K q 2) ∘ (fun k => TwOf K q 2 (words k))
      = fun k => Finsupp.single (perms k) (1 : K) := by
    funext k
    simp only [Function.comp_apply]
    rw [orbitMap_TwOf K q 2 _ (words_isReduced k), wordProd_words]
  rw [hcomp]
  exact (Finsupp.linearIndependent_single_one K (Equiv.Perm (Fin 3))).comp _
    perms_injective

end Words

/-! ## A generator with `y² = h y + 1` is a unit -/

/-- `y² = h y + 1` makes `y` a unit with inverse `y − h`. -/
def unitOfQuadratic {K A : Type*} [CommRing K] [Ring A] [Algebra K A] (h : K) (y : A)
    (hy : y * y = h • y + 1) : Aˣ where
  val := y
  inv := y - h • 1
  val_inv := by rw [mul_sub, hy, mul_smul_comm, mul_one]; abel
  inv_val := by rw [sub_mul, hy, smul_mul_assoc, one_mul]; abel

/-! ## The rescaled generators of `H₃(t²)` -/

section Rescaled

variable {K : Type*} [Field K] (t : K)

/-- The corpus generator `σ_i = t⁻¹ T_i ∈ H₃(t²)`, satisfying
    `σ_i² = (t − t⁻¹) σ_i + 1`. -/
noncomputable def sg (i : Fin 2) : IwahoriHecke K (t ^ 2) 2 := t⁻¹ • σ K (t ^ 2) 2 i

theorem sg_quadratic (ht : t ≠ 0) (i : Fin 2) :
    sg t i * sg t i = (t - t⁻¹) • sg t i + 1 := by
  have h1 : t⁻¹ * t⁻¹ * (t ^ 2 - 1) = (t - t⁻¹) * t⁻¹ := by field_simp
  have h2 : t⁻¹ * t⁻¹ * t ^ 2 = 1 := by field_simp
  rw [sg, smul_mul_smul_comm, σ_quadratic, smul_add, smul_smul, smul_smul, smul_smul, h1, h2,
    one_smul]

theorem sg_braid :
    sg t 0 * sg t 1 * sg t 0 = sg t 1 * sg t 0 * sg t 1 := by
  have hb := σ_braid K (t ^ 2) 2 0 (by decide)
  simp only [sg, smul_mul_smul_comm]
  exact congrArg _ hb

/-- The second generator as a unit of `H₃(t²)`. -/
noncomputable def sgUnit (ht : t ≠ 0) : (IwahoriHecke K (t ^ 2) 2)ˣ :=
  unitOfQuadratic (t - t⁻¹) (sg t 1) (sg_quadratic t ht 1)

theorem linearIndependent_sg (ht : t ≠ 0) :
    LinearIndependent K
      ![(1 : IwahoriHecke K (t ^ 2) 2), sg t 0, sg t 1, sg t 0 * sg t 1, sg t 1 * sg t 0,
        sg t 0 * sg t 1 * sg t 0] := by
  have hti : t⁻¹ ≠ 0 := inv_ne_zero ht
  let c : Fin 6 → Kˣ := ![1, Units.mk0 t⁻¹ hti, Units.mk0 t⁻¹ hti,
    Units.mk0 (t⁻¹ * t⁻¹) (mul_ne_zero hti hti), Units.mk0 (t⁻¹ * t⁻¹) (mul_ne_zero hti hti),
    Units.mk0 (t⁻¹ * t⁻¹ * t⁻¹) (mul_ne_zero (mul_ne_zero hti hti) hti)]
  have h := (linearIndependent_six K (t ^ 2)).units_smul c
  convert h using 1
  funext k
  fin_cases k <;> simp [c, sg, Units.smul_def, smul_smul, mul_assoc]

/-- **In the corpus's `H₃(t²)`, no product of two photons is a nonzero multiple of
    `σ₀σ₁σ₀`.** Here `σ_i = t⁻¹ T_i` are the corpus-normalised generators
    (`σ_i² = (t − t⁻¹)σ_i + 1`) and `γ` is `QOU.Photon.photon`, the photon
    `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`. Holds for every nonzero `t` in every field. -/
theorem photon_mul_photon_ne_smul_longest_H3 (ht : t ≠ 0) (φ ψ : Colour K) (c : K)
    (hprod : photon (sg t 0) (sgUnit t ht) φ * photon (sg t 0) (sgUnit t ht) ψ
      = c • (sg t 0 * sg t 1 * sg t 0)) :
    c = 0 :=
  LongestWordNotTwoPhoton.photon_mul_photon_ne_smul_longest (t - t⁻¹) (sg t 0)
    (sgUnit t ht) (sg_quadratic t ht 0) (sg_quadratic t ht 1) (sg_braid t)
    (linearIndependent_sg t ht) φ ψ c hprod

/-- The same, against the unnormalised longest word `T₀T₁T₀` of the presentation:
    `σ₀σ₁σ₀ = t⁻³ T₀T₁T₀`, so the two statements are equivalent. -/
theorem photon_mul_photon_ne_smul_T_longest (ht : t ≠ 0) (φ ψ : Colour K) (c : K)
    (hprod : photon (sg t 0) (sgUnit t ht) φ * photon (sg t 0) (sgUnit t ht) ψ
      = c • (σ K (t ^ 2) 2 0 * σ K (t ^ 2) 2 1 * σ K (t ^ 2) 2 0)) :
    c = 0 := by
  have hlong : σ K (t ^ 2) 2 0 * σ K (t ^ 2) 2 1 * σ K (t ^ 2) 2 0
      = (t * t * t) • (sg t 0 * sg t 1 * sg t 0) := by
    simp only [sg, smul_mul_smul_comm, smul_smul]
    rw [show t * t * t * (t⁻¹ * t⁻¹ * t⁻¹) = 1 by field_simp, one_smul]
  rw [hlong, smul_smul] at hprod
  have := photon_mul_photon_ne_smul_longest_H3 t ht φ ψ _ hprod
  rcases mul_eq_zero.mp this with h | h
  · exact h
  · exact absurd h (by simp [ht])

end Rescaled

end QOU.BraidKnot.LongestWordNotTwoPhotonHecke
