/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Dilogarithm machinery scaffold (2026-06-04)

This file scaffolds the q-dilogarithm infrastructure needed for the
Faddeev / Bloch-Wigner family of categorical attacks on Q_β residue A
(see AGENTS.md §"Critical framing — Q_β c_3 truncation order").

## Definitions provided

| Symbol | Definition | Notes |
|--------|-----------|-------|
| `qDilogPartial q N` | `∑_{n=1}^N q^n / (n · (1 - q^n))` | Truncated compact q-dilog (finite version; legacy "Faddeev" naming) |

## Why this matters

The AGENTS.md "Critical framing" note states: the Q_β c_3 problem is a
**fibre-level Habiro element** whose archimedean evaluation at q_0 is
sought. compact-q-dilog / Li_2^q vs. Φ_q context-sorting determines the
expansion. This file provides the symbolic primitives.

## Theorems provided (all proved)

- `qDilogPartial_zero`: `qDilogPartial q 0 = 0` (empty sum)
- `qDilogPartial_at_q_zero`: `qDilogPartial 0 N = 0` (all terms vanish)

## Removed 2026-08-07 — the `blochWignerD` stub (bean `qou-ir1l`)

This file used to carry

    noncomputable def blochWignerD (_q : ℝ) (_n : ℕ) : ℝ := 0
    theorem blochWignerD_real_pos (q n) (_hq : 0 < q) : blochWignerD q n = 0 := rfl

which is the banned tautology pattern (AGENTS.md §Strict Lean Discipline 5):
the conclusion is `rfl` on a definitional `0` and the hypothesis `0 < q` is
never used, so the "theorem" asserts nothing falsifiable.

It was also misleading. The name `blochWignerD` reads as *the* Bloch–Wigner
function while being bound to the constant `0`, encoding a special-case
vanishing as if it were the function. The Chain 1 β NEGATIVE verdict
(PR #1768) it recorded is about `D(qⁿ)` for **real positive** `q`, where `D`
vanishes for the trivial reason that `D` vanishes on the whole real axis —
not because Bloch–Wigner is degenerate on the substrate.

The real Bloch–Wigner function now lives in
[`QOU/Archimedean/BlochWignerLobachevsky.lean`](../Archimedean/BlochWignerLobachevsky.lean)
as `BlochWigner_lob`, defined through the ideal-tetrahedron dihedral angles and
therefore valid off the unit circle. The genuine vanishing statement is
`BlochWigner_lob_real_eq_zero` there: it is *proved* from `Λ(0) = Λ(π/2) = 0`
rather than asserted by definition, and it makes the actual content visible —
`D` vanishes on the reals because a real shape parameter degenerates the
tetrahedron, which is a fact about `D`, not about the substrate.

That the corpus carries a sharp non-zero Bloch–Wigner value elsewhere
(`D(y₊) = Vol(5₂)/3`, published as Broadhurst eq (73)) is the practical reason
the old stub had to go: a reader meeting `blochWignerD := 0` would conclude the
opposite.

## Cross-refs

- `QBetaCategoricalPrecisionLadder.lean` (the c_3 ladder Faddeev family attaches to)
- Audit: [`docs/coordination/2026-06-03-qbeta-habiro-chain-1-scope.md`](../../../../../docs/coordination/2026-06-03-qbeta-habiro-chain-1-scope.md)
- AGENTS.md §"Critical framing — Q_β c_3 truncation order"
-/

import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

open BigOperators

namespace QOU.Machinery

/-! ## Partial q-dilogarithm `Li_2^q_N(q) = ∑_{n=1}^N q^n / (n·(1-q^n))` -/

/-- Partial q-dilogarithm (truncated compact-q-dilog form). Sums from `n = 1`
to `N`. Returns 0 when `N = 0`. -/
noncomputable def qDilogPartial (q : ℝ) (N : ℕ) : ℝ :=
  ∑ n ∈ Finset.range N, (q ^ (n + 1) / ((n + 1) * (1 - q ^ (n + 1))))

/-! ## Basic identities (proved) -/

/-- **Empty sum case**: `qDilogPartial q 0 = 0`. -/
theorem qDilogPartial_zero (q : ℝ) : qDilogPartial q 0 = 0 := by
  unfold qDilogPartial
  simp

/-- **At q = 0**: each term `0^(n+1) / (… · …) = 0` so the sum is 0. -/
theorem qDilogPartial_at_q_zero (N : ℕ) : qDilogPartial 0 N = 0 := by
  unfold qDilogPartial
  apply Finset.sum_eq_zero
  intro n _
  -- `0^(n+1) = 0^n * 0 = 0` (pow_succ + mul_zero), so the term is `0 / (…) = 0`.
  -- Uses pow_succ rather than zero_pow to avoid the `n ≠ 0` vs `0 < n`
  -- signature drift across Mathlib versions.
  rw [pow_succ, mul_zero, zero_div]

/-! ## Bloch-Wigner D function — moved

The `blochWignerD := 0` stub that lived here was removed 2026-08-07
(bean `qou-ir1l`); see the file header for why. The real function is
`QOU.Archimedean.BlochWigner_lob`, and the vanishing on the real axis is
`QOU.Archimedean.BlochWigner_lob_real_eq_zero` — proved rather than
definitional. Nothing referenced the stub. -/

/-! ## Conditional class for compact-q-dilog / Φ_q context

The Φ_q (compact q-dilog) vs. Li_2^q (Rogers) distinction is context-sorting
infrastructure for the Habiro element promotion. -/

/-- Conditional class axiomatising the compact quantum dilogarithm
context for the Habiro element. NEAR-MATCH tier; instance not
constructed (requires upstream Bloch–Wigner machinery).

**Legacy name.** `FaddeevQuantumDilogContext` (and the field prefix
`faddeev_`) are retained for compatibility with existing `lean.ref`
consumers, but the object here is the **compact q-Pochhammer `Φ_q`**
`∏(1−q^{-k}z)^{-1}` — **not** Faddeev's non-compact modular-double `Φ_b`
(see `QOU.QBeta.FaddeevModularDouble` and the 2026-07-06 terminology
ruling in `docs/audits/2026-07-06-qbeta-faddeev-phi-b-modular-double-accuracy.md`). -/
class FaddeevQuantumDilogContext (q : ℝ) where
  /-- The compact q-dilogarithm `Φ_q(z) = ∏_{k≥0} (1 - q^{-k} z)^{-1}`
      carried as an abstract real function of `z` (the concrete infinite
      product / its convergence is the open derivation). -/
  Phi : ℝ → ℝ
  /-- The `Φ_q` **functional equation** `(1 - z)·Φ_q(z) = Φ_q(q⁻¹ z)`
      (was `True`).  Derivation for the `k ≥ 0` product convention: the
      `k = 0` factor of `P(z) := ∏_{k≥0}(1 - q^{-k}z)` peels off as
      `P(z) = (1 - z)·P(q⁻¹ z)`, and `Φ_q = P⁻¹` inverts this to the
      stated relation. -/
  faddeev_functional_equation : ∀ z : ℝ, (1 - z) * Phi z = Phi (q⁻¹ * z)

end QOU.Machinery
