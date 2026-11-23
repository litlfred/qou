import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Order.Filter.AtTopBot.Basic

/-!
# QOU.FluidDynamics.DSSObstructions — five structural facts about the
# discretely self-similar (DSS) blow-up scenario

Backing for the 2026-11-21 restatement of `conj:regularity-breakdown` and of the
Leray profile block (issue #8864). Each lemma isolates one step that the earlier
wording of those blocks got wrong or left implicit. None of them uses an
empirical value. The analytic theorems they are combined with (Nečas–Růžička–
Šverák, Tsai, Seregin, Chae, Chae–Wolf) are **cited in the prose, not assumed in
Lean**: no lemma here takes a literature theorem as a hypothesis class.

## The five lemmas

* **L1 `IntegerSpin.even_of_neg_one_pow_eq_one`** (in `QOU/FluidDynamics/IntegerSpin.lean`, split out per §7c because it is generic) — integer spin only. On the spin-`j`
  summand of an `SU(2)`-representation the central element `-1` acts by
  `(-1)^{2j}`. On velocity fields on `ℝ³` the `SU(2)` action factors through
  `SO(3)`, so `-1` acts as the identity. Hence `(-1)^{2j} = 1`, and over any
  commutative ring with `2 ≠ 0` this forces `2j` even: no half-integer spins.
  (The two representation-theoretic facts are standard and are the hypotheses
  of the lemma, not re-proved here.)
* **L2 `qKappa_pow_two_kappa`, `qKappa_is_root_of_unity`** — the parameter
  `q_κ = exp(iπ/κ)` is a `2κ`-th root of unity. A scaling factor `λ_κ` built
  from it therefore conflicts with the standing QOU requirement that `q` is not a
  root of unity (`def:substrate-parameter`).
* **L3 `lerayEnstrophy_blowup`** — in Leray variables
  `y = (x - x₀)/√(T - t)`, `s = -log(T - t)`, the enstrophy of a backward
  self-similar field is `(T - t)^{-1/2} E(s)` with `E(s) = ‖∇_y V(·, s)‖²`.
  If `E` is periodic and positive somewhere, the enstrophy is unbounded as
  `t → T⁻`. So enstrophy blow-up is a *consequence* of a nonzero DSS profile,
  not an independent conjecture.
* **L4 `dss_L3_norm_not_tendsto_atTop`** — the `L³` norm is invariant under the
  Leray rescaling, so along a DSS solution it equals `N(s(t))` with `N`
  periodic. If `N` is continuous it is bounded, so it does not tend to `+∞` as
  `t → T⁻`. Combined with Seregin's theorem (CMP 2012: `‖v(t)‖_{L³} → ∞` at any
  blow-up time), which is cited and not formalised, this excludes every DSS
  blow-up whose profile is continuous in `s` with values in `L³` (Chae,
  arXiv:1306.0305, Thm 1.1 proves this directly).
* **L5 `sup_unbounded_without_finite_time_blowup`** — a quantity can be
  unbounded on `[0, ∞)` while bounded on every `[0, T]`. So
  `Ω(1) := sup_{t ≥ 0} (enstrophy) = +∞` does not by itself say that anything
  blows up in finite time.

## Base ring (§7c)
L1 is generic and lives in `IntegerSpin.lean`. L2 needs `ℂ` (`Complex.exp`). L3–L5 are
statements about real-valued functions of time; `ℝ` is required (logarithm,
square root, order, topology).

## References
- [leitner2026] fluid-dynamics/regularity-breakdown, leray-profile,
  leray-profile-construction
- Nečas–Růžička–Šverák, Acta Math. 176 (1996) (`necas-ruzicka-sverak1996`)
- Tsai, Arch. Ration. Mech. Anal. 143 (1998) (`tsai1998`)
- Seregin, Comm. Math. Phys. (2012), `L³` norm blow-up
- Chae, arXiv:1306.0305; Chae–Wolf, arXiv:1610.09464
-/

namespace QOU.FluidDynamics.DSSObstructions

/-! ### L2 — `q_κ = exp(iπ/κ)` is a root of unity -/

