import CompactQuantumMetrics.OqSU2PBW
import QOU.FluidDynamics.q_ns_haar_field_invariance
import Mathlib.Algebra.Ring.GeomSum

/-!
# QOU.FluidDynamics.q_ns_haar_field_invariance_full — `h ∘ X = 0` on all of `O_q(SU(2))`

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`).

PR #9713 (`q_ns_haar_field_invariance`) proved `h(X₊ x) = 0` and `h(X₋ x) = 0` for `x` in
the blocks `K[ζ]`, `βδ·K[ζ]`, `αγ·K[ζ]` (`ζ = βγ`), and listed the whole-algebra statement
as open because the corpus had no PBW spanning result. `OqSU2PBW` now supplies the PBW
basis, and this file closes the gap.

## Results (sorry-free)

For `q` not a root of unity (`hq : ∀ n > 0, q^n ≠ 1`):

* `haarState_fieldPlus_eq_zero` — `h(X₊ x) = 0` for **every** `x ∈ O_q(SU(2))`;
* `haarState_fieldMinus_eq_zero` — `h(X₋ x) = 0` for every `x`;
* `haarState_fieldZero_eq_zero` — `h(X₀ x) = 0` for every `x`, where `X₀ = X_{(1,0,0)}`.

## Proof

1. **Equivariance.** For a torus automorphism `θ = θ_{u,v}`,
   `θ ∘ X₊ = (u v⁻¹) X₊ ∘ θ`, `θ ∘ X₋ = (v u⁻¹) X₋ ∘ θ`, `θ ∘ X₀ = X₀ ∘ θ`
   (`torus_fieldPlus`, …). Both sides are twisted derivations with the same twist and agree
   on generators; `twistedLeibniz_ext` says such maps are equal.
2. **Weights.** `θ_{u,v}` scales the PBW monomial `(a, b, c)` by `u^a v^(b−c)`
   (`torus_pbwMono`). So `X₊ pbwMono(a,b,c)` is scaled by `u^(a+1) v^(b−c−1)`; since `h` is torus
   invariant, `h(X₊ pbwMono(a,b,c)) = 0` unless `a = −1` and `b = c + 1`
   (`haarState_eq_zero_of_torus` with `(u, v) = (q, 1)` or `(1, q)`).
3. **The one surviving weight.** `pbwMono(−1, c+1, c) = δ β^(c+1) γ^c` is a scalar multiple of
   `ζ^c βδ` (`monoD_one_eq`), which is #9713's block; likewise `pbwMono(1, b, b+1)` is a multiple
   of `ζ^b αγ` for `X₋`, and `pbwMono(0, b, b) = ζ^b` for `X₀`, where `X₀ ζ^b = 0`.
4. **Basis.** `h ∘ X` is linear and vanishes on the PBW basis (`pbwBasis`), so it is zero.

## Hypotheses

`hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1`. It is used to make a torus weight `q^m`, `m ≠ 0`,
differ from `1`, and it implies the moment condition `∀ n, [n+1]_{q²} ≠ 0`
(`qSqNum_ne_zero_of_not_root`) that #9713's block lemmas take. Positivity of `q` is not used.

## Not established

* Full coproduct invariance `(id ⊗ h)Δ = h(·)1` and the root-of-unity no-go are now proved in
  `q_ns_haar_coproduct_invariance.lean`, from the three statements here.
* Any link to the q-NS advection term (no `∇_q` on `O_q(SU(2))` in the corpus).

Everything is algebraic, so the file stays out of `QOU/Transcendental/`. No empirical value
enters any proof.

-- Ref: [woronowicz1987-twisted-su2]
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.HaarFieldInvarianceFull

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.HaarFieldInvariance

/-! ## Twisted derivations are fixed by their values on generators -/

section Ext

variable {R : Type*} [CommRing R] (q : Rˣ)

theorem twisted_map_one (θ ρ : OqSU2 R q →ₐ[R] OqSU2 R q) (D : OqSU2 R q →ₗ[R] OqSU2 R q)
    (hD : ∀ f g, D (f * g) = D f * ρ g + θ f * D g) : D 1 = 0 := by
  have h := hD 1 1
  simp only [mul_one, map_one, one_mul] at h
  have h' : D 1 + D 1 = D 1 + 0 := by rw [add_zero]; exact h.symm
  exact add_left_cancel h'

/-- Two linear maps with the same twisted Leibniz rule `D(fg) = D f · ρ g + θ f · D g` agree
everywhere once they agree on `α, β, γ, δ`. -/
theorem twistedLeibniz_ext (θ ρ : OqSU2 R q →ₐ[R] OqSU2 R q)
    (D₁ D₂ : OqSU2 R q →ₗ[R] OqSU2 R q)
    (h₁ : ∀ f g, D₁ (f * g) = D₁ f * ρ g + θ f * D₁ g)
    (h₂ : ∀ f g, D₂ (f * g) = D₂ f * ρ g + θ f * D₂ g)
    (hα : D₁ (α q) = D₂ (α q)) (hβ : D₁ (β q) = D₂ (β q))
    (hγ : D₁ (γ q) = D₂ (γ q)) (hδ : D₁ (δ q) = D₂ (δ q)) (x : OqSU2 R q) : D₁ x = D₂ x := by
  let S : Subalgebra R (OqSU2 R q) :=
    { carrier := {x | D₁ x = D₂ x}
      mul_mem' := by
        intro x y hx hy
        simp only [Set.mem_setOf_eq] at *
        rw [h₁, h₂, hx, hy]
      add_mem' := by
        intro x y hx hy
        simp only [Set.mem_setOf_eq, map_add] at *
        rw [hx, hy]
      algebraMap_mem' := by
        intro r
        simp only [Set.mem_setOf_eq, Algebra.algebraMap_eq_smul_one, map_smul,
          twisted_map_one q θ ρ D₁ h₁, twisted_map_one q θ ρ D₂ h₂] }
  exact mem_of_gens S hα hβ hγ hδ x

/-- Torus automorphisms commute. -/
theorem torus_comm (u v a b : Rˣ) (x : OqSU2 R q) :
    torusScaleAlgHom q u v (torusScaleAlgHom q a b x) =
      torusScaleAlgHom q a b (torusScaleAlgHom q u v x) := by
  have h₁ := AlgHom.congr_fun (torusScaleAlgHom_comp (R := R) q u v a b) x
  have h₂ := AlgHom.congr_fun (torusScaleAlgHom_comp (R := R) q a b u v) x
  simp only [AlgHom.comp_apply] at h₁ h₂
  rw [h₁, h₂, mul_comm a u, mul_comm b v]

/-! ## Equivariance of the three fields under the torus -/

/-- The twist `R = θ_{q⁻¹, q}` of `field_leibniz`. -/
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

theorem torus_field_leibniz (s0 sp sm : R) (u v : Rˣ) (c : R) (f g : OqSU2 R q) :
    c • field q s0 sp sm (torusScaleAlgHom q u v (f * g)) =
      c • field q s0 sp sm (torusScaleAlgHom q u v f) *
          (torusScaleAlgHom q u v).comp tw g +
        torusScaleAlgHom q u v f * c • field q s0 sp sm (torusScaleAlgHom q u v g) := by
  rw [map_mul, field_leibniz, AlgHom.comp_apply, torus_comm, smul_add, smul_mul_assoc,
    mul_smul_comm]

theorem field_torus_leibniz (s0 sp sm : R) (u v : Rˣ) (f g : OqSU2 R q) :
    torusScaleAlgHom q u v (field q s0 sp sm (f * g)) =
      torusScaleAlgHom q u v (field q s0 sp sm f) * (torusScaleAlgHom q u v).comp tw g +
        torusScaleAlgHom q u v f * torusScaleAlgHom q u v (field q s0 sp sm g) := by
  rw [field_leibniz, map_add, map_mul, map_mul, AlgHom.comp_apply]

/-- `θ_{u,v} ∘ X₊ = (u v⁻¹) · X₊ ∘ θ_{u,v}`. -/
theorem torus_fieldPlus (u v : Rˣ) (x : OqSU2 R q) :
    torusScaleAlgHom q u v (fieldPlus q x) =
      ((u : R) * ((v⁻¹ : Rˣ) : R)) • fieldPlus q (torusScaleAlgHom q u v x) := by
  obtain ⟨pa, pb, pg, pd⟩ := fieldPlus_generators (R := R) q
  refine twistedLeibniz_ext q (torusScaleAlgHom q u v) ((torusScaleAlgHom q u v).comp tw)
    ((torusScaleAlgHom q u v).toLinearMap ∘ₗ fieldPlus q)
    (((u : R) * ((v⁻¹ : Rˣ) : R)) • (fieldPlus q ∘ₗ (torusScaleAlgHom q u v).toLinearMap))
    (fun f g => field_torus_leibniz q 0 1 0 u v f g)
    (fun f g => torus_field_leibniz q 0 1 0 u v _ f g) ?_ ?_ ?_ ?_ x <;>
  simp only [LinearMap.comp_apply, LinearMap.smul_apply, AlgHom.toLinearMap_apply,
    torusScaleAlgHom, liftQuadruple_alpha, liftQuadruple_beta, liftQuadruple_gamma,
    liftQuadruple_delta, map_smul, pa, pb, pg, pd, map_zero, smul_zero, smul_smul]
  · congr 1; rw [mul_assoc, Units.inv_mul, mul_one]
  · congr 1; rw [mul_comm (_ : R) ((_⁻¹ : Rˣ) : R), Units.inv_mul_cancel_left]

/-- `θ_{u,v} ∘ X₋ = (v u⁻¹) · X₋ ∘ θ_{u,v}`. -/
theorem torus_fieldMinus (u v : Rˣ) (x : OqSU2 R q) :
    torusScaleAlgHom q u v (fieldMinus q x) =
      ((v : R) * ((u⁻¹ : Rˣ) : R)) • fieldMinus q (torusScaleAlgHom q u v x) := by
  obtain ⟨pa, pb, pg, pd⟩ := fieldMinus_generators (R := R) q
  refine twistedLeibniz_ext q (torusScaleAlgHom q u v) ((torusScaleAlgHom q u v).comp tw)
    ((torusScaleAlgHom q u v).toLinearMap ∘ₗ fieldMinus q)
    (((v : R) * ((u⁻¹ : Rˣ) : R)) • (fieldMinus q ∘ₗ (torusScaleAlgHom q u v).toLinearMap))
    (fun f g => field_torus_leibniz q 0 0 1 u v f g)
    (fun f g => torus_field_leibniz q 0 0 1 u v _ f g) ?_ ?_ ?_ ?_ x <;>
  simp only [LinearMap.comp_apply, LinearMap.smul_apply, AlgHom.toLinearMap_apply,
    torusScaleAlgHom, liftQuadruple_alpha, liftQuadruple_beta, liftQuadruple_gamma,
    liftQuadruple_delta, map_smul, pa, pb, pg, pd, map_zero, smul_zero, smul_smul]
  · congr 1; rw [mul_assoc, Units.inv_mul, mul_one]
  · congr 1; rw [mul_comm (_ : R) ((_⁻¹ : Rˣ) : R), Units.inv_mul_cancel_left]

/-- The Cartan field `X₀ : (α, β, γ, δ) ↦ (α, −qβ, γ, −qδ)`. -/
noncomputable abbrev fieldZero : OqSU2 R q →ₗ[R] OqSU2 R q := field q 1 0 0

theorem fieldZero_generators :
    fieldZero q (α q) = α q ∧ fieldZero q (β q) = (-(q : R)) • β q ∧
      fieldZero q (γ q) = γ q ∧ fieldZero q (δ q) = (-(q : R)) • δ q := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [fieldZero, field_alpha]
  · rw [field_beta, zero_smul, zero_sub, mul_one]
    exact (neg_smul (R := R) (M := OqSU2 R q) _ _).symm
  · simp [fieldZero, field_gamma]
  · rw [field_delta, zero_smul, zero_sub, mul_one]
    exact (neg_smul (R := R) (M := OqSU2 R q) _ _).symm

/-- `θ_{u,v} ∘ X₀ = X₀ ∘ θ_{u,v}`. -/
theorem torus_fieldZero (u v : Rˣ) (x : OqSU2 R q) :
    torusScaleAlgHom q u v (fieldZero q x) = fieldZero q (torusScaleAlgHom q u v x) := by
  obtain ⟨pa, pb, pg, pd⟩ := fieldZero_generators (R := R) q
  have key := twistedLeibniz_ext q (torusScaleAlgHom q u v) ((torusScaleAlgHom q u v).comp tw)
    ((torusScaleAlgHom q u v).toLinearMap ∘ₗ fieldZero q)
    ((1 : R) • (fieldZero q ∘ₗ (torusScaleAlgHom q u v).toLinearMap))
    (fun f g => field_torus_leibniz q 1 0 0 u v f g)
    (fun f g => torus_field_leibniz q 1 0 0 u v _ f g)
    (by simp [torusScaleAlgHom, pa])
    (by simp only [LinearMap.comp_apply, AlgHom.toLinearMap_apply,
          torusScaleAlgHom, liftQuadruple_beta, map_smul, pb, smul_smul,
          one_smul, mul_comm])
    (by simp [torusScaleAlgHom, pg])
    (by simp only [LinearMap.comp_apply, AlgHom.toLinearMap_apply,
          torusScaleAlgHom, liftQuadruple_delta, map_smul, pd, smul_smul,
          one_smul, mul_comm]) x
  simpa using key

/-- `X₀ ζ = 0`. -/
theorem fieldZero_zetaB : fieldZero q (zetaB (R := R) q) = 0 := by
  obtain ⟨-, pb, pg, -⟩ := fieldZero_generators (R := R) q
  obtain ⟨-, -, tg, -⟩ := field_twist_generators (R := R) q
  rw [zetaB, field_leibniz, pb, pg, tg]
  rw [smul_mul_smul_comm, neg_mul, Units.mul_inv]
  have h1 : ((-1 : R) • (β q * γ q) : OqSU2 R q) = -(β q * γ q) := by
    exact (neg_smul (R := R) (M := OqSU2 R q) 1 _).trans (by rw [one_smul])
  rw [h1]
  exact neg_add_cancel _

/-- `X₀ ζ^k = 0`. -/
theorem fieldZero_zetaB_pow (k : ℕ) : fieldZero q (zetaB (R := R) q ^ k) = 0 := by
  induction k with
  | zero => rw [pow_zero]; exact field_one q 1 0 0
  | succ k ih => rw [pow_succ, field_leibniz, ih, fieldZero_zetaB, zero_mul, mul_zero, add_zero]

/-! ## Torus weights of the PBW monomials -/

theorem torus_monoY (u v : Rˣ) (b c : ℕ) :
    torusScaleAlgHom q u v (monoY q b c) =
      ((v : R) ^ b * ((v⁻¹ : Rˣ) : R) ^ c) • monoY (R := R) q b c := by
  simp only [monoY, map_mul, map_pow, torusScaleAlgHom, liftQuadruple_beta, liftQuadruple_gamma,
    smul_pow, smul_mul_smul_comm]

/-- `θ_{u,v}` scales the PBW monomial `(a, b, c)` by `u^a v^(b−c)`. -/
theorem torus_pbwMono (u v : Rˣ) (i : MonoIdx) :
    torusScaleAlgHom q u v (pbwMono q i) =
      ((u ^ i.1 * v ^ ((i.2.1 : ℤ) - i.2.2) : Rˣ) : R) • pbwMono (R := R) q i := by
  obtain ⟨a, b, c⟩ := i
  have hv : ((v ^ ((b : ℤ) - c) : Rˣ) : R) = (v : R) ^ b * ((v⁻¹ : Rˣ) : R) ^ c := by
    rw [zpow_sub, zpow_natCast, zpow_natCast, ← inv_pow, Units.val_mul,
      Units.val_pow_eq_pow_val, Units.val_pow_eq_pow_val]
  rcases le_or_gt 0 a with ha | ha
  · obtain ⟨n, rfl⟩ := Int.eq_ofNat_of_zero_le ha
    simp only [pbwMono_nat, monoA, map_mul, map_pow, torus_monoY]
    simp only [torusScaleAlgHom, liftQuadruple_alpha, smul_pow, smul_mul_smul_comm, Units.val_mul,
      hv, zpow_natCast, Units.val_pow_eq_pow_val]
  · obtain ⟨n, hn⟩ := Int.exists_eq_neg_ofNat ha.le
    subst hn
    simp only [pbwMono_neg_nat, monoD, map_mul, map_pow, torus_monoY]
    simp only [torusScaleAlgHom, liftQuadruple_delta, smul_pow, smul_mul_smul_comm, Units.val_mul,
      hv, zpow_neg, zpow_natCast, ← inv_pow, Units.val_pow_eq_pow_val]

end Ext

/-! ## The Haar state on torus weight vectors -/

section Haar

variable {K : Type*} [Field K] (q : Kˣ)

/-- If `θ_{u,v} y = w y` with `w ≠ 1`, then `h(y) = 0`. -/
theorem haarState_eq_zero_of_torus (u v : Kˣ) (w : K) (hw : w ≠ 1) (y : OqSU2 K q)
    (hy : torusScaleAlgHom q u v y = w • y) : haarState q y = 0 := by
  have h := haarState_torus q u v y
  rw [hy, map_smul, smul_eq_mul] at h
  have h' : (w - 1) * haarState q y = 0 := by linear_combination h
  exact (mul_eq_zero.1 h').resolve_left (sub_ne_zero.2 hw)

/-- Not a root of unity: integer powers. -/
theorem zpow_ne_one (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1) {z : ℤ} (hz : z ≠ 0) :
    (((q ^ z : Kˣ)) : K) ≠ 1 := by
  rw [Units.val_zpow_eq_zpow_val]
  rcases Int.eq_nat_or_neg z with ⟨n, rfl | rfl⟩
  · rw [zpow_natCast]; exact hq n (by omega)
  · rw [zpow_neg, zpow_natCast, inv_ne_one]; exact hq n (by omega)

/-- Not a root of unity implies `[n+1]_{q²} ≠ 0` for every `n`. -/
theorem qSqNum_ne_zero_of_not_root (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1) (n : ℕ) :
    qSqNum q n ≠ 0 := by
  intro h0
  have hgeom := geom_sum_mul ((q : K) ^ 2) (n + 1)
  have hs : qSqNum q n = ∑ i ∈ Finset.range (n + 1), ((q : K) ^ 2) ^ i := by
    simp only [qSqNum, ← pow_mul]
  rw [← hs, h0, zero_mul, ← pow_mul] at hgeom
  exact hq (2 * (n + 1)) (by omega) (sub_eq_zero.1 hgeom.symm)

/-- The PBW-indexed weight bookkeeping: `X` with shift `c(u,v)` applied to a weight vector. -/
theorem torus_field_pbwMono {X : OqSU2 K q →ₗ[K] OqSU2 K q} (c : Kˣ → Kˣ → K)
    (hX : ∀ u v x, torusScaleAlgHom q u v (X x) = c u v • X (torusScaleAlgHom q u v x))
    (u v : Kˣ) (i : MonoIdx) :
    torusScaleAlgHom q u v (X (pbwMono q i)) =
      (c u v * ((u ^ i.1 * v ^ ((i.2.1 : ℤ) - i.2.2) : Kˣ) : K)) • X (pbwMono q i) := by
  rw [hX, torus_pbwMono, map_smul, smul_smul]

/-! ## The surviving weights are #9713's blocks -/

theorem zetaB_pow_eq (c : ℕ) : zetaB (R := K) q ^ c = monoY q c c := by
  rw [zetaB, monoY, (show Commute (β (R := K) q) (γ q) from rel_bg q).mul_pow]

/-- `δ β^(c+1) γ^c = q⁻¹ q^(−2c) ζ^c β δ`. -/
theorem monoD_one_eq (c : ℕ) :
    monoD q 1 (c + 1) c = (((q⁻¹ : Kˣ) : K) * (((q⁻¹ : Kˣ) : K) * ((q⁻¹ : Kˣ) : K)) ^ c) •
      (zetaB (R := K) q ^ c * (β q * δ q)) := by
  rw [monoD, pow_one, ← beta_mul_monoY, ← zetaB_pow_eq, ← mul_assoc, delta_beta, smul_mul_assoc,
    skew_pow_right (betaDelta_zeta q), smul_smul]

/-- `α β^b γ^(b+1) = q^(2b) ζ^b α γ`. -/
theorem monoA_one_eq (b : ℕ) :
    monoA q 1 b (b + 1) = ((q : K) * q) ^ b • (zetaB (R := K) q ^ b * (α q * γ q)) := by
  have hY : monoY (R := K) q b (b + 1) = zetaB q ^ b * γ q := by
    rw [zetaB_pow_eq, monoY, monoY, pow_succ, mul_assoc]
  rw [monoA, pow_one, hY, ← mul_assoc, skew_pow_right (alpha_zeta q), smul_mul_assoc, mul_assoc]

/-! ## Main theorems -/

variable (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1)
include hq

/-- **`h ∘ X₊ = 0` on all of `O_q(SU(2))`**, for `q` not a root of unity. -/
theorem haarState_fieldPlus_eq_zero (x : OqSU2 K q) : haarState q (fieldPlus q x) = 0 := by
  have hX := torus_field_pbwMono q (X := fieldPlus q) (fun u v => (u : K) * ((v⁻¹ : Kˣ) : K))
    (fun u v x => torus_fieldPlus q u v x)
  suffices h : (haarState q).comp (fieldPlus q) = 0 from LinearMap.congr_fun h x
  refine (pbwBasis q).ext fun i => ?_
  obtain ⟨a, b, c⟩ := i
  simp only [pbwBasis_apply, LinearMap.comp_apply, LinearMap.zero_apply]
  by_cases ha : a + 1 = 0
  · by_cases hs : (b : ℤ) - c - 1 = 0
    · -- the surviving weight `(−1, 1)`: `#9713`'s block `βδ · K[ζ]`
      obtain rfl : a = -((1 : ℕ) : ℤ) := by omega
      obtain rfl : b = c + 1 := by omega
      rw [pbwMono_neg_nat, monoD_one_eq, map_smul, map_smul,
        haarState_fieldPlus_zeta_pow_betaDelta q (qSqNum_ne_zero_of_not_root q hq), smul_zero]
    · refine haarState_eq_zero_of_torus q 1 q _ ?_ _ (hX 1 q (a, b, c))
      have hw : ((1 : Kˣ) : K) * ((q⁻¹ : Kˣ) : K) *
          ((1 ^ a * q ^ ((b : ℤ) - c) : Kˣ) : K) = ((q ^ ((b : ℤ) - c - 1) : Kˣ) : K) := by
        rw [one_zpow, one_mul, Units.val_one, one_mul, ← Units.val_mul, zpow_sub_one, mul_comm]
      rw [hw]; exact zpow_ne_one q hq hs
  · refine haarState_eq_zero_of_torus q q 1 _ ?_ _ (hX q 1 (a, b, c))
    have hw : (q : K) * ((1⁻¹ : Kˣ) : K) * ((q ^ a * 1 ^ ((b : ℤ) - c) : Kˣ) : K) =
        ((q ^ (a + 1) : Kˣ) : K) := by
      rw [inv_one, Units.val_one, mul_one, one_zpow, mul_one, ← Units.val_mul, zpow_add_one,
        mul_comm]
    rw [hw]; exact zpow_ne_one q hq ha

