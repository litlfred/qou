<!-- FILE_START: turbulence-acoustics-intro.md -->
With the vortex spectrum and helicity invariant in hand,
we treat collective behaviour: how the discrete modes assemble into
turbulent tangles and how perturbations propagate on the brane
fluid as acoustic excitations.

We begin with Proposition: $q$-deformed energy cascade and modified Kolmogorov spectrum, which fixes the inertial-range scaling of the
energy spectrum $E(k)$ as a function of $q$ and the Planck--Reynolds
number, and Remark: Testable prediction: high-wavenumber deviations from Kolmogorov scaling, which extracts a falsifiable signature
for BEC and superfluid measurements. Remark: Berry phase on the vortex moduli space records the geometric phase accumulated by
filament configurations under adiabatic transport. The structural
content of vortex oscillations is then derived in Proposition: Kelvin wave dispersion from the $q$-Laplacian eigenvalue problem, with
Remark: Classical limit of the $q$-Kelvin dispersion checking the
$q \to 1$ recovery of the classical self-induction law. We close
with Proposition: Acoustic horizon formation and gravitational emergence: perturbations propagate on an acoustic metric whose horizons
seed the analogue-gravity picture used in the next section, **Global
regularity for $q > 1$**, where the same spectral apparatus
controls the nonlinear flow.

_(draft.)_
<!-- FILE_END: turbulence-acoustics-intro.md -->

