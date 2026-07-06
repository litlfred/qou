### Proof sketch

1. **Completeness.** The Rosso–Jones formula decomposes $J_{\tau(r,s)}(q) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$ into irreps of $H_r(q)$. Every irrep $\lambda$ is recoverable from the torus knot data by Möbius inversion on the power sums $\omega^s$. The self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ provides the required inner product. Thus, $\mathcal{E}_g$ spans the representation ring at each degree $\leq \lfloor 2g/(g-1) \rfloor$.

2. **Inductive chain construction.** We add each nucleon $k$ by extending the $2\!\times\!2$ chain matrices: $M_j \leftarrow M_j \cdot T_{j {}^j\!\bowtie_k k}(q)$ for existing positions $j < k$, and $M_{k-1} = T_{(k\!-\!1) {}^{k-1}\!\bowtie_k k}(q)$ for the new position. The Hecke reduction $\sigma^2 = (q - q^{-1})\sigma + 1$ acts strictly within each $2\!\times\!2$ chain. This demands zero Yang–Baxter steps and zero Hecke steps on the multi-generator element. The nuclear word $\mathcal{N}_{Z,N} = \prod_j (\mathfrak{w}^+_j \sigma_j + \mathfrak{w}^0_j)$ employs distinct generators, ensuring it remains in Gröbner--Shirshov normal form.

3. **Shell cancellation.** The parent and daughter nuclei share all chains except those traversing the converting nucleon. The log ratio $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}}) = \sum_j [\log_q \hat{V}_j^{\mathrm{dau}} - \log_q \hat{V}_j^{\mathrm{par}}]$ therefore accumulates contributions only from generators $j$ that explicitly interact with the converting nucleon.

4. **Pauli projection.** A fully occupied shell of $n$ fermions is completely antisymmetric. Under the Schur–Weyl decomposition of $H_3(q)$, the decay operator $T_{\beta\text{-decay}}(q)$ projects onto the alternating irrep $(1^3)$ via $e_{(1^3)} \cdot T_{\beta\text{-decay}}(q) \cdot e_{(1^3)}$. The symmetric and standard irreps cancel entirely in the fully occupied state.

5. **Tower termination.** The degree-$k$ tower knot $\tau(r, s^k)$ demands genus $(r-1)(s^k - 1)/2$. For $g = 4$: degree $1$ admits $4$ knots, degree $2$ admits $2$ knots ($\tau(2,9)$ and $\tau(3,4)$), and degree $3$ requires genus $\geq 13$. Consequently, the jet bundle over $\Sigma_4$ possesses exactly three non-zero levels ($k = 0, 1, 2$).

Degree-$1$ knots are already encoded in $\mathcal{Q}_{\mathrm{bare}}$ through distinct vertex weights ($\mathfrak{p} {}^i\!\oplus_j \mathfrak{p}$, $\mathfrak{n} {}^i\!\oplus_j \mathfrak{n}$, $\mathfrak{p} {}^i\!\oplus_j \mathfrak{n}$ — inter-particle Hopf links with crossing indices $i, j$), so $F = 1$ for shells $1$–$4$. The active correction comes from degree-$2$ knots only.

### Jet bundle structure

The knot operators form a **jet bundle over the exceptional divisor chain** of $\Sigma_g$. The jet index is the Gröbner--Shirshov class (the degree in the degree tower) of each torus knot.

See [Table 2](#tbl:spectral-decomposition-qvalue-table2-data).

The jet decomposition is exact and finite. This finiteness arises not from truncation, but from the finite dimensionality of the regular representation of $H_n(q)$ on $\Sigma_g$. Completeness follows from the self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones expansion. Every irrep of $H_n(q)$ is recoverable from the torus knot invariants. Consequently, the knots form a complete orthogonal basis under the Markov trace inner product.
