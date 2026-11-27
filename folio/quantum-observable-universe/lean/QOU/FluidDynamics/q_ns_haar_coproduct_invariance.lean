import QOU.FluidDynamics.q_ns_haar_field_invariance_full
import CompactQuantumMetrics.OqSU2Coassoc

/-!
# Coproduct invariance of the `O_q(SU(2))` Haar state, and the root-of-unity no-go

Bean `qou-q3dc`. `q_ns_haar_field_invariance_full` proves `h ∘ X = 0` on the whole algebra for
the three left-invariant fields `X₊, X₋, X₀`, for `q` not a root of unity. This file upgrades
that to invariance under the coproduct itself, proves the invariant state is unique, and shows
why roots of unity are excluded.

## Results (sorry-free, over a field `K`)

* `eq_smul_haarState` (**uniqueness**). If `g ∘ X₊ = g ∘ X₋ = g ∘ X₀ = 0` then `g = g(1) h`.
  The PBW basis does the work. `X₊` and `X₋` hit every monomial with `α` or `δ` up to a
  nonzero `q`-number (`fieldPlus_monoA`, `fieldMinus_monoD`). `(1 − q⁻¹) X₀ = id − R`, where
  `R` is the Leibniz twist (`fieldZero_eq`), which removes `β^b γ^c` with `b ≠ c`. On the
  block `ζ^k` the operator `X₊X₋` is bidiagonal with nonzero diagonal (`lap_zeta_pow`).
* `haarState_leftInvOp` (**right invariance**): `(id ⊗ h) Δ x = h(x) · 1`.
  Proof: for a functional `f`, `g := h ∘ (f ⊗ id)Δ` kills the fields (they commute with
  `(f ⊗ id)Δ`, `leftConv_leftInvOp`), so `g = f(1) h`; then `f((id⊗h)Δx) = g(x)`
  (`pair_leftInvOp`), and coordinate functionals separate points.
* `haarState_leftConv` (**left invariance**): `(h ⊗ id) Δ x = h(x) · 1`, from right invariance
  through the transpose `T` (`Δ T = flip (T ⊗ T) Δ`) and `h ∘ T = h`.
* `eq_smul_haarState_of_leftConv`: every functional with `(g ⊗ id) Δ = g(·) 1` is `g(1) h`.
* **Roots of unity.** `qSqNum_ne_zero_of_fieldPlus`: if some `g` has `g(1) ≠ 0` and
  `g ∘ X₊ = 0`, then `[n+1]_{q²} ≠ 0` for all `n`. So when `q²` is a nontrivial root of unity
  (`qSqNum_eq_zero_of_root`) no functional with `g(1) ≠ 0` is killed by `X₊`
  (`exists_fieldPlus_ne_zero_of_root`). In particular there is no normalised invariant state
  (`not_leftConv_invariant_of_root`). The obstruction is the moment recursion on `ζ^k`.

The cases `q = ±1` are not covered: they are roots of unity, so the non-root hypothesis
excludes them, while `[n+1]_{q²} = n + 1` need not vanish there.

No empirical value enters any proof.

-- Ref: [woronowicz1987]
-/

namespace QOU.FluidDynamics.HaarCoproductInvariance

open TensorProduct
open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2 QOU.FluidDynamics.HaarFieldInvariance
  QOU.FluidDynamics.HaarFieldInvarianceFull

/-! ## Field values on PBW monomials (any commutative ring) -/

section Ring

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

theorem fieldPlus_alpha_pow (n : ℕ) : fieldPlus q (α (R := R) q ^ n) = 0 := by
  induction n with
  | zero => rw [pow_zero]; exact field_one q 0 1 0
  | succ n ih =>
    rw [pow_succ, field_leibniz, ih, (fieldPlus_generators q).1, zero_mul, mul_zero, add_zero]

theorem fieldPlus_gamma_pow (n : ℕ) : fieldPlus q (γ (R := R) q ^ n) = 0 := by
  induction n with
  | zero => rw [pow_zero]; exact field_one q 0 1 0
  | succ n ih =>
    rw [pow_succ, field_leibniz, ih, (fieldPlus_generators q).2.2.1, zero_mul, mul_zero, add_zero]

