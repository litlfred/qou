---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3–manifolds"
section_id: sec-011-a-census
section_title: "A census"
section_number: null
pages: 12-15
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
Proposition 4.1The complete list of non-hyperbolic closed 3–manifolds of topological volumes
at most3.07, their explicit volumes and their minimisers are given in Table 1Table 1. In particular,
each of these manifolds contains a unique volume minimiser. In all cases the volume minimiser
is a knot.
ProofFrom Theorem 1.5 of [ GHM+21GHM+21], cf. [ Mil09Mil09], we know the complete list of cusped hy-
perbolic 3–manifolds of volume at most 3.07. These are:
V=

m003,m004,m006,m007,m009,m010,m011,m015,m016,m017,m019,m022,m023,m026

All of these have exactly one cusp. Hence the non-hyperbolic 3–manifolds of topological volumes
at most 3.07 are precisely the exceptional fillings on these manifolds, and thus there are finitely
many.
We claim that the volumes of the manifolds in the above list satisfy:
volH(m003) = volH(m004)<vol H(m006) = volH(m007)
<vol H(m009) = volH(m010)
<vol H(m011)
<vol H(m015) = volH(m016) = volH(m017)
<vol H(m019)
<vol H(m022) = volH(m023)
<vol H(m026)
We first note that the above equalities and inequalities are correct if one computes the volumes
with precisionup to two decimal places. Hence it remains to show that the stated equalities
hold.
We first note thatm003 andm004 are once-punctured torus bundles with monodromies−RL
andRL, respectively. HereR,L∈SL(2,Z) denote the standard generators
R=
1 1
0 1

, L=
1 0
1 1

