import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-!
# QOU.QBeta.SilverAnchorGrounding

**Categorical grounding of the Q_β silver-ratio anchor.** From the single
defining relation of the silver ratio `q² − 2q − 1 = 0` (`q = 1 + √2`) this file
proves the two structural facts the existing silver-anchored `c_k` work *assumed*
but never derived:

1. **The silver locus is the Q_A decay-prefactor zero.** The substrate-branch
   `Q_A` numerator factor `2q + 1 − q²` equals `−(q² − 2q − 1)`, so it vanishes
   exactly on the silver locus. Hence `F = Q_β / [Q_A · cos α_eff]` has its
   **pole** there — this is the "categorical derivation of `Q_A·cos α_eff`'s
   zero" direction flagged as productive in
   `QOU.QBeta.RationalCoeffRecurrence`. That pole is the dominant
   `1/u_substrate` characteristic root of the `c_k` C-finite recurrence
   (`RationalCoeffRecurrence.pole_reciprocal_is_char_root`).

2. **Hoefsmit `b² = 7/8` at that same locus.** With the Hoefsmit value
   `b² = (q⁴ + q² + 1)/(q² + 1)²`, the silver relation forces
   `8·(q⁴ + q² + 1) = 7·(q² + 1)²`, i.e. `b² = 7/8`. The c_8/c_9/c_10 silver
   rationals in `QOU.QBeta.Cn_at_silver` (PR #1793) take `b² = 7/8` as a
   *premise*; this file derives it from the silver definition.

So the silver ratio is **one locus playing two roles**: the `Q_A` zero (the
F-pole fixing the `c_k` tail's characteristic root) and the `b² = 7/8` point
grounding the silver rungs. The algebraic content is the factorisation
`q⁴ − 6q² + 1 = (q² − 2q − 1)(q² + 2q − 1)` — the silver factor and its
bar-conjugate.

Pure algebra from `q² = 2q + 1`; stated over a generic `CommRing` per
CLAUDE.md §7c (no `ℝ`, no `√2` needed). The field form is added only for the
literal `b² = 7/8` ratio. This grounds — it does **not** make any `c_k ≥ 3`
canonical (the Pell–Lucas pattern still breaks at the free rungs; registry §8);
no `c_k` value is claimed here.

LaTeX label: `prop:qbeta-silver-anchor-grounding`

## References
- Silver-rung values grounded here: `QOU.QBeta.Cn_at_silver` (PR #1793);
  `docs/coordination/ck-dk-canonical-registry.md` (the c_8/c_9/c_10 row).
- F-pole ⇒ reciprocal characteristic root: `QOU.QBeta.RationalCoeffRecurrence`.
- `Q_A` substrate branch `(2q+1−q²)`: canonical chain Step 9 /
  `computations/free-neutron-decay.py`.
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-- **The silver locus is the `Q_A` decay-prefactor zero.** The substrate-branch
`Q_A` numerator factor `2q + 1 − q²` equals `−(q² − 2q − 1)`, so it vanishes
exactly when `q` satisfies the silver relation `q² − 2q − 1 = 0`. This is where
`F = Q_β/[Q_A·cos α_eff]` has its pole — the dominant `1/u_substrate`
characteristic root of the `c_k` recurrence. -/
theorem qA_numerator_zero_at_silver (q : R) (hsilver : q ^ 2 - 2 * q - 1 = 0) :
    2 * q + 1 - q ^ 2 = 0 := by
  linear_combination -hsilver

/-- **The defining factorisation** `q⁴ − 6q² + 1 = (q² − 2q − 1)(q² + 2q − 1)`:
the silver factor `q² − 2q − 1` and its bar-conjugate `q² + 2q − 1`. This is the
algebraic content behind the Hoefsmit `b²` identity below (it is the
`linear_combination` cofactor). -/
theorem silver_quartic_factor (q : R) :
    q ^ 4 - 6 * q ^ 2 + 1 = (q ^ 2 - 2 * q - 1) * (q ^ 2 + 2 * q - 1) := by
  ring

/-- **Hoefsmit `b²` numerator identity at the silver locus** (division-free,
generic `CommRing`). With `b² = (q⁴ + q² + 1)/(q² + 1)²` (Hoefsmit), the relation
`q² − 2q − 1 = 0` forces `8·(q⁴ + q² + 1) = 7·(q² + 1)²` — i.e. `b² = 7/8`. The
`linear_combination` certificate is the cofactor `(q² + 2q − 1)` of
`silver_quartic_factor`. -/
theorem hoefsmit_bSq_numerator_silver (q : R) (hsilver : q ^ 2 - 2 * q - 1 = 0) :
    8 * (q ^ 4 + q ^ 2 + 1) = 7 * (q ^ 2 + 1) ^ 2 := by
  linear_combination (q ^ 2 + 2 * q - 1) * hsilver

/-- **Hoefsmit `b² = 7/8` at the silver locus** (field form). Dividing the
division-free identity `hoefsmit_bSq_numerator_silver` by the nonzero `(q²+1)²`
gives the literal Hoefsmit ratio used by the silver-rung values. The denominator
nonvanishing holds at `q = 1+√2` (there `q²+1 = 2+2√2 ≠ 0`). -/
theorem hoefsmit_bSq_eq_at_silver {K : Type*} [Field K] [CharZero K] (q : K)
    (hsilver : q ^ 2 - 2 * q - 1 = 0) (hden : (q ^ 2 + 1) ^ 2 ≠ 0) :
    (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 = 7 / 8 := by
  rw [div_eq_div_iff hden (by norm_num : (8 : K) ≠ 0)]
  linear_combination (q ^ 2 + 2 * q - 1) * hsilver

end QOU.QBeta
