import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Order.Group.Nat
import Mathlib.Algebra.Group.Nat.Even
import Mathlib.Algebra.Ring.Parity


/-!
# QOU.Archimedean.nuclear_spin_parity — Nuclear spin parity from A mod 2

The nuclear spin quantum number J is integral when A is even and
half-integral when A is odd.  This follows from each nucleon being
a spin-½ fermion (single-component knot) and the tensor product
decomposition of SU_q(2) representations.

LaTeX label: `prop:nuclear-spin-parity`

## References
- [leitner2026] §6/nuclear-spin-parity
-/

namespace QOU.Archimedean

/-- A nucleus has integer or half-integer spin determined by A mod 2. -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
inductive SpinParity where
  | integer     -- J ∈ ℤ (bosonic nucleus)
  | halfInteger -- J ∈ ℤ + ½ (fermionic nucleus)
deriving DecidableEq, Repr

/-- The spin parity of a nucleus with mass number A. -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
def nuclearSpinParity (A : ℕ) : SpinParity :=
  if A % 2 = 0 then SpinParity.integer else SpinParity.halfInteger

/-- Even A gives integer spin (bosonic). -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
theorem nuclear_spin_parity_even {A : ℕ} (h : Even A) :
    nuclearSpinParity A = SpinParity.integer := by
  unfold nuclearSpinParity
  simp [Nat.even_iff.mp h]

/-- Odd A gives half-integer spin (fermionic). -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
theorem nuclear_spin_parity_odd {A : ℕ} (h : Odd A) :
    nuclearSpinParity A = SpinParity.halfInteger := by
  unfold nuclearSpinParity
  simp [Nat.odd_iff.mp h]

/-- ¹⁴N has integer spin. -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
example : nuclearSpinParity 14 = SpinParity.integer := by decide

/-- ³H has half-integer spin. -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
example : nuclearSpinParity 3 = SpinParity.halfInteger := by decide

/-- ⁴He has integer spin. -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
example : nuclearSpinParity 4 = SpinParity.integer := by decide

/-- Adding one nucleon (beta decay preserves A) preserves spin parity.
    Requires `1 ≤ n` (β⁻ decay consumes one neutron; with truncated
    `ℕ`-subtraction the statement is false at `n = 0`). -/
-- Ref: [leitner2026] §6/nuclear-spin-parity
theorem beta_decay_preserves_spin_parity (p n : ℕ) (hn : 1 ≤ n) :
    nuclearSpinParity (p + n) = nuclearSpinParity ((p + 1) + (n - 1)) := by
  have h : p + n = (p + 1) + (n - 1) := by omega
  rw [h]

end QOU.Archimedean