theorem fieldMinus_delta_pow (n : ℕ) : fieldMinus q (δ (R := R) q ^ n) = 0 := by
  induction n with
  | zero => rw [pow_zero]; exact field_one q 0 0 1
  | succ n ih =>
    rw [pow_succ, field_leibniz, ih, (fieldMinus_generators q).2.2.2, zero_mul, mul_zero,
      add_zero]

theorem fieldMinus_beta_pow (n : ℕ) : fieldMinus q (β (R := R) q ^ n) = 0 := by
  induction n with
  | zero => rw [pow_zero]; exact field_one q 0 0 1
  | succ n ih =>
    rw [pow_succ, field_leibniz, ih, (fieldMinus_generators q).2.1, zero_mul, mul_zero, add_zero]

/-- `X₊ β^{m+1} = q^m [m+1]_{q⁻²} α β^m`. -/
theorem fieldPlus_beta_pow_succ (m : ℕ) :
    fieldPlus q (β (R := R) q ^ (m + 1)) =
      ((q : R) ^ m * jk (qi * qi) (m + 1)) • (α q * β q ^ m) := by
  induction m with
  | zero => simp [(fieldPlus_generators q).2.1]
  | succ m ih =>
    rw [pow_succ, field_leibniz, ih, (field_twist_generators q).2.1, (fieldPlus_generators q).2.1,
      skew_pow_left (beta_alpha_skew q), smul_mul_smul_comm, mul_assoc (α q), ← pow_succ,
      ← add_smul]
    congr 1
    have h1 : ((q : R) * qi) ^ (m + 1) = 1 := by rw [q_mul_qi, one_pow]
    rw [jk_succ _ (m + 1)]
    linear_combination (-(qi ^ (m + 1))) * h1

/-- `X₋ γ^{m+1} = q^{−m} [m+1]_{q²} δ γ^m`. -/
theorem fieldMinus_gamma_pow_succ (m : ℕ) :
    fieldMinus q (γ (R := R) q ^ (m + 1)) =
      (qi ^ m * jk ((q : R) * q) (m + 1)) • (δ q * γ q ^ m) := by
  induction m with
  | zero => simp [(fieldMinus_generators q).2.2.1]
  | succ m ih =>
    rw [pow_succ, field_leibniz, ih, (field_twist_generators q).2.2.1,
      (fieldMinus_generators q).2.2.1, skew_pow_left (rel_gd q), smul_mul_smul_comm, mul_assoc (δ q),
      ← pow_succ, ← add_smul]
    congr 1
    have h1 : (qi * (q : R)) ^ (m + 1) = 1 := by rw [qi_mul_q, one_pow]
    rw [jk_succ _ (m + 1)]
    linear_combination (-((q : R) ^ (m + 1))) * h1

/-- `X₊ (α^n β^{m+1} γ^c) = q^m [m+1]_{q⁻²} q^{−c} α^{n+1} β^m γ^c`. -/
theorem fieldPlus_monoA (n m c : ℕ) :
    fieldPlus q (monoA (R := R) q n (m + 1) c) =
      ((q : R) ^ m * jk (qi * qi) (m + 1) * qi ^ c) • monoA q (n + 1) m c := by
  rw [monoA, monoY, field_leibniz, fieldPlus_alpha_pow, zero_mul, zero_add, field_leibniz,
    fieldPlus_gamma_pow, mul_zero, add_zero, fieldPlus_beta_pow_succ, map_pow,
    (field_twist_generators q).2.2.1, smul_pow, smul_mul_smul_comm, mul_smul_comm, monoA, monoY,
    pow_succ]
  simp only [mul_assoc]

/-- `X₋ (δ^n β^b γ^{m+1}) = q^{−m} [m+1]_{q²} q^b δ^{n+1} β^b γ^m`. -/
theorem fieldMinus_monoD (n b m : ℕ) :
    fieldMinus q (monoD (R := R) q n b (m + 1)) =
      (qi ^ m * jk ((q : R) * q) (m + 1) * (q : R) ^ b) • monoD q (n + 1) b m := by
  rw [monoD, monoY, field_leibniz, fieldMinus_delta_pow, zero_mul, zero_add, field_leibniz,
    fieldMinus_beta_pow, zero_mul, zero_add, fieldMinus_gamma_pow_succ, mul_smul_comm,
    mul_smul_comm, ← mul_assoc (β q ^ b), skew_pow_left (rel_bd q), smul_mul_assoc,
    mul_smul_comm, smul_smul, monoD, monoY, pow_succ]
  simp only [mul_assoc]

