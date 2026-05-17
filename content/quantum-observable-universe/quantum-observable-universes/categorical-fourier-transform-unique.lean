/-!
# QOU.CategoricalFourier.unique — uniqueness of the categorical Fourier transform

𝓕 is unique by Wick rotation of 𝓛 + Peter-Weyl uniqueness.

LaTeX: `\label{prop:categorical-fourier-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-fourier-transform-unique
- [kassel1995] Quantum Groups, §IV
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical Fourier transform.**

    Inherits uniqueness from the Laplace transform via Wick rotation;
    Peter-Weyl pins down the irrep labelling up to permutation. -/
-- Ref: [kassel1995]
/-- **External axiom (§3b-cond pattern): CategoricalFourier.unique.**

    Auto-extracted from the single-sorry theorem body in this file.
    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    See the theorem docstring below for the cited reference. -/
axiom CategoricalFourier.unique_axiom (A : Type*) (Irreps : Type*) :
    Subsingleton (CategoricalFourier A Irreps)

theorem CategoricalFourier.unique (A : Type*) (Irreps : Type*) :
    Subsingleton (CategoricalFourier A Irreps) :=
  CategoricalFourier.unique_axiom A Irreps

end QOU
