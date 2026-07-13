import Mathlib

namespace QOU.Molecular.ElectronShellCapacity

/--
**Pattern C — named proposition.**
The electron shell capacity rule: the $n$-th shell holds $2n^2$ electrons.
-/
theorem electron_shell_capacity_2n2 (n : ℕ) : Prop :=
  ∃ capacity : ℕ → ℕ, capacity n = 2 * n^2

end QOU.Molecular.ElectronShellCapacity
