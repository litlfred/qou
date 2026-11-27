import QOU.Transcendental.MassTheory.KohnoAssembly
import BraidKnotOctonion.TensorEmbeddingGL

/-!
# Drinfeld–Kohno for `V = ℂ^d`, every `d`

`KohnoAssembly` proves the Kohno comparison on `V^{⊗(m+1)}` with `V = ℂ²`. This file proves it
for the vector representation of `𝔤𝔩_d`, `V = ℂ^d`, every `d`. The case `d = 3` is the colour
factor that `BridgeAColourSplit.colourFlavour_monodromy_conj` takes as its hypothesis `hcol`.

The proof is the same assembly. Only the `ℂ²`-specific inputs change:

* `permRepN` — the permutation representation of `S_k` on `(ℂ^d)^{⊗k}`, in the coordinate model
  `(Fin k → Fin d) → ℂ`;
* `permRepN_adjSwap` — at `q = 1` Jimbo's `𝔤𝔩_d` braiding `TensorEmbedGL.strandBraid 1 1 j` is
  the permutation matrix of `(j, j+1)`, exactly, with no scalar;
* `jimboRepN` — the Jimbo action `H_{m+1}(q) → End((ℂ^d)^{⊗(m+1)})`, built from the Hecke
  relations already proved in `TensorEmbeddingGL` (`isHeckeGenerator_braidAt`,
  `braidAt_braid`, `braidAt_commute`);
* `continuous_strandBraidN_exp` — its generators are continuous in the coupling.

The rest is unchanged from `KohnoAssembly`: the KZ generators satisfy the Hecke quadratic for
every `ρ` (`LocalMonodromy.kzBraidRep_sigma_isHeckeQuad`), and the rigidity interface
`conj_of_isPreconnected_hecke` is stated for matrices over any finite index type.

## Results

* `kz_conj_jimboN_complex` — for every complex `κ` with `q = e^{2πiκ}` not a root of unity,
  the KZ representation of `H_{m+1}(q)` on `(ℂ^d)^{⊗(m+1)}`, rescaled by `e^{2πiκc}` per
  crossing, is conjugate to Jimbo's `𝔤𝔩_d` representation by an invertible matrix.
* `kz_conj_jimboN_complex_σ` — the same on the braid generators:
  `U (e^{2πiκc} θ_κ(σ_j)) = Ř_{j,j+1}(q) U` for every `j`, with one `U`.

Sorry-free. Roots of unity `q ≠ 1` are excluded, as in `KohnoAssembly`. Conjugacy only: `U` comes
from rank comparison, and no explicit intertwiner is constructed.

## Base ring (§7c)

`permRepN`, `permRepN_adjSwap`, `strandBraidN_map` and `jimboRepN` are over a generic
commutative ring or field. The assembly is over `ℂ`, because it uses continuity in the coupling
and the topology of the `κ`-plane.

-- Ref: [kohno1987] T. Kohno, Monodromy representations of braid groups and Yang–Baxter
--   equations, Ann. Inst. Fourier 37 (1987) 139–160.
-- Ref: [drinfeld1990] V. G. Drinfeld, Quasi-Hopf algebras, Leningrad Math. J. 1 (1990).
-- Ref: [jimbo1986] M. Jimbo, A q-analogue of U(gl(N+1)), Hecke algebra, and the Yang–Baxter
--   equation, Lett. Math. Phys. 11 (1986) 247–252.
-/

namespace QOU.Mass.KohnoAssemblyGL

open QOU.IwahoriHecke.TensorEmbedGL
open QOU.SchurWeyl QOU.SchurWeyl.JMProjector
open QOU.Mass.KZHolonomy QOU.Mass.BraidHeckeFactor QOU.MathlibExt.Braid
open QOU.Mass.KohnoAssembly (qC qC_ne_zero qC_zero continuous_qC
  countable_rootOfUnity_couplings conj_of_isPreconnected_hecke)
open Complex Set

variable {d : ℕ}

/-! ## The permutation representation and the base point -/

section Perm

variable {R : Type*} [CommRing R] {k : ℕ}

