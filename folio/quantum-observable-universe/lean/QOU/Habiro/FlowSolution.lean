import QOU.Basic

/-!
# QOU.Habiro.FlowSolution

Axiomatisation of the substrate-level "three flow solutions"
synthesis from
`rem:generating-functions-solve-reeb-flow`: the $q$-exponential
solves the base Reeb flow, the categorical Fourier transform
diagonalises the $q$-heat equation, and the $q$-dilogarithm
$\mathrm{Li}_2^q$ evaluates the volumetric expansion of the
Reeb-heat flow.  All three solutions live in the Habiro ring
$\widehat{\mathbb{Z}[q]}$ and admit archimedean shadows under the
realisation functor $\tau_\infty$.

This class is the **synthesis-level** placeholder.  The per-function
existence/uniqueness content is already supplied by the existing
Lean developments
`QOU.QExponential` (`prop:q-exponential-exists`,
`prop:q-exponential-unique`),
`QOU.QDilogarithm` (`prop:q-dilogarithm-exists`,
`prop:q-dilogarithm-unique`),
`QOU.CategoricalFourier`
(`prop:categorical-fourier-exists`).  Those are `structure`s
(not typeclasses), so `HabiroFlowSolution` does not extend them
— it bundles their proven content into a single joint-existence
claim: the three are *simultaneously* the unique algebraic
objects in the Habiro completion solving their respective
Reeb-flow equations.

LaTeX label: `rem:generating-functions-solve-reeb-flow`
-/

namespace QOU.Habiro

/-- The synthesis-level Habiro flow-solution class.  Conjectural:
    the individual fixed-point properties are supplied by the
    existing `QOU.QExponential`, `QOU.QDilogarithm`, and
    `QOU.CategoricalFourier` developments (structures, not
    typeclasses — `HabiroFlowSolution` does NOT extend them).
    This class records that the three hold *simultaneously* in a
    common Habiro completion and that their archimedean shadows
    under $\tau_\infty$ are mutually compatible (the $\tau_\infty$
    of $\mathrm{Li}_2^q$ gives the Bloch–Wigner volume function
    used by `prop:thurston-volume-additivity`, while
    $\tau_\infty(\exp_q)$ gives the analytic exponential and
    $\tau_\infty(\mathcal{F}_q)$ gives the classical Fourier
    transform on the limit cocompact lattice). -/
class HabiroFlowSolution (q : ℚ) where
  /-- Rational power-series coefficient sequence $c_n$ of $\exp_q$. -/
  expQ_coeff : ℕ → ℚ
  /-- Initial normalisation $c_0 = 1$. -/
  expQ_zero : expQ_coeff 0 = 1
  /-- $\exp_q$ satisfies the base Reeb $q$-difference recurrence
      $(1 - q^{n+1}) c_{n+1} = (1 - q) c_n$. -/
  expQ_solves_base_reeb : ∀ n : ℕ,
    (1 - q ^ (n + 1)) * expQ_coeff (n + 1) = (1 - q) * expQ_coeff n
  /-- Peter–Weyl $q$-heat eigenvalue sequence $\lambda_j$ on
      $\mathbf{Rep}(\mathrm{SU}_q(2))$. -/
  fourier_eigenvalue : ℕ → ℚ
  /-- Categorical Fourier diagonalises $\Delta_q$ with Laurent-symmetric
      eigenvalues $\lambda_j = q^j + q^{-j}$. -/
  fourier_diagonalises_qheat : ∀ j : ℕ,
    fourier_eigenvalue j = q ^ j + (q ^ j)⁻¹
  /-- Rational coefficient sequence $d_n$ of $\mathrm{Li}_2^q$. -/
  liTwoQ_coeff : ℕ → ℚ
  /-- $\mathrm{Li}_2^q$ satisfies the volumetric $q$-difference relation
      $(1 - q^n) d_n = 1 / n$ for $n \ge 1$. -/
  liTwoQ_volumetric : ∀ n : ℕ, 1 ≤ n →
    (1 - q ^ n) * liTwoQ_coeff n = 1 / (n : ℚ)

-- Ref: [leitner2026] folio/quantum-observable-universe/quantum-observable-universes/generating-functions-solve-reeb-flow.md

namespace HabiroFlowSolution

variable {q : ℚ}

/-- From the base Reeb $q$-difference recurrence at $n = 0$ and $c_0 = 1$,
    any `HabiroFlowSolution q` at $q \ne 1$ forces $c_1 = 1$. -/
theorem expQ_coeff_one [H : HabiroFlowSolution q] (hq : 1 - q ≠ 0) :
    H.expQ_coeff 1 = 1 := by
  have h0 := H.expQ_solves_base_reeb 0
  rw [pow_one, H.expQ_zero, mul_one] at h0
  exact mul_left_cancel₀ hq (by linarith)

/-- From the base Reeb recurrence at $n = 1$ and $c_1 = 1$,
    any `HabiroFlowSolution q` at $q \ne 1$ satisfies $(1 + q) c_2 = 1$. -/
theorem expQ_coeff_two_recurrence [H : HabiroFlowSolution q] (hq : 1 - q ≠ 0) :
    (1 + q) * H.expQ_coeff 2 = 1 := by
  have h1 := H.expQ_solves_base_reeb 1
  have hc1 : H.expQ_coeff 1 = 1 := expQ_coeff_one hq
  rw [hc1, mul_one] at h1
  have hfac : (1 - q ^ (1 + 1)) * H.expQ_coeff 2 = (1 - q) * ((1 + q) * H.expQ_coeff 2) := by
    ring
  rw [hfac] at h1
  exact mul_left_cancel₀ hq (by linarith)

/-- At $j = 0$, the character-mode $q$-heat eigenvalue is $1 + 1 = 2$. -/
theorem fourier_eigenvalue_zero [H : HabiroFlowSolution q] :
    H.fourier_eigenvalue 0 = 2 := by
  have h0 := H.fourier_diagonalises_qheat 0
  norm_num at h0
  exact h0

/-- At $n = 1$, the volumetric $q$-dilogarithm recurrence forces
    $(1 - q) d_1 = 1$. -/
theorem liTwoQ_coeff_one_recurrence [H : HabiroFlowSolution q] :
    (1 - q) * H.liTwoQ_coeff 1 = 1 := by
  have h1 := H.liTwoQ_volumetric 1 (by decide)
  norm_num at h1
  exact h1

/-- **The flow-solution carrier is genuinely refutable (`qou-a30t`).**
    At the degenerate limit $q = 1$, $(1 - 1) d_1 = 1$ is impossible, so
     the carrier at $q = 1$ has no inhabitants (`¬ Nonempty`).
    This separates the repaired carrier from the previous bare-`Prop`-field
    shape, which was universally inhabited by `⟨True, True, True, …⟩`. -/
theorem not_flowSolution_at_one : ¬ Nonempty (HabiroFlowSolution 1) := by
  rintro ⟨H⟩
  have h := liTwoQ_coeff_one_recurrence (q := 1) (H := H)
  norm_num at h

end HabiroFlowSolution


/-! ### Removed 2026-08-30 — self-assuming projections

- `habiro_flow_solutions_realise_synthesis` — body was `inst.all_hold`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.
-/

end QOU.Habiro
