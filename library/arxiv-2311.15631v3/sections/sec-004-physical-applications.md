---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI"
section_id: sec-004-physical-applications
section_title: "Physical applications"
section_number: null
pages: 23-30
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three Ken KIKUCHI — We classify connected ´ etale algebras A’s in pre-modular fusion categories B with rank(B) ≤"
---
In this section, we discuss physical applications of the classiﬁcation results.
Consider a two-dimensional C-symmetric gapped phase (an existence of braiding is not
assumed at this level). It is known [32, 33] that such phases stand in bijection with C-module
categories
{2d C-symmetric gapped phases } ∼= {C-module categories M}. (3.1)
In particular, ground state degeneracy (GSD) in the LHS is given by rank(M) of a module
category M in the RHS. Therefore, we can translate physical problems in the LH S to math-
ematical problems in the RHS. One of the most important physical pr oblems is whether the
C symmetry is spontaneously broken or not. In this setup, a sponta neous symmetry breaking
(SSB) in the LHS is deﬁned as follows:
Deﬁnition. [3] Let C be a fusion category and M be a (left) C-module category de-
scribing a C-symmetric gapped phase. A symmetry c ∈ C is called spontaneously broken if
∃m ∈ M such that c ⊲ m ⁄∼= m. We also say C is spontaneously broken if there exists a
23
spontaneously broken object c ∈ C . A categorical symmetry C is called preserved (i.e., not
spontaneously broken) if all objects act trivially.
With the deﬁnition, we can show a
Lemma. [3] Let C be a fusion category and M be an indecomposable (left) C-module
category. Then, rank (M) > 1 implies SSB of C (i.e., C is spontaneously broken).
Therefore, in two-dimensional gapped phases, we can mathematic ally prove SSB of a
(categorical) symmetry C by classifying C-module categories. In particular, if M is ﬁnite, it
is known [8, 1] that ∃A ∈ C such that M ≃ C A. In classifying such module categories, it is
natural to assume A be connected ´ etale. (Note that we also assume ambient categorie s be
pre-modular at this point. There are inﬁnitely many examples in this cla ss, relevant deforma-
tions of rational conformal ﬁeld theories.) Then, our classiﬁcation results can be translated
to physics side. We arrive the
Theorem. Let B be a pre-modular fusion category and A ∈ B a connected ´ etale algebra.
Suppose two-dimensional B-symmetric gapped phases are described by indecomposable BA’s.
Then, the gapped phases have
GSD ∈



