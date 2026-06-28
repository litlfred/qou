The number of stable nuclear configurations at a given substrate
parameter $q$ is **finite**.  The stability boundary is the zero
locus of the Skein polynomial $P_{\mathcal{N}(p,n)}(q)$.

## The nuclear chart lattice

The set of stable configurations forms a **finite lattice**
in the $(p, n)$ plane:

$$
  \mathcal{L}(q)
  = 
  \bigl\{
    (p, n) \in \mathbb{N}^2 :
    P_{\mathcal{N}(p,n)}(q) > 0
  \bigr\}
$$

This lattice is bounded by:
- The **beta-stability line** $p^*(A)$
  ([beta stability](#prop:beta-stability)) — the minimum-energy
  proton count at each $A$.
- The **Skein polynomial zero** $P(q) = 0$ — the drip line
  where the Skein polynomial changes sign.
- The **shell closures** ([shell closure](#prop:shell-closure-normal-form))
  — islands of enhanced stability where the palindromic Poincaré
  distribution gives maximum binding.

The lattice $\mathcal{L}(q)$ at $q = q_0$ reproduces the
experimental nuclear chart: stable isotopes cluster along the
valley of stability with magic-number shell closures at
$N, Z \in \{2, 8, 20, 28, 50, 82, 126\}$.
