import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-
  Spectator normalization factor.

  S(Z_spec, N_spec) = a^{Z_spec} × b^{N_spec} where
  a = Σ_c G_P(c) = −h/2 and b = Σ_c G_N(c).

  Ref: [leitner2026] Ch 11 §9 / spectator-normalization
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
  have hq0 : q > 0 := by linarith
  constructor
  · -- a = -(q - q⁻¹)/2 < 0 for q > 1
    unfold protonChannelSum'
    have hinv : q⁻¹ < 1 := by
      rw [inv_lt_one₀ hq0]
      exact hq
    have hge : q⁻¹ < q := by linarith
    have : q - q⁻¹ > 0 := by linarith
    linarith
  · -- b < 0: (q²-1) > 0 and (q²+1)² > 0 and q³ > 0
    unfold neutronChannelSum
    have hq2 : q^2 > 1 := by nlinarith
    have hpos2 : (q^2 + 1)^2 > 0 := by positivity
    have hq3 : q^3 > 0 := by positivity
    have hnum : -3 * (q^2 - 1) * (q^2 + 1)^2 < 0 := by nlinarith
    rw [div_neg_iff]
    right
    exact ⟨hnum, by positivity⟩

-- Helper: a negative real raised to a natural power is positive iff the exponent is even.
private lemma neg_pow_pos_iff {x : ℝ} (hx : x < 0) (n : ℕ) :
    0 < x ^ n ↔ Even n := by
  constructor
  · intro hpos
    by_contra hodd
    rw [Nat.not_even_iff_odd] at hodd
    have : x ^ n < 0 := hodd.pow_neg hx
    linarith
  · intro heven
    exact heven.pow_pos (ne_of_lt hx)

/-- The parity regime: for q > 1, both channel sums are negative,
    so sign(a^Z × b^N) = (−1)^{Z+N}. The spectator product is
    positive when Z + N is even (odd A in beta decay). -/
theorem spectatorSignPattern (q : ℝ) (hq : q > 1) (Z N : ℕ) :
    (0 < spectatorNorm q Z N) ↔ Even (Z + N) := by
  obtain ⟨ha, hb⟩ := spectatorSign q hq
  simp only [spectatorNorm]
  -- spectatorNorm = a^Z * b^N where a < 0 and b < 0.
  -- a^Z * b^N > 0 iff both powers are the same sign, i.e. Z and N have the
  -- same parity, i.e. Z+N is even.
  constructor
  · intro hpos
    by_contra hne
    rw [Nat.not_even_iff_odd] at hne
    -- Z+N odd ⇒ exactly one of Z, N is odd; the corresponding factor is < 0,
    -- the other > 0, so the product is < 0, contradicting hpos.
    rcases mul_pos_iff.mp hpos with ⟨hZ, hN⟩ | ⟨hZ, hN⟩
    · -- both factors positive ⇒ both exponents even ⇒ Z+N even
      have hZe : Even Z := (neg_pow_pos_iff ha Z).mp hZ
      have hNe : Even N := (neg_pow_pos_iff hb N).mp hN
      exact (Nat.not_even_iff_odd.mpr hne) (hZe.add hNe)
    · -- both factors negative ⇒ both exponents odd ⇒ Z+N even
      have hZo : Odd Z := by
        by_contra h
        rw [Nat.not_odd_iff_even] at h
        have : 0 < (protonChannelSum' q) ^ Z := (neg_pow_pos_iff ha Z).mpr h
        linarith
      have hNo : Odd N := by
        by_contra h
        rw [Nat.not_odd_iff_even] at h
        have : 0 < (neutronChannelSum q) ^ N := (neg_pow_pos_iff hb N).mpr h
        linarith
      exact (Nat.not_even_iff_odd.mpr hne) (hZo.add_odd hNo)
  · intro heven
    rw [Nat.even_add] at heven
    by_cases hZe : Even Z
    · -- both even: a^Z > 0 and b^N > 0, product positive
      have hNe : Even N := heven.mp hZe
      exact mul_pos ((neg_pow_pos_iff ha Z).mpr hZe) ((neg_pow_pos_iff hb N).mpr hNe)
    · -- both odd: a^Z < 0 and b^N < 0, product positive
      have hZo : Odd Z := Nat.not_even_iff_odd.mp hZe
      have hNe : ¬ Even N := fun hn => hZe (heven.mpr hn)
      have hNo : Odd N := Nat.not_even_iff_odd.mp hNe
      exact mul_pos_of_neg_of_neg (hZo.pow_neg ha) (hNo.pow_neg hb)

end QOU.ParticleInteractions
