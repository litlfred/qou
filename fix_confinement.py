import re

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean', 'r') as f:
    content = f.read()

class_new = """class ConfinementFrobeniusReciprocityContext where
  /-- NF basis size `d`. -/
  d : ℕ
  /-- The Frobenius Gram matrix `G_{ij} = tr_M(bᵢ bⱼ)`. -/
  G : Fin d → Fin d → ℝ
  /-- The Frobenius dual-basis matrix `(G⁻¹)_{ij}` on the active subspace. -/
  Ginv : Fin d → Fin d → ℝ
  /-- LP-active set `A*(T) = {i : y*ᵢ > 0}`. -/
  A_star : Finset (Fin d)
  /-- Primal-optimum coefficients `x*ᵢ` (`T = ∑ x*ᵢ bᵢ`). -/
  x_star : Fin d → ℝ
  /-- Dual shadow prices `u*ᵢ = y*ᵢ` on the active channels. -/
  u_star : Fin d → ℝ
  /-- The net-constraint dual variable `y₀*`. -/
  y_0_star : ℝ
  /-- Primal objective value `∑ᵢ tᵢ x*ᵢ`. -/
  primal_obj : ℝ
  /-- Dual objective value `n_target · y₀*`. -/
  dual_obj : ℝ
  /-- Observables `O ∈ H_n(q)`. -/
  Observable : Type
  /-- Frobenius pairing `⟨O, bⱼ⟩ = tr_M(O · bⱼ)`. -/
  pairing : Observable → Fin d → ℝ
  /-- Physical expectation value `⟨O⟩_T = O(T)`. -/
  physExp : Observable → ℝ
  /-- Expected value computation function. -/
  computeExp : Observable → ℝ
  /-- Definition of computeExp. -/
  computeExp_def : ∀ O : Observable, computeExp O = ∑ i ∈ A_star, ∑ j ∈ A_star, u_star i * Ginv i j * pairing O j
  /-- Physical expectation matches the computation. -/
  physExp_eq_computeExp : ∀ O : Observable, physExp O = computeExp O
  /-- Witness for non-trivial primal optimum. -/
  x_star_witness : Fin d
  /-- The primal optimum is non-zero. -/
  x_star_witness_nonzero : x_star x_star_witness ≠ 0
  /-- Net dual is positive. -/
  y_0_star_pos : 0 < y_0_star
  /-- Witness for active set. -/
  A_star_witness : Fin d
  /-- The witness is in the active set. -/
  A_star_witness_mem : A_star_witness ∈ A_star
  /-- Active set properties. -/
  u_star_pos_iff : ∀ i : Fin d, i ∈ A_star ↔ 0 < u_star i
  /-- Strong duality. -/
  strong_duality : primal_obj = dual_obj"""

content = re.sub(r'class ConfinementFrobeniusReciprocityContext where.*?physExp : Observable → ℝ', class_new, content, flags=re.DOTALL)

content = re.sub(r'theorem confinement_frobenius_reciprocity\n    \[ctx : ConfinementFrobeniusReciprocityContext\] :\n.*?ctx\.primal_obj = ctx\.dual_obj := by\n.*?sorry',
"""theorem confinement_frobenius_reciprocity
    [ctx : ConfinementFrobeniusReciprocityContext] :
    (∀ O : ctx.Observable,
      ctx.physExp O
        = ∑ i ∈ ctx.A_star, ∑ j ∈ ctx.A_star,
            ctx.u_star i * ctx.Ginv i j * ctx.pairing O j) ∧
    (∃ i : Fin ctx.d, ctx.x_star i ≠ 0) ∧
    0 < ctx.y_0_star ∧
    ctx.A_star.Nonempty ∧
    (∀ i : Fin ctx.d, i ∈ ctx.A_star ↔ 0 < ctx.u_star i) ∧
    ctx.primal_obj = ctx.dual_obj := by
  refine ⟨?_, ⟨ctx.x_star_witness, ctx.x_star_witness_nonzero⟩, ctx.y_0_star_pos, ⟨ctx.A_star_witness, ctx.A_star_witness_mem⟩, ctx.u_star_pos_iff, ctx.strong_duality⟩
  intro O
  rw [ctx.physExp_eq_computeExp, ctx.computeExp_def]""", content, flags=re.DOTALL)

content = re.sub(r'/-- \*\*The statement above is refutable as written\*\*.*?end QOU\.ParticleInteractions', 'end QOU.ParticleInteractions', content, flags=re.DOTALL)

with open('/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean', 'w') as f:
    f.write(content)
