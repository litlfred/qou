import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.CrossingEnergyBarParity

Which involution the words *bar-even* and *bar-odd* are computed against, for
the two crossing-energy channels.

## Context

`def:bar-involution` is the ring anti-involution on `H_n(q)` given by
`bar σᵢ = σᵢ⁻¹` and `bar q = q⁻¹`.  It has **two independently-applicable
halves**, and different corpus blocks silently apply different ones:

* the **coefficient half** `q ↦ q⁻¹`, holding the diagram fixed;
* the **diagram half** `σᵢ ↦ σᵢ⁻¹` — geometrically the mirror, exchanging
  positive and negative crossings, i.e. `p ↔ m`.

`obs:crossing-energy-decomposition` splits `E_cross = p·q - m·q⁻¹` into
`E_sym = (p - m)·cosh λ` and `E_asym = (p + m)·sinh λ`.  Its weights are
described by their parity under the coefficient half (`cosh` even, `sinh`
odd), while its item 2 describes the *channel totals* by their behaviour
under the mirror.  Those two descriptions disagree, which has read as an
error in one of them.

## What is proved here

Each channel, under each half and under the composite:

| | coefficient half | diagram half (mirror) | full involution |
|---|---|---|---|
| `eSym`  | even (`eSym_coef`)  | odd (`eSym_mirror`)  | odd (`eSym_bar`)  |
| `eAsym` | odd (`eAsym_coef`)  | even (`eAsym_mirror`) | odd (`eAsym_bar`) |

The two consequences that matter:

* `eSym_mirror` together with `eSym_coef` shows the disagreement is **not an
  error**: the same summand is coefficient-even and mirror-odd, because the
  mirror flips the multiplicity `p - m` as well as the weight.
* `bar_neg_of_both` — under the **full** involution, the one
  `def:bar-involution` actually defines, *both* channels are negated.  So the
  parity words do not distinguish the channels there; they distinguish them
  only against a named half.  This is why the notation register must name the
  half rather than say "bar" unqualified.

Multiplicities are taken in the coefficient ring rather than in `ℕ`, which is
both more general and avoids natural-number subtraction in `p - m`.

Base ring: a general `Field R` per AGENTS §7c — the content is purely
algebraic, needing only inverses and `2 ≠ 0` for the halving.  No ordering, no
`Real.sqrt`, no archimedean hypothesis; `λ = log q` and the reading of the
weights as `cosh`/`sinh` belong past the substrate wall and play no role in
any statement below.

Companion compute: `computations/bar_parity_involution_atlas_probe.py`
(witness `bar-parity-involution-atlas.witness.json`), which additionally
places the spin-involution sectors (grading D) on the coefficient half and
checks that the full involution fixes both Hecke idempotents (grading B).
-/

namespace QOU.BraidKnot

variable {R : Type*} [Field R]

/-- The bar-even crossing weight `cosh λ = (q + q⁻¹)/2 = [2]_q/2`. -/
noncomputable def coshW (q : R) : R := (q + q⁻¹) / 2

/-- The bar-odd crossing weight `sinh λ = (q - q⁻¹)/2 = h/2`. -/
noncomputable def sinhW (q : R) : R := (q - q⁻¹) / 2

/-- The symmetric channel total `E_sym = (p - m)·cosh λ`. -/
noncomputable def eSym (p m q : R) : R := (p - m) * coshW q

/-- The antisymmetric channel total `E_asym = (p + m)·sinh λ`. -/
noncomputable def eAsym (p m q : R) : R := (p + m) * sinhW q

/-- The crossing energy `E_cross = p·q - m·q⁻¹`. -/
noncomputable def eCross (p m q : R) : R := p * q - m * q⁻¹

/-- The two channels reconstruct the crossing energy exactly. -/
theorem eSym_add_eAsym (p m q : R) (h2 : (2 : R) ≠ 0) :
    eSym p m q + eAsym p m q = eCross p m q := by
  unfold eSym eAsym eCross coshW sinhW
  field_simp
  ring

/-- The bar-even weight is fixed by the coefficient half `q ↦ q⁻¹`. -/
theorem coshW_coef (q : R) : coshW q⁻¹ = coshW q := by
  unfold coshW
  rcases eq_or_ne q 0 with rfl | hq
  · simp
  · rw [inv_inv]; ring

/-- The bar-odd weight is negated by the coefficient half `q ↦ q⁻¹`. -/
theorem sinhW_coef (q : R) : sinhW q⁻¹ = -sinhW q := by
  unfold sinhW
  rcases eq_or_ne q 0 with rfl | hq
  · simp
  · rw [inv_inv]; ring

/-- **Coefficient half, symmetric channel: even.**  Holding the diagram
fixed, `q ↦ q⁻¹` fixes `E_sym`. -/
theorem eSym_coef (p m q : R) : eSym p m q⁻¹ = eSym p m q := by
  unfold eSym; rw [coshW_coef]

/-- **Coefficient half, antisymmetric channel: odd.** -/
theorem eAsym_coef (p m q : R) : eAsym p m q⁻¹ = -eAsym p m q := by
  unfold eAsym; rw [sinhW_coef]; ring

/-- **Diagram half (mirror), symmetric channel: odd.**  Exchanging positive
and negative crossings negates `E_sym`.

Together with `eSym_coef` this is the apparent double inversion: the same
summand is coefficient-*even* and mirror-*odd*, because the mirror flips the
multiplicity `p - m` as well as the weight.  Neither block is wrong; they
report parity under different halves. -/
theorem eSym_mirror (p m q : R) : eSym m p q = -eSym p m q := by
  unfold eSym; ring

/-- **Diagram half (mirror), antisymmetric channel: even.** -/
theorem eAsym_mirror (p m q : R) : eAsym m p q = eAsym p m q := by
  unfold eAsym; ring

/-- **Full involution, symmetric channel: odd.** -/
theorem eSym_bar (p m q : R) : eSym m p q⁻¹ = -eSym p m q := by
  rw [eSym_coef, eSym_mirror]

/-- **Full involution, antisymmetric channel: odd.** -/
theorem eAsym_bar (p m q : R) : eAsym m p q⁻¹ = -eAsym p m q := by
  rw [eAsym_coef, eAsym_mirror]

/-- **The full bar involution does not separate the two channels: it negates
both.**

Hence "bar-even" and "bar-odd" cannot be read against `def:bar-involution`
itself — against that involution the two channels have the *same* parity.
The words are meaningful only relative to a named half, which is what the
notation-register disambiguation records. -/
theorem bar_neg_of_both (p m q : R) :
    eSym m p q⁻¹ = -eSym p m q ∧ eAsym m p q⁻¹ = -eAsym p m q :=
  ⟨eSym_bar p m q, eAsym_bar p m q⟩

/-- Consequently the full involution negates the crossing energy itself. -/
theorem eCross_bar (p m q : R) : eCross m p q⁻¹ = -eCross p m q := by
  unfold eCross
  rcases eq_or_ne q 0 with rfl | hq
  · simp
  · rw [inv_inv]; ring

/-- Adding the crossing energy to its bar-involution image cancels to zero (`qou-jjge`). -/
theorem eCross_bar_add_eq_zero (p m q : R) :
    eCross m p q⁻¹ + eCross p m q = 0 := by
  rw [eCross_bar p m q, neg_add_cancel]

end QOU.BraidKnot
