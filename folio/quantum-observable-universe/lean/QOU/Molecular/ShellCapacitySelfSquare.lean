import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.Molecular.ShellCapacitySelfSquare — orbital shell capacity `2n²` as a self-square

Formalises the **capacity** leg of the electron-shell program: principal shell
`n` holds `2n²` electrons, and this count is the *self-square* of the angular
`q`-dimension evaluated at `q = 1`,

  `2 n² = 2 [n]_q² |_{q=1}`,   `[n]_q² = ∑_{ℓ=0}^{n-1} [2ℓ+1]_q`  (q-Clebsch–Gordan).

At `q = 1` the angular `q`-dimension `[2ℓ+1]_q` degenerates to the classical
sub-shell multiplicity `2ℓ+1`, so the categorical self-square reduces to the
elementary identity `∑_{ℓ<n} (2ℓ+1) = n²` (sum of the first `n` odd numbers),
doubled by the spin factor `2`.  The full `q`-deformed self-square
(`[n]_q = U_{n-1}((q+q⁻¹)/2)`, the bar-even Chebyshev evaluation) is verified
symbolically in `computations/shell_capacity_chebyshev_bridge.py`; the present
file proves, sorry-free, the `q = 1` integer specialisation on which the
periodic-table shell capacities `[2, 8, 18, 32]` rest.

**No second `SU(2)`.** The `SO(4) = SU(2) × SU(2)` `(j,j)` "doubling" is here the
self-fusion `V ⊗ V` of *one* angular object — the second factor a copy of the
first, tied by the coproduct — vindicating the owner's "we don't need a second
`SU(2)`".

This is the **derived** leg of the program (audit
`docs/audits/2026-06-20-electron-shell-program-synthesis.md` §1).  The *ordering*
(Aufbau / Madelung) leg is an open derivation target and is deliberately **not**
formalised as an accepted input.
-/

namespace QOU.Molecular

/-- **Orbital count of principal shell `n` is `n²`.**  The number of orbital
    sub-states in shell `n` is the sum of the sub-shell multiplicities `2ℓ+1`
    over `ℓ = 0, …, n-1` — the sum of the first `n` odd numbers.  This is the
    `q → 1` value of the angular `q`-dimension self-square `[n]_q²`. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-capacity-self-square.md
theorem orbital_n_squared (n : ℕ) :
    ∑ l ∈ Finset.range n, (2 * l + 1) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih => rw [Finset.sum_range_succ, ih]; ring

/-- **Shell capacity as a self-square.**  Principal shell `n` holds `2n²`
    electrons: the spin factor `2` times the orbital count
    `n² = ∑_{ℓ<n} (2ℓ+1)`.  Equivalently the bar-even self-square `2[n]_q²`
    evaluated at `q = 1`.  The doubling is the self-fusion of one angular object,
    not a product of two `SU(2)` factors. -/
-- Ref: [manuscript] quantum-observable-universe/molecular-construction/shell-capacity-self-square.md
theorem shell_capacity_self_square (n : ℕ) :
    ∑ l ∈ Finset.range n, 2 * (2 * l + 1) = 2 * n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih => rw [Finset.sum_range_succ, ih]; ring

end QOU.Molecular
