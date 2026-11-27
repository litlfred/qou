import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Group.Defs
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Symmetry-Reduced LP/SDP Dual Certificates, Extremal-Functional Uniqueness, Finite-`A` Chamber Kinks, and Graver Test-Set Optimality

Reusable substrate-side (§7c generic ordered-algebra) formalization backing QOU's
arbitrary-precision LP/SDP witness pipeline (`clarabel-mpfr` → `.witness.json` →
exact rational Lean 4 verification), extremal-functional discrete selection,
isotypic Young-diagram block collapse, finite-`A` magic-shell shadow-price kinks,
and Layer-2 Sturmfels–Thomas / Graver chamber optimality:

1. **Section 1 — Weak LP Duality & Zero-Trust Optimality Certificates**
   (`lp_duality_gap_decomposition`, `lp_primal_lower_bound_of_dual`,
   `lp_optimal_of_zero_gap`): once a rationalized dual multiplier `u` satisfies
   `Aᵀ u ≤ c`, weak duality holds over any linearly ordered commutative ring `R`,
   requiring zero trust in the external floating/MPFR interior-point solver.
2. **Section 2 — Extremal-Functional / Strict Complementary-Slackness Uniqueness**
   (`complementary_slackness_of_zero_gap`, `unique_support_of_strict_dual_slack`,
   `unique_primal_of_strict_dual_slack`, `simplex_unique_optimal_of_strict_dual_slack`):
   if `u*` achieves zero duality gap against `x*` and every index `i ∉ S` has
   strictly positive dual slack `cᵢ - (Aᵀ u*)ᵢ > 0`, then **every** optimal primal
   solution `x ≥ 0` vanishes identically outside `S`; when `S = {i₀}` with a
   normalising row `A_{k₀, i₀} ≠ 0`, the optimal primal state is **algebraically unique**.
3. **Section 3 — Gatermann–Parrilo / Delsarte–Schrijver Isotypic Block Collapse**
   (`central_cone_iff_character_weights_nonneg`, `central_idempotent_pairing_nonneg_iff`):
   a central tuple `y : Λ → R` is trace-nonnegative against all Wedderburn block
   squares `∑_λ y_λ tr(M_λᵀ M_λ)` (and against orthogonal central idempotent squares)
   if and only if `0 ≤ y_λ` on every active block `λ`, collapsing matrix SDP
   positivity to scalar partition inequalities.
4. **Section 4 — Finite-`A` Parametric LP Concavity & Shadow-Price Kink Jumps**
   (`piecewise_linear_concave_of_parametric_lp`,
   `piecewise_linear_kink_shadow_price_jump`, `exists_chamber_neighborhood_kink_jump`):
   `E(θ) = min_{i ∈ F} (aᵢ + bᵢ θ)` over a finite nonempty set `F` is concave
   piecewise-linear, and at a chamber wall `θ*` where optimal branch switches from
   `i` (`bᵢ`) to `j` (`bⱼ < bᵢ`), the left and right shadow prices jump strictly
   by `bᵢ - bⱼ > 0` at finite `|F|`, requiring no Lee–Yang `N → ∞` limit.
5. **Section 5 — Graver / Sturmfels–Thomas Test-Set Global Integer Optimality**
   (`graver_test_set_certifies_global_ip_min`,
   `graver_test_set_certifies_strict_global_ip_min`): over any linearly ordered
   additive commutative group `R`, nonnegative conformal/test-set decompositions
   `u - u* = ∑_r n_r g_r` (`n_r ∈ ℕ`) with `0 ≤ c · g_r` certify global integer
   optimality `c · u* ≤ c · u` across the entire chamber.

-- Ref: [farkas1902] Gyula Farkas, J. Reine Angew. Math. 124 (1902) 1–27.
-- Ref: [kantorovich1939] Leonid V. Kantorovich, Matematicheskie metody organizatsii i planirovaniya proizvodstva (1939).
-- Ref: [viazovska2017] Maryna S. Viazovska, Ann. of Math. 185 (2017) 991–1016.
-- Ref: [elshowk2012] Sheer El-Showk et al., Phys. Rev. D 86 (2012) 025022.
-- Ref: [gatermann-parrilo2004] Karin Gatermann and Pablo A. Parrilo, J. Pure Appl. Algebra 192 (2004) 95–128.
-- Ref: [schrijver2005] Alexander Schrijver, IEEE Trans. Inform. Theory 51 (2005) 2859–2866.
-- Ref: [perdew-parr-levy-balduz1982] John P. Perdew, Robert G. Parr, Mel Levy, and Jose L. Balduz Jr., Phys. Rev. Lett. 49 (1982) 1691–1694.
-- Ref: [sturmfels-thomas1997] Bernd Sturmfels and Rekha R. Thomas, Math. Programming 77 (1997) 357–387.
-- Ref: [graver1975] Jack E. Graver, Math. Programming 9 (1975) 207–226.
-- Ref: [dvorak-kolmogorov2024] Martin Dvorak and Vladimir Kolmogorov, arXiv:2409.08119 (2024).
-/

namespace QOU.MathlibInfra

open scoped BigOperators

/-! ## §1. Weak LP Duality and Zero-Trust Optimality Certificates -/

section WeakDualityAndOptimality

variable {m n : Type*} [Fintype m] [Fintype n]

/-- Dual slack at column `i`: `cᵢ - (Aᵀ u)ᵢ = cᵢ - ∑ₖ Aₖᵢ uₖ`. -/
def dualSlack {R : Type*} [CommRing R] (A : m → n → R) (c : n → R) (u : m → R) (i : n) : R :=
  c i - ∑ k, A k i * u k

