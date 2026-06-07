import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.BraidKnot.QuantumDilogarithm
  — Disambiguation of Φ_q (product form) and Li_2^q (integral form)

Two distinct functions appear in the QOU mass formulae:

  1. **Φ_q(z) = ∏_{k=1}^∞ (1 - q^{-k}z)^{-1}** — the quantum
     dilogarithm product, unbounded as |z| → 1.

  2. **-Li_2^q(-z) = ∫_0^z (ln_q(1+t) / t) dt
       = Σ_{n ≥ 1} z^n / (n · [n]_q)** — the symmetric q-dilogarithm
     (Kashaev integration limit), bounded in [0.1, 0.82] for
     z ∈ (0, 1) at q_0.

These functions are **not equal**: their values differ by 6 orders
of magnitude at z = 0.989 (the typical per-generator volume scale
in atomic braid words at q_0). The historical paper-level identity
claim Φ_q(z) = ∫_0^z (ln_q(1+t)/t) dt is **false**.

The corrected canonical form of the mass-endomorphism tower (per
`prop:mass-endomorphism-tower`, resolution note 2026-05-17) uses
`-Li_2^q(-|V|)` — NOT `Φ_q(|V|)` — at every site that evaluates the
tower on per-generator amplitudes.

LaTeX label: `\label{def:quantum-dilogarithm-disambiguation}`

Ref: [manuscript] `prop:mass-endomorphism-tower` (resolution note)
-/

namespace QOU.BraidKnot

universe u

/-- The **quantum dilogarithm product** at substrate `q` and
    argument `z`. Defined formally as the infinite product

      Φ_q(z) = ∏_{k=1}^∞ (1 - q^{-k} z)^{-1}.

    At z = 0 the product is empty, giving Φ_q(q, 0) = 1.
    Unbounded near |z| = 1 (concretely, Φ_q(0.989) ≈ 6.7 × 10^5 at
    q_0 ≈ 1.110). Used in `mass_endomorphism.py` and
    `brane_tower_isospin_diagnosis.py` (the latter as a *diagnostic*
    that exposes the −737 MeV mirror-nucleus pathology when the
    archimedean specialisation is taken to be Φ_q instead of
    the corrected −Li_2^q(−z)).

    Axiomatised here pending a Lean infinite-product implementation;
    the value at z = 0 is fixed by the empty-product convention. -/
-- Ref: [manuscript] prop:mass-endomorphism-tower §Quantum-dilogarithm form
axiom phi_q_residual : ℝ → ℝ → ℝ

/-- Quantum dilogarithm encoded as the empty-product baseline `1`
    plus the higher-order-in-`z` correction. The `phi_q_residual`
    axiom abstracts everything beyond the empty-product term so that
    `phi_q q 0 = 1` becomes provable by `ring` rather than axiomatic.
    This is a strict improvement: the empty-product convention is now
    a *theorem*, and only the second-order-and-above behaviour of
    Φ_q stays opaque. -/
noncomputable def phi_q (q z : ℝ) : ℝ := 1 + z * phi_q_residual q z

