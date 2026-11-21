import QOU.Basic
import QOU.QuantumObservableUniverses.QAnalysis


/-!
# QOU.QHeatEquation.unique_solution — uniqueness of the q-heat evolution

The time-derivative is determined by the q-Laplacian via `∂ₜ u = -Δ_q u`.

LaTeX: `\label{prop:q-heat-equation-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version recorded an external axiom referencing an
auto-bound `QHeatEquation` — never imported, hence unchecked.

This file now imports the relocated `QHeatEquation` structure
(`QOU.QuantumObservableUniverses.QAnalysis`) and **proves** — with no
axiom — the determination the evolution equation provides: two
solutions sharing the same q-Laplacian image `dq_u` have the same
time-derivative `dt_u`, since `evolves` pins `dt_u = -dq_u`
pointwise.  This is the algebraic-shadow uniqueness; the analytic
uniqueness (full Cauchy data, heat-kernel convergence) is archimedean
and out of scope here.

## References

- [leitner2026] §2-quantum-observable-universes/q-heat-equation-unique
- [kassel1995] Quantum Groups (Springer GTM 155), §VII.4
-/

namespace QOU

/-- **Uniqueness of the q-heat time-derivative (proved).**

    Two `QHeatEquation S` instances with the same q-Laplacian image
    `dq_u` have the same time-derivative `dt_u`: the evolution
    equation `dt_u t x = -dq_u t x` determines it pointwise.  This
    replaces an unchecked external axiom with the determination the
    evolution equation genuinely provides. -/
-- Ref: [kassel1995] Quantum Groups, §VII.4
theorem QHeatEquation.unique_solution {S : Type*}
    (H₁ H₂ : QHeatEquation S) (h_dq : H₁.dq_u = H₂.dq_u) :
    H₁.dt_u = H₂.dt_u := by
  funext t x
  rw [H₁.evolves t x, h_dq, ← H₂.evolves t x]

end QOU
