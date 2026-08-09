/-
  Hoefsmit binding amplitude b² = [3]_q / [2]_q².

  The off-diagonal element of the Hoefsmit seminormal matrix for
  the standard representation (2,1) of H₃(q). This controls the
  entanglement between the two lepton channels inside the meson.

  Base ring (CLAUDE.md §7c): generic `{R : Type*} [Field R]`. Every
  declaration below is q-deformation combinatorics — `q ± q⁻¹`, the
  quantum integers `[2]_q` / `[3]_q`, and three identities discharged
  by `field_simp` + `ring`. Nothing here uses an ordering, a radical,
  or any other archimedean construct, so the statements live strictly
  on the substrate side of the wall; the `.md` records the same fact
  ("exact in q, independent of the substrate parameter"). Specialise
  with `(R := ℝ)` at the archimedean evaluation site if a numerical
  value is ever needed.

  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.BraidsAndKnots

variable {R : Type*} [Field R] (q : R)

/-- The Hecke deformation parameter h = q - q⁻¹. -/
def hecke_h : R := q - q⁻¹

/-- The quantum integer [2]_q = q + q⁻¹. -/
def qInt2 : R := q + q⁻¹

/-- The quantum integer [3]_q = q² + 1 + q⁻². -/
def qInt3 : R := q^2 + 1 + q⁻¹^2

/-- **Bridge to the canonical balanced bracket** for the `[2]_q` shorthand. -/
theorem qInt2_eq_canonical (h : q - q⁻¹ ≠ 0) :
    qInt2 q = QOU.QInteger.qIntBal q 2 :=
  (QOU.QInteger.qIntBal_two q h).symm

/-- **Bridge to the canonical balanced bracket** for the `[3]_q` shorthand —
and it needs one hypothesis more than `[2]_q` does.

`q ≠ 0` is not boilerplate here: the middle term of `q² + 1 + q⁻²` is `1 = q·q⁻¹`,
which is `0` rather than `1` when `q = 0` under Lean's `0⁻¹ = 0`.  So the
longhand and the canonical bracket agree *away from the degenerate locus*, not
everywhere — the distinction a body swap would have buried. -/
theorem qInt3_eq_canonical (hq : q ≠ 0) (h : q - q⁻¹ ≠ 0) :
    qInt3 q = QOU.QInteger.qIntBal q 3 :=
  (QOU.QInteger.qIntBal_three q hq h).symm

/-- Key identity: [2]_q² = h² + 4.
  Proof: (q+q⁻¹)² = q² + 2 + q⁻² = (q-q⁻¹)² + 4 = h² + 4. -/
theorem qInt2_sq_eq_h_sq_plus_4 (hq : q ≠ 0) :
    (qInt2 q)^2 = (hecke_h q)^2 + 4 := by
  unfold qInt2 hecke_h
  field_simp
  ring

/-- Key identity: [3]_q = [2]_q² - 1.
  Proof: q² + 1 + q⁻² = (q+q⁻¹)² - 1. -/
theorem qInt3_eq_qInt2_sq_minus_one (hq : q ≠ 0) :
    qInt3 q = (qInt2 q)^2 - 1 := by
  unfold qInt3 qInt2
  field_simp
  ring

/-- The Hoefsmit binding amplitude identity:
  b² = [3]_q / [2]_q² = 1 - 1/[2]_q².

  This is the central structural identity connecting the meson
  binding topology to the q-integer tower. -/
theorem hoefsmit_b_sq_eq_q3_over_q2sq (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    qInt3 q / (qInt2 q)^2 = 1 - 1 / (qInt2 q)^2 := by
  rw [qInt3_eq_qInt2_sq_minus_one q hq]
  field_simp

/-- The de-entanglement fraction: 1 - b² = 1/[2]_q². -/
theorem de_entanglement_fraction (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    1 - qInt3 q / (qInt2 q)^2 = 1 / (qInt2 q)^2 := by
  rw [qInt3_eq_qInt2_sq_minus_one q hq]
  field_simp
  ring

end QOU.BraidsAndKnots
