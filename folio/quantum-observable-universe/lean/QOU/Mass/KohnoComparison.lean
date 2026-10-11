import QOU.Mass.IdempotentTraceRigidity
import Mathlib.Data.Matrix.Basis
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas

/-!
# Rigidity comparison for representations of a split semisimple algebra

This is step (b) of the rigidity route to the Kohno comparison
(docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §5), proved in the form in which the
argument is actually clean: **for a fixed split semisimple algebra**

    B = ∏_{i ∈ ι} Matrix (d i) (d i) K,

which is what the Hecke algebra becomes after the Wedderburn isomorphism
(`QOU.SchurWeyl.heckeWedderburn : Hecke K q q⁻¹ n ≃ₐ[K] ∏_λ Matrix (SYT λ) (SYT λ) K`).

Write `u i a b = Pi.single i (E_{ab})` for the matrix units of `B` and `o i : d i` for a chosen
base index in each block.

* `decomp` — for an algebra map `φ : B →ₐ[K] End V`, the map
  `v ↦ (i, a) ↦ φ(u i (o i) a) v` is a linear isomorphism of `V` onto
  `∏_i (d i → R_i)`, `R_i = range φ(u i (o i) (o i))` (the multiplicity space of block `i`), and
  it intertwines `φ` with the standard action (`decomp_map`).
* `exists_intertwiner_of_finrank_eq` — **two representations with the same multiplicities
  `dim R_i` are isomorphic.** This is the algebraic core that replaces "a module over a
  semisimple algebra is determined by its character" in a form that needs no character theory.
* `exists_conj_of_rank_eq` — the same in matrices: if `rank φ(u i o o) = rank ψ(u i o o)` for
  every block, then `φ` and `ψ` are conjugate by an invertible matrix.
* `conj_of_isPreconnected` — **rigidity.** Two families `x ↦ φ_x, ψ_x` of algebra maps
  `B →ₐ[ℂ] Matrix n n ℂ`, continuous in `x` on a preconnected set `S` (only the images of the
  base idempotents `u i o o` need be continuous), that are conjugate at one point `x₀ ∈ S`,
  are conjugate at every point of `S`. The multiplicities are ranks of continuous idempotent
  families, hence locally constant (`QOU.Mass.IdempotentTraceRigidity`).

## What this does and does not give for KZ versus Jimbo

To turn `conj_of_isPreconnected` into the Kohno comparison one needs, on a connected set `S`
of couplings `κ` with `q = e^{2πiκ}`:

1. the KZ representation factors through `H_n(q)` — proved for two strands
   (`QOU.Mass.KZTwoStrandHecke.heckeOfKZTwoStrand`), reduced to one generator for all `n`
   (`QOU.Mass.BraidHeckeFactor.isHeckeQuad_all_of_zero`), **open for `n ≥ 3`**;
2. both representations, pulled back along `(heckeWedderburn q)⁻¹`, are continuous in `κ` on
   the base idempotents. **Open**: `heckeWedderburn` is built at each `q` separately by
   `AlgEquiv.ofBijective`, and nothing proves its inverse varies continuously with `q`;
3. a base point `x₀ ∈ S` where the two are conjugate. At `κ = 0` both are the flip action, but
   `q = 1` there, and `heckeWedderburn` assumes `q` is not a root of unity, which excludes
   `q = 1`; so the base point must be supplied by the `q = 1` (group-algebra) Wedderburn
   decomposition glued continuously to the generic one, which is again item 2.

None of 1–3 is assumed or claimed here. The theorems below are unconditional statements about
representations of a fixed `∏ Matrix`.
-/

namespace QOU.Mass.KohnoComparison

open Matrix Module

section Blocks

variable (K : Type*) [Field K] {ι : Type*} [Fintype ι] [DecidableEq ι]
  (d : ι → Type*) [∀ i, Fintype (d i)] [∀ i, DecidableEq (d i)]

