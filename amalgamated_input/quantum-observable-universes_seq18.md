<!-- FILE_START: geometric-interpretations-intro.md -->
We interpret the categorical operators $d_q$, $\delta_q$, $\Delta_q$, and the fermion--boson decomposition through the dictionary of classical vector calculus. The $q$-Laplacian $\Delta_q \alpha = 0$ identifies equilibrium between the spatial environment and internal quantum spin. The closed form $\delta_q = q^{-1}\delta + (1-q^{-1}) \mathcal{L}_\xi^* \circ \iota_\xi$ enables a three-term expansion of $\Delta_q$ into classical diffusion, Coriolis cross-coupling, and pure spin diffusion.

A particle is simultaneously $q$-closed and $q$-coclosed. Allowing $q$ to acquire a phase destroys the positivity of the Haar functional and is excluded by the observability axiom, but the algebraic sector remains internally consistent.
<!-- FILE_END: geometric-interpretations-intro.md -->

<!-- FILE_START: vector-calculus-bridge.md -->
We recall the classical vector calculus operators as differential forms on a smooth Riemannian manifold $(M, g)$.

A $0$-form is a scalar field $f \colon M \to \mathbb{R}$. A $1$-form $\alpha$ assigns a number to each tangent vector. A $2$-form $\beta$ measures oriented flux through an infinitesimal parallelogram.

The exterior derivative $d$ yields the gradient $df$ on a $0$-form and the curl $d\alpha$ on a $1$-form. The identity $d^2 = 0$ encodes $\nabla \times (\nabla f) = 0$ and $\nabla \cdot (\nabla \times \mathbf{F}) = 0$.

The Hodge star $\star$ maps $k$-forms to $(n{-}k)$-forms by complementing directions. The codifferential $\delta = (-1)^{nk+n+1}\star d\star$ is the formal adjoint of $d$, acting as $-\mathrm{div}(\alpha^{\sharp})$ on $1$-forms. The Hodge Laplacian is $\Delta = d\delta + \delta d$. A function $f$ is harmonic ($\Delta f = 0$) when its value equals the average over any small sphere centered at the point.
<!-- FILE_END: vector-calculus-bridge.md -->

<!-- FILE_START: q-laplacian-interpretation.md -->
The $q$-Laplacian $\Delta_q = d_q\delta_q + \delta_qd_q$ replaces the classical neighbourhood with a quantum-twisted neighbourhood that weights the horizontal (spatial) and vertical (Reeb/spin) directions differently.

Setting $\Delta_q \alpha = 0$ specifies that the field $\alpha$ is in equilibrium between its spatial environment and its internal quantum spin. The geometric twist precisely counterbalances the spatial diffusion:
- **At $q = 1$**: $d_q = d$, and $\Delta_q$ reduces to the Hodge Laplacian $\Delta$. The quantum twist vanishes, and $q$-harmonic forms are ordinary harmonic forms.
- **At $q \to \infty$**: $d_q$ projects onto $\pi_V \circ d$. A $q$-harmonic form is averaged purely along the internal fibre.

A $q$-harmonic form ($\Delta_q \alpha = 0$) is a particle: a field configuration in perfect $q$-equilibrium with its twisted geometric environment. The substrate parameter $q$ tunes the relative weight of spatial diffusion versus internal spin.
<!-- FILE_END: q-laplacian-interpretation.md -->

<!-- FILE_START: q-codifferential-formula-prop.md -->
Let $d_q = q^{-1}d + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi$ be the $q$-exterior derivative. The formal adjoint of $d_q$ with respect to the Webster inner product $\langle \cdot, \cdot \rangle_\varTheta$ is

$$
  \delta_q =  q^{-1}\delta +  (1 - q^{-1})\mathcal{L}_\xi^* \circ \iota_\xi.
$$

This is uniquely characterised by the adjoint relation $\langle d_q\alpha, \beta \rangle_\varTheta = \langle \alpha, \delta_q\beta \rangle_\varTheta$ for all compactly supported forms $\alpha, \beta$.
<!-- FILE_END: q-codifferential-formula-prop.md -->

<!-- FILE_START: q-codifferential-formula.md -->
In the archimedean realisation, the $q$-exterior derivative is $d_q = q^{-1}d + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi$. To find the formal adjoint $\delta_q$, each operation in $d_q$ is replaced by its geometric mirror:
1. The derivative $d$ becomes the codifferential $\delta$.
2. Wedging with the contact form ($\varTheta \wedge$) becomes contraction with the Reeb vector field ($\iota_\xi$).
3. The Lie derivative $\mathcal{L}_\xi$ becomes its formal adjoint $\mathcal{L}_\xi^*$.

