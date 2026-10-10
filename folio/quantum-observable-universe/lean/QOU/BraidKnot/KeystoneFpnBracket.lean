import Mathlib.Tactic

/-!
# Keystone target-3 — the deuteron `f_pn` bracket gate (archimedean)

The full-Hecke geometric-index program's falsifiable **target (3)** (see
`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`): *any* index reproducing the
`W_λ` family must land the deuteron proton/neutron interface fraction `f_pn` in the bracket

  `f_pn ∈ (0.39479…, 0.66067…)`,

which **strictly contains** the AME-exact `f_pn ≈ 0.58776` (#2503 / #2528 consumer).

This file formalizes that target as a machine-checkable gate, parallel to the order-`h²` defect gate
(`KeystoneG2Gate`, target 1) and the conjugation symmetry (`qPlancherelWeight_conj`, target 4) — but
at the **archimedean / deuteron-observable** level rather than the pure-`ℤ` structural level.

**Honest scope.** Unlike the defect cubic (a proved `ℤ` identity), the bracket bounds are
**q₀-derived real numbers** from the algebraic `W_(2,1)` (the `n=3` standard-rep weight) evaluated at
the substrate: the lower bound is the LP-dual `a_K/R` ratio `≈ 0.39479017` (witness
`computations/a-K-via-lp-dual.witness.json`); the upper bound `≈ 0.66067` and the bracket framing are
the #2503/#2528 consumer of `W_(2,1)`. Those derivations live in the q₀ **compute layer**; they are
**cited here, not re-derived in Lean**. The Lean content is the **gate predicate** (`f_pn` lands the
bracket), the **strict containment** of the experimental value, and the bracket's non-degeneracy —
the falsifiable check the geometric `W_λ` index (#2524) must pass for the deuteron. No fit.
-/

namespace QOU.BraidKnot.KeystoneFpnBracket

/-- **Lower bracket bound** for the deuteron `f_pn`, from the algebraic `W_(2,1)` at q₀: the LP-dual
`a_K/R` ratio `≈ 0.39479017` (witness `a-K-via-lp-dual`). Cited (q₀-derived), not Lean-derived. -/
noncomputable def fpnLower : ℝ := 0.39479017

/-- **Upper bracket bound** for the deuteron `f_pn`, from the algebraic `W_(2,1)` at q₀ `≈ 0.66067`
(#2503 / #2528 consumer). Cited (q₀-derived), not Lean-derived. -/
noncomputable def fpnUpper : ℝ := 0.66067

/-- The **AME-exact** deuteron interface fraction `f_pn ≈ 0.58776`. -/
noncomputable def fpnAME : ℝ := 0.58776

/-- **The deuteron `f_pn` bracket gate.** A candidate index passes iff its predicted deuteron
interface fraction lands strictly inside the `W_(2,1)`-derived bracket. -/
def PassesFpnBracket (fpn : ℝ) : Prop := fpnLower < fpn ∧ fpn < fpnUpper

/-- **The bracket is non-degenerate** (`lower < upper`) — it has a genuine falsifiable margin, not a
point. -/
theorem fpnBracket_nondegenerate : fpnLower < fpnUpper := by
  unfold fpnLower fpnUpper; norm_num

/-- **The bracket has positive width** — the size of the falsifiable margin. -/
theorem fpnBracket_width_pos : 0 < fpnUpper - fpnLower := by
  unfold fpnLower fpnUpper; norm_num

/-- **The experimental value is strictly bracketed.** The AME-exact `f_pn ≈ 0.58776` passes the gate
— the `W_(2,1)`-derived bracket strictly contains the measured deuteron interface fraction, so an
index that lands the bracket is deuteron-consistent. This is the target-(3) content: the bracket is
*about* the right number. -/
theorem ame_strictly_bracketed : PassesFpnBracket fpnAME := by
  unfold PassesFpnBracket fpnLower fpnUpper fpnAME
  constructor <;> norm_num

/-- **Membership is decidable margin both sides.** For a candidate `f_pn`, passing is equivalent to
beating both bounds — restating the gate as the conjunction a checker evaluates. -/
theorem passesFpnBracket_iff (fpn : ℝ) :
    PassesFpnBracket fpn ↔ fpnLower < fpn ∧ fpn < fpnUpper := Iff.rfl

end QOU.BraidKnot.KeystoneFpnBracket
