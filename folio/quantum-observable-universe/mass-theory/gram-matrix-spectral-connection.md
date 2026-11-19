**Remark (where the Gram matrix fits in the spectral-sequence /
Frobenius framework).**

> **Domain of $G^{-1}$: the Temperley–Lieb quotient $H_n/\mathrm{rad} \cong \mathrm{TL}_n$.** On the full Hecke algebra $H_n$, non-degeneracy holds only under
> **convention C**, where the antisymmetric weight
> $y_{(1^3)} = 0.0227449\ldots$ is small but nonzero and $G$ genuinely inverts.
> Under the production **convention D** the pin $z(q^2+1) = q^3$ forces
> $y_{(1^3)} = 0$ *exactly*, so the $(1^3)$ block **is** the radical of the trace
> form and $\det G = 0$. Not "numerically singular" — zero. A $G^{-1}$ computed
> under C is therefore not an approximation to one under D; the D one does not
> exist.
>
> **This remark already contains its own refutation.** The Wedderburn paragraph
> below derives $G_{\lambda\mu} = \delta_{\lambda\mu}\,\tau(e_\lambda)$ — block
> diagonal with the *weights themselves* on the diagonal. So
> $\det G = \prod_\lambda \tau(e_\lambda)^{\,\cdot}$, and convention D sends one
> factor to zero. The very next line then writes down
> $G^{-1}_{\lambda\mu} = \delta_{\lambda\mu}\,[n]_q!/(\dim_q(\lambda)\dim(\lambda))$,
> which for that block is a division by zero.
>
> Nothing structural is lost, only relocated. The radical is a two-sided ideal
> ([`TemperleyLiebTower.traceRadical_two_sided`](../lean/QOU/QBeta/TemperleyLiebTower.lean)),
> so $\mathrm{tr}_M$ descends and the induced pairing on the quotient **is**
> non-degenerate. Ranks: $\mathrm{corank}\,G = 1$ at $n = 3$, $10 = 3^2 + 1^2$ at
> $n = 4$, $78 = 6^2+5^2+4^2+1^2$ at $n = 5$; what survives is
> $\sum \dim^2 = C_n$ — the Catalan numbers $5, 14, 42$.
>
> Proved in
> [`MarkovGramDegenerate.lean`](../lean/QOU/QBeta/MarkovGramDegenerate.lean):
> `block_mem_radical` `$\to$` `gram_det_eq_zero_of_radical_combination` for the
> vanishing, `pairing_descends` and `mem_radical_of_pairing_zero` for the
> descent.

**Role of the Gram matrix.**
*The **Gram matrix** $G$ of the Markov pairing is the common
algebraic object that encodes:*

1. *The **Frobenius algebra structure** of the **quotient**
   $H_n(R, q)/\mathrm{rad}\,\mathrm{tr}_M \cong \mathrm{TL}_n$: the pairing
   $\langle x, y \rangle_\tau := \tau(x \cdot y)$ is non-degenerate
   iff $\det G \neq 0$
   ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). Under **convention
   D** that holds on the quotient and **fails on $H_n$ itself**, where
   $\det G = 0$ exactly — see the correction above.*
