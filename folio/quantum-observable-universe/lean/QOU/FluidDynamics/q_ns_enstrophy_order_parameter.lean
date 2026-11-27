import HeckeTemperleyLieb.QIntegerCanonical
import QOU.FluidDynamics.q_ns_wellposedness

/-!
# QOU.FluidDynamics.q_ns_enstrophy_order_parameter

Content block: [`conj:regularity-breakdown`](../../../quantum-observable-universe/fluid-dynamics/regularity-breakdown.md),
**Part A** (the `q`-family): the enstrophy order parameter

  `Ω(q) = sup_{t ≥ 0} ∑_k [k]_q² |v̂_k(t)|²`

is asserted to diverge as `q → 1⁺`, "for suitable data".  Bean `qou-innq`.

## What this file proves (sorry-free)

**Part A is incompatible with the corpus's own formalisation of
`thm:q-ns-wellposedness` (`QNsWellposednessContext`) whenever the initial
modal amplitudes do not depend on `q`; and with `q`-dependent data it carries
no content.**  Four steps.

1. **Algebraic, over any ordered field.**  The balanced quantum integer
   `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)` is the Chebyshev sequence `U_{n-1}` evaluated
   at `s = q + q⁻¹` (`qIntBal_eq_chebU`), and that sequence is nonnegative,
   nondecreasing in `n` and nondecreasing in `s` for `s ≥ 2`
   (`chebU_nonneg_mono`, `chebU_mono_param`).  Since `q ↦ q + q⁻¹` is
   nondecreasing on `q ≥ 1`, `[n]_q` is nondecreasing in `q` on `q > 1`
   (`qIntBal_mono`).  No analysis: induction and ring identities.
2. **The supremum over time is attained at `t = 0`.**  The context's modal
   inequality gives `|v̂_k(t)| ≤ |v̂_k(0)| e^{−ν_q [k]_q² t} ≤ |v̂_k(0)|`
   (already proved there as `q_ns_spectral_decay`), so the enstrophy at every
   `t ≥ 0` is at most the initial enstrophy, and `Ω(q)` *equals* the initial
   enstrophy (`q_ns_enstrophy_isGreatest`).
3. **Monotone in `q`, hence bounded as `q → 1⁺`.**  For `q`-independent
   amplitudes `a_k`, `Ω(q) = ∑ [k]_q² a_k²` is nondecreasing in `q`, so
   `Ω(q) ≤ Ω(q₀)` on `(1, q₀]` and `Ω` does not tend to `+∞` as `q → 1⁺`
   (`omega_not_tendsto_atTop`, and for families of contexts
   `partA_fails_for_q_independent_data`).
4. **`q`-dependent data makes Part A empty.**  Every nonnegative function of
   `q` is `Ω(q)` for some `q`-dependent datum (`omega_realises_any`), so
   "`Ω(q) ~ (q − 1)^{−α}` for suitable data" holds for every `α` and constrains
   nothing.

**The hypotheses are not vacuous.**  `stokesContext` instantiates every field
of `QNsWellposednessContext`, for every `q > 1` and every amplitude sequence,
with the linear Stokes flow `v̂_k(t) = a_k e^{−ν_q [k]_q² t}`.  It shows two things.
The family hypotheses of step 3 hold with nonzero data
(`partA_fails_stokes`). The context also does not tell Stokes flow from
Navier–Stokes flow. That is the
diagnosis: the field `modal_inequality` forbids the nonlinear transfer between
modes that Part A's heuristic ("loss of UV regularisation", "cascade becomes
continuous") relies on.

## Scope of the negative

(b), relative to `QNsWellposednessContext`: the invariant is the field
`modal_inequality` together with the monotonicity of `[k]_q` (step 1).  It is
**not** a statement about any equation whose modes exchange energy; a context
whose modal law keeps the triad transfer term is not covered, and there Part A
remains open.  No empirical value enters any proof.

## References
- [leitner2026] quantum-observable-universe/fluid-dynamics/regularity-breakdown.md
  (`conj:regularity-breakdown`, Part A)