/-- **The Cartan field is a difference operator**: `(1 − q⁻¹) X₀ = id − R`, where `R` is the
twist `(q⁻¹α, qβ, q⁻¹γ, qδ)` of the Leibniz rule. -/
theorem fieldZero_eq (x : OqSU2 R q) : (1 - qi) • fieldZero q x = x - tw x := by
  obtain ⟨pa, pb, pg, pd⟩ := fieldZero_generators (R := R) q
  obtain ⟨ta, tb, tg, td⟩ := field_twist_generators (R := R) q
  have key := twistedLeibniz_ext q (AlgHom.id R (OqSU2 R q)) tw
    ((1 - qi) • fieldZero q) (LinearMap.id - (tw).toLinearMap)
    (fun f g => by
      simp only [LinearMap.smul_apply, field_leibniz, smul_add, smul_mul_assoc, AlgHom.id_apply,
        mul_smul_comm])
    (fun f g => by
      simp only [LinearMap.sub_apply, LinearMap.id_apply, AlgHom.toLinearMap_apply, map_mul,
        AlgHom.id_apply, sub_mul, mul_sub]
      abel)
    ?_ ?_ ?_ ?_ x
  · simpa using key
  all_goals
    simp only [LinearMap.smul_apply, LinearMap.sub_apply, LinearMap.id_apply,
      AlgHom.toLinearMap_apply, pa, pb, pg, pd, ta, tb, tg, td, smul_smul]
  · rw [sub_smul, one_smul]
  · rw [show (1 - qi) * -(q : R) = 1 - (q : R) by linear_combination qi_mul_q q,
      sub_smul, one_smul]
  · rw [sub_smul, one_smul]
  · rw [show (1 - qi) * -(q : R) = 1 - (q : R) by linear_combination qi_mul_q q,
      sub_smul, one_smul]

/-- Convolving the transpose: `(f ⊗ id) Δ (T x) = T ((id ⊗ f∘T) Δ x)`. -/
theorem leftConv_transpose (f : OqSU2 R q →ₗ[R] R) (x : OqSU2 R q) :
    leftConv q f (transpose q x) =
      transpose q (leftInvOp q (f ∘ₗ (transpose q).toLinearMap) x) := by
  rw [leftConv_apply, coprod_transpose_apply, leftInvOp_apply']
  generalize coprod q x = z
  induction z using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp
  | add z w hz hw => simp only [map_add, hz, hw]

/-- The corner functionals vanish on `1`. -/
theorem triFun_one (s0 sp sm : R) : triFun q s0 sp sm (1 : OqSU2 R q) = 0 := by
  have h := triFun_twisted q s0 sp sm 1 1
  simp only [mul_one, map_one, one_mul] at h
  linear_combination -h

end Ring

/-! ## Over a field -/

section Field

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))
local notation "tw" => torusScaleAlgHom q q⁻¹ q⁻¹⁻¹

theorem jk_inv_ne_zero (k : ℕ) (h : qSqNum q k ≠ 0) : jk (qi * qi) (k + 1) ≠ 0 := by
  rw [jk_inv_eq, ← qSqNum_eq_jk]
  have hq0 : (q : K)⁻¹ ≠ 0 := inv_ne_zero q.ne_zero
  exact mul_ne_zero (pow_ne_zero _ (mul_ne_zero hq0 hq0)) h

/-- A functional killed by `X₊` satisfies the moment recursion on the block `ζ^k`. -/
theorem lap_recursion (g : OqSU2 K q →ₗ[K] K) (hp : ∀ x, g (fieldPlus q x) = 0) (k : ℕ) :
    (jk (qi * qi) (k + 1) * ((q : K) * qSqNum q k)) * g (zetaB q ^ k) +
      (jk (qi * qi) (k + 1) * qSqNum q (k + 1)) * g (zetaB q ^ (k + 1)) = 0 := by
  have h := hp (fieldMinus q (zetaB q ^ (k + 1)))
  rw [← lap_apply, lap_zeta_pow, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul] at h
  rw [qSqNum_eq_jk, qSqNum_eq_jk]
  exact h

variable (hq : ∀ n : ℕ, 0 < n → (q : K) ^ n ≠ 1)
include hq

