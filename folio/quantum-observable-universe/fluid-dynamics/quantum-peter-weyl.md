Let $(\mathbf{C}, A, \tau)$ define a [QOU](#def:quantum-observable-universe) with [aether parameter](#def:substrate-parameter) $q > 1$. Let $\{V_j\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$ denote the simple objects of $\mathbf{C}$ indexed by spin $j$, with categorical dimension $\dim(V_j) = 2j + 1$. For indices $-j \leq m, n \leq j$, define the **matrix coefficient**

$$
  D^j_{mn}
  = 
  (\mathrm{ev}_{V_j} \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes e^j_m \otimes (e^j_n)^\vee)
  \circ \mathrm{coev}_{V_j}
   \in  A,
$$

where $\{e^j_m\}$ forms an orthonormal basis of $\tau(V_j)$, and $\mathrm{ev}, \mathrm{coev}$ represent the rigid evaluation and coevaluation maps.

Then:

*(a) Orthogonality.* Under the [Frobenius pairing](#def:frobenius-pairing):

$$
  \int_A (D^j_{mn})^\dagger \cdot D^{j'}_{m'n'}
  = 
  \frac{\delta_{jj'}\delta_{mm'}\delta_{nn'}}{[2j+1]_q},
$$

where $[2j+1]_q$ is the quantum dimension.

*(b) Completeness.* The set $\{[2j+1]_q^{1/2}D^j_{mn}\}$ constitutes a complete orthonormal system over the Hilbert completion $L^2(A) = \overline{A}^{\int_A}$:

$$
  \sum_{j \geq 0} [2j+1]_q
  \sum_{m,n=-j}^{j} D^j_{mn} \otimes (D^j_{mn})^\dagger
  =  \mathrm{id}_A.
$$

*(c) $\Delta_q$-eigendecomposition.* Each coefficient $D^j_{mn}$ is an eigenfunction of $\Delta_q$ with eigenvalue $[j]_q[j+1]_q$ (the $q$-Casimir):

$$
  \Delta_qD^j_{mn} = [j]_q[j+1]_qD^j_{mn}.
$$

The dimension of the corresponding eigenspace evaluates exactly to $(2j+1)^2$.
