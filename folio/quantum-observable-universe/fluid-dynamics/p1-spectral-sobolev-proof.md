**Proof of (a).**

The argument adapts the classical Rellich--Kondrachov
compactness theorem to the $q$-deformed setting.

*Step 1: Self-adjointness.*
$\Delta_q$ is formally self-adjoint with respect to
$\langle\cdot,\cdot\rangle_\varTheta$ by the
[Hodge--Laplacian relation](#rem:hodge-laplacian-relation):
$\langle \Delta_q\alpha, \beta\rangle_\varTheta
= \langle d_q\alpha, d_q\beta\rangle_\varTheta +
\langle \delta_q\alpha, \delta_q\beta\rangle_\varTheta
= \langle \alpha, \Delta_q\beta\rangle_\varTheta$.
This follows from the [Hodge--Laplacian relation](#rem:hodge-laplacian-relation).

*Step 2: Non-negativity.*
$\langle \Delta_q\alpha, \alpha\rangle_\varTheta
= \lVert d_q\alpha\rVert^2 + \lVert\delta_q\alpha\rVert^2
\geq 0$.
This is immediate from Step 1.

*Step 3: Eigenvalue computation.*
The [Kelvin dispersion derivation](#prop:kelvin-dispersion-derivation)
shows $\Delta_q(z^k) = -[k]_q^2z^k$ by direct computation of
the $q$-derivative $D_q(z^k) = [k]_qz^{k-1}$.
*Step 4: Completeness of eigenbasis.*
The eigenfunctions $\{z^k\}_{k \in \mathbb{Z}}$ form a complete
orthogonal system in $\overline{\Omega^1(A)}$.

This is the [quantum Peter--Weyl
theorem](#thm:quantum-peter-weyl), using
Tannaka--Krein reconstruction (the fibre functor $\tau$ gives
$A \cong \bigoplus_j \mathrm{End}(\tau(V_j))$, spanned by
matrix coefficients) and Schur's lemma.

*Step 5: Compact resolvent.*
Given completeness, the resolvent
$(\lambda - \Delta_q)^{-1}$ acts on the eigenbasis as
$(\lambda - \Delta_q)^{-1}(z^k) = (\lambda + [k]_q^2)^{-1}z^k$.
Since $[k]_q^2 \to \infty$ exponentially, the eigenvalues
$(\lambda + [k]_q^2)^{-1} \to 0$ super-exponentially, so the
resolvent is **trace-class** (and in particular compact):

$$
  \sum_{k=1}^\infty \frac{1}{|\lambda + [k]_q^2|}
   \leq 
  \sum_{k=1}^\infty \frac{1}{[k]_q^2}
   \leq 
  \frac{(q - q^{-1})^2q^2}{q^2 - 1}
   <  \infty,
$$

using $[k]_q \geq q^{k-1}/(q - q^{-1})$ for $k \geq 1$.

**Proof of (c): Sobolev embedding.**

For $v = \sum_k \hat{v}_kz^k$ with
$\lVert v \rVert_{H^1_q}^2
= \sum_k (1 + [k]_q^2)|\hat{v}_k|^2 < \infty$:

$$
  |v(s)|
   \leq 
  \sum_k |\hat{v}_k|
   \leq 
  \left(\sum_k \frac{1}{1+[k]_q^2}\right)^{1/2}
  \!\cdot\!
  \left(\sum_k (1+[k]_q^2)|\hat{v}_k|^2\right)^{1/2}
$$

by Cauchy--Schwarz. The first factor is $C_q$ (finite for
$q > 1$ since $[k]_q^{-2} = O(q^{-2k})$); the second is
$\lVert v \rVert_{H^1_q}$.
