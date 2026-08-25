---
doc_id: arxiv-1803.04009v2
doc_title: "Prepared for submission to JHEP IPMU-18-0045"
section_id: sec-005-b3-s-transformation-of-3d-scft
section_title: "B.3 S-transformation of 3d SCFT"
section_number: null
pages: 52-59
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
Now it is clear why theSU (2) andSO(3) types are exchanged under the Gaiotto-Witten’s
S∈ SL(2, Z) transformation of 3d SCFT. We start from some 3d theoryT . Then, theS
transformation is performed as follows.
If theT has symmetrySU (2), then we addT [SU (2)] and gauge the diagonalSU (2)
subgroup of theSU (2) ofT and theSU (2)H of T [SU (2)]. Then, w2(SO(3)H) = 0, and
hence the anomaly vanishes. Thesu(2)C symmetry isSO(3)C. On the other hand, if the
T has the symmetrySO(3), then we can (and choose to do) gauge the diagonalSO(3)
subgroup of theSO(3) ofT and the SO(3)H of T [SU (2)]. Because of the anomaly, or
– 51 –
more explicitly by the consideration of the monopole operators discussed above, thesu(2)C
becomes SU (2)C.
In summary, if the originalT hasSO(3) symmetry, theS-transformed theoryS·T has
SU (2) symmetry and vice versa. In this way,SU (2) and SO(3) are exchanged under the
S-transformation.
B.4 SU (2)/SO(3) symmetry types of knots from six dimensions
From the point of view of 6dN = (2, 0) theory, the symmetry type is determined as follows.
First we have to recall some of the properties of this theory [65]. For simplicity we focus
on the case of theA1 theory corresponding tosu(2).
Let X6 be a six manifold. To determine the partition function on X6, we have to
give some additional data. LetH3(X6, Z2) be the third homology withZ2 coeﬃcients. By
Poincare duality, it is possible to split this homology as
H3(X6, Z2) =A⊕B. (B.13)
This is chosen such that any two elementsa,a′ ∈ A have zero intersection⟨a,a′⟩ = 0,
and similarly forB, and the pairings betweenA and B are non-degenerate. The splitting
of H3(X6, Z2) into A and B is not unique, but we have to choose one to deﬁne partition
functions of the 6d theory. We call this splitting as polarization, and callA and B as
A-cycles and B-cycles, respectively. The partition function of the theory not only depends
on the manifoldX6, but also on the polarization.
Letuscompactifythe6dtheoryon S1 andconsider X6 =S1×X5. Thenweget5dSYM
theory with gauge algebrasu(2). Then, the above splitting determines theSU (2)/SO(3)
types of the 5d gauge theory. First, notice that the cohomology is given as
H3(S1×X5, Z2)∼=H2(X5, Z2)⊕H3(X5, Z2). (B.14)
Under this isomorphism, we deﬁne
ˆA =A∩H2(X5, Z2), ˆB =B∩H2(X5, Z2). (B.15)
Then, the 5dsu(2) theory has the following properties. Roughly speaking, the theory is
SU (2) type for A-cycles andSO(3) type for B-cycles, respectively. More precisely, letw2 be
the second Stiefel-Whitney class of thesu(2) bundle onX5. For a 2-cycleˆa∈ ˆA, we require
that
∫
ˆaw2 = 0.15 On the other hand, forˆb∈ ˆB, we sum over all gauge conﬁgurations with
diﬀerent values of
∫
ˆbw2 in the path integeral.
Applications of the above framework to 4d class S theories were studied in [66]. Here
we want to do it for 3d/3d correspondence. More speciﬁcally, we want to determine the
SU (2)/SO(3) types of the ﬂavor symmetry associated to a knot.
15In the presence of background ﬁelds for 1-form center symmetry, it can take nonzero but ﬁxed values
determined by the background ﬁeld.
– 52 –
Take the 6d manifold asX6 =X3×M3, whereX3 is “space-time” andM3 is “internal
space” which is closed. The holomogy is given by
H3(X3×M3, Z2)
=H3(X3, Z2)⊕ [H2(X3, Z2)⊗H1(M3, Z2)]⊕ [H1(X3, Z2)⊗H2(M3, Z2)]⊕H3(M3, Z2)
(B.16)
First we have to choose a polarization (B.13). There is no unique way to do it. However,
there are only a few choices which preserve the diﬀeomorphism invariance ofX3 andM3,16
and we assume that one of those choices is realized in 3d/3d correspondence.
One possible choice is to take
A =H3(X3, Z2)⊕ [H1(X3, Z2)⊗H2(M3, Z2)],
B =H3(M3, Z2)⊕ [H2(X3, Z2)⊗H1(M3, Z2)]. (B.17)
In this case, by takingX3 =S1×X2, we get
ˆA =H2(X2, Z2)⊕H2(M3, Z2), (B.18)
ˆB =H1(X2, Z2)⊗H1(M3, Z2). (B.19)
One of the consequences of this choice is as follows. LetK∈ M3 be a knot, and take a
codimension-2defectalong X3×K⊂X6. Afterthereductiononthe S1 ofthe X3 =S1×X2,
thedefectbecomesthe T [SU (2)]theorycoupledtothe5dgaugetheoryalong X2×K. Then,
there are two cases, depending on whether the homology class ofK, which we denote[K],
is nontrivial or not inH1(M3, Z2). If [K] is nonzero, then theX2×K can contain nontrivial
elements ofH1(X2, Z2)⊗H1(M3, Z2) which have nonzero values of the Stiefel-Whitney class
w2 on them. Then, by coupling the symmetrysu(2)H of T [SU (2)] to the 5d gauge group,
thesu(2)C becomes SU (2)C by the anomaly explained in the previous subsections. On the
other hand, if [K] is zero inH1(M3, Z2), then theH1(X2, Z2)⊗H1(M3, Z2) restricted to
the X2×K is trivial. Hence, thesu(2)C is SO(3)C type.
Let us summarized the above result. Under the choice of polarization (B.17);
• If the knotK has a nontrivial homology inH1(M3, Z2), then the type of the symmetry
associated to the knot isSU (2).
• If the knotK has a trivial homology inH1(M3, Z2), then the type of the symmetry
associated to the knot isSO(3).
Let us compare this result with the criterion ofSU (2)/SO(3) given in Sec. 2. There, we
consider the knot complementN3 := M3\K. The boundary ofN3 is a torus,∂N3∼= T 2,
and letA be the A-cycle of the torus which is contractible on the ambient manifoldM3.
Let [A]∈ H1(N3, Z2) be the image ofA in the Z2 homology of the knot complementN3.
The proposal in Sec. 2 is that if[A] is trivial inH1(N3, Z2), then the knot is ofSU (2) type,
and if [A] is nontrivial, it is ofSO(3)-type.
16There is no way to preserve the diﬀeomorphism invariance of the full 6d spaceX6 because the splitting
(B.13) breaks it.
– 53 –
Suppose that [A] is nonzero in H1(N3, Z2). Poincare-Lefschetz duality implies that
there is a dual cycleB∈ H2(N3,∂N 3, Z2) in the relative homology groupH2(N3,,∂N 3, Z2)
such that[A] andB has intersection number1 mod 2 . By regardingB as a chain ofN3, we
can take the boundary∂B∈ H1(∂N3, Z2) (or more precisely, this map is a connection ho-
momorphism in the long exact sequence ofH∗(N3, Z2),H∗(N3,∂N 3, Z2) andH∗(∂N3, Z2)).
On ∂N3∼=T 2, the [A] and ∂B regarded as elements ofH1(∂N3, Z2) has intersection num-
ber 1 mod 2 because, roughly speaking, the intersection of[A] andB must happen on the
boundary∂N3. Therefore,∂B is of the form[B +pA], whereB is the B-cycle on∂N3, andp
is an integer. If we embedB into the ambient manifoldM3, then we get∂B = [B+pA] = [K]
inH1(M3, Z2) because A is contractible inM3 andB is homotopic toK. Therefore, [K] is
trivial. Conversely, it is also true by Poincare-Lefschetz duality that if[K] is trivial, then
[A] is nonzero inH1(N3, Z2). Thus we get
[A]∈H1(N3, Z2) is nonzero⇐⇒[K]∈H1(M3, Z2) is zero. (B.20)
This means that the result forSU (2)/SO(3) types obtained in this appendix is the same
as the proposal in Sec. 2.
Remember that there are only a few polarization choices which preserve the diﬀeo-
morphism invariance of M3 and X3. One of them (B.17) reproduces the rules for the
SU (2)/SO(3) symmetry types of knots. This is a nontrivial check of our proposal. Thus
we assume that the choice (B.17) is realized in 3d/3d correspondence.
There are other consequences of the above choice of polarization. The fact that
H2(M3, Z2) is in ˆA means that the 5d gauge bundle does not have a nontrivial Stiefel-
Whitney class on M3. This means that the complex Chern-Simons theory on the 3-
manifold has the SU (2)C = SL(2, C) bundles instead of SO(3)C = PSL (2, C), as far
as the Stiefel-Whitney class (i.e., discrete magnetic ﬂux) onM3 is concerned. However,
this does not mean that the periodicity of holonomy is ofSL(2, C) type. Indeed, because
H1(X2, Z2)⊗H1(M3, Z2) is in ˆB, the holonomies have periodicities ofPSL (2, C) type.
This fact can be seen as follows. There can be a nontrivial magnetic ﬂuxw2 on S1
X×S1
M
whereS1
X⊂X2 andS1
M⊂M3. This is possible only if[S1
M]∈H1(M3, Z2) is nonzero. Now
consider holonomies in the spinJ representation ofsu(2) gauge algebra around the cycle
p×S1
M, wherep is a point onS1
X. If we let the pointp go aroundS1
X and return to the
same point, the value of the holonomy changes as
exp(2Jπi
∫
S1
X×S1
M
w2), (B.21)
where we have assumed that the holonomy is taken in the spinJ representation ofsu(2).
Thus, the well-deﬁnedness of the holonomy requires that we only consider representations
with integer spin J ∈ Z. This means that only the representations of SO(3) type are
consistent. This is a version of the Dirac quantization condition argument. On the other
hand, if [S1
M]∈ H1(M3, Z2) is zero, then holonomy may be well-deﬁned for half-integer
representations ofsu(2).
Thus, in complex Chern-Simons theory onM3, we get the following conditions;
– 54 –
• We only consider gauge bundles of zero Stiefel-Whitney classw2 = 0 on M3.
• Holonomies around cyclesS1
M∈M3 are deﬁned only forPSL (2, C) representations if
[S1
M]∈H1(M3, Z2) is nonzero, while they may be deﬁned forSL(2, C) representations
if [S1
M] is zero.
The ﬁrst condition is consistent with the connection coming from hyperbolic metric, because
the tangent bundle of any orientable 3-manifold hasw2(tangent) = 0. The second condition
is consistent with constructingPSL (2, C) connections by ideal triangulations. If we try
to uplift the holonomy toSL(2, C), then there may be± ambiguity. For example, the
holonomies (2.64) contain square roots√z1,√z2, and so on, which represent this ambiguity.
References
[1] K. A. Intriligator and N. Seiberg,Mirror symmetry in three-dimensional gauge theories,
Phys. Lett. B387 (1996) 513–519, [hep-th/9607207].
[2] J. de Boer, K. Hori, H. Ooguri, and Y. Oz,Mirror symmetry in three-dimensional gauge
theories, quivers and D-branes, Nucl. Phys. B493 (1997) 101–147, [hep-th/9611063].
[3] O. Aharony, A. Hanany, K. A. Intriligator, N. Seiberg, and M. J. Strassler,Aspects of N=2
supersymmetric gauge theories in three-dimensions, Nucl. Phys. B499 (1997) 67–99,
[hep-th/9703110].
[4] D. Gaiotto,N=2 dualities, JHEP 08 (2012) 034, [arXiv:0904.2715].
[5] D. Gaiotto, G. W. Moore, and A. Neitzke,Wall-crossing, Hitchin Systems, and the WKB
Approximation, arXiv:0907.3987.
[6] J. Yagi,3d TQFT from 6d SCFT, JHEP 1308 (2013) 017, [arXiv:1305.0291].
[7] C. Cordova and D. L. Jaﬀeris,Complex Chern-Simons from M5-branes on the Squashed
Three-Sphere, arXiv:1305.2891.
[8] S. Lee and M. Yamazaki,3d Chern-Simons Theory from M5-branes, arXiv:1305.2429.
[9] T. Dimofte,Complex Chern???Simons Theory at Level k via the 3d???3d Correspondence,
Commun. Math. Phys.339 (2015), no. 2 619–662, [arXiv:1409.0857].
[10] D. Gang, N. Kim, M. Romo, and M. Yamazaki,Aspects of Defects in 3d-3d Correspondence,
JHEP 10 (2016) 062, [arXiv:1510.05011].
[11] K. Hikami,Generalized volume conjecture and the A-polynomials: The Neumann Zagier
potential function as a classical limit of the partition function, Journal of Geometry and
Physics 57 (Aug., 2007) 1895–1940, [math/0604094].
[12] T. Dimofte,Quantum Riemann Surfaces in Chern-Simons Theory, Adv. Theor. Math. Phys.
17 (2013), no. 3 479–599, [arXiv:1102.4847].
[13] J. Ellegaard Andersen and R. Kashaev,A TQFT from Quantum Teichmüller Theory,
Commun.Math.Phys. 330 (2014) 887–934, [arXiv:1109.6295].
[14] T. D. Dimofte and S. Garoufalidis,The Quantum content of the gluing equations, Geom.
Topol. 17 (2013) 1253–1316, [arXiv:1202.6268].
[15] S. Kim,The Complete superconformal index for N=6 Chern-Simons theory, Nucl. Phys.
B821 (2009) 241–284, [arXiv:0903.4172]. [Erratum: Nucl. Phys.B864,884(2012)].
– 55 –
[16] A. Kapustin, B. Willett, and I. Yaakov,Exact Results for Wilson Loops in Superconformal
Chern-Simons Theories with Matter, JHEP 03 (2010) 089, [arXiv:0909.4559].
[17] N. Hama, K. Hosomichi, and S. Lee,Notes on SUSY Gauge Theories on Three-Sphere,
JHEP 03 (2011) 127, [arXiv:1012.3512].
[18] Y. Imamura and S. Yokoyama,Index for three dimensional superconformal ﬁeld theories with
general R-charge assignments, JHEP 04 (2011) 007, [arXiv:1101.0557].
[19] T. Dimofte, D. Gaiotto, and S. Gukov,Gauge Theories Labelled by Three-Manifolds,
Commun. Math. Phys.325 (2014) 367–419, [arXiv:1108.4389].
[20] H.-J. Chung, T. Dimofte, S. Gukov, and P. Su??kowski,3d-3d Correspondence Revisited,
JHEP 04 (2016) 140, [arXiv:1405.3663].
[21] D. Gaiotto and E. Witten,S-Duality of Boundary Conditions inN = 4 Super Yang-Mills
Theory, Adv.Theor.Math.Phys. 13 (2009) 721, [arXiv:0807.3720].
[22] Y. Tachikawa,N=2 supersymmetric dynamics for pedestrians, vol. 890. 2014.
[23] D. Gang, Y. Tachikawa, and K. Yonekura,Smallest 3d hyperbolic manifolds via simple 3d
theories, arXiv:1706.06292.
[24] F. Benini, S. Benvenuti, and Y. Tachikawa,Webs of ﬁve-branes and N=2 superconformal
ﬁeld theories, JHEP 09 (2009) 052, [arXiv:0906.0359].
[25] F. Benini, Y. Tachikawa, and D. Xie,Mirrors of 3d Sicilian theories, JHEP 09 (2010) 063,
[arXiv:1007.0992].
[26] D. Gaiotto, G. W. Moore, and Y. Tachikawa,On 6dN =(2,0) theory compactiﬁed on a
Riemann surface with ﬁnite area, PTEP 2013 (2013) 013B03, [arXiv:1110.2657].
[27] O. Chacaltana, J. Distler, and Y. Tachikawa,Nilpotent orbits and codimension-two defects of
6d N=(2,0) theories, Int. J. Mod. Phys.A28 (2013) 1340006, [arXiv:1203.2930].
[28] K. Yonekura,Supersymmetric gauge theory, (2,0) theory and twisted 5d Super-Yang-Mills,
JHEP 01 (2014) 142, [arXiv:1310.7943].
[29] D. Xie and K. Yonekura,The moduli space of vacua ofN = 2 classS theories, JHEP 10
(2014) 134, [arXiv:1404.7521].
[30] N. Hama, K. Hosomichi, and S. Lee,SUSY Gauge Theories on Squashed Three-Spheres,
JHEP 05 (2011) 014, [arXiv:1102.4716].
[31] D. Gang, N. Kim, and S. Lee,Holography of 3d-3d correspondence at Large N, JHEP 04
(2015) 091, [arXiv:1409.6206].
[32] J.-B. Bae, D. Gang, and J. Lee,3DN = 2 Minimal SCFTs from Wrapped M5-Branes,
arXiv:1610.09259.
[33] V. Mikhaylov,Teichmuller TQFT vs Chern-Simons Theory, arXiv:1710.04354.
[34] D. Gang and Y. Hatsuda,S-duality resurgence in SL(2) Chern-Simons theory,
arXiv:1710.09994.
[35] S. Tillmann,Degenerations of ideal hyperbolic triangulations, Mathematische Zeitschrift 272
(2012), no. 3 793–823.
[36] W. D. Neumann,Combinatorics of triangulations and the chern-simons invariant for
hyperbolic 3-manifolds, Topology 90 (1992) 243–272.
– 56 –
[37] W. D. Neumann and D. Zagier,Volumes of hyperbolic three-manifolds, Topology 24 (1985),
no. 3 307–332.
[38] E. Witten,SL(2,Z) action on three-dimensional conformal ﬁeld theories with Abelian
symmetry, hep-th/0307041.
[39] S. Garoufalidis, C. D. Hodgson, J. Hyam Rubinstein, and H. Segerman,1-eﬃcient
triangulations and the index of a cusped hyperbolic 3-manifold, ArXiv e-prints(Mar., 2013)
[arXiv:1303.5278].
[40] T. Dimofte, D. Gaiotto, and S. Gukov,3-Manifolds and 3d Indices, Adv. Theor. Math. Phys.
17 (2013), no. 5 975–1076, [arXiv:1112.5179].
[41] D. Rolfsen,Rational surgery calculus: extension of kirby???s theorem, Paciﬁc journal of
mathematics 110 (1984), no. 2 377–386.
[42] B. Martelli and C. Petronio,Dehn ﬁlling of the" magic" 3-manifold, arXiv preprint
math/0204228 (2002).
[43] D. Pei and K. Ye,A 3d-3d appetizer, JHEP 11 (2016) 008, [arXiv:1503.04809].
[44] A. Gadde, S. Gukov, and P. Putrov,Fivebranes and 4-manifolds, arXiv:1306.4320.
[45] S. Gukov, D. Pei, P. Putrov, and C. Vafa,BPS spectra and 3-manifold invariants,
arXiv:1701.06567.
[46] L. F. Alday, P. Benetti Genolini, M. Bullimore, and M. van Loon,Reﬁned 3d-3d
Correspondence, JHEP 04 (2017) 170, [arXiv:1702.05045].
[47] O. Aharony and D. Fleischer,IR Dualities in General 3D SupersymmetricSU (N) QCD
Theories, JHEP 02 (2015) 162, [arXiv:1411.5475].
[48] P. Di Francesco, P. Mathieu, and D. Senechal,Conformal Field Theory. Graduate Texts in
Contemporary Physics. Springer-Verlag, New York, 1997.
[49] E. Witten,Quantum Field Theory and the Jones Polynomial, Commun. Math. Phys.121
(1989) 351–399.
[50] N. Seiberg and E. Witten,Gapped Boundary Phases of Topological Insulators via Weak
Coupling, PTEP 2016 (2016), no. 12 12C101, [arXiv:1602.04251].
[51] Y. Tachikawa and K. Yonekura,On time-reversal anomaly of 2+1d topological phases, PTEP
2017 (2017), no. 3 033B04, [arXiv:1610.07010].
[52] Y. Tachikawa and K. Yonekura,More on time-reversal anomaly of 2+1d topological phases,
Phys. Rev. Lett.119 (2017), no. 11 111603, [arXiv:1611.01601].
[53] W. B. R. Lickorish,A representation of orientable combinatorial3-manifolds, Ann. of Math.
(2) 76 (1962) 531–540.
[54] A. H. Wallace,Modiﬁcations and cobounding manifolds, Canad. J. Math.12 (1960) 503–528.
[55] D. Gang, M. Romo, and M. Yamazaki,All-Order Volume Conjecture for Closed 3-Manifolds
from Complex Chern-Simons Theory, arXiv:1704.00918.
[56] F. Benini, P.-S. Hsin, and N. Seiberg,Comments on global symmetries, anomalies, and
duality in (2 + 1)d, JHEP 04 (2017) 135, [arXiv:1702.07035].
[57] Z. Komargodski, A. Sharon, R. Thorngren, and X. Zhou,Comments on Abelian Higgs
Models and Persistent Order, arXiv:1705.04786.
– 57 –
[58] Z. Komargodski, T. Sulejmanpasic, and M. Ünsal,Walls, anomalies, and deconﬁnement in
quantum antiferromagnets, Phys. Rev. B97 (2018), no. 5 054418, [arXiv:1706.05731].
[59] H. Shimizu and K. Yonekura,Anomaly constraints on deconﬁnement and chiral phase
transition, arXiv:1706.06104.
[60] D. Gaiotto, Z. Komargodski, and N. Seiberg,Time-Reversal Breaking in QCD4, Walls, and
Dualities in 2+1 Dimensions, arXiv:1708.06806.
[61] Y. Tanizaki, T. Misumi, and N. Sakai,Circle compactiﬁcation and ’t Hooft anomaly,
arXiv:1710.08923.
[62] Y. Tanizaki, Y. Kikuchi, T. Misumi, and N. Sakai,Anomaly matching for phase diagram of
massless ZN-QCD, arXiv:1711.10487.
[63] T. Sulejmanpasic, H. Shao, A. Sandvik, and M. Unsal,Conﬁnement in the bulk,
deconﬁnement on the wall: infrared equivalence between compactiﬁed QCD and quantum
magnets, Phys. Rev. Lett.119 (2017), no. 9 091601, [arXiv:1608.09011].
[64] T. Sulejmanpasic and Y. Tanizaki,C-P-T anomaly in bosonic systems, arXiv:1802.02153.
[65] E. Witten,AdS / CFT correspondence and topological ﬁeld theory, JHEP 12 (1998) 012,
[hep-th/9812012].
[66] Y. Tachikawa,On the 6d origin of discrete additional data of 4d gauge theories, JHEP 05
(2014) 020, [arXiv:1309.0697].
– 58 –
