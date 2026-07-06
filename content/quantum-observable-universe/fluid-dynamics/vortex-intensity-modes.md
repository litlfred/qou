The [substrate parameter](#def:substrate-parameter) $q$ imposes algebraic discreteness on vortex circulation that the classical Navier--Stokes equations cannot provide. Four classical mechanisms exhibit discrete modes but continuous intensity. The $q$-deformation closes this gap.

**1. Kelvin waves on vortex filaments.**
A classical vortex filament supports standing-wave perturbations (Kelvin modes) with discrete wavelengths $\lambda_k = L/k$ for $k = 1, 2, 3, \ldots$, where $L$ denotes the filament length. The dispersion relation is:

$$
  \omega_k =  \frac{\Gamma}{4\pi a^2}k^2
  \bigl(\ln(L/a) - \text{const}\bigr),
$$

with vortex core radius $a$ and circulation $\Gamma$. These modes are discrete in wave number, but the circulation $\Gamma$ remains a free continuous parameter. In the $q$-deformed setting, the filament lives in the 1-jet bundle $J^1 \mathcal{S}_n$. The $q$-Laplacian $\Delta_q$ replaces the classical Laplacian. Its eigenvalues are the $q$-integers $[k]_q = (q^k - q^{-k})/(q - q^{-1})$. This produces a spectrum discrete in both wave number and intensity:

$$
  \omega_k^{(q)} = 
  \frac{\Gamma_q}{4\pi a_q^2}[k]_q^2
  \bigl(\ln_q(L/a_q) - c_q\bigr).
$$

As $q \to 1$, the $q$-integers collapse to ordinary integers, recovering the classical Kelvin spectrum.

**2. Superfluid vortex quantisation.**
In superfluid helium and Bose--Einstein condensates, the macroscopic wave function $\psi = |\psi|e^{i\varTheta}$ forces circulation to be quantised: $\Gamma_n = n \cdot h/m$ for $n \in \mathbb{Z}$. This constitutes a topological constraint: the phase must be single-valued around any closed loop. The QOU analogue provides the holonomy of the $\mathrm{SU}(2)$ connection around a vortex filament. The [primordial vortex](#rem:primordial-vortex) carries topological charge because the representation theory of $\mathrm{SU}_q(2)$ quantises the $\mathrm{SU}(2)$ holonomy. The Casimir eigenvalue $[j]_q[j+1]_q$ with $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$ replaces the continuous $\Gamma$.

**3. Vortex breakdown states.**
In confined swirling flows (pipe flow, combustion chambers), vortices transition between topologically distinct stable configurations (columnar, bubble breakdown, spiral breakdown) separated by finite energy barriers. These represent discrete states, not modes. In the brane fluid, the analogous transitions manifest as the [geodesic vortex](#rem:geodesic-vortices) fixed points of the $q$-deformed energy functional. Each fixed point constitutes a stable vortex configuration. Passage between them requires crossing a barrier set by $q$.

**4. Stability eigenvalues.**
The Lamb--Oseen vortex and other smooth classical vortex profiles possess discrete eigenvalues in their linear stability spectrum. Perturbations grow or decay at specific discrete rates. For the $q$-deformed vortex, the weight-space decomposition of the adjoint bundle governs these eigenvalues. The longitudinal modes (Cartan subalgebra) determine the stable eigenvalues (laminar, decaying). The ladder modes ($E_\pm$) determine the unstable eigenvalues (entangling, growing). The separation between these two families forms an algebraic consequence of the $\mathrm{SU}_q(2)$ structure, not a coincidence of initial conditions.

The correspondence appears in [Table: Classical fluid concepts and their $q$-deformed analogues](#tbl:vortex-intensity-modes-table-data).