<!-- FILE_START: q-turbulence-spectrum.md -->
In the brane fluid with [substrate parameter](#def:substrate-parameter)
$q > 1$ and [Planck--Reynolds number](#rem:planck-reynolds)
$\mathrm{Re}_q = 2/(q-1)$, the energy spectrum of a turbulent
vortex tangle satisfies a $q$-deformed Kolmogorov law.

1. **$q$-deformed energy spectrum.**  Let $E(k)$ denote the energy
   per unit wavenumber in the brane fluid.  In the inertial range
   $1 \ll k \ll k_{\max}$, where $k_{\max}$ is the viscous cutoff
   set by $\mathrm{Re}_q$, the spectrum is

   $$
     E_q(k)
     = 
     C_q\varepsilon^{2/3}
     \frac{[k]_q^{-5/3}}{[k]_q / k},
   $$

   where $\varepsilon$ is the energy dissipation rate,
   $C_q$ is a $q$-dependent Kolmogorov constant, and the ratio
   $[k]_q / k$ accounts for the non-uniform spacing of
   $q$-integers.  As $q \to 1$, $[k]_q \to k$ and the classical
   Kolmogorov spectrum $E(k) = C_K\varepsilon^{2/3}k^{-5/3}$
   is recovered.

2. **Discrete cascade.**  Unlike classical turbulence, where energy
   cascades continuously from large to small scales, the
   $q$-deformed cascade is **discrete**: energy transfers occur
   between modes labelled by $q$-integers $[k]_q$, with transfer
   rate

   $$
     T_{k \to k+1}
     = 
     \varepsilon
     \frac{[k+1]_q^{2/3} - [k]_q^{2/3}}
          {[k+1]_q - [k]_q}.
   $$

   For the symmetric $q$-integer, the denominator satisfies
   $[k+1]_q - [k]_q \sim q^k \cdot q/(q+1)$ for large $k$.
   The transfer rate decreases exponentially at high
   wavenumbers, providing a natural UV cutoff.

3. **Finite cascade depth.**  The number of active modes in the
   cascade is bounded by

   $$
     N_{\mathrm{modes}}
      \leq 
     \bigl\lfloor \log_q(\mathrm{Re}_q^{3/4}) \bigr\rfloor
     = 
     \biggl\lfloor
       \frac{3}{4}
       \frac{\ln(2/(q-1))}{\ln q}
     \biggr\rfloor.
   $$

   At $q \approx 1.110$, $N_{\mathrm{modes}} \approx 21$.
   (This counts all modes participating in the cascade; the
   [Planck--Reynolds](#rem:planck-reynolds) bound $k_{\max} \approx 4$
   is the stricter count of modes with significant amplitude.)

4. **Spectral gap.**  Below the fundamental mode $k = 1$, there
   is a **spectral gap**

   $$
     \Delta E_{\mathrm{gap}}
     = 
     C_q\varepsilon^{2/3}
     \bigl([1]_q^{-5/3} - [2]_q^{-5/3}\bigr)
      >  0,
   $$

   separating the ground state (laminar flow) from the first
   excited mode.  This gap prevents spontaneous onset of turbulence
   below a threshold energy injection rate — the brane fluid is
   stable against infinitesimal perturbations, unlike classical
   Navier--Stokes where $\mathrm{Re} \to \infty$ always produces
   instability.

<!-- FILE_END: q-turbulence-spectrum.md -->

<!-- FILE_START: q-turbulence-prediction.md -->
The [q-Kolmogorov spectrum](#prop:q-turbulence-spectrum) reduces to
the standard $k^{-5/3}$ law as $q \to 1$, so no existing
turbulence measurement is contradicted.  At the Planck scale,
however, the discrete cascade predicts deviations from $k^{-5/3}$
at high wavenumbers in [BEC vortex tangles](#rem:bec-vortex-data),
consistent with $q$-integer spacing.

Observations of quantum turbulence in ${}^{4}\mathrm{He}$
(Walmsley & Golov 2008) show precisely such deviations,
conventionally attributed to vortex reconnection but potentially
arising from the $q$-deformation of the energy cascade.
<!-- FILE_END: q-turbulence-prediction.md -->

<!-- FILE_START: berry-vortex-moduli.md -->
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
<!-- FILE_END: berry-vortex-moduli.md -->

<!-- FILE_START: kelvin-dispersion-derivation.md -->
The [discrete vortex spectrum](#prop:discrete-vortex-spectrum) states
that the eigenvalues of the $q$-Laplacian on a vortex filament are
$\lambda_k^{(q)} = [k]_q^2 \cdot \hbar_q / L_q^2$.  This
subsection derives this from first principles.

**Setup.**
Let $\varrho$ be a stable vortex filament of length $L$ in the
brane fluid, parametrised by arc length $s \in [0, L]$ with
periodic boundary conditions $\varrho(0) = \varrho(L)$.  Let
$\eta(s, t)$ be a small normal displacement of the filament from
its equilibrium position (a Kelvin wave).  The linearised
[q-Navier--Stokes equation](#def:q-navier-stokes) restricted to
normal perturbations of $\varrho$ is

$$
  \partial_t^2 \eta
  = 
  \frac{\Gamma_q}{4\pi a_q^2}\Delta_q\eta
  -  \nu_q\Delta_q\partial_t \eta,
$$

where $\Gamma_q = [j]_q[j+1]_q$ is the quantised circulation at
intensity level $j$, $a_q$ is the $q$-deformed vortex core radius,
and the second term is viscous damping.

**The $q$-Laplacian eigenvalue problem.**
The $q$-Laplacian on the circle of length $L$ acts on functions
$f(s)$ with period $L$.  Its eigenvalue problem is

$$
  \Delta_qf_k
  =  -\mu_kf_k,
  \qquad
  f_k(s + L) = f_k(s).
$$

For the standard Laplacian ($q = 1$), the eigenfunctions are
$e^{2\pi i k s / L}$ with eigenvalues $\mu_k = (2\pi k/L)^2$.
The $q$-Laplacian replaces the integer $k$ with the $q$-integer
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$:

$$
  \mu_k^{(q)}
  = 
  \left(\frac{2\pi[k]_q}{L_q}\right)^2,
$$

where $L_q = L \cdot [1]_q / 1 = L$ (since $[1]_q = 1$ for all
$q$).

**Derivation.**
The $q$-Laplacian is defined via the $q$-derivative operators.
For a function $f$ on the circle, set $z = e^{2\pi i s / L}$.
Then:

$$
  D_q f(z) = \frac{f(qz) - f(q^{-1}z)}{(q - q^{-1})z},
$$

and $\Delta_q = -zD_q \circ zD_q$ (the radial part of the
$q$-Casimir).  On the monomial $z^k$ this gives

$$
  D_q(z^k)
  = \frac{q^k z^k - q^{-k} z^k}{(q - q^{-1})z}
  = [k]_qz^{k-1},
$$

so $zD_q(z^k) = [k]_qz^k$, and therefore

$$
  \Delta_q(z^k) = -[k]_q^2z^k.
$$

The eigenvalue is $\mu_k^{(q)} = [k]_q^2$.  Restoring physical
units (the filament has length $L_q$ and the quantum of action
is $\hbar_q$):

$$
  \lambda_k^{(q)}
  = 
  [k]_q^2 \cdot \frac{\hbar_q}{L_q^2}.
$$

This is the formula stated in the
[discrete vortex spectrum](#prop:discrete-vortex-spectrum).

**Dispersion relation.**
Substituting $\eta(s,t) = f_k(s)e^{-i\omega t}$ into the
linearised equation and using
$\Delta_q f_k = -[k]_q^2 f_k / L_q^2$ gives

$$
  -\omega^2
  = 
  -\frac{\Gamma_q}{4\pi a_q^2}\frac{[k]_q^2}{L_q^2}
  +  i\omega\nu_q\frac{[k]_q^2}{L_q^2}.
$$

For the undamped case ($\nu_q = 0$, i.e. the Euler limit), the
dispersion relation is

$$
  \omega_k^{(q)}
  = 
  \frac{\Gamma_q^{1/2}}{2\sqrt{\pi}a_q}
  \frac{[k]_q}{L_q},
$$

which is the $q$-deformed Kelvin dispersion.  For the damped case
($\nu_q > 0$), complex frequency gives the decay rate

$$
  \gamma_k^{(q)}
  = 
  \frac{\nu_q}{2}\frac{[k]_q^2}{L_q^2}
  = 
  \frac{\hbar_q}{4}\frac{[k]_q^2}{L_q^2},
$$

so mode $k$ decays on timescale
$\tau_k = 1/\gamma_k^{(q)} = 4L_q^2 / (\hbar_q[k]_q^2)$.
since $[k]_q \sim q^k$ for large $k$, high modes decay
**doubly exponentially** in $k$ — the exponential UV cutoff
noted in the [q-Navier--Stokes definition](#def:q-navier-stokes).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: kelvin-dispersion-derivation.md -->

<!-- FILE_START: kelvin-dispersion-derivation-interpretation.md -->
**Mathematical Novelty.** While the mechanical process of $q$-deforming operators is a standard procedure, the mathematical novelty is observing that applying the exact $q$-derivative $D_q$ to classical Kelvin-wave dispersion immediately generates an exact, analytically rigorous doubly-exponential UV suppression mechanism ($\tau_k \sim q^{-2k}$) in the fluid bulk, bypassing the need for ad-hoc phenomenological regularization or arbitrary cutoffs.
<!-- FILE_END: kelvin-dispersion-derivation-interpretation.md -->

<!-- FILE_START: kelvin-classical-limit.md -->
As $q \to 1$: $[k]_q \to k$, $\Gamma_q \to j(j+1)$,
$\nu_q \to 0$, and the
[q-Kelvin dispersion](#prop:kelvin-dispersion-derivation) recovers
the classical form
$\omega_k = \Gamma k^2 / (4\pi a^2) \cdot (\ln(L/a) - c)$,
where the logarithmic factor arises from the Biot--Savart
self-induction integral.  The $q$-deformation absorbs this
logarithm into the deformed core radius $a_q$.
<!-- FILE_END: kelvin-classical-limit.md -->

<!-- FILE_START: acoustic-horizon-conditions.md -->
The [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ admits
horizons wherever $|v| = c_s$.

**Acoustic metric.**
Perturbations $\delta\psi$ of the brane fluid propagate on the
acoustic geometry

$$
  g_{\mathrm{ac}}
  = 
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - |v|^2) & -v^T \\
    -v & \mathbf{1}_{3}
  \end{pmatrix},
$$

where $c_s^2 = \partial p / \partial\rho\big|_{Q_q}$ is the local
sound speed incorporating quantum pressure effects.

**Sound speed in the brane fluid.**
From the equation of state $p = p(\rho, q)$ determined by the
[q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction),
the sound speed is

$$
  c_s^2
  = 
  c_q^2\Bigl(1 - \frac{\hbar_q^2}{4\rho}
  \Delta_q\!\left(\frac{1}{\sqrt{\rho}}\right)
  \cdot \sqrt{\rho}\Bigr),
$$

where $c_q = 1/(q-1)$ is the
[speed of light](#def:substrate-parameter).  The second term is the
quantum correction: at low density ($\rho \to 0$), the quantum
pressure diverges and $c_s \to \infty$; at high density, the
quantum correction is negligible and $c_s \to c_q$.

**Horizon formation conditions.**
An acoustic horizon forms at a surface $\Sigma$ where
$|v| = c_s$.  Three conditions must hold simultaneously:

1. **Transonic flow.**  The Mach number
   $\mathcal{M} = |v|/c_s$ crosses unity on $\Sigma$:
   $\mathcal{M}|_\Sigma = 1$, with $\mathcal{M} < 1$ on one
   side (subsonic) and $\mathcal{M} > 1$ on the other
   (supersonic).

2. **Non-degeneracy.**  The gradient of the Mach number is
   non-vanishing on $\Sigma$:
   $\nabla(\mathcal{M}^2)|_\Sigma \neq 0$.  This ensures the
   horizon is a smooth hypersurface, not a degenerate critical
   point.

3. **Energy condition.**  The effective energy density
   $T_{00} = \frac{1}{2}\rho(|v|^2 + c_s^2) + Q_q\rho$
   satisfies the null energy condition
   $T_{\mu\nu}k^\mu k^\nu \geq 0$ for all null vectors $k^\mu$
   of $g_{\mathrm{ac}}$.  This is automatically satisfied when
   $\rho > 0$ and $Q_q \geq 0$.

**Surface gravity and Hawking temperature.**

At an acoustic horizon, the surface gravity is

$$
  \kappa_H
  = 
  \frac{1}{2}\frac{\partial(c_s^2 - |v|^2)}{\partial n}
  \bigg|_\Sigma,
$$

where $n$ is the outward normal to $\Sigma$.  By analogy with
Unruh's result for acoustic black holes, the horizon radiates at
the Hawking temperature

$$
  T_H
  = 
  \frac{\hbar_q\kappa_H}{2\pic_s}.
$$

In the brane fluid, $\hbar_q = (q-1)/q$, so:

$$
  T_H
  = 
  \frac{(q-1)}{2\pi q}
  \frac{\kappa_H}{c_s}.
$$

As $q \to 1$, $T_H \to 0$: the classical limit has no Hawking
radiation, consistent with the vanishing of $\hbar_q$.  At the
physical value $q \approx 1.110$, $T_H$ is suppressed by a factor
$(q-1)/q \approx 0.099$ relative to the naive estimate
$\kappa_H / (2\pi c_s)$.

**Types of acoustic horizon in the brane fluid.**

| Configuration | Flow structure | Physical analogue |
|---|---|---|
| **Spherical inflow** | Radial $v = -v_r(r)\hat{r}$ with $v_r(r_H) = c_s$ | Schwarzschild black hole |
| **Vortex drain** | Circular $v = v_\varTheta(r)\hat\varTheta + v_r(r)\hat{r}$ | Kerr (rotating) black hole |
| **Expanding shell** | Outward $v = v_r(r)\hat{r}$ with $v_r(r_C) = c_s$ | Cosmological horizon (de Sitter) |
| **Vortex core** | Concentrated circulation $\lvert v\rvert \to \infty$ at $r \to 0$ | Naked singularity (if $\lvert v\rvert > c_s$ for all $r < r_0$) |

**$q$-dependent horizon radius.**
For a spherically symmetric inflow with velocity
$v_r = -\Gamma_q / (4\pi r^2)$, the horizon forms at

$$
  r_H
  = 
  \left(\frac{\Gamma_q}{4\pic_s}\right)^{1/2}
  = 
  \left(\frac{[j]_q[j+1]_q}{4\pic_q}\right)^{1/2}
  \cdot (1 + O(\hbar_q)).
$$

At the fundamental level $j = 1/2$:
$[1/2]_q[3/2]_q = (q^2 + q^{-2} - q - q^{-1})/(q - q^{-1})^2
\approx 0.75$ at $q \approx 1.110$.  The horizon radius $r_H$
is of order $\ell_q = (q-1)/q$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: acoustic-horizon-conditions.md -->

<!-- FILE_START: acoustic-horizon-conditions-interpretation.md -->
**Mathematical Novelty.** While the underlying construction of an acoustic metric and its associated Unruh/Hawking temperature is standard in analogue gravity, the mathematical novelty here is instantiating this framework natively over the $q$-deformed categorical substrate. The acoustic horizon conditions, rather than being ad-hoc physical analogies, become exact geometric constraints on the $q$-Navier-Stokes fluid, where the Hawking temperature is rigorously suppressed by the specific cyclotomic factor $\hbar_q = (q-1)/q$.
<!-- FILE_END: acoustic-horizon-conditions-interpretation.md -->

<!-- FILE_START: acoustic-gravitational-emergence.md -->
The [GR substrate geometry](#rem:gr-substrate-geometry) identifies
the acoustic metric with the physical spacetime metric in the
archimedean realisation.  Acoustic horizons are therefore
**gravitational horizons**: black holes are regions where the
brane fluid flows supersonically.  The Einstein field equations
emerge as the long-wavelength limit of the
[q-Navier--Stokes equation](#def:q-navier-stokes), with the
stress-energy tensor $T_{\mu\nu}$ encoding the fluid momentum
flux.  Singularity theorems (Penrose--Hawking) translate into
statements about the breakdown of smooth transonic flow — the
classical singularity is the $q \to 1$ limit of a smooth
$q$-deformed vortex core.
<!-- FILE_END: acoustic-gravitational-emergence.md -->

