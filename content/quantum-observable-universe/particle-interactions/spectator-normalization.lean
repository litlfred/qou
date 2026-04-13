/-
  Spectator normalization factor.

  S(Z_spec, N_spec) = a^{Z_spec} × b^{N_spec} where
  a = Σ_c G_P(c) = −h/2 and b = Σ_c G_N(c).

  Ref: [manuscript] Ch 11 §9 / spectator-normalization
-/

namespace QOU.ParticleInteractions

/-- The proton channel sum: a = −(q − q⁻¹)/2. -/
noncomputable def protonChannelSum' (q : ℝ) : ℝ := -(q - q⁻¹) / 2

/-- The neutron channel sum: b = −3(q²−1)(q²+1)²/(4q³). -/
noncomputable def neutronChannelSum (q : ℝ) : ℝ :=
  -3 * (q^2 - 1) * (q^2 + 1)^2 / (4 * q^3)

/-- Spectator normalization: product of per-nucleon channel sums
    for unchanged nucleons in a beta decay.
    S(Z, N-1) = a^Z × b^{N-1}. -/
noncomputable def spectatorNorm (q : ℝ) (Z_spec N_spec : ℕ) : ℝ :=
  (protonChannelSum' q) ^ Z_spec * (neutronChannelSum q) ^ N_spec

/-- Both channel sums are negative for q > 1, giving the
    fermionic sign: sign(a^Z × b^{N-1}) = (−1)^{A−1}. -/
theorem spectatorSign (q : ℝ) (hq : q > 1) :
    protonChannelSum' q < 0 ∧ neutronChannelSum q < 0 := by
  constructor
  · -- a = -(q - q⁻¹)/2 < 0 for q > 1
    simp [protonChannelSum']
    have : q - q⁻¹ > 0 := by
      have hq0 : q > 0 := by linarith
      rw [inv_eq_one_div]
      have : 1/q < q := by rw [div_lt_iff hq0]; nlinarith
      linarith
    linarith
  · -- b < 0: (q²-1) > 0 and (q²+1)² > 0 and q³ > 0
    simp [neutronChannelSum]
    have hq0 : q > 0 := by linarith
    have hq2 : q^2 > 1 := by nlinarith
    have : (q^2 + 1)^2 > 0 := by positivity
    have : q^3 > 0 := by positivity
    nlinarith

/-- The parity regime: for q > 1, both channel sums are negative,
    so sign(a^Z × b^N) = (−1)^{Z+N}. The spectator product is
    positive when Z + N is even (odd A in beta decay).
    Ref: [manuscript] Ch 11 §9 / parity-regime-selection -/
-- Ref: [manuscript] Ch 11 §9 / parity-regime-selection
-- Proof: a < 0 and b < 0 (spectatorSign), so a^Z × b^N has sign (−1)^{Z+N}.
-- Positive iff Z+N even. Requires Even.neg_pow / Odd.neg_pow from Mathlib.
-- The mathematical content is: sign(spectatorNorm) = (−1)^{A−1} where A = Z+N+1.
-- Lean verification deferred to lean-build-fix pass (Mathlib API alignment).
theorem spectatorSignPattern (q : ℝ) (hq : q > 1) (Z N : ℕ) :
    (0 < spectatorNorm q Z N) ↔ Even (Z + N) := by
  obtain ⟨ha, hb⟩ := spectatorSign q hq
  simp only [spectatorNorm, protonChannelSum', neutronChannelSum]
  -- Ref: [kock2004] — sign of product of negative reals raised to natural powers
  sorry

end QOU.ParticleInteractions
