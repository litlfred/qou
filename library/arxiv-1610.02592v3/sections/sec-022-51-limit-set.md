---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-022-51-limit-set
section_title: "Limit set"
section_number: 5.1
pages: 143-151
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We then use the limit set to deﬁne a canonical decomposition of cusped
hyperbolic manifolds into ideal polyhedra, called theEpstein–Penner decom-
position.
We also devote some time to prove Theorem 5.2.1, which states that
every smooth homotopy equivalenceM→ N between two closed hyperbolic
manifolds lifts to a mapHn→ Hn that extends nicely to the compactiﬁcations
Hn→ Hn. This fact will have important applications in the study of hyperbolic
manifolds in the subsequent chapters.
5.1. Limit set
How does a discrete groupΓ of isometries ofHn act on the boundary at
inﬁnity∂Hn? We now prove that∂Hn divides canonically into twoΓ-invariant
subsets: an open zone Ω(Γ) where Γ acts properly discontinuously, and a
closed one Λ(Γ) where it does not. These regions are called respectively the
domain of discontinuityand thelimit setof Γ.
5.1.1. The limit set.Throughout this section, we letΓ be a non-trivial
discrete group of isometries ofHn. Fix a pointx∈ Hn. We now that the orbit
Γ(x) is a discrete subset ofHn. The limit set Λ(Γ)⊂∂Hn of Γ is the set of
all the accumulation points of the orbitΓ(x) in Hn.
Exercise 5.1.1. The limit set does not depend onx.
The limit set is clearly a closedΓ-invariant subset of∂Hn. If Γ′ < Γ we
obviously get Λ(Γ′)⊂ Λ(Γ).
Exercise 5.1.2. IfΓ′ has ﬁnite index inΓ then Λ(Γ′) = Λ(Γ).
Recall that Γ is elementary if it ﬁxes a ﬁnite set of points inHn.
135
136 5. THE SPHERE AT INFINITY
Example 5.1.3. If Γ is elementary and acts freely, that isM = Hn/Γ is
wither a cusp or a tube (see Proposition 4.2.9), thenΛ(Γ) = Fix(Γ) consists
of one or two points.
We now characterise the elementary subgroups ofIsom(Hn). Recall that
Γ is virtually P if it has a ﬁnite-index subgroup that is P (where P is some
property).
Proposition 5.1.4. The following are equivalent:
(1) Γ is elementary,
(2) Γ ﬁxes either a pointx∈ Hn, or a line, or a pointx∈∂Hn and all
the horospheres centred atx,
(3) Γ is virtually abelian,
(4) Λ(Γ) consists of 0, 1, or 2 points.
Proof. (1)⇒ (2). We expand on the proof of Proposition 4.2.9 by taking
elliptic elements into account.
By hypothesisΓ ﬁxes a ﬁnite set of points inHn. If some of them lie inHn,
then Γ ﬁxes their barycenter and we are done. IfΓ ﬁxes more than two points
in ∂Hn, a barycenter is also deﬁned: their convex hull is an ideal polyhedron
of dimension at least 2, we can truncate (via horospheres) all the vertices by
the same small volume and take the barycenter of the vertices of the resulting
compact combinatorial polyhedron. So we are done also in this case. IfΓ ﬁxes
two points, it ﬁxes a line.
Weareleftwiththecasewhere Γﬁxesapointx∈∂Hn, andnootherﬁnite
set of points. The proof of Lemma 4.2.2 extends as is whenϕ2 is elliptic, and
shows that ifΓ contains a hyperbolic elementϕ1 then every other non-trivial
element of Γ is either hyperbolic or elliptic and ﬁxes the same axis ofϕ1, but
this is excluded: soΓ contains only parabolics and elliptics, and these must ﬁx
all the horospheres centred atx, as required.
(2)⇒ (3). The group Γ is virtually isomorphic to a discrete subgroup of
Isom(Rm) for somem and we apply Theorem 4.4.8.
(3)⇒ (4). By Exercise 5.1.2 we may suppose that Γ is abelian. By
adaptingtheproofof Lemma4.2.1to elliptics wesee(exercise)that Γsatisﬁes
(2) and hence we get (4).
(4)⇒ (1). If Λ(Γ) is empty thenΓ is ﬁnite and ﬁxes a point by Proposition
2.4.7. If it consists of one or two points, these are preserved byΓ. □
5.1.2. Minimality. Let Γ be a non elementary non-trivial discrete group
of isometries ofHn. We are interested in the action ofΓ on Λ(Γ). We want
to prove that the action isminimal, that isΛ(Γ) has no invariant non-empty
proper closed subset.
Recall from Section 3.2.1 that every closed subsetS⊂ Hn has a well-
deﬁned convex hullC(S)⊂ Hn. The convex hullC(S) is closed and is the
5.1. LIMIT SET 137
intersection of all the closed half-spaces containingS. We haveC(S)∩∂Hn =
S∩∂Hn.
Proposition 5.1.5. If Γ is not elementary, its action onΛ(Γ) is minimal.
Proof. LetS⊂ Λ(Γ) be a non-empty closedΓ-invariant subset. SinceS is
Γ-invariant, its convex hullC(S) also is. SinceΓ is not elementary,S contains
at least two points and hence the intersectionC(S)∩ Hn is not empty. If
x∈C(S)∩ Hn, itsΓ-orbit is conﬁned inC(S) and hence also its accumulation
points are: thereforeΛ(Γ)⊂C(S)∩∂Hn =S and hence Λ(Γ) =S. □
Corollary 5.1.6. If Γ is not elementary and Γ′ ◁ Γ is an inﬁnite normal
subgroup, then Λ(Γ′) = Λ(Γ).
Proof. For everyγ∈ Γ we haveγ−1Γ′γ = Γ′, soγ sends the orbitΓ′(x) to
the orbit Γ′(γ(x)) and hence preservesΛ(Γ′). Therefore Λ(Γ′) is Γ-invariant.
The limit setΛ(Γ′) is not empty becauseΓ′ is inﬁnite: the minimality of
Λ(Γ) implies that Λ(Γ′) = Λ(Γ). □
5.1.3. The convex core.IfC⊂ Hn is a closed convex set, we deﬁne the
nearest point retraction
r : Hn→C
as the map that sendsx to the pointr (x)∈C that is closer tox. Ifx∈∂Hn,
we interpretr (x) as the ﬁrst point ofC that is contained in some horosphere
centred atx. We haver (x) =x if and only ifx∈C. The mapr is continuous.
Using the geodesic fromx to r (x) we can construct a natural deformation
retraction of Hn onto the closed convex setC.
Let Γ < Isom(Hn) be a non elementary non-trivial discrete group. The
convex hull ofΛ(Γ) is Γ-invariant, so it makes sense to deﬁne the following.
Deﬁnition 5.1.7. Theconvex coreof the orbifoldO = Hn/Γ is the quotient
C(Λ(Γ))/Γ⊂O of the convex hullC(Λ(Γ)) of the limit setΛ(Γ).
We are of course mostly interested in the case whereΓ acts freely and
hence M = Hn/Γ is a manifold. The deformation retraction deﬁned above
is Γ-invariant, therefore every complete hyperbolic manifoldM deformation
retracts onto its convex core. In particular,M is homotopically equivalent to
its convex core.
5.1.4. The domain of discontinuity.Let Γ < Isom(Hn) be a non ele-
mentary non-trivial discrete group. Thedomain of discontinuityof Γ is the
open set
Ω(Γ) =∂Hn\ Λ(Γ).
The following proposition explains the terminology.
Proposition 5.1.8.The action ofΓ on Hn∪Ω(Γ) is properly discontinuous.
138 5. THE SPHERE AT INFINITY
Proof. The nearest point retractionr sends Hn∪ Ω(Γ) toC(Λ(Γ))\ Λ(Γ)
and commutes withΓ. The action ofΓ on the latter set is properly discontin-
uous (since it is contained inHn), so the action on the former also is. □
Proposition 5.1.9. If Vol(Hn/Γ)< +∞ then Λ(Γ) =∂Hn.
Proof. If Ω(Γ)⁄= ∅, pickx ∈ Ω(Γ). The point x has a neighbourhood
system consisting of half-spaces. Since Γ acts properly discontinuously on
Hn∪ Ω(Γ), there is some half-spaceH which intersects only ﬁnitely many
Γ-translates, contradicting the ﬁnite volume hypothesis. □
In this book we are mostly interested in ﬁnite-volume complete hyper-
bolic manifolds or orbifoldsHn/Γ, and for these the limit set is just the whole
boundary, regardless ofΓ. This apparently disappointing piece of information
has some interesting algebraic consequences.
Corollary 5.1.10. If Vol(Hn/Γ) < +∞ then Γ does not contain any non-
trivial virtually abelian normal subgroup.
Proof. LetH◁ Γ be virtually abelian. IfH is inﬁnite, thenΛ(H) = Λ(Γ) =
∂Hn by Corollary 5.1.6, contradicting Proposition 5.1.4. IfH is ﬁnite, then
Fix(H) is a non-empty proper subspace ofHn and Γ acts on Fix(H) because
H is normal. If Fix(H) is a point then Γ is elementary, otherwise we get
Λ(Γ)⊂∂Fix(H), a contradiction in both cases. □
Corollary 5.1.11.The fundamental group of a ﬁnite-volume complete hy-
perbolic manifold is never solvable.
Proof. Solvablegroupshavenon-trivialnormalabeliansubgroups,asproved
in Proposition 1.4.10. □
5.1.5. Schottky groups. In all the examples encountered up to now the
limit set Λ(Γ) consists of either few points or the whole of∂Hn. There are
many cases whereΛ(Γ) is a more interesting (and often beautiful) set. The
simplest examples are probably the following.
Chooseanumber k> 2and 2k half-spacesH1,...,H 2k⊂ Hn withdisjoint
closures in Hn. The closed complement C = Hn\ int(H1∪... ∪H2k) is a
convex subset bounded by 2k disjoint hyperplanes. If we pair isometrically
these hyperplanes we get a complete (exercise) hyperbolic manifoldM, which
is henceM = Hn/Γ for someΓ. The hyperbolic manifoldM has inﬁnite volume
and is the interior of a compact manifold that decomposes into one 0-handle
andk 1-handles. The groupΓ is free withk generators.
Exercise 5.1.12. Ifn = 2, the limit setΛ(Γ)⊂∂H2 =S1 is a Cantor set.
5.1. LIMIT SET 139
5.1.6. Parabolic and hyperbolic points. Let Γ < Isom(Hn) be a non
elementary non-trivial discrete group. Aparabolic pointx∈ ∂Hn for Γ is a
point that is ﬁxed by some parabolic elementγ∈ Γ. Similarly, a hyperbolic
point is a point that is ﬁxed by some hyperbolic element.
Proposition 5.1.13. The set of all parabolic (hyperbolic) points is either
empty or a dense subset ofΛ(Γ).
Proof. They clearly form aΓ-invariant subset, so its closure also is. We
conclude because Λ(Γ) is minimal. □
Corollary 5.1.14.If Vol(Hn/Γ)< +∞, the set of all parabolic (hyperbolic)
points is either empty or dense in∂Hn.
5.1.7. Horoballs in the hyperboloid model.In the conformal models,
horoballs are just Euclidean balls tangent to the boundary at inﬁnity. In the
hyperboloid modelIn there is a more algebraic description. We denote by
L ={x∈ Rn+1⏐⏐⟨x,x⟩ = 0, xn+1> 0}
the positive light cone and recall from Section 2.2.3 that the boundary at
inﬁnity∂In may be interpreted as the set of rays inL. More than that, every
vectorx∈L determines a horoballO centred at [x]∈∂In, via the equation
O =
{
y∈In| −1⩽⟨x,y⟩< 0
}
.
The horoball gets smaller asx goes to inﬁnity.
Exercise 5.1.15. This is really a horoball centred at[x].
Hint. Prove that the boundary horosphere⟨x,y⟩ =−1 is orthogonal to all
the lines pointing tox. □
There is also a simple (and maybe surprising) geometric relation between
the vectorx and the corresponding horoball in the Poincaré disc modelDn.
RepresentDn inside the hyperplanexn+1 = 0, and letπ :In→Dn the isom-
etry obtained by projecting towardsP = (0,..., 0,−1), considered in Section
2.1.6. By projecting towardsP we also get a homeomorphismπ :L→Dn.
Exercise 5.1.16. The Euclidean centre of the horoballπ(O) isπ(x).
5.1.8. The Epstein–Penner decomposition.We now show that every
cusped ﬁnite-volume hyperbolic manifold decomposes canonically into some
ideal polyhedra. This decomposition is known as thecanonical or Epstein–
Penner decomposition.
LetM = Hn/Γ be a non-compact ﬁnite-volume complete hyperbolic man-
ifold. The manifoldM is diﬀeomorphic to the interior of a compactN with
c> 1 boundary components. We ﬁxc disjoint truncated cuspsH1,...,H c⊂
M. Their lifts inHn arec disjoint Γ-orbitsBi
1,...,B i
c of disjoint horoballs.
140 5. THE SPHERE AT INFINITY
Figure 5.1. By glueing two identical ideal triangles along their sides we
get a thrice-punctured sphereS, and we choose three disjoint truncated
cusps in it having the same area (left). In the universal cover, the two
ideal triangles ofS lift to the Farey tessellation already shown in Figure
3.8, and each of the three truncated cusps lifts to inﬁnitely many disjoint
horoballs (right). The Euclidean centre of the horoballs is shown here, in
relation to Exercise 5.1.16.
Example5.1.17. Considerthethrice-puncturedsphere S obtainedbygluing
two identical copies of an ideal triangle along their sides. This is a complete
ﬁnite-volume hyperbolic surface with three cusps. We may ﬁx three disjoint
truncated cusps of the same area, as sketched in Figure 5.1-(left). These lift
to three families of disjoint horoballs as in Figure 5.1-(right).
We use the hyperboloid modelIn and interpret a horoball as a point in
the positive light coneL as explained in the previous section. TheΓ-orbits
Bi
1,...,B i
c of horoballs form a discrete subset inL. If we modify the initial
truncated cuspHj, all the pointsBi
j∈L are rescaled by the same constant.
We make a crucial observation: the pointsBi
j are discrete inL, but the
rays that contain them form a countable dense subset ofL, because they
correspond to the parabolic points ofΓ, that are dense by Corollary 5.1.14.
We now deﬁneC⊂ Rn+1 as the convex hull of the pointsBi
j in Rn+1. We
note thatC is Γ-invariant. An example is shown in Figure 5.2. The convex
hull will deﬁne a decomposition ofM into ideal polyhedra.
The convex hullC is contained in the convex hull ofL, that consists of all
the positive timelike and lightlike vectors. The following proposition says that
C intersectsL into countably many half-lines based at the pointsBi
j.
Proposition 5.1.18.The setC∩L is the set of pointsαBi
j for someα> 1.
Proof. Pick a pointx ∈ L not of this type: the segment 0x does not
intersect{Bi
j}. Since{Bi
j}⊂ L is discrete, we can perturb the hyperplaneH
tangent inx toL so that it intersectsL into a small ellipsoid around0x, and
so that{Bi
j} lies on the opposite side ofH ofx. Thereforex⁄∈C.
5.1. LIMIT SET 141
Figure 5.2. A portion of the convex hullC for the thrice-punctured
sphere of Figure 5.1. As suggested by Exercise 5.1.16 we determine the
horoballs inL by projecting the Euclidean centers of their representations
in the disc model. The black half-line above each horoball inLis contained
inC, see Proposition 5.1.18.
Conversely, pick a pointx = αBi0
j0. The rays containing the points Bi
j
form a dense set inL, so we can ﬁnd a sequence ofBi
j⁄=Bi0
j0 such that [Bi
j ]
converges to [Bi0
j0]. Since{Bi
j} is discrete, the pointsBi
j go to inﬁnity in the
sequence and hence the segment with endpointsBi
j and Bi0
j0 approachesx in
the limit. Thereforex∈C. □
Proposition 5.1.19. Every timelike ray intersects∂C exactly once.
Proof. Everytimelikeray r entersintheinteriorofapolyhedronspannedby
someBi
j, so it intersectsC and hence∂C. Consider a pointx∈∂C∩r. Every
supporting hyperplane forx must be spacelike because the rays containing the
Bi
j are dense. ThereforeC∩r is a half-line andx is its endpoint. □
Inparticular ∂C = (∂lC)⊔(∂tC)consistsofthelightlikevectors ∂lC =C∩L
and some timelike vectors∂tC. The previous proposition furnishes a natural 1-
1 correspondence∂tC←→In with the hyperboloid model by projecting along
timelike lines.
Proposition 5.1.20.The timelike boundary∂tC is tessellated by countably
many Euclideann-dimensional polyhedra with vertices in{Bi
j}.
Proof. Consider a pointx ∈ ∂tC and a supporting hyperplane H. As
already mentioned, the hyperplaneH is spacelike and the intersectionH∩∂tC
is somek-dimensional polyhedron, convex hull of ﬁnitely many points in{Bi
j}.
142 5. THE SPHERE AT INFINITY
Figure 5.3. The Γ-invariant decomposition of the hyperbolic plane into
ideal polygons obtained by projecting the Euclidean polygons of Figure 5.2
from∂C toI2. This is in fact the Farey tessellation of Figure 5.1.
If k < nwe can rotateH until it meets one more pointBi
j and after ﬁnitely
many rotations we get an-dimensional polyhedron.
We have proved that∂tC is paved byn-dimensional polyhedra with vertices
in{Bi
j} and intersecting in common faces. The polyhedra are locally ﬁnite
because{Bi
j} is discrete, hence they form a tessellation. □
The tessellation of∂tC is Γ-invariant and projects to aΓ-invariant tessel-
lation of the hyperbolic spaceIn into ideal polyhedra, which projects in turn to
a tessellation ofM into ﬁnitely many ideal polyhedra, called thecanonical or
Epstein-Penner decomposition. An example is shown in Figure 5.3. We have
discovered the following.
Theorem 5.1.21. Every ﬁnite-volume non-compact complete hyperbolic
manifold can be tessellated into ﬁnitely many ideal polyhedra.
The canonical tessellation depends only on the chosen initial truncated
cuspsH1,...,H c. Diﬀerent choices may give diﬀerent canonical tessellations,
an example is sketched in Figure 5.4. We can parametrize these choices by
recording the volumesV1,...,V c>0 of the truncated cusps (or the areas of
∂Hi, that areVi/(n− 1) by Proposition 4.1.7).
Proposition 5.1.22.If we multiply all volumesV1,...,V c by the same con-
stantλ> 0 we get the same canonical tessellation.
Proof. The setBi
j changes by a global rescaling, and hence also the tes-
sellation does. Its projection onIn is unaﬀected. □
