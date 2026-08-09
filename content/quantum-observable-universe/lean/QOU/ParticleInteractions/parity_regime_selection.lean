import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Even

/-!
# QOU.ParticleInteractions.parity_regime_selection

**Canonical declaration** for content block
[`thm:parity-regime-selection`](../../../quantum-observable-universe/particle-interactions/parity-regime-selection.md): *QOU.ParticleInteractions.parity_regime_selection*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.ParticleInteractions


/-- Abstract context for the `parity_regime_selection` claim —
    manuscript-themed typed fields carrying the substrate parameter,
    the proton/neutron counts, the channel amplitudes, the sign value,
    the Q-value, and the mass-asymmetry / Frobenius-positive sums.
    These are the **data**; nothing here asserts the regime identities
    (they are named below as a `Prop`, not projected from class
    fields). -/
class ParityRegimeSelectionContext where
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Mass number `A = Z + N`. -/
  A : ℕ
  A_eq : A = Z + N
  /-- The proton-channel amplitude `a : ℝ`. -/
  a : ℝ
  /-- The neutron-channel amplitude `b : ℝ`. -/
  b : ℝ
  /-- The sign of `a^Z · b^{N − 1}` as `±1` (encoded as `ℝ` with value
      `±1`). -/
  sign_val : ℝ
  /-- Electron rest mass (MeV). -/
  m_e : ℝ
  /-- The Q-value `Q(Z, N)` (MeV) of the decay. -/
  Q_value : ℝ
  /-- Mass-asymmetry product `S · Δ = a^Z · b^{N-1} · (a − b)`. -/
  S_Delta : ℝ
  /-- Sum of Frobenius-positive Markov-trace configurations
      (`Σ_FP`) used in the even-`A` regime. -/
  Sigma_FP : ℝ

/-- **Parity regime selection** (from manuscript):

For all $q > 1$ the parent decay obeys the sign identity

$$
  \operatorname{sign}(a^Z \cdot b^{N-1}) = (-1)^{A-1}
$$

and the Q-value falls into one of three regimes by the parity of $A$.

The Lean encoding **names** the conditional conjecture as a `Prop`
(pattern C of the vacuity-fix playbook): the context class carries the
decay data, and `ParityRegimeSelection` is the proposition that the
four manuscript sub-claims hold — (i) the sign identity
`sign(a^Z·b^{N−1}) = (−1)^{A−1}`; (ii) odd-`A`, `A ≥ 3`:
`Q = |S·Δ|·m_e`; (iii) even-`A`: `Q = (Σ_FP + 1)·m_e`; (iv) `A = 1`
neutron decay: `Q = (S·Δ + 1)·m_e`.  It is *not* asserted (no
`theorem … := ⟨ctx.claim_*⟩` self-assuming projection); an instance
discharging it is the open conditional claim. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/parity-regime-selection.ts
theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] :
    ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) ∧
    (Odd ctx.A → 3 ≤ ctx.A → ctx.Q_value = |ctx.S_Delta| * ctx.m_e) ∧
    (Even ctx.A → ctx.Q_value = (ctx.Sigma_FP + 1) * ctx.m_e) ∧
    (ctx.A = 1 → ctx.Q_value = (ctx.S_Delta + 1) * ctx.m_e) := by
  -- Ref: [manuscript] quantum-observable-universe/particle-interactions/parity-regime-selection.ts
  sorry

/-- **The statement above is refutable as written** — the class never relates
    the fields its conclusion names, so `∀ instances` admits ones that simply
    disagree. Not an open gap: the `sorry` cannot be discharged. Fixing it
    means giving the class the hypotheses the derivation needs (bean qou-octr,
    criterion §10 `proof-unclosable-context-sorry`). This refutation is the
    evidence, not the fix. -/
theorem parity_regime_selection_unconstrained_false :
    ¬ ∀ ctx : ParityRegimeSelectionContext,
        ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) := by
  intro h
  have := h { q := 2, q_gt_one := by norm_num, Z := 1, N := 0, A := 1,
              A_eq := rfl, a := 0, b := 0, sign_val := 0, m_e := 0,
              Q_value := 0, S_Delta := 0, Sigma_FP := 0 }
  norm_num at this

end QOU.ParticleInteractions
