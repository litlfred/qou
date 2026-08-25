---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-020-71-the-bound-for-degrees-of-hkn
section_title: "The bound for degrees of HK,n"
section_number: 7.1
pages: 16-17
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
deg±(f g) = deg ±(f ) + deg±(g), and deg +(f + g) ≤ max(deg+(f ), deg+(g)).
From deg±{k} = ±k/2, we get
deg±({k}!) = ±k(k + 1)/4, deg±(
[ n
k
]
) = ±k(n − k)/2.
From these and Equation ( 13) we get
deg+(HK,n (q)) ≤ max
1≤k≤n+1
(
− (2n + 2)(2n + 3)
4 + k + k
2 + (n + 1 + k)(n + 1 − k)
2 + deg+(JK,k )
)
.
Using Proposition 6.1 for the upper bound of deg +(JK,k ), after a simpliﬁcation, we get
deg+(HK,n (q)) ≤ max
1≤k≤n+1
(
− n(n + 3)
2 + c(k − 1)2
4 + (k − 1)s+
2 + |ω|(k2 − 1)
4
)
.
The right hand side reaches maximum when k = n + 1. Using ω ≤ c + 2, we have
deg+(HK,n (q)) ≤ n2c/2 + n(s+ + c − 1)/2.
A similar calculation shows that
deg−(HK,n (q)) ≥ −(n2c/2 + n(s− + c − 1)/2).
If we choose A0 bigger than c and |s± + c − 1|, then we have |deg±(HK,n )| ≤ A0n2. This proves the ﬁrst
statement of Theorem 4.2.
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 17
