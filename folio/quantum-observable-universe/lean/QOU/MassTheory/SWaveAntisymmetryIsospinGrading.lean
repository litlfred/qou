/-!
# S-Wave Antisymmetry and Isospin vs T3 Grading (`qou-7nwg`)

This module formalizes the structural resolution of `qou-7nwg`:

1. **S-wave spin-isospin lock (`s_wave_spin_isospin_bijection`):**
   For two nucleons in a relative S-wave (`L = 0`), generalized fermion antisymmetry
   constrains the total spin `S in {0, 1}` and total isospin `T in {0, 1}` to satisfy
   `S + T = 1`. Consequently, `S = 1 <-> T = 0` (`3S1` deuteron channel) and
   `S = 0 <-> T = 1` (`1S0` dinucleon channels), so grading by total isospin `T`
   in the 2-strand algebra separates the `3S1` and `1S0` channels without requiring
   an explicit spinor `C^2` factor.

2. **Sign flip across `T` vs unbound modulation across `T3` (`isospin_t_flips_sign_while_t3_stays_unbound`):**
   Empirical two-nucleon scattering lengths (`a` in units of `10^-3 fm`) satisfy:
   - `a(np, T = 0, T3 = 0) = +5419` (`+5.419 fm`, bound deuteron),
   - `a(pp, T = 1, T3 = +1) = -17300` (`-17.3 fm`, unbound),
   - `a(nn, T = 1, T3 = -1) = -18900` (`-18.9 fm`, unbound),
   - `a(np, T = 1, T3 = 0) = -23740` (`-23.740 fm`, unbound).
   Thus the sign flips across `T`, whereas all three `T3` projections at `T = 1`
   remain strictly negative (unbound).

3. **Charge-independence breaking vs isospin jump (`cib_spread_within_t1_smaller_than_isospin_jump`):**
   Within `T = 1`, the charge-independence-breaking spread across `T3` is
   `a(pp, T=1) - a(np, T=1) = 6440` (`6.44 fm`), which is more than `4x` smaller
   than the isospin jump `a(np, T=0) - a(np, T=1) = 29159` (`29.159 fm`).
-/

namespace QOU.MassTheory.SWaveAntisymmetryIsospinGrading

/-- Relative S-wave (`L = 0`) fermion antisymmetry constraint `S in {0, 1}`, `T in {0, 1}`, `S + T = 1`. -/
def sWaveAntisymmetric (S T : Int) : Prop :=
  (S = 0 ∨ S = 1) ∧ (T = 0 ∨ T = 1) ∧ S + T = 1

/-- Two-nucleon S-wave scattering length in units of `10^-3 fm` indexed by `(T, T3)`. -/
def scatteringLengthScaled (T T3 : Int) : Int :=
  if T = 0 then 5419
  else if T3 = 1 then -17300
  else if T3 = -1 then -18900
  else -23740

/-- On any relative S-wave two-nucleon state (`sWaveAntisymmetric S T`), spin triplet
    `S = 1` is equivalent to isospin singlet `T = 0`, and spin singlet `S = 0` is
    equivalent to isospin triplet `T = 1` (`qou-7nwg`). -/
theorem s_wave_spin_isospin_bijection
    (S T : Int) (hanti : sWaveAntisymmetric S T) :
    (S = 1 ↔ T = 0) ∧ (S = 0 ↔ T = 1) := by
  have hsum : S + T = 1 := hanti.2.2
  have h10 : S = 1 ↔ T = 0 := by
    omega
  have h01 : S = 0 ↔ T = 1 := by
    omega
  exact ⟨h10, h01⟩

/-- The scattering length is strictly positive at `T = 0` (`+5419`) and strictly
    negative across all three `T3 in {1, -1, 0}` projections at `T = 1` (`qou-7nwg`). -/
theorem isospin_t_flips_sign_while_t3_stays_unbound :
    scatteringLengthScaled 0 0 > 0 ∧
    scatteringLengthScaled 1 1 < 0 ∧
    scatteringLengthScaled 1 (-1) < 0 ∧
    scatteringLengthScaled 1 0 < 0 := by
  have ht0 : scatteringLengthScaled 0 0 > 0 := by
    unfold scatteringLengthScaled
    omega
  have ht1_pp : scatteringLengthScaled 1 1 < 0 := by
    unfold scatteringLengthScaled
    omega
  have ht1_nn : scatteringLengthScaled 1 (-1) < 0 := by
    unfold scatteringLengthScaled
    omega
  have ht1_np : scatteringLengthScaled 1 0 < 0 := by
    unfold scatteringLengthScaled
    omega
  exact ⟨ht0, ht1_pp, ht1_nn, ht1_np⟩

/-- The `T = 1` charge-independence-breaking spread across `T3` (`6440` in `10^-3 fm`)
    is more than `4x` smaller than the `T = 0` vs `T = 1` jump (`29159`) (`qou-7nwg`). -/
theorem cib_spread_within_t1_smaller_than_isospin_jump :
    scatteringLengthScaled 1 1 - scatteringLengthScaled 1 0 = 6440 ∧
    scatteringLengthScaled 0 0 - scatteringLengthScaled 1 0 = 29159 ∧
    (scatteringLengthScaled 0 0 - scatteringLengthScaled 1 0) >
      4 * (scatteringLengthScaled 1 1 - scatteringLengthScaled 1 0) := by
  have hcib : scatteringLengthScaled 1 1 - scatteringLengthScaled 1 0 = 6440 := by
    unfold scatteringLengthScaled
    omega
  have hjump : scatteringLengthScaled 0 0 - scatteringLengthScaled 1 0 = 29159 := by
    unfold scatteringLengthScaled
    omega
  have hgt : (scatteringLengthScaled 0 0 - scatteringLengthScaled 1 0) >
      4 * (scatteringLengthScaled 1 1 - scatteringLengthScaled 1 0) := by
    rw [hcib, hjump]
    omega
  exact ⟨hcib, hjump, hgt⟩

end QOU.MassTheory.SWaveAntisymmetryIsospinGrading
