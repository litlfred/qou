The Iwahori–Hecke algebra $H_3(q)$ has three irreducible
representations indexed by partitions of $3$: the trivial (sym)
$\lambda = (3)$, the standard $\lambda = (2, 1)$, and the sign
(alt) $\lambda = (1, 1, 1)$
([three parameters Wedderburn](#prop:three-parameters-wedderburn)).
This proposition derives the per-channel vertex-volume formulas
used in [tower binding energy](#prop:tower-binding-energy) from
the explicit image of the Hecke generators under each irrep.

## Statement

**Proposition.**
*Let $T \in H_3(q)$ satisfy the Hecke relation
$(T - q)(T + q^{-1}) = 0$, with matrix form
$T = c \cdot \sigma + d \cdot \mathbf{1}$ where
$(c, d) \in \mathbb{Q}[q, q^{-1}]^2$.*

**(i) Symmetric channel.** *Under the trivial irrep
$\rho^{\mathrm{sym}}$, every generator $\sigma_i$ maps to the
scalar $q$.  Hence*

$$
  \rho^{\mathrm{sym}}(T) \;=\; c q + d
  \quad\text{and}\quad
  \hat{V}^{\mathrm{sym}}(q) \;=\; \prod_{j \in \mathrm{chain}}
    (c_j q + d_j).
$$

**(ii) Alternating channel.** *Under the sign irrep
$\rho^{\mathrm{alt}}$, every generator $\sigma_i$ maps to the
scalar $-q^{-1}$.  Hence*

$$
  \rho^{\mathrm{alt}}(T) \;=\; -c/q + d
  \quad\text{and}\quad
  \hat{V}^{\mathrm{alt}}(q) \;=\; \prod_{j \in \mathrm{chain}}
    (-c_j/q + d_j).
$$

**(iii) Standard channel.** *Under the $2$-dimensional standard
irrep $\rho^{\mathrm{std}}$ (with generators $\sigma_0, \sigma_1$
mapped to distinct $2 \times 2$ matrices satisfying the Hecke and
braid relations), the Markov trace $\mathrm{tr}_M$ of an element
$T = c \cdot \sigma + d \cdot \mathbf{1}$ in the transfer chain
reduces to*

$$
  \hat{V}^{\mathrm{std}}(q) \;=\; z \cdot a + b,
$$

*where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter and
$(a, b)$ are the linear and constant coefficients of the
$2 \times 2$ trace:
$\mathrm{tr}\,\rho^{\mathrm{std}}(T) = a \cdot (q - q^{-1}) + 2 b$
under the specific basis where $\sigma_i$ act as reflection
matrices in the $2$-dim representation.*

## Proof

**(i) Sym irrep.**  The trivial $1$-dim representation of $S_n$
has every transposition $s_i = (i, i+1)$ act as $+1$; its
$q$-deformation in $H_n(q)$ sends $\sigma_i \mapsto q$ (the
positive Hecke eigenvalue).  For any linear combination
$T = c \sigma_i + d \mathbf{1}$ we get
$\rho^{\mathrm{sym}}(T) = c q + d$.  For a product
$T_1 T_2 \cdots T_m$ of such elements (the transfer chain at a
given generator index), multiplicativity gives
$\rho^{\mathrm{sym}}(\prod T_j) = \prod (c_j q + d_j)$.

**(ii) Alt irrep.**  The sign $1$-dim representation sends each
transposition to $-1$; its $q$-deformation sends
$\sigma_i \mapsto -q^{-1}$ (the negative Hecke eigenvalue).  By
the same multiplicativity argument,
$\rho^{\mathrm{alt}}(T) = -c/q + d$ on a single $T$, and the
product form on a chain.

**(iii) Std irrep.**  The $2$-dim standard representation is
spanned by row vectors $v_1, v_2$ with

$$
  \rho^{\mathrm{std}}(\sigma_i) \;=\;
  \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix}
  \quad (\text{up to a choice of basis and gauge}),
$$

and $\rho^{\mathrm{std}}(\sigma_{i+1})$ is the related
reflection matrix.  For $T_j = c_j \sigma + d_j \mathbf{1}$,
$\rho^{\mathrm{std}}(T_j) = c_j \rho(\sigma) + d_j I$ has trace
$\mathrm{tr} = c_j (q - q^{-1}) + 2 d_j$.

The **Markov trace** on $H_n(q)$ descends from the Markov axiom
$\mathrm{tr}_M(x \cdot \sigma_{n-1}) = z \cdot \mathrm{tr}_M(x)$
and is the normalised character of $\rho^{\mathrm{std}}$ divided
by the $q$-dimension.  After the transfer-chain reduction (the
$2 \times 2$ product $\prod_j \rho^{\mathrm{std}}(T_j)$ collapses
to a row-eigenvector in the $z$-grading), the scalar
$\hat{V}^{\mathrm{std}} = \mathrm{tr}_M(\prod T_j)$ takes the form
$z \cdot a + b$ where $(a, b)$ are the accumulated
$(\mathrm{off\text{-}diagonal}, \mathrm{diagonal})$ coefficients.

Computational form: one recursion step per crossing $(c_j, d_j)$
updates $(a, b)$ via

$$
  (a_{\mathrm{new}}, b_{\mathrm{new}})
  \;=\;
  (a c_j (q - q^{-1}) + a d_j + b c_j,\; a c_j + b d_j).
$$

This is the standard Garside-staircase recursion implemented in
[`full-tower-mass.py::per_gen_volumes`](https://github.com/litlfred/qou/blob/claude/continue-hamdover-QGLMZ/folio-assistant/computations/full-tower-mass.py#L32)
and in the Rust port
[`h_a_tower::per_gen_volumes_ha`](https://github.com/litlfred/qou/blob/claude/continue-hamdover-QGLMZ/tools/hecke-engine/src/h_a_tower.rs). $\square$

## Verification

The eigenvalues $\rho^{\mathrm{sym}}(\sigma_i) = q$ and
$\rho^{\mathrm{alt}}(\sigma_i) = -q^{-1}$ are the two roots of the
Hecke relation $(T - q)(T + q^{-1}) = 0$.  They appear in the
spectral decomposition of every transposition's image and are the
unique one-dimensional irrep eigenvalues in any rank $n$ Hecke
algebra.  This fixes $\hat{V}^{\mathrm{sym}}$ and
$\hat{V}^{\mathrm{alt}}$ uniquely.

The standard $2$-dim irrep is specified up to basis transformation;
the particular matrix form above is the **Jones–Ocneanu reflection
basis** (Jones 1987, Ocneanu 1987) under which the Markov trace
takes the $z \cdot a + b$ form with $z$ the Markov parameter.

**Witness**: exact reproduction at $q_0$ verified to $10^{-12}$ via
`full-tower-mass.py` (symbolic) vs `h_a_tower::binding_ha` (Rust
numeric); 3 tests in `hecke-engine/src/h_a_tower.rs::tests` pass.
