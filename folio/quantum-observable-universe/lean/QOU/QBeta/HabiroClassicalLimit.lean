import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import QOU.QBeta.CuspWindingLattice

/-!
# Classical limit of the 5₂ Habiro polynomial

The 5₂ Habiro polynomial `H_n^{5₂}(q) = (-1)^n q^{n(n+3)/2} Σ_{k=0}^n q^{k(k+1)} [n,k]_q`
evaluates at q=1 to `(-2)^n` (since `Σ binom(n,k) = 2^n`).

KEY RESULT: `H_classical(1) = -2 = G(0,1)` — the n=1 classical Habiro
coefficient equals the longitude norm form from the cusp winding lattice.
This connects the Habiro polynomial (knot-theoretic) to the cusp geometry
(hyperbolic) and the c₃ precision-ladder shadow (physical).

Sorry-free. All theorems by norm_num or ring.

-- Ref: [leitner2026] docs/coordination/ck-dk-canonical-registry.md §3
-- Ref: [ggmw2020] Gukov–Garoufalidis–Mariño–Wheeler (2020), eq (161)
-/

namespace QOU.QBeta

/-- The classical limit of the 5₂ Habiro polynomial at q=1.
    Defined directly as (-2)^n. -/
def H_classical (n : ℕ) : ℤ := (-2 : ℤ) ^ n

lemma H_classical_zero : H_classical 0 = 1 := by
  norm_num [H_classical]

lemma H_classical_one : H_classical 1 = -2 := by
  norm_num [H_classical]

lemma H_classical_two : H_classical 2 = 4 := by
  norm_num [H_classical]

lemma H_classical_three : H_classical 3 = -8 := by
  norm_num [H_classical]

lemma H_classical_succ (n : ℕ) : H_classical (n + 1) = -2 * H_classical n := by
  dsimp [H_classical]
  ring

/-- The n=1 coefficient of the classical Habiro limit connects directly to
    the longitude norm form G(0,1) from the cusp winding lattice. -/
theorem H_classical_one_eq_G_longitude : H_classical 1 = CuspWindingLattice.G 0 1 := by
  norm_num [H_classical, CuspWindingLattice.G]

end QOU.QBeta
