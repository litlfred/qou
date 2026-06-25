import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# QOU.Mass.BindingRecurrenceSpectral — the depth-2 binding kernel is extensive

The fibre q-difference kernel for the binding generating function is depth-2,
`R(q,x) = x² − τ·x + 1` with `det = 1` (constant term `1`), and `τ` is fixed
**without fit** by the selection-rule anchors `a_D^(n) = lw(n−1)`
(`binding_selection_rule_tau_closure.py`, PR #2612); `τ(q₀) = 2.6424`.

The body-order recurrence `a_{n+2} = τ·a_{n+1} − a_n`
(`QOU.Mass.BindingQDifferenceRecurrence`, depth `2`, kernel `[−1, τ]`) has
characteristic roots `λ_± = (τ ± √(τ²−4))/2`. This file proves the three
structural facts that make the kernel **extensive** (its solutions grow), which
is exactly the property the saturating `|χ|` joint trace lacks
(`productModel_3body_nonpos`; PR #2703: `B_joint` is A-independent, λ_eff ≈ 1):

* `lambdaPlus_isRoot`     — `λ₊` solves `x² − τx + 1 = 0`;
* `lambda_product_eq_one` — `λ₊ · λ₋ = 1` (the `det = 1` / reciprocal-roots fact);
* `lambdaPlus_gt_one`     — for `τ > 2`, the dominant root `λ₊ > 1` (extensive
  growth), whence `λ₋ = 1/λ₊ < 1`.

The `τ > 2` hypothesis is **discharged for every substrate** `0 < q` (no fit, no
geometric input). The selection-rule trace `τ = (a_D^(2)+a_D^(4))/a_D^(3)` with
anchors `a_D^(2)=1`, `a_D^(3)=(s+2)/3`, `a_D^(4)=(3s²−2)/4` in `s = [2]_q = q+q⁻¹`
has the closed form `τ([2]_q) = 3(3[2]_q²+2)/(4([2]_q+2))` (PR #2722), and
`[2]_q ≥ 2` (AM–GM) forces `τ > 2`:

* `tauOfBracket`             — the selection-rule trace as a function of `[2]_q`;
* `tauOfBracket_eq_anchor_ratio` — it equals the anchor ratio `(a_D²+a_D⁴)/a_D³`;
* `two_le_qBracket2`         — `[2]_q = q + q⁻¹ ≥ 2` for `0 < q` (AM–GM);
* `two_lt_tauOfBracket`      — `2 ≤ s ⇒ τ(s) > 2`;
* `binding_extensive_of_pos` — **q-robust extensivity**: `0 < q ⇒ λ₊(τ([2]_q)) > 1`.

So extensivity holds for the **whole** substrate family, independent of the specific
(owner-gated, geometric) value `τ(q₀) = 2.6424`.

So `τ > 2 ⇒ λ₊ > 1`: the kernel encodes the extensive (A-scaling) binding the
saturating multiplicative trace (sitting at the degenerate `τ = 2`, `λ = 1`
no-growth boundary) cannot source. `τ(q₀) = 2.6424 > 2` satisfies the hypothesis.

**Scope (PR #2752).** These are unconditional facts about the roots of
`x² − τx + 1`; read as a claim about binding they are a *conditional* — IF the
binding generating function had this fixed-τ depth-2 kernel, THEN it is
extensive. The physical body-order coefficients `a_D^(n) = lw(n−1)` in fact grow
*super-geometrically* (#2708; ratios → 2.76, past `λ₊`), so `λ₊ > 1` witnesses
that the *seed* kernel is extensive — correct but weaker than "the binding grows
at rate `λ₊`". The qualitative "extensive, not saturating" conclusion is thereby
reinforced, not weakened. See
`docs/audits/2026-06-25-spectral-bridge-tautology-recurrence-vs-lw.md`.

LaTeX label: `prop:binding-recurrence-extensive` (interprets
`prop:binding-genfun-qdifference`).

## References
- [manuscript] §mass-theory/binding-genfun-qdifference
-/

namespace QOU.Mass

open Real

/-- Dominant root of the depth-2 binding kernel `x² − τx + 1`. -/
noncomputable def lambdaPlus (τ : ℝ) : ℝ := (τ + Real.sqrt (τ ^ 2 - 4)) / 2

/-- Sub-dominant root of the depth-2 binding kernel `x² − τx + 1`. -/
noncomputable def lambdaMinus (τ : ℝ) : ℝ := (τ - Real.sqrt (τ ^ 2 - 4)) / 2

/-- `λ₊` is a root of the characteristic polynomial `x² − τx + 1`. -/
theorem lambdaPlus_isRoot {τ : ℝ} (hτ : 2 < τ) :
    (lambdaPlus τ) ^ 2 - τ * lambdaPlus τ + 1 = 0 := by
  unfold lambdaPlus
  have hs : Real.sqrt (τ ^ 2 - 4) ^ 2 = τ ^ 2 - 4 := Real.sq_sqrt (by nlinarith)
  have expand :
      ((τ + Real.sqrt (τ ^ 2 - 4)) / 2) ^ 2 - τ * ((τ + Real.sqrt (τ ^ 2 - 4)) / 2) + 1
        = (Real.sqrt (τ ^ 2 - 4) ^ 2 - (τ ^ 2 - 4)) / 4 := by ring
  rw [expand, hs]; ring

/-- **det = 1**: the two roots are reciprocal, `λ₊ · λ₋ = 1` (the constant term). -/
theorem lambda_product_eq_one {τ : ℝ} (hτ : 2 < τ) :
    lambdaPlus τ * lambdaMinus τ = 1 := by
  unfold lambdaPlus lambdaMinus
  have hs : Real.sqrt (τ ^ 2 - 4) ^ 2 = τ ^ 2 - 4 := Real.sq_sqrt (by nlinarith)
  have expand :
      (τ + Real.sqrt (τ ^ 2 - 4)) / 2 * ((τ - Real.sqrt (τ ^ 2 - 4)) / 2)
        = (τ ^ 2 - Real.sqrt (τ ^ 2 - 4) ^ 2) / 4 := by ring
  rw [expand, hs]; ring

/-- **Extensive growth.** For `τ > 2` the dominant root exceeds `1`; with
`λ₊ · λ₋ = 1` this forces `λ₋ < 1`. The depth-2 binding kernel therefore has a
growing (extensive) general solution — the property a saturating multiplicative
trace (`τ = 2`, `λ = 1`) lacks. -/
theorem lambdaPlus_gt_one {τ : ℝ} (hτ : 2 < τ) : 1 < lambdaPlus τ := by
  unfold lambdaPlus
  have hpos : (0 : ℝ) < τ ^ 2 - 4 := by nlinarith
  have hs : 0 < Real.sqrt (τ ^ 2 - 4) := Real.sqrt_pos.mpr hpos
  linarith

/-! ## The selection-rule trace `τ([2]_q)` discharges the `τ > 2` hypothesis

The anchors `a_D^(n) = lw(n−1)` (`linking_weight_family_a`, PRs #2612/#2722) give,
in `s = [2]_q = q + q⁻¹`, the closed-form trace below. We prove it is `> 2` for
every `s ≥ 2`, and `[2]_q ≥ 2` for every `0 < q` (AM–GM), so the dominant root
exceeds `1` for the **whole** substrate family — no fit, no geometric input. -/

/-- The selection-rule trace as a function of the quantum integer `s = [2]_q`.
From `a_D^(2)=1`, `a_D^(3)=(s+2)/3`, `a_D^(4)=(3s²−2)/4`,
`τ = (a_D^(2)+a_D^(4))/a_D^(3) = 3(3s²+2)/(4(s+2))`. -/
noncomputable def tauOfBracket (s : ℝ) : ℝ := 3 * (3 * s ^ 2 + 2) / (4 * (s + 2))

/-- The closed form equals the anchor ratio `(a_D^(2)+a_D^(4))/a_D^(3)`
(whenever `s ≠ -2`). -/
theorem tauOfBracket_eq_anchor_ratio {s : ℝ} (hs : s + 2 ≠ 0) :
    tauOfBracket s = (1 + (3 * s ^ 2 - 2) / 4) / ((s + 2) / 3) := by
  unfold tauOfBracket
  field_simp
  ring

/-- The quantum integer `[2]_q = q + q⁻¹`. -/
noncomputable def qBracket2 (q : ℝ) : ℝ := q + q⁻¹

/-- **AM–GM.** For `0 < q`, `[2]_q = q + q⁻¹ ≥ 2` (equality iff `q = 1`), since
`q + q⁻¹ − 2 = (q−1)²/q ≥ 0`. -/
theorem two_le_qBracket2 {q : ℝ} (hq : 0 < q) : 2 ≤ qBracket2 q := by
  unfold qBracket2
  have hq0 : q ≠ 0 := ne_of_gt hq
  have key : (0 : ℝ) ≤ (q - 1) ^ 2 / q := div_nonneg (sq_nonneg _) hq.le
  have hid : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by field_simp; ring
  linarith [key, hid]

/-- **`τ(s) > 2` for `s ≥ 2`.** Clearing the positive denominator `4(s+2)`,
`τ(s) − 2 = (9s² − 8s − 10)/(4(s+2))`, and `9s² − 8s − 10 ≥ 10 > 0` for `s ≥ 2`. -/
theorem two_lt_tauOfBracket {s : ℝ} (hs : 2 ≤ s) : 2 < tauOfBracket s := by
  have hd : (0 : ℝ) < 4 * (s + 2) := by linarith
  have hne : (4 : ℝ) * (s + 2) ≠ 0 := ne_of_gt hd
  have hsplit : tauOfBracket s - 2 = (9 * s ^ 2 - 8 * s - 10) / (4 * (s + 2)) := by
    unfold tauOfBracket; field_simp; ring
  have hpos : 0 < (9 * s ^ 2 - 8 * s - 10) / (4 * (s + 2)) :=
    div_pos (by nlinarith [sq_nonneg (s - 2)]) hd
  linarith [hsplit, hpos]

/-- **q-robust extensivity.** For **any** substrate `0 < q`, the dominant root of
the binding kernel exceeds `1`: chaining `[2]_q ≥ 2` (AM–GM) ⇒ `τ([2]_q) > 2` ⇒
`λ₊ > 1`. The extensive (A-scaling) binding is therefore a structural consequence
of the depth-2 `det = 1` kernel and the selection-rule trace — independent of the
specific (owner-gated, geometric) value `τ(q₀) = 2.6424`. -/
theorem binding_extensive_of_pos {q : ℝ} (hq : 0 < q) :
    1 < lambdaPlus (tauOfBracket (qBracket2 q)) :=
  lambdaPlus_gt_one (two_lt_tauOfBracket (two_le_qBracket2 hq))

end QOU.Mass
