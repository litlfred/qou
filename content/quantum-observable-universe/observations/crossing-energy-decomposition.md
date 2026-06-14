*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The [crossing energy](#def:crossing-energy) assigns weights
$+q$ to positive crossings and $-q^{-1}$ to negative crossings,
with $q > 1$.  Writing $q = e^\lambda$ where $\lambda = \ln q > 0$,
the crossing weights decompose into symmetric and antisymmetric
parts under the mirror operation $\sigma$:

$$
  q =  \cosh\lambda + \sinh\lambda, \qquad
  q^{-1} =  \cosh\lambda - \sinh\lambda.
$$

**Statement.**
For any knot composite $\mathfrak{H}$ with crossing energy
$\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = \sum_i \epsilon_i$ where
$\epsilon_i \in \{q, -q^{-1}\}$:

1. **Symmetric channel.**  The component
   $E_{\mathrm{sym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \cosh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$
   is invariant under the mirror operation $\sigma$ (which reverses
   all crossing signs).

2. **Antisymmetric channel.**  The component
   $E_{\mathrm{asym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \sinh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$
   reverses sign under $\sigma$.

3. **Pair cancellation.**  For a particle--antiparticle pair
   $(\mathfrak{H}, \mathfrak{H}^{\sigma})$, the combined crossing energy is purely
   antisymmetric:

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) + \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma})
     =  2E_{\mathrm{asym}}(\mathfrak{H}).
   $$

4. **Ratio identity.**  The antisymmetric-to-symmetric ratio is

   $$
     \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
     =  \tanh(\ln q),
   $$

   independent of the knot composite $\mathfrak{H}$.

## Algebraic-to-hyperbolic bridge

The decomposition is the per-crossing case of a general identity: writing
$\lambda = \ln q$, every algebraic $q$-power is a hyperbolic exponential,

$$
  q^{n} = \cosh(n\lambda) + \sinh(n\lambda),
  \qquad
  q^{n} - q^{-n} = 2\sinh(n\lambda),
$$

consequently the **quantum integer is a ratio of hyperbolic sines**:

$$
  [n]_q \;=\; \frac{q^{n} - q^{-n}}{q - q^{-1}}
  \;=\; \frac{\sinh(n\lambda)}{\sinh(\lambda)}.
$$

This is the precise sense in which the Hecke datum is *archimedean*: the
discrete algebraic invariant $[n]_q \in \mathbb{Z}[q^{\pm 1/2}]$ is a value
of the transcendental hyperbolic sine at the crossing rapidity $\lambda$.
It is the $q$-deformed seed of the Kashaev volume realisation
([Kashaev as Archimedean realisation](#rem:kashaev-as-archimedean-realization)),
where the $N\to\infty$ limit of the colored Jones polynomial integrates
these hyperbolic lengths into the transcendental knot volume. The
$\cosh = q^{n} + q^{-n}$ symmetric (strong) and $\sinh = q^{n} - q^{-n}$
antisymmetric (Coulomb) channels are the real and "rotational" parts of
that exponential.

These identities are formalised in the Lean sibling
(`q_pow_eq_cosh_add_sinh`, `two_sinh_nat_log`, `qbracket_eq_sinh_ratio`),
holding for every $q > 0$.
