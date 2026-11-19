The [aether parameter](#def:substrate-parameter) $q$ imposes an algebraic discreteness on vortex circulation absent in classical Navier--Stokes. Four classical mechanisms exhibit discrete modes but continuous intensity; the $q$-deformation closes this gap.

**1. Kelvin waves on vortex filaments.**
A classical vortex filament supports standing-wave perturbations (Kelvin modes) at discrete wavelengths $\lambda_k = L/k$, for integers $k \geq 1$ and filament length $L$. The dispersion relation reads

$$
  \omega_k =  \frac{\Gamma}{4\pi a^2}k^2
  \bigl(\ln(L/a) - \text{const}\bigr),
$$

with vortex core radius $a$ and circulation $\Gamma$. These modes are discrete in wave number, yet the circulation $\Gamma$ remains a free continuous parameter. Under $q$-deformation, the filament inhabits the 1-jet bundle $J^1 \mathcal{S}_n$, and the $q$-Laplacian $\Delta_q$ replaces the classical Laplacian. Its eigenvalues correspond to the $q$-integers $[k]_q = (q^k - q^{-k})/(q - q^{-1})$, yielding a spectrum discrete in **both** wave number and intensity:

$$
  \omega_k^{(q)} = 
  \frac{\Gamma_q}{4\pi a_q^2}[k]_q^2
  \bigl(\ln_q(L/a_q) - c_q\bigr).
$$

As $q \to 1$, the $q$-integers collapse to classical integers, recovering the standard Kelvin spectrum.

**2. Superfluid vortex quantisation.**
In superfluid helium and Bose--Einstein condensates, the macroscopic wave function $\psi = |\psi|e^{i\varTheta}$ forces circulation to quantise as $\Gamma_n = n \cdot h/m$ for $n \in \mathbb{Z}$. This constitutes a topological constraint: the phase must remain single-valued around any closed loop. The QOU analogue is the holonomy of the $\mathrm{SU}(2)$ connection around a vortex filament. The [primordial vortex](#rem:primordial-vortex) carries topological charge because the representation theory of $\mathrm{SU}_q(2)$ quantises the $\mathrm{SU}(2)$ holonomy: the Casimir eigenvalue $[j]_q[j+1]_q$ with $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$ replaces the continuous $\Gamma$.

**3. Vortex breakdown states.**
In confined swirling flows (e.g., pipe flow), vortices transition between topologically distinct stable configurations — columnar, bubble breakdown, spiral breakdown — separated by finite energy barriers. These act as discrete **states** rather than modes. In the brane fluid, the [geodesic vortex](#rem:geodesic-vortices) fixed points of the $q$-deformed energy functional supply the analogous transitions: each fixed point forms a stable vortex configuration, and transitioning between them requires crossing an energy barrier set by $q$.

**4. Stability eigenvalues.**
Smooth classical vortex profiles like the Lamb--Oseen vortex possess discrete eigenvalues in their linear stability spectrum. Perturbations grow or decay at specific discrete rates. For the $q$-deformed vortex, the weight-space decomposition of the adjoint bundle governs these eigenvalues. The **longitudinal modes** (Cartan subalgebra) govern the stable, decaying eigenvalues, while the **ladder modes** ($E_\pm$) govern the unstable, entangling eigenvalues. This separation is an algebraic consequence of the $\mathrm{SU}_q(2)$ structure rather than an artefact of initial conditions.

The correspondence is summarised in the [table of classical and $q$-deformed fluid concepts](#tbl:vortex-intensity-modes-table-data).
