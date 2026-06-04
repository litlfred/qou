/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Pochhammer symbols `(q;q)_n` — categorical machinery scaffold (2026-06-04)

This file scaffolds the q-Pochhammer infrastructure needed for the
Habiro-element promotion of the Q_β residue A and m_μ closure
(audit doc `docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`).

## Definitions provided

| Symbol | Definition | Notes |
|--------|-----------|-------|
| `qPochhammerFinite a q n` | `∏_{k=0}^{n-1} (1 - a·q^k)` | Finite q-Pochhammer `(a;q)_n` |
| `qPochhammerDiag q n` | `qPochhammerFinite q q n = ∏_{k=0}^{n-1} (1 - q^(k+1))` | Diagonal case `(q;q)_n` |
| `qBinomial n k q` | `(q;q)_n / ((q;q)_k · (q;q)_{n-k})` | Gaussian q-binomial |

## Theorems provided (all proved)

- `qPochhammerFinite_zero`: `(a;q)_0 = 1` (empty product)
- `qPochhammerFinite_one`: `(a;q)_1 = 1 - a`
- `qPochhammerFinite_succ_eq_mul`: recursion `(a;q)_{n+1} = (a;q)_n · (1 - a·q^n)`
- `qPochhammerDiag_zero`: `(q;q)_0 = 1`
- `qPochhammerDiag_one`: `(q;q)_1 = 1 - q`
- `qPochhammerDiag_at_q_one`: `(q;q)_n = 0` for all `n ≥ 1` at `q = 1` (collapses)

## Cross-refs

- `MmuR9V9Closure.lean` (downstream consumer for residue A promotion)
- `QBetaCategoricalPrecisionLadder.lean` (uses ℏ_q^k which is dual to (q;q)_n)
- Audit: [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../../../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Algebra.GeomSum
import Mathlib.Algebra.Order.Ring.Lemmas
import Mathlib.Analysis.SpecialFunctions.Pow.Real

open BigOperators

namespace QOU.Machinery

/-! ## Finite q-Pochhammer `(a;q)_n` -/

/-- Finite q-Pochhammer `(a;q)_n = ∏_{k=0}^{n-1} (1 - a·q^k)`. -/
noncomputable def qPochhammerFinite (a q : ℝ) (n : ℕ) : ℝ :=
  ∏ k ∈ Finset.range n, (1 - a * q ^ k)

/-- Diagonal q-Pochhammer `(q;q)_n = ∏_{k=0}^{n-1} (1 - q^(k+1))`. -/
noncomputable def qPochhammerDiag (q : ℝ) (n : ℕ) : ℝ :=
  qPochhammerFinite q q n

/-! ## Basic identities (proved) -/

/-- **(a;q)_0 = 1** (empty product). -/
theorem qPochhammerFinite_zero (a q : ℝ) : qPochhammerFinite a q 0 = 1 := by
  unfold qPochhammerFinite
  simp

/-- **(a;q)_1 = 1 - a**. -/
theorem qPochhammerFinite_one (a q : ℝ) : qPochhammerFinite a q 1 = 1 - a := by
  unfold qPochhammerFinite
  simp

/-- **(q;q)_0 = 1** (empty product). -/
theorem qPochhammerDiag_zero (q : ℝ) : qPochhammerDiag q 0 = 1 := by
  unfold qPochhammerDiag
  exact qPochhammerFinite_zero q q

/-- **(q;q)_1 = 1 - q**. -/
theorem qPochhammerDiag_one (q : ℝ) : qPochhammerDiag q 1 = 1 - q := by
  unfold qPochhammerDiag
  exact qPochhammerFinite_one q q

/-- **Recursion**: `(a;q)_{n+1} = (a;q)_n · (1 - a·q^n)`. -/
theorem qPochhammerFinite_succ (a q : ℝ) (n : ℕ) :
    qPochhammerFinite a q (n + 1) = qPochhammerFinite a q n * (1 - a * q ^ n) := by
  unfold qPochhammerFinite
  rw [Finset.prod_range_succ]

/-- **At q = 1**, `(q;q)_n = 0` for all `n ≥ 1` because the `k = 0`
factor is `1 - q^1 = 0`. -/
theorem qPochhammerDiag_at_q_one (n : ℕ) (hn : 0 < n) :
    qPochhammerDiag 1 n = 0 := by
  unfold qPochhammerDiag qPochhammerFinite
  apply Finset.prod_eq_zero (i := 0)
  · exact Finset.mem_range.mpr hn
  · simp

/-! ## Gaussian q-binomial `[n choose k]_q`

The standard form `[n k]_q = (q;q)_n / ((q;q)_k · (q;q)_{n-k})`.
Currently a placeholder; promotion to `derived` requires the q-binomial
theorem and Pascal-type recursion (q-deformed). -/

/-- **Gaussian q-binomial** `[n k]_q` as a quotient of q-Pochhammers.
Well-defined when `(q;q)_k ≠ 0` and `(q;q)_{n-k} ≠ 0`. -/
noncomputable def qBinomial (n k : ℕ) (q : ℝ) : ℝ :=
  qPochhammerDiag q n / (qPochhammerDiag q k * qPochhammerDiag q (n - k))

/-- `[n 0]_q = 1` for any q and n. -/
theorem qBinomial_zero (n : ℕ) (q : ℝ) (hq : qPochhammerDiag q n ≠ 0) :
    qBinomial n 0 q = 1 := by
  unfold qBinomial
  rw [qPochhammerDiag_zero]
  simp
  exact div_self hq

/-! ## Conditional class for the q-Pochhammer / Habiro link

The Habiro ring identification of the Q_β residue A (per the KLR/crystal
infra scope) requires the q-Pochhammer module to be wired into a
Habiro-ring structure. This is captured as a conditional class so
downstream theorems can carry it as a hypothesis. -/

/-- Conditional class axiomatising the Habiro-ring evaluation of
q-Pochhammer products at roots of unity. NEAR-MATCH tier — instance
not constructed (requires upstream Habiro-ring machinery in Mathlib). -/
class QPochhammerHabiroEvaluation (q : ℝ) : Prop where
  /-- The finite q-Pochhammer evaluates consistently at unity-shifted
  arguments (opaque marker for the open derivation). -/
  habiro_evaluation : True

end QOU.Machinery
