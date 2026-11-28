import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.EightfoldWay.MarkovTraceKeepsBothChannels — convention D does not pick a two-strand channel

`HeckeSignChannelIsFermi` shows that Fermi exchange is the `-q⁻¹` channel of the two-strand
braiding, and leaves open which channel matter takes. This module tests whether the Markov
trace picks one.

On `H₂(q) = span{1, σ}` with `σ² = (q - q⁻¹)σ + 1`, the channel idempotents are
`p₊ = (σ + q⁻¹)/(q + q⁻¹)` (eigenvalue `q`) and `p₋ = (q - σ)/(q + q⁻¹)` (eigenvalue `-q⁻¹`).
A Markov trace with parameter `z` has `tr 1 = 1`, `tr σ = z`, so on `a + bσ` it is `a + b z`.

* `trace_sign_eq_zero_iff` — `tr_z p₋ = 0` iff `z = q`: only the augmentation trace kills the
  sign (Fermi) channel.
* `trace_sym_eq_zero_iff` — `tr_z p₊ = 0` iff `z = -q⁻¹`.
* `zD_trace_sign`, `zD_trace_sym` — at convention D, `z_D = q³/(q² + 1)`, the weights are
  `q²/(q² + 1)²` and `(q⁴ + q² + 1)/(q² + 1)²`.
* `zD_keeps_both` — for `q ≠ 0`, `q² + 1 ≠ 0`, `q⁴ + q² + 1 ≠ 0`, both weights are nonzero.

So convention D keeps both channels and does not choose between them. This is a scope-(a)
negative: it says the Markov trace at `z_D` does not supply the choice, not that no
construction does. The one trace that does kill a channel, the augmentation `z = q`, kills
the Fermi channel, which is the opposite of what matter needs.

Base ring: a generic field `K` (§7c). No empirical input.
-/

namespace QOU.EightfoldWay.MarkovTraceKeepsBothChannels

variable {K : Type*} [Field K]

/-- Markov trace with parameter `z` on `a + b σ ∈ H₂(q)`. -/
def tr (z a b : K) : K := a + b * z

/-- `tr_z p₋`, with `p₋ = (q - σ)/(q + q⁻¹)`. -/
def trSign (q z : K) : K := tr z (q / (q + q⁻¹)) (-1 / (q + q⁻¹))

/-- `tr_z p₊`, with `p₊ = (σ + q⁻¹)/(q + q⁻¹)`. -/
def trSym (q z : K) : K := tr z (q⁻¹ / (q + q⁻¹)) (1 / (q + q⁻¹))

/-- Convention D. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

private theorem two_ne {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : q + q⁻¹ ≠ 0 := by
  intro h
  apply h2
  have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
  rw [← this, h, mul_zero]

theorem trace_sign_eq_zero_iff {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (z : K) :
    trSign q z = 0 ↔ z = q := by
  have hs := two_ne hq h2
  unfold trSign tr
  constructor
  · intro h
    have h' : (q - z) / (q + q⁻¹) = 0 := by rw [← h]; ring
    have : q - z = 0 := (div_eq_zero_iff.mp h').resolve_right hs
    linear_combination -this
  · rintro rfl
    field_simp
    ring

theorem trace_sym_eq_zero_iff {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (z : K) :
    trSym q z = 0 ↔ z = -q⁻¹ := by
  have hs := two_ne hq h2
  unfold trSym tr
  constructor
  · intro h
    have h' : (q⁻¹ + z) / (q + q⁻¹) = 0 := by rw [← h]; ring
    have : q⁻¹ + z = 0 := (div_eq_zero_iff.mp h').resolve_right hs
    linear_combination this
  · rintro rfl
    field_simp
    ring

theorem zD_trace_sign {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trSign q (zD q) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have hs := two_ne hq h2
  unfold trSign tr zD
  field_simp
  ring

theorem zD_trace_sym {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    trSym q (zD q) = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hs := two_ne hq h2
  unfold trSym tr zD
  field_simp
  ring

/-- Convention D gives both two-strand channels nonzero weight. -/
theorem zD_keeps_both {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    trSign q (zD q) ≠ 0 ∧ trSym q (zD q) ≠ 0 := by
  rw [zD_trace_sign hq h2, zD_trace_sym hq h2]
  exact ⟨div_ne_zero (pow_ne_zero 2 hq) (pow_ne_zero 2 h2),
    div_ne_zero h4 (pow_ne_zero 2 h2)⟩

/-- The two weights sum to `1` for every `z` (the trace of `p₊ + p₋ = 1`). -/
theorem trSign_add_trSym {q : K} (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (z : K) :
    trSign q z + trSym q z = 1 := by
  have hs := two_ne hq h2
  unfold trSign trSym tr
  field_simp
  ring

end QOU.EightfoldWay.MarkovTraceKeepsBothChannels
