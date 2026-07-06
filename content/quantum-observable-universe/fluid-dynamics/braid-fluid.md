The categorical [braid-group action](#prop:braid-action-tensor) acquires a hydrodynamic interpretation in the brane fluid.

**Arnold's geodesic framework.**
Arnold (1966) showed that the Euler equation on $(M, g)$ is the geodesic equation on $\mathrm{SDiff}(M)$ with the $L^2$ metric: $\nabla_{\dot\phi}\dot\phi = 0$. The velocity $v = \dot\phi \circ \phi^{-1}$ solves $\partial_t v + \nabla_v v = -\nabla p$.

**$q$-deformed diffeomorphisms.**
The classical group $\mathrm{SDiff}(M)$ is replaced by $\mathrm{SDiff}_q(\mathcal{S})$ on the [state bundle](#ex:c-quantum-observable-universe). This has two consequences:

1. The $L^2$ metric becomes the [Webster inner product](#sec:webster-inner-product). Geodesics solve the [quantum Euler equation](#rem:madelung-fluid) with pressure $Q_q$.
2. Restricting to flows with vorticity on $n$ filaments gives a quotient onto $B_n$. The configuration space $\mathrm{Conf}_n(M)/S_n$ has fundamental group $B_n$.

**Braid generators as vortex exchanges.**
Each Artin generator $\sigma_i$ acts as a half-twist exchange of filaments $i$ and $i+1$. The [representation](#prop:braid-action-tensor) $\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V} \otimes \mathrm{id}^{\otimes(n-i-1)}$ is realised as the holonomy of the $\mathrm{SU}(2)$ connection around the exchange path. The [Yang--Baxter equation](#prop:r-matrix-braiding-structure) ensures braiding three vortices remains path-independent (Reidemeister III).

**The dictionary.**

See [Table](#tbl:braid-fluid-table-data).

**Hecke relation as scattering.**
The relation $(T - q)(T + q^{-1}) = 0$ implies two vortex tubes interact with exactly two eigenvalues: $q$ (symmetric pass-through) and $-q^{-1}$ (antisymmetric reconnection). The universal ratio

$$
  \frac{\text{reconnection}}{\text{pass-through}}
  = q^{-2}
$$

depends only on the substrate parameter. This provides the fluid-dynamical origin of the [skein crossing asymmetry](#rem:skein-crossing-asymmetry).

**Helicity as Markov trace.**
The [Jones polynomial](#thm:jones-markov-trace) $J_L(q)$ measures the **topological helicity** of the vortex tangle. This refines classical helicity $H = \int v \cdot \omegadV$ and distinguishes configurations invisible to $H$ (e.g. trefoil from unknot).
