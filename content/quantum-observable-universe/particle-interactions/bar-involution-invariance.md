**Proposition (conditional on [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production) and [`conj:crystal-graph-realization`](#conj:crystal-graph-realization)).**
*Let $\bar\cdot \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{Z}[q, q^{-1}]$
be the bar-involution sending $q \mapsto q^{-1}$ (the Dynkin-fold
involution on the $A_{n-1}$ Hecke algebra after Type-B folding;
\cite{kashiwara1991, khovanovlauda2009, brundankleshchev2009}).
Then:*

1. *(**Plancherel-weight invariance**) For every partition
 $\lambda \vdash n$ and every $q > 0$, the Plancherel weight
 satisfies $\overline{w_\lambda(q)} = w_\lambda(q)$, i.e.
 $w_\lambda(q^{-1}) = w_\lambda(q)$.*
2. *(**Transpose-pair equality**) $w_\lambda(q) = w_{\lambda^T}(q)$
 for every $\lambda \vdash n$, where $\lambda^T$ is the transpose
 partition (the Dynkin involution / chirality-reversal
 from [`conj:cpt-orbit-closure-density`](#conj:cpt-orbit-closure-density)).*
3. *(**Type-B-folded normal forms**) Any Hecke normal form $T_w$
 produced by the symmetric-crystal pair-production engine of
 [`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production)
 is bar-invariant: $\overline{T_w} = T_w$. Equivalently, the
 image of the folded crystal-step operator
 $(\tilde f_i, \tilde f_{\bar i})$ is fixed by the bar-involution.*

## Why this is a witness against hand-rolled CPT violations

The conditions $\overline{T_w} = T_w$ and
$w_\lambda(q^{-1}) = w_\lambda(q)$ are *necessary* consequences of
Type-B folding. Any normal form, mass formula, or LP cost vector
computed via the QOU pipeline must satisfy them; **failure of
either condition signals that the computation has snuck in a
chirality bias incompatible with the symmetric-crystal substrate**.

This block packages the invariance lemmas as a regression-test
witness — a structural cross-check that downstream Lean files in
`particle-interactions/` can call to certify that no hand-rolled
$\mathbb{Z}/2\mathbb{Z}$ CPT rule has been introduced.

## Proofs

**(1) Plancherel-weight invariance.** The Plancherel weight is
$w_\lambda(q) = \dim_q(V_\lambda)^2 / [n]_q!$ where the $q$-integer
is $[k]_q = (q^k - q^{-k})/(q - q^{-1})$. Direct calculation:

$$
  [k]_{q^{-1}}
  \;=\; \frac{q^{-k} - q^k}{q^{-1} - q}
  \;=\; \frac{-(q^k - q^{-k})}{-(q - q^{-1})}
  \;=\; [k]_q.
$$

So $[k]_q$ is bar-invariant on the nose. Since $\dim_q V_\lambda$
is a ratio of products of $q$-integers (hook formula), and
$[n]_q!$ is a product of $q$-integers, the entire Plancherel weight
is a quotient of bar-invariants, hence bar-invariant. $\square$

**(2) Transpose-pair equality.** Hook lengths are unchanged by
transpose: if $\lambda^T$ is obtained from $\lambda$ by swapping
rows and columns, then for every cell $x = (i, j) \in \lambda$
there is a corresponding cell $x^T = (j, i) \in \lambda^T$ with
$h_{\lambda^T}(x^T) = h_\lambda(x)$. Hence
$\prod_x [h(x)]_q$ is unchanged, $\dim_q V_\lambda = \dim_q V_{\lambda^T}$,
and squaring and dividing by $[n]_q!$ gives
$w_\lambda(q) = w_{\lambda^T}(q)$. $\square$

**(3) Type-B-folded normal forms.** This is the structural
content of the symmetric-crystal pair-production conjecture
([`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production)):
the folded operator pair $(\tilde f_i, \tilde f_{\bar i})$ produces
two descendants whose Hecke normal forms are bar-conjugates. Their
sum (the only object the engine emits, never a single descendant)
is therefore bar-invariant. Single-chirality outputs are
unreachable.

Steps (1) and (2) are unconditional; step (3) is conditional on
[`conj:symmetric-crystal-pair-production`](#conj:symmetric-crystal-pair-production)
and is registered as such in the Lean file (class-conditional, per
AGENTS.md §3b-cond).

## Worked example: $n = 3$

The three Wedderburn blocks $(3)$, $(2, 1)$, $(1, 1, 1)$ have
hook lengths

| $\lambda$ | hooks | $[\,h\,]_q$ products |
|---|---|---|
| $(3)$ | $3, 2, 1$ | $[3]_q [2]_q [1]_q$ |
| $(2, 1)$ | $3, 1, 1$ | $[3]_q [1]_q [1]_q$ |
| $(1, 1, 1)$ | $3, 2, 1$ | $[3]_q [2]_q [1]_q$ |

Transpose pairing $(3) \leftrightarrow (1, 1, 1)$ has identical
hook products $\to$ identical $\dim_q$ $\to$ identical $w_\lambda$, as
predicted by (2). The self-dual $(2, 1)$ has $\lambda = \lambda^T$
by definition.

Bar-invariance under $q \mapsto q^{-1}$ follows from $[k]_{q^{-1}} = [k]_q$
on every factor.

## Lean formalisation

[`bar-involution-invariance.lean`](bar-involution-invariance.lean)

- Defines `barInvolution : ℝ → ℝ → ℝ` as the substitution
 $q \mapsto q^{-1}$ on the multiplicative group $\mathbb{R}_{>0}$.
- Defines `qInteger` (the $q$-integer $[k]_q$) and proves
 `q_integer_bar_invariant`: $[k]_{q^{-1}} = [k]_q$ for $q > 0$.
- Defines the abstract Plancherel weight as a quotient of
 $q$-integer products and proves
 `plancherel_weight_bar_invariant` and
 `plancherel_weight_transpose_eq` (parts 1 and 2 above).
- Records part 3 as a conditional theorem under the class
 `SymmetricCrystalPairProduction n` (per AGENTS.md §3b-cond),
 citing the upstream conjecture.
