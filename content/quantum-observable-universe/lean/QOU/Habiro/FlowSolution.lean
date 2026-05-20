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
existence/uniqueness content is already carried by the parent
classes
`QOU.QExponential` (`prop:q-exponential-exists`,
`prop:q-exponential-unique`),
`QOU.QDilogarithm` (`prop:q-dilogarithm-exists`,
`prop:q-dilogarithm-unique`),
`QOU.CategoricalFourierTransform`
(`prop:categorical-fourier-exists`).  What this class adds is the
joint synthesis: that the three are *simultaneously* the unique
algebraic objects in the Habiro completion solving their
respective Reeb-flow equations.

LaTeX label: `rem:generating-functions-solve-reeb-flow`
-/

namespace QOU.Habiro

/-- The synthesis-level Habiro flow-solution class.  Conjectural:
    the individual fixed-point properties are carried by the parent
    classes; this class records that they hold *simultaneously* in
    a common Habiro completion and that their archimedean shadows
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

-- Ref: [manuscript] content/quantum-observable-universe/quantum-observable-universes/generating-functions-solve-reeb-flow.md

/-- The synthesis class instances exist when the three individual
    flow-solution propositions are supplied.  Trivial consumer of
    the class data; downstream theorems can chain through. -/
theorem habiro_flow_solutions_realise_synthesis
    [inst : HabiroFlowSolution] :
    inst.expQ_solves_base_reeb ∧
    inst.fourier_diagonalises_qheat ∧
    inst.liTwoQ_volumetric :=
  inst.all_hold

end QOU.Habiro
