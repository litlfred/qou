**Remark (the three energy terms, limits, and crossing-energy relation).**

This remark unpacks the three terms of the [$q$-energy](#def:q-energy) $\mathfrak{E}_q(K)$, its classical and deep-quantum limits, and its relation to the crossing energy.

**The three terms.**

1. **Rotational term** $J_q^2 \cdot \hbar_q$: The $q$-deformed rotational energy. For a spin-$\frac{1}{2}$ particle at the substrate parameter $q$, this yields $[1/2]_q [3/2]_q \cdot \hbar_q \approx 0.818 \times 0.0991 = 0.0811$. This vanishes at $q = 1$ (where $\hbar_q \to 0$).
2. **Translational term** $p_q^2 \cdot \hbar_q / (2[n]_q)$: The $q$-deformed kinetic energy from the writhe. The denominator $[n]_q$ provides the $q$-deformed "number of strands" (inertia).
3. **Action term** $\mathfrak{S}_q(K)$: The categorical action $\mathfrak{S}_q = \mathrm{tr}(\mathscr{L}_q)$ evaluated on the knot. This constitutes the **rest mass energy** — the categorical action (Markov trace of the braid representation):

$$
  \mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta))
$$

At a single brane level, this equals $|\mathrm{tr}_M(\rho(\beta))|$ ([categorical mass as Markov trace](#prop:categorical-mass-markov)). For torus knots (including the trefoil / electron), the single-level action is nonzero but the hyperbolic volume vanishes. The mass then arises from the quantum dilogarithm contributions across the tower ([mass endomorphism conjecture](#conj:mass-endomorphism)).

The action term dominates: for hadrons, $\mathfrak{S}_q \sim 10^3$ MeV, while the rotational and translational terms sit at $O(\hbar_q) \sim 0.1$.

**Limits.**

| Limit | $\mathfrak{E}_q$ |
|-------|-------|
| $q = 1$ (classical) | $j(j+1) \cdot 0 + w^2 \cdot 0 + \mathfrak{S}_1 = \mathfrak{S}_1$ |
| $q \to \infty$ (deep-quantum) | $J_q^2 \to q^{2j+1}, \; p_q \to w \cdot q, \; \mathfrak{S}_q \to \infty$ |
| Rest frame | $\mathfrak{S}_q(K)$ (mass) |

**Relation to crossing energy.**

Each crossing in the braid word contributes energy $\mathfrak{E}_\times(q) = \frac{1}{2}(q - q^{-1}) = 0.1045$ (in units of the mass scale $\mu_0$). The total action is:

$$
  \mathfrak{S}_q(K) \;=\; \sum_{j=1}^{k} \mathfrak{E}_\times^{(\epsilon_j)}(q)
$$

where $\epsilon_j = \pm 1$ represents the crossing sign. For a positive crossing: $\mathfrak{E}_\times^{(+)} = q$. For a negative crossing: $\mathfrak{E}_\times^{(-)} = q^{-1}$. The asymmetry $q \neq q^{-1}$ at the substrate parameter $q$ forces positive crossings to carry more energy than negative ones. This is the energy signature of parity violation.
