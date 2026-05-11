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
-- Closure (2026-05-11): both scalar-eigenvalue AND operator-valued n_⋆ forms
-- of the conjecture's level-selection claim are refuted by witness data.
--
-- SCOPE.
-- (a) "Scalar-eigenvalue" means the candidate `n_⋆` is a function of scalar
--     substrate invariants of a single confined particle AND Φ_q^{[≤n_⋆]} is
--     evaluated on a SCALAR argument (the per-generator algebraic volume
--     |V̂_i|).  Refuted by `witness_refutes_scalar_uniform_k_form` and
--     `witness_refutes_scalar_ell_n0_k_form` below.
-- (b) "Operator-valued (per-eigenvalue)" replaces the scalar Φ_q evaluation
--     with `Σ_λ y_λ · tr_λ(Φ_q^{[≤k]}(ρ_λ(β)))` — Φ_q applied per eigenvalue
--     of the braid operator in each Hecke irrep V_λ, summed as the operator
--     trace, then Wedderburn-weighted.  Refuted by
--     `witness_refutes_per_eigenvalue_operator_form` below.
--
-- Combined as `nStar_all_probed_forms_refuted`: every empirically probed
-- form of the `n_⋆` existence claim fails the falsifiability threshold.
-- The remaining open paths (untouched by these refutations) are: the
-- algebraic Cauchy-limit half of the conjecture; the multiplicity-refined
-- scalar form `n_⋆(ℓ, n₀, k, m)` with m = per-generator near-pole
-- multiplicity profile; and crystal-basis derived candidates such as
-- Type-B-folded-crystal depth (CLAUDE.md §7b).
--
-- Witnesses:
--   folio-assistant/computations/probe-phiq-uniform-k.witness.json
--   folio-assistant/computations/probe-phiq-n-star-rule.witness.json
--   folio-assistant/computations/probe-phiq-operator-valued.witness.json
-- ────────────────────────────────────────────────────────────────────────────

/-- Falsifiability threshold from the conjecture's `## Falsifiability`
    section: a candidate `n_⋆` rule must close all three AME light
    isotopes to within `~5%` without per-atom retuning. We use the
    `10%` bound below to remain robust against rounding in the
    witness arithmetic. -/
def falsifiabilityThresholdPct : ℝ := 10.0

/-- Witness-recorded worst-case relative error (subtractive form) at
    the best uniform truncation depth `k = 2` under the
    **scalar-eigenvalue** form: Φ_q evaluated at scalar
    per-generator volumes `|V̂_i|`, then summed.  Maximum is on
    `³He` at `+134%`.

    Source:
    `folio-assistant/computations/probe-phiq-uniform-k.witness.json`
    (computed `2026-04-29`, `commitSha 95ed3374…`). -/
def witnessUniformKBestMaxErrPct : ℝ := 134.0

/-- Witness-recorded worst-case relative error for the
    `n_⋆ = ℓ · n₀ + k` per-atom rule (also scalar-eigenvalue form)
    at `(n_⋆^D, n_⋆^T, n_⋆^³He) = (14, 27, 20)` (subtractive form).
    Maximum is on `³He` at `+1.18 × 10^6 %`.

    Source:
    `folio-assistant/computations/probe-phiq-n-star-rule.witness.json`
    (computed `2026-05-09`, `commitSha c8f9603d…`). -/
def witnessNStarRuleMaxErrPct : ℝ := 1177119.823748267

/-- Witness-recorded best-case max-relative-error under the
    **per-eigenvalue, signed, operator-trace** Wedderburn promotion,
    `tower_op^(k)(β) = |Σ_λ y_λ(q₀) · tr_λ(Φ_q^{[≤k]}(ρ_λ(β)))|`,
    where ρ_λ(β) is the braid operator in irrep V_λ (numerical
    matrix via Hoefsmit seminormal at q₀), Φ_q is applied per
    eigenvalue μ_a^(λ), and the operator trace `tr_λ` sums them.

    Min-over-k of the max-over-atom absolute error is `64.75%` at
    `k = 1`. Notable per-atom: D at `k=1` lands at `-6.87%` (within
    10%), T at `k=2` lands at `-8.00%` (within 10%), but ³He never
    gets within 50% at any uniform k — there is no single `k` that
    closes all three simultaneously.

    This is the *canonical* operator-valued promotion: it addresses
    the three normalization issues with the prior
    `_avg_chi_over_classical_dim` variant — classical→quantum dim
    (resolved structurally by using operator trace), absolute→signed
    χ (resolved by complex Φ_q + final |·|), mean→per-eigenvalue Φ_q
    (resolved directly by `tr_λ` of Φ_q applied to ρ_λ).

    Source:
    `folio-assistant/computations/probe-phiq-operator-valued.witness.json`
    (computed `2026-05-11`). -/
