---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-054-127-sol-geometry
section_title: "Sol geometry"
section_number: 12.7
pages: 404-408
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
The Sol geometry is the least symmetric one among the eight. It has a
bundle structure, but with a one-dimensional basis: it is aR2-bundle over R.
Again, the geometry is fully governed by a Lie groupSol.
12.7.1. The Lie group Sol.The Lie groupSol is the spaceR3 equipped
with the following operation
(x,y,z )· (x′,y′,z′) = (x +e−zx′,y +ezy′,z +z′).
Exercise 12.7.1. We have
(x,y,z )−1 = (−xez,−ye−z,−z),
[(x,y,z ), (x′,y′,z′)] =
(
x(1−e−z′
)−x′(1−e−z ),y (1−ez′
)−y′(1−ez ), 0
)
,
[(x,y,z ), (x′,y′, 0)] =
(
−x′(1−e−z ),−y′(1−ez ), 0
)
.
12.7. SOL GEOMETRY 397
The subgroup R2 consisting of all elements(x,y, 0) is the centre ofSol
and by settingp(x,y,z ) =z we get an exact sequence
0−→ R2−→Sol
p
−→ R−→0.
Therefore Sol is a plane bundle overR. Exercise 12.7.1 implies the following.
Exercise 12.7.2. We have[Sol, Sol] = R2 and hence Sol is solvable. How-
ever [Sol, R2] = R2 and hence Sol is not nilpotent.
We deﬁne a Riemannian metric onSol by assigning the scalar product


e2z 0 0
0 e−2z 0
0 0 1


to the point (x,y,z ). The metric is left-invariant and every planez = k is
isometric to the EuclideanR2. This is the geometry with the smallest amount
of symmetries.
We remark that the metric tensor has unit determinant at every point:
therefore the volume form onSol is the standard one onR3.
The non-zero Christoﬀel symbols at(x,y,z ) are
Γ1
13 = Γ1
31 = 1,
Γ2
23 = Γ2
32 =−1,
Γ3
11 =−e2z, Γ3
22 =e−2z.
The Ricci tensor is 

0 0 0
0 0 0
0 0 −2

.
The average value of the sectional curvatures of the planes containingv ∈
T(x,y,z )Sol ranges from−1 to 0, and is minimal whenv = (0, 0,±1).
12.7.2. Sol geometry. We start with a simple exercise.
Exercise 12.7.3. The eight maps
(x,y,z )↦→ (±x,±y,z ), (x,y,z )↦→ (±y,±x,−z)
are isometries and form the dihedral groupD8. The orientation-preserving
ones form the subgroupD4 = Z2× Z2.
Let Isom∗(R2) < Isom(R2) be the subgroup consisting of all mapsv↦→
±v +b. It has two components, one being the translationsR2.
Proposition 12.7.4. Every isometry ofSol preserves the plane bundle and
induces an isometry ofR. We have
0−→Isom∗(R2)−→Isom+(Sol)
p
−→Isom(R)−→0.
398 12. THE EIGHT GEOMETRIES
The group Isom+(Sol) has four components, one of which isSol acting by
left-multiplication.
Proof. The group Sol acts transitively and freely on Sol itself, and to
conclude it suﬃces to check that the stabiliser of the origin0 is the dihedral
D4 described in Exercise 12.7.3.
The Ricci tensor tells us that an isometry ﬁxing a point also ﬁxes the
vertical axis and the horizontal plane. Therefore the vertical unitary constant
vector ﬁeldX = (0, 0, 1) is preserved up to sign by any isometry ofSol. The
covariant diﬀerentiationv↦→∇ vX deﬁnes an endomorphism ofTpSol for all
p∈ Sol. We have∇eiX = Γk
i3ek and therefore the endomorphism is


1 0 0
0 −1 0
0 0 0

