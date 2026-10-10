The [crossing energy](#def:crossing-energy) assigns $+q$ to positive crossings and $-q^{-1}$ to negative crossings ($q > 1$). Writing $q = e^\lambda$ with $\lambda = \ln q > 0$, the weights decompose into symmetric and antisymmetric components under the mirror operation $\sigma$:

$$
  q = \cosh\lambda + \sinh\lambda, \qquad
  q^{-1} = \cosh\lambda - \sinh\lambda.
$$

Equivalently, in the form that exhibits the mirror action, reversing a crossing negates its $\cosh$ part and leaves its $\sinh$ part unchanged:

$$
  +q = +\cosh\lambda + \sinh\lambda, \qquad -q^{-1} = -\cosh\lambda + \sinh\lambda.
$$

**Statement.**
Let $\mathfrak{H}$ be a knot composite carrying $p$ positive and $m$ negative crossings, so that $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = pq - mq^{-1}$.

1. **Channel decomposition.** Summing the two weights above over the composite gives

   $$
     E_{\mathrm{sym}}(\mathfrak{H}) = (p - m)\cosh\lambda,
     \qquad
     E_{\mathrm{asym}}(\mathfrak{H}) = (p + m)\sinh\lambda,
   $$

   and these reconstruct the crossing energy exactly: $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = E_{\mathrm{sym}}(\mathfrak{H}) + E_{\mathrm{asym}}(\mathfrak{H})$. The two channels carry different multiplicities, $p - m$ against $p + m$, because the $\sinh$ part is blind to the crossing sign.

2. **Mirror behaviour.** The mirror $\sigma$ reverses every crossing, exchanging $p$ and $m$. Hence

   $$
     E_{\mathrm{sym}}(\mathfrak{H}^{\sigma}) = -E_{\mathrm{sym}}(\mathfrak{H}),
     \qquad
     E_{\mathrm{asym}}(\mathfrak{H}^{\sigma}) = E_{\mathrm{asym}}(\mathfrak{H}).
   $$

   The symmetric total negates and the antisymmetric total is fixed. This inverts the parity of the weight functions themselves, where $\cosh$ is even and $\sinh$ is odd in $\lambda$, because under $\sigma$ the multiplicity flips as well.

3. **Pair cancellation.** For a particle-antiparticle pair $(\mathfrak{H}, \mathfrak{H}^{\sigma})$ the symmetric contributions cancel and the antisymmetric contributions add:

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) + \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma})
     = 2E_{\mathrm{asym}}(\mathfrak{H}).
   $$

4. **Ratio identity.** For a positive braid closure, that is $m = 0$ with $p \geq 1$, the antisymmetric-to-symmetric ratio is

   $$
     \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
     = \tanh(\ln q),
   $$

   independent of the crossing number $p$. For a composite with mixed crossing signs and $p \neq m$ the ratio acquires the multiplicity factor

   $$
     \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
     = \frac{p + m}{p - m}\,\tanh(\ln q),
   $$

   so it is not independent of $\mathfrak{H}$ in general.

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
