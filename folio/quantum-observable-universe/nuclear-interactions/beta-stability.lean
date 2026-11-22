import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Braiding.beta_stability — Beta-stability line from ∂L_bind/∂p = 0

The stable proton number for a nucleus of mass number A is
p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)), derived from extremizing
the Skein binding Lagrangian under beta variation.

LaTeX label: `prop:beta-stability`

## References
- [leitner2026] §4/beta-stability

**Ground ring (Lean sibling): archimedean specialisation over `ℝ`**
(AGENTS.md §7c) — the stability line uses `rpow` (`A^{2/3}`), division,
and strict ordering, all of which are archimedean. The underlying
combinatorial `q`-data stays generic over a commutative ring; only this
numerical-evaluation slice is specialised to `ℝ`.
-/

namespace QOU.Braiding

open Real

/-- Beta-stability line: p*(A) = A / (2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [leitner2026] §4/beta-stability
noncomputable def betaStabilityLine (A a_C a_A : ℝ) : ℝ :=
  A / (2 + a_C * A ^ ((2 : ℝ) / 3) / (2 * a_A))

/-- At a_C = 0 (no Coulomb repulsion), all nuclei have p = A/2:
    symmetric nuclear matter. -/
-- Ref: [leitner2026] §4/beta-stability
theorem classical_limit_symmetric (A a_A : ℝ) :
    betaStabilityLine A 0 a_A = A / 2 := by
  unfold betaStabilityLine
  simp

/-- The denominator of the stability line is > 2 when a_C > 0 and A > 0,
    so p*(A) < A/2: heavy nuclei have more neutrons than protons. -/
-- Ref: [leitner2026] §4/beta-stability
theorem neutron_excess (A a_C a_A : ℝ) (hA : 0 < A) (hC : 0 < a_C) (haA : 0 < a_A) :
    betaStabilityLine A a_C a_A < A / 2 := by
  unfold betaStabilityLine
  have hpow : 0 < A ^ ((2 : ℝ) / 3) := Real.rpow_pos_of_pos hA _
  have h1 : 0 < a_C * A ^ ((2 : ℝ) / 3) / (2 * a_A) := by
    apply div_pos (mul_pos hC hpow)
    linarith
  have hden : (2 : ℝ) < 2 + a_C * A ^ ((2 : ℝ) / 3) / (2 * a_A) := by linarith
  exact div_lt_div_of_pos_left hA (by norm_num) hden

/-- Stable neutron number: n*(p) = A*(p) - p where A*(p) is the
    fixed point of A = p·(2 + a_C·A^{2/3}/(2·a_A)). -/
-- Ref: [leitner2026] §4/beta-stability
noncomputable def stableNeutronNumber (p : ℕ) (A_stable : ℝ) : ℝ :=
  A_stable - p

/-- The n/p ratio is 1 when the stable mass number is 2p (the
    symmetric a_C = 0 fixed point). -/
-- Ref: [leitner2026] §4/beta-stability
theorem nOverP_classical (p : ℕ) (hp : 0 < p) :
    stableNeutronNumber p (2 * p) / p = 1 := by
  unfold stableNeutronNumber
  have hp0 : (0 : ℝ) < p := by exact_mod_cast hp
  field_simp
  ring

end QOU.Braiding
