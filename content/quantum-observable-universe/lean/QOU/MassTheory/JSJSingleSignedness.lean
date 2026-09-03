/-
# Single-signedness of a JSJ-volume-sourced binding term

**The hinge of the #5817-vs-#5812 adjudication.**

`conj:jsj-decomposition-linearity` sources a term from the JSJ decomposition of
the atomic knot complement, as a sum of piece volumes. Hyperbolic volume is
non-negative, so any such term is a sum of non-negative pieces.

`docs/audits/2026-08-26-faddeev-niemi-qh34-verdict.md` excludes, scope-(b), any
**non-negative** functional as the source of a **mixed-sign** residual — the
same shape as the Option-E PROBE-4 KL-positivity prune.

These files establish the step that connects them: a JSJ-sourced term is
single-signed, and a single-signed family cannot agree pointwise with a
sign-changing one. Whether the residual actually *is* mixed-sign is a separate,
measured question — and it is **form-dependent**: measured over the four
committed binding forms, `B_sym` and `B_law` give mixed signs while `B_lin` and
`B_magic` do not (`bsym-residual-sign-form-dependence.witness.json`). So these
theorems say *if* the target is mixed-sign *then* JSJ cannot supply it; they do
not assert the antecedent.

Base ring per AGENTS.md §7c: generic `LinearOrderedAddCommGroup`, never `ℝ`.
Ordering is genuinely required (the whole content is about signs); no
archimedean construct is used, so no specialisation to `ℝ` is warranted.
-/
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Order.Monotone.Basic
import Mathlib.Algebra.Order.Group.Int

namespace QOU.MassTheory

variable {ι κ : Type*} {R : Type*}
  [AddCommGroup R] [PartialOrder R] [IsOrderedAddMonoid R]

omit [IsOrderedAddMonoid R] in
/-- A family that is non-negative everywhere cannot agree pointwise with a
family that takes a strictly negative value somewhere. This is the abstract
content of the KL-positivity prune and of the Faddeev–Niemi verdict alike. -/
theorem nonneg_ne_of_neg {c t : ι → R} (hc : ∀ i, 0 ≤ c i)
    {i : ι} (hi : t i < 0) : ∃ k, c k ≠ t k := by
  refine ⟨i, fun h => ?_⟩
  have h0 : (0 : R) ≤ c i := hc i
  rw [h] at h0
  exact absurd (lt_of_lt_of_le hi h0) (lt_irrefl _)

/-- A JSJ-sourced quantity is a finite sum of piece volumes. Hyperbolic volume
is non-negative, so the sum is. -/
theorem jsj_sum_nonneg {s : Finset κ} {vol : κ → R}
    (h : ∀ i ∈ s, 0 ≤ vol i) : 0 ≤ ∑ i ∈ s, vol i :=
  Finset.sum_nonneg h

/-- **The hinge, volume side.** A term sourced from a per-isotope JSJ sum of
non-negative piece volumes cannot reproduce a residual that is strictly
negative at any isotope — hence cannot reproduce a sign-changing residual. -/
theorem jsj_cannot_match_negative
    {s : ι → Finset κ} {vol : ι → κ → R} {t : ι → R}
    (hvol : ∀ a, ∀ i ∈ s a, 0 ≤ vol a i)
    {a : ι} (ha : t a < 0) :
    ∃ k, (∑ i ∈ s k, vol k i) ≠ t k :=
  nonneg_ne_of_neg (fun k => Finset.sum_nonneg (hvol k)) ha

/-- **The hinge, transport side.** Binding is read off the carrier volume
through an *antitone* map: more volume in the bound state means more mass and
therefore *less* binding. So a non-negative volume addition contributes
non-positively to the binding — single-signed, with the sign flipped. -/
theorem antitone_volume_gives_nonpos_binding
    {B : R → R} (hB : Antitone B) {V dV : R} (hdV : 0 ≤ dV) :
    B (V + dV) ≤ B V :=
  hB (le_add_of_nonneg_right hdV)

/-- Monotone transport, for the opposite sign convention. Together with
`antitone_volume_gives_nonpos_binding` this is the point: under **either**
monotonicity direction the JSJ contribution is single-signed, so the exclusion
does not depend on which convention the framework uses — only on the map being
monotone at all. -/
theorem monotone_volume_gives_nonneg_binding
    {B : R → R} (hB : Monotone B) {V dV : R} (hdV : 0 ≤ dV) :
    B V ≤ B (V + dV) :=
  hB (le_add_of_nonneg_right hdV)

/-- The non-vacuity witness the §3b-tax discipline asks for: the hypotheses are
satisfiable, and the conclusion is not automatic. A constant-zero volume family
is non-negative, and a residual that is strictly negative somewhere then
genuinely differs from it. -/
example : ∃ (c t : ℤ → ℤ), (∀ i, 0 ≤ c i) ∧ t 0 < 0 ∧ ∃ k, c k ≠ t k :=
  ⟨fun _ => 0, fun _ => -1, fun _ => le_refl 0, by decide,
   nonneg_ne_of_neg (i := 0) (fun _ => le_refl 0) (by decide : (-1 : ℤ) < 0)⟩

-- Axiom audit: every declaration above must rest only on Lean's three
-- standard axioms — no `sorryAx`.
#print axioms QOU.MassTheory.nonneg_ne_of_neg
#print axioms QOU.MassTheory.jsj_sum_nonneg
#print axioms QOU.MassTheory.jsj_cannot_match_negative
#print axioms QOU.MassTheory.antitone_volume_gives_nonpos_binding
#print axioms QOU.MassTheory.monotone_volume_gives_nonneg_binding

end QOU.MassTheory
