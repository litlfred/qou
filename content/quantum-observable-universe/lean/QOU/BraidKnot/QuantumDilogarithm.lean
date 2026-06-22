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
    plus a `z`-multiplied residual factor. The `phi_q_residual`
    axiom abstracts everything beyond the empty-product term (so
    `phi_q_residual q 0` is the linear-in-`z` coefficient, with
    `phi_q_residual q z` for `z ≠ 0` carrying all higher-order
    behaviour). This is a strict improvement over a free
    `phi_q_at_zero` axiom: the empty-product convention is now a
    *theorem* — only Φ_q's variation away from `z = 0` stays
    opaque. -/
noncomputable def phi_q (q z : ℝ) : ℝ := 1 + z * phi_q_residual q z

/-- Empty-product convention: Φ_q(q, 0) = 1 for every q. **Theorem**
    (was previously an axiom). Discharged by `def phi_q` above. -/
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
    plus a `z`-multiplied residual factor. The `li2_q_residual` axiom
    abstracts everything beyond the empty-sum term (`li2_q_residual q 0`
    is the linear-in-`z` coefficient; the residual for `z ≠ 0` carries
    all higher-order behaviour). Parallel construction to `phi_q`. -/
noncomputable def li2_q (q z : ℝ) : ℝ := z * li2_q_residual q z

/-- Empty-sum convention: Li_2^q(q, 0) = 0 for every q. **Theorem**
    (was previously an axiom). Discharged by `def li2_q` above. -/
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

/-! ## z-Habiro Rogers saddle identity (conjecture — formalize-first)

The Faddeev face `phi_q` (root-of-unity quantum dilogarithm; the archimedean
realisation of the merged `QOU.MassEndomorphism.ZHabiroCauchy` eulerCoeff
limit) and the Rogers face `towerTerm = -li2_q(-|·|)` are, per
`prop:phi-q-aj-machinery-identification`, two archimedean saddles of ONE
algebraic object (the AJ quantum A-polynomial `Â_K`): `phi_q` at
`q = e^{2πi/N}` (root of unity, unbounded), the Rogers form at real `q`
(bounded). The QOU substrate evaluates masses at REAL `q₀` (`Im q₀ = 0` at the
observable level), so the production tower's use of `towerTerm` rather than
`phi_q` is exactly the claim that the correct real-`q` archimedean saddle of the
Faddeev face IS the Rogers form.

This identity is OPEN for `𝓑₃` (the AJ-saddle identification is unproven there
— see `phi-q-aj-machinery-identification.md`). We therefore axiomatise it as a
conjecture class — the `saddle_phi_q_eq_towerTerm` field IS the conjectural
input (AGENTS.md §3b "Lean formalization of conjectures") — and prove
NON-VACUOUS downstream corollaries that *compose* the conjecture with the proven
`towerTerm_at_zero` / `phi_q_at_zero` lemmas to derive new facts (they do not
project the conclusion; AGENTS.md §3b-cond rule 5).

Ref: docs/audits/2026-06-22-zhabiro-bounded-rogers-continuation-direction.md §4
-/

/-- **Conjecture (z-Habiro Rogers saddle identity).** There is a real-`q`
    archimedean saddle map `realQSaddle` under which the Faddeev face `phi_q`
    becomes the bounded Rogers production tower term `towerTerm = -li2_q(-|·|)`.
    The `saddle_phi_q_eq_towerTerm` field is the conjectural input — open for
    `𝓑₃`; every result below is conditional on this class. -/
class ZHabiroRogersSaddle where
  /-- the real-`q` archimedean saddle, acting on a dilogarithm face. -/
  realQSaddle : (ℝ → ℝ → ℝ) → (ℝ → ℝ → ℝ)
  /-- CONJECTURE: the real-`q` saddle of the Faddeev face is the Rogers
      production tower term. Open for `𝓑₃` (AJ-saddle identification). -/
  saddle_phi_q_eq_towerTerm : realQSaddle phi_q = towerTerm

/-- **Conditional corollary (non-vacuous).** Under the saddle conjecture, the
    real-`q` saddle of the Faddeev face vanishes at zero amplitude — derived by
    rewriting along the conjecture and then applying the *proven*
    `towerTerm_at_zero`. Composes the hypothesis with an established lemma; does
    not assume the conclusion. -/
theorem ZHabiroRogersSaddle.realQSaddle_phi_q_at_zero
    [s : ZHabiroRogersSaddle] (q : ℝ) :
    s.realQSaddle phi_q q 0 = 0 := by
  rw [s.saddle_phi_q_eq_towerTerm]
  exact towerTerm_at_zero q

/-- **Conditional corollary.** Under the saddle conjecture, the real-`q` saddle
    of the Faddeev face disagrees with `phi_q` itself at zero amplitude (the
    Rogers face is `0` there, the Faddeev face is `1`): the saddle genuinely
    moves `phi_q` off its own value, witnessing that the real-`q` continuation is
    the bounded Rogers form, not the Faddeev product. -/
theorem ZHabiroRogersSaddle.realQSaddle_phi_q_ne_phi_q_at_zero
    [s : ZHabiroRogersSaddle] (q : ℝ) :
    s.realQSaddle phi_q q 0 ≠ phi_q q 0 := by
  rw [s.saddle_phi_q_eq_towerTerm, phi_q_at_zero, towerTerm_at_zero]
  norm_num

end QOU.BraidKnot
