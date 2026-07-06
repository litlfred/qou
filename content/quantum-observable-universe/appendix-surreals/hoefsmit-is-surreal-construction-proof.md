## Proof sketch

We build the Hoefsmit seminormal basis by inductively decomposing $V^{\otimes n}$ via the chain $H_1(q) \subset H_2(q) \subset \cdots \subset H_n(q)$. At each step $k$, every existing eigenvector $|t\rangle$ for $H_k(q)$ splits under $\sigma_k$ into two components:

- $a^+_t \cdot |t \cup \square_{k+1}^{\to}\rangle$ (extend tableau rightward; $q$-eigenvalue).
- $a^-_t \cdot |t \cup \square_{k+1}^{\downarrow}\rangle$ (extend tableau downward; $-q^{-1}$-eigenvalue).

Conway's surreal construction at stage $k$ takes each existing surreal $x$ with sign-sequence $s$ and produces exactly two new surreals. These are $x^+$ (insert $+$ at position $k+1$) and $x^-$ (insert $-$ at position $k+1$). The bijection $\Phi$ matches these two-fold splittings step-by-step.

The eigenvalue convention forces compatibility with sums. The decomposition of $\sigma_i$ into $q$-eigenspace and $-q^{-1}$-eigenspace matches Conway's $\{L \mid R\}$ pairing $L < x < R$.

For tableaux of shape $\lambda$ with $\ell(\lambda) \leq 2$, the restriction to the "first or second row" acts precisely as the $\mathrm{SU}(2)$ constraint. This limits Young diagrams to two-rowed shapes and yields the binary split required for the sign-sequence interpretation.

A full proof requires three formalizations:

- The YJM-tableau tree structure (in Mathlib: `Combinatorics.YoungTableau` plus a `successor` relation).
- Gonshor's sign-sequence-to-surreal map (currently open in Mathlib's `SetTheory.Game.Surreal` development).
- The eigenvalue conventions (Hoefsmit uses $q$ and $-q^{-1}$; Conway's construction uses left and right of midpoint).

The Lean stub axiomatizes the bijection ([sign sequence functor](#def:sign-sequence-of-braid)) pending these prerequisites.
