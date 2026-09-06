/-
  Hoefsmit binding amplitude b² = [3]_q / [2]_q².

  The off-diagonal element of the Hoefsmit seminormal matrix for
  the standard representation (2,1) of H₃(q). This controls the
  entanglement between the two lepton channels inside the meson.

  Base ring (CLAUDE.md §7c): generic `{R : Type*} [CommRing R]` with
  the modulus carried as a unit `q : Rˣ`. Every declaration below is
  q-deformation combinatorics — `q ± q⁻¹` and the quantum integers
  `[2]_q` / `[3]_q` — and each identity is a single
  `linear_combination` against `q.mul_inv : ↑q * ↑q⁻¹ = 1`. Nothing
  here uses an ordering, a radical, or any other archimedean construct,
  so the statements live strictly on the substrate side of the wall;
  the `.md` records the same fact ("exact in q, independent of the
  substrate parameter").

  In particular the square root that appears in the Hoefsmit
  off-diagonal is **deliberately avoided**: the amplitude enters only
  through its defining quadratic relation `b² · [2]_q² = [3]_q`, so no
  radical — and hence no ℝ — is needed. `binding_amplitude_iff` states
  that relation and its de-entanglement partner `(1 − b²) · [2]_q² = 1`
  division-free, over any commutative ring.

  A field is used only in the `RatioForm` section, where the two
  quotient presentations quoted in the narrative (`b² = [3]_q/[2]_q²`
  and `1 − b² = 1/[2]_q²`) are recovered. Specialise with `(R := ℝ)` at
  the archimedean evaluation site if a numerical value is ever needed.

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- The Hecke deformation parameter h = q - q⁻¹. -/
def hecke_h : R := (q : R) - (↑q⁻¹ : R)

/-- The quantum integer [2]_q = q + q⁻¹. -/
def qInt2 : R := (q : R) + (↑q⁻¹ : R)

/-- The quantum integer [3]_q = q² + 1 + q⁻². -/
def qInt3 : R := (q : R) ^ 2 + 1 + (↑q⁻¹ : R) ^ 2

/-- **Bridge to the canonical balanced bracket** for the `[2]_q` shorthand.

The canonical `qIntBal` is a guarded division and stays over a field; this is
where the unit-valued shorthand above meets it. -/
theorem qInt2_eq_canonical {S : Type*} [Field S] (q : Sˣ)
    (h : (q : S) - (q : S)⁻¹ ≠ 0) :
    qInt2 q = QOU.QInteger.qIntBal (q : S) 2 := by
  unfold qInt2
  rw [QOU.QInteger.qIntBal_two (q : S) h, Units.val_inv_eq_inv_val]

/-- **Bridge to the canonical balanced bracket** for the `[3]_q` shorthand.

Over a field the field-valued form needed `q ≠ 0` on top of `q − q⁻¹ ≠ 0`: the
middle term of `q² + 1 + q⁻²` is `1 = q·q⁻¹`, which is `0` rather than `1` at
`q = 0` under Lean's `0⁻¹ = 0`.  Carrying `q` as a **unit** discharges that
hypothesis at the type level, so only the denominator guard survives. -/
theorem qInt3_eq_canonical {S : Type*} [Field S] (q : Sˣ)
    (h : (q : S) - (q : S)⁻¹ ≠ 0) :
    qInt3 q = QOU.QInteger.qIntBal (q : S) 3 := by
  unfold qInt3
  rw [QOU.QInteger.qIntBal_three (q : S) q.ne_zero h, Units.val_inv_eq_inv_val]

/-- Key identity: [2]_q² = h² + 4.
  Proof: (q+q⁻¹)² = q² + 2 + q⁻² = (q-q⁻¹)² + 4 = h² + 4. -/
theorem qInt2_sq_eq_h_sq_plus_4 :
    (qInt2 q) ^ 2 = (hecke_h q) ^ 2 + 4 := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  unfold qInt2 hecke_h
  linear_combination (4 : R) * h

/-- Key identity: [3]_q = [2]_q² - 1.
  Proof: q² + 1 + q⁻² = (q+q⁻¹)² - 1. -/
theorem qInt3_eq_qInt2_sq_minus_one :
    qInt3 q = (qInt2 q) ^ 2 - 1 := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  unfold qInt3 qInt2
  linear_combination (-2 : R) * h

/-- **The Hoefsmit binding amplitude relation, division-free.**

  The amplitude `b` is defined by `b² = [3]_q / [2]_q²`; written
  multiplicatively that is `b² · [2]_q² = [3]_q`, which needs no
  division and no radical. This theorem says it is *equivalent* to the
  de-entanglement form `(1 − b²) · [2]_q² = 1` — i.e. `1 − b² = 1/[2]_q²`
  — over any commutative ring, with no non-vanishing hypotheses.

  This is the central structural identity connecting the meson binding
  topology to the q-integer tower. -/
theorem binding_amplitude_iff (b : R) :
    b ^ 2 * (qInt2 q) ^ 2 = qInt3 q ↔ (1 - b ^ 2) * (qInt2 q) ^ 2 = 1 := by
  constructor
  · intro hb
    linear_combination -hb - qInt3_eq_qInt2_sq_minus_one q
  · intro hb
    linear_combination -hb - qInt3_eq_qInt2_sq_minus_one q

/-! ## Ratio presentations (a field is needed only to divide)

The narrative quotes the amplitude as the quotient `[3]_q / [2]_q²`.
A quotient needs division, so these two — and only these two — are
stated over a field; both follow from `qInt3_eq_qInt2_sq_minus_one`. -/

section RatioForm

variable {K : Type*} [Field K] (q : Kˣ)

/-- The Hoefsmit binding amplitude identity:
  b² = [3]_q / [2]_q² = 1 - 1/[2]_q². -/
theorem hoefsmit_b_sq_eq_q3_over_q2sq (hq2 : qInt2 q ≠ 0) :
    qInt3 q / (qInt2 q) ^ 2 = 1 - 1 / (qInt2 q) ^ 2 := by
  have h2 : (qInt2 q) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  rw [qInt3_eq_qInt2_sq_minus_one, sub_div, div_self h2]

/-- The de-entanglement fraction: 1 - b² = 1/[2]_q². -/
theorem de_entanglement_fraction (hq2 : qInt2 q ≠ 0) :
    1 - qInt3 q / (qInt2 q) ^ 2 = 1 / (qInt2 q) ^ 2 := by
  rw [hoefsmit_b_sq_eq_q3_over_q2sq q hq2]
  ring

end RatioForm

/-! ## Where the amplitude vanishes — the non-semisimple locus

The corpus already carries `b² = [3]_q/[2]_q²` (above) and, separately, the
Wenzl/Schur-element semisimplicity machinery (`QOU.SchurWeyl.HeckeSemisimpleReal`,
`QOU.MathlibExt.WenzlSchurElement`).  **Nothing linked them.**  These three
lemmas do, arithmetically: they pin the vanishing locus of the Hoefsmit coupling
to the cyclotomic condition `q⁶ = 1, q² ≠ 1` — the classical point where
`H₃(q)` stops being semisimple.

Added 2026-09-06 because a merged probe (#6889) read `b² = 0` as "degenerate"
and used it to exclude phases from a search.  It is not a degeneracy of the
construction; it is the locus where the Wedderburn decomposition the whole
`tr = Σ_λ y_λ χ^λ` machinery rests on ceases to exist.

**Scope.** These are the ARITHMETIC half only.  They do not prove
non-semisimplicity — that needs the Schur-element criterion, which the corpus
carries elsewhere.  What they establish is that `b²` vanishes exactly at the
cyclotomic points, so a probe finding `b² = 0` has found a root of unity, not a
defect. -/

section VanishingLocus

variable {K : Type*} [Field K] (q : Kˣ)

/-- **The amplitude vanishes exactly when `[3]_q` does** (given `[2]_q ≠ 0`). -/
theorem hoefsmit_b_sq_eq_zero_iff (hq2 : qInt2 q ≠ 0) :
    qInt3 q / (qInt2 q) ^ 2 = 0 ↔ qInt3 q = 0 := by
  rw [div_eq_zero_iff]
  simp [pow_eq_zero_iff, hq2]

/-- `[3]_q = 0` is the cyclotomic condition `q⁴ + q² + 1 = 0`.
    (`qInt3 q = q² + 1 + q⁻²`, so multiply through by `q²`.) -/
theorem qInt3_eq_zero_iff_cyclotomic :
    qInt3 q = 0 ↔ (q : K) ^ 4 + (q : K) ^ 2 + 1 = 0 := by
  have hq : (q : K) ≠ 0 := q.ne_zero
  have hinv : (↑q⁻¹ : K) = (q : K)⁻¹ := by
    simp [Units.val_inv_eq_inv_val]
  unfold qInt3
  rw [hinv]
  constructor
  · intro h
    field_simp at h
    linear_combination h
  · intro h
    field_simp
    linear_combination h

/-- **The vanishing locus is a sixth root of unity.**  `q⁶ - 1 = (q² - 1)(q⁴ + q² + 1)`,
    so `[3]_q = 0` forces `q⁶ = 1`. -/
theorem q_pow_six_eq_one_of_qInt3_eq_zero (h : qInt3 q = 0) : (q : K) ^ 6 = 1 := by
  have hc : (q : K) ^ 4 + (q : K) ^ 2 + 1 = 0 :=
    (qInt3_eq_zero_iff_cyclotomic q).mp h
  linear_combination ((q : K) ^ 2 - 1) * hc

/-- …and it is a PRIMITIVE one: `q² = 1` is incompatible with `[3]_q = 0`,
    since there `q⁴ + q² + 1 = 3`.  (Needs `3 ≠ 0` in `K`.) -/
theorem q_sq_ne_one_of_qInt3_eq_zero (h3 : (3 : K) ≠ 0) (h : qInt3 q = 0) :
    (q : K) ^ 2 ≠ 1 := by
  intro hq2
  have hc : (q : K) ^ 4 + (q : K) ^ 2 + 1 = 0 :=
    (qInt3_eq_zero_iff_cyclotomic q).mp h
  apply h3
  have h4 : (q : K) ^ 4 = 1 := by
    have : (q : K) ^ 4 = ((q : K) ^ 2) ^ 2 := by ring
    rw [this, hq2, one_pow]
  linear_combination hc - h4 - hq2

end VanishingLocus

end QOU.BraidsAndKnots
