<!-- FILE_START: particles-intro.md -->
The transport equation $\mathcal{D}_\nabla \psi = 0$ selects on-shell solutions, but requires a formal definition of a particle. We define a particle as a $q$-harmonic form, read off the fermion--boson decomposition from the weight splitting, and treat observation as a structural operation acting on these solutions.
<!-- FILE_END: particles-intro.md -->

<!-- FILE_START: categorical-q-ext-deriv.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The **$q$-deformed exterior derivative** $d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is

$$
  d_q =  q^{-1}d + (1 - q^{-1})\pi_V \circ d,
$$

where $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is the differential of the non-commutative de Rham complex. The operator $d_q$ acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms. The *$q$-adjoint* $\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$ is the formal adjoint of $d_q$ with respect to the dagger structure. These operators exist and are unique.
<!-- FILE_END: categorical-q-ext-deriv.md -->

<!-- FILE_START: q-harmonic-form.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $q$-deformed exterior derivative $d_q$. The *$q$-Laplacian* on $\Omega^k(A)$ is $\Delta_q = d_q\delta_q + \delta_qd_q$. A **particle** is an element $\alpha \in \Omega^k(A)$ that is $q$-harmonic: $\Delta_q \alpha = 0$.
<!-- FILE_END: q-harmonic-form.md -->

<!-- FILE_START: fermion-boson-decomposition.md -->
Let $\mathcal{H}_q^k = \ker\Delta_q \subset \Omega^k(A)$ denote the space of particles. The weight decomposition restricts to a short exact sequence

$$
  0 \to \mathcal{H}_{q,H}^k \to \mathcal{H}_q^k \xrightarrow{\pi_V} \mathcal{H}_{q,V}^k \to 0,
$$

where $\mathcal{H}_{q,H}^k = \mathcal{H}_q^k \cap \Omega^k_H(A)$ and $\mathcal{H}_{q,V}^k = \pi_V(\mathcal{H}_q^k)$. A **boson** is a particle in the kernel $\mathcal{H}_{q,H}^k$ (purely horizontal: $\alpha_V = 0$). A **fermion** is a particle with $\alpha_V \neq 0$. The sequence splits via $\pi_H$, giving $\mathcal{H}_q^k \cong \mathcal{H}_{q,H}^k \oplus \mathcal{H}_{q,V}^k$.
<!-- FILE_END: fermion-boson-decomposition.md -->

<!-- FILE_START: categorical-point.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum universe. A **categorical point** of $A$ is a morphism $p \colon \mathbf{1} \to A$. In the archimedean realisation $A = C^\infty(M)$, a categorical point corresponds to evaluation at $p \in M$. The augmentation ideal at $p$ is $\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$, and the germ of $A$ at $p$ is the quotient $A / \mathfrak{m}_p^2$.
<!-- FILE_END: categorical-point.md -->

<!-- FILE_START: observation.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with state bundle $\mathcal{S} \to M$. Let $p \colon \mathbf{1} \to A$ be a categorical point, and let $U \subset M$ be an open causal neighbourhood of $p$. An **observation** on $U$ is a pair $(\mathfrak{O}, \epsilon)$ where $\epsilon \in \{+1, -1\}$ is the direction and $\mathfrak{O} \in \Gamma\bigl(U, \mathrm{Ad}(J^1 \mathcal{S})\bigr)$ is a section of the adjoint bundle of the $1$-jet prolongation of $\mathcal{S}$.

The section $\mathfrak{O}$ satisfies:
1. **Frobenius compatibility:** The observation preserves the Frobenius form on $U$. The trace is preserved.
2. **Adjoint backreaction:** The observation acts on the colour fibre via the adjoint representation of $G$. The section $\mathfrak{O}_p$ rotates the colour degrees of freedom, shifting the substrate parameter $q \mapsto q' = q + \delta q$ via the Hopf coaction $\delta q(p) = \int_A(\mathfrak{O}_p(a_{(1)})S(a_{(2)}))$.

The sign $\epsilon$ determines whether the crossing injected at $p$ is $\sigma_i$ (forward, $+1$) or $\sigma_i^{-1}$ (backward, $-1$). The $J^1$ (jet) component receives information, reading the field and its first derivative. The $\mathrm{Ad}$ (adjoint) component sends back, rotating the gauge degrees of freedom and perturbing $q$.
<!-- FILE_END: observation.md -->

