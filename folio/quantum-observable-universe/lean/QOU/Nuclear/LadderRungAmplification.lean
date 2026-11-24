/-
# QOU.QBeta.LadderRungAmplification — the `c₃` gap between two Markov
# conventions is the cosine gap divided by `u³`, exactly.

Bean `qou-cds1`. Re-extracting the Q_β ladder at the convention-D Markov
parameter returns `c₃ ≈ −974.43` against convention C's `−2.069`, and that
figure is quoted as though it showed convention D breaking the channel.

Measured (`qbeta_alpha_required_c_vs_d_probe`, 4/4) it shows something much
narrower: the two conventions' `cos(α_eff)` differ by `6.0×10⁻⁴` *relative*,
and `1/u³ = 1.6×10⁶`, whose product `972.95` reproduces the observed gap
`972.36` to `0.06 %`. This file proves that this is not a numerical
coincidence at one anchor but an **identity**: the whole gap is the cosine
gap, amplified by exactly `u⁻³`.

Consequences worth stating, because they are what the identity buys:

* **The convention enters the rung only through the cosine**
  (`c3Of_congr`). Everything else in the extraction — `Q_A`, `b`, `u` — is
  built from the Hoefsmit couplings and never reads `z`.
* **Equal cosines ⟹ equal rungs** (`c3Of_sub_eq_zero_iff`), so a large `c₃`
  gap is *never* evidence of a large structural difference on its own; it is
  evidence of a cosine gap times `u⁻³`.
* **The amplification factor is exactly `u⁻³`** (`c3Of_sub_mul_u_cubed`), the
  same factor behind `σ(c_k) = σ_R / u^k` that already makes extracted `c_k`
  noise-dominated in this channel.

**Scope — what this does NOT say.** It does not derive `α`, which is asserted
in both frames and derived in neither; it proposes no phase, no `c_k` value,
and settles no convention. It does not license substituting `z_D` into the
C-frame functional form — `decayLadder_zC_threeRow_ne_zero` proves the ladder
must be re-derived under D, and that is untouched here. What it removes is
one specific inference: that `−974` measures how wrong convention D is. It
measures `u⁻³`.

Base ring: a generic `Field`, per §7c. Pure algebra — `cs` is an arbitrary
field element standing for `cos(α_eff)`, never `Real.cos` — so there is no
archimedean content and this specialises to `ℝ` for free.

-- Ref: [leitner2026] bean `qou-cds1`;
-- `computations/qbeta/qbeta_alpha_required_c_vs_d_probe.py`;
-- `computations/qbeta/qbeta_ck_cache.py` (the extraction this mirrors).
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {R : Type*} [Field R]

/-- The ladder's extracted third rung as a function of the N=1 cosine.

Mirrors `c3 = (Q_codata / Q_N2 − 1) / u³` with `Q_N2 = Q_A · cs · (1 − u²)`,
which is the extraction in `qbeta_ck_cache.py`. `cs` stands for
`cos(α_eff)`: it is the **only** place a Markov convention enters, since
`Q_A`, `b` and `u` are built from the Hoefsmit couplings. -/
noncomputable def c3Of (Qc Qa cs u : R) : R :=
  (Qc / (Qa * cs * (1 - u ^ 2)) - 1) / u ^ 3

/-- **The convention enters only through the cosine.** Two conventions with
the same `cos(α_eff)` give the same rung, whatever else differs about them. -/
theorem c3Of_congr (Qc Qa u : R) {c c' : R} (h : c = c') :
    c3Of Qc Qa c u = c3Of Qc Qa c' u := by
  rw [h]

/-- **The amplification identity.**

The gap between the rungs extracted under two conventions is the gap between
their cosine *reciprocals*, scaled by `Q_c/(Q_A(1−u²))` and divided by `u³`.
Nothing else contributes. -/
theorem c3Of_sub (Qc Qa cC cD u : R)
    (hQa : Qa ≠ 0) (hC : cC ≠ 0) (hD : cD ≠ 0) (hu : u ≠ 0)
    (hu2 : 1 - u ^ 2 ≠ 0) :
    c3Of Qc Qa cD u - c3Of Qc Qa cC u
      = Qc / (Qa * (1 - u ^ 2)) * (1 / cD - 1 / cC) / u ^ 3 := by
  unfold c3Of
  field_simp
  ring

/-- **The amplification factor is exactly `u⁻³`.**

Multiplying the rung gap by `u³` leaves a quantity with no `u`-scaling in it
at all beyond the `(1 − u²)` prefactor — so the `1/u³ = 1.6×10⁶` at the
substrate anchor is the entire magnification, not a coincidence of scale. -/
theorem c3Of_sub_mul_u_cubed (Qc Qa cC cD u : R)
    (hQa : Qa ≠ 0) (hC : cC ≠ 0) (hD : cD ≠ 0) (hu : u ≠ 0)
    (hu2 : 1 - u ^ 2 ≠ 0) :
    (c3Of Qc Qa cD u - c3Of Qc Qa cC u) * u ^ 3
      = Qc / (Qa * (1 - u ^ 2)) * (1 / cD - 1 / cC) := by
  rw [c3Of_sub Qc Qa cC cD u hQa hC hD hu hu2]
  field_simp

/-- **A rung gap is nonzero exactly when the cosines differ** (given a
nonvanishing overall scale). So an enormous `c₃` gap carries no information
beyond "the cosines differ" — the size of it is `u⁻³`, not evidence about the
conventions. -/
theorem c3Of_sub_eq_zero_iff (Qc Qa cC cD u : R)
    (hQa : Qa ≠ 0) (hC : cC ≠ 0) (hD : cD ≠ 0) (hu : u ≠ 0)
    (hu2 : 1 - u ^ 2 ≠ 0) (hQc : Qc ≠ 0) :
    c3Of Qc Qa cD u - c3Of Qc Qa cC u = 0 ↔ cD = cC := by
  rw [c3Of_sub Qc Qa cC cD u hQa hC hD hu hu2]
  constructor
  · intro h
    have hscale : Qc / (Qa * (1 - u ^ 2)) ≠ 0 := by
      simp [hQc, hQa, hu2]
    have h' : 1 / cD - 1 / cC = 0 := by
      have := div_eq_zero_iff.mp h
      rcases this with h1 | h2
      · rcases mul_eq_zero.mp h1 with hA | hB
        · exact absurd hA hscale
        · exact hB
      · exact absurd h2 (pow_ne_zero 3 hu)
    have h2 : (1 : R) / cD = 1 / cC := sub_eq_zero.mp h'
    simp only [one_div] at h2
    exact inv_injective h2
  · intro h
    rw [h]
    simp

end QOU.QBeta

