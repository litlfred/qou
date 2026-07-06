We fix an intensity level $j$ and a knot type $K$. The **moduli space** $\mathcal{M}_{j,K}$ classifies [geodesic vortex](#rem:geodesic-vortices) configurations of type $(j, K)$ modulo gauge equivalence:

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
  \big/ \mathcal{G}.
$$

The group $\mathcal{G}$ denotes gauge transformations. For the fundamental fermion ($j = \frac{1}{2}$, $K$ = trefoil), $\mathcal{M}_{1/2, T_{2,3}}$ forms a finite-dimensional manifold parametrised by the position and orientation of the vortex filament.

**Berry connection.**
We restrict the $q$-Schrödinger equation to states near the vortex ground state. This defines a line bundle $\mathcal{L} \to \mathcal{M}_{j,K}$. The fibre at a configuration $\varrho$ is the ground-state eigenspace of the linearised Hamiltonian. The **Berry connection** on this bundle is

$$
  \mathcal{A}_{\mathrm{Berry}}
  = 
  i\langle\psi_\varrho|d|\psi_\varrho\rangle.
$$

The state $|\psi_\varrho\rangle$ denotes the ground state at $\varrho$. The operator $d$ is the exterior derivative on $\mathcal{M}_{j,K}$.

**Berry curvature.**
The curvature $\mathcal{F} = d\mathcal{A}_{\mathrm{Berry}}$ measures the local geometric phase per unit area in moduli space. For a configuration with $n$ separated filaments $\{\varrho_1, \ldots, \varrho_n\}$, the Berry curvature decomposes as

$$
  \mathcal{F}
  = 
  \sum_i \mathcal{F}_i^{\mathrm{self}}
  + 
  \sum_{i < j}
  \mathcal{F}_{ij}^{\mathrm{mutual}}.
$$

The self-curvature $\mathcal{F}_i^{\mathrm{self}}$ tracks the writhe of filament $\varrho_i$. The mutual curvature $\mathcal{F}_{ij}^{\mathrm{mutual}}$ tracks the linking between filaments $\varrho_i$ and $\varrho_j$.

**Categorical interpretation.**
The [braid--fluid correspondence](#rem:braid-fluid) identifies the fundamental group $\pi_1(\mathcal{M}_{j,K})$ with a quotient of the braid group $B_n$. An adiabatic exchange of two vortex filaments — a closed loop in moduli space — accumulates a Berry phase

$$
  \Phi_{\mathrm{Berry}}(\sigma_i)
  = 
  \arg\bigl(\text{eigenvalue of } \rho_n(\sigma_i)\bigr).
$$

The map $\rho_n(\sigma_i)$ is the [braid-group representation](#prop:braid-action-tensor) on $V^{\otimes n}$. For the $\mathrm{SU}_q(2)$ R-matrix, the two eigenvalues yield the Berry phases

$$
  \Phi_+  = \arg(q) = \frac{\pi}{\kappa}
  \quad(\text{symmetric channel}),
  \qquad
  \Phi_-  = \arg(-q^{-1}) = \pi - \frac{\pi}{\kappa}
  \quad(\text{antisymmetric channel}).
$$

We define $q = e^{i\pi/\kappa}$ at a root of unity. The difference $\Phi_+ - \Phi_- = 2\pi/\kappa - \pi$ provides the **statistical angle**. This phase distinguishes bosonic from fermionic exchange.

**Connection to helicity.**
The total Berry phase accumulated by a vortex tangle $L$ around a closed loop in moduli space equals the [categorical helicity](#prop:helicity-conservation) $\mathcal{H}_q$ of the tangle:

$$
  \Phi_{\mathrm{Berry}}[L]
  = 
  2\pi\mathcal{H}_q[L] \pmod{2\pi}.
$$

We identify a hydrodynamic invariant (helicity) with a quantum-mechanical phase (statistics). This completes the triad:

$$
  \text{Knot topology (Jones polynomial)}
  \longleftrightarrow
  \text{Fluid helicity}
  \longleftrightarrow
  \text{Berry phase (statistics)}.
$$

**Anyonic statistics.**
For generic $q$ (not a root of unity), the Berry phase $\Phi_{\mathrm{Berry}}(\sigma_i)$ is an irrational multiple of $\pi$. The vortex filaments behave as **anyons**. At a root of unity $q = e^{i\pi/\kappa}$ for $\kappa \in \mathbb{Z}$, the $B_n$ representations factor through the Iwahori--Hecke algebra $H_n(q)$ and statistics become rational. At the physical value $q \approx 1.110$, we are not at a root of unity, but the deformation from $q = 1$ remains small. We find $\Phi_+ \approx 0.03\pi$. This shift drives the classical spin-statistics connection: particles are "nearly bosonic" or "nearly fermionic" depending on the dominant R-matrix eigenvalue. The limit $q \to 1$ snaps the statistics precisely to $0$ or $\pi$.