.
The three coordinate axis are precisely the eigenvectors of the endomorphism,
and being intrinsically deﬁned they are preserved by every isometry. Therefore
the orientation-preserving stabiliser of a point isD4. □
Proposition 12.7.5.A discrete groupΓ< Isom+(Sol) is coﬁnite if and only
if bothp(Γ) and Γ∩ kerp are discrete and coﬁnite.
Proof. Ifp(Γ) is discrete we get
Vol
(
Sol/Γ
)
= Length(R/p(Γ))× Area
(
R2/Γ∩kerp
)
.
This formula is proved as above by taking a fundamental domain forp(Γ). We
now prove thatp(Γ) is in fact discrete (sinceΓ is).
Up to taking an index-four subgroup we suppose thatΓ< Sol. Ifγ∈ Sol
does not lie in R2, then it ﬁxes a vertical line. To prove that, note that
γ = (x,y,z ) acts on R3 as an aﬃne transformation, which permutes the
vertical lines and acts onR2 as (x′,y′)↦→ (x +e−zx′,y +ezy′). Ifz⁄= 0 this
map has a ﬁxed point (because1 is not an eigenvalue of its linearisation).
If Γ is abelian, either it is contained inR2 or it ﬁxes a vertical line: in both
cases we get a discretep(Γ). If Γ is non-abelian, then[Γ, Γ]< R2 is non-trivial
so Γ contains a non-trivial elementγ∈ R2 and anotherη⁄∈ R2. The elements
γ and ηγη−1 are both inR2 and independent, hence R2/Γ∩kerp is compact.
This implies easily thatp(Γ) is discrete (sinceΓ is). □
We now classify the manifolds modelled onSol. Recall that every semi-
bundle is doubly covered by a canonical bundle. A torus bundle isof Anosov
type if its monodromy is Anosov. A torus semi-bundle is of Anosov type if its
double-covering is.
Proposition 12.7.6. The interior of a compact orientable manifoldM ad-
mits a ﬁnite-volume completeSol geometry if and only if it is a torus (semi-
)bundle of Anosov type.
12.7. SOL GEOMETRY 399
Proof. If int(M) = Sol/Γ has ﬁnite volume, then bothΓ∩ kerp andp(Γ)
are discrete and coﬁnite. The horizontal foliation ofSol into Euclidean planes
z =k is preserved byΓ and projected to a surface bundle over the 1-orbifold
R/p(Γ), which is eitherS1 or an interval. The ﬁbres are ﬂat and have ﬁnite
area, hence they are tori or Klein bottles.
If p(Γ) acts by translations, thenM is a torus bundle with an Anosov
monodromy±
(e−z 0
0 ez
)
for somez >0. IfM is a semi-bundle, this holds on its
double-covering.
Conversely, letMA beatorusbundlewithAnosovmonodromy A∈ SL2(Z).
We haveMA = R3/Γ where Γ is generated by the aﬃne maps
(x,y,z )↦→ (x + 1,y,z ), (x,y,z )↦→ (x,y + 1,z ), (¯x,z )↦→ (A¯x,z +h)
where ¯x = (x,y ) and h > 0 is any positive number. A linear isomorphism
ψ of R2 conjugates A into a diagonal matrix±
(e−a 0
0 ea
)
for somea > 0 and
transforms the generators into
(¯x,z )↦→ (¯x + ¯v,z ), (¯x,z )↦→ (¯x + ¯w,z ), (x,y,z )↦→ (±e−ax,±eay,z +h)
where ¯v = ψ(1, 0) and ¯w = ψ(0, 1). If trA >0 and h = a these maps are
left-multiplications by the following elements ofSol:
(¯v, 0), ( ¯w, 0), (¯0,a )
where ¯0 = (0, 0), and we are done. IftrA< 0 we compose the third generator
with the isometry(x,y,z )↦→ (−x,−y,z ).
If M is a semi-bundle double-covered byMA, we represent it as R3/Γ′
where Γ′ is generated by the groupΓ representingMA plus the element
(x,y,z )↦→
(
x + 1
2,−y,−z
)
which will be transformed viaψ into an isometry ofSol. □
Corollary 12.7.7. If a closed three-manifoldM has a Sol geometry, then
π1(M) is virtually solvable but not virtually nilpotent.
Proof. It is virtually solvable becauseSol has ﬁnite index inIsom+(Sol).
The proof of Proposition 12.7.6 shows that up to ﬁnite indexM = Sol/Γ and
Γ is generated by
(¯v, 0), ( ¯w, 0), (¯0,a ).
Exercise 12.7.1 implies that[(¯0,a ), (¯v, 0)] = (¯v′, 0) for some¯v′⁄= 0 and hence
Γ is not nilpotent. This holds for anyΓ of this kind, and thereforeΓ is not
virtually nilpotent, either. □
400 12. THE EIGHT GEOMETRIES
