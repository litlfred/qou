---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-011-42-estimates-for-the-number-of-factorizations
section_title: "Estimates for the number of factorizations"
section_number: 4.2
pages: 13-15
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
bound of the number of factorizations ofπ with a given value of the statistic
o(σ1, σ2).
Lemma 13. Let π, σ1, σ2 ∈ Sl be such that π = σ1σ2. There exist per-
mutations σ′
1, σ′
2 ∈ Sl such that π = σ′
1σ′
2, |σ′
1| + |σ′
2| = |σ1| + |σ2|,
|σ′
2| = |σ′
2σ−1
2 | + |σ2| and every cycle of σ′
1 is contained in some cycle
of σ′
2. Furthermore, |σ′
1| = o(σ1, σ2).
Proof. If every cycle of σ1 is contained in some cycle of σ2 then σ′
1 = σ1
and σ′
2 = σ2 have the required property.
Otherwise, there exist a, b ∈ { 1, . . . , n} such that a and b belong to the
same cycle of σ1 but not to the same cycle of σ2. We deﬁne σ′
1 = σ1(a, b),
σ′
2 = ( a, b)σ2. Notice that |σ′
1| = |σ1| − 1, |σ′
2| = |σ2| + 1, and the orbits
under the action of the subgroups ⟨σ1, σ2⟩ and ⟨σ′
1, σ′
2⟩ are the same.
We iterate this procedure if necessary (it will ﬁnish after a ﬁnite number
of steps because the length ofσ1 decreases in each step). It remains to prove
that |σ′
2| ≥ | σ′
2σ−1
2 | + |σ2| (the opposite inequality follows from the triangle
inequality): notice that |σ′
2| − | σ2| is equal to k (where k is the number of
steps after which the procedure has terminated) and σ′
2σ−1
2 is a product of k
transpositions, hence |σ′
2σ−1
2 | ≤ k.
Furthermore, as every cycle of σ′
1 is contained in some cycle of σ′
2, the
set of orbits of the group ⟨σ′
1, σ′
2⟩ is equal to C(σ′
2), so
o(σ1, σ2) = o(σ′
1, σ′
2) = l − |C(σ′
1)| = |σ′
1|. □
14 V ALENTIN FÉRAY AND PIOTR ´SNIADY
Lemma 14. For any integersl ≥ 1 and i ≥ 0 and for any π ∈ Sl
(19) #{σ ∈ Sl : |σ| = i} ≤ l2i
i! .
Proof. Since every permutation in Sl appears exactly once in the product
[1 + (12)][1 + (13) + (23)] · · ·[1 + (1l) + · · · + (l − 1, l)],
we have∑
i
xi #
{
σ ∈ Sl : |σ| = i
}
= (1 + x)(1 + 2x) · · ·
(
1 + (l − 1)x
)
.
Each of the coefﬁcients of xk on the right-hand side is bounded from above
by the corresponding coefﬁcient of exe2x · · · e(l−1)x = e
l(l−1)x
2 , ﬁnishing the
proof. □
Lemma 15. There exists a constant C0 with a property that for any k the
number of minimal factorisations σ1σ2 = π, |σ1| + |σ2| = |π| of a cycle
π = (1 , . . . , k) and such that the associated graph ˜G consists of s ≥ 2
components is bounded from above by
(C0k)2s−2
(2s − 2)! .
Proof. Since the factorization is minimal therefore the graph G associated
to σ1, σ2 is a tree. We will give to G a structure of planted planar tree: the
root is the cycle of σ1 containing 1 and his left-most edge links it to the
cycle of σ2 containing 1.
In each connected component of ˜G there is at most one vertex of degree
higher than one and we shall decorate this vertex. If in some c onnected
component of ˜G there are no such vertices we decorate any of them which
is not a leaf in G. In this way the decorated vertices can be identiﬁed with
connected components of ˜G.
We consider the graph G′ obtained from G by removing the leaves (ex-
cept the root) and the graph G′′ which consists of the decorated vertices of
˜G; we connect two vertices A, B ∈ G′′ by an edge if vertices A, B are con-
nected in G (or, equivalently,G′) by a direct path, i.e. a path which does not
pass through any connected component of ˜G other than the ones speciﬁed
by A and B. It is easy to see that G′′ inherits the structure of a plane rooted
tree from G (we deﬁne the root of G′′ to be the connected component of ˜G
of the root of G) and it has s vertices. It follows that the number of such
trees G′′ is bounded from above by the Catalan number 1
s+1
( 2s
s
)
< 4s.
In order to reconstruct the tree G′ from G′′ we have to specify for each
edge of G′′ if it comes from a single edge of G′ or from a pair or a triple
of consecutive edges of G′; it follows that we have (at most) 3s−1 choices.
