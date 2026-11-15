---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-026-a31-perfect-matchings
section_title: "A.3.1 Perfect matchings"
section_number: null
pages: 42-44
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
toc_source: outline
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
The specialization v = 1 −u of the generating function is also the weighted enumeration 
of perfect matchings of a certain portion of the square grid: First observe that, by 
extending the bijection between monotone triangles with bottom row 1, 2, . . . , n and 
n × n ASMs to monotone triangles with arbitrary increasing bottom row of positive4
integers, say, b1, . . . , bn, we see that the latter are in bijection to n × m matrices, where 
m is any positive integer with m ≥bn that have the same properties as ASMs with 
the exception that column sums do not have to be 1, but it is still required that the 
topmost non-zero entry of each column is 1, and, in addition, the column sums have to 
be 1 precisely for the columns b1, . . . , bn.
Now let ARn,m denote the rectangular graph that consists of n rows of sequences of 
m consecutive cells of the form 3, see Fig. 5 (left) for AR4,7. It is a well-known fact, see 
[7], that the perfect matchings of ARn,n can be partitioned into classes that are indexed 
by n × n ASMs, such that, for a given ASM, the number of perfect matchings in the 
4 It is no restriction to conﬁne our considerations to monotone triangles that contain only positive integers 
in the bottom row, because every monotone triangle that contains non-positive integers can be transformed 
to one that has only positive integers by adding the same positive integer to every entry.
602
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
Fig. 6. Urban renewal.
associated class is a power of 2, where the exponent is just the number of 1’s in the 
ASMs. This can be extended to the “rectangular alternating sign matrices” described 
in the previous paragraph as follows. For a given strictly increasing sequence of positive 
integers b = (b1, . . . , bn) of length n and m ≥bn, let ARn,m
b
denote the graph that 
is obtained from ARn,m by adding vertical edges incident with the bottom vertices of 
the cells in the bottom row of ARn,m except for the vertices in columns b1, . . . , bn. For 
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
2
5
2
4
6
1
3
4
7
The corresponding rectangular alternating sign matrix can be obtained by counting, for 
each cell, the number of edges that are part of the perfect matching and subtract 1, 
see Fig. 5 (right), where we have put the numbers into the appropriate cells. The other 
perfect matchings that are in the class of the given monotone triangle are obtained by 
“rotating” the perfect matching edges of those cells that contain two matching edges 
independently.
Next we introduce edge weights such that the weighted enumeration of the per-
fect matchings of ARn,m
b
associated with a ﬁxed monotone triangle M
is just 
uinv(M)(1 −u)inv′(M): in each cell, we assign the weights 1, 1, u, 1 −u to the edges, 
where we start at the NW edge and go around the cell clockwise, see Fig. 6 right. As a 
side remark note that this shows that the special cases (u, v) = (1, 0) and (u, v) = (0, 1)
in the generating function amounts to compute the number of perfect matchings of a 
hexagonal grid (since (u, v) = (1, 0) corresponds to the deletion of the SW edge of each 
cell, while (u, v) = (0, 1) corresponds to the deletion of the SE edge of each cell), which 
is no surprise, because counting perfect matchings of hexagonal grids corresponds to 
lozenge tiling enumeration, which in turn is related to the enumeration of semistandard 
tableaux and thus of Gelfand–Tsetlin patterns.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604
603