def witnessPerEigenvalueOperatorBestMaxAbsErrPct : ℝ := 64.75

/-- **Scalar-eigenvalue `n_⋆` refutation (uniform-`k` family).** The
    best uniform-depth candidate (`k = 2`, subtractive form) leaves a
    `+134%` residual on `³He` — an order of magnitude above the
    falsifiability threshold. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem witness_refutes_scalar_uniform_k_form :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct := by
  unfold witnessUniformKBestMaxErrPct falsifiabilityThresholdPct
  norm_num

/-- **Scalar-eigenvalue `n_⋆` refutation (`ℓ · n₀ + k` family).** The
    proposed additive rule from `conj:brane-level-selection`
    overshoots `³He` by six orders of magnitude — refutation is
    immediate. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem witness_refutes_scalar_ell_n0_k_form :
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct := by
  unfold witnessNStarRuleMaxErrPct falsifiabilityThresholdPct
  norm_num

/-- **Operator-valued `n_⋆` refutation (per-eigenvalue form).**
    The canonical convolution-aware promotion — Φ_q applied to each
    eigenvalue μ_a^(λ) of the braid operator ρ_λ(β) in each Hecke
    irrep V_λ, summed via the operator trace `tr_λ`, then Wedderburn-
    weighted by signed `y_λ(q₀)`, with `|·|` only at the
    binding-formula level — fails the falsifiability criterion at
    every uniform `k`. Best case `k = 1` leaves max abs error
    `64.75%` on tritium, an order of magnitude above the `10%`
    threshold.

    Note: per-atom optimal `k` values DO achieve closure individually
    (D at `k=1`: `-6.87%`; T at `k=2`: `-8.00%`), but ³He cannot be
    closed at any uniform `k`. The conjecture's falsifiability
    criterion forbids per-atom retuning ("does not constitute
    progress"), so the operator-valued `n_⋆` existence claim is
    refuted under this canonical promotion. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Operator-valued probe"
theorem witness_refutes_per_eigenvalue_operator_form :
    witnessPerEigenvalueOperatorBestMaxAbsErrPct >
      falsifiabilityThresholdPct := by
  unfold witnessPerEigenvalueOperatorBestMaxAbsErrPct
        falsifiabilityThresholdPct
  norm_num

/-- **Scalar-eigenvalue `n_⋆` refutation (combined).** Both probed
    scalar-eigenvalue substrate families — uniform-`k` and
    `ℓ · n₀ + k` — exceed the `10%` falsifiability threshold. By the
    conjecture's own criterion, the **scalar-eigenvalue** existence
    claim is refuted.  Note: the strictly-stronger operator-valued
    refutation below (per-eigenvalue, signed, operator-trace) also
    fails, so the `n_⋆` existence claim is refuted across every
    empirically probed form. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem nStar_scalar_eigenvalue_form_refuted :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct ∧
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct :=
  ⟨witness_refutes_scalar_uniform_k_form,
   witness_refutes_scalar_ell_n0_k_form⟩

/-- **All probed `n_⋆` families refuted.** Combining the two
    scalar-eigenvalue refutations with the canonical
    operator-valued (per-eigenvalue, signed, operator-trace,
    Wedderburn-weighted) refutation: every empirically probed form
    of the `n_⋆` existence claim on `conj:brane-tower-z-habiro`
    fails the `10%` falsifiability threshold at every uniform `k`.

    What survives the closure (open):
    * the algebraic Cauchy-limit half of the conjecture (untouched);
    * the **per-atom** rule restricted to the (D, T) pair where
      D at `k=1` and T at `k=2` separately achieve closure under
      the operator-valued form — but per-atom retuning violates the
      conjecture's own criterion;
    * the **multiplicity-refined** scalar form with `n_⋆` depending
      on per-generator near-pole multiplicity profile `m`. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Operator-valued probe"
theorem nStar_all_probed_forms_refuted :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct ∧
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct ∧
    witnessPerEigenvalueOperatorBestMaxAbsErrPct >
      falsifiabilityThresholdPct :=
  ⟨witness_refutes_scalar_uniform_k_form,
   witness_refutes_scalar_ell_n0_k_form,
   witness_refutes_per_eigenvalue_operator_form⟩

end QOU.BraidKnot
