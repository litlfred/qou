The [substrate parameter](#def:substrate-parameter) $q$ imposes
algebraic discreteness on vortex circulation that classical
Navier--Stokes cannot provide.  Four classical mechanisms exhibit
discrete modes but continuous intensity; the $q$-deformation
closes this gap.

**1. Kelvin waves on vortex filaments.**
A classical vortex filament supports standing-wave perturbations
(Kelvin modes) with discrete wavelengths $\lambda_k = L/k$,
$k = 1, 2, 3, \ldots$, where $L$ is the filament length.  The
dispersion relation is

$$
  \omega_k =  \frac{\Gamma}{4\pi a^2}k^2
  \bigl(\ln(L/a) - \text{const}\bigr),
$$

with vortex core radius $a$ and circulation $\Gamma$.  These
modes are discrete in wave number but the circulation $\Gamma$
itself is a free continuous parameter.  In the $q$-deformed
setting the filament lives in the 1-jet bundle $J^1 \mathcal{S}_n$,
and the $q$-Laplacian $\Delta_q$ replaces the classical
Laplacian.  Its eigenvalues are the $q$-integers
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$, producing a spectrum
that is discrete in **both** wave number and intensity:

$$
  \omega_k^{(q)} = 
  \frac{\Gamma_q}{4\pi a_q^2}[k]_q^2
  \bigl(\ln_q(L/a_q) - c_q\bigr).
$$

As $q \to 1$ the $q$-integers collapse to ordinary integers and
the classical Kelvin spectrum is recovered.

**2. Superfluid vortex quantisation.**
In superfluid helium and Bose--Einstein condensates, the
macroscopic wave function $\psi = |\psi|e^{i\varTheta}$
forces circulation to be quantised:
$\Gamma_n = n \cdot h/m$, $n \in \mathbb{Z}$.  This is a
topological constraint — the phase must be single-valued around
any closed loop.  The QOU analogue is the holonomy of the
$\mathrm{SU}(2)$ connection around a vortex filament.  The
[primordial vortex](#rem:primordial-vortex) carries topological
charge because the $\mathrm{SU}(2)$ holonomy is quantised by
the representation theory of $\mathrm{SU}_q(2)$: the
Casimir eigenvalue $[j]_q[j+1]_q$ with $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$
replaces the continuous $\Gamma$.

**3. Vortex breakdown states.**
In confined swirling flows (pipe flow, combustion chambers),
vortices transition between topologically distinct stable
configurations — columnar, bubble breakdown, spiral breakdown —
separated by finite energy barriers.  These are discrete
**states**, not modes.  In the brane fluid, the analogous
transitions are the [geodesic vortex](#rem:geodesic-vortices)
fixed points of the $q$-deformed energy functional: each fixed
point is a stable vortex configuration, and passage between
them requires crossing a barrier set by $q$.

**4. Stability eigenvalues.**
The Lamb--Oseen vortex and other smooth classical vortex
profiles have discrete eigenvalues in their linear stability
spectrum.  Perturbations grow or decay at specific discrete
rates.  For the $q$-deformed vortex, these eigenvalues are
governed by the weight-space decomposition of the adjoint
bundle: the **longitudinal modes** (Cartan subalgebra) give
the stable eigenvalues (laminar, decaying), while the
**ladder modes** ($E_\pm$) give the unstable eigenvalues
(entangling, growing).  The separation between these two
families is not a coincidence of initial conditions but an
algebraic consequence of the $\mathrm{SU}_q(2)$ structure.

The following table summarises the correspondence:

| Classical fluid concept | QOU $q$-deformed analogue | Discreteness source |
|---|---|---|
| Kelvin wave number $k$ | $q$-Laplacian eigenvalue $[k]_q$ | $q$-integer spectrum |
| Circulation $\Gamma$ (continuous) | Casimir $[j]_q[j+1]_q$ (discrete) | $\mathrm{SU}_q(2)$ representation theory |
| Breakdown states (topological) | Geodesic vortex fixed points | $q$-energy functional critical set |
| Stability eigenvalues | Weight-space longitudinal/ladder split | Adjoint bundle decomposition |
| Superfluid $\Gamma_n = nh/m$ | Holonomy quantisation by $j$ | Topological charge of $\mathrm{SU}(2)$ |
| Reynolds number $\mathrm{Re}$ | [Planck--Reynolds](#rem:planck-reynolds) $\mathrm{Re}_q$ | $q$-deformation parameter |

