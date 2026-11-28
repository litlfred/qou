import QOU.BraidsAndKnots.RationalAssociator.AssociatorRealign

/-!
# Pentagon implies hexagon: the reduction to the Lie-algebra statement

Bean `qou-3fdg` (epic `qou-dk7p`). Furusho (*Pentagon and hexagon equations*, Ann. of Math. 171
(2010)) proves that a group-like solution of the pentagon equation satisfies the two hexagon
equations for some `μ`, with `μ² = 24·⟨φ | [A, B]⟩`. This file proves two pieces of that, both
algebraic over `ℚ` and sorry-free, and states the remaining input as a named `Prop`.

1. **Degree 2, with the parameter `μ`** (`hexagon_mu_iff`). For `φ_c = 1 + c[A, B]` and the
   exponential `exp(μx/2)`, the hexagon modulo degree 3 holds iff `(c − μ²/24)·[t₁₂, t₂₃] = 0`.
   This is Furusho's relation `μ² = 24c` at the lowest degree. (`LowDegree.hexagon_iff` is the
   case `μ = 1`.) The pentagon modulo degree 3 holds for every `c` (`LowDegree.pentagon`), so
   the pentagon does not see `μ`; the relation is what fixes it.
2. **The degree-by-degree reduction** (`assocU4_of_pentagon`). Let `ε(E) = 1` and suppose
   * `GroupLikeKAssociatorTower K E` (the existing analytic hypothesis: one group-like
     `K`-associator per level), and
   * `PentagonHexagonLie d` for every `d ≥ 3` (Furusho's Lie-algebra theorem in degree `d`,
     stated below; proved for every `d ≥ 3` in `FurushoHexagon.lean`,
     `pentagonHexagonLie_of_three_le`).
   Then a rational `Φ` with `ε(Φ) = 1`, group-like modulo `FF2 N`, satisfying **only the
   pentagon** in `U4 N`, and agreeing with an associator modulo degree 3 (`AssocU4 3 E Φ`), is
   an associator in `U4 N` (`N ≥ 3`): inversion (5.12) and the hexagon follow.

## The remaining statement

`PentagonHexagonLie d`: every homogeneous primitive (equivalently, by Friedrichs, Lie) `h` of
degree `d` whose linearised pentagon (5.20) vanishes in `U4 (d + 1)` has all of its linearised
associator equations vanish there, i.e. also (5.17) (the 2-cycle) and (5.18) (the linearised
hexagon). For `d ≥ 3` this is the Lie-algebra form of Furusho's theorem ("`grt₁` is cut out by
the pentagon"). It is **false at `d = 2`**: `h = [A, B]` satisfies (5.20) but its linearised
hexagon is `−3[t₁₂, t₂₃]` (the `c = 1, μ = 0` case of item 1). That is why the reduction starts
at degree 3 and asks for `AssocU4 3 E Φ`.

## What the reduction does not do

It does not remove `GroupLikeKAssociatorTower`. Each step compares the pentagon-only `Φ` with a
genuine associator `Φ + x` one degree up, supplied by `levelStep` from the `K`-tower; the
difference is a primitive pentagon solution of degree `d`, and `PentagonHexagonLie d` turns its
linear pentagon into the linear hexagon. Without some genuine associator to compare against, the
degree-`d` hexagon defect of `Φ` is a nonlinear quantity that this argument does not control. So
the hypothesis is not shrunk to a pentagon-only `K`-tower; what is proved is that, given the
existing tower and the Lie statement, the hexagon is redundant for rational group-like
solutions normalised in degree 2 (`assocU4_iff_pentagon`).

No analysis and no numerical value is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

/-! ### 1. Degree 2 with the parameter `μ` -/

section Mu

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- `exp(μx/2)` truncated at degree 3. -/
def expHalfMu (μ : ℚ) (x : R) : R := 1 + (μ / 2) • x + (μ ^ 2 / 8) • (x * x)

theorem expHalfMu_one (x : R) : expHalfMu 1 x = expHalf x := by
  simp [expHalfMu, expHalf]

