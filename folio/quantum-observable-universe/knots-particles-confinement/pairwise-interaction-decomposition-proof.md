*Proof.* Part 1 is the hexagon axiom for the braiding, solved for $c_{X \otimes Y, Z}$. The hexagon states that the two paths from $(X \otimes Y) \otimes Z$ to $Z \otimes (X \otimes Y)$ — cross the composite in one step, or cross its factors one at a time — agree. Reassociating gives the displayed identity.

Part 2 follows from part 1 together with naturality of the braiding. Apply part 1 to $c_{X, Y \otimes Z}$ to expand the same morphism in two ways: expanding first on the left factor gives $c_1 c_2 c_1$, expanding first on the right factor gives $c_2 c_1 c_2$. Naturality identifies the two expansions.

Part 3 rests on the locality of an elementary crossing. Read the word through its action on strand positions, so that $c_i$ acts as the transposition $s_i$ exchanging the adjacent positions $i$ and $i+1$, and say a pair $\{a, b\}$ with $a < b$ has *crossed* under a permutation $\sigma$ when $\sigma(b) < \sigma(a)$. Suppose $a < b$ have crossed under $s_i \sigma$ but not under $\sigma$. Writing $u = \sigma(a)$ and $v = \sigma(b)$, this says $u < v$ while $s_i(v) < s_i(u)$. Since $s_i$ exchanges only the adjacent positions $i$ and $i+1$ and fixes the order of every other pair, the only possibility is $u = i$ and $v = i+1$. As $\sigma$ is a bijection, at most one pair $\{a, b\}$ satisfies this. Hence one elementary crossing adds at most one pair to the crossed set.

The empty word crosses no pair, so induction on the length of $w$ gives $|P(w)| \le \ell$. If $P(w)$ is all of the $\binom{n}{2}$ pairs then $\binom{n}{2} \le \ell$. $\square$

## Logical dependencies of the three parts

The parts do not carry equal weight, and the difference matters to how the
proposition should be read.

| part | epistemic tier | rests on |
|---|---|---|
| 1. composite reduction | the hexagon axiom, solved for $c_{X \otimes Y, Z}$ | axiom of `BraidedCategory` |
| 2. route independence | theorem | hexagon + naturality of the braiding |
| 3. crossing count | theorem, proved here | the locality of an elementary crossing |

Part 1 rearranges an axiom rather than establishing anything new: the hexagon
identities are fields of the braided-category structure, so a composite object's
failure to contribute an interaction of its own is stipulated with the scaffold.
Part 2 is a genuine derivation, and a standard one — the Yang--Baxter equation
follows from the hexagons together with naturality. Part 3 is independent of
both and is the only part whose argument is not classical.

Neither part 1 nor part 2 is derivable from the remaining quantum-universe
axioms, nor from the observability conditions; the hexagon identities enter
only as part of the braided structure.

## Lean structure

The formalization is [`pairwise-interaction-decomposition.lean`](pairwise-interaction-decomposition.lean), namespace `QOU.Braiding`. The declaration `pairwise_interaction_decomposition` is the conjunction of all three parts, each proved separately.

Parts 1 and 2 are inherited from Mathlib's braided-category library: `composite_crossing_eq_two_elementary` is `braiding_tensor_left_hom`, and `triple_crossing_route_independent` is `yang_baxter`.

Part 3 is proved from scratch. The locality step is `AdjSwap.eq_of_reverses`, the per-letter bound is `card_crossedPairs_step`, the induction is `card_crossedPairs_le_length`, and the conclusion is `card_allPairs_le_length`; the pair count $|P| = \binom{n}{2}$ is `card_allPairs`. The three-strand instance is `three_crossings_needed`.

Every declaration depends only on `propext`, `Classical.choice`, and `Quot.sound`.
