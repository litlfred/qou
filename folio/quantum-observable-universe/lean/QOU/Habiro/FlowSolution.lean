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
class HabiroFlowSolution where
  /-- $\exp_q$ is the unique Habiro-grouplike satisfying
      $D_q \exp_q = \exp_q$.  Encoded as a proposition the
      consumer must supply. -/
  expQ_solves_base_reeb : Prop
  /-- Categorical Fourier diagonalises $\Delta_q$ on the
      Peter–Weyl decomposition of $\mathbf{Rep}(\mathrm{SU}_q(2))$. -/
  fourier_diagonalises_qheat : Prop
  /-- $\mathrm{Li}_2^q$ is the formal Habiro antiderivative of
      $\log_q(1+t)/t$, giving the volumetric expansion of the
      Reeb-heat flow. -/
  liTwoQ_volumetric : Prop
  /-- The three propositions hold in the Habiro completion. -/
  all_hold : expQ_solves_base_reeb ∧ fourier_diagonalises_qheat
              ∧ liTwoQ_volumetric

-- Ref: [manuscript] folio/quantum-observable-universe/quantum-observable-universes/generating-functions-solve-reeb-flow.md


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
