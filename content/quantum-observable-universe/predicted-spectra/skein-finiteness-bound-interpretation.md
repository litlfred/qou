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

## Particle finiteness

The same argument applies to elementary particles.  A knot $K$
on the Bring surface ($\chi = -6$, genus $4$) must satisfy:

1. **Embeddability**: the torus knot $T_{m,n}$ embeds in
   genus $g$ only if $(m-1)(n-1)/2 \leq g$.  For $g = 4$:
   $(m-1)(n-1) \leq 8$.

2. **Positive Skein polynomial**: $P_K(q) > 0$ at the
   physical $q$.

The embeddability constraint gives a **finite list** of allowed
torus knots: $T_{2,3}$, $T_{2,5}$, $T_{2,7}$, $T_{2,9}$,
$T_{3,4}$, $T_{3,5}$.  These are the quarks, leptons, and force
carriers.  No other torus knot fits on the Bring surface — the
particle content is **determined by the genus**.
