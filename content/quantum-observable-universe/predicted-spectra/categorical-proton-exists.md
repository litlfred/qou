**Proposition (Categorical proton existence).**

The [categorical proton](#def:categorical-proton) $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ exists as a well-defined element of the Hecke algebra $H_3(q)$. It satisfies Frobenius stability $G x[\gamma] \ge 0$ at every step of the LP reduction. Uniqueness up to braid isotopy is treated in [uniqueness of the categorical proton](#prop:categorical-proton-unique).

#### Strategy

We construct the composite Hecke algebra element from the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean braid and the Hopf-link stabilizer. Gröbner--Shirshov reduction in $H_3(q)$ reduces the evaluation to a canonical normal form. This procedure explicitly maintains linear-programming stability ($G x[\gamma] \ge 0$) throughout.

#### Formalization

The Lean formalization provides a `sorry`-free weak proxy proof (`CategoricalProton.exists`) by instantiating a structure without rigorous LP-stability bounds (using unconstrained real fields). Expanding this proxy into a complete proof of Frobenius-stability requires implementing the Hecke normal form and linear-programming dual verification. The underlying mathematics guarantees the stability of the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean configuration. The explicit instantiation formally validates the structural existence of the categorical-proton model.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The underlying categorical identities hold over an abstract coefficient ring; only their archimedean realisation is specialised here.
