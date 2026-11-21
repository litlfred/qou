import QOU.Archimedean.ParticleKnots
import QOU.BraidKnot.ElectronWordCandidates
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Archimedean.Electron — the braid word σ₀σ₁σ₀ ∈ B₃ (closure: Hopf link)

The electron is the braid word `σ₀σ₁σ₀ ∈ B₃` (owner ruling 2026-11-21), the
longest basis element of `H₃(q)`. Its closure is the positive Hopf link. The
trefoil braid `σ₀³ ∈ B₂`, which this file recorded until 2026-11-21, is the
documented backup.

LaTeX label: `def:electron-knot`

## References
- [kassel2008] Kassel & Turaev, Braid Groups, §2.2 (closure components = cycles
  of the underlying permutation)
- [leitner2026] Ch. 5, §electron-knot

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
-/

namespace QOU.Archimedean

open QOU.BraidKnot.ElectronWordCandidates

/-- The closure of the electron word `σ₀σ₁σ₀` on three strands has two
components: its permutation is a transposition. So the electron's closure is a
two-component link (the Hopf link), not a knot. The statement is falsifiable:
the word `σ₀σ₁σ₀σ₁` closes to one component (`numCycles_s0s1_sq`). -/
-- Ref: [kassel2008] §2.2
theorem electron_closure_two_components :
    numCycles (permOf ({} : Electron).braidLetters) = 2 :=
  numCycles_s0s1s0

/-- The closure of the positron word `σ₀⁻¹σ₁⁻¹σ₀⁻¹` also has two components
(the negative Hopf link): crossing signs do not change the permutation. -/
-- Ref: [kassel2008] §2.2
theorem positron_closure_two_components :
    numCycles (permOf ({} : Positron).braidLetters) = 2 :=
  numCycles_s0s1s0

end QOU.Archimedean
