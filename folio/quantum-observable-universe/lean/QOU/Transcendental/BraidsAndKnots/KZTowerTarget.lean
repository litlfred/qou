import QOU.BraidsAndKnots.RationalAssociator.FurushoSingleLevel
import QOU.BraidsAndKnots.RationalAssociator.PentagonObstruction
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.RingTheory.Ideal.Quotient.Operations

/-!
# The KZ fallback for a rational associator: what the descent actually needs

The descent `rational_associator_of_tower` (`RationalAssociator/AssociatorChain.lean`) turns a
`GroupLikeKAssociatorTower K E` into rational associators modulo every `N`. That hypothesis
fixes **one** polynomial `E ∈ ℚ⟨X, Y⟩` for all levels `N`. This file shows, algebraically,
that for the exponential case this cannot be met by the KZ associator, or by anything else,
states the per-level hypothesis the KZ associator does provide, and discharges it at the
levels where it can be proved here.

1. **A fixed polynomial `E` gives no tower at `μ ≠ 0`.**
   `hexagon_sq_eq`: if `Φ` is an associator in `U4 N` for `E`, then in every commutative
   `ℚ`-algebra, for every `y` with `y ^ N = 0`, `(E(2y))² = (E(y))⁴`, where `E(x) = eval x 0 E`.
   (Send every generator `tᵢⱼ` to `y`: the hexagon becomes `E(2y) = F·E(y)·F·E(y)·F` with
   `F = Φ(y, y)`, and inversion gives `F² = 1`.) For `expHalfPoly = 1 + X/2 + X²/8` this fails
   at `y = 8z`, `z⁴ = 0`, `z³ ≠ 0`, so `not_assocU4_expHalfPoly`: there is **no** associator for
   `expHalfPoly` in `U4 N`, `N ≥ 4`, and `not_groupLikeKAssociatorTower_expHalfPoly`: the tower
   hypothesis for `expHalfPoly` is false over every field `K`. The tower can hold only if
   `E(2y)² = E(y)⁴` for nilpotent `y` of every order (`tower_forces_square_law`). Informally
   that makes `x ↦ E(x, 0)` an exact exponential power series, which a polynomial is only
   when it is `1` (`μ = 0`); that general statement is argued here, not formalized. What is
   formalized is the `expHalfPoly` case.
2. **The per-level target.** `expHalfTrunc N = Σ_{k<N} X^k / (2^k k!)` is `exp(X/2)` truncated
   at degree `N`, which is exact in `U4 N`. `KZAssociatorExists K` asks, for every `N ≥ 2`, for
   a group-like `K`-associator for `expHalfTrunc N` modulo `N`. This is what Drinfeld's KZ
   associator `Φ_KZ` provides over `ℂ` (after rescaling its arguments by `2πi`); it is a named
   hypothesis with content, **not proved here**.
3. **Low levels, unconditionally.** `assocU4_three`, `GL_three`: `φ = 1 + [X, Y]/24` is a
   rational associator for `expHalfTrunc 3 = expHalfPoly` modulo `3` and group-like modulo
   `FF2 3`. Hence `kzLevel_three`: the field of `KZAssociatorExists` holds at `N = 3`
   over every field `K`, with no analysis.
4. **The descent, conditional.** `rational_associator_of_kz`: under `[KZAssociatorExists K]`,
   for every `N ≥ 2` there is a rational `Φ`, an associator for `expHalfTrunc N` modulo `N`,
   group-like modulo `FF2 N`. This is conditional on the class and is not called proved.

Nothing in this file is analytic: no limit, integral, `exp`, `π` or `ζ`. It sits behind the
transcendental boundary because it is the interface to the analytic KZ construction
(`AssociatorKZ.lean`, `DrinfeldAssociator.lean`), which is what an instance of
`KZAssociatorExists ℂ` would be built from. Audit:
`docs/audits/2026-11-27-grt-action-pentagon-derivation.md` §17o.
-/

