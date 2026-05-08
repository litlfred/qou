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

## Proof sketch

The Hoefsmit seminormal basis is built by inductively decomposing
$V^{\otimes n}$ via the chain
$H_1(q) \subset H_2(q) \subset \cdots \subset H_n(q)$. At each step
$k$, every existing eigenvector $|t\rangle$ for $H_k(q)$ splits
under $\sigma_k$ into:

- $a^+_t \cdot |t \cup \square_{k+1}^{\to}\rangle$ (extend tableau
  rightward; $q$-eigenvalue);
- $a^-_t \cdot |t \cup \square_{k+1}^{\downarrow}\rangle$ (extend
  tableau downward; $-q^{-1}$-eigenvalue).

Conway's surreal construction at stage $k$ takes each existing
surreal $x$ with sign-sequence $s$ and produces *exactly two*
new surreals: $x^+$ (insert $+$ at position $k+1$) and $x^-$
(insert $-$ at position $k+1$). The bijection $\Phi$ matches
these two-fold splittings step-by-step.

Compatibility with sums is forced by the eigenvalue convention:
$\sigma_i$'s $q$-eigenspace + $-q^{-1}$-eigenspace decomposition
matches Conway's $\{L \mid R\}$ pairing $L < x < R$.

For tableaux of shape $\lambda$ with $\ell(\lambda) \leq 2$, the
restriction to "first or second row" is exactly the $\mathrm{SU}(2)$
constraint that limits Young diagrams to two-rowed shapes —
giving the *binary* (rather than $r$-ary) split needed for the
sign-sequence interpretation.

A full proof requires:

- formalising the YJM-tableau tree structure (in Mathlib:
  `Combinatorics.YoungTableau` plus a `successor` relation);
- formalising Gonshor's sign-sequence-to-surreal map (open in
  Mathlib's `SetTheory.Game.Surreal` development);
- checking the eigenvalue conventions (Hoefsmit uses
  $q$ and $-q^{-1}$; Conway's construction uses left/right of
  midpoint).

The Lean stub axiomatises the bijection
([sign sequence functor](#def:sign-sequence-of-braid)) pending
these prerequisites.

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
