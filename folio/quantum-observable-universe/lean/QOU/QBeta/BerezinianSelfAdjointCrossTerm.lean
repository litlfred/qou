/-
Copyright (c) 2026 litlfred. All rights reserved.

# The graded-self-adjoint Berezinian cross-term is bar-EVEN (a parity obstruction)

Formalize-first structural brick for the super-DM / Berezinian `c₃`-mixing wall
(`qCubicGradedSplit`, bean `qou-jqof`, PR #4140, off-`main`). The odd-face bricks
(`OddDecayWeightParity.crossTerm_bar_odd`) *model* the first even/odd mixing order
`c₃` as the Berezinian off-diagonal cross-term `t = B·D⁻¹·C` and *assume* it is
bar-ODD via a factorization `t = g·γ` (bar-even dressing × bar-odd weight).

This file computes the parity of the cross-term **when the super-matrix is graded
self-adjoint** — the natural hypothesis, since the mass endomorphism `𝓜`
(`Re 𝔙 = binding`) is bar-self-adjoint. Graded self-adjointness makes the odd
off-diagonal blocks bar-conjugate, `C = −σ(B)`. The result is the **opposite** of
the assumed model:

> **The self-adjoint cross-term `t = B·D⁻¹·C = −B·D⁻¹·σB` is bar-EVEN** (`σ t = t`),
> not bar-odd. It is a norm-squared object `|B|²/D`, intrinsically self-conjugate.

**Consequence (the honest structural constraint this surfaces).** If `c₃` is
genuinely bar-ODD (the whole premise of the odd-face split), then the Berezinian
cross-term that realizes it **cannot** come from a graded-self-adjoint super-matrix:
the off-diagonal blocks must be **independent** (`C ≠ −σ(B)`), *not* adjoint-linked.
So the `OddDecayWeightParity` `t = g·γ` model is only consistent with a
**non-self-adjoint** super-structure — a real constraint on any derivation of the
wall `q_cubic = C1`, and a correction to the intuition that graded self-adjointness
"forces" the bar-odd cross-term (it forces the bar-EVEN one).

**Scope (constraint, not closure).** This proves a parity obstruction, not a
derivation of `c₃`. It prunes the fittable space by ruling out the self-adjoint
route to a bar-odd cross-term. No `c_k` value is derived; nothing is wired; no
dependency on PR #4140's unmerged `SuperDMBerezinian.lean` (uses only on-`main`
`ZBarParity`). §7c: generic `{R : Type*} [CommRing R]` with an abstract bar
involution `σ : R →+* R`; no archimedean construct, no `ℝ`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-31-berezinian-selfadjoint-crossterm-bar-even.md
-/
import QOU.QBeta.ZBarParity

namespace QOU.QBeta.BerezinianSelfAdjointCrossTerm

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- **The graded-self-adjoint Berezinian cross-term is bar-EVEN.** If the odd
off-diagonal blocks are bar-conjugate (`C = −σ B`, the graded-self-adjointness
condition) and the even inverse-block `Dinv` is bar-even (`σ Dinv = Dinv`), then the
scalar cross-term `t = B·Dinv·C = −B·Dinv·σB` satisfies `σ t = t` — it is bar-EVEN
(a `|B|²/D` norm-squared object), for **any** ring involution `σ` (`σ∘σ = id`). This
is the opposite of the `OddDecayWeightParity` assumption. -/
theorem selfadjoint_crossTerm_bar_even
    (B C Dinv : R) (hinv : ∀ x : R, σ (σ x) = x)
    (hC : C = -σ B) (hDinv : σ Dinv = Dinv) :
    σ (B * Dinv * C) = B * Dinv * C := by
  subst hC
  simp only [map_mul, map_neg, hDinv, hinv]
  ring

/-- **A bar-ODD cross-term forbids graded self-adjointness (modulo 2-torsion).**
Contrapositive of `selfadjoint_crossTerm_bar_even`: if the cross-term
`t = B·Dinv·C` is bar-ODD (`σ t = −t`, the parity `c₃` must have) with `Dinv`
bar-even, then the self-adjointness relation `C = −σ B` forces `2·t = 0`. So over a
2-torsion-free ring a **genuinely** bar-odd cross-term cannot arise from
bar-conjugate (self-adjoint) off-blocks — the off-diagonal blocks must be
independent. This is the constraint the odd-face `g·γ` model implicitly requires. -/
theorem barOdd_crossTerm_forbids_selfadjoint
    (B C Dinv : R) (hinv : ∀ x : R, σ (σ x) = x)
    (hDinv : σ Dinv = Dinv) (hC : C = -σ B)
    (hodd : σ (B * Dinv * C) = -(B * Dinv * C)) :
    2 * (B * Dinv * C) = 0 := by
  have heven := selfadjoint_crossTerm_bar_even σ B C Dinv hinv hC hDinv
  -- σ t = t (self-adjoint) and σ t = −t (bar-odd) ⇒ t = −t ⇒ 2t = 0
  rw [heven] at hodd
  linear_combination hodd

end QOU.QBeta.BerezinianSelfAdjointCrossTerm