- [leitner2026] quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md
  (`thm:q-ns-wellposedness`, property 3)
-/

namespace QOU.FluidDynamics.EnstrophyOrderParameter

open Filter Topology Set
open QOU.QInteger

/-! ### Step 1: the balanced quantum integer is monotone in `q` -/

/-- The Chebyshev sequence `U_{n-1}(s/2)`: `u₀ = 0`, `u₁ = 1`,
    `u_{n+2} = s·u_{n+1} − u_n`.  Defined over any commutative ring. -/
def chebU {K : Type*} [CommRing K] (s : K) : ℕ → K
  | 0 => 0
  | 1 => 1
  | (n + 2) => s * chebU s (n + 1) - chebU s n

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- For `s ≥ 2` the Chebyshev sequence is nonnegative and nondecreasing. -/
theorem chebU_nonneg_mono {s : K} (hs : 2 ≤ s) :
    ∀ n, 0 ≤ chebU s n ∧ chebU s n ≤ chebU s (n + 1) := by
  intro n
  induction n with
  | zero => simp [chebU]
  | succ n ih =>
    obtain ⟨h0, h1⟩ := ih
    refine ⟨le_trans h0 h1, ?_⟩
    show chebU s (n + 1) ≤ s * chebU s (n + 1) - chebU s n
    have hu : 0 ≤ chebU s (n + 1) := le_trans h0 h1
    nlinarith [mul_nonneg (sub_nonneg.mpr hs) hu]

/-- For `2 ≤ s ≤ t`, the difference `U(t) − U(s)` is nonnegative and
    nondecreasing in `n`; in particular `U_n(s) ≤ U_n(t)`. -/
theorem chebU_mono_param {s t : K} (hs : 2 ≤ s) (hst : s ≤ t) :
    ∀ n, 0 ≤ chebU t n - chebU s n ∧
      chebU t n - chebU s n ≤ chebU t (n + 1) - chebU s (n + 1) := by
  intro n
  induction n with
  | zero => simp [chebU]
  | succ n ih =>
    obtain ⟨h0, h1⟩ := ih
    refine ⟨le_trans h0 h1, ?_⟩
    show chebU t (n + 1) - chebU s (n + 1) ≤
      (t * chebU t (n + 1) - chebU t n) - (s * chebU s (n + 1) - chebU s n)
    have hu : 0 ≤ chebU s (n + 1) := (chebU_nonneg_mono hs (n + 1)).1
    have hw : 0 ≤ chebU t (n + 1) - chebU s (n + 1) := le_trans h0 h1
    have ht2 : 0 ≤ t - 2 := by linarith
    nlinarith [mul_nonneg ht2 hw, mul_nonneg (sub_nonneg.mpr hst) hu]

/-- The three-term recurrence of the balanced quantum integer. -/
theorem qIntBal_rec (q : K) (hq0 : q ≠ 0) (n : ℕ) :
    qIntBal q (n + 2) = (q + q⁻¹) * qIntBal q (n + 1) - qIntBal q n := by
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
  have hnum : q ^ (n + 2) - q⁻¹ ^ (n + 2)
      = (q + q⁻¹) * (q ^ (n + 1) - q⁻¹ ^ (n + 1)) - (q ^ n - q⁻¹ ^ n) := by
    linear_combination (q⁻¹ ^ n - q ^ n) * hqq
  simp only [qIntBal_def]
  rw [hnum]
  ring

/-- **`[n]_q = U_{n-1}` at `s = q + q⁻¹`.** -/
theorem qIntBal_eq_chebU (q : K) (hq0 : q ≠ 0) (hq : q - q⁻¹ ≠ 0) :
    ∀ n, qIntBal q n = chebU (q + q⁻¹) n
  | 0 => by simp [chebU]
  | 1 => by simp [chebU, div_self hq]
  | (n + 2) => by
    rw [qIntBal_rec q hq0 n, qIntBal_eq_chebU q hq0 hq (n + 1),
      qIntBal_eq_chebU q hq0 hq n]
    rfl

