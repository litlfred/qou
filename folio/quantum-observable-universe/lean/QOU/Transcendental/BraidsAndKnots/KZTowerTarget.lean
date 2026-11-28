import QOU.BraidsAndKnots.RationalAssociator.ExpHalfTrunc
import QOU.BraidsAndKnots.RationalAssociator.PentagonObstruction
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.RingTheory.Ideal.Quotient.Operations

/-!
# The KZ fallback for a rational associator: what the descent actually needs

The descent `rational_associator_of_tower` (`RationalAssociator/AssociatorChain.lean`) turns a
`GroupLikeKAssociatorTower K E` into rational associators modulo every `N`. Since 2026-11-28
(owner ruling, audit §17p) the tower takes a **per-level** exponential `E : ℕ → F2` with
`ExpFamily E`. This file records why the previous fixed-`E` form could not be met for the
exponential, and states the KZ hypothesis in the per-level form.

1. **A fixed polynomial `E` gives no tower at `μ ≠ 0`.**
   `hexagon_sq_eq`: if `Φ` is an associator in `U4 N` for `E`, then in every commutative
   `ℚ`-algebra, for every `y` with `y ^ N = 0`, `(E(2y))² = (E(y))⁴`, where `E(x) = eval x 0 E`.
   (Send every generator `tᵢⱼ` to `y`: the hexagon becomes `E(2y) = F·E(y)·F·E(y)·F` with
   `F = Φ(y, y)`, and inversion gives `F² = 1`.) For `expHalfPoly = 1 + X/2 + X²/8` this fails
   at `y = 8z`, `z⁴ = 0`, `z³ ≠ 0`, so `not_assocU4_expHalfPoly`: there is **no** associator for
   `expHalfPoly` in `U4 N`, `N ≥ 4`, and `not_groupLikeKAssociatorTower_expHalfPoly`: the
   constant tower `fun _ => expHalfPoly` is false over every field `K`.
   `tower_forces_square_law`: for any compatible family, `E_M(2y)² = E_M(y)⁴` whenever
   `y ^ N = 0`, `N ≤ M`. For a constant family this forces the square law at every nilpotency
   order (informally: `E = 1`); for `expHalfTrunc` it is consistent, since `expHalfTrunc M` is the
   exponential modulo degree `M`.
2. **The per-level target.** `expHalfTrunc N = Σ_{k<N} X^k / (2^k k!)`
   (`RationalAssociator/ExpHalfTrunc.lean`). `KZAssociatorExists K` asks, for every `N ≥ 2`, for
   a group-like `K`-associator for `expHalfTrunc N` modulo `N`; `kzAssociatorExists_iff_tower`:
   this is exactly `GroupLikeKAssociatorTower K expHalfTrunc`. It is what Drinfeld's KZ associator
   provides over `ℂ` (after rescaling by `2πi`); it is a named hypothesis with content,
   **not proved here**, and no instance is declared.
3. **Low levels, unconditionally** (in `ExpHalfTrunc.lean`). `assocU4_three`, `GL_three`,
   `kzLevel_three`: `1 + [X, Y]/24` at level `3`.
4. **The descent, conditional.** `rational_associator_of_kz`: under `[KZAssociatorExists K]`,
   for every `N ≥ 2` there is a rational `Φ`, an associator for `expHalfTrunc N` modulo `N`,
   group-like modulo `FF2 N`, obtained from `rational_associator_of_tower expFamily_expHalfTrunc`.
   Conditional on the class; not called proved.

Nothing in this file is analytic: no limit, integral, `exp`, `π` or `ζ`. It sits behind the
transcendental boundary because it is the interface to the analytic KZ construction
(`AssociatorKZ.lean`, `DrinfeldAssociator.lean`), which is what an instance of
`KZAssociatorExists ℂ` would be built from. Audit:
`docs/audits/2026-11-27-grt-action-pentagon-derivation.md` §17o, §17p.
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
    ¬ GroupLikeKAssociatorTower K (fun _ => expHalfPoly) := by
  intro hT
  obtain ⟨Φ, hA, -⟩ := rational_associator_of_tower (expFamily_const algebraMapInv_expHalfPoly) hT
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

/-- **What any tower forces on its exponentials.** If a tower exists over some field `K` for a
compatible family `E`, then at every level `M ≥ 2` and for every `y` with `y ^ N = 0`, `N ≤ M`,
in every commutative `ℚ`-algebra, `E_M(2y)² = E_M(y)⁴`. For a constant family `E` this is the
square law on `E` for nilpotents of every order. -/
theorem tower_forces_square_law {E : ℕ → F2} (hE : ExpFamily E)
    (hT : GroupLikeKAssociatorTower K E) {C : Type*} [CommRing C] [Algebra ℚ C] (y : C)
    {N M : ℕ} (hy : y ^ N = 0) (hNM : N ≤ M) (hM : 2 ≤ M) :
    (eval (y + y) 0 (E M)) ^ 2 = (eval y 0 (E M)) ^ 4 := by
  have hy' : y ^ M = 0 := by
    obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hNM
    rw [pow_add, hy, zero_mul]
  obtain ⟨Φ, hA, -⟩ := rational_associator_of_tower hE hT hM
  exact hexagon_sq_eq hA y hy'

/-! ### 2. The KZ hypothesis, per level

The per-level exponential `expHalfTrunc`, its compatibility `expFamily_expHalfTrunc` and the
unconditional level-`3` results now live in `RationalAssociator/ExpHalfTrunc.lean`. -/

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

/-- **The KZ hypothesis is the per-level tower.** `KZAssociatorExists K` is exactly
`GroupLikeKAssociatorTower K expHalfTrunc`. -/
theorem KZAssociatorExists.tower [KZAssociatorExists K] :
    GroupLikeKAssociatorTower K expHalfTrunc :=
  ⟨KZAssociatorExists.exists_assoc⟩

theorem kzAssociatorExists_iff_tower :
    KZAssociatorExists K ↔ GroupLikeKAssociatorTower K expHalfTrunc :=
  ⟨fun _ => KZAssociatorExists.tower, fun h => ⟨h.exists_assoc⟩⟩

/-! ### 3. The descent, conditional on the KZ hypothesis -/

/-- **Rational associators modulo every `N ≥ 2`, conditional on `KZAssociatorExists K`.**
For the per-level exponential `expHalfTrunc N` there is a rational associator modulo `N`,
group-like modulo `FF2 N`. Conditional; the class has no instance in this repository. -/
theorem rational_associator_of_kz [KZAssociatorExists K] {N : ℕ} (hN : 2 ≤ N) :
    ∃ Φ : F2, AssocU4 N (expHalfTrunc N) Φ ∧ GL N Φ :=
  rational_associator_of_tower expFamily_expHalfTrunc (KZAssociatorExists.tower (K := K)) hN

end QOU.Transcendental.KZTowerTarget
