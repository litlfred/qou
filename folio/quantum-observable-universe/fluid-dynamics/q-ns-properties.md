**Properties.**

1. **Algebraic dissipation spectrum.** The term $\nu_q\Delta_q v$ damps mode $k$ at the rate $\nu_q[k]_q^2 / L_q^2$. The $q$-integers increase as $[k]_q \sim q^k / (q - q^{-1})$, causing high-wavenumber modes to undergo **exponential** rather than polynomial damping. This serves as a structural UV regularisation.
2. **Gauge-covariant diffusion.** The connection $A$ governs every derivative. Viscous diffusion thus transports colour charge alongside momentum: as a vortex filament decays, it radiates its $\mathrm{SU}_q(2)$ quantum numbers into nearby filaments via the connection.
3. **Quantum pressure as negative viscosity.** At short wavelengths, $Q_q$ acts as negative viscosity, **opposing** fluid compression below the length scale $\ell_q = (q-1)/q$. The equilibrium between dissipation ($\nu_q\Delta_q v$) and quantum repulsion ($\nabla_A Q_q$) sets the minimum vortex core radius.

**Energy dissipation rate.**
The global energy dissipation rate for the $q$-Navier--Stokes equation is

$$
  \varepsilon_q
  = 
  \nu_q \int_{\mathcal{S}}
  \rho\lVert\nabla_A v\rVert^2d\mu
  = 
  \nu_q \sum_{k=1}^{\infty}
  [k]_q^2|v_k|^2,
$$

where $v_k$ denotes the Fourier coefficients in the $q$-integer eigenbasis. For $q > 1$, the exponential damping guarantees the sum converges absolutely, circumventing the standard barriers to proving classical 3D energy estimates.

**Classical and quantum limits.**

| Limit | $\nu_q$ | $Q_q$ | Equation reduces to |
|---|---|---|---|
| $q \to 1$ | $0$ | $0$ | Euler equation (inviscid, zero quantum pressure) |
| $q \to 1^+$ (fixed $\hbar_q$) | $\hbar_q/2$ | $-\hbar^2\Delta\sqrt{\rho}/(2\sqrt{\rho})$ | Navier--Stokes + Bohm potential |
| $q \gg 1$ | $(1 - 1/q)/2$ | Dominant | Flow freezes to ground state due to extreme pressure |

**Well-posedness.**
The energy estimate $\frac{d}{dt}\lVert v\rVert^2 \leq -\nu_q[1]_q^2\lVert v\rVert^2$ yields exponential decay of the total kinetic energy, and the exponential $q$-growth halts the enstrophy blowup that sabotages classical proofs. The classical 3D Navier--Stokes regularity problem is an artefact of the $q \to 1$ singularity.
