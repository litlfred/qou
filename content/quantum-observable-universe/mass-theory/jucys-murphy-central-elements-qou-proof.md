**Step 1: JM elements commute.**  $\sigma_{i,k}$ denotes the
braid transposition swapping strands $i,k$ in $H_n(q)$. The
relations

$$
  J_k J_\ell = J_\ell J_k \quad \forall k, \ell
$$

are a direct calculation from the braid relations of $H_n(q)$;
see Kassel (1995, §V.5) and Jucys (1974) for the
$q \to 1$ origin (this works in $\mathbb{C}[S_n]$). The commuting
subalgebra $\mathbb{C}\langle J_1,\ldots,J_n\rangle \subset
H_n(q)$ is the Gelfand–Tsetlin algebra.

**Step 2: Symmetric polynomials in JM elements are central.**
Murphy (1992; the $q$-deformation of Murphy 1981) showed that
the elementary symmetric polynomials
$P_\ell = e_\ell(J_1,\ldots,J_n)$ commute with every generator
$\sigma_i$ of $H_n(q)$:

$$
  \sigma_i P_\ell = P_\ell \sigma_i \quad \forall i, \ell.
$$

The proof is by induction on $\ell$: $P_1 = J_1 + \cdots + J_n
= \sum_{i < k} q^{1-k}\sigma_{i,k}$ is centralised by every
$\sigma_j$ (each $\sigma_j$ acts on the sum by permuting the
transpositions, fixing the symmetric sum). The higher $P_\ell$
are constructed from sums of products of $J_k$'s; their
$\sigma_j$-invariance follows from the same permutation
argument applied at the level of multi-index summations.

Hence $P_\ell \in Z(H_n(q))$ for all $1 \leq \ell \leq n$.

**Step 3: Spectrum on Wedderburn blocks.** The seminormal
basis $\{|T\rangle\}_T$ (T = standard Young tableau of shape
$\lambda$) diagonalises every $J_k$:

$$
  J_k |T\rangle = q^{2 c(
$\qquad\blacksquare$
