import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Even
import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.parity_regime_selection

**Canonical declaration** for content block
[`thm:parity-regime-selection`](../../../quantum-observable-universe/nuclear-interactions/parity-regime-selection.md):
*QOU.ParticleInteractions.parity_regime_selection*.

## Restructure (bean `parity_regime_selection` / `qou-uot9`)

Previously `ParityRegimeSelectionContext` carried the four conclusion conjuncts
(`sign_identity`, `odd_regime`, `even_regime`, `neutron_regime`) verbatim as
class fields and `parity_regime_selection` projected them back out as a 4-tuple.

Here:
1. The fermionic spectator sign `sign_val = (-1)^(A - 1)` is **derived** from
   the factored spectator sign `sign_val = (-1)^Z * (-1)^(N - 1)` (arising from
   `a < 0` and `b < 0` for `q > 1`), `1 ≤ N`, and `A = Z + N` via `pow_add` and
   exponent arithmetic (`Z + (N - 1) = A - 1`);
2. The dimensional `Q_value` across the three parity regimes (`Odd A` with
   `3 ≤ A`, `Even A`, and `A = 1`) is **derived** from the dimensional scaling
   `Q_value = Q_dimless * m_e` together with the dimensionless regime selector
   `Q_dimless`;
3. The spectator-amplitude asymmetry numerator `(q² - 1)(3(q² + 1)² - 2q²) > 0`
   for `q > 1` (from `parity-regime-selection-proof.md`) is proved outright in
   `spectator_asymmetry_num_pos`;
4. Consistency of `ParityRegimeSelectionContext` is witnessed by the concrete
   tritium (`A = 3, Z = 1, N = 2`) instance `tritiumParityRegimeContext`.
-/

namespace QOU.ParticleInteractions

/-- **Spectator-amplitude asymmetry numerator is positive for `q > 1`**
    (`parity-regime-selection-proof.md`):
    `a - b = (q² - 1)(3(q² + 1)² - 2q²) / (4q³) > 0`. -/
theorem spectator_asymmetry_num_pos {q : ℝ} (hq : 1 < q) :
    0 < (q ^ 2 - 1) * (3 * (q ^ 2 + 1) ^ 2 - 2 * q ^ 2) := by
  have hq2 : 1 < q ^ 2 := by nlinarith
  have h1 : 0 < q ^ 2 - 1 := by linarith
  have h2 : 0 < 3 * (q ^ 2 + 1) ^ 2 - 2 * q ^ 2 := by
    have : 3 * (q ^ 2 + 1) ^ 2 - 2 * q ^ 2 = 3 * q ^ 4 + 4 * q ^ 2 + 3 := by ring
    rw [this]
    positivity
  exact mul_pos h1 h2

/-- Context and upstream factored-sign / dimensionless-regime hypotheses for
    [`thm:parity-regime-selection`]. -/
