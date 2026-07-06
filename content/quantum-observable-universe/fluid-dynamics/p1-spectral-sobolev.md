Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter) $q > 1$. Let
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

for all $k \geq 1$. In particular,
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
converges because $[k]_q^{-2} = O(q^{-2k})$). As $q \to 1$,
$[k]_q \to k$ and $C_q^2 \to \sum k^{-2} = \pi^2/6$ in the
1-dimensional case. On the 3-dimensional state bundle
$\mathcal{S}$, eigenvalue multiplicities $(2j+1)^2$ cause
$C_q$ to diverge — the embedding fails in the classical limit.