/-- Empty-product convention: Φ_q(q, 0) = 1 for every q. **Theorem
    (was axiom prior to PR #1968).** Discharged by `def phi_q` above. -/
theorem phi_q_at_zero : ∀ q : ℝ, phi_q q 0 = 1 := by
  intro q
  unfold phi_q
  ring

/-- The **symmetric q-dilogarithm** evaluated at `z`. Defined as

      Li_2^q(z) = Σ_{n ≥ 1} z^n / (n · [n]_q)

    where `[n]_q = (q^n − q^{-n}) / (q − q^{-1})` is the q-bracket.

    Equivalently (Kashaev integration limit identity):

      −Li_2^q(−z) = ∫_0^z (ln_q(1+t) / t) dt.

    Bounded in [0.1, 0.82] for z ∈ (0, 1) at q_0 — this is the
    correct archimedean specialisation of `Vol_q^(S)` in the
    mass-endomorphism tower. The series has empty first term at
    z = 0, giving Li_2^q(q, 0) = 0. -/
-- Ref: [manuscript] prop:mass-endomorphism-tower §Trace-vs-evaluation note
axiom li2_q_residual : ℝ → ℝ → ℝ

/-- Symmetric q-dilogarithm encoded as the empty-sum baseline `0`
    plus the higher-order-in-`z` correction. The `li2_q_residual`
    axiom abstracts everything beyond the empty-sum term so that
    `li2_q q 0 = 0` becomes provable by `ring` rather than axiomatic
    (parallel discharge to `phi_q_at_zero` — see PR #1968). -/
noncomputable def li2_q (q z : ℝ) : ℝ := z * li2_q_residual q z

/-- Empty-sum convention: Li_2^q(q, 0) = 0 for every q. **Theorem
    (was axiom prior to PR #1968).** Discharged by `def li2_q` above. -/
theorem li2_q_at_zero : ∀ q : ℝ, li2_q q 0 = 0 := by
  intro q
  unfold li2_q
  ring

/-- The two functions are **NOT** equal under the historical
    identity claim `Φ_q(z) = -Li_2^q(-z)`. The proof exhibits a
    counter-example at `z = 0`, where Φ_q is the empty product
    `1` and -Li_2^q(-0) is the empty sum `0`. -/
-- Ref: [manuscript] prop:mass-endomorphism-tower §Kashaev-integration-identity audit
theorem phi_q_ne_li2_q :
    ¬ (∀ q z : ℝ, phi_q q z = - li2_q q (-z)) := by
  intro h
  have h0 := h 1 0
  rw [phi_q_at_zero, neg_zero, li2_q_at_zero, neg_zero] at h0
  -- h0 : (1 : ℝ) = 0
  exact one_ne_zero h0

/-- **Canonical tower form (corrected).** The mass-endomorphism
    tower uses `-Li_2^q(-|V|)` on per-generator amplitudes, NOT
    `Φ_q(|V|)`. The corrected per-generator term is:

      towerTerm q V = -li2_q q (-|V|)

    Empirically bounded; Markov-invariant via the Plancherel-series
    factoring of each `z^n` summand through tr_M(σ_i^n) (see
    `brane_tower_plancherel_scaffold.py`). -/
noncomputable def towerTerm (q V : ℝ) : ℝ := - li2_q q (-|V|)

/-- At zero amplitude the corrected tower term vanishes:
    `towerTerm q 0 = 0`. -/
theorem towerTerm_at_zero (q : ℝ) : towerTerm q 0 = 0 := by
  unfold towerTerm
  rw [abs_zero, neg_zero, li2_q_at_zero, neg_zero]

/-- At zero amplitude the historical Φ_q form is 1, NOT 0. This
    is the elementary witness that the historical identity fails. -/
theorem phi_q_at_zero_ne_towerTerm_at_zero (q : ℝ) :
    phi_q q 0 ≠ towerTerm q 0 := by
  rw [phi_q_at_zero, towerTerm_at_zero]
  norm_num

/-- **Anti-regression discipline.** Any consumer of the mass-
    endomorphism tower that takes `f` as the archimedean
    specialisation function should assert
    `f = towerTerm`, not `f = phi_q`. The latter is the historical
    pathological form preserved only as a diagnostic. -/
class HasCorrectedMassEndomorphismTower where
  /-- The archimedean specialisation function used in this instance. -/
  archimedeanSpec : ℝ → ℝ → ℝ
  /-- The instance uses the corrected `-Li_2^q(-|V|)` form. -/
  uses_li2q : archimedeanSpec = towerTerm

/-- Any class instance using the corrected form vanishes at zero. -/
theorem HasCorrectedMassEndomorphismTower.archimedeanSpec_at_zero
    [c : HasCorrectedMassEndomorphismTower] (q : ℝ) :
    c.archimedeanSpec q 0 = 0 := by
  rw [c.uses_li2q]
  exact towerTerm_at_zero q

/-- Any class instance using the corrected form **disagrees** with
    `phi_q` at z = 0 (since Φ_q(q, 0) = 1 ≠ 0 = towerTerm(q, 0)). -/
theorem HasCorrectedMassEndomorphismTower.ne_phi_q_at_zero
    [c : HasCorrectedMassEndomorphismTower] (q : ℝ) :
    c.archimedeanSpec q 0 ≠ phi_q q 0 := by
  rw [c.uses_li2q, phi_q_at_zero, towerTerm_at_zero]
  norm_num


/-- Quantum-dilogarithm disambiguation (placeholder marker for content block ref resolution) -/
-- Ref: [manuscript] disambiguation marker for content-block resolution
structure QuantumDilogarithm where

end QOU.BraidKnot
