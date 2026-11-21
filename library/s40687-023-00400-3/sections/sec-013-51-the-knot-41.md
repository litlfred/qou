---
doc_id: s40687-023-00400-3
doc_title: "Twisted Neumann–Zagier matrices"
section_id: sec-013-51-the-knot-41
section_title: "The knot 41"
section_number: 5.1
pages: 21-21
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
toc_source: outline
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
In Sect. 3.1, we already gave the twisted NZ matrices of the 41 knot. Using the same
notation, we now give the remaining data, namely the shapes of the complete hyperbolic
structure and ﬂattenings, which are needed to compute the twisted 1-loop invariant.
The solution for the complete structure is z1 = z2 = 1+√−3
2
. Equations (41) and (42)
give
G(t) diag(ζ) + G′(t) diag(ζ ′) + G′′(t) diag(ζ ′′) =

2ζ1t + ζ ′
1t2
ζ ′
2 + 2ζ2t
ζ ′
1t + 2ζ ′′
1 t2 2ζ ′′
2 t + ζ ′
2t2

.
(68)
One easily checks that (f1, f2) = (0, 0), (f ′
1, f ′
2) = (1, 1), and (f ′′
1 , f ′′
2 ) = (0, 0) are a combina-
torial ﬂattening of T . Therefore, the twisted 1-loop invariant of T is given by
τ CS(T , t) = ±
det

2ζ1t + ζ ′
1t2
ζ ′
2 + 2ζ2t
ζ ′
1t + 2ζ ′′
1 t2 2ζ ′′
2 t + ζ ′
2t2

ζ ′
1ζ ′
2
(69)
= ±t(t −1)

t2 −z1z2 + 2z1 + 2z2 −4
z1z2
t + 1

.
(70)
Substituting the solution for the complete structure into the above, we obtain
τ CS(T , t) = ±t(t −1)(t2 −5t + 1)
well deﬁned up to multiplication by a monomial ±tr for some integer r, hence
τ CS
λ (T ) = ±3 .
