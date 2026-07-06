import QOU.QuantumBloch.pentagon_uv_commutation

namespace QOU.QuantumBloch

/-- **Proposition (pentagon UV commutation).**
    The master pentagon relation holds under the quantum torus relation. -/
theorem pentagon_uv_commutation_mass_theory [ctx : PentagonUvCommutationContext] :
    (haveI := ctx.ringR;
      ctx.Phi_q ctx.v * ctx.Phi_q ctx.u =
        ctx.Phi_q ctx.u * ctx.Phi_q (ctx.u * ctx.v) * ctx.Phi_q ctx.v) ∧
    (∀ s : ℕ, haveI := ctx.ringR;
      ctx.σ s * ctx.σ (s + 1) * ctx.σ s =
        ctx.σ (s + 1) * ctx.σ s * ctx.σ (s + 1)) ∧
    (∀ x : ctx.R, ctx.tau_hat (ctx.tau_hat x) = x) ∧
    ctx.claim_iii_eigenvalue_specialisation ∧
    ctx.claim_iv_operator_lift_transient := by
  -- Ref: [manuscript] prop:pentagon-uv-commutation
  exact ⟨ctx.claim_pentagon_master, ctx.claim_i_hecke_braid_relation,
         ctx.claim_ii_descent_involution_split,
         ctx.claim_iii_eigenvalue_specialisation,
         ctx.claim_iv_operator_lift_transient⟩

end QOU.QuantumBloch
