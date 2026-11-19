Fix an intensity level $j$ and a topological knot type $K$. The **moduli space** $\mathcal{M}_{j,K}$ classifies [geodesic vortex](#rem:geodesic-vortices) configurations of type $(j, K)$ modulo gauge equivalence:

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

where $\mathcal{G}$ denotes the gauge group. For the fundamental fermion ($j = \frac{1}{2}$, $K$ = trefoil), $\mathcal{M}_{1/2, T_{2,3}}$ forms a finite-dimensional manifold parametrised strictly by the position and orientation of the vortex filament.

**Berry connection.**
The $q$-Schrödinger equation evaluated near the vortex ground state constructs a line bundle $\mathcal{L} \to \mathcal{M}_{j,K}$. The fibre over a vortex configuration $\varrho$ corresponds to the ground-state eigenspace of the linearised Hamiltonian evaluated around $\varrho$. The **Berry connection** traversing this bundle reads

$$
  \mathcal{A}_{\mathrm{Berry}}
  = 
  i\langle v_\varrho, d\, v_\varrho\rangle_F,
$$

where $v_\varrho$ denotes the ground state at configuration $\varrho$ and $d$ acts as the exterior derivative on $\mathcal{M}_{j,K}$.

**Berry curvature.**
The curvature $\mathcal{F} = d\mathcal{A}_{\mathrm{Berry}}$ maps the local geometric phase per unit area across the moduli space. For a vortex configuration sustaining $n$ well-separated filaments $\{\varrho_1, \ldots, \varrho_n\}$, the Berry curvature splits as

$$
  \mathcal{F}
  = 
  \sum_i \mathcal{F}_i^{\mathrm{self}}
  + 
  \sum_{i < j}
  \mathcal{F}_{ij}^{\mathrm{mutual}}.
$$

Here $\mathcal{F}_i^{\mathrm{self}}$ derives strictly from the geometry of filament $\varrho_i$ (the writhe contribution), while $\mathcal{F}_{ij}^{\mathrm{mutual}}$ originates from the relative position of filaments $\varrho_i$ and $\varrho_j$ (the linking contribution).

**Categorical interpretation.**
The [braid--fluid correspondence](#rem:braid-fluid) maps the fundamental group $\pi_1(\mathcal{M}_{j,K})$ to a quotient of the braid group $B_n$. Traversing a closed loop in moduli space (enacting an adiabatic exchange of two vortex filaments) integrates the Berry phase

$$
  \Phi_{\mathrm{Berry}}(\sigma_i)
  = 
  \arg\bigl(\text{eigenvalue of } \rho_n(\sigma_i)\bigr),
$$

where $\rho_n(\sigma_i)$ represents the [braid-group representation](#prop:braid-action-tensor) acting on $V^{\otimes n}$. For the $\mathrm{SU}_q(2)$ R-matrix, the two eigenvalues yield the distinct Berry phases

$$
  \Phi_+  = \arg(q) = \frac{\pi}{\kappa}
  \quad(\text{symmetric channel}),
  \qquad
  \Phi_-  = \arg(-q^{-1}) = \pi - \frac{\pi}{\kappa}
  \quad(\text{antisymmetric channel}),
$$

assuming $q = e^{i\pi/\kappa}$ acts as a root of unity. The differential $\Phi_+ - \Phi_- = 2\pi/\kappa - \pi$ yields the **statistical angle**, the exact phase distinguishing bosonic from fermionic exchange.

**Connection to helicity.**
The total Berry phase accumulated by a vortex tangle $L$ executing a closed loop in moduli space equals the [categorical helicity](#prop:helicity-conservation) $\mathcal{H}_q$ of the tangle:

$$
  \Phi_{\mathrm{Berry}}[L]
  = 
  2\pi\mathcal{H}_q[L] \pmod{2\pi}.
$$

This equation maps helicity (a hydrodynamic invariant) directly to a quantum-mechanical phase, completing the structural triad:

$$
  \text{Knot topology (Jones polynomial)}
  \longleftrightarrow
  \text{Fluid helicity}
  \longleftrightarrow
  \text{Berry phase (statistics)}.
$$

**Anyonic statistics.**
For generic $q$ (not a root of unity), the Berry phase $\Phi_{\mathrm{Berry}}(\sigma_i)$ resolves to an irrational multiple of $\pi$. The vortex filaments behave as **anyons**, functioning as neither strict bosons nor strict fermions. At a root of unity $q = e^{i\pi/\kappa}$ with $\kappa \in \mathbb{Z}$, the representations of $B_n$ factor through the Iwahori--Hecke algebra $H_n(q)$ and the statistics lock to rational values. The physical anchor $q \approx 1.110$ remains distinct from a root of unity, but its offset from $q = 1$ (the bosonic pole) is small: $\Phi_+ \approx 0.03\pi$. This generates the spin-statistics connection observed near the classical limit: particles behave as "nearly bosonic" or "nearly fermionic" depending on which R-matrix eigenvalue dominates, and the $q \to 1$ collapse snaps the statistics definitively to $0$ or $\pi$.
