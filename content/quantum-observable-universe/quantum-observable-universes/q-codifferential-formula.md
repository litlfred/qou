In the archimedean realisation, the $q$-exterior derivative is
$d_q = q^{-1}d + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi$
([archimedean $d_q$](#ex:q-ext-deriv)). To find the formal adjoint
$\delta_q$ with respect to the Webster inner product
$\langle \cdot, \cdot \rangle_\varTheta$, every operation in $d_q$ is
replaced by its geometric mirror:

- The classical derivative $d$ becomes the classical codifferential
  $\delta$.
- Wedging with the contact form ($\varTheta \wedge$) becomes
  contraction with the Reeb vector field ($\iota_\xi$), because
  $\xi$ is the metric dual to $\varTheta$: $\varTheta(X) = \langle \xi, X \rangle_\varTheta$ for all $X$.
- The Lie derivative $\mathcal{L}_\xi$ becomes its formal adjoint
  $\mathcal{L}_\xi^*$.

The resulting closed formula is:

$$
  \delta_q =  q^{-1}\delta
  +  (1 - q^{-1})\mathcal{L}_\xi^* \circ \iota_\xi.
$$

In words: where $d_q$ uses the Reeb vector field to *add* a vertical
spin twist to a form (via $\varTheta \wedge \mathcal{L}_\xi$), the
codifferential $\delta_q$ uses contraction with $\xi$ (via
$\iota_\xi$) to *extract* and step down that vertical spin. They are
exact geometric duals under the Webster metric.

The $q$-codifferential is uniquely characterised by the
adjoint relation:

$$
  \langle d_q\alpha, \beta \rangle_\varTheta
  = 
  \langle \alpha, \delta_q\beta \rangle_\varTheta
$$

for all compactly supported forms $\alpha, \beta$.
