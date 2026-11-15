import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.Archimedean.QMomentum

**Canonical declaration** for content block at
[`quantum-observable-universe/climax-volume-mass/q-momentum.ts`](quantum-observable-universe/climax-volume-mass/q-momentum.ts).

Formalises the manuscript **definition** of the `q`-momentum as the
`q`-bracket-weighted sum of the crossing signs of a braid word,

`p_q(β) = Σ_j [ε_j]_q = Σ_j (q^{ε_j} − q^{−ε_j})/(q − q⁻¹)`,

and proves the owner-ruled canonical fact (2026-07-05): whenever
`q − q⁻¹ ≠ 0` (i.e. `q ≠ ±1`; at `q = 1` the identity holds in the limit)
`[+1]_q = +1` and `[−1]_q = −1` exactly, so `p_q(β)` equals the classical
writhe `w(β) = Σ_j ε_j`. (This corrects the block's boxed
formula: the spurious `ε_j` prefactor and the inequivalent `Σ(q^{2ε}−1)/(q²−1)`
form both disagree with the building-block table for negative crossings.)
§7c: archimedean over `ℝ` (uses `q⁻¹`).
-/

namespace QOU.Archimedean

/-- The `q`-integer `[e]_q = (q^e − q^{−e})/(q − q⁻¹)` for `e : ℤ`. -/
noncomputable abbrev qBracket (q : ℝ) (e : ℤ) : ℝ :=
  QOU.QInteger.qIntBalZ q e

/-- `[+1]_q = 1`. -/
theorem qBracket_one (q : ℝ) (hq : q - q⁻¹ ≠ 0) : qBracket q 1 = 1 := by
  simp only [qBracket, QOU.QInteger.qIntBalZ]
  rw [zpow_one, zpow_neg, zpow_one, div_self hq]

/-- `[−1]_q = −1`. -/
theorem qBracket_neg_one (q : ℝ) (hq : q - q⁻¹ ≠ 0) : qBracket q (-1) = -1 := by
  simp only [qBracket, QOU.QInteger.qIntBalZ]
  rw [zpow_neg, zpow_one, neg_neg, zpow_one]
  rw [div_eq_iff hq]
  ring

/-- Data for the `q`-momentum of a braid word.

    A `definition` carrier: the substrate `q` (with `q − q⁻¹ ≠ 0`) and the
    crossing-sign word `crossings : List ℤ`, each entry `±1`. -/
structure QMomentum where
  /-- Substrate parameter `q`. -/
  q : ℝ
  /-- `q − q⁻¹ ≠ 0` (the `q`-bracket denominator is nonzero). -/
  q_reg : q - q⁻¹ ≠ 0
  /-- The signed crossing word `ε₁,…,ε_k` of the braid representative. -/
  crossings : List ℤ
  /-- Each crossing is `±1`. -/
  signs : ∀ e ∈ crossings, e = 1 ∨ e = -1

/-- The `q`-momentum `p_q(β) = Σ_j [ε_j]_q`. -/
noncomputable def QMomentum.p_q (M : QMomentum) : ℝ :=
  (M.crossings.map (qBracket M.q)).sum

/-- The classical writhe `w(β) = Σ_j ε_j`. -/
def QMomentum.writhe (M : QMomentum) : ℤ := M.crossings.sum

-- Ref: [leitner2026] quantum-observable-universe/climax-volume-mass/q-momentum.ts

/-- Auxiliary: over a `±1` word, the `q`-bracket sum collapses to the integer
    sum, because `[±1]_q = ±1`. -/
theorem qMomentum_aux (q : ℝ) (hq : q - q⁻¹ ≠ 0) :
    ∀ l : List ℤ, (∀ e ∈ l, e = 1 ∨ e = -1) →
      (l.map (qBracket q)).sum = ((l.sum : ℤ) : ℝ) := by
  intro l
  induction l with
  | nil => intro _; simp
  | cons a t ih =>
    intro h
    have ht : ∀ e ∈ t, e = 1 ∨ e = -1 := fun e he => h e (List.mem_cons_of_mem a he)
    simp only [List.map_cons, List.sum_cons, Int.cast_add]
    rw [ih ht]
    rcases h a (List.mem_cons_self ..) with ha | ha
    · rw [ha, qBracket_one q hq]; push_cast; ring
    · rw [ha, qBracket_neg_one q hq]; push_cast; ring

/-- **Owner-ruled canonical identity (2026-07-05):** for `q` with
    `q − q⁻¹ ≠ 0` (`M.q_reg`) the `q`-momentum equals the writhe — because
    `[±1]_q = ±1` exactly, each crossing contributes its sign with no residual
    `q`-dependence. -/
theorem p_q_eq_writhe (M : QMomentum) : M.p_q = (M.writhe : ℝ) :=
  qMomentum_aux M.q M.q_reg M.crossings M.signs

end QOU.Archimedean
