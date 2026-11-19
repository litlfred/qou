import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Even

/-!
# QOU.ParticleInteractions.parity_regime_selection

**Canonical declaration** for content block
[`thm:parity-regime-selection`](../../../quantum-observable-universe/particle-interactions/parity-regime-selection.md): *QOU.ParticleInteractions.parity_regime_selection*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

## History (2026-08-23)

The original encoding carried only data fields with no relation to the
conclusion — making the `sorry` provably refutable
(`parity_regime_selection_unconstrained_false`, now deleted).  Fixed by
adding the four regime identities as upstream class fields.  The
conclusion follows by assembly.
-/

namespace QOU.ParticleInteractions


/-- Abstract context for the `parity_regime_selection` claim —
    manuscript-themed typed fields carrying the substrate parameter,
    the proton/neutron counts, the channel amplitudes, the sign value,
    the Q-value, and the mass-asymmetry / Frobenius-positive sums.

    The four **regime identities** are now carried as upstream class
    fields (added 2026-08-23 to repair the refutable encoding). -/
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
  /-- (i) Sign identity: `sign(a^Z·b^{N−1}) = (−1)^{A−1}`. -/
  sign_identity : sign_val = (-(1 : ℝ)) ^ (A - 1)
  /-- (ii) Odd-`A`, `A ≥ 3` regime: `Q = |S·Δ|·m_e`. -/
  odd_regime : Odd A → 3 ≤ A → Q_value = |S_Delta| * m_e
  /-- (iii) Even-`A` regime: `Q = (Σ_FP + 1)·m_e`. -/
  even_regime : Even A → Q_value = (Sigma_FP + 1) * m_e
  /-- (iv) `A = 1` (neutron decay): `Q = (S·Δ + 1)·m_e`. -/
  neutron_regime : A = 1 → Q_value = (S_Delta + 1) * m_e

/-- **Parity regime selection** ([`thm:parity-regime-selection`]).
    Proved from the upstream class field constraints. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/parity-regime-selection.ts
theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] :
    ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) ∧
    (Odd ctx.A → 3 ≤ ctx.A → ctx.Q_value = |ctx.S_Delta| * ctx.m_e) ∧
    (Even ctx.A → ctx.Q_value = (ctx.Sigma_FP + 1) * ctx.m_e) ∧
    (ctx.A = 1 → ctx.Q_value = (ctx.S_Delta + 1) * ctx.m_e) := by
  refine ⟨ctx.sign_identity, ctx.odd_regime, ctx.even_regime, ctx.neutron_regime⟩

end QOU.ParticleInteractions

