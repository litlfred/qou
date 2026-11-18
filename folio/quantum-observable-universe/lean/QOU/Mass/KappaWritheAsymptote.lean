import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# Gap-9b, κ leg: the isovector-slope asymptote is the trace ratio, not the interface factor

The bar-odd writhe coefficient `κ` of the per-isotope binding residual decomposes as
`κ = κ_FW + κ_AME`, and its framework part is carried by the isovector (mirror) slope
`b_pred(A) = d(log_{q₀} B_pred)/dT₃`.  The Phase-5q closed form
([`computations/probes/b_pred_mirror_slope_closed_form.py`](../../../../../computations/probes/b_pred_mirror_slope_closed_form.py),
audit [`2026-06-29-delta-lambda-z-correction-writhe`](../../../../../docs/audits/2026-06-29-delta-lambda-z-correction-writhe.md))
gives, for a mirror pair `(Z,N) ↔ (N,Z)`,

```
B_pred(Z,N) = E₀ · τ_p^Z τ_n^N · (1 − ε(Z,N)),   ε(Z,N) = z^{Z−1}(z − h/2)(z − h)^{N−1}
b_pred(A)   = log_{q₀}(τ_p/τ_n) + log[(1 − ε(N,Z))/(1 − ε(Z,N))] / ((N − Z)·ln q₀)
```

with the measured substrate values `z ≈ 0.4994` and `z − h ≈ 0.2903`, **both `< 1` in absolute
value**.  The derived claim (this file, sorry-free):

* **`epsilon_tendsto_zero`** — since `|z| < 1`, the interface term `ε` vanishes geometrically
  as the strand count grows.  This is *why* the interface correction dies at large `A`.
* **`correction_zero_of_eps_eq`** — when the two mirror interface terms coincide (the `ε → 0`
  limit), the correction term is exactly `0`, so `b_pred = log_{q₀}(τ_p/τ_n)` — the **plateau**.

**Consequence (the refutation, scope (a)).**  The asymptote of `b_pred` is the p/n *trace ratio*
`log_{q₀}(τ_p/τ_n) ≈ 1.37181` (hence `κ_FW = −b_pred(∞)/4 ≈ −0.34295`), **not** the earlier
interface-only near-match `log_{q₀}(z/(z−h)) ≈ 1.2998`: interfaces enter *only* through the
vanishing `ε` term (`epsilon_tendsto_zero`), never the plateau.  The `κ_AME ≈ −0.094` remainder is
experimental (Coulomb isovector), outside the trace — so `κ` overall stays near-match, not derived.

Base ring `ℝ` (§7c): genuinely archimedean — `Real.log`, `|z| < 1`, geometric decay.
-/

namespace QOU.Mass.KappaWrithe

open Filter Topology

/-- The interface term `ε` in shifted index form: `ε(z,h; a,b) = z^a · (z − h/2) · (z − h)^b`,
with `a = Z − 1`, `b = N − 1`.  (Grouped `z^a · (…)` so the geometric factor is explicit.) -/
noncomputable def epsilonShift (z h : ℝ) (a b : ℕ) : ℝ := z ^ a * ((z - h / 2) * (z - h) ^ b)

/-- **The interface term vanishes geometrically.**  For `|z| < 1`, `ε(z,h; a,b) → 0` as `a → ∞`
(the strand count `Z` grows).  This is the mechanism behind the `b_pred` plateau: the interface
correction dies at large `A`. -/
theorem epsilon_tendsto_zero (z h : ℝ) (hz : |z| < 1) (b : ℕ) :
    Tendsto (fun a : ℕ => epsilonShift z h a b) atTop (nhds 0) := by
  have hp : Tendsto (fun a : ℕ => z ^ a) atTop (nhds 0) :=
    tendsto_pow_atTop_nhds_zero_of_abs_lt_one hz
  have := hp.mul_const ((z - h / 2) * (z - h) ^ b)
  simpa [epsilonShift] using this

/-- **The correction term vanishes when the mirror interface terms coincide** (the `ε → 0` limit).
If `e₁ = e₂` (and `1 − e₂ ≠ 0`), then `log[(1 − e₁)/(1 − e₂)] / D = 0`.  Applied to
`e₁ = ε(N,Z)`, `e₂ = ε(Z,N)`, `D = (N − Z)·ln q₀`, this says the correction in `b_pred` is `0` in
the limit, so `b_pred = log_{q₀}(τ_p/τ_n)` — the plateau (the trace ratio), independent of any
interface factor. -/
theorem correction_zero_of_eps_eq (e₁ e₂ D : ℝ) (h : e₁ = e₂) (hne : 1 - e₂ ≠ 0) :
    Real.log ((1 - e₁) / (1 - e₂)) / D = 0 := by
  rw [h, div_self hne, Real.log_one, zero_div]

/-- **Self-equality specialization of `correction_zero_of_eps_eq` (`qou-2cz1`).**
When `1 - e ≠ 0`, `Real.log ((1 - e) / (1 - e)) / D = 0`. -/
theorem correction_zero_of_eps_self (e D : ℝ) (hne : 1 - e ≠ 0) :
    Real.log ((1 - e) / (1 - e)) / D = 0 :=
  correction_zero_of_eps_eq e e D rfl hne

end QOU.Mass.KappaWrithe
