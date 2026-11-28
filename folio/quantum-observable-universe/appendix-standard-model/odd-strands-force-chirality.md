**Proposition.** Label a state of $n$ strands by the subset $S \subseteq \{0,\dots,n-1\}$ it
carries, take matter to be the even part ($|S|$ even), and let the conjugate of $S$ be its
complement $S^c$, so that $y_{S^c} = -y_S$ for every traceless diagonal charge $y$. Then:

1. $|S^c|$ is even exactly when $|S|$ and $n$ have the same parity;
2. if $n$ is even, every matter state's conjugate is matter; if $n$ is odd, no matter state's
   conjugate is matter;
3. the matter part equals its conjugate exactly when $n$ is even;
4. if $n$ is even, $\sum_{|S| \text{ even}} f(y_S) = \sum_{|S| \text{ even}} f(-y_S)$ for every
   $f$, so every odd moment of the charges, the cubic anomaly included, vanishes with no
   cancellation condition: the matter is vector-like.

So chiral matter (no matter state whose conjugate is also matter) is equivalent to an odd
number of strands. The oddness used in
[`prop:even-strand-generation`](even-strand-generation.md) follows from chirality and is
not a separate input.

**Proof.** $|S^c| = n - |S|$, which gives 1. Item 2 follows from 1, and 3 from 2 together
with the test state $S = \varnothing$, whose conjugate has $n$ strands. For 4, reindex the
sum by $S \mapsto S^c$ using 3 and $y_{S^c} = -y_S$.

**What stays open.** Why matter is the even part rather than the odd part (the chirality
sign), and why $n = 5$ rather than another odd number. A single charge such as the
electric charge can still have a symmetric spectrum on chiral matter; chirality here is a
statement about states, not about one charge.

## Lean structure

`QOU.StandardModel.OddStrands`: `even_card_compl_iff`, `evenPart_dichotomy`,
`evenPart_image_compl_eq_iff`, `evenPart_vectorlike_of_even`,
`evenPart_odd_moment_zero`. Sorry-free, any $n$, any commutative ring.
