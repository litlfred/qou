import Mathlib.Tactic

/-!
# QOU.Information.BhStateCounting — conjectural class

**§3b class axiomatisation** for content block
[`conj:bh-state-counting`](../../../quantum-observable-universe/information-theory/bh-state-counting.md):
*the quantum dimension of the exterior horizon-mode space of a jet
horizon equals `exp (s⋆ · A)`, the exponential of the Bekenstein
entropy* — the QOU form of the third postulate of black hole
complementarity.

This is a **conjecture** (primary): the class fields carry the
parameter-quantified content of the claim (the puncture partition pole
and the exponential state count); no instance is declared (the open
state).  Base ring is `ℝ` per AGENTS.md §7c: the statement is
archimedean (it uses `Real.exp`, ordering, and a substrate evaluation),
so the specialisation is genuine, not gratuitous.

Intended interpretation: `numLabels` enumerates the admissible puncture
labels `V_j`; `qdim j` is the quantum integer `[2j+1]_{q₀}`; `action j`
is the Casimir action `τ(C_{q₀}(V_j))`; `sStar` is the pole of the
per-puncture partition function `Z₁`; `horizonQdim A` is the quantum
dimension of the GNS closure of the exterior horizon-mode algebra at
mode rank `A = dim Γ(𝓗, A₁/A₀)`.
-/

namespace QOU.Information

open Finset in
/-- Black-hole state counting (STU postulate 3, exterior sector).

    Conjectural class — see
    [`conj:bh-state-counting`](../../../quantum-observable-universe/information-theory/bh-state-counting.md).

    Fields encode: positivity of the q-dimension and action data, the
    partition pole `Z₁(s⋆) = 1`, its uniqueness on the positive axis,
    and the exponential count `dim_q = exp (s⋆ · A)`. -/
class BhStateCounting where
  /-- Number of admissible puncture labels. -/
  numLabels : ℕ
  /-- At least one admissible label. -/
  numLabels_pos : 0 < numLabels
  /-- Quantum dimension `[2j+1]_{q₀}` of the `j`-th label. -/
  qdim : ℕ → ℝ
  /-- Quantum dimensions are positive in the Wenzl-positive window. -/
  qdim_pos : ∀ j < numLabels, 0 < qdim j
  /-- Casimir action `τ(C_{q₀}(V_j))` of the `j`-th label. -/
  action : ℕ → ℝ
  /-- Casimir actions are positive. -/
  action_pos : ∀ j < numLabels, 0 < action j
  /-- The entropy density: the pole of the per-puncture partition
      function. -/
  sStar : ℝ
  sStar_pos : 0 < sStar
  /-- **Pole relation:** `Z₁(s⋆) = 1`, i.e.
      `∑_j [2j+1]_{q₀} · exp (−s⋆ · τ(C_{q₀}(V_j))) = 1`. -/
  pole : ∑ j ∈ range numLabels, qdim j * Real.exp (-(sStar * action j)) = 1
  /-- Uniqueness of the positive pole. -/
  pole_unique :
    ∀ s : ℝ, 0 < s →
      (∑ j ∈ range numLabels, qdim j * Real.exp (-(s * action j)) = 1) →
      s = sStar
  /-- Quantum dimension of the exterior horizon-mode state space, as a
      function of the mode rank `A = dim Γ(𝓗, A₁/A₀)`. -/
  horizonQdim : ℝ → ℝ
  /-- **Conjecture (open):** the exponential state count
      `dim_q 𝓗ᵉˣᵗ_BH = exp (s⋆ · A) = exp S(M)` for every mode rank. -/
  state_count : ∀ A : ℝ, 0 ≤ A → horizonQdim A = Real.exp (sStar * A)

-- No instance is declared: the conjecture is open.  Downstream
-- conditional results take `[BhStateCounting]` as an explicit
-- hypothesis (§3b-cond).
-- Ref: [susskind1993] https://doi.org/10.1103/PhysRevD.48.3743

end QOU.Information
