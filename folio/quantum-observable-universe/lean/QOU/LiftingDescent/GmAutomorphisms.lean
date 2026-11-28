import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.MonoidAlgebra.MapDomain
import Mathlib.Tactic

/-!
# `Aut(G_m) = {±1}`: the orientation of `G_m` is exactly one bit

`G_m = Spec R[q, q⁻¹]` with coproduct `Δ q = q ⊗ q`. An endomorphism of the group `G_m` is an
`R`-algebra map `φ` of `R[q, q⁻¹]` with `Δ ∘ φ = (φ ⊗ φ) ∘ Δ`. Since `φ` is fixed by `φ q`, and
`Δ`, `φ ⊗ φ` are algebra maps, this says exactly that `p = φ q` is **group-like**:
`Δ p = p ⊗ p`. Here `R[q, q⁻¹] ⊗ R[q, q⁻¹] = R[ℤ × ℤ]`, `Δ` is the diagonal `n ↦ (n, n)` and
`p ⊗ p = ι₁ p · ι₂ p`.

* `isGroupLike_iff`: over a domain, the group-like elements are exactly the `qᵏ`.
* `algHom_T_eq_of_isGroupLike`: so every endomorphism of `G_m` is `q ↦ qᵏ`, `k ∈ ℤ`
  (`End(G_m) = ℤ`, the character group).
* `eq_one_or_neg_one_of_surjective`: an automorphism has `k = ±1`.
* `isGroupLike_T`: both `q ↦ q` and `q ↦ q⁻¹` occur.

