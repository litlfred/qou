import CompactQuantumMetrics.OqSU2HaarState
import CompactQuantumMetrics.OqSU2Star
import CompactQuantumMetrics.HaarMomentKernel
import Mathlib.Algebra.Ring.GeomSum

/-!
# Positivity of the Haar state on `O_q(SU(2))`

Bean `qou-q3dc`. `OqSU2HaarState.lean` builds the Haar state `h` algebraically. This
file proves it is positive for the star `compactStar` of `OqSU2Star.lean`:
`h(x^* x) ≥ 0` for every `x`, over any linearly ordered field `K`, at every unit
`q` with `0 < q` and `q ≠ 1`. The proof is algebraic throughout: no analysis, no
limits, no numerical values.

## Proof outline

1. **Monomials span.** `monoMap_cyclic`: every `x` is `μ(π(x)e₀)`, a finite
   combination of ordered monomials `A_a β^b γ^c` (`A_a = α^a` or `δ^{-a}`).
2. **Star of a monomial.** `star_mono_mul_mono`: `(A_a β^b γ^c)^* A_a β^{b'} γ^{c'}` is a
   scalar times `N_a ζ^{b+c'}`, where `ζ = βγ` and `N_a = A_a^* A_a`.
3. **Weight orthogonality.** `haarState_star_mono_mul_ne`: by torus invariance,
   monomials of different weight `(a, b − c)` are `h`-orthogonal.
4. **Twisted moments.** `haarState_normSq`: `h(N_a ζ^k) = C_a ρ_a^k / ∏_{m<A}(1 − q^{2(k+1+m)})`,
   from the closed forms `GV_closed`, `GW_closed` of `HaarMomentKernel.lean`.
5. **Sums of squares.** `gram_isWSOS`: on each weight block the Gram kernel is a
   `q`-Pick kernel, a weighted sum of squares by `isWSOS_qPick`. So the Gram form is
   nonnegative, giving `haarState_star_mul_self_nonneg_of_lt_one` for `0 < q < 1`.
6. **Inversion.** `invHom : O_q → O_{q⁻¹}`, `α ↦ δ', β ↦ qβ', γ ↦ q⁻¹γ', δ ↦ α'`, is an
   algebra map (`isOqSU2Quadruple_inv`) that intertwines the stars
   (`invHom_compactStar`). The Haar moments are symmetric under `q ↦ q⁻¹`
   (`haarMoment_inv`), so `h_q = h_{q⁻¹} ∘ φ` (`haarState_invHom`). This moves `q > 1`
   to `q⁻¹ < 1` (`haarState_star_mul_self_nonneg_of_one_lt`).

## Main results (sorry-free)

* `haarState_star_mul_self_nonneg`: `0 < q`, `q ≠ 1` ⇒ `0 ≤ h(x^* x)`.
* `haarState_invHom`: `h_{q⁻¹}(φ x) = h_q(x)`.
* `haarState_mono`: `h(A_a β^b γ^c) = [a = 0 ∧ b = c] · h(ζ^b)`.

## Not established

* Faithfulness (`h(x^* x) = 0 ⇒ x = 0`); it needs PBW independence of the monomials.
* Full coproduct invariance `(id ⊗ h)Δ = h · 1`.
* The case `q = 1` (commutative `O(SU(2))`). The proof uses `q^2 ≠ 1` for the
  closed forms of the moments.

## References

- [woronowicz1987-twisted-su2] Woronowicz, *Twisted SU(2) group*, Publ. RIMS 23
  (1987) 117–181, Thm. 1.4 (the `*`-structure).
-/

/-! ## More on weighted sums of squares -/

namespace QOU.AlgebraicSubstrate.PickSOS.IsWSOS

set_option linter.unusedSectionVars false

open Finset

variable {𝕜 : Type*} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] {ι : Type*}
  {s : Finset ι} {K L : ι → ι → 𝕜}

omit [IsStrictOrderedRing 𝕜] in
theorem zero : IsWSOS s fun (_ _ : ι) => (0 : 𝕜) :=
  ⟨0, Fin.elim0, Fin.elim0, fun t => t.elim0, fun _ _ _ _ => by simp⟩

omit [IsStrictOrderedRing 𝕜] in
theorem add (hK : IsWSOS s K) (hL : IsWSOS s L) : IsWSOS s fun i j => K i j + L i j := by
  obtain ⟨n, w, g, hw, hK⟩ := hK
  obtain ⟨m, v, f, hv, hL⟩ := hL
  refine ⟨n + m, Fin.append w v, Fin.append g f, fun t => ?_, fun i hi j hj => ?_⟩
  · refine Fin.addCases (fun t => ?_) (fun t => ?_) t <;> simp [hw, hv]
  · dsimp only
    rw [hK i hi j hj, hL i hi j hj, Fin.sum_univ_add]
    simp

theorem sum {κ : Type*} (u : Finset κ) {F : κ → ι → ι → 𝕜} (hF : ∀ k ∈ u, IsWSOS s (F k)) :
    IsWSOS s fun i j => ∑ k ∈ u, F k i j := by
  classical
  induction u using Finset.induction_on with
  | empty => simpa using (zero (s := s) (𝕜 := 𝕜))
  | insert a u ha ih =>
    have h1 := hF a (mem_insert_self a u)
    have h2 := ih fun k hk => hF k (mem_insert_of_mem hk)
    exact (h1.add h2).congr_on fun i _ j _ => by rw [sum_insert ha]

omit [IsStrictOrderedRing 𝕜] in
/-- Pull back along an index map. -/
theorem comap {ι' : Type*} [DecidableEq ι'] (f : ι → ι') {K' : ι' → ι' → 𝕜}
    (h : IsWSOS (s.image f) K') (hK : ∀ i ∈ s, ∀ j ∈ s, K i j = K' (f i) (f j)) :
    IsWSOS s K := by
  obtain ⟨n, w, g, hw, h⟩ := h
  exact ⟨n, w, fun t i => g t (f i), hw, fun i hi j hj => by
    rw [hK i hi j hj, h _ (mem_image_of_mem f hi) _ (mem_image_of_mem f hj)]⟩

/-- A kernel that vanishes between different blocks and is a weighted sum of squares on
each block is a weighted sum of squares. -/
theorem of_blocks {κ : Type*} [DecidableEq κ] (key : ι → κ)
    (hoff : ∀ i ∈ s, ∀ j ∈ s, key i ≠ key j → K i j = 0)
    (hblk : ∀ k ∈ s.image key, IsWSOS (s.filter fun i => key i = k) K) : IsWSOS s K := by
  classical
  have hterm : ∀ k ∈ s.image key,
      IsWSOS s fun i j => if key i = k ∧ key j = k then K i j else 0 := by
    intro k hk
    obtain ⟨n, w, g, hw, h⟩ := hblk k hk
    refine ⟨n, w, fun t i => if key i = k then g t i else 0, hw, fun i hi j hj => ?_⟩
    dsimp only
    by_cases hij : key i = k ∧ key j = k
    · rw [if_pos hij, h i (mem_filter.2 ⟨hi, hij.1⟩) j (mem_filter.2 ⟨hj, hij.2⟩)]
      simp [hij.1, hij.2]
    · rw [if_neg hij]
      refine (sum_eq_zero fun t _ => ?_).symm
      by_cases h1 : key i = k
      · have h2 : key j ≠ k := fun h2 => hij ⟨h1, h2⟩
        simp [h2]
      · simp [h1]
  refine (sum (s.image key) hterm).congr_on fun i hi j hj => ?_
  by_cases hij : key i = key j
  · rw [sum_eq_single (key i)]
    · simp [hij]
    · intro k _ hk; simp [Ne.symm hk]
    · intro h; exact absurd (mem_image_of_mem key hi) h
  · rw [hoff i hi j hj hij]
    simp

