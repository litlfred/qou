/-
# Convention D weighs the two eigenlines `[3]_q : 1`, at every tower level

Bean `qou-wkcd` (epic `qou-qs0e`). Owner decision (a), 2026-11-15: does the one-sidedness
of the corner `sl₂` (exclusive at `n = 4`, lost at `n = 5`) persist in a weighted form?

A Markov trace `τ` sees an eigenline only through `τ(P₊)` and `τ(P₋)`, and those are fixed
by `τ(1) = 1` and `τ(σ) = z` alone. They do not depend on the tower level `n`.

## Proved here (generic `[Field K] [Ring A] [Algebra K A]`)

* `trace_Pp`, `trace_Pm`: for any `K`-linear `τ` with `τ 1 = 1`, `τ σ = z`,
  `τ(P₊) = (z + q⁻¹)/[2]` and `τ(P₋) = (q − z)/[2]`.
* `zD_line_ratio`: at `z = z_D = q³/(q²+1)` (convention D),
  `τ(P₊) = [3]_q · τ(P₋)` with `[3]_q = q² + 1 + q⁻²`.
* `zD_trace_Pm`: `τ(P₋) = q / ((q²+1)(q+q⁻¹))`, nonzero. So the `(−q⁻¹)`-line is
  weighted, not killed. The bias is `[3]_q : 1`, not `1 : 0`.
* `three_bar_invariant`: `[3]_q` is unchanged by `q ↦ q⁻¹`, and by `q ↦ −q⁻¹`.
* `zD_ratio_at_one`: at `q = 1`, `z_D = 1/2` and the ratio is `3 : 1`.

## Reading (observation, scope (a))

`[3]_q : 1` is the quantum-dimension ratio of `Sym²V : Λ²V` for the `SU_q(2)`
fundamental `V`. Convention D is the trace of that fibre (`prop:markov-trace-frobenius-
selection`). The bias is present at `q = 1` and is bar-invariant in size. So it is a
property of convention D, not of `|q| > 1`. Which line receives the `[3]_q` is the line
that D's root label calls `q`. That is `leftLine` when `q > 1` (`LeftLineDefinition`).
Nothing here identifies either line with a physical chirality.

No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.OneSidedWeakVertex

namespace QOU.QuarkState.ConventionDLines

open QOU.QuarkState.Helicity

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
variable {q z : K} {s : A}

/-- Trace of the `q`-line projector. -/
theorem trace_Pp (τ : A →ₗ[K] K) (h1 : τ 1 = 1) (hz : τ s = z) :
    τ (Pp q s) = (q + q⁻¹)⁻¹ * (z + q⁻¹) := by
  unfold Pp
  rw [map_smul, map_add, map_smul, hz, h1, smul_eq_mul, smul_eq_mul, mul_one]

/-- Trace of the `(−q⁻¹)`-line projector. -/
theorem trace_Pm (τ : A →ₗ[K] K) (h1 : τ 1 = 1) (hz : τ s = z) :
    τ (Pm q s) = (q + q⁻¹)⁻¹ * (q - z) := by
  unfold Pm
  rw [map_smul, map_sub, map_smul, hz, h1, smul_eq_mul, smul_eq_mul, mul_one]

/-- **Convention D weighs the lines `[3]_q : 1`.** -/
theorem zD_line_ratio (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (τ : A →ₗ[K] K) (h1 : τ 1 = 1)
    (hz : τ s = q ^ 3 / (q ^ 2 + 1)) :
    τ (Pp q s) = (q ^ 2 + 1 + q⁻¹ ^ 2) * τ (Pm q s) := by
  rw [trace_Pp τ h1 hz, trace_Pm τ h1 hz]
  field_simp
  ring

/-- The `(−q⁻¹)`-line keeps a nonzero weight under convention D. -/
theorem zD_trace_Pm (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0) (τ : A →ₗ[K] K) (h1 : τ 1 = 1)
    (hz : τ s = q ^ 3 / (q ^ 2 + 1)) :
    τ (Pm q s) = q / ((q ^ 2 + 1) * (q + q⁻¹)) := by
  rw [trace_Pm τ h1 hz]
  have h2 : q + q⁻¹ ≠ 0 := by
    intro h
    apply hq1
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  field_simp
  ring

/-- `[3]_q = q² + 1 + q⁻²` is invariant under `q ↦ q⁻¹`. -/
theorem three_bar_invariant (q : K) :
    q⁻¹ ^ 2 + 1 + q⁻¹⁻¹ ^ 2 = q ^ 2 + 1 + q⁻¹ ^ 2 := by
  rw [inv_inv]; ring

/-- … and under the root relabel `q ↦ −q⁻¹`. -/
theorem three_relabel_invariant (q : K) :
    (-q⁻¹) ^ 2 + 1 + (-q⁻¹)⁻¹ ^ 2 = q ^ 2 + 1 + q⁻¹ ^ 2 := by
  rw [inv_neg, inv_inv]; ring

/-- At `q = 1`: `z_D = 1/2`, and the ratio is `3 : 1`. -/
theorem zD_ratio_at_one (h2 : (2 : K) ≠ 0) (τ : A →ₗ[K] K) (h1 : τ 1 = 1)
    (hz : τ s = (1 : K) ^ 3 / ((1 : K) ^ 2 + 1)) :
    τ (Pp (1 : K) s) = 3 * τ (Pm (1 : K) s) := by
  have := zD_line_ratio (q := (1 : K)) one_ne_zero (by norm_num; exact h2) τ h1 hz
  rw [this]; norm_num

end QOU.QuarkState.ConventionDLines
