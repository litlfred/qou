*Proof.* Part 1 is the hexagon axiom for the braiding, solved for $c_{X \otimes Y, Z}$. The hexagon states that the two paths from $(X \otimes Y) \otimes Z$ to $Z \otimes (X \otimes Y)$ — cross the composite in one step, or cross its factors one at a time — agree. Reassociating gives the displayed identity.

Part 2 follows from part 1 together with naturality of the braiding. Apply part 1 to $c_{X, Y \otimes Z}$ to expand the same morphism in two ways: expanding first on the left factor gives $c_1 c_2 c_1$, expanding first on the right factor gives $c_2 c_1 c_2$. Naturality identifies the two expansions.

For part 3, read a word $w$ on three strands as a word in the adjacent transpositions $s_1, s_2$ of $S_3$, and let $P(w)$ be the set of pairs $\{i, j\}$ with $i < j$ whose order the underlying permutation reverses. There are three such pairs. The empty word reverses none, and a single letter reverses exactly one. Enumerating the four words of length two shows each reverses at most two, so $|P(w)| = 3$ forces the length of $w$ to be at least three. $\square$

## Lean structure

The formalization is [`pairwise-interaction-decomposition.lean`](pairwise-interaction-decomposition.lean).

Parts 1 and 2 are inherited from Mathlib's braided-category library: `composite_crossing_eq_two_elementary` is `braiding_tensor_left_hom`, and `triple_crossing_route_independent` is `yang_baxter`. The declaration `pairwise_interaction_decomposition` is their conjunction.

Part 3 is `three_crossings_needed`, proved by enumeration over $S_3$ from the two counting lemmas `crossedPairs_one` and `crossedPairs_two_lt_three`. All declarations are sorry-free and depend only on `propext`, `Classical.choice`, and `Quot.sound`.
