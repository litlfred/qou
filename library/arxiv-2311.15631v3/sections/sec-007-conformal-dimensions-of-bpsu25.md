---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three"
section_id: sec-007-conformal-dimensions-of-bpsu25
section_title: "Conformal dimensions of Bpsu(2)5"
section_number: null
pages: 26-30
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
toc_source: outline
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three — We classify connected ´etale algebras A’s in pre-modular fusion categories B with rank(B) ≤3 including"
---
By deﬁnition, the S-matrix in this example is given by (in the basis {1, X, Y })
eS =


1
dX
dY
dX
e−4πihX + e2πi(hY −2hX)dY
e−2πihY dX + e−2πihXdY
dY
e−2πihY dX + e−2πihXdY
e−4πihY + e2πi(hX−2hY )dX + e−2πihY dY

.
The S-matrix obeys eSi∗,j = eS∗
i,j. Since all simple objects are self-dual b∗∼= b, this means all
components should be real. This imposes three necessary conditions on conformal dimensions
hX, hY :
e−4πihX + e2πi(hY −2hX)dY
!∈R,
e−2πihY dX + e−2πihXdY
!∈R,
e−4πihY + e2πi(hX−2hY )dX + e−2πihY dY
!∈R.
(B.1)
Solving the conditions for (dX, dY ) = (
sin π
7
cos π
14 , −
sin 2π
7
cos π
14 ), (−
sin 3π
7
cos 3π
14 ,
sin π
7
cos 3π
14 ), (
sin 2π
7
sin π
7 ,
sin 3π
7
sin π
7 ), one ﬁnds
(hX, hY ) =





