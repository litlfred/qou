/-
# The D(u) closed-form law: which factor is convention-dependent, and where
  the two frames agree

Bean `qou-cxon`; adjudicates `qou-iayk`. Audit:
`docs/audits/2026-08-23-d-u-closed-form-is-convention-c.md`.
Probe: `computations/markov/d_frame_closed_form_law_probe.py`.

The landed atomic-braid law is

    D_C(u) = 2^(2A+1) · u^(18Z+21N+1) · (1+u²)^(3A−1)

and the measured convention-D law (exact per atom, `markov_peel.tr_M_atomic`)

    D_D(u) = 6·2^(2A+1) · u^(12Z+20N+14) · (1+u⁴)^(A+2Z−1)

`d_u_closed_form_proof.py:18` writes the Markov parameter as
`z = 1/(q^(1/2) + q^(-1/2))`, and derives the `(1+u²)` factor by clearing
that `z`'s denominator. `zC_spelling_eq` below is the reason that spelling is
**convention C** and not something else — it is the detector-blind form
catalogued in #5124. So the landed law encodes C *structurally*, which is why
convention-D output appears to contradict it.

WHAT IS AND IS NOT PROVED HERE. The `z` identities are theorems. The exponent
*agreement characterisations* are theorems about the two stated formulas. The
formulas themselves are NOT proved here: the per-atom denominators they come
from are exact, but their `(Z,N)` closed forms are three-parameter fits over
four atoms (one degree of validation each). This file therefore proves things
*about* the fits; it does not upgrade them to derivations. See the audit.

§7c: generic `Field`, no `ℝ`. The C spelling needs a square root of `q`, which
is supplied as a hypothesis `s^2 = q` rather than by `Real.sqrt`, so nothing
here crosses the substrate→archimedean wall.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta

variable {K : Type*} [Field K]

/-- **The detector-blind convention-C spelling.**

`1/(s + s⁻¹) = s/(q+1)` whenever `s² = q`. Writing `s` for `√q`, the
left-hand side is `d_u_closed_form_proof.py:18`'s
`z = 1/(q^(1/2) + q^(-1/2))` and the right-hand side is `√q/(q+1)` = `z_C`.

This is the identity that makes a grep for the convention-C *form* miss the
landed proof, and it is the load-bearing step of the `qou-iayk`
adjudication. -/
theorem zC_spelling_eq {s q : K} (hs : s ≠ 0) (hq : s ^ 2 = q)
    (hq1 : q + 1 ≠ 0) : (s + s⁻¹)⁻¹ = s / (q + 1) := by
  subst hq
  have hsum : s + s⁻¹ = (s ^ 2 + 1) / s := by field_simp
  rw [hsum, inv_div]

/-- **The two frames clear genuinely different denominators.**

At `q = u²` convention C's `z` is `u/(1+u²)` and convention D's is
`u⁶/(1+u⁴)`. The landed law's cyclotomic factor is the *first* denominator
cleared once per Markov peel, so the only way it survives the convention
change is if the two denominators coincide — and they do not, for any `u`
outside `{0, ±1}`.

An earlier draft of this file stated the C form as `u/(u²+1) = u/(u²+1)`,
which is `rfl` and says nothing. This is the non-vacuous statement it was
reaching for. -/
theorem clearedDenom_C_ne_D (u : K) (hu : u ≠ 0) (hu1 : u ^ 2 ≠ 1) :
    u ^ 2 + 1 ≠ u ^ 4 + 1 := by
  intro h
  -- No order on a general `Field`, so this is cancellation, not `linarith`.
  have h2 : u ^ 2 = u ^ 4 := add_right_cancel h
  have hne : u ^ 2 ≠ 0 := pow_ne_zero 2 hu
  apply hu1
  have hfac : u ^ 2 * (u ^ 2 - 1) = 0 := by linear_combination -h2
  rcases mul_eq_zero.mp hfac with h3 | h3
  · exact absurd h3 hne
  · exact sub_eq_zero.mp h3