,
which correspond to right and left Dehn twists about the standard generators of the once-
punctured torus. Hence they are related by volume-preserving mutation along the fibre and
so vol H(m003) = vol H(m004). Similarly,m009 andm010 are once-punctured torus bundles
with monodromiesRRLand−RRL, respectively; andm022 andm023 are once-punctured
torus bundles with monodromies−RRRLandRRRL, respectively. We can verify these home-
omorphisms using SnapPy by constructing the once-punctured torus bundles with the given
monodromies and checking that they are isometric to the claimed census manifolds.
For vol H(m006) = vol H(m007) and vol H(m015) = vol H(m016) = vol H(m017) we refer to
Section ASection A, where we use the gluing and completeness equations to show that the manifolds
claimed to have the same volume are built from tetrahedra with equal shapes.
In [Dun20Dun20], Dunfield provides a complete list of all exceptional fillings of SnapPy [ CDGW21CDGW21]
manifolds with one cusp. This algorithmic search is made feasible by the 6-theorem of Agol and
Lackenby [Ago00Ago00,Lac00Lac00], and the fact that the low complexity non-hyperbolic closed 3–manifolds
that arise can easily be identified.
Thus we can determine the topological volume of any exceptional filling along a manifold in
Vas follows. First enumerate all exceptional fillings of the two manifolds of smallest volume.
Then enumerate all exceptional fillings of the manifolds with second smallest volume in the list
12
and only keep those non-hyperbolic 3–manifolds that have not yet been found. Then continue
this process iteratively. If an exceptional filling is found as fillings of multiple distinct cusped
manifolds of the same volume, or by filling one manifold with different surgery coefficients, we
report all instances in which it arises. We present the results in Table 1Table 1, where we sort our
results by volume.
Table 1: The complete list of non-hyperbolic manifolds of volume less than 3.07 or-
dered by their volumes. Here the columnManifoldcontains the Regina name [ BBPBBP]
as used by Dunfield [ Dun20Dun20], whereS2T,A, andDdescribe the case that the
base surface is the 2-sphere, the 2-torus, the annulus, and the 2-disk, respectively.
Note that the notation of the Seifert fibered space agrees with the one used in
Proposition 3.3Proposition 3.3 as for example shown in Section 7 of [BKM26BKM26]. The columnVolume
contains a verified approximation of the volume (i.e. at most the last digit is wrong),
and the columnRealisationsdescribes different ways to get the manifold by Dehn
filling a SnapPy census manifold. Here and in the rest of this article the slopes in a
cusp of a census manifold are measured with respect to thegeometric basisof the
cusp given by the two shortest curves. This might in general differ from the Seifert
basis if the census manifold is the complement of a knot inS 3.
Manifold Volume Realisations
S3 2.02988321281931m004(1,0)
L(5,1) 2.02988321281931m003(−1,1)m003(0,1)
L(10,3) 2.02988321281931m003(1,0)
SFS[S2 : (2,1)(3,2)(3,−1)] 2.02988321281931m003(−2,1)m003(1,1)
SFS[S2 : (2,1)(3,1)(7,−6)] 2.02988321281931m004(−1,1)m004(1,1)
SFS[S2 : (2,1)(4,1)(5,−4)] 2.02988321281931m004(−2,1)m004(2,1)
SFS[S2 : (3,1)(3,1)(4,−3)] 2.02988321281931m004(−3,1)m004(3,1)
T×I/[−2,−1|−1,−1] 2.02988321281931m003(−1,2)
T×I/[2,1|1,1] 2.02988321281931m004(0,1)
SFS[D: (2,1)(2,1)]∪ (0,1|1,1)SFS[D: (2,1)(3,2)] 2.02988321281931m003(1,2)m003(−3,2)
SFS[D: (2,1)(2,1)]∪ (0,1|1,0)SFS[D: (2,1)(3,1)] 2.02988321281931m004(−4,1)m004(4,1)
L(15,4) 2.56897060093671m006(0,1)
L(5,2) 2.56897060093671m006(1,0)
L(3,1) 2.56897060093671m007(1,0)
SFS[S2 : (2,1)(3,2)(4,−3)] 2.56897060093671m006(−1,1)
SFS[S2 : (2,1)(2,1)(3,2)] 2.56897060093671m006(1,1)
SFS[S2 : (2,1)(2,1)(5,−2)] 2.56897060093671m007(1,1)
SFS[S2 : (2,1)(3,1)(7,−5)] 2.56897060093671m006(−2,1)
SFS[S2 : (3,1)(3,1)(3,−1)] 2.56897060093671m007(0,1)
SFS[S2 : (2,1)(4,1)(5,−3)] 2.56897060093671m007(−1,1)
SFS[S2 : (2,1)(3,1)(9,−7)] 2.56897060093671m007(−2,1)
SFS[A: (2,1)]/[0,−1|−1,0] 2.56897060093671m006(−3,1)
SFS[D: (2,1)(3,1)]∪ (−1,1|0,1)SFS[D: (2,1)(3,1)] 2.56897060093671m006(1,2)
SFS[A: (2,1)]/[0,1|1,0] 2.56897060093671m007(−3,1)
L(2,1) 2.66674478344906m009(1,0)
L(6,1) 2.66674478344906m010(1,0)
SFS[S2 : (2,1)(2,1)(4,−1)] 2.66674478344906m010(0,1)
SFS[S2 : (2,1)(3,1)(8,−7)] 2.66674478344906m009(0,1)
SFS[S2 : (2,1)(4,1)(6,−5)] 2.66674478344906m009(−1,1)
SFS[S2 : (3,1)(3,1)(5,−4)] 2.66674478344906m009(−2,1)
SFS[S2 : (3,1)(3,2)(3,−1)] 2.66674478344906m010(1,1)
T×I/[3,2|1,1] 2.66674478344906m009(1,1)
T×I/[−3,−2|−1,−1] 2.66674478344906m010(−2,1)
SFS[D: (2,1)(2,1)]∪ (0,1|1,0)SFS[D: (2,1)(4,1)] 2.66674478344906m009(−3,1)
continued on next page –
13
Table 1 – continued from previous page
Manifold Volume Realisations
SFS[D: (2,1)(2,1)]∪ (−1,2|0,1)SFS[D: (2,1)(3,1)] 2.66674478344906m009(3,1)
SFS[D: (2,1)(2,1)]∪ (0,1|1,1)SFS[D: (2,1)(4,3)] 2.66674478344906m010(2,1)
L(2,1)#L(3,1) 2.66674478344906m010(−1,1)
L(9,2) 2.78183391239608m011(0,1)
L(13,3) 2.78183391239608m011(1,0)
SFS[S2 : (2,1)(3,2)(4,−1)] 2.78183391239608m011(−1,1)
SFS[S2 : (2,1)(2,1)(3,−2)] 2.78183391239608m011(1,1)
SFS[S2 : (2,1)(3,2)(5,−3)] 2.78183391239608m011(2,1)
SFS[D: (2,1)(3,1)]∪ (0,1|1,1)SFS[D: (2,1)(3,2)] 2.78183391239608m011(−1,2)
L(19,7) 2.82812208833078m016(−1,1)
L(18,5) 2.82812208833078m016(0,1)
L(21,8) 2.82812208833078m017(−1,1)
L(14,3) 2.82812208833078m017(0,1)
L(7,2) 2.82812208833078m017(1,0)
SFS[S2 : (2,1)(4,1)(7,−5)] 2.82812208833078m015(0,1)
SFS[S2 : (3,1)(3,1)(5,−3)] 2.82812208833078m015(1,1)
SFS[S2 : (2,1)(3,1)(11,−9)] 2.82812208833078m015(−1,1)
SFS[D: (2,1)(2,1)]∪ (0,1|1,0)SFS[D: (2,1)(3,2)] 2.82812208833078m015(2,1)
SFS[A: (2,1)]/[0,1|1,−1] 2.82812208833078m015(−2,1)
SFS[D: (2,1)(2,1)]∪ (1,1|0,1)SFS[D: (2,1)(3,1)] 2.82812208833078m016(2,1)
SFS[D: (2,1)(3,1)]∪ (−1,1|0,1)SFS[D: (2,1)(3,2)] 2.82812208833078m016(−1,2)
SFS[D: (2,1)(2,1)]∪ (0,1|1,1)SFS[D: (2,1)(3,1)] 2.82812208833078m017(−2,1)
SFS[A: (2,1)]/(0,−1|−1,1) 2.82812208833078m017(2,1)
L(17,5) 2.944106486676m019(0,1)
L(11,3) 2.944106486676m019(1,1)
SFS[S2 : (2,1)(3,2)(5,−2)] 2.944106486676m019(−1,1)
SFS[D: (2,1)(3,2)]∪ (0,1|1,1)SFS[D: (2,1)(3,2)]] 2.944106486676m019(−2,1)
L(7,1) 2.98912028293m022(1,0)
SFS[S2 : (2,1)(3,1)(4,−1)] 2.98912028293m022(0,1)
SFS[S2 : (3,2)(3,2)(4,−3)] 2.98912028293m022(−1,1)
SFS[S2 : (2,1)(3,1)(9,−8)] 2.98912028293m023(0,1)
SFS[S2 : (2,1)(4,1)(7,−6)] 2.98912028293m023(1,1)
SFS[S2 : (3,1)(3,1)(6,−5)] 2.98912028293m023(2,1)
TxI/[−4,−3|−1,−1] 2.98912028293m022(2,1)
TxI/[4,3|1,1] 2.98912028293m023(−1,1)
SFS[D: (2,1)(2,1)]∪ (0,1|1,1)SFS[D: (2,1)(5,4)]] 2.98912028293m022(−2,1)
SFS[D: (2,1)(2,1)]∪ (0,1|1,0)SFS[D: (2,1)(5,1)] 2.98912028293m023(3,1)
L(19,4) 3.059338057779m026(0,1)
L(8,3) 3.059338057779m026(1,0)
SFS[S2 : (2,1)(3,2)(5,−4)] 3.059338057779m026(−1,1)
SFS[S2 : (2,1)(3,1)(3,2)] 3.059338057779m026(1,1)
SFS[D: (2,1)(3,1)]∪ (−1,1|0,1)SFS[D: (2,1)(4,1)] 3.059338057779m026(1,2)
Remark 4.2Upper bounds on the volume of non-hyperbolic manifolds not appearing in our
census can be computed from Dunfield’s data [ Dun20Dun20]. The sharpness on these bounds depends
on determining further terms in the volume spectrum of one-cusped hyperbolic 3–manifolds.
The data ordered for our setting can be accessed at [ KRS+23KRS+23].
14
