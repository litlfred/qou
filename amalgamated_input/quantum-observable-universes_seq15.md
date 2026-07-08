<!-- FILE_START: categorical-action-intro.md -->
The Lagrangian $\mathcal{L}_q$ acts as an endomorphism of $A$. We trace it to a morphism $\mathbf{1} \to \mathbf{1}$ and read off the gravity, gauge, and matter terms that the QOU axioms force into the result. The rigid duality supplies the trace; no spacetime measure is invoked.

The categorical action defines $\mathfrak{S} = \mathrm{tr}(\Phi)$ for a physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$. Choosing $\Phi_q = \mathcal{L}_q$ delivers $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$, which expands via the Frobenius--Hopf decomposition of $\mathcal{D}_\nabla^2$ into three terms: gravity $\mathrm{tr}(q R_{\int})$, gauge $\int_A \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$, and matter $\int_A(\psi^* \cdot \mathcal{D}_\nabla \psi)$. This holds uniquely up to a single scalar $\lambda \in R^\times$ tracking the normalisation of $\int_A$.
<!-- FILE_END: categorical-action-intro.md -->

<!-- FILE_START: categorical-action.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. A :defterm[categorical action]{#categorical-action} on $(\mathbf{C}, A, \tau)$ is a morphism $\mathfrak{S} \colon \mathbf{1} \to \mathbf{1}$ of the form

$$
  \mathfrak{S}
  = 
  \mathrm{ev}_A
    \circ
    \bigl(\mathrm{id}_{A^\vee} \otimes \Phi\bigr)
    \circ
    \mathrm{coev}_A,
$$

where $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ is the physics endomorphism. The evaluation $\mathrm{ev}_A \colon A^\vee \otimes A \to \mathbf{1}$ and coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$ are the structure maps of the rigid duality on $A$. Composing them with an inserted endomorphism produces the categorical trace $\mathfrak{S} = \mathrm{tr}(\Phi)$.

As a string diagram, the action forms a single closed loop with $\Phi$ inserted. The rigid structure provides the integration; the physics endomorphism encodes the dynamics.
<!-- FILE_END: categorical-action.md -->

<!-- FILE_START: categorical-action-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe and $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ a physics endomorphism. The categorical action $\mathfrak{S}_\Phi = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi) \circ \mathrm{coev}_A$ exists as a morphism in $\mathbf{C}$ and equals the categorical trace $\mathrm{tr}(\Phi)$.
<!-- FILE_END: categorical-action-exists.md -->

<!-- FILE_START: categorical-action-unique.md -->
For a fixed physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$, the categorical action $\mathfrak{S}_\Phi = \mathrm{tr}(\Phi)$ is uniquely determined. Any morphism $\mathbf{1} \to \mathbf{1}$ factoring as $\mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi) \circ \mathrm{coev}_A$ equals $\mathrm{tr}(\Phi)$.
<!-- FILE_END: categorical-action-unique.md -->

<!-- FILE_START: categorical-action-notation.md -->
The following notation applies to the categorical action:
- $\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$ is the categorical trace.
- $R_{\int} \in \mathrm{End}_{\mathbf{C}}(A)$ is the Frobenius--Ricci endomorphism: the curvature of the Frobenius form $\int_A$, defined by $R_{\int} = (\mathrm{id}_A \otimes \int_A) \circ F_{\nabla_{\int}}$, where $\nabla_{\int}(a) = \int_A(a_{(1)}) \otimes a_{(2)} - a \otimes 1$.
- $\mathrm{tr}_A \colon \mathrm{End}_{\mathbf{C}}(A \otimes \Omega^{\bullet}(A)) \to \mathrm{End}_{\mathbf{C}}(\Omega^{\bullet}(A))$ is the partial trace over the $A$ factor.
- $\psi^* = \int_A \circ S(\psi) \colon A \to \mathbf{1}$ is the adjoint section.
- $D_\nabla = q^{-1}\nabla + (1 - q^{-1})\iota_\xi\nabla$ is the $q$-deformed covariant derivative.
<!-- FILE_END: categorical-action-notation.md -->

<!-- FILE_START: categorical-action-notation-su2.md -->
For $A = \mathcal{O}(\mathrm{SU}(2))$ with Haar integral $\int_A = \int_G$, connection $\nabla f = df + \mathcal{A} \cdot f$, and state $\psi \in A$:

1. **Categorical trace:** $\mathrm{tr}(T) = \sum_m \langle j,m \mid T \mid j,m \rangle$ is the usual matrix trace.
2. **Frobenius--Ricci:** $R_{\int}$ measures curvature of the Haar integral itself. On $\mathrm{SU}(2)$, $R_{\int} = 0$ in the classical limit $q = 1$.
3. **Adjoint section:** For $\psi \colon \mathbb{C} \to A$, the adjoint is $\psi^*(f) = \int_G \overline{\psi(g)}f(g)dg$.
4. **$q$-deformed derivative:** At $q = 1$, $D_\nabla = \nabla$. For $q \neq 1$, the Reeb component couples the connection to the contact geometry.
<!-- FILE_END: categorical-action-notation-su2.md -->

<!-- FILE_START: qou-canonical-action.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe equipped with connection $\nabla$, substrate parameter $q$, $q$-Hodge star $\star_q$, and state $\psi \colon \mathbf{1} \to A$. Then $(\mathbf{C}, A, \tau)$ determines a categorical action, unique up to a scalar $\lambda \in R^{\times}$:

$$
  \mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q),
$$

where $\mathcal{L}_q = \mathcal{L}_q(\nabla, \psi)$ is the categorical Lagrangian. The square of the Dirac operator decomposes as:

$$
  \mathcal{D}_\nabla^{2} = q \cdot R_{\int} + \mathrm{tr}_A\!\bigl(F_\nabla \wedge_q \star_q F_\nabla\bigr).
$$

Applying the categorical trace term by term yields the gravity $+$ gauge $+$ matter decomposition:

$$
  \mathfrak{S}_q = 
  \underbrace{\int_A \mathrm{tr}_A\bigl(q \cdot R_{\int}\bigr)}_{\text{gravity}} + 
  \underbrace{\int_A \mathrm{tr}_A\bigl(F_\nabla \wedge_q \star_q F_\nabla\bigr)}_{\text{gauge}} + 
  \underbrace{\int_A\!\bigl(\psi^* \cdot \mathcal{D}_\nabla\psi\bigr)}_{\text{matter}}.
$$

The categorical trace factors as $\mathrm{tr} = \int_A \circ \mathrm{tr}_A$, so all three summands share the same integration. The gauge term forms the Yang--Mills curvature integral. The action $\mathfrak{S}_q$ acts as the analogue of Hamilton's classical $S = \int L\,\mathrm{d}t$, with $\int_A$ replacing integration over spacetime and $\mathcal{L}_q$ replacing the Lagrangian density. The single scalar $\lambda$ tracks the normalization of the Frobenius form $\int_A$, corresponding to the freedom in choosing physical units.
<!-- FILE_END: qou-canonical-action.md -->

<!-- FILE_START: canonical-action-obstruction.md -->
The observability axiom $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ensures that the trace $\mathrm{tr} \colon \mathrm{End}(A) \to R$ is faithful. No endomorphism is invisible to integration. Relaxing this condition allows hidden symmetries and introduces a nontrivial kernel in the trace. The obstruction to recovering a well-defined action is classified by the cohomology class $\kappa \in H^2(\mathcal{S}, \mathcal{B})$ that obstructs lifting in the Yekutieli sense.
<!-- FILE_END: canonical-action-obstruction.md -->

