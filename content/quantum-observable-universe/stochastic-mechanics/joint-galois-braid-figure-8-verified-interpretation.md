**Remark (why the figure-8 case is structurally trivial, and what remains).**

### Why this case is structurally trivial

The verification works because **the bar and braid actions touch
disjoint structure**:

- Braid acts on the *cell* $e_{(2,2)} \in Z(H_4(q))$ — but by definition,
 since central idempotents are fixed by inner automorphisms.
- Bar acts on the *coefficient ring* $q$ and the *shape parameter*
 $\zeta_6 \in F^\times$ — but not on the cell.

**Trivial commutativity from disjoint action.** This verifies the
*easiest* case of the joint-action conjecture; the structurally
non-trivial case is **chiral pairs**, where bar swaps cells while
braid acts non-by definition on the swapped pair.

### What this verifies and what remains

**Verified**: $(\lambda, K) = ((2, 2), 4_1)$ — a self-conjugate cell.
By extension, any self-conjugate cell with a polylog argument in
$F^\times$ has by definition commuting bar $\times$ braid action.

**Remaining (open)**: chiral-pair cases, e.g.

- $(\lambda, K) = ((3) + (1, 1, 1), 3_1)$ — trefoil cell pair.
- $(\lambda, K) = ((3, 1) + (2, 1, 1), 4_1$-related$)$ — chiral-pair
 partition of 4.
- $(\lambda, K) = (\text{chiral hyperbolic}, 5_2)$ — non-trivial
 cell pair + hyperbolic geometry.

For the trefoil case ($n = 3$): bar takes $e_{(3)}$ to $e_{(1,1,1)}$;
braid $\sigma_1, \sigma_2$ act on the $(2, 1)$ standard rep
non-by definition but commute with central idempotent assignment.
**Verification possible by direct computation** but technical.

### Significance

**The joint-action conjecture
[`conj:joint-galois-braid-action`](#conj:joint-galois-braid-action)
is verified at the figure-8 row** — the canonical depth-2 row of
B1. The verification is structural (disjoint actions by definition
commute), not numerical. Combined with the figure-8 row's
theorem-level B1 status
([`prop:b1-figure-8-row-theorem`](#prop:b1-figure-8-row-theorem)):

> **The figure-8 row of the bi-filtration carries the full
> graded-Mikusiński structure as a theorem**: depth-2 inclusion,
> strong sharpness over $\mathbb{Q}(\zeta_6)$, joint Galois $\times$ braid
> commutativity, VC asymptotic match, depth correspondence
> verified.

Reduces remaining open questions about the joint action to *non-
self-conjugate / chiral-pair* cases.
