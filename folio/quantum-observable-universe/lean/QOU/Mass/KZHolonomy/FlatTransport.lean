import QOU.Mass.KZHolonomy.LinearODE
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Topology.MetricSpace.Thickening
import Mathlib.Topology.UniformSpace.HeineCantor
import Mathlib.Analysis.Convex.Star

/-!
# Parallel transport of a flat connection on a star-shaped open set

Let `E` be a real normed space, `A` a real Banach algebra, `D ⊆ E` open, and
`ω : E → (E →L[ℝ] A)` a connection form on `D` with derivative `ω'`.  Transport along a
`C¹` path `γ : [0,1] → D` is the fundamental solution `U` of

    U'(t) = ω(γ t)(γ' t) · U(t),   U(0) = 1.

The form is *flat* when `∂_a ω_b − ∂_b ω_a = ω_a ω_b − ω_b ω_a`, i.e.

    ω' y a b − ω' y b a = ω y a * ω y b − ω y b * ω y a.

**Main result** (`flat_transport_eq`).  If `D` is star-shaped about `c` and `ω` is flat on
`D`, there is `Φ : E → A`, a unit at every point of `D`, such that transport along every
`C¹` path `γ` in `D` satisfies `U(1) · Φ(γ 0) = Φ(γ 1)`.  In particular the transport only
depends on the end points of the path (path independence), which is the form of homotopy
invariance used for the KZ braid representation in `BraidRep.lean`.

`Φ x` is radial transport from `c` to `x`.  The analytic input is that `Φ` is Fréchet
differentiable on `D` with `DΦ(x) h = ω(x)(h) · Φ(x)` (`hasFDerivAt_radialTransport`),
proved by a Grönwall estimate on

    G(t) = U_{x+h}(t) − U_x(t) − t · ω(γ t)(h) · U_x(t),

whose defect `G' − X_{x+h} G` is `o(‖h‖)` because the `O(t‖h‖)` commutator terms cancel by
flatness (`defect_identity`).  No homotopy theory is needed.
-/

set_option autoImplicit false

namespace QOU.Mass.KZHolonomy

open Set Filter Topology Metric

section Aux

/-- A function continuous at every point of a compact set is uniformly continuous *at* that
set, in metric form. -/
lemma exists_uniform_near_compact {α β : Type*} [PseudoMetricSpace α] [PseudoMetricSpace β]
    {s : Set α} (hs : IsCompact s) (f : α → β) (hf : ∀ a ∈ s, ContinuousAt f a)
    {ε : ℝ} (hε : 0 < ε) :
    ∃ η > 0, ∀ a ∈ s, ∀ b, dist a b < η → dist (f a) (f b) < ε := by
  obtain ⟨η, hη, h⟩ := Metric.mem_uniformity_dist.1
    (hs.uniformContinuousAt_of_continuousAt f hf (Metric.dist_mem_uniformity hε))
  exact ⟨η, hη, fun a ha b hab => h hab ha⟩

/-- Normed-group form of `exists_uniform_near_compact`. -/
lemma exists_uniform_near_compact_norm {α β : Type*} [PseudoMetricSpace α]
    [SeminormedAddCommGroup β] {s : Set α} (hs : IsCompact s) (f : α → β)
    (hf : ∀ a ∈ s, ContinuousAt f a) {ε : ℝ} (hε : 0 < ε) :
    ∃ η > 0, ∀ a ∈ s, ∀ b, dist a b < η → ‖f b - f a‖ < ε := by
  obtain ⟨η, hη, h⟩ := exists_uniform_near_compact hs f hf hε
  exact ⟨η, hη, fun a ha b hab => by rw [← dist_eq_norm, dist_comm]; exact h a ha b hab⟩

/-- `gronwallBound` with zero initial value is linear in the forcing term. -/
lemma gronwallBound_zero_eq (K r x : ℝ) :
    gronwallBound 0 K r x = r * gronwallBound 0 K 1 x := by
  unfold gronwallBound
  split_ifs <;> ring

lemma gronwallBound_zero_nonneg (K x : ℝ) (hx : 0 ≤ x) : 0 ≤ gronwallBound 0 K 1 x := by
  unfold gronwallBound
  split_ifs with hK
  · simpa using hx
  · rcases lt_or_gt_of_ne hK with hK | hK
    · have : Real.exp (K * x) ≤ 1 := Real.exp_le_one_iff.2 (mul_nonpos_of_nonpos_of_nonneg hK.le hx)
      have h2 : 0 ≤ 1 / K * (Real.exp (K * x) - 1) :=
        mul_nonneg_of_nonpos_of_nonpos (by rw [one_div]; exact inv_nonpos.2 hK.le) (by linarith)
      simpa using h2
    · have : 1 ≤ Real.exp (K * x) := Real.one_le_exp (mul_nonneg hK.le hx)
      have h2 : 0 ≤ 1 / K * (Real.exp (K * x) - 1) := mul_nonneg (by positivity) (by linarith)
      simpa using h2