/-- The split semisimple algebra `∏_i Matrix (d i) (d i) K`. -/
abbrev Blocks : Type _ := ∀ i, Matrix (d i) (d i) K

variable {K d}

/-- The matrix unit `E_{ab}` of block `i`. -/
def unit (i : ι) (a b : d i) : Blocks K d := Pi.single i (Matrix.single a b 1)

omit [Fintype ι] in
lemma unit_mul_same (i : ι) (a b c : d i) : unit i a b * unit i b c = (unit i a c : Blocks K d) := by
  rw [unit, unit, unit, ← Pi.single_mul, single_mul_single_same, one_mul]

omit [Fintype ι] in
lemma unit_mul_of_ne (i : ι) (a b c e : d i) (h : b ≠ c) :
    unit i a b * unit i c e = (0 : Blocks K d) := by
  rw [unit, unit, ← Pi.single_mul, single_mul_single_of_ne _ _ _ _ h, Pi.single_zero]

omit [Fintype ι] in
lemma unit_mul_of_ne_idx {i j : ι} (h : i ≠ j) (a b : d i) (c e : d j) :
    unit i a b * unit j c e = (0 : Blocks K d) := by
  funext k
  simp only [unit, Pi.mul_apply, Pi.zero_apply]
  by_cases hk : k = i
  · subst hk; simp [Pi.single_apply, h]
  · simp [Pi.single_apply, hk]

omit [Fintype ι] in
lemma matrix_sum_single_diag (k : ι) :
    ∑ a : d k, (Matrix.single a a (1 : K)) = 1 := by
  ext r s
  simp only [Matrix.sum_apply, Matrix.single, Matrix.of_apply, Matrix.one_apply]
  by_cases hrs : r = s
  · subst hrs; simp
  · rw [if_neg hrs]
    exact Finset.sum_eq_zero fun c _ => if_neg fun (h : c = r ∧ c = s) => hrs (h.1 ▸ h.2)

lemma sum_unit_diag : ∑ i, ∑ a : d i, unit i a a = (1 : Blocks K d) := by
  funext k
  simp only [Finset.sum_apply, unit, Pi.one_apply]
  rw [Finset.sum_eq_single k]
  · simp only [Pi.single_eq_same]
    exact matrix_sum_single_diag k
  · intro j _ hj
    exact Finset.sum_eq_zero fun a _ => by simp [Ne.symm hj]
  · simp

omit [Fintype ι] [DecidableEq ι] in
lemma single_mul_eq_sum (k : ι) (x a : d k) (M : Matrix (d k) (d k) K) :
    Matrix.single x a (1 : K) * M = ∑ c, M a c • Matrix.single x c 1 := by
  ext r s
  simp only [Matrix.mul_apply, Matrix.sum_apply, Matrix.smul_apply, Matrix.single,
    Matrix.of_apply, smul_eq_mul]
  by_cases hr : x = r
  · subst hr; simp
  · simp [hr]

omit [Fintype ι] in
lemma unit_mul_blocks (i : ι) (x a : d i) (b : Blocks K d) :
    unit i x a * b = ∑ c, b i a c • unit i x c := by
  rw [unit, ← Pi.single_mul_left, single_mul_eq_sum]
  simp only [unit, ← Pi.single_smul]
  exact map_sum (AddMonoidHom.single (fun i => Matrix (d i) (d i) K) i) _ _

/-! ## The block decomposition of a representation -/

variable {V : Type*} [AddCommGroup V] [Module K V] (o : ∀ i, d i)

/-- The multiplicity space of block `i`: the range of the base idempotent. -/
def mult (φ : Blocks K d →ₐ[K] End K V) (i : ι) : Submodule K V :=
  LinearMap.range (φ (unit i (o i) (o i)))

lemma mem_mult (φ : Blocks K d →ₐ[K] End K V) (i : ι) (a : d i) (v : V) :
    φ (unit i (o i) a) v ∈ mult o φ i :=
  ⟨φ (unit i (o i) a) v, by rw [← Module.End.mul_apply, ← map_mul, unit_mul_same]⟩

