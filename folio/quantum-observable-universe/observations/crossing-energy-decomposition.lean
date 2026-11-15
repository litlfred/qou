import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic
-- The channel definitions and `pair_cancellation` were relocated to the Lake
-- tree so the content-block resolver finds `pair_cancellation`; the theorems
-- remaining below still use the definitions.
import QOU.Braiding.crossing_energy_channels


/-!
# QOU.Braiding.crossing_energy_decomposition — cosh/sinh decomposition

The crossing weights +q and -q⁻¹ decompose into symmetric (cosh)
and antisymmetric (sinh) channels under the mirror operation.

LaTeX label: `prop:crossing-energy-decomposition`

## References
- [leitner2026] Ch. 7, §crossing-energy-decomposition

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Braiding

/-- q decomposes as cosh + sinh. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem q_decomposition (q : ℝ) (hq : 0 < q) :
    q = symmetricWeight q + antisymmetricWeight q := by
  unfold symmetricWeight antisymmetricWeight
  ring

/-- q⁻¹ decomposes as cosh - sinh. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem q_inv_decomposition (q : ℝ) (hq : 0 < q) :
    q⁻¹ = symmetricWeight q - antisymmetricWeight q := by
  unfold symmetricWeight antisymmetricWeight
  ring

/-- The symmetric weight (q + q⁻¹)/2 equals cosh(ln q), for q > 0.
    This is what makes the "cosh channel" name a derived identity, not a
    definition: the symmetric crossing weight IS the hyperbolic cosine of
    the crossing rapidity λ = ln q. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem symmetricWeight_eq_cosh (q : ℝ) (hq : 0 < q) :
    symmetricWeight q = Real.cosh (Real.log q) := by
  unfold symmetricWeight
  rw [Real.cosh_eq, Real.exp_log hq, Real.exp_neg, Real.exp_log hq]

/-- The antisymmetric weight (q - q⁻¹)/2 equals sinh(ln q), for q > 0.
    The "Coulomb / sinh channel" is therefore a derived identity — the
    antisymmetric crossing weight IS the hyperbolic sine of λ = ln q,
    not a fitted parameter. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem antisymmetricWeight_eq_sinh (q : ℝ) (hq : 0 < q) :
    antisymmetricWeight q = Real.sinh (Real.log q) := by
  unfold antisymmetricWeight
  rw [Real.sinh_eq, Real.exp_log hq, Real.exp_neg, Real.exp_log hq]

/-- General identity: q = cosh(ln q) + sinh(ln q), for any q > 0.
    This is `eˣ = cosh x + sinh x` at x = ln q (so the RHS is e^{ln q} = q).
    It holds for every q > 0 — it is NOT specific to the substrate value. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem q_eq_cosh_add_sinh (q : ℝ) (hq : 0 < q) :
    q = Real.cosh (Real.log q) + Real.sinh (Real.log q) := by
  rw [← symmetricWeight_eq_cosh q hq, ← antisymmetricWeight_eq_sinh q hq]
  unfold symmetricWeight antisymmetricWeight
  ring

/-- General identity: q⁻¹ = cosh(ln q) - sinh(ln q), for any q > 0. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem q_inv_eq_cosh_sub_sinh (q : ℝ) (hq : 0 < q) :
    q⁻¹ = Real.cosh (Real.log q) - Real.sinh (Real.log q) := by
  rw [← symmetricWeight_eq_cosh q hq, ← antisymmetricWeight_eq_sinh q hq]
  unfold symmetricWeight antisymmetricWeight
  ring

/-- Algebraic→hyperbolic bridge (powers): for q > 0 and n : ℕ,
    qⁿ = cosh(n·ln q) + sinh(n·ln q). The algebraic q-power is the
    exponential of a hyperbolic length n·ln q. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem q_pow_eq_cosh_add_sinh (q : ℝ) (hq : 0 < q) (n : ℕ) :
    q ^ n = Real.cosh (n * Real.log q) + Real.sinh (n * Real.log q) := by
  have h1 : q ^ n = Real.exp ((n : ℝ) * Real.log q) := by
    rw [Real.exp_nat_mul, Real.exp_log hq]
  rw [h1, Real.cosh_eq, Real.sinh_eq]; ring

