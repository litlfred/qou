import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# Agreement between admissible functionals forces the element's class

`qou-99qc`, Option E (*derive a different element `Δ` for an admissible
functional to act on*), formalize-first.

## Why this lemma is the narrowing

Option E is dangerous to attack numerically. A functional on `H₃(q)` is
surjective, so a free `Δ` reproduces **any** target and the search is a
six-parameter fit against one anchor. Two structural facts prune it:

* under convention D the admissible **traces** span a `2`-dimensional space
  (`qbeta_admissible_functional_hierarchy_probe`, 13/13), so an admissible
  evaluation of `Δ` sees it only through the pair `(χ_(3)(Δ), χ_(2,1)(Δ))` —
  six unknowns collapse to **two**;
* nothing selects a point of that `2`-dimensional space, so a prediction that
  depends on the choice depends on an unfixed convention.

Demanding that two independent admissible functionals return the **same** value
is therefore two equations in those two unknowns. This file proves such a
system has a unique solution: **the class of `Δ` is forced, not fitted**, which
is what would make Option E a derivation rather than a search.

## What this does NOT claim

Functional-independence is a **posited** requirement, not a theorem of the
framework. The honest objection: the augmentation and the Markov trace are
different measurements, and nothing compels a physical quantity to be invariant
under exchanging them, any more than the trace and determinant of an operator
must agree. What the lemma buys is that the requirement is *falsifiable and
cheap* — it names one class, and one then checks whether a legitimate
braid-word difference realises it, instead of searching.

Nothing here evaluates `Q_β`, fixes a convention, or proposes a `c_k`.
-/

namespace QOU.QBeta.AdmissibleAgreement

variable {K : Type*} [Field K]

/-- **Two independent functionals agreeing on a value pin the pair uniquely.**

Read `(x, y)` as `(χ_(3)(Δ), χ_(2,1)(Δ))`, the only data an admissible trace
sees; `(a₁, b₁)`, `(a₂, b₂)` as two admissible functionals in that basis; `T` as
the target `Q_β / E₀`. The hypothesis is exactly linear independence of the two
functionals — measured to hold for the augmentation and `tr_M` at `z_D`
(`rank {aug, tr_D} = 2`).

The element's class is therefore **determined**, not chosen: no residual freedom
survives to absorb an anchor, which is what separates this from the
one-parameter weight fit `qou-99qc` refuses. -/
theorem agreement_determines_class
    (a₁ b₁ a₂ b₂ T : K) (hdet : a₁ * b₂ - a₂ * b₁ ≠ 0) :
    ∃! p : K × K, a₁ * p.1 + b₁ * p.2 = T ∧ a₂ * p.1 + b₂ * p.2 = T := by
  -- Explicit rewrites rather than `field_simp`: the latter renormalises the
  -- determinant to a different spelling on each goal and then cannot discharge
  -- its own denominator.
  refine ⟨(T * (b₂ - b₁) / (a₁ * b₂ - a₂ * b₁),
           T * (a₁ - a₂) / (a₁ * b₂ - a₂ * b₁)), ⟨?_, ?_⟩, ?_⟩
  · rw [← mul_div_assoc, ← mul_div_assoc, ← add_div, div_eq_iff hdet]
    ring
  · rw [← mul_div_assoc, ← mul_div_assoc, ← add_div, div_eq_iff hdet]
    ring
  · rintro ⟨x, y⟩ ⟨h₁, h₂⟩
    have hx : x * (a₁ * b₂ - a₂ * b₁) = T * (b₂ - b₁) := by
      linear_combination b₂ * h₁ - b₁ * h₂
    have hy : y * (a₁ * b₂ - a₂ * b₁) = T * (a₁ - a₂) := by
      linear_combination a₁ * h₂ - a₂ * h₁
    have hx' : x = T * (b₂ - b₁) / (a₁ * b₂ - a₂ * b₁) := eq_div_of_mul_eq hdet hx
    have hy' : y = T * (a₁ - a₂) / (a₁ * b₂ - a₂ * b₁) := eq_div_of_mul_eq hdet hy
    simp [hx', hy']

/-- **The augmentation-anchored form.** The augmentation *is* `χ_(3)`, so in this
basis it is the covector `(1, 0)`; independence then reduces to `b₂ ≠ 0`, i.e.
the other functional must carry a genuine `(2,1)` component.