( 3
7, 1
7), ( 4
7, 6
7)
(1st quantum dimensions),
( 2
7, 3
7), ( 5
7, 4
7)
(2nd quantum dimensions),
( 1
7, 5
7), ( 6
7, 2
7)
(3rd quantum dimensions).
(B.2)
Indeed, these conformal dimensions give known forms [9] of S-matrices, and the MFCs exist.
26
Naively, we also ﬁnd trivial conformal dimensions hX = 0 = hY (mod 1) satisfy the nec-
essary conditions. However, we can rule them out by a
Lemma. There does not exist a pre-modular fusion category with fusion ring K(psu(2)5)
and trivial conformal dimension. In other words, all pre-modular fusion categories with fu-
sion ring K(psu(2)5) are modular.
Proof. Assume the opposite, and suppose there exist pre-MFCs with trivial conformal
dimensions obeying the fusion ring K(psu(2)5). When conformal dimensions are trivial, they
turn out to be symmetric. For a symmetric fusion category B, there exists a ﬁnite group
G such that B ≃Rep(G) [30]. The only possibilities in our case is G = Z/3Z, S3 [34], and
such symmetric fusion categories should have fusion rings K(Rep(Z/3Z)) or K(Rep(S3)) =
K(0, 1, 0, 1) (in the notation of the paper). However, the fusion ring of psu(2)5 is diﬀerent
from neither of them, leading to a contradiction. □
References
[1] P. Etingof, S. Gelaki, D. Nikshych and V. Ostrik, “Tensor Categories,” American Math-
ematical Society, 2015.
[2] A. Davydov, M. M¨uger, D. Nikshych and V. Ostrik, “The Witt group of non-degenerate
braided fusion categories,” Journal f¨ur die reine und angewandte Mathematik (Crelles
Journal), 2013(677), 135-177. https://doi.org/10.1515/crelle.2012.014 [arXiv:1009.2117
[math.QA]].
[3] K. Kikuchi, “Ground state degeneracy and module category,” [arXiv:2311.00746 [hep-
th]].
[4] P. Etingof, D. Nikshych and V. Ostrik, “On fusion categories,” Annals of Mathematics
162, no. 2 (2005): 581–642. http://www.jstor.org/stable/20159926 [arXiv:math/0203060
[math.QA]].
[5] A. Kirillov Jr. and V. Ostrik, “ON A q-ANALOG OF THE MCKAY CORRE-
SPONDENCE AND THE ADE CLASSIFICATION OF slb2 CONFORMAL FIELD,”
Advances in Mathematics 171(2002), 183-227. https://doi.org/10.1006/aima.2002.2072
[arXiv:math/0101219 [math.QA]].
[6] A. Kitaev, “Anyons in an exactly solved model and beyond,” Annals Phys. 321, no.1,
2-111 (2006) doi:10.1016/j.aop.2005.10.005 [arXiv:cond-mat/0506438 [cond-mat.mes-
hall]].
27
[7] K. Fredenhagen, K. H. Rehren and B. Schroer, “Superselection sectors with braid group
statistics and exchange algebras. 2. Geometric aspects and conformal covariance,” Rev.
Math. Phys. 4, no.spec01, 113-157 (1992) doi:10.1142/S0129055X92000170
[8] V.
Ostrik,
“MODULE
CATEGORIES,
WEAK
HOPF
ALGEBRAS
AND
MODULAR
INVARIANTS,”
Transformation
Groups
8,
177–206
(2003).
https://doi.org/10.1007/s00031-003-0515-6 [arXiv:math/0111139 [math.QA]].
[9] E. Rowell, R. Stong, Z. Wang, “On classiﬁcation of modular tensor categories,” Commu-
nications in Mathematical Physics 292(2009), 343-389. https://doi.org/10.1007/s00220-
009-0908-z [arXiv:0712.1377 [math.QA]].
[10] V. Ostrik, “Fusion categories of rank 2,” Mathematical Research Letters 10 (2002): 177-
183. https://dx.doi.org/10.4310/MRL.2003.v10.n2.a5 [arXiv:math/0203255 [math.QA]].
[11] V. Ostrik, “Pivotal fusion categories of rank 3,” Mosc. Math. J., 15(2015), 373–396.
https://doi.org/10.17323/1609-4514-2015-15-2-373-396 [arXiv:1309.4822 [math.QA]].
[12] “AnyonWiki,” https://anyonwiki.github.io/
[13] Z. Liu, S. Palcoux and Y. Ren, “Classiﬁcation of Grothendieck rings of complex fu-
sion categories of multiplicity one up to rank six,” Lett Math Phys 112, 54 (2022).
https://doi.org/10.1007/s11005-022-01542-1 [arXiv:2010.10264 [math.CT]].
[14] G. Vercleyen and J. Slingerland, “On Low Rank Fusion Rings,” [arXiv:2205.15637 [math-
ph]].
[15] T. Booker and A. Davydov,
“Commutative Algebras in Fibonacci Categories,”
Journal of Algebra 355(2012), 176-204. https://doi.org/10.1016/j.jalgebra.2011.12.029
[arXiv:1103.3537 [math.CT]].
[16] T.
J.
Hagge
and
S.-M.
Hong,
“Some
non-braided
fusion
categories
of
rank
3,”
Communications
in
Contemporary
Mathematics
11(2009),
615-637.
https://doi.org/10.1142/S0219199709003521 [arXiv:0704.0208 [math.GT]].
[17] V. Drinfeld, S. Gelaki, D. Nikshych and V. Ostrik, “On braided fusion categories
I,” Selecta Mathematica 16(2010), 1-119. https://doi.org/10.1007/s00029-010-0017-z
[arXiv:0906.0620 [math.QA]].
[18] D. Gepner and A. Kapustin, “On the classiﬁcation of fusion rings,” Phys. Lett. B 349,
71-75 (1995) doi:10.1016/0370-2693(95)00172-H [arXiv:hep-th/9410089 [hep-th]].
[19] P. Bruillard, S.H. Ng, E.C. Rowell, and Z. Wang, “ON CLASSIFICATION OF MOD-
ULAR CATEGORIES BY RANK,” [arXiv:1507.05139 [math.QA]].
28
[20] A. Ocneanu, “The classiﬁcation of subgroups of quantum SU(N),” Quantum Sym-
metries in Theoretical Physics and Mathematics R. Coquereaux et al (ed), American
Mathematical Society, Providence, 2002, pp.133–159.
[21] D. E. Evans and M. Pugh, “SU(3)-Goodman-de la Harpe-Jones subfactors and the
realization of SU(3) modular invariants,” Rev. Math. Phys. 21 (2009), 877–928.
https://doi.org/10.1142/S0129055X09003761 [arXiv:0906.4252 [math.OA]].
[22] D. Copeland and C. Edie-Michell, “CELL SYSTEMS FOR Rep(Uq(slN )) MODULE
CATEGORIES,” [arXiv:2301.13172 [math.QA]].
[23] T. Gannon, “Exotic quantum subgroups and extensions of aﬃne Lie algebra VOAs –
part I,” [arXiv:2301.07287 [math.QA]].
[24] C. Edie-Michell, “TYPE II QUANTUM SUBGROUPS OF slN . I: SYMMETRIES OF
LOCAL MODULES,” Communications of the American Mathematical Society 3(2023),
112-165. https://doi.org/10.1090/cams/19 [arXiv:2102.09065 [math.QA]].
[25] J.
Fuchs,
I.
Runkel
and
C.
Schweigert,
“TFT
construction
of
RCFT
cor-
relators.
2.
Unoriented
world
sheets,”
Nucl.
Phys.
B
678,
511-637
(2004)
doi:10.1016/j.nuclphysb.2003.11.026 [arXiv:hep-th/0306164 [hep-th]].
[26] Y. Kawahigashi and R. Longo, “Classiﬁcation of local conformal nets: Case c < 1,”
Annals Math. 160, 493-522 (2004) [arXiv:math-ph/0201015 [math-ph]].
[27] J. Fuchs, I. Runkel and C. Schweigert, “TFT construction of RCFT correlators 1. Parti-
tion functions,” Nucl. Phys. B 646, 353-497 (2002). doi:10.1016/S0550-3213(02)00744-7
[arXiv:hep-th/0204148 [hep-th]].
[28] D. Barter, J. C. Bridgeman and R. Wolf, “Computing associators of endomorphism
fusion categories,” SciPost Phys. 13, 029 (2022) doi: 10.21468/SciPostPhys.13.2.029
[arXiv:2110.03644 [math.QA]].
[29] S. X. Cui, M. S. Zini and Z. Wang, “On generalized symmetries and structure of modular
categories,” Sci China Math, 62(2019), 417–446. https://doi.org/10.1007/s11425-018-
9455-5 [arXiv:1809.00245 [math.QA].
[30] P. Deligne, “Cat´egories tensorielles,” Moscow Math. Journal 2(2002) , 227-248.
https://doi.org/10.17323/1609-4514-2002-2-2-227-248
[31] K. Kikuchi, “Classiﬁcation of connected ´etale algebras in multiplicity-free modular fusion
categories up to rank nine,” [arXiv:2404.16125 [math.QA]].
[32] R. Thorngren and Y. Wang, “Fusion Category Symmetry I: Anomaly In-Flow and
Gapped Phases,” [arXiv:1912.02817 [hep-th]].
29
[33] T. C. Huang,
Y. H. Lin and S. Seifnashri,
“Construction of two-dimensional
topological ﬁeld theories with non-invertible symmetries,” JHEP 12, 028 (2021)
doi:10.1007/JHEP12(2021)028 [arXiv:2110.02958 [hep-th]].
[34] V.
Ostrik,
“Pre-modular
categories
of
rank
3,”
Mosc.
Math.
J.,
8(2008),
111–118.
https://doi.org/10.17323/1609-4514-2008-8-1-111-118 [arXiv:math/0503564
[math.QA]].
[35] C. Vafa, “Toward classiﬁcation of conformal theories,” Phys.Lett.B 206 (1988) 421–426.
https://doi.org/10.1016/0370-2693(88)91603-6
30