/-- **`h ∘ X₋ = 0` on all of `O_q(SU(2))`**, for `q` not a root of unity. -/
theorem haarState_fieldMinus_eq_zero (x : OqSU2 K q) : haarState q (fieldMinus q x) = 0 := by
  have hX := torus_field_pbwMono q (X := fieldMinus q) (fun u v => (v : K) * ((u⁻¹ : Kˣ) : K))
    (fun u v x => torus_fieldMinus q u v x)
  suffices h : (haarState q).comp (fieldMinus q) = 0 from LinearMap.congr_fun h x
  refine (pbwBasis q).ext fun i => ?_
  obtain ⟨a, b, c⟩ := i
  simp only [pbwBasis_apply, LinearMap.comp_apply, LinearMap.zero_apply]
  by_cases ha : a - 1 = 0
  · by_cases hs : (b : ℤ) - c + 1 = 0
    · -- the surviving weight `(1, −1)`: `#9713`'s block `αγ · K[ζ]`
      obtain rfl : a = ((1 : ℕ) : ℤ) := by omega
      obtain rfl : c = b + 1 := by omega
      rw [pbwMono_nat, monoA_one_eq, map_smul, map_smul,
        haarState_fieldMinus_zeta_pow_alphaGamma q (qSqNum_ne_zero_of_not_root q hq), smul_zero]
    · refine haarState_eq_zero_of_torus q 1 q _ ?_ _ (hX 1 q (a, b, c))
      have hw : (q : K) * ((1⁻¹ : Kˣ) : K) *
          ((1 ^ a * q ^ ((b : ℤ) - c) : Kˣ) : K) = ((q ^ ((b : ℤ) - c + 1) : Kˣ) : K) := by
        rw [inv_one, Units.val_one, mul_one, one_zpow, one_mul, ← Units.val_mul, zpow_add_one,
          mul_comm]
      rw [hw]; exact zpow_ne_one q hq hs
  · refine haarState_eq_zero_of_torus q q 1 _ ?_ _ (hX q 1 (a, b, c))
    have hw : ((1 : Kˣ) : K) * ((q⁻¹ : Kˣ) : K) * ((q ^ a * 1 ^ ((b : ℤ) - c) : Kˣ) : K) =
        ((q ^ (a - 1) : Kˣ) : K) := by
      rw [Units.val_one, one_mul, one_zpow, mul_one, ← Units.val_mul, zpow_sub_one, mul_comm]
    rw [hw]; exact zpow_ne_one q hq ha

