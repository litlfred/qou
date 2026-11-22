---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-035-c-categorification-of-the-turaev-viro-invariants
section_title: "Categorification of the Turaev-Viro invariants"
section_number: C
pages: 74-81
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
The aim of this paper is to introduce and study new three-manifold invariants. Along the way,
we have seen the important roles played by boundary conditions, abelian ﬂat connections,
homological blocks, reﬁnement, and line operators. Here, we outline how these ideas can be
applied to categoriﬁcation of the Turaev-Viro invariants.
Deﬁned via a state-sum model, the Turaev-Viro (TV) invariants [93] involve a “counting”
problem from the start. This motivates a series of questions: do TV invariants of M3 have
a natural home in physics? Could it be that they are counting BPS states associated with
the theory T[M3] and can be categoriﬁed in a way similar to the WRT invariant? How are
they related to the new invariants discussed in this paper? Can they also be decomposed into
the “atoms” of three-manifold invariants — the homological blocks and abelian connections?
Can they be reﬁned?
From the perspective of the state-sum model, categoriﬁcation of the Turaev-Viro invari-
ants may potentially seem even more natural than that of Chern-Simons (WRT) invariants,
though the two problems are closely connected. Thus, the TV invariant of a closed 3-manifold
M3 is simply the square of the corresponding SU(2) WRT/CS invariants [94–96]:
TV(M3, q) =

ZCS(M3, q)

