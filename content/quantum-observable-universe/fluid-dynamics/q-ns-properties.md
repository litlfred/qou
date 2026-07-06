**Properties.**

1. **Algebraic dissipation spectrum.** The viscous term
 $\nu_q\Delta_q v$ damps mode $k$ at rate
 $\nu_q[k]_q^2 / L_q^2$. Because the $q$-integers
 grow as $[k]_q \sim q^k / (q - q^{-1})$ for large $k$,
 high-wavenumber modes are damped **exponentially** rather than
 polynomially, providing a natural UV regularisation absent from
 classical Navier--Stokes.

2. **Gauge-covariant diffusion.** The connection $A$ appears in
 every derivative. Viscous diffusion transports not only momentum
 but also colour charge: a vortex filament that decays by viscous
 damping radiates its $\mathrm{SU}_q(2)$ quantum numbers into
 neighbouring filaments via the connection.

3. **Quantum pressure as negative viscosity.** The $Q_q$ term
 acts as a negative viscosity at short wavelengths: it
 **opposes** compression of the fluid below the scale
 $\ell_q = (q-1)/q$. The balance between $\nu_q\Delta_q v$
 (dissipation) and $\nabla_A Q_q$ (quantum repulsion) determines
 the minimum vortex core radius.

**Energy dissipation rate.**
The global energy dissipation rate of the $q$-Navier--Stokes
equation is

$$
  \varepsilon_q
  = 
  \nu_q \int_{\mathcal{S}}
  \rho\lVert\nabla_A v\rVert^2d\mu
  = 
  \nu_q \sum_{k=1}^{\infty}
  [k]_q^2|v_k|^2,
$$

where $v_k$ are the Fourier coefficients in the $q$-integer
eigenbasis. For $q > 1$, the sum converges absolutely
(exponential damping of high modes), resolving the classical
difficulty of proving energy estimates for 3d Navier--Stokes.

**Classical and quantum limits.**

| Limit | $\nu_q$ | $Q_q$ | Equation reduces to |
|---|---|---|---|
| $q \to 1$ | $0$ | $0$ | Euler equation (inviscid, no quantum pressure) |
| $q \to 1^+$ with $\hbar_q$ held | $\hbar_q/2$ | $-\hbar^2\Delta\sqrt{\rho}/(2\sqrt{\rho})$ | Ordinary Navier--Stokes + Bohm potential |
| $q \gg 1$ | $(1 - 1/q)/2$ | Dominant | Quantum pressure dominates; flow frozen to ground state |

**Well-posedness.**
The exponential damping of high-wavenumber modes by the
$q$-Laplacian ensures that the $q$-Navier--Stokes equation is
globally well-posed in 3d for any $q > 1$ (see
[the well-posedness theorem](#thm:q-ns-wellposedness)): the energy estimate
$\frac{d}{dt}\lVert v\rVert^2 \leq -\nu_q[1]_q^2\lVert v\rVert^2$
gives exponential decay of the total kinetic energy, and the
$q$-integer growth prevents the enstrophy blowup that obstructs
classical regularity proofs. The classical 3d Navier--Stokes
regularity problem is thus an artefact of the $q \to 1$
degeneration.
