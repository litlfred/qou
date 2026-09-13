---
doc_id: arxiv-2512.02998v1
doc_title: "STABILITY OFKNOT EQUIVALENCE AT LOW REGULARITY, AND SYMMETRIC CRITICAL KNOTS FOR THEMÖBIUS ENERGY"
section_id: sec-002-12-isomorphic-fundamental-groups-via-localized-d
section_title: "Isomorphic fundamental groups via localized distortion"
section_number: 1.2
pages: 1-3
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
---
1.3. Stability of knot equivalence 3
1.4. Symmetric critical points for scale-invariant knot energies 4
1.5. Strategy and outline of the paper 5
2. Sets with local distortion below a quarter circle 6
3. Pseudo-gradient flow for the distance function 9
4. Isomorphisms of fundamental groups 12
5. Stability of knot equivalence 15
6. Harmonic substitution 17
7. Weak fractional compactness 23
8. Symmetric critical knots 29
Acknowledgements 31
References 31
1.Introduction
1.1.Motivation.The notion ofambient isotopyis used in classical knot theory to distinguish
between different knot classes. It follows from a result of Fisher [20, Theorem 15] that two
knotsγ 1,γ 2 ∈C 0(R/Z,R 3) are ambiently isotopic if there exists an orientation preserving
homeomorphismh:R 3→R 3 such thath◦γ 1 =γ 2. In concrete applications it might be hard
to come up with such a homeomorphism, but in the smooth category one has the following
Date: December 3, 2025.
1
arXiv:2512.02998v1  [math.GT]  2 Dec 2025
2 SIMON BLATT, ALEXANDRA GILSBACH, PHILIPP REITER, AND HEIKO VON DER MOSEL
useful stability theorem which to the best of our knowledge has first been explicitly stated and
proven by Diao et al. who give also credit to Ken Millet.
Theorem A(C 1-isotopy stability [18, Lemma 3·2], [35], [16, Proposition 3.1]).For any im-
mersed embedded curveγ∈C 1(R/Z,R 3)there is some numberϵ γ >0such that all curves
η∈C 1(R/Z,R 3)with∥γ−η∥ C1 <ϵ γ are embedded and ambiently isotopic toγ.
This result also follows from the fact that anyC 1-isotopy can be extended to an ambient
isotopy in arbitrary dimensions and co-dimensions which was proven1 by the first author in [1].
TheC 1-stability of isotopy is used quite frequently ingeometric knot theorywhere one produces
and investigates specific knot representatives as minimizers or critical points of so-called knot
energies, to obtain more information about their knot classes; see, e.g., the surveys [4, 38–41]
and the many references therein. However, for the most interesting and mathematically more
challenging scale-invariant knot energies such as the M¨ obius energy2 introduced by O’Hara [32]
the underlying energy spaces donotembed intoC 1. Therefore, one cannot expect, e.g., that
minimizing sequences for these energies subconverge inC 1, so that it is a priori not clear if the
limit curves still belong to the prescribed knot class. One of our goals in the present paper is
therefore to develop criteria for stability of knot classes at low regularity.
For that we consider the slightly weaker notion ofknot equivalenceinstead of ambient isotopy.
Two knotsγ 1,γ 2∈C 0(R/Z,R 3) are said to beequivalent, denoted byγ 1∼γ 2, if and only if there
is a homeomorphismh:R 3→R 3 such thath(γ 1(R/Z)) =γ 2(R/Z); cf. [14, p. 4]. It is known,
e.g., that the trefoil knot is not ambiently isotopic to its mirror image; see [9, Theorem 3.39
(b)]. The corresponding reflection, however, is an orientation reversing homeomorphism of
R3 mapping the image of the trefoil knot onto its mirror image, so that the two knots are
equivalent. So, there are more (ambient) isotopy types than knot equivalence classes in knot
space. On the other hand, if two tame arclength parametrized knots are equivalent, then one
can show that they are either ambiently isotopic, or one is ambiently isotopic to the other one’s
mirror image.
Gordon and Luecke studied in [24] the fundamental groups of the knots’ complements, also
calledknot groups, and their peripheral subgroups. Combining their work with results of
Waldhausen [43] yields the following sufficient criteria for knot equivalence.
Theorem B(Knot equivalence via knot complements [24, 43]).Letγ 1,γ 2∈C 0(R/Z,R 3)be
two tame knots.
(i)If their complementsR 3\γi(R/Z),i= 1,2, are homeomorphic, thenγ 1∼γ 2.
(ii)Ifγ 1,γ 2 are prime and their knot groupsπ 1(R3\γi(R/Z)),i= 1,2,are isomorphic, then
γ1∼γ 2.
(iii)If the knot groupsπ 1(R3\γ i(R/Z)),i= 1,2,are isomorphic and if this isomorphism
induces isomorphic peripheral subgroupsP γi,i= 1,2,thenγ 1∼γ 2 even if theγ i are
composite knots.
Recall that for a setM⊂R n with path-connected complementR n\Mtwo closed loops
c1,c 2∈C 0(R/Z,Rn\M) are equivalent if they are homotopic, and that the fundamental group
π1(Rn\M) consists of the respective equivalence classes. The group structure is induced by
concatenation of closed loops containing a fixed base point inR n\M. The peripheral subgroup
PM ⊂π 1(Rn\M) then consists of all equivalence classes that possess representative loops
arbitrarily close toM.
1.2.Isomorphic fundamental groups via localized distortion.In order to apply the
results on knot equivalence, i.e., Theorem B, under low regularity assumptions we are going to
1For a proof in the simpler setting of theC 2-category see [26, Chapter 8].
2In addition to scale-invariance the M¨ obius energy is also invariant under M¨ obius transformations of the
ambient Euclidean space [21, Theorem 2.1], which lent this energy that name.
STABILITY OF KNOT EQUIV ALENCE AND SYMMETRIC CRITICAL KNOTS 3
use a localized version of Gromov’s distortion [25]. For a closed, path-connected setM⊂R n
itsdistortionis defined as the quantity
(1.1)δ(M) := sup
x,y∈M
x̸=y
dM(x,y)
|x−y| ≥1,
whered M(x,y) denotes theintrinsic distancebetween the pointsx,y, i.e., the length of the
shortest curve inMconnectingxwithy. It is well-known that the circlec 2π satisfiesδ(c 2π) = π
2
uniquely minimizing the distortion among all closed curves (see [29, Proposition 2.1] for a nice
and short proof of that fact). Moreover, any non-trivial tame knotγ∈C 0(R/Z,R 3) has
distortion at least 5π
3 , which was shown by Denne and Sullivan in [17]. So, distortion detects
knottedness, but it is not useful to distinguish between different knots. For example, distortion
cannot prevent the pull-tight phenomenon where knotted subarcs of a curve can be scaled
down to vanish in the limit without any effect on the curve’s distortion [31]. In addition,
O’Hara constructed infinitely many different prime knots with a uniform upper bound on their
distortion [33, Theorem 3.5]. On the other hand, Gromov asked if there is a universal bound
on the distortion under whicheveryknot type can be represented. This was answered to the
negative by Pardon in [34, Theorems 1.1 & 1.2] who also points out [34, p. 638] that there are
even wild knots with finite distortion such as [14, Figure 5].
Nevertheless, a universal bound on a localized version of distortion together with a compa-
rableL∞-distance guarantees knot equivalence as we will see in Corollary 1.3 below.
Definition 1.1.For a nonempty closed, path-connected setM⊂R n andr >0we define the
local distortion ofMat scaleras
(1.2)δ(M,r) := sup
x,y∈M
0<|x−y|≤2r
dM(x,y)
|x−y| .
We say thatMhas local distortion strictly belowε >0if there is somer M >0such that
δ(M,r M)<ε, and we call any suchr M >0anadmissible scale.
Our first result on fundamental groups is stated for general subsets ofRn and might therefore
be of independent interest. Its formulation uses the dimension-dependent constant
(1.3)g n :=
r
2n−2
n arcsin
r n
2n−2 forn≥3,
converging in a strictly decreasing manner tog ∞ := π√
8 asn→ ∞. Notice thatg 3 =
2√
3 arcsin
√
3
2 =
√
32√
27g∞ equals the distortion of one third of a circle, whereasg ∞ is the dis-
tortion of a quarter circle.
Theorem 1.2(Isomorphic fundamental groups).Letn≥3. If two nonempty closed, path-
connected setsM i⊂R n with path-connected complementsR n\Mi have local distortion strictly
belowg n at scalesr Mi >0fori= 1,2, and satisfy
(1.4) dist H(M1,M 2)< 1
4 min{rM1,rM2},
then there exists an isomorphismJ:π 1(Rn\M 1)→π 1(Rn\M 2)such that its restriction to
the peripheral subgroupP M1⊂π 1(Rn\M 1)mapsP M1 isomorphically ontoP M2⊂π 1(Rn\M 2).
