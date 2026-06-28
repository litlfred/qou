**Proposition.**
*In the Iwahori–Hecke algebra $H_n(q)$, the Jucys–Murphy
elements*

$$
  J_k \;=\; q^{1-k}\sum_{i < k} \sigma_{i,k},
  \qquad k = 1, 2, \ldots, n
$$

*generate a maximal commutative subalgebra. The elementary
symmetric polynomials*

$$
  P_\ell \;:=\; e_\ell(J_1, J_2, \ldots, J_n)
  \;\in\; Z\bigl(H_n(q)\bigr)
$$

*lie in the centre, and act on the Wedderburn block $V_\lambda$
($\lambda \vdash n$) as the scalar*

$$
  c_\ell(\lambda) \;=\; e_\ell\!\left(\{q^{2c(\square)} :
    \square \in \lambda\}\right)
$$

*where $c(\square) = j - i$ is the content of cell
$\square = (i,j)$.*

*Proof.*

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
  J_k |T\rangle = q^{2 c(\square_k(T))}\, |T\rangle
$$

where $\square_k(T)$ is the cell of $T$ containing $k$ and
$c(\square) = j - i$. (This is the Hoefsmit–Wenzl formula;
see Kassel 1995 §VI.6 for the $H_n(q)$ version.)

The seminormal basis decomposes $V_\lambda$ as a direct sum
over standard tableaux of shape $\lambda$. Symmetric polynomials
in $\{q^{2c(\square_k(T))} : k = 1, \ldots, n\}$ depend only on
the multiset of contents — which is the multiset
$\{c(\square) : \square \in \lambda\}$, *independent* of the
particular tableau $T$. Hence

$$
  P_\ell |T\rangle =
  e_\ell\!\left(\{q^{2c(\square)} : \square \in \lambda\}\right)
  |T\rangle
$$

acts as the same scalar $c_\ell(\lambda)$ on every $|T\rangle$
of shape $\lambda$.

By Schur's lemma (each $V_\lambda$ is irreducible), this is
the unique scalar action of the central element $P_\ell$ on
$V_\lambda$. $\square$

**Corollary (closed form for level-$\ell$ corrections).**
The level-$\ell$ correction to the QOU mass formula is the
$\tau$-extraction of $P_\ell$ restricted to height-$(\ell{+}1)$
partitions:

$$
  T^{(\ell)}(\varrho)
  \;=\; m_e \cdot \frac{
    \sum_{\lambda \vdash 3A,\, \mathrm{ht}(\lambda) = \ell+1}
      w_\lambda(q) \cdot c_\ell(\lambda)
  }{[3A]_q!}
$$

where $w_\lambda(q) = \dim_q(\lambda)^2 / [n]_q!$ is the
Wedderburn weight and $\mathrm{ht}(\lambda)$ is the number of
non-zero parts.

**Application: $\alpha_5$ derivation.** For
$\ell = 5$, ht=6, this gives

$$
  \alpha_5 \;=\; m_e \cdot \frac{
    \sum_{\lambda \vdash 3A,\, \mathrm{ht}(\lambda) = 6}
      w_\lambda(q) \cdot c_5(\lambda)
  }{[3A]_q!}
$$

a finite combinatorial sum over height-6 partitions of $3A$.
This is the **simplest closed-form ansatz** consistent with the
LP-dual characterisation of
`prop:mass-formula-iterative-lp-dual`;
it is *conjectural*, not implied by the central-element theorem.

**Empirical status.** The companion witness
[`alpha-5-jucys-murphy-central.witness.json`](computations/alpha/alpha-5-jucys-murphy-central.witness.json)
**refutes** this ansatz at $\ell = 5$: the relative spread of
the normalised quantity across $A \in \{2, 3, 4\}$ is
$\approx 482\%$ at $q_0$, and the spread is uniformly bad
across the entire physical regime $|q| \in (1, \varphi)$.
See [`docs/audits/2026-05-31-ck-exploratory-probes-removed.md`](../../../docs/audits/2026-05-31-ck-exploratory-probes-removed.md)
for the empirical-findings record. The structural framework
(Murphy 1992 + LP-dual extraction) is intact; the simplest
closed form is not.
