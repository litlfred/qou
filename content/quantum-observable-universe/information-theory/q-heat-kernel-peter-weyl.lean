import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Data.Int.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Algebra.InfiniteSum.Basic


/-!
# QOU.qHeatKernelPeterWeyl — Peter-Weyl decomposition of q-heat kernel

The q-heat kernel decomposes over Hecke-algebra irreducibles:

  u(t,x) = Σ_{λ ⊢ n} d_λ(q) · exp(-μ_λ(q) t) · π_λ(u₀)(x),

with the content-Casimir eigenvalue

  μ_λ(q) = ℏ_q² Σ [c]_q [c+1]_q.

LaTeX label: `prop:q-heat-kernel-peter-weyl`

## References

- [manuscript] §9-information-theory/q-heat-kernel-peter-weyl
- [manuscript] §2-quantum-observable-universes/q-laplacian-expansion

**Char 0 only**: archimedean realisation needs convergent heat-kernel sum.
-/

namespace QOU

noncomputable section
open Finset

/-- Jackson integer [k]_q = (1 - q^k)/(1 - q) over ℝ (q ≠ 1). -/
-- Ref: [manuscript] §9
def jacksonInt (q : ℝ) (k : ℤ) : ℝ :=
  if q = 1 then (k : ℝ)
  else (1 - q^k) / (1 - q)

/-- Quantum Planck constant ℏ_q = (q - 1)/q. -/
-- Ref: [manuscript] §9
def hbar_q (q : ℝ) : ℝ := (q - 1) / q

/-- Classical content-sum for a partition: Σ c(c+1). -/
-- Ref: [manuscript] §9
def contentSumClassical (lam : YoungDiagram) : ℤ :=
  ∑ cell ∈ lam.cells, (cell.2 - cell.1) * (cell.2 - cell.1 + 1)

/-- q-Casimir content-sum for a partition: Σ [c]_q [c+1]_q. -/
-- Ref: [manuscript] §9
def contentSumQCasimir (q : ℝ) (lam : YoungDiagram) : ℝ :=
  ∑ cell ∈ lam.cells,
    jacksonInt q (cell.2 - cell.1) * jacksonInt q (cell.2 - cell.1 + 1)

/-- **Reeb-spin eigenvalue on Wedderburn block**:

    μ_λ(q) = ℏ_q² · Σ_{□ ∈ λ} [c(□)]_q · [c(□)+1]_q.

    The base-manifold eigenvalue q⁻² |k|² is separate and depends
    on the spatial mode, not on the partition λ. -/
-- Ref: [manuscript] §9
def muLambda (q : ℝ) (lam : YoungDiagram) : ℝ :=
  (hbar_q q)^2 * contentSumQCasimir q lam

/-- **At q = 1** (classical limit): μ_λ reduces to the classical
    content sum (the spin term vanishes because ℏ_q = 0). -/
-- Ref: [manuscript] §9
theorem muLambda_classical (lam : YoungDiagram) :
    muLambda 1 lam = 0 := by
  unfold muLambda hbar_q
  simp

/-- The single-cell Young diagram λ = (1), i.e. cells `{(0,0)}`. The
    singleton is a lower set because `(0,0)` is the minimum of `ℕ × ℕ`. -/
-- Ref: [manuscript] §9
def singleCellDiagram : YoungDiagram where
  cells := {(0, 0)}
  isLowerSet := by
    intro a b hba ha
    simp only [Finset.coe_singleton, Set.mem_singleton_iff] at ha ⊢
    subst ha
    have h1 : b.1 ≤ 0 := hba.1
    have h2 : b.2 ≤ 0 := hba.2
    exact Prod.ext_iff.mpr ⟨by omega, by omega⟩

/-- **Single-cell partition** λ = (1) has μ_λ = 0. -/
-- Ref: [manuscript] §9
theorem muLambda_single (q : ℝ) (hq : q ≠ 0) :
    muLambda q singleCellDiagram = 0 := by
  unfold muLambda contentSumQCasimir singleCellDiagram
  simp [jacksonInt]

/-- **Peter-Weyl heat-kernel convergence** (conjecture, archimedean).

    The named statement of `prop:q-heat-kernel-peter-weyl`: for `0 < q`,
    `q ≠ 1` and a heat time `t > 0`, the spectral series

      `Σ_{λ} d_λ(q) · exp(-μ_λ(q) · t)`

    of the `q`-heat kernel is (absolutely) summable over the Wedderburn
    blocks `λ` (indexed by `YoungDiagram`), where `μ_λ(q) = muLambda q λ`
    is the content-Casimir eigenvalue and `dLambda λ` is the Steinberg
    `q`-hook dimension of the block.

    This is the Mercer-type convergence whose justification (`μ_λ ≍ n²/q²`
    for `λ ⊢ n` against polynomial-in-`n` dimensions) is given in the
    narrative but not yet formalised; per AGENTS.md §1a / §3b (Pattern C)
    we **name** the conditional conjecture as a `Prop` rather than fake a
    proof. The carrier asserts the real `Summable` claim — there is no
    instance / proof term, the honest open state. -/
-- Ref: [manuscript] §9
def qHeatKernelPeterWeyl (q t : ℝ) (dLambda : YoungDiagram → ℝ)
    (_hq : 0 < q) (_hq1 : q ≠ 1) (_ht : 0 < t) : Prop :=
  Summable (fun lam : YoungDiagram => dLambda lam * Real.exp (-(muLambda q lam) * t))

end

end QOU
