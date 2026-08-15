---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-024-44-flattening-compatible-with-a-longitude
section_title: "Flattening compatible with a longitude"
section_number: 4.4
pages: 25-26
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
combinatorial ﬂattening that is compatible with a longitude.
Recall what is a combinatorial ﬂattening of an ideal triangulation T from Deﬁnition 2.1.
Given a simple peripheral curve λ on the boundary of M that represents a longitude — in
particular, having intersection number one with the chosen meridian µ — we can construct
the sum of combinatorial edge parameters along λ, just as in Section 2.2. It takes the form
(4.7) λ :
N∑
i=1
(
GN +2,iZi + G′
N +2,iZ ′
i + G′′
N +2,iZ ′′
i
)
,
for integer vectors GN +1, G′
N +2, G′′
N +2. Just as we obtained A, B, and ν from the edge and
meridian equations (with or without deformation), we may also now de ﬁne
(4.8) Ci = 1
2(GN +2,i− G′
N +2,i ), D i = 1
2(G′′
N +2,i− G′
N +2,i ), ν λ =−1
2
N∑
i=1
G′
N +2,i .
Deﬁnition 4.4. A combinatorial ﬂattening ( f,f ′,f ′′) is compatible with a longitude if in
addition to Equations (
2.10a)–(2.10b), it also satisﬁes
(4.9) GN +2,if + G′
N +2,if ′ + G′′
N +2,if ′′ = 0.
Equivalently, a combinatorial ﬂattening compatible with the longitude is a vector ( f,f ′′)∈
Z2N that satisﬁes
(4.10) Af + Bf ′′ =ν, C ·f +D·f ′′ =νλ,
A combinatorial ﬂattening compatible with a longitude always exists [
Neu92, Lem.6.1].
In the context of functions on the character variety, it is natura l to deform the meridian
gluing equation, and simultaneously to introduce a longitude gluing equ ation, in the form
(4.11a) µ :
N∑
i=1
(
GN +1,iZi + G′
N +1,iZ ′
i + G′′
N +1,iZ ′′
i
)
= 2u
(4.11b) λ :
N∑
i=1
(
GN +2,iZi + G′
N +2,iZ ′
i + G′′
N +2,iZ ′′
i
)
= 2v,
for some complex parameters u and v. Upon exponentiation, these equations reduce to the
expected (
4.5)–(4.6) if
(4.12) m2 =e2u, ℓ 2 =e2v.
26 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
(It is easy to show, following [
NZ85], that C and D as deﬁned by ( 4.10) are the correct
exponents for the exponentiated longitude equation ( 4.6).) If M is a knot complement and
we want to lift from PSL (2, C) to SL(2, C) representations, we should take m = eu and
ℓ =−ev and divide ( 4.11b) by two before exponentiating. This provides the correct way to
take a square root of the exponentiated gluing equation, cf. [Cal06].
The remarkable symplectic property of A and B may be extended to C and D, even
though in general C, D are vectors of half-integers rather than integers. Namely, ther e
exists a completion of ( A B) to a full symplectic matrix ( A B
C D ) such that the bottom rows of
C and D are the vectors C and D [NZ85]. In particular, this means that
(4.13) AN·D− BN·C = 1,
where AN, BN are the bottom (meridian) rows of A, B.
