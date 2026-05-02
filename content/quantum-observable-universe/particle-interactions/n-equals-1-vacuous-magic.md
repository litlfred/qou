## Statement

**Proposition (vacuous primality at $n = 1$).**
*For every substrate $q > 1$, the integer $n = 1$ is algebraically
prime ([def:algebraic-primality](#def:algebraic-primality)).
Equivalently, the canonical state $\psi_1(q)$ is not in the closed
span of any non-trivial tensor product of canonical states indexed
by a decomposition $1 = n_1 + \cdots + n_k$ with $k \geq 2$ and
$n_i \geq 1$ — because no such decomposition exists.*

## Proof

The claim reduces to a vacuous-truth statement about positive-integer
decompositions.

1. Suppose, for contradiction, that a decomposition $1 = n_1 + n_2 +
   \cdots + n_k$ exists with $k \geq 2$ and $n_i \geq 1$ for all
   $i = 1, \ldots, k$.

2. Lower-bound the sum:
   $$
     \sum_{i=1}^{k} n_i \;\geq\; \sum_{i=1}^{k} 1 \;=\; k \;\geq\; 2.
   $$

3. By hypothesis $\sum_{i=1}^{k} n_i = 1$, so $1 \geq 2$.
   Contradiction.

4. Therefore no decomposition with $k \geq 2$ and all $n_i \geq 1$
   summing to $1$ exists.

5. The universal-quantifier statement
   "$\psi_1(q) \notin \overline{\mathrm{span}}\{\cdots\}$ for every
   such decomposition" ranges over the empty set of decompositions
   and is vacuously true.

Therefore $1$ is algebraically prime at every $q > 1$.
$\square$

## Remarks

- The proof uses only **elementary arithmetic** (positivity-induced
  lower bound for sum vs length). No SDP analysis, no Hecke-algebra
  machinery, no tensor-product manipulation.

- This is the **base case of the recursion** in
  [def:algebraic-primality](#def:algebraic-primality). Every
  primality check at $n \geq 2$ ultimately bottoms out at $n = 1$
  through repeated decomposition.

- The proposition holds **uniformly in $q$**: whatever SDP machinery
  is supplied for $\psi_n(q)$ at general $n$, the case $n = 1$
  always trivialises by structural impossibility of the decomposition.

- **Relation to the empirical "magic-1" question.** Empirical
  nuclear magic numbers start at $2$, so the framework's $n = 1$
  primality is sometimes glossed as "trivial" or "below the lowest
  shell closure." The proposition above clarifies that within the
  algebraic-primality framework, $n = 1$ is **strictly magic** —
  just for a *vacuous* reason. Including $1$ in the predicted magic
  set is consistent with the framework's definition; whether to
  display it alongside the empirical $\{2, 8, 20, 28, 50, 82, 126\}$
  is a presentation choice, not a mathematical claim.

## Lean formalisation

The Lean proof
[`one_isAlgebraicallyPrime`](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/content/quantum-observable-universe/lean/QOU/Interactions/AlgebraicPrimality.lean)
encodes the four steps above. The auxiliary lemma
`sum_ge_length_of_all_pos` is proved by list induction (base case:
empty list trivial; step case: sum of `a :: as` ≥ 1 + length of
`as`, by inductive hypothesis on the tail). The main theorem
combines `length ≥ 2` and `sum = 1` via `omega` to derive the
contradiction.

The proof contains **no `sorry`**.