end Aux

variable {E A : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedRing A] [NormedAlgebra ℝ A]

/-- The algebraic heart of the flatness argument: the defect of
`G = W − U − t·(b U)` against the perturbed equation is, after flatness, the sum of a term
linear in `d − t·L h (v+h)` and a term quadratic in `h`.  Here `P = a + b + d` stands for
`ω(γ t + t h)(v + h)`, `a = ω(γ t) v`, `b = ω(γ t) h`, `d = Δ(v + h)` and
`Lxy = ω'(γ t) x y`. -/
lemma defect_identity (t : ℝ) (P a b d U W Lhv Lvh Lhh : A) (hP : P = a + b + d)
    (hflat : Lhv - Lvh = b * a - a * b) :
    P * W - a * U - (t • (Lvh * U + b * (a * U)) + (1 : ℝ) • (b * U))
      - P * (W - U - t • (b * U))
      = (d - t • (Lhv + Lhh)) * U + t • ((Lhh + b * b + d * b) * U) := by
  subst hP
  obtain rfl : Lvh = Lhv - (b * a - a * b) := by rw [← hflat]; abel
  simp only [one_smul, add_mul, mul_sub, sub_mul, smul_add, smul_sub, smul_mul_assoc,
    mul_smul_comm, mul_assoc]
  abel