namespace QOU.Transcendental.KZTowerTarget

open QOU.BraidsAndKnots.RationalAssociator TensorProduct Friedrichs Polynomial

local notation "F2" => FreeAlgebra ℚ (Fin 2)

/-! ### 1. The hexagon on a single nilpotent element -/

/-- Sending all six generators of `U4 N` to one element `y` with `y ^ N = 0` of a commutative
`ℚ`-algebra. -/
noncomputable def diagMap {C : Type*} [CommRing C] [Algebra ℚ C] (N : ℕ) (y : C)
    (hy : y ^ N = 0) : U4 N →ₐ[ℚ] C :=
  lift N (fun _ => y)
    ⟨Commute.all _ _, Commute.all _ _, Commute.all _ _, Commute.all _ _, Commute.all _ _,
      Commute.all _ _, Commute.all _ _, Commute.all _ _, Commute.all _ _, Commute.all _ _,
      Commute.all _ _, Commute.all _ _, Commute.all _ _, Commute.all _ _, Commute.all _ _⟩
    (fun w hw => by rw [List.map_const', List.prod_replicate, hw, hy])

/-- **The hexagon forces `E(2y)² = E(y)⁴`.** If `Φ` is an associator in `U4 N` for `E`, then
for every `y` with `y ^ N = 0` in a commutative `ℚ`-algebra, `(eval (y + y) 0 E)² =
(eval y 0 E)⁴`. -/
theorem hexagon_sq_eq {C : Type*} [CommRing C] [Algebra ℚ C] {N : ℕ} {E Φ : F2}
    (h : AssocU4 N E Φ) (y : C) (hy : y ^ N = 0) :
    (eval (y + y) 0 E) ^ 2 = (eval y 0 E) ^ 4 := by
  set f := diagMap N y hy
  have ht : ∀ i, f (t N i) = y := fun i => lift_t _ _ _ _ i
  have hx := congrArg f h.hex
  simp only [map_mul, QOU.BraidsAndKnots.RationalAssociator.map_eval, map_add, map_zero,
    ht] at hx
  have hi := congrArg f (h.inv (t N 0) (t N 0) (t_mem_Fil_one 0) (t_mem_Fil_one 0))
  simp only [map_mul, QOU.BraidsAndKnots.RationalAssociator.map_eval, map_one, ht] at hi
  set F := eval y y Φ
  set e := eval y 0 E
  linear_combination (eval (y + y) 0 E + F * e * F * e * F) * hx + (e ^ 4 * (F ^ 4 + F ^ 2 + 1)) * hi

/-- `expHalfPoly` has constant term `1`. -/
theorem algebraMapInv_expHalfPoly : FreeAlgebra.algebraMapInv expHalfPoly = 1 := by
  simp [expHalfPoly, FreeAlgebra.algebraMapInv]

/-- The test algebra `ℚ[X]/(X⁴)` and its element `z = X`. -/
private abbrev Tst := Polynomial ℚ ⧸ Ideal.span {(X : ℚ[X]) ^ 4}

private theorem z_pow_four : (Ideal.Quotient.mk _ X : Tst) ^ 4 = 0 := by
  rw [← map_pow, Ideal.Quotient.eq_zero_iff_mem]
  exact Ideal.mem_span_singleton_self _

private theorem z_pow_three_ne : (Ideal.Quotient.mk _ X : Tst) ^ 3 ≠ 0 := by
  rw [← map_pow, Ne, Ideal.Quotient.eq_zero_iff_mem, Ideal.mem_span_singleton]
  intro hd
  have := Polynomial.natDegree_le_of_dvd hd (pow_ne_zero 3 X_ne_zero)
  simp at this

private theorem expHalf_eight_mul {C : Type*} [CommRing C] [Algebra ℚ C] (z : C) :
    expHalf ((8 : C) * z) = 1 + 4 * z + 8 * (z * z) := by
  unfold expHalf
  rw [Algebra.smul_def, Algebra.smul_def]
  have h1 : algebraMap ℚ C (1 / 2) * (8 * z) = 4 * z := by
    rw [← mul_assoc, ← map_ofNat (algebraMap ℚ C) 8, ← map_mul]; norm_num
    exact congrArg (· * z) (map_ofNat (algebraMap ℚ C) 4)
  have h2 : algebraMap ℚ C (1 / 8) * (8 * z * (8 * z)) = 8 * (z * z) := by
    rw [show (8 : C) * z * (8 * z) = 64 * (z * z) by ring, ← mul_assoc,
      ← map_ofNat (algebraMap ℚ C) 64, ← map_mul]; norm_num
    exact congrArg (· * (z * z)) (map_ofNat (algebraMap ℚ C) 8)
  rw [h1, h2]

/-- **No associator for `expHalfPoly` modulo `N ≥ 4`.** The hexagon with the degree-2
polynomial `1 + X/2 + X²/8` in place of `exp(X/2)` has no solution in `U4 N` once words of
length `3` survive. -/
theorem not_assocU4_expHalfPoly {N : ℕ} (hN : 4 ≤ N) (Φ : F2) :
    ¬ AssocU4 N expHalfPoly Φ := by
  intro h
  set z : Tst := Ideal.Quotient.mk _ X
  have hz4 : z ^ 4 = 0 := z_pow_four
  have hy : ((8 : Tst) * z) ^ N = 0 := by
    obtain ⟨k, rfl⟩ : ∃ k, N = 4 + k := ⟨N - 4, by omega⟩
    rw [mul_pow, pow_add z, hz4]; simp
  have key := hexagon_sq_eq h _ hy
  rw [eval_expHalfPoly, eval_expHalfPoly,
    show (8 : Tst) * z + 8 * z = 8 * (2 * z) by ring, expHalf_eight_mul,
    expHalf_eight_mul] at key
  have h128 : (128 : Tst) * z ^ 3 = 0 := by
    linear_combination (-1 : Tst) * key -
      (1152 + 5120 * z + 8192 * z ^ 2 + 8192 * z ^ 3 + 4096 * z ^ 4) * hz4
  have hinv : algebraMap ℚ Tst (1 / 128) * 128 = 1 := by
    rw [← map_ofNat (algebraMap ℚ Tst) 128, ← map_mul]; norm_num
  have h3 : z ^ 3 = 0 := by
    linear_combination algebraMap ℚ Tst (1 / 128) * h128 - z ^ 3 * hinv
  exact z_pow_three_ne h3

variable {K : Type*} [Field K] [Algebra ℚ K]

/-- **The fixed-`E` tower is false for `expHalfPoly`, over every field `K`.** By the descent,
a tower would give a rational associator for `expHalfPoly` modulo `4`, which
`not_assocU4_expHalfPoly` excludes. -/
theorem not_groupLikeKAssociatorTower_expHalfPoly :
    ¬ GroupLikeKAssociatorTower K expHalfPoly := by
  intro hT
  obtain ⟨Φ, hA, -⟩ := rational_associator_of_tower algebraMapInv_expHalfPoly hT
    (by norm_num : 2 ≤ 4)
  exact not_assocU4_expHalfPoly le_rfl Φ hA

/-- **The single-level form at level `4`, over every field `K`**: no group-like
`K`-associator for `expHalfPoly` modulo `4`. -/
theorem not_exists_assocK_expHalfPoly_four :
    ¬ ∃ Ψ : K ⊗[ℚ] F2, AssocK K 4 expHalfPoly Ψ ∧ GLK K 4 Ψ := by
  rintro ⟨Ψ, hK, hG⟩
  obtain ⟨Φ, hA, -⟩ := rational_associator_of_groupLikeK (by norm_num : 2 ≤ 4)
    algebraMapInv_expHalfPoly hK hG
  exact not_assocU4_expHalfPoly le_rfl Φ hA

/-- **What any tower forces on `E`.** If a tower exists for `E` over some field `K` and `E` has
constant term `1`, then `E(2y)² = E(y)⁴` for every nilpotent `y` of every commutative
`ℚ`-algebra. -/
theorem tower_forces_square_law {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {C : Type*} [CommRing C] [Algebra ℚ C] (y : C)
    {N : ℕ} (hy : y ^ N = 0) : (eval (y + y) 0 E) ^ 2 = (eval y 0 E) ^ 4 := by
  have hy' : y ^ (N + 2) = 0 := by rw [pow_add, hy, zero_mul]
  obtain ⟨Φ, hA, -⟩ := rational_associator_of_tower hE hT (by omega : 2 ≤ N + 2)
  exact hexagon_sq_eq hA y hy'

/-! ### 2. The per-level exponential and the KZ hypothesis -/

/-- `exp(X/2)` truncated at degree `N`: `Σ_{k<N} X^k / (2^k k!)`. In `U4 N` (words of length
`N` vanish) its evaluations are those of the full exponential. -/
noncomputable def expHalfTrunc (N : ℕ) : F2 :=
  ∑ k ∈ Finset.range N, ((2 ^ k * k.factorial : ℕ) : ℚ)⁻¹ • FreeAlgebra.ι ℚ 0 ^ k

theorem expHalfTrunc_three : expHalfTrunc 3 = expHalfPoly := by
  simp only [expHalfTrunc, expHalfPoly, Finset.sum_range_succ, Finset.sum_range_zero]
  norm_num [Nat.factorial, pow_two]

theorem algebraMapInv_expHalfTrunc {N : ℕ} (hN : 1 ≤ N) :
    FreeAlgebra.algebraMapInv (expHalfTrunc N) = 1 := by
  obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
  rw [expHalfTrunc, map_sum, Finset.sum_range_succ', Finset.sum_eq_zero (fun i _ => ?_), zero_add]
  · simp [FreeAlgebra.algebraMapInv]
  · simp [pow_succ, FreeAlgebra.algebraMapInv]

variable (K) in
/-- **The KZ hypothesis, per level.** For every `N ≥ 2` there is a `K`-associator modulo `N`
for the exponential `expHalfTrunc N`, group-like modulo `FF2K N`. For `K = ℂ` this is the
content of Drinfeld's theorem that `Φ_KZ(t/(2πi))` satisfies inversion, the pentagon and the
hexagon with `e^{t/2}` and is group-like; that theorem is **not** proved in this repository in
this form (`AssociatorKZ.lean` builds `Φ_KZ` as an evaluated connection matrix, not as an element
of `ℂ ⊗ ℚ⟨X, Y⟩` modulo degree `N`). No instance is declared. -/
class KZAssociatorExists : Prop where
  exists_assoc : ∀ N : ℕ, 2 ≤ N →
    ∃ Ψ : K ⊗[ℚ] F2, AssocK K N (expHalfTrunc N) Ψ ∧ GLK K N Ψ

/-! ### 3. Level `3`, unconditionally -/

/-- The commutator of two primitive elements is primitive. -/
theorem IsPrimitive.commutator {p q : F2} (hp : IsPrimitive p) (hq : IsPrimitive q) :
    IsPrimitive (p * q - q * p) := by
  unfold IsPrimitive at *
  rw [map_sub, map_mul, map_mul, hp, hq]
  simp only [add_mul, mul_add, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul,
    sub_tmul, tmul_sub]
  abel

theorem isPrimitive_ι (i : Fin 2) : IsPrimitive (FreeAlgebra.ι ℚ i) := by
  unfold IsPrimitive; exact cop_g i

/-- `[X, Y]` lies in `FF 2`. -/
theorem commutator_mem_FF2 :
    FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 - FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0 ∈ FF 2 :=
  sub_mem (mul_mem_FF' (a := 1) (b := 1) (c := 2) rfl (ι_mem_FF_one 0) (ι_mem_FF_one 1))
    (mul_mem_FF' (a := 1) (b := 1) (c := 2) rfl (ι_mem_FF_one 1) (ι_mem_FF_one 0))

/-- `φ_c = 1 + c·[X, Y]` is group-like modulo `FF2 3`, for every `c`. -/
theorem GL_three (c : ℚ) : GL 3 (phiPoly c) := by
  have hp : IsPrimitive (c • (FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 -
      FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0)) :=
    Friedrichs.IsPrimitive.smul
      (IsPrimitive.commutator (isPrimitive_ι 0) (isPrimitive_ι 1)) c
  exact GL.add_primitive (d := 2) (by norm_num) (map_one _) (GL_one 3)
    (Submodule.smul_mem _ c commutator_mem_FF2) hp

/-- In `U4 3`, any set of elements of filtration `≥ 1` has vanishing triple products. -/
private theorem trunc3_of_fil {S : Set (U4 3)} (hS : ∀ w ∈ S, w ∈ Fil 3 1) : Trunc3 S :=
  fun hx hy hz => eq_zero_of_mem_Fil (mul_mem_Fil' (a := 2) (b := 1) (c := 3) rfl
    (mul_mem_Fil' (a := 1) (b := 1) (c := 2) rfl (hS _ hx) (hS _ hy)) (hS _ hz))

/-- **A rational associator modulo `3`**: `1 + [X, Y]/24` for `expHalfPoly`. -/
theorem assocU4_three : AssocU4 3 expHalfPoly (phiPoly (1 / 24)) where
  const := by simp [phiPoly, FreeAlgebra.algebraMapInv]
  inv := fun a b ha hb => by
    rw [eval_phiPoly, eval_phiPoly]
    refine inversion _ (trunc3_of_fil ?_)
    intro w hw; rcases hw with rfl | rfl <;> assumption
  hex := by
    have dk := dk4 3
    have hT : Trunc3 ({t 3 0, t 3 1, t 3 3} : Set (U4 3)) := by
      refine trunc3_of_fil ?_
      intro w hw; rcases hw with rfl | rfl | rfl <;> exact t_mem_Fil_one _
    rw [hexagon_expHalfPoly_iff, hexagon_iff _ hT dk.n12_3 dk.n13_2]
    simp
  pent := by
    refine pentagon_phiPoly _ (trunc3_of_fil ?_) (dk4 3)
    intro w hw; rcases hw with rfl | rfl | rfl | rfl | rfl | rfl <;> exact t_mem_Fil_one _

/-- **The KZ field at level `3`, with no analysis.** Over every field `K` there is a
group-like `K`-associator modulo `3` for `expHalfTrunc 3`: the base change of `1 + [X, Y]/24`. -/
theorem kzLevel_three :
    ∃ Ψ : K ⊗[ℚ] F2, AssocK K 3 (expHalfTrunc 3) Ψ ∧ GLK K 3 Ψ := by
  rw [expHalfTrunc_three]
  exact ⟨(1 : K) ⊗ₜ phiPoly (1 / 24), assocK_of_assocU4 assocU4_three, GLK_of_GL (GL_three _)⟩

/-! ### 4. The descent, conditional on the KZ hypothesis -/

/-- **Rational associators modulo every `N ≥ 2`, conditional on `KZAssociatorExists K`.**
For the per-level exponential `expHalfTrunc N` there is a rational associator modulo `N`,
group-like modulo `FF2 N`. Conditional; the class has no instance in this repository. -/
theorem rational_associator_of_kz [KZAssociatorExists K] {N : ℕ} (hN : 2 ≤ N) :
    ∃ Φ : F2, AssocU4 N (expHalfTrunc N) Φ ∧ GL N Φ := by
  obtain ⟨Ψ, hK, hG⟩ := KZAssociatorExists.exists_assoc (K := K) N hN
  exact rational_associator_of_groupLikeK hN (algebraMapInv_expHalfTrunc (by omega)) hK hG

end QOU.Transcendental.KZTowerTarget
