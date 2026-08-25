---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-003-11-motivation
section_title: "Motivation"
section_number: 1.1
pages: 1-3
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
1.2 Torsionanditstwistedversion ............................ 3
1.3 Neumann–Zagiermatricesandtheirtwistedversion ................ 4
1.4 The1-loopinvariantanditstwistedversion ..................... 7
2 Proofs:twistedNZmatrices ................................. 9
3E x a m p l e s........................................... 1 2
3.1 Theknot4 1 ....................................... 1 2
3.2 Theknot6 3 ....................................... 1 4
4 Proofs:twisted1-loopinvariant ............................... 1 6
5 Examples,continued ..................................... 2 1
5.1 Theknot4 1 ....................................... 2 1
5.2 Theknot6 3 ....................................... 2 1
References ............................................ 2 2
1 Introduction
1.1 Motivation
Ideal triangulations of 3-manifolds with torus boundary components were introduced
by Thurston [26] as a convenient way to describe and eﬀectively compute [2] complete
123 ©The Author(s) 2023. This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougiveappropriatecredittotheoriginal
author(s)andthesource,providealinktotheCreativeCommonslicence,andindicateifchangesweremade.Theimagesorother
thirdpartymaterialinthisarticleareincludedinthearticle’sCreativeCommonslicence,unlessindicatedotherwiseinacreditline
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by
statutoryregulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthecopyrightholder.Toview
acopyofthislicence,visit http://creativecommons.org/licenses/by/4.0/.
0123456789().,–: volV
37 Page 2 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
hyperbolic structures on 3-manifolds. To do so, one assigns a complex number diﬀerent
from 0 or 1 to each tetrahedron and a polynomial equation around each edge of the
triangulation. These so-called gluing equations have special shape that can be described
by two matrices A and B (with rows and columns indexed by the edges and by the
tetrahedra,respectively)whoseentriesdescribethenumberoftimes(but not theorderby
which)tetrahedrawindaroundanedge.OneofthemaindiscoveriesofNeumann–Zagier
is that the matrix (A|B) becomes, after some minor modiﬁcations, the upper part of a
symplectic matrix with integer entries [22]. The symplectic property of the NZ matrices
andofthecorrespondinggluingequationsdeﬁnealinearsymplecticstructureonavector
space whose quantization leads to a plethora of quantum invariants that include the
loop invariants of Dimofte and the ﬁrst author [6,8], the 3D-index in both the original
formulationofDimofte-Gaiotto-Gukov[ 9,10]aswellasthestate-integralformulationof
Kashaevandtheﬁrstauthor[ 13]andKashaev–Luo–Vartanovstate-integral[ 1,20].Allof
those invariants are deﬁned using the NZ matrices of a suitable ideal triangulation, and
their topological invariance follows by proving that they are unchanged under Pachner
2–3moves.
Our original motivation was to study the behavior of the loop invariants of [6]u n d e r
cyclic covers. Since the latter are deﬁned in terms of NZ data of an ideal triangulation,
we were led to study the behavior of the NZ matrices under cyclic covers. By elementary
topology, each tetrahedron of an ideal triangulation lifts ton tetrahedra in then-fold
cyclic cover, and lifting all the way to the inﬁnite cyclic cover leads to the notion of
NZ matrices which we can callequivariant or twisted (as is common in algebraic and
geometric topology) or t-deformed (as is common in physics). We will use the term
“twisted”, and keep in mind that the variablet below encodes topological information of
cycliccovers.
Said diﬀerently, as the triangulation of the cyclic cover unfolds, so do its edges and the
tetrahedra that wind around them. This is the content of the twisted NZ matrices. How
canthiselementaryideabenon-trivialorinteresting?
ItturnsoutthatthetwistedNZmatriceshavetwistedsymplecticpropertieswhichcome
from topology and using them one can give twisted versions of the above mentioned
invariants, i.e., of the loop invariants [6,8], the 3D-index in [9,10]a n d[13] and KLV
state-integral [1,20]. A key property of such a twisted invariant is that it determines the
corresponding (untwisted) invariant of all cyclic covers. For example, the twisted 1-loop
invariantofaknotcomplementdeﬁnedbelowsatisﬁesthisproperty.
Our goal is to deﬁne the twisted NZ matrices, describe their properties and show how
tocomputethemintermsofthemethodsdevelopedby SnapPy[2].Havingdoneso,we
canusethetwistedNZmatricestodeﬁneatwistedversionofthe1-loopinvariant,prove
its topological invariance and conjecture that it equals to the adjoint twisted Alexander
polynomial. It is interesting to note that the twisted 1-loop invariant depends only on
the combinatorics of the NZ matrices of the inﬁnite cyclic cover (which is abelian infor-
mation), whereas the adjoint twisted Alexander polynomial depends on the complete
hyperbolicstructuregivenasarepresentationofthefundamentalgroup.
The twisted NZ matrices introduced in thispaper have further applications aside from
the topological 1-loop polynomial invariants studied in the present paper. In the sequel
paper [16], we use the twisted NZ matrices to study the behavior of the higher-loop
invariants of [6] under cyclic coverings. The latter were recently shown to be topological
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 3 of 23 37
invariants of cusped hyperbolic 3-manifolds [14]. A further application of twisted NZ
matrices was given in our joint work [17] where we introduced a super-version of them
todeﬁne1-looptorsionpolynomialsforallrepresentationsof sl2(C)thatweconjectured
to be equal to their corresponding twisted Alexander polynomials. This conjecture was
recentlyprovenforallﬁbered3-manifolds[ 15].
