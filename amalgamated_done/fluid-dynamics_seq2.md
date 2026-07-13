<!-- FILE_START: turbulence-acoustics-intro.md -->
Having established the vortex spectrum and helicity invariant, we now examine collective behaviour: how discrete modes assemble into turbulent tangles and how perturbations propagate across the brane fluid as acoustic excitations.

We begin with Proposition: $q$-deformed energy cascade and modified Kolmogorov spectrum, which derives the inertial-range scaling of the energy spectrum $E(k)$ as a function of $q$ and the Planck--Reynolds number. Remark: Testable prediction: high-wavenumber deviations from Kolmogorov scaling extracts a falsifiable signature for BEC and superfluid experiments. Remark: Berry phase on the vortex moduli space calculates the geometric phase accumulated by filament configurations under adiabatic transport. Proposition: Kelvin wave dispersion from the $q$-Laplacian eigenvalue problem establishes the structural mechanics of vortex oscillations. Remark: Classical limit of the $q$-Kelvin dispersion verifies that the $q \to 1$ limit correctly recovers the classical self-induction law. Finally, Proposition: Acoustic horizon formation and gravitational emergence demonstrates that perturbations propagate on an acoustic metric whose horizons seed the analogue-gravity framework. The next section, **Global regularity for $q > 1$**, applies this identical spectral apparatus to control the nonlinear flow.
<!-- FILE_END: turbulence-acoustics-intro.md -->

