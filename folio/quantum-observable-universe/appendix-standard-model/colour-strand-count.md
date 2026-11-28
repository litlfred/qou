**Proposition.** *Split the five strands into a colour block of size $k$ and a weak block of size $m$, $k + m = 5$. In a block of size $k \ge 1$, the conjugate of a single strand is its complement in the block, a $(k-1)$-strand state, so the fundamental layer is self-conjugate exactly when $k = 2$. Suppose:*

- *(C) the colour block is non-abelian and its fundamental is not self-conjugate: $k \ge 2$ and $k \ne 2$;*
- *(W) the weak block is non-abelian: $m \ge 2$.*

*Then $k = 3$ and $m = 2$. The split $3 + 2$ satisfies both conditions, and its weak fundamental is self-conjugate. Every other split fails one: $4+1$ and $5+0$ have an abelian weak block, $2+3$ has a self-conjugate colour fundamental, and $1+4$ has an abelian colour block.*

*Proof.* The complement of a $1$-subset of $\{1,\dots,k\}$ is a $(k-1)$-subset, and the layers agree exactly when $k - 1 = 1$, checked for $k = 1,\dots,5$. With $k \ge 3$, $m \ge 2$ and $k + m = 5$, the only solution is $(3,2)$. $\square$

**Scope.** This is the strand form of "the fundamental of $\mathrm{SU}(k)$ is self-conjugate only for $k = 2$". Conditions (C) and (W) are inputs, not derived from the braid or Bring structure. (C) is the complex-type requirement on colour; (W) asks for a weak doublet. Given them and five strands ([`prop:strand-count-from-bring`](strand-count-from-bring.md)), the $3 + 2$ split follows with no count chosen to match data.
