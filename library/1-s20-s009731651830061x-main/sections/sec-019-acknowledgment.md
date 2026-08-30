---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-019-acknowledgment
section_title: "Acknowledgment"
section_number: null
pages: 41-44
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
The author thanks an anonymous referee for the careful reading of the paper and 
several interesting comments.
Appendix A.  The case v =1  − u
A.1. The cases (u, v) =( 0, 1) and (u, v) =( 1, 0)
The generating function of monotone triangles with bottom row b1, ...,  bn evaluated 
at (u, v) =( 0, 1) is equal to the number of monotone triangles with that bottom row, 
where SE-diagonals are strictly increasing, while the evaluation at (u, v) =( 1 , 0) is  
the number of monotone triangles that are strictly increasing along NE-diagonals. The 
number is in both cases ∏
1≤i<j≤n
bj −bi
j−i as both sets are in bijective correspondence with 
Gelfand–Tsetlin patterns with bottom row b1 −1, b2 −2, ...,  bn −n (in the ﬁrst case, this 
follows by subtracting i from the i-th NE-diagonal for all i, counted from the left, while 
in the second case, this follows by subtracting i from the i-th SE-diagonal for all i, also 
counted from the left), and the number of Gelfand–Tsetlin patterns with bottom row 
b1, ...,  bn is ∏
1≤i<j≤n
bj −bi +j−i
j−i , see [18]o r [30, Corollary 7.21.4 and Lemma 7.21.1].
A.2. The case (u, v) =( 1
2 , 1
2 )
On the other hand, the generating function of monotone triangles with bottom 
row b1, ...,  bn evaluated at (u, v) =( 1
2 , 1
2 )i s — u p to the factor 2
(n
2
)
—equal to the 
2-enumeration of monotone triangles with respect to the number of entries that lie strictly 
between their SW-neighbors and their SE-neighbors. By [27, Theorem 2], this number is 
2
(n
2
)∏
1≤i<j≤n
bj −bi
j−i . If (b1, ...,  bn) =( 1, ...,  n), this corresponds to the 2-enumeration 
of ASMs with respect to the number of −1’s, or, equivalently, to the enumeration of 
domino tilings of the Aztec diamond of order n, see [10]a n d also [8, Remark 4.3], where 
in order to obtain the number of the latter one has to multiply by 2n.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 601
Fig. 5. AR4,7 (left) and an example (right).
A.3. The general case
The results mentioned in the previous two paragraphs can also be deduced from 
Theorem 2 as follows. In all cases, ∏
1≤p<q≤n Exq Strictxq,xp is a symmetric polyno-
mial in Δx1 , ...,  Δxn with constant term 1, and the enumeration formulas follow from 
the fact that the application of an “operator” polynomial with these properties to ∏
1≤i<j≤n
xj −xi
j−i leaves the polynomial invariant as was shown, e.g., in [15, Lemma 2.5]. 
In fact, a common generalization follows if we assume that v =1  − u, because in 
this case the same argument applies and we can conclude that the generating func-
tion is ∏
1≤i<j≤n
bj −bj
j−i . (This result could also be derived using known proofs for the 
2-enumeration of ASMs or the enumeration of perfect matchings of the Aztec diamonds, 
see, e.g., [27,10].) In particular, it follows that the generating function is independent 
of u.
A.3.1. Perfect matchings
The specialization v =1  −u of the generating function is also the weighted enumeration 
of perfect matchings of a certain portion of the square grid: First observe that, by 
extending the bijection between monotone triangles with bottom row 1, 2, ...,  n and 
n × n ASMs to monotone triangles with arbitrary increasing bottom row of positive4
integers, say, b1, ...,  bn, we see that the latter are in bijection to n × m matrices, where 
m is any positive integer with m ≥ bn that have the same properties as ASMs with 
the exception that column sums do not have to be 1, but it is still required that the 
topmost non-zero entry of each column is 1, and, in addition, the column sums have to 
be 1 precisely for the columns b1, ...,  bn.
Now let ARn,m denote the rectangular graph that consists of n rows of sequences of 
m consecutive cells of the form 3, see Fig. 5 (left) for AR4,7. It is a well-known fact, see 
[7], that the perfect matchings of ARn,n can be partitioned into classes that are indexed 
by n × n ASMs, such that, for a given ASM, the number of perfect matchings in the 
4 It is no restriction to conﬁne our considerations to monotone triangles that contain only positive integers 
in the bottom row, because every monotone triangle that contains non-positive integers can be transformed 
to one that has only positive integers by adding the same positive integer to every entry.
602 I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
Fig. 6. Urban renewal.
associated class is a power of 2, where the exponent is just the number of 1’s in the 
ASMs. This can be extended to the “rectangular alternating sign matrices” described 
in the previous paragraph as follows. For a given strictly increasing sequence of positive 
integers b =( b1, ...,  bn)o f  length n and m ≥ bn, let ARn,m
b denote the graph that 
is obtained from ARn,m by adding vertical edges incident with the bottom vertices of 
the cells in the bottom row of ARn,m except for the vertices in columns b1, ...,  bn. For 
instance, the underlying graph in Fig. 5 (right) is AR4,7
1,3,4,7. Then the perfect matchings 
of ARn,m
b
can be partitioned such that the classes are indexed by monotone triangles 
with bottom row b and the number of elements in each class is a power of 2, where the 
exponent is the number of 1’s in the corresponding rectangular alternating sign matrix. 
The perfect matching in Fig. 5 (right) is a perfect matching that lies in the class of the 
following monotone triangle.
5
25
246
1347
The corresponding rectangular alternating sign matrix can be obtained by counting, for 
each cell, the number of edges that are part of the perfect matching and subtract 1, 
see Fig. 5 (right), where we have put the numbers into the appropriate cells. The other 
perfect matchings that are in the class of the given monotone triangle are obtained by 
“rotating” the perfect matching edges of those cells that contain two matching edges 
independently.
Next we introduce edge weights such that the weighted enumeration of the per-
fect matchings of ARn,m
b associated with a ﬁxed monotone triangle M is just 
uinv(M )(1 − u)inv′(M ): in each cell, we assign the weights 1, 1, u, 1 − u to the edges, 
where we start at the NW edge and go around the cell clockwise, see Fig. 6 right. As a 
side remark note that this shows that the special cases (u, v) =( 1, 0) and (u, v) =( 0, 1)
in the generating function amounts to compute the number of perfect matchings of a 
hexagonal grid (since (u, v) =( 1, 0) corresponds to the deletion of the SW edge of each 
cell, while (u, v) =( 0, 1) corresponds to the deletion of the SE edge of each cell), which 
is no surprise, because counting perfect matchings of hexagonal grids corresponds to 
lozenge tiling enumeration, which in turn is related to the enumeration of semistandard 
tableaux and thus of Gelfand–Tsetlin patterns.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 603
A.3.2. Independence of u
We sketch an argument that shows that the weighted enumeration of our perfect 
matchings is independent of u, and thus the generating function of monotone triangles 
(after setting v =1  − u): This is done with the help of the local graph operation urban 
renewal which was introduced by Kuperberg and Propp, see Fig. 6. If we replace a cell 
with edge weights a, b, c, d by the conﬁguration indicated in Fig. 6 (right), the generat-
ing function of perfect matchings of the original graph is obtained from the generating 
function of the modiﬁed graph by multiplication of ad + bc. We perform this operation 
to every cell of, say, AR4,7
1,3,4,7.
In the graph that is obtained this way, there are two trivial simpliﬁcations that can 
be made at several places: If the two edges that are incident with a vertex of degree 2
have weight 1, they can be contracted without changing the generating function, and 
each edge with weight 1t h a t is incident with a vertex of degree 1c a n be deleted along 
with all edges incident with the other vertex of the edge. This implies that the weighted 
enumeration of the perfect matchings of AR4,7
1,3,4,7 is equal to the sum of the weighted 
enumeration of the perfect matchings of the following graphs: AR3,6
2,3,6, AR3,6
1,3,6, AR3,6
2,3,5, 
AR3,6
1,3,5, AR3,6
2,3,4, AR3,6
1,3,4. (The sequences arise as follows: The complement of {1, 3, 4, 7}
in {1, ...,  7} is {2, 5, 6}, and now we allow for each element i in the complement that 
either the element itself or i − 1i s  an element of the new complements. If we take 
complements in {1, ...,  6}, then we obtain our sequences.) We can assume by induction 
with respect to n that the generating function of the perfect matchings of each of these 
graphs is independent of u.