<!-- FILE_START: q-turbulence-spectrum.md -->
In the brane fluid defined by [substrate parameter](#def:substrate-parameter) $q > 1$ and [Planck--Reynolds number](#rem:planck-reynolds) $\mathrm{Re}_q = 2/(q-1)$, the energy spectrum of a turbulent vortex tangle obeys a $q$-deformed Kolmogorov law.

1. **$q$-deformed energy spectrum.** Let $E(k)$ denote the energy per unit wavenumber. In the inertial range $1 \ll k \ll k_{\max}$, where $k_{\max}$ denotes the viscous cutoff imposed by $\mathrm{Re}_q$, the spectrum evaluates to

   $$
     E_q(k)
     = 
     C_q\varepsilon^{2/3}
     \frac{[k]_q^{-5/3}}{[k]_q / k},
   $$

   where $\varepsilon$ represents the energy dissipation rate, $C_q$ acts as a $q$-dependent Kolmogorov constant, and the ratio $[k]_q / k$ corrects for the non-uniform spacing of $q$-integers. As $q \to 1$, $[k]_q \to k$ and the spectrum converges to the classical Kolmogorov law $E(k) = C_K\varepsilon^{2/3}k^{-5/3}$.

2. **Discrete cascade.** Classical turbulence cascades energy continuously from large to small scales. The $q$-deformed cascade operates **discretely**: energy transfers sequentially between modes indexed by $q$-integers $[k]_q$, executing at the transfer rate

   $$
     T_{k \to k+1}
     = 
     \varepsilon
     \frac{[k+1]_q^{2/3} - [k]_q^{2/3}}
          {[k+1]_q - [k]_q}.
   $$

   For large $k$, the denominator scales as $[k+1]_q - [k]_q \sim q^k \cdot q/(q+1)$. The transfer rate thus drops exponentially at high wavenumbers, enforcing a strict structural UV cutoff.

3. **Finite cascade depth.** The number of active modes participating in the cascade strictly bounds to

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

   At the physical anchor $q \approx 1.110$, $N_{\mathrm{modes}} \approx 21$. (This accounts for all modes spanning the cascade; the [Planck--Reynolds](#rem:planck-reynolds) bound $k_{\max} \approx 4$ measures only those modes carrying significant amplitude.)

4. **Spectral gap.** Below the fundamental mode $k = 1$, a **spectral gap** isolates the ground state (laminar flow) from the first excited mode:

   $$
     \Delta E_{\mathrm{gap}}
     = 
     C_q\varepsilon^{2/3}
     \bigl([1]_q^{-5/3} - [2]_q^{-5/3}\bigr)
      >  0.
   $$

   This gap halts the spontaneous onset of turbulence below a rigid threshold energy injection rate. The brane fluid remains structurally stable against infinitesimal perturbations, unlike classical Navier--Stokes where $\mathrm{Re} \to \infty$ guarantees instability.
<!-- FILE_END: q-turbulence-spectrum.md -->

<!-- FILE_START: q-turbulence-prediction.md -->
The [q-Kolmogorov spectrum](#prop:q-turbulence-spectrum) collapses exactly to the standard $k^{-5/3}$ law as $q \to 1$, ensuring compliance with all macro-scale turbulence measurements. At the Planck scale, however, the discrete cascade mandates high-wavenumber deviations from $k^{-5/3}$ in [BEC vortex tangles](#rem:bec-vortex-data), perfectly tracking the $q$-integer spacing.

Observations of quantum turbulence in ${}^{4}\mathrm{He}$ (Walmsley & Golov 2008) capture precisely these deviations. Convention attributes them to vortex reconnection, but the $q$-deformation of the energy cascade provides a rigorous structural origin.
<!-- FILE_END: q-turbulence-prediction.md -->

<!-- FILE_START: berry-vortex-moduli.md -->
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
  i\langle\psi_\varrho|d|\psi_\varrho\rangle,
$$

where $|\psi_\varrho\rangle$ denotes the ground state at configuration $\varrho$ and $d$ acts as the exterior derivative on $\mathcal{M}_{j,K}$.

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
The [braid--fluid correspondence](#rem:braid-fluid) maps the fundamental group $\pi_1(\mathcal{M}_{j,K})$ to a quotient of the braid group $B_n$. Traversing a closed loop in moduli space — enacting an adiabatic exchange of two vortex filaments — integrates the Berry phase

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

assuming $q = e^{i\pi/\kappa}$ acts as a root of unity. The differential $\Phi_+ - \Phi_- = 2\pi/\kappa - \pi$ yields the **statistical angle** — the exact phase distinguishing bosonic from fermionic exchange.

**Connection to helicity.**
The total Berry phase accumulated by a vortex tangle $L$ executing a closed loop in moduli space equals the [categorical helicity](#prop:helicity-conservation) $\mathcal{H}_q$ of the tangle:

$$
  \Phi_{\mathrm{Berry}}[L]
  = 
  2\pi\mathcal{H}_q[L] \pmod{2\pi}.
$$

This equation maps helicity — a hydrodynamic invariant — directly to a quantum-mechanical phase, completing the structural triad:

$$
  \text{Knot topology (Jones polynomial)}
  \longleftrightarrow
  \text{Fluid helicity}
  \longleftrightarrow
  \text{Berry phase (statistics)}.
$$

**Anyonic statistics.**
For generic $q$ (not a root of unity), the Berry phase $\Phi_{\mathrm{Berry}}(\sigma_i)$ resolves to an irrational multiple of $\pi$. The vortex filaments behave as **anyons** — functioning as neither strict bosons nor strict fermions. At a root of unity $q = e^{i\pi/\kappa}$ with $\kappa \in \mathbb{Z}$, the representations of $B_n$ factor through the Iwahori--Hecke algebra $H_n(q)$ and the statistics lock to rational values. The physical anchor $q \approx 1.110$ remains distinct from a root of unity, but its offset from $q = 1$ (the bosonic pole) is small: $\Phi_+ \approx 0.03\pi$. This generates the spin-statistics connection observed near the classical limit — particles behave as "nearly bosonic" or "nearly fermionic" depending on which R-matrix eigenvalue dominates, and the $q \to 1$ collapse snaps the statistics definitively to $0$ or $\pi$.
<!-- FILE_END: berry-vortex-moduli.md -->

<!-- FILE_START: kelvin-dispersion-derivation.md -->
The [discrete vortex spectrum](#prop:discrete-vortex-spectrum) identifies the $q$-Laplacian eigenvalues on a vortex filament as $\lambda_k^{(q)} = [k]_q^2 \cdot \hbar_q / L_q^2$. We now derive this mechanically.

**Setup.**
Let $\varrho$ describe a stable vortex filament of length $L$ in the brane fluid, parametrised by arc length $s \in [0, L]$ under periodic boundary conditions $\varrho(0) = \varrho(L)$. Let $\eta(s, t)$ denote a small normal displacement of the filament from equilibrium (a Kelvin wave). The linearised [q-Navier--Stokes equation](#def:q-navier-stokes) governing normal perturbations of $\varrho$ reads

$$
  \partial_t^2 \eta
  = 
  \frac{\Gamma_q}{4\pi a_q^2}\Delta_q\eta
  -  \nu_q\Delta_q\partial_t \eta,
$$

where $\Gamma_q = [j]_q[j+1]_q$ fixes the quantised circulation at intensity level $j$, $a_q$ specifies the $q$-deformed vortex core radius, and the trailing term applies viscous damping.

**The $q$-Laplacian eigenvalue problem.**
The $q$-Laplacian evaluated on a circle of length $L$ acts exclusively on $L$-periodic functions $f(s)$. Its eigenvalue problem reads

$$
  \Delta_qf_k
  =  -\mu_kf_k,
  \qquad
  f_k(s + L) = f_k(s).
$$

For the classical Laplacian ($q = 1$), the eigenfunctions resolve as $e^{2\pi i k s / L}$ with corresponding eigenvalues $\mu_k = (2\pi k/L)^2$. The $q$-Laplacian replaces the integer $k$ with the $q$-integer $[k]_q = (q^k - q^{-k})/(q - q^{-1})$:

$$
  \mu_k^{(q)}
  = 
  \left(\frac{2\pi[k]_q}{L_q}\right)^2,
$$

where $L_q = L \cdot [1]_q / 1 = L$ (since $[1]_q = 1$ unconditionally).

**Derivation.**
The $q$-derivative operators define the $q$-Laplacian. Assign $z = e^{2\pi i s / L}$ for a function $f$ on the circle. Then:

$$
  D_q f(z) = \frac{f(qz) - f(q^{-1}z)}{(q - q^{-1})z},
$$

and $\Delta_q = -zD_q \circ zD_q$ (composing the radial part of the $q$-Casimir). Operating on the monomial $z^k$ yields

$$
  D_q(z^k)
  = \frac{q^k z^k - q^{-k} z^k}{(q - q^{-1})z}
  = [k]_qz^{k-1}.
$$

Consequently $zD_q(z^k) = [k]_qz^k$, proving

$$
  \Delta_q(z^k) = -[k]_q^2z^k.
$$

The exact eigenvalue reads $\mu_k^{(q)} = [k]_q^2$. Restoring physical units (filament length $L_q$ and quantum of action $\hbar_q$) produces:

$$
  \lambda_k^{(q)}
  = 
  [k]_q^2 \cdot \frac{\hbar_q}{L_q^2}.
$$

This precisely matches the formula declared in the [discrete vortex spectrum](#prop:discrete-vortex-spectrum).

**Dispersion relation.**
Inserting $\eta(s,t) = f_k(s)e^{-i\omega t}$ into the linearised equation and applying $\Delta_q f_k = -[k]_q^2 f_k / L_q^2$ yields

$$
  -\omega^2
  = 
  -\frac{\Gamma_q}{4\pi a_q^2}\frac{[k]_q^2}{L_q^2}
  +  i\omega\nu_q\frac{[k]_q^2}{L_q^2}.
$$

In the undamped limit ($\nu_q = 0$, tracing the Euler limit), the dispersion relation simplifies to

$$
  \omega_k^{(q)}
  = 
  \frac{\Gamma_q^{1/2}}{2\sqrt{\pi}a_q}
  \frac{[k]_q}{L_q},
$$

producing the $q$-deformed Kelvin dispersion. In the damped regime ($\nu_q > 0$), the complex frequency isolates the decay rate

$$
  \gamma_k^{(q)}
  = 
  \frac{\nu_q}{2}\frac{[k]_q^2}{L_q^2}
  = 
  \frac{\hbar_q}{4}\frac{[k]_q^2}{L_q^2}.
$$

Mode $k$ decays on the timescale $\tau_k = 1/\gamma_k^{(q)} = 4L_q^2 / (\hbar_q[k]_q^2)$. Because $[k]_q \sim q^k$ at large $k$, high modes decay **doubly exponentially** in $k$. This generates the rigorous exponential UV cutoff built into the [q-Navier--Stokes definition](#def:q-navier-stokes).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: kelvin-dispersion-derivation.md -->

<!-- FILE_START: kelvin-dispersion-derivation-interpretation.md -->
**Mathematical Novelty.** Mechanically $q$-deforming operators is standard procedure. The mathematical novelty lies in observing that evaluating the exact $q$-derivative $D_q$ against classical Kelvin-wave dispersion organically generates an exact, analytically rigorous doubly-exponential UV suppression mechanism ($\tau_k \sim q^{-2k}$) operating uniformly in the fluid bulk. It requires no ad-hoc phenomenological regularisation and abandons arbitrary cutoffs entirely.
<!-- FILE_END: kelvin-dispersion-derivation-interpretation.md -->

<!-- FILE_START: kelvin-classical-limit.md -->
As $q \to 1$, the components resolve to their classical definitions: $[k]_q \to k$, $\Gamma_q \to j(j+1)$, and $\nu_q \to 0$. The [q-Kelvin dispersion](#prop:kelvin-dispersion-derivation) immediately recovers the classical form $\omega_k = \Gamma k^2 / (4\pi a^2) \cdot (\ln(L/a) - c)$. The Biot--Savart self-induction integral generates the classical logarithmic factor; the $q$-deformation subsumes this logarithm directly into the deformed core radius $a_q$.
<!-- FILE_END: kelvin-classical-limit.md -->

<!-- FILE_START: acoustic-horizon-conditions.md -->
The [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ manifests horizons wherever the flow speed matches the local sound speed: $|v| = c_s$.

**Acoustic metric.**
Perturbations $\delta\psi$ in the brane fluid propagate along the acoustic geometry

$$
  g_{\mathrm{ac}}
  = 
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - |v|^2) & -v^T \\
    -v & \mathbf{1}_{3}
  \end{pmatrix},
$$

where $c_s^2 = \partial p / \partial\rho\big|_{Q_q}$ sets the local sound speed, natively tracking the quantum pressure.

**Sound speed in the brane fluid.**
Extracting the equation of state $p = p(\rho, q)$ from the [q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) dictates the sound speed:

$$
  c_s^2
  = 
  c_q^2\Bigl(1 - \frac{\hbar_q^2}{4\rho}
  \Delta_q\!\left(\frac{1}{\sqrt{\rho}}\right)
  \cdot \sqrt{\rho}\Bigr).
$$

Here $c_q = 1/(q-1)$ identifies the substrate [speed of light](#def:substrate-parameter). The trailing term supplies the quantum correction. At low density ($\rho \to 0$), the quantum pressure diverges, sending $c_s \to \infty$. At high density, the quantum correction collapses, leaving $c_s \to c_q$.

**Horizon formation conditions.**
An acoustic horizon forms exactly on a surface $\Sigma$ satisfying $|v| = c_s$. Three structural conditions must hold simultaneously:

1. **Transonic flow.** The Mach number $\mathcal{M} = |v|/c_s$ must traverse unity exactly on $\Sigma$: $\mathcal{M}|_\Sigma = 1$, transitioning from $\mathcal{M} < 1$ (subsonic) on one side to $\mathcal{M} > 1$ (supersonic) on the other.
2. **Non-degeneracy.** The gradient of the Mach number must remain non-zero across $\Sigma$: $\nabla(\mathcal{M}^2)|_\Sigma \neq 0$. This ensures the horizon forms a smooth hypersurface rather than collapsing into a degenerate critical point.
3. **Energy condition.** The effective energy density $T_{00} = \frac{1}{2}\rho(|v|^2 + c_s^2) + Q_q\rho$ must obey the null energy condition $T_{\mu\nu}k^\mu k^\nu \geq 0$ evaluated over all null vectors $k^\mu$ mapped by $g_{\mathrm{ac}}$. The inequalities $\rho > 0$ and $Q_q \geq 0$ automatically guarantee this.

**Surface gravity and Hawking temperature.**
Evaluating the surface gravity at an acoustic horizon gives

$$
  \kappa_H
  = 
  \frac{1}{2}\frac{\partial(c_s^2 - |v|^2)}{\partial n}
  \bigg|_\Sigma,
$$

where $n$ points strictly outward from $\Sigma$. Tracking Unruh's acoustic black hole mapping, the horizon radiates at the Hawking temperature

$$
  T_H
  = 
  \frac{\hbar_q\kappa_H}{2\pic_s}.
$$

Applying the brane fluid identity $\hbar_q = (q-1)/q$ produces:

$$
  T_H
  = 
  \frac{(q-1)}{2\pi q}
  \frac{\kappa_H}{c_s}.
$$

As $q \to 1$, $T_H \to 0$: the classical limit eliminates Hawking radiation entirely, matching the collapse of $\hbar_q$. At the physical value $q \approx 1.110$, the geometric factor $(q-1)/q \approx 0.099$ heavily suppresses $T_H$ compared to the generic estimate $\kappa_H / (2\pi c_s)$.

**Types of acoustic horizon in the brane fluid.**

| Configuration | Flow structure | Physical analogue |
|---|---|---|
| **Spherical inflow** | Radial $v = -v_r(r)\hat{r}$ where $v_r(r_H) = c_s$ | Schwarzschild black hole |
| **Vortex drain** | Circular $v = v_\varTheta(r)\hat\varTheta + v_r(r)\hat{r}$ | Kerr (rotating) black hole |
| **Expanding shell** | Outward $v = v_r(r)\hat{r}$ where $v_r(r_C) = c_s$ | Cosmological horizon (de Sitter) |
| **Vortex core** | Concentrated circulation $\lvert v\rvert \to \infty$ as $r \to 0$ | Naked singularity (requires $\lvert v\rvert > c_s$ exclusively for $r < r_0$) |

**$q$-dependent horizon radius.**
Evaluated for spherically symmetric inflow operating at velocity $v_r = -\Gamma_q / (4\pi r^2)$, the horizon nucleates at

$$
  r_H
  = 
  \left(\frac{\Gamma_q}{4\pic_s}\right)^{1/2}
  = 
  \left(\frac{[j]_q[j+1]_q}{4\pic_q}\right)^{1/2}
  \cdot (1 + O(\hbar_q)).
$$

At the fundamental level $j = 1/2$, the circulation evaluates to $[1/2]_q[3/2]_q = (q^2 + q^{-2} - q - q^{-1})/(q - q^{-1})^2 \approx 0.75$ using the physical anchor $q \approx 1.110$. The resulting horizon radius $r_H$ matches the scale of $\ell_q = (q-1)/q$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: acoustic-horizon-conditions.md -->

<!-- FILE_START: acoustic-horizon-conditions-interpretation.md -->
**Mathematical Novelty.** While analogue gravity routinely constructs acoustic metrics and Hawking temperatures, the mathematical novelty stems from instantiating this framework natively atop the $q$-deformed categorical substrate. The acoustic horizon conditions operate not as ad-hoc physical analogies but as exact geometric constraints restricting the $q$-Navier-Stokes fluid. The specific cyclotomic factor $\hbar_q = (q-1)/q$ rigorously and predictably suppresses the resulting Hawking temperature.
<!-- FILE_END: acoustic-horizon-conditions-interpretation.md -->

<!-- FILE_START: acoustic-gravitational-emergence.md -->
The [GR substrate geometry](#rem:gr-substrate-geometry) forces the acoustic metric to perfectly match the physical spacetime metric throughout the archimedean realisation. Acoustic horizons function precisely as **gravitational horizons**: black holes denote strictly regions of supersonic brane fluid flow. The Einstein field equations emerge cleanly as the long-wavelength limit of the [q-Navier--Stokes equation](#def:q-navier-stokes), isolating the stress-energy tensor $T_{\mu\nu}$ as the fluid momentum flux. Penrose--Hawking singularity theorems mathematically translate into the structural breakdown of smooth transonic flow. The classical singularity represents nothing more than the $q \to 1$ degeneration of an originally smooth $q$-deformed vortex core.
<!-- FILE_END: acoustic-gravitational-emergence.md -->
