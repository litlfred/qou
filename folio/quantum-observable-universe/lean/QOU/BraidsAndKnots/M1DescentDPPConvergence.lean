import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.Order.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.M1DescentDPPConvergence — the cited external inputs to `M₁ > 0`, as a Lean class

`M₁ = Cov_Planch(Σ_□ h, Σ_□ c²) > 0` for **all n** is the sole open input of the Δ_λ
super-exponential growth bound (bean `qou-k5r5`, epic `qou-x631`). The Cauchy–Schwarz reduction
(`YoungDiagramKernelCSMargin.lean`, PR #5896) makes it sufficient that the **(CS) margin**
`m(n) = ρ_P(n) − σ_D(n)/σ_A(n)` is positive, and the leading order is settled:

* `ρ_P(n) → ρ_P∞ = 2√6/5` (`CSMarginCorrelationConstant.csMargin_rho_eq`, sorry-free),
* `σ_D(n)/σ_A(n) → √(V_D/V_A) = 0.67961…`, `V_A = 8/(9π²)`, `V_D = 0.041597…` (audit
  `2026-08-29-covariance-kernel-M1-po72-leading-constants.md`, PR #5969),
* leading margin `m∞ = 0.300186 > 0`, and `m(n) > 0` exactly for `4 ≤ n ≤ 40`
  (`finite_n_cs_margin.py`).

What remains is an **effective finite-n statement** turning these limits into positivity for every
`n`. This file formalizes the *external analytic inputs* that supply it, as a §3b-cond **conditional
class** — content-bearing (`Filter.Tendsto` to the exact limits plus the strict leading gap), **cited,
and deliberately without an instance**: the class is the honest carrier of the open input, and the
theorems below derive the eventual (CS) margin — hence eventual `M₁ > 0` — from it by a sorry-free
`Filter.Tendsto` argument.

The cited results (see `folio/schema/references.ts`, all in `library/`):

* **[ivanov-olshanski2003]** — Kerov's CLT for the Plancherel measure: the limiting (co)variances
  are `Σ_k f̂_k ĝ_k / k`. Gives the *limits* `ρ_P∞`, `√(V_D/V_A)`.
* **[borodin-okounkov-olshanski2000]** — the descent set is a determinantal point process with the
  discrete Bessel kernel; the content statistics are its linear statistics. Bulk sine-kernel limit
  (Thm 3, rate-free); Toeplitz structure (Rem 1.6).
* **[johansson2001]** — Lemma 3.9: explicit super-exponential Bessel tail bound past the edge (the
  Olver-free *tail* half, `tail_bulk_split.py`); Lemma 3.8: de-Poissonization with explicit `C/N²`.
* **[gorbunov2024]** — Berry–Esseen *rate* for linear statistics of the Bessel-kernel DPP
  (Kac–Akhiezer + Borodin–Okounkov Toeplitz): the machinery for the *bulk* rate, i.e. what upgrades
  the qualitative `Tendsto` below to an explicit crossover `N₀`. That `N₀`, with the exact table for
  `n < N₀`, closes all-n via `YoungDiagramKernelCSMargin.m1_pos_all_of_base_and_tail`.

**This is NOT a proof of `M₁ > 0`.** Per the anti-laundering discipline, axiomatizing a cited result
as a class is *assuming* it, not proving it — the class has no instance, and the bulk-rate step
(discrete Plancherel descent variance) remains genuinely open. What is sorry-free here is the
*derivation of eventual positivity from the assumed convergence*, which is real Mathlib topology.

§7c: this is the archimedean layer (`ℝ`, `√`, ordered limits), so `ℝ` is warranted.
-/

namespace QOU.BraidsAndKnots.M1DescentDPPConvergence

open Filter Topology

/-- **Conditional class (cited external input): the descent-DPP (CS)-margin ingredients converge to
their exact leading limits, with a strictly positive leading gap.**

Parameterized by the finite-n correlation `rhoP = Corr(Σ|c|, ω₃)(n)`, the finite-n ratio
`sigRatio = σ_D(n)/σ_A(n)`, and their limits. The three fields carry genuine content:

* `rhoP_tendsto` — `ρ_P(n) → ρ_P∞`.
  Ref: [ivanov-olshanski2003] (limit) · [borodin-okounkov-olshanski2000] (descent DPP / bulk kernel).
* `sigRatio_tendsto` — `σ_D(n)/σ_A(n) → √(V_D/V_A)`.
  Ref: [johansson2001] (tail Lemma 3.9 + de-Poisson Lemma 3.8) · [gorbunov2024] (bulk rate machinery).
* `leading_margin_pos` — `√(V_D/V_A) < 2√6/5`, i.e. `m∞ > 0`
  (`CSMarginCorrelationConstant.csMargin_rho_eq`; `V_D < 64/(75π²)`).

No instance is provided: an instance would assert the open bulk-rate result. -/
class DescentDPPMarginConvergence (rhoP sigRatio : ℕ → ℝ) (rhoInf sigRatioInf : ℝ) : Prop where
  /-- `ρ_P(n) → ρ_P∞`. -- Ref: [ivanov-olshanski2003] [borodin-okounkov-olshanski2000] -/
  rhoP_tendsto : Tendsto rhoP atTop (𝓝 rhoInf)
  /-- `σ_D(n)/σ_A(n) → √(V_D/V_A)`. The bulk rate is a Toeplitz-determinant Fisher–Hartwig asymptotic
  (arc symbol ⇒ algebraic remainder), the remaining open computation.
  -- Ref: [johansson2001] [gorbunov2024] [deift-its-krasovsky2012] -/
  sigRatio_tendsto : Tendsto sigRatio atTop (𝓝 sigRatioInf)
  /-- the leading margin is strictly positive. -- Ref: [leitner2026] docs/audits/2026-08-29-covariance-kernel-M1-po72-leading-constants.md -/
  leading_margin_pos : sigRatioInf < rhoInf

/-- **The (CS) margin holds eventually (sorry-free), from the cited convergence.**

Since `σ_D/σ_A → sigRatioInf < rhoInf ← ρ_P`, eventually `σ_D(n)/σ_A(n) < ρ_P(n)`. This is the
`hCS`-input of `YoungDiagramKernelCSMargin.m1_pos_of_cs_margin` for all large `n`. -/
theorem cs_margin_eventually (rhoP sigRatio : ℕ → ℝ) (rhoInf sigRatioInf : ℝ)
    [h : DescentDPPMarginConvergence rhoP sigRatio rhoInf sigRatioInf] :
    ∀ᶠ n in atTop, sigRatio n < rhoP n :=
  h.sigRatio_tendsto.eventually_lt h.rhoP_tendsto h.leading_margin_pos

/-- **`M₁ > 0` holds eventually (sorry-free), from the cited convergence.**

Combines `cs_margin_eventually` with the Cauchy–Schwarz core: with the Fulman split
`M₁ = P − N`, `P = ρ_P σ_A σ_W`, the universal `N ≤ σ_D σ_W`, and `σ_W > 0`, the margin
`σ_D/σ_A < ρ_P` (⇔ `σ_D < ρ_P σ_A` since `σ_A > 0`) forces `M₁ = σ_W(ρ_P σ_A − σ_D) + (σ_D σ_W − N) > 0`.
(The algebra mirrors `YoungDiagramKernelCSMargin.m1_pos_of_cs_margin`; kept inline so the file stays
Mathlib-only for standalone verification.) The eventual-vs-all-`n` gap is closed by the explicit
threshold from [gorbunov2024] plus the exact table, via `…CSMargin.m1_pos_all_of_base_and_tail`. -/
theorem m1_pos_eventually
    (rhoP sigRatio sigA sigD sigW P N M1 : ℕ → ℝ) (rhoInf sigRatioInf : ℝ)
    [DescentDPPMarginConvergence rhoP sigRatio rhoInf sigRatioInf]
    (hratio : ∀ n, sigRatio n = sigD n / sigA n)
    (hsigA : ∀ n, 0 < sigA n)
    (hP : ∀ n, P n = rhoP n * sigA n * sigW n)
    (hN : ∀ n, N n ≤ sigD n * sigW n)
    (hM1 : ∀ n, M1 n = P n - N n)
    (hsigW : ∀ n, 0 < sigW n) :
    ∀ᶠ n in atTop, 0 < M1 n := by
  filter_upwards [cs_margin_eventually rhoP sigRatio rhoInf sigRatioInf] with n hmargin
  have hCS : sigD n < rhoP n * sigA n := by
    rw [hratio n] at hmargin
    exact (div_lt_iff₀ (hsigA n)).mp hmargin
  have hmarginpos : 0 < rhoP n * sigA n - sigD n := by linarith
  have hkey : 0 < sigW n * (rhoP n * sigA n - sigD n) := mul_pos (hsigW n) hmarginpos
  have hsplit : M1 n = sigW n * (rhoP n * sigA n - sigD n) + (sigD n * sigW n - N n) := by
    rw [hM1 n, hP n]; ring
  have hslack : 0 ≤ sigD n * sigW n - N n := by linarith [hN n]
  rw [hsplit]; linarith

/-- **The leading-margin field, reduced to the rigorous `V_D` ceiling (sorry-free).**

`leading_margin_pos` asks `sigRatioInf < rhoInf` with `sigRatioInf = √(V_D/V_A)`, `rhoInf = 2√6/5`.
Because `π` cancels in the square, this is exactly `V_D < 64/(75π²)` — and that bound is proved
rigorously (certified interval partial sum + explicit analytic tail majorant,
`wlambda_covariance_epic_M1_VD_ceiling_rigorous.py`: `V_D < 0.0415975 < 0.0864607`). This lemma is the
Lean reduction: given `V_A = 8/(9π²)`, `sigRatioInf² = V_D/V_A`, `rhoInf² = 24/25`
(`CSMarginCorrelationConstant.csMargin_rhoSq_eq`), `0 ≤ rhoInf`, and the ceiling `V_D < 64/(75π²)`,
the strict inequality follows by `π`-cancellation in the square. **Unlike the two `Tendsto` fields,
this one is NOT gated on the open bulk kernel rate** — it is a fact about the exact limit constants,
now discharged modulo the certified numeric ceiling.

-- Ref: [leitner2026] docs/audits/2026-08-29-covariance-kernel-M1-po72-leading-constants.md -/
theorem leading_margin_pos_of_VD_ceiling
    (VA VD sigRatioInf rhoInf p : ℝ)
    (hp : 0 < p)
    (hVA : VA = 8 / (9 * p ^ 2))
    (hceil : VD < 64 / (75 * p ^ 2))
    (hsig : sigRatioInf ^ 2 = VD / VA)
    (hrho2 : rhoInf ^ 2 = 24 / 25)
    (hrhonn : 0 ≤ rhoInf) :
    sigRatioInf < rhoInf := by
  have hsq : sigRatioInf ^ 2 < rhoInf ^ 2 := by
    rw [hsig, hrho2, hVA, div_lt_iff₀ (by positivity)]
    have h : (24 : ℝ) / 25 * (8 / (9 * p ^ 2)) = 64 / (75 * p ^ 2) := by
      field_simp; ring
    rw [h]; exact hceil
  exact lt_of_pow_lt_pow_left₀ 2 hrhonn hsq

end QOU.BraidsAndKnots.M1DescentDPPConvergence
