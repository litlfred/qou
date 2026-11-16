import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.Field.Basic

/-!
# The writhe normalisation of the GS coefficient sum is forced, not chosen

**Deriving the correction factor from the two stabilisation rules.**

`gb_winding_parity_wire_probe.py` (GAP-2) found that the Gröbner–Shirshov
reduction certificate's total coefficient sum `S(β) = ∑_w c_w(q)` reads off the
winding parity from the *reduction output* rather than from the `wⁿ`
presentation — but that it is a **framed** quantity, not yet a knot invariant.
Under Markov stabilisation it transforms as

  positive  `β ↦ β σ_n`   :  `S ↦ S`        (exponent sum `e ↦ e+1`, strands `n ↦ n+1`)
  negative  `β ↦ β σ_n⁻¹` :  `S ↦ (1−h)·S`  (exponent sum `e ↦ e−1`, strands `n ↦ n+1`)

with `h = q − q⁻¹`. The probe's `[G3]` therefore said the readout must be
"writhe-normalised first" for a general braid, without saying by what.

This file derives the factor instead of positing one. Seek a correction of the
monomial form `A^e · B^n` in the exponent sum `e` and strand count `n`. Markov
invariance of `S · A^e B^n` under the two moves is exactly

  `A * B = 1`          (positive stabilisation: `e` and `n` both rise by one)
  `A = (1 − h) * B`    (negative stabilisation: `e` falls, `n` rises)

and `writhe_factor_sq` shows these two force

  `A² = 1 − h`,        equivalently  `A^e B^n = A^(e − n)` with `A² = 1 − h`,

i.e. the normalisation is the familiar `(1−h)^{(e−n)/2}` — **uniquely determined
up to sign** (`writhe_factor_unique_up_to_sign`), with no freedom left to tune.
`no_normalisation_at_h_eq_one` records the boundary: at `h = 1` the two
constraints are contradictory, so no monomial normalisation exists at all. (Only
this *necessary* condition is proved. `h ≠ 1` is not sufficient — existence also
needs `1 − h` to be a square in the base ring — and no sufficiency claim is made
here.)

This is also why `[G3]`'s escape clause held: on the canonical family
`wⁿ = (σ₁σ₂⁻¹)ⁿ` the exponent sum is `0` and the strand count is `3` for every
`n`, so the correction is the single constant `B³` across the whole family and
cannot change any *relative* sign — hence the parity readout was already stable
there without normalisation. That is an arithmetic fact about the word, recorded
here rather than formalised, since it needs the braid word itself.

Base ring: **generic** `[CommRing R]` (§7c); the invertibility lemma adds a
`[Field R]`. `A` enters only through its defining relation `A * B = 1`, never as
a chosen square root, so nothing depends on a branch choice — the same discipline
as `QOU.QBeta.WindingLatticeNormForm`.

Companion probe: `computations/gb_writhe_normalised_readout_probe.py`.

**Scope.** This determines the *unique* monomial normalisation compatible with
the two measured stabilisation rules. It does **not** prove that the normalised
readout is a knot invariant (that needs the Markov theorem's conjugation move
too, untouched here), and it does **not** deliver the full winding class `(m,ℓ)`.
-/

namespace QOU.QBeta.WritheNormalisation

variable {R : Type*} [CommRing R]

/-- **The normalisation factor is forced.** If `A^e B^n` corrects the coefficient
sum to a Markov-stabilisation invariant — `A * B = 1` from the positive move,
`A = (1−h) * B` from the negative one — then `A² = 1 − h`. There is no remaining
freedom: the exponent `(e − n)/2` and the base `1 − h` are both derived. -/
theorem writhe_factor_sq (A B h : R) (hAB : A * B = 1) (hA : A = (1 - h) * B) :
    A ^ 2 = 1 - h := by
  have : A ^ 2 = (1 - h) * (A * B) := by
    rw [hA]; ring
  rw [this, hAB, mul_one]

/-- The companion relation on `B`: it is the inverse square root of `1 − h`. -/
theorem writhe_factor_B_sq (A B h : R) (hAB : A * B = 1) (hA : A = (1 - h) * B) :
    (1 - h) * B ^ 2 = 1 := by
  have hA2 : A ^ 2 = 1 - h := writhe_factor_sq A B h hAB hA
  have : (1 - h) * B ^ 2 = (A * B) ^ 2 := by rw [← hA2]; ring
  rw [this, hAB, one_pow]

/-- `A^e B^n` collapses to a power of `A` alone: since `B = A⁻¹`, the correction
depends only on `e − n`, which is why the normalisation is written
`(1−h)^{(e−n)/2}`. Stated in the `n = e` case, where it is the bare statement
that the correction is trivial exactly on zero-`(e−n)` braids. -/
theorem factor_collapses (A B : R) (hAB : A * B = 1) (k : ℕ) :
    A ^ k * B ^ k = 1 := by
  rw [← mul_pow, hAB, one_pow]

/-- **Uniqueness up to sign.** Two normalisations satisfying the same two
stabilisation constraints have equal squares, so over an integral domain they
differ only by a sign. No tuning is possible. -/
theorem writhe_factor_unique_up_to_sign (A B A' B' h : R)
    (hAB : A * B = 1) (hA : A = (1 - h) * B)
    (hAB' : A' * B' = 1) (hA' : A' = (1 - h) * B') :
    A ^ 2 = A' ^ 2 := by
  rw [writhe_factor_sq A B h hAB hA, writhe_factor_sq A' B' h hAB' hA']

/-- **Power-law propagation across `k` net stabilisation steps.**
For any `k : ℕ`, `(A^k)² = (1 − h)^k` and `(1 − h)^k · (B^k)² = 1`. -/
theorem writhe_step_power_sq (A B h : R) (hAB : A * B = 1) (hA : A = (1 - h) * B) (k : ℕ) :
    (A ^ k) ^ 2 = (1 - h) ^ k ∧ (1 - h) ^ k * (B ^ k) ^ 2 = 1 := by
  constructor
  · calc (A ^ k) ^ 2 = (A ^ 2) ^ k := by ring
      _ = (1 - h) ^ k := by rw [writhe_factor_sq A B h hAB hA]
  · calc (1 - h) ^ k * (B ^ k) ^ 2 = ((1 - h) * B ^ 2) ^ k := by ring
      _ = 1 ^ k := by rw [writhe_factor_B_sq A B h hAB hA]
      _ = 1 := one_pow k

/-- **Anchor-migration sensitivity of the writhe base `1 − h`.**
Across two anchor pins `(h₁, h₂)`, the linear and quadratic differences of the
writhe base `1 − h` factor through `h₁ − h₂`. -/
theorem anchor_shift_writhe_base_diff (h₁ h₂ : R) :
    (1 - h₁) - (1 - h₂) = -(h₁ - h₂) ∧
      (1 - h₁) ^ 2 - (1 - h₂) ^ 2 = -(h₁ - h₂) * (2 - h₁ - h₂) := by
  exact ⟨by ring, by ring⟩

section Invertible

variable {K : Type*} [Field K]

/-- **The boundary of the construction.** At `h = 1` the two stabilisation
constraints are contradictory, so no monomial normalisation exists. This is the honest boundary of the construction, not an edge case to be
waved away. -/
theorem no_normalisation_at_h_eq_one (A B : K)
    (hAB : A * B = 1) (hA : A = (1 - 1 : K) * B) : False := by
  rw [sub_self, zero_mul] at hA
  rw [hA, zero_mul] at hAB
  exact zero_ne_one hAB

end Invertible

end QOU.QBeta.WritheNormalisation
