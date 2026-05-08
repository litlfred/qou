The categorical [braid-group action](#prop:braid-action-tensor)
acquires a hydrodynamic interpretation in the brane fluid.

**Arnold's geodesic framework.**
Arnold (1966) showed that the Euler equation on $(M, g)$ is the
geodesic equation on $\mathrm{SDiff}(M)$ with the $L^2$ metric:
$\nabla_{\dot\phi}\dot\phi = 0$.  The velocity
$v = \dot\phi \circ \phi^{-1}$ solves
$\partial_t v + \nabla_v v = -\nabla p$.

**$q$-deformed diffeomorphisms.**
The classical $\mathrm{SDiff}(M)$ is replaced by
$\mathrm{SDiff}_q(\mathcal{S})$ on the
[state bundle](#ex:c-quantum-observable-universe), with two consequences:

1. The $L^2$ metric becomes the
   [Webster inner product](#rem:webster-inner-product).
   Geodesics solve the [quantum Euler
   equation](#rem:madelung-fluid) with pressure $Q_q$.

2. Restricting to flows with vorticity on $n$ filaments gives
   a quotient onto $B_n$: the configuration space
   $\mathrm{Conf}_n(M)/S_n$ has fundamental group $B_n$.

**Braid generators as vortex exchanges.**
Each Artin generator $\sigma_i$ is a half-twist exchange of
filaments $i$ and $i+1$.  The
[representation](#prop:braid-action-tensor)
$\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V}
\otimes \mathrm{id}^{\otimes(n-i-1)}$
is realised as holonomy of the $\mathrm{SU}(2)$ connection around
the exchange path.  The [Yang--Baxter
equation](#prop:r-matrix-braiding-structure) ensures braiding
three vortices is path-independent (Reidemeister III).

**The dictionary.**

| Categorical (Ch 4) | Hydrodynamic |
|---|---|
| Braided monoidal $\mathbf{C}$ | $\mathrm{SDiff}_q(\mathcal{S})$ |
| Braiding $c_{V,V}$ | Half-twist vortex exchange |
| Yang--Baxter | Path-independence of 3-vortex braiding |
| R-matrix eigenvalues $q, -q^{-1}$ | Symmetric / antisymmetric channels |
| [Hecke relation](#rem:skein-crossing-asymmetry) | Pass-through vs reconnection |
| [Markov trace](#thm:jones-markov-trace) | Topological helicity |
| [Crossing energy](#def:crossing-energy) | Kinetic energy of exchange |

**Hecke relation as scattering.**
$(T - q)(T + q^{-1}) = 0$ means two vortex tubes interact with
exactly two eigenvalues: $q$ (symmetric pass-through) and
$-q^{-1}$ (antisymmetric reconnection).  The universal ratio

$$
  \frac{\text{reconnection}}{\text{pass-through}}
  = q^{-2}
$$

depends only on the substrate parameter.  This is the
fluid-dynamical origin of the
[skein crossing asymmetry](#rem:skein-crossing-asymmetry).

**Helicity as Markov trace.**
The [Jones polynomial](#thm:jones-markov-trace) $J_L(q)$ is
the **topological helicity** of the vortex tangle — a refinement
of classical helicity $H = \int v \cdot \omegadV$ that
distinguishes configurations invisible to $H$ (e.g. trefoil
from unknot).
