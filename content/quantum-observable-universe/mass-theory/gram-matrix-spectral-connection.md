**Remark.**
*User question: where does the Gram matrix fit in the
spectral-sequence / Frobenius framework?*

**Role of the Gram matrix.**
*The **Gram matrix** $G$ of the Markov pairing is the common
algebraic object that encodes:*

1. *The **Frobenius algebra structure** of $H_n(R, q)$: the pairing
   $\langle x, y \rangle_\tau := \tau(x \cdot y)$ is non-degenerate
   iff $\det G \neq 0$
   ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).*
2. *The **inverse** $G^{-1}$ enters the **Frobenius co-Casimir**
   ([Frobenius universal](#thm:frobenius-codim-universal)):
   $C_{\dim_q} = \sum_{i, j} (G^{-1})_{ij} \cdot b_i \cdot b_j$
   in a non-central-idempotent basis (standard Frobenius
   identity).*
3. *The **spectral-sequence pairing**: each $E_\infty^{p, *}$ is
   paired with $\mathrm{tr}_M$ via the Gram matrix restricted to
   the stratum — so $E_\infty^{p, *}(T_w) \to R$ is really
   $T_w \mapsto G_{T_w, *}$ projected to the stratum.*
4. *The **knot-factor Frobenius pairing**
   ([knot factor Frobenius pairing](#conj:knot-factor-frobenius-pairing))
   computes $G_{\beta, \beta^*}$ for braid-mirror pairs — the
   chirality factor $a_K$ of Term 5 is a normalised Gram-matrix
   entry.*

**Gram matrix in the three derived terms.**

| term | Gram matrix role |
|---|---|
| Term 1 (descended) | $G_{T_w, \mathbf{1}} = \tau(T_w)$ — single matrix entry |
| Term 2, 3 (brane tower) | $G_{\sigma_i, \sigma_i} = \tau(\sigma_i^2) = hz + 1$; pair $G_{\sigma_i \sigma_j, \sigma_j \sigma_i}$ |
| Term 4 (Frobenius co-Casimir) | $\tau(C_{\dim_q}) = \mathrm{tr}(G^{-1} \cdot D)$ where $D_{ij} = \delta_{ij}/\dim_q$ per block basis |
| Term 5 (chirality) | $a_K = G_{\beta, \beta^*} / G_{\mathbf{1}, \mathbf{1}}$ |
| Term 6 (jet-prefix) | $G$ restricted to higher filtration strata |

**Gram matrix for $H_3(R, q)$ over $R$.**

*Basis: $\{1, \sigma_0, \sigma_1, \sigma_0 \sigma_1, \sigma_1 \sigma_0, \sigma_0 \sigma_1 \sigma_0\}$.
Markov trace on standard basis ([Markov trace factorization](#thm:markov-trace-factorization)):
$\tau(T_w) = z^{\ell(w)}$ for $w \in S_n$ reduced, where
$\ell(w)$ is the length.  So $\tau(1) = 1$, $\tau(\sigma_i) = z$,
$\tau(\sigma_i \sigma_j) = z^2$. The naïve length rule $z^{\ell(w)}$
**fails for adjacent triples** (the rule assumes the rightmost
generator lies in the proper sub-algebra; this fails for
$\sigma_0\sigma_1\sigma_0$ since $\sigma_1\sigma_0 \notin H_2$).
The canonical Ocneanu--Wenzl recursion gives
$\tau(\sigma_0\sigma_1\sigma_0) = hz^2 + z$
(formerly stated as $z^3$ in this block; corrected per
[Markov-bug audit](https://github.com/litlfred/qou/blob/main/docs/audits/-trm5-markov-bug.md)).*

*Gram matrix $G_{ij} = \tau(b_i b_j^{-1})$ (cyclic self-pairing).
The first-row/column entries below shown as $z^3$ are stale per
the Markov-bug fix and should read $hz^2 + z$:*

$$
  G \;=\;
  \begin{pmatrix}
    1 & z & z & z^2 & z^2 & z^3 \\
    z & 1 + hz & * & * & * & * \\
    z & * & 1 + hz & * & * & * \\
    z^2 & * & * & * & * & * \\
    z^2 & * & * & * & * & * \\
    z^3 & * & * & * & * & *
  \end{pmatrix},
$$

*with off-diagonal entries computed via Hecke relations.  At
$q = q_0$, $\det G \neq 0$ (generically), confirming the
Frobenius property.*

**Gram $\leftrightarrow$ Wedderburn conjugation.**
*In the central-idempotent basis $\{e_\lambda\}$, the Gram matrix
is **block-diagonal**: $G_{\lambda, \mu} = \delta_{\lambda \mu}
\cdot \tau(e_\lambda^2) = \delta_{\lambda \mu} \cdot \tau(e_\lambda)
= \delta_{\lambda \mu} \cdot \frac{\dim_q(\lambda) \cdot \dim(\lambda)}{[n]_q!}$.
The inverse is
$G^{-1}_{\lambda, \mu} = \delta_{\lambda \mu} \cdot \frac{[n]_q!}{\dim_q(\lambda) \cdot \dim(\lambda)}$.
Summing $G^{-1}$ diagonal times $1/\dim_q$ gives exactly the Frobenius
co-Casimir trace $\sum_\lambda 1/\dim_q(\lambda)$ — recovering
([Frobenius universal](#thm:frobenius-codim-universal)).*

*The quantum dimensions $\dim_q(\lambda)$ entering this block structure
are the Wedderburn-block face of the $q$-Laplacian spectral tower
([the $q$-Laplacian spectral tower](#prop:q-laplacian-spectral-tower)):
at a root of unity $q = e^{i\pi/\kappa}$ they truncate to the finite
Verlinde/ADE set, so the Gram matrix becomes finite block-diagonal
modular-tensor data there.*

**Gram-matrix rank and the spectral sequence.**

*The filtration $J^\bullet(q)$ induces a block structure on $G$:
entries $G_{ij}$ with $b_i \in J^p$ and $b_j \in J^{q}$ sit in
the $(p, q)$-block.  The filtered Gram matrix has **block-triangular**
shape in the standard basis (since $\tau(J^p \cdot J^q) \subset J^{p+q}$
generically), and its **diagonal blocks** $G^{(p)} :=
G|_{J^p/J^{p+1}}$ are the **pairings on $E_0^{p, *}$**.  The
spectral-sequence differentials $d_r$ are encoded in the
**off-diagonal** blocks of $G$ under filtered inversion.*

*So the Gram matrix is the **single algebraic object** whose
block structure generates the entire spectral sequence and its
mass-term identification.  Computing $G$ explicitly for $H_3(R, q)$
([spectral-sequence H3 explicit](#prop:spectral-sequence-h3-explicit))
is equivalent to computing all pages $E_r^{p, *}$.*
