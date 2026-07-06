The Hoefsmit seminormal form ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)) diagonalises the Iwahori--Hecke algebra $H_n(q)$ acting on $V^{\otimes n}$ along a tower of Young--Jucys--Murphy elements indexed by standard tableaux. At each step, a Hecke generator $\sigma_i$ splits a tableau-vector into two eigencomponents:

- The **symmetric** ($q$-eigen) component, corresponding to the tableau where boxes $i$ and $i+1$ lie in the same row.
- The **antisymmetric** ($-q^{-1}$-eigen) component, corresponding to the tableau where they lie in the same column.

This is structurally identical to Conway's recursive surreal construction.

## Statement

Let $\mathrm{Tab}(\lambda)$ denote the set of standard tableaux of shape $\lambda$. We view this as the vertex set of a tree $\mathcal{T}_n$ whose edges record the Young--Jucys--Murphy ordering. Let $\mathbf{No}_{= n}^{\mathrm{dy}}$ denote the set of dyadic surreals of birthday exactly $n$ (equivalently, sign sequences of length $n$).

**Cardinality note.** The number of two-rowed standard tableaux of size $n$ is $\binom{n}{\lfloor n/2 \rfloor}$. The number of dyadic surreals of birthday exactly $n$ is $2^n$. These counts do not match. The map below is an injective embedding, not a bijection of forests.

We establish a canonical injective embedding:

$$
  \Phi : \bigsqcup_{\lambda \vdash n,\, \ell(\lambda) \leq 2}
    \mathrm{Tab}(\lambda)
   \hookrightarrow
  \mathbf{No}_{\leq n}^{\mathrm{dy}}
$$

It maps to dyadic surreals of birthday $\leq n$ such that:

1. The empty tableau at $n = 0$ and the singleton tableau at $n = 1$ both map to the surreal $0$. For $n \geq 2$, the one-row tableau $(n)$ maps to a non-zero value determined by its sign sequence.
2. Each YJM-edge $t \to t'$ in the tableau forest corresponds to a unique sign-sequence extension $s \to s\!\cdot\! +$ (symmetric channel) or $s \to s\!\cdot\! -$ (antisymmetric channel). The sign sequence of a size-$n$ tableau has length $n - 1$.
3. The birthday $b(\Phi(t))$ is bounded by the length of the sign sequence (i.e., by $n - 1$). Surreals in the image are of birthday $\leq n - 1$. The complement of the image in $\mathbf{No}_{\leq n}^{\mathrm{dy}}$ consists of non-tableau dyadic rationals not reachable by YJM-extension from a two-rowed shape.

## Corollaries

This identification yields several immediate consequences:

1. **Sign-sequence braid invariant.** The invariant is well-defined and lives in $\mathbf{No}_{\leq c(\beta)}^{\mathrm{dy}}$ for a braid $\beta$ of crossing number $c(\beta)$.
2. **Birthday refines crossing number.** We have $b(\mathrm{surr}(\beta, t)) \leq c(\beta)$, with equality for reduced braids.
3. **Hoefsmit factorisation equals Conway construction.** The closed formula for $\rho_\lambda(\sigma_i)$ as a $2 \times 2$ matrix in YJM coordinates acts exactly as the recursive surreal recipe $x = \{x^- \mid x^+\}$. The eigenvalue ratio $q : -q^{-1}$ determines the position of $x$ between $x^-$ and $x^+$.
4. **Jones polynomial re-expression.** The Jones polynomial $J_K(q)$ evaluates as a weighted sum over surreal sign sequences rather than over tableaux. This exposes a previously-hidden combinatorial structure ([Jones polynomial birthday refinement](#conj:jones-birthday)).
5. **Knot complexity refinement.** Knot complexity acquires an ordinal-valued refinement. Knots of unbounded crossing number live at birthdays approaching $\omega$.

## Significance

This is the central observation of the appendix. We already use the Hoefsmit seminormal form as the algebraic-combinatorial backbone of the paper. It powers the mass formula, the $\mathcal{Q}$-value derivations, and the spectral decomposition on $\Sigma_g$. This proposition shows that the same backbone, viewed differently, acts as a literal instance of Conway's surreal-number construction.

The surreal lift of QOU does not impose a new structure. It provides a different language for what Hoefsmit already provides.
