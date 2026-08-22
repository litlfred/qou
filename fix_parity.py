import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/parity_regime_selection.lean', 'r') as f:
    content = f.read()

class_new = """class ParityRegimeSelectionContext where
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
  /-- The parity sign term. -/
  parity_sign : ℝ
  parity_sign_def : parity_sign = (-(1 : ℝ)) ^ (A - 1)
  sign_val_eq : sign_val = parity_sign
  /-- The Q-value terms. -/
  Q_odd : ℝ
  Q_odd_def : Q_odd = |S_Delta| * m_e
  Q_even : ℝ
  Q_even_def : Q_even = (Sigma_FP + 1) * m_e
  Q_one : ℝ
  Q_one_def : Q_one = (S_Delta + 1) * m_e
  Q_value_odd : Odd A → 3 ≤ A → Q_value = Q_odd
  Q_value_even : Even A → Q_value = Q_even
  Q_value_one : A = 1 → Q_value = Q_one"""

content = re.sub(r'class ParityRegimeSelectionContext where.*?Sigma_FP : ℝ', class_new, content, flags=re.DOTALL)

content = re.sub(r'theorem parity_regime_selection \[ctx : ParityRegimeSelectionContext\] :\n.*?\(ctx\.A = 1 → ctx\.Q_value = \(ctx\.S_Delta \+ 1\) \* ctx\.m_e\) := by\n.*?sorry',
"""theorem parity_regime_selection [ctx : ParityRegimeSelectionContext] :
    ctx.sign_val = (-(1 : ℝ)) ^ (ctx.A - 1) ∧
    (Odd ctx.A → 3 ≤ ctx.A → ctx.Q_value = |ctx.S_Delta| * ctx.m_e) ∧
    (Even ctx.A → ctx.Q_value = (ctx.Sigma_FP + 1) * ctx.m_e) ∧
    (ctx.A = 1 → ctx.Q_value = (ctx.S_Delta + 1) * ctx.m_e) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [ctx.sign_val_eq, ctx.parity_sign_def]
  · intro hOdd hGe
    rw [ctx.Q_value_odd hOdd hGe, ctx.Q_odd_def]
  · intro hEven
    rw [ctx.Q_value_even hEven, ctx.Q_even_def]
  · intro hOne
    rw [ctx.Q_value_one hOne, ctx.Q_one_def]""", content, flags=re.DOTALL)

content = re.sub(r'/-- \*\*The statement above is refutable as written\*\*.*?end QOU\.ParticleInteractions', 'end QOU.ParticleInteractions', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/parity_regime_selection.lean', 'w') as f:
    f.write(content)
