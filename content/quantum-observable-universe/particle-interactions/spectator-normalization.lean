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
-- Helper: a negative real raised to a natural power is positive iff the exponent is even.
private lemma neg_pow_pos_iff {x : ℝ} (hx : x < 0) (n : ℕ) :
    0 < x ^ n ↔ Even n := by
  constructor
  · intro hpos
    by_contra hodd
    rw [Nat.not_even_iff_odd] at hodd
    exact not_lt.mpr (le_of_lt hpos |>.antisymm (le_of_lt (Odd.neg_pow hodd ▸
      neg_neg_of_neg (pow_neg hx n |>.elim (fun h => absurd hpos (not_lt.mpr (le_of_lt h)))
        (fun h => absurd hpos (not_lt.mpr (le_of_eq h.symm))))))) |> absurd hpos ∘ ne_of_gt
    -- Simplification: use Even.pow_pos and Odd.pow_neg
  · intro heven
    exact Even.pow_pos heven hx

-- Helper: product of two positive reals is positive.
private lemma mul_pos_of_pos {a b : ℝ} (ha : 0 < a) (hb : 0 < b) : 0 < a * b :=
  mul_pos ha hb

theorem spectatorSignPattern (q : ℝ) (hq : q > 1) (Z N : ℕ) :
    (0 < spectatorNorm q Z N) ↔ Even (Z + N) := by
  obtain ⟨ha, hb⟩ := spectatorSign q hq
  simp only [spectatorNorm]
  -- spectatorNorm = a^Z * b^N where a < 0 and b < 0.
  -- a^Z * b^N > 0 iff both powers are the same sign,
  -- which happens iff Z and N have the same parity, i.e. Z+N is even.
  constructor
  · intro hpos
    -- If the product is positive, both factors have the same sign.
    -- Since a < 0 and b < 0, a^Z > 0 iff Even Z, a^Z < 0 iff Odd Z (same for b^N).
    -- Product positive => both even or both odd => Z+N even.
    by_contra hne
    rw [Nat.not_even_iff_odd] at hne
    -- Z+N odd means exactly one of Z, N is odd.
    obtain ⟨hZ_even, hN_odd⟩ | ⟨hZ_odd, hN_even⟩ := Nat.Even.add_odd_or_odd_add hne
    all_goals {
      have := mul_pos_iff.mp hpos
      simp only [Even.pow_pos, Odd.pow_neg, *] at this
      · linarith
    }
  · intro heven
    -- Z+N even means Z and N have the same parity.
    -- Both even: a^Z > 0 and b^N > 0, product positive.
    -- Both odd: a^Z < 0 and b^N < 0, product positive.
    obtain ⟨hZe, hNe⟩ | ⟨hZo, hNo⟩ := Nat.even_add.mp heven |>.elim
      (fun ⟨l, r⟩ => Or.inl ⟨l, r⟩) (fun ⟨l, r⟩ => Or.inr ⟨l, r⟩)
    · exact mul_pos (Even.pow_pos hZe ha) (Even.pow_pos hNe hb)
    · exact mul_pos_of_neg_of_neg (Odd.pow_neg hZo ha) (Odd.pow_neg hNo hb)


/-- **def:spectator-normalization** — placeholder stub; full definition TBD. -/
structure SpectatorNormalization where
  witness : ℝ
  witness_pos : 0 < witness
end QOU.ParticleInteractions
