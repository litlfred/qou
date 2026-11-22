---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Constant term formulas for refined enumerations of Gog and Magog trapezoids"
section_id: sec-027-a32-independence-of-u
section_title: "A.3.2 Independence of u"
section_number: null
pages: 44-44
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
toc_source: outline
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
We sketch an argument that shows that the weighted enumeration of our perfect 
matchings is independent of u, and thus the generating function of monotone triangles 
(after setting v = 1 −u): This is done with the help of the local graph operation urban 
renewal which was introduced by Kuperberg and Propp, see Fig. 6. If we replace a cell 
with edge weights a, b, c, d by the conﬁguration indicated in Fig. 6 (right), the generat-
ing function of perfect matchings of the original graph is obtained from the generating 
function of the modiﬁed graph by multiplication of ad + bc. We perform this operation 
to every cell of, say, AR4,7
1,3,4,7.
In the graph that is obtained this way, there are two trivial simpliﬁcations that can 
be made at several places: If the two edges that are incident with a vertex of degree 2
have weight 1, they can be contracted without changing the generating function, and 
each edge with weight 1 that is incident with a vertex of degree 1 can be deleted along 
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
in {1, . . . , 7} is {2, 5, 6}, and now we allow for each element i in the complement that 
either the element itself or i −1 is an element of the new complements. If we take 
complements in {1, . . . , 6}, then we obtain our sequences.) We can assume by induction 
with respect to n that the generating function of the perfect matchings of each of these 
graphs is independent of u.
