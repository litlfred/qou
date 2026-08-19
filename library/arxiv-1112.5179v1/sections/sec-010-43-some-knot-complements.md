---
doc_id: arxiv-1112.5179v1
doc_title: "Prepared for submission to JHEP 3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA "
section_id: sec-010-43-some-knot-complements
section_title: "Some knot complements"
section_number: 4.3
pages: 28-34
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA 2Trinity College, Cambridge CB2 1TQ, UK — We"
---
A well-studied class of 3-manifolds are the complements of knots in the 3-sphere. One forms
a knot complementMK by slightly thickening a knotK∈S3 into a solid torusNK, and then
cutting it out,
MK =S3\NK. (4.13)
With the single exception of the unknot complement, all knot complements seem to admit 14
ideal triangulations that can be used to deﬁne the index IMK, a topological invariant of MK.
K
Figure 4. Meridian and longitude cycles on the
boundary of a knot complement.
The boundary of a knot complement is
a torus T 2, and its phase space PT 2 has a
canonical polarization Π. To deﬁne it, one
ﬁrst identiﬁes the so-called meridian and lon-
gitude cycles on the boundary: the meridian
µ is a small loop linking the knot K, which
would be contractible in the thickened knot
neighborhood NK; and the longitude λ is a
loop running parallel to K that has zero link-
ing number with K and is null-homologous
inMK (Figure 4). The orientation of MK in-
duces a relative orientation on these cycles. The eigenvalues of theSL(2, C) holonomies along
λ andµ, typically denoted𝓁 andm, then provide C∗ coordinates for the boundary phase space
13Cf. the end of Section 4.1. The potential issue here is that the sums (4.6) in the deﬁnition of the index
may not converge uniformly — so that order of summations can be interchanged. From all tested examples,
it appears that avoiding univalent edges is suﬃcient for convergence. Otherwise, we should only use reﬁned,
“easy” triangulations. It is highly plausible that the set of “easy” triangulations is fully connected by 2–3
moves, but it is not yet known rigorously.
14All ideal triangulations of the unknot have a univalent (“peripherally homotopic”) edge. Otherwise, it has
been proven that all hyperbolic knot complements have non-univalent triangulations [58], and the same seems
to hold even for non-hyperbolic knots [56].
– 27 –
(see e.g. [28]):
P∂M =
(
C∗× C∗)/
Z2 = {(𝓁,m )}
/
(𝓁,m )∼ (𝓁−1,m−1) . (4.14)
Finally, we take the canonical position coordinate 15 to be U ≡ 2 log(m) and its conjugate
momentum to be v ≡ log(−𝓁). These logarithmic coordinates are periodic, and have an
identiﬁcation (U,v )∼ (−U,−v).
The coordinatesU andv are easily expressed as sums and diﬀerences of edge parameters of
tetrahedra in a triangulation ofMK [23, 50], and thus ﬁt nicely into the general combinatorial
framework of Section 4.1 for constructing theories TMK and indicesIMK. In particular, any
knot complement theoryTMK has a singleU(1) ﬂavor symmetry, with twisted mass parameter
U. Therefore, the index IMK(m,e ) depends on a single electric charge e and magnetic ﬂux
m. We expect that the manifest U(1) symmetry is actually enhanced to SU (2), allowing
knot complement theories to couple to the 4d theory T [∂MK] = T [T 2], which is N = 4
SU (2) super-Yang-Mills. A classical indication of this enhancement appears in the Z2 Weyl
symmetry of the phase space (4.14). The enhancement would also imply that the index
satisﬁes
IMK(m,e ;q) =IMK(−m,−e;q), (4.15)
which can be considered a quantum version of symmetry in the phase space.
We now give a few examples.
Figure-eight from two tetrahedra
D
B
z￿￿
z
z￿
z￿￿
z
z￿
AC
C
A w
w￿
w￿￿
w
w￿
w￿￿
B
D
w
w
￿
w
￿￿
z z
￿
w
w
￿
w
￿￿
zz
￿
z
￿￿
z
￿￿
m
￿
glue w
￿￿
w
￿
z
￿￿
w z
z
￿
w
￿
z
￿￿
z
w
w
￿￿
z
￿
Figure 5. The standard triangulation of the ﬁgure-eight knot complement
The standard triangulation of the ﬁgure-eight (41) knot complement has two ideal tetra-
hedra, say ∆Z and ∆W . All tetrahedron faces are glued together pairwise, and the T 2 bound-
ary is made up from small, truncated ideal vertices of the tetrahedra (Figure 5). We ﬁnd a
meridianU =Z−W′′ and a longitude v =Z′′−Z. There are two internal edge coordinates,
but only one of them is independent, and we can take it to be C = 2Z′′ +Z′ + 2W′′ +W′.
15The factor of 2 in the deﬁnition of U ensures that U and v are canonically conjugate. The minus sign
in v = log(−𝓁) is merely convenient when dealing with combinatorics of triangulations, to avoid unwanted
factors of iπ. Geometrically, this sign is correlated with the lift from PSL (2) to SL(2) holonomy on a knot
complement.
– 28 –
Finally, the conjugate momentum to C can be deﬁned as (say) Γ = −W′′. The change of
polarization from ΠZ× ΠW to ~Π then becomes


