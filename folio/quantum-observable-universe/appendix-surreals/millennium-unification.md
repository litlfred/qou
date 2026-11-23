Six classical-limit problems tackled by the QOU framework (the Riemann hypothesis, 3D Navier--Stokes regularity, Collatz, P vs NP, Birch--Swinnerton-Dyer, and the Yang--Mills mass gap) reduce to a single surreal inequality between the cost of a standard-real deviation and the mass-gap infinitesimal. The adelic--Tate factorisation provides the local-global refinement.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)) and $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). Recall from [surreal rate calculus](#prop:surreal-rate-calculus):

$$
\Delta_q \asymp \varepsilon^3 \qquad (\text{mass-gap dissipation, positive infinitesimal}),
$$

$$
\Omega_q \asymp \varepsilon^{-1} \qquad (\text{Reeb-period budget, positive transfinite}).
$$

Each problem identifies a drift $\delta$ that measures the standard-real deviation from the classical stable configuration. The [surreal squeeze](#lem:surreal-squeeze) delivers the identical inequality:

$$
\delta^2 \cdot \Omega_q > \Delta_q \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Expanding $\Omega_q \asymp \varepsilon^{-1}$ and $\Delta_q \asymp \varepsilon^3$: for every standard real $\delta > 0$, $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$.

See [Table 1](#tbl:millennium-unification-table1-data).

The first three rows are unconditional surreal translations of existing QOU propositions ([collapse of the quantum gap](#thm:quantum-gap-collapse), blowup as lifting obstruction, [$q$-Collatz](#conj:q-collatz)). The fourth row is conditional on [P vs NP in the QOU](#conj:p-vs-np-qou). The fifth row is conditional on [$q$-BSD](#conj:q-birch-swinnerton-dyer); the adelic refinement ([adelic--Tate surreal squeeze](#rem:adelic-tate-squeeze)) localises this row at each prime. The sixth row is unconditional once the QOU substrate is posited: the mass gap is a categorical invariant of $\mathbf{C}$ with $\ordw(\Delta_q) = -3$, and Yang--Mills on $\mathbb{R}^4$ is the standard part of the $q$-deformation.

**The Navier--Stokes row is a different inference, not a sixth instance of the same one.** Five rows follow the schema above: a *hypothetical* standard-real drift $\delta > 0$ would cost more than the budget, so no such drift can persist, so $\delta = 0$ and the conjecture holds. The Navier--Stokes row does not. Its cost column carries no $\delta$ at all — the enstrophy ceiling $\mathcal{Z}_q \asymp \varepsilon^{-4/3}$ is a *fixed rate*, and the inequality $\mathcal{Z}_q > \Delta_q$ is, in the words of the row's own source block ([surreal bound for Navier--Stokes](#rem:ns-surreal-bound)), "automatic". Nothing is being forbidden; a production rate is being compared to an absorption rate, and the conclusion is that the excess is unabsorbed, i.e. that the event **occurs**.

Both patterns are individually coherent — *hypothetical cost exceeds budget, therefore forbidden* and *production exceeds absorption, therefore singular* — but they are not the same argument, and the sentence below about "identifying the problem-specific drift $\delta$ and translating the classical statement into the vanishing of this drift" describes only the first. It does not cover the Navier--Stokes row, whose drift is not asserted to vanish. Read the table as five instances of a squeeze plus one rate comparison sharing a notation, not as six instances of one theorem.

The mass-gap scaling $\Delta_q \asymp \varepsilon^3$ is a fixed structural invariant of the rigid :refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}$. It remains constant across problems. The Reeb-period scaling $\Omega_q \asymp \varepsilon^{-1}$ is similarly a fixed structural invariant of the Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb-derivation)). The content of each millennium problem resides in identifying the problem-specific drift $\delta$ and translating the classical statement into the vanishing of this drift. Once $\delta$ is identified, the squeeze $\delta^2 / \varepsilon > \varepsilon^3$ closes the argument uniformly.

The six millennium problems are not independent questions but six instances of a single substrate-stability requirement: the observable universe contains only classical-limit configurations where no standard-real drift absorbs more substrate energy than the mass gap dissipates. The Riemann hypothesis is the spectral instance, Navier--Stokes is the hydrodynamic instance, Collatz is the arithmetic instance, P vs NP is the complexity instance, BSD is the elliptic-curve instance, and Yang--Mills is the gauge-theory instance. The adelic--Tate framework ([adelic--Tate surreal squeeze](#rem:adelic-tate-squeeze)) localises each instance at every prime, rendering the squeeze strictly local-global.

The $\omega$-adic form of each squeeze is registered in the [body asymptotics catalog](#rem:body-asymptotics-catalog) under the $\ordw$-entry of the corresponding body block ([Big-O via $\ordw$](#rem:conway-normal-form)). These remarks can be read in either the "$\delta^2 \cdot \Omega_q > \Delta_q$ in $\mathbb{R}(\varepsilon)$" register or the "$\ordw(\text{cost}) > \ordw(\text{budget})$" register. The two are equivalent by the Big-O bridge.