<!-- FILE_START: observation-energy.md -->
Let $\mathfrak{O}$ be an observation with positive substrate perturbation $\delta q > 0$. The quantum Planck constant $\hbar_q = 1 - q^{-1}$ satisfies

$$
  \hbar_{q + \delta q} - \hbar_q =  \frac{\delta q}{q(q + \delta q)} >  0.
$$

Every observation with positive substrate perturbation strictly increases the quantum energy of the system.

The categorical action evaluated at the perturbed parameter $q' = q + \delta q$ satisfies

$$
  \mathfrak{S}_{q'} = \mathfrak{S}_q +  \delta q \cdot \frac{\partial \mathfrak{S}_q}{\partial q} + O((\delta q)^2).
$$

The first-order shift is the observation cost. The classical energy can increase or decrease under observation; only the quantum energy monotonically increases.
<!-- FILE_END: observation-energy.md -->

<!-- FILE_START: two-observer-parallelogram.md -->
Let $p \colon \mathbf{1} \to A$ be a categorical point. Consider two independent observations $\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p} \colon A / \mathfrak{m}_p^2 \to A / \mathfrak{m}_p^2$ acting on a fermion $\alpha$. The commutator is

$$
  [\mathfrak{O}_{1,p}, \mathfrak{O}_{2,p}](\alpha_p) = [q_1'(p), q_2'(p)] \cdot (\alpha_V)_p.
$$

This vanishes if and only if the shifted parameters commute at $p$ or the particle is a boson ($(\alpha_V)_p = 0$). The non-cocommutativity of the Hopf structure ensures $[q_1'(p), q_2'(p)] \neq 0$: independent observations of a fermion at the same point necessarily disagree.

At a point $p$, the commutator of two observations equals the $q$-curvature $F_q$ of the $q$-connection evaluated on the loop spanned by the two observation directions: $[\delta q_1, \delta q_2] = F_q$. The observers agree if and only if the $q$-curvature vanishes. Swapping the observers negates the curvature.
<!-- FILE_END: two-observer-parallelogram.md -->

<!-- FILE_START: q-harmonic-flow.md -->
The substrate parameter $q(p)$ is conjectured to evolve by the **$q$-harmonic-map heat flow**:

$$
  \partial_t\, q \;=\; -\,\Delta_q\, q,
  \qquad
  \Delta_q \;=\; q^{-2}\Delta \;+\; q^{-1}(1-q^{-1})\,\mathfrak{C}
            \;+\; (1-q^{-1})^2\,\Delta_\xi ,
$$

where $\Delta$ is the base Laplacian, $\mathfrak{C}$ the first-order Casimir/drift term, and $\Delta_\xi$ the Reeb-fibre Laplacian. Its stationary configurations $\Delta_q q = 0$ are the $q$-harmonic sections; the vacuum constant $q \equiv q_0$ is the trivial one. This PDE serves as an ansatz for the dynamical evolution of the substrate parameter.
<!-- FILE_END: q-harmonic-flow.md -->

<!-- FILE_START: observation-fermion-action.md -->
The $\mathrm{Ad}$ component of an observation acts directly on fermions via the eigenspace decomposition of the Hecke generator $\sigma$:

$$
  V \otimes V = \underbrace{\mathrm{Sym}^2(V)}_{\text{bosonic, } q} \oplus \underbrace{\textstyle\bigwedge^2(V)}_{\text{fermionic, } {-q^{-1}}}
$$

On bosons ($\mathrm{Sym}^2$), the observation preserves the eigenspace. The $\mathrm{Ad}$ action commutes with the symmetric projection. The commutator of two observations vanishes on bosons. Bosons can be observed without interference.

On fermions ($\bigwedge^2$), the $\mathrm{Ad}$ action conjugates the antisymmetric component by $G$, mixing the fermionic state with the bosonic eigenspace. The observation partially converts fermionic content to bosonic content, depositing $q + q^{-1}$ per crossing in the colour fibre. Two observers acting on the same fermion interfere because their rotations in the colour fibre do not commute. The geometric non-commutativity of $G = \mathrm{SU}_2(R)$ forces this uncertainty.
<!-- FILE_END: observation-fermion-action.md -->
