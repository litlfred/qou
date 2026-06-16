**Proposition (single-generator Hecke polynomial reduction).**
*Let $\sigma_i$ be a Hecke generator, satisfying the quadratic relation
$\sigma_i^2 = (q - q^{-1})\,\sigma_i + 1$. For any finite list of scalars
$d_1, \dots, d_r \in R$, the product of single-generator factors collapses
to an $R$-linear combination of $\sigma_i$ and the identity,*

$$
  \prod_{j=1}^{r} \bigl(\sigma_i + d_j\,1\bigr) \;=\; \alpha\,\sigma_i + \beta\,1,
$$

*where $(\alpha, \beta)$ is given by the division-free recursion*

$$
  (\alpha,\beta)_{\varnothing} = (0,\,1),
  \qquad
  (\alpha,\beta)_{d\,::\,\mathrm{ds}}
    = \bigl(\alpha'\,(h + d) + \beta',\;\; \alpha' + \beta'\,d\bigr),
$$

*with $h = q - q^{-1}$ and $(\alpha',\beta')$ the coefficients for the
tail $\mathrm{ds}$.*

## Proof

By induction on the list. The empty product is $1 = 0\cdot\sigma_i + 1\cdot 1$.
For the step, suppose $\prod_{\mathrm{ds}} = \alpha'\,\sigma_i + \beta'\,1$.
Then
$$
\begin{aligned}
(\sigma_i + d\,1)\,(\alpha'\,\sigma_i + \beta'\,1)
  &= \alpha'\,\sigma_i^2 + (\beta' + d\,\alpha')\,\sigma_i + d\,\beta'\,1 \\
  &= \alpha'\,\bigl((q-q^{-1})\sigma_i + 1\bigr) + (\beta' + d\,\alpha')\,\sigma_i + d\,\beta'\,1 \\
  &= \bigl(\alpha'(h + d) + \beta'\bigr)\,\sigma_i + \bigl(\alpha' + \beta'\,d\bigr)\,1,
\end{aligned}
$$
using the quadratic relation in the second line. This is exactly
$(\alpha,\beta)_{d\,::\,\mathrm{ds}}$. $\qquad\blacksquare$

This is the Cayley–Hamilton reduction for the rank-one quadratic that
every Hecke generator satisfies: since $\sigma_i$ annihilates
$(x - q)(x + q^{-1})$, any polynomial in $\sigma_i$ alone is congruent to a
linear remainder $\alpha\,\sigma_i + \beta\,1$ modulo that quadratic. The
recursion is purely ring-theoretic, holding over any commutative base ring
$R$ with no archimedean or invertibility hypothesis. (The closed eigenvalue
form $\alpha = (E_1 - E_2)/(q + q^{-1})$, $E_1 = \prod_j (q + d_j)$,
$E_2 = \prod_j (-q^{-1} + d_j)$ used for numerical speed is a corollary that
does require $q + q^{-1}$ to be invertible.)

## Consequence for the Markov trace

In a seminormal (Gelfand–Zetlin) representation the diagonal entry of
$\alpha\,\sigma_i + \beta\,1$ on a two-box block depends only on the
content gap $\delta'$ of the two boxes added at that step, through the
eigenvalue $D(\delta')$ of $\sigma_i$. Hence whenever a braid word has a
**monotone** generator sequence — as the multi-nucleon atom word
$\beta_{\mathrm{atom}}$ does, each nucleon contributing
$\sigma_{3k}, \sigma_{3k+1}$ and one interface crossing $\sigma_{3k+2}$
without revisiting a generator — every per-generator operator $O_g$ is a
single-generator polynomial, and its seminormal diagonal is a single
$\alpha_g\,D(\delta'_g) + \beta_g$. The character then factorises as a sum
over Bratteli chains of a product of such local factors:
$$
  \chi^\lambda(\beta_{\mathrm{atom}})
   = \sum_{\varnothing = s_0 \subset s_1 \subset \cdots \subset s_n = \lambda}
       \ \prod_g \bigl(\alpha_g\,D(\delta'_g) + \beta_g\bigr),
$$
a transfer matrix over the Young lattice that never materialises the
$d_\lambda$-dimensional Hoefsmit representation. This is the mechanism by
which the canonical Markov trace
$\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$ scales to large
atoms (Steps 3 and 9b of the mass–binding chain): the per-block work drops
to a few field operations, removing the $n!$ wall of the per-basis-vector
evaluation.

## Lean formalization

The division-free reduction is formalised in
`QOU.Braiding.hecke_gen_poly_reduction`, proved by induction over the
factor list from the Hecke quadratic alone (the coefficient recursion is
`QOU.Braiding.heckeAB`). The transfer-matrix character built on it is
implemented and validated to the 50-digit floor in
`computations/chi_monotone_transfer.py`.
