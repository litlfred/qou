import QOU.Mathlib.EllipticDivisorDegree
import QOU.Mathlib.EllipticAnnulusDescent
import QOU.Mathlib.EllipticAnnulusWinding

/-!
# QOU.Mathlib.LiouvilleThird — Liouville's third theorem, proved

**Theorem** (`QOU.Mathlib.EllipticDivisorDegree.elliptic_divisor_degree_zero`). For
`f` meromorphic on `ℂ` and periodic under `ℝ`-independent `ω₁, ω₂`, the divisor of
`f` sums to zero over the half-open fundamental parallelogram: zeros and poles in
one cell are equinumerous with multiplicity.

Bean `qou-z4jb` (owner ruling 2026-11-20 on #8526). Route:

1. degenerate case — if `f` vanishes locally anywhere it does everywhere
   (connectedness of `ℂ`), the divisor is `0` and the sum is trivially `0`;
2. orient the second period so `p = exp (2πi ω₂'/ω₁)` has `‖p‖ > 1`;
3. pull back along `w = exp (2πi z/ω₁)`
   (`QOU.Mathlib.EllipticAnnulusDescent`): meromorphic on `ℂ*`, orders preserved,
   and `g (p w) = g w`;
4. choose a radius `ρ` whose circles `|w| = ρ, ‖p‖ρ` avoid every zero, pole and
   removable irregularity of `g` (`exists_clean_radius`);
5. the annulus argument principle plus the winding identity give
   `Σ_{ρ < |w| < ‖p‖ρ} ord_w g = 0`
   (`QOU.Mathlib.EllipticAnnulusWinding.annulus_divisor_sum_eq_zero`);
6. `w ↦ red (ω₁/2πi · log w)` is a bijection from the annulus support onto the
   parallelogram support preserving orders (`red` = reduction modulo the lattice),
   so the two sums agree.

No `sorry`, no axiom beyond Lean's three; nonconstancy of `f` is not used.
The main proof raises `maxHeartbeats` (it is one long declaration).
-/

open Filter Topology Complex Metric

namespace QOU.Mathlib.LiouvilleThird

/-- A set that is locally isolated near every point of a compact set meets that
compact set in finitely many points. -/
theorem finite_inter_of_locally_isolated {B K : Set ℂ} (hK : IsCompact K)
    (hloc : ∀ x ∈ K, ∀ᶠ z in 𝓝[≠] x, z ∉ B) : (K ∩ B).Finite := by
  classical
  have hU : ∀ x ∈ K, {z | z ≠ x → z ∉ B} ∈ 𝓝 x := by
    intro x hx
    have := hloc x hx
    rw [eventually_nhdsWithin_iff] at this
    exact this
  obtain ⟨t, -, hcov⟩ := hK.elim_nhds_subcover (fun x => {z | z ≠ x → z ∉ B}) hU
  refine (t.finite_toSet).subset ?_
  rintro b ⟨hbK, hbB⟩
  obtain ⟨x, hx, hbx⟩ := Set.mem_iUnion₂.mp (hcov hbK)
  by_contra hbt
  have hne : b ≠ x := fun h => hbt (h ▸ hx)
  exact hbx hne hbB

/-- **A clean radius.** If `g` is meromorphic with finite order at every point
of `ℂ*` and `‖p‖ > 1`, there is `ρ ∈ (1, ‖p‖)` such that `g` is analytic and
nonzero on both circles `|w| = ρ` and `|w| = ‖p‖ ρ`. -/
theorem exists_clean_radius {g : ℂ → ℂ} {p : ℂ} (hp : 1 < ‖p‖)
    (hmero : ∀ w, w ≠ 0 → MeromorphicAt g w)
    (hord : ∀ w, w ≠ 0 → meromorphicOrderAt g w ≠ ⊤) :
    ∃ ρ : ℝ, 1 < ρ ∧ ρ < ‖p‖ ∧
      ∀ z, (‖z‖ = ρ ∨ ‖z‖ = ‖p‖ * ρ) → AnalyticAt ℂ g z ∧ g z ≠ 0 := by
  set B : Set ℂ := {w | ¬ (AnalyticAt ℂ g w ∧ g w ≠ 0)} with hB
  set K : Set ℂ := closedBall (0 : ℂ) (‖p‖ ^ 2) \ ball (0 : ℂ) 1 with hKdef
  have hK : IsCompact K := (isCompact_closedBall _ _).diff isOpen_ball
  have hK0 : ∀ x ∈ K, x ≠ 0 := by
    intro x hx h
    have := hx.2; rw [h] at this; simp at this
  have hloc : ∀ x ∈ K, ∀ᶠ z in 𝓝[≠] x, z ∉ B := by
    intro x hx
    have hx0 := hK0 x hx
    filter_upwards [(hmero x hx0).eventually_analyticAt,
      ((meromorphicOrderAt_ne_top_iff_eventually_ne_zero (hmero x hx0)).mp (hord x hx0))]
      with z h1 h2
    simp only [hB, Set.mem_setOf_eq, not_not]
    exact ⟨h1, h2⟩
  have hfin : (K ∩ B).Finite := finite_inter_of_locally_isolated hK hloc
  set F : Set ℝ := (fun w : ℂ => ‖w‖) '' (K ∩ B) with hF
  have hFfin : F.Finite := hfin.image _
  have hp0 : 0 < ‖p‖ := by linarith
  set X : Set ℝ := F ∪ (fun r => r / ‖p‖) '' F with hX
  have hXfin : X.Finite := hFfin.union (hFfin.image _)
  obtain ⟨ρ, hρI, hρX⟩ := ((Set.Ioo_infinite hp).diff hXfin).nonempty
  refine ⟨ρ, hρI.1, hρI.2, ?_⟩
  intro z hz
  by_contra hbad
  have hzB : z ∈ B := hbad
  have hzK : z ∈ K := by
    rcases hz with hz | hz
    · refine ⟨?_, ?_⟩
      · rw [mem_closedBall, dist_zero_right, hz]; nlinarith [hρI.2]
      · rw [mem_ball, dist_zero_right, hz]; linarith [hρI.1]
    · refine ⟨?_, ?_⟩
      · rw [mem_closedBall, dist_zero_right, hz, sq]
        exact mul_le_mul_of_nonneg_left hρI.2.le hp0.le
      · rw [mem_ball, dist_zero_right, hz]; nlinarith [hρI.1]
  have hnF : ‖z‖ ∈ F := ⟨z, ⟨hzK, hzB⟩, rfl⟩
  apply hρX
  rcases hz with hz | hz
  · exact Or.inl (hz ▸ hnF)
  · refine Or.inr ⟨‖z‖, hnF, ?_⟩
    simp only [hz]; field_simp

/-! ### Lattice coordinates and reduction to the fundamental parallelogram -/

section Coords

variable (ω₁ ω₂ : ℂ)

/-- Second lattice coordinate: `z = s ω₁ + t ω₂` gives `t = Im(z/ω₁) / Im(ω₂/ω₁)`. -/
noncomputable def tc (z : ℂ) : ℝ := (z / ω₁).im / (ω₂ / ω₁).im

/-- First lattice coordinate. -/
noncomputable def sc (z : ℂ) : ℝ := (z / ω₁).re - tc ω₁ ω₂ z * (ω₂ / ω₁).re

variable {ω₁ ω₂}

theorem decomp (hω : ω₁ ≠ 0) (him : (ω₂ / ω₁).im ≠ 0) (z : ℂ) :
    z = (sc ω₁ ω₂ z : ℂ) * ω₁ + (tc ω₁ ω₂ z : ℂ) * ω₂ := by
  have key : z / ω₁ = (sc ω₁ ω₂ z : ℂ) + (tc ω₁ ω₂ z : ℂ) * (ω₂ / ω₁) := by
    apply Complex.ext
    · simp [sc, tc]
    · simp [sc, tc]; field_simp
  calc z = (z / ω₁) * ω₁ := by field_simp
    _ = _ := by rw [key]; field_simp

theorem tc_lin (hω : ω₁ ≠ 0) (him : (ω₂ / ω₁).im ≠ 0) (s t : ℝ) :
    tc ω₁ ω₂ ((s : ℂ) * ω₁ + (t : ℂ) * ω₂) = t := by
  have : ((s : ℂ) * ω₁ + (t : ℂ) * ω₂) / ω₁ = s + t * (ω₂ / ω₁) := by field_simp
  simp only [tc, this]
  simp; field_simp

theorem sc_lin (hω : ω₁ ≠ 0) (him : (ω₂ / ω₁).im ≠ 0) (s t : ℝ) :
    sc ω₁ ω₂ ((s : ℂ) * ω₁ + (t : ℂ) * ω₂) = s := by
  have : ((s : ℂ) * ω₁ + (t : ℂ) * ω₂) / ω₁ = s + t * (ω₂ / ω₁) := by field_simp
  rw [sc, tc_lin hω him, this]
  simp

/-- Reduction modulo the lattice into the half-open fundamental parallelogram. -/
noncomputable def red (ω₁ ω₂ : ℂ) (z : ℂ) : ℂ :=
  z - (⌊sc ω₁ ω₂ z⌋ : ℂ) * ω₁ - (⌊tc ω₁ ω₂ z⌋ : ℂ) * ω₂

theorem red_eq (hω : ω₁ ≠ 0) (him : (ω₂ / ω₁).im ≠ 0) (z : ℂ) :
    red ω₁ ω₂ z = ((Int.fract (sc ω₁ ω₂ z) : ℝ) : ℂ) * ω₁
      + ((Int.fract (tc ω₁ ω₂ z) : ℝ) : ℂ) * ω₂ := by
  unfold red
  conv_lhs => arg 1; arg 1; rw [decomp hω him z]
  simp only [Int.fract, Complex.ofReal_sub, Complex.ofReal_intCast]
  ring

theorem red_mem (hω : ω₁ ≠ 0) (him : (ω₂ / ω₁).im ≠ 0) (z : ℂ) :
    red ω₁ ω₂ z ∈ EllipticDivisorDegree.fundamentalParallelogram ω₁ ω₂ :=
  ⟨Int.fract (sc ω₁ ω₂ z), Int.fract (tc ω₁ ω₂ z),
    ⟨Int.fract_nonneg _, Int.fract_lt_one _⟩, ⟨Int.fract_nonneg _, Int.fract_lt_one _⟩,
    by rw [red_eq hω him]; simp [Complex.real_smul]⟩

theorem red_of_mem (hω : ω₁ ≠ 0) (him : (ω₂ / ω₁).im ≠ 0) {z : ℂ}
    (hz : z ∈ EllipticDivisorDegree.fundamentalParallelogram ω₁ ω₂) : red ω₁ ω₂ z = z := by
  obtain ⟨s, t, hs, ht, rfl⟩ := hz
  simp only [Complex.real_smul] at *
  rw [red_eq hω him, sc_lin hω him, tc_lin hω him, Int.fract_eq_self.mpr hs,
    Int.fract_eq_self.mpr ht]

theorem red_add (hω : ω₁ ≠ 0) (him : (ω₂ / ω₁).im ≠ 0) (z : ℂ) (m n : ℤ) :
    red ω₁ ω₂ (z + (m : ℂ) * ω₁ + (n : ℂ) * ω₂) = red ω₁ ω₂ z := by
  have hz : z + (m : ℂ) * ω₁ + (n : ℂ) * ω₂
      = (((sc ω₁ ω₂ z + m : ℝ)) : ℂ) * ω₁ + ((tc ω₁ ω₂ z + n : ℝ) : ℂ) * ω₂ := by
    conv_lhs => rw [decomp hω him z]
    push_cast; ring
  rw [red_eq hω him, red_eq hω him, hz, sc_lin hω him, tc_lin hω him,
    Int.fract_add_intCast, Int.fract_add_intCast]

end Coords

open EllipticDivisorDegree EllipticAnnulusDescent EllipticAnnulusWinding
  ArgumentPrincipleAnnulus

theorem norm_exp_two_pi_I_mul (x : ℂ) :
    ‖exp (2 * Real.pi * I * x)‖ = Real.exp (-(2 * Real.pi * x.im)) := by
  rw [Complex.norm_exp]; congr 1; simp

/-- The divisor of a doubly periodic meromorphic function is lattice-periodic. -/
theorem divisor_lattice {f : ℂ → ℂ} {ω₁ ω₂ : ℂ} (hf : IsElliptic f ω₁ ω₂) (z : ℂ) (m n : ℤ) :
    MeromorphicOn.divisor f Set.univ (z + (m : ℂ) * ω₁ + (n : ℂ) * ω₂)
      = MeromorphicOn.divisor f Set.univ z := by
  have hper : Function.Periodic f ((m : ℂ) * ω₁ + (n : ℂ) * ω₂) :=
    (hf.periodic₁.int_mul m).add_period (hf.periodic₂.int_mul n)
  rw [add_assoc]
  exact divisor_translate hf.meromorphic hper z

theorem divisor_red {f : ℂ → ℂ} {ω₁ ω₂ : ℂ} (hf : IsElliptic f ω₁ ω₂) (z : ℂ) :
    MeromorphicOn.divisor f Set.univ (red ω₁ ω₂ z) = MeromorphicOn.divisor f Set.univ z := by
  have : red ω₁ ω₂ z = z + ((-⌊sc ω₁ ω₂ z⌋ : ℤ) : ℂ) * ω₁ + ((-⌊tc ω₁ ω₂ z⌋ : ℤ) : ℂ) * ω₂ := by
    simp only [red]; push_cast; ring
  rw [this, divisor_lattice hf]

theorem zpow_eq_zero_of_bounds {P ρ x y : ℝ} (hP : 1 < P) (hρ : 0 < ρ) {k : ℤ}
    (h : x = y * P ^ k) (hx1 : ρ < x) (hx2 : x < P * ρ) (hy1 : ρ < y) (hy2 : y < P * ρ) :
    k = 0 := by
  have hP0 : 0 < P := by linarith
  have hy0 : 0 < y := by linarith
  by_contra hk
  rcases lt_or_gt_of_ne hk with hk | hk
  · have h1 : P ^ k ≤ P ^ (-1 : ℤ) := zpow_le_zpow_right₀ hP.le (by omega)
    have h2 : x ≤ y * P⁻¹ := by
      rw [h, ← zpow_neg_one]; exact mul_le_mul_of_nonneg_left h1 hy0.le
    have h3 : y * P⁻¹ < ρ := by rw [← div_eq_mul_inv, div_lt_iff₀ hP0]; linarith
    linarith
  · have h1 : P ^ (1 : ℤ) ≤ P ^ k := zpow_le_zpow_right₀ hP.le (by omega)
    rw [zpow_one] at h1
    have h2 : y * P ≤ x := by rw [h]; exact mul_le_mul_of_nonneg_left h1 hy0.le
    nlinarith

theorem exists_zpow_window {x ρ P : ℝ} (hx : 0 < x) (hρ : 0 < ρ) (hP : 1 < P) :
    ∃ k : ℤ, ρ < x * P ^ (-k) ∧ x * P ^ (-k) ≤ P * ρ := by
  obtain ⟨k, hk1, hk2⟩ := exists_mem_Ioc_zpow (div_pos hx hρ) hP
  have hP0 : 0 < P := by linarith
  have hpk : 0 < P ^ k := zpow_pos hP0 k
  refine ⟨k, ?_, ?_⟩
  · rw [zpow_neg, ← div_eq_mul_inv, lt_div_iff₀ hpk]
    rw [lt_div_iff₀ hρ] at hk1; linarith
  · rw [zpow_neg, ← div_eq_mul_inv, div_le_iff₀ hpk]
    rw [div_le_iff₀ hρ, zpow_add_one₀ hP0.ne'] at hk2; linarith

set_option maxHeartbeats 1000000 in
/-- **Liouville's third theorem.** The divisor of an elliptic function sums to
zero over the half-open fundamental parallelogram. -/
theorem divisor_sum_eq_zero {f : ℂ → ℂ} {ω₁ ω₂ : ℂ}
    (hf : IsElliptic f ω₁ ω₂)
    (hindep : LinearIndependent ℝ ![ω₁, ω₂])
    (S : Finset ℂ)
    (hS : (S : Set ℂ) =
      {z | z ∈ fundamentalParallelogram ω₁ ω₂ ∧
        (MeromorphicOn.divisor f Set.univ) z ≠ 0}) :
    ∑ z ∈ S, (MeromorphicOn.divisor f Set.univ) z = 0 := by
  classical
  set D := MeromorphicOn.divisor f Set.univ with hD
  have hSD : ∀ z ∈ S, z ∈ fundamentalParallelogram ω₁ ω₂ ∧ D z ≠ 0 := by
    intro z hz
    have : z ∈ (S : Set ℂ) := hz
    rw [hS] at this; exact this
  have hmero : ∀ z, MeromorphicAt f z := fun z => hf.meromorphic z trivial
  -- the degenerate case: `f` vanishes locally somewhere, hence everywhere
  by_cases htop : ∃ z, meromorphicOrderAt f z = ⊤
  · have hall : ∀ z, meromorphicOrderAt f z = ⊤ := by
      intro z
      by_contra hz
      obtain ⟨z₀, hz₀⟩ := htop
      have := (hf.meromorphic.exists_meromorphicOrderAt_ne_top_iff_forall isConnected_univ).mp
        ⟨⟨z, trivial⟩, hz⟩ ⟨z₀, trivial⟩
      exact this hz₀
    refine Finset.sum_eq_zero fun z _ => ?_
    rw [hD, MeromorphicOn.divisor_apply hf.meromorphic (Set.mem_univ z), hall z]; rfl
  push_neg at htop
  -- nondegenerate periods
  have hω : ω₁ ≠ 0 := by
    have := hindep.ne_zero 0; simpa using this
  have him : (ω₂ / ω₁).im ≠ 0 := by
    intro h
    have hτ : ω₂ / ω₁ = ((ω₂ / ω₁).re : ℂ) := Complex.ext (by simp) (by simp [h])
    have h2 : ω₂ = ((ω₂ / ω₁).re : ℂ) * ω₁ := by
      rw [← hτ]; field_simp
    have := LinearIndependent.pair_iff.mp hindep ((ω₂ / ω₁).re) (-1)
      (by rw [Complex.real_smul, Complex.real_smul, ← h2]; push_cast; ring)
    norm_num at this
  -- orient the second period so that the dilation factor has norm `> 1`
  set σ : ℤ := if (ω₂ / ω₁).im < 0 then 1 else -1 with hσ
  have hσσ : (σ : ℝ) * σ = 1 := by rw [hσ]; split_ifs <;> norm_num
  set ω₂' : ℂ := (σ : ℂ) * ω₂ with hω₂'
  have hper₂' : Function.Periodic f ω₂' := hf.periodic₂.int_mul σ
  set τ' : ℂ := ω₂' / ω₁ with hτ'
  have hτ'im : τ'.im = σ * (ω₂ / ω₁).im := by
    rw [hτ', hω₂', mul_div_assoc]; simp
  have hτ'neg : τ'.im < 0 := by
    rw [hτ'im, hσ]
    split_ifs with h
    · simpa using h
    · push_neg at h; have := lt_of_le_of_ne h (Ne.symm him); simp; linarith
  set a : ℝ := -(2 * Real.pi * τ'.im) with ha
  have ha0 : 0 < a := by rw [ha]; nlinarith [Real.pi_pos]
  set p : ℂ := exp (2 * Real.pi * I * τ') with hp
  have hpn : ‖p‖ = Real.exp a := by rw [hp, norm_exp_two_pi_I_mul]
  have hp1 : 1 < ‖p‖ := by rw [hpn]; exact Real.one_lt_exp_iff.mpr ha0
  have hpn0 : 0 < ‖p‖ := by linarith
  -- the pull-back
  set c : ℂ := ω₁ / (2 * Real.pi * I) with hc
  have h2pi : (2 * (Real.pi : ℂ) * I) ≠ 0 := by simp [Real.pi_ne_zero, I_ne_zero]
  set g := annulusPullback f ω₁ with hg
  have hmg : ∀ w, w ≠ 0 → MeromorphicAt g w ∧
      meromorphicOrderAt g w = meromorphicOrderAt f (c * log w) :=
    fun w hw => annulusPullback_meromorphicAt_order hω hmero hf.periodic₁ hw
  have hinv : ∀ w, w ≠ 0 → g (p * w) = g w :=
    fun w hw => annulusPullback_mul hω hf.periodic₁ hper₂' hw
  obtain ⟨ρ, hρ1, -, hbd⟩ := exists_clean_radius hp1 (fun w hw => (hmg w hw).1)
    (fun w hw => by rw [(hmg w hw).2]; exact htop _)
  have hρ0 : 0 < ρ := by linarith
  set K := closedAnnulus ρ (‖p‖ * ρ) with hK
  have hK0 : ∀ w ∈ K, w ≠ 0 := by
    intro w hw h
    have := (mem_closedAnnulus.mp hw).1; rw [h, norm_zero] at this; linarith
  have hKm : MeromorphicOn g K := fun w hw => (hmg w (hK0 w hw)).1
  set S' : Finset ℂ :=
    ((MeromorphicOn.divisor g K).finiteSupport (isCompact_closedAnnulus _ _)).toFinset.filter
      (fun w => ρ < ‖w‖ ∧ ‖w‖ < ‖p‖ * ρ) with hS'def
  have hS' : (S' : Set ℂ) = {z | (ρ < ‖z‖ ∧ ‖z‖ < ‖p‖ * ρ) ∧
      (MeromorphicOn.divisor g K) z ≠ 0} := by
    ext w; simp [hS'def, Function.mem_support, and_comm]
  have h0 := annulus_divisor_sum_eq_zero hp1 hρ0 (fun w hw => (hmg w hw).1) hinv S' hbd hS'
  -- the divisor of `g` on the open annulus is the divisor of `f` at the reduced point
  have hDg : ∀ w, ρ < ‖w‖ → ‖w‖ < ‖p‖ * ρ →
      MeromorphicOn.divisor g K w = D (red ω₁ ω₂ (c * log w)) := by
    intro w h1 h2
    have hwK : w ∈ K := mem_closedAnnulus.mpr ⟨h1.le, h2.le⟩
    rw [MeromorphicOn.divisor_apply hKm hwK, (hmg w (hK0 w hwK)).2, divisor_red hf,
      MeromorphicOn.divisor_apply hf.meromorphic (Set.mem_univ _)]
  have hlog : ∀ w, w ≠ 0 → 2 * Real.pi * I * (c * log w / ω₁) = log w := by
    intro w hw; rw [hc]; field_simp
  rw [← h0]
  symm
  refine Finset.sum_bij (fun w _ => red ω₁ ω₂ (c * log w)) ?_ ?_ ?_ ?_
  · -- lands in `S`
    intro w hw
    have hw' : w ∈ (S' : Set ℂ) := hw
    rw [hS'] at hw'
    obtain ⟨⟨h1, h2⟩, hne⟩ := hw'
    have : (red ω₁ ω₂ (c * log w)) ∈ (S : Set ℂ) := by
      rw [hS]
      exact ⟨red_mem hω him _, by rw [← hDg w h1 h2]; exact hne⟩
    exact this
  · -- injective
    intro w₁ hw₁ w₂ hw₂ heq
    have hw₁' : w₁ ∈ (S' : Set ℂ) := hw₁
    have hw₂' : w₂ ∈ (S' : Set ℂ) := hw₂
    rw [hS'] at hw₁' hw₂'
    obtain ⟨⟨h11, h12⟩, -⟩ := hw₁'
    obtain ⟨⟨h21, h22⟩, -⟩ := hw₂'
    have hw₁0 : w₁ ≠ 0 := by intro h; rw [h, norm_zero] at h11; linarith
    have hw₂0 : w₂ ≠ 0 := by intro h; rw [h, norm_zero] at h21; linarith
    simp only [red] at heq
    set m : ℤ := ⌊sc ω₁ ω₂ (c * log w₁)⌋ - ⌊sc ω₁ ω₂ (c * log w₂)⌋ with hm
    set n : ℤ := ⌊tc ω₁ ω₂ (c * log w₁)⌋ - ⌊tc ω₁ ω₂ (c * log w₂)⌋ with hn
    have hdiff : c * log w₁ = c * log w₂ + (m : ℂ) * ω₁ + (n : ℂ) * ω₂ := by
      rw [hm, hn]; push_cast; linear_combination heq
    have hσ2 : (σ : ℂ) * σ = 1 := by exact_mod_cast hσσ
    have hτσ : ((n * σ : ℤ) : ℂ) * (2 * Real.pi * I * τ') = (n : ℂ) * (2 * Real.pi * I * (ω₂ / ω₁)) := by
      rw [hτ', hω₂']; push_cast
      linear_combination ((n : ℂ) * (2 * Real.pi * I) * (ω₂ / ω₁)) * hσ2
    have hlog1 : log w₁ = log w₂ + (m : ℂ) * (2 * Real.pi * I)
        + ((n * σ : ℤ) : ℂ) * (2 * Real.pi * I * τ') := by
      rw [hτσ, ← hlog w₁ hw₁0, ← hlog w₂ hw₂0, hdiff]
      field_simp
    have hw : w₁ = w₂ * p ^ (n * σ) := by
      rw [← exp_log hw₁0, hlog1, Complex.exp_add, Complex.exp_add, exp_log hw₂0,
        Complex.exp_int_mul_two_pi_mul_I, mul_one, Complex.exp_int_mul, hp]
    have hnorm : ‖w₁‖ = ‖w₂‖ * ‖p‖ ^ (n * σ) := by rw [hw, norm_mul, norm_zpow]
    have hk' : n * σ = 0 := zpow_eq_zero_of_bounds hp1 hρ0 hnorm h11 h12 h21 h22
    rw [hw, hk', zpow_zero, mul_one]
  · -- surjective
    intro z hz
    obtain ⟨hzP, hzD⟩ := hSD z hz
    obtain ⟨e, he⟩ : ∃ e : ℂ, e = exp (2 * Real.pi * I * (z / ω₁)) := ⟨_, rfl⟩
    have he0 : 0 < ‖e‖ := by rw [he]; exact norm_pos_iff.mpr (exp_ne_zero _)
    obtain ⟨k, hwlo0, hwhi0⟩ := exists_zpow_window he0 hρ0 hp1
    obtain ⟨w, hwdef⟩ : ∃ w : ℂ, w = e * p ^ (-k) := ⟨_, rfl⟩
    have hw0 : w ≠ 0 := by
      rw [hwdef]
      exact mul_ne_zero (norm_pos_iff.mp he0) (zpow_ne_zero _ (by
        intro h; rw [h, norm_zero] at hpn0; linarith))
    have hwn : ‖w‖ = ‖e‖ * ‖p‖ ^ (-k) := by rw [hwdef, norm_mul, norm_zpow]
    have hwlo : ρ < ‖w‖ := hwn ▸ hwlo0
    have hwhi : ‖w‖ ≤ ‖p‖ * ρ := hwn ▸ hwhi0
    -- `c log w` is `z` up to the lattice
    obtain ⟨m, hm⟩ : ∃ m : ℤ, log w = 2 * Real.pi * I * (z / ω₁)
        + (-k : ℤ) * (2 * Real.pi * I * τ') + m * (2 * Real.pi * I) := by
      have : exp (log w) = exp (2 * Real.pi * I * (z / ω₁) + (-k : ℤ) * (2 * Real.pi * I * τ')) := by
        rw [exp_log hw0, Complex.exp_add, Complex.exp_int_mul, hwdef, he, hp]
      obtain ⟨m, hm⟩ := exp_eq_exp_iff_exists_int.mp this
      exact ⟨m, hm⟩
    have hcl : c * log w = z + (m : ℂ) * ω₁ + ((-k * σ : ℤ) : ℂ) * ω₂ := by
      rw [hm, hc, hτ', hω₂']; push_cast; field_simp; ring
    have hred : red ω₁ ω₂ (c * log w) = z := by
      rw [hcl, red_add hω him, red_of_mem hω him hzP]
    have hDw : D (c * log w) ≠ 0 := by
      rw [← divisor_red hf, hred]; exact hzD
    have hwhi' : ‖w‖ < ‖p‖ * ρ := by
      refine lt_of_le_of_ne hwhi fun heq => hDw ?_
      obtain ⟨han, hne⟩ := hbd w (Or.inr heq)
      have hord0 : meromorphicOrderAt g w = 0 := by
        rw [han.meromorphicOrderAt_eq, analyticOrderAt_eq_zero.mpr (Or.inr hne)]; rfl
      rw [(hmg w hw0).2] at hord0
      rw [hD, MeromorphicOn.divisor_apply hf.meromorphic (Set.mem_univ _), hord0]; rfl
    refine ⟨w, ?_, hred⟩
    have : w ∈ (S' : Set ℂ) := by
      rw [hS']
      exact ⟨⟨hwlo, hwhi'⟩, by rw [hDg w hwlo hwhi', hred]; exact hzD⟩
    exact this
  · -- summands agree
    intro w hw
    have hw' : w ∈ (S' : Set ℂ) := hw
    rw [hS'] at hw'
    exact hDg w hw'.1.1 hw'.1.2

end QOU.Mathlib.LiouvilleThird

namespace QOU.Mathlib.EllipticDivisorDegree

/-- **Liouville's third theorem: the degree of an elliptic divisor is zero.**
For `f` meromorphic on `ℂ`, periodic under `ℝ`-independent `ω₁, ω₂`, and `S` the
finite set of points of the half-open fundamental parallelogram where the divisor
is nonzero, `Σ_{z∈S} ord_z f = 0`. Proved sorry-free; see
`QOU.Mathlib.LiouvilleThird.divisor_sum_eq_zero`. (The earlier statement carried
a nonconstancy hypothesis; it is not needed.) -/
-- Ref: [ahlfors1979] Ahlfors, Complex Analysis, 3rd ed., Ch. 7 §2 (Liouville's
--   third theorem on elliptic functions).
theorem elliptic_divisor_degree_zero {f : ℂ → ℂ} {ω₁ ω₂ : ℂ}
    (hf : IsElliptic f ω₁ ω₂)
    (hindep : LinearIndependent ℝ ![ω₁, ω₂])
    (S : Finset ℂ)
    (hS : (S : Set ℂ) =
      {z | z ∈ fundamentalParallelogram ω₁ ω₂ ∧
        (MeromorphicOn.divisor f Set.univ) z ≠ 0}) :
    ∑ z ∈ S, (MeromorphicOn.divisor f Set.univ) z = 0 :=
  QOU.Mathlib.LiouvilleThird.divisor_sum_eq_zero hf hindep S hS

end QOU.Mathlib.EllipticDivisorDegree


