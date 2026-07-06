**Proof.**

*Step 1: Orthogonality (a).*
The Frobenius form $\int_A$ induces a categorical trace $\mathrm{tr}_A(f) = \int_A \circ f$ via the [snake identities](#def:frobenius-pairing) (pairing\_snake\_left, pairing\_snake\_right). The matrix coefficient $D^j_{mn}$ is the $(m,n)$ entry of the representation morphism $\rho_j \colon A \to \mathrm{End}(V_j)$.

The $V_j$ are simple objects. Schur's lemma in $\mathbf{C}$ gives $\mathrm{Hom}_{\mathbf{C}}(V_j, V_{j'}) = 0$ for $j \neq j'$. Composing with the Frobenius trace yields

$$
  \int_A (D^j_{mn})^\dagger \cdot D^{j'}_{m'n'}
  = \mathrm{tr}_A(\rho_j(e^j_m, e^j_n)^\dagger \circ
    \rho_{j'}(e^{j'}_{m'}, e^{j'}_{n'}))
  = \frac{\delta_{jj'}\delta_{mm'}\delta_{nn'}}
    {\mathrm{tr}_A(\mathrm{id}_{V_j})}.
$$

The quantum dimension from the [Pawlowski--Leitner norm](#prop:pawlowski-leitner-inner-product) gives $\mathrm{tr}_A(\mathrm{id}_{V_j}) = [2j+1]_q$.
This result uses only the Frobenius trace and Schur's lemma (which holds in any semisimple abelian category).

*Step 2: Completeness (b).*
We use the Tannaka--Krein reconstruction. The fibre functor $\tau \colon \mathbf{C} \to R\text{-Mod}$ is faithful and exact (axiom of QOU). By the Tannaka--Krein theorem, $A$ is recovered as the algebra of matrix coefficients:

$$
  A  \cong  \bigoplus_{j \geq 0}
  \mathrm{End}(\tau(V_j))
   \cong 
  \bigoplus_{j \geq 0}
  \mathrm{span}\{D^j_{mn} : -j \leq m,n \leq j\}.
$$

The isomorphism is algebraic. The matrix coefficients span $A$ as a vector space. Since $A$ is dense in $L^2(A)$ (by definition of the Hilbert completion), the matrix coefficients are total in $L^2(A)$. Combined with orthogonality (a), they form a complete orthonormal system.
This step relies on the Tannaka--Krein theorem, which follows from the [QOU axioms](#def:quantum-observable-universe) (the existence of $\tau$).

*Step 3: Eigendecomposition (c).*
The $q$-Laplacian $\Delta_q = d_q\delta_q + \delta_q d_q$ commutes with the $\mathrm{SU}_q(2)$ action because $d_q$ is equivariant and $\delta_q$ is its adjoint. By Schur's lemma, $\Delta_q$ acts as a scalar on each isotypic component $\mathrm{End}(V_j)$. The scalar is the $q$-Casimir eigenvalue $[j]_q[j+1]_q$. This is computed from the [q-angular momentum](#def:q-angular-momentum) structure:

$$
  \Delta_q|_{V_j} = C_q(j) \cdot \mathrm{id}_{V_j},
  \qquad
  C_q(j) = [j]_q[j+1]_q.
$$

The eigenvalue identity follows from the equivariance of $d_q$, Schur's lemma, and the Casimir computation.