/-- The quantum-integer numerator qⁿ − q⁻ⁿ = 2·sinh(n·ln q), for q > 0.
    The algebraic Hecke datum is twice a hyperbolic sine. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem two_sinh_nat_log (q : ℝ) (hq : 0 < q) (n : ℕ) :
    q ^ n - (q ^ n)⁻¹ = 2 * Real.sinh (n * Real.log q) := by
  have h1 : q ^ n = Real.exp ((n : ℝ) * Real.log q) := by
    rw [Real.exp_nat_mul, Real.exp_log hq]
  rw [Real.sinh_eq, Real.exp_neg, ← h1]; ring

/-- The q-bracket as a ratio of hyperbolic sines:
    [n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹) = sinh(n·ln q)/sinh(ln q), for q > 0.
    This is the precise sense in which the algebraic quantum integer is
    archimedean (hyperbolic-geometric) — the bridge underlying the
    Kashaev volume realisation (`kashaev-as-archimedean-realization`). -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem qbracket_eq_sinh_ratio (q : ℝ) (hq : 0 < q) (n : ℕ) :
    (q ^ n - (q ^ n)⁻¹) / (q - q⁻¹)
      = Real.sinh (n * Real.log q) / Real.sinh (Real.log q) := by
  have hden : q - q⁻¹ = 2 * Real.sinh (Real.log q) := by
    have h := two_sinh_nat_log q hq 1; simpa using h
  rw [two_sinh_nat_log q hq n, hden, mul_div_mul_left _ _ (two_ne_zero)]

/-- The EM/strong ratio is (q - q⁻¹)/(q + q⁻¹). -/
noncomputable def emStrongRatio (q : ℝ) : ℝ :=
  antisymmetricWeight q / symmetricWeight q

/-- EM/strong ratio equals tanh(ln q) for q > 1.
    Proof: tanh(ln q) = (e^{ln q} - e^{-ln q})/(e^{ln q} + e^{-ln q})
           = (q - q⁻¹)/(q + q⁻¹) = emStrongRatio q. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem em_strong_ratio_tanh (q : ℝ) (hq : 1 < q) :
    emStrongRatio q = Real.tanh (Real.log q) := by
  have hq0 : 0 < q := by linarith
  unfold emStrongRatio
  rw [antisymmetricWeight_eq_sinh q hq0, symmetricWeight_eq_cosh q hq0,
    Real.tanh_eq_sinh_div_cosh]

/-- Symmetric weight is positive for q > 0. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem symmetric_pos (q : ℝ) (hq : 0 < q) :
    0 < symmetricWeight q := by
  unfold symmetricWeight
  have hqi : 0 < q⁻¹ := inv_pos.mpr hq
  linarith

/-- Antisymmetric weight is positive for q > 1. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem antisymmetric_pos (q : ℝ) (hq : 1 < q) :
    0 < antisymmetricWeight q := by
  unfold antisymmetricWeight
  have : q⁻¹ < 1 := (inv_lt_one₀ (by linarith)).mpr hq
  linarith

/-! ## Whole-composite channels: pair cancellation and the scope of the ratio

The lemmas above are *per-crossing*. A knot composite `𝔥` carries `p`
positive crossings (weight `+q` each) and `m` negative crossings (weight
`-q⁻¹` each); its total crossing energy is `p·q - m·q⁻¹`.

