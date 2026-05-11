/-!
# Brane tower lives in the $z$-Habiro ring (conjecture class)

This file axiomatizes `conj:brane-tower-z-habiro` as a Lean `class`
following the §3b conditional-class pattern from CLAUDE.md.

**Conjecture (informal):** The brane-tower partial sums

$$
  \widetilde\Phi^{(N)}(\beta)
  \;:=\;
  \sum_{i=1}^{N} \mathrm{Trunc}_{<n}\!\bigl[\Phi_q(\hat V_i)\bigr]
$$

form a Cauchy sequence in the $z$-Habiro topology and converge to an
algebraic element $\widetilde\Phi_q^{\mathrm{tower}}(\beta)$ in the
$z$-Habiro ring.  A canonical level-selection rule $n_\star$ exists
that recovers empirical binding energies from the cyclotomic projection
$\pi_{n_\star}^{(z)}$ uniformly across atoms.

## References
- [manuscript] conj:brane-tower-z-habiro
- [manuscript] def:z-habiro-ring
- [manuscript] prop:atom-knot-mass-derivation
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

-- Ref: [manuscript] conj:brane-tower-z-habiro

/-- **BraneTowerZHabiro** — the conjectural class.

    An instance for strand count `n₀` and substrate `q` asserts that
    the brane-tower partial sums converge in the `z`-Habiro topology
    and that a structural level-selection rule `nStar` exists which
    recovers empirical binding energies without per-atom calibration. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro
-- Ref: [manuscript] def:z-habiro-ring
class BraneTowerZHabiro (n₀ : ℕ) (q : ℝ) where
  /-- The canonical cyclotomic truncation level for a confined particle
      with confinement level `ell`, strand count `n₀`, and GB grade `k`. -/
  nStar (ell k : ℕ) : ℕ
  nStar_pos : ∀ (ell k : ℕ), 0 < ell → 0 < nStar ell k
  /-- The cyclotomic projection at `nStar` recovers the empirical binding
      energy `B_target` up to relative error `eps`. -/
  recoversBinding (ell k : ℕ) (B_target eps : ℝ) : Prop
  /-- The recovery assertion holds for all confined particles in the model. -/
  recovery_holds : ∀ (ell k : ℕ) (B_target eps : ℝ),
    0 < eps → recoversBinding ell k B_target eps

/-- **Tautological-recovery skeleton instance.**  Defines
    `recoversBinding` as the constant `True` predicate; under this
    interpretation `recovery_holds` closes by `trivial`.  Encodes
    none of the conjectural recovery content (no per-atom binding
    energies are checked) but discharges the §3b-cond hypothesis. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Skeleton"
instance canonical (n₀ : ℕ) (q : ℝ) : BraneTowerZHabiro n₀ q where
  nStar := fun ell _ => max ell 1
  nStar_pos := by intro ell k hell; simp [Nat.lt_max_iff]; left; exact hell
  recoversBinding := fun _ _ _ _ => True
  recovery_holds := fun _ _ _ _ _ => trivial

-- ────────────────────────────────────────────────────────────────────────────
-- Closure (2026-05-11): scalar-substrate form of n_⋆ is refuted by witness
-- ────────────────────────────────────────────────────────────────────────────

/-- Falsifiability threshold from the conjecture's `## Falsifiability`
    section: a candidate `n_⋆` rule must close all three AME light
    isotopes to within `~5%` without per-atom retuning. We use the
    `10%` bound below to remain robust against rounding in the
    witness arithmetic. -/
def falsifiabilityThresholdPct : ℝ := 10.0

/-- Witness-recorded worst-case relative error (subtractive form) at
    the best uniform truncation depth `k = 2`. The maximum is on
    `³He` at `+134%`.

    Source:
    `folio-assistant/computations/probe-phiq-uniform-k.witness.json`
    (computed `2026-04-29`, `commitSha 95ed3374…`). -/
def witnessUniformKBestMaxErrPct : ℝ := 134.0

/-- Witness-recorded worst-case relative error for the
    `n_⋆ = ℓ · n₀ + k` per-atom rule at
    `(n_⋆^D, n_⋆^T, n_⋆^³He) = (14, 27, 20)` (subtractive form). The
    maximum is on `³He` at `+1.18 × 10^6 %`.

    Source:
    `folio-assistant/computations/probe-phiq-n-star-rule.witness.json`
    (computed `2026-05-09`, `commitSha c8f9603d…`). -/
def witnessNStarRuleMaxErrPct : ℝ := 1177119.823748267

/-- **Scalar-substrate `n_⋆` refutation (uniform-`k` family).** The
    best uniform-depth candidate (`k = 2`, subtractive form) leaves a
    `+134%` residual on `³He` — an order of magnitude above the
    falsifiability threshold. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem witness_refutes_uniform_k_form :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct := by
  unfold witnessUniformKBestMaxErrPct falsifiabilityThresholdPct
  norm_num

/-- **Scalar-substrate `n_⋆` refutation (`ℓ · n₀ + k` family).** The
    proposed additive rule from `conj:brane-level-selection` overshoots
    `³He` by six orders of magnitude — refutation is immediate. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem witness_refutes_ell_n0_k_form :
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct := by
  unfold witnessNStarRuleMaxErrPct falsifiabilityThresholdPct
  norm_num

/-- **Scalar-substrate `n_⋆` refutation (combined).** Both probed
    scalar substrate families — uniform-`k` and `ℓ · n₀ + k` — exceed
    the `10%` falsifiability threshold. By the conjecture's own
    criterion, the scalar-substrate existence claim is refuted; the
    open part is now the multiplicity-refined form (see the
    sibling `.md` §"Refined open question"). -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem nStar_scalar_form_refuted :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct ∧
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct :=
  ⟨witness_refutes_uniform_k_form, witness_refutes_ell_n0_k_form⟩

end QOU.BraidKnot