The forced class is then `χ_(3)(Δ) = T` — the augmentation alone fixes the first
coordinate — with the second determined by how far the other functional departs
from the augmentation on the trivial block. -/
theorem augmentation_agreement_forces
    (a₂ b₂ T x y : K) (hb : b₂ ≠ 0) :
    ((1 : K) * x + 0 * y = T ∧ a₂ * x + b₂ * y = T)
      ↔ (x = T ∧ y = T * (1 - a₂) / b₂) := by
  constructor
  · rintro ⟨h₁, h₂⟩
    have hx : x = T := by simpa using h₁
    subst hx
    refine ⟨rfl, ?_⟩
    rw [eq_div_iff hb]
    linear_combination h₂
  · rintro ⟨hx, hy⟩
    subst hx
    subst hy
    refine ⟨by ring, ?_⟩
    rw [mul_div_cancel₀ _ hb]
    ring

/-- **THE SHARP FORM: the whole normalised admissible family agrees on `x` iff
`x` is a scalar modulo the radical.**

Both candidate functionals are *normalised* (`ε(1) = 1`): the augmentation is
`χ_(3)`, and `tr_M` at `z_D` decomposes as `α·χ_(3) + β·χ_(2,1)` with
`α + 2β = 1` — verified symbolically, `α = (q⁴+1)/(q²+1)²`, `β = q²/(q²+1)²`.
Since `χ_(3)(1) = 1` and `χ_(2,1)(1) = dim V_(2,1) = 2`, that line **is** the
normalised admissible family, and it is one-parameter.

Writing `a = χ_(3)(x)` and `b = χ_(2,1)(x)`, a normalised admissible trace gives
`(1 - 2β)·a + β·b`. This is independent of `β` — i.e. **every** normalised
admissible trace returns the same value, not merely the two named ones —
exactly when `b = 2a`.

That condition is `χ_λ(x) / dim V_λ` equal across both surviving blocks, which
says precisely that **`x` is a scalar in the semisimple quotient**: for `x = c·1`
one has `χ_λ(x) = c · dim V_λ`. So the requirement "the answer must not depend on
which admissible functional is used" is not an arbitrary extra condition — it is
the statement that `Δ` is central-scalar modulo the radical, and it determines
the common value to be `χ_(3)(Δ)`.

**Consequence for `qou-99qc`.** `Δ_S` has `χ_(2,1)(Δ_S) = 0` exactly over `ℚ(q)`
while `χ_(3)(Δ_S) = (1-q⁴)/(2q²) ≠ 0`, so `b = 2a` fails. `Δ_S` is **not** a
scalar modulo the radical, and no admissible-functional choice can make the
Q-value independent of that choice. -/
theorem normalised_agreement_iff_scalar (a b : K) :
    (∀ β : K, (1 - 2 * β) * a + β * b = a) ↔ b = 2 * a := by
  constructor
  · intro h
    linear_combination h 1
  · rintro rfl β
    ring

/-- The common value, when the scalar condition holds, is the trivial-block
coordinate — so the augmentation reads it off directly. -/
theorem normalised_common_value (a b β : K) (hb : b = 2 * a) :
    (1 - 2 * β) * a + β * b = a := by
  subst hb; ring

/-- **Degeneracy is exactly dependence, and it is not a technicality.** If the
second functional is a multiple of the first, the two equations are one, and the
solution set is a *line*: two distinct points satisfy it, so nothing is pinned.

Recorded so the independence hypothesis of `agreement_determines_class` is not
read as a convenience — it carries the entire content. Concretely: were `tr_M`
at `z_D` proportional to the augmentation, Option E's narrowing would evaporate
and the element would again be a fit. -/
theorem dependent_functionals_do_not_determine
    (a₁ T c : K) (ha : a₁ ≠ 0) :
    ¬ ∃! p : K × K, a₁ * p.1 + 0 * p.2 = T ∧ (c * a₁) * p.1 + (c * 0) * p.2 = c * T := by
  rintro ⟨p, -, huniq⟩
  have h0 : ((T / a₁, (0 : K)) : K × K) = p := by
    refine huniq _ ⟨?_, ?_⟩ <;> (field_simp; try ring)
  have h1 : ((T / a₁, (1 : K)) : K × K) = p := by
    refine huniq _ ⟨?_, ?_⟩ <;> (field_simp; try ring)
  have : ((T / a₁, (0 : K)) : K × K) = (T / a₁, 1) := h0.trans h1.symm
  simpa using this

end QOU.QBeta.AdmissibleAgreement