/-- **Exact algebraic duality-gap decomposition.**
Whenever `A x = b` row-wise, the primal–dual objective gap equals the inner product
of the dual slack vector `c - Aᵀ u` with `x`:
`∑ᵢ cᵢ xᵢ - ∑ₖ bₖ uₖ = ∑ᵢ (cᵢ - ∑ₖ Aₖᵢ uₖ) xᵢ`. -/
theorem lp_duality_gap_decomposition {R : Type*} [CommRing R]
    (A : m → n → R) (b : m → R) (c : n → R) (x : n → R) (u : m → R)
    (heq : ∀ k, ∑ i, A k i * x i = b k) :
    (∑ i, c i * x i) - (∑ k, b k * u k) = ∑ i, dualSlack A c u i * x i := by
  have hbu : ∑ k, b k * u k = ∑ i, (∑ k, A k i * u k) * x i := by
    calc
      ∑ k, b k * u k
          = ∑ k, (∑ i, A k i * x i) * u k := by
            refine Finset.sum_congr rfl (fun k _ => ?_)
            rw [heq k]
      _ = ∑ k, ∑ i, A k i * x i * u k := by
            refine Finset.sum_congr rfl (fun k _ => ?_)
            rw [Finset.sum_mul]
      _ = ∑ i, ∑ k, A k i * x i * u k := Finset.sum_comm
      _ = ∑ i, (∑ k, A k i * u k) * x i := by
            refine Finset.sum_congr rfl (fun i _ => ?_)
            rw [Finset.sum_mul]
            refine Finset.sum_congr rfl (fun k _ => ?_)
            ring
  rw [hbu, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  unfold dualSlack
  ring

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Primal feasibility for `min ⟨c, x⟩` subject to `A x = b` and `x ≥ 0`. -/
structure LPPrimalFeasible (A : m → n → R) (b : m → R) (x : n → R) : Prop where
  /-- Equality constraints `A x = b`. -/
  eq : ∀ k, ∑ i, A k i * x i = b k
  /-- Nonnegativity `x ≥ 0`. -/
  nonneg : ∀ i, 0 ≤ x i

/-- Dual feasibility for `max ⟨b, u⟩` subject to `Aᵀ u ≤ c`. -/
structure LPDualFeasible (A : m → n → R) (c : n → R) (u : m → R) : Prop where
  /-- Column-wise dual inequality `(Aᵀ u)ᵢ ≤ cᵢ`. -/
  le : ∀ i, ∑ k, A k i * u k ≤ c i

omit [Fintype n] in
/-- Dual slack is nonnegative at every column for any dual-feasible `u`. -/
lemma dualSlack_nonneg {A : m → n → R} {c : n → R} {u : m → R}
    (hd : LPDualFeasible A c u) (i : n) :
    0 ≤ dualSlack A c u i := by
  unfold dualSlack
  linarith [hd.le i]

/-- **Weak LP Duality (`lp_primal_lower_bound_of_dual`).**
Any rationalized dual vector `u` satisfying `Aᵀ u ≤ c` certifies the global lower bound
`⟨b, u⟩ ≤ ⟨c, x⟩` for every primal-feasible `x`, with zero trust in any external solver. -/
theorem lp_primal_lower_bound_of_dual
    {A : m → n → R} {b : m → R} {c : n → R} {x : n → R} {u : m → R}
    (hp : LPPrimalFeasible A b x) (hd : LPDualFeasible A c u) :
    ∑ k, b k * u k ≤ ∑ i, c i * x i := by
  have hgap := lp_duality_gap_decomposition A b c x u hp.eq
  have hsum : 0 ≤ ∑ i, dualSlack A c u i * x i :=
    Finset.sum_nonneg (fun i _ => mul_nonneg (dualSlack_nonneg hd i) (hp.nonneg i))
  linarith

/-- **Zero-Gap Optimality Certificate (`lp_optimal_of_zero_gap`).**
If `xStar` is primal-feasible, `uStar` is dual-feasible, and `⟨b, uStar⟩ = ⟨c, xStar⟩`,
then `xStar` is globally optimal among all primal-feasible vectors `x`. -/
theorem lp_optimal_of_zero_gap
    {A : m → n → R} {b : m → R} {c : n → R} {xStar x : n → R} {uStar : m → R}
    (_hpStar : LPPrimalFeasible A b xStar) (hdStar : LPDualFeasible A c uStar)
    (hzero : ∑ k, b k * uStar k = ∑ i, c i * xStar i)
    (hp : LPPrimalFeasible A b x) :
    ∑ i, c i * xStar i ≤ ∑ i, c i * x i := by
  rw [← hzero]
  exact lp_primal_lower_bound_of_dual hp hdStar

end WeakDualityAndOptimality

/-! ## §2. Extremal-Functional / Strict Complementary-Slackness Uniqueness -/

section ExtremalFunctionalUniqueness

variable {m n : Type*} [Fintype m] [Fintype n]

/-- **Complementary slackness at zero duality gap.**
If `x` is primal-feasible, `uStar` is dual-feasible, and `⟨b, uStar⟩ ≥ ⟨c, x⟩`,
then every summand `(cᵢ - (Aᵀ uStar)ᵢ) xᵢ` vanishes identically. -/
theorem complementary_slackness_of_zero_gap
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    {A : m → n → R} {b : m → R} {c : n → R} {x : n → R} {uStar : m → R}
    (hp : LPPrimalFeasible A b x) (hdStar : LPDualFeasible A c uStar)
    (hopt : ∑ i, c i * x i ≤ ∑ k, b k * uStar k) (i : n) :
    dualSlack A c uStar i * x i = 0 := by
  have hgap := lp_duality_gap_decomposition A b c x uStar hp.eq
  have hnonneg : ∀ j ∈ Finset.univ, 0 ≤ dualSlack A c uStar j * x j :=
    fun j _ => mul_nonneg (dualSlack_nonneg hdStar j) (hp.nonneg j)
  have hsum_zero : ∑ j, dualSlack A c uStar j * x j = 0 := by
    have hle : ∑ j, dualSlack A c uStar j * x j ≤ 0 := by linarith
    have hge : 0 ≤ ∑ j, dualSlack A c uStar j * x j := Finset.sum_nonneg hnonneg
    exact le_antisymm hle hge
  exact (Finset.sum_eq_zero_iff_of_nonneg hnonneg).mp hsum_zero i (Finset.mem_univ i)

/-- **Extremal-Functional Support Localization (`unique_support_of_strict_dual_slack`,
Viazovska / El-Showk theorem).**
Suppose `uStar` achieves zero duality gap against `xStar`, and every index `i ∉ S` has
strictly positive dual slack `0 < cᵢ - (Aᵀ uStar)ᵢ`. Then **every** optimal primal
solution `x` vanishes identically outside `S` (`∀ i ∉ S, x i = 0`). -/
theorem unique_support_of_strict_dual_slack
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    {A : m → n → R} {b : m → R} {c : n → R} {xStar x : n → R} {uStar : m → R}
    (S : Finset n)
    (hdStar : LPDualFeasible A c uStar)
    (hzero : ∑ k, b k * uStar k = ∑ i, c i * xStar i)
    (hslack : ∀ i, i ∉ S → 0 < dualSlack A c uStar i)
    (hp : LPPrimalFeasible A b x)
    (hopt : ∑ i, c i * x i ≤ ∑ i, c i * xStar i) :
    ∀ i, i ∉ S → x i = 0 := by
  intro i hi
  have hle_dual : ∑ j, c j * x j ≤ ∑ k, b k * uStar k := by linarith
  have hcs := complementary_slackness_of_zero_gap hp hdStar hle_dual i
  have hpos := hslack i hi
  rcases mul_eq_zero.mp hcs with h0 | hx0
  · exfalso; exact ne_of_gt hpos h0
  · exact hx0

/-- **Algebraic Uniqueness of Singleton-Support Extremal States
(`unique_primal_of_strict_dual_slack`).**
When every index `i ≠ i₀` has strictly positive dual slack `0 < cᵢ - (Aᵀ uStar)ᵢ` and
constraint row `k₀` has nonzero entry `A k₀ i₀ ≠ 0`, the optimal primal solution is
**algebraically unique**: every optimal primal-feasible `x` satisfies `x = xStar`. -/
theorem unique_primal_of_strict_dual_slack
    {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R] [DecidableEq n]
    {A : m → n → R} {b : m → R} {c : n → R} {xStar x : n → R} {uStar : m → R}
    (i₀ : n) (k₀ : m)
    (hpStar : LPPrimalFeasible A b xStar)
    (hdStar : LPDualFeasible A c uStar)
    (hzero : ∑ k, b k * uStar k = ∑ i, c i * xStar i)
    (hslack : ∀ i, i ≠ i₀ → 0 < dualSlack A c uStar i)
    (hnorm : A k₀ i₀ ≠ 0)
    (hp : LPPrimalFeasible A b x)
    (hopt : ∑ i, c i * x i ≤ ∑ i, c i * xStar i) :
    x = xStar := by
  have hx_off : ∀ i, i ≠ i₀ → x i = 0 := by
    intro i hi
    exact unique_support_of_strict_dual_slack {i₀} hdStar hzero
      (fun j hj => hslack j (Finset.notMem_singleton.mp hj)) hp hopt i
      (Finset.notMem_singleton.mpr hi)
  have hxStar_off : ∀ i, i ≠ i₀ → xStar i = 0 := by
    intro i hi
    exact unique_support_of_strict_dual_slack {i₀} hdStar hzero
      (fun j hj => hslack j (Finset.notMem_singleton.mp hj)) hpStar (le_refl _) i
      (Finset.notMem_singleton.mpr hi)
  have hrow_x : A k₀ i₀ * x i₀ = b k₀ := by
    rw [← hp.eq k₀]
    symm
    exact Finset.sum_eq_single i₀
      (fun j _ hj => by rw [hx_off j hj, mul_zero])
      (fun h => absurd (Finset.mem_univ i₀) h)
  have hrow_xStar : A k₀ i₀ * xStar i₀ = b k₀ := by
    rw [← hpStar.eq k₀]
    symm
    exact Finset.sum_eq_single i₀
      (fun j _ hj => by rw [hxStar_off j hj, mul_zero])
      (fun h => absurd (Finset.mem_univ i₀) h)
  funext i
  by_cases hi : i = i₀
  · subst hi
    exact mul_left_cancel₀ hnorm (hrow_x.trans hrow_xStar.symm)
  · rw [hx_off i hi, hxStar_off i hi]

/-- **Probability-Simplex Discrete-Selection Uniqueness
(`simplex_unique_optimal_of_strict_dual_slack`).**
On the discrete candidate simplex `∑ᵢ xᵢ = 1, x ≥ 0`, if candidate `i₀` has strictly
smaller cost than every competitor (`∀ i ≠ i₀, c i₀ < c i`), then the pure vertex
`Pi.single i₀ 1` is the **unique** primal-feasible solution achieving `∑ᵢ cᵢ xᵢ ≤ c i₀`. -/
theorem simplex_unique_optimal_of_strict_dual_slack
    {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R] [DecidableEq n]
    {c x : n → R} (i₀ : n)
    (hstrict : ∀ i, i ≠ i₀ → c i₀ < c i)
    (hsum : ∑ i, x i = 1)
    (hnonneg : ∀ i, 0 ≤ x i)
    (hopt : ∑ i, c i * x i ≤ c i₀) :
    x = Pi.single i₀ 1 := by
  let A : Unit → n → R := fun _ _ => 1
  let b : Unit → R := fun _ => 1
  let uStar : Unit → R := fun _ => c i₀
  let xStar : n → R := Pi.single i₀ 1
  have hpStar : LPPrimalFeasible A b xStar := by
    refine ⟨fun _ => ?_, fun i => ?_⟩
    · simp [A, b, xStar]
    · by_cases hi : i = i₀
      · subst hi; simp [xStar]
      · simp [xStar, Pi.single_eq_of_ne hi]
  have hdStar : LPDualFeasible A c uStar := by
    refine ⟨fun i => ?_⟩
    by_cases hi : i = i₀
    · subst hi; simp [A, uStar]
    · simp only [A, uStar, Fintype.univ_punit, Finset.sum_singleton, one_mul]
      exact le_of_lt (hstrict i hi)
  have hxStar_sum : ∑ i, c i * xStar i = c i₀ := by
    rw [Finset.sum_eq_single i₀]
    · simp [xStar]
    · intro j _ hj; simp [xStar, Pi.single_eq_of_ne hj]
    · intro h; exact absurd (Finset.mem_univ i₀) h
  have hzero : ∑ k, b k * uStar k = ∑ i, c i * xStar i := by
    rw [hxStar_sum]
    simp [b, uStar]
  have hslack : ∀ i, i ≠ i₀ → 0 < dualSlack A c uStar i := by
    intro i hi
    simp only [dualSlack, A, uStar, Fintype.univ_punit, Finset.sum_singleton, one_mul]
    linarith [hstrict i hi]
  have hp : LPPrimalFeasible A b x := by
    refine ⟨fun _ => ?_, hnonneg⟩
    simpa [A, b] using hsum
  have hopt' : ∑ i, c i * x i ≤ ∑ i, c i * xStar i := by
    rwa [hxStar_sum]
  exact unique_primal_of_strict_dual_slack i₀ () hpStar hdStar hzero hslack one_ne_zero hp hopt'

end ExtremalFunctionalUniqueness

/-! ## §3. Gatermann–Parrilo / Delsarte–Schrijver Isotypic Block Collapse -/

section IsotypicBlockCollapse

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Gatermann–Parrilo / Delsarte–Schrijver Wedderburn Block Collapse
(`central_cone_iff_character_weights_nonneg`).**
Given central character/shadow-price weights `y : Λ → R` across finite nonempty
isotypic matrix blocks `Matrix (d l) (d l) R`, the central trace form
`∑_l y_l tr(M_lᵀ M_l)` is nonnegative for every tuple of block matrices `M`
**if and only if** `0 ≤ y_l` on every block `l : Λ`. -/
theorem central_cone_iff_character_weights_nonneg
    {Λ : Type*} [Fintype Λ] [DecidableEq Λ]
    {d : Λ → Type*} [∀ l, Fintype (d l)] [∀ l, DecidableEq (d l)] [∀ l, Nonempty (d l)]
    (y : Λ → R) :
    (∀ M : ∀ l, Matrix (d l) (d l) R,
        0 ≤ ∑ l, y l * Matrix.trace ((M l).transpose * M l)) ↔
      (∀ l, 0 ≤ y l) := by
  constructor
  · intro hcone l₀
    obtain ⟨i₀⟩ := (inferInstance : Nonempty (d l₀))
    let M₀ : ∀ l, Matrix (d l) (d l) R := fun l i j =>
      if h : l = l₀ then
        if h ▸ i = i₀ ∧ h ▸ j = i₀ then 1 else 0
      else 0
    have hval := hcone M₀
    have htrace_l₀ : Matrix.trace ((M₀ l₀).transpose * M₀ l₀) = 1 := by
      simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply, M₀]
      rw [Finset.sum_eq_single i₀]
      · rw [Finset.sum_eq_single i₀]
        · simp
        · intro k _ hk; simp [hk]
        · intro h; exact absurd (Finset.mem_univ i₀) h
      · intro i _ hi
        refine Finset.sum_eq_zero (fun k _ => ?_)
        simp [hi]
      · intro h; exact absurd (Finset.mem_univ i₀) h
    have htrace_other : ∀ l, l ≠ l₀ → Matrix.trace ((M₀ l).transpose * M₀ l) = 0 := by
      intro l hl
      simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply, M₀,
        dif_neg hl, mul_zero, Finset.sum_const_zero]
    have hsum : (∑ l, y l * Matrix.trace ((M₀ l).transpose * M₀ l)) = y l₀ := by
      rw [Finset.sum_eq_single l₀]
      · rw [htrace_l₀, mul_one]
      · intro l _ hl; rw [htrace_other l hl, mul_zero]
      · intro h; exact absurd (Finset.mem_univ l₀) h
    rwa [hsum] at hval
  · intro hy M
    refine Finset.sum_nonneg (fun l _ => ?_)
    refine mul_nonneg (hy l) ?_
    simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply]
    exact Finset.sum_nonneg (fun i _ =>
      Finset.sum_nonneg (fun k _ => mul_self_nonneg (M l k i)))

