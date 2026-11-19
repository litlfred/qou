Let $(\mathbf{C}, A, \tau)$ define a [QOU](#def:quantum-observable-universe) carrying [aether parameter](#def:substrate-parameter) $q > 1$. Let $\Delta_q = d_q\delta_q + \delta_q d_q$ be the [$q$-Laplacian](#rem:q-laplacian-interpretation) operating on $\Omega^1(A)$, and let $\langle \cdot, \cdot \rangle_\varTheta$ supply the [Webster inner product](#rem:hodge-laplacian-relation).

Then:

*(a) Compact resolvent and discrete spectrum.* For any $\lambda \notin \mathrm{spec}(\Delta_q)$ the resolvent $(\lambda\mathrm{id} - \Delta_q)^{-1}$ is compact on the Hilbert completion $\overline{\Omega^1(A)}^{\langle\cdot,\cdot\rangle_\varTheta}$, so the spectrum is discrete: $\mathrm{spec}(\Delta_q) = \{\mu_k^{(q)}\}_{k \geq 0}$, ordered $0 \leq \mu_0^{(q)} \leq \mu_1^{(q)} \leq \cdots$, with $\mu_k^{(q)} \to \infty$.

*(b) Exponential eigenvalue growth.* The precise eigenvalues read

$$
  \mu_k^{(q)} = [k]_q^2,
  \qquad
  [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}},
$$

bounded tightly by

$$
  \frac{q^{2k}}{(q - q^{-1})^2}
   \leq 
  \mu_k^{(q)}
   \leq 
  \frac{q^{2k}}{(q - q^{-1})^2}
  \left(1 + q^{-4k}\right)
$$

for all $k \geq 1$. In particular, $\mu_k^{(q)} = \Theta(q^{2k})$, establishing strictly exponential growth in $k$.

*(c) Categorical Sobolev embedding.* Write $H^1_q(A) = \{v \in \Omega^1(A) : \lVert v \rVert_A^2 + \lVert d_q v \rVert_A^2 < \infty\}$ for the $q$-Sobolev space. $H^1_q(A)$ embeds continuously into the space of bounded 1-forms:

$$
  \lVert v \rVert_{L^\infty}
   \leq 
  C_q\lVert v \rVert_{H^1_q},
  \qquad
  C_q = \left(\sum_{k=1}^\infty [k]_q^{-2}\right)^{1/2}.
$$

The constant $C_q$ converges for all $q > 1$ because $[k]_q^{-2} = O(q^{-2k})$. In the one-dimensional classical limit ($q \to 1$), $[k]_q \to k$ and $C_q^2 \to \sum k^{-2} = \pi^2/6$. However, across the 3-dimensional state bundle $\mathcal{S}$, the growing eigenvalue multiplicities $(2j+1)^2$ force $C_q$ to diverge. The embedding fails in the classical 3D limit.
