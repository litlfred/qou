import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.Card

/-!
# QOU.Mass.prolongation_fixed_depth_recurrence — existence half of the keystone

The keystone (`conj:qdifference-kernel-prolongation-symbol`) splits into
EXISTENCE (a fixed-depth recurrence on the prolonged periods exists) and
IDENTIFICATION (its kernel is the Bring Picard–Fuchs operator). This file
**proves the existence half.**

The prolonged Seiberg–Witten periods are orbits `a n = φ (Mⁿ v₀)` of the
jet-prolongation operator `M` on the finite-rank Gauss–Manin period space.
Being finite-rank, `M` satisfies a degree-`d` polynomial relation (its
characteristic polynomial — Cayley–Hamilton): `M^d = Σ_{j<d} c_j • M^j`.
The theorem below shows this forces the **operator** recurrence
`M^{n+d} = Σ_{j<d} c_j • M^{n+j}` for every `n`, with the SAME
`n`-independent kernel `c`. Applying any linear functional `φ(· v₀)` to both
sides (one use of `map_sum`/`map_smul`) yields the scalar period recurrence
`a(n+d) = Σ_{j<d} c_j · a(n+j)` — the fixed-depth recurrence the keystone
asserts. Only the explicit `d` and `c` (the Bring PF operator) remain open.

LaTeX label: `prop:prolonged-periods-fixed-depth`.

**Ground ring**: generic `[CommRing R]`. See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

open scoped BigOperators

variable {R : Type*} [CommRing R] {V : Type*} [AddCommGroup V] [Module R V]

/-- **Existence half of the keystone.** If the prolongation operator `M`
satisfies the depth-`d` polynomial relation `M^d = Σ_{j<d} c_j • M^j`
(Cayley–Hamilton on the finite-rank period space), then its powers obey the
depth-`d` linear recurrence `M^{n+d} = Σ_{j<d} c_j • M^{n+j}` for every `n`,
with the SAME `n`-independent kernel. Hence so does every period orbit. -/
-- Ref: [leitner2026] §mass-theory/prolonged-periods-fixed-depth
theorem prolongation_fixed_depth_recurrence
    (M : Module.End R V) (d : ℕ) (c : Fin d → R)
    (hCH : (M ^ d) = ∑ j : Fin d, c j • (M ^ (j : ℕ))) (n : ℕ) :
    (M ^ (n + d)) = ∑ j : Fin d, c j • (M ^ (n + (j : ℕ))) := by
  rw [pow_add, hCH, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun j _ => ?_)
  rw [mul_smul_comm, ← pow_add]

end QOU.Mass
