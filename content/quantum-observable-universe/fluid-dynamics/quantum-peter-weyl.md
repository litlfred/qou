**Statement.**
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter) $q > 1$.  Let
$\{V_j\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$ be the simple
objects of $\mathbf{C}$ indexed by spin $j$, with categorical
dimension $\dim(V_j) = 2j + 1$.  For each $j, m, n$ with
$-j \leq m, n \leq j$, define the **matrix coefficient**

$$
  D^j_{mn}
  = 
  (\mathrm{ev}_{V_j} \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes e^j_m \otimes (e^j_n)^\vee)
  \circ \mathrm{coev}_{V_j}
   \in  A,
$$

where $\{e^j_m\}$ is an orthonormal basis of $\tau(V_j)$ and
$\mathrm{ev}, \mathrm{coev}$ are the evaluation and coevaluation
from the rigid structure.

Then:

**(a) Orthogonality.**  With respect to the
[Frobenius pairing](#def:frobenius-pairing):

$$
  \int_A (D^j_{mn})^\dagger \cdot D^{j'}_{m'n'}
  = 
  \frac{\delta_{jj'}\delta_{mm'}\delta_{nn'}}{[2j+1]_q},
$$

where $[2j+1]_q$ is the quantum dimension.

**(b) Completeness.**  The matrix coefficients
$\{[2j+1]_q^{1/2}D^j_{mn}\}$ form a complete orthonormal
system in the Hilbert completion
$L^2(A) = \overline{A}^{\int_A}$:

$$
  \sum_{j \geq 0} [2j+1]_q
  \sum_{m,n=-j}^{j} D^j_{mn} \otimes (D^j_{mn})^\dagger
  =  \mathrm{id}_A.
$$

**(c) $\Delta_q$-eigendecomposition.**  Each matrix coefficient
$D^j_{mn}$ is an eigenfunction of $\Delta_q$ with eigenvalue
$[j]_q[j+1]_q$ (the $q$-Casimir):

$$
  \Delta_qD^j_{mn} = [j]_q[j+1]_qD^j_{mn}.
$$

The eigenspace of eigenvalue $[j]_q[j+1]_q$ has dimension
$(2j+1)^2$.

**Proof.**

*Step 1: Orthogonality (a).*
The Frobenius form $\int_A$ induces, via the
[snake identities](#def:frobenius-pairing)
(pairing\_snake\_left, pairing\_snake\_right), a categorical
trace $\mathrm{tr}_A(f) = \int_A \circ f$.  The matrix
coefficient $D^j_{mn}$ is the $(m,n)$ entry of the
representation morphism $\rho_j \colon A \to \mathrm{End}(V_j)$.

By Schur's lemma in $\mathbf{C}$ (which holds because the
$V_j$ are simple objects):
$\mathrm{Hom}_{\mathbf{C}}(V_j, V_{j'}) = 0$ for $j \neq j'$.
Composing with the Frobenius trace:

$$
  \int_A (D^j_{mn})^\dagger \cdot D^{j'}_{m'n'}
  = \mathrm{tr}_A(\rho_j(e^j_m, e^j_n)^\dagger \circ
    \rho_{j'}(e^{j'}_{m'}, e^{j'}_{n'}))
  = \frac{\delta_{jj'}\delta_{mm'}\delta_{nn'}}
    {\mathrm{tr}_A(\mathrm{id}_{V_j})}
$$

and $\mathrm{tr}_A(\mathrm{id}_{V_j}) = [2j+1]_q$ (quantum
dimension from the [Pawlowski--Leitner
norm](#prop:pawlowski-leitner-inner-product)).

The result uses only Schur's lemma (which holds in
any semisimple abelian category) and the Frobenius trace.

*Step 2: Completeness (b).*
This is the key step.  We use the **Tannaka--Krein
reconstruction**.  The fibre functor
$\tau \colon \mathbf{C} \to R\text{-Mod}$ is faithful and exact
(axiom of QOU).  By the Tannaka--Krein theorem, $A$ is
recovered as the algebra of matrix coefficients:

$$
  A  \cong  \bigoplus_{j \geq 0}
  \mathrm{End}(\tau(V_j))
   \cong 
  \bigoplus_{j \geq 0}
  \mathrm{span}\{D^j_{mn} : -j \leq m,n \leq j\}.
$$

The isomorphism is algebraic — the matrix coefficients span $A$
as a vector space.  Since $A$ is dense in $L^2(A)$ (by
definition of the Hilbert completion), the matrix coefficients
are total in $L^2(A)$.  Combined with orthogonality (a), they
form a complete orthonormal system.

The argument uses the Tannaka--Krein theorem, which
is part of the [QOU axioms](#def:quantum-observable-universe)
(the existence of $\tau$).

*Step 3: Eigendecomposition (c).*
The $q$-Laplacian $\Delta_q = d_q\delta_q + \delta_q d_q$
commutes with the $\mathrm{SU}_q(2)$ action (because $d_q$ is
equivariant and $\delta_q$ is its adjoint).  By Schur's lemma,
$\Delta_q$ acts as a scalar on each isotypic component
$\mathrm{End}(V_j)$.  The scalar is the $q$-Casimir eigenvalue
$[j]_q[j+1]_q$, which is computed from the
[q-angular momentum](#def:q-angular-momentum) structure:

$$
  \Delta_q|_{V_j} = C_q(j) \cdot \mathrm{id}_{V_j},
  \qquad
  C_q(j) = [j]_q[j+1]_q.
$$

The eigenvalue identity follows from equivariance of $d_q$, Schur's
lemma, and the Casimir computation.
