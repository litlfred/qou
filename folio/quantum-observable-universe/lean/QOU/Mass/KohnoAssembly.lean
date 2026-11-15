import QOU.Mass.KohnoComparison
import QOU.Mass.KZHolonomy.Continuity
import QOU.Mass.KZHolonomy.LocalMonodromy
import QOU.Mass.BraidHeckeFactor
import QOU.SchurWeyl.JMProjectorContinuity
import QOU.IwahoriHecke.TensorEmbedding
import QOU.SchurWeyl.JimboActionKernel
import Mathlib.Analysis.Matrix
import Mathlib.Analysis.NormedSpace.Connected
import Mathlib.Topology.Algebra.Module.Cardinality
import Mathlib.LinearAlgebra.Complex.FiniteDimensional

/-!
# Assembly of the Kohno comparison: KZ is conjugate to Jimbo on the real segment

This file assembles the rigidity route of docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md
§5 into one theorem, **with no hypotheses**. Gap 1 of §5.1 (the Hecke quadratic for the KZ
generator) is `QOU.Mass.KZHolonomy.LocalMonodromy.kzBraidRep_sigma_isHeckeQuad`; gaps 2 and 3
(continuity of the Wedderburn matrix units through `q = 1`, and the base point) are
`QOU.SchurWeyl.JMProjectorContinuity`. `kz_conj_jimbo` is first proved conditionally on the
quadratic (`KZQuad`), and `kzQuad_holds` then discharges it.

## Conventions (checked against the source, not assumed)

* The KZ representation is `QOU.Mass.KZHolonomy.kzBraidRep ρ κ c`, built from the transport of
  the KZ form with coupling `κ`; its generator, rescaled by `s = e^{2πiκc}`, satisfies the Hecke
  quadratic with **`q = e^{2πiκ}`** (`KZTwoStrandHecke`). Note `2πiκ`, not `iπκ`: with the
  corpus's normalisation of `kzForm`, the coupling of the real pin `q₀` is
  `κ₀ = ln q₀ / (2πi)`, purely imaginary.
* The Jimbo action is `QOU.SchurWeyl.JimboActionKernel.jimbo q : Hecke ℂ q q⁻¹ m →ₐ Matrix`,
  `σ_j ↦ Ř_{j,j+1}` (`strandBraid q q⁻¹ j`); `Ř` has eigenvalues `q` (symmetric channel) and
  `−q⁻¹` (antisymmetric channel).
* Both are maps out of the **same** algebra `Hecke ℂ q q⁻¹ m` with the same quadratic
  `β² = (q − q⁻¹)β + 1`. The KZ side needs the scalar `s = e^{2πiκc}` per crossing; that is the
  whole normalisation mismatch (it absorbs the choice of the Casimir shift `c`, e.g. the
  `gl₂` vs `sl₂` shift), and it is built into `heckeOfBraidRep`.
* At `κ = 0` the KZ generator is `ρ(s_j)` (`kzBraidRep_zero_σ`) and `s = 1`; at `q = 1` the
  Jimbo generator is the flip of sites `j, j+1` (`rCheck_one`). With `ρ = permRep`, the
  permutation representation of `S_{m+1}` on `V^{⊗(m+1)}`, `V = ℂ²`, the two agree **exactly**
  (`permRep_adjSwap`), with no scalar.

## Results

* `strandBraid_map` — the Jimbo generator commutes with any ring map of coefficients; with
  `laurentT := (T 1, T (-1))` over `LaurentPolynomial`, `strandBraid q q⁻¹ j` is the
  evaluation at `q` of one fixed Laurent-polynomial matrix (`strandBraid_eq_eval`).
