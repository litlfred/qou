This remark unpacks the three terms of the [$q$-energy](#def:q-energy) $\mathfrak{E}_q(K)$ in the aether action/mass chart of the [categorical Hamiltonian](#def:categorical-hamiltonian), its classical and deep-quantum limits, and its distinction from the crossing energy.

**The three terms.**

1. **Rotational term** $J_q^2 \cdot \hbar_q$: The $q$-deformed rotational contribution. For a spin-$\frac{1}{2}$ state at the aether parameter $q$, $[1/2]_q [3/2]_q \cdot \hbar_q \approx 0.818 \times 0.0991 \approx 0.0811$. This vanishes at $q = 1$ (where $\hbar_q \to 0$).
2. **Translational term** $p_q^2 \cdot \hbar_q / (2[n]_q)$: The $q$-deformed writhe kinetic contribution, with denominator $[n]_q$ supplying the $q$-deformed strand inertia.
3. **Rest-action term** $\mathfrak{S}_q(K)$: The categorical action $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$ evaluated on the static knot ($\mathcal{L}_1 = 0$), which coincides with the rest projection of the [categorical Hamiltonian](#def:categorical-hamiltonian) in the aether mass chart ($\ell_P = \hbar_q\,t_P = 1$):

$$
  \mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta)).
$$

At a single brane level, its magnitude equals $|\mathrm{tr}_M(\rho(\beta))|$ ([categorical mass as Markov trace](#prop:categorical-mass-markov)). Converting from the aether mass chart to the causal-cone chart multiplies by $c_q^2 = 1/(q - 1)^2$, while dividing the electronic causal-cone rest energy $\mathfrak{m}_e c_q^2$ by the Planck tick $t_P = q/(q - 1)$ yields the per-tick hadronic scale $\mathfrak{E}_0 = \mathfrak{m}_e/\bigl(q(q - 1)\bigr)$. For torus knots (including the trefoil), the single-level trace is nonzero whereas the hyperbolic volume vanishes; the tower mass arises from quantum dilogarithm contributions across the brane tower ([mass endomorphism conjecture](#conj:mass-endomorphism)).

**Limits.**

| Limit | $\mathfrak{E}_q(K)$ (aether mass chart) |
|-------|-------|
| $q = 1$ (classical) | $j(j+1) \cdot 0 + w^2 \cdot 0 + \mathfrak{S}_1 = \mathfrak{S}_1$ |
| $q \to \infty$ (deep-quantum) | $J_q^2 \to q^{2j+1}, \; p_q \to w \cdot q, \; \mathfrak{S}_q \to \infty$ |
| Rest frame ($p_q = 0, J_q = 0$) | $\mathfrak{S}_q(K) = \mathfrak{m}(K)$ (rescaled to $\mathfrak{m}(K)\,c_q^2$ in the causal-cone chart) |

**Distinction from crossing energy.**

Whereas $\mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta))$ is a non-additive Markov trace invariant under braid conjugation and Reidemeister moves (up to framing), the crossing-level functional assigns $q$ to each positive crossing and $-q^{-1}$ to each negative crossing, with mean asymmetry $\frac{1}{2}(q - q^{-1}) \approx 0.1045$ per crossing. Because $q \neq q^{-1}$, positive and negative crossings carry unequal Skein weights, providing the algebraic source of parity asymmetry before trace evaluation.