/-- The permutation representation of `S_k` on `V^{⊗k}`, `V = R^d`, in the coordinate model
`(Fin k → Fin d) → R`: `permRepN σ a b = 1` iff `b = a ∘ σ`. -/
def permRepN : Equiv.Perm (Fin k) →* Matrix (Fin k → Fin d) (Fin k → Fin d) R where
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

theorem permRepN_apply (σ : Equiv.Perm (Fin k)) (a b : Fin k → Fin d) :
    (permRepN σ : Matrix _ _ R) a b = if b = a ∘ σ then 1 else 0 := rfl

/-- At `q = 1` Jimbo's `𝔤𝔩_d` `Ř` is the flip `e_x ⊗ e_y ↦ e_y ⊗ e_x`. -/
theorem rCheckN_one_apply (a b : Fin d × Fin d) :
    rCheckN (1 : R) 1 a b = if a = (b.2, b.1) then 1 else 0 := by
  rw [rCheckN_apply, sub_self]
  by_cases hab : a = b
  · subst hab
    by_cases h : a.1 = a.2
    · simp [h]
      intro hne
      exact absurd (Prod.ext (x := a) (y := (a.2, a.2)) h rfl) hne
    · have : a ≠ (a.2, a.1) := fun e => h (congrArg Prod.fst e)
      simp [h, this]
  · rw [if_neg hab]

/-- **At `q = 1` the `𝔤𝔩_d` Jimbo generator is the permutation matrix of the adjacent
transposition**, exactly. This is the base-point match with KZ at coupling `0`. -/
theorem permRepN_adjSwap {m : ℕ} (j : Fin m) :
    (permRepN (adjSwap j) : Matrix _ _ R) = strandBraid (d := d) (1 : R) 1 j := by
  ext a b
  rw [permRepN_apply, strandBraid, braidAt, embedPair_apply, rCheckN_one_apply]
  simp only [Prod.mk.injEq]
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

/-! ## The Jimbo generator as a function of `q` -/

section JimboFamily

variable {R S : Type*} [CommRing R] [CommRing S]

theorem rCheckN_map (f : R →+* S) (q qi : R) :
    (rCheckN (d := d) q qi).map f = rCheckN (f q) (f qi) := by
  ext a b
  simp only [Matrix.map_apply, rCheckN_apply]
  split_ifs <;> simp

theorem embedPairN_map (f : R →+* S) {n : ℕ} (i j : Fin n)
    (M : Matrix (Fin d × Fin d) (Fin d × Fin d) R) :
    (embedPair i j M).map f = embedPair i j (M.map f) := by
  ext a b
  simp only [Matrix.map_apply, embedPair_apply]
  split_ifs <;> simp

/-- The `𝔤𝔩_d` Jimbo generator commutes with change of coefficients. -/
theorem strandBraidN_map (f : R →+* S) {m : ℕ} (q qi : R) (j : Fin m) :
    (strandBraid (d := d) q qi j).map f = strandBraid (f q) (f qi) j := by
  simp only [strandBraid, braidAt, embedPairN_map, rCheckN_map]

/-- The `𝔤𝔩_d` Jimbo generator is continuous in the coupling: with `q = e^z` every entry is
`0`, `1`, `q` or `q − q⁻¹`. -/
theorem continuous_strandBraidN_exp {m : ℕ} (j : Fin m) :
    Continuous (fun z : ℂ => strandBraid (d := d) (Complex.exp z) (Complex.exp z)⁻¹ j) := by
  refine continuous_matrix fun a b => ?_
  simp only [strandBraid, braidAt, embedPair_apply, rCheckN_apply]
  split_ifs
  · exact Complex.continuous_exp
  · exact Complex.continuous_exp.sub (Complex.continuous_exp.inv₀ fun z => Complex.exp_ne_zero z)
  all_goals exact continuous_const

end JimboFamily

/-! ## The `𝔤𝔩_d` Jimbo action on the skein presentation -/

section JimboHecke

variable {K : Type*} [Field K]