/-- **L2.** `q_κ = exp(iπ/κ)` satisfies `q_κ^{2κ} = 1`. -/
theorem qKappa_pow_two_kappa (κ : ℕ) (hκ : κ ≠ 0) :
    Complex.exp (Real.pi * Complex.I / κ) ^ (2 * κ) = 1 := by
  rw [← Complex.exp_nat_mul]
  have hκC : (κ : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hκ
  have : ((2 * κ : ℕ) : ℂ) * (Real.pi * Complex.I / κ) = 2 * Real.pi * Complex.I := by
    push_cast
    field_simp
  rw [this, Complex.exp_two_pi_mul_I]

/-- **L2, as a conflict.** `q_κ` fails the QOU requirement "`q^n ≠ 1` for every
    `n ≥ 1`": the exponent `n = 2κ` is a witness. -/
theorem qKappa_is_root_of_unity (κ : ℕ) (hκ : κ ≠ 0) :
    ¬ ∀ n : ℕ, 0 < n → Complex.exp (Real.pi * Complex.I / κ) ^ n ≠ 1 :=
  fun h => h (2 * κ) (by omega) (qKappa_pow_two_kappa κ hκ)

/-! ### L3 — enstrophy blow-up is forced by a nonzero periodic profile -/

/-- Enstrophy of a backward self-similar field in Leray variables:
    `(T - t)^{-1/2} · E(-log(T - t))`, where `E(s) = ‖∇_y V(·, s)‖²` is the
    enstrophy of the rescaled profile at similarity time `s`. -/
noncomputable def lerayEnstrophy (E : ℝ → ℝ) (T t : ℝ) : ℝ :=
  E (-Real.log (T - t)) / Real.sqrt (T - t)

/-- **L3.** If the rescaled profile enstrophy `E` is periodic in `s` with period
    `P > 0` and positive at some `s₀`, the physical enstrophy is unbounded as
    `t → T⁻`: for every `M` and every `ε > 0` there is `t ∈ (T - ε, T)` with
    enstrophy `> M`. -/
theorem lerayEnstrophy_blowup {E : ℝ → ℝ} {P : ℝ} (hP : 0 < P)
    (hper : Function.Periodic E P) {s₀ : ℝ} (hs₀ : 0 < E s₀) (T : ℝ) :
    ∀ M ε : ℝ, 0 < ε → ∃ t, T - ε < t ∧ t < T ∧ M < lerayEnstrophy E T t := by
  intro M ε hε
  set S : ℝ := max (-Real.log ε) (2 * M / E s₀) with hSdef
  obtain ⟨n, hn⟩ := exists_nat_gt ((S - s₀) / P)
  set s : ℝ := s₀ + n * P with hs
  have hsS : S < s := by
    have := (div_lt_iff₀ hP).mp hn
    linarith
  refine ⟨T - Real.exp (-s), ?_, ?_, ?_⟩
  · have h1 : -Real.log ε < s := lt_of_le_of_lt (le_max_left _ _) hsS
    have : Real.exp (-s) < ε := by
      calc Real.exp (-s) < Real.exp (Real.log ε) := Real.exp_lt_exp.mpr (by linarith)
        _ = ε := Real.exp_log hε
    linarith
  · have := Real.exp_pos (-s)
    linarith
  · unfold lerayEnstrophy
    have hTt : T - (T - Real.exp (-s)) = Real.exp (-s) := by ring
    rw [hTt, Real.log_exp, neg_neg]
    have hEs : E s = E s₀ := by rw [hs]; exact (hper.nat_mul n) s₀
    rw [hEs]
    have hsqrt : Real.sqrt (Real.exp (-s)) = Real.exp (-s / 2) := by
      rw [show -s = (-s / 2) + (-s / 2) by ring, Real.exp_add,
        Real.sqrt_mul_self (Real.exp_pos _).le]
      ring_nf
    rw [hsqrt, div_eq_mul_inv, ← Real.exp_neg, show -(-s / 2) = s / 2 by ring]
    have h2 : 2 * M / E s₀ < s := lt_of_le_of_lt (le_max_right _ _) hsS
    have h3 : 2 * M < s * E s₀ := (div_lt_iff₀ hs₀).mp h2
    have h4 : s / 2 + 1 ≤ Real.exp (s / 2) := by
      have := Real.add_one_le_exp (s / 2); linarith
    have h5 : E s₀ * (s / 2 + 1) ≤ E s₀ * Real.exp (s / 2) :=
      mul_le_mul_of_nonneg_left h4 hs₀.le
    nlinarith

/-! ### L4 — the `L³` norm of a continuous DSS profile stays bounded -/

/-- **L4.** Let `N(s) = ‖V(·, s)‖_{L³}` be the `L³` norm of the rescaled
    profile; by scale invariance it equals `‖v(t)‖_{L³}` at `s = -log(T - t)`.
    If `N` is continuous and periodic with period `P ≠ 0`, then `‖v(t)‖_{L³}`
    does **not** tend to `+∞` as `t → T⁻`. Read with Seregin's `L³` blow-up
    theorem (cited, not formalised), no such DSS solution blows up at `T`. -/
theorem dss_L3_norm_not_tendsto_atTop {N : ℝ → ℝ} {P : ℝ} (hP : P ≠ 0)
    (hper : Function.Periodic N P) (hcont : Continuous N) (T : ℝ) :
    ¬ Filter.Tendsto (fun t => N (-Real.log (T - t)))
        (nhdsWithin T (Set.Iio T)) Filter.atTop := by
  intro htend
  obtain ⟨B, hB⟩ := (hper.compact_of_continuous hP hcont).bddAbove
  have hev := (Filter.tendsto_atTop.mp htend) (B + 1)
  obtain ⟨t, ht⟩ := hev.exists
  have : N (-Real.log (T - t)) ≤ B := hB ⟨_, rfl⟩
  linarith

/-! ### L5 — `sup_{t ≥ 0}` unbounded is not finite-time blow-up -/

/-- **L5.** There is a continuous `Ω : ℝ → ℝ` that is unbounded on `[0, ∞)` yet
    bounded on every `[0, T]` (namely `Ω t = t`). So `sup_{t ≥ 0} Ω = +∞` does
    not imply blow-up at any finite time. -/
theorem sup_unbounded_without_finite_time_blowup :
    ∃ Ω : ℝ → ℝ, Continuous Ω ∧ ¬ BddAbove (Ω '' Set.Ici 0) ∧
      ∀ T : ℝ, BddAbove (Ω '' Set.Icc 0 T) := by
  refine ⟨id, continuous_id, ?_, fun T => ?_⟩
  · rw [Set.image_id]
    exact not_bddAbove_Ici 0
  · rw [Set.image_id]
    exact bddAbove_Icc

end QOU.FluidDynamics.DSSObstructions