{1} (B ≃ VectC),
{1, 2} (B ≃ Vec1
Z/ 2Z (two with (2 .6))),
{2} (B ≃ Vecα
Z/ 2Z (the other 14)) ,
{2} (B ≃ Fib),
{1, 3} (B ≃ Vec1
Z/ 3Z with hX = hY = 0),
{3} (B ≃ Vec1
Z/ 3Z with hX = hY = ± 1
3 ),
{3} (B ≃ Ising),
{1, 2, 3} (B ≃ Rep(S3) (two with ( dY , hY ) = (2 , 0)),
{3} (B ≃ Rep(S3) (the other six)) ,
{3} (B ≃ psu(2)5).
24
In particular, categorical symmetries B’s are spontaneously broken for
B ≃



Vecα
Z/ 2Z with ( dX, hX ) ⁄= (1, 0),
Fib,
Vec1
Z/ 3Z with hX = hY = ± 1
3 ,
Ising,
Non-symmetric Rep( S3),
Symmetric Rep( S3) with dY = −1,
psu(2)5.
Remark. As noted in [3] Example 6, commutativity of an algebra seems too str ong; a
numerical computation suggests an existence of two-dimensional B-symmetric gapped phase
described by BA with non-commutative connected separable algebra A ∈ B .
A Conformal dimensions of B ≃ Rep(S3)
There are two classes of pre-MFCs with fusion ring FR 3, 0
2 (or K(0, 1, 0, 1) in the notation of
[34]); both are degenerate, but one is symmetric and the other is no n-symmetric. In this
appendix, we compute conformal dimensions of them.
Symmetric Rep (S3). The symmetric Rep( S3) has S-matrix (in the basis {1, X, Y })
~S =


1 1 dY
1 1 dY
dY dY d2
Y

 .
(We used dX = 1.) Since the ( i, j) component is deﬁned by ~Si,j := tr( cbj ,b i · cbi,b j ) =∑ rank(B)
k=1 Ni,j
k e2πih k
e2πi (hi+hj ) dk, we can read oﬀ the conformal dimensions. The (2 , 3) component
says e2πih X = 1, or
hX = 0 (mod 1) . (A.1)
Similarly, the (3 , 3) component imposes d2
Y = 2e−4πih Y + e−2πih Y dY , or
hY = 0 (mod 1) . (A.2)
Non-symmetric Rep (S3). The non-symmetric Rep( S3) has S-matrix [34]
~S =


1 1 dY
1 1 dY
dY dY e−4πih Y (2 + e2πih Y dY )


25
with (3 , 3) component equals to ( −2). (We already used e2πih X = 1, or hX = 0 mod 1.)
Solving
−2 = e−4πih Y (2 + e2πih Y dY )
for dY = 2, −1, we ﬁnd
hX = 0, h Y =
{
1
3 , 2
3 (dY = 2),
no solution ( dY = −1), (mod 1) . (A.3)
The possibility hY = 1
3 is realized by even primaries in the ˆsu(2)4 WZW model, and another
hY = 2
3 is realized by rank three pre-modular fusion subcategory of MFC de scribing M(6, 5)
minimal model. Thus, both of them exist. For dY = −1, we naively get hY = 1
2π arccos 1
4 ,
however, this contradicts Vafa’s theorem [35]; ∃N ∈ N× such that
(
e2πih Y
) N
= 1. Thus,
we conclude non-symmetric pre-MFC with fusion ring K(Rep(S3)) must have dY = 2 and
hY = ± 1
3 mod 1.
B Conformal dimensions of B ≃ psu(2)5
By deﬁnition, the S-matrix in this example is given by (in the basis {1, X, Y })
~S =


1 dX dY
dX e−4πih X + e2πi (hY −2hX )dY e−2πih Y dX + e−2πih X dY
dY e−2πih Y dX + e−2πih X dY e−4πih Y + e2πi (hX −2hY )dX + e−2πih Y dY

 .
The S-matrix obeys ~Si∗,j = ~S∗
i,j . Since all simple objects are self-dual b∗ ∼= b, this means all
components should be real. This imposes three necessary condition s on conformal dimensions
hX, hY :
e−4πih X + e2πi (hY −2hX )dY
!
∈ R,
e−2πih Y dX + e−2πih X dY
!
∈ R,
e−4πih Y + e2πi (hX −2hY )dX + e−2πih Y dY
!
∈ R.
(B.1)
Solving the conditions for ( dX, dY ) = (
sin π
7
cos π
14
, −
sin 2π
7
cos π
14
), (−
sin 3π
7
cos 3π
14
,
sin π
7
cos 3π
14
), (
sin 2π
7
sin π
7
,
sin 3π
7
sin π
7
), one ﬁnds
(hX, hY ) =



( 3
7, 1
7), ( 4
7, 6
7 ) (1st quantum dimensions) ,
( 2
7, 3
7), ( 5
7, 4
7 ) (2nd quantum dimensions) ,
( 1
7, 5
7), ( 6
7, 2
7 ) (3rd quantum dimensions) .
(B.2)
Indeed, these conformal dimensions give known forms [9] of S-matrices, and the MFCs exist.
26
Naively, we also ﬁnd trivial conformal dimensions hX = 0 = hY (mod 1) satisfy the nec-
essary conditions. However, we can rule them out by a
Lemma. There does not exist a pre-modular fusion category with fusi on ring K(psu(2)5)
and trivial conformal dimension. In other words, all pre-mo dular fusion categories with fu-
sion ring K(psu(2)5) are modular.
Proof. Assume the opposite, and suppose there exist pre-MFCs with trivia l conformal
dimensions obeying the fusion ring K(psu(2)5). When conformal dimensions are trivial, they
turn out to be symmetric. For a symmetric fusion category B, there exists a ﬁnite group
G such that B ≃ Rep(G) [30]. The only possibilities in our case is G = Z/3Z, S3 [34], and
such symmetric fusion categories should have fusion rings K(Rep(Z/3Z)) or K(Rep(S3)) =
K(0, 1, 0, 1) (in the notation of the paper). However, the fusion ring of psu(2)5 is diﬀerent
from neither of them, leading to a contradiction. □
References
[1] P. Etingof, S. Gelaki, D. Nikshych and V. Ostrik, “Tensor Catego ries,” American Math-
ematical Society, 2015.
[2] A. Davydov, M. M¨ uger, D. Nikshych and V. Ostrik, “The Witt gro up of non-degenerate
braided fusion categories,” Journal f¨ ur die reine und angewandte Mathematik (Crelles
Journal), 2013(677), 135-177. https://doi.org/10.1515/crelle.2 012.014 [arXiv:1009.2117
[math.QA]].
[3] K. Kikuchi, “Ground state degeneracy and module category,” [ar Xiv:2311.00746 [hep-
th]].
[4] P. Etingof, D. Nikshych and V. Ostrik, “On fusion categories,” An nals of Mathematics
162, no. 2 (2005): 581–642. http://www.jstor.org/stable/2015 9926 [arXiv:math/0203060
[math.QA]].
[5] A. Kirillov Jr. and V. Ostrik, “ON A q-ANALOG OF THE MCKAY CORRE-
SPONDENCE AND THE ADE CLASSIFICATION OF slb2 CONFORMAL FIELD ,”
Advances in Mathematics 171(2002), 183-227. https://doi.org/1 0.1006/aima.2002.2072
[arXiv:math/0101219 [math.QA]].
[6] A. Kitaev, “Anyons in an exactly solved model and beyond,” Annals Phys. 321, no.1,
2-111 (2006) doi:10.1016/j.aop.2005.10.005 [arXiv:cond-mat/05064 38 [cond-mat.mes-
hall]].
27
[7] K. Fredenhagen, K. H. Rehren and B. Schroer, “Superselectio n sectors with braid group
statistics and exchange algebras. 2. Geometric aspects and conf ormal covariance,” Rev.
Math. Phys. 4, no.spec01, 113-157 (1992) doi:10.1142/S0129055X92000170
[8] V. Ostrik, “MODULE CATEGORIES, WEAK HOPF ALGEBRAS AND
MODULAR INV ARIANTS,” Transformation Groups 8, 177–206 (2003).
https://doi.org/10.1007/s00031-003-0515-6 [arXiv:math/01111 39 [math.QA]].
[9] E. Rowell, R. Stong, Z. Wang, “On classiﬁcation of modular tensor categories,” Commu-
nications in Mathematical Physics 292(2009), 343-389. https://d oi.org/10.1007/s00220-
009-0908-z [arXiv:0712.1377 [math.QA]].
[10] V. Ostrik, “Fusion categories of rank 2,” Mathematical Resear ch Letters 10 (2002): 177-
183. https://dx.doi.org/10.4310/MRL.2003.v10.n2.a5 [arXiv:math/0203255 [math.QA]].
[11] V. Ostrik, “Pivotal fusion categories of rank 3,” Mosc. Math. J ., 15(2015), 373–396.
https://doi.org/10.17323/1609-4514-2015-15-2-373-396 [arX iv:1309.4822 [math.QA]].
[12] “AnyonWiki,” https://anyonwiki.github.io/
[13] Z. Liu, S. Palcoux and Y. Ren, “Classiﬁcation of Grothendieck rin gs of complex fu-
sion categories of multiplicity one up to rank six,” Lett Math Phys 112, 54 (2022).
https://doi.org/10.1007/s11005-022-01542-1 [arXiv:2010.10264 [math.CT]].
[14] G. Vercleyen and J. Slingerland, “On Low Rank Fusion Rings,” [arX iv:2205.15637 [math-
ph]].
[15] T. Booker and A. Davydov, “Commutative Algebras in Fibonacci Categories,”
Journal of Algebra 355(2012), 176-204. https://doi.org/10.101 6/j.jalgebra.2011.12.029
[arXiv:1103.3537 [math.CT]].
[16] T. J. Hagge and S.-M. Hong, “Some non-braided fusion categor ies of
rank 3,” Communications in Contemporary Mathematics 11(2009), 6 15-637.
https://doi.org/10.1142/S0219199709003521 [arXiv:0704.0208 [ma th.GT]].
[17] V. Drinfeld, S. Gelaki, D. Nikshych and V. Ostrik, “On braided fus ion categories
I,” Selecta Mathematica 16(2010), 1-119. https://doi.org/10.100 7/s00029-010-0017-z
[arXiv:0906.0620 [math.QA]].
[18] D. Gepner and A. Kapustin, “On the classiﬁcation of fusion rings ,” Phys. Lett. B 349,
71-75 (1995) doi:10.1016/0370-2693(95)00172-H [arXiv:hep-th/ 9410089 [hep-th]].
[19] P. Bruillard, S.H. Ng, E.C. Rowell, and Z. Wang, “ON CLASSIFICATI ON OF MOD-
ULAR CATEGORIES BY RANK,” [arXiv:1507.05139 [math.QA]].
28
[20] A. Ocneanu, “The classiﬁcation of subgroups of quantum SU (N),” Quantum Sym-
metries in Theoretical Physics and Mathematics R. Coquereaux et a l (ed), American
Mathematical Society, Providence, 2002, pp.133–159.
[21] D. E. Evans and M. Pugh, “ SU (3)-Goodman-de la Harpe-Jones subfactors and the
realization of SU (3) modular invariants,” Rev. Math. Phys. 21 (2009), 877–928.
https://doi.org/10.1142/S0129055X09003761 [arXiv:0906.4252 [ma th.OA]].
[22] D. Copeland and C. Edie-Michell, “CELL SYSTEMS FOR Rep(Uq(slN ) ) MODULE
CATEGORIES,” [arXiv:2301.13172 [math.QA]].
[23] T. Gannon, “Exotic quantum subgroups and extensions of aﬃn e Lie algebra VOAs –
part I,” [arXiv:2301.07287 [math.QA]].
[24] C. Edie-Michell, “TYPE II QUANTUM SUBGROUPS OF slN . I: SYMMETR IES OF
LOCAL MODULES,” Communications of the American Mathematical Soc iety 3(2023),
112-165. https://doi.org/10.1090/cams/19 [arXiv:2102.09065 [mat h.QA]].
[25] J. Fuchs, I. Runkel and C. Schweigert, “TFT construction of RCFT cor-
relators. 2. Unoriented world sheets,” Nucl. Phys. B 678, 511-637 (2004)
doi:10.1016/j.nuclphysb.2003.11.026 [arXiv:hep-th/0306164 [hep-th ]].
[26] Y. Kawahigashi and R. Longo, “Classiﬁcation of local conforma l nets: Case c < 1,”
Annals Math. 160, 493-522 (2004) [arXiv:math-ph/0201015 [math-ph]].
[27] J. Fuchs, I. Runkel and C. Schweigert, “TFT construction of RCFT correlators 1. Parti-
tion functions,” Nucl. Phys. B 646, 353-497 (2002). doi:10.1016/S0550-3213(02)00744-7
[arXiv:hep-th/0204148 [hep-th]].
[28] D. Barter, J. C. Bridgeman and R. Wolf, “Computing associator s of endomorphism
fusion categories,” SciPost Phys. 13, 029 (2022) doi: 10.21468/Sc iPostPhys.13.2.029
[arXiv:2110.03644 [math.QA]].
[29] S. X. Cui, M. S. Zini and Z. Wang, “On generalized symmetries and structure of modular
categories,” Sci China Math, 62(2019), 417–446. https://doi.org /10.1007/s11425-018-
9455-5 [arXiv:1809.00245 [math.QA].
[30] P. Deligne, “Cat´ egories tensorielles,” Moscow Math. Journal 2 (2002) , 227-248.
https://doi.org/10.17323/1609-4514-2002-2-2-227-248
[31] K. Kikuchi, “Classiﬁcation of connected ´ etale algebras in multiplicity-free modular fusion
categories up to rank nine,” [arXiv:2404.16125 [math.QA]].
[32] R. Thorngren and Y. Wang, “Fusion Category Symmetry I: Ano maly In-Flow and
Gapped Phases,” [arXiv:1912.02817 [hep-th]].
29
[33] T. C. Huang, Y. H. Lin and S. Seifnashri, “Construction of two- dimensional
topological ﬁeld theories with non-invertible symmetries,” JHEP 12, 028 (2021)
doi:10.1007/JHEP12(2021)028 [arXiv:2110.02958 [hep-th]].
[34] V. Ostrik, “Pre-modular categories of rank 3,” Mosc. Math. J., 8(2008),
111–118. https://doi.org/10.17323/1609-4514-2008-8-1-111 -118 [arXiv:math/0503564
[math.QA]].
[35] C. Vafa, “Toward classiﬁcation of conformal theories,” Phys.L ett.B 206 (1988) 421–426.
https://doi.org/10.1016/0370-2693(88)91603-6
30
