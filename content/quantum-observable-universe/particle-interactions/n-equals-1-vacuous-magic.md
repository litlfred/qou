## Statement

**Proposition (vacuous primality at $n = 1$).**
*For every substrate $q > 1$, the integer $n = 1$ is algebraically
prime (def:algebraic-primality).
Equivalently, the canonical state $\psi_1(q)$ is not in the closed
span of any non-trivial tensor product of canonical states indexed
by a decomposition $1 = n_1 + \cdots + n_k$ with $k \geq 2$ and
$n_i \geq 1$ — because no such decomposition exists.*

## Remarks

- The proof uses only **elementary arithmetic** (positivity-induced
  lower bound for sum vs length). No SDP analysis, no Hecke-algebra
  machinery, no tensor-product manipulation.

- This is the **base case of the recursion** in
  def:algebraic-primality. Every
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
empty list trivial; step case: sum of `a :: as` $\ge$ 1 + length of
`as`, by inductive hypothesis on the tail). The main theorem
combines `length ≥ 2` and `sum = 1` via `omega` to derive the
contradiction.

The proof contains **no `sorry`**.
