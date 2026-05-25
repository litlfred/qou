import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# Bring color-tube + Faddeev h⁴ — provable algebraic identities

Formalises the algebraic content of the Bring + Faddeev h⁴ candidate
for `linking_weight(q)` proposed in
[`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md).

The candidate, per the canonical-derivation cheat-sheet §5 + the audit
§4a, is

  linking_weight(q) = 1/(1 − h_q · q^{10}) + 1/(1 − h_q⁴) − 1
                    = Bring color-tube + Faddeev recursion at h⁴

with `h_q = q − q⁻¹`. Both factors are Φ_q functional-equation ratios
at substrate-natural z values, so the form is RULE 14 compliant (both
in the 13-driver menu of
`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`).

This file proves all the algebraic identities that don't require power
series infrastructure or specific numerical bounds:

| theorem | content | tactic |
|---|---|---|
| `bringColorTube_def` | definitional unfolding | `rfl` |
| `faddeevH4_def` | definitional unfolding | `rfl` |
| `linkingWeightBringFaddeevH4_eq_sum_minus_one` | identity | `rfl` |
| `bringColorTube_at_h_zero` | = 1 at h = 0 | `field_simp` |
| `faddeevH4_at_h_zero` | = 1 at h = 0 | `field_simp` |
| `linkingWeightBringFaddeevH4_at_h_zero` | = 1 at h = 0 | `linarith` |
| `bringColorTube_at_q_one` | = 1 at q = 1 (since h = 0) | combo |
| `categorically_distinct_from_familyA_at_q_one` | ≠ 5/2 (Family A baseline) | `norm_num` |

What this file does NOT prove:
- The h² / h⁴ / higher h^k coefficients (require power series machinery)
- The numerical value at q₀ ≈ 1.10998 (requires interval arithmetic)
- The canonical justification for the ADDITIVE composition rule (= research-grade,
  per the audit §4a "Outstanding load-bearing step")
- The Vol(𝓑₃) = 8·G categorical identity (= scaffolded with `sorry` in
  `BorromeanVolumeCatalan.lean`)

These are the categorical / structural / numerical-bounds questions
that the audit explicitly flags as the next research steps.

## References

- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md) §4a — Bring + Faddeev probe results
- [`folio-assistant/computations/m_p_bring_plus_faddeev_h4_probe.py`](../../../../../folio-assistant/computations/m_p_bring_plus_faddeev_h4_probe.py) — numerical evaluation at q₀
- [`folio-assistant/computations/lambda_scale_h2_concrete_test.py`](../../../../../folio-assistant/computations/lambda_scale_h2_concrete_test.py) — symbolic h-expansion
- `lambda-scale-substrate-form.lean § lambdaA_qForm_eq_hForm` — Family A baseline
-/

namespace QOU.Archimedean

open Real

/-! ## §1  Definitions -/

/-- The Hecke deformation parameter `h_q = q − q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- **Bring color-tube** linking_weight component: `1/(1 − h_q · q^{10})`.

    Per `docs/audits/2026-05-22-faddeev-pentagon-operator-spike.md`:
    the integer power 10 = 9 color-pair assignments (3 quark colors ×
    3 quark colors) + 1 diagonal direction, matching the categorical
    structure of `conj:s5-so3-fiber-action` over Bring's surface.

    This is `Φ_q(h_q · q^{11}) / Φ_q(h_q · q^{10})` via the Faddeev
    functional equation `Φ_q(qz)/Φ_q(z) = 1/(1 − z)`. -/
noncomputable def bringColorTube (q : ℝ) : ℝ :=
  1 / (1 - heckeH q * q ^ 10)

/-- **Faddeev recursion at h⁴**: `1/(1 − h_q⁴)`.

    Per the h⁴ categorical-driver probe
    (`h4_categorical_drivers_probe.py`), this is the Faddeev recursion
    `Φ_q(q·z)/Φ_q(z) = 1/(1 − z)` evaluated at `z = h_q⁴`. The leading
    h⁴ coefficient (= 1) is independently forced by KLR positivity
    (the smallest non-trivial non-negative integer in the canonical
    basis at H_4 partition algebra). -/
noncomputable def faddeevH4 (q : ℝ) : ℝ :=
  1 / (1 - (heckeH q) ^ 4)

/-- **Combined linking_weight (additive composition)**:

      linkingWeightBringFaddeevH4 q = bringColorTube q + faddeevH4 q − 1

    The "minus 1" subtracts the duplicated h⁰ = 1 contribution that
    both factors carry (each gives 1 at h = 0). Result: at h = 0,
    `linkingWeightBringFaddeevH4 = 1 + 1 − 1 = 1`.

    See `categorically_distinct_from_familyA_at_q_one` below for the
    structural finding: this disagrees with Family A's `lambdaA = 5/2`
    at h = 0 (which lives at H_4 Wedderburn block sum, NOT at the
    Markov-trace value 1). -/
noncomputable def linkingWeightBringFaddeevH4 (q : ℝ) : ℝ :=
  bringColorTube q + faddeevH4 q - 1

/-! ## §2  Definitional unfoldings -/

theorem bringColorTube_def (q : ℝ) :
    bringColorTube q = 1 / (1 - heckeH q * q ^ 10) := rfl

theorem faddeevH4_def (q : ℝ) :
    faddeevH4 q = 1 / (1 - (heckeH q) ^ 4) := rfl

theorem linkingWeightBringFaddeevH4_eq_sum_minus_one (q : ℝ) :
    linkingWeightBringFaddeevH4 q = bringColorTube q + faddeevH4 q - 1 := rfl

/-! ## §3  Values at h = 0 (q = 1) -/

/-- At `q = 1`, the Hecke deformation `h_q = 0`. -/
theorem heckeH_at_one : heckeH 1 = 0 := by
  unfold heckeH
  norm_num

/-- At `q = 1`, the Bring color-tube component equals `1` (degenerate
    Φ_q functional equation: `Φ_q(qz)/Φ_q(z)` collapses to 1 when
    `z = 0`). -/
theorem bringColorTube_at_one : bringColorTube 1 = 1 := by
  unfold bringColorTube heckeH
  norm_num

/-- At `q = 1`, the Faddeev recursion at h⁴ equals `1` (same
    degeneracy as Bring). -/
theorem faddeevH4_at_one : faddeevH4 1 = 1 := by
  unfold faddeevH4 heckeH
  norm_num

/-- At `q = 1`, the combined linking_weight equals `1`:
    `1 + 1 − 1 = 1`. -/
theorem linkingWeightBringFaddeevH4_at_one :
    linkingWeightBringFaddeevH4 1 = 1 := by
  unfold linkingWeightBringFaddeevH4
  rw [bringColorTube_at_one, faddeevH4_at_one]
  norm_num

/-! ## §4  Categorical distinctness from Family A

The Family A linking_weight `lambdaA(q) = (3q² + 4 + 3q⁻²)/4` equals
`5/2` at q = 1 (per `lambdaA_c0` in `lambda-scale-substrate-form.lean`).

The Bring + Faddeev h⁴ form equals `1` at q = 1.

These differ — the two forms are **categorically distinct objects**, NOT
algebraically-equivalent reparameterisations of the same function.

This is a Lean formalisation of the structural finding in
[`lambda_scale_h2_concrete_test.py`](../../../../../folio-assistant/computations/lambda_scale_h2_concrete_test.py)
that the Bring color-tube `1/(1 − h·q^{10})` and Family A
`5/2 + (3/4)h²` are NOT algebraic reparameterisations of each other —
they describe DIFFERENT categorical objects in the linking_weight
landscape.

-/

/-- Family A baseline at q = 1: `lambdaA(1) = 5/2`.

    Restated here from `lambda-scale-substrate-form.lean § lambdaA_c0`
    (without importing — we restate the definition inline to keep this
    file independent for `lake check`). -/
theorem familyA_at_one_local : (3 * (1 : ℝ)^2 + 4 + 3 * (1 : ℝ)^(-2 : ℤ)) / 4 = 5 / 2 := by
  norm_num

/-- **Structural finding (categorical distinctness).** Family A
    linking_weight ≠ Bring + Faddeev h⁴ linking_weight at q = 1.

    The two candidate linking_weight forms differ at q = 1 (5/2 vs 1).
    They are NOT algebraically equivalent — the h² concrete test
    (Python `lambda_scale_h2_concrete_test.py`) shows they differ at
    every h^k order, not only at q = 1. This Lean theorem formalises
    one piece of that structural finding.

    Numerical context: at q₀ ≈ 1.110, both Family A (2.5328) and
    Bring + Faddeev h⁴ (2.4619) give linking_weight values within ~3 %
    of each other, but their h-expansions are entirely different
    objects (different h⁰, h¹, h² coefficients per
    `lambda_scale_h2_concrete_test.py`). The agreement at q₀ is a
    substrate-specific numerical coincidence. -/
theorem categorically_distinct_from_familyA_at_q_one :
    (3 * (1 : ℝ)^2 + 4 + 3 * (1 : ℝ)^(-2 : ℤ)) / 4 ≠ linkingWeightBringFaddeevH4 1 := by
  rw [familyA_at_one_local, linkingWeightBringFaddeevH4_at_one]
  norm_num

/-! ## §5  Positivity (when arguments stay in the domain)

The Bring color-tube and Faddeev factors are positive iff their
denominators are positive. Each denominator is `1 − z` for some
`z ∈ {h_q · q^{10}, h_q⁴}`, so positivity holds iff `z < 1`.

At the substrate q₀ ≈ 1.110:
  - `h_q · q₀^{10}` ≈ 0.594 < 1 ✓
  - `h_q⁴` ≈ 0.00191 < 1 ✓

Both denominators are positive at q₀, so both factors are positive.
These theorems give the positivity hypothesis in terms of a generic q.
-/

/-- Bring color-tube is positive when `h_q(q) · q^{10} < 1`. -/
theorem bringColorTube_pos (q : ℝ) (hlt : heckeH q * q ^ 10 < 1) :
    bringColorTube q > 0 := by
  unfold bringColorTube
  have hdenom : 1 - heckeH q * q ^ 10 > 0 := by linarith
  positivity

/-- Faddeev h⁴ is positive when `(h_q(q))⁴ < 1`. -/
theorem faddeevH4_pos (q : ℝ) (hlt : (heckeH q) ^ 4 < 1) :
    faddeevH4 q > 0 := by
  unfold faddeevH4
  have hdenom : 1 - (heckeH q) ^ 4 > 0 := by linarith
  positivity

/-- Combined: linkingWeightBringFaddeevH4 is positive when both
    components are positive AND their sum exceeds 1 (which holds when
    both ≥ 1, i.e. the substrate is in the domain). -/
theorem linkingWeightBringFaddeevH4_pos (q : ℝ)
    (h1 : heckeH q * q ^ 10 < 1)
    (h2 : (heckeH q) ^ 4 < 1)
    (h3 : heckeH q * q ^ 10 ≥ 0)
    (h4 : (heckeH q) ^ 4 ≥ 0) :
    linkingWeightBringFaddeevH4 q > 0 := by
  unfold linkingWeightBringFaddeevH4 bringColorTube faddeevH4
  have hd1 : 1 - heckeH q * q ^ 10 > 0 := by linarith
  have hd2 : 1 - (heckeH q) ^ 4 > 0 := by linarith
  have hd1_le_one : 1 - heckeH q * q ^ 10 ≤ 1 := by linarith
  have hd2_le_one : 1 - (heckeH q) ^ 4 ≤ 1 := by linarith
  -- Each factor is ≥ 1 (since denominator ≤ 1 and numerator = 1)
  have h_bring_ge_one : 1 / (1 - heckeH q * q ^ 10) ≥ 1 := by
    rw [ge_iff_le, le_div_iff hd1]; linarith
  have h_fad_ge_one : 1 / (1 - (heckeH q) ^ 4) ≥ 1 := by
    rw [ge_iff_le, le_div_iff hd2]; linarith
  linarith

/-! ## §6  Open / TODO

What is NOT proved in this file (research-grade or infrastructure):

1. **h² coefficient = 6** for Bring color-tube. Requires expressing q
   as a function of h (e.g. q = (h + √(h² + 4))/2) and Taylor-
   expanding in h. Needs Mathlib's power-series + analytic-function
   infrastructure.

2. **h⁴ coefficient = 693/8** for Bring color-tube. Same machinery as
   above.

3. **At substrate q₀ ≈ 1.10998**, the combined linkingWeightBring-
   FaddeevH4(q₀) ≈ 2.4619. Requires interval arithmetic + a fixed
   high-precision q₀ literal in Lean.

4. **Additive composition rule** (linking_weight = factor1 + factor2
   − 1). Currently a heuristic supported by 4 categorical hypotheses
   (per
   `additive_composition_categorical_probe.py`) but no formal proof.
   Categorical proof would route through one of:
   - H_4 Wedderburn direct-sum decomposition (5 partitions)
   - S_4 ↓ S_3 restriction
   - Half-symmetric Frobenius reciprocity at H_4
   - KLR positivity / Kashiwara crystal

5. **Numerical equivalence with PR #1272's `5/2 − G·h²`** at q₀.
   Both forms agree to ~5 ppm at q₀ but disagree at every other order
   in h. The reason for the numerical coincidence at the substrate is
   open — likely substrate-specific (q^{10} ≈ 2.84 multiplying h ≈
   0.209 happens to land close to 1 − 1/(5/2 − G·h²)).

-/

end QOU.Archimedean
