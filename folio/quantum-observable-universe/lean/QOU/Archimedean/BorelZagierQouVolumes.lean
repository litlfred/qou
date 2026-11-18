import Mathlib.Tactic

/-!
# QOU.Archimedean.BorelZagierQouVolumes — conjecture carrier (content-bearing, no instance)

**§3b-cond class axiomatisation** for content block
[`conj:borel-zagier-qou-volumes`](../../../quantum-observable-universe/archimedean-universe/borel-zagier-qou-volumes.md): *Rational linear independence of QOU hyperbolic volumes (Borel--Zagier)*.

This is a **conjecture**, and the honest open state is a **content-bearing class
with no instance** (AGENTS.md §3b-tax). `BorelZagierQouVolumes` carries three real volume fields (`vol41`, `vol52`, `volBorromean`) and
`qLinearIndependent`, which states that a vanishing rational combination of
them forces all three coefficients to vanish — the conjecture's content, not a
placeholder.

**No instance is provided anywhere in this file.** An instance *is* the
conjecture; fabricating one would be the audit-dodge §1a forbids. A downstream
result takes `[BorelZagierQouVolumes]` as an explicit `[Instance]` hypothesis and
is thereby **conditional on it** — rigorous modulo this single named input, per
§3b-cond. It is not unconditional, and calling it so would be the
"conditional-proved ≠ premise-established" confusion AGENTS.md warns about.
-/

namespace QOU.Archimedean

/-- Rational linear independence of QOU hyperbolic volumes (Borel--Zagier)

    Conjectural class — see [`conj:borel-zagier-qou-volumes`](../../../quantum-observable-universe/archimedean-universe/borel-zagier-qou-volumes.md). -/
class BorelZagierQouVolumes where
  -- Witness: computations/none
  /-- **Content statement** (from manuscript):

      **Conjecture (Borel--Zagier for QOU volumes).**
The three QOU hyperbolic volumes are $\mathbb{Q}$-linearly independent.

      The field asserts the conjecture's shape: every *nontrivial*
      rational combination of the three volumes is non-vanishing.
      The three volume fields are data pinned by the manuscript's
      definitions; tying them to formalised values is the remaining
      refinement. -/
  vol41 : ℝ
  vol52 : ℝ
  volBorromean : ℝ
  /-- No nontrivial rational relation: a vanishing rational
      combination forces all three coefficients to vanish. -/
  qLinearIndependent :
    ∀ a b c : ℚ,
      (a : ℝ) * vol41 + (b : ℝ) * vol52 + (c : ℝ) * volBorromean = 0 →
      a = 0 ∧ b = 0 ∧ c = 0

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/borel-zagier-qou-volumes.ts
-- **No instance is provided — that is the honest open state** (AGENTS.md §3b-tax).

namespace BorelZagierQouVolumes

/-- Conditional on `BorelZagierQouVolumes`, the first volume `vol41` is non-zero. -/
theorem vol41_ne_zero [h : BorelZagierQouVolumes] : h.vol41 ≠ 0 := by
  intro h0
  have hlin : ((1 : ℚ) : ℝ) * h.vol41 + ((0 : ℚ) : ℝ) * h.vol52 + ((0 : ℚ) : ℝ) * h.volBorromean = 0 := by
    simp [h0]
  have ⟨ha, _, _⟩ := h.qLinearIndependent 1 0 0 hlin
  exact one_ne_zero ha

/-- Conditional on `BorelZagierQouVolumes`, the second volume `vol52` is non-zero. -/
theorem vol52_ne_zero [h : BorelZagierQouVolumes] : h.vol52 ≠ 0 := by
  intro h0
  have hlin : ((0 : ℚ) : ℝ) * h.vol41 + ((1 : ℚ) : ℝ) * h.vol52 + ((0 : ℚ) : ℝ) * h.volBorromean = 0 := by
    simp [h0]
  have ⟨_, hb, _⟩ := h.qLinearIndependent 0 1 0 hlin
  exact one_ne_zero hb

/-- Conditional on `BorelZagierQouVolumes`, the third volume `volBorromean` is non-zero. -/
theorem volBorromean_ne_zero [h : BorelZagierQouVolumes] : h.volBorromean ≠ 0 := by
  intro h0
  have hlin : ((0 : ℚ) : ℝ) * h.vol41 + ((0 : ℚ) : ℝ) * h.vol52 + ((1 : ℚ) : ℝ) * h.volBorromean = 0 := by
    simp [h0]
  have ⟨_, _, hc⟩ := h.qLinearIndependent 0 0 1 hlin
  exact one_ne_zero hc

/-- Conditional on `BorelZagierQouVolumes`, `vol41` is not a rational multiple of `vol52`. -/
theorem vol41_ne_rat_smul_vol52 [h : BorelZagierQouVolumes] (q : ℚ) :
    h.vol41 ≠ (q : ℝ) * h.vol52 := by
  intro heq
  have hlin : ((1 : ℚ) : ℝ) * h.vol41 + ((-q : ℚ) : ℝ) * h.vol52 + ((0 : ℚ) : ℝ) * h.volBorromean = 0 := by
    push_cast
    linarith
  have ⟨ha, _, _⟩ := h.qLinearIndependent 1 (-q) 0 hlin
  exact one_ne_zero ha

/-- Conditional on `BorelZagierQouVolumes`, `vol52` is not a rational multiple of `volBorromean`. -/
theorem vol52_ne_rat_smul_volBorromean [h : BorelZagierQouVolumes] (q : ℚ) :
    h.vol52 ≠ (q : ℝ) * h.volBorromean := by
  intro heq
  have hlin : ((0 : ℚ) : ℝ) * h.vol41 + ((1 : ℚ) : ℝ) * h.vol52 + ((-q : ℚ) : ℝ) * h.volBorromean = 0 := by
    push_cast
    linarith
  have ⟨_, hb, _⟩ := h.qLinearIndependent 0 1 (-q) hlin
  exact one_ne_zero hb

/-- Conditional on `BorelZagierQouVolumes`, rational linear combinations of the three volumes
    uniquely determine all three rational coefficients. -/
theorem rat_comb_inj [h : BorelZagierQouVolumes] {a₁ b₁ c₁ a₂ b₂ c₂ : ℚ}
    (heq : (a₁ : ℝ) * h.vol41 + (b₁ : ℝ) * h.vol52 + (c₁ : ℝ) * h.volBorromean =
      (a₂ : ℝ) * h.vol41 + (b₂ : ℝ) * h.vol52 + (c₂ : ℝ) * h.volBorromean) :
    a₁ = a₂ ∧ b₁ = b₂ ∧ c₁ = c₂ := by
  have hlin :
      ((a₁ - a₂ : ℚ) : ℝ) * h.vol41 + ((b₁ - b₂ : ℚ) : ℝ) * h.vol52 +
        ((c₁ - c₂ : ℚ) : ℝ) * h.volBorromean = 0 := by
    push_cast
    linarith
  obtain ⟨ha, hb, hc⟩ := h.qLinearIndependent (a₁ - a₂) (b₁ - b₂) (c₁ - c₂) hlin
  exact ⟨sub_eq_zero.mp ha, sub_eq_zero.mp hb, sub_eq_zero.mp hc⟩

end BorelZagierQouVolumes

end QOU.Archimedean