The closed formula is $\delta_q = q^{-1}\delta + (1 - q^{-1})\mathcal{L}_\xi^* \circ \iota_\xi$. While $d_q$ uses the Reeb vector field to add a vertical spin twist, the codifferential $\delta_q$ uses contraction with $\xi$ to extract it.
<!-- FILE_END: q-codifferential-formula.md -->

<!-- FILE_START: q-laplacian-expansion.md -->
Expanding $\Delta_q = d_q\delta_q + \delta_qd_q$ separates the $q$-Laplacian into three terms:

1. **Classical core** ($\propto q^{-2}$): Proportional to $q^{-2}\Delta$, this is the standard spatial diffusion operator.
2. **Quantum spin core** ($\propto (1 - q^{-1})^2$): Involving only Reeb operations ($\varTheta \wedge \mathcal{L}_\xi$ and $\mathcal{L}_\xi^* \circ \iota_\xi$), these terms represent pure internal Reeb dynamics.
3. **Cross-coupling terms** ($\propto q^{-1}(1 - q^{-1})$): Mixed terms combining spatial derivatives with Reeb operations measure the interference between macroscopic spatial motion and internal spin.

The expansion is:
$$
  \Delta_q = q^{-2}\Delta +  q^{-1}(1 - q^{-1})\bigl[d(\mathcal{L}_\xi^* \iota_\xi) + (\varTheta \wedge \mathcal{L}_\xi)\delta + \delta(\varTheta \wedge \mathcal{L}_\xi) + (\mathcal{L}_\xi^* \iota_\xi)d\bigr] +  (1 - q^{-1})^2\Delta_{\xi},
$$
where $\Delta_\xi = (\varTheta \wedge \mathcal{L}_\xi) (\mathcal{L}_\xi^* \iota_\xi) + (\mathcal{L}_\xi^* \iota_\xi) (\varTheta \wedge \mathcal{L}_\xi)$ is the pure spin Laplacian.
<!-- FILE_END: q-laplacian-expansion.md -->

<!-- FILE_START: q-laplacian-spectral-tower.md -->
The $q$-Laplacian $\Delta_q$ has eigenvalues given by the $q$-integer tower

$$
  [k]_q^2, \qquad [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}} \quad (k = 1, 2, 3, \ldots).
$$

At a primitive root of unity $q = e^{i\pi/\kappa}$, the $q$-integer $[\kappa]_q$ vanishes, and the spectrum truncates to the finite set

$$
  \{\,[1]_q^2, [2]_q^2, \ldots, [\kappa-1]_q^2\,\},
$$

yielding the Verlinde / ADE quantum-dimension data of the truncated representation category. The surviving quantum dimensions are exact algebraic numbers in the cyclotomic field $\mathbb{Q}(\zeta_\kappa)$.
<!-- FILE_END: q-laplacian-spectral-tower.md -->

<!-- FILE_START: q-laplacian-consumers.md -->
The $q$-Laplacian spectral tower acts as the organizing data for multiple $q$-deformed structures. The $q$-heat equation $\partial_t u = -\Delta_q u$ dictates that mode $k$ decays as $e^{-[k]_q^2 t}$. The $q$-Navier–Stokes dissipation exhibits eigenvalues $[k]_q^2 \sim q^{2k}$. The Markov trace / Gram blocks encode block quantum dimensions $[2j+1]_q$, and the Yekutieli lifting obstruction tower caps at $\kappa-1$.

The exact truncation at roots of unity guarantees that spectral computations form finite exact sums with no series-truncation error. The tower and its truncation form fibre-level statements; the observable component requires evaluating at the real archimedean substrate value $q_0$.
<!-- FILE_END: q-laplacian-consumers.md -->

<!-- FILE_START: hodge-laplacian-relation.md -->
The $q$-Hodge star $\star_q$ rescales the inner product by the substrate parameter $q$, and the $q$-codifferential $\delta_q$ inherits this deformation. The $q$-Laplacian $\Delta_q$ is formally self-adjoint with respect to the Webster inner product.

Self-adjointness guarantees real eigenvalues and orthogonal eigenspaces. The space of particles, $\ker \Delta_q$, is a well-defined subspace with a canonical complement.
<!-- FILE_END: hodge-laplacian-relation.md -->

<!-- FILE_START: categorical-lichnerowicz.md -->
Let $\nabla$ be a categorical connection on an adjoint bundle over the contact affine chart with Reeb derivation $\xi$ and $q$-Hodge star $\star_q$. Let $\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \, \iota_\xi \nabla$ be the categorical Dirac operator, and $\Delta_\nabla^q$ the categorical $q$-Laplacian. On the categorical-instanton saddle $\star_q F_\nabla = F_\nabla$:

$$
  \Delta_\nabla^q  =  \mathfrak{D}_\nabla^2  +  \tfrac{1}{4}\,\mathrm{Sc}_q,