end QOU.AlgebraicSubstrate.PickSOS.IsWSOS

namespace QOU.AlgebraicSubstrate.OqSU2

open Finsupp

section Algebra

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- `ζ = β γ`. -/
noncomputable abbrev zeta : OqSU2 R q := β q * γ q

theorem pow_comm_of {A : Type*} [Ring A] [Algebra R A] {x y : A} {c : R}
    (h : y * x = c • (x * y)) (n : ℕ) : y * x ^ n = c ^ n • (x ^ n * y) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, h, mul_smul_comm, smul_smul,
      ← mul_assoc, pow_succ]

theorem beta_alpha : β q * α (R := R) q = ((q⁻¹ : Rˣ) : R) • (α q * β q) := by
  rw [rel_ab, smul_smul, ← Units.val_mul, inv_mul_cancel, Units.val_one, one_smul]

theorem gamma_alpha : γ q * α (R := R) q = ((q⁻¹ : Rˣ) : R) • (α q * γ q) := by
  rw [rel_ag, smul_smul, ← Units.val_mul, inv_mul_cancel, Units.val_one, one_smul]

theorem beta_delta : β (R := R) q * δ q = (q : R) • (δ q * β q) := rel_bd q

theorem gamma_delta : γ (R := R) q * δ q = (q : R) • (δ q * γ q) := rel_gd q

theorem gamma_beta : γ (R := R) q * β q = β q * γ q := (rel_bg q).symm

theorem gamma_beta_pow (b : ℕ) : γ (R := R) q * β q ^ b = β q ^ b * γ q := by
  have h : γ (R := R) q * β q = (1 : R) • (β q * γ q) := by rw [one_smul]; exact gamma_beta q
  simpa using pow_comm_of h b