class ParityRegimeSelectionContext where
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N ≥ 1`. -/
  N : ℕ
  N_pos : 1 ≤ N
  /-- Mass number `A = Z + N`. -/
  A : ℕ
  A_eq : A = Z + N
  /-- The proton-channel amplitude `a : ℝ` (`a < 0` for `q > 1`). -/
  a : ℝ
  a_neg : a < 0
  /-- The neutron-channel amplitude `b : ℝ` (`b < 0` for `q > 1`). -/
  b : ℝ
  b_neg : b < 0
  /-- The sign of `a^Z · b^{N − 1}` as `±1` in `ℝ`. -/
  sign_val : ℝ
  /-- Factored spectator sign from `a < 0` and `b < 0`:
      `sign(a^Z · b^{N - 1}) = (-1)^Z · (-1)^{N - 1}`. -/
  sign_val_factored : sign_val = (-(1 : ℝ)) ^ Z * (-(1 : ℝ)) ^ (N - 1)
  /-- Electron rest mass `m_e` (MeV). -/
  m_e : ℝ
  /-- Dimensionless β-decay energy release `Q / m_e`. -/
  Q_dimless : ℝ
  /-- The dimensional Q-value `Q(Z, N) = Q_dimless · m_e` (MeV). -/
  Q_value : ℝ
  Q_value_eq_dimless_mul_me : Q_value = Q_dimless * m_e
  /-- Mass-asymmetry product `S · Δ = a^Z · b^{N-1} · (a − b)`. -/
  S_Delta : ℝ
  /-- Sum of Frobenius-positive Markov-trace configurations (`Σ_FP`). -/
  Sigma_FP : ℝ
  /-- Dimensionless odd-`A` (`A ≥ 3`) regime: `Q_dimless = |S · Δ|`. -/
  Q_dimless_odd_ge_three : Odd A → 3 ≤ A → Q_dimless = |S_Delta|
  /-- Dimensionless even-`A` regime: `Q_dimless = Σ_FP + 1`. -/
  Q_dimless_even : Even A → Q_dimless = Sigma_FP + 1
  /-- Dimensionless `A = 1` (free neutron) regime: `Q_dimless = S · Δ + 1`. -/
  Q_dimless_one : A = 1 → Q_dimless = S_Delta + 1

/-- **Fermionic spectator sign law (`sign_val = (-1)^(A - 1)`)**, derived from
    the factored channel sign `(-1)^Z * (-1)^(N - 1)`, `1 ≤ N`, and `A = Z + N`. -/
theorem sign_identity_of_factored [ctx : ParityRegimeSelectionContext] :
    ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) := by
  rw [ctx.sign_val_factored, ← pow_add]
  have hexp : ctx.Z + (ctx.N - 1) = ctx.A - 1 := by
    have hA := ctx.A_eq
    have hN := ctx.N_pos
    omega
  rw [hexp]

/-- **Odd-`A` (`A ≥ 3`) dimensional Q-value**, derived from `Q_value = Q_dimless * m_e`
    and `Q_dimless_odd_ge_three`. -/
theorem odd_regime_of_dimless [ctx : ParityRegimeSelectionContext]
    (hodd : Odd ctx.A) (h3 : 3 ≤ ctx.A) :
    ctx.Q_value = |ctx.S_Delta| * ctx.m_e := by
  rw [ctx.Q_value_eq_dimless_mul_me, ctx.Q_dimless_odd_ge_three hodd h3]

/-- **Even-`A` dimensional Q-value**, derived from `Q_value = Q_dimless * m_e`
    and `Q_dimless_even`. -/
theorem even_regime_of_dimless [ctx : ParityRegimeSelectionContext]
    (heven : Even ctx.A) :
    ctx.Q_value = (ctx.Sigma_FP + 1) * ctx.m_e := by
  rw [ctx.Q_value_eq_dimless_mul_me, ctx.Q_dimless_even heven]

/-- **Neutron (`A = 1`) dimensional Q-value**, derived from
    `Q_value = Q_dimless * m_e` and `Q_dimless_one`. -/
theorem neutron_regime_of_dimless [ctx : ParityRegimeSelectionContext]
    (h1 : ctx.A = 1) :
    ctx.Q_value = (ctx.S_Delta + 1) * ctx.m_e := by
  rw [ctx.Q_value_eq_dimless_mul_me, ctx.Q_dimless_one h1]

/-- **Parity regime selection** ([`thm:parity-regime-selection`]).
    Derived from the factored spectator sign and dimensionless regime scaling. -/
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/parity-regime-selection.ts
theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] :
    ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) ∧
    (Odd ctx.A → 3 ≤ ctx.A → ctx.Q_value = |ctx.S_Delta| * ctx.m_e) ∧
    (Even ctx.A → ctx.Q_value = (ctx.Sigma_FP + 1) * ctx.m_e) ∧
    (ctx.A = 1 → ctx.Q_value = (ctx.S_Delta + 1) * ctx.m_e) :=
  ⟨sign_identity_of_factored,
   odd_regime_of_dimless,
   even_regime_of_dimless,
   neutron_regime_of_dimless⟩

/-- Concrete tritium (`³H → ³He`, `Z = 1, N = 2, A = 3`) instance witnessing
    that `ParityRegimeSelectionContext` is consistent and inhabited. -/
noncomputable def tritiumParityRegimeContext : ParityRegimeSelectionContext where
  q := 2
  q_gt_one := by norm_num
  Z := 1
  N := 2
  N_pos := by decide
  A := 3
  A_eq := rfl
  a := -1
  a_neg := by norm_num
  b := -2
  b_neg := by norm_num
  sign_val := 1
  sign_val_factored := by norm_num
  m_e := 0.511
  S_Delta := 0.035
  Sigma_FP := 0
  Q_dimless := |0.035|
  Q_value := |0.035| * 0.511
  Q_value_eq_dimless_mul_me := rfl
  Q_dimless_odd_ge_three := fun _ _ => rfl
  Q_dimless_even := fun heven => by
    exfalso
    revert heven
    decide
  Q_dimless_one := fun h1 => by omega

/-- `ParityRegimeSelectionContext` is inhabited. -/
theorem nonempty_parityRegimeSelectionContext :
    Nonempty ParityRegimeSelectionContext :=
  ⟨tritiumParityRegimeContext⟩

end QOU.ParticleInteractions
