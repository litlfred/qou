/-
# The measured A=4 Brunnian level deficit is NEGATIVE (τ_L₄ > 1) — the scope-(b)
# antecedent of the Route-3 sign wall is REFUTED, not confirmed.

Companion to `QOU.MassTheory.HeliumFourBodyCluster` (#4376).  That file proved the
A=4 sign wall `mu4_ne_brunnian4Cluster` **scope-(b) CONDITIONAL on** the 4-component
Brunnian level deficit being non-negative (`τ_L₄ ≤ 1`), exactly the #4360 invariant
for the bare Borromean.  Whether that antecedent actually holds at the substrate
`q₀` for a *genuine* 4-component Brunnian link was the open companion input.

**The measurement (Task 3, `a4-h12-brunnian-deficit-measure.witness.json`).**  A
genuinely Brunnian 4-braid was constructed as the iterated left-normed commutator
of pure-braid band generators, `w₄ = [[A₀₁, A₁₂], A₂₃]`, and its Brunnian-ness was
verified EXACTLY: the strand-forgetting map `d_k` collapses the nested commutator to
the identity braid for every `k`, so all four proper sub-links are the unlink
(trace deficit machine-zero, ~1e-15).  The genuine-Brunnian joint-trace deficit at
the substrate is

    τ_L₄  = g_link / g_unlink ≈ 1.000146  >  1,
    1 − τ_L₄ ≈ −1.46·10⁻⁴  <  0     (leading Milnor order O(h⁶) = 2·(4−1), measured n≈6.06),

robust across three Brunnian representatives (left-normed, right-normed, negative-inner)
and across the `|χ|`-vs-signed perblock convention.  So the Brunnian deficit is
**NEGATIVE** — the antecedent `τ_L₄ ≤ 1` is measured **FALSE**.

**Consequence (this file, honest branch).**  Because `τ_L₄ > 1`, the deficit cluster
`c₄ = E₀·(1 − τ_L₄)` is NEGATIVE (mirror of `brunnian4Cluster_nonneg`), i.e. it has
the **SAME sign** as the derived `μ₄ = −4.591 < 0`.  The sign OBSTRUCTION the merged
wall asserted (a non-negative Brunnian deficit `≠` a negative `μ₄`) therefore does
NOT arise at the substrate: on sign grounds the genuine Brunnian cluster is
*compatible* with `μ₄`.  The A=4 recipe is REOPENED on sign; the magnitude question
(`|c₄|` vs `|μ₄| = 4.591`) becomes the live test.  This file does **not** assume the
antecedent to make the wall unconditional, and does **not** modify the merged
conditional theorem — it records the *measured* value and its arithmetic
consequences.  It also does NOT claim `μ₄` is derived: the sign obstruction being
removed is not a magnitude derivation, and no coefficient is fitted or wired.

**A=3 vs A=4 — a Milnor-parity sign flip (both measured).**  The A=3 Borromean
(length-3 Milnor) deficit is POSITIVE (`τ_Borr ≈ 0.99837 < 1`, O(h⁴)); the A=4
Brunnian (length-4 Milnor) deficit is NEGATIVE (`τ_L₄ > 1`, O(h⁶)).  The sign
alternates with Milnor length parity — a structural observation, 0-fit.

Base ring (§7c): `ℝ`, because every statement is an archimedean ordering/sign fact
(`< 1`, `1 <`, `0 <`, a numeric value `<` a numeric target).

-- Ref: [leitner2026] computations/deltalambda/a4-h12-brunnian-deficit-measure.witness.json
   (Task 3 measured input; genuine Brunnian w₄=[[A₀₁,A₁₂],A₂₃], substrate q₀).
-/
import Mathlib.Tactic

namespace QOU.MassTheory.BrunnianDeficitMeasured

/-! ### The derived A=4 residual `μ₄` is negative (mirror of #4376, forward AME−model) -/

/-- The A=4 4-body simplex residual coefficient (mirror of
`HeliumFourBodyCluster.mu4Residual`): derived, negative, the α-cluster saturation
signature.  The sign — not the digits — is load-bearing. -/
noncomputable def mu4Residual : ℝ := -4.591

theorem mu4Residual_neg : mu4Residual < 0 := by unfold mu4Residual; norm_num

/-! ### The Brunnian binding cluster, as a trace deficit against the unlink -/

/-- The 4-body Brunnian cluster realized as an energy-scaled trace deficit against
the unlink, `c₄ = E₀·(1 − τ)` (mirror of `HeliumFourBodyCluster.brunnian4Cluster`,
with the level trace `τ` supplied as a scalar rather than a function). -/
noncomputable def brunnian4Cluster (E0 τ : ℝ) : ℝ := E0 * (1 - τ)

/-! ### The MEASURED substrate values (Task 3 witness) -/

/-- Measured genuine-Brunnian level trace at the substrate `q₀`:
`τ_L₄ = g_link/g_unlink ≈ 1.000146 > 1` for `w₄ = [[A₀₁, A₁₂], A₂₃]` (base n=4,
robust to representative + convention + width-3 cabling).  This is an *empirically
measured input*, cited to the witness — not a derived closed form. -/
noncomputable def tauL4Measured : ℝ := 1.000145898

theorem tauL4Measured_gt_one : 1 < tauL4Measured := by unfold tauL4Measured; norm_num

/-- Measured A=3 Borromean level trace at the substrate: `τ_Borr ≈ 0.99837 < 1`
(the POSITIVE-deficit, O(h⁴) case that #4360 proved). -/
noncomputable def tauBorr3Measured : ℝ := 0.9983666226

theorem tauBorr3Measured_lt_one : tauBorr3Measured < 1 := by
  unfold tauBorr3Measured; norm_num

/-! ### The measured antecedent REFUTES `τ_L₄ ≤ 1` -/

/-- **The scope-(b) antecedent `τ_L₄ ≤ 1` of the merged wall is measured FALSE.** -/
theorem measured_antecedent_fails : ¬ (tauL4Measured ≤ 1) := by
  simp only [not_le]; exact tauL4Measured_gt_one

/-- **Mirror of `brunnian4Cluster_nonneg`.**  When the level trace lies *above* the
unlink (`τ > 1`, the measured case) and the energy scale is positive, the Brunnian
deficit cluster is NEGATIVE. -/
theorem brunnian4Cluster_neg_of_tau_gt_one {E0 τ : ℝ} (hE : 0 < E0) (hτ : 1 < τ) :
    brunnian4Cluster E0 τ < 0 := by
  unfold brunnian4Cluster
  exact mul_neg_of_pos_of_neg hE (by linarith)

/-- The measured genuine-Brunnian cluster is negative at the substrate. -/
theorem brunnian4Cluster_measured_neg {E0 : ℝ} (hE : 0 < E0) :
    brunnian4Cluster E0 tauL4Measured < 0 :=
  brunnian4Cluster_neg_of_tau_gt_one hE tauL4Measured_gt_one

/-! ### The sign OBSTRUCTION is removed: `μ₄` and the measured cluster share a sign -/

/-- **(CAPSTONE, sign) The measured Brunnian cluster is sign-COMPATIBLE with `μ₄`.**
Both `μ₄ = −4.591 < 0` and the measured `c₄ = E₀·(1 − τ_L₄) < 0` are negative, so the
sign-exclusion the merged conditional wall asserts under `τ ≤ 1` does NOT arise at the
substrate: on sign grounds the genuine 4-component Brunnian binding cluster *could*
match `μ₄`.  The Route-3 sign wall does **not** close unconditionally — its antecedent
is measured false — and the A=4 recipe reopens on sign.  (This is NOT a magnitude
derivation of `μ₄`; the magnitude test is separate and unfitted.) -/
theorem mu4_sign_compatible_measured_brunnian {E0 : ℝ} (hE : 0 < E0) :
    mu4Residual < 0 ∧ brunnian4Cluster E0 tauL4Measured < 0 ∧
      (0 < mu4Residual) = (0 < brunnian4Cluster E0 tauL4Measured) := by
  refine ⟨mu4Residual_neg, brunnian4Cluster_measured_neg hE, ?_⟩
  have h1 : ¬ (0 < mu4Residual) := not_lt.mpr (le_of_lt mu4Residual_neg)
  have h2 : ¬ (0 < brunnian4Cluster E0 tauL4Measured) :=
    not_lt.mpr (le_of_lt (brunnian4Cluster_measured_neg hE))
  simp [h1, h2]

/-- **(CAPSTONE) The A=3 → A=4 Milnor-parity sign FLIP (both measured).**  The A=3
Borromean deficit is positive (`τ_Borr < 1`) while the A=4 Brunnian deficit is
negative (`τ_L₄ > 1`): the level trace crosses the unlink between the length-3 and
length-4 Milnor objects.  Contrast the merged `sign_swap_a3_a4`, which is a *residual*
sign swap (`μ₃>0` vs `μ₄<0`) proved under the ASSUMED `τ ≤ 1`; here the *Brunnian
deficit itself* flips sign, measured, and that flip removes the A=4 sign wall. -/
theorem brunnian_deficit_sign_flip_a3_a4 :
    tauBorr3Measured < 1 ∧ 1 < tauL4Measured :=
  ⟨tauBorr3Measured_lt_one, tauL4Measured_gt_one⟩

end QOU.MassTheory.BrunnianDeficitMeasured
