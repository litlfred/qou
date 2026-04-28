/-!
# QOU.ObservableMTC.bnAction

Categorical braiding on 𝐕⊗𝐕 induces a B_n representation on 𝐕^⊗n
that does not factor through the symmetric-group quotient, because
the observable MTC braiding is non-symmetric on some simple.

LaTeX label: `prop:bn-mtc-action`

**Ground ring**: `ℂ` (categorical; non-computational).
-/

import Mathlib.CategoryTheory.Monoidal.Braided.Basic

namespace QOU

open CategoryTheory MonoidalCategory BraidedCategory

/-- **Non-factoring through S_n**: in an observable MTC there exists
    a simple V on which the categorical braid relation
    σ_i² ≠ id holds, so the induced B_n action on V^⊗n does not
    descend to S_n.

    LaTeX: `\label{prop:bn-mtc-action}`
    Ref: [kitaev2006] https://doi.org/10.1016/j.aop.2005.10.005 -/
theorem bnAction
    (C : Type*) [Category C] [MonoidalCategory C] [BraidedCategory C]
    [MTC : ObservableMTC C] :
    ∃ V : C, (β_ V V).hom ≫ (β_ V V).hom ≠ 𝟙 (V ⊗ V) :=
  MTC.braiding_nonsymmetric

end QOU