/-- **Furusho's `μ² = 24c` modulo degree 3.** With the `𝔱₃` relations, the hexagon for
`φ_c = 1 + c[A, B]` and `exp(μx/2)` holds modulo degree 3 iff `(c − μ²/24)·[t₁₂, t₂₃] = 0`. -/
theorem hexagon_mu_iff (c μ : ℚ) {t12 t13 t23 : R} (h : Trunc3 ({t12, t13, t23} : Set R))
    (c1 : Commute t12 (t13 + t23)) (c2 : Commute t13 (t12 + t23)) :
    expHalfMu μ (t13 + t23) =
        phi c t13 t12 * expHalfMu μ t13 * phi c t23 t13 * expHalfMu μ t23 * phi c t12 t23 ↔
      (c - μ ^ 2 / 24) • (t12 * t23 - t23 * t12) = 0 := by
  unfold Trunc3 at h
  have e1 := c1.eq
  have e2 := c2.eq
  simp only [mul_add, add_mul] at e1 e2
  have e2' : t23 * t13 = t13 * t12 + t13 * t23 - t12 * t13 := by rw [e2]; simp
  have e1' : t12 * t13 = t13 * t12 + t23 * t12 - t12 * t23 := by rw [← e1]; simp
  have key :
      expHalfMu μ (t13 + t23) -
          phi c t13 t12 * expHalfMu μ t13 * phi c t23 t13 * expHalfMu μ t23 * phi c t12 t23 =
        (-3 : ℚ) • ((c - μ ^ 2 / 24) • (t12 * t23 - t23 * t12)) := by
    simp only [phi, expHalfMu, mul_add, add_mul, mul_sub, sub_mul, smul_mul_assoc,
      mul_smul_comm, one_mul, mul_one, ← mul_assoc, smul_zero, sub_zero, add_zero, smul_add,
      smul_sub, h, Set.mem_insert_iff, Set.mem_singleton_iff, true_or, or_true]
    rw [e2', e1']
    module
  rw [← sub_eq_zero, key, smul_eq_zero]
  norm_num

end Mu

/-! ### 2. Truncation maps `U4 N → U4 M` -/

section Trunc

theorem word_eq_zero_of_le_trunc {M N : ℕ} (hMN : M ≤ N) (w : List (Fin 6)) (hw : w.length = N) :
    (w.map (t M)).prod = 0 := by
  rw [← List.take_append_drop M w, List.map_append, List.prod_append,
    word_eq_zero M (w.take M) (by simp; omega), zero_mul]

/-- The truncation `U4 N → U4 M`, `M ≤ N`, sending generators to generators. -/
noncomputable def truncU4 {M N : ℕ} (hMN : M ≤ N) : U4 N →ₐ[ℚ] U4 M :=
  lift N (t M) (dk4 M) (word_eq_zero_of_le_trunc hMN)

@[simp] theorem truncU4_t {M N : ℕ} (hMN : M ≤ N) (i : Fin 6) : truncU4 hMN (t N i) = t M i :=
  by unfold truncU4; exact lift_t _ _ _ _ i

theorem truncU4_word {M N : ℕ} (hMN : M ≤ N) (w : List (Fin 6)) :
    truncU4 hMN (w.map (t N)).prod = (w.map (t M)).prod := by
  rw [map_list_prod, List.map_map]
  congr 1
  exact List.map_congr_left (fun i _ => truncU4_t hMN i)

/-- Every element of `Fil M 1` lifts to `Fil N 1`. -/
theorem exists_lift_Fil {M N : ℕ} (hMN : M ≤ N) {a : U4 M} (ha : a ∈ Fil M 1) :
    ∃ a' ∈ Fil N 1, truncU4 hMN a' = a := by
  induction ha using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, hw, rfl⟩ := hx
    exact ⟨_, word_mem_Fil w hw, truncU4_word hMN w⟩
  | zero => exact ⟨0, zero_mem _, map_zero _⟩
  | add x y _ _ hx hy =>
    obtain ⟨x', hx', rfl⟩ := hx
    obtain ⟨y', hy', rfl⟩ := hy
    exact ⟨x' + y', add_mem hx' hy', map_add _ _ _⟩
  | smul r x _ hx =>
    obtain ⟨x', hx', rfl⟩ := hx
    exact ⟨r • x', Submodule.smul_mem _ r hx', map_smul _ _ _⟩

variable {M N : ℕ} {E Φ : F2}

/-- The pentagon descends along truncation. -/
theorem pentagon_trunc (hMN : M ≤ N)
    (hp : Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)) :
    Pentagon Φ (t M 0) (t M 1) (t M 3) (t M 4) (t M 5) := by
  have := congrArg (truncU4 hMN) hp
  simpa only [map_mul, map_eval, map_add, truncU4_t] using this

/-- Associators descend along truncation. -/
theorem AssocU4.trunc (hMN : M ≤ N) (h : AssocU4 N E Φ) : AssocU4 M E Φ where
  const := h.const
  inv a b ha hb := by
    obtain ⟨a', ha', rfl⟩ := exists_lift_Fil hMN ha
    obtain ⟨b', hb', rfl⟩ := exists_lift_Fil hMN hb
    have := congrArg (truncU4 hMN) (h.inv a' b' ha' hb')
    simpa only [map_mul, map_eval, map_one] using this
  hex := by
    have := congrArg (truncU4 hMN) h.hex
    simpa only [Hexagon, map_mul, map_eval, map_add, map_zero, truncU4_t] using this
  pent := pentagon_trunc hMN h.pent

end Trunc

