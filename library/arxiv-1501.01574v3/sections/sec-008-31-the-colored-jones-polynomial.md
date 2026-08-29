---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-008-31-the-colored-jones-polynomial
section_title: "The colored Jones polynomial"
section_number: 3.1
pages: 9-10
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
---
recall the deﬁnition of the Chebyshev polynomials of the sec ond kind. For n ≥ 0, the
polynomial Sn(x) is deﬁned recursively as follows:
(2) Sn+2(x) = xSn+1(x) − Sn(x), S 1(x) = x, S 0(x) = 1 .
Let D be a diagram of a knot K. For an integer m > 0, let Dm denote the diagram
obtained from D by taking m parallels copies of K. This is the m-cable of D using the
blackboard framing; if m = 1 then D1 = D. Let ⟨Dm⟩ denote the Kauﬀman bracket of
Dm: this is a Laurent polynomial over the integers in a variable v−1/ 4 normalized so that
10
⟨unknot⟩ = −(v1/ 2 + v−1/ 2). Let c = c(D) = c+ + c− denote the crossing number and
w = w(D) = c+ − c− denote the writhe of D.
For n > 0, we deﬁne
JK (n) := (( −1)n−1v(n2−1)/ 4)w(−1)n−1⟨Sn−1(D)⟩
where Sn−1(D) is a linear combination of blackboard cablings of D, obtained via equation
(2), and the notation ⟨Sn−1(D)⟩ means extend the Kauﬀman bracket linearly. That is, for
diagrams D1 and D2 and scalars a1 and a2, ⟨a1D1 + a2D2⟩ = a1⟨D1⟩ + a2⟨D2⟩.
For a Laurent polynomial f (v) ∈ C[v±1/ 4], let d+[f ] and d−[f ] be respectively the
maximal and minimal degree of f in v.
Deﬁnition 3.1. A quasi-polynomial is a function
f : N → C, f (n) =
d∑
i=0
ci(n)ni
for some d ∈ N, where ci(n) is a periodic function with integral period for i = 1, · · · , d. If
cd(n) is not identically zero, then the degree of f (n) is d.
The period π of a quasi-polynomial f (n) as above is the common period of ci(n).
Garoufalidis [9] showed that for any knot K ⊂ S3 the degrees d+[JK (n)] and d−[JK (n)]
are quadratic quasi-polynomials. The common period of d+[JK (n)] and d−[JK (n)] is called
the period of K, denoted by π(K).