U
C
v
Γ

 =


Z−W′′
2Z′′ +Z′ + 2W′′ +W′
Z′′−Z
−W′′

 =


1 0 0 −1
−1−1 1 1
−1 0 1 0
0 0 0 −1




Z
W
Z′′
W′′

 +


0
2πi + ℏ
0
0

 . (4.16)
Correspondingly, the product index I∆Z(m1,e 1)I∆W (m2,e 2) gets transformed by the
aﬃne Sp(4, Z) action above to
I{∆i},˜Π(m1,m 2,e 1,e 2) =
(
−q
1
2
)−2e2
I∆(m1−e2,m 1+e1−e2)I∆(−m2+e1−e2,−e2), (4.17)
and then after breaking the U(1) symmetry associated to the internal edge C we obtain
I41(m,e ) =
∑
e2∈Z
I∆(m−e2,m +e−e2)I∆(e−e2,−e2). (4.18)
It can be checked for any charges (m,e ) and to any order in q that
I41(m,e ) =I41(−m,e ) =I41(m,−e) =I41(−m,−e). (4.19)
For example,
I41(1, 1) =I41(1,−1) =−q−q2 + 2q3 + 7q4 + 11q5 + 11q6 + 3q7 +... , (4.20)
etc. Thus, in addition to the Weyl symmetry (4.15), there is a parity-like symmetry that
inverts the sign of a single charge. Geometrically, this is a result of the fact that the ﬁgure-
eight knot complement is amphicheiral ( i.e. is equivalent to its mirror image).
Figure-eight from six tetrahedra
In [19], we noted that the gauge theory arising from the simple, “hard” triangulation of the
ﬁgure-eight knot complement above is a bit singular. Roughly, it is a U(1) gauge theory with
two chiral multiplets, both of charge +1. The U(1) vector ﬂavor symmetry (promoted to
SU (2)) corresponds appropriately to the meridian coordinate U. However, the topological
U(1) symmetry (corresponding to the internal edge C) should be broken, and there appears
to be no operator OI around that can break it.
To remedy this problem, one can use a reﬁned, “easy” triangulation consisting of six
tetrahedra, which leads to a perfectly good description of T41 with all desired operators
present. We argued above that this reﬁnement of triangulations should not be necessary
in the calculation of the index, and we can now verify this. In Appendix B, we use the
six-tetrahedron decomposition to ﬁnd the index. We have checked computationally that the
more complicated expression (B.2) there agrees with (4.18) for 0 ≤m≤ 3 and 0≤e≤ 3, up
to 7th order in q. One should be able to prove the complete equivalence of these expressions
using a sequence of 2–3 transformations on the index (or by using diﬀerence equations), but
we do not do so here.
– 29 –
Trefoil
The trefoil ( 31) knot complement, like the ﬁgure-eight knot, has an ideal triangulation con-
sisting of two tetrahedra{∆Z, ∆W}. The triangulation is a bit asymmetric. The two internal
edges have “valency” 2 and 10, with coordinates 16
C2 =Z +W (2 dihedral angles),
C10 =Z + 2Z′ + 2Z′′ +W + 2W′ + 2W′′ (10 dihedral angles). (4.21)
Note that C2 +C10 = 4πi + 2ℏ = (2πi + ℏ)×(# tetrahedra). The meridian and longitude
holonomies can be described as U = W′′−Z′′ and v =−2Z′′ + 2W′′−W +iπ + ℏ
2. Then,
usingC≡C2 as the independent internal gluing constraint, and taking Γ =Z as its canonical
conjugate, the change of polarization ~Π =g◦ (ΠZ× ΠW ) becomes


U
C
v
Γ

 =


−Z′′ +W′′
Z +W
−2Z′′ + 2W′′−W +iπ + ℏ
2
Z

 =


0 0 −1 1
1 1 0 0
0−1−2 2
0 0 1 0




Z
W
Z′′
W′′

 +


0
0
iπ + ℏ
2
0

 . (4.22)
From this, we compute the index and ﬁnd a small surprise:
I31(m,e ) =
∑
e2∈Z
(
−q
1
2
)2e2+mI∆(e− 2m,e 2)I∆(2m−e,e 2 +m).
=δe,3m. (4.23)
Alternatively, in a fugacity basis, we could write I31(m;q,ζ ) =ζ3m.
Such a simple index indicates thatT31 could, for example, be a pureN = 2 Chern-Simons
theory in the IR. Properly verifying this guess would require reﬁning the above triangulation
of the knot complement, because it contains a “hard” internal edge C10, and thus cannot be
used to deﬁne T31. Nevertheless, the triangulation is perfectly reasonable for calculating the
index. Due to the anticipated relation between the index and SL(2, C) Chern-Simons theory
(Section 6), we actually expect that any torus knot complement has a delta-function index.
For example, an (a,b ) torus knot with ab even should haveI(m,e ) =δe,ab
2 m .
4.4 Mapping tori and T [SU (2)]
One could also try constructing indices for some 3-manifolds without explicit reference to ideal
triangulations. Another popular construction of 3-manifolds starts with a Riemann surface
C and builds a 3-manifold by identifying the “top” and “bottom” boundaries of a mapping
cylinder Mϕ =C×ϕI,
M = C×ϕS1≡C×ϕI
/
(x, 0)∼ (ϕ(x), 1), (4.24)
16The gluing data of this triangulation, and triangulations of any other knot or link complement, can be
easily obtained from computer packages such as snap [59] or SnapPy [60].
– 30 –
with an element of the mapping class group ϕ :C→C. For example, if C =T 2\{ pt} is a
punctured torus, the mapping class group is PSL (2, Z) generated by the S and T elements.
Many interesting 3-manifolds can be represented as punctured torus bundles overS1, e.g. the
ﬁgure-eight knot complement is a punctured torus bundle over S1 with monodromy
ϕ = TST−1S−1. (4.25)
ϕ
C
C
Figure 6 . A mapping cylinder for
an element ϕ acting on the punc-
tured torus C =T 2\{p}.
This construction of 3-manifolds has a natural inter-
pretation in combined 3d/4d system as a periodic array
of duality walls (determined byϕ) in the 4dN = 2 gauge
theory T [C] [9, 27, 38]. For instance, if C is a punctured
torus, then T [C] is the so-called N = 2∗ theory in four
dimensions. Moreover, every element ϕ∈ PSL (2, Z) in
this example can be represented as a word (a sequence)
of S and T generators, each associated to a basic duality
wall in the four-dimensional gauge theory.
Relegating further details of the combined 3d/4d sys-
tem to Section 5, we can brieﬂy summarize here the rules
for calculating the index of 3d theories TM, at least in
the large class of examples (4.24) where C is a punctured
torus. Roughly speaking, for every word ϕ =γ1·γ2·... in the basic duality generators γi one
can associate a periodic array of 3d theories Tγi on the corresponding duality walls, such that
IMϕ = “Tr” (Iγ1Iγ2... ) , (4.26)
reﬂecting the geometry (4.24) of the mapping torus Mϕ. For punctured torus bundles, one
needs to describe only two duality walls that correspond to the S and T generators of the
mapping class group SL(2, Z).
The theory on the duality wall associated withTk transformation is very simple: it simply
carries a Chern-Simons action for the ﬂavor symmetry at level k. Hence, it contributes to the
integrand of (4.26) a factor
ITk = ζkm, (4.27)
written in terms of the fugacity ζ and magnetic ﬂux m.
Similarly, the S transformation corresponds to a duality wall described by a three-
dimensionalN = 2 SQED with Nf = 2 ﬂavors, also known as the mass-deformed theory
T [SU (2)]:
theory T [SU (2)]
q1 q2 q3 q4 φ0 fugacity ﬂux
U(1)gauge 1 1 −1−1 0 z s
U(1)bottom 1 −1 1 −1 0 u v
U(1)puncture 1 1 1 1 −2 α m
U(1)top 0 0 0 0 0 w n
(4.28)
– 31 –
Here, the global symmetry U(1)bottom associated to the “bottom” boundary of the mapping
cylinder is actually a Cartan subgroup of the SU (2) ﬂavor symmetry group, as suggested
by the charge assignments (4.28). This symmetry is gauged when one glues the bottom
boundary to something else. Similarly, the top boundary of the mapping cylinder shown on
Figure 6 corresponds to the topological symmetry U(1)top. Furthermore, we denote the axial
symmetry by U(1)puncture since it corresponds to the puncture of C =T 2\{p}.
The index of this theory is
IT [SU (2)] = χ(qα−2,−2m)
∑
s∈Z
∫ dz
2πizznwsχ(zαu,m +s +v)χ(z−1αu−1,m−s−v)
·χ(zαu−1,m +s−v)χ(z−1αu,m−s +v)
(4.29)
where (w,n ) are the parameters (fugacity and ﬂux) for the topological symmetry U(1)top,
and
χ(ζ,m ) = ( q1/2ζ−1)−m/2I∆(ζ,m ) = ( −1)
m+|m|
2 (q1/2ζ−1)|m|/2
∞∏
r=0
1−qr+ 1
2|m|+1ζ−1
1−qr+ 1
2|m|ζ
(4.30)
is the contribution of a single chiral multiplet of R-charge 0, which agrees up to a sign with
cf. [17].
The index of this theory is written in the charge basis as
IT [SU (2)] =
∑
e1,e2
qe1+e2χ(e1 +e2,−2m)
·χ(eα−n +eu
4 +e1,m +s +v)χ(eα +n−eu
4 +e1,m−s−v)
·χ(eα−n−eu
4 +e2,m +s−v)χ(eα +n +eu
4 +e2,m−s +v) (4.31)
where
χ(e,m ) = q−m/4I∆(e−m/2,m ) (4.32)
is the index of a free chiral of R-charge 0 in the charge basis.
Alternatively, adopting the results of [17] one can be easily evaluate the integral in (4.29).
There are four sets of poles at
z−1 =



αuq
|s+m+v|
2 +j+ 1
4
αu−1q
|s+m−v|
2 +j+ 1
4
and z =



αu−1q
|s−m+v|
2 +j+ 1
4
αuq
|s−m−v|
2 +j+ 1
4
(4.33)
with j∈ Z≥0. Moreover, we can assume 17 that these two groups correspond to poles outside
and inside of the unit circle, respectively. Therefore, taking the residues of the ﬁrst group
17Besides|q|< 1, which is required forq-expansions to make sense, this assumption also involves|αuq1/4|< 1
and|αu−1q1/4|< 1. The answer with parameters outside of this range can be obtained by analytic continuation.
– 32 –
of poles for n <0 and the residues of the second group of poles for n >0, one easily ﬁnds
a closed form of expression (4.29) that depends on three sets of parameters (fugacities and
ﬂuxes), namely (α,m ), (u,v ) and (w,n ).
We might emphasize that although the index of T [SU (2)] here was not deﬁned with
respect to a triangulation, there does exist a triangulation of the appropriate mapping cylinder
M that can be used to construct both T [SU (2)] = TM and its index (4.31). Describing the
triangulation is a focus of [61].