/-- **Uniqueness.** A functional killed by `X₊`, `X₋` and `X₀` is `g(1)` times the Haar
state. -/
theorem eq_smul_haarState (g : OqSU2 K q →ₗ[K] K) (hp : ∀ x, g (fieldPlus q x) = 0)
    (hm : ∀ x, g (fieldMinus q x) = 0) (h0 : ∀ x, g (fieldZero q x) = 0) :
    g = g 1 • haarState q := by
  set D := g - g 1 • haarState q with hD
  have Dp : ∀ x, D (fieldPlus q x) = 0 := fun x => by
    simp [hD, hp, haarState_fieldPlus_eq_zero q hq]
  have Dm : ∀ x, D (fieldMinus q x) = 0 := fun x => by
    simp [hD, hm, haarState_fieldMinus_eq_zero q hq]
  have D0 : ∀ x, D (fieldZero q x) = 0 := fun x => by
    simp [hD, h0, haarState_fieldZero_eq_zero q hq]
  have D1 : D 1 = 0 := by simp [hD, haarState_one]
  have hq1 : (1 : K) - qi ≠ 0 := by
    rw [sub_ne_zero, ne_comm, qi_eq_inv, inv_ne_one]
    simpa using hq 1 one_pos
  -- `D` is fixed by the twist
  have Dtw : ∀ x, D (tw x) = D x := fun x => by
    have h := congrArg D (fieldZero_eq q x)
    rw [map_smul, D0, smul_zero, map_sub] at h
    exact (sub_eq_zero.1 h.symm).symm
  have hns := qSqNum_ne_zero_of_not_root q hq
  suffices h : D = 0 from sub_eq_zero.1 h
  refine (pbwBasis q).ext fun i => ?_
  obtain ⟨a, b, c⟩ := i
  simp only [pbwBasis_apply, LinearMap.zero_apply]
  rcases lt_trichotomy a 0 with ha | rfl | ha
  · -- `a < 0`: the monomial is in the image of `X₋`
    obtain ⟨n, hn⟩ : ∃ n : ℕ, a = -((n + 1 : ℕ) : ℤ) := ⟨(-a - 1).toNat, by omega⟩
    subst hn
    rw [pbwMono_neg_nat]
    have h := Dm (monoD q n b (c + 1))
    rw [fieldMinus_monoD, map_smul, smul_eq_mul] at h
    refine (mul_eq_zero.1 h).resolve_left ?_
    refine mul_ne_zero (mul_ne_zero (pow_ne_zero _ (Units.ne_zero _)) ?_)
      (pow_ne_zero _ q.ne_zero)
    rw [← qSqNum_eq_jk]; exact hns c
  · by_cases hbc : b = c
    · -- the block `ζ^c`
      subst hbc
      rw [show ((0 : ℤ), b, b) = (((0 : ℕ) : ℤ), b, b) from rfl, pbwMono_nat, monoA_zero,
        ← zetaB_pow_eq]
      induction b with
      | zero => rw [pow_zero]; exact D1
      | succ k ih =>
        have h := lap_recursion q D Dp k
        rw [ih, mul_zero, zero_add] at h
        exact (mul_eq_zero.1 h).resolve_left
          (mul_ne_zero (jk_inv_ne_zero q k (hns k)) (hns (k + 1)))
    · -- weight `b − c ≠ 0` under the twist
      have hw := torus_pbwMono (R := K) q q⁻¹ q⁻¹⁻¹ (0, b, c)
      have h := Dtw (pbwMono q (0, b, c))
      rw [hw, map_smul, smul_eq_mul, inv_inv, zpow_zero, one_mul] at h
      have h' : ((((q ^ ((b : ℤ) - c) : Kˣ)) : K) - 1) * D (pbwMono q (0, b, c)) = 0 := by
        linear_combination h
      exact (mul_eq_zero.1 h').resolve_left
        (sub_ne_zero.2 (zpow_ne_one q hq (by omega)))
  · -- `a > 0`: the monomial is in the image of `X₊`
    obtain ⟨n, hn⟩ : ∃ n : ℕ, a = ((n + 1 : ℕ) : ℤ) := ⟨(a - 1).toNat, by omega⟩
    subst hn
    rw [pbwMono_nat]
    have h := Dp (monoA q n (b + 1) c)
    rw [fieldPlus_monoA, map_smul, smul_eq_mul] at h
    refine (mul_eq_zero.1 h).resolve_left ?_
    exact mul_ne_zero (mul_ne_zero (pow_ne_zero _ q.ne_zero) (jk_inv_ne_zero q b (hns b)))
      (pow_ne_zero _ (Units.ne_zero _))

omit hq in
/-- Coordinate functionals separate points. -/
theorem eq_of_forall_functional {x y : OqSU2 K q}
    (h : ∀ f : OqSU2 K q →ₗ[K] K, f x = f y) : x = y :=
  (pbwBasis q).ext_elem fun i => by simpa using h ((pbwBasis q).coord i)

/-- **Right invariance**: `(id ⊗ h) Δ x = h(x) · 1`. -/
theorem haarState_leftInvOp (x : OqSU2 K q) :
    leftInvOp q (haarState q) x = haarState q x • 1 := by
  refine eq_of_forall_functional q fun f => ?_
  set g := haarState q ∘ₗ leftConv q f with hg
  have gX : ∀ (s0 sp sm : K) y, g (field q s0 sp sm y) = haarState q (field q s0 sp sm
      (leftConv q f y)) := fun s0 sp sm y => by
    simp only [hg, LinearMap.comp_apply, field, leftConv_leftInvOp]
  have key := eq_smul_haarState q hq g
    (fun y => by rw [gX]; exact haarState_fieldPlus_eq_zero q hq _)
    (fun y => by rw [gX]; exact haarState_fieldMinus_eq_zero q hq _)
    (fun y => by rw [gX]; exact haarState_fieldZero_eq_zero q hq _)
  have g1 : g 1 = f 1 := by
    simp [hg, leftConv_one, haarState_one]
  have := LinearMap.congr_fun key x
  rw [g1] at this
  rw [pair_leftInvOp, map_smul, smul_eq_mul]
  simpa [hg, mul_comm] using this

theorem haarState_pbwMono_eq_zero (i : MonoIdx) (hi : i.1 ≠ 0 ∨ (i.2.1 : ℤ) - i.2.2 ≠ 0) :
    haarState q (pbwMono q i) = 0 := by
  rcases hi with ha | hs
  · refine haarState_eq_zero_of_torus q q 1 _ ?_ _ (torus_pbwMono q q 1 i)
    rw [one_zpow, mul_one]; exact zpow_ne_one q hq ha
  · refine haarState_eq_zero_of_torus q 1 q _ ?_ _ (torus_pbwMono q 1 q i)
    rw [one_zpow, one_mul]; exact zpow_ne_one q hq hs

/-- The Haar state is transpose invariant. -/
theorem haarState_transpose (x : OqSU2 K q) : haarState q (transpose q x) = haarState q x := by
  suffices h : haarState q ∘ₗ (transpose q).toLinearMap = haarState q from
    LinearMap.congr_fun h x
  refine (pbwBasis q).ext fun i => ?_
  obtain ⟨a, b, c⟩ := i
  simp only [pbwBasis_apply, LinearMap.comp_apply, AlgHom.toLinearMap_apply, transpose_pbwMono]
  by_cases h : a = 0 ∧ b = c
  · obtain ⟨rfl, rfl⟩ := h; rfl
  · have h' : a ≠ 0 ∨ (b : ℤ) - c ≠ 0 := by omega
    rw [haarState_pbwMono_eq_zero q hq (a, b, c) h', haarState_pbwMono_eq_zero q hq (a, c, b)
      (by rcases h' with h' | h'; exacts [Or.inl h', Or.inr (by dsimp only; omega)])]