theorem zeta_mul_pow (b c : ℕ) :
    zeta (R := R) q * (β q ^ b * γ q ^ c) = β q ^ (b + 1) * γ q ^ (c + 1) := by
  rw [zeta, mul_assoc, ← mul_assoc (γ q), gamma_beta_pow, mul_assoc, ← pow_succ',
    ← mul_assoc, ← pow_succ']

theorem zeta_delta_pow (n : ℕ) :
    zeta (R := R) q * δ q ^ n = (q : R) ^ (2 * n) • (δ q ^ n * zeta q) := by
  rw [zeta, mul_assoc, pow_comm_of (gamma_delta q), mul_smul_comm, ← mul_assoc,
    pow_comm_of (beta_delta q), smul_mul_assoc, smul_smul, mul_assoc, ← pow_add]
  ring_nf

theorem zeta_alpha_pow (n : ℕ) :
    zeta (R := R) q * α q ^ n = ((q⁻¹ : Rˣ) : R) ^ (2 * n) • (α q ^ n * zeta q) := by
  rw [zeta, mul_assoc, pow_comm_of (gamma_alpha q), mul_smul_comm, ← mul_assoc,
    pow_comm_of (beta_alpha q), smul_mul_assoc, smul_smul, mul_assoc, ← pow_add]
  ring_nf

theorem alpha_delta_pow_succ (n : ℕ) :
    α q * δ (R := R) q ^ (n + 1) = δ q ^ n + (q : R) ^ (2 * n + 1) • (δ q ^ n * zeta q) := by
  rw [pow_succ', ← mul_assoc, det_left', add_mul, one_mul, smul_mul_assoc, zeta_delta_pow,
    smul_smul, ← pow_succ']

theorem delta_alpha_pow_succ (n : ℕ) :
    δ q * α (R := R) q ^ (n + 1) =
      α q ^ n + ((q⁻¹ : Rˣ) : R) ^ (2 * n + 1) • (α q ^ n * zeta q) := by
  have hdr : δ q * α (R := R) q = 1 + ((q⁻¹ : Rˣ) : R) • zeta q := by
    rw [← rel_det_right q]; abel
  rw [pow_succ', ← mul_assoc, hdr, add_mul, one_mul, smul_mul_assoc, zeta_alpha_pow,
    smul_smul, ← pow_succ']

end Algebra

/-! ## Ordered monomials and the monomial map -/

section Mono

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- `α^n` for `n ≥ 0` and `δ^(-n)` for `n < 0`. -/
noncomputable def Apow : ℤ → OqSU2 R q
  | Int.ofNat n => α q ^ n
  | Int.negSucc n => δ q ^ (n + 1)

theorem Apow_nat (n : ℕ) : Apow q (n : ℤ) = α (R := R) q ^ n := rfl

theorem Apow_neg (n : ℕ) : Apow q (-(n : ℤ)) = δ (R := R) q ^ n := by
  cases n with
  | zero => simpa using Apow_nat q 0
  | succ n => rfl

/-- The ordered monomial `A_a β^b γ^c`. -/
noncomputable def mono (a : ℤ) (b c : ℕ) : OqSU2 R q := Apow q a * β q ^ b * γ q ^ c

/-- The monomial map `μ : e(a,b,c) ↦ A_a β^b γ^c`. -/
noncomputable def monoMap : MonoMod R →ₗ[R] OqSU2 R q :=
  linearCombination R fun I : MonoIdx => mono q I.1 I.2.1 I.2.2

@[simp] theorem monoMap_e (a : ℤ) (b c : ℕ) : monoMap q (eb R a b c) = mono q a b c := by
  simp [monoMap, linearCombination_single]

theorem monoMap_ext {f g : MonoMod R →ₗ[R] OqSU2 R q}
    (h : ∀ a b c, f (eb R a b c) = g (eb R a b c)) : f = g := by
  apply Finsupp.lhom_ext'
  rintro ⟨a, b, c⟩
  apply LinearMap.ext_ring
  exact h a b c

theorem qz_nat (n : ℕ) : qz q (n : ℤ) = (q : R) ^ n := by simp [qz]

theorem qz_neg_nat (n : ℕ) : qz q (-(n : ℤ)) = ((q⁻¹ : Rˣ) : R) ^ n := by
  simp [qz, zpow_neg]

theorem mono_nat (n : ℕ) (b c : ℕ) : mono q (n : ℤ) b c = α (R := R) q ^ n * β q ^ b * γ q ^ c := by
  rw [mono, Apow_nat]

theorem mono_neg (n : ℕ) (b c : ℕ) :
    mono q (-(n : ℤ)) b c = δ (R := R) q ^ n * β q ^ b * γ q ^ c := by
  rw [mono, Apow_neg]

theorem monoMap_mA (a : ℤ) (b c : ℕ) :
    monoMap q (mA q (eb R a b c)) = α q * mono q a b c := by
  obtain ⟨n, rfl | rfl⟩ := Int.eq_nat_or_neg a
  · rw [mA_e_nonneg q (by positivity), monoMap_e, show (n : ℤ) + 1 = ((n + 1 : ℕ) : ℤ) by push_cast; ring,
      mono_nat, mono_nat, pow_succ']
    simp only [mul_assoc]
  · cases n with
    | zero =>
      rw [mA_e_nonneg q (by simp), monoMap_e, show (-((0 : ℕ) : ℤ)) + 1 = ((1 : ℕ) : ℤ) by simp,
        mono_nat, mono_neg]
      simp [mul_assoc]
    | succ m =>
      rw [mA_e_neg q (by push_cast; omega), map_add, map_smul, monoMap_e, monoMap_e,
        show -((m + 1 : ℕ) : ℤ) + 1 = -(m : ℤ) by push_cast; ring,
        show -2 * -((m + 1 : ℕ) : ℤ) - 1 = ((2 * m + 1 : ℕ) : ℤ) by push_cast; ring,
        qz_nat, mono_neg, mono_neg, mono_neg, mul_assoc, mul_assoc, mul_assoc, ← mul_assoc (α q),
        alpha_delta_pow_succ, add_mul, smul_mul_assoc, mul_assoc, zeta_mul_pow]

theorem monoMap_mD (a : ℤ) (b c : ℕ) :
    monoMap q (mD q (eb R a b c)) = δ q * mono q a b c := by
  obtain ⟨n, rfl | rfl⟩ := Int.eq_nat_or_neg a
  · cases n with
    | zero =>
      rw [mD_e_nonpos q (by simp), monoMap_e, show ((0 : ℕ) : ℤ) - 1 = -((1 : ℕ) : ℤ) by simp,
        mono_neg, mono_nat]
      simp [mul_assoc]
    | succ m =>
      rw [mD_e_pos q (by push_cast; omega), map_add, map_smul, monoMap_e, monoMap_e,
        show ((m + 1 : ℕ) : ℤ) - 1 = (m : ℤ) by push_cast; ring,
        show 1 - 2 * ((m + 1 : ℕ) : ℤ) = -((2 * m + 1 : ℕ) : ℤ) by push_cast; ring,
        qz_neg_nat, mono_nat, mono_nat, mono_nat, mul_assoc, mul_assoc, mul_assoc, ← mul_assoc (δ q),
        delta_alpha_pow_succ, add_mul, smul_mul_assoc, mul_assoc, zeta_mul_pow]
  · rw [mD_e_nonpos q (by omega), monoMap_e, show -(n : ℤ) - 1 = -((n + 1 : ℕ) : ℤ) by push_cast; ring,
      mono_neg, mono_neg, pow_succ']
    simp only [mul_assoc]

theorem monoMap_mB (a : ℤ) (b c : ℕ) :
    monoMap q (mB q (eb R a b c)) = β q * mono q a b c := by
  rw [mB_e, map_smul, monoMap_e]
  obtain ⟨n, rfl | rfl⟩ := Int.eq_nat_or_neg a
  · rw [qz_neg_nat, mono_nat, mono_nat, ← mul_assoc, ← mul_assoc, pow_comm_of (beta_alpha q),
      smul_mul_assoc, smul_mul_assoc, pow_succ']
    simp only [mul_assoc]
  · rw [neg_neg, qz_nat, mono_neg, mono_neg, ← mul_assoc, ← mul_assoc, pow_comm_of (beta_delta q),
      smul_mul_assoc, smul_mul_assoc, pow_succ']
    simp only [mul_assoc]

theorem monoMap_mG (a : ℤ) (b c : ℕ) :
    monoMap q (mG q (eb R a b c)) = γ q * mono q a b c := by
  rw [mG_e, map_smul, monoMap_e]
  obtain ⟨n, rfl | rfl⟩ := Int.eq_nat_or_neg a
  · rw [qz_neg_nat, mono_nat, mono_nat, ← mul_assoc, ← mul_assoc, pow_comm_of (gamma_alpha q),
      smul_mul_assoc, smul_mul_assoc, mul_assoc _ (γ q), gamma_beta_pow, pow_succ']
    simp only [mul_assoc]
  · rw [neg_neg, qz_nat, mono_neg, mono_neg, ← mul_assoc, ← mul_assoc, pow_comm_of (gamma_delta q),
      smul_mul_assoc, smul_mul_assoc, mul_assoc _ (γ q), gamma_beta_pow, pow_succ']
    simp only [mul_assoc]

/-- **The monomial map inverts the cyclic vector map**: `μ(π(x) v) = x μ(v)`. -/
theorem monoMap_monoRep (x : OqSU2 R q) (v : MonoMod R) :
    monoMap q (monoRep q x v) = x * monoMap q v := by
  let S : Subalgebra R (OqSU2 R q) :=
    { carrier := {x | ∀ v, monoMap q (monoRep q x v) = x * monoMap q v}
      mul_mem' := by
        intro x y hx hy v
        simp only [Set.mem_setOf_eq] at *
        rw [map_mul, Module.End.mul_apply, hx, hy, mul_assoc]
      add_mem' := by
        intro x y hx hy v
        simp only [Set.mem_setOf_eq] at *
        rw [map_add, LinearMap.add_apply, map_add, hx, hy, add_mul]
      algebraMap_mem' := by
        intro r v
        rw [AlgHom.commutes, Module.algebraMap_end_apply, map_smul, Algebra.smul_def] }
  have gen : ∀ (g : OqSU2 R q) (T : Module.End R (MonoMod R)), monoRep q g = T →
      (∀ a b c, monoMap q (T (eb R a b c)) = g * mono q a b c) → g ∈ S := by
    intro g T hT h v
    rw [hT]
    have : (monoMap q).comp T = (LinearMap.mulLeft R g).comp (monoMap q) :=
      monoMap_ext q fun a b c => by simpa using h a b c
    exact LinearMap.congr_fun this v
  exact mem_of_gens S (gen _ _ (by simp [monoRep]) (monoMap_mA q))
    (gen _ _ (by simp [monoRep]) (monoMap_mB q)) (gen _ _ (by simp [monoRep]) (monoMap_mG q))
    (gen _ _ (by simp [monoRep]) (monoMap_mD q)) x v

theorem monoMap_e000 : monoMap q (eb R 0 0 0) = 1 := by
  simp [mono, Apow]

/-- Every element is recovered from its cyclic vector: `x = μ(π(x) e₀)`. -/
theorem monoMap_cyclic (x : OqSU2 R q) : monoMap q (monoRep q x (eb R 0 0 0)) = x := by
  rw [monoMap_monoRep, monoMap_e000, mul_one]

end Mono

/-! ## The star of a monomial and the Haar values `h(m* m')` -/

section Values

variable {R : Type*} [CommRing R] (q : Rˣ)

theorem compactStar_pow (x : OqSU2 R q) (n : ℕ) :
    compactStar q (x ^ n) = compactStar q x ^ n := by
  induction n with
  | zero => simpa using compactStar_one q
  | succ n ih => rw [pow_succ, compactStar_mul, ih, pow_succ']

theorem commute_beta_gamma : Commute (β (R := R) q) (γ q) := rel_bg q

theorem commute_beta_DA (n : ℕ) : Commute (β (R := R) q) (δ q ^ n * α q ^ n) := by
  show β q * (δ q ^ n * α q ^ n) = δ q ^ n * α q ^ n * β q
  rw [← mul_assoc, pow_comm_of (beta_delta q), smul_mul_assoc, mul_assoc,
    pow_comm_of (beta_alpha q), mul_smul_comm, smul_smul, ← mul_pow, ← Units.val_mul,
    mul_inv_cancel, Units.val_one, one_pow, one_smul, mul_assoc]

theorem commute_gamma_DA (n : ℕ) : Commute (γ (R := R) q) (δ q ^ n * α q ^ n) := by
  show γ q * (δ q ^ n * α q ^ n) = δ q ^ n * α q ^ n * γ q
  rw [← mul_assoc, pow_comm_of (gamma_delta q), smul_mul_assoc, mul_assoc,
    pow_comm_of (gamma_alpha q), mul_smul_comm, smul_smul, ← mul_pow, ← Units.val_mul,
    mul_inv_cancel, Units.val_one, one_pow, one_smul, mul_assoc]

theorem commute_beta_AD (n : ℕ) : Commute (β (R := R) q) (α q ^ n * δ q ^ n) := by
  show β q * (α q ^ n * δ q ^ n) = α q ^ n * δ q ^ n * β q
  rw [← mul_assoc, pow_comm_of (beta_alpha q), smul_mul_assoc, mul_assoc,
    pow_comm_of (beta_delta q), mul_smul_comm, smul_smul, ← mul_pow, ← Units.val_mul,
    inv_mul_cancel, Units.val_one, one_pow, one_smul, mul_assoc]

theorem commute_gamma_AD (n : ℕ) : Commute (γ (R := R) q) (α q ^ n * δ q ^ n) := by
  show γ q * (α q ^ n * δ q ^ n) = α q ^ n * δ q ^ n * γ q
  rw [← mul_assoc, pow_comm_of (gamma_alpha q), smul_mul_assoc, mul_assoc,
    pow_comm_of (gamma_delta q), mul_smul_comm, smul_smul, ← mul_pow, ← Units.val_mul,
    inv_mul_cancel, Units.val_one, one_pow, one_smul, mul_assoc]

/-- `A_a^* A_a`: `δ^n α^n` for `a = n ≥ 0`, `α^n δ^n` for `a = -n`. -/
noncomputable def normSq : ℤ → OqSU2 R q
  | Int.ofNat n => δ q ^ n * α q ^ n
  | Int.negSucc n => α q ^ (n + 1) * δ q ^ (n + 1)

theorem compactStar_Apow_mul (a : ℤ) :
    compactStar q (Apow q a) * Apow q a = normSq (R := R) q a := by
  cases a with
  | ofNat n => simp [Apow, normSq, compactStar_pow]
  | negSucc n => simp [Apow, normSq, compactStar_pow]

theorem commute_beta_normSq (a : ℤ) : Commute (β (R := R) q) (normSq q a) := by
  cases a with
  | ofNat n => exact commute_beta_DA q n
  | negSucc n => exact commute_beta_AD q (n + 1)

theorem commute_gamma_normSq (a : ℤ) : Commute (γ (R := R) q) (normSq q a) := by
  cases a with
  | ofNat n => exact commute_gamma_DA q n
  | negSucc n => exact commute_gamma_AD q (n + 1)

/-- `m(a,b,c)^* m(a,b',c') = (-q⁻¹)^c (-q)^b · A_a^*A_a · ζ^(b+c')` when `b + c' = c + b'`. -/
theorem star_mono_mul_mono (a : ℤ) (b c b' c' : ℕ) (h : b + c' = c + b') :
    compactStar q (mono q a b c) * mono q a b' c' =
      ((-((q⁻¹ : Rˣ) : R)) ^ c * (-(q : R)) ^ b) • (normSq q a * zeta q ^ (b + c')) := by
  have hN := compactStar_Apow_mul q a
  have hk : c + b' = b + c' := by omega
  rw [mono, mono, compactStar_mul, compactStar_mul, compactStar_pow, compactStar_pow,
    compactStar_beta, compactStar_gamma, smul_pow, smul_pow]
  -- `(s β)^c ((t γ)^b A*) (A β^b' γ^c')`
  have e : β q ^ c * (γ q ^ b * compactStar q (Apow q a)) * (Apow q a * β q ^ b' * γ q ^ c') =
      normSq q a * zeta q ^ (b + c') := by
    calc β q ^ c * (γ q ^ b * compactStar q (Apow q a)) * (Apow q a * β q ^ b' * γ q ^ c')
        = β q ^ c * γ q ^ b * normSq q a * β q ^ b' * γ q ^ c' := by
          rw [← hN]; simp only [mul_assoc]
      _ = normSq q a * (β q ^ c * (γ q ^ b * β q ^ b') * γ q ^ c') := by
          rw [mul_assoc (β q ^ c) (γ q ^ b), ((commute_gamma_normSq q a).pow_left b).eq,
            ← mul_assoc,
            ((commute_beta_normSq q a).pow_left c).eq]
          simp only [mul_assoc]
      _ = normSq q a * (β q ^ (c + b') * γ q ^ (b + c')) := by
          rw [((commute_beta_gamma q).pow_pow b' b).eq.symm, ← mul_assoc (β q ^ c), ← pow_add,
            mul_assoc, ← pow_add]
      _ = normSq q a * zeta q ^ (b + c') := by
          rw [hk, zeta, (commute_beta_gamma q).mul_pow]
  simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
  rw [e]
  congr 1
  ring

end Values

/-! ## Haar values on monomials -/

/-- Decide an identity between products of (integer or natural) powers of units. -/
macro "units_ac'" : tactic =>
  `(tactic| (apply Additive.ofMul.injective <;>
    simp only [ofMul_mul, ofMul_zpow, ofMul_pow, ofMul_inv, Nat.cast_add, Nat.cast_one,
      Nat.cast_zero] <;>
    module))

section HaarValues

variable {R : Type*} [CommRing R] (q : Rˣ)

theorem monoRep_zeta_pow (k b c : ℕ) :
    monoRep q (zeta q ^ k) (eb R 0 b c) = eb R 0 (b + k) (c + k) := by
  induction k generalizing b c with
  | zero => simp
  | succ k ih =>
    rw [pow_succ, map_mul, Module.End.mul_apply]
    have : monoRep q (zeta (R := R) q) (eb R 0 b c) = eb R 0 (b + 1) (c + 1) := by
      simp [zeta, monoRep, Module.End.mul_apply]
    rw [this, ih, Nat.add_right_comm b, Nat.add_right_comm c]; rfl

theorem zeroWeight_zeta_pow (lam : ℕ → R) (k : ℕ) :
    zeroWeightFunctional q lam (zeta q ^ k) = lam k := by
  rw [zeroWeightFunctional_apply, monoRep_zeta_pow]
  simp

theorem normSq_nat (n : ℕ) : normSq q (n : ℤ) = δ (R := R) q ^ n * α q ^ n := rfl

theorem normSq_neg (n : ℕ) : normSq q (-(n : ℤ)) = α (R := R) q ^ n * δ q ^ n := by
  cases n with
  | zero => simpa using normSq_nat q 0
  | succ n => rfl

/-- `T_{u,v}` scales the monomial `m(a,b,c)` by `u^a v^(b-c)`. -/
theorem torus_mono (u v : Rˣ) (a : ℤ) (b c : ℕ) :
    torusScaleAlgHom q u v (mono q a b c) = ((u ^ a * v ^ ((b : ℤ) - c) : Rˣ) : R) • mono q a b c := by
  cases a with
  | ofNat n =>
    simp only [mono, Apow, map_mul, map_pow, torusScaleAlgHom, liftQuadruple_alpha,
      liftQuadruple_beta, liftQuadruple_gamma, smul_pow, smul_mul_smul_comm]
    congr 1
    simp only [← Units.val_pow_eq_pow_val, ← Units.val_mul]
    congr 1
    simp only [Int.ofNat_eq_coe]
    units_ac'
  | negSucc n =>
    simp only [mono, Apow, map_mul, map_pow, torusScaleAlgHom, liftQuadruple_delta,
      liftQuadruple_beta, liftQuadruple_gamma, smul_pow, smul_mul_smul_comm]
    congr 1
    simp only [← Units.val_pow_eq_pow_val, ← Units.val_mul]
    congr 1
    simp only [Int.negSucc_eq]
    units_ac'

end HaarValues

/-! ## Haar values over a field -/

section FieldValues

open HaarKernel

variable {K : Type*} [Field K] (q : Kˣ)

theorem haarMoment_eq_lamQ (hq2 : (q : K) ^ 2 ≠ 1) (k : ℕ) :
    haarMoment q k = lamQ (q : K) k := by
  have hg : qSqNum q k * (1 - (q : K) ^ 2) = 1 - (q : K) ^ (2 * (k + 1)) := by
    have := geom_sum_mul ((q : K) ^ 2) (k + 1)
    simp only [← pow_mul] at this
    rw [qSqNum]
    linear_combination -this
  have h1 : (1 : K) - (q : K) ^ 2 ≠ 0 := sub_ne_zero.2 (Ne.symm hq2)
  rw [haarMoment, lamQ, ← hg, mul_comm (qSqNum q k), mul_div_mul_left _ _ h1]

theorem haarState_zeta_pow (k : ℕ) : haarState q (zeta q ^ k) = haarMoment q k :=
  zeroWeight_zeta_pow q _ k

theorem haarState_normSq_nat (hq2 : (q : K) ^ 2 ≠ 1) (n k : ℕ) :
    haarState q (normSq q (n : ℤ) * zeta q ^ k) = GW (q : K) n k := by
  induction n generalizing k with
  | zero =>
    rw [normSq_nat]; simp only [pow_zero, one_mul]
    rw [haarState_zeta_pow, haarMoment_eq_lamQ q hq2]; rfl
  | succ n ih =>
    have key : normSq q ((n + 1 : ℕ) : ℤ) * zeta q ^ k = normSq q (n : ℤ) * zeta q ^ k +
        ((q⁻¹ : Kˣ) : K) ^ (2 * n + 1) • (normSq q (n : ℤ) * zeta q ^ (k + 1)) := by
      rw [normSq_nat, normSq_nat, pow_succ (δ q), mul_assoc (δ q ^ n), delta_alpha_pow_succ,
        mul_add, mul_smul_comm, add_mul, smul_mul_assoc, pow_succ' (zeta q) k]
      simp only [mul_assoc]
    rw [key, map_add, map_smul, ih, ih, GW, smul_eq_mul, Units.val_inv_eq_inv_val, inv_pow]

theorem haarState_normSq_neg (hq2 : (q : K) ^ 2 ≠ 1) (n k : ℕ) :
    haarState q (normSq q (-(n : ℤ)) * zeta q ^ k) = GV (q : K) n k := by
  induction n generalizing k with
  | zero =>
    rw [normSq_neg]; simp only [pow_zero, one_mul]
    rw [haarState_zeta_pow, haarMoment_eq_lamQ q hq2]; rfl
  | succ n ih =>
    have key : normSq q (-((n + 1 : ℕ) : ℤ)) * zeta q ^ k = normSq q (-(n : ℤ)) * zeta q ^ k +
        (q : K) ^ (2 * n + 1) • (normSq q (-(n : ℤ)) * zeta q ^ (k + 1)) := by
      rw [normSq_neg, normSq_neg, pow_succ (α q), mul_assoc (α q ^ n), alpha_delta_pow_succ,
        mul_add, mul_smul_comm, add_mul, smul_mul_assoc, pow_succ' (zeta q) k]
      simp only [mul_assoc]
    rw [key, map_add, map_smul, ih, ih, GV, smul_eq_mul]

end FieldValues

/-! ## Orthogonality of weights and the quadratic-form expansion -/

section Ordered

open HaarKernel PickSOS Finset

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (q : Kˣ)

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- `T_{u,v}` scales `m(a,b,c)^* m(a',b',c')` by `u^(a'-a) v^((b'-c')-(b-c))`. -/
theorem torus_star_mono_mul (u v : Kˣ) (a : ℤ) (b c : ℕ) (a' : ℤ) (b' c' : ℕ) :
    torusScaleAlgHom q u v (compactStar q (mono q a b c) * mono q a' b' c') =
      ((u ^ (a' - a) * v ^ (((b' : ℤ) - c') - ((b : ℤ) - c)) : Kˣ) : K) •
        (compactStar q (mono q a b c) * mono q a' b' c') := by
  have h := compactStar_torusScale q u⁻¹ v⁻¹ (mono q a b c)
  rw [inv_inv, inv_inv] at h
  rw [map_mul, ← h, torus_mono, torus_mono, map_smul, smul_mul_assoc, mul_smul_comm, smul_smul,
    ← Units.val_mul]
  congr 2
  units_ac'

theorem two_zpow_ne_one {z : ℤ} (hz : z ≠ 0) : ((Units.mk0 (2 : K) two_ne_zero ^ z : Kˣ) : K) ≠ 1 := by
  rw [Units.val_zpow_eq_zpow_val, Units.val_mk0]
  intro h
  exact hz ((zpow_eq_one_iff_right₀ zero_le_two (by norm_num)).1 h)

/-- **Weight orthogonality**: `h(m^* m') = 0` unless the two monomials have the same weight. -/
theorem haarState_star_mono_mul_ne (a : ℤ) (b c : ℕ) (a' : ℤ) (b' c' : ℕ)
    (hne : (a, (b : ℤ) - c) ≠ (a', (b' : ℤ) - c')) :
    haarState q (compactStar q (mono q a b c) * mono q a' b' c') = 0 := by
  set X := compactStar q (mono q a b c) * mono q a' b' c'
  have key : ∀ u v : Kˣ, haarState q X =
      ((u ^ (a' - a) * v ^ (((b' : ℤ) - c') - ((b : ℤ) - c)) : Kˣ) : K) * haarState q X := by
    intro u v
    rw [← smul_eq_mul, ← map_smul, ← torus_star_mono_mul, haarState_torus]
  let two : Kˣ := Units.mk0 2 two_ne_zero
  by_cases ha : a = a'
  · subst ha
    have hn : ((b' : ℤ) - c') - ((b : ℤ) - c) ≠ 0 := by
      intro h; apply hne; ext <;> simp; omega
    have := key 1 two
    simp only [one_zpow, one_mul] at this
    have h2 := two_zpow_ne_one (K := K) hn
    have : (1 - ((two ^ (((b' : ℤ) - c') - ((b : ℤ) - c)) : Kˣ) : K)) * haarState q X = 0 := by
      rw [sub_mul, one_mul, ← this, sub_self]
    exact (mul_eq_zero.1 this).resolve_left (sub_ne_zero.2 h2.symm)
  · have hn : a' - a ≠ 0 := sub_ne_zero.2 (Ne.symm ha)
    have := key two 1
    simp only [one_zpow, mul_one] at this
    have h2 := two_zpow_ne_one (K := K) hn
    have : (1 - ((two ^ (a' - a) : Kˣ) : K)) * haarState q X = 0 := by
      rw [sub_mul, one_mul, ← this, sub_self]
    exact (mul_eq_zero.1 this).resolve_left (sub_ne_zero.2 h2.symm)

/-- The Gram kernel of the monomials. -/
noncomputable def gram (I J : MonoIdx) : K :=
  haarState q (compactStar q (mono q I.1 I.2.1 I.2.2) * mono q J.1 J.2.1 J.2.2)

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- `h(μ(v)^* μ(v)) = ∑ v_I v_J h(m_I^* m_J)`. -/
theorem haarState_star_monoMap (v : MonoMod K) :
    haarState q (compactStar q (monoMap q v) * monoMap q v) =
      ∑ I ∈ v.support, ∑ J ∈ v.support, v I * v J * gram q I J := by
  simp only [monoMap, linearCombination_apply, Finsupp.sum, map_sum, map_smul, sum_mul_sum,
    smul_mul_assoc, mul_smul_comm, smul_smul, smul_eq_mul, gram]
  refine sum_congr rfl fun I _ => sum_congr rfl fun J _ => ?_
  ring

end Ordered

/-! ## The Gram kernel is a weighted sum of squares; positivity for `0 < q < 1` -/

section Positivity

open HaarKernel PickSOS Finset

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (q : Kˣ)

/-- Number of Pick factors of the weight-`a` block. -/
def blkA : ℤ → ℕ
  | Int.ofNat n => n + 1
  | Int.negSucc d => d + 2

/-- The positive constant of the weight-`a` block. -/
noncomputable def blkC : ℤ → K
  | Int.ofNat n => (1 - (q : K) ^ 2) * (q : K) ^ (2 * n) * pochQ (q : K) n
  | Int.negSucc d => (1 - (q : K) ^ 2) * pochQ (q : K) (d + 1)

/-- The scale `r ≥ 0` of the weight-`a` block (`ρ = -q r`). -/
noncomputable def blkR : ℤ → K
  | Int.ofNat n => (q : K) ^ (2 * n)
  | Int.negSucc _ => 1

section
variable {q}
variable (hq0 : 0 < (q : K)) (hq1 : (q : K) < 1)
include hq0 hq1

theorem blkC_nonneg (a : ℤ) : 0 ≤ blkC q a := by
  have h1 : 0 < 1 - (q : K) ^ 2 := one_sub_pow_pos hq0 hq1 (by norm_num)
  cases a with
  | ofNat n => exact (mul_pos (mul_pos h1 (pow_pos hq0 _)) (pochQ_pos hq0 hq1 n)).le
  | negSucc d => exact (mul_pos h1 (pochQ_pos hq0 hq1 _)).le

omit hq1 in
theorem blkR_nonneg (a : ℤ) : 0 ≤ blkR q a := by
  cases a with
  | ofNat n => exact (pow_pos hq0 _).le
  | negSucc d => exact zero_le_one

theorem haarState_normSq (a : ℤ) (k : ℕ) :
    haarState q (normSq q a * zeta q ^ k) =
      blkC q a * (-(q : K) * blkR q a) ^ k / denQ (q : K) (blkA a) k := by
  have hq2 : (q : K) ^ 2 ≠ 1 := (pow_lt_one₀ hq0.le hq1 (by norm_num)).ne
  cases a with
  | ofNat n =>
    rw [Int.ofNat_eq_coe, haarState_normSq_nat q hq2, GW_closed hq0 hq1]
    simp only [blkC, blkR, blkA, mul_pow, ← pow_mul]
    ring_nf
  | negSucc d =>
    have e : Int.negSucc d = -((d + 1 : ℕ) : ℤ) := by rw [Int.negSucc_eq]; push_cast; ring
    have h := haarState_normSq_neg q hq2 (d + 1) k
    rw [← e] at h
    rw [h, GV_closed hq0 hq1]
    simp only [blkC, blkR, blkA, mul_one]
end

/-- The sign-and-power prefactor of a weight-`n` block. -/
noncomputable def blkP (n : ℤ) : K :=
  if 0 ≤ n then (-(q : K)) ^ n.natAbs else (-((q⁻¹ : Kˣ) : K)) ^ n.natAbs

theorem prefactor (C ρ : K) (D : ℕ → K) (b c b' c' : ℕ) (n : ℤ) (hn : (b : ℤ) - c = n)
    (hn' : (b' : ℤ) - c' = n) :
    (-((q⁻¹ : Kˣ) : K)) ^ c * (-(q : K)) ^ b * (C * ρ ^ (b + c') / D (b + c')) =
      blkP q n * C * ρ ^ n.natAbs * ρ ^ (min b c + min b' c') /
        D (min b c + min b' c' + n.natAbs) := by
  have hinv : (-((q⁻¹ : Kˣ) : K)) * (-(q : K)) = 1 := by
    rw [neg_mul_neg, ← Units.val_mul, inv_mul_cancel, Units.val_one]
  rcases le_total c b with hcb | hbc
  · obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hcb
    have hb' : b' = c' + t := by omega
    subst hb'
    have hnt : n = t := by omega
    subst hnt
    have e1 : min (c + t) c = c := by omega
    have e2 : min (c' + t) c' = c' := by omega
    rw [e1, e2, Int.natAbs_natCast, blkP, if_pos (by positivity),
      show c + t + c' = c + c' + t by ring, Int.natAbs_natCast]
    have : (-((q⁻¹ : Kˣ) : K)) ^ c * (-(q : K)) ^ (c + t) = (-(q : K)) ^ t := by
      rw [pow_add, ← mul_assoc, ← mul_pow, hinv, one_pow, one_mul]
    rw [this, pow_add ρ (c + c') t]
    ring
  · obtain ⟨t, rfl⟩ := Nat.exists_eq_add_of_le hbc
    have hc' : c' = b' + t := by omega
    subst hc'
    have hnt : n = -(t : ℤ) := by omega
    subst hnt
    have e1 : min b (b + t) = b := by omega
    have e2 : min b' (b' + t) = b' := by omega
    rw [e1, e2, Int.natAbs_neg, Int.natAbs_natCast, show b + (b' + t) = b + b' + t by ring]
    have : (-((q⁻¹ : Kˣ) : K)) ^ (b + t) * (-(q : K)) ^ b = (-((q⁻¹ : Kˣ) : K)) ^ t := by
      rw [pow_add, mul_right_comm, ← mul_pow, hinv, one_pow, one_mul]
    rw [this, pow_add ρ (b + b') t, blkP]
    split_ifs with h0
    · have : t = 0 := by omega
      subst this; simp
    · simp only [Int.natAbs_neg, Int.natAbs_natCast]; ring

theorem blkP_mul_nonneg (hq0 : 0 < (q : K)) (n : ℤ) {r : K} (hr : 0 ≤ r) :
    0 ≤ blkP q n * (-(q : K) * r) ^ n.natAbs := by
  have hinv : (-((q⁻¹ : Kˣ) : K)) * (-(q : K)) = 1 := by
    rw [neg_mul_neg, ← Units.val_mul, inv_mul_cancel, Units.val_one]
  rw [blkP]
  split_ifs
  · rw [← mul_pow]
    apply pow_nonneg
    rw [show -(q : K) * (-(q : K) * r) = (q : K) ^ 2 * r by ring]
    positivity
  · rw [← mul_pow, ← mul_assoc, hinv, one_mul]
    exact pow_nonneg hr _

/-- **The Gram kernel of the ordered monomials is a weighted sum of squares** (`0 < q < 1`). -/
theorem gram_isWSOS (hq0 : 0 < (q : K)) (hq1 : (q : K) < 1) (s : Finset MonoIdx) :
    IsWSOS s (gram q) := by
  classical
  refine IsWSOS.of_blocks (fun I : MonoIdx => (I.1, (I.2.1 : ℤ) - I.2.2)) ?_ ?_
  · rintro ⟨a, b, c⟩ - ⟨a', b', c'⟩ - hne
    exact haarState_star_mono_mul_ne q a b c a' b' c' hne
  · rintro ⟨a, n⟩ -
    set ρ := -(q : K) * blkR q a
    have hc₀ : 0 ≤ blkP q n * blkC q a * ρ ^ n.natAbs := by
      rw [mul_right_comm]
      exact mul_nonneg (blkP_mul_nonneg q hq0 n (blkR_nonneg hq0 a)) (blkC_nonneg hq0 hq1 a)
    refine IsWSOS.comap (fun I : MonoIdx => min I.2.1 I.2.2)
      (isWSOS_qPick hq0 hq1 _ (blkA a) n.natAbs ρ hc₀) ?_
    rintro ⟨a₁, b, c⟩ hI ⟨a₂, b', c'⟩ hJ
    simp only [mem_filter, Prod.mk.injEq] at hI hJ
    obtain ⟨-, rfl, hn⟩ := hI
    obtain ⟨-, rfl, hn'⟩ := hJ
    have hbc : b + c' = c + b' := by omega
    dsimp only
    rw [gram, star_mono_mul_mono q a₂ b c b' c' hbc, map_smul, smul_eq_mul,
      haarState_normSq hq0 hq1, prefactor q _ _ _ b c b' c' n hn hn']

/-- **Positivity of the Haar state** for `0 < q < 1`: `h(x^* x) ≥ 0` for every `x`. -/
theorem haarState_star_mul_self_nonneg_of_lt_one (hq0 : 0 < (q : K)) (hq1 : (q : K) < 1)
    (x : OqSU2 K q) : 0 ≤ haarState q (compactStar q x * x) := by
  rw [← monoMap_cyclic q x, haarState_star_monoMap]
  exact (gram_isWSOS q hq0 hq1 _).quadForm_nonneg _

end Positivity

/-! ## The inversion `*`-isomorphism `O_q(SU(2)) → O_{q⁻¹}(SU(2))` -/

section Inversion

variable {R : Type*} [CommRing R] (q : Rˣ)

private theorem smul_inv_cancel_of_eq {x y : OqSU2 R q⁻¹} (h : x = ((q⁻¹ : Rˣ) : R) • y) :
    y = (q : R) • x := by
  rw [h, smul_smul, ← Units.val_mul, mul_inv_cancel, Units.val_one, one_smul]

/-- The images `δ', qβ', q⁻¹γ', α'` satisfy the relations of `O_q(SU(2))`. -/
theorem isOqSU2Quadruple_inv :
    IsOqSU2Quadruple (R := R) q (δ q⁻¹) ((q : R) • β q⁻¹) (((q⁻¹ : Rˣ) : R) • γ q⁻¹)
      (α q⁻¹) := by
  have h1 : δ (R := R) q⁻¹ * β q⁻¹ = (q : R) • (β q⁻¹ * δ q⁻¹) :=
    smul_inv_cancel_of_eq q (rel_bd q⁻¹)
  have h2 : δ (R := R) q⁻¹ * γ q⁻¹ = (q : R) • (γ q⁻¹ * δ q⁻¹) :=
    smul_inv_cancel_of_eq q (rel_gd q⁻¹)
  have h3 : β (R := R) q⁻¹ * α q⁻¹ = (q : R) • (α q⁻¹ * β q⁻¹) :=
    smul_inv_cancel_of_eq q (rel_ab q⁻¹)
  have h4 : γ (R := R) q⁻¹ * α q⁻¹ = (q : R) • (α q⁻¹ * γ q⁻¹) :=
    smul_inv_cancel_of_eq q (rel_ag q⁻¹)
  have hu : ((q : R) * ((q⁻¹ : Rˣ) : R)) = 1 := by
    rw [← Units.val_mul, mul_inv_cancel, Units.val_one]
  have hu' : (((q⁻¹ : Rˣ) : R) * (q : R)) = 1 := by
    rw [← Units.val_mul, inv_mul_cancel, Units.val_one]
  constructor
  · rw [mul_smul_comm, h1, smul_mul_assoc]
  · rw [mul_smul_comm, h2, smul_mul_assoc, smul_comm]
  · rw [smul_mul_assoc, h3, mul_smul_comm]
  · rw [smul_mul_assoc, h4, mul_smul_comm, smul_comm]
  · rw [smul_mul_assoc, mul_smul_comm, smul_mul_assoc, mul_smul_comm, rel_bg, smul_comm]
  · have := rel_det_right (R := R) q⁻¹
    rw [inv_inv] at this
    rw [smul_mul_assoc, mul_smul_comm, smul_smul, smul_smul, mul_assoc, hu, mul_one]
    exact this
  · have := rel_det_left (R := R) q⁻¹
    rw [smul_mul_assoc, mul_smul_comm, smul_smul, smul_smul, hu', one_mul]
    exact this

/-- **The inversion isomorphism** `φ : O_q → O_{q⁻¹}`,
`α ↦ δ', β ↦ qβ', γ ↦ q⁻¹γ', δ ↦ α'`. -/
noncomputable def invHom : OqSU2 R q →ₐ[R] OqSU2 R q⁻¹ :=
  liftQuadruple q _ _ _ _ (isOqSU2Quadruple_inv q)

@[simp] theorem invHom_alpha : invHom q (α (R := R) q) = δ q⁻¹ := by simp [invHom]
@[simp] theorem invHom_beta : invHom q (β (R := R) q) = (q : R) • β q⁻¹ := by simp [invHom]
@[simp] theorem invHom_gamma :
    invHom q (γ (R := R) q) = ((q⁻¹ : Rˣ) : R) • γ q⁻¹ := by simp [invHom]
@[simp] theorem invHom_delta : invHom q (δ (R := R) q) = α q⁻¹ := by simp [invHom]

/-- `φ` intertwines the stars of `O_q` and `O_{q⁻¹}`. -/
theorem invHom_compactStar (x : OqSU2 R q) :
    invHom q (compactStar q x) = compactStar q⁻¹ (invHom q x) := by
  have hu : ((q : R) * ((q⁻¹ : Rˣ) : R)) = 1 := by
    rw [← Units.val_mul, mul_inv_cancel, Units.val_one]
  have hu' : (((q⁻¹ : Rˣ) : R) * (q : R)) = 1 := by
    rw [← Units.val_mul, inv_mul_cancel, Units.val_one]
  induction x using induction_gen with
  | hα => simp
  | hβ => simp [smul_smul, hu]
  | hγ => simp [smul_smul, hu']
  | hδ => simp
  | halg r => simp [compactStar_algebraMap]
  | hadd x y hx hy => simp only [map_add, hx, hy]
  | hmul x y hx hy => rw [compactStar_mul, map_mul, map_mul, hx, hy, compactStar_mul]

theorem invHom_Apow (a : ℤ) : invHom q (Apow (R := R) q a) = Apow q⁻¹ (-a) := by
  cases a with
  | ofNat n =>
    rw [Int.ofNat_eq_coe, Apow_nat, map_pow, invHom_alpha, Apow_neg]
  | negSucc n =>
    rw [Int.neg_negSucc]
    show invHom q (δ q ^ (n + 1)) = Apow q⁻¹ ((n + 1 : ℕ) : ℤ)
    rw [map_pow, invHom_delta, Apow_nat]

theorem invHom_mono (a : ℤ) (b c : ℕ) :
    invHom q (mono (R := R) q a b c) =
      ((q : R) ^ b * ((q⁻¹ : Rˣ) : R) ^ c) • mono q⁻¹ (-a) b c := by
  rw [mono, mono, map_mul, map_mul, map_pow, map_pow, invHom_Apow, invHom_beta, invHom_gamma,
    smul_pow, smul_pow, mul_smul_comm, mul_smul_comm, smul_mul_assoc, smul_smul,
    mul_comm (((q⁻¹ : Rˣ) : R) ^ c)]

end Inversion

/-! ## Positivity for every `q > 0`, `q ≠ 1` -/

section AllQ

open HaarKernel

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (q : Kˣ)

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem qSqNum_inv (k : ℕ) : qSqNum q⁻¹ k * (q : K) ^ (2 * k) = qSqNum q k := by
  have hq : (q : K) ≠ 0 := q.ne_zero
  induction k with
  | zero => simp [qSqNum]
  | succ k ih =>
    rw [qSqNum_succ, qSqNum_succ', ← ih, Units.val_inv_eq_inv_val, add_mul, ← mul_pow,
      inv_mul_cancel₀ hq, one_pow]
    ring

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- The Haar moments are symmetric under `q ↦ q⁻¹`. -/
theorem haarMoment_inv (k : ℕ) : haarMoment q⁻¹ k = haarMoment q k := by
  have hq : (q : K) ≠ 0 := q.ne_zero
  rw [haarMoment, haarMoment, ← qSqNum_inv q k, mul_comm, ← div_div, pow_mul, ← div_pow,
    Units.val_inv_eq_inv_val]
  congr 2
  field_simp

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem Apow_zero : Apow (R := K) q 0 = 1 := pow_zero _

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem zeta_pow_eq (b : ℕ) : zeta (R := K) q ^ b = β q ^ b * γ q ^ b := by
  induction b with
  | zero => simp
  | succ b ih => rw [pow_succ', ih, zeta_mul_pow]

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem mono_zero_zero : mono (R := K) q 0 0 0 = 1 := by
  simp [mono, Apow_zero q]

/-- The Haar state on an ordered monomial. -/
theorem haarState_mono (a : ℤ) (b c : ℕ) :
    haarState q (mono q a b c) = if a = 0 ∧ b = c then haarMoment q b else 0 := by
  split_ifs with h
  · obtain ⟨rfl, rfl⟩ := h
    rw [mono, Apow_zero q, one_mul, ← zeta_pow_eq,
      haarState_zeta_pow]
  · have := haarState_star_mono_mul_ne q 0 0 0 a b c (by
      intro h'; simp only [Prod.mk.injEq] at h'; apply h; omega)
    rwa [mono_zero_zero, compactStar_one, one_mul] at this

/-- **`h_q = h_{q⁻¹} ∘ φ`.** -/
theorem haarState_invHom (x : OqSU2 K q) : haarState q⁻¹ (invHom q x) = haarState q x := by
  rw [← monoMap_cyclic q x]
  generalize monoRep q x (eb K 0 0 0) = v
  induction v using Finsupp.induction_linear with
  | zero => simp
  | add v w hv hw => simp only [map_add, hv, hw]
  | single I r =>
    obtain ⟨a, b, c⟩ := I
    rw [show Finsupp.single (a, b, c) r = r • eb K a b c by simp, map_smul, monoMap_e, map_smul,
      map_smul, invHom_mono, map_smul, haarState_mono, map_smul, haarState_mono]
    simp only [neg_eq_zero, smul_eq_mul]
    split_ifs with h
    · obtain ⟨rfl, rfl⟩ := h
      rw [haarMoment_inv, ← mul_pow, Units.mul_inv, one_pow, one_mul]
    · simp

/-- **Positivity of the Haar state** for `q > 1`, by transport along `φ`. -/
theorem haarState_star_mul_self_nonneg_of_one_lt (hq1 : 1 < (q : K))
    (x : OqSU2 K q) : 0 ≤ haarState q (compactStar q x * x) := by
  have hq0 : 0 < (q : K) := zero_lt_one.trans hq1
  rw [← haarState_invHom, map_mul, invHom_compactStar]
  refine haarState_star_mul_self_nonneg_of_lt_one q⁻¹ ?_ ?_ _
  · rw [Units.val_inv_eq_inv_val]; exact inv_pos.2 hq0
  · rw [Units.val_inv_eq_inv_val]; exact inv_lt_one_of_one_lt₀ hq1

/-- **Positivity of the Haar state on `O_q(SU(2))`** for every `q > 0`, `q ≠ 1`,
over any linearly ordered field: `h(x^* x) ≥ 0`. -/
theorem haarState_star_mul_self_nonneg (hq0 : 0 < (q : K)) (hq1 : (q : K) ≠ 1)
    (x : OqSU2 K q) : 0 ≤ haarState q (compactStar q x * x) := by
  rcases hq1.lt_or_gt with h | h
  · exact haarState_star_mul_self_nonneg_of_lt_one q hq0 h x
  · exact haarState_star_mul_self_nonneg_of_one_lt q h x

end AllQ

end QOU.AlgebraicSubstrate.OqSU2