theorem strandBraidN_quad {m : ℕ} {q : K} (hq : q ≠ 0) (j : Fin m) :
    strandBraid (d := d) q q⁻¹ j * strandBraid q q⁻¹ j =
      (q - q⁻¹) • strandBraid q q⁻¹ j + (q * q⁻¹) • (1 : Matrix (Fin (m + 1) → Fin d) _ K) := by
  have h := isHeckeGenerator_braidAt (R := K) (d := d) q q⁻¹ (i := j.castSucc) (j := j.succ)
    (by simp [Fin.ext_iff]) (mul_inv_cancel₀ hq)
  have h' : strandBraid (d := d) q q⁻¹ j * strandBraid q q⁻¹ j =
      algebraMap K _ (q - q⁻¹) * strandBraid q q⁻¹ j + 1 := h
  rw [h', mul_inv_cancel₀ hq, one_smul, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]

/-- **The `𝔤𝔩_d` Jimbo action** `H_{m+1}(q) →ₐ End((K^d)^{⊗(m+1)})`, `σ_j ↦ Ř_{j,j+1}`. -/
noncomputable def jimboRepN (q : K) (hq : q ≠ 0) (m : ℕ) :
    Hecke K q q⁻¹ m →ₐ[K] Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K :=
  Hecke.lift K q q⁻¹ m (fun j => strandBraid q q⁻¹ j) (fun j => strandBraidN_quad hq j)
    (fun i hi => braidAt_braid (R := K) (d := d) q q⁻¹ (i := i.castSucc) (j := i.succ)
      (k := (⟨(i : ℕ) + 1, hi⟩ : Fin m).succ)
      (by simp [Fin.ext_iff]) (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff])
      (mul_inv_cancel₀ hq) |>.trans (by
        have e : (⟨(i : ℕ) + 1, hi⟩ : Fin m).castSucc = i.succ := by simp [Fin.ext_iff]
        simp only [strandBraid, e]))
    (fun i j hij => braidAt_commute (R := K) (d := d) q q⁻¹ (by simp [Fin.ext_iff])
      (by simp [Fin.ext_iff]) (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega)
      (by simp [Fin.ext_iff]; omega) (by simp [Fin.ext_iff]; omega))

@[simp] theorem jimboRepN_σ (q : K) (hq : q ≠ 0) (m : ℕ) (j : Fin m) :
    jimboRepN (d := d) q hq m (Hecke.σ K q q⁻¹ m j) = strandBraid q q⁻¹ j :=
  Hecke.lift_σ _ _ _ _ _ _ _ _ j

end JimboHecke

/-! ## The assembly at complex couplings -/

section Assembly

variable {m : ℕ}

/-- Shorthand for `End((ℂ^d)^{⊗(m+1)})`. -/
abbrev MatN (d m : ℕ) := Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) ℂ

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

theorem kzQuadN (m : ℕ) (c κ : ℂ) :
    ∀ hm : 0 < m, IsHeckeQuad (Complex.exp (2 * κ * (Real.pi * I) * c)) (qC κ) (qC κ)⁻¹
      ((kzBraidRep (permRepN (R := ℂ) (d := d) (k := m + 1)) κ c (σ ⟨0, hm⟩) :
        (MatN d m)ˣ) : MatN d m) := by
  intro hm
  cases m with
  | zero => exact absurd hm (lt_irrefl 0)
  | succ k =>
      exact LocalMonodromy.kzBraidRep_sigma_isHeckeQuad
        (permRepN (R := ℂ) (d := d) (k := k + 2)) κ c 0

/-- The KZ representation of `H_{m+1}(q(κ))` on `(ℂ^d)^{⊗(m+1)}` at a complex coupling `κ`. -/
noncomputable def kzHeckeN (m : ℕ) (c κ : ℂ) :
    Hecke ℂ (qC κ) (qC κ)⁻¹ m →ₐ[ℂ] MatN d m :=
  heckeOfBraidRepOfZero (s := Complex.exp (2 * κ * (Real.pi * I) * c))
    (kzBraidRep permRepN κ c) (kzQuadN m c κ)

theorem kzHeckeN_σ (c κ : ℂ) (j : Fin m) :
    kzHeckeN (d := d) m c κ (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j) =
      Complex.exp (2 * κ * (Real.pi * I) * c) •
        ((kzBraidRep permRepN κ c (σ j) : (MatN d m)ˣ) : MatN d m) := by
  simp only [kzHeckeN, heckeOfBraidRepOfZero, heckeOfBraidRep_σ]

