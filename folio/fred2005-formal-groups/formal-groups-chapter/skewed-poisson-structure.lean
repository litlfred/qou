/-!
# Fred2005.SkewedPoissonStructure

Sibling stub for content block
[`def:skewed-poisson-structure`](skewed-poisson-structure.md). The declaration is

```lean
abbrev Fred2005.SkewedPoissonStructure (R : Type*) [CommRing R] {I : Type*} [DecidableEq I]
    (A : I → Type*) [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)] :=
  QOU.FormalGroups.SplayPoisson R A
```

in [`Fred2005/FormalGroups.lean`](../lean/Fred2005/FormalGroups.lean). `SplayPoisson` is a
skew-symmetric bi-derivation with Jacobi identity on the free product `∐ᵢ Aᵢ` that
vanishes on each `Aᵢ` (`QOU/FormalGroups/SplayPoisson.lean`). Strong filtration is
`QOU.FormalGroups.PoissonStructure.StronglyFiltered`.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Def. 1.1.
-/
