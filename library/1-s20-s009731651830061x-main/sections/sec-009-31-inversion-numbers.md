---
doc_id: 1-s20-s009731651830061x-main
doc_title: "Journal of Combinatorial Theory, Series A 158 (2018) 560–604 Contents lists available at ScienceDirect Journal of Combinatorial Theory, Series A www.elsevier.com/locate/jcta Consta"
section_id: sec-009-31-inversion-numbers
section_title: "Inversion numbers"
section_number: 3.1
pages: 15-16
source_pdf: 1-s2.0-S009731651830061X-main.pdf
source_sha256: 8d591fe7f1673c52
doc_brief: "Fischer, Constant term formulas for refined enumerations of Gog and Magog trapezoids (JCTA 158, 2018, 560–604) — alternating sign matrices, plane partitions, constant-term methods."
---
The two inversion numbers are deﬁned in the obvious way: Suppose M =( mi,j)i s an 
(m, n, k)-Gog trapezoid, then
inv(M)=# {mi,j : mi,j = mi+1,j+1},
inv′(M)=# {mi,j : mi,j = mi+1,j}.
So, in order for the entry mi,j to contribute to inv(A), it must have a SE neighbor in the 
(m, n, k)-Gog trapezoid and this neighbor must be equal to mi,j; however, mi,j need not 
to have a SW neighbor. Similar for the complementary inversion number. Corollary 6
implies the following.
Theorem 8. The generating function of (m, n, k)-Gog trapezoids with bottom row 
b1, ...,  bk w.r.t. inv and inv′ is the constant term of
k∏
i=1
(1 + xi)bi x−n+1
i
n∏
i=k+1
(1 + xi)m+i+1(1 + uxi)k−ix−n+i−k
i
×
∏
1≤i<j≤n
(xi − xj)(1 + (1− v)xi + u(xj + xixj)) (3.1)
in x1, ...,  xn.
The additional factor 
n∏
i=k+1
1+xi
1+uxi
is caused by the fact that the u-weight should not 
take into account the entries in the k-th NE-diagonal that are equal to their upper bound.
I. Fischer / Journal of Combinatorial Theory, Series A 158 (2018) 560–604 575
