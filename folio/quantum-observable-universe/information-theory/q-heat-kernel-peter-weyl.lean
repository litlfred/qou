import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Data.Int.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Topology.Algebra.InfiniteSum.Basic


/-!
# QOU.qHeatKernelPeterWeyl — Peter-Weyl decomposition of q-heat kernel

The q-heat kernel decomposes over Hecke-algebra irreducibles:

  u(t,x) = Σ_{λ ⊢ n} d_λ(q) · exp(-μ_λ(q) t) · π_λ(u₀)(x),

with the content-Casimir eigenvalue, in **symmetric** quantum integers and with **no** `ℏ_q²`:

  μ_λ(q) = Σ_{□ ∈ λ} [c(□)]_q [c(□)+1]_q,   [k]_q = (q^k − q^{−k})/(q − q⁻¹).

Corrected 2026-11-16 (issue #8091; `docs/audits/2026-11-16-binding-reeb-holonomy-laplacian.md`).
Before that date this file used Jackson integers and the prefactor `ℏ_q² = (1 − q⁻¹)²`.

* **Symmetric, not Jackson.** `Σ[c][c+1]` is the block eigenvalue of an element of `H_n(q)` only in
  symmetric integers: it is then a Laurent polynomial in the Murphy eigenvalues `q^{2c}`.  The
  operator is the Reeb-holonomy Laplacian `Σ_k (q·L_k + q⁻¹·L_k⁻¹ − (q + q⁻¹)) / (q − q⁻¹)²`, with
  `L_k` the relative full twist (`QOU.BraidKnot.Hecke.reebLaplacianB_smul_of_weight`,
  `fullTwistB_succ_eq_mul_jmRawB`; centrality `QOU.SchurWeyl.contentCasimir_comm_σ`).
* **No `ℏ_q²`.** On a mode with no horizontal derivative, `d_q = q⁻¹d + ℏ_q Θ∧L_ξ` and
  `δ_q = q⁻¹δ + ℏ_q L_ξ*ι_ξ` reduce to `d` and `δ`, because `q⁻¹ + ℏ_q = 1`.  So the Reeb part of
  `Δ_q` enters with weight `(q⁻¹ + ℏ_q)² = 1`, not `ℏ_q²`: the classical-core and cross terms of the
  three-term expansion also act on Reeb modes.  This is written in the audit, not formalised here.

LaTeX label: `prop:q-heat-kernel-peter-weyl`

## References

- [leitner2026] §9-information-theory/q-heat-kernel-peter-weyl
- [leitner2026] §2-quantum-observable-universes/q-laplacian-expansion

**Char 0 only** for the heat-kernel series (`qHeatKernelPeterWeyl`): the archimedean realisation
needs a convergent sum.  The eigenvalue itself is stated over any field.
-/

namespace QOU

noncomputable section
open Finset

open Classical in
/-- Symmetric quantum integer `[k]_q = (q^k − q^{−k})/(q − q⁻¹)`, with the value `k` at `q = q⁻¹`
(where the quotient is the limit `k`). -/
-- Ref: [leitner2026] §9
def symInt {K : Type*} [Field K] (q : K) (k : ℤ) : K :=
  if q = q⁻¹ then (k : K) else (q ^ k - q⁻¹ ^ k) / (q - q⁻¹)

/-- Classical content-sum for a partition: Σ c(c+1). -/
-- Ref: [leitner2026] §9
def contentSumClassical (lam : YoungDiagram) : ℤ :=
  ∑ cell ∈ lam.cells, (cell.2 - cell.1) * (cell.2 - cell.1 + 1)

/-- q-Casimir content-sum for a partition: Σ [c]_q [c+1]_q, symmetric integers. -/
-- Ref: [leitner2026] §9
def contentSumQCasimir {K : Type*} [Field K] (q : K) (lam : YoungDiagram) : K :=
  ∑ cell ∈ lam.cells,
    symInt q ((cell.2 : ℤ) - cell.1) * symInt q ((cell.2 : ℤ) - cell.1 + 1)

/-- **Reeb-spin eigenvalue on a Wedderburn block**:

    μ_λ(q) = Σ_{□ ∈ λ} [c(□)]_q · [c(□)+1]_q.

    No `ℏ_q²` (see the module docstring).  The base-manifold eigenvalue `q⁻²|k|²` is separate and
    depends on the spatial mode, not on the partition λ. -/
-- Ref: [leitner2026] §9
def muLambda {K : Type*} [Field K] (q : K) (lam : YoungDiagram) : K :=
  contentSumQCasimir q lam

/-- **At q = 1** (classical limit) `μ_λ` is the classical content sum `Σ c(c+1)`. -/
-- Ref: [leitner2026] §9
theorem muLambda_classical {K : Type*} [Field K] (lam : YoungDiagram) :
    muLambda (1 : K) lam = (contentSumClassical lam : K) := by
  unfold muLambda contentSumQCasimir contentSumClassical symInt
  simp only [inv_one, ↓reduceIte]
  push_cast
  rfl

/-- The single-cell Young diagram λ = (1), i.e. cells `{(0,0)}`. The
    singleton is a lower set because `(0,0)` is the minimum of `ℕ × ℕ`. -/
-- Ref: [leitner2026] §9
def singleCellDiagram : YoungDiagram where
  cells := {(0, 0)}
  isLowerSet := by
    intro a b hba ha
    simp only [Finset.coe_singleton, Set.mem_singleton_iff] at ha ⊢
    subst ha
    have h1 : b.1 ≤ 0 := hba.1
    have h2 : b.2 ≤ 0 := hba.2
    exact Prod.ext_iff.mpr ⟨by omega, by omega⟩

/-- **Single-cell partition** λ = (1) has μ_λ = 0 (its one content is `0`, and `[0]_q = 0`). -/
-- Ref: [leitner2026] §9
theorem muLambda_single {K : Type*} [Field K] (q : K) :
    muLambda q singleCellDiagram = 0 := by
  unfold muLambda contentSumQCasimir singleCellDiagram symInt
  split_ifs <;> simp

/-- **Reflection `c ↦ −c − 1`**: `[−c−1]_q [−c]_q = [c]_q [c+1]_q`, since `[−m]_q = −[m]_q`.
    So each cell's value is the `U_q(𝔰𝔩₂)` Casimir value `[j][j+1]` at the spin `j ≥ 0` among
    `c`, `−c−1`.  (The cleared Hecke-side form is `QOU.BraidKnot.Hecke.reebStep_reflect`.) -/
-- Ref: [leitner2026] §9
theorem symInt_reflect {K : Type*} [Field K] (q : K) (c : ℤ) :
    symInt q (-c - 1) * symInt q (-c) = symInt q c * symInt q (c + 1) := by
  unfold symInt
  split_ifs with h
  · push_cast; ring
  · have e1 : -c - 1 = -(c + 1) := by ring
    rw [e1, zpow_neg, zpow_neg, zpow_neg, zpow_neg]
    simp only [inv_zpow, inv_inv]
    ring

/-- **Peter-Weyl heat-kernel convergence** (conjecture, archimedean).

    The named statement of `prop:q-heat-kernel-peter-weyl`: for `0 < q`,
    `q ≠ 1` and a heat time `t > 0`, the spectral series

      `Σ_{λ} d_λ(q) · exp(-μ_λ(q) · t)`

    of the `q`-heat kernel is (absolutely) summable over the Wedderburn
    blocks `λ` (indexed by `YoungDiagram`), where `μ_λ(q) = muLambda q λ`
    is the content-Casimir eigenvalue (symmetric integers, no `ℏ_q²`) and `dLambda λ` is the Steinberg
    `q`-hook dimension of the block.

    This is the Mercer-type convergence whose justification (`μ_λ ≍ n²/q²`
    for `λ ⊢ n` against polynomial-in-`n` dimensions) is given in the
    narrative but not yet formalised; per AGENTS.md §1a / §3b (Pattern C)
    we **name** the conditional conjecture as a `Prop` rather than fake a
    proof. The carrier asserts the real `Summable` claim — there is no
    instance / proof term, the honest open state. -/
-- Ref: [leitner2026] §9
def qHeatKernelPeterWeyl (q t : ℝ) (dLambda : YoungDiagram → ℝ)
    (_hq : 0 < q) (_hq1 : q ≠ 1) (_ht : 0 < t) : Prop :=
  Summable (fun lam : YoungDiagram => dLambda lam * Real.exp (-(muLambda q lam) * t))

end

end QOU