/-- **Left invariance**: `(h ⊗ id) Δ x = h(x) · 1`. -/
theorem haarState_leftConv (x : OqSU2 K q) :
    leftConv q (haarState q) x = haarState q x • 1 := by
  obtain ⟨y, rfl⟩ : ∃ y, transpose q y = x := ⟨transpose q x, transpose_transpose q x⟩
  have hT : haarState q ∘ₗ (transpose q).toLinearMap = haarState q :=
    LinearMap.ext (haarState_transpose q hq)
  rw [leftConv_transpose, hT, haarState_leftInvOp q hq, map_smul, map_one,
    haarState_transpose q hq]

/-- **Uniqueness of the invariant state.** A functional with `(g ⊗ id) Δ = g(·) 1` is
`g(1) h`. -/
theorem eq_smul_haarState_of_leftConv (g : OqSU2 K q →ₗ[K] K)
    (hg : ∀ x, leftConv q g x = g x • 1) : g = g 1 • haarState q := by
  have gX : ∀ (s0 sp sm : K) y, g (field q s0 sp sm y) = 0 := fun s0 sp sm y => by
    rw [field, pair_leftInvOp, hg, map_smul, triFun_one, smul_zero]
  exact eq_smul_haarState q hq g (gX 0 1 0) (gX 0 0 1) (gX 1 0 0)

