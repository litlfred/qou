The [crossing energy](#def:crossing-energy) assigns weights
$+q$ to positive crossings and $-q^{-1}$ to negative crossings,
with $q > 1$.  Writing $q = e^\lambda$ where $\lambda = \ln q > 0$,
the crossing weights decompose into symmetric and antisymmetric
parts under the mirror operation $\sigma$:

$$
  q \;=\; \cosh\lambda + \sinh\lambda, \qquad
  q^{-1} \;=\; \cosh\lambda - \sinh\lambda.
$$

**Statement.**
For any knot composite $H$ with crossing energy
$\mathbf{E}_{\mathrm{cross}}(H) = \sum_i \epsilon_i$ where
$\epsilon_i \in \{q, -q^{-1}\}$:

1. **Symmetric channel.**  The component
   $E_{\mathrm{sym}}(H) = \sum_i |\epsilon_i| \cdot \cosh(\ln q)
   \cdot \mathrm{sgn}(\epsilon_i)$
   is invariant under the mirror operation $\sigma$ (which reverses
   all crossing signs).

2. **Antisymmetric channel.**  The component
   $E_{\mathrm{asym}}(H) = \sum_i |\epsilon_i| \cdot \sinh(\ln q)
   \cdot \mathrm{sgn}(\epsilon_i)$
   reverses sign under $\sigma$.

3. **Pair cancellation.**  For a particle--antiparticle pair
   $(H, \sigma(H))$, the combined crossing energy is purely
   antisymmetric:
   $$
     \mathbf{E}_{\mathrm{cross}}(H) + \mathbf{E}_{\mathrm{cross}}(\sigma(H))
     \;=\; 2\,E_{\mathrm{asym}}(H).
   $$

4. **Ratio identity.**  The antisymmetric-to-symmetric ratio is
   $$
     \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
     \;=\; \tanh(\ln q),
   $$
   independent of the knot composite $H$.
