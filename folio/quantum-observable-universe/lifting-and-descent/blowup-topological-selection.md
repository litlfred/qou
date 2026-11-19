**The :refterm[descent]{#descent} condition and vortex reconnection.**
The [twisted 2-cocycle condition](#prop:descent-condition)
$$
  d(g_{ijk}^{(n)}) = a_{ij}^{(n)} \cdot g_{ijk}^{(n)}
  \cdot (a_{jk}^{(n)})^{-1}
$$
fails at the singular set $\Sigma$ because the transition functions $g_{ij}^{(n)}$ develop discontinuities there. These discontinuities correspond to [vortex reconnection](#rem:vortex-reconnection) events where the divisor topology changes. The obstruction class $\kappa_{n^*}$ measures the total topological change at $\Sigma$. It acts as the net "reconnection charge": the signed count of reconnection events weighted by their fusion-rule multiplicities.

**Constraint from Berry phase.**
The obstruction class must align with $\mathrm{SU}_q(2)$ representation theory. The class $\kappa_{n^*}$ must lie in the image of the character map:
$$
  \chi \colon
  \mathrm{Rep}(\mathrm{SU}_q(2))
   \to 
  H^2(\Sigma, \mathcal{B}).
$$
This restricts the possible values of $\kappa_{n^*}$ to a discrete lattice. This forms a **topological selection rule** on the blowup: only vorticity concentrations with cohomological charges compatible with the categorical structure are permitted.
