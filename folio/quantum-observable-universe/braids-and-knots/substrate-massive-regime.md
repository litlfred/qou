**Proposition.** *Let $q \in \mathbb{R}$ with $q > 0$ and $q \neq 1$, and set*

$$
  \delta(q) = q + q^{-1}, \qquad \Delta(q) = \tfrac{1}{2}\,\delta(q).
$$

*Then $\Delta(q) > 1$.*

Here $\delta$ is the Temperley--Lieb loop weight, the balanced quantum integer $[2]_q$, and $\Delta$ is the anisotropy of the associated spin chain. The proof is the arithmetic--geometric mean inequality in the form $q + q^{-1} - 2 = (q-1)^2/q$, which is strictly positive exactly when $q \neq 1$.

Two features of the statement matter more than its difficulty.

First, the hypothesis is *only* $q \neq 1$. No calibration input enters, and no parameter is available to adjust: the conclusion is forced by the substrate being a genuine deformation rather than the classical point. Writing $q = e^{\lambda}$ gives $\Delta = \cosh \lambda$, so the inequality is the statement that a real deformation parameter cannot produce $|\Delta| < 1$.

Second, the value $\Delta = 1$ is a phase boundary rather than an arbitrary threshold. The regime $\Delta > 1$ is the massive, Ising-like phase of the chain; the regime $|\Delta| < 1$ is the massless phase, reached only on $|q| = 1$. The contrapositive is recorded alongside the proposition: an anisotropy at or below unity forces $q = 1$, so the massless phase is unreachable from a real substrate parameter.

## Algebraic structure

The algebraic content is stated over a generic field, with no ordering and no archimedean construct, and the inequality is separated into its own section over $\mathbb{R}$. Two scalar identities are recorded as well:

$$
  2\Delta(q) + h(q) = 2q, \qquad 2\Delta(q) - h(q) = 2q^{-1},
  \qquad h(q) = q - q^{-1},
$$

which say that the anisotropy and the Hecke parameter recombine to $q$ and $q^{-1}$. These are the entries in which the Temperley--Lieb generator differs from an undeformed exchange operator, and they are what the identification in the accompanying remark rests on.
