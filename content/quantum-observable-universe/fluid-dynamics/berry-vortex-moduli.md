Fix an intensity level $j$ and a topological type (knot type
$K$).  The **moduli space** $\mathcal{M}_{j,K}$ is the space of
[geodesic vortex](#rem:geodesic-vortices) configurations of type
$(j, K)$ modulo gauge equivalence:

$$
  \mathcal{M}_{j,K}
  = 
  \bigl\{
    \varrho \colon S^1 \to \mathcal{S}
     \big| 
    \delta\mathcal{E}_q[\varrho] = 0,
    \mathrm{type}(\varrho) = K,
    \mathrm{level}(\varrho) = j
  \bigr\}
  \big/ \mathcal{G},
$$

where $\mathcal{G}$ is the gauge group.  For the fundamental
fermion ($j = \frac{1}{2}$, $K$ = trefoil), $\mathcal{M}_{1/2, T_{2,3}}$
is a finite-dimensional manifold parametrised by the position and
orientation of the vortex filament.

**Berry connection.**
The $q$-Schrödinger equation restricted to states near the
vortex ground state defines a line bundle
$\mathcal{L} \to \mathcal{M}_{j,K}$ whose fibre at a vortex
configuration $\varrho$ is the ground-state eigenspace of the
linearised Hamiltonian around $\varrho$.  The **Berry connection**
on this bundle is

$$
  \mathcal{A}_{\mathrm{Berry}}
  = 
  i\langle\psi_\varrho|d|\psi_\varrho\rangle,
$$

where $|\psi_\varrho\rangle$ is the ground state at configuration
$\varrho$ and $d$ is the exterior derivative on $\mathcal{M}_{j,K}$.

**Berry curvature.**
The curvature $\mathcal{F} = d\mathcal{A}_{\mathrm{Berry}}$
measures the local geometric phase per unit area in moduli space.
For a vortex configuration with $n$ well-separated filaments
$\{\varrho_1, \ldots, \varrho_n\}$, the Berry curvature
decomposes as

$$
  \mathcal{F}
  = 
  \sum_i \mathcal{F}_i^{\mathrm{self}}
  + 
  \sum_{i < j}
  \mathcal{F}_{ij}^{\mathrm{mutual}},
$$

where $\mathcal{F}_i^{\mathrm{self}}$ depends on the geometry
of filament $\varrho_i$ alone (writhe contribution) and
$\mathcal{F}_{ij}^{\mathrm{mutual}}$ depends on the relative
position of filaments $\varrho_i$ and $\varrho_j$ (linking
contribution).

**Categorical interpretation.**
The [braid--fluid correspondence](#rem:braid-fluid) identifies
the fundamental group $\pi_1(\mathcal{M}_{j,K})$ with a quotient
of the braid group $B_n$.  A closed loop in moduli space —
an adiabatic exchange of two vortex filaments — accumulates
Berry phase

$$
  \Phi_{\mathrm{Berry}}(\sigma_i)
  = 
  \arg\bigl(\text{eigenvalue of } \rho_n(\sigma_i)\bigr),
$$

where $\rho_n(\sigma_i)$ is the
[braid-group representation](#prop:braid-action-tensor) acting on
$V^{\otimes n}$.  For the R-matrix of $\mathrm{SU}_q(2)$, the
two eigenvalues give Berry phases

$$
  \Phi_+  = \arg(q) = \frac{\pi}{\kappa}
  \quad(\text{symmetric channel}),
  \qquad
  \Phi_-  = \arg(-q^{-1}) = \pi - \frac{\pi}{\kappa}
  \quad(\text{antisymmetric channel}),
$$

where $q = e^{i\pi/\kappa}$ at a root of unity.  The difference
$\Phi_+ - \Phi_- = 2\pi/\kappa - \pi$ is the **statistical
angle** — the phase that distinguishes bosonic from fermionic
exchange.

**Connection to helicity.**
The total Berry phase accumulated by a vortex tangle $L$ around
a closed loop in moduli space equals the
[categorical helicity](#prop:helicity-conservation)
$\mathcal{H}_q$ of the tangle:

$$
  \Phi_{\mathrm{Berry}}[L]
  = 
  2\pi\mathcal{H}_q[L] \pmod{2\pi}.
$$

This identifies the helicity — a hydrodynamic invariant — with
a quantum-mechanical phase, completing the triangle:

$$
  \text{Knot topology (Jones polynomial)}
  \longleftrightarrow
  \text{Fluid helicity}
  \longleftrightarrow
  \text{Berry phase (statistics)}.
$$

**Anyonic statistics.**
For a general $q$ (not a root of unity), the Berry phase
$\Phi_{\mathrm{Berry}}(\sigma_i)$ is an irrational multiple of
$\pi$, and the vortex filaments are **anyons** — neither bosons
nor fermions.  At a root of unity $q = e^{i\pi/\kappa}$ with
$\kappa \in \mathbb{Z}$, the representations of $B_n$ factor
through the Iwahori--Hecke algebra $H_n(q)$ and the statistics become
rational.  The physical value $q \approx 1.110$ is not a root of
unity, but the deformation from $q = 1$ (bosonic) is small:
$\Phi_+ \approx 0.03\pi$, which is the origin of the spin-statistics
connection in the classical limit — particles are "nearly bosonic"
or "nearly fermionic" depending on which R-matrix eigenvalue
dominates, and the $q \to 1$ limit snaps the statistics to
$0$ or $\pi$.
