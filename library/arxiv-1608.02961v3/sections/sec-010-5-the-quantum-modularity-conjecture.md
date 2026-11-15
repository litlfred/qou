---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-010-5-the-quantum-modularity-conjecture
section_title: "The Quantum Modularity Conjecture"
section_number: 5
pages: 22-33
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
The Quantum Modularity Conjecture
Our ﬁnal topic concerns the relation between complex Chern-Simons theory and Zagier’s
Quantum Modularity Conjecture (QMC) [36]. Strictly speaking, the QMC concerns certain
limits of colored Jones polynomials of knots in S3. Physically, colored Jones polynomials
have to do with SU(2) Chern-Simons theory. However, by embedding SU(2) theory into a
holomorphic sector of SL(2, C) theory, one can use complex Chern-Simons theory to study
the very same limits [35]. Moreover, SL(2, C) theory and its various stringy realizations may
have a chance of explaining some of the subtler aspects of the conjecture.
To formulate a precise statement, we begin by recalling that the colored Jones polynomials
JK(N, q) of a knot K ⊂S3 are expectation values in SU(2) Chern-Simons theory of Wilson
loops in the N-dimensional representation [104, 105, 17]. Physically, the parameter q =
exp 2πi
k encodes the renormalized level k ∈Z of the SU(2) theory, but (as the name suggest)
the Jones polynomials can be analytically continued to Laurent polynomials in a formal
22
variable q. For any k-th root of unity qk = 1, the Jones polynomials are periodic JK(N, q) =
JK(N + k, q).
The colored Jones polynomials can equivalently be deﬁned using the wavefunction of
SU(2) Chern-Simons at renormalized level k on the knot complement M = S3\K. (The
bare level appearing in the Lagrangian is k −2.)
Recall, e.g. from Section 2, that the
Hilbert space H[T 2]k in compact Chern-Simons theory is k −1 dimensional. The SU(2)
wavefunction Z[M]k is thus a vector in Ck−1, whose components are precisely the Jones
polynomials JK(1, e
2πi
k ), JK(2, e
2πi
k ), ..., JK(k −1, e
2πi
k ).
For any rational number α = a/c, Zagier deﬁnes
JK(α) := JK(c, e
2πia
c ) .
(5.1)
Crucially, this is just outside the natural range of states in SU(2) Chern-Simons at renor-
malized level c, hinting that some analytic continuation will be necessary for a physical
interpretation of (5.1) (just like it was in the Volume Conjecture).
The QMF states in part that JK(α) shows exponential growth as α tends to any ﬁxed
rational number α0 through rational values, with the rate of growth governed by the hyper-
bolic volume of M = S3\K. Speciﬁcally, let ( a b
c d ) ∈SL(2, Z) with c > 0, and let X →∞
in a ﬁxed coset of Q/Z (for example: X = 1, 2, 4, 5, ... or X =
3
4, 7
4, 11
4 , ... with constant
denominators). Set ℏ= 2πi/(cX +d). Then, conjecturally, there is an asymptotic expansion
JK
aX + b
cX + d

∼JK(X)
2πi
ℏ
 3
