---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-011-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 10-11
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
The authors would like to thank Michael Abel, Ben Elias and Matt Hogancamp for explain-
ing to us their results [1, 23, 36], and Mikhail Gorsky, Daniel Halpern-Leistner, Mikhail Kho-
vanov, Ivan Losev, Davesh Maulik, Michael McBreen, Hugh Morton, Alexei Oblomkov, An-
drei Okounkov, Claudiu Raicu, Sam Raskin, Raphael Rouquier, Lev Rozansky, Peter Samuel-
son, Peng Shan and Monica Vazirani for very useful discussions. Special thanks to Ian Gro-
jnowski for explaining Example 2.5 to us. The work of E. G. was partially supported by the
NSF grant DMS-1559338 and the Hellman fellowship. The work of A. N. was partially sup-
ported by the NSF grant DMS-1600375. The work of E.G. in sections 3, 5 and 6 was supported
by the grant 16-11-10018 of the Russian Science Foundation.
2. T HE FLAG HILBERT SCHEME
2.1. Deﬁnition. Let us recall the usual Hilbert scheme ofn points on C2:
Hilbn ={idealI⊂ C[x,y ], dimC C[x,y ]/I =n}
There is a tautological bundle of rankn on the Hilbert scheme given by:
Tn|I = C[x,y ]/I
Similarly, one can deﬁne the ﬂag Hilbert scheme FHilbn(C2) ofn points on C2 [16, 54] as
the moduli space of complete ﬂags of ideals:
(2.1) FHilbn(C2) ={In⊂...⊂I1⊂I0 = C[x,y ], dimIk−1/Ik = 1,∀k}
Clearly, FHilbn(C2) can be thought of as the closed subscheme of Hilbn×...× Hilb1× Hilb0
cut out by the inclusions Ik⊂ Ik−1 for all k. We will not pursue this description, and instead
work with an alternative one given in the next Subsection. Meanwhile, let us point out several
general features of the ﬂag Hilbert scheme (2.1). We may pull Tn back to FHilbn(C2), where
we have a full ﬂag of tautological bundles:
of ranksn,..., 1. For any k∈{ 1,...,n}, the ﬁbers ofTk over ﬂags In⊂ ...⊂ I0 are precisely
the quotients C[x,y ]/Ik. We deﬁne the tautological line bundles as the successive kernels:
(2.2) Lk = Ker (Tk↠Tk−1)
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 11
Moreover, there is a morphism:
(2.3) ρ : FHilbn(C2)−→ C2n = Cn× Cn
(In⊂...⊂I0)↦→ (x1,...,x n,y 1,...,y n)
where (xk,yk) = suppIk−1/Ik. We may consider the various ﬁbers of this map:
FHilbn(C) =ρ−1(Cn×{ 0}), FHilbn(point) =ρ−1({0}×{ 0})
These will be the moduli spaces of ﬂags of sheaves set-theoretically supported on the line
{y = 0} and at the point (0, 0), respectively. The vector bundles Tk andLk are deﬁned as
before. As a rule, we will write:
FHilbn for any of FHilbn(C2), FHilbn(C) or FHilbn(point)
when we will make general statements that apply to all our ﬂag Hilbert schemes.
Example 2.1. It is well-known that Hilb2 is the blow-up of the diagonal inside (C2× C2)/S2.
It should be no surprise that:
(2.4) FHilb2(C2) = Bl∆
(
C2× C2)
= Proj
( C[x1,x 2,y 1,y 2,z,w ]
(x1−x2)w− (y1−y2)z
)
where the variables xi,yi sit in degree 0, while z,w sit in degree 1 with respect to the Proj.
Settingy1 =y2 = 0, respectivelyx1 =x2 =y1 =y2 = 0, we obtain:
(2.5) FHilb2(C) = P1× A1∪ A1× A1 = Proj
( C[x1,x 2,z,w ]
(x1−x2)w
)
(2.6) FHilb2(point) = P1 = Proj (C[z,w ])
