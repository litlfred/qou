The Hoefsmit seminormal form
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form))
diagonalises the Iwahori--Hecke algebra $H_n(q)$ acting on
$V^{\otimes n}$ along a tower of Young--Jucys--Murphy elements
indexed by standard tableaux. At each step, a Hecke generator $\sigma_i$
splits a tableau-vector into two eigencomponents:

- the **symmetric** ($q$-eigen) component, corresponding to the
  tableau where boxes $i$ and $i+1$ lie in the same row;
- the **antisymmetric** ($-q^{-1}$-eigen) component, corresponding
  to the tableau where they lie in the same column.

This is structurally identical to Conway's recursive surreal
construction.

## Statement

Let $\mathrm{Tab}(\lambda)$ denote the set of standard tableaux of
shape $\lambda$, viewed as the vertex set of a tree $\mathcal{T}_n$
whose edges record the Young--Jucys--Murphy ordering. Let
$\mathbf{No}_{= n}^{\mathrm{dy}}$ denote the set of dyadic surreals
of birthday *exactly* $n$ (equivalently, sign sequences of length
$n$).

**Cardinality note.** The number of two-rowed standard tableaux of
size $n$ is $\binom{n}{\lfloor n/2 \rfloor}$; the number of
dyadic surreals of birthday exactly $n$ is $2^n$.  These counts do
not match (e.g., $n = 3$ gives $3$ tableaux versus $8$ surreals), so
the map below is an **injective embedding**, not a bijection of
forests.

There is a canonical injective embedding

$$
  \Phi : \bigsqcup_{\lambda \vdash n,\, \ell(\lambda) \leq 2}
    \mathrm{Tab}(\lambda)
   \hookrightarrow
  \mathbf{No}_{\leq n}^{\mathrm{dy}}
$$

(taking values in dyadic surreals of birthday $\leq n$) such that:

1. The empty tableau at $n = 0$ and the singleton tableau at
   $n = 1$ both map to the surreal $0$ (the singleton's sign
   sequence is empty, of length $n - 1 = 0$).  For $n \geq 2$ the
   one-row tableau $(n)$ maps to a non-zero value determined by
   its sign sequence (see item 2).
2. Each YJM-edge $t \to t'$ in the tableau forest corresponds to a
   unique sign-sequence extension $s \to s\!\cdot\! +$ (symmetric
   channel: new box in the top row) or $s \to s\!\cdot\! -$
   (antisymmetric channel: new box in the bottom row).  The sign
   sequence of a size-$n$ tableau has length $n - 1$ (no choice at
   the first box placement).
3. The birthday $b(\Phi(t))$ is bounded by the length of the
   sign sequence, i.e., by $n - 1$.  Surreals in the image are
   therefore of birthday $\leq n - 1$; the complement of the image
   in $\mathbf{No}_{\leq n}^{\mathrm{dy}}$ consists of
   "non-tableau" dyadic rationals not reachable by YJM-extension
   from a two-rowed shape.

## Consequences

This identification has several immediate consequences:

1. **Sign-sequence braid invariant** is well-defined and lives
   in $\mathbf{No}_{\leq c(\beta)}^{\mathrm{dy}}$ for braid $\beta$
   of crossing number $c(\beta)$.

2. **Birthday refines crossing number**:
   $b(\mathrm{surr}(\beta, t)) \leq c(\beta)$, with equality for
   reduced braids.

3. **Hoefsmit factorisation = Conway construction**: the closed
   formula for $\rho_\lambda(\sigma_i)$ as a $2 \times 2$ matrix
   in YJM coordinates is *exactly* the recursive surreal recipe
   $x = \{x^- \mid x^+\}$ with the eigenvalue ratio
   $q : -q^{-1}$ determining the position of $x$ between $x^-$
   and $x^+$.

4. **The Jones polynomial $J_K(q)$** can be re-expressed as a
   weighted sum over surreal sign sequences (rather than over
   tableaux), exposing a previously-hidden combinatorial
   structure
   ([Jones polynomial birthday refinement](#conj:jones-birthday)).

5. **Knot complexity** acquires an honest ordinal-valued
   refinement: knots of unbounded crossing number live at
   birthdays approaching $\omega$.

## Significance

This is the central observation of the appendix. The QOU paper
already uses the Hoefsmit seminormal form as its
algebraic-combinatorial backbone (it powers the mass formula,
the $\mathcal{Q}$-value derivations, the spectral decomposition
on $\Sigma_g$). What this proposition shows is that the same
backbone, viewed differently, is a literal instance of Conway's
surreal-number construction.

The surreal lift of QOU is therefore not a *new* structure
imposed on the paper; it is a different *language* for what
Hoefsmit already provides.