/-! ### 3. The Lie-algebra statement, and the reduction -/

/-- **Furusho's theorem, Lie-algebra form, in degree `d`** (the remaining input of this file).
A homogeneous primitive `h` of degree `d` (a Lie element, by Friedrichs) whose linearised pentagon
(5.20) vanishes in `U4 (d + 1)` has every linearised associator equation vanish there: (5.17) at
every pair of `Fil (d + 1) 1` and the linearised hexagon (5.18). By hand computation (not
formalised here): true at `d = 1` (the pentagon kills degree 1) and false at `d = 2`
(`h = [A, B]`: linearised pentagon zero, linearised hexagon `−3[t₁₂, t₂₃]`). For `d ≥ 3` it is
the Lie-algebra form of Furusho's theorem, proved in `FurushoHexagon.lean`
(`pentagonHexagonLie_of_three_le`); this file does not import that proof. -/
def PentagonHexagonLie (d : ℕ) : Prop :=
  ∀ h : F2, Homog d h → IsPrimitive h → (assocLin (d + 1) h).2.2 = 0 → assocLin (d + 1) h = 0

/-- The pentagon component of `assocDefect` vanishes iff the pentagon holds. -/
theorem assocDefect_pent_eq_zero {N : ℕ} {E Φ : F2}
    (hp : Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)) :
    (assocDefect N E Φ).2.2 = 0 := by
  simp only [assocDefect]
  exact sub_eq_zero.2 hp.symm

variable {K : Type*} [Field K] [Algebra ℚ K]