* `continuous_strandBraid_exp` — hence continuous in the coupling.
* `permRep`, `permRep_adjSwap` — the base point match.
* `conj_of_isPreconnected_hecke` — the rigidity interface (written by the gap-2/3 prover on
  PR #7738, comment 6130311989 on #7673; committed here).
* `kz_conj_jimbo` — **the assembly.** For every `L ≥ 0`, if the first KZ generator satisfies
  the Hecke quadratic along the segment of couplings `κ(t) = t/(2πi)`, `t ∈ [0, L]`
  (so `q = e^{t}` real in `[1, e^L]`), then for every such `t` the KZ representation through
  `H_{m+1}(q)` is conjugate to the Jimbo representation by an invertible matrix.
* `kz_conj_jimbo_σ` — the same, stated on the braid generators.
* `kzQuad_holds` — the hypothesis holds; `kz_conj_jimbo_hecke`, `kz_conj_jimbo_σ'` are the
  unconditional statements for every `t ≥ 0`, every `m`, every `c`.
* `kz_conj_jimbo_pin` — at a real pin `q₀ ≥ 1`, coupling `κ₀ = ln q₀/(2πi)`
  (`kappa_eq`: `κ(t) = −i t/(2π)`), the rescaled KZ generators are simultaneously conjugate to
  Jimbo's `Ř(q₀)`. `qOf_mem`: along the segment `q` is real in `[1, q₀]`.
* `kz_conj_jimbo_complex`, `kz_conj_jimbo_complex_σ` — every complex `κ` with `q(κ)` not a
  root of unity; the root-of-unity couplings are countable (`countable_rootOfUnity_couplings`),
  so their complement in `ℂ` is path-connected and dense.
* `kz_conj_jimbo_real`, `kz_conj_jimbo_pos` — the same at every real `t`, i.e. every real
  `q₀ > 0` (rigidity run on `[t, 0]` for `t < 0`).

## Scope

* Representation space: `V^{⊗(m+1)}`, `V = ℂ²`, i.e. the KZ system with `ρ = permRep`
  (the `gl₂`-type Casimir `P − c` with an arbitrary scalar shift `c`).
* Couplings: every complex `κ` with `q = e^{2πiκ}` not a root of unity
  (`kz_conj_jimbo_complex`), and also every real `q > 0` including `q = 1`
  (`kz_conj_jimbo_real`, `kz_conj_jimbo_pos`). Roots of unity `q ≠ 1` (`κ ∈ ℚ ∖ {0}`) are
  not covered: there the Hecke algebra is not semisimple and the rank argument does not apply.
* The Jimbo map is `jimboRep`, built here from the universal property; `jimboRep_eq_jimbo`
  identifies it with the corpus's `JimboActionKernel.jimbo`.
* Conjugacy, not an explicit intertwiner: `U` is produced by rank comparison.
-/

namespace QOU.Mass.KohnoAssembly

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open QOU.SchurWeyl QOU.SchurWeyl.JMProjector
open QOU.Mass.KZHolonomy QOU.Mass.BraidHeckeFactor QOU.MathlibExt.Braid
open Complex Set

/-! ## The Jimbo generator as a function of `q` -/

section JimboFamily

variable {R S : Type*} [CommRing R] [CommRing S]

theorem rCheck_map (f : R →+* S) (q qi : R) : (rCheck q qi).map f = rCheck (f q) (f qi) := by
  ext a b
  simp only [Matrix.map_apply, rCheck_apply]
  split_ifs <;> simp

theorem embedPair_map (f : R →+* S) {n : ℕ} (i j : Fin n)
    (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R) :
    (embedPair i j M).map f = embedPair i j (M.map f) := by
  ext a b
  simp only [Matrix.map_apply, embedPair_apply]
  split_ifs <;> simp

/-- **The Jimbo generator commutes with change of coefficients.** -/
theorem strandBraid_map (f : R →+* S) {m : ℕ} (q qi : R) (j : Fin m) :
    (strandBraid q qi j).map f = strandBraid (f q) (f qi) j := by
  simp only [strandBraid, braidAt, embedPair_map, rCheck_map]

/-- **The Jimbo generator is a Laurent-polynomial matrix in `q`.** For every unit `q` of a
commutative ring, `Ř_{j,j+1}(q, q⁻¹)` is the evaluation at `q` of the fixed matrix
`Ř_{j,j+1}(T, T⁻¹)` over `R[T, T⁻¹]`. -/
theorem strandBraid_eq_eval {m : ℕ} (q : Rˣ) (j : Fin m) :
    strandBraid (q : R) (↑q⁻¹ : R) j =
      (strandBraid (LaurentPolynomial.T 1 : LaurentPolynomial R) (LaurentPolynomial.T (-1)) j).map
        (LaurentPolynomial.eval₂ (RingHom.id R) q) := by
  rw [strandBraid_map]
  congr 1
  · simp [LaurentPolynomial.eval₂_T]
  · simp [LaurentPolynomial.eval₂_T]

/-- **The Jimbo generator is continuous in the coupling.** With `q = e^z`, `z ∈ ℂ`
(`z = 2πiκ` in the KZ normalisation), every entry is `0`, `1`, `q` or `q − q⁻¹`. -/
theorem continuous_strandBraid_exp {m : ℕ} (j : Fin m) :
    Continuous (fun z : ℂ => strandBraid (Complex.exp z) (Complex.exp z)⁻¹ j) := by
  refine continuous_matrix fun a b => ?_
  simp only [strandBraid, braidAt, embedPair_apply, rCheck_apply]
  split_ifs
  · exact Complex.continuous_exp
  · exact Complex.continuous_exp.sub (Complex.continuous_exp.inv₀ fun z => Complex.exp_ne_zero z)
  all_goals exact continuous_const

end JimboFamily

/-! ## The permutation representation and the base point -/

section Perm

variable {R : Type*} [CommRing R] {k : ℕ}

/-- The permutation representation of `S_k` on `V^{⊗k}`, `V = R²`, in the coordinate model
`(Fin k → Fin 2) → R`: `permRep σ a b = 1` iff `b = a ∘ σ`. -/
def permRep : Equiv.Perm (Fin k) →* Matrix (Fin k → Fin 2) (Fin k → Fin 2) R where
  toFun σ := Matrix.of fun a b => if b = a ∘ σ then 1 else 0
  map_one' := by
    ext a b
    simp only [Equiv.Perm.coe_one, Function.comp_id, Matrix.of_apply, Matrix.one_apply]
    simp only [eq_comm]
  map_mul' σ τ := by
    ext a b
    simp only [Matrix.of_apply, Matrix.mul_apply, Equiv.Perm.coe_mul, mul_ite, mul_one, mul_zero]
    rw [Finset.sum_eq_single (a ∘ σ)]
    · simp [Function.comp_assoc]
    · intro c _ hc; simp [hc]
    · simp

theorem permRep_apply (σ : Equiv.Perm (Fin k)) (a b : Fin k → Fin 2) :
    (permRep σ : Matrix _ _ R) a b = if b = a ∘ σ then 1 else 0 := rfl

/-- **At `q = 1` the Jimbo generator is the permutation matrix of the adjacent transposition**,
exactly (no scalar). This is the base-point match between KZ at coupling `0`
(`kzBraidRep_zero_σ`) and Jimbo at `q = 1`. -/
theorem permRep_adjSwap {m : ℕ} (j : Fin m) :
    (permRep (adjSwap j) : Matrix _ _ R) = strandBraid (1 : R) 1 j := by
  ext a b
  rw [permRep_apply, strandBraid, braidAt, embedPair_apply, rCheck_one]
  simp only [QOU.IwahoriHecke.RMatrix.flip, Matrix.of_apply, Prod.mk.injEq]
  have hne : (j.castSucc : Fin (m + 1)) ≠ j.succ := by simp [Fin.ext_iff]
  by_cases hb : b = a ∘ adjSwap j
  · subst hb
    simp only [if_true, adjSwap, Function.comp_apply, Equiv.swap_apply_left,
      Equiv.swap_apply_right, and_self]
    rw [if_pos]
    intro k hk1 hk2
    rw [Equiv.swap_apply_of_ne_of_ne hk1 hk2]
  · rw [if_neg hb]
    symm
    rw [ite_eq_right_iff, ite_eq_right_iff]
    intro hagree h
    exfalso
    apply hb
    funext k
    simp only [adjSwap, Function.comp_apply]
    by_cases hk1 : k = j.castSucc
    · subst hk1; rw [Equiv.swap_apply_left]; exact h.2.symm
    · by_cases hk2 : k = j.succ
      · subst hk2; rw [Equiv.swap_apply_right]; exact h.1.symm
      · rw [Equiv.swap_apply_of_ne_of_ne hk1 hk2]; exact (hagree k hk1 hk2).symm

end Perm

/-! ## The Jimbo action on the skein presentation

`QOU.SchurWeyl.JimboActionKernel.jimbo` is the same map routed through the balanced
presentation. The map below is defined directly by the universal property of
`QOU.SchurWeyl.Hecke`; `jimboRep_eq_jimbo` proves the two are equal. -/

section JimboHecke

variable {K : Type*} [Field K]

theorem strandBraid_quad {m : ℕ} {q : K} (hq : q ≠ 0) (j : Fin m) :
    strandBraid q q⁻¹ j * strandBraid q q⁻¹ j =
      (q - q⁻¹) • strandBraid q q⁻¹ j + (q * q⁻¹) • (1 : Matrix (Fin (m + 1) → Fin 2) _ K) := by
  have h := (isHeckeGenerator_braidAt (R := K) q q⁻¹ (i := j.castSucc) (j := j.succ)
    (by simp [Fin.ext_iff]) (mul_inv_cancel₀ hq))
  have h' : strandBraid q q⁻¹ j * strandBraid q q⁻¹ j =
      algebraMap K _ (q - q⁻¹) * strandBraid q q⁻¹ j + 1 := h
  rw [h', mul_inv_cancel₀ hq, one_smul, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]

/-- **The Jimbo action** `H_{m+1}(q) →ₐ M_{2^{m+1}}(K)`, `σ_j ↦ Ř_{j,j+1}`. -/
noncomputable def jimboRep (q : K) (hq : q ≠ 0) (m : ℕ) :
    Hecke K q q⁻¹ m →ₐ[K] Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) K :=
  Hecke.lift K q q⁻¹ m (fun j => strandBraid q q⁻¹ j) (fun j => strandBraid_quad hq j)
    (fun i hi => braidAt_braid (R := K) q q⁻¹ (i := i.castSucc) (j := i.succ)
      (k := (⟨(i : ℕ) + 1, hi⟩ : Fin m).succ)
      (by simp [Fin.ext_iff]) (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff])
      (mul_inv_cancel₀ hq) |>.trans (by
        have e : (⟨(i : ℕ) + 1, hi⟩ : Fin m).castSucc = i.succ := by simp [Fin.ext_iff]
        simp only [strandBraid, e]))
    (fun i j hij => braidAt_commute (R := K) q q⁻¹ (by simp [Fin.ext_iff])
      (by simp [Fin.ext_iff]) (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega)
      (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega))

