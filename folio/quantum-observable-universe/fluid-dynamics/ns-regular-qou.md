Let $(\mathbf{C}, A, \tau)$ define a [quantum universe](#def:quantum-universe) over a closed orientable spectral surface $\mathcal{S}$ sustaining a [brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$ alongside [quantum characteristic classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

The **NS obstruction** governing $(\mathbf{C}, A, \tau)$ is the **global** surface Euler class of the Reeb $\mathrm{U}(1)$-bundle $\xi$ on $\mathcal{S}$:

$$
  \mathrm{NS}(A)
  =
  \kappa_0
  =
  e(\xi)
   \in
  H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z},
$$

whose degree is the Euler characteristic $\deg e(\xi) = \mathrm{tr}(\kappa_0) = \chi(A)$ ([Descartes theorem](#thm:ns-singularity-descartes), item 1).

Accordingly, $(\mathbf{C}, A, \tau)$ is classified as:

- **NS-regular** if $\mathrm{NS}(A) = 0$ (equivalently $\chi(A) = 0$);
- **NS-singular** if $\mathrm{NS}(A) \neq 0$ (equivalently $\chi(A) \neq 0$).

The NS obstruction tracks only the rigid categorical topology of $(\mathbf{C}, A, \tau)$ on $\mathcal{S}$. It operates independently of the selected substrate section $q$ and ignores specific initial data:

| $\chi(A)$ | $\mathrm{NS}(A) = e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$ | Internal model status |
|---|---|---|
| $\neq 0$ | $\neq 0$ | NS-singular (internal QOU label) |
| $= 0$ | $= 0$ | NS-regular (internal QPU label) |

*Why $\mathrm{NS}(A)$ is defined on the global surface $\mathcal{S}$ rather than on $\Sigma$.* Restricting $\kappa_0$ to a one-dimensional vortex-collision locus $\Sigma \subset \mathcal{S}$ gives $\kappa_0|_\Sigma \in H^2(\Sigma, \mathcal{B}) = 0$, because $\dim \Sigma = 1$ forces every surface class to restrict to zero on $\Sigma$ ([Descartes theorem](#thm:ns-singularity-descartes), item 3). Defining $\mathrm{NS}(A)$ as the global surface class $e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$ provides a non-degenerate topological invariant determined directly by $\deg e(\xi) = \chi(A)$, at the cost that $\mathrm{NS}(A)$ does not localise on a collision curve $\Sigma$.

The defining observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ acts as a **sufficient condition** guaranteeing $\chi(A) \neq 0$ (forcing rigid irreducibility on the adjoint representation to guarantee a nonzero Euler class). Consequently every quantum observable universe satisfies $\mathrm{NS}(A) = e(\xi) \neq 0$ and is internally NS-singular; a $\chi(A) = 0$ universe is a quantum pre-universe (QPU), not a QOU.

**Scope of the 3D Navier--Stokes bridge (framework model correspondence).** "NS-regular" and "NS-singular" are internal categorical labels for the global Euler class $\mathrm{NS}(A) = e(\xi)$ on $\mathcal{S}$. Connecting this internal invariant to global regularity or finite-time blowup of the classical unforced 3D incompressible Navier--Stokes equations on $\mathbb{R}^3$ or $\mathbb{T}^3$ is a **framework model correspondence**, not a deductive PDE equivalence:

1. *Tao's averaged Navier--Stokes barrier.* By Tao's theorem (*J. Amer. Math. Soc.* **29** (2016), 601--674), any regularity argument for critical or supercritical 3D Navier--Stokes whose inputs are invariant under rotational, dilation, and Fourier-multiplier averaging of the bilinear advection operator $B(u, u) = P[(u \cdot \nabla)u]$ applies unchanged to an averaged operator $\tilde{B}(u, u)$ that admits finite-time blowup. Because $\mathrm{NS}(A) = e(\xi)$ is a purely topological invariant of $\mathcal{S}$ using no property of the PDE nonlinearity $B$, the condition $\mathrm{NS}(A) = 0$ cannot by itself constitute a deductive proof of classical 3D global regularity.
2. *Scaling branch at $q \to 1$.* Taking $q \to 1$ at fixed $\nu_q = (q - 1)/(2q)$ yields the inviscid Euler limit ($\nu_1 = 0$); viscous Navier--Stokes sits on the fixed-$\hbar_q$ scaling branch, and transferring internal $q > 1$ subcritical regularity or $q \to 1$ surface obstructions across that limit to 3D physical solutions remains an open bridge.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
