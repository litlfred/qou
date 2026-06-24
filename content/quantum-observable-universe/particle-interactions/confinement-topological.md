Confinement is **topological**, not energetic.  This is proved
by showing that the linear program over $H_3(q)$ has a strictly
lower optimum than $\mathcal{B}_3$, but that optimum is not
realizable as a braid group element.

## Statement

**Proposition.**
*Let $G \in \mathbb{R}^{6 \times 6}$ be the Gram matrix of $H_3(q)$
at $q = q_0$ ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).
Consider the linear program:*

$$
  \min_{x \in \mathbb{R}^6} \;
  \sum_{i=1}^{6} t_i x_i
  \qquad
  \text{s.t.} \quad
  \mathbf{1}^\top x = n_{\mathrm{target}},
  \quad
  Gx \geq 0
$$

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the
NF basis elements.*

**(i)** *The LP has optimal value $\mathrm{tr}_M^* = 0$, achieved
by exploiting the negative eigenvalue $\lambda_{\min}(G) < 0$.*

**(ii)** *The LP optimum $x^*$ has $|x_i^*| \gg 1$ for some
components (specifically $x_{e^-}^* \to +\infty$ without bounds).
It is NOT in the image of the braid group representation
$\rho \colon B_3 \to H_3(q)$.*

**(iii)** *Among all elements $\Phi \in H_3(q)$ that are images
of braid group elements of length $\leq 6$,
$\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the unique element
with $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - n_{\mathrm{target}}| = 0$
for both proton and neutron typed crossings.*

## Proof of (iii): exhaustive enumeration

Among the $4^6 = 4096$ braid words of length exactly $6$ over
generators $\{\sigma_0, \sigma_1, \sigma_0^{-1}, \sigma_1^{-1}\}$,
and all shorter words:

- $\mathcal{B}_3 = \sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1}$
  achieves $|\Delta\mathrm{net}| = 0.000$ for both proton and neutron.
- The mirror $\mathcal{B}_3^{\sigma} = \sigma_0^{-1}\sigma_1\sigma_0^{-1}\sigma_1\sigma_0^{-1}\sigma_1$
  achieves $|\Delta\mathrm{net}| = 0.004$ — an order of magnitude worse.
- All other words have $|\Delta\mathrm{net}| > 0.01$.

## Physical interpretation

The LP result has a precise physical meaning:

1. **Energy minimization alone permits unphysical states.**
   The continuous LP finds algebra elements with zero Markov trace
   (zero action) by mixing basis elements with large negative
   coefficients.  These cannot be realized as physical braid words.

2. **The Borromean property is an independent constraint.**
   The topological requirement that removing any one quark
   unlinks the other two (Borromean linking) restricts the
   feasible set from $\mathbb{R}^6$ to the image of $B_3$
   under $\rho$.  This discrete constraint is what selects
   $\mathcal{B}_3$.

3. **Confinement = topology + action minimization.**
   $\mathcal{B}_3$ is selected by the conjunction of:
   (a) Borromean topology (braid group element),
   (b) net constraint (physical mass),
   (c) minimum action among (a)+(b)-feasible elements.

**Witness**: `confinement-lp.witness.json`.
