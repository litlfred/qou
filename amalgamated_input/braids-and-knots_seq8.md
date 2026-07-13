<!-- FILE_START: braid-involutions-intro.md -->
The braid group carries two canonical involutions: the twist-flip $\tau$ that swaps adjacent strands, and the $\rho$-conjugation that conjugates each generator by the half-twist. We record both involutions, exhibit the twist-flip on the trefoil holonomy, and connect the $\rho$-conjugation to the chirality pairing.
<!-- FILE_END: braid-involutions-intro.md -->

<!-- FILE_START: lagrange-resolvent-transform.md -->
Let $C_n$ act on an $n$-dimensional vector space $V$ with coordinates $x_0, \ldots, x_{n-1}$, and let $\zeta = e^{2\pi i/n}$. The **Lagrange resolvent transform** is the discrete Fourier transform on $C_n$:
$$
  w_k =  \frac{1}{\sqrt{n}}\sum_{j=0}^{n-1}\zeta^{kj}x_j,
  \qquad k \in \{0, \ldots, n-1\}.
$$
The cyclic permutation $\sigma \colon x_j \mapsto x_{j+1}$ acts diagonally: $\sigma(w_k) = \zeta^{-k} w_k$. This manifests the $C_n$ symmetry as a phase rotation of the Fourier modes. Any $C_n$-invariant polynomial constraint on the $x_j$ transforms to a constraint on $C_n$-equivariant products that pair conjugate modes $w_k$ and $w_{n-k}$.

For $n = 5$, the three power-sum constraints transform into a linear projection $w_0 = 0$, a Hermitian quadric $w_1 w_4 + w_2 w_3 = 0$, and a symmetric cubic $w_1^2 w_3 + w_4^2 w_2 + w_2^2 w_1 + w_3^2 w_4 = 0$.

**Mathematical Novelty:** Using a Discrete Fourier Transform to diagonalize a cyclic action is standard. However, explicitly formalizing the $n=5$ Bring-surface case with modular zeta-power reduction constitutes a non-trivial mathematical contribution.
<!-- FILE_END: lagrange-resolvent-transform.md -->

<!-- FILE_START: braid-twist-flip.md -->
Let $\mathbf{w}=(w_1,w_2,w_3,w_4)$ be a spectral resolvent tuple. The two involutions are the **twist**:
```tex
\begin{align}
  \sigma_1(\mathbf{w}) &= (w_2,w_1,w_4,w_3)
    \label{eq:braid-twist}\\[4pt]
  \sigma_2(\mathbf{w}) &= (w_4,w_3,w_2,w_1)
    &&\text{(\textbf{flip}).}
    \label{eq:braid-flip}
\end{align}
```
As $4\times 4$ permutation matrices, these are:
```tex
\begin{equation}\label{eq:perm-matrices}
  \sigma_1=\begin{pmatrix}
    0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0
  \end{pmatrix},\quad
  \sigma_2=\begin{pmatrix}
    0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0
  \end{pmatrix}.
\end{equation}
```
On the 4-tuple, these involutions generate the Klein four-group $V_4=\{\mathrm{id},\sigma_1,\sigma_2,\sigma_1\sigma_2\}$, with $\sigma_1\sigma_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$.
<!-- FILE_END: braid-twist-flip.md -->

<!-- FILE_START: holonomy-trefoil.md -->
Given a branched cover $\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$ with singular fibres at the critical values, we choose two loops $\gamma_1,\gamma_2$ in $\mathbb{P}^1(\mathbb{C})$ encircling distinct branch points. Parallel-transporting the spectral modes $w_k$ around these loops yields the holonomy operators:
```tex
\begin{equation}\label{eq:holonomy-generators}
  H_1=\sigma_1,\qquad H_2=\sigma_2.
\end{equation}
```
In the $\mathrm{SU}(2)$ embedding, these become:
$$
  H_1=\exp(T\varTheta e_1),\qquad H_2=\exp(T\varTheta e_2),
$$
with $T$ the geometric torsion scalar and $\varTheta$ a branch angle. The holonomy group provides a representation of $B_3$ inside $\mathrm{SU}(2)$.

The fundamental group of the trefoil-knot complement has the presentation $\langle x,y\mid xyx=yxy\rangle \cong B_3$. The mapping $x\mapsto H_1$, $y\mapsto H_2$ forms an isomorphism $\pi_1(S^3\setminus K_{3,2})\xrightarrow{ \sim } \langle H_1,H_2\rangle$. Thus, the monodromy group of the branched cover is exactly the trefoil-knot group.

The composite holonomy $H_1 H_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$ acts as the $3$-cycle $\alpha$ and satisfies $(H_1 H_2)^3=\mathrm{id}$ on $\mathrm{SO}(3)$.
<!-- FILE_END: holonomy-trefoil.md -->

<!-- FILE_START: rho-s3-holonomy-exposition.md -->
The representation $\rho \colon B_3 \to \mathrm{SU}(2)$ specifies the exact holonomy of the symmetric group $S_3$ acting on the branched cover $\mathcal{S} \to \mathbb{P}^1(\mathbb{C})$. It determines how the spectral Lagrange resolvents $w_k$ are physically permuted when transported around the branch points.

The chiral sheets of the geometry are defined by these spectral coordinates. The conjugate pairs $(w_1, w_4)$ and $(w_2, w_3)$ span two-dimensional eigenspaces of the cyclic action. They tile the four non-trivial modes into time-like and space-like sectors. The representation $\rho$ acts through two elementary operations:

1. **The $\alpha$ operator (twist).** The generator $\sigma_1$ swaps the conjugate pairs. In the $\mathrm{SU}(2)$ embedding, this is a rotation by $T\varTheta$ around the $e_1$ axis. Physically, $\alpha$ rotates the time-like pairs carrying the dynamical phase of the Reeb flow, leaving the overall chirality unchanged.
2. **The $\beta$ operator (flip).** The generator $\sigma_2$ reverses the full tuple. In $\mathrm{SU}(2)$, this is a rotation around $e_2$ that reflects the space-like axis. The flip exchanges the two chirality sectors, implementing the geometric equivalent of parity inversion.

Together, $\alpha$ and $\beta$ generate the Klein four-group $V_4$ acting on the resolvent tuple. Their composition $\alpha\beta$ is the $3$-cycle whose cube returns to the identity on $\mathrm{SO}(3)$. The full $S_3$ holonomy is generated by these rotations and reflections of the chiral sheets.

Whenever $\rho$ appears in braid-group representations or knot invariants, it acts physically by twisting the time-like modes and reflecting the space-like axis. This rotation-reflection on the chiral sheets is the physical content of the topological symmetry.
<!-- FILE_END: rho-s3-holonomy-exposition.md -->