So `Aut(G_m) = {±1}`: the only non-trivial automorphism is the inversion `q ↦ q⁻¹`, the bar
involution. In the chirality question (`QOU.StandardModel.ChiralityOrientation`, and the
complex-conjugation results on PR #9811) this means the choice to be derived is **one bit**:
an orientation of `G_m`. Complex conjugation acts on `μ_n = G_m[n]` by this inversion.

Pure algebra over any domain (in particular `ℤ`). No measured values.
-/

namespace QOU.FormalGroups.GmAut

open LaurentPolynomial AddMonoidAlgebra

noncomputable section

variable {R : Type*} [CommRing R]

/-- Laurent polynomials in two variables, `R[ℤ × ℤ] = R[q, q⁻¹] ⊗ R[q, q⁻¹]`. -/
abbrev L2 (R : Type*) [CommRing R] := AddMonoidAlgebra R (ℤ × ℤ)

/-- The coproduct `Δ qⁿ = qⁿ ⊗ qⁿ`. -/
def comul : R[T;T⁻¹] →+* L2 R :=
  mapDomainRingHom R (AddMonoidHom.prod (AddMonoidHom.id ℤ) (AddMonoidHom.id ℤ))

/-- `p ↦ p ⊗ 1`. -/
def inl : R[T;T⁻¹] →+* L2 R := mapDomainRingHom R (AddMonoidHom.inl ℤ ℤ)

/-- `p ↦ 1 ⊗ p`. -/
def inr : R[T;T⁻¹] →+* L2 R := mapDomainRingHom R (AddMonoidHom.inr ℤ ℤ)

/-- `p` is group-like: `Δ p = p ⊗ p`. -/
def IsGroupLike (p : R[T;T⁻¹]) : Prop := comul p = inl p * inr p

theorem comul_apply (p : R[T;T⁻¹]) (a b : ℤ) :
    comul p (a, b) = if a = b then p a else 0 := by
  unfold comul
  simp only [mapDomainRingHom_apply]
  split_ifs with h
  · subst h
    have hinj : Function.Injective
        (AddMonoidHom.prod (AddMonoidHom.id ℤ) (AddMonoidHom.id ℤ)) := fun x y h => by
      simpa using congrArg Prod.fst h
    exact Finsupp.mapDomain_apply hinj p a
  · apply Finsupp.mapDomain_notin_range
    rintro ⟨n, hn⟩
    simp only [AddMonoidHom.prod_apply, AddMonoidHom.id_apply, Prod.mk.injEq] at hn
    exact h (hn.1.symm.trans hn.2)

theorem inl_mul_inr_apply (p r : R[T;T⁻¹]) (a b : ℤ) :
    (inl p * inr r) (a, b) = p a * r b := by
  induction p using Finsupp.induction_linear with
  | zero => simp
  | add f g hf hg => rw [map_add, add_mul, Finsupp.add_apply, hf, hg, Finsupp.add_apply, add_mul]
  | single a₀ c =>
    induction r using Finsupp.induction_linear with
    | zero => simp
    | add f g hf hg =>
      rw [map_add, mul_add, Finsupp.add_apply, hf, hg, Finsupp.add_apply, mul_add]
    | single b₀ d =>
      have h1 : inl (Finsupp.single a₀ c : R[T;T⁻¹]) = (Finsupp.single (a₀, 0) c : L2 R) :=
        Finsupp.mapDomain_single
      have h2 : inr (Finsupp.single b₀ d : R[T;T⁻¹]) = (Finsupp.single (0, b₀) d : L2 R) :=
        Finsupp.mapDomain_single
      rw [h1, h2, AddMonoidAlgebra.single_mul_single]
      simp only [Prod.mk_add_mk, add_zero, zero_add, Finsupp.single_apply, Prod.mk.injEq]
      split_ifs <;> simp_all

variable [IsDomain R]

/-- **Group-like elements of `R[q, q⁻¹]` are exactly the `qᵏ`** (over a domain). -/
theorem isGroupLike_iff (p : R[T;T⁻¹]) : IsGroupLike p ∧ p ≠ 0 ↔ ∃ k, p = T k := by
  constructor
  · rintro ⟨hg, hp⟩
    have hco : ∀ a b, (if a = b then p a else 0) = p a * p b := fun a b => by
      rw [← comul_apply, ← inl_mul_inr_apply, hg]
    obtain ⟨k, hk⟩ : ∃ k, p k ≠ 0 := by
      by_contra h; push_neg at h; exact hp (Finsupp.ext h)
    have hkk : p k = 1 := by
      have := hco k k
      rw [if_pos rfl] at this
      have h2 : p k * (p k - 1) = 0 := by linear_combination -this
      rcases mul_eq_zero.mp h2 with h | h
      · exact absurd h hk
      · linear_combination h
    refine ⟨k, Finsupp.ext fun a => ?_⟩
    show p a = (Finsupp.single k 1 : ℤ →₀ R) a
    rw [Finsupp.single_apply]
    split_ifs with h
    · subst h; exact hkk
    · have := hco a k
      rw [if_neg (Ne.symm h)] at this
      rcases mul_eq_zero.mp this.symm with h' | h'
      · exact h'
      · exact absurd h' hk
  · rintro ⟨k, rfl⟩
    refine ⟨?_, fun h => by simpa using congrArg (fun f : R[T;T⁻¹] => f k) h⟩
    unfold IsGroupLike
    ext ⟨a, b⟩
    rw [comul_apply, inl_mul_inr_apply]
    show _ = (Finsupp.single k 1 : ℤ →₀ R) a * (Finsupp.single k 1 : ℤ →₀ R) b
    simp only [Finsupp.single_apply]
    split_ifs <;> simp_all

theorem isGroupLike_T (k : ℤ) : IsGroupLike (T k : R[T;T⁻¹]) :=
  ((isGroupLike_iff _).mpr ⟨k, rfl⟩).1

/-- An endomorphism of `G_m`: an algebra map whose value on `q` is group-like. -/
def IsGmEndo (φ : R[T;T⁻¹] →ₐ[R] R[T;T⁻¹]) : Prop := IsGroupLike (φ (T 1))

omit [IsDomain R] in
theorem algHom_T_one_ne_zero [Nontrivial R] (φ : R[T;T⁻¹] →ₐ[R] R[T;T⁻¹]) : φ (T 1) ≠ 0 := by
  intro h
  have h1 : φ (T 1 * T (-1)) = 1 := by rw [← T_add, add_neg_cancel, T_zero, map_one]
  rw [map_mul, h, zero_mul] at h1
  exact zero_ne_one h1

/-- **Every endomorphism of `G_m` is `q ↦ qᵏ`.** -/
theorem algHom_T_eq_of_isGroupLike (φ : R[T;T⁻¹] →ₐ[R] R[T;T⁻¹]) (hφ : IsGmEndo φ) :
    ∃ k, φ (T 1) = T k :=
  (isGroupLike_iff _).mp ⟨hφ, algHom_T_one_ne_zero φ⟩

omit [IsDomain R] in
theorem algHom_T (φ : R[T;T⁻¹] →ₐ[R] R[T;T⁻¹]) {k : ℤ} (hk : φ (T 1) = T k) (n : ℤ) :
    φ (T n) = T (k * n) := by
  have hinv : φ (T (-1)) = T (-k) := by
    have h1 : φ (T 1) * φ (T (-1)) = 1 := by
      rw [← map_mul, ← T_add, add_neg_cancel, T_zero, map_one]
    rw [hk] at h1
    have h2 : T k * T (-k) = (1 : R[T;T⁻¹]) := by rw [← T_add, add_neg_cancel, T_zero]
    calc φ (T (-1)) = T (-k) * (T k * φ (T (-1))) := by
          rw [← mul_assoc, mul_comm (T (-k)), h2, one_mul]
      _ = T (-k) := by rw [h1, mul_one]
  rcases Int.eq_nat_or_neg n with ⟨m, rfl | rfl⟩
  · have e : (T (m : ℤ) : R[T;T⁻¹]) = T 1 ^ m := by rw [T_pow]; simp
    rw [e, map_pow, hk, T_pow]
    congr 1; ring
  · have e : (T (-(m : ℤ)) : R[T;T⁻¹]) = T (-1) ^ m := by rw [T_pow]; simp
    rw [e, map_pow, hinv, T_pow]
    congr 1; ring

/-- The coefficients of `φ f` live on `kℤ`. -/
omit [IsDomain R] in
theorem coeff_algHom_eq_zero (φ : R[T;T⁻¹] →ₐ[R] R[T;T⁻¹]) {k : ℤ} (hk : φ (T 1) = T k)
    (f : R[T;T⁻¹]) (a : ℤ) (ha : ¬ k ∣ a) : φ f a = 0 := by
  induction f using LaurentPolynomial.induction_on' with
  | add p q hp hq => rw [map_add, Finsupp.add_apply, hp, hq, add_zero]
  | C_mul_T n c =>
    have hC : φ (C c) = C c := by rw [C_eq_algebraMap, AlgHom.commutes]
    rw [map_mul, hC, algHom_T φ hk, ← single_eq_C_mul_T]
    rw [Finsupp.single_apply, if_neg]
    rintro rfl
    exact ha (dvd_mul_right k n)

/-- **An automorphism of `G_m` is `q ↦ q` or `q ↦ q⁻¹`:** `Aut(G_m) = {±1}`. -/
theorem eq_one_or_neg_one_of_surjective (φ : R[T;T⁻¹] →ₐ[R] R[T;T⁻¹]) (hφ : IsGmEndo φ)
    (hs : Function.Surjective φ) : φ (T 1) = T 1 ∨ φ (T 1) = T (-1) := by
  obtain ⟨k, hk⟩ := algHom_T_eq_of_isGroupLike φ hφ
  obtain ⟨f, hf⟩ := hs (T 1)
  have hdiv : k ∣ 1 := by
    by_contra h
    have := coeff_algHom_eq_zero φ hk f 1 h
    rw [hf, T, Finsupp.single_apply, if_pos rfl] at this
    exact one_ne_zero this
  rcases Int.isUnit_iff.mp (isUnit_of_dvd_one hdiv) with rfl | rfl
  · exact Or.inl hk
  · exact Or.inr hk

end

end QOU.FormalGroups.GmAut
