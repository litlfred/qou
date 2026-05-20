[Vertex operators factor through the exceptional divisor](#prop:vertex-is-exceptional-divisor)
asserts a general factorisation: every Hecke generator
$\sigma_i$ acting on the categorical state space is supported on
$\mathcal{S}_p$, and every braid word $\beta \in B_n$ has a
Markov-trace image inside the Reeb bundle $\mathcal{R}_p$.  The
*proof* is a structural statement about localisation; it does not
exhibit specific factorisations.  The
[six canonical knot operators](#prop:six-canonical-knot-operators)
proposition fills that gap: the six elements of $S_3$ — under the
projection $B_3 \to S_3$ — supply the **named geometric
instances** of the vertex-factorisation claim, each with a fully
explicit Reeb-flow trajectory and boundary permutation.

**One-to-one dictionary.**

| vertex-factorisation slot | named geometric instance |
|---|---|
| factorisation of $\sigma_1$ | $\sigma_1$ row of [six canonical knot operators](#prop:six-canonical-knot-operators) — two-strand spiral on $\{r, g\}$ with $b$ spectator, boundary $(rg)$ |
| factorisation of $\sigma_2$ | $\sigma_2$ row — symmetric two-strand spiral on $\{g, b\}$ with $r$ spectator, boundary $(gb)$ |
| factorisation of $\sigma_1\sigma_2\sigma_1$ | Garside row + [explicit closed-form](#rem:garside-flow-explicit-closed-form) — three-stage compound flow with green displacement carrier, boundary $(rb)$ |
| factorisation of $\sigma_1\sigma_2$ | 3-cycle$_+$ row — global vortex with $k = +1$ uniformly, boundary $(rgb)$ |
| factorisation of $\sigma_2\sigma_1$ | 3-cycle$_-$ row — opposite-chirality global vortex, boundary $(rbg)$ |
| trivial factorisation (identity) | identity row — three parallel meridians |

**What this gives the rest of the section.**  The
Markov-trace-product theorem
([product factorization of the Markov trace](#thm:markov-trace-product))
that follows now has six concrete worked cases against which to
sanity-check.  In particular: the Markov trace of a 3-cycle is
the trace on a torus knot, which by
[torus-knot zero volume via Reeb](#rem:torus-knot-zero-volume-via-reeb)
contributes zero hyperbolic volume; the Markov trace of the
Garside element is the trace on a non-torus braid whose
complement has a hyperbolic JSJ piece, per
[hyperbolic-knot positive volume via Reeb](#rem:hyperbolic-knot-positive-volume-via-reeb).
The vertex-factorisation claim is therefore not just structural —
it specialises to a verifiable geometric dictionary on a generating
set for the $S_3$ image of $B_3$, and the rest of the chapter
inherits that dictionary as the bridge between the algebraic
Hecke action and the JSJ-graded volume content.

**Limits of the bridge.**  The dictionary above is genuinely
exhaustive only for $S_3$.  Longer braid words in $B_n$ for
$n \geq 4$ produce knot trajectories that the six $S_3$
representatives only approximate locally; the general
factorisation in
[vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)
remains the working statement for those cases.  The six rows
above are the **base case** of an induction on braid-word
length, not a complete enumeration of braid trajectories.
