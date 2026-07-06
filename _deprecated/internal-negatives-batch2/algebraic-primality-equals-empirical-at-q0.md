## Statement

**Proposition 7 (algebraic primality $\Leftrightarrow$ empirical magic at $q_0$).**
*At substrate $q = q_0$, the framework's distinguished value
fixed by the categorical mass-formula CODATA match, the set of
algebraically-prime integers
([def:algebraic-primality](#def:algebraic-primality)) equals*

$$
  \bigl\{ n \in \mathbb{N}_{\geq 1} \,:\, n \text{ is algebraically prime at } q_0 \bigr\}
  \;=\;
  \{1,\; 2,\; 8,\; 20,\; 28,\; 50,\; 82,\; 126\}.
$$

## Status

**Conjecture** (AGENTS.md §3b axiom-class).

The "$1$" is **proved** ([prop:n-equals-1-vacuous-magic](#prop:n-equals-1-vacuous-magic))
— at every $q > 1$, including $q_0$, the integer $1$ is vacuously
algebraically prime.

The remaining set $\{2, 8, 20, 28, 50, 82, 126\}$ is the conjectural
$q_0$-specific prediction:

- **Forward direction** ($n \in \{2, 8, 20, 28, 50, 82, 126\}
  \Rightarrow n$ alg-prime at $q_0$):
  asserts that at the empirical magic numbers, the SDP optimum
  $\psi_n(q_0)$ has dynamical content not contained in any tensor
  product of smaller canonical states.
- **Reverse direction** ($n$ alg-prime at $q_0 \Rightarrow n \in
  \{1, 2, 8, 20, 28, 50, 82, 126\}$):
  asserts that no other integer $n$ achieves tensor-product
  irreducibility at $q_0$. This is the *exclusion* claim — every
  other $n$ has $\psi_n(q_0)$ expressible as a tensor product of
  smaller magic states.

## Partial proof — what's already discharged

The Lean module
[`QOU.Interactions.AlgebraicPrimality`](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/content/quantum-observable-universe/lean/QOU/Interactions/AlgebraicPrimality.lean)
factors the conjecture into per-$n$ assertions:

**Assembly theorem (proved).** If for each $n$ we have either an
`IsKnownMagic n q` or `IsKnownNotMagic n q` instance — depending on
whether $n$ lies on the empirical ladder — then
`MagicEqualsEmpirical` holds at $q$.

This reduces the conjecture to a **finite collection of per-$n$
checks**. The factor count: 8 magic-checks (one per ladder element)
plus a non-magic-check at every other $n$ in the relevant range.

**Discharged so far (proved unconditionally):**

| Per-$n$ assertion | Status | Lean term |
|---|---|---|
| `IsKnownMagic 1 q` | **proved** for every $q$ | `one_isKnownMagic q` |
| `IsKnownNotMagic 0 q` | **proved** for every $q$ | `zero_isKnownNotMagic q` |
| `not_prime_of_inTensorSpan` | **proved** for every $(n, q)$ | tautological from definition |

**Still axiomatic (conjectural per-$n$ axioms):**

| Per-$n$ assertion | Status | What's needed |
|---|---|---|
| `IsKnownMagic 2 q_0` | conjectural | $\psi_2(q_0) \neq \psi_1(q_0) \otimes \psi_1(q_0)$ |
| `IsKnownMagic 8 q_0` | conjectural | $\psi_8(q_0)$ irreducible against all decomps of 8 |
| `IsKnownMagic 20 q_0` | conjectural | $\psi_{20}(q_0)$ irreducible against all decomps of 20 |
| ... | conjectural | through 28, 50, 82, 126 |
| `IsKnownNotMagic n q_0`, $n \notin$ ladder | conjectural | $\psi_n(q_0)$ in some tensor span |

The proof status is: **1 of 8 forward-direction primalities
proved unconditionally**; the other 7 forward primalities and all
reverse-direction non-primalities require the SDP machinery.

The `not_prime_of_inTensorSpan` lemma converts each remaining
forward axiom into "show no admissible decomposition realises the
canonical state" — concrete, finite-search-space at fixed $n$.

## Falsification path

For each $n \in \{2, 3, 4, \ldots, 130\}$, compute $\psi_n(q_0)$
via the iterative brane-tower construction at $q_0$, then check
tensor-product irreducibility against all decompositions
$n = \sum n_i$ with $n_i \in \{1, 2, 8, 20, 28, 50, 82, 126\}$.

The conjecture predicts the alg-prime set is exactly $\{1, 2, 8,
20, 28, 50, 82, 126\}$. If any other $n$ turns out alg-prime at
$q_0$, the framework is refuted; if any of the listed magic numbers
fails alg-primality at $q_0$, the framework is also refuted.

## Equivalence to other conjectural characterisations

The conjecture is conjecturally equivalent to:

- [conj:homological-shell-condensation](#conj:homological-shell-condensation)
  — same set characterised via spectral-sequence collapse;
- The empirical proposition
  [prop:magic-numbers-from-q](#prop:magic-numbers-from-q) which
  observes the same set via the Hoefsmit-Wedderburn $\delta^2 \Phi$
  signal at $K \leq 10$.

All five characterisations should give the same magic ladder. Any
inconsistency among them would refute the framework.

## Why this is the cleanest formulation

The algebraic-primality definition has three structural advantages
over the previous conjectural characterisations:

1. **No empirical input in the definition itself.** The set of
   algebraically-prime integers is fully determined by the SDP /
   Hecke / tensor-product structure. The empirical match is a
   *separate* claim ($q = q_0$ specifically).

2. **No "n = 2 degeneracy" special clause.** The earlier concern
   that no self-conjugate partition of $2$ exists (empty
   distinct-odd-parts decomposition) is irrelevant: primality reads
   $\psi_2 \neq \psi_1 \otimes \psi_1$, which holds whenever the
   SDP at $n = 2$ produces a non-trivial bound state. The
   self-conjugacy of the dominant Young-diagram label is a
   *separate* algebraic property.

3. **Recursive but well-founded.** Primality at $n$ depends on
   $\psi_m$ for $m < n$, but the recursion bottoms out at $n = 1$
   via [prop:n-equals-1-vacuous-magic](#prop:n-equals-1-vacuous-magic).
   No infinite regress, no need for an external base.
