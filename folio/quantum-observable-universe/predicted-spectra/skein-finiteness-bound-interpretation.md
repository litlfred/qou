The number of stable nuclear configurations at a given aether parameter $q$ is finite. The stability boundary precisely traces the zero locus of the Skein polynomial $P_{\mathcal{N}(p,n)}(q)$.

## The nuclear chart lattice

The set of stable configurations forms a finite lattice in the $(p, n)$ plane:

$$
  \mathcal{L}(q)
  = 
  \bigl\{
    (p, n) \in \mathbb{N}^2 :
    P_{\mathcal{N}(p,n)}(q) > 0
  \bigr\}
$$

Three boundaries constrain this lattice:
- The beta-stability line $p^*(A)$ ([beta stability](#prop:beta-stability)). This defines the minimum-energy proton count at each $A$.
- The Skein polynomial zero $P(q) = 0$. This defines the drip line where the Skein polynomial changes sign.
- The shell closures ([shell closure](#prop:shell-closure-normal-form)). These form islands of enhanced stability where the palindromic Poincaré distribution maximizes binding.

The lattice $\mathcal{L}(q)$ at $q = q_0$ reproduces the experimental nuclear chart. Stable isotopes cluster tightly along the valley of stability. They are anchored by magic-number shell closures at $N, Z \in \{2, 8, 20, 28, 50, 82, 126\}$.

## Particle finiteness

The identical argument restricts elementary particles. A knot $K$ on the Bring surface ($\chi = -6$, genus $4$) must satisfy two conditions:

1. **Embeddability**: The torus knot $T_{m,n}$ embeds in genus $g$ only if $(m-1)(n-1)/2 \leq g$. For $g = 4$, this forces $(m-1)(n-1) \leq 8$.
2. **Positive Skein polynomial**: At the physical parameter $q$, $P_K(q) > 0$.

The embeddability constraint immediately produces a finite list of allowed torus knots: $T_{2,3}$, $T_{2,5}$, $T_{2,7}$, $T_{2,9}$, $T_{3,4}$, $T_{3,5}$. These correspond exactly to the quarks, leptons, and force carriers. No other torus knot fits on the Bring surface.
