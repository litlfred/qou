The categorical [braid-group action](#prop:braid-action-tensor) possesses a direct hydrodynamic interpretation on the brane fluid.

**Arnold's geodesic framework.**
Arnold demonstrated that the Euler equation on $(M, g)$ behaves exactly as the geodesic equation over $\mathrm{SDiff}(M)$ acting under the $L^2$ metric: $\nabla_{\dot\phi}\dot\phi = 0$. The velocity vector $v = \dot\phi \circ \phi^{-1}$ solves $\partial_t v + \nabla_v v = -\nabla p$.

**$q$-deformed diffeomorphisms.**
The [state bundle](#ex:c-quantum-observable-universe) promotes the classical $\mathrm{SDiff}(M)$ group to $\mathrm{SDiff}_q(\mathcal{S})$. This imposes two structural shifts:

1. The $L^2$ metric upgrades to the [Webster inner product](#sec:webster-inner-product). The resulting geodesics solve the [quantum Euler equation](#rem:madelung-fluid) subject to pressure $Q_q$.
2. Confining the state space to flows exhibiting concentrated vorticity across $n$ filaments forces a strict topological quotient onto $B_n$. The fundamental group of the configuration space $\mathrm{Conf}_n(M)/S_n$ resolves uniquely to $B_n$.

**Braid generators as vortex exchanges.**
The Artin generator $\sigma_i$ dictates the half-twist spatial exchange of filaments $i$ and $i+1$. The representation $\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V} \otimes \mathrm{id}^{\otimes(n-i-1)}$ ([braid-group action on tensor powers](#prop:braid-action-tensor)) manifests physically as the $\mathrm{SU}(2)$ holonomy traversing the exchange path. The [Yang--Baxter equation](#prop:r-matrix-braiding-structure) enforces Reidemeister III, ensuring three-vortex braiding stays rigorously path-independent.

**The dictionary.**

The [braid--fluid dictionary table](#tbl:braid-fluid-table-data) summarises the structural correspondence.

**Hecke relation as scattering.**
The quadratic rule $(T - q)(T + q^{-1}) = 0$ restricts two-vortex interactions to exactly two terminal eigenvalues: $q$ (symmetric unperturbed pass-through) and $-q^{-1}$ (antisymmetric core reconnection). The universal intensity ratio

$$
  \frac{\text{reconnection}}{\text{pass-through}}
  = q^{-2}
$$

relies entirely on the aether parameter. This ratio establishes the fluid-dynamical source mechanism for the [skein crossing asymmetry](#rem:skein-crossing-asymmetry).

**Helicity as Markov trace.**
The [Jones polynomial](#thm:jones-markov-trace) $J_L(q)$ operates as the **topological helicity** governing the vortex tangle. This categorical metric refines classical helicity $H = \int v \cdot \omega \, dV$, distinguishing topological states invisible to $H$ (separating the trefoil from the unknot).