lemma idem_mult (φ : Blocks K d →ₐ[K] End K V) (i : ι) (w : mult o φ i) :
    φ (unit i (o i) (o i)) w = w := by
  obtain ⟨y, hy⟩ := w.2
  rw [← hy, ← Module.End.mul_apply, ← map_mul, unit_mul_same]

/-- The recomposition map `w ↦ Σ_{i,a} φ(u i a (o i)) (w i a)`. -/
def recomp (φ : Blocks K d →ₐ[K] End K V) (w : ∀ i, d i → mult o φ i) : V :=
  ∑ i, ∑ a, φ (unit i a (o i)) (w i a)

/-- **The block decomposition** `V ≃ ∏_i (d i → R_i)`. -/
noncomputable def decomp (φ : Blocks K d →ₐ[K] End K V) : V ≃ₗ[K] (∀ i, d i → mult o φ i) where
  toFun v i a := ⟨φ (unit i (o i) a) v, mem_mult o φ i a v⟩
  map_add' v w := by funext i a; exact Subtype.ext (map_add _ _ _)
  map_smul' c v := by funext i a; exact Subtype.ext (map_smul _ _ _)
  invFun := recomp o φ
  left_inv v := by
    simp only [recomp]
    have h : ∀ i (a : d i), φ (unit i a (o i)) (φ (unit i (o i) a) v) = φ (unit i a a) v := by
      intro i a; rw [← Module.End.mul_apply, ← map_mul, unit_mul_same]
    simp only [h]
    have hs : ∑ i, ∑ a : d i, φ (unit i a a) v = φ (∑ i, ∑ a : d i, unit i a a) v := by
      simp only [map_sum, LinearMap.coeFn_sum, Finset.sum_apply]
    rw [hs, sum_unit_diag, map_one, Module.End.one_apply]
  right_inv w := by
    funext i a
    apply Subtype.ext
    simp only [recomp, map_sum]
    rw [Finset.sum_eq_single i]
    · rw [Finset.sum_eq_single a]
      · rw [← Module.End.mul_apply, ← map_mul, unit_mul_same]
        exact idem_mult o φ i (w i a)
      · intro c _ hc
        rw [← Module.End.mul_apply, ← map_mul, unit_mul_of_ne _ _ _ _ _ (Ne.symm hc), map_zero,
          LinearMap.zero_apply]
      · simp
    · intro j _ hj
      refine Finset.sum_eq_zero fun c _ => ?_
      rw [← Module.End.mul_apply, ← map_mul, unit_mul_of_ne_idx (Ne.symm hj), map_zero,
        LinearMap.zero_apply]
    · simp

@[simp] lemma decomp_apply (φ : Blocks K d →ₐ[K] End K V) (v : V) (i : ι) (a : d i) :
    ((decomp o φ v i a : mult o φ i) : V) = φ (unit i (o i) a) v := rfl

/-- **The decomposition intertwines `φ` with the standard action.** -/
lemma decomp_map (φ : Blocks K d →ₐ[K] End K V) (b : Blocks K d) (v : V) (i : ι) (a : d i) :
    decomp o φ (φ b v) i a = ∑ c, b i a c • decomp o φ v i c := by
  apply Subtype.ext
  simp only [decomp_apply, Submodule.coe_sum, Submodule.coe_smul]
  rw [← Module.End.mul_apply, ← map_mul, unit_mul_blocks, map_sum, LinearMap.sum_apply]
  simp only [map_smul, LinearMap.smul_apply]

/-! ## Equal multiplicities give isomorphic representations -/

variable {W : Type*} [AddCommGroup W] [Module K W]

