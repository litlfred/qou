import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

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
geometric input) in `QOU.Mass.BindingTauAnchorClosure`: the selection-rule trace
`τ = (a_D^(2)+a_D^(4))/a_D^(3) = 3(3[2]_q²+2)/(4([2]_q+2))` satisfies `0 < q ⇒ 2 < τ`
(`tauAnchor_gt_two`, sum-of-squares), and `binding_extensive_at_substrate` composes
it with `lambdaPlus_gt_one` below to give `λ₊ > 1` for the whole substrate family.

So `τ > 2 ⇒ λ₊ > 1`: the kernel encodes the extensive (A-scaling) binding the
saturating multiplicative trace (sitting at the degenerate `τ = 2`, `λ = 1`
no-growth boundary) cannot source. `τ(q₀) = 2.6424 > 2` satisfies the hypothesis.

**Scope (2026-11-16).** A q-difference equation `G(qx) = R(q,x) G(x)` does
**not** give a constant-coefficient recurrence: comparing `x^n` gives
`(q^n − r_0) B_n = Σ_{j≥1} r_j B_{n−j}`, with coefficients depending on `n`
(`prop:binding-genfun-qdifference`, corrected the same day). So the
constant-`τ` recurrence `a_{n+2} = τ a_{n+1} − a_n` studied here is not the one
`R = x² − τx + 1` induces; it is a separate model, and the facts below are about
that model only.

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
- [leitner2026] §mass-theory/binding-genfun-qdifference
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

/-- `λ₋` is also a root of the characteristic polynomial `x² − τx + 1`. -/
theorem lambdaMinus_isRoot {τ : ℝ} (hτ : 2 < τ) :
    (lambdaMinus τ) ^ 2 - τ * lambdaMinus τ + 1 = 0 := by
  unfold lambdaMinus
  have hs : Real.sqrt (τ ^ 2 - 4) ^ 2 = τ ^ 2 - 4 := Real.sq_sqrt (by nlinarith)
  have expand :
      ((τ - Real.sqrt (τ ^ 2 - 4)) / 2) ^ 2 - τ * ((τ - Real.sqrt (τ ^ 2 - 4)) / 2) + 1
        = (Real.sqrt (τ ^ 2 - 4) ^ 2 - (τ ^ 2 - 4)) / 4 := by ring
  rw [expand, hs]; ring

/-- **Trace identity:** the sum of the two characteristic roots equals `τ`. -/
theorem lambda_sum_eq_tau (τ : ℝ) :
    lambdaPlus τ + lambdaMinus τ = τ := by
  unfold lambdaPlus lambdaMinus
  ring

/-- **Sub-dominant root lies strictly in `(0, 1)`.**
    For `τ > 2`, `0 < λ₋ < 1`. -/
theorem lambdaMinus_pos_and_lt_one {τ : ℝ} (hτ : 2 < τ) :
    0 < lambdaMinus τ ∧ lambdaMinus τ < 1 := by
  have hprod := lambda_product_eq_one hτ
  have hgt := lambdaPlus_gt_one hτ
  have hpos_plus : 0 < lambdaPlus τ := by linarith
  refine ⟨?_, ?_⟩
  · by_contra hle
    push_neg at hle
    have : lambdaPlus τ * lambdaMinus τ ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos (le_of_lt hpos_plus) hle
    linarith
  · nlinarith

/-- **General solution of the depth-2 binding recurrence.**
    Every linear combination `c₊ · λ₊^n + c₋ · λ₋^n` satisfies the depth-2
    recurrence `a_{n+2} = τ · a_{n+1} - a_n`. -/
theorem recurrence_general_solution {τ : ℝ} (hτ : 2 < τ) (cPlus cMinus : ℝ) (n : ℕ) :
    cPlus * (lambdaPlus τ) ^ (n + 2) + cMinus * (lambdaMinus τ) ^ (n + 2) =
      τ * (cPlus * (lambdaPlus τ) ^ (n + 1) + cMinus * (lambdaMinus τ) ^ (n + 1)) -
        (cPlus * (lambdaPlus τ) ^ n + cMinus * (lambdaMinus τ) ^ n) := by
  have h1 := lambdaPlus_isRoot hτ
  have h2 := lambdaMinus_isRoot hτ
  linear_combination cPlus * (lambdaPlus τ) ^ n * h1 + cMinus * (lambdaMinus τ) ^ n * h2

end QOU.Mass
