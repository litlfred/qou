<!-- FILE_START: variational-equations-intro.md -->
The canonical action $\mathfrak{S}_q$ depends on the Frobenius form $\int_A$, the connection $\nabla$, and the state $\psi$. Varying each yields one of the three classical field equations in categorical form: the categorical Einstein equation, the categorical Yang--Mills equation, and the categorical transport equation. The transport equation governs the spatial propagation of states, combining parallel transport and Reeb diffraction. We trace this propagation through a double-slit geometry to predict a material-dependent torsion phase shift.
<!-- FILE_END: variational-equations-intro.md -->

<!-- FILE_START: variational-equations.md -->
Let $\mathfrak{S}_q$ be the categorical action. The three variational equations are:

1. **Gravity (vary $\int_A$)**: $\delta\mathfrak{S}_q / \delta\!\int_A = 0$ yields the *categorical Einstein equation*:
   $$
     R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})\mathrm{id}_A =  T_q[\nabla, \psi],
   $$
   where $T_q$ is the stress-energy endomorphism constructed from the gauge and matter terms.

2. **Gauge (vary $\nabla$)**: $\delta\mathfrak{S}_q / \delta\nabla = 0$ yields the *categorical Yang--Mills equation*:
   $$
     \nabla \star_q F_\nabla + q \cdot [F_\nabla, \star_q F_\nabla] =  J_\psi,
   $$
   where $J_\psi = \psi^* \otimes D_\nabla\psi - D_\nabla\psi^* \otimes \psi$ is the matter current.

3. **Matter (vary $\psi$)**: $\delta\mathfrak{S}_q / \delta\psi = 0$ yields the *categorical transport equation*:
   $$
     D_\nabla\psi =  0.
   $$
<!-- FILE_END: variational-equations.md -->

<!-- FILE_START: wavefront-propagation.md -->
The categorical transport equation $\mathcal{D}_\nabla\psi = 0$ governs the spatial propagation of a state $\psi \colon \mathbf{1} \to A$ through the quantum observable universe. It is the categorical analog of the classical wave equation.

The two terms of the categorical Dirac operator $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$ contribute distinct physical effects:

1. **Parallel transport** ($q^{-1}\nabla$): The state $\psi$ is covariantly transported along geodesics of the connection $\nabla$. At $q = 1$, this is the only term, and the wavefront propagates without transverse spreading.
2. **Reeb diffraction** ($(1-q^{-1})\iota_\xi\nabla$): The Reeb contraction $\iota_\xi$ couples $\psi$ to the vertical contact direction, inducing wavefront spreading. The state acquires transverse amplitude proportional to the quantum Planck constant $\hbar_q = 1 - q^{-1}$.

The beam width emerges as a derived quantity, determined by the Green's function of $\mathcal{D}_\nabla$ on the instanton background. On a flat instanton ($F_\nabla = 0$), the Gaussian beam waist $w_0$ is fixed by $q$ and the source geometry. At a material boundary, $F_\nabla \neq 0$ and the wavefront diffracts around the edge. The on-shell condition $\mathcal{D}_\nabla\psi = 0$ eliminates the matter term from the Lagrangian, leaving only the topological gauge sector.
<!-- FILE_END: wavefront-propagation.md -->

<!-- FILE_START: photon-wavefront-example.md -->
We trace the wavefront propagation equation $\mathcal{D}_\nabla\psi = 0$ through a double-slit experiment, using the photon as the test particle. In the QOU, a photon carries color content $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$, where the Hecke generators encode polarisation on the exceptional divisor. The purely horizontal identity component acts as a boson; the color dressing $\varphi_i\sigma_i$ adds polarisation-dependent Reeb phase.

**Free propagation (source to barrier):** The connection is the flat instanton ($F_\nabla = 0$). Since $\psi$ is horizontal, the Reeb contraction $\iota_\xi\nabla\psi$ extracts the vertical part of the connection's action, producing Gaussian spreading with beam waist $w_0$.

**Slit interaction (barrier):** The barrier material consists of localized knots with knot type $K_{\mathrm{mat}}$. At the slit walls, $F_\nabla \neq 0$, and the instanton condition $\star_q F_\nabla = F_\nabla$ constrains the curvature to be self-dual with topological charge determined by $K_{\mathrm{mat}}$. At each slit wall, the Reeb term $(1-q^{-1})\iota_\xi\nabla$ imparts a torsion phase:

$$
  \tau(y) = \hbar_q \cdot \mathrm{Vol}(K_{\mathrm{mat}}) \cdot \eta(y)^2 \cdot k w,
$$

where $\eta = |y|/(d/2)$ is the normalized slit coordinate, $k = 2\pi/\lambda$ is the wavenumber, and $w$ is the slit thickness. This constitutes the $q$-deformed Huygens--Fresnel correction.

**Post-slit propagation (barrier to screen):** After passing through the slits, $\psi$ satisfies $\mathcal{D}_\nabla\psi = 0$ on a flat background with boundary conditions set by the two slit openings. The wavefronts interfere, producing the intensity pattern

$$
  I(x) = \left| \sum_{s=1}^{2} \int_{-d/2}^{d/2} e^{ik(r_1+r_2)} e^{i\tau(y)} e^{-y_s^2/w_0^2} dy \right|^2.
$$

The torsion correction $\tau(y)$ is absent in the classical $q = 1$ limit. Its magnitude depends on the hyperbolic volume $\mathrm{Vol}(K_{\mathrm{mat}})$ of the barrier material's knot type. Different slit materials produce material-dependent fringe shifts.

When the photon carries non-trivial color content, each polarisation mode $\sigma_i$ acquires its own Hecke eigenvalue weighting the torsion phase. The corrected torsion becomes

$$
  \tau^{(\mathrm{color})}(y) = \tau(y) + (\varphi_0 q - \varphi_1 q^{-1}) \hbar_q \cdot \mathrm{Vol}(K_{\mathrm{mat}}) \cdot \eta(y)^2 \cdot k w.
$$

For linearly polarised light, the correction is first order in $\hbar_q$ and depends on the polarisation angle, yielding a measurable signature distinct from classical birefringence.
<!-- FILE_END: photon-wavefront-example.md -->
