import QOU.Infra.Polylogarithm
import QOU.Infra.DirichletL
import QOU.Infra.Clausen

/-!
# Cyclotomic Cl_n decomposes into Dirichlet L-values

Compiled formalisation of
`prop:cyclotomic-l-value-decomposition` from
`folio/quantum-observable-universe/braids-and-knots/cyclotomic-l-value-decomposition.md`.

The sibling docstub at
`braids-and-knots/cyclotomic-l-value-decomposition.lean`
points here via the `lean.ref` URI
`qou:QOU.BraidKnot.CyclotomicLValueDecomposition.beta_3_from_jonquiere`.

This file is Lake-compiled (the sibling is documentation only).
Carries one verified `ring`-arithmetic theorem
(`beta_3_from_jonquiere`) and one `class`-level conjecture
(`LValueDecomposition`) per the §3b-cond conditional-class
pattern.

References:
- [bloch2000] Bloch, Higher regulators and L-values.
- [zagier1986] Zagier, polylog / L-value identities.
- Lewin (1991), *Polylogarithms and Associated Functions*.
-/

namespace QOU.BraidKnot.CyclotomicLValueDecomposition

open QOU.Infra.Polylogarithm
open QOU.Infra.DirichletL

/-- **Theorem (`prop:cyclotomic-l-value-decomposition`,
    arithmetic core).**

    `lean.ref` alias for the manuscript's
    `prop:cyclotomic-l-value-decomposition` block.  Forwards to
    the canonical proof in `QOU.Infra.Polylogarithm`
    (`beta3_from_jonquiere`) to avoid duplicating the
    arithmetic identity.  Per Gemini review:
    central utility goes in the infra module; chapter modules
    forward. -/
theorem beta_3_from_jonquiere : imLi3ZetaPredicted 4 = beta3 :=
  QOU.Infra.Polylogarithm.beta3_from_jonquiere

/-- **Conditional-class wrapper for the full L-value decomposition.**

    Records the manuscript claim

      `β(3) = L(χ_4, 3) = Im Li_3(i) = π³ / 32`

    via the full chain (1) Theorem A → (2) β(3) Dirichlet series →
    (3) Hurwitz-Lerch decomposition → (4) L(χ, n) identification.

    Steps (2)-(4) are conjectural-class content (require Mathlib
    `Polylogarithm` / `DirichletL` infrastructure not yet
    available); step (1) is the verified `beta_3_from_jonquiere`
    above.  Downstream propositions taking
    `[LValueDecomposition]` as a hypothesis become rigorous
    conditional results per AGENTS.md §3b-cond. -/
class LValueDecomposition where
  /-- The full chain β(3) = L(χ_4, 3) = Im Li_3(i) = π³ / 32. -/
  full_decomposition : beta3 = Real.pi ^ 3 / 32

/-- Subtracting the beta-three constant from the predicted value at four cancels to zero (`qou-jvav`). -/
theorem beta_3_from_jonquiere_sub_eq_zero :
    imLi3ZetaPredicted 4 - beta3 = 0 := by
  rw [beta_3_from_jonquiere, sub_self]

end QOU.BraidKnot.CyclotomicLValueDecomposition