$$

where $\mathrm{Sc}_q$ is the $q$-scalar curvature. On the Bring background, the Reeb generator $\xi = e_3$ is parallel, forcing $\mathrm{Sc}_q = 0$ and simplifying the identity to $\Delta_\nabla^q = \mathfrak{D}_\nabla^2$. The $q$-scalar curvature $\mathrm{Sc}_q = R + O(\hbar_q)$ encodes both the classical scalar curvature and the $q$-anomaly contribution from $d_q^2 \neq 0$.
<!-- FILE_END: categorical-lichnerowicz.md -->

<!-- FILE_START: lichnerowicz-wkb-corollary.md -->
The categorical Lichnerowicz identity provides the gauge Hessian at the categorical-instanton saddle. This $q$-Laplacian $\Delta_\nabla^q$ equals $\mathfrak{D}_\nabla^2$ on the parallel-Reeb background. The Pfaffian structure on chiral spinors converts $-\tfrac{1}{2}\log \det \Delta_\nabla^q = -\log \det |\mathfrak{D}_\nabla| = -\tfrac{1}{2}\log \det \mathfrak{D}_\nabla$, recovering the WKB $S_1$ formula.
<!-- FILE_END: lichnerowicz-wkb-corollary.md -->

<!-- FILE_START: lichnerowicz-q-correction.md -->
The $q$-scalar curvature $\mathrm{Sc}_q = R + O(\hbar_q)$ encodes both the classical scalar curvature and the anomaly contribution from $d_q^2 \neq 0$. The $O(\hbar_q)$ correction adds a contact-curvature term on a non-flat substrate. On the contact-flat Bring background, both contributions vanish, yielding $\Delta_\nabla^q = \mathfrak{D}_\nabla^2$.
<!-- FILE_END: lichnerowicz-q-correction.md -->

<!-- FILE_START: q-harmonic-particle.md -->
By the self-adjointness and positive-definiteness of $\Delta_q$, a form $\alpha$ is $q$-harmonic ($\Delta_q \alpha = 0$) if and only if it is simultaneously $q$-closed and $q$-coclosed:

$$
  d_q\alpha = 0 \quad\text{and}\quad \delta_q\alpha = 0.
$$

A particle is a field configuration in perfect equilibrium with respect to the $q$-deformed geometry. The fermion--boson decomposition classifies particles by their vertical component under the weight decomposition. Bosons are purely horizontal ($\alpha_V = 0$); fermions have non-trivial vertical part.

The logical chain is: $\text{QOU} \to \text{$q$-exterior derivative} \to \text{$q$-codifferential} \to \text{$q$-Laplacian} \to \text{particle} \to \text{boson $\oplus$ fermion}$.
<!-- FILE_END: q-harmonic-particle.md -->

<!-- FILE_START: brings-geometric-connection.md -->
The geometric structures of the $q$-Laplacian, fermion--boson decomposition, and contact affine chart manifest concretely on the Bring surface. The contact structure $\varTheta$, Reeb vector field $\xi$, and substrate parameter $q$ reduce to explicit formulas on a genus-$4$ Riemann surface with $S_5$ symmetry. The abstract equilibrium $\Delta_q \alpha = 0$ reduces to computable eigenvalue problems, and the boson--fermion split becomes a Hodge decomposition of the harmonic space.
<!-- FILE_END: brings-geometric-connection.md -->

<!-- FILE_START: complex-substrate-interpretation.md -->
For a complex substrate parameter $q = |q|e^{i\varTheta}$, the quantum Planck constant is $\hbar_q = 1 - |q|^{-1} e^{-i\varTheta}$. When $\varTheta \neq 0$, $\hbar_q$ acquires an imaginary part, and the $q$-equilibrium mixes amplitudes with phases.

The observability axiom demands positive-definiteness of the Haar functional $h_q$. This requires $d_q^\dagger$ to be the formal adjoint of $d_q$, which holds if and only if $q \in \mathbb{R}_{>0}$. Relaxing the observability axiom gives the phase $\varTheta$ geometric meaning:

1. Complex $q$ contributes a continuous relative phase between over- and under-crossings.
2. Chirality reversal acts as a continuous rotation in the $\varTheta$-circle.
3. The non-Hermitian $q$-Laplacian produces complex eigenvalues, generating a probability current along the Reeb fibre.

The specialisation at root-of-unity $q_0 = e^{\pi i / \kappa}$ is complex. Root-of-unity categories carry a modified quantum trace $\mathrm{tr}_q$ restoring a non-degenerate pairing without requiring Hilbert-space positive-definiteness, forming a consistent algebraic sector outside the strict observability axiom.
<!-- FILE_END: complex-substrate-interpretation.md -->