/-- `q + q⁻¹ ≥ 2` for `q > 0`. -/
theorem two_le_add_inv {q : K} (hq : 0 < q) : 2 ≤ q + q⁻¹ := by
  have hi : 0 < q⁻¹ := inv_pos.mpr hq
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq.ne'
  nlinarith [mul_nonneg (sq_nonneg (q - 1)) hi.le]

/-- `q ↦ q + q⁻¹` is nondecreasing on `q ≥ 1`. -/
theorem add_inv_mono {q p : K} (hq : 1 ≤ q) (hqp : q ≤ p) :
    q + q⁻¹ ≤ p + p⁻¹ := by
  have hq0 : 0 < q := lt_of_lt_of_le zero_lt_one hq
  have hp0 : 0 < p := lt_of_lt_of_le hq0 hqp
  have key : q⁻¹ - p⁻¹ ≤ p - q := by
    rw [inv_sub_inv hq0.ne' hp0.ne']
    apply div_le_self (sub_nonneg.mpr hqp)
    nlinarith
  linarith

theorem sub_inv_ne_zero {q : K} (hq : 1 < q) : q - q⁻¹ ≠ 0 := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  intro h
  linarith

/-- `[n]_q ≥ 0` for `q > 1`. -/
theorem qIntBal_nonneg {q : K} (hq : 1 < q) (n : ℕ) : 0 ≤ qIntBal q n := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  rw [qIntBal_eq_chebU q hq0.ne' (sub_inv_ne_zero hq)]
  exact (chebU_nonneg_mono (two_le_add_inv hq0) n).1

/-- **`[n]_q` is nondecreasing in `q` on `q > 1`.**  Algebraic: no limits,
    no derivatives. -/
theorem qIntBal_mono {q p : K} (hq : 1 < q) (hqp : q ≤ p) (n : ℕ) :
    qIntBal q n ≤ qIntBal p n := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hp : 1 < p := lt_of_lt_of_le hq hqp
  have hp0 : 0 < p := lt_trans zero_lt_one hp
  rw [qIntBal_eq_chebU q hq0.ne' (sub_inv_ne_zero hq),
    qIntBal_eq_chebU p hp0.ne' (sub_inv_ne_zero hp)]
  have := (chebU_mono_param (two_le_add_inv hq0) (add_inv_mono hq.le hqp) n).1
  linarith

end Ordered

/-! ### Step 3 (abstract form): `Ω(q) = ∑ [k]_q² a_k²` is monotone in `q` -/

/-- The enstrophy of `q`-independent modal amplitudes `a`, at parameter `q`. -/
noncomputable def omega (a : ℕ → ℝ) (q : ℝ) : ℝ :=
  ∑' k, qIntBal q k ^ 2 * a k ^ 2

theorem omega_term_mono {a : ℕ → ℝ} {q p : ℝ} (hq : 1 < q) (hqp : q ≤ p) (k : ℕ) :
    qIntBal q k ^ 2 * a k ^ 2 ≤ qIntBal p k ^ 2 * a k ^ 2 :=
  mul_le_mul_of_nonneg_right
    (pow_le_pow_left₀ (qIntBal_nonneg hq k) (qIntBal_mono hq hqp k) 2) (sq_nonneg _)

/-- **Monotonicity.**  If the enstrophy series converges at `q₀`, it converges
    at every `q ∈ (1, q₀]` and its sum there is at most the sum at `q₀`. -/
theorem omega_mono {a : ℕ → ℝ} {q q₀ : ℝ} (hq : 1 < q) (hqq₀ : q ≤ q₀)
    (hsum : Summable fun k => qIntBal q₀ k ^ 2 * a k ^ 2) :
    Summable (fun k => qIntBal q k ^ 2 * a k ^ 2) ∧ omega a q ≤ omega a q₀ := by
  have hle := omega_term_mono (a := a) hq hqq₀
  have hnn : ∀ k, 0 ≤ qIntBal q k ^ 2 * a k ^ 2 :=
    fun k => mul_nonneg (sq_nonneg _) (sq_nonneg _)
  have hs : Summable (fun k => qIntBal q k ^ 2 * a k ^ 2) :=
    Summable.of_nonneg_of_le hnn hle hsum
  exact ⟨hs, hs.tsum_le_tsum hle hsum⟩

/-- **Part A fails for `q`-independent amplitudes.**  If the enstrophy is finite
    at a single `q₀ > 1`, then `Ω(q)` does not tend to `+∞` as `q → 1⁺`. -/
theorem omega_not_tendsto_atTop {a : ℕ → ℝ} {q₀ : ℝ} (hq₀ : 1 < q₀)
    (hsum : Summable fun k => qIntBal q₀ k ^ 2 * a k ^ 2) :
    ¬ Tendsto (omega a) (𝓝[>] 1) atTop := by
  intro h
  have hev : ∀ᶠ q in 𝓝[>] (1 : ℝ), omega a q₀ < omega a q ∧ q ∈ Ioc 1 q₀ :=
    (h.eventually (eventually_gt_atTop (omega a q₀))).and (Ioc_mem_nhdsGT hq₀)
  obtain ⟨q, hlt, hq1, hqq₀⟩ := hev.exists
  exact absurd (omega_mono hq1 hqq₀ hsum).2 (not_le.mpr hlt)

/-! ### Step 4: with `q`-dependent data, Part A says nothing -/

theorem omega_single (c q : ℝ) (hq : 1 < q) :
    omega (fun k => if k = 1 then c else 0) q = c ^ 2 := by
  unfold omega
  rw [tsum_eq_single 1]
  · have h1 : qIntBal q 1 = 1 := by
      simp [div_self (sub_inv_ne_zero hq)]
    show qIntBal q 1 ^ 2 * (if (1 : ℕ) = 1 then c else 0) ^ 2 = c ^ 2
    rw [h1, if_pos rfl]
    ring
  · intro k hk
    simp [hk]

/-- **Every nonnegative profile is realised.**  For any `f : ℝ → ℝ` with
    `f ≥ 0` on `q > 1`, the `q`-dependent datum `a(q) = √(f q)·δ_{k,1}` has
    `Ω(q) = f q`.  So "`Ω(q) ~ (q−1)^{−α}` for suitable data" holds for every
    `α`, and for no divergence at all, depending only on how the data are chosen. -/
theorem omega_realises_any (f : ℝ → ℝ) (hf : ∀ q, 1 < q → 0 ≤ f q) :
    ∃ a : ℝ → ℕ → ℝ, ∀ q, 1 < q → omega (a q) q = f q :=
  ⟨fun q k => if k = 1 then Real.sqrt (f q) else 0, fun q hq => by
    rw [omega_single _ q hq, Real.sq_sqrt (hf q hq)]⟩

/-! ### Step 2: inside `QNsWellposednessContext`, `Ω(q)` is the initial enstrophy -/

/-- The enstrophy `∑_k [k]_q² |v̂_k|²` of a velocity, in a context. -/
noncomputable def qnsEnstrophy [ctx : QNsWellposednessContext] (v : ctx.Velocity) : ℝ :=
  ∑' k, ctx.q_int k ^ 2 * ctx.v_hat k v ^ 2

/-- **The enstrophy never exceeds its initial value.**  Uses only
    `q_ns_spectral_decay` (proved from the field `modal_inequality`), and
    that `v̂_k` is a magnitude, hence nonnegative. -/
theorem q_ns_enstrophy_le_initial [ctx : QNsWellposednessContext]
    (sol : ℝ → ctx.Velocity × ctx.Pressure) (hsol : ctx.IsSolution sol)
    (hnn : ∀ k t, 0 ≤ t → 0 ≤ ctx.v_hat k (sol t).1)
    (hsum : Summable fun k => ctx.q_int k ^ 2 * ctx.v_hat k ctx.v₀ ^ 2)
    (t : ℝ) (ht : 0 ≤ t) :
    Summable (fun k => ctx.q_int k ^ 2 * ctx.v_hat k (sol t).1 ^ 2) ∧
      qnsEnstrophy (sol t).1 ≤ qnsEnstrophy ctx.v₀ := by
  have h0 : ∀ k, 0 ≤ ctx.v_hat k ctx.v₀ := fun k => by
    simpa [ctx.initial_datum sol hsol] using hnn k 0 le_rfl
  have hpt : ∀ k, ctx.v_hat k (sol t).1 ≤ ctx.v_hat k ctx.v₀ := fun k => by
    have hd := q_ns_spectral_decay sol hsol k t ht
    have harg : -(ctx.ν_q * ctx.q_int k ^ 2) * t ≤ 0 := by
      have : 0 ≤ ctx.ν_q * ctx.q_int k ^ 2 * t :=
        mul_nonneg (mul_nonneg ctx.ν_q_pos.le (sq_nonneg _)) ht
      linarith
    have hexp : Real.exp (-(ctx.ν_q * ctx.q_int k ^ 2) * t) ≤ 1 :=
      Real.exp_le_one_iff.mpr harg
    calc ctx.v_hat k (sol t).1
        ≤ ctx.v_hat k ctx.v₀ * Real.exp (-(ctx.ν_q * ctx.q_int k ^ 2) * t) := hd
      _ ≤ ctx.v_hat k ctx.v₀ * 1 := mul_le_mul_of_nonneg_left hexp (h0 k)
      _ = ctx.v_hat k ctx.v₀ := mul_one _
  have hle : ∀ k, ctx.q_int k ^ 2 * ctx.v_hat k (sol t).1 ^ 2
      ≤ ctx.q_int k ^ 2 * ctx.v_hat k ctx.v₀ ^ 2 := fun k =>
    mul_le_mul_of_nonneg_left (pow_le_pow_left₀ (hnn k t ht) (hpt k) 2) (sq_nonneg _)
  have hs : Summable (fun k => ctx.q_int k ^ 2 * ctx.v_hat k (sol t).1 ^ 2) :=
    Summable.of_nonneg_of_le (fun k => mul_nonneg (sq_nonneg _) (sq_nonneg _)) hle hsum
  exact ⟨hs, hs.tsum_le_tsum hle hsum⟩

/-- **`Ω(q)` is attained at `t = 0`.**  The set of enstrophies along the
    solution, over `t ≥ 0`, has greatest element the initial enstrophy; so the
    supremum in the definition of `Ω(q)` is the initial enstrophy. -/
theorem q_ns_enstrophy_isGreatest [ctx : QNsWellposednessContext]
    (sol : ℝ → ctx.Velocity × ctx.Pressure) (hsol : ctx.IsSolution sol)
    (hnn : ∀ k t, 0 ≤ t → 0 ≤ ctx.v_hat k (sol t).1)
    (hsum : Summable fun k => ctx.q_int k ^ 2 * ctx.v_hat k ctx.v₀ ^ 2) :
    IsGreatest ((fun t => qnsEnstrophy (sol t).1) '' Ici 0) (qnsEnstrophy ctx.v₀) := by
  refine ⟨⟨0, left_mem_Ici, ?_⟩, ?_⟩
  · simp [ctx.initial_datum sol hsol]
  · rintro _ ⟨t, ht, rfl⟩
    exact (q_ns_enstrophy_le_initial sol hsol hnn hsum t ht).2

/-- **Part A fails in every `q`-family of corpus contexts with `q`-independent
    initial amplitudes.**  Let `C q` be a `QNsWellposednessContext` for each
    `q > 1`, whose quantum integer is the canonical `[k]_q` and whose initial
    amplitudes `|v̂_k(0)| = a_k` do not depend on `q`.  If the initial enstrophy
    is finite at one `q₀ > 1`, the order parameter (which is the initial
    enstrophy, by `q_ns_enstrophy_isGreatest`) does not tend to `+∞` as `q → 1⁺`. -/
theorem partA_fails_for_q_independent_data (C : ℝ → QNsWellposednessContext)
    (a : ℕ → ℝ)
    (hqint : ∀ q, 1 < q → (C q).q_int = fun k => qIntBal q k)
    (hdata : ∀ q, 1 < q → ∀ k, (C q).v_hat k (C q).v₀ = a k)
    {q₀ : ℝ} (hq₀ : 1 < q₀)
    (hsum : Summable fun k => qIntBal q₀ k ^ 2 * a k ^ 2) :
    ¬ Tendsto (fun q => @qnsEnstrophy (C q) (C q).v₀) (𝓝[>] 1) atTop := by
  intro h
  have heq : (fun q => @qnsEnstrophy (C q) (C q).v₀) =ᶠ[𝓝[>] (1 : ℝ)] omega a := by
    filter_upwards [self_mem_nhdsWithin] with q hq
    simp only [qnsEnstrophy, omega, hqint q hq, hdata q hq]
  exact omega_not_tendsto_atTop hq₀ hsum (h.congr' heq)

/-! ### Non-vacuity: the linear Stokes flow satisfies every field -/

/-- **The linear Stokes flow as a `QNsWellposednessContext`.**  At parameter
    `q > 1`, with any amplitudes `a`: the velocity carrier is the elapsed time,
    the unique solution is `t ↦ t`, and `|v̂_k| = a_k e^{−ν_q [k]_q² t}`.  Every
    field holds, including the modal inequality (with equality).  This both
    shows the hypotheses of `partA_fails_for_q_independent_data` are satisfiable
    with nonzero data, and shows that the context cannot tell a flow without
    nonlinear mode transfer from one with it. -/
noncomputable def stokesContext (q : ℝ) (hq : 1 < q) (a : ℕ → ℝ) :
    QNsWellposednessContext where
  q := q
  q_gt_one := hq
  ν_q := (1 - q⁻¹) / 2
  ν_q_eq := rfl
  ν_q_pos := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  Velocity := ℝ
  Pressure := Unit
  v₀ := 0
  norm_sq := fun _ => 0
  dissipation := fun _ _ => 0
  v_hat := fun k τ => a k * Real.exp (-((1 - q⁻¹) / 2 * qIntBal q k ^ 2) * τ)
  q_int := fun k => qIntBal q k
  Smooth := fun _ => True
  IsSolution := fun sol => sol = fun t => (t, ())
  energyRate := fun _ _ => 0
  dissipationRate := fun _ _ => 0
  modalRate := fun k traj t =>
    -((1 - q⁻¹) / 2 * qIntBal q k ^ 2) *
      (a k * Real.exp (-((1 - q⁻¹) / 2 * qIntBal q k ^ 2) * traj t))
  existence_uniqueness := ⟨fun t => (t, ()), rfl, fun _ h => h⟩
  smooth_of_isSolution := fun _ _ => trivial
  initial_datum := fun _ h => by subst h; rfl
  dissipation_zero := fun _ _ => rfl
  energy_continuousOn := fun _ _ _ => by simpa using continuousOn_const
  energy_hasDeriv := fun _ _ _ t _ => by
    simpa using (hasDerivWithinAt_const t (Ici t) (0 : ℝ))
  energy_balance := fun _ _ _ _ => by norm_num
  modal_continuousOn := fun sol h k T => by
    subst h
    exact (continuous_const.mul (Real.continuous_exp.comp
      (continuous_const.mul continuous_id))).continuousOn
  modal_hasDeriv := fun sol h k T t _ => by
    subst h
    set c := (1 - q⁻¹) / 2 * qIntBal q k ^ 2
    have hd : HasDerivAt (fun s : ℝ => a k * Real.exp (-c * s))
        (a k * (Real.exp (-c * t) * (-c * 1))) t :=
      (((hasDerivAt_id t).const_mul (-c)).exp).const_mul (a k)
    have : a k * (Real.exp (-c * t) * (-c * 1)) = -c * (a k * Real.exp (-c * t)) := by ring
    rw [this] at hd
    exact hd.hasDerivWithinAt
  modal_inequality := fun sol h k t _ => by
    subst h
    exact le_refl _

/-- In `stokesContext`, the initial amplitudes are the given `a`, independent of `q`. -/
theorem stokesContext_v_hat_v₀ (q : ℝ) (hq : 1 < q) (a : ℕ → ℝ) (k : ℕ) :
    (stokesContext q hq a).v_hat k (stokesContext q hq a).v₀ = a k := by
  simp [stokesContext]

/-- The family `q ↦ stokesContext q`, extended arbitrarily to `q ≤ 1`. -/
noncomputable def stokesFamily (a : ℕ → ℝ) (q : ℝ) : QNsWellposednessContext :=
  if hq : 1 < q then stokesContext q hq a else stokesContext 2 one_lt_two a

theorem stokesFamily_eq (a : ℕ → ℝ) {q : ℝ} (hq : 1 < q) :
    stokesFamily a q = stokesContext q hq a := dif_pos hq

/-- **Part A fails on the Stokes family, for every nonzero `q`-independent
    amplitude sequence with finite enstrophy at some `q₀ > 1`.**  A concrete,
    non-vacuous instance of `partA_fails_for_q_independent_data`. -/
theorem partA_fails_stokes (a : ℕ → ℝ) {q₀ : ℝ} (hq₀ : 1 < q₀)
    (hsum : Summable fun k => qIntBal q₀ k ^ 2 * a k ^ 2) :
    ¬ Tendsto (fun q => @qnsEnstrophy (stokesFamily a q) (stokesFamily a q).v₀)
      (𝓝[>] 1) atTop :=
  partA_fails_for_q_independent_data (stokesFamily a) a
    (fun q hq => by rw [stokesFamily_eq a hq]; rfl)
    (fun q hq k => by rw [stokesFamily_eq a hq]; exact stokesContext_v_hat_v₀ q hq a k)
    hq₀ hsum

/-- A concrete nonzero datum: `a = δ_{k,1}` has `Ω(q) = 1` for every `q > 1`,
    a constant, so certainly not divergent. -/
theorem omega_delta_one (q : ℝ) (hq : 1 < q) :
    omega (fun k => if k = 1 then 1 else 0) q = 1 := by
  rw [omega_single 1 q hq]; norm_num

/-! ### The physical-layer reading is a unit artifact

`def:qns-unit-layers`: enstrophies convert between the layers by `(q − 1)²`,
`Ω_sub = Ω_phys / (q − 1)²`.  If the data are held fixed in the **physical**
layer, with physical enstrophy `Ω_phys > 0`, the substrate-layer value
diverges like `(q − 1)^{−2}` by the conversion alone, whatever the dynamics.
So that reading of Part A is satisfied with `α = 2` by unit conversion and
carries no dynamical content; and the **substrate**-layer reading (data fixed
there) is the one refuted above inside `QNsWellposednessContext`. -/

/-- **Unit-artifact divergence.**  For fixed `Ω_phys > 0`,
    `Ω_phys / (q − 1)² → +∞` as `q → 1⁺`. -/
theorem physical_layer_conversion_diverges {Ωp : ℝ} (hΩ : 0 < Ωp) :
    Tendsto (fun q : ℝ => Ωp / (q - 1) ^ 2) (𝓝[>] 1) atTop := by
  have h0 : Tendsto (fun q : ℝ => (q - 1) ^ 2) (𝓝[>] 1) (𝓝[>] 0) := by
    refine tendsto_nhdsWithin_iff.mpr ⟨?_, ?_⟩
    · have : Tendsto (fun q : ℝ => (q - 1) ^ 2) (𝓝 1) (𝓝 ((1 - 1) ^ 2)) :=
        ((continuous_id.sub continuous_const).pow 2).tendsto 1
      simpa using this.mono_left nhdsWithin_le_nhds
    · filter_upwards [self_mem_nhdsWithin] with q hq
      exact pow_pos (sub_pos.mpr (show (1 : ℝ) < q from hq)) 2
  refine (h0.inv_tendsto_nhdsGT_zero.const_mul_atTop hΩ).congr (fun q => ?_)
  simp [div_eq_mul_inv]

end QOU.FluidDynamics.EnstrophyOrderParameter
