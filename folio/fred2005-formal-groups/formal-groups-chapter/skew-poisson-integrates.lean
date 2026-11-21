/-!
# Fred2005.integration_commutator — the construction step of Thm. 3.7

Sibling stub for content block [`thm:skew-poisson-integrates`](skew-poisson-integrates.md).

```lean
theorem Fred2005.integration_commutator (π : SkewedPoissonStructure R A) (f g : SplayAlgebra R A) :
    integrationMk π.toPoissonStructure f * integrationMk π.toPoissonStructure g -
        integrationMk π.toPoissonStructure g * integrationMk π.toPoissonStructure f =
      integrationMk π.toPoissonStructure (π.toPoissonStructure.bracket f g)
```

in [`Fred2005/FormalGroups.lean`](../lean/Fred2005/FormalGroups.lean), from
`QOU.FormalGroups.integrationMk_commutator` (`RingQuot` of the relation
`fg ~ gf + π(f, g)`). `QOU.FormalGroups.commutatorIntegrationEquiv` proves that the
commutator bracket gives `U ≃ T`. That `U` is the distribution algebra of a formal group
is the content of Thm. 3.7 and is not formalised.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Thm. 3.7.
-/