2 .
(C.1)
As explained in detail in this paper, the WRT invariants can be written as a linear sum of
homological blocks and, when there is only one block,
TV(M3, q) = bZ0(M3, q) bZ0(M3, q−1) = IT[M3](q)
(C.2)
is exactly given by the index of the theory T[M3].
So, for homological spheres, we have
already categoriﬁed their TV invariants!
For general M3, the story will be more interesting.61 If we use VB to denote the vector
space of boundary conditions on S1 of the theory T[M3] (a de-categoriﬁcation of CB), then
60more precisely, the linear combination of cablings up to n-th, given by (B.1)
61To streamline the presentation, we will ignore normalization factors, Weyl group actions, etc.
– 73 –
there are two natural bases {|ba⟩} and {|a⟩} corresponding to the homological blocks and
(connected components of) abelian ﬂat connections. There are several distinct elements in
VB, one is |0⟩— the boundary condition at the origin of D2, and another is |CS⟩— the
boundary condition at ∂D2 that is used to reproduce the WRT invariant. Partition function
of the theory T[M3] on S1 × I × S1 deﬁnes the inner product on VB and a map VB →V ∗
B.
Then we have62
ZCS(q, t) = ⟨0|CS⟩,
(C.3)
Za(q, t) = ⟨0|a⟩,
(C.4)
bZa(q, t) = ⟨0|ba⟩,
(C.5)
I(q, t) =
⟨0|0⟩,
(C.6)
and also, in the unreﬁned limit,
TV(q) = ZCS(q)ZCS(q−1) = ⟨0|CS⟩⟨CS|0⟩.
(C.7)
Using
|CS⟩=
X
a
e2πikCS(a)|a⟩,
(C.8)
we have
|CS⟩⟨CS| =
X
a,b
e2πik(CS(a)−CS(b))|a⟩⟨b| =
X
j
Oj,
(C.9)
where
Oj =
X
a
eq ℓk(j,2a−j)|a −j⟩⟨a|,
(C.10)
is the shift operator that acts on Za by
Za 7→eq ℓk(j,2a−j)Za−j
(C.11)
with
eq = e−2πik
(C.12)
being the modular transform of q. The shift operators are the S-dual of Wilson loops, whose
action on the homological block for M3 = L(k, 1), as we have seen in section 4.3.1, is
bZa 7→qj(2a−j) bZa−j.
(C.13)
The S-duality of type IIB string theory becomes 3d mirror symmetry of T[M3] that
exchanges Wilson loops and vortex loops (see e.g. [97] for a detailed description of the map in
a very large class of 3d N = 4 theories), and one expects that Oj corresponds to the insertion
62To obtain homological invariants, one just needs to decompactify the time S1 circle, and VB will be come
the category CB that the 3d theory T[M3] associates to S1. Then the homological invariants are identiﬁed
with Hom(B1, B2) between two boundary conditions B1, B2 in CB.
– 74 –
of a vortex line. Similar to a Wilson loop, which carries an electric charge, a vortex loop
carries a magnetic ﬂux, creating a holonomy along its meridian — no surprise that it will
shift a which is characterized by holonomies. The relation between vortex loops and abelian
ﬂat connections can be understood more precisely using the M-theory geometry, as we now
explain.
Vortex loops come from codimension-two defects in 6d (2,0) theory and can be engineered
by a stacks of “defect M5-branes” as follows:
M5-branes:
R ×
M3
× D2
∩
∩
space-time:
R × T ∗M3 × TN
∪
∪
“defect” M5′-branes:
R ×
M3
× T ∗|O
,
(C.14)
where T ∗|O is the cotangent space at O. The defect ﬁvebranes have a ﬂat background 2-
form connection (“gerbe connection”) on its world volume. The vortex lines will carry ﬂuxes,
labeled by elements in H1(M3, Z)∗. Analogous to the BPS state counting analysis with M2-
branes, the non-torsion part of H1(M3, Z)∗results in Q-exact deformations of the system,
enabling us to consider only the torsion part (Tor H1(M3, Z))∗. Taking into account multiple
ﬁvebranes gives (Tor H1(M3, Λwt,g))∗/WG. In other words, non-trivial BPS vortex loop are
labeled by components of abelian ﬂat connections. For M2-branes propagating in this system
(C.14), this generates the above mentioned shift action of vortex loops on ﬂat connections.
We have now identiﬁed the system relevant for the Turaev-Viro invariant: T[M3] on
R × S2 with the insertion of a exotic defect, given by a linear combination of vortex loops,63
whose BPS Hilbert space should categorify the TV invariant.
This Hilbert space will be
doubly-graded for generic M3 and at least triply-graded for Seifert M3. In the latter case, we
will have reﬁnement for both TV invariants and the “TV homologies.” It would be interesting
to test this proposal in concrete examples, which we leave for future work.
References
[1] P. Kronheimer and T. Mrowka, Monopoles and three-manifolds, vol. 10. Cambridge University
Press, 2007.
[2] A. Floer, An instanton-invariant for 3-manifolds, Comm. Math. Phys. 118 (1988) 215–240.
[3] P. Ozsv´ath and Z. Szab´o, Holomorphic disks and topological invariants for closed
three-manifolds, Annals of Mathematics (2004) 1027–1158.
[4] E. Witten, Quantum Field Theory and the Jones Polynomial, Commun. Math. Phys. 121
(1989) 351–399.
[5] N. Reshetikhin and V. G. Turaev, Invariants of 3-manifolds via link polynomials and quantum
groups, Invent. Math. 103 (1991) 547–597.
63This defect can be viewed as the S-dual of a Wilson loop labeled by a reducible representation, but it will
be interesting to ﬁnd an alternative way to characterize this defect.
– 75 –
[6] D. Birmingham, M. Blau, M. Rakowski and G. Thompson, Topological ﬁeld theory, Phys. Rept.
209 (1991) 129–340.
[7] L. Rozansky and H. Saleur, S and T matrices for the superU(1,1) WZW model: Application to
surgery and three manifolds invariants based on the Alexander-Conway polynomial, Nucl. Phys.
B389 (1993) 365–423, [hep-th/9203069].
[8] D. Chang, I. Phillips and L. Rozansky, R matrix approach to quantum superalgebras su-q(m/n),
J. Math. Phys. 33 (1992) 3710–3715, [hep-th/9207075].
[9] L. Rozansky and H. Saleur, Reidemeister torsion, the Alexander polynomial and U(1,1)
Chern-Simons Theory, J. Geom. Phys. 13 (1994) 105–123, [hep-th/9209073].
[10] G. Meng and C. H. Taubes, Sw= milnor torsion, Mathematical Research Letters 3 (1996)
661–674.
[11] L. Crane and I. B. Frenkel, Four-dimensional topological quantum ﬁeld theory, Hopf categories,
and the canonical bases, J. Math. Phys. 35 (1994) 5136–5154.
[12] M. Khovanov, A categoriﬁcation of the jones polynomial, arXiv preprint math.QA/9908171
(1999) .
[13] M. Khovanov and L. Rozansky, Matrix factorizations and link homology, Fundamenta
Mathematicae 199 (2008) 1–91.
[14] I. Frenkel, C. Stroppel and J. Sussan, Categorifying fractional Euler characteristics,
Jones-Wenzl projectors and 3j-symbols, Quantum Topol. 3 (2012) 181–253.
[15] H. Ooguri and C. Vafa, Knot invariants and topological strings, Nucl. Phys. B577 (2000)
419–438, [hep-th/9912123].
[16] S. Gukov, A. S. Schwarz and C. Vafa, Khovanov-Rozansky homology and topological strings,
Lett. Math. Phys. 74 (2005) 53–74, [hep-th/0412243].
[17] S. Gukov, Gauge theory and knot homologies, Fortsch. Phys. 55 (2007) 473–490, [0706.2369].
[18] E. Witten, Fivebranes and Knots, 1101.3216.
[19] M. Aganagic and S. Shakirov, Knot Homology and Reﬁned Chern-Simons Index, Commun.
Math. Phys. 333 (2015) 187–228, [1105.5117].
[20] S. Chun, S. Gukov and D. Roggenkamp, Junctions of surface operators and categoriﬁcation of
quantum groups, 1507.06318.
[21] S. Nawata and A. Oblomkov, Lectures on knot homology, 2015. 1510.01795.
[22] S. Gukov, M. Marino and P. Putrov, Resurgence in complex Chern-Simons theory, 1605.07615.
[23] S. Cecotti and C. Vafa, Topological antitopological fusion, Nucl. Phys. B367 (1991) 359–461.
[24] S. Pasquetti, Factorisation of N = 2 Theories on the Squashed 3-Sphere, JHEP 04 (2012) 120,
[1111.6905].
[25] C. Beem, T. Dimofte and S. Pasquetti, Holomorphic Blocks in Three Dimensions, JHEP 12
(2014) 177, [1211.1986].
[26] S. Cecotti, D. Gaiotto and C. Vafa, tt∗geometry in 3 and 4 dimensions, JHEP 05 (2014) 055,
[1312.1008].
– 76 –
[27] S. Gukov, P. Putrov and C. Vafa, Fivebranes and 3-manifold homology, 1602.05302.
[28] K. Hikami, Decomposition of witten-reshetikhin-turaev invariant: linking pairing and modular
forms, Chern-Simons Gauge Theory 20 (2011) 131–151.
[29] M. Atiyah, On framings of 3-manifolds, Topology 29 (1990) 1–7.
[30] Y. Yoshida and K. Sugiyama, Localization of 3d N = 2 Supersymmetric Theories on S1 × D2,
1409.6713.
[31] D. Pei and K. Ye, A 3d-3d appetizer, JHEP 11 (2016) 008, [1503.04809].
[32] T. Dimofte, S. Gukov and L. Hollands, Vortex Counting and Lagrangian 3-manifolds, Lett.
Math. Phys. 98 (2011) 225–287, [1006.0977].
[33] M. Blau and G. Thompson, Aspects of N(T) ≥2 topological gauge theories and D-branes,
Nucl.Phys. B492 (1997) 545–590, [hep-th/9612143].
[34] M. Blau and G. Thompson, Euclidean SYM theories by time reduction and special holonomy
manifolds, Phys.Lett. B415 (1997) 242–252, [hep-th/9706225].
[35] K. Hori, A. Iqbal and C. Vafa, D-branes and mirror symmetry, hep-th/0005247.
[36] A. Haydys, Fukaya-Seidel category and gauge theory, J. Sympl. Geom. 13 (2015) 151–207,
[1010.2353].
[37] S. Cautis and J. Kamnitzer, Knot homology via derived categories of coherent sheaves. I. The
sl(2)-case, Duke Math. J. 142 (2008) 511–588.
[38] P. Seidel and I. Smith, A link invariant from the symplectic geometry of nilpotent slices, Duke
Math. J. 134 (2006) 453–514.
[39] C. Manolescu, Link homology theories from symplectic geometry, Adv. Math. 211 (2007)
363–416.
[40] M. Abouzaid and I. Smith, Khovanov homology from Floer cohomology, 1504.01230.
[41] S. Cautis, Rigidity in higher representation theory, 1409.0827.
[42] M. Mackaay and B. Webster, Categoriﬁed skew Howe duality and comparison of knot
homologies, 1502.06011.
[43] H. Awata, S. Gukov, P. Sulkowski and H. Fuji, Volume Conjecture: Reﬁned and Categoriﬁed,
Adv. Theor. Math. Phys. 16 (2012) 1669–1777, [1203.2182].
[44] S. Gukov, S. Nawata, I. Saberi, M. Stoi and P. Sukowski, Sequencing BPS Spectra, JHEP 03
(2016) 004, [1512.07883].
[45] A. Beliakova, C. Blanchet and T. T. Q. Le, Laplace transform and universal sl(2) invariants,
math/0509394.
[46] A. Beliakova, C. Blanchet and T. T. Q. Le, Uniﬁed quantum invariants and their reﬁnements
for homology 3-spheres with 2-torsion, Fund. Math. 201 (2008) 217–239.
[47] J. Ellegaard Andersen and R. Kashaev, A TQFT from Quantum Teichmller Theory, Commun.
Math. Phys. 330 (2014) 887–934, [1109.6295].
– 77 –
[48] J. Ellegaard Andersen and R. Kashaev, A new formulation of the Teichm¨uller TQFT,
1305.4291.
[49] J. E. Andersen and R. Kashaev, Faddeevs Quantum Dilogarithm and State-Integrals on Shaped
Triangulations, in Proceedings, Winter School in Mathematical Physics: Mathematical Aspects
of Quantum Field Theory: Les Houches, France, January 29-February 3, 2012, pp. 131–152,
Springer, Springer, 2015. DOI.
[50] S. Garoufalidis and R. Kashaev, From state integrals to q-series, 1304.2705.
[51] S. Garoufalidis, The 3D index of an ideal triangulation and angle structures, Ramanujan J. 40
(2016) 573–604.
[52] S. Garoufalidis, C. D. Hodgson, J. H. Rubinstein and H. Segerman, 1-eﬃcient triangulations
and the index of a cusped hyperbolic 3-manifold, 1303.5278.
[53] S. Garoufalidis, C. Hodgson, N. Hoﬀman and H. Rubinstein, The 3D-index and normal surfaces,
1604.02688.
[54] S. Gukov and D. Pei, Equivariant Verlinde formula from ﬁvebranes and vortices, 1501.01310.
[55] M. Blau and G. Thompson, Chern-Simons Theory with Complex Gauge Group on Seifert Fibred
3-Manifolds, 1603.01149.
[56] F. Benini and A. Zaﬀaroni, A topologically twisted index for three-dimensional supersymmetric
theories, JHEP 07 (2015) 127, [1504.03698].
[57] J. M. F. Labastida, M. Marino and C. Vafa, Knots, links and branes at large N, JHEP 11
(2000) 007, [hep-th/0010102].
[58] E. Gorsky, S. Gukov and M. Stosic, Quadruply-graded colored homology of knots, 1304.3481.
[59] M. Aganagic, T. Ekholm, L. Ng and C. Vafa, Topological Strings, D-Model, and Knot Contact
Homology, Adv. Theor. Math. Phys. 18 (2014) 827–956, [1304.5778].
[60] V. Shende, D. Treumann and E. Zaslow, Legendrian knots and constructible sheaves, 1402.0490.
[61] V. Shende, D. Treumann, H. Williams and E. Zaslow, Cluster varieties from Legendrian knots,
1512.08942.
[62] D. Jaﬀeris and X. Yin, A Duality Appetizer, 1103.5700.
[63] A. Kapustin, H. Kim and J. Park, Dualities for 3d Theories with Tensor Matter, JHEP 12
(2011) 087, [1110.2547].
[64] C. Beem, M. Lemos, P. Liendo, W. Peelaers, L. Rastelli and B. C. van Rees, Inﬁnite Chiral
Symmetry in Four Dimensions, Commun. Math. Phys. 336 (2015) 1359–1433, [1312.5344].
[65] M. Dedushenko, S. S. Pufu and R. Yacoby, A one-dimensional theory for Higgs branch
operators, 1610.00740.
[66] A. Gadde, S. Gukov and P. Putrov, Fivebranes and 4-manifolds, 1306.4320.
[67] H.-J. Chung, T. Dimofte, S. Gukov and P. Sukowski, 3d-3d Correspondence Revisited, JHEP 04
(2016) 140, [1405.3663].
[68] Y. Imamura and S. Yokoyama, Index for three dimensional superconformal ﬁeld theories with
general R-charge assignments, JHEP 04 (2011) 007, [1101.0557].
– 78 –
[69] S. Gukov, D. Pei, W. Yan and K. Ye, Equivariant Verlinde algebra from superconformal index
and Argyres-Seiberg duality, 1605.06528.
[70] J. E. Andersen, S. Gukov and D. Pei, The Verlinde formula for Higgs bundles, 1608.01761.
[71] D. Halpern-Leistner, The equivariant Verlinde formula on the moduli of Higgs bundles, ArXiv
e-prints (Aug., 2016) , [1608.01754].
[72] I. Cherednik, Jones polynomials of torus knots via DAHA, Int.Math.Res.Not. 23 (2013)
5366–5425, [1111.6195].
[73] F. Benini, Y. Tachikawa and D. Xie, Mirrors of 3d Sicilian theories, JHEP 09 (2010) 063,
[1007.0992].
[74] D. Gang, E. Koh and K. Lee, Superconformal Index with Duality Domain Wall, JHEP 10
(2012) 187, [1205.0069].
[75] D. Gang, E. Koh, S. Lee and J. Park, Superconformal Index and 3d-3d Correspondence for
Mapping Cylinder/Torus, JHEP 01 (2014) 063, [1305.0937].
[76] T. Dimofte, D. Gaiotto and S. Gukov, Gauge Theories Labelled by Three-Manifolds, Commun.
Math. Phys. 325 (2014) 367–419, [1108.4389].
[77] T. Dimofte, D. Gaiotto and S. Gukov, 3-Manifolds and 3d Indices, Adv. Theor. Math. Phys. 17
(2013) 975–1076, [1112.5179].
[78] D. Gang, N. Kim, M. Romo and M. Yamazaki, Taming supersymmetric defects in 3d3d
correspondence, J. Phys. A49 (2016) 30LT02, [1510.03884].
[79] S. Gukov and M. Stosic, Homological Algebra of Knots and BPS States, Proc. Symp. Pure Math.
85 (2012) 125–172, [1112.0030].
[80] M. Khovanov, Categoriﬁcations of the colored jones polynomial, Journal of Knot Theory and Its
Ramiﬁcations 14 (2005) 111–130.
[81] S. Gukov and J. Walcher, Matrix factorizations and Kauﬀman homology, hep-th/0512298.
[82] L. Rozansky, A categoriﬁcation of the stable su (2) witten-reshetikhin-turaev invariant of links
in s2 x s1, arXiv preprint arXiv:1011.1958 (2010) .
[83] H. Itoyama, A. Mironov, A. Morozov and A. Morozov, HOMFLY and superpolynomials for
ﬁgure eight knot in all symmetric and antisymmetric representations, JHEP 07 (2012) 131,
[1203.5978].
[84] P. Wedrich, Exponential growth of colored HOMFLY-PT homology, 1602.02769.
[85] Ya. Kononov and A. Morozov, Rectangular superpolynomials for the ﬁgure-eight knot,
1609.00143.
[86] N. Reshetikhin and V. G. Turaev, Invariants of 3-manifolds via link polynomials and quantum
groups, Inventiones mathematicae 103 (1991) 547–597.
[87] E. Witten, Quantum ﬁeld theory and the jones polynomial, Communications in Mathematical
Physics 121 (1989) 351–399.
[88] F. Deloup and V. Turaev, On reciprocity, Journal of Pure and Applied Algebra 208 (2007)
153–158.
– 79 –
[89] L. C. Jeﬀrey, Chern-simons-witten invariants of lens spaces and torus bundles, and the
semiclassical approximation, Communications in mathematical physics 147 (1992) 563–604.
[90] R. Lawrence and D. Zagier, Modular forms and quantum invariants of 3-manifolds, Asian
Journal of Mathematics 3 (1999) 93–108.
[91] B. Cooper and V. Krushkal, Categoriﬁcation of the Jones-Wenzl projectors, Quantum Topol. 3
(2012) 139–180.
[92] B. Cooper, M. Hogancamp and V. Krushkal, SO(3) homology of graphs and links, Algebr.
Geom. Topol. 11 (2011) 2137–2166.
[93] V. Turaev and O. Viro, State sum invariants of 3-manifolds and quantum 6j-symbols, Topology
31 (1992) 865 – 902.
[94] V. G. Turaev et al., Shadow links and face models of statistical mechanics, J. Diﬀerential Geom
36 (1992) 35–74.
[95] K. Walker, On wittens 3-manifold invariants, preprint (1991) .
[96] V.-G. Turaev, Quantum invariants of knots and 3-manifolds. Walter de Gruyter &Co., 1994.
[97] B. Assel and J. Gomis, Mirror Symmetry And Loop Operators, JHEP 11 (2015) 055,
[1506.01718].
– 80 –
