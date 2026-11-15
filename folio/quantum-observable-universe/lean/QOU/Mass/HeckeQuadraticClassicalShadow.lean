import QOU.Mass.HeckeStokesEigenvalues
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

/-!
# The classical shadow of the Hecke quadratic is a reflection

Step-2 option **B** of
`docs/audits/2026-09-06-step-2-plan-hecke-monodromy.md` (cheat-sheet §2a: the monodromy quadratic
`F(σ) = σ² − (q − q⁻¹)σ − 1`, historically called a curvature 2-form, is *stipulated* for the
substrate connection, not computed; for the 𝔰𝔩₂ KZ connection on two points it is derived in
`QOU.Mass.KohnoTwoPoint.kzExchange_quad`).

**B — the order-zero shadow is derived.** The probe
`computations/probes/colour_cubic_branch_monodromy_probe.py` continues the three roots of the
colour cubic around each of its six simple branch points and finds a **transposition** every time
(Picard–Lefschetz), the six generating `S₃` with identity product. On the two colliding roots a
transposition is the swap `S = [[0,1],[1,0]]`, an involution with eigenvalues `±1`. This file records
the algebra that makes that the `q = 1` shadow of Step 2:

* `hecke_quadratic_at_one` — `X² − (1 − 1⁻¹)X − 1 = (X − 1)(X + 1)`: the Hecke quadratic at
  `q = 1` is the minimal polynomial of a reflection;
* `swap_sq`, `swap_satisfies_hecke_at_one` — the swap is an involution and satisfies that
  quadratic; `swap_eigen_one`, `swap_eigen_neg_one` — its eigenvectors, so the two Stokes/Hecke
  eigenvalues `q, −q⁻¹` of `stokes_curvature_factors` specialise to `+1, −1` on the swap;
* `Equiv.swap` on `Fin 3` squares to the identity (`transposition_sq`) — the monodromy element
  itself, as a permutation of the three roots.

So the relation Step 2 stipulates is, at `q = 1`, a theorem about branch-point monodromy; what
remains stipulated is exactly the deformation `1 ↦ q`.

The archimedean companion (option C's prune: a unit-modulus KZ eigenvalue is never the real pin
`q₀`) lives in `QOU/Mass/KZUnitModulusPrune.lean`, split off per §7c.

Base ring §7c: everything here is over a generic field `K` (matrix and polynomial identities).

-- Ref: [leitner2026] computations/probes/colour_cubic_branch_monodromy_probe.py
-- Ref: [kohno1987] Kohno, *Monodromy representations of braid groups and Yang–Baxter equations*,
--      Ann. Inst. Fourier 37 (1987) — KZ monodromy factors through the Hecke algebra.
-- Ref: [leitner2026] docs/canonical-derivation-cheat-sheet.md §2a
-/

namespace QOU.Mass.HeckeQuadraticClassicalShadow

open Matrix

section Shadow

variable {K : Type*} [Field K]

/-- The Hecke quadratic `X² − (q − q⁻¹)X − 1` at `q = 1` is `(X − 1)(X + 1)`: the minimal
polynomial of a reflection. (The `q ≠ 0` factorisation `stokes_curvature_factors` specialised.) -/
theorem hecke_quadratic_at_one (X : K) :
    X ^ 2 - ((1 : K) - (1 : K)⁻¹) * X - 1 = (X - 1) * (X + 1) := by
  simpa using QOU.Mass.HeckeStokes.stokes_curvature_factors (1 : K) one_ne_zero X

/-- The swap of the two colliding roots at a simple branch point. -/
def swap : Matrix (Fin 2) (Fin 2) K := !![0, 1; 1, 0]

/-- A transposition is an involution: `S² = 1`. -/
theorem swap_sq : (swap : Matrix (Fin 2) (Fin 2) K) * swap = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [swap, Matrix.mul_apply, Fin.sum_univ_two]

/-- The swap satisfies the Hecke quadratic at `q = 1`: `S² − (1 − 1⁻¹)S − 1 = 0`. -/
theorem swap_satisfies_hecke_at_one :
    (swap : Matrix (Fin 2) (Fin 2) K) * swap - ((1 : K) - (1 : K)⁻¹) • swap - 1 = 0 := by
  rw [swap_sq]; simp

/-- Eigenvector for the eigenvalue `+1` (the symmetric channel `L₊` at `q = 1`). -/
theorem swap_eigen_one : (swap : Matrix (Fin 2) (Fin 2) K).mulVec ![1, 1] = (1 : K) • ![1, 1] := by
  ext i; fin_cases i <;> simp [swap, Matrix.mulVec, dotProduct]

/-- Eigenvector for the eigenvalue `−1` (the antisymmetric channel `L₋` at `q = 1`). -/
theorem swap_eigen_neg_one :
    (swap : Matrix (Fin 2) (Fin 2) K).mulVec ![1, -1] = (-1 : K) • ![1, -1] := by
  ext i; fin_cases i <;> simp [swap, Matrix.mulVec, dotProduct]

/-- The monodromy element itself, as a permutation of the three roots: a transposition squares
to the identity. -/
theorem transposition_sq (i j : Fin 3) : Equiv.swap i j * Equiv.swap i j = 1 :=
  Equiv.swap_mul_self i j

end Shadow


end QOU.Mass.HeckeQuadraticClassicalShadow
