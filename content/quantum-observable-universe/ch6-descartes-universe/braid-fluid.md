The categorical [braid-group action](#prop:braid-action-tensor) of
[Chapter](#chap:path-integrals-braiding) acquires a direct
hydrodynamic interpretation in the brane fluid.  This subsection
makes the correspondence precise.

**Arnold's geodesic framework.**
V. I. Arnold (1966) showed that the Euler equation for an ideal
incompressible fluid on a Riemannian manifold $(M, g)$ is the
geodesic equation on the infinite-dimensional group
$\mathrm{SDiff}(M)$ of volume-preserving diffeomorphisms, equipped
with the right-invariant $L^2$ metric.  A fluid trajectory
$\phi(t) \in \mathrm{SDiff}(M)$ satisfies

$$
  \nabla_{\dot\phi}\dot\phi = 0
  \quad\text{on}\quad
  \mathrm{SDiff}(M),
$$

where $\nabla$ is the Levi-Civita connection of the $L^2$ metric.
The velocity field $v = \dot\phi \circ \phi^{-1}$ then solves the
Euler equation $\partial_t v + \nabla_v v = -\nabla p$, with
pressure $p$ enforcing incompressibility.

**$q$-deformed volume-preserving diffeomorphisms.**
In the brane fluid, the classical group $\mathrm{SDiff}(M)$ is
replaced by its $q$-deformed analogue
$\mathrm{SDiff}_q(\mathcal{S})$, acting on the
[state bundle](#def:state-bundle) $\mathcal{S}$.  The
$q$-deformation has two effects:

1. The $L^2$ metric is replaced by the
   [Webster inner product](#rem:webster-inner-product) adapted to
   the contact structure $(\theta, \xi)$.  Geodesics on
   $\mathrm{SDiff}_q(\mathcal{S})$ are therefore solutions of the
   [quantum Euler equation](#rem:madelung-fluid) with quantum
   pressure $Q_q$.

2. The group $\mathrm{SDiff}_q(\mathcal{S})$ admits a
   finite-dimensional quotient onto the braid group $B_n$ via the
   **vortex reduction**: restricting attention to flows whose
   vorticity is concentrated on $n$ parallel filaments yields a
   finite-dimensional configuration space
   $\mathrm{Conf}_n(M) / S_n$, whose fundamental group is $B_n$.

**Braid generators as vortex exchanges.**
Each Artin generator $\sigma_i \in B_n$ corresponds to a specific
vortex-tube exchange: the $i$-th and $(i+1)$-th filaments wind
around each other through a half-twist, with the rotation sense
determined by the sign of the [R-matrix](#prop:r-matrix-braiding-structure).
Concretely:

- The [braid-group representation](#prop:braid-action-tensor)
  $\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V}
  \otimes \mathrm{id}^{\otimes(n-i-1)}$
  acts on the $n$-fold tensor product $V^{\otimes n}$ of
  $\mathrm{SU}_q(2)$ representations.

- In the brane fluid, this same $\rho_n(\sigma_i)$ is realised as
  the **holonomy of the $\mathrm{SU}(2)$ connection $A$** around
  the exchange path of two vortex tubes.  The R-matrix
  $\check{R} = P \circ \mathcal{R}$ computes the phase acquired
  during the exchange.

- The [Yang--Baxter equation](#prop:r-matrix-braiding-structure)
  $\mathcal{R}_{12}\mathcal{R}_{13}\mathcal{R}_{23} =
  \mathcal{R}_{23}\mathcal{R}_{13}\mathcal{R}_{12}$
  ensures that the result of braiding three vortices is
  independent of the decomposition into pairwise exchanges — the
  hydrodynamic analogue of Reidemeister III invariance.

**The dictionary.**
The following table summarises the correspondence between the
categorical braid theory and its fluid realisation:

| Categorical (Ch 4) | Hydrodynamic (brane fluid) |
|---|---|
| Braided monoidal category $\mathbf{C}$ | $\mathrm{SDiff}_q(\mathcal{S})$ with Webster metric |
| Braiding $c_{V,V} \colon V \otimes V \to V \otimes V$ | Half-twist exchange of two vortex tubes |
| Artin generator $\sigma_i$ | Pairwise vortex exchange in $\mathrm{Conf}_n$ |
| Yang--Baxter equation | Path-independence of 3-vortex braiding |
| R-matrix eigenvalues $q, -q^{-1}$ | Symmetric / antisymmetric scattering channels |
| [Hecke relation](#sec:hecke-skein) $(T - q)(T + q^{-1}) = 0$ | Two-outcome vortex collision: pass-through vs reconnection |
| [Markov trace](#prop:jones-markov-trace) $\to$ Jones polynomial | Topological invariant of the vortex tangle |
| [Crossing energy](#def:crossing-energy) | Kinetic energy of vortex exchange |

**Physical interpretation.**
The Hecke relation $(T - q)(T + q^{-1}) = 0$ has a sharp fluid
meaning: when two vortex tubes approach, the interaction has
exactly two eigenvalues.  The $q$-eigenvalue corresponds to
**symmetric scattering** (the tubes pass through each other,
exchanging strands but preserving topology), while the
$(-q^{-1})$-eigenvalue corresponds to **antisymmetric
reconnection** (the tubes break and rejoin in a new topology).
The ratio

$$
  \frac{\text{reconnection amplitude}}{\text{pass-through amplitude}}
  \;=\; \frac{q^{-1}}{q}
  \;=\; q^{-2}
$$

is universal — it depends only on the substrate parameter, not on
the vortex configuration.  This universality is the fluid-dynamical
origin of the [skein crossing asymmetry](#rem:skein-crossing-asymmetry):
the asymmetry between $L_+$ and $L_-$ in the skein relation is
precisely the asymmetry between pass-through and reconnection in
vortex scattering.

**Helicity as Markov trace.**
The [Jones polynomial](#prop:jones-markov-trace) $J_L(q)$, computed
as the Markov trace on the Hecke algebra, acquires a hydrodynamic
meaning: it is the **topological helicity** of the vortex tangle.
Classical helicity $H = \int v \cdot \omega\,dV$ measures the
linking and knotting of vortex lines; the Jones polynomial refines
this to a full knot invariant that distinguishes vortex
configurations invisible to classical helicity (e.g. the trefoil
from the unknot, both of which can have $H = 0$).