/-- **Two representations of `∏ Matrix` with equal multiplicities are isomorphic.** -/
theorem exists_intertwiner_of_finrank_eq [FiniteDimensional K V] [FiniteDimensional K W]
    (φ : Blocks K d →ₐ[K] End K V) (ψ : Blocks K d →ₐ[K] End K W)
    (h : ∀ i, finrank K (mult o φ i) = finrank K (mult o ψ i)) :
    ∃ T : V ≃ₗ[K] W, ∀ b v, T (φ b v) = ψ b (T v) := by
  let α : ∀ i, mult o φ i ≃ₗ[K] mult o ψ i := fun i => LinearEquiv.ofFinrankEq _ _ (h i)
  let A : (∀ i, d i → mult o φ i) ≃ₗ[K] (∀ i, d i → mult o ψ i) :=
    LinearEquiv.piCongrRight fun i => LinearEquiv.piCongrRight fun _ => α i
  refine ⟨(decomp o φ).trans (A.trans (decomp o ψ).symm), fun b v => ?_⟩
  apply (decomp o ψ).injective
  simp only [LinearEquiv.trans_apply, LinearEquiv.apply_symm_apply]
  funext i a
  rw [decomp_map o ψ b]
  simp only [LinearEquiv.apply_symm_apply]
  show α i (decomp o φ (φ b v) i a) = ∑ c, b i a c • α i (decomp o φ v i c)
  rw [decomp_map o φ b, map_sum]
  simp only [map_smul]

end Blocks

/-! ## The matrix form -/

section MatrixForm

variable {K : Type*} [Field K] {ι : Type*} [Fintype ι] [DecidableEq ι]
  {d : ι → Type*} [∀ i, Fintype (d i)] [∀ i, DecidableEq (d i)] (o : ∀ i, d i)
  {n : Type*} [Fintype n] [DecidableEq n]

