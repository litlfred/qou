The [crossing energy](#def:crossing-energy) assigns $+q$ to positive crossings and $-q^{-1}$ to negative crossings ($q > 1$). Writing $q = e^\lambda$ with $\lambda = \ln q > 0$, the weights decompose into symmetric and antisymmetric components under the mirror operation $\sigma$:

$$
  q = \cosh\lambda + \sinh\lambda, \qquad
  q^{-1} = \cosh\lambda - \sinh\lambda.
$$

**Statement.**
Let $\mathfrak{H}$ be a knot composite with crossing energy $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = \sum_i \epsilon_i$, where $\epsilon_i \in \{q, -q^{-1}\}$.

1. **Symmetric channel.** The component $E_{\mathrm{sym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \cosh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$ is invariant under $\sigma$.
2. **Antisymmetric channel.** The component $E_{\mathrm{asym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \sinh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$ reverses sign under $\sigma$.
3. **Pair cancellation.** For a particle-antiparticle pair $(\mathfrak{H}, \mathfrak{H}^{\sigma})$, the combined crossing energy is antisymmetric:

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) + \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma})
     = 2E_{\mathrm{asym}}(\mathfrak{H}).
   $$

4. **Ratio identity.** The antisymmetric-to-symmetric ratio is

   $$
     \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
     = \tanh(\ln q),
   $$

   which is independent of $\mathfrak{H}$.

## Algebraic-to-hyperbolic bridge

Writing $\lambda = \ln q$, every algebraic $q$-power maps to a hyperbolic exponential:

$$
  q^{n} = \cosh(n\lambda) + \sinh(n\lambda),
  \qquad
  q^{n} - q^{-n} = 2\sinh(n\lambda).
$$

The quantum integer evaluates to a ratio of hyperbolic sines:

$$
  [n]_q \;=\; \frac{q^{n} - q^{-n}}{q - q^{-1}}
  \;=\; \frac{\sinh(n\lambda)}{\sinh(\lambda)}.
$$

This Archimedean evaluation of the Hecke datum seeds the Kashaev volume realization ([Kashaev as Archimedean realisation](#rem:kashaev-as-archimedean-realization)). The limit $N \to \infty$ of the colored Jones polynomial integrates these lengths into the knot volume. The symmetric $\cosh$ and antisymmetric $\sinh$ channels denote the real and rotational parts.
