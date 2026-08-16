---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-011-5-examples-continued
section_title: "Examples, continued"
section_number: 5
pages: 21-22
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
Inthissection,whichisacontinuationofSect. 3,wecomputethetwisted1-loopinvariant
ofanidealtriangulationusingthemethodsof SnapPy.
5.1 The knot 4 1
In Sect.3.1, we already gave the twisted NZ matrices of the 41 knot. Using the same
notation, we now give the remaining data, namely the shapes of the complete hyperbolic
structureandﬂattenings,whichareneededtocomputethetwisted1-loopinvariant.
The solution for the complete structure isz
1 = z2 = 1+√−3
2 . Equations (41)a n d(42)
give
G(t)diag( ζ) + G′(t)diag( ζ′) + G′′(t)diag( ζ′′) =
(
2ζ1t + ζ′
1t2 ζ′
2 +2ζ2t
ζ′
1t +2ζ′′
1 t2 2ζ′′
2 t + ζ′
2t2
)
. (68)
One easily checks that (f1,f2) = (0,0), (f ′
1 ,f ′
2) = (1,1), and (f ′′
1 ,f ′′
2 ) = (0,0) are a combina-
torialﬂatteningof T .Therefore,thetwisted1-loopinvariantof T isgivenby
τCS(T ,t) =±
det
(
2ζ1t + ζ′
1t2 ζ′
2 +2ζ2t
ζ′
1t +2ζ′′
1 t2 2ζ′′
2 t + ζ′
2t2
)
ζ′
1ζ′
2
(69)
=± t(t −1)
(
t2 − z1z2 +2z1 +2z2 −4
z1z2
t +1
)
. (70)
Substitutingthesolutionforthecompletestructureintotheabove,weobtain
τCS(T ,t) =± t(t −1)(t2 −5t +1)
welldeﬁneduptomultiplicationbyamonomial ±tr forsomeinteger r,hence
τCS
λ (T ) =± 3 .
5.2 The knot 6 3
In this section, we give the geometric solution and the ﬂattenings of the triangulation of
the63 knottocomputeitstwisted1-loopinvariant,followingthenotationofSect. 3.2.
Thetraceﬁeldofthe6 3 knotisthenumberﬁeldoftype[0 ,3]anddiscriminant −11·312
givenby F = Q[ξ]where ξ ≈ 1.073−0.558√−1satisﬁes ξ6 −ξ5 −ξ4 +2ξ3 −ξ +1 = 0.
Thesolutionforthecompletestructureisgivenexactly
(z1,z2,z3,z4,z5,z6) = (−ξ2 + ξ ,−ξ2 +1,−ξ3 + ξ ,−ξ2 +1,−ξ3 + ξ ,−ξ2 + ξ)
(71)
andapproximatelyby
z1 ≈ 0.23279 +0.64139 i, z2 ≈ 0.15884 +1.20014 i, z3 ≈ 0.84116 +1.20014 i,
37 Page 22 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
z4 ≈ 0.15884 +1.20014 i, z5 ≈ 0.84116 +1.20014 i, z6 ≈ 0.23279 +0.64139 i.
It is easy to check that (f1,... ,f6) = (0,1,0,1,0,0), (f ′
1 ,... ,f ′
6) = (1,0,1,0,1,1), and
(f ′′
1 ,... ,f ′′
6 ) = (0,0,0,0,0,0) is a combinatorial ﬂattening ofT . Equations (44)a n d(45)
givethat
τCS(T ,t) = det
(
G(t)diag( ζ) + G′(t)diag( ζ′) + G′′(t)diag( ζ′′)
)
ζ′
1ζ2ζ′
3ζ4ζ′
5ζ′
6
=
det
⎛
⎜⎜
⎜
⎜
⎜
⎜⎝
ζ
1t ζ2t2 ζ3t ζ4 0 ζ6t
ζ′
1 ζ′′
2 t + ζ′
2t2 + ζ′′
2 t3 0 ζ′′
4 + ζ′
4t + ζ′′
4 t2 0 ζ′
6t3
ζ′′
1 ζ′
2t ζ′
3t 0 ζ′
5 ζ′′
6 t
ζ′′
1 t2 0 ζ′
3t2 ζ′
4t2 ζ′
5t3 ζ′′
6 t3
ζ′
1t2 0 ζ′′
3 + ζ3t + ζ′′
3 t2 0 ζ′′
5 + ζ5t + ζ′′
5 t2 ζ′
6
ζ1t2 ζ2t2 0 ζ4t2 ζ5t2 ζ6t2
⎞
⎟⎟
⎟
⎟
⎟
⎟⎠
ζ′
1ζ2ζ′
3ζ4ζ′
5ζ′
6
Substitutingthesolutionforthecompletestructureintotheabove,weobtain
τCS(T ,t) =(t −1)t8(
44 −15ξ −15ξ2 +34ξ3 −19ξ5
+(t + t−1)(−31 +7ξ +7ξ2 −10ξ3 +3ξ5)
+(t2 + t−2)(15 −3ξ −3ξ2 +2ξ3 + ξ5) −5(t3 + t−3) +(t4 + t−4)
)
≈ t4(−1.000 +6.000t −12.805t2 +33.472t3 −85.242t4
+85.242t5 −33.472t6 +12.805t7 −6.000t8 +1.000t9).
uptomultiplicationbyamonomial ±tr forsomeinteger r,hence
τCS
λ (T ) =± (4 −7ξ −7ξ2 +18ξ3 −11ξ5) ≈± 15.8506 .
Acknowledgements
TheﬁrstauthorwishestothankNathanDunﬁeldforenlighteningconversationsandforsharinghisdrawingprogramof
thetriangulatedcuspofanidealtriangulation.ThesecondauthorwassupportedbyBasicScienceResearchProgram
throughtheNRFofKoreafundedbytheMinistryofEducation(2020R1A6A3A03037901).
Funding Information
OpenAccessfundingenabledandorganizedbyProjektDEAL.
Author details
1InternationalCenterforMathematics,DepartmentofMathematics,SouthernUniversityofScienceandTechnology,
Shenzhen,China, 2MaxPlanckInstituteforMathematics,Bonn,Germany.
Received: 22 December 2022 Accepted: 29 July 2023 Published online: 5 September 2023
