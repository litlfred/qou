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