@[simp] theorem jimboRep_σ (q : K) (hq : q ≠ 0) (m : ℕ) (j : Fin m) :
    jimboRep q hq m (Hecke.σ K q q⁻¹ m j) = strandBraid q q⁻¹ j :=
  Hecke.lift_σ _ _ _ _ _ _ _ _ j

/-- **`jimboRep` is the corpus's Jimbo action** `JimboActionKernel.jimbo` (`heckeActionN` read
through the balanced-presentation bridge): both send `σ_j` to `Ř_{j,j+1}`. -/
theorem jimboRep_eq_jimbo (q : K) (hq : q ≠ 0) (m : ℕ) :
    jimboRep q hq m = QOU.SchurWeyl.JimboActionKernel.jimbo q hq m :=
  Hecke.hom_ext _ _ _ _ fun j => by
    rw [jimboRep_σ, QOU.SchurWeyl.JimboActionKernel.jimbo_σ]

end JimboHecke

/-! ## The rigidity interface

Written by the gap-2/3 prover (PR #7738; posted as comment 6130311989 on PR #7673) and committed
here. Two families of Hecke representations over a preconnected parameter set, with continuous
generator matrices, conjugate on generators at one base point (which may be `q = 1`), are
conjugate at every generic parameter. -/

section Interface

open QOU.Mathlib (StandardYoungTableau)
open Hecke

variable {X : Type*} [TopologicalSpace X] {S : Set X} {q : X → ℂ} {n : ℕ}
  {m : Type*} [Fintype m] [DecidableEq m]

lemma rank_eq_of_intertwine {A B : Matrix m m ℂ} (U : (Matrix m m ℂ)ˣ)
    (h : (U : Matrix m m ℂ) * A = B * U) : A.rank = B.rank := by
  have hdet : IsUnit (U : Matrix m m ℂ).det := (Matrix.isUnit_iff_isUnit_det _).mp U.isUnit
  rw [← Matrix.rank_mul_eq_right_of_isUnit_det (U : Matrix m m ℂ) A hdet, h,
    Matrix.rank_mul_eq_left_of_isUnit_det (U : Matrix m m ℂ) B hdet]

theorem conj_of_isPreconnected_hecke (hS : IsPreconnected S)
    (hq : ContinuousOn q S) (hq0 : ∀ x ∈ S, q x ≠ 0)
    (hsep : ∀ x ∈ S, Set.InjOn (qInt2 (q x)) {d | d ∈ contentRange n})
    (hdense : S ⊆ closure (S ∩ {x | GenericParameter.NotRootOfUnity (q x)}))
    (ρ ρ' : ∀ x : X, Hecke ℂ (q x) (q x)⁻¹ n →ₐ[ℂ] Matrix m m ℂ)
    (hρ : ∀ i, ContinuousOn (fun x => ρ x (σ ℂ (q x) (q x)⁻¹ n i)) S)
    (hρ' : ∀ i, ContinuousOn (fun x => ρ' x (σ ℂ (q x) (q x)⁻¹ n i)) S)
    (o : ∀ lam : Nat.Partition (n + 1), StandardYoungTableau (QOU.Mathlib.partitionShape lam))
    {x₀ : X} (hx₀ : x₀ ∈ S) (U₀ : (Matrix m m ℂ)ˣ)
    (hU₀ : ∀ i, (U₀ : Matrix m m ℂ) * ρ x₀ (σ ℂ (q x₀) (q x₀)⁻¹ n i)
      = ρ' x₀ (σ ℂ (q x₀) (q x₀)⁻¹ n i) * U₀)
    {x : X} (hx : x ∈ S) (hgen : GenericParameter.NotRootOfUnity (q x)) :
    ∃ U : (Matrix m m ℂ)ˣ, ∀ h, (U : Matrix m m ℂ) * ρ x h = ρ' x h * U := by
  set W := heckeWedderburn (q x) (hq0 x hx) hgen n
  have hrank : ∀ lam, ((ρ x).comp W.symm.toAlgHom
      (KohnoComparison.unit lam (o lam) (o lam))).rank
      = ((ρ' x).comp W.symm.toAlgHom (KohnoComparison.unit lam (o lam) (o lam))).rank := by
    intro lam
    show (ρ x (W.symm (Pi.single lam (Matrix.single (o lam) (o lam) 1)))).rank
      = (ρ' x (W.symm (Pi.single lam (Matrix.single (o lam) (o lam) 1)))).rank
    rw [projFamily_eq_wedderburn ρ (o lam) x (hq0 x hx) hgen,
      projFamily_eq_wedderburn ρ' (o lam) x (hq0 x hx) hgen,
      IdempotentTraceRigidity.rank_const_of_isPreconnected hS
        (continuousOn_projFamily ρ hq hq0 hsep hρ (o lam))
        (isIdempotentElem_projFamily ρ hq hq0 hsep hρ hdense (o lam)) hx hx₀,
      IdempotentTraceRigidity.rank_const_of_isPreconnected hS
        (continuousOn_projFamily ρ' hq hq0 hsep hρ' (o lam))
        (isIdempotentElem_projFamily ρ' hq hq0 hsep hρ' hdense (o lam)) hx hx₀]
    exact rank_eq_of_intertwine U₀ (projFamily_conj ρ U₀ hU₀ (o lam))
  obtain ⟨U, hU⟩ := KohnoComparison.exists_conj_of_rank_eq o ((ρ x).comp W.symm.toAlgHom)
    ((ρ' x).comp W.symm.toAlgHom) hrank
  refine ⟨U, fun h => ?_⟩
  have := hU (W h)
  simpa using this

end Interface

/-! ## The assembly on the real segment

Couplings `κ(t) = t / (2πi)`, `t ∈ [0, L]`, so `2πiκ = t` and `q = e^{t}` is real in `[1, e^L]`.
The framework's real pin `q₀` corresponds to `L = ln q₀`. -/

section Assembly

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

/-- The KZ coupling along the segment: `κ(t) = t / (2πi)`, purely imaginary. -/
noncomputable def kappa (t : ℝ) : ℂ := (t : ℂ) / (2 * (Real.pi * I))

theorem two_kappa (t : ℝ) : 2 * kappa t * (Real.pi * I) = t := by
  have hπ : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  unfold kappa
  field_simp

theorem kappa_zero : kappa 0 = 0 := by simp [kappa]

theorem continuous_kappa : Continuous kappa :=
  Complex.continuous_ofReal.div_const _

/-- The Hecke parameter of the KZ representation at `κ(t)`: `q = e^{2πiκ(t)}`. -/
noncomputable def qOf (t : ℝ) : ℂ := Complex.exp (2 * kappa t * (Real.pi * I))

/-- **Along the segment the Hecke parameter is the positive real `e^t`.** -/
theorem qOf_eq (t : ℝ) : qOf t = (Real.exp t : ℂ) := by
  rw [qOf, two_kappa, Complex.ofReal_exp]

theorem qOf_ne_zero (t : ℝ) : qOf t ≠ 0 := Complex.exp_ne_zero _

theorem qOf_zero : qOf 0 = 1 := by rw [qOf_eq, Real.exp_zero, Complex.ofReal_one]

theorem qOf_ne_one {t : ℝ} (ht : t ≠ 0) : qOf t ≠ 1 := by
  rw [qOf_eq]
  intro h
  have h' : Real.exp t = 1 := by exact_mod_cast h
  exact ht (Real.exp_eq_one_iff t |>.mp h')

theorem continuous_qOf : Continuous qOf :=
  Complex.continuous_exp.comp ((continuous_const.mul continuous_kappa).mul continuous_const)

variable {m : ℕ}

/-- The scalar `s = e^{2πiκc}` by which each KZ crossing is rescaled. -/
noncomputable def kzScale (c : ℂ) (t : ℝ) : ℂ := Complex.exp (2 * kappa t * (Real.pi * I) * c)

/-- **Hypothesis H1 (gap 1).** At coupling `κ(t)`, the first KZ generator on `m + 1` strands
(with `ρ = permRep`, i.e. on `V^{⊗(m+1)}`, `V = ℂ²`), rescaled by `e^{2πiκc}`, satisfies the
Hecke quadratic with `q = e^{2πiκ}`. Proved for `m = 1` (`kzTwoStrand_isHeckeQuad`); open for
`m ≥ 2`. This is exactly the shape of `KZTwoStrandHecke.kzTwoStrand_isHeckeQuad`. -/
def KZQuad (m : ℕ) (c : ℂ) (t : ℝ) : Prop :=
  ∀ hm : 0 < m, IsHeckeQuad (kzScale c t) (qOf t) (qOf t)⁻¹
    ((kzBraidRep (permRep (R := ℂ) (k := m + 1)) (kappa t) c (σ ⟨0, hm⟩) :
      (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
      Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)

/-- The KZ representation through `H_{m+1}(q)` along the segment (`σ_j ↦ e^{2πiκc} θ_κ(σ_j)`);
off the segment it is set to the Jimbo map, which plays no role. -/
noncomputable def kzHecke (c : ℂ) {L : ℝ} (H1 : ∀ t ∈ Icc (0 : ℝ) L, KZQuad m c t) (t : ℝ) :
    Hecke ℂ (qOf t) (qOf t)⁻¹ m →ₐ[ℂ] Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ :=
  if h : t ∈ Icc (0 : ℝ) L then
    heckeOfBraidRepOfZero (s := kzScale c t) (kzBraidRep permRep (kappa t) c) (H1 t h)
  else jimboRep (qOf t) (qOf_ne_zero t) m

theorem kzHecke_σ (c : ℂ) {L : ℝ} (H1 : ∀ t ∈ Icc (0 : ℝ) L, KZQuad m c t) {t : ℝ}
    (ht : t ∈ Icc (0 : ℝ) L) (j : Fin m) :
    kzHecke c H1 t (Hecke.σ ℂ (qOf t) (qOf t)⁻¹ m j) =
      kzScale c t • ((kzBraidRep permRep (kappa t) c (σ j) :
        (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) := by
  simp only [kzHecke, dif_pos ht, heckeOfBraidRepOfZero, heckeOfBraidRep_σ]

theorem continuousOn_kzHecke_σ (c : ℂ) {L : ℝ} (H1 : ∀ t ∈ Icc (0 : ℝ) L, KZQuad m c t)
    (j : Fin m) :
    ContinuousOn (fun t => kzHecke c H1 t (Hecke.σ ℂ (qOf t) (qOf t)⁻¹ m j)) (Icc 0 L) := by
  have hc : Continuous (fun t : ℝ => kzScale c t • ((kzBraidRep permRep (kappa t) c (σ j) :
      (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) := by
    have hk := (continuous_kzBraidRep_σ
      (A := Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)
      (permRep (R := ℂ) (k := m + 1)) c j).comp continuous_kappa
    refine Continuous.smul ?_ hk
    exact Complex.continuous_exp.comp
      (((continuous_const.mul continuous_kappa).mul continuous_const).mul continuous_const)
  exact hc.continuousOn.congr fun t ht => kzHecke_σ c H1 ht j

theorem continuous_jimboRep_σ (j : Fin m) :
    Continuous (fun t => jimboRep (qOf t) (qOf_ne_zero t) m (Hecke.σ ℂ (qOf t) (qOf t)⁻¹ m j)) := by
  simp only [jimboRep_σ, qOf]
  exact (continuous_strandBraid_exp j).comp
    ((continuous_const.mul continuous_kappa).mul continuous_const)

/-- **The base point.** At `t = 0` (coupling `0`, `q = 1`) the KZ and Jimbo maps agree on the
generators: both send `σ_j` to the permutation matrix of `(j, j+1)`. -/
theorem kzHecke_zero_σ (c : ℂ) {L : ℝ} (hL : 0 ≤ L) (H1 : ∀ t ∈ Icc (0 : ℝ) L, KZQuad m c t)
    (j : Fin m) :
    kzHecke c H1 0 (Hecke.σ ℂ (qOf 0) (qOf 0)⁻¹ m j) =
      jimboRep (qOf 0) (qOf_ne_zero 0) m (Hecke.σ ℂ (qOf 0) (qOf 0)⁻¹ m j) := by
  rw [kzHecke_σ c H1 ⟨le_rfl, hL⟩, jimboRep_σ]
  have hs : kzScale c 0 = 1 := by simp [kzScale, kappa_zero]
  rw [hs, one_smul, kappa_zero, kzBraidRep_zero_σ, permRep_adjSwap, qOf_zero, inv_one]

/-- **The assembled Kohno comparison on the real segment.** Fix `c ∈ ℂ` and `L ≥ 0`. Assume
only **H1**: along the couplings `κ(t) = t/(2πi)`, `t ∈ [0, L]`, the first KZ generator
satisfies the Hecke quadratic with `q = e^{t}` (gap 1). Then at every `t ∈ [0, L]` the KZ
representation of `H_{m+1}(e^t)` on `V^{⊗(m+1)}` is conjugate to the Jimbo representation by
an invertible matrix.

The Wedderburn continuity and the base point at `q = 1` (gaps 2 and 3) are not hypotheses:
they are discharged by `JMProjectorContinuity` and `permRep_adjSwap`. -/
theorem kz_conj_jimbo (c : ℂ) {L : ℝ} (H1 : ∀ t ∈ Icc (0 : ℝ) L, KZQuad m c t)
    {t : ℝ} (ht : t ∈ Icc (0 : ℝ) L) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ h,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) * kzHecke c H1 t h = jimboRep (qOf t) (qOf_ne_zero t) m h * U := by
  have hL : 0 ≤ L := ht.1.trans ht.2
  rcases eq_or_lt_of_le ht.1 with h0 | hpos
  · -- base point: the two maps are equal
    subst h0
    have he : kzHecke c H1 0 = jimboRep (qOf 0) (qOf_ne_zero 0) m :=
      Hecke.hom_ext _ _ _ _ (kzHecke_zero_σ c hL H1)
    exact ⟨1, fun h => by rw [he]; simp⟩
  have hLpos : 0 < L := hpos.trans_le ht.2
  have hposq : ∀ x ∈ Icc (0 : ℝ) L, ∃ s : ℝ, 0 < s ∧ qOf x = s :=
    fun x _ => ⟨Real.exp x, Real.exp_pos x, qOf_eq x⟩
  have hdense : Icc (0 : ℝ) L ⊆
      closure (Icc (0 : ℝ) L ∩ {x | GenericParameter.NotRootOfUnity (qOf x)}) := by
    have h1 : Ioc (0 : ℝ) L ⊆ Icc (0 : ℝ) L ∩ {x | GenericParameter.NotRootOfUnity (qOf x)} := by
      intro x hx
      exact (generic_of_pos (S := Icc (0 : ℝ) L) hposq
        ⟨Ioc_subset_Icc_self hx, qOf_ne_one (ne_of_gt hx.1)⟩)
    calc Icc (0 : ℝ) L = closure (Ioc 0 L) := (closure_Ioc hLpos.ne).symm
      _ ⊆ _ := closure_mono h1
  have hgen : GenericParameter.NotRootOfUnity (qOf t) := by
    have := generic_of_pos (S := Icc (0 : ℝ) L) hposq ⟨ht, qOf_ne_one (ne_of_gt hpos)⟩
    exact this.2
  exact conj_of_isPreconnected_hecke (n := m) isPreconnected_Icc continuous_qOf.continuousOn
    (fun x _ => qOf_ne_zero x) (sep_of_pos hposq) hdense
    (kzHecke c H1) (fun x => jimboRep (qOf x) (qOf_ne_zero x) m)
    (continuousOn_kzHecke_σ c H1) (fun j => (continuous_jimboRep_σ j).continuousOn)
    (fun _ => Classical.arbitrary _) (x₀ := 0) ⟨le_rfl, hL⟩ 1
    (fun j => by rw [kzHecke_zero_σ c hL H1]; simp) ht hgen

/-- **Generator form.** Under H1, at every `t ∈ [0, L]` there is one invertible `U` with
`U · (e^{2πiκc} θ_κ(σ_j)) · U⁻¹ = Ř_{j,j+1}(q)` for every generator, `κ = t/(2πi)`, `q = e^t`. -/
theorem kz_conj_jimbo_σ (c : ℂ) {L : ℝ} (H1 : ∀ t ∈ Icc (0 : ℝ) L, KZQuad m c t)
    {t : ℝ} (ht : t ∈ Icc (0 : ℝ) L) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ j : Fin m,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) * (kzScale c t • ((kzBraidRep permRep (kappa t) c (σ j) :
        (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) =
        strandBraid (qOf t) (qOf t)⁻¹ j * U := by
  obtain ⟨U, hU⟩ := kz_conj_jimbo c H1 ht
  refine ⟨U, fun j => ?_⟩
  have := hU (Hecke.σ ℂ (qOf t) (qOf t)⁻¹ m j)
  rwa [kzHecke_σ c H1 ht, jimboRep_σ] at this

/-! ## Discharging H1: gap 1 is closed

`QOU.Mass.KZHolonomy.kzBraidRep_sigma_isHeckeQuad` (local monodromy, `LocalMonodromy.lean`)
proves the Hecke quadratic for every generator, every `ρ`, every `κ, c`, on `≥ 2` strands. -/

/-- **H1 holds unconditionally.** -/
theorem kzQuad_holds (m : ℕ) (c : ℂ) (t : ℝ) : KZQuad m c t := by
  intro hm
  cases m with
  | zero => exact absurd hm (lt_irrefl 0)
  | succ k =>
      exact LocalMonodromy.kzBraidRep_sigma_isHeckeQuad (permRep (R := ℂ) (k := k + 2)) (kappa t) c 0

/-- The KZ representation through `H_{m+1}(q)`, `q = e^{2πiκ(t)}`, for every `t`:
`σ_j ↦ e^{2πiκc} θ_κ(σ_j)`. -/
noncomputable def kzHeckeRep (m : ℕ) (c : ℂ) (t : ℝ) :
    Hecke ℂ (qOf t) (qOf t)⁻¹ m →ₐ[ℂ] Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ :=
  heckeOfBraidRepOfZero (s := kzScale c t) (kzBraidRep permRep (kappa t) c) (kzQuad_holds m c t)

theorem kzHeckeRep_σ (c : ℂ) (t : ℝ) (j : Fin m) :
    kzHeckeRep m c t (Hecke.σ ℂ (qOf t) (qOf t)⁻¹ m j) =
      kzScale c t • ((kzBraidRep permRep (kappa t) c (σ j) :
        (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) := by
  simp only [kzHeckeRep, heckeOfBraidRepOfZero, heckeOfBraidRep_σ]

/-- **Kohno comparison, unconditional, for all real couplings `κ = t/(2πi)`, `t ≥ 0`.**
For every number of strands `m + 1`, every Casimir shift `c ∈ ℂ` and every `t ≥ 0`, the KZ
representation of `H_{m+1}(q)`, `q = e^t`, on `V^{⊗(m+1)}`, `V = ℂ²`, is conjugate to the Jimbo
representation by an invertible matrix. -/
theorem kz_conj_jimbo_hecke (c : ℂ) {t : ℝ} (ht : 0 ≤ t) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ h,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) * kzHeckeRep m c t h =
        jimboRep (qOf t) (qOf_ne_zero t) m h * U := by
  have H1 : ∀ s ∈ Icc (0 : ℝ) t, KZQuad m c s := fun s _ => kzQuad_holds m c s
  have hmem : t ∈ Icc (0 : ℝ) t := ⟨ht, le_rfl⟩
  have he : kzHecke c H1 t = kzHeckeRep m c t :=
    Hecke.hom_ext _ _ _ _ fun j => by rw [kzHecke_σ c H1 hmem, kzHeckeRep_σ]
  obtain ⟨U, hU⟩ := kz_conj_jimbo c H1 hmem
  exact ⟨U, fun h => by rw [← he]; exact hU h⟩

/-- **Generator form, unconditional.** For every `t ≥ 0` one invertible `U` conjugates every
rescaled KZ generator to the Jimbo `Ř`-matrix: `U (e^{2πiκc} θ_κ(σ_j)) = Ř_{j,j+1}(q) U`. -/
theorem kz_conj_jimbo_σ' (c : ℂ) {t : ℝ} (ht : 0 ≤ t) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ j : Fin m,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) *
        (kzScale c t • ((kzBraidRep permRep (kappa t) c (σ j) :
          (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
          Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) =
        strandBraid (qOf t) (qOf t)⁻¹ j * U :=
  kz_conj_jimbo_σ c (fun s _ => kzQuad_holds m c s) ⟨ht, le_rfl⟩

/-! ## Specialisation to a real pin `q₀ ≥ 1`

No numerical value of `q₀` is used: `q₀` is any real `≥ 1`. The coupling is
`κ₀ = ln q₀ / (2πi) = −i ln q₀ / (2π)`, purely imaginary, and along `κ(t)`, `t ∈ [0, ln q₀]`,
the Hecke parameter `q = e^t` runs through the real interval `[1, q₀]`. -/

theorem kappa_eq (t : ℝ) : kappa t = -((t / (2 * Real.pi) : ℝ) : ℂ) * I := by
  have hπ : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  unfold kappa
  push_cast
  field_simp
  rw [Complex.I_sq]
  ring

/-- The couplings form a preconnected set (the image of `[0, L]`). -/
theorem isPreconnected_kappa_image (L : ℝ) : IsPreconnected (kappa '' Icc 0 L) :=
  isPreconnected_Icc.image _ continuous_kappa.continuousOn

/-- Along the segment, `q` is real and lies in `[1, e^L]`. -/
theorem qOf_mem (L : ℝ) {t : ℝ} (ht : t ∈ Icc (0 : ℝ) L) :
    ∃ r : ℝ, qOf t = r ∧ 1 ≤ r ∧ r ≤ Real.exp L :=
  ⟨Real.exp t, qOf_eq t, Real.one_le_exp ht.1, Real.exp_le_exp.mpr ht.2⟩

theorem qOf_log {q₀ : ℝ} (hq₀ : 0 < q₀) : qOf (Real.log q₀) = q₀ := by
  rw [qOf_eq, Real.exp_log hq₀]

/-- **The Kohno comparison at a real pin `q₀ ≥ 1`.** At the coupling `κ₀ = ln q₀/(2πi)` the
rescaled KZ generators on `V^{⊗(m+1)}` are simultaneously conjugate to Jimbo's `Ř(q₀)`. -/
theorem kz_conj_jimbo_pin (c : ℂ) {q₀ : ℝ} (hq₀ : 1 ≤ q₀) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ j : Fin m,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) *
        (kzScale c (Real.log q₀) • ((kzBraidRep permRep (kappa (Real.log q₀)) c (σ j) :
          (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
          Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) =
        strandBraid (q₀ : ℂ) (q₀ : ℂ)⁻¹ j * U := by
  obtain ⟨U, hU⟩ := kz_conj_jimbo_σ' (m := m) c (Real.log_nonneg hq₀)
  refine ⟨U, fun j => ?_⟩
  rw [hU j, qOf_log (lt_of_lt_of_le one_pos hq₀)]

/-! ## Every real `q > 0`: the full real line of couplings

The argument above works on any closed interval containing the base point `t = 0`. Below it is
run on `[0, t]` for `t > 0` and on `[t, 0]` for `t < 0`, with the unconditional family
`kzHeckeRep`, so the comparison holds at every `q = e^t > 0`. -/

theorem continuous_kzHeckeRep_σ (c : ℂ) (j : Fin m) :
    Continuous (fun t => kzHeckeRep m c t (Hecke.σ ℂ (qOf t) (qOf t)⁻¹ m j)) := by
  have hk := (continuous_kzBraidRep_σ
    (A := Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)
    (permRep (R := ℂ) (k := m + 1)) c j).comp continuous_kappa
  have hc : Continuous (fun t : ℝ => kzScale c t • ((kzBraidRep permRep (kappa t) c (σ j) :
      (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) := by
    refine Continuous.smul ?_ hk
    exact Complex.continuous_exp.comp
      (((continuous_const.mul continuous_kappa).mul continuous_const).mul continuous_const)
  simpa only [kzHeckeRep_σ] using hc

theorem kzHeckeRep_zero_σ (c : ℂ) (j : Fin m) :
    kzHeckeRep m c 0 (Hecke.σ ℂ (qOf 0) (qOf 0)⁻¹ m j) =
      jimboRep (qOf 0) (qOf_ne_zero 0) m (Hecke.σ ℂ (qOf 0) (qOf 0)⁻¹ m j) := by
  rw [kzHeckeRep_σ, jimboRep_σ]
  have hs : kzScale c 0 = 1 := by simp [kzScale, kappa_zero]
  rw [hs, one_smul, kappa_zero, kzBraidRep_zero_σ, permRep_adjSwap, qOf_zero, inv_one]

/-- Rigidity on a closed interval `S` through the base point `0`, given that the points with
`t ≠ 0` are dense in `S`. -/
theorem kzHeckeRep_conj_of_interval (c : ℂ) {S : Set ℝ} (hS : IsPreconnected S) (h0 : (0 : ℝ) ∈ S)
    (hdense0 : S ⊆ closure (S ∩ {x | x ≠ 0})) {t : ℝ} (ht : t ∈ S) (ht0 : t ≠ 0) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ h,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) * kzHeckeRep m c t h =
        jimboRep (qOf t) (qOf_ne_zero t) m h * U := by
  have hposq : ∀ x ∈ S, ∃ s : ℝ, 0 < s ∧ qOf x = s :=
    fun x _ => ⟨Real.exp x, Real.exp_pos x, qOf_eq x⟩
  have hdense : S ⊆ closure (S ∩ {x | GenericParameter.NotRootOfUnity (qOf x)}) := by
    refine hdense0.trans (closure_mono fun x hx => ?_)
    exact generic_of_pos (S := S) hposq ⟨hx.1, qOf_ne_one hx.2⟩
  have hgen : GenericParameter.NotRootOfUnity (qOf t) :=
    (generic_of_pos (S := S) hposq ⟨ht, qOf_ne_one ht0⟩).2
  exact conj_of_isPreconnected_hecke (n := m) hS continuous_qOf.continuousOn
    (fun x _ => qOf_ne_zero x) (sep_of_pos hposq) hdense
    (kzHeckeRep m c) (fun x => jimboRep (qOf x) (qOf_ne_zero x) m)
    (fun j => (continuous_kzHeckeRep_σ c j).continuousOn)
    (fun j => (continuous_jimboRep_σ j).continuousOn)
    (fun _ => Classical.arbitrary _) (x₀ := 0) h0 1
    (fun j => by rw [kzHeckeRep_zero_σ c j]; simp) ht hgen

/-- **Kohno comparison at every real coupling `κ = t/(2πi)`, `t ∈ ℝ`** (every real `q = e^t > 0`):
the KZ representation of `H_{m+1}(q)` on `V^{⊗(m+1)}` is conjugate to Jimbo's. -/
theorem kz_conj_jimbo_real (c : ℂ) (t : ℝ) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ h,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) * kzHeckeRep m c t h =
        jimboRep (qOf t) (qOf_ne_zero t) m h * U := by
  rcases lt_trichotomy t 0 with hneg | h0 | hpos
  · refine kzHeckeRep_conj_of_interval (S := Icc t 0) c isPreconnected_Icc ⟨hneg.le, le_rfl⟩ ?_
      ⟨le_rfl, hneg.le⟩ hneg.ne
    calc Icc t 0 = closure (Ico t 0) := (closure_Ico hneg.ne).symm
      _ ⊆ _ := closure_mono fun x (hx : x ∈ Ico t 0) =>
        (⟨Ico_subset_Icc_self hx, hx.2.ne⟩ : x ∈ Icc t 0 ∩ {x | x ≠ 0})
  · subst h0
    have he : kzHeckeRep m c 0 = jimboRep (qOf 0) (qOf_ne_zero 0) m :=
      Hecke.hom_ext _ _ _ _ (kzHeckeRep_zero_σ c)
    exact ⟨1, fun h => by rw [he]; simp⟩
  · refine kzHeckeRep_conj_of_interval (S := Icc 0 t) c isPreconnected_Icc ⟨le_rfl, hpos.le⟩ ?_
      ⟨hpos.le, le_rfl⟩ hpos.ne'
    calc Icc 0 t = closure (Ioc 0 t) := (closure_Ioc hpos.ne).symm
      _ ⊆ _ := closure_mono fun x (hx : x ∈ Ioc 0 t) =>
        (⟨Ioc_subset_Icc_self hx, hx.1.ne'⟩ : x ∈ Icc 0 t ∩ {x | x ≠ 0})

/-- **The Kohno comparison at every real `q₀ > 0`.** At the coupling `κ₀ = ln q₀/(2πi)` the
rescaled KZ generators on `V^{⊗(m+1)}` are simultaneously conjugate to Jimbo's `Ř(q₀)`. -/
theorem kz_conj_jimbo_pos (c : ℂ) (q₀ : ℝ) (hq₀ : 0 < q₀) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ j : Fin m,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) *
        (kzScale c (Real.log q₀) • ((kzBraidRep permRep (kappa (Real.log q₀)) c (σ j) :
          (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
          Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) =
        strandBraid (q₀ : ℂ) (q₀ : ℂ)⁻¹ j * U := by
  obtain ⟨U, hU⟩ := kz_conj_jimbo_real (m := m) c (Real.log q₀)
  refine ⟨U, fun j => ?_⟩
  have := hU (Hecke.σ ℂ (qOf (Real.log q₀)) (qOf (Real.log q₀))⁻¹ m j)
  rw [kzHeckeRep_σ, jimboRep_σ, qOf_log hq₀] at this
  exact this

/-! ## Complex couplings: every `κ` with `q = e^{2πiκ}` not a root of unity

Parameter space: the whole `κ`-plane. The set `G` of couplings with `q(κ)` a root of unity is
countable (`κ ∈ ℚ`), so its complement is path-connected (`ℂ` has real rank `2`) and dense.
The rigidity set is `S = {κ | the q²-integers [d]_{q²}, |d| ≤ m, are distinct}`; it contains
`ℂ ∖ G` (`qInt2_injective`) and the base point `κ = 0` (`q = 1`, `qInt2_one_injective`), and it
lies in the closure of `ℂ ∖ G`, hence is preconnected. -/

/-- The Hecke parameter as a function of a complex coupling: `q(κ) = e^{2πiκ}`. -/
noncomputable def qC (κ : ℂ) : ℂ := Complex.exp (2 * κ * (Real.pi * I))

theorem qC_ne_zero (κ : ℂ) : qC κ ≠ 0 := Complex.exp_ne_zero _

theorem qC_zero : qC 0 = 1 := by simp [qC]

theorem continuous_qC : Continuous qC :=
  Complex.continuous_exp.comp ((continuous_const.mul continuous_id).mul continuous_const)

/-- **The root-of-unity couplings are countable**: `q(κ)^k = 1` with `k > 0` forces `κ ∈ ℚ`. -/
theorem countable_rootOfUnity_couplings :
    {κ : ℂ | ¬ GenericParameter.NotRootOfUnity (qC κ)}.Countable := by
  refine (Set.countable_range (fun p : ℤ × ℕ => (p.1 : ℂ) / (p.2 : ℂ))).mono ?_
  intro κ hκ
  simp only [GenericParameter.NotRootOfUnity, Set.mem_setOf_eq, not_forall, not_not] at hκ
  obtain ⟨k, hk, hpow⟩ := hκ
  rw [qC, ← Complex.exp_nat_mul, Complex.exp_eq_one_iff] at hpow
  obtain ⟨n, hn⟩ := hpow
  refine ⟨(n, k), ?_⟩
  have hπ : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
  have hk' : (k : ℂ) ≠ 0 := by exact_mod_cast hk.ne'
  show (n : ℂ) / (k : ℂ) = κ
  rw [div_eq_iff hk']
  have h2 : (2 * (Real.pi : ℂ) * I) ≠ 0 := by simp [hπ, Complex.I_ne_zero]
  apply mul_right_cancel₀ h2
  linear_combination -hn

theorem kzQuadC (m : ℕ) (c κ : ℂ) :
    ∀ hm : 0 < m, IsHeckeQuad (Complex.exp (2 * κ * (Real.pi * I) * c)) (qC κ) (qC κ)⁻¹
      ((kzBraidRep (permRep (R := ℂ) (k := m + 1)) κ c (σ ⟨0, hm⟩) :
        (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) := by
  intro hm
  cases m with
  | zero => exact absurd hm (lt_irrefl 0)
  | succ k => exact LocalMonodromy.kzBraidRep_sigma_isHeckeQuad (permRep (R := ℂ) (k := k + 2)) κ c 0

/-- The KZ representation of `H_{m+1}(q(κ))` at a complex coupling `κ`. -/
noncomputable def kzHeckeC (m : ℕ) (c κ : ℂ) :
    Hecke ℂ (qC κ) (qC κ)⁻¹ m →ₐ[ℂ] Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ :=
  heckeOfBraidRepOfZero (s := Complex.exp (2 * κ * (Real.pi * I) * c))
    (kzBraidRep permRep κ c) (kzQuadC m c κ)

theorem kzHeckeC_σ (c κ : ℂ) (j : Fin m) :
    kzHeckeC m c κ (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j) =
      Complex.exp (2 * κ * (Real.pi * I) * c) • ((kzBraidRep permRep κ c (σ j) :
        (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) := by
  simp only [kzHeckeC, heckeOfBraidRepOfZero, heckeOfBraidRep_σ]

theorem continuous_kzHeckeC_σ (c : ℂ) (j : Fin m) :
    Continuous (fun κ => kzHeckeC m c κ (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j)) := by
  have hk := continuous_kzBraidRep_σ
    (A := Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)
    (permRep (R := ℂ) (k := m + 1)) c j
  have hc : Continuous (fun κ : ℂ => Complex.exp (2 * κ * (Real.pi * I) * c) •
      ((kzBraidRep permRep κ c (σ j) :
      (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
        Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) := by
    refine Continuous.smul ?_ hk
    exact Complex.continuous_exp.comp
      (((continuous_const.mul continuous_id).mul continuous_const).mul continuous_const)
  simpa only [kzHeckeC_σ] using hc

theorem continuous_jimboRepC_σ (j : Fin m) :
    Continuous (fun κ => jimboRep (qC κ) (qC_ne_zero κ) m (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j)) := by
  simp only [jimboRep_σ, qC]
  exact (continuous_strandBraid_exp j).comp
    ((continuous_const.mul continuous_id).mul continuous_const)

theorem kzHeckeC_zero_σ (c : ℂ) (j : Fin m) :
    kzHeckeC m c 0 (Hecke.σ ℂ (qC 0) (qC 0)⁻¹ m j) =
      jimboRep (qC 0) (qC_ne_zero 0) m (Hecke.σ ℂ (qC 0) (qC 0)⁻¹ m j) := by
  rw [kzHeckeC_σ, jimboRep_σ]
  have hs : Complex.exp (2 * (0 : ℂ) * (Real.pi * I) * c) = 1 := by simp
  rw [hs, one_smul, kzBraidRep_zero_σ, permRep_adjSwap, qC_zero, inv_one]

/-- **The Kohno comparison at every complex coupling `κ` with `q = e^{2πiκ}` not a root of
unity.** The KZ representation of `H_{m+1}(q)` on `V^{⊗(m+1)}`, `V = ℂ²`, rescaled by
`e^{2πiκc}` per crossing, is conjugate to Jimbo's by an invertible matrix. No separation
hypothesis is needed: it follows from `q` not being a root of unity. -/
theorem kz_conj_jimbo_complex (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ)) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ h,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) * kzHeckeC m c κ h =
        jimboRep (qC κ) (qC_ne_zero κ) m h * U := by
  set G : Set ℂ := {κ : ℂ | ¬ GenericParameter.NotRootOfUnity (qC κ)}
  set S : Set ℂ := {κ : ℂ | Set.InjOn (qInt2 (qC κ)) {d | d ∈ contentRange m}}
  have hGc : G.Countable := countable_rootOfUnity_couplings
  have hrank : (1 : Cardinal) < Module.rank ℝ ℂ := by
    rw [Complex.rank_real_complex]; norm_num
  have hGcS : Gᶜ ⊆ S := fun x hx =>
    (qInt2_injective (qC x) (qC_ne_zero x) (by simpa [G] using hx)).injOn
  have hcl : closure Gᶜ = Set.univ := (hGc.dense_compl ℂ).closure_eq
  have hS : IsPreconnected S :=
    (hGc.isPathConnected_compl_of_one_lt_rank hrank).isConnected.isPreconnected.subset_closure
      hGcS (by rw [hcl]; exact Set.subset_univ _)
  have hdense : S ⊆ closure (S ∩ {x | GenericParameter.NotRootOfUnity (qC x)}) := by
    have : Gᶜ ⊆ S ∩ {x | GenericParameter.NotRootOfUnity (qC x)} := fun x hx =>
      ⟨hGcS hx, by simpa [G] using hx⟩
    calc S ⊆ closure Gᶜ := by rw [hcl]; exact Set.subset_univ _
      _ ⊆ _ := closure_mono this
  have h0 : (0 : ℂ) ∈ S := by
    show Set.InjOn (qInt2 (qC 0)) _
    rw [qC_zero]
    exact (qInt2_one_injective (K := ℂ)).injOn
  have hκS : κ ∈ S := hGcS (by simpa [G] using hκ)
  exact conj_of_isPreconnected_hecke (n := m) hS continuous_qC.continuousOn
    (fun x _ => qC_ne_zero x) (fun x hx => hx) hdense
    (kzHeckeC m c) (fun x => jimboRep (qC x) (qC_ne_zero x) m)
    (fun j => (continuous_kzHeckeC_σ c j).continuousOn)
    (fun j => (continuous_jimboRepC_σ j).continuousOn)
    (fun _ => Classical.arbitrary _) (x₀ := 0) h0 1
    (fun j => by rw [kzHeckeC_zero_σ c j]; simp) hκS hκ

/-- **Generator form at a complex coupling.** If `q = e^{2πiκ}` is not a root of unity, one
invertible `U` satisfies `U · (e^{2πiκc} θ_κ(σ_j)) = Ř_{j,j+1}(q) · U` for every `j`. -/
theorem kz_conj_jimbo_complex_σ (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ)) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ, ∀ j : Fin m,
      (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) *
        (Complex.exp (2 * κ * (Real.pi * I) * c) • ((kzBraidRep permRep κ c (σ j) :
          (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
          Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)) =
        strandBraid (qC κ) (qC κ)⁻¹ j * U := by
  obtain ⟨U, hU⟩ := kz_conj_jimbo_complex (m := m) c κ hκ
  refine ⟨U, fun j => ?_⟩
  have := hU (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j)
  rwa [kzHeckeC_σ, jimboRep_σ] at this

end Assembly

end QOU.Mass.KohnoAssembly
