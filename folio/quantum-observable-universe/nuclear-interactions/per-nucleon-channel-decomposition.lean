/-
  Per-nucleon channel decomposition via S₃ᴬ branching.

  The Garside matrix element for a nucleus of mass number A
  factors as a product of per-nucleon contributions, each
  decomposed into four channels by the T_{2,3} eigenstructure
  of H₃(q).

  Ref: [leitner2026] Ch 11 §9 / per-nucleon-channel-decomposition
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

namespace QOU.ParticleInteractions

/-- The four channels from T_{2,3} eigendecomposition. -/
inductive KnotChannel where
  | triv   -- trivial (λ = q³)
  | conf   -- confining (λ = q⁻¹)
  | unconf -- unconfining (λ = −q)
  | sign   -- sign (λ = −q⁻³)

/-- The q-bracket `[2]_q = q + q⁻¹`. -/
noncomputable def qBracket2 (q : ℝ) : ℝ := q + q⁻¹


/-- **Bridge to the canonical bracket.** The longhand `q + q⁻¹` is this site's
body and its proofs use it, so the consolidation is the identity, not an alias.
Conditional: the two agree away from `q − q⁻¹ = 0`. -/
theorem qBracket2_eq_canonical (q : ℝ) (h : q - q⁻¹ ≠ 0) :
    qBracket2 q = QOU.QInteger.qIntBal q 2 := (QOU.QInteger.qIntBal_two q h).symm

/-- Proton symmetric (trivial) channel factor, explicit from the
    per-nucleon table: `q · (½[2]_q)²`. -/
noncomputable def gP_sym (q : ℝ) : ℝ := q * (qBracket2 q / 2)^2

/-- Proton alternating (sign) channel factor: `(−q⁻¹) · (½[2]_q)²`. -/
noncomputable def gP_alt (q : ℝ) : ℝ := (-q⁻¹) * (qBracket2 q / 2)^2

/-- Neutron symmetric (trivial) channel factor: `q⁻¹ · (½[2]_q)²`. -/
noncomputable def gN_sym (q : ℝ) : ℝ := q⁻¹ * (qBracket2 q / 2)^2

/-- Neutron alternating (sign) channel factor: `(−q) · (½[2]_q)²`. -/
noncomputable def gN_alt (q : ℝ) : ℝ := (-q) * (qBracket2 q / 2)^2

/-- **Proton channel sum** `a = Σ_c G_P(c) = −h/2` (`h = q − q⁻¹`),
    stated conditionally on the standard-channel summed expectation
    `stdP = ⟨v₁|Δ₃|v₁⟩ + ⟨v₂|Δ₃|v₂⟩`.  The two standard-channel values
    are the quadratic-root eigendata of `e⁻ = σ₀σ₁σ₀` in the 2-dim
    standard representation — not elementary in `q` — and are computed in
    `def:typed-crossing-operator`; this lemma verifies that, summed with
    the explicit symmetric/alternating factors, they give `−h/2`
    (§3b-cond conditional pattern). -/
-- Ref: [leitner2026] def:typed-crossing-operator (standard-channel Δ₃ eigendata)
theorem protonChannelSum (q : ℝ) (hq : q ≠ 0) (stdP : ℝ)
    (hstd : stdP = -(q - q⁻¹) * (2 + (q + q⁻¹)^2) / 4) :
    gP_sym q + stdP + gP_alt q = -(q - q⁻¹) / 2 := by
  subst hstd
  simp only [gP_sym, gP_alt, qBracket2]
  field_simp
  ring

/-- **Neutron channel sum** `b = Σ_c G_N(c) = −3(q²−1)(q²+1)²/(4q³)`,
    stated conditionally on the standard-channel summed expectation
    `stdN` (computed in `def:typed-crossing-operator`). -/
-- Ref: [leitner2026] def:typed-crossing-operator (standard-channel Δ₃ eigendata)
theorem neutronChannelSum (q : ℝ) (hq : q ≠ 0) (stdN : ℝ)
    (hstd : stdN = -(q^2 - 1)*(q^2 + 1)^2 / (2*q^3)) :
    gN_sym q + stdN + gN_alt q = -3*(q^2 - 1)*(q^2 + 1)^2 / (4*q^3) := by
  subst hstd
  simp only [gN_sym, gN_alt, qBracket2]
  field_simp
  ring

/-- Both channel sums are strictly negative for `q > 1` (`a, b < 0`),
    the sign input to the branching factorization `a^Z · b^{N−1} · (a − b)`. -/
-- Ref: [leitner2026] Ch 11 §9 / branching-qvalue-factorization
theorem branchingFactorizationSigns (q : ℝ) (hq : q > 1) :
    (-(q - q⁻¹)/2 : ℝ) < 0 ∧ -3*(q^2 - 1)*(q^2 + 1)^2 / (4*q^3) < 0 := by
  have hq0 : q > 0 := by linarith
  have hqinv : q⁻¹ < q := by
    rw [inv_lt_iff_one_lt_mul₀ hq0]; nlinarith
  refine ⟨by linarith, ?_⟩
  have h1 : q^2 - 1 > 0 := by nlinarith
  have hpos : (0:ℝ) < 3*(q^2 - 1)*(q^2 + 1)^2 / (4*q^3) :=
    div_pos (mul_pos (mul_pos (by norm_num) h1) (by positivity)) (by positivity)
  have heq : -3*(q^2 - 1)*(q^2 + 1)^2 / (4*q^3)
      = -(3*(q^2 - 1)*(q^2 + 1)^2 / (4*q^3)) := by ring
  rw [heq]; linarith

end QOU.ParticleInteractions