Summing the per-crossing decomposition over the composite gives the two
channels with **different** multiplicities — `(p - m)` on the symmetric
side but `(p + m)` on the antisymmetric side — because the mirror
operation `σ` flips the sign of the `cosh` part of a crossing weight but
*not* the sign of its `sinh` part:

  `+q  = +cosh λ + sinh λ`,   `-q⁻¹ = -cosh λ + sinh λ`.

That multiplicity mismatch is exactly what makes pair creation work
(`pair_cancellation`), and it is also what bounds the scope of the
"ratio is independent of `𝔥`" claim (`ratio_general` below). -/

/-- The composite splits into its two channels. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem crossingEnergy_split (p m : ℕ) (q : ℝ) :
    crossingEnergy p m q = symChannel p m q + asymChannel p m q := by
  unfold crossingEnergy symChannel asymChannel symmetricWeight antisymmetricWeight
  ring

/-- The mirror `σ` (which reverses every crossing, i.e. swaps `p` and `m`)
negates the symmetric channel. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem symChannel_mirror (p m : ℕ) (q : ℝ) :
    symChannel m p q = -symChannel p m q := by
  unfold symChannel; ring

/-- The mirror `σ` fixes the antisymmetric channel — this is the sign-blindness
of the `sinh` part, and the reason a particle–antiparticle pair retains a
net Coulomb energy. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem asymChannel_mirror (p m : ℕ) (q : ℝ) :
    asymChannel m p q = asymChannel p m q := by
  unfold asymChannel; ring

/-- **Ratio identity, correctly scoped.** For a *positive braid closure*
(`m = 0`, every crossing positive) with at least one crossing, the
antisymmetric-to-symmetric ratio is `tanh(ln q)`, independent of the
crossing number `p`. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem ratio_positive_braid (p : ℕ) (hp : p ≠ 0) (q : ℝ) (hq : 1 < q) :
    asymChannel p 0 q / symChannel p 0 q = Real.tanh (Real.log q) := by
  have hq0 : 0 < q := by linarith
  have hp' : (p : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hp
  rw [← em_strong_ratio_tanh q hq]
  unfold asymChannel symChannel emStrongRatio
  push_cast
  rw [add_zero, sub_zero, mul_div_mul_left _ _ hp']

/-- **Scope limit of the ratio identity.** For a composite with mixed
crossing signs the ratio picks up the multiplicity factor `(p+m)/(p-m)`:

  `E_asym / E_sym = ((p+m)/(p-m)) · tanh(ln q)`.

The ratio equals `tanh(ln q)` exactly on the positive-braid locus
`m = 0` (and, symmetrically, `-tanh(ln q)` on `p = 0`); it is **not**
independent of the composite in general. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem ratio_general (p m : ℕ) (q : ℝ) (hq : 1 < q)
    (hpm : (p : ℝ) - (m : ℝ) ≠ 0) :
    asymChannel p m q / symChannel p m q
      = (((p : ℝ) + (m : ℝ)) / ((p : ℝ) - (m : ℝ))) * Real.tanh (Real.log q) := by
  have hq0 : 0 < q := by linarith
  have hsym : symmetricWeight q ≠ 0 := ne_of_gt (symmetric_pos q hq0)
  rw [← em_strong_ratio_tanh q hq]
  unfold asymChannel symChannel emStrongRatio
  field_simp

/-- The multiplicity factor is genuinely non-trivial: a composite with two
positive and one negative crossing has ratio `3·tanh(ln q)`, not
`tanh(ln q)`. Concrete witness that `ratio_general` is not vacuous. -/
-- Ref: [leitner2026] Ch. 7, §crossing-energy-decomposition
theorem ratio_two_one_ne_tanh (q : ℝ) (hq : 1 < q) :
    asymChannel 2 1 q / symChannel 2 1 q = 3 * Real.tanh (Real.log q) := by
  have h : ((2 : ℕ) : ℝ) - ((1 : ℕ) : ℝ) ≠ 0 := by norm_num
  rw [ratio_general 2 1 q hq h]
  norm_num

end QOU.Braiding