/-- **The reduction step.** Let `d ≥ 1`, `ε(E) = 1`, and `PentagonHexagonLie d`. If `Φ`
satisfies the level invariant at degree `d` (some group-like `K`-associator at every level
`N ≥ d + 1` agrees with `1 ⊗ Φ` modulo `FFK d`), and `Φ` satisfies the pentagon in `U4 (d + 1)`
and is group-like modulo `FF2 (d + 1)`, then `Φ` is an associator in `U4 (d + 1)`. -/
theorem assocU4_succ_of_pentagon {d : ℕ} (hd : 1 ≤ d) (hFL : PentagonHexagonLie d) {E Φ : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (h : LevelInv K E d Φ)
    (hp : Pentagon Φ (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5))
    (hg : GL (d + 1) Φ) : AssocU4 (d + 1) E Φ := by
  have hΦ := h.1
  obtain ⟨x, hx, ha, hgx, -⟩ := levelStep hE hd h
  have hA1 : Φ + x - 1 ∈ FF 1 := by
    have e : Φ + x - 1 = (Φ - algebraMap ℚ F2 (FreeAlgebra.algebraMapInv Φ)) + x := by
      rw [hΦ, map_one]; abel
    rw [e]
    exact add_mem (sub_algebraMapInv_mem_FF Φ) (FF_anti hd hx)
  have hδ : primDef (-x) ∈ FF2 (d + 1) :=
    primDef_mem_of_GL_add hd hA1 (neg_mem hx) hgx (by rwa [add_neg_cancel_right])
  obtain ⟨k, hk, hxk, hkp⟩ := exists_primitive_layer (neg_mem hx) hδ
  -- the defects of `Φ` are minus the linear terms of `x`
  have hdef : assocDefect (d + 1) E Φ = -assocLin (d + 1) x := by
    have h0 := (assocU4_iff.1 ha).2
    rw [assocDefect_add hd hE hΦ hx] at h0
    exact eq_neg_of_add_eq_zero_left h0
  have hlk : assocLin (d + 1) k = -assocLin (d + 1) x := by
    have e : k = -x - (-x - k) := by abel
    rw [e, map_sub, assocLin_eq_zero_of_mem_FF hxk, sub_zero, map_neg]
  have hpk : (assocLin (d + 1) k).2.2 = 0 := by
    rw [hlk, ← hdef]; exact assocDefect_pent_eq_zero hp
  have hk0 := hFL k hk hkp hpk
  refine assocU4_iff.2 ⟨hΦ, ?_⟩
  have hx0 : assocLin (d + 1) x = 0 := by rw [← neg_eq_zero, ← hlk, hk0]
  rw [hdef, hx0, neg_zero]

/-- A level invariant at degree `d` for `Φ'` transfers to `Φ ≡ Φ' (mod FF d)`. -/
theorem LevelInv.congr {E Φ Φ' : F2} {d : ℕ} (h : LevelInv K E d Φ')
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) (hmod : Φ - Φ' ∈ FF d) : LevelInv K E d Φ := by
  refine ⟨hΦ, fun N hN => ?_⟩
  obtain ⟨Ψ, hK, hGL, hm⟩ := h.2 N hN
  refine ⟨Ψ, hK, hGL, ?_⟩
  have e : Ψ - (1 : K) ⊗ₜ Φ = (Ψ - (1 : K) ⊗ₜ Φ') - (1 : K) ⊗ₜ (Φ - Φ') := by
    rw [tmul_sub]; abel
  rw [e]
  exact sub_mem hm (tmul_mem_FFK _ hmod)

/-- If `Φ` is already an associator one degree up, the level invariant moves up with it
(`realign` with the prescribed correction `0`). -/
theorem LevelInv.succ_of_assoc {E Φ : F2} {d : ℕ} (hd : 1 ≤ d)
    (hE : FreeAlgebra.algebraMapInv E = 1) (h : LevelInv K E d Φ) (ha : AssocU4 (d + 1) E Φ)
    (hg : GL (d + 1) Φ) : LevelInv K E (d + 1) Φ := by
  refine ⟨h.1, fun N hN => ?_⟩
  obtain ⟨Ψ, hK, hGL, hm⟩ := h.2 N (by omega)
  obtain ⟨Ψ', hK', hGL', hm'⟩ := realign (x := 0) hd (by omega) hE h.1 (zero_mem _)
    (by rwa [add_zero]) (by rwa [add_zero]) hK hGL hm
  exact ⟨Ψ', hK', hGL', by rwa [add_zero] at hm'⟩

/-- The level invariant at degree 3 for any `Φ` that is an associator modulo degree 3 and
group-like modulo `FF2 3`, given the `K`-tower. -/
theorem levelInv_three {E Φ : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) (h3 : AssocU4 3 E Φ) (hg : GL 3 Φ) :
    LevelInv K E 3 Φ := by
  have h₀ : LevelInv K E 1 1 := by
    refine ⟨map_one _, fun N hN => ?_⟩
    obtain ⟨Ψ, hK, hGL⟩ := hT.exists_assoc N hN
    refine ⟨Ψ, hK, hGL, ?_⟩
    rw [← Algebra.TensorProduct.one_def]
    exact hK.sub_one_mem_FFK
  have h1 : LevelInv K E 1 Φ := by
    refine h₀.congr h3.const ?_
    have := sub_algebraMapInv_mem_FF Φ
    rwa [h3.const, map_one] at this
  have h2 : LevelInv K E 2 Φ :=
    h1.succ_of_assoc le_rfl hE (h3.trunc (by omega)) (FF2_anti (by omega) hg)
  exact h2.succ_of_assoc (by omega) hE h3 hg

/-- **Pentagon implies hexagon, modulo the Lie statement.** Let `ε(E) = 1`, `N ≥ 3`, and assume
`GroupLikeKAssociatorTower K E` and `PentagonHexagonLie d` for all `d ≥ 3`. A rational `Φ`,
group-like modulo `FF2 N`, satisfying the pentagon in `U4 N`, and an associator modulo degree 3,
is an associator in `U4 N`: (5.12) and the hexagon hold. -/
theorem assocU4_of_pentagon {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) (hFL : ∀ d, 3 ≤ d → PentagonHexagonLie d)
    {N : ℕ} (hN : 3 ≤ N) {Φ : F2} (h3 : AssocU4 3 E Φ)
    (hp : Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)) (hg : GL N Φ) :
    AssocU4 N E Φ := by
  have key : ∀ d, 3 ≤ d → d ≤ N → AssocU4 d E Φ ∧ LevelInv K E d Φ := by
    intro d hd
    induction d, hd using Nat.le_induction with
    | base => exact fun _ => ⟨h3, levelInv_three hE hT h3 (FF2_anti hN hg)⟩
    | succ d hd ih =>
      intro hdN
      obtain ⟨-, hL⟩ := ih (by omega)
      have hg' : GL (d + 1) Φ := FF2_anti hdN hg
      have ha := assocU4_succ_of_pentagon (by omega) (hFL d hd) hE hL
        (pentagon_trunc hdN hp) hg'
      exact ⟨ha, hL.succ_of_assoc (by omega) hE ha hg'⟩
  exact (key N hN le_rfl).1

/-- **The hexagon is redundant for group-like solutions normalised in degree 2**, under the same
hypotheses: for `N ≥ 3` and `Φ` group-like modulo `FF2 N`, `Φ` is an associator in `U4 N` iff it
satisfies the pentagon in `U4 N` and is an associator modulo degree 3. -/
theorem assocU4_iff_pentagon {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) (hFL : ∀ d, 3 ≤ d → PentagonHexagonLie d)
    {N : ℕ} (hN : 3 ≤ N) {Φ : F2} (hg : GL N Φ) :
    AssocU4 N E Φ ↔
      AssocU4 3 E Φ ∧ Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5) :=
  ⟨fun h => ⟨h.trunc hN, h.pent⟩, fun h => assocU4_of_pentagon hE hT hFL hN h.1 h.2 hg⟩

end QOU.BraidsAndKnots.RationalAssociator