/-- **Orthogonal Central-Idempotent Cone Collapse
(`central_idempotent_pairing_nonneg_iff`).**
In any `R`-algebra `A` equipped with an `R`-linear trace `τ : A →ₗ[R] R` and pairwise
orthogonal central idempotents `e : Λ → A` of strictly positive trace `0 < τ (e l)` on
`active : Finset Λ`, the central element `∑_{l ∈ active} y_l • e_l` pairs nonnegatively
with every central square `∑_{l ∈ active} z_l² • e_l` **iff** `∀ l ∈ active, 0 ≤ y_l`. -/
theorem central_idempotent_pairing_nonneg_iff
    {Λ A : Type*} [DecidableEq Λ] [Ring A] [Algebra R A]
    (active : Finset Λ) (e : Λ → A) (τ : A →ₗ[R] R)
    (horth : ∀ l ∈ active, ∀ l' ∈ active, e l * e l' = if l = l' then e l else 0)
    (hpos : ∀ l ∈ active, 0 < τ (e l))
    (y : Λ → R) :
    (∀ z : Λ → R,
        0 ≤ τ ((∑ l ∈ active, y l • e l) * (∑ l' ∈ active, (z l' ^ 2) • e l'))) ↔
      (∀ l ∈ active, 0 ≤ y l) := by
  have hprod : ∀ z : Λ → R,
      τ ((∑ l ∈ active, y l • e l) * (∑ l' ∈ active, (z l' ^ 2) • e l')) =
        ∑ l ∈ active, (y l * z l ^ 2) * τ (e l) := by
    intro z
    rw [Finset.sum_mul, map_sum]
    refine Finset.sum_congr rfl (fun l hl => ?_)
    rw [Finset.mul_sum, map_sum, Finset.sum_eq_single l]
    · rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, smul_smul, horth l hl l hl,
          if_pos rfl, LinearMap.map_smul, smul_eq_mul]
    · intro l' hl' hne
      rw [Algebra.smul_mul_assoc, Algebra.mul_smul_comm, smul_smul, horth l hl l' hl',
          if_neg (Ne.symm hne), smul_zero, map_zero]
    · intro hnot; exact absurd hl hnot
  constructor
  · intro hcone l₀ hl₀
    let z₀ : Λ → R := fun l => if l = l₀ then 1 else 0
    have hz := hcone z₀
    rw [hprod z₀, Finset.sum_eq_single l₀] at hz
    · simp only [z₀, if_pos rfl, one_pow, mul_one] at hz
      by_contra hneg
      push_neg at hneg
      exact not_lt_of_ge hz (mul_neg_of_neg_of_pos hneg (hpos l₀ hl₀))
    · intro l _ hlne
      simp [z₀, hlne]
    · intro hnot; exact absurd hl₀ hnot
  · intro hy z
    rw [hprod z]
    exact Finset.sum_nonneg (fun l hl =>
      mul_nonneg (mul_nonneg (hy l hl) (sq_nonneg (z l))) (le_of_lt (hpos l hl)))

end IsotypicBlockCollapse

/-! ## §4. Finite-`A` Parametric LP Concavity and Shadow-Price Kink Jumps -/

section ParametricKinksAndShadowPrices

/-- Parametric ground-state energy envelope `E(θ) = min_{i ∈ F} (aᵢ + bᵢ θ)` over a
finite nonempty motif/regime family `F`. -/
def parametricMinEnvelope {ι R : Type*} [CommRing R] [LinearOrder R]
    (F : Finset ι) (hF : F.Nonempty) (a b : ι → R) (θ : R) : R :=
  F.inf' hF (fun i => a i + b i * θ)

/-- Every branch `i ∈ F` upper-bounds `E(θ)`. -/
lemma parametricMinEnvelope_le {ι R : Type*} [CommRing R] [LinearOrder R]
    (F : Finset ι) (hF : F.Nonempty) (a b : ι → R) (θ : R) {i : ι} (hi : i ∈ F) :
    parametricMinEnvelope F hF a b θ ≤ a i + b i * θ :=
  Finset.inf'_le _ hi

/-- **Concavity of Finite Parametric LP Envelopes
(`piecewise_linear_concave_of_parametric_lp`).**
For any finite nonempty set `F` over a linearly ordered commutative ring `R`,
`E(θ) = min_{i ∈ F} (aᵢ + bᵢ θ)` is concave: for all `θ₁, θ₂ : R` and `0 ≤ t ≤ 1`,
`(1 - t) E(θ₁) + t E(θ₂) ≤ E((1 - t) θ₁ + t θ₂)`. -/
theorem piecewise_linear_concave_of_parametric_lp
    {ι R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (F : Finset ι) (hF : F.Nonempty) (a b : ι → R)
    (θ₁ θ₂ t : R) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    (1 - t) * parametricMinEnvelope F hF a b θ₁ + t * parametricMinEnvelope F hF a b θ₂ ≤
      parametricMinEnvelope F hF a b ((1 - t) * θ₁ + t * θ₂) := by
  unfold parametricMinEnvelope
  refine Finset.le_inf' hF _ (fun i hi => ?_)
  have h1 : F.inf' hF (fun k => a k + b k * θ₁) ≤ a i + b i * θ₁ := Finset.inf'_le _ hi
  have h2 : F.inf' hF (fun k => a k + b k * θ₂) ≤ a i + b i * θ₂ := Finset.inf'_le _ hi
  have h1m : 0 ≤ 1 - t := sub_nonneg.mpr ht1
  have hm1 := mul_le_mul_of_nonneg_left h1 h1m
  have hm2 := mul_le_mul_of_nonneg_left h2 ht0
  have hlin : (1 - t) * (a i + b i * θ₁) + t * (a i + b i * θ₂) =
      a i + b i * ((1 - t) * θ₁ + t * θ₂) := by ring
  linarith

/-- **Finite-`A` Shadow-Price Kink Jump Theorem
(`piecewise_linear_kink_shadow_price_jump`).**
Over any linearly ordered field `R`, if `E(θ) = min_{k ∈ F} (aₖ + bₖ θ)` switches
optimal branch across a chamber wall `θ*` from `i ∈ F` at `θ₋ < θ*` to `j ∈ F` at
`θ₊ > θ*` with `bⱼ < bᵢ` and both branches tied at `θ*`, then:
1. The left difference quotient `(E(θ*) - E(θ₋)) / (θ* - θ₋)` equals `bᵢ`,
2. The right difference quotient `(E(θ₊) - E(θ*)) / (θ₊ - θ*)` equals `bⱼ`, and
3. The dual shadow price / chemical potential jumps strictly by `bᵢ - bⱼ > 0` at
   finite `|F|`, requiring no `N → ∞` thermodynamic limit. -/
theorem piecewise_linear_kink_shadow_price_jump
    {ι R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (F : Finset ι) (hF : F.Nonempty) (a b : ι → R)
    {i j : ι} (_hi : i ∈ F) (_hj : j ∈ F)
    {θm θStar θp : R} (hm : θm < θStar) (hp : θStar < θp)
    (hslope : b j < b i)
    (htie_i : parametricMinEnvelope F hF a b θStar = a i + b i * θStar)
    (htie_j : parametricMinEnvelope F hF a b θStar = a j + b j * θStar)
    (hleft : parametricMinEnvelope F hF a b θm = a i + b i * θm)
    (hright : parametricMinEnvelope F hF a b θp = a j + b j * θp) :
    let uLeft := (parametricMinEnvelope F hF a b θStar - parametricMinEnvelope F hF a b θm) /
      (θStar - θm)
    let uRight := (parametricMinEnvelope F hF a b θp - parametricMinEnvelope F hF a b θStar) /
      (θp - θStar)
    uLeft = b i ∧ uRight = b j ∧ uLeft - uRight = b i - b j ∧ 0 < uLeft - uRight := by
  dsimp only
  have hdm : θStar - θm ≠ 0 := sub_ne_zero.mpr (ne_of_gt hm)
  have hdp : θp - θStar ≠ 0 := sub_ne_zero.mpr (ne_of_gt hp)
  have hL : (parametricMinEnvelope F hF a b θStar - parametricMinEnvelope F hF a b θm) /
      (θStar - θm) = b i := by
    rw [htie_i, hleft]
    have : (a i + b i * θStar) - (a i + b i * θm) = b i * (θStar - θm) := by ring
    rw [this, mul_div_cancel_right₀ _ hdm]
  have hR : (parametricMinEnvelope F hF a b θp - parametricMinEnvelope F hF a b θStar) /
      (θp - θStar) = b j := by
    rw [hright, htie_j]
    have : (a j + b j * θp) - (a j + b j * θStar) = b j * (θp - θStar) := by ring
    rw [this, mul_div_cancel_right₀ _ hdp]
  refine ⟨hL, hR, ?_, ?_⟩
  · rw [hL, hR]
  · rw [hL, hR]; linarith

/-- Alias matching the Bean `qou-1aqc` name `dual_shadow_price_jump_at_kink`. -/
theorem dual_shadow_price_jump_at_kink
    {ι R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (F : Finset ι) (hF : F.Nonempty) (a b : ι → R)
    {i j : ι} (hi : i ∈ F) (hj : j ∈ F)
    {θm θStar θp : R} (hm : θm < θStar) (hp : θStar < θp)
    (hslope : b j < b i)
    (htie_i : parametricMinEnvelope F hF a b θStar = a i + b i * θStar)
    (htie_j : parametricMinEnvelope F hF a b θStar = a j + b j * θStar)
    (hleft : parametricMinEnvelope F hF a b θm = a i + b i * θm)
    (hright : parametricMinEnvelope F hF a b θp = a j + b j * θp) :
    0 < (parametricMinEnvelope F hF a b θStar - parametricMinEnvelope F hF a b θm) / (θStar - θm) -
        (parametricMinEnvelope F hF a b θp - parametricMinEnvelope F hF a b θStar) / (θp - θStar) :=
  (piecewise_linear_kink_shadow_price_jump F hF a b hi hj hm hp hslope
    htie_i htie_j hleft hright).2.2.2

/-- **Existence of Exact Chamber Neighborhoods Around a Two-Branch Kink
(`exists_chamber_neighborhood_kink_jump`).**
If `i, j ∈ F` tie at `E(θ*)` with `bⱼ < bᵢ` and every non-`{i,j}` branch `k ∈ F` has
strictly positive slack `E(θ*) < aₖ + bₖ θ*` at `θ*`, then there exists `δ > 0` in `R`
such that `i` uniquely realises `E(θ₋)` for all `θ₋ ∈ (θ* - δ, θ*)` and `j` uniquely
realises `E(θ₊)` for all `θ₊ ∈ (θ*, θ* + δ)`. -/
theorem exists_chamber_neighborhood_kink_jump
    {ι R : Type*} [DecidableEq ι] [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (F : Finset ι) (hF : F.Nonempty) (a b : ι → R)
    {i j : ι} (hi : i ∈ F) (hj : j ∈ F) (θStar : R)
    (hslope : b j < b i)
    (htie_i : a i + b i * θStar = parametricMinEnvelope F hF a b θStar)
    (htie_j : a j + b j * θStar = parametricMinEnvelope F hF a b θStar)
    (hstrict_off : ∀ k ∈ F, k ≠ i → k ≠ j →
      parametricMinEnvelope F hF a b θStar < a k + b k * θStar) :
    ∃ δ : R, 0 < δ ∧
      (∀ θm, θStar - δ < θm → θm < θStar →
        parametricMinEnvelope F hF a b θm = a i + b i * θm) ∧
      (∀ θp, θStar < θp → θp < θStar + δ →
        parametricMinEnvelope F hF a b θp = a j + b j * θp) := by
  let EStar := parametricMinEnvelope F hF a b θStar
  let rest := F.filter (fun k => k ≠ i ∧ k ≠ j)
  let step : ι → R := fun k =>
    ((a k + b k * θStar) - EStar) / (|b k - b i| + |b k - b j| + 1)
  have hstep_pos : ∀ k ∈ rest, 0 < step k := by
    intro k hk
    rcases (Finset.mem_filter.mp hk) with ⟨hkF, hki, hkj⟩
    have hnum : 0 < (a k + b k * θStar) - EStar :=
      sub_pos.mpr (hstrict_off k hkF hki hkj)
    have hden : 0 < |b k - b i| + |b k - b j| + 1 := by
      have h1 := abs_nonneg (b k - b i)
      have h2 := abs_nonneg (b k - b j)
      linarith
    exact div_pos hnum hden
  let δ : R := if hrest : rest.Nonempty then min 1 (rest.inf' hrest step) else 1
  have hδ_pos : 0 < δ := by
    dsimp [δ]
    split_ifs with hrest
    · refine lt_min one_pos ?_
      exact (Finset.lt_inf'_iff hrest).mpr hstep_pos
    · exact one_pos
  have hδ_le_step : ∀ k ∈ rest, δ ≤ step k := by
    intro k hk
    have hrest : rest.Nonempty := ⟨k, hk⟩
    dsimp [δ]
    rw [dif_pos hrest]
    exact le_trans (min_le_right _ _) (Finset.inf'_le step hk)
  refine ⟨δ, hδ_pos, ?_, ?_⟩
  · intro θm hlow hhigh
    apply le_antisymm (parametricMinEnvelope_le F hF a b θm hi)
    refine Finset.le_inf' hF _ (fun k hk => ?_)
    by_cases hki : k = i
    · subst k; exact le_refl _
    · by_cases hkj : k = j
      · subst k
        have htie : a i + b i * θStar = a j + b j * θStar := htie_i.trans htie_j.symm
        have hdiff : (a j + b j * θm) - (a i + b i * θm) =
            (b i - b j) * (θStar - θm) - ((a i + b i * θStar) - (a j + b j * θStar)) := by ring
        rw [htie, sub_self, sub_zero] at hdiff
        have hpos : 0 < (b i - b j) * (θStar - θm) :=
          mul_pos (sub_pos.mpr hslope) (sub_pos.mpr hhigh)
        linarith
      · have hk_rest : k ∈ rest := Finset.mem_filter.mpr ⟨hk, hki, hkj⟩
        have hle := hδ_le_step k hk_rest
        have hden : 0 < |b k - b i| + |b k - b j| + 1 := by
          linarith [abs_nonneg (b k - b i), abs_nonneg (b k - b j)]
        have hgap : (θStar - θm) * (|b k - b i| + |b k - b j| + 1) <
            (a k + b k * θStar) - EStar := by
          have hlt_δ : θStar - θm < δ := by linarith
          have hlt_step : θStar - θm < step k := lt_of_lt_of_le hlt_δ hle
          exact (lt_div_iff₀ hden).mp hlt_step
        have habs_m : (b i - b k) * (θStar - θm) ≤ |b k - b i| * (θStar - θm) := by
          have hle_abs : b i - b k ≤ |b k - b i| := by
            rw [abs_sub_comm]
            exact le_abs_self (b i - b k)
          exact mul_le_mul_of_nonneg_right hle_abs (le_of_lt (sub_pos.mpr hhigh))
        have hnonneg_extra : 0 ≤ (|b k - b j| + 1) * (θStar - θm) :=
          mul_nonneg (by linarith [abs_nonneg (b k - b j)]) (le_of_lt (sub_pos.mpr hhigh))
        have hident : (a k + b k * θm) - (a i + b i * θm) =
            ((a k + b k * θStar) - (a i + b i * θStar)) - (b k - b i) * (θStar - θm) := by ring
        have hsub_le : (b k - b i) * (θStar - θm) ≤ |b k - b i| * (θStar - θm) :=
          mul_le_mul_of_nonneg_right (le_abs_self (b k - b i)) (le_of_lt (sub_pos.mpr hhigh))
        have hE : a i + b i * θStar = EStar := htie_i
        linarith
  · intro θp hlow hhigh
    apply le_antisymm (parametricMinEnvelope_le F hF a b θp hj)
    refine Finset.le_inf' hF _ (fun k hk => ?_)
    by_cases hkj : k = j
    · subst k; exact le_refl _
    · by_cases hki : k = i
      · subst k
        have htie : a i + b i * θStar = a j + b j * θStar := htie_i.trans htie_j.symm
        have hdiff : (a i + b i * θp) - (a j + b j * θp) =
            (b i - b j) * (θp - θStar) + ((a i + b i * θStar) - (a j + b j * θStar)) := by ring
        rw [htie, sub_self, add_zero] at hdiff
        have hpos : 0 < (b i - b j) * (θp - θStar) :=
          mul_pos (sub_pos.mpr hslope) (sub_pos.mpr hlow)
        linarith
      · have hk_rest : k ∈ rest := Finset.mem_filter.mpr ⟨hk, hki, hkj⟩
        have hle := hδ_le_step k hk_rest
        have hden : 0 < |b k - b i| + |b k - b j| + 1 := by
          linarith [abs_nonneg (b k - b i), abs_nonneg (b k - b j)]
        have hgap : (θp - θStar) * (|b k - b i| + |b k - b j| + 1) <
            (a k + b k * θStar) - EStar := by
          have hlt_δ : θp - θStar < δ := by linarith
          have hlt_step : θp - θStar < step k := lt_of_lt_of_le hlt_δ hle
          exact (lt_div_iff₀ hden).mp hlt_step
        have hneg_le : -(b k - b j) * (θp - θStar) ≤ |b k - b j| * (θp - θStar) :=
          mul_le_mul_of_nonneg_right (neg_le_abs (b k - b j)) (le_of_lt (sub_pos.mpr hlow))
        have hnonneg_extra : 0 ≤ (|b k - b i| + 1) * (θp - θStar) :=
          mul_nonneg (by linarith [abs_nonneg (b k - b i)]) (le_of_lt (sub_pos.mpr hlow))
        have hident : (a k + b k * θp) - (a j + b j * θp) =
            ((a k + b k * θStar) - (a j + b j * θStar)) + (b k - b j) * (θp - θStar) := by ring
        have hE : a j + b j * θStar = EStar := htie_j
        linarith

end ParametricKinksAndShadowPrices

/-! ## §5. Graver / Sturmfels–Thomas Test-Set Global Integer Optimality -/

section GraverTestSetOptimality

variable {m : Type*} [Fintype m]
variable {R : Type*} [AddCommGroup R]

/-- Integer-program linear cost `c · u = ∑ⱼ uⱼ • cⱼ` over an additive commutative group `R`. -/
def ipObj (c : m → R) (u : m → ℤ) : R :=
  ∑ j, u j • c j

lemma ipObj_sub (c : m → R) (u v : m → ℤ) :
    ipObj c u - ipObj c v = ∑ j, (u j - v j) • c j := by
  unfold ipObj
  rw [← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  rw [sub_zsmul, sub_eq_add_neg]

omit [Fintype m] in
private lemma sum_zsmul_left {α : Type*} (s : Finset α) (f : α → ℤ) (x : R) :
    (∑ a ∈ s, f a) • x = ∑ a ∈ s, f a • x := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, add_zsmul, ih]

omit [Fintype m] in
private lemma nsmul_sum_right {α : Type*} (s : Finset α) (n : ℕ) (f : α → R) :
    n • ∑ a ∈ s, f a = ∑ a ∈ s, n • f a := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, nsmul_add, ih]

lemma ipObj_diff_eq_sum_nsmul {k : ℕ} (c : m → R) (uStar u : m → ℤ)
    (g : Fin k → m → ℤ) (n : Fin k → ℕ)
    (hdecomp : ∀ j, u j - uStar j = ∑ r : Fin k, (n r : ℤ) * g r j) :
    ipObj c u - ipObj c uStar = ∑ r : Fin k, n r • ipObj c (g r) := by
  rw [ipObj_sub]
  calc
    ∑ j, (u j - uStar j) • c j
        = ∑ j, (∑ r : Fin k, (n r : ℤ) * g r j) • c j := by
          refine Finset.sum_congr rfl (fun j _ => ?_)
          rw [hdecomp j]
    _ = ∑ j, ∑ r : Fin k, ((n r : ℤ) * g r j) • c j := by
          refine Finset.sum_congr rfl (fun j _ => ?_)
          exact sum_zsmul_left Finset.univ (fun r => (n r : ℤ) * g r j) (c j)
    _ = ∑ r : Fin k, ∑ j, ((n r : ℤ) * g r j) • c j := Finset.sum_comm
    _ = ∑ r : Fin k, n r • ipObj c (g r) := by
          refine Finset.sum_congr rfl (fun r _ => ?_)
          unfold ipObj
          rw [nsmul_sum_right Finset.univ (n r) (fun j => g r j • c j)]
          refine Finset.sum_congr rfl (fun j _ => ?_)
          rw [mul_zsmul, natCast_zsmul]

variable [LinearOrder R] [IsOrderedAddMonoid R]

/-- **Graver / Universal Gröbner Test-Set Global Optimality
(`graver_test_set_certifies_global_ip_min`, Graver 1975 / Sturmfels–Thomas 1997).**
Over any linearly ordered additive commutative group `R`, if `u - uStar` decomposes as a
nonnegative integer combination `∑ᵣ nᵣ gᵣ` (`nᵣ ∈ ℕ`) of test-set moves `gᵣ` that each have
nonnegative cost `0 ≤ ipObj c (gᵣ)`, then `ipObj c uStar ≤ ipObj c u`. -/
theorem graver_test_set_certifies_global_ip_min
    {k : ℕ} (c : m → R) (uStar u : m → ℤ)
    (g : Fin k → m → ℤ) (n : Fin k → ℕ)
    (hdecomp : ∀ j, u j - uStar j = ∑ r : Fin k, (n r : ℤ) * g r j)
    (hcost : ∀ r : Fin k, 0 ≤ ipObj c (g r)) :
    ipObj c uStar ≤ ipObj c u := by
  have hdiff := ipObj_diff_eq_sum_nsmul c uStar u g n hdecomp
  have hnonneg : 0 ≤ ∑ r : Fin k, n r • ipObj c (g r) :=
    Finset.sum_nonneg (fun r _ => nsmul_nonneg (hcost r) (n r))
  exact sub_nonneg.mp (hdiff ▸ hnonneg)

/-- **Strict Graver Test-Set Global Uniqueness
(`graver_test_set_certifies_strict_global_ip_min`).**
When every test move in the decomposition has strictly positive cost `0 < ipObj c (gᵣ)`
and at least one move has positive multiplicity `0 < n r₀`, `ipObj c uStar < ipObj c u`. -/
theorem graver_test_set_certifies_strict_global_ip_min
    {k : ℕ} (c : m → R) (uStar u : m → ℤ)
    (g : Fin k → m → ℤ) (n : Fin k → ℕ)
    (hdecomp : ∀ j, u j - uStar j = ∑ r : Fin k, (n r : ℤ) * g r j)
    (hcost : ∀ r : Fin k, 0 < ipObj c (g r))
    (hne : ∃ r₀ : Fin k, 0 < n r₀) :
    ipObj c uStar < ipObj c u := by
  rcases hne with ⟨r₀, hr₀⟩
  have hdiff := ipObj_diff_eq_sum_nsmul c uStar u g n hdecomp
  have hpos : 0 < ∑ r : Fin k, n r • ipObj c (g r) := by
    refine Finset.sum_pos' (fun r _ => nsmul_nonneg (le_of_lt (hcost r)) (n r))
      ⟨r₀, Finset.mem_univ r₀, nsmul_pos (hcost r₀) (Nat.ne_of_gt hr₀)⟩
  exact sub_pos.mp (hdiff ▸ hpos)

end GraverTestSetOptimality

end QOU.MathlibInfra
