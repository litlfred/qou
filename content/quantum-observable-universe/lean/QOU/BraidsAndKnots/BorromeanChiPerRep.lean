/-
  Borromean per-representation character: the standard-irrep character
  χ^{(2,1)}(β_Bor) — algebraic equivalence of its two published forms.

  The content proposition `prop:borromean-markov-trace-closed-form`
  (`borromean-markov-trace-closed-form.md` lines 101–110) records the
  standard (2-dimensional) irrep character of the Borromean braid in two
  forms:

      χ^{(2,1)}(β_Bor) = (−q¹² + 3q¹⁰ − 3q⁸ + 4q⁶ − 3q⁴ + 3q² − 1) / q⁶
                       = 2 − 3h⁴ − h⁶,      h = q − q⁻¹.

  This file proves the **algebraic equivalence of the two forms** (the
  q-rational equals the h-polynomial), which is a pure field identity
  (`field_simp; ring`).

  SCOPE / HONESTY.  This lemma proves the two *forms* agree.  It does NOT
  prove that the character of β_Bor *equals* this value — that fact (the
  per-representation decomposition `χ^{(3)} = χ^{(1³)} = 1`,
  `χ^{(2,1)} = 2 − 3h⁴ − h⁶`) is, at the time of writing, NARRATIVE-ONLY
  in the content `.md` (it requires the seminormal Hecke-representation
  machinery, not present in Lean).  It is independently CONFIRMED
  NUMERICALLY (≤ 4e-50) by `borromean_chi_independent_crosscheck.py`
  (PR #1947) against the skein-validated engine `homfly_ocneanu_trace`.
  See `docs/audits/2026-06-07-borromean-chi-crossmethod-proof-status.md`.

  Companion to `BorromeanMarkovTrace.lean`, which proves the *full*
  tr_M closed form `(4 + h² − 3h⁴ − h⁶)/(h² + 4)` (the standard irrep is
  the only one contributing the h⁴, h⁶ corrections).

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [murasugi1996] ISBN 978-0-8176-3817-7
-/
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum

namespace QOU.BraidsAndKnots

/- §7c base-ring convention: these are pure algebraic identities with no
   ordering and no `Real.*` constructs, so they are stated over a generic
   `{R : Type*} [Field R]` rather than specialised to `ℚ`. `Field` (not
   merely `CommRing`) is the weakest typeclass that admits the Kauffman
   Laurent's genuine inverses (`1/q`, negative `q`-powers). `ℚ` is a
   `Field`, so every existing call site still unifies. -/

/-- The standard-irrep Borromean character in its q-rational form. -/
def chi21_borromean_qform {R : Type*} [Field R] (q : R) : R :=
  (-q^12 + 3*q^10 - 3*q^8 + 4*q^6 - 3*q^4 + 3*q^2 - 1) / q^6

/-- The standard-irrep Borromean character in its h-polynomial form,
    `2 − 3h⁴ − h⁶` with `h = q − q⁻¹` (written `q − 1/q`). -/
def chi21_borromean_hform {R : Type*} [Field R] (q : R) : R :=
  2 - 3*(q - 1/q)^4 - (q - 1/q)^6

/-- **The two published forms of `χ^{(2,1)}(β_Bor)` are equal** for every
    non-zero `q` in any field. Pure field identity. -/
theorem chi21_borromean_qform_eq_hform {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    chi21_borromean_qform q = chi21_borromean_hform q := by
  unfold chi21_borromean_qform chi21_borromean_hform
  field_simp
  ring

/-- The h-form is purely even in `h = q − q⁻¹` (bar-invariant under
    `q ↦ q⁻¹`): replacing `q` by `q⁻¹` sends `h ↦ −h` and the even powers
    `h⁴, h⁶` are unchanged. Stated directly as invariance under `q ↦ 1/q`. -/
theorem chi21_borromean_hform_bar_invariant {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    chi21_borromean_hform (1 / q) = chi21_borromean_hform q := by
  have hq' : (1 : R) / q ≠ 0 := one_div_ne_zero hq
  unfold chi21_borromean_hform
  field_simp
  ring

end QOU.BraidsAndKnots