/-- Grönwall for a function whose defect against a bounded linear equation is bounded. -/
lemma norm_le_of_linear_defect {G G' p : ℝ → A} {K r : ℝ}
    (hG : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt G (G' t) (Icc 0 1) t)
    (hG0 : G 0 = 0) (hp : ∀ t ∈ Icc (0:ℝ) 1, ‖p t‖ ≤ K)
    (hr : ∀ t ∈ Icc (0:ℝ) 1, ‖G' t - p t * G t‖ ≤ r) :
    ‖G 1‖ ≤ gronwallBound 0 K r 1 := by
  have key := norm_le_gronwallBound_of_norm_deriv_right_le (f := G) (f' := G') (δ := 0)
    (K := K) (ε := r) (a := 0) (b := 1)
    (fun t ht => (hG t ht).continuousWithinAt)
    (fun t ht => (hG t (Ico_subset_Icc_self ht)).mono_of_mem_nhdsWithin
      (Icc_mem_nhdsGE_of_mem ht))
    (by simp [hG0])
    (fun t ht => by
      have ht' := Ico_subset_Icc_self ht
      calc ‖G' t‖ = ‖(G' t - p t * G t) + p t * G t‖ := by rw [sub_add_cancel]
        _ ≤ ‖G' t - p t * G t‖ + ‖p t * G t‖ := norm_add_le _ _
        _ ≤ r + K * ‖G t‖ := add_le_add (hr t ht')
            ((norm_mul_le _ _).trans (mul_le_mul_of_nonneg_right (hp t ht') (norm_nonneg _)))
        _ = K * ‖G t‖ + r := add_comm _ _)
    1 ⟨zero_le_one, le_rfl⟩
  simpa using key

/-! ### Flat connections, transport, radial transport -/

/-- `ω` is a flat connection form on `D` with derivative `ω'` (`ω' y a = ∂_a ω` at `y`):
differentiable with continuous derivative on `D`, and with vanishing curvature
`∂_a ω_b − ∂_b ω_a − [ω_a, ω_b] = 0`. -/
structure IsFlatOn (ω : E → E →L[ℝ] A) (ω' : E → E →L[ℝ] E →L[ℝ] A) (D : Set E) : Prop where
  hasFDerivAt : ∀ y ∈ D, HasFDerivAt ω (ω' y) y
  continuousOn : ContinuousOn ω' D
  flat : ∀ y ∈ D, ∀ a b : E, ω' y a b - ω' y b a = ω y a * ω y b - ω y b * ω y a

/-- `U` is the parallel transport of `ω` along the path `γ` with velocity `γ'`. -/
def IsTransport (ω : E → E →L[ℝ] A) (γ γ' : ℝ → E) (U : ℝ → A) : Prop :=
  IsFundSol (fun t => ω (γ t) (γ' t)) U

/-- The coefficient of the transport equation along the segment from `c` to `x`. -/
def radialX (ω : E → E →L[ℝ] A) (c x : E) (t : ℝ) : A := ω (c + t • (x - c)) (x - c)

variable [CompleteSpace A]

/-- Radial transport from `c` to `x` (equal to `1` when the coefficient is not continuous,
which never happens for `x` in a star-shaped domain of a connection). -/
noncomputable def radialTransport (ω : E → E →L[ℝ] A) (c x : E) : A := by
  classical
  exact if h : ContinuousOn (radialX ω c x) (Icc 0 1) then (exists_isFundSol h).choose 1 else 1

omit [CompleteSpace A] in
theorem IsFundSol.eqOn {X U V : ℝ → A} (hX : ContinuousOn X (Icc 0 1)) (hU : IsFundSol X U)
    (hV : IsFundSol X V) : EqOn U V (Icc 0 1) :=
  linear_eqOn_of_hasDerivWithinAt hX hU.2 hV.2 (hU.1.trans hV.1.symm)

theorem radialTransport_eq {ω : E → E →L[ℝ] A} {c x : E} {U : ℝ → A}
    (hX : ContinuousOn (radialX ω c x) (Icc 0 1)) (hU : IsFundSol (radialX ω c x) U) :
    radialTransport ω c x = U 1 := by
  rw [radialTransport, dif_pos hX]
  exact (exists_isFundSol hX).choose_spec.eqOn hX hU ⟨zero_le_one, le_rfl⟩

omit [CompleteSpace A] in
theorem continuousOn_radialX {ω : E → E →L[ℝ] A} {c x : E}
    (hω : ∀ t ∈ Icc (0:ℝ) 1, ContinuousAt ω (c + t • (x - c))) :
    ContinuousOn (radialX ω c x) (Icc 0 1) := by
  intro t ht
  have h1 : ContinuousAt (fun s : ℝ => ω (c + s • (x - c))) t :=
    ContinuousAt.comp (g := ω) (f := fun s : ℝ => c + s • (x - c)) (hω t ht) (by fun_prop)
  exact (h1.clm_apply continuousAt_const).continuousWithinAt

omit [CompleteSpace A] in
theorem continuousOn_transportCoeff {ω : E → E →L[ℝ] A} {γ γ' : ℝ → E}
    (hω : ∀ t ∈ Icc (0:ℝ) 1, ContinuousAt ω (γ t)) (hγ : ContinuousOn γ (Icc 0 1))
    (hγ' : ContinuousOn γ' (Icc 0 1)) :
    ContinuousOn (fun t => ω (γ t) (γ' t)) (Icc 0 1) := by
  have : ContinuousOn (fun t => ω (γ t)) (Icc 0 1) := fun t ht =>
    (hω t ht).comp_continuousWithinAt (hγ t ht)
  exact this.clm_apply hγ'

/-! ### Differentiability of radial transport -/

lemma mul_le_half_of_le {a e x : ℝ} (ha : 0 ≤ a) (he : 0 < e) (hx0 : 0 ≤ x)
    (hx : x ≤ e / (2 * (a + 1))) : a * x ≤ e / 2 := by
  have h1 : a * x ≤ (a + 1) * x := by nlinarith
  have h2 : (a + 1) * x ≤ (a + 1) * (e / (2 * (a + 1))) :=
    mul_le_mul_of_nonneg_left hx (by linarith)
  have h3 : (a + 1) * (e / (2 * (a + 1))) = e / 2 := by
    field_simp
  linarith

lemma norm_le_of_dist_lt {F : Type*} [SeminormedAddCommGroup F] {p q : F} {B r : ℝ}
    (hp : ‖p‖ ≤ B) (hpq : dist p q < r) : ‖q‖ ≤ B + r := by
  have := norm_sub_norm_le q p
  rw [norm_sub_rev, ← dist_eq_norm] at this
  linarith

set_option maxHeartbeats 1600000 in
/-- **Radial transport is differentiable**, with `DΦ(x) h = ω(x)(h) · Φ(x)`, at every `x`
whose segment from `c` lies in the open set `D` on which `ω` is flat. -/
theorem hasFDerivAt_radialTransport {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A}
    {D : Set E} {c x : E} (hD : IsOpen D) (hfl : IsFlatOn ω ω' D)
    (hseg : ∀ t ∈ Icc (0:ℝ) 1, c + t • (x - c) ∈ D) :
    HasFDerivAt (radialTransport ω c)
      ((ContinuousLinearMap.mul ℝ A).flip (radialTransport ω c x) ∘L ω x) x := by
  set v := x - c with hv
  set γ : ℝ → E := fun t => c + t • v with hγ
  have hωc : ∀ y ∈ D, ContinuousAt ω y := fun y hy => (hfl.hasFDerivAt y hy).continuousAt
  have hω'c : ∀ y ∈ D, ContinuousAt ω' y := fun y hy =>
    hfl.continuousOn.continuousAt (hD.mem_nhds hy)
  set K := γ '' Icc 0 1 with hK
  have hKc : IsCompact K := isCompact_Icc.image (by fun_prop)
  have hKD : K ⊆ D := by rintro _ ⟨t, ht, rfl⟩; exact hseg t ht
  have hγK : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ K := fun t ht => ⟨t, ht, rfl⟩
  obtain ⟨δ₀, hδ₀, hδ₀D⟩ := hKc.exists_thickening_subset_open hD hKD
  have hnearD : ∀ y ∈ K, ∀ z, dist y z < δ₀ → z ∈ D := fun y hy z hz =>
    hδ₀D (mem_thickening_iff.2 ⟨y, hy, by rwa [dist_comm]⟩)
  obtain ⟨M₀, hM₀⟩ := hKc.exists_bound_of_continuousOn (f := ω)
    (fun y hy => (hωc y (hKD hy)).continuousWithinAt)
  obtain ⟨M₀', hM₀'⟩ := hKc.exists_bound_of_continuousOn (f := ω')
    (fun y hy => (hω'c y (hKD hy)).continuousWithinAt)
  obtain ⟨η₁, hη₁, hη₁'⟩ := exists_uniform_near_compact_norm hKc ω (fun y hy => hωc y (hKD hy)) one_pos
  set M := max M₀ 0 + 1 with hM
  set M' := max M₀' 0 + 1 with hM'
  have hM0 : 0 ≤ M := by positivity
  have hM'0 : 0 ≤ M' := by positivity
  have hωK : ∀ y ∈ K, ‖ω y‖ ≤ M := fun y hy => by
    have := (hM₀ y hy).trans (le_max_left M₀ 0); linarith
  have hω'K : ∀ y ∈ K, ‖ω' y‖ ≤ M' := fun y hy => by
    have := (hM₀' y hy).trans (le_max_left M₀' 0); linarith
  have hωM : ∀ y ∈ K, ∀ z, dist y z < η₁ → ‖ω z‖ ≤ M := fun y hy z hz => by
    have h1 := hη₁' y hy z hz
    have h2 := norm_sub_norm_le (ω z) (ω y)
    have h3 := hωK y hy
    have h4 : ‖ω y‖ ≤ max M₀ 0 := (hM₀ y hy).trans (le_max_left _ _)
    linarith
  -- the unperturbed fundamental solution
  have hXc : ContinuousOn (radialX ω c x) (Icc 0 1) :=
    continuousOn_radialX (fun t ht => hωc _ (hseg t ht))
  obtain ⟨U, hU⟩ := exists_isFundSol hXc
  have hΦx : radialTransport ω c x = U 1 := radialTransport_eq hXc hU
  obtain ⟨B₀, hB₀⟩ := isCompact_Icc.exists_bound_of_continuousOn hU.continuousOn
  set BU := max B₀ 0 with hBU
  have hBU0 : 0 ≤ BU := le_max_right _ _
  have hUB : ∀ t ∈ Icc (0:ℝ) 1, ‖U t‖ ≤ BU := fun t ht => (hB₀ t ht).trans (le_max_left _ _)
  set Kg := M * (‖v‖ + 1) with hKg
  set g := gronwallBound 0 Kg 1 1 with hgdef
  have hg : 0 ≤ g := gronwallBound_zero_nonneg _ _ zero_le_one
  set C1 := M' + M ^ 2 + (1 + M') * (‖v‖ + 1) * M with hC1
  have hC10 : 0 ≤ C1 := by positivity
  clear_value g Kg C1 BU M M'
  -- derivative of `t ↦ ω (γ t) h`
  have hγd : ∀ t : ℝ, HasDerivAt γ v t := fun t => by
    show HasDerivAt (fun s : ℝ => c + s • v) v t
    simpa using ((hasDerivAt_id t).smul_const v).const_add c
  have hb : ∀ h : E, ∀ t ∈ Icc (0:ℝ) 1,
      HasDerivWithinAt (fun s => ω (γ s) h) (ω' (γ t) v h) (Icc 0 1) t := by
    intro h t ht
    have h1 : HasDerivAt (fun s => ω (γ s)) (ω' (γ t) v) t :=
      (hfl.hasFDerivAt _ (hseg t ht)).comp_hasDerivAt t (hγd t)
    simpa using (h1.clm_apply (hasDerivAt_const t h)).hasDerivWithinAt
  -- the core estimate
  have core : ∀ ε, 0 < ε → ε ≤ 1 → ∃ η > 0, ∀ h : E, ‖h‖ < η →
      ‖radialTransport ω c (x + h) - radialTransport ω c x - ω x h * radialTransport ω c x‖
        ≤ g * (‖h‖ * BU * (ε * (‖v‖ + 1) + ‖h‖ * C1)) := by
    intro ε hε hε1
    obtain ⟨η₃, hη₃, hη₃'⟩ :=
      exists_uniform_near_compact_norm hKc ω' (fun y hy => hω'c y (hKD hy)) hε
    refine ⟨min (min δ₀ 1) (min η₁ η₃), by positivity, ?_⟩
    intro h hh
    have hhδ : ‖h‖ < δ₀ := hh.trans_le ((min_le_left _ _).trans (min_le_left _ _))
    have hh1 : ‖h‖ ≤ 1 := (hh.trans_le ((min_le_left _ _).trans (min_le_right _ _))).le
    have hhη₁ : ‖h‖ < η₁ := hh.trans_le ((min_le_right _ _).trans (min_le_left _ _))
    have hhη₃ : ‖h‖ < η₃ := hh.trans_le ((min_le_right _ _).trans (min_le_right _ _))
    have hth : ∀ t ∈ Icc (0:ℝ) 1, ‖t • h‖ ≤ ‖h‖ := fun t ht => by
      rw [norm_smul, Real.norm_of_nonneg ht.1]
      exact mul_le_of_le_one_left (norm_nonneg _) ht.2
    have hdist : ∀ t ∈ Icc (0:ℝ) 1, dist (γ t) (γ t + t • h) ≤ ‖h‖ := fun t ht => by
      rw [dist_self_add_right]; exact hth t ht
    have hseg' : ∀ t : ℝ, c + t • (x + h - c) = γ t + t • h := fun t => by
      rw [show x + h - c = v + h by rw [hv]; abel, smul_add, ← add_assoc]
    have hXc' : ContinuousOn (radialX ω c (x + h)) (Icc 0 1) :=
      continuousOn_radialX (fun t ht => by
        rw [hseg' t]
        exact hωc _ (hnearD _ (hγK t ht) _ ((hdist t ht).trans_lt hhδ)))
    obtain ⟨W, hW⟩ := exists_isFundSol hXc'
    rw [radialTransport_eq hXc' hW, hΦx]
    -- the comparison function and its derivative
    set G : ℝ → A := fun t => W t - U t - t • (ω (γ t) h * U t) with hG
    set G' : ℝ → A := fun t => radialX ω c (x + h) t * W t - radialX ω c x t * U t
      - (t • (ω' (γ t) v h * U t + ω (γ t) h * (radialX ω c x t * U t))
        + (1:ℝ) • (ω (γ t) h * U t)) with hG'
    have hGd : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt G (G' t) (Icc 0 1) t := fun t ht =>
      ((hW.2 t ht).sub (hU.2 t ht)).sub
        ((hasDerivWithinAt_id t _).smul ((hb h t ht).fun_mul (hU.2 t ht)))
    have hG0 : G 0 = 0 := by simp [hG, hW.1, hU.1]
    have hp : ∀ t ∈ Icc (0:ℝ) 1, ‖radialX ω c (x + h) t‖ ≤ Kg := fun t ht => by
      have e : radialX ω c (x + h) t = ω (γ t + t • h) (v + h) := by
        rw [radialX, hseg' t, show x + h - c = v + h by rw [hv]; abel]
      rw [e]
      calc ‖ω (γ t + t • h) (v + h)‖ ≤ ‖ω (γ t + t • h)‖ * ‖v + h‖ := (ω _).le_opNorm _
        _ ≤ M * (‖v‖ + 1) := by
          gcongr
          · exact hωM _ (hγK t ht) _ ((hdist t ht).trans_lt hhη₁)
          · exact (norm_add_le _ _).trans (by linarith)
        _ = Kg := hKg.symm
    have hr : ∀ t ∈ Icc (0:ℝ) 1, ‖G' t - radialX ω c (x + h) t * G t‖
        ≤ ‖h‖ * BU * (ε * (‖v‖ + 1) + ‖h‖ * C1) := by
      intro t ht
      set Ω := ω (γ t) with hΩ
      set L := ω' (γ t) with hL
      set Δ := ω (γ t + t • h) - Ω with hΔ
      have hP : radialX ω c (x + h) t = Ω v + Ω h + Δ (v + h) := by
        rw [radialX, hseg' t, show x + h - c = v + h by rw [hv]; abel, hΔ,
          ContinuousLinearMap.sub_apply]
        simp only [map_add]
        abel
      have hid := defect_identity t (radialX ω c (x + h) t) (Ω v) (Ω h) (Δ (v + h)) (U t) (W t)
        (L h v) (L v h) (L h h) hP (hfl.flat (γ t) (hseg t ht) h v)
      have hGt : G' t - radialX ω c (x + h) t * G t
          = (Δ (v + h) - t • (L h v + L h h)) * U t
            + t • ((L h h + Ω h * Ω h + Δ (v + h) * Ω h) * U t) := hid
      rw [hGt]
      -- the estimates
      have e1 : Δ (v + h) - t • (L h v + L h h) = (Δ - L (t • h)) (v + h) := by
        simp only [ContinuousLinearMap.sub_apply, map_smul, ContinuousLinearMap.smul_apply,
          map_add, smul_add]
        abel
      have hmvt : ‖Δ - L (t • h)‖ ≤ ε * ‖h‖ := by
        have hball : ∀ z ∈ ball (γ t) (min η₃ δ₀), HasFDerivWithinAt ω (ω' z)
            (ball (γ t) (min η₃ δ₀)) z := fun z hz =>
          (hfl.hasFDerivAt z (hnearD _ (hγK t ht) z
            ((mem_ball'.1 hz).trans_le (min_le_right _ _)))).hasFDerivWithinAt
        have hbd : ∀ z ∈ ball (γ t) (min η₃ δ₀), ‖ω' z - L‖ ≤ ε := fun z hz => by
          exact (hη₃' (γ t) (hγK t ht) z ((mem_ball'.1 hz).trans_le (min_le_left _ _))).le
        have hys : γ t + t • h ∈ ball (γ t) (min η₃ δ₀) :=
          mem_ball'.2 ((hdist t ht).trans_lt (lt_min hhη₃ hhδ))
        have := (convex_ball (γ t) (min η₃ δ₀)).norm_image_sub_le_of_norm_hasFDerivWithin_le'
          hball hbd (mem_ball_self (lt_min hη₃ hδ₀)) hys
        rw [add_sub_cancel_left] at this
        calc ‖Δ - L (t • h)‖ = ‖ω (γ t + t • h) - ω (γ t) - L (t • h)‖ := by rw [hΔ, hΩ]
          _ ≤ ε * ‖t • h‖ := this
          _ ≤ ε * ‖h‖ := by gcongr; exact hth t ht
      have hΩb : ‖Ω‖ ≤ M := hωK _ (hγK t ht)
      have hLb : ‖L‖ ≤ M' := hω'K _ (hγK t ht)
      have hLth : ‖L (t • h)‖ ≤ M' * ‖h‖ :=
        (L.le_opNorm _).trans (mul_le_mul hLb (hth t ht) (norm_nonneg _) hM'0)
      have hΔb : ‖Δ‖ ≤ (ε + M') * ‖h‖ := by
        calc ‖Δ‖ = ‖(Δ - L (t • h)) + L (t • h)‖ := by rw [sub_add_cancel]
          _ ≤ ‖Δ - L (t • h)‖ + ‖L (t • h)‖ := norm_add_le _ _
          _ ≤ ε * ‖h‖ + M' * ‖h‖ := add_le_add hmvt hLth
          _ = (ε + M') * ‖h‖ := by ring
      have hvh : ‖v + h‖ ≤ ‖v‖ + 1 := (norm_add_le _ _).trans (by linarith)
      have hnh := norm_nonneg h
      have hnv := norm_nonneg v
      have hεM : 0 ≤ ε + M' := by linarith
      have hMh : 0 ≤ M * ‖h‖ := mul_nonneg hM0 hnh
      have hb' : ‖Ω h‖ ≤ M * ‖h‖ :=
        (Ω.le_opNorm h).trans (mul_le_mul_of_nonneg_right hΩb hnh)
      have hLhh : ‖L h h‖ ≤ M' * ‖h‖ * ‖h‖ :=
        ((L h).le_opNorm h).trans (mul_le_mul_of_nonneg_right
          ((L.le_opNorm h).trans (mul_le_mul_of_nonneg_right hLb hnh)) hnh)
      have hd : ‖Δ (v + h)‖ ≤ (ε + M') * ‖h‖ * (‖v‖ + 1) :=
        (Δ.le_opNorm _).trans (mul_le_mul hΔb hvh (norm_nonneg _) (mul_nonneg hεM hnh))
      have hUt := hUB t ht
      have ht0 : |t| ≤ 1 := by rw [abs_of_nonneg ht.1]; exact ht.2
      have hX : ‖Δ (v + h) - t • (L h v + L h h)‖ ≤ ε * ‖h‖ * (‖v‖ + 1) := by
        rw [e1]
        exact ((Δ - L (t • h)).le_opNorm _).trans
          (mul_le_mul hmvt hvh (norm_nonneg _) (mul_nonneg hε.le hnh))
      have hY : ‖L h h + Ω h * Ω h + Δ (v + h) * Ω h‖
          ≤ M' * ‖h‖ * ‖h‖ + (M * ‖h‖) * (M * ‖h‖)
            + ((ε + M') * ‖h‖ * (‖v‖ + 1)) * (M * ‖h‖) :=
        (norm_add_le _ _).trans (add_le_add ((norm_add_le _ _).trans (add_le_add hLhh
          ((norm_mul_le _ _).trans (mul_le_mul hb' hb' (norm_nonneg _) hMh))))
          ((norm_mul_le _ _).trans (mul_le_mul hd hb' (norm_nonneg _)
            (mul_nonneg (mul_nonneg hεM hnh) (by linarith)))))
      have hA1 : 0 ≤ ε * ‖h‖ * (‖v‖ + 1) := mul_nonneg (mul_nonneg hε.le hnh) (by linarith)
      have hA2 : 0 ≤ M' * ‖h‖ * ‖h‖ + (M * ‖h‖) * (M * ‖h‖)
            + ((ε + M') * ‖h‖ * (‖v‖ + 1)) * (M * ‖h‖) := by
        have := norm_nonneg (L h h + Ω h * Ω h + Δ (v + h) * Ω h)
        linarith
      have hfin : ‖h‖ * BU * (ε * (‖v‖ + 1) + ‖h‖ * C1)
          - ((ε * ‖h‖ * (‖v‖ + 1)) * BU + (M' * ‖h‖ * ‖h‖ + (M * ‖h‖) * (M * ‖h‖)
            + ((ε + M') * ‖h‖ * (‖v‖ + 1)) * (M * ‖h‖)) * BU)
          = ‖h‖ * ‖h‖ * (‖v‖ + 1) * M * BU * (1 - ε) := by
        rw [hC1]; ring
      have hfin0 : 0 ≤ ‖h‖ * ‖h‖ * (‖v‖ + 1) * M * BU * (1 - ε) :=
        mul_nonneg (mul_nonneg (mul_nonneg (mul_nonneg (mul_nonneg hnh hnh) (by linarith)) hM0)
          hBU0) (by linarith)
      calc _ ≤ ‖Δ (v + h) - t • (L h v + L h h)‖ * ‖U t‖
            + ‖(L h h + Ω h * Ω h + Δ (v + h) * Ω h)‖ * ‖U t‖ := by
            refine (norm_add_le _ _).trans (add_le_add (norm_mul_le _ _) ?_)
            rw [norm_smul, Real.norm_eq_abs]
            exact (mul_le_of_le_one_left (norm_nonneg _) ht0).trans (norm_mul_le _ _)
        _ ≤ (ε * ‖h‖ * (‖v‖ + 1)) * BU
            + (M' * ‖h‖ * ‖h‖ + (M * ‖h‖) * (M * ‖h‖)
              + ((ε + M') * ‖h‖ * (‖v‖ + 1)) * (M * ‖h‖)) * BU :=
            add_le_add (mul_le_mul hX hUt (norm_nonneg _) hA1)
              (mul_le_mul hY hUt (norm_nonneg _) hA2)
        _ ≤ ‖h‖ * BU * (ε * (‖v‖ + 1) + ‖h‖ * C1) := by linarith
    have key := norm_le_of_linear_defect hGd hG0 hp hr
    rw [gronwallBound_zero_eq, ← hgdef] at key
    have hG1 : G 1 = W 1 - U 1 - ω x h * U 1 := by
      simp only [hG, one_smul, hγ, hv, add_sub_cancel]
    rw [← hG1]
    exact key.trans_eq (mul_comm _ _)
  -- conclude
  rw [hasFDerivAt_iff_isLittleO_nhds_zero, Asymptotics.isLittleO_iff]
  intro ε' hε'
  set Q := g * BU with hQ
  have hQ0 : 0 ≤ Q := mul_nonneg hg hBU0
  set ε := min 1 (ε' / (2 * (Q * (‖v‖ + 1) + 1))) with hεdef
  have hε0 : 0 < ε := lt_min one_pos (by positivity)
  obtain ⟨η, hη, hηb⟩ := core ε hε0 (min_le_left _ _)
  have hmem : ball (0 : E) (min η (ε' / (2 * (Q * C1 + 1)))) ∈ 𝓝 (0 : E) :=
    ball_mem_nhds _ (lt_min hη (by positivity))
  filter_upwards [hmem] with h hh
  rw [mem_ball_zero_iff] at hh
  have h1 := hηb h (hh.trans_le (min_le_left _ _))
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.flip_apply,
    ContinuousLinearMap.mul_apply']
  refine h1.trans ?_
  have a1 : Q * (‖v‖ + 1) * ε ≤ ε' / 2 :=
    mul_le_half_of_le (by positivity) hε' hε0.le (min_le_right _ _)
  have a2 : Q * C1 * ‖h‖ ≤ ε' / 2 :=
    mul_le_half_of_le (by positivity) hε' (norm_nonneg _) (hh.trans_le (min_le_right _ _)).le
  have hnh := norm_nonneg h
  calc g * (‖h‖ * BU * (ε * (‖v‖ + 1) + ‖h‖ * C1))
      = ‖h‖ * (Q * (‖v‖ + 1) * ε + Q * C1 * ‖h‖) := by rw [hQ]; ring
    _ ≤ ‖h‖ * (ε' / 2 + ε' / 2) := by gcongr
    _ = ε' * ‖h‖ := by ring

/-! ### Path independence on a star-shaped domain -/

omit [CompleteSpace A] in
lemma seg_mem_of_starConvex {D : Set E} {c x : E} (hstar : StarConvex ℝ c D) (hx : x ∈ D)
    {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) : c + t • (x - c) ∈ D := by
  have := hstar hx (sub_nonneg.2 ht.2) ht.1 (sub_add_cancel 1 t)
  convert this using 1
  simp only [sub_smul, one_smul, smul_sub]
  abel

/-- Radial transport is invertible at every point of a star-shaped domain. -/
theorem isUnit_radialTransport {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A}
    {D : Set E} {c x : E} (hstar : StarConvex ℝ c D) (hfl : IsFlatOn ω ω' D) (hx : x ∈ D) :
    IsUnit (radialTransport ω c x) := by
  have hXc : ContinuousOn (radialX ω c x) (Icc 0 1) := continuousOn_radialX fun t ht =>
    (hfl.hasFDerivAt _ (seg_mem_of_starConvex hstar hx ht)).continuousAt
  obtain ⟨U, hU⟩ := exists_isFundSol hXc
  rw [radialTransport_eq hXc hU]
  exact hU.isUnit hXc 1 ⟨zero_le_one, le_rfl⟩

/-- **Path independence of flat transport.**  On an open domain `D`, star-shaped about `c`,
on which `ω` is flat, transport along any `C¹` path `γ` in `D` satisfies
`U(1) · Φ(γ 0) = Φ(γ 1)`, where `Φ = radialTransport ω c`. -/
theorem flat_transport_eq {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A}
    {D : Set E} {c : E} (hD : IsOpen D) (hstar : StarConvex ℝ c D) (hfl : IsFlatOn ω ω' D)
    {γ γ' : ℝ → E} (hγD : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ D)
    (hγd : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt γ (γ' t) (Icc 0 1) t)
    (hγ'c : ContinuousOn γ' (Icc 0 1)) {U : ℝ → A} (hU : IsTransport ω γ γ' U) :
    U 1 * radialTransport ω c (γ 0) = radialTransport ω c (γ 1) := by
  have hXc : ContinuousOn (fun t => ω (γ t) (γ' t)) (Icc 0 1) :=
    continuousOn_transportCoeff (fun t ht => (hfl.hasFDerivAt _ (hγD t ht)).continuousAt)
      (fun t ht => (hγd t ht).continuousWithinAt) hγ'c
  have hΦd : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt (fun s => radialTransport ω c (γ s))
      (ω (γ t) (γ' t) * radialTransport ω c (γ t)) (Icc 0 1) t := fun t ht => by
    have := (hasFDerivAt_radialTransport hD hfl
      (fun s hs => seg_mem_of_starConvex hstar (hγD t ht) hs)).comp_hasDerivWithinAt t (hγd t ht)
    simpa only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.flip_apply,
      ContinuousLinearMap.mul_apply'] using this
  have hV : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt (fun s => U s * radialTransport ω c (γ 0))
      (ω (γ t) (γ' t) * (U t * radialTransport ω c (γ 0))) (Icc 0 1) t := fun t ht => by
    simpa only [mul_assoc] using (hU.2 t ht).mul_const (radialTransport ω c (γ 0))
  have := linear_eqOn_of_hasDerivWithinAt hXc hV hΦd (by simp [hU.1]) ⟨zero_le_one, le_rfl⟩
  simpa using this

/-- Transport between two points of a flat star-shaped domain does not depend on the path. -/
theorem flat_transport_eq_of_endpoints {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A}
    {D : Set E} {c : E} (hD : IsOpen D) (hstar : StarConvex ℝ c D) (hfl : IsFlatOn ω ω' D)
    {γ₁ γ₁' γ₂ γ₂' : ℝ → E} (h₁D : ∀ t ∈ Icc (0:ℝ) 1, γ₁ t ∈ D)
    (h₁d : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt γ₁ (γ₁' t) (Icc 0 1) t)
    (h₁c : ContinuousOn γ₁' (Icc 0 1)) (h₂D : ∀ t ∈ Icc (0:ℝ) 1, γ₂ t ∈ D)
    (h₂d : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt γ₂ (γ₂' t) (Icc 0 1) t)
    (h₂c : ContinuousOn γ₂' (Icc 0 1)) (h0 : γ₁ 0 = γ₂ 0) (h1 : γ₁ 1 = γ₂ 1)
    {U₁ U₂ : ℝ → A} (hU₁ : IsTransport ω γ₁ γ₁' U₁) (hU₂ : IsTransport ω γ₂ γ₂' U₂) :
    U₁ 1 = U₂ 1 := by
  have e₁ := flat_transport_eq hD hstar hfl h₁D h₁d h₁c hU₁
  have e₂ := flat_transport_eq hD hstar hfl h₂D h₂d h₂c hU₂
  rw [h0, h1] at e₁
  exact (isUnit_radialTransport hstar hfl (h₂D 0 ⟨le_rfl, zero_le_one⟩)).mul_right_cancel
    (e₁.trans e₂.symm)

end QOU.Mass.KZHolonomy