omit hq

/-! ## Roots of unity -/

/-- **No-go.** If some functional with `g(1) ≠ 0` is killed by `X₊`, then every
`[n+1]_{q²}` is nonzero. -/
theorem qSqNum_ne_zero_of_fieldPlus (g : OqSU2 K q →ₗ[K] K) (h1 : g 1 ≠ 0)
    (hp : ∀ x, g (fieldPlus q x) = 0) (n : ℕ) : qSqNum q n ≠ 0 := by
  suffices h : ∀ n, qSqNum q n ≠ 0 ∧ g (zetaB q ^ n) ≠ 0 from (h n).1
  intro n
  induction n with
  | zero =>
    refine ⟨?_, by rwa [pow_zero]⟩
    rw [qSqNum_eq_jk, jk_one]; exact one_ne_zero
  | succ k ih =>
    have h := lap_recursion q g hp k
    have hA : (jk (qi * qi) (k + 1) * ((q : K) * qSqNum q k)) * g (zetaB q ^ k) ≠ 0 :=
      mul_ne_zero (mul_ne_zero (jk_inv_ne_zero q k ih.1) (mul_ne_zero q.ne_zero ih.1)) ih.2
    have hB : (jk (qi * qi) (k + 1) * qSqNum q (k + 1)) * g (zetaB q ^ (k + 1)) ≠ 0 := by
      intro h0; rw [h0, add_zero] at h; exact hA h
    exact ⟨right_ne_zero_of_mul (left_ne_zero_of_mul hB), right_ne_zero_of_mul hB⟩

/-- `[N]_{q²} = 0` when `q^{2N} = 1` and `q² ≠ 1`. -/
theorem qSqNum_eq_zero_of_root {N : ℕ} (h : (q : K) ^ (2 * (N + 1)) = 1)
    (h2 : (q : K) ^ 2 ≠ 1) : qSqNum q N = 0 := by
  have hgeom := geom_sum_mul ((q : K) ^ 2) (N + 1)
  have hs : qSqNum q N = ∑ i ∈ Finset.range (N + 1), ((q : K) ^ 2) ^ i := by
    simp only [qSqNum, ← pow_mul]
  rw [← hs, ← pow_mul, h, sub_self] at hgeom
  exact (mul_eq_zero.1 hgeom).resolve_right (sub_ne_zero.2 h2)

/-- At a nontrivial root of unity every functional with `g(1) ≠ 0` fails `g ∘ X₊ = 0`. -/
theorem exists_fieldPlus_ne_zero_of_root {N : ℕ} (h : (q : K) ^ (2 * (N + 1)) = 1)
    (h2 : (q : K) ^ 2 ≠ 1) (g : OqSU2 K q →ₗ[K] K) (h1 : g 1 ≠ 0) :
    ∃ x, g (fieldPlus q x) ≠ 0 := by
  by_contra hx
  push_neg at hx
  exact qSqNum_ne_zero_of_fieldPlus q g h1 hx N (qSqNum_eq_zero_of_root q h h2)

/-- At a nontrivial root of unity there is no left-invariant functional with `g(1) ≠ 0`. -/
theorem not_leftConv_invariant_of_root {N : ℕ} (h : (q : K) ^ (2 * (N + 1)) = 1)
    (h2 : (q : K) ^ 2 ≠ 1) (g : OqSU2 K q →ₗ[K] K) (h1 : g 1 ≠ 0) :
    ¬ ∀ x, leftConv q g x = g x • 1 := by
  intro hg
  obtain ⟨x, hx⟩ := exists_fieldPlus_ne_zero_of_root q h h2 g h1
  apply hx
  show g (leftInvOp q (triFun q 0 1 0) x) = 0
  rw [pair_leftInvOp, hg, map_smul, triFun_one, smul_zero]

end Field

end QOU.FluidDynamics.HaarCoproductInvariance