2
e
1
cℏSCS(geom)φK,a/c(ℏ) ,
(5.2)
where SCS(geom) = CS(M) + iVol(M) is the volume of the geometric ﬂat connection on M,
containing the hyperbolic volume as in Section 4.1; and φK,a/c(ℏ) is a formal power series in
ℏthat depends only on a/c mod 1. Moreover, it was conjectured that after dividing by the
leading coeﬃcient to make eφK,a/c(ℏ) = φK,a/c(ℏ)/φK,a/c(0) monic, the subleading coeﬃcients
all belong to the trace ﬁeld of K adjoined a c-th root of unity ΓK(e
2πia
c ). (The number ﬁeld
ΓK contains the traces of all holonomies of the geometric ﬂat SL(2, C) connection on M.)
For ( a b
c d ) = ( 0 −1
1
0 ) and X = 1, 2, 3, ... ∈N, the QMC (5.2) reduces to the usual Volume
Conjecture.13 Heuristically, one may think of the Volume Conjecture as studying a limit of
colored Jones polynomials as q →1, and the QMC as studying limits where q approaches
all the rational points on the unit circle.
In order to embed the QMC in SL(2, C) Chern-Simons theory, one can consider singular
limits very similar to (4.3).14 Namely, it was argued in [35] that when ﬁxing the integer level
k and sending s →−ik in complex Chern-Simons theory, or equivalently (k + is, k −is) →
13The number-theoretic properties of the asymptotic expansion in the Volume Conjecture were explored
from a physical perspective in [49], leading to the notion of an Arithmetic Quantum Field Theory.
14There may be other ways to embed the QMC into complex Chern-Simons theory. It was proposed in
[106] that setting (k +is, k −is) →(a, c) to ﬁnite integer values, which is a perfectly regular limit in complex
Chern-Simons, may also be related to the QMC.
23
(2k, 0), the knot-complement partition function has an asymptotic expansion
Z[M]k,s
s→−ik
∼
2πi
ℏ
 3