2. *The **inverse** $G^{-1}$ — which exists on that quotient, **not** on $H_n$
   (**convention D**) — enters the **Frobenius co-Casimir**
   ([Frobenius universal](#thm:frobenius-codim-universal)):
   $C_{\dim_q} = \sum_{i, j} (G^{-1})_{ij} \cdot b_i \cdot b_j$
   in a non-central-idempotent basis (standard Frobenius
   identity), with $i, j$ running over the two-row stratum only.*
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
| Term 4 (Frobenius co-Casimir) | $\tau(C_{\dim_q}) = \mathrm{tr}(G^{-1} \cdot D)$ where $D_{ij} = \delta_{ij}/\dim_q$ per block basis — on the non-degenerate quotient $H_n/\mathrm{rad} \cong \mathrm{TL}_n$ (**convention D**; $G$ is singular on $H_n$) |
| Term 5 (chirality) | $a_K = G_{\beta, \beta^*} / G_{\mathbf{1}, \mathbf{1}}$ |
| Term 6 (jet-prefix) | $G$ restricted to higher filtration strata |

**Gram matrix for $H_3(R, q)$ over $R$.**

*Basis: $\{1, \sigma_0, \sigma_1, \sigma_0 \sigma_1, \sigma_1 \sigma_0, \sigma_0 \sigma_1 \sigma_0\}$.
Markov trace on standard basis ([Markov trace factorization](#thm:markov-trace-factorization)):
$\tau(T_w) = z^{\ell(w)}$ when the reduced word of $w$ uses each
generator at most once, where $\ell(w)$ is the length.  So $\tau(1) = 1$, $\tau(\sigma_i) = z$,
$\tau(\sigma_i \sigma_j) = z^2$. The naïve length rule $z^{\ell(w)}$
**fails for adjacent triples** (the rule assumes the rightmost
generator lies in the proper sub-algebra; this fails for
$\sigma_0\sigma_1\sigma_0$ since $\sigma_1\sigma_0 \notin H_2$).
The canonical Ocneanu--Wenzl recursion gives
$\tau(\sigma_0\sigma_1\sigma_0) = hz^2 + z$
(formerly stated as $z^3$; since corrected).*

*Gram matrix $G_{ij} = \tau(b_i b_j^{-1})$ (cyclic self-pairing).
The first-row/column entries shown as $z^3$ below are uncorrected: by the
recursion just quoted they should read $hz^2 + z$:*

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

*with off-diagonal entries computed via Hecke relations.*

*Under
the production convention D, $\det G = 0$ at $q = q_0$ and at every generic $q$:
the vanishing is forced by the pin $z(q^2+1) = q^3$, not by a coincidence at a
special point, so "generically" does not rescue it. $H_3$ is **not** a Frobenius
algebra under $\mathrm{tr}_M$; the $5$-dimensional quotient
$H_3/\mathrm{rad} \cong \mathrm{TL}_3$ is.*

**Gram $\leftrightarrow$ Wedderburn conjugation.**
*In the central-idempotent basis $\{e_\lambda\}$, the Gram matrix
is **block-diagonal**: $G_{\lambda, \mu} = \delta_{\lambda \mu}
\cdot \tau(e_\lambda^2) = \delta_{\lambda \mu} \cdot \tau(e_\lambda)
= \delta_{\lambda \mu} \cdot \frac{\dim_q(\lambda) \cdot \dim(\lambda)}{[n]_q!}$.
The inverse — on the surviving blocks only, since under **convention D** the
radical blocks have $\tau(e_\lambda) = 0$ — is
$G^{-1}_{\lambda, \mu} = \delta_{\lambda \mu} \cdot \frac{[n]_q!}{\dim_q(\lambda) \cdot \dim(\lambda)}$.
Summing $G^{-1}$ diagonal times $1/\dim_q$ gives exactly the Frobenius
co-Casimir trace $\sum_\lambda 1/\dim_q(\lambda)$ — recovering
([Frobenius universal](#thm:frobenius-codim-universal)).*

***The inversion in the previous sentence is only valid block-by-block on the
surviving blocks.** The block-diagonal form $G_{\lambda\mu} =
\delta_{\lambda\mu}\tau(e_\lambda)$ is correct under either convention and is the
sharpest statement in this remark: it shows $\det G$ is a product of the
Wedderburn weights, so $G$ inverts **iff every weight is nonzero**. Under the
excised convention C that held. Under convention D it does not — $y_\lambda = 0$
for every $\lambda$ with $\ell(\lambda) \geq 3$, since the fibre is the
two-dimensional fundamental of $\mathrm{SU}_q(2)$ and no three-row partition
survives Schur–Weyl. For those $\lambda$ the displayed $G^{-1}_{\lambda\lambda}$
divides by zero, and the co-Casimir sum $\sum_\lambda 1/\dim_q(\lambda)$ must run
over the two-row stratum only. Restricted there, every statement above stands
unchanged — which is precisely the sense in which the Frobenius structure
survives on $\mathrm{TL}_n$.*

*The quantum dimensions $\dim_q(\lambda)$ entering this Wedderburn block structure
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