/-- **`h ∘ X₀ = 0` on all of `O_q(SU(2))`**, for `q` not a root of unity. -/
theorem haarState_fieldZero_eq_zero (x : OqSU2 K q) : haarState q (fieldZero q x) = 0 := by
  have hX := torus_field_pbwMono q (X := fieldZero q) (fun _ _ => 1)
    (fun u v x => by rw [one_smul]; exact torus_fieldZero q u v x)
  suffices h : (haarState q).comp (fieldZero q) = 0 from LinearMap.congr_fun h x
  refine (pbwBasis q).ext fun i => ?_
  obtain ⟨a, b, c⟩ := i
  simp only [pbwBasis_apply, LinearMap.comp_apply, LinearMap.zero_apply]
  by_cases ha : a = 0
  · by_cases hs : (b : ℤ) - c = 0
    · -- weight zero: `pbwMono(0, b, b) = ζ^b`, and `X₀ ζ^b = 0`
      subst ha
      have hbc : b = c := by omega
      subst hbc
      rw [show ((0 : ℤ), b, b) = (((0 : ℕ) : ℤ), b, b) from rfl, pbwMono_nat, monoA_zero,
        ← zetaB_pow_eq, fieldZero_zetaB_pow, map_zero]
    · refine haarState_eq_zero_of_torus q 1 q _ ?_ _ (hX 1 q (a, b, c))
      rw [one_mul, one_zpow, one_mul]; exact zpow_ne_one q hq hs
  · refine haarState_eq_zero_of_torus q q 1 _ ?_ _ (hX q 1 (a, b, c))
    rw [one_mul, one_zpow, mul_one]; exact zpow_ne_one q hq ha

end Haar

end QOU.FluidDynamics.HaarFieldInvarianceFull
