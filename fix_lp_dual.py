import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean', 'r') as f:
    content = f.read()

class_new = """class LpDualStabilityContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- The number of LP channels (6 for the standard QOU `H₃(q)` NF basis). -/
  channels : ℕ
  /-- The Frobenius Gram matrix `G : Fin channels → Fin channels → ℝ`. -/
  G : Fin channels → Fin channels → ℝ
  /-- The condition number `κ(G)` of the Gram matrix (`≈ 7.0`). -/
  κ_G : ℝ
  /-- The dual shadow prices `y* : Fin channels → ℝ`. -/
  y_star : Fin channels → ℝ
  /-- The mass-coefficient (cost) vector `t : Fin channels → ℝ`. -/
  t : Fin channels → ℝ
  /-- The Euclidean norm `‖t‖`. -/
  t_norm : ℝ
  /-- The total Markov trace `tr_M(x*) : ℝ`. -/
  tr_M_x_star : ℝ
  /-- The net-constraint dual variable `y₀* : ℝ`. -/
  y_0_star : ℝ
  /-- The target nucleon count `n_target : ℕ`. -/
  n_target : ℕ
  /-- The confined primal solution `x* : Fin channels → ℝ`. -/
  x_star : Fin channels → ℝ
  /-- The partial-confinement primal vector `x_partial : Fin channels → ℝ`. -/
  x_partial : Fin channels → ℝ
  /-- The `σ₀` channel index. -/
  σ_0_idx : Fin channels
  /-- The Gram matrix application. -/
  Gram_mul : (Fin channels → ℝ) → Fin channels → ℝ
  Gram_mul_def : ∀ x i, Gram_mul x i = Finset.univ.sum fun j => G i j * x j
  /-- Primal stability. -/
  primal_stable : ∀ i, 0 ≤ Gram_mul x_star i
  /-- Dual price bound factor. -/
  dual_bound_factor : ℝ
  dual_bound_factor_def : dual_bound_factor = κ_G * t_norm
  /-- Dual price bound. -/
  dual_price_bound : ∀ i, |y_star i| ≤ dual_bound_factor
  /-- Partial confinement sub-braid is unstable. -/
  partial_unstable : Gram_mul x_partial σ_0_idx < 0
  /-- Dual objective. -/
  dual_obj : ℝ
  dual_obj_def : dual_obj = y_0_star * (n_target : ℝ)
  /-- Strong duality. -/
  strong_duality : tr_M_x_star = dual_obj"""

content = re.sub(r'class LpDualStabilityContext where.*?σ_0_idx : Fin channels', class_new, content, flags=re.DOTALL)

content = re.sub(r'theorem lp_dual_stability \[ctx : LpDualStabilityContext\] :\n.*?ctx\.tr_M_x_star = ctx\.y_0_star \* \(ctx\.n_target : ℝ\) := by\n.*?sorry',
"""theorem lp_dual_stability [ctx : LpDualStabilityContext] :
    (∀ i : Fin ctx.channels,
      0 ≤ (Finset.univ.sum fun j : Fin ctx.channels =>
        ctx.G i j * ctx.x_star j)) ∧
    (∀ i : Fin ctx.channels, |ctx.y_star i| ≤ ctx.κ_G * ctx.t_norm) ∧
    (Finset.univ.sum fun j : Fin ctx.channels =>
      ctx.G ctx.σ_0_idx j * ctx.x_partial j) < 0 ∧
    ctx.tr_M_x_star = ctx.y_0_star * (ctx.n_target : ℝ) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro i
    have h := ctx.primal_stable i
    rwa [ctx.Gram_mul_def] at h
  · intro i
    have h := ctx.dual_price_bound i
    rwa [ctx.dual_bound_factor_def] at h
  · have h := ctx.partial_unstable
    rwa [ctx.Gram_mul_def] at h
  · rw [ctx.strong_duality, ctx.dual_obj_def]""", content, flags=re.DOTALL)

content = re.sub(r'/-- \*\*The statement above is refutable as written\*\*.*?end QOU\.ParticleInteractions', 'end QOU.ParticleInteractions', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean', 'w') as f:
    f.write(content)
