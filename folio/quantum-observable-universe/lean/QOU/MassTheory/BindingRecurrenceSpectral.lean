import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.LinearCombination
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
characteristic roots `λ_± = (τ ± √(τ²−4))/2`. This file proves, for a root
`λ` carried as a parameter with its defining quadratic `λ² − τλ + 1 = 0` (no
`Real.sqrt`; owner ruling 2026-11-27, transcendental boundary), the three
structural facts that make the kernel **extensive** (its solutions grow), which
is exactly the property the saturating `|χ|` joint trace lacks
(`productModel_3body_nonpos`; PR #2703: `B_joint` is A-independent, λ_eff ≈ 1):

* `root_mul_partner_eq_one` — a root `λ` and its partner `τ − λ` multiply to `1`
  (the `det = 1` / reciprocal-roots fact);
* `root_add_partner`        — the two roots sum to `τ`;
* `dominantRoot_gt_one`     — for `τ > 2`, a root with `τ ≤ 2λ` (the dominant
  one) exceeds `1` (extensive growth), whence its partner `1/λ < 1`.

The real roots `lambdaPlus τ = (τ + √(τ²−4))/2` and `lambdaMinus τ`, and the
proof that `lambdaPlus` is the dominant root, live behind the boundary in
`QOU.Transcendental.MassTheory.BindingRecurrenceSpectralReal`.

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

variable {K : Type*}

/-- The partner of a root `λ` of `x² − τx + 1` is `τ − λ`, and the two are reciprocal:
`λ · (τ − λ) = 1` (the `det = 1` constant term). -/
theorem root_mul_partner_eq_one [CommRing K] {τ l : K} (hl : l ^ 2 - τ * l + 1 = 0) :
    l * (τ - l) = 1 := by
  linear_combination -hl

/-- The partner `τ − λ` is itself a root of `x² − τx + 1`. -/
theorem partner_isRoot [CommRing K] {τ l : K} (hl : l ^ 2 - τ * l + 1 = 0) :
    (τ - l) ^ 2 - τ * (τ - l) + 1 = 0 := by
  linear_combination hl

/-- **Trace identity.** The two roots sum to `τ`. -/
theorem root_add_partner [CommRing K] (τ l : K) : l + (τ - l) = τ := by ring

/-- **Extensive growth.** For `τ > 2`, the dominant root (`τ ≤ 2λ`) of `x² − τx + 1`
exceeds `1`; with `λ · (τ − λ) = 1` its partner is `< 1`. The depth-2 binding kernel
therefore has a growing (extensive) general solution — the property a saturating
multiplicative trace (`τ = 2`, `λ = 1`) lacks. -/
theorem dominantRoot_gt_one [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {τ l : K} (hτ : 2 < τ) (hdom : τ ≤ 2 * l) : 1 < l := by
  linarith

/-- The partner of the dominant root lies strictly between `0` and `1`. -/
theorem partner_lt_one [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {τ l : K} (hτ : 2 < τ) (hl : l ^ 2 - τ * l + 1 = 0) (hdom : τ ≤ 2 * l) :
    0 < τ - l ∧ τ - l < 1 := by
  have h1 := dominantRoot_gt_one hτ hdom
  have hp := root_mul_partner_eq_one hl
  constructor <;> nlinarith

end QOU.Mass
