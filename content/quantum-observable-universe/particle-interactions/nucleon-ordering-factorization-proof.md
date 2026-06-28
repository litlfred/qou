## Proof

**(i)** The Wedderburn--Artin theorem decomposes $H_3(q)$ into
three irreducible representations: symmetric ($\dim = 1$),
standard ($\dim = 2$), and alternating ($\dim = 1$).  On the
one-dimensional representations, the crossing operator
$c \cdot \sigma_i + d \cdot \mathbf{1}$ acts as a scalar:
$\lambda_{\mathrm{sym}} = cq + d$ (eigenvalue $q$) and
$\lambda_{\mathrm{alt}} = -cq^{-1} + d$ (eigenvalue $-q^{-1}$).
The product of scalars commutes, so $S(\pi)$ and $A(\pi)$ are
permutation-invariant.

**(ii)** On the standard representation, the crossing acts by
the $2 \times 2$ transfer matrix
$T^{\mathrm{std}}(c, d) = \bigl(\begin{smallmatrix}
c(q - q^{-1}) + d & c \\ c & d
\end{smallmatrix}\bigr)$.
This follows from the Hecke relation $T^2 = (q - q^{-1})T + 1$
restricted to the $2$-dimensional standard representation, where
$T$ has eigenvalues $q$ and $-q^{-1}$ with trace $q - q^{-1}$.

**(iii)** The confinement theorem proves that $\mathcal{B}_3$
(Borromean braid) is the unique braid-realizable minimum of the
Markov trace among length $\leq 6$ braid words.  The nucleon NF
is stable under further Gröbner--Shirshov reduction — no rule
in the GS basis applies to a reduced nucleon word.  This stability
is exactly the jet-descended property: the nucleon contribution to
the transfer matrix is fixed, independent of the nuclear context.
Precomputing $T_\mathfrak{p}^{\mathrm{std}}$ and
$T_\mathfrak{n}^{\mathrm{std}}$ is justified by this stability.

**(iv)** The jet-stratified reduction algorithm partitions
$S$-polynomial pairs into descended $\times$ descended (already
resolved) and transient (requiring verification).  At the nuclear
level:
- Descended $\times$ descended = intra-nucleon reductions (cached)
- Transient = inter-nucleon crossings (simple $2 \times 2$ matrices)
- Mixed = cross-terms (resolved by the final pass of Algorithm 3
  in [jet-stratified-reduction](#unital-groebner-bases:prop:jet-stratified-reduction))

The inter-nucleon crossing matrices follow from the crossing
conventions:
$\mathfrak{p}\mathfrak{p}$: $\sigma_0$ ($c = 1, d = 0$),
$\mathfrak{n}\mathfrak{n}$: $\sigma_0^{-1}$ ($c = 1, d = -(q - q^{-1})$),
$\mathfrak{p}\mathfrak{n}$: $\tfrac{1}{2}(\sigma_0 + \sigma_0^{-1})$
($c = 1, d = -\tfrac{1}{2}(q - q^{-1})$).  $\square$

## Computational consequence

The ground-state ordering search for $\mathcal{N}(Z, N)$ tests
$\binom{A}{Z}$ nucleon permutations.  For each permutation:

| Component | Cost (original) | Cost (factorized) |
|-----------|----------------|-------------------|
| Symmetric channel | $O(K)$ scalar mults | **Precomputed** (ordering-independent) |
| Alternating channel | $O(K)$ scalar mults | **Precomputed** (ordering-independent) |
| Standard channel | $O(K)$ $\times$ 6 ops per crossing | $O(A^2)$ $\times$ 4 ops per $2 \times 2$ mult |
| Nucleon-internal | $O(n_p A)$ crossings ($n_p \approx 11$) | **Precomputed** ($T_\mathfrak{p}, T_\mathfrak{n}$ cached) |

**Effective speedup factors:**

1. **Channel elimination**: Symmetric and alternating products
   computed once per $(Z, N)$, not per ordering.  Saves $2/3$ of
   per-crossing work.

2. **Nucleon precomputation**: Each nucleon contributes $n_p$
   crossings to the chain.  With precomputed $T_\mathfrak{p}$ and
   $T_\mathfrak{n}$, these collapse to a single $2 \times 2$
   matrix per nucleon per generator.

3. **$2 \times 2$ vs $6 \times 6$**: The standard-channel matrix
   multiply is $O(4)$ instead of $O(36)$ per crossing.

Combined: the ordering search cost drops from
$\binom{A}{Z} \times O(A^2) \times O(36)$ to
$\binom{A}{Z} \times O(A^2) \times O(4)$, a **$\sim 9 \times$
reduction per ordering** plus elimination of redundant channel
computation.

## Compact nucleon notation

The factorization suggests a natural **nucleon-level alphabet**:

$$
  \mathfrak{p}
  \;\longleftrightarrow\;
  (T_\mathfrak{p}^{\mathrm{std}},\; s_\mathfrak{p},\; a_\mathfrak{p})
  \in \mathbb{R}^{2 \times 2} \times \mathbb{R} \times \mathbb{R}
$$

$$
  \mathfrak{n}
  \;\longleftrightarrow\;
  (T_\mathfrak{n}^{\mathrm{std}},\; s_\mathfrak{n},\; a_\mathfrak{n})
  \in \mathbb{R}^{2 \times 2} \times \mathbb{R} \times \mathbb{R}
$$

A nucleus $\mathcal{N}(Z, N)$ with ordering $\pi$ is written:

$$
  \mathcal{N}(\pi)
  =
  \mathfrak{t}_1 \cdot \mathfrak{t}_2 \cdots \mathfrak{t}_A
$$

where each $\mathfrak{t}_k \in \{\mathfrak{p}, \mathfrak{n}\}$ and
inter-nucleon crossings are encoded in the multiplication rule.
The full $H_3(q)$ normal form is recovered by evaluating the
$2 \times 2$ product and combining with the precomputed scalar
channels.

This is the **hadronic Hecke alphabet**: six NF coefficients per
nucleon collapse to a $2 \times 2$ matrix (4 numbers) in the
standard channel, plus two precomputed scalars.  For
${}^{56}\mathrm{Fe}$: $6 \times 56 = 336$ NF coefficients reduce
to $56 \times (4 + 2) = 336$ hadronic parameters — no size
reduction, but the multiplication is $9\times$ faster and
$2/3$ of the per-ordering work vanishes.