theorem continuous_kzHeckeN_σ (c : ℂ) (j : Fin m) :
    Continuous (fun κ => kzHeckeN (d := d) m c κ (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j)) := by
  have hk := continuous_kzBraidRep_σ (A := MatN d m) (permRepN (R := ℂ) (d := d) (k := m + 1)) c j
  have hc : Continuous (fun κ : ℂ => Complex.exp (2 * κ * (Real.pi * I) * c) •
      ((kzBraidRep permRepN κ c (σ j) : (MatN d m)ˣ) : MatN d m)) := by
    refine Continuous.smul ?_ hk
    exact Complex.continuous_exp.comp
      (((continuous_const.mul continuous_id).mul continuous_const).mul continuous_const)
  simpa only [kzHeckeN_σ] using hc

theorem continuous_jimboRepN_σ (j : Fin m) :
    Continuous (fun κ => jimboRepN (d := d) (qC κ) (qC_ne_zero κ) m
      (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j)) := by
  simp only [jimboRepN_σ, qC]
  exact (continuous_strandBraidN_exp j).comp
    ((continuous_const.mul continuous_id).mul continuous_const)

theorem kzHeckeN_zero_σ (c : ℂ) (j : Fin m) :
    kzHeckeN (d := d) m c 0 (Hecke.σ ℂ (qC 0) (qC 0)⁻¹ m j) =
      jimboRepN (qC 0) (qC_ne_zero 0) m (Hecke.σ ℂ (qC 0) (qC 0)⁻¹ m j) := by
  rw [kzHeckeN_σ, jimboRepN_σ]
  have hs : Complex.exp (2 * (0 : ℂ) * (Real.pi * I) * c) = 1 := by simp
  rw [hs, one_smul, kzBraidRep_zero_σ, permRepN_adjSwap, qC_zero, inv_one]

/-- **Drinfeld–Kohno for `V = ℂ^d`.** At every complex coupling `κ` with `q = e^{2πiκ}` not a
root of unity, the KZ representation of `H_{m+1}(q)` on `(ℂ^d)^{⊗(m+1)}`, rescaled by
`e^{2πiκc}` per crossing, is conjugate to Jimbo's `𝔤𝔩_d` representation by an invertible
matrix. -/
theorem kz_conj_jimboN_complex (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ)) :
    ∃ U : (MatN d m)ˣ, ∀ h,
      (U : MatN d m) * kzHeckeN (d := d) m c κ h =
        jimboRepN (d := d) (qC κ) (qC_ne_zero κ) m h * U := by
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
    (kzHeckeN (d := d) m c) (fun x => jimboRepN (d := d) (qC x) (qC_ne_zero x) m)
    (fun j => (continuous_kzHeckeN_σ c j).continuousOn)
    (fun j => (continuous_jimboRepN_σ j).continuousOn)
    (fun _ => Classical.arbitrary _) (x₀ := 0) h0 1
    (fun j => by rw [kzHeckeN_zero_σ c j]; simp) hκS hκ

/-- **Generator form.** If `q = e^{2πiκ}` is not a root of unity, one invertible `U` satisfies
`U · (e^{2πiκc} θ_κ(σ_j)) = Ř_{j,j+1}(q) · U` for every `j`, on `(ℂ^d)^{⊗(m+1)}`. -/
theorem kz_conj_jimboN_complex_σ (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ)) :
    ∃ U : (MatN d m)ˣ, ∀ j : Fin m,
      (U : MatN d m) * (Complex.exp (2 * κ * (Real.pi * I) * c) •
        ((kzBraidRep permRepN κ c (σ j) : (MatN d m)ˣ) : MatN d m)) =
        strandBraid (d := d) (qC κ) (qC κ)⁻¹ j * U := by
  obtain ⟨U, hU⟩ := kz_conj_jimboN_complex (d := d) (m := m) c κ hκ
  refine ⟨U, fun j => ?_⟩
  have := hU (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ m j)
  rwa [kzHeckeN_σ, jimboRepN_σ] at this

end Assembly

end QOU.Mass.KohnoAssemblyGL