2
e
1
kℏSCS(geom)φK,1/k(ℏ) ,
ℏ= 2πik −is
k + is
(5.3)
with the same series as in (5.2). Using the state-sum construction (4.6) (on one hand) and
detailed computations of Garoufalidis and Zagier for asymptotics of colored Jones polyno-
mials (on the other hand), the agreement between (5.2) and (5.3) was veriﬁed in dozens of
examples. By performing a saddle-point expansion of the state-sum model, one also deduces
that coeﬃcients of eφK,1/k(ℏ) lie in the number ﬁeld ΓK(e
2πi
k ) as desired.
In terms of the 3d-3d correspondence, the singular limit in (5.3) corresponds to computing
the partition function of T[M] on a squashed lens space L(k, 1)b ≃S3
b /Zk, and sending to
zero the squashing parameter b2 →0. The 1/k dependence in the leading asymptotic can be
explained from the simple fact that the lens space is a k-fold quotient of the three-sphere.
It would be interesting to make further physical predictions for the QMC by relating the
partition functions of T[M] on diﬀerent lens spaces L(k, 1)b, or more generally L(c, a)b.
−3
−2
−1
1
2
3
4
1
2
3
4
log(JK(↵)/JK(1/↵))
↵
Figure 5.1: The graph of JK(α)/JK(1/α) when K is the ﬁgure-eight knot, from [36].
Another observation of [36] is that, for hyperbolic several knots, the ratio JK(α)/JK(γ(α))
for γ ∈SL(2, Z) has some very interesting ﬁnite behavior. This ratio measures the failure of
JK(α) to be truly “modular.” For the ﬁgure-eight knot, a graph of this function appears in
[36, Fig. 4], reproduced above. The graph is almost monotonic (it violates monotonicity at
24
a very ﬁne scales) and discontinuous at all rational points a/c, the size of the discontinuity
being roughly proportional to the denominator |c|.
If we turn this graph on its side, any condensed matter theorist would recognize it imme-
diately: it is the plot of Hall resistivity as a function of magnetic ﬁeld in a two-dimensional
electron system. The plot has plateaus at rational points, due to the fractional quantum Hall
eﬀect. It is extremely tempting to think that this must be related to the eﬀective complex
Chern-Simons theory in quantum-Hall systems [42]; the connection is investigated in [54].
Acknowledgements
I am grateful to Stavros Garoufalidis, Sergei Gukov, Neil Hoﬀman, Craig Hodgson, Hyam
Rubinstein, Daniel Jaﬀeris, and Cumrun Vafa for many insightful discussions on the themes
that entered this review.
References
[1] V. Pestun and M. Zabzine, eds., Localization techniques in quantum ﬁeld theory,
vol. xx. Journal of Physics A, 2016. 1608.02952.
https://arxiv.org/src/1608.02952/anc/LocQFT.pdf,
http://pestun.ihes.fr/pages/LocalizationReview/LocQFT.pdf.
[2] A. Achucarro and P. K. Townsend, “A Chern-Simons action for three-dimensional
anti-de Sitter supergravity theories,” Phys. Lett. B180 (1986) 89–92.
[3] E. Witten, “2+1 Dimensional Gravity as an Exactly Soluble System,” Nucl. Phys.
B311 (1988) no. 1, 46–78. http:
//www.ams.org/mathscinet/search/publications.html?pg1=MR&s1=MR974271.
[4] E. Witten, “Topology-Changing Amplitudes in (2+1)-Dimensional Gravity,” Nucl.
Phys. B323 (1989) 113. http://adsabs.harvard.edu/abs/1989NuPhB.323..113W.
[5] E. Witten, “Quantization of Chern-Simons Gauge Theory with Complex Gauge
Group,” Comm. Math. Phys 137 (1991) 29–66.
[6] A. Campoleoni, S. Fredenhagen, S. Pfenninger, and S. Theisen, “Asymptotic
symmetries of three-dimensional gravity coupled to higher-spin ﬁelds,” JHEP 1011
(2010) 007, 1008.4744v2. http://arxiv.org/abs/1008.4744v2.
[7] M. R. Gaberdiel and R. Gopakumar, “Minimal Model Holography,” J. Phys. A46
(2013) 214002, 1207.6697v2. http://arxiv.org/abs/1207.6697v2.
[8] C. Cordova and D. L. Jaﬀeris, “Complex Chern-Simons from M5-branes on the
Squashed Three-Sphere,” 1305.2891v1. http://arxiv.org/abs/1305.2891v1.
25
[9] S. Lee and M. Yamazaki, “3d Chern-Simons Theory from M5-branes,” JHEP 1312
(2013) 035, 1305.2429v2. http://arxiv.org/abs/1305.2429v2.
[10] J. Yagi, “3d TQFT from 6d SCFT,” JHEP 1308 (2013) 017, 1305.0291v1.
http://arxiv.org/abs/1305.0291v1.
[11] T. Dimofte, S. Gukov, and L. Hollands, “Vortex Counting and Lagrangian
3-manifolds,” Lett. Math. Phys. 98 (2011) 225–287, 1006.0977v1.
http://arxiv.org/abs/1006.0977v1.
[12] T. Dimofte and S. Gukov, “Chern-Simons Theory and S-duality,” JHEP 1305 (2013)
109, 1106.4550v1. http://arxiv.org/abs/1106.4550v1.
[13] Y. Terashima and M. Yamazaki, “SL(2,R) Chern-Simons, Liouville, and Gauge
Theory on Duality Walls,” JHEP 1108 (2011) 135, 1103.5748v1.
http://arxiv.org/abs/1103.5748v1.
[14] T. Dimofte, D. Gaiotto, and S. Gukov, “Gauge Theories Labelled by
Three-Manifolds,” Comm. Math. Phys. 325 (2014) 367–419, 1108.4389v1.
http://arxiv.org/abs/1108.4389v1.
[15] L. F. Alday, D. Gaiotto, and Y. Tachikawa, “Liouville Correlation Functions from
Four-Dimensional Gauge Theories,” Lett. Math. Phys. 91 (2010) no. 2, 167–197,
0906.3219v1. http://arxiv.org/abs/0906.3219v1.
[16] A. Gadde, S. Gukov, and P. Putrov, “Fivebranes and 4-manifolds,” 1306.4320v1.
http://arxiv.org/abs/1306.4320v1.
[17] E. Witten, “Quantum Field Theory and the Jones Polynomial,” Comm. Math. Phys.
121 (1989) no. 3, 351–399.
[18] N. Reshetikhin and V. Turaev, “Invariants of 3-manifolds via link polynomials and
quantum groups,” Invent. Math. 103 (1991) no. 3, 547–597.
http://www.springerlink.com/index/U416971M947560R7.pdf.
[19] J. E. Andersen and R. Kashaev, “A TQFT from quantum Teichm¨uller theory,”
1109.6295v1. http://arxiv.org/abs/1109.6295v1.
[20] T. Dimofte, D. Gaiotto, and S. Gukov, “3-Manifolds and 3d Indices,” Adv. Theor.
Math. Phys. 17 (2013) 975–1076, 1112.5179v1.
http://arxiv.org/abs/1112.5179v1.
[21] J. E. Andersen and R. Kashaev, “Complex Quantum Chern-Simons,” 1409.1208v1.
http://arxiv.org/abs/1409.1208v1.
[22] T. Dimofte, “Complex Chern-Simons theory at level k via the 3d-3d
correspondence,” Comm. Math. Phys. 339 (2015) no. 2, 619–662, 1409.0857v1.
http://arxiv.org/abs/1409.0857v1.
26
[23] S. Gukov and D. Pei, “Equivariant Verlinde formula from ﬁvebranes and vortices,”
1501.01310v1. http://arxiv.org/abs/1501.01310v1.
[24] D. Pei and K. Ye, “A 3d-3d appetizer,” 1503.04809v1.
http://arxiv.org/abs/1503.04809v1.
[25] S. Gukov, “Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the
A-Polynomial,” Commun. Math. Phys. 255 (2005) no. 3, 577–627,
hep-th/0306165v1. http://arxiv.org/abs/hep-th/0306165v1.
[26] R. M. Kashaev, “The hyperbolic volume of knots from quantum dilogarithm,” Lett.
Math. Phys. 39 (1997) 269–265, q-alg/9601025v2.
http://arxiv.org/abs/q-alg/9601025v2.
[27] H. Murakami and J. Murakami, “The colored Jones polynomials and the simplicial
volume of a knot,” Acta Math. 186 (2001) no. 1, 85–104, math/9905075v2.
http://arxiv.org/abs/math/9905075v2.
[28] E. Witten, “Analytic Continuation of Chern-Simons Theory,” Chern-Simons gauge
theory: 20 Years After (AMS/IP Stud. Adv. Math.) (2011) 347–446, 1001.2933v2.
http://arxiv.org/abs/1001.2933v4.
[29] R. Dijkgraaf and H. Fuji, “The Volume Conjecture and Topological Strings,”
Fortschr. Phys. 57 (2009) no. 9, 825–856, 0903.2084v2.
http://arxiv.org/abs/0903.2084v2.
[30] S. Gukov and P. Su lkowski, “A-polynomial, B-model, and Quantization,” JHEP
1202 (2012) 070, 1108.0002v1. http://arxiv.org/abs/1108.0002v1.
[31] G. Borot and B. Eynard, “All-order asymptotics of hyperbolic knot invariants from
non-perturbative topological recursion of A-polynomials,” 1205.2261v2.
http://arxiv.org/abs/1205.2261v2.
[32] B. Eynard and N. Orantin, “Invariants of Algebraic Curves and Topological
Expansion,” Commun. Number Theory Phys. 1 (2007) no. 2, 347–452,
math-ph/0702045v4. http://arxiv.org/abs/math-ph/0702045v4.
[33] H. Fuji, S. Gukov, and P. Su lkowski, “Volume Conjecture: Reﬁned and Categoriﬁed,”
1203.2182v1. http://arxiv.org/abs/1203.2182v1.
[34] S. Gukov, P. Putrov, and C. Vafa, “Fivebranes and 3-manifold homology,”
1602.05302v1. http://arxiv.org/abs/1602.05302v1.
[35] T. Dimofte and S. Garoufalidis, “Quantum modularity and complex Chern-Simons
theory,” 1511.05628v1. http://arxiv.org/abs/1511.05628v1.
27
[36] D. Zagier, “Quantum Modular Forms,” Quanta of Maths, Clay Math. Proc. 11
(2010) 659–675. AMS, Prividence, RI.
[37] Y. Terashima and M. Yamazaki, “3d N=2 Theories from Cluster Algebras,” PTEP
023 (2014) B01, 1301.5902v1. http://arxiv.org/abs/1301.5902v1.
[38] T. Dimofte, M. Gabella, and A. B. Goncharov, “K-Decompositions and 3d Gauge
Theories,” 1301.0192v1. http://arxiv.org/abs/1301.0192v1.
[39] L. Chekhov and V. V. Fock, “Quantum Teichm¨uller Space,” Theoret. and Math.
Phys. 120 (1999) no. 3, 1245–1259, math/9908165v2.
http://arxiv.org/abs/math/9908165v2.
[40] R. M. Kashaev, “Quantization of Teichm¨uller Spaces and the Quantum
Dilogarithm,” Lett. Math. Phys. 43 (1998) no. 2, 105–115. http:
//www.ams.org/mathscinet/search/publications.html?pg1=MR&s1=MR1607296.
[41] V. V. Fock and A. B. Goncharov, “Cluster ensembles, quantization and the
dilogarithm,” Annales Scientiﬁques L’Ecole Normal Superier, 4-e series t.42 (2009)
865–930, math/0311245v5. http://arxiv.org/abs/math/0311245v5.
[42] C. Vafa, “Fractional Quantum Hall Eﬀect and M-Theory,” 1511.03372v3.
http://arxiv.org/abs/1511.03372v3.
[43] M. Atiyah, “Geometry and Physics of Knots,” Cambridge Univ. Press, Cambridge
(1990) 78pp. http://books.google.com/books?hl=en&lr=&id=lOWaaHA5rBcC&oi=
fnd&pg=PA291&dq=%2522atiyah%2522+%2522knots%2522&ots=55BgFRpwVT&sig=
1Rg8AWBVtC1ibLt7986jgkmK4Vw.
[44] H.-J. Chung, T. Dimofte, S. Gukov, and P. Su lkowski, “3d-3d Correspondence
Revisited,” 1405.3663v1. http://arxiv.org/abs/1405.3663v1.
[45] S. Garoufalidis, C. Hodgson, N. Hoﬀman, and H. Rubinstein, “The 3D-index and
normal surfaces,” arXiv:1604.02688 [math.GT].
[46] T. Dumitrescu, “An Introduction to Supersymmetric Field Theories in Curved
Space,” Journal of Physics A xx (2016) 000, 1608.02957.
[47] B. Willett, “Localization on three-dimensional manifolds,” Journal of Physics A xx
(2016) 000, 1608.02958.
[48] J. E. Andersen and N. L. Gammelgaard, “The Hitchin-Witten Connection and
Complex Quantum Chern-Simons Theory,” 1409.1035v1.
http://arxiv.org/abs/1409.1035v1.
[49] T. Dimofte, S. Gukov, J. Lenells, and D. Zagier, “Exact Results for Perturbative
Chern-Simons Theory with Complex Gauge Group,” Comm. Num. Thy. and Phys. 3
(2009) no. 2, 363–443, 0903.2472v1. http://arxiv.org/abs/0903.2472v1.
28
[50] S. Gukov and E. Witten, “Branes and Quantization,” Adv. Theor. Math. Phys. 13
(2009) no. 5, 1445–1518, 0809.0305v2. http://arxiv.org/abs/0809.0305v2.
[51] S. Gukov, “Quantization via Mirror Symmetry,” 1011.2218v1.
http://arxiv.org/abs/1011.2218v1.
[52] N. Hitchin, “The self-duality equations on a Riemann surface,” Proc. London Math.
Soc (1987) . http://plms.oxfordjournals.org/cgi/reprint/s3-55/1/59.pdf.
[53] S. Axelrod, S. D. Pietra, and E. Witten, “Geometric Quantization of Chern-Simons
Gauge Theory,” J. Diﬀ. Geom. 33 (1991) no. 3, 787–902. http:
//www.ams.org/mathscinet/search/publications.html?pg1=MR&s1=MR1100212.
[54] T. Dimofte, S. Gukov, and C. Vafa, “Work in progress,”.
[55] T. Nishioka and Y. Tachikawa, “Para-Liouville/Toda central charges from
M5-branes,” Phys. Rev. D84 (2011) 046009, 1106.1172v1.
http://arxiv.org/abs/1106.1172v1.
[56] C. Cordova and D. L. Jaﬀeris, “Toda Theory From Six Dimensions,”
arXiv:1605.03997 [hep-th].
[57] C. Beem, T. Dimofte, and S. Pasquetti, “Holomorphic Blocks in Three Dimensions,”
1211.1986v1. http://arxiv.org/abs/1211.1986v1.
[58] G. Mostow, “Strong Rigidity of Locally Symmetric Spaces,” Ann. Math. Studies,
Princeton Univ. Press, Princeton, NJ 78 (1973) . http://books.google.com/
books?hl=en&lr=&id=xT0SFmrFrWoC&oi=fnd&pg=PA3&dq=%2522mostow%2522+
%2522strong%2522&ots=kACCabOaTW&sig=igChC-yXFJUQLgjr8FoYi6YU5jc.
[59] W. Thurston, “The Geometry and Topology of Three-Manifolds,” Lecture notes at
Princeton University (1980) . http://pi.unl.edu/~mbrittenham2/classwk/
990s08/public/thurston.notes.pdf/6a.pdf.
[60] T. Dimofte, “3d Superconformal Theories from Three-Manifolds,” Math. Phys. Stud.
9783319187693 (2016) 339–373, 1412.7129v1.
http://arxiv.org/abs/1412.7129v1. J. Teschner, ed.
[61] D. Gang, N. Kim, M. Romo, and M. Yamazaki, “Aspects of Defects in 3d-3d
Correspondence,” 1510.05011v1. http://arxiv.org/abs/1510.05011v1.
[62] D. Gaiotto, “N=2 dualities,” JHEP 1208 (2012) 034, 0904.2715v1.
http://arxiv.org/abs/0904.2715v1.
[63] D. Gaiotto, G. W. Moore, and A. Neitzke, “Four-dimensional wall-crossing via
three-dimensional ﬁeld theory,” Comm. Math. Phys. 299 (2010) no. 1, 163–224,
0807.4723v1. http://arxiv.org/abs/0807.4723v1.
29
[64] S. Cecotti, C. Cordova, and C. Vafa, “Braids, Walls, and Mirrors,” 1110.2115v1.
http://arxiv.org/abs/1110.2115v1.
[65] C. Cordova, S. Espahbodi, B. Haghighat, A. Rastogi, and C. Vafa, “Tangles,
Generalized Reidemeister Moves, and Three-Dimensional Mirror Symmetry,”
1211.3730v1. http://arxiv.org/abs/1211.3730v1.
[66] M. Aganagic and S. Shakirov, “Knot Homology from Reﬁned Chern-Simons Theory,”
1105.5117v1. http://arxiv.org/abs/1105.5117v1.
[67] S. Gukov and H. Murakami, “SL(2,C) Chern-Simons theory and the asymptotic
behavior of the colored Jones polynomial,” Lett. Math. Phys. 86 (2008) no. 2-3,
79–98, math/0608324v2. http://arxiv.org/abs/math/0608324v2.
[68] D. B. Ray and I. M. Singer, “R-torsion and the Laplacian on Riemannian manifolds,”
Adv. in Math. 7 (1971) 145–210. http:
//www.ams.org/mathscinet/search/publications.html?pg1=MR&s1=MR0295381.
[69] D. Bar-Natan and E. Witten, “Perturbative expansion of Chern-Simons theory with
non-compact gauge group,” Comm. Math. Phys. 141 (1991) no. 2, 423–440.
http://www.springerlink.com/index/G417376W368T0806.pdf.
[70] J. Cheeger and J. Simons, “Diﬀerential characters and geometric invariants,” Lecture
Notes in Math. 1167 (1985) 50–80. Springer, Berlin.
[71] S.-S. Chern and J. Simons, “Characteristic forms and geometric invariants,” Ann. of
Math 99 (1974) no. 2, 48–69.
[72] K. Hikami, “Generalized Volume Conjecture and the A-Polynomials - the
Neumann-Zagier Potential Function as a Classical Limit of Quantum Invariant,” J.
Geom. Phys. 57 (2007) no. 9, 1895–1940, math/0604094v1.
http://arxiv.org/abs/math/0604094v1.
[73] T. D. Dimofte and S. Garoufalidis, “The quantum content of the gluing equations,”
Geom. Topol. 17 (2013) no. 3, 1253–1315, 1202.6268v1.
http://arxiv.org/abs/1202.6268v1.
[74] M. Henningson and K. Skenderis, “The Holographic Weyl anomaly,” JHEP 9807
(1998) 023, hep-th/9806087v2. http://arxiv.org/abs/hep-th/9806087v2.
[75] J. A. Harvey, R. Minasian, and G. Moore, “Non-abelian Tensor-multiplet
Anomalies,” JHEP 9809 (1998) 004, hep-th/9808060v1.
http://arxiv.org/abs/hep-th/9808060v1.
[76] J. P. Gauntlett, N. Kim, and D. Waldram, “M-Fivebranes Wrapped on
Supersymmetric Cycles,” Phys. Rev. D63 (2001) 126001, hep-th/0012195v2.
http://arxiv.org/abs/hep-th/0012195v2.
30
[77] S. Garoufalidis, D. P. Thurston, and C. K. Zickert, “The complex volume of
SL(n,C)-representations of 3-manifolds,” 1111.2828v1.
http://arxiv.org/abs/1111.2828v1.
[78] D. Martelli, A. Passias, and J. Sparks, “The gravity dual of supersymmetric gauge
theories on a squashed three-sphere,” Nucl. Phys. B864 (2012) 840–868,
1110.6400v3. http://arxiv.org/abs/1110.6400v3.
[79] D. Gang, N. Kim, and S. Lee, “Holography of 3d-3d correspondence at Large N,”
JHEP 1504 (2015) 091, 1409.6206v1. http://arxiv.org/abs/1409.6206v1.
[80] P. Menal-Ferrer and J. Porti, “Higher dimensional Reidemeister torsion invariants for
cusped hyperbolic 3-manifolds,” J. of Topol. 7 (2014) no. 1, 69–119, 1110.3718v2.
http://arxiv.org/abs/1110.3718v2.
[81] S. Garoufalidis, “The 3D index of an ideal triangulation and angle structures,”
1208.1663v1. http://arxiv.org/abs/1208.1663v1.
[82] S. Garoufalidis, C. D. Hodgson, J. H. Rubinstein, and H. Segerman, “1-eﬃcient
triangulations and the index of a cusped hyperbolic 3-manifold,” 1303.5278v1.
http://arxiv.org/abs/1303.5278v1.
[83] T. Dimofte, “Quantum Riemann Surfaces in Chern-Simons Theory,” Adv. Theor.
Math. Phys. 17 (2013) 479–599, 1102.4847v1.
http://arxiv.org/abs/1102.4847v1.
[84] J. E. Andersen and R. Kashaev, “A new formulation of the Teichm¨uller TQFT,”
1305.4291v1. http://arxiv.org/abs/1305.4291v1.
[85] S. Kim, “The complete superconformal index for N=6 Chern-Simons theory,” Nucl.
Phys. B821 (2009) 241–284, 0903.4172v5. http://arxiv.org/abs/0903.4172v5.
[86] Y. Imamura and S. Yokoyama, “Index for three dimensional superconformal ﬁeld
theories with general R-charge assignments,” JHEP 1104 (2011) 007, 1101.0557v3.
http://arxiv.org/abs/1101.0557v3.
[87] A. Kapustin and B. Willett, “Generalized Superconformal Index for Three
Dimensional Field Theories,” 1106.2484v1. http://arxiv.org/abs/1106.2484v1.
[88] F. Benini, T. Nishioka, and M. Yamazaki, “4d Index to 3d Index and 2d TQFT,”
Phys. Rev. D86 (2012) 065015, 1109.0283v2. http://arxiv.org/abs/1109.0283v2.
[89] Y. Imamura, H. Matsuno, and D. Yokoyama, “Factorization of S3/Zn partition
function,” Phys. Rev. D89 (2014) 085003, 1311.2371v3.
http://arxiv.org/abs/1311.2371v3.
31
[90] W. D. Neumann and D. Zagier, “Volumes of hyperbolic three-manifolds,” Topology
24 (1985) no. 3, 307–332.
[91] W. Neumann, “Combinatorics of Triangulations and the Chern-Simons Invariant for
Hyperbolic 3-Manifolds,” in Topology ’90, Ohio State Univ. Math. Res. Inst. Publ. 1
(1992) . http://www.math.columbia.edu/~neumann/preprints/cspaper.pdf.
[92] S. Garoufalidis and R. Kashaev, “From state integrals to q-series,” 1304.2705v1.
http://arxiv.org/abs/1304.2705v1.
[93] L. Faddeev, “Current-Like Variables in Massive and Massless Integrable Models,” in
Quantum groups and their applications in physics (Varenna 1994), Proc. Internat.
School Phys. Enrico Fermi, 127, IOS, Amsterdam (1996) 117–135.
http://arxiv.org/abs/hep-th/9408041.
[94] L. D. Faddeev and R. M. Kashaev, “Quantum Dilogarithm,” Modern Phys. Lett. A9
(1994) no. 5, 427–434, hep-th/9310070v1.
http://arxiv.org/abs/hep-th/9310070v1.
[95] C. Petronio and J. Weeks, “Partially Flat Ideal Triangulations of Cusped Hyperbolic
3–Manifolds,” Osaka J. Math. 37 (2000) no. 2, 453–466.
http://www.projecteuclid.org/DPubS/Repository/1.0/Disseminate?handle=
euclid.ojm/1200789209&view=body&content-type=pdf_1.
[96] M. Culler, N. Dunﬁeld, and J. R. Weeks, “SnapPy, a computer program for studying
the geometry and topology of 3-manifolds,”. http://snappy.computop.org.
http://snappy.computop.org.
[97] E. Witten, “Constraints on supersymmetry breaking,” Nucl. Phys. B202 (1982)
no. 2, 253–316. http:
//www.ams.org/mathscinet/search/publications.html?pg1=MR&s1=MR668987.
[98] A. Gadde, S. Gukov, and P. Putrov, “Walls, Lines, and Spectral Dualities in 3d
Gauge Theories,” 1302.0015v1. http://arxiv.org/abs/1302.0015v1.
[99] S. Garoufalidis, “The Jones slopes of a knot,” Quant. Topol. 2 (2011) 43–69,
0911.3627v4. http://arxiv.org/abs/0911.3627v4.
[100] S. Garoufalidis, “On the Characteristic and Deformation Varieties of a Knot,” Geom.
Topol. Monogr. 7 (2004) 291–304, math/0306230v4.
http://arxiv.org/abs/math/0306230v4.
[101] D. Cooper, M. Culler, H. Gillet, D. Long, and P. Shalen, “Plane Curves Associated
to Character Varieties of 3-Manifolds,” Invent. Math. 118 (1994) no. 1, 47–84.
http://www.springerlink.com/index/R865T605G509312U.pdf.
32
[102] A. Hatcher, “On the boundary curves of incompressible surfaces,” Paciﬁc J. Math.
99 (1982) 373–377.
[103] J. H. Rubinstein, “An algorithm to recognize the 3-sphere,” Proc. International
Congress of Math. 1 (1994) no. 2, 601–611. Birkhauser, Basel.
[104] V. F. R. Jones, “A polynomial invariant for knots via von Neumann algebras,” Bull.
Amer. Math. Soc. (N.S.) 12 (1985) no. 1, 103–111. http:
//www.ams.org/mathscinet/search/publications.html?pg1=MR&s1=MR766964.
[105] V. G. Turaev, “The Yang-Baxter equation and invariants of links,” Invent. Math. 92
(1988) no. 3, 527–553. http:
//www.ams.org/mathscinet/search/publications.html?pg1=MR&s1=MR939474.
[106] S. Garoufalidis and R. Kashaev, “Evaluation of state integrals at rational points,”
Comm. Num. Thy. Phys. 9 (2015) no. 3, 549–582, 1411.6062v2.
http://arxiv.org/abs/1411.6062v2.
33
