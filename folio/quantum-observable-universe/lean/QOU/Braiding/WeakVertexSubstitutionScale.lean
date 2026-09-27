import QOU.Braiding.WeakVertexT35TraceClosedForm

/-!
# The `s² → |W|²` substitution is not a small correction

`prf:hadron-half-life` (item 1) and `rem:hadron-half-life-fermi` (open
computation 2) prescribe replacing the single-crossing coupling
`s² = (q^{1/2} − q^{-1/2})² = (q − 1)²/q` in the decay rate by the full
weak-vertex form factor `|W(q)|²`, with
`W(q) = tr_M((σ₀σ₁)⁵) = q²(q¹² + q⁸ − 1)/(q² + 1)²`
(`WeakVertexT35TraceClosedForm`). The rate scales by `|W|²/s²` under that
substitution, so the half-lives scale by `s²/|W|²`.

This file records, as a checked inequality at the proton pin
`q₀ ≈ 1.1099785`, that the factor lies between `129` and `130` — the
substitution shortens every predicted half-life by two orders of magnitude.
It therefore cannot be the `10–17 %` correction the corpus attributed to it.
This is a scope-(a) negative about the *prescribed substitution*, not about
`W`: the closed form is correct, the coupling it was to replace is a
different normalisation. Bean `qou-ix74`.

> **🛑 THE POWER WAS WRONG UNTIL 2026-09-05 — this file said `s⁴` and `10⁴`
> (bean `qou-xql6`).** `substitutionRateFactor` was defined as
> `(weakVertexTrace q)^2 / (sSq q)^2`, and **`sSq` is already `s²`**
> (`sSq q = (√q − 1/√q)²`, and `sSq_eq` says `q + q⁻¹ − 2`), so squaring it
> gave `s⁴`. A name reading *"s, squared"* was consumed as *"s"*.
>
> The rate carries `s²` exactly once. `prf:trace-ratio-observable` states it:
> `|ℳ_q|² = |skein_amp|²·|tr(par)/tr(dau)|²` with
> `skein_amp = q^{1/2} − q^{−1/2}`, *"the Skein amplitude at the beta-decay
> vertex"*. Nothing else in the rate carries an `s` — `[2]_q` is full-scale,
> the pair-Skein denominator is the half-scale **sum** `q^{1/2} + q^{−1/2}`,
> and `Q ∝ q − q⁻¹` is full-scale.
>
> So `11875.4418937` becomes **`129.405107404`**, high by `1/s² = 91.77×`.
> **The scope-(a) negative SURVIVES** — 129× still cannot be a 10–17 %
> correction — but "four orders of magnitude" is withdrawn in favour of two.
> Producer `beta_rate_skein_power_audit.py` (9/9); witness
> `beta-rate-skein-power-audit.witness.json`.

Ground ring `ℝ` (archimedean evaluation at `q₀`); the identities are stated
over a field. Verified `lean`-direct.
-/

namespace QOU.Braiding.WeakVertexT35

variable {K : Type*} [Field K]

/-- The single-crossing coupling `s² = (q^{1/2} − q^{-1/2})² = q + q⁻¹ − 2 = (q − 1)²/q`,
written without the square root. -/
noncomputable def sSq (q : K) : K := (q - 1) ^ 2 / q

/-- `s² = q + q⁻¹ − 2`: the square-root form and the rational form agree. -/
theorem sSq_eq (q : K) (hq : q ≠ 0) : sSq q = q + q⁻¹ - 2 := by
  unfold sSq
  field_simp
  ring

/-- The rate-scaling factor of the prescribed substitution, `|W|²/s²`, as a rational
function of `q`. **One** power of `sSq`: the rate carries the single-crossing amplitude
squared exactly once, and `sSq` *is* that square (see the corrected note above). -/
noncomputable def substitutionRateFactor (q : K) : K :=
  (weakVertexTrace q) ^ 2 / sSq q

/-- Closed form of the factor: `q⁵ (q¹² + q⁸ − 1)² / ((q² + 1)⁴ (q − 1)²)`. -/
theorem substitutionRateFactor_eq (q : K) (hq0 : q ≠ 0) (hq1 : q ≠ 1) (h2 : q ^ 2 + 1 ≠ 0) :
    substitutionRateFactor q =
      q ^ 5 * (q ^ 12 + q ^ 8 - 1) ^ 2 / ((q ^ 2 + 1) ^ 4 * (q - 1) ^ 2) := by
  unfold substitutionRateFactor weakVertexTrace sSq
  have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  field_simp

/-- **The negative, checked at the proton pin, at the corrected power.** At
`q₀ = 1.1099785` the factor lies in `(129, 130)`: the substitution multiplies every decay
rate by about `129`, shortening every predicted half-life by two orders of magnitude. Far
too large to be the `10–17 %` correction the corpus attributed to it, so the scope-(a)
negative stands — at `129×`, not the `1.19·10⁴` this file claimed until 2026-09-05
(bean `qou-xql6`). Stated as a two-sided band on the measured value, not a round window. -/
theorem substitutionRateFactor_near_one_hundred_thirty :
    (129 : ℝ) < substitutionRateFactor (1.1099785 : ℝ) ∧
      substitutionRateFactor (1.1099785 : ℝ) < 130 := by
  rw [substitutionRateFactor_eq _ (by norm_num) (by norm_num) (by positivity)]
  constructor <;> norm_num

/-- **Why the factor has no classical limit** — the fact that retired the "order derived"
bridge of bean `qou-q2l7`. At `q = 1` the denominator vanishes while the numerator does
not: `s²(1) = 0` but `W(1)² = 1/16`. So `|W|²/s^k` diverges as `q → 1` for every `k ≥ 1`,
and no finite constant is its leading value — in particular the `−96` of
`couplingRatio_one` is the leading value of `(J − 1)/s²`, a *different* ratio, whose
numerator vanishes because `V_K(1) = 1` for every knot. -/
theorem substitutionRateFactor_denominator_vanishes_numerator_does_not :
    sSq (1 : ℝ) = 0 ∧ weakVertexTrace (1 : ℝ) ^ 2 = 1 / 16 := by
  refine ⟨by simp [sSq], ?_⟩
  rw [weakVertexTrace_one]
  norm_num

end QOU.Braiding.WeakVertexT35
