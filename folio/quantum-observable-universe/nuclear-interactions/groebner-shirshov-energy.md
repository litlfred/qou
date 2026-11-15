The Gröbner--Shirshov basis theory gives a stronger result than uniqueness: the energy of the nuclear braid word is a topological invariant, computed with no path dependence. The invariance holds for a fixed word; it does not say that the word selected for a nucleus is independent of the order in which it was assembled.

**Theorem.**
Define the energy functional on $H_A(q)$ by

$$
  E(\xi) =  \sum_{w \in B} |c_w(q)| \cdot \ell(w)
$$

where $\xi$ is the normal form and $\ell(w)$ is the word length. Then:

1. **Only Hecke reductions change energy.** The Yang--Baxter relation and far commutativity preserve coefficients and lengths. The Hecke relation is the unique energy-changing generator.
2. **Energy is path-independent.** The total energy change is independent of the order of applied basis elements. This follows from confluence.
3. **Each Hecke step has a definite energy.** Replacing $\sigma_i^2$ with $(q - q^{-1})\sigma_i + 1$ changes energy by $|c| \cdot |q - q^{-1}|$. Every Hecke step increases the total weight.

**Archimedean specialisation.** The energy $|c|\,(q - q^{-1})$ and its positivity for $q > 1$ are stated over $\mathbb{R}$. What follows sits on the archimedean side of the substrate wall.
