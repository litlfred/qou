---
doc_id: arxiv-0903.1376v1
doc_title: "Particle Topology, Braids and Braided Belts"
section_id: sec-005-algebra
section_title: "Algebra"
section_number: null
pages: 16-19
source_pdf: 0903.1376v1.pdf
source_sha256: c106071c1a3110e8
toc_source: outline
doc_brief: "Particle Topology, Braids and Braided Belts — Recent work [1, 2] suggests that topological features of certain quantum gravity theories can be interpreted as particles, matching the known fermions"
---
Algebra
In this section we give a representation of the three-strand braid group in terms
of permutation matrices. A permutation matrix P is a matrix whose columns
are a permutation of the columns of the identity matrix. Such a matrix acts
as a permutation on the standard basis (column vectors that have a single
unit entry). We shall sometimes refer to P as a permutation, rather than a
permutation matrix, for brevity. For example,
P1,2 =


0
1
0
1
0
0
0
0
1


(10)
and
P2,3 =


1
0
0
0
0
1
0
1
0

.
(11)
Obviously


0
1
0
1
0
0
0
0
1




1
0
0

=


0
1
0


and so on.
If D is a diagonal matrix and P is a permutation matrix, then
PD = DP P
(12)
where DP = P(D) denotes the result of permuting the elements of D along the
diagonal according to the permutation P. This is directly analogous to eqn. (2)
The permutation matrices P1,2 and P2,3 generate (by taking products) all
permutations on three letters. These permutations can be used to represent
permutations induced by a braid, and hence they can stand in for the braid
word. A general twist word [a, b, c] may be represented by the matrix
[a, b, c] =


ta
0
0
0
tb
0
0
0
tc

.
The reader should be aware that the permutation matrices do not give a com-
plete image of the braid group, because they do not deﬁne the direction of
crossing. Hence the Ps contain less information than the σis. However we can
ﬁnd the pure twist form of a braid using this matrix representation in a manner
we will now describe.
16
Consider the identity 3-belt, as illustrated in ﬁg. 5. If we perform trinion
ﬂips on the top of the belt, we induce both crossings and twistings. When the
crossings created in this process correspond to a given generator, σi, the twists
induced are the negative of the twists corresponding to σi, as listed in eqns (1).
The relative minus sign occurs because eqns (1) list the twist words created
when crossings are eliminated, rather than created. In the interests of notational
clarity, we shall therefore write ρi to denote the twists and permutations induced
on an initially trivial 3-belt by performing a trinion ﬂip to cross strand i over
strand i + 1. The corresponding twists and permutations are then;
ρ1
→

−1
2, −1
2, 1
2

P1,2
ρ−1
1
→
 1
2, 1
2, −1
2

P1,2
ρ2
→
 1
2, −1
2, −1
2

P2,3
ρ−1
2
→

−1
2, 1
2, 1
2

P2,3
(13)
compare this with eqns (1). Applying eqn. (12) we see that
P1,2[a, b, c] = [b, a, c]P1,2
and
P2,3[a, b, c] = [a, c, b]P2,3.
To ﬁnd the pure twist-word corresponding to a given braid word, we ﬁrst
replace the σi with the equivalent ρi e.g.
σ1σ2σ−1
1
→ρ1ρ2ρ−1
1 .
We next substitute in the twist words and permutations from eqns (13), and
apply eqn. (12). Once all the twist words have been shifted to the far left of the
resulting expression and summed, we read oﬀthe negative of this twist word to
ﬁnd the pure twist-word corresponding to our initial braid word.
Example: Let us ﬁnd the pure twist word corresponding to the braid σ1σ2σ−1
1 .
We proceed as follows;
ρ1ρ2ρ−1
1
=

−1
2, −1
2, 1
2

P1,2
1
2, −1
2, −1
2

P2,3
1
2, 1
2, −1
2

P1,2
=

−1
2, −1
2, 1
2
 
−1
2, 1
2, −1
2

P1,2P2,3
1
2, 1
2, −1
2

P1,2
=

−1
2, −1
2, 1
2
 
−1
2, 1
2, −1
2
 
−1
2, 1
2, 1
2

P1,2P2,3P1,2
=

−3
2, 1
2, 1
2

P1,2P2,3P1,2
We then take the negative of the computed twist word, to obtain our result,
[ 3
2, −1
2, −1
2].
17
Figure 15: Uniquely forming the product of two braids (left) by joining them
box-to-box, to yield a link (right).
These assignments of framed permutations to braids gives a representation
of the framed braid group into framed permutations. To see this we can directly
verify that σ1σ2σ1 = σ2σ1σ2 at the level of the framed permutations as follows;
ρ1ρ2ρ1
=

−1
2, −1
2, 1
2

P1,2
1
2, −1
2, −1
2

P2,3

−1
2, −1
2, 1
2

P1,2
=

−1
2, −1
2, 1
2
 
−1
2, 1
2, −1
2

P1,2P2,3

−1
2, −1
2, 1
2

P1,2
=
[−1, 0, 0] P1,2P2,3

−1
2, −1
2, 1
2

P1,2
=
[−1, 0, 0] P1,2

−1
2, 1
2, −1
2

P2,3P1,2
=
[−1, 0, 0]
1
2, −1
2, −1
2

P1,2P2,3P1,2
=

−1
2, −1
2, −1
2

P1,2P2,3P1,2.
(14)
Similarly, we ﬁnd that
ρ2ρ1ρ2 =

−1
2, −1
2, −1
2

P2,3P1,2P2,3.
Since ρ1ρ2ρ1 and ρ2ρ1ρ2 yield the same twist word we conclude that σ1σ2σ1 =
σ2σ1σ2. It is noteworthy that P1,2P2,3P1,2 = P2,3P1,2P2,3, however this has
no bearing on the result because the twist words alone are suﬃcient to deﬁne
isomorphism.
18
Figure 16: If the edge running through the external network (represented by the
box) carries no twists, other than those on the braided belt strands themselves,
the strands may be cyclically permuted by passing one strand under (or around)
the others (top row, left to right). Fig. 7 gives an explicit example of such a case.
If the edge does twist around other edges in the rest of the network (bottom
row) then such cyclic permutations are not allowed.
