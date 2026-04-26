Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter) $q > 1$.  Let
$\Delta_q = d_q\delta_q + \delta_q d_q$ be the
[$q$-Laplacian](#rem:q-laplacian-interpretation) acting on
$\Omega^1(A)$, and let
$\langle \cdot, \cdot \rangle_\varTheta$ be the
[Webster inner product](#rem:hodge-laplacian-relation).

Then the following hold:

**(a) Compact resolvent and discrete spectrum.**
The operator $\Delta_q$ on $\Omega^1(A)$ has compact resolvent:
for any $\lambda \notin \mathrm{spec}(\Delta_q)$, the resolvent
$(\lambda\mathrm{id} - \Delta_q)^{-1}$ is a compact operator
on the Hilbert completion
$\overline{\Omega^1(A)}^{\langle\cdot,\cdot\rangle_\varTheta}$.
Consequently, the spectrum is discrete:
$\mathrm{spec}(\Delta_q) = \{\mu_k^{(q)}\}_{k \geq 0}$
with $0 \leq \mu_0^{(q)} \leq \mu_1^{(q)} \leq \cdots$ and
$\mu_k^{(q)} \to \infty$.

**(b) Exponential eigenvalue growth.**
The eigenvalues satisfy

$$
  \mu_k^{(q)} = [k]_q^2,
  \qquad
  [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}},
$$

with the growth bound

$$
  \frac{q^{2k}}{(q - q^{-1})^2}
   \leq 
  \mu_k^{(q)}
   \leq 
  \frac{q^{2k}}{(q - q^{-1})^2}
  \left(1 + q^{-4k}\right)
$$

for all $k \geq 1$.  In particular,
$\mu_k^{(q)} = \Theta(q^{2k})$ — exponential in $k$.

**(c) Categorical Sobolev embedding.**
Define the $q$-Sobolev space
$H^1_q(A) = \{v \in \Omega^1(A) :
\lVert v \rVert_A^2 + \lVert d_q v \rVert_A^2 < \infty\}$.
Then $H^1_q(A)$ embeds continuously into the space of bounded
1-forms:

$$
  \lVert v \rVert_{L^\infty}
   \leq 
  C_q\lVert v \rVert_{H^1_q},
  \qquad
  C_q = \left(\sum_{k=1}^\infty [k]_q^{-2}\right)^{1/2}.
$$

The constant $C_q$ is finite for all $q > 1$ (the series
converges because $[k]_q^{-2} = O(q^{-2k})$).  As $q \to 1$,
$[k]_q \to k$ and $C_q^2 \to \sum k^{-2} = \pi^2/6$ in the
1-dimensional case.  On the 3-dimensional state bundle
$\mathcal{S}$, eigenvalue multiplicities $(2j+1)^2$ cause
$C_q$ to diverge — the embedding fails in the classical limit.

**Proof of (a).**

The argument adapts the classical Rellich--Kondrachov
compactness theorem to the $q$-deformed setting.

*Step 1: Self-adjointness.*
$\Delta_q$ is formally self-adjoint with respect to
$\langle\cdot,\cdot\rangle_\varTheta$ by the
[Hodge--Laplacian relation](#rem:hodge-laplacian-relation):
$\langle \Delta_q\alpha, \beta\rangle_\varTheta
= \langle d_q\alpha, d_q\beta\rangle_\varTheta
+ \langle \delta_q\alpha, \delta_q\beta\rangle_\varTheta
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
resolvent is not merely compact but **trace-class**:

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

by Cauchy--Schwarz.  The first factor is $C_q$ (finite for
$q > 1$ since $[k]_q^{-2} = O(q^{-2k})$); the second is
$\lVert v \rVert_{H^1_q}$.
