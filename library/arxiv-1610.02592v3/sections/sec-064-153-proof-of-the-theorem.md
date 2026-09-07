---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-064-153-proof-of-the-theorem
section_title: "Proof of the theorem"
section_number: 15.3
pages: 469-476
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We want to prove thath furnishes a nice parametrisation for thec-dimensional
space Def(M,T ). The letter h stands for “holonomy”: recall thathi is the
holonomy ofγi, see Exercise 14.2.6.
As in Section 15.2.5, we deﬁneH(z) = logh(z). We get a map
G×H : Cn
+−→ Cn× Cc.
As above, the diﬀerential splits as a composition of linear maps
d(G×H)z : Cn Z−→ C2n ¯A′
−→ Cn× Cc
where ¯A′ is constructed from ¯A exactly asA′ fromA.
Proposition 15.2.16. The diﬀerentiald(G×H)z is injective∀z∈ Cn
+.
Proof. As above, Proposition 15.2.15 implies that the rows of¯A′ form a
lagrangian subspace of dimensionn and we conclude with the same proof as
Proposition 15.2.12. □
Corollary 15.2.17.The restriction
h|Def(M,T ) : Def(M,T )−→
(~C∗)c
is a local biholomorphism.
A complete solution z ∈ Def(M,T ) is one that determines a complete
metric onM, that is such thath(z) = (1,..., 1).
Corollary 15.2.18.Every complete solution inDef(M,T ) is isolated.
The local biholomorphismh depends on the isotopy class of the curvesγi
chosen: diﬀerent choices give diﬀerent parametrisations. Note however that
the condition thathi (z) = 1 corresponds geometrically to the completeness
ofTi and hence does not depend onγi.
15.3. Proof of the theorem
We now conclude the proof of Theorem 15.1.1. Through all this section,
we letM = int(N) be a complete orientable ﬁnite-volume cusped hyperbolic
three-manifold. We have∂N =T1∪... ∪Tc for somec> 1. We also ﬁx a
positive pairmi,li of generators forπ1(Ti ) at eachTi. Recall that eachTi has
Euclidean structure, deﬁned up to rescaling.
15.3.1. Near the complete solution. We now suppose thatM has a
geometric decompositionT into ideal hyperbolic tetrahedra, in other words
the space Def(M,T ) is non-empty and contains a complete solutionz 0. We
want to studyDef(M,T ) nearz 0.
We deﬁned in Section 14.2.7 the generalised Dehn ﬁlling invariant of a
solution z∈ Def(M,T ) at Ti to be∞ if µ(mi ) = µ(li ) = 1 , or the unique
462 15. HYPERBOLIC DEHN FILLING
point (p,q )∈ R2 such that ˜µ(mi )p ˜µ(li )q = e2πi otherwise. We denote this
invariant bydi (z)∈S2 = R2∪{∞} and get a map
d : Def(M,T )−→S2×... ×S2
| {z }
c
such thatd(z 0) = (∞,..., ∞).
Proposition 15.3.1. The mapd is a local homeomorphism atz 0.
Proof. We set
ui = log ˜µ(mi ), v i = log ˜µ(li ).
The sets (u1,...,u c) and (v1,...,v c) are both biholomorphic coordinates on
Def(M,T ) which vanish atz 0. Moreovervi vanishes precisely whereui does
(on solutions that are complete atTi ).
Recall from Exercise 14.2.4 thatµ =ρ′ is the derivative of the holonomyρ
atTi. Whenui =vi = 0 the solution is complete atTi and up to conjugation
we have
ρ(mi ) :z↦→z + 1, ρ (li ) :z↦→z +wi
for somewi∈ C withℑwi > 0 which determines the cusp shape ofTi. When
ui,vi⁄= 0 the solution is incomplete and
ρ(mi ) :z↦→az, ρ (li ) :z↦→bz
for some a,b ⁄= 0. When ui,vi → 0, a fundamental domain of Imρ with
vertices atx,ax,bx,abx tends up to rescaling to one with vertices atx,x +
1,x +wi,x + 1 +wi. Sincea,b→ 1 we get
vi = logb∼b− 1∼wi (a− 1)∼wi loga =wiui
where∼meansﬁrst-orderequality. Thereforevi
ui
=wi atthecompletesolution
v = u = 0 . We deduce in particular that the function vi
ui
is analytic on
Def(M,T ). In what follows we only use thatℑwi > 0.
We consider the following map, deﬁned whenever(pi,qi )⁄= (0, 0) for alli:
ϕ
(
(p1,q 1),..., (pc,qc)
)
= 2πi
( 1
p1 +q1w1
,..., 1
pc +qcwc
)
.
We extend it continuously to the case(pi,qi ) =∞ by setting thei-th com-
ponent of the image to be zero. By composingΦ = ϕ◦d we get a map
Φ : Def(M,T )→ Cc that sends the complete solutionu = 0 to (0,..., 0).
We prove thatΦ is diﬀerentiable anddΦ0 is invertible: this will conclude the
proof. Whenuj,vj⁄= 0 we have
pjuj +qjvj = 2πi
and Proposition 14.2.12 gives
pj =−2π ℜvj
ℑ( ¯ujvj ), q j = 2π ℜuj
ℑ( ¯ujvj ).
15.3. PROOF OF THE THEOREM 463
Nearu =v = 0 we havevj∼wjuj and hence
pj∼− 2πℜwjℜuj−ℑwjℑuj
|uj|2ℑwj
, q j∼ 2π ℜuj
|uj|2ℑwj
and therefore
ϕj = 2πi 1
pj +qjwj
∼i |uj|2ℑwj
−ℜwjℜuj +ℑwjℑuj +wjℜuj
=i |uj|2ℑwj
ℑwjℑuj +iℑwjℜuj
=i|uj|2ℑwj
i ¯ujℑwj
=uj
givingdΦ0 = id. □
IfM has a geometric decompositionT into ideal tetrahedra, we can easily
conclude the proof of Theorem 15.1.1 as follows: the geometric ideal trian-
gulationT determines a complete solutionz 0∈ Def(M,T ), and by Propo-
sition 15.3.1 the image of the generalised Dehn ﬁlling mapd : Def(M,T )→
S2×... ×S2 is an open setU containing (∞,..., ∞). The discussion in
Section 14.2.7 ﬁnishes the proof.
However, we still do not know if every complete cusped ﬁnite-volumeM
decomposes into ideal tetrahedra! If that were the case, we would be done.
Unfortunately we are not able to prove this, so more eﬀort is needed to com-
plete the proof.
15.3.2. Triangulations with ﬂat tetrahedra.As we said, we are not able
to prove that every cusped ﬁnite-volumeM decomposes into ideal tetrahedra.
The best that we can do is to show thatM decomposes into ideal tetrahedra
that are either ordinary or “ﬂat”, that is degenerated to an ideal quadrilateral.
We show this using the Epstein–Penner canonical decomposition.
The Epstein-Penner canonical decomposition (see Theorem 5.1.21) parti-
tions M into some ideal polyhedraP1,...,P k, glued isometrically along their
faces. Can we further subdivide this partition to get a geometric triangulation
ofM? We start by triangulating eachPi individually.
Proposition 15.3.2. Every ideal polyhedronP ⊂ H3 subdivides into ideal
tetrahedra.
Proof. We can use the Klein model, so that ideal polyhedra inH3 corre-
spond to Euclidean polyhedra with vertices inS2. We ﬁx a vertexv∈P, and
a vertexvi in every facefi ofP not incident toP. We triangulate eachfi by
coning alongvi, and then we triangulateP by coning all the triangulated faces
fi alongv. □
The problem is, that we are not able to guarantee that the triangulations
of the polyhedraP1,...,P k match at each pair of glued faces. The typical
situation is shown in Figure 15.13-(left): two isometricn-gons (withn> 4)
are triangulated by coning on distinct verticesv⁄=v′.
464 15. HYPERBOLIC DEHN FILLING
v
v'
Figure 15.13. The triangulations of two isometric faces that do not
match (left) because they are obtained by coning along distinct vertices
v⁄=v′ (centre). We can add some additional “ﬂat” tetrahedra to correct
this (right).
There is one thing that we can do, however: we can insert someﬂattetra-
hedrabetweenthetwo n-gonsthatconnectthetwomismatchingtriangulations
as in Figure 15.13-(right), and obtain a partially-ﬂat ideal triangulation ofM.
The ﬂat tetrahedra can be inserted as follows: ifv and v′ share an edge we
insert n− 3 ﬂat tetrahedra as suggested by Figure 15.13-(right); otherwise,
the diagonal joiningv andv′ is common to both triangulations and we proceed
inductively on each of the two sub-polygons cut by this diagonal.
The resulting ideal triangulationT containsn tetrahedra ∆1,..., ∆n; each
∆i is either fat (it lies inside some polyhedronPj) or ﬂat(it connects two
faces of thePj). We now ﬁx arbitrarily a pair of opposite edges in each∆i
and denote byzi ∈ C the modulus of ∆i at these edges. If ∆i is fat, then
ℑzi > 0 as usual; if∆i is ﬂat, the moduluszi still makes sense as a number
in R\{ 0, 1}: the vertex triangle of Figure 14.2-(left) is a degenerated ﬂat
triangle with three vertices0, 1,zi. The ﬂat tetrahedron has three real moduli
zi, zi−1
zi
, 1
1−zi
; two arguments are0 and one isπ.
We set z 0 = (z1,...,z n). By construction, the point z 0 satisﬁes the
consistency equations (29).
15.3.3. Perturbations. We now letU be a small contractible neighbour-
hood ofz 0 in (C\{ 0, 1})n. Note that U necessarily contains some points
z withℑzi < 0 for some i. The consistency equations (29) make sense
in U, and we deﬁneDefU ⊂ U to be the set of solutions. We still have
DefU =G−1(2πi,..., 2πi ).
15.3. PROOF OF THE THEOREM 465
Does a solutionz ∈ DefU determine a hyperbolic structure onM? In-
tuitively, each moduluszj withℑzj = 0 should represent a ﬂat tetrahedron,
eachzj withℑzj < 0 a negatively oriented fat tetrahedron, and positively and
negatively oriented tetrahedra should overlap; although appealing, it is how-
ever hard (and sometimes impossible) to translate this idea into a concrete
deﬁnition in general.
Our aim is to prove Theorem 15.1.1 by perturbingz 0, so we only need here
to furnish a geometric interpretation for the solutionsz that lie in a suﬃciently
small neighbourhoodU. We do this as follows.
If z is suﬃciently close toz 0, all the fat tetrahedra that triangulate a
single polyhedronPi stay positively fat, and since they satisfy the consistency
equations along the internal edges ofPi they glue to form a possibly non-
convex polyhedronPi (z)⊂ H3. The original faces ofPi are now bent inPi (z)
along their diagonals.
We now consider the originally ﬂat tetrahedra joining two faces of two
polyhedraPi (z) andPj (z). We assign all of them to one of the two polyhedra,
say Pi (z), and forget aboutPj (z). These tetrahedra are attached to some
n-gonal facef ofPi (z), bent along its diagonals. The eﬀect of each attached
tetrahedron ∆j is to ﬂip a diagonal, and we modifyPi (z) accordingly by re-
placing the two ideal triangles inf incident to the old diagonal with the two
triangles sharing the new one. Geometrically, this corresponds to adding∆j if
ℑzi > 0, or to cut∆j away fromPj (z) isℑzj < 0. At the end of the process,
we get a new polyhedronP′
j (z) with the same vertices asPj (z), whose faces
are bent along diﬀerent diagonals.
Thenewpossiblynon-convexpolyhedra P′
j (z)glueisometricallyalongtheir
paired faces, that are now bent along the same diagonals. The consistency
equations are satisﬁed along these diagonals, hence we get a hyperbolic struc-
ture forM. We summarise our discoveries:
Proposition 15.3.3. If U is suﬃciently small, every solutionz ∈ DefU
represents naturally a hyperbolic structure onM.
15.3.4. Local smoothness. We have seen that every solutionz that is
suﬃciently close toz 0 determines a hyperbolic metric onM. We now need to
extend Corollary 15.2.13.
Proposition 15.3.4.IfU is suﬃciently small thenDefU is a complex man-
ifold of dimensionc.
Proof. As in Corollary 15.2.13, it suﬃces to prove thatdGz 0 :Vn→ kerB′
has maximum rank and is hence invertible.
The only place where we usedℑzj > 0 is the proof of Proposition 15.2.12,
and we now modify it so that it applies also to our partially ﬂat solutionz 0.
We haveM =Z⊺(A′)⊺ and we need to prove thatrkM = rkA′ =n−c.
466 15. HYPERBOLIC DEHN FILLING
We neededzi⁄∈ R to prove thatZ⊺|R2n is injective: this is not the case
here, since 1
zi
and 1
zi−1 are not R-independent when ∆i is ﬂat. Now we have
kerZ⊺|R2n = Span{ziei + (1−zi )ei+n| ∆i is ﬂat}.
For K = R, C we write
K2n = K2n
fat⊕ K2n
ﬂat, Kn = Kn
fat⊕ Kn
ﬂat
where K2n
fat (K2n
ﬂat) is generated by theei,ei+n such that ∆i is fat (ﬂat), and
similarly Kn
fat (Kn
ﬂat) is generated by theei such that ∆i is fat (ﬂat).
The following restriction ofZ⊺ is still an isomorphism:
Z⊺|R2n
fat
: R2n
fat−→ Cn
fat.
We use it to push-forwardω to a symplectic formΩ on Cn
fat, and we extend
it trivially to an alternating bilinear formΩ on Cn with radical Cn
ﬂat.
It is still true thatM(R2n) has real dimensionn−c, because (A′)⊺(R2n)
intersects kerZ⊺ trivially. To prove this, suppose that a vectorv′∈ R2n that
is R-generated by the rows ofA′ lies in the kernel ofZ⊺, that is:
• (v′
i,v′
i+n) = (0, 0) for every fat∆i,
• (v′
i,v′
i+n) =ki (zi, 1−zi ) for someki∈ R, for every ﬂat∆i.
We deﬁnev∈ R3n by setting
vi =v′
i, v n+i =−v′
n+i, ,v 2n+i = 0
for alli = 0,...,n − 1. We note that each triple (vi,vn+i,v 2n+i ) is either
(0, 0, 0), or it contains three pairwise distinct real numbers. The vectorv′∈
R2n is generated by then rows ofA′⇐⇒the vectorv∈ R3n is generated by
then rows ofA (exercise).
We interpretv as a colouring of the3n edge pairs inT. The colouring
v is everywhere zero on all fat tetrahedra, and on each ﬂat tetrahedron it is
either (0, 0, 0) or consists of three pairwise distinct numbers. We must prove
that it is zero everywhere.
Thevector v iscontainedinthelagrangiansubspacegeneratedbytherows
A1,...,A 2n of A. In particular we haveω(v,A n+i ) = 0 for alli. Every row
An+i corresponds to an edgee ofT, and this equality says that the colours
on all tetrahedra incident toe of the edge pairs not containinge sum to zero,
provided that they are counted with signs in each tetrahedron. This implies
the following: if all such tetrahedra except one∆j have colour zero on all their
edge pairs, then two edge pairs on∆j have the same colours, and by what just
said onv this implies that all colours are zero also on∆j.
Consider a sequence∆1,..., ∆k of ﬂat tetrahedra that connects two faces
of two polyhedraPi andPj of the Epstein-Penner decomposition. There is one
edge of ∆1 that is incident only to fat tetrahedra except∆1, and the above
discussion implies that all the colours on∆1 are zero; by induction we deduce
that all the ﬂat∆i have zero colours. Thereforev = 0, as required.
15.3. PROOF OF THE THEOREM 467
We have proved that dimM(R2n) = n−c, and we conclude as in the
proof of Proposition 15.2.12. The formΩdeﬁnes a positive semideﬁnite scalar
product⟨,⟩ on Cn with radical Cn
ﬂat. If rkM < n−c, there are two vectors
v1,v 2∈ Rn such thatM(v1 +iv 2) = 0 whileMv1⁄= 0 andMv2⁄= 0. We get
‖Mv1‖ =‖Mv2‖ = 0 as in the proof of Proposition 15.2.12, and this implies
thatMv1,Mv 2 both lie in the radicalCn
ﬂat.
If Mv1,Mv 2∈ Cn
ﬂat then bothMv1 and Mv2 are real since 1
zi
, 1
zi−1∈ R
for every ﬂat∆i. Now 0 = M(v1 +iv 2) = Mv1 +iMv 2 implies thatMv1 =
Mv2 = 0, a contradiction. □
15.3.5. Conclusion of the proof.The proof of Theorem 15.1.1 ﬁnishes
like in the geometric triangulation case. All the discussion of Section 15.2.7
applies here: the holonomies are deﬁned also in this context and may be used
to parametrize the complex manifoldU(z 0). The strategy of Section 15.3.1 is
still valid: the generalised Dehn ﬁlling invariant mapd sendsU(z 0) to an open
neighbourhood of (∞,..., ∞) inS2×... ×S2 and the discussion in Section
14.2.7 ﬁnishes the proof. We have completed the proof of Theorem 15.1.1.
15.3.6. Mostow–Prasad rigidity.We can use the Dehn ﬁlling Theorem
15.1.1 to extend Mostow Rigidity Theorem 13.3.1 from the closed to the
cusped case. The cusped case was proved by Prasad in 1973, hence the
theorem is known asMostow–Prasad Rigidity Theorem.
Let N a be compact orientable three-manifold bounded by somec > 0
tori, and letM = int(N).
Theorem 15.3.5 (Mostow–Prasad rigidity).The manifold M admits at
most one ﬁnite-volume complete hyperbolic metric up to isometries homotopic
to the identity.
Proof. Thec = 0 case is Theorem 13.3.1, so we supposec >1. Roughly,
the metric onM is unique because it is the limit of hyperbolic metrics on its
closed Dehn ﬁllings, that are unique by Theorem 13.3.1. (We are using the
hyperbolic Dehn ﬁlling theorem as a trick to extend Mostow’s rigidity from
the closed to the cusped case: this is certainly not Prasad’s original proof,
that was published before any hyperbolic Dehn ﬁlling was studied, and more
importantly it applies to all dimensionsn> 3.)
Moreprecisely, letM havetwoﬁnite-volumehyperbolicmetrics m1 andm2.
The Dehn ﬁlling Theorem holds for both, and yields sequencesMj
i of closed
hyperbolic three-manifolds obtained fromM by Dehn ﬁlling with parametersj
such thatsj→ (∞,..., ∞), fori = 1, 2.
Mostow theorem furnishes an isometryMj
1→Mj
2 homotopic to the iden-
tity. The core closed geodesics of the ﬁlling solid tori are unique in their ho-
motopy classes, hence by removing them we get isometric incomplete metrics.
Sincem1 andm2 are limits of these, they are also isometric.
468 15. HYPERBOLIC DEHN FILLING
This latter sentence can be made rigorous as follows: letT be a partially
ﬂatidealtriangulationfor M inthemetric m1. Pickanidealtetrahedron ∆inT
and note that it can be straightened uniquely also in the incomplete metrics for
M close to the complete ones, just by extending the construction in the proof
of Proposition 7.4.9 from dimension two to three (an orientation of the core
geodesics is needed to deﬁne the straightening unambiguously). The modulus
z∈ C>0∪ (R\{ 0, 1}) of the straightened∆ in M is intrinsically determined
as the limit of the moduli of the straightenings of∆ in theMj
i, hence it is the
same for both metricsm1 andm2. It follows thatm2 has the same geometric
ideal decomposition ofm1, and hencem1 =m2 after a homotopy. □