/-- Convention D at `q = u²`: `z_D = u⁶/(1+u⁴)`.

The cleared factor is `(1+u⁴)`, **not** `(1+u²)` — so the landed law's
cyclotomic base cannot survive the convention change. -/
theorem zD_at_usq (u : K) :
    ((u ^ 2) ^ 3) / (((u ^ 2) ^ 2) + 1) = u ^ 6 / (u ^ 4 + 1) := by
  congr 1 <;> ring

/-! ### The exponents, and where the two frames agree -/

/-- Cyclotomic exponent of the landed convention-C law: `3A − 1`. -/
def cycloExpC (Z N : ℤ) : ℤ := 3 * (Z + N) - 1

/-- Cyclotomic exponent measured in convention D: `A + 2Z − 1`. -/
def cycloExpD (Z N : ℤ) : ℤ := (Z + N) + 2 * Z - 1

/-- `u`-exponent of the landed convention-C law: `18Z + 21N + 1`. -/
def uExpC (Z N : ℤ) : ℤ := 18 * Z + 21 * N + 1

/-- `u`-exponent measured in convention D: `12Z + 20N + 14`. -/
def uExpD (Z N : ℤ) : ℤ := 12 * Z + 20 * N + 14

/-- **Convention C is blind to the proton/neutron distinction, and this says
exactly how.**

The two cyclotomic exponents agree **iff `N = 0`** — i.e. only on
pure-proton configurations. Under C every nucleon contributes 3; under D a
proton contributes 3 and a neutron 1, so the frames coincide precisely when
there are no neutrons. -/
theorem cycloExp_agree_iff (Z N : ℤ) :
    cycloExpC Z N = cycloExpD Z N ↔ N = 0 := by
  unfold cycloExpC cycloExpD
  constructor <;> intro h <;> linarith

/-- The two `u`-exponents agree **iff `6Z + N = 13`** (equivalently
`A + 5Z = 13`).

This is a codimension-1 line in `(Z,N)`, not a coincidence — see
`helium3_unique_uExp_agreement` for why one atom appeared to satisfy the
C-frame law exactly while its mass-3 partner did not. -/
theorem uExp_agree_iff (Z N : ℤ) :
    uExpC Z N = uExpD Z N ↔ 6 * Z + N = 13 := by
  unfold uExpC uExpD
  constructor <;> intro h <;> linarith

/-- The same line in the `(A, Z)` coordinates the law is usually written in. -/
theorem uExp_agree_iff_A (Z N : ℤ) :
    uExpC Z N = uExpD Z N ↔ (Z + N) + 5 * Z = 13 := by
  rw [uExp_agree_iff]; constructor <;> intro h <;> linarith

/-- **³He is the unique light atom where the two `u`-exponents agree.**

`qou-iayk` recorded that ³He matched the convention-C exponent exactly
(58 = 58) while its mass-3 partner tritium was off by 5, and read the
irregularity as evidence the fresh values were incoherent. They are not:
`(Z,N) = (2,1)` is simply the one point with `N ≤ 2` lying on the agreement
line `6Z + N = 13`.

The bound on `Z` is not needed: `N ≤ 2` alone forces `6Z ∈ {11,12,13}`, hence
`Z = 2`. Stated without it, since carrying a hypothesis the proof does not use
would overstate what the result requires. -/
theorem helium3_unique_uExp_agreement (Z N : ℕ) (hN : N ≤ 2) :
    (6 * Z + N = 13) ↔ (Z = 2 ∧ N = 1) := by
  omega

/-- The deuteron is *not* on the agreement line — the frames genuinely differ
there, by the `+6` recorded in `qou-iayk`. -/
theorem deuteron_uExp_differs : uExpC 1 1 ≠ uExpD 1 1 := by decide

/-- …and the gap is exactly the `−6` the bean recorded (C minus D). -/
theorem deuteron_uExp_gap : uExpC 1 1 - uExpD 1 1 = -6 := by decide

end QOU.QBeta
