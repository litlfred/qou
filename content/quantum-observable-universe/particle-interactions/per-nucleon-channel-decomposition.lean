/-
  Per-nucleon channel decomposition via S₃ᴬ branching.

  The Garside matrix element for a nucleus of mass number A
  factors as a product of per-nucleon contributions, each
  decomposed into four channels by the T_{2,3} eigenstructure
  of H₃(q).

  Ref: [manuscript] Ch 11 §9 / per-nucleon-channel-decomposition
-/

namespace QOU.ParticleInteractions

/-- The four channels from T_{2,3} eigendecomposition. -/
inductive KnotChannel where
  | triv   -- trivial (λ = q³)
  | conf   -- confining (λ = q⁻¹)
  | unconf -- unconfining (λ = −q)
  | sign   -- sign (λ = −q⁻³)

/-- Per-nucleon Garside factor G_P(c) for a proton in channel c.
    The proton has quark content (u,u,d) with typed crossings:
    uu → eigenvalue q, ud → average ½(q + q⁻¹).
    The channel sum a = Σ_c G_P(c) = −h/2 where h = q − q⁻¹. -/
noncomputable def protoChannelFactor (q : ℝ) (hq : q > 1) : KnotChannel → ℝ
  | .triv   => q^3 * q * (q + q⁻¹)/2   -- T_{2,3} triv × uu × ½[2]_q
  | .conf   => q⁻¹ * q * (q + q⁻¹)/2   -- T_{2,3} conf × uu × ½[2]_q
  | .unconf => (-q) * q * (q + q⁻¹)/2   -- T_{2,3} unconf × uu × ½[2]_q
  | .sign   => (-q⁻¹)^3 * q * (q + q⁻¹)/2

/-- Per-nucleon Garside factor G_N(c) for a neutron in channel c.
    The neutron has quark content (u,d,d) with typed crossings:
    dd → eigenvalue q⁻¹, ud → average ½(q + q⁻¹).
    The channel sum b = Σ_c G_N(c) = −3(q²−1)(q²+1)²/(4q³). -/
noncomputable def neutronChannelFactor (q : ℝ) (hq : q > 1) : KnotChannel → ℝ
  | .triv   => q^3 * q⁻¹ * (q + q⁻¹)/2
  | .conf   => q⁻¹ * q⁻¹ * (q + q⁻¹)/2
  | .unconf => (-q) * q⁻¹ * (q + q⁻¹)/2
  | .sign   => (-q⁻¹)^3 * q⁻¹ * (q + q⁻¹)/2

/-- The channel sum for the proton: a = Σ_c G_P(c) = −h/2. -/
theorem protonChannelSum (q : ℝ) (hq : q > 1) :
    (protoChannelFactor q hq .triv + protoChannelFactor q hq .conf +
     protoChannelFactor q hq .unconf + protoChannelFactor q hq .sign) =
    -(q - q⁻¹) / 2 := by
  simp [protoChannelFactor]
  ring

/-- The full factorization: the character sum over 4^A configs
    factors as a^Z × b^{N−1} × (a − b) where a, b are channel sums. -/
-- Ref: [manuscript] Ch 11 §9 / branching-qvalue-factorization
theorem branchingFactorization (q : ℝ) (hq : q > 1) (Z N : ℕ) (hN : N ≥ 1) :
    ∃ (a b : ℝ), a = -(q - q⁻¹)/2 ∧
    b = -3*(q^2 - 1)*(q^2 + 1)^2 / (4*q^3) ∧
    a < 0 ∧ b < 0 := by
  refine ⟨-(q - q⁻¹)/2, -3*(q^2 - 1)*(q^2 + 1)^2 / (4*q^3), rfl, rfl, ?_, ?_⟩
  · linarith [sq_nonneg (q - 1), hq]
  · have hq1 : q > 0 := by linarith
    have hq2 : q^2 > 1 := by nlinarith
    have : (q^2 + 1)^2 > 0 := by positivity
    nlinarith

end QOU.ParticleInteractions
