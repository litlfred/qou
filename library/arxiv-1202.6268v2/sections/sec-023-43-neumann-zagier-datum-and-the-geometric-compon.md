---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-023-43-neumann-zagier-datum-and-the-geometric-compon
section_title: "Neumann-Zagier datum and the geometric component"
section_number: 4.3
pages: 24-25
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
with torus boundary and T a (combinatorial) ideal triangulation. The Neumann-Zagier
datum βT = (z, A, B) may be generalized for representations ρ∈ XM besides the discrete
faithful.
To begin, choose a representation ρ : π1(M) −→ PSL(2, C), and, if desired, a lift to
SL(2, C). Let ( µ,λ ) be meridian and longitude cycles 4 on ∂M , and let ( m±1,ℓ ±1) be the
eigenvalues of ρ(µ) and ρ(λ), respectively. For example, for the lift of the discrete faithful
representation to SL(2, C), we have (m,ℓ ) = (1,−1) [Cal06]. These eigenvalues deﬁne a map
(4.4) XM−→ (C∗)2/Z2,
whose image is a curve YM , the zero-locus of the A-polynomial AM (ℓ,m ) = 0 [ CCG+94]. We
will denote the representation ρ as ρm to emphasize its meridian eigenvalue.
Now, given a triangulation T , and with A, B, and ν deﬁned as in Section 2.3, the gluing
equations ( 2.12) can easily be deformed to account for m⁄= 1. Namely, we ﬁnd [ NZ85]
(4.5)
N∏
j=1
zj
Aijz′′
j
Bij = (−1)νim2δiN.
The developing map (4.3) maps every solution of these equations to a representation π1(M)−→
PSL(2, C) with meridian eigenvalue±m. The triangulation T isρm-regular if and only if ρm
is in the image of this map. We can similarly express the longitude eigenva lue as a product
of shape parameters
(4.6)
N∏
j=1
zj
2Cjz′′
j
2Dj = (−1)2νλℓ2,
4Recall again that these cycles are only canonically deﬁned for knot c omplements. In general there is
some freedom in choosing them, but the torsion depends in a predict able way on the choice, cf. [Yam08].
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 25
for some 2Cj, 2Dj, 2νλ∈ Z. Then, if T is a ρm-regular triangulation, the irreducible compo-
nent of YM containingρm is explicitly obtained by eliminating all shapes zj from (4.5)–(4.6).
In general, the shapes zj are algebraic functions on components of the varietyYM . However,
ifM is hyperbolic andT is regular for all but ﬁnitely many representations on the geometric
componentY geom
M , then the shapes zj become rational functions, zj∈C(Y geom
M ). We provide
a proof of this fact in Appendix B. The ﬁeld of functions C(Y geom
M ) may be identiﬁed with
Q(m)[ℓ]/
(
Ageom(ℓ,m )
)
, and the functions zj(ℓ,m ) can easily be obtained from equations
(4.5)–(4.6).
