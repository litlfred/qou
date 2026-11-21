import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.BraidKnot.chirality_frobenius_self_pairing

Canonical Lean for content block
[`prop:chirality-from-frobenius-self-pairing`](../../../quantum-observable-universe/braids-and-knots/chirality-from-frobenius-self-pairing.md).

The `.md` derives the **amphichiral** case of the chirality factor
from the Fricke trace relation in `H_3(R, q)`: the figure-eight
character evaluates to `χ_{4_1}((2,1)) = 2 − [3]_q = −1 − h²`, from
which the chirality factor is `a_{4_1} = 1 − h²` (`h = q − q⁻¹` the
Hecke deformation, `[3]_q = q² + 1 + q⁻²` the balanced quantum
integer).

This file derives those identities **directly** over a generic commutative
ring `{R : Type*} [CommRing R]`, with the substrate parameter carried as a
**unit** `q : Rˣ` (§7c). Both `[3]_q = q² + 1 + q⁻²` and `h = q − q⁻¹` are
Laurent expressions in `q`: the only structure they need is that `q` be
invertible, which a `Units` element supplies by construction. So no field
is required, no `field_simp`, and no `q ≠ 0` side condition — each identity
is a `linear_combination` of the single defining unit relation `q · q⁻¹ = 1`.
The substrate evaluation at `q₀ ∈ ℝ` happens elsewhere, past the wall.

A previous encoding axiomatised the conclusion `χ = 1 − h²` as a class field
and projected it (`:= ctx.claim_chirality_factor`); that was a vacuous
self-assuming projection and is removed in favour of the genuine derivations
below.

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/chirality-from-frobenius-self-pairing.md
-/

-- Declarations here are nested one namespace deeper than `QOU.BraidKnot` so
-- this module and `QOU.BraidKnot.HoefsmitV21CosSymmetrization` can be
-- imported together: both declared `heckeH`, and Lean rejects the second
-- import with "environment already contains" (bean `qou-kfcl`).
--
-- They are the SAME quantity — the Hecke structure constant `q - q^-1` of
-- AGENTS.md §7a — at two ground rings: `(q : R)` over ℝ there, and the
-- generic `(q : Rˣ)` over a `CommRing` here. The generic one is the better
-- long-term home per §7c, but it has no importers while the ℝ one has three,
-- so the cheap move is to nest this side. Consolidating onto the generic
-- version is left to `qou-u87j`.
namespace QOU.BraidKnot.ChiralityFrobenius

variable {R : Type*} [CommRing R]

/-- The balanced quantum integer `[3]_q = q² + 1 + q⁻²`.

`q` is a unit of `R`, so `q⁻²` is the square of the `Units` inverse — a
division-free Laurent expression over `CommRing`, not a field inverse. -/
def qInt3 (q : Rˣ) : R := (q : R) ^ 2 + 1 + ((q⁻¹ : Rˣ) : R) ^ 2

/-- The Hecke deformation parameter `h = q − q⁻¹` (AGENTS.md §7a), again with
the inverse supplied by the unit structure. -/
def heckeH (q : Rˣ) : R := (q : R) - ((q⁻¹ : Rˣ) : R)

/-- **Bridge to the canonical bracket**, restated for the unit-valued `qInt3`.

The canonical `qIntBal` is a guarded division and so stays over a field; the
bridge is where this file meets it.  Of the two hypotheses the field-valued
form carried, `q ≠ 0` is now discharged by the `Units` structure, leaving
`q − q⁻¹ ≠ 0` — the genuine one, guarding the bracket's denominator — as the
only hypothesis. -/
theorem qInt3_eq_canonical {S : Type*} [Field S] (q : Sˣ)
    (h : (q : S) - (q : S)⁻¹ ≠ 0) :
    qInt3 q = QOU.QInteger.qIntBal (q : S) 3 := by
  unfold qInt3
  rw [QOU.QInteger.qIntBal_three (q : S) q.ne_zero h, Units.val_inv_eq_inv_val]

/-- **Figure-eight Fricke identity** (manuscript, amphichiral case).

The figure-eight character in the standard `(2,1)` representation of
`H_3(R, q)` is `χ_{4_1}((2,1)) = 2 − [3]_q`, and this equals `−1 − h²`
with `h = q − q⁻¹`. The identity is exactly `−2·(q·q⁻¹ − 1)`, i.e. a
multiple of the unit relation. -/
-- Ref: [leitner2026] prop:chirality-from-frobenius-self-pairing (Fricke trace relation in H_3)
theorem chirality_figure_eight_character (q : Rˣ) :
    2 - qInt3 q = -1 - heckeH q ^ 2 := by
  unfold qInt3 heckeH
  linear_combination (-2 : R) * q.mul_inv

/-- **Amphichiral chirality factor of the figure-eight** as a quantum
integer.

The manuscript's amphichiral chirality factor is `a_{4_1} = 1 − h²`.
Writing it through the balanced quantum integer `[3]_q`, the closed
form is `1 − h² = 4 − [3]_q` (since `[3]_q = q² + 1 + q⁻²` and
`h² = q² − 2 + q⁻²`). This is the normalisation-free algebraic face
of the chirality factor; like the Fricke identity it is a multiple of
the unit relation, here `+2·(q·q⁻¹ − 1)`. -/
-- Ref: [leitner2026] prop:chirality-from-frobenius-self-pairing (a_{4_1} = 1 − h²)
theorem chirality_amphichiral_via_qInt3 (q : Rˣ) :
    1 - heckeH q ^ 2 = 4 - qInt3 q := by
  unfold qInt3 heckeH
  linear_combination (2 : R) * q.mul_inv

end QOU.BraidKnot.ChiralityFrobenius
