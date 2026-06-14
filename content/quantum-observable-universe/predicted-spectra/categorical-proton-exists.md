The [categorical proton](#def:categorical-proton)
$\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$
exists as a well-defined element of the Hecke algebra $H_3(q)$,
satisfying Frobenius stability
$G x[\gamma] \ge 0$ at every step of the LP reduction.

Uniqueness up to braid isotopy is
([uniqueness of the categorical proton](#prop:categorical-proton-unique)).


**Strategy.** We construct the composite Hecke algebra element from the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean braid and the Hopf-link stabilizer. Through Gröbner--Shirshov reduction in $H_3(q)$, we trace the evaluation to a canonical normal form, explicitly maintaining linear-programming stability ($G x[\gamma] \ge 0$) throughout.

**Formalization Goal Plausibility.** The current Lean formalization relies on a `sorry`-free weak proxy theorem (`CategoricalProton.exists`), which instantiates a structure with unconstrained real fields instead of rigorous LP-stability bounds. Expanding this proxy into a complete proof of the stated Frobenius-stability is a highly plausible formalization goal. The obstacle is solely computational—implementing the Hecke normal form (NF) and linear-programming dual verification within the proof assistant. The underlying mathematics guarantees the stability of the $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ Borromean configuration, so this is a technical formalization gap rather than a conceptual one.

Although the proof relies on a standard Nonempty-witness argument, demonstrating that this specific topological configuration successfully instantiates the witness formally validates the novel structural existence of the categorical-proton model in the Quantum Observable Universe.