lemma mult_toLin_finrank (φ : Blocks K d →ₐ[K] Matrix n n K) (i : ι) :
    finrank K (mult o ((Matrix.toLinAlgEquiv' : Matrix n n K ≃ₐ[K] End K (n → K)).toAlgHom.comp φ)
      i) = (φ (unit i (o i) (o i))).rank := by
  rfl

/-- **Matrix form.** Two algebra maps `∏ Matrix →ₐ Matrix n n K` whose base idempotents have the
same ranks are conjugate by an invertible matrix. -/
theorem exists_conj_of_rank_eq (φ ψ : Blocks K d →ₐ[K] Matrix n n K)
    (h : ∀ i, (φ (unit i (o i) (o i))).rank = (ψ (unit i (o i) (o i))).rank) :
    ∃ U : (Matrix n n K)ˣ, ∀ b, (U : Matrix n n K) * φ b = ψ b * U := by
  set L : Matrix n n K ≃ₐ[K] End K (n → K) := Matrix.toLinAlgEquiv'
  obtain ⟨T, hT⟩ := exists_intertwiner_of_finrank_eq o (L.toAlgHom.comp φ) (L.toAlgHom.comp ψ)
    (fun i => by rw [mult_toLin_finrank, mult_toLin_finrank]; exact h i)
  let U : (Matrix n n K)ˣ :=
    { val := LinearMap.toMatrix' T.toLinearMap
      inv := LinearMap.toMatrix' T.symm.toLinearMap
      val_inv := by
        rw [← LinearMap.toMatrix'_comp]
        simp [LinearMap.toMatrix'_id]
      inv_val := by
        rw [← LinearMap.toMatrix'_comp]
        simp [LinearMap.toMatrix'_id] }
  refine ⟨U, fun b => ?_⟩
  apply Matrix.toLin'.injective
  apply LinearMap.ext
  intro v
  rw [Matrix.toLin'_mul, Matrix.toLin'_mul, LinearMap.comp_apply, LinearMap.comp_apply]
  show Matrix.toLin' (LinearMap.toMatrix' T.toLinearMap) (Matrix.toLin' (φ b) v) =
    Matrix.toLin' (ψ b) (Matrix.toLin' (LinearMap.toMatrix' T.toLinearMap) v)
  rw [Matrix.toLin'_toMatrix']
  exact hT b v

/-- Conjugate representations have equal block ranks. -/
lemma rank_eq_of_conj (φ ψ : Blocks K d →ₐ[K] Matrix n n K) (U : (Matrix n n K)ˣ)
    (hU : ∀ b, (U : Matrix n n K) * φ b = ψ b * U) (i : ι) :
    (φ (unit i (o i) (o i))).rank = (ψ (unit i (o i) (o i))).rank := by
  have hψ : ψ (unit i (o i) (o i)) = (U : Matrix n n K) * φ (unit i (o i) (o i)) *
      ((U⁻¹ : (Matrix n n K)ˣ) : Matrix n n K) := by
    rw [hU, mul_assoc, Units.mul_inv, mul_one]
  rw [hψ, Matrix.rank_mul_eq_left_of_isUnit_det _ _
      ((Matrix.isUnit_iff_isUnit_det _).mp (Units.isUnit _)),
    Matrix.rank_mul_eq_right_of_isUnit_det _ _
      ((Matrix.isUnit_iff_isUnit_det _).mp (Units.isUnit _))]

end MatrixForm

/-! ## Rigidity on a connected parameter set -/

section Rigidity

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
  {d : ι → Type*} [∀ i, Fintype (d i)] [∀ i, DecidableEq (d i)] (o : ∀ i, d i)
  {n : Type*} [Fintype n] [DecidableEq n] {X : Type*} [TopologicalSpace X]

lemma isIdempotentElem_unit (i : ι) : IsIdempotentElem (unit i (o i) (o i) : Blocks ℂ d) :=
  unit_mul_same i (o i) (o i) (o i)

/-- **Rigidity comparison.** Let `x ↦ φ_x, ψ_x : ∏ Matrix →ₐ[ℂ] Matrix n n ℂ` be two families
whose base idempotents `φ_x(u i o o)`, `ψ_x(u i o o)` are continuous on a preconnected set `S`.
If `φ_{x₀}` and `ψ_{x₀}` are conjugate for one `x₀ ∈ S`, then `φ_x` and `ψ_x` are conjugate for
every `x ∈ S`. -/
theorem conj_of_isPreconnected {S : Set X} (hS : IsPreconnected S)
    (φ ψ : X → Blocks ℂ d →ₐ[ℂ] Matrix n n ℂ)
    (hφ : ∀ i, ContinuousOn (fun x => φ x (unit i (o i) (o i))) S)
    (hψ : ∀ i, ContinuousOn (fun x => ψ x (unit i (o i) (o i))) S)
    {x₀ : X} (hx₀ : x₀ ∈ S)
    (h₀ : ∃ U : (Matrix n n ℂ)ˣ, ∀ b, (U : Matrix n n ℂ) * φ x₀ b = ψ x₀ b * U) :
    ∀ x ∈ S, ∃ U : (Matrix n n ℂ)ˣ, ∀ b, (U : Matrix n n ℂ) * φ x b = ψ x b * U := by
  intro x hx
  obtain ⟨U₀, hU₀⟩ := h₀
  refine exists_conj_of_rank_eq o (φ x) (ψ x) fun i => ?_
  have hidφ : ∀ y ∈ S, IsIdempotentElem (φ y (unit i (o i) (o i))) :=
    fun y _ => (isIdempotentElem_unit o i).map (φ y)
  have hidψ : ∀ y ∈ S, IsIdempotentElem (ψ y (unit i (o i) (o i))) :=
    fun y _ => (isIdempotentElem_unit o i).map (ψ y)
  rw [QOU.Mass.IdempotentTraceRigidity.rank_const_of_isPreconnected hS (hφ i) hidφ hx hx₀,
    QOU.Mass.IdempotentTraceRigidity.rank_const_of_isPreconnected hS (hψ i) hidψ hx hx₀]
  exact rank_eq_of_conj o (φ x₀) (ψ x₀) U₀ hU₀ i

end Rigidity

end QOU.Mass.KohnoComparison
