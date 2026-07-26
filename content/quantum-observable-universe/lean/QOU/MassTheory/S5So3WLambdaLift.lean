/-
# The s5-so3 keystone `W_λ` re-weighting of the A=3 Borromean cluster is a
# coefficient rescale of the production `y_λ` trace — closure is a coefficient
# identity, not an order change.

Route-1 attack on the residual `1.6×` gap left by
`QOU.MassTheory.BorromeanMagnitudeLift` (#4364):

* #4360 derived the A=3 3-body cluster **sign** `c₃ = E₀·(1 − τ_Borr) > 0`.
* #4364 lifted the **magnitude** to the `H₉` joint-trace level via faithful
  width-3 cabling, reaching `v_{y} = 0.297 MeV = 0.63× μ₃` (`μ₃ = 0.4708`),
  measured `O(h⁴)`, `0` fit — a `~1.6×` NEAR-MISS.  Its key theorem
  `lift_is_coefficient_ratio` proves a **level lift is a pure coefficient
  rescale** `κ₁/κ₂` (the shared `h⁴` cancels), so the residual `1.6×` is a
  **coefficient** question, never an order one.

This file formalizes **Route 1**: the H₉ joint trace `ρ_F` normalizes the
Wedderburn blocks `λ ⊢ 9` with the **production** weight `y_λ` (Wenzl principal
specialization `s_λ(1,q,q²,…)`).  The s5-so3 keystone posits a **different,
geometrically-derived** block weight — the Ocneanu / q-Plancherel measure

    W_λ = d_q(λ)² / [n]_q!          (balanced q-integers, Σ_{λ⊢n} W_λ = 1),

the object of `docs/coordination/s5-so3-keystone.md`.  Re-weighting the cluster
trace `y_λ → W_λ` is, by the same argument as `lift_is_coefficient_ratio`, a
**coefficient rescale** `r = κ_W / κ_y` of the `O(h⁴)` cluster — it can supply a
coefficient enhancement but **cannot change the leading `h`-order**.  So the
Route-1 question is exactly: *does the derived `W_λ` re-weight ratio `r` equal
the `μ₃/v_y ≈ 1.585×` needed to close?*

**Anti-fit discipline (STRICT).**  `W_λ` is fixed by `q₀` + the partition
hook-lengths — 0 free parameters, never inverted from `μ₃`.  The companion probe
`computations/deltalambda/s5so3_wlambda_borromean_lift_probe.py` forward-evaluates
the `W_λ`-weighted `H₉` cabled-Borromean cluster.  This file carries (1) the
order-invariance of the re-weight (proved unconditionally) and (2) the closure
predicate as a *conditional coefficient identity* on the derived value.  A `W_λ`
that closes is a DERIVATION; a `W_λ` that misses is an honest WALL — the residual
stays a coefficient question and must **not** be tuned to `μ₃`.

Base ring (§7c): `ℝ` — archimedean magnitude / ordering facts.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-! ### The `H₉` cluster deficit at a block weight is `D(h) = h⁴ · κ h` -/

/-- A Brunnian-order-suppressed `H₉` cluster deficit at a *given block weight*
(`y_λ` or `W_λ`) has the shape `D(h) = h⁴ · κ h`, with the weight's `h⁴`-coefficient
`κ`.  (Cabling preserves the Brunnian order-suppression — probe-measured exponent
`4.098` — so both weights give an `O(h⁴)` deficit; only `κ` differs.) -/
noncomputable def weightedDeficit (κ : ℝ → ℝ) (h : ℝ) : ℝ := h ^ 4 * κ h

/-- **The `y_λ → W_λ` re-weight is a coefficient ratio, never an order change.**
Two block weights give deficits `h⁴·κ_y h` and `h⁴·κ_W h`; their ratio is
`κ_W h / κ_y h` — the shared `h⁴` cancels.  Re-weighting the trace therefore
rescales the *coefficient* and **cannot** move the leading `h`-order.  (Same
structural fact as `BorromeanMagnitudeLift.lift_is_coefficient_ratio`, applied to
the block-weight axis rather than the level axis.) -/
theorem reweight_is_coefficient_ratio {κ_y κ_W : ℝ → ℝ} {h : ℝ}
    (hh : h ≠ 0) (hκy : κ_y h ≠ 0) :
    weightedDeficit κ_W h / weightedDeficit κ_y h = κ_W h / κ_y h := by
  unfold weightedDeficit
  have h4 : h ^ 4 ≠ 0 := pow_ne_zero 4 hh
  field_simp

/-- The physical A=3 cluster magnitude at a block weight is
`c₃ = E₀ · h⁴ · κ` (the weight's `h⁴`-coefficient at the physical `h`). -/
noncomputable def clusterMagnitude (E0 h κ : ℝ) : ℝ := E0 * (h ^ 4 * κ)

/-- **The re-weight ratio scales the magnitude linearly.**  `c₃(W_λ) =
r · c₃(y_λ)` with `r = κ_W / κ_y`.  So the derived `W_λ` cluster is the
`y_λ` cluster (`0.297`) times the derived ratio `r` — a forward, 0-fit number. -/
theorem clusterMagnitude_reweight (E0 h κ_y r : ℝ) :
    clusterMagnitude E0 h (r * κ_y) = r * clusterMagnitude E0 h κ_y := by
  unfold clusterMagnitude; ring

/-! ### Closure is a conditional coefficient identity on the derived `W_λ` ratio -/

/-- **Route-1 closure predicate.**  The A=3 magnitude closes under the keystone
`W_λ` re-weight iff the `W_λ`-weighted cluster equals `μ₃`:
`E₀ · h⁴ · (r · κ_y) = μ₃`, equivalently `r · v_y = μ₃` where `v_y = 0.297`.
`r` is FIXED by `q₀` + hook-lengths (0 fit); a `r` chosen to satisfy this would be
a FIT and is declined. -/
def Route1Closes (v_y r μ₃ : ℝ) : Prop := r * v_y = μ₃

theorem route1_closes_iff {v_y r μ₃ : ℝ} :
    Route1Closes v_y r μ₃ ↔ r * v_y = μ₃ := Iff.rfl

/-- The exact ratio the near-miss needs: `r* = μ₃ / v_y = 0.4708 / 0.297 ≈ 1.585`.
Route 1 closes **iff** the *derived* keystone ratio `r` equals this `r*` — the
sole empirical question, evaluated forward by the probe (never inverted). -/
noncomputable def requiredRatio (v_y μ₃ : ℝ) : ℝ := μ₃ / v_y

theorem route1_closes_iff_ratio_eq {v_y r μ₃ : ℝ} (hv : v_y ≠ 0) :
    Route1Closes v_y r μ₃ ↔ r = requiredRatio v_y μ₃ := by
  unfold Route1Closes requiredRatio
  rw [eq_div_iff hv]

/-! ### RESULT — filled from the forward, 0-fit probe (see final commit). -/

end QOU.MassTheory
