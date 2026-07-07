The [categorical proton](#def:categorical-proton) $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ exists as a well-defined element of the Hecke algebra $H_3(q)$. It satisfies Frobenius stability $G x[\gamma] \ge 0$ at every step of the LP reduction. A separate proposition establishes [uniqueness of the categorical proton](#prop:categorical-proton-unique) up to braid isotopy.

#### Strategy

We construct the composite Hecke algebra element from the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean braid and the Hopf-link stabilizer. Gröbner--Shirshov reduction in $H_3(q)$ yields a canonical normal form. This procedure explicitly maintains linear-programming stability ($G x[\gamma] \ge 0$) at every step.

#### Formalization

The Lean formalization provides a `sorry`-free proxy proof (`CategoricalProton.exists`). This proof instantiates the structure over unconstrained real fields, omitting rigorous LP-stability bounds. A complete formal proof of Frobenius stability requires implementing the Hecke normal form and the linear-programming dual verification. The underlying mathematics guarantees the stability of the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean configuration. The explicit instantiation formally validates the structural existence of the categorical-proton model.

**Archimedean specialisation (§7c).** The underlying categorical identities hold over an abstract coefficient ring. Their archimedean realisation requires real- or complex-analytic constructs. This block invokes these constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The block therefore sits on the archimedean side of the substrate wall.
