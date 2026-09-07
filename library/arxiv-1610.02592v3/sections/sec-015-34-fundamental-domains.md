---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-015-34-fundamental-domains
section_title: "Fundamental domains"
section_number: 3.4
pages: 97-105
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Figure 3.14. A Voronoi tessellation of the Euclidean plane.
Proposition 3.3.4. The setD(p) is a polyhedron and the polyhedraD(p)
asp∈S varies form a tessellation ofHn.
Proof. It is an easy exercise to show that the points inHn having the same
distance from two distinct ﬁxed points form a hyperplane. For everyp′∈ S
diﬀerent fromp we deﬁne the half-space
Hp′ =
{
q∈ Hn ⏐⏐d(q,p )⩽d(q,p′)
}
.
The setD(p) is the intersection of the half-pacesHp′ asp′ varies inS\{p}.
Since S is discrete, these half-spaces are locally ﬁnite (there are ﬁnitely
manypointsin S atboundeddistancefrom p,henceﬁnitelymanyhyperplanes).
ThereforeD(p) is a polyhedron. SinceS is discrete, every pointq∈ Hn has
at least one nearest pointp∈S: therefore the polyhedraD(p) cover Hn as
p∈S varies.
It remains to prove that the polyhedraD(p)intersect along common faces.
We haveD(p)∩D(p′) =D(p)∩∂Hp′ and henceD(p)∩D(p′) is either empty
or a face ofD(p). The case of multiple intersections follows from Exercise
3.2.2. □
Voronoi tessellations of course make sense also inRn and Sn, see Figure
3.14. Wehavejustprovedthattessellationsarenotexoteric, butquiteordinary
objects, and we now show that they are useful to study hyperbolic manifolds.
3.4. Fundamental domains
We turn back to our discrete subgroupsΓ< Isom(Hn). The geometry of a
discrete Γ is nicely controlled by some polyhedra, calledfundamental domains.
We introduce these objects and make some important examples.
3.4.1. Fundamental and Dirichlet domains.Let Γ be a discrete group
of isometries ofHn. The groupΓ may or may not act freely onHn.
90 3. HYPERBOLIC MANIFOLDS
Figure 3.15. The shadowed triangle (with one ideal vertex) is a fun-
damental domain for Γ = PSL2(Z) acting on the half-spaceH2. The
translates of the fundamental domain form the tessellation shown.
Deﬁnition 3.4.1. Afundamental domain for Γ is a polyhedronD⊂ Hn
whose translatesg(D) as g∈ Γ varies are distinct and form a tessellation of
the space Hn.
If D is a fundamental domain, the group Γ acts freely and transitively
on the tessellation
{
g(D)
}
g∈Γ, so in particular the polyhedrag(D) are all
isometric.
We describe a procedure that builds a fundamental domain for any discrete
subgroup Γ< Isom(Hn). Pick a pointp∈ Hn with trivial stabiliserΓp, which
exists by Proposition 3.1.9. The groupΓ acts freely and transitively on the
orbit Γ(p), which is discrete by Proposition 3.1.8.
The discrete orbit Γ(p) deﬁnes aΓ-invariant Voronoi tessellation ofHn,
and every polyhedron of the tessellation is a fundamental domain. The poly-
hedronD(p) of the tessellation containingp is called theDirichlet domainfor
Γ centred atp. By construction we have
D(g(p)) =g(D(p))
for allg∈ Γ. We have proved in particular the following.
Proposition 3.4.2. Every discrete groupΓ< Isom(Hn) has a fundamental
domain.
Fundamental domains are far from being unique. The Dirichlet domain
D(p) depends onp in a continuous fashion, and many fundamental domains
are not Dirichlet domains.
Exercise 3.4.3. Prove that the shadowed triangle in Figure 3.15 is a fun-
damental domain for the modular groupPSL2(Z).
Everything we say also holds forRn andSn.
3.4. FUNDAMENTAL DOMAINS 91
3.4.2. Fundamental domain of manifolds.Let Γ< Isom(Hn) be a dis-
crete subgroup that acts freely onHn and D be a fundamental domain for
Γ. We can get some information on the hyperbolic manifoldM = Hn/Γ by
looking atD.
Proposition 3.4.4. Let M = Hn/Γ be a hyperbolic manifold andD a fun-
damental domain forΓ. The projectionπ : Hn→M restricts to a surjective
mapD→M that sendsint(D) isometrically onto an open dense subset ofM.
In particular we have
Vol(D) = Vol(M).
IfD is a Dirichlet domain, it is compact if and only ifM is.
Proof. The translatesg(D) cover Hn, hence the projectionD→ M is
surjective. The translates g(int(D)) are disjoint, hence int(D) is sent iso-
metrically insideM. The boundary ∂D has measure zero, hence Vol(D) =
Vol(int(D)) = Vol(M).
If D is compact thenM clearly is. If D = D(p) is a Dirichlet domain
andM is compact,M has ﬁnite diameterδ and hence every point inHn is at
distance⩽δ of some point in the orbit ofp. HenceD(p) is contained in the
closure ofB(p,δ ). □
A fundamental domainD alone however does not determineM: we will
soon see in Section 3.4.8 that a square inR2 is the fundamental domain of
two non homeomorphic compact ﬂat surfaces.
3.4.3. Asteroids. The facets of a fundamental domainD are naturally
partitioned into isometric pairs, as follows. Ever facetf ofD is incident toD
and to another fundamental domaing(D) of the tessellation. The isometry
g−1 sendsg(D) toD and hence sendsf to another facetf′ ofD. One checks
immediately that (f′)′ =f, sof andf′ are paired isometrically.
One should think ofM as obtained fromD by identifying these facets in
pairs: we can picture an observer – say, a spaceship – ﬂoating and traveling
insideM by visualising it inD, and jumping fromf tof′ every time it crosses
the interior of a facetf, like in the 1979 video gameAsteroids.
3.4.4. Spineandcutlocus. Anotherpicturethatmayhelptounderstand
M geometrically is thespine S⊂M deﬁned asS =π(∂D). This is a(n− 1)-
dimensional object inM whose complement is an open ball. WhenD =D(p)
is the Dirichlet domain of a pointp, the spineS is called thecut locusof the
pointq =π(p)∈M.
Exercise 3.4.5. The cut locus ofq∈M consists of all pointsq′ such that
there are at least two geodesics of minimal length connectingq toq′.
We now exhibit some important examples of discrete groups of isometries
in the three geometriesHn, Rn, andSn, and study their fundamental domains.
92 3. HYPERBOLIC MANIFOLDS
3.4.5. Triangle groups.Leta,b,c > 2 be natural numbers and∆ be the
triangle inH2,S 2, orR2 with inner anglesπ
a, π
b, π
c. By reﬂecting iteratively∆
along its sides we get a tessellationT, see Section 3.3.1.
The triangle group Γ = Γ(a,b,c ) is the group of isometries ofS2, R2, or
H2 generated by the reﬂectionsx,y,z along the three sides of∆ opposite to
the vertices with inner anglesa,b,c , respectively.
Proposition 3.4.6.The triangle groupΓ(a,b,c ) acts freely and transitively
on the triangles of the tessellationT. Hence it is discrete and∆ is a funda-
mental domain forΓ. A presentation for the group is
⟨x,y,z |x 2,y 2,z 2, (xy )c, (yz )a, (zx )b⟩.
Proof. We restrict for simplicity to the hyperbolic case, the others being
analogous. It is convenient to construct the tessellationT abstractly (this
also furnishes a rigorous proof that by mirroring∆ along its sides we get a
tessellation of H2).
We denote byx,y,z both the sides of∆ and the reﬂections along them.
For everyg∈ Γ we deﬁne an abstract copy∆g of ∆, and then we glue all these
abstract copies altogether by pairing their sides as follows: for every side of
∆, sayx, and everyg∈ Γ, we identify the two copies of the sidex in ∆g and
∆gx with the obvious identity map.
Via these identiﬁcations we get an abstract spaceT tessellated into the
triangles ∆g. The groupΓ acts freely and transitively on the tessellation (the
elementg′∈ Γsends ∆g to ∆g′g). Wenowprovethat T hasanaturalstructure
of a hyperbolic surface: sinceΓ acts transitively, it suﬃces to check this for
the pointsp lying in ∆e. If p lies in the interior of∆e or of a side, this is
clear by construction. Ifp is a vertex, say with inner anglea, by construction a
cycle of2a triangles ∆e, ∆y, ∆yz, ∆yzy, ∆yzyz ,... is attached aroundp because
(yz )a =e, and henceT is naturally a hyperbolic surface also nearp.
The hyperbolic surfaceT is easily seen to be connected and complete.
There is a natural developing mapϕ:T→ H2 that sends ∆g to g(∆). The
map ϕ is a local isometry, hence a covering by Proposition 1.2.19, hence an
isometry since H2 is simply connected. We identifyT with H2 throughϕ.
It remains to prove thatΓ may be presented as stated. LetG be the group
presented as
⟨x,y,z |x 2,y 2,z 2, (xy )c, (yz )a, (zx )b⟩.
There is a natural surjectionG→ Γ. We may repeat all the arguments above
using G instead of Γ and get anotherT′ isometric to H2 that coversT. We
deduce thatT′ =T andG = Γ. □
The triangle groupΓ(2, 2,c )∼= Z/2Z×D2c has order4c and is the symme-
try group of a prism. The triangle groupsΓ(2, 3, 3), Γ(2, 3, 4), and Γ(2, 3, 5)
3.4. FUNDAMENTAL DOMAINS 93
have order24, 48, and120 and are the symmetry groups of the regular tetra-
hedron, octahedron, and icosahedron: the reader is invited to check all these
facts visually by looking at Figure 3.5.
The triangle groupsΓ(2, 3, 6), Γ(2, 4, 4), andΓ(3, 3, 3) are discrete groups
of isometries ofR2 with compact quotientR2/Γ. If 1
a + 1
b + 1
c < 1 the group
Γ(a,b,c )isadiscretesubgroupof Isom(H2). Itcontainsinﬁnitelymanyelliptic
elements, such as reﬂections along lines and ﬁnite-order rotations around the
vertices of the triangles. By Selberg’s Lemma, there is a torsion-free subgroup
Γ′ < Γ of some ﬁnite indexh. The quotient H2/Γ′ is a closed hyperbolic
surface and is tessellated intoh triangles isometric to∆.
3.4.6. Coxeter polyhedra. Triangle groups may be generalised to all di-
mensionsasfollows. Apolyhedron P in Hn (or Rn,Sn)isa Coxeterpolyhedron
if the dihedral angle of every codimension-two face dividesπ. For instance,
the regular ideal tetrahedron and octahedron are Coxeter polyhedra.
The following theorem generalises Proposition 3.4.6. LetP be a ﬁnite
Coxeter polyhedron: it is the convex hull of ﬁnitely many vertices inHn (or
Rn, Sn) and hask facets, that we number as1,...,k ; we denote byri the
reﬂection along thei-th facet, and byπ
aij
the dihedral angle formed by thei-th
and j-th facets, if they are incident. LetΓ be the isometry group generated
by the reﬂections along the facets ofP.
Theorem 3.4.7. By mirroring iteratively a ﬁnite Coxeter polyhedronP
along its facets we get a tessellation ofHn (or Rn,Sn). The group Γ acts
freely and transitively on the tessellation: hence it is discrete andP is a fun-
damental domain forΓ. A presentation forΓ is
⟨r1,...,r k|r 2
i , (rirj )aij⟩
wherei varies in 1,...,k and the pairi,j varies among the incident facets.
Proof. Same proof as Proposition 3.4.6, with in addition an induction on
the dimensionn. Here are the details. We consider for simplicity only the
hyperbolic case.
For everyg∈ Γ we deﬁne an abstract copyPg of P, and we identify the
i-th facet ofPg and Pgri for allg∈ Γ and alli. To prove that the resulting
spaceT is naturally a hyperbolic manifold, we use the induction hypothesis as
follows. Every p∈ Pe lies in the interior of someh-dimensional facef, and
let Γf < Γ be the subgroup generated by the reﬂections along all the facets of
P containing f. The pointp is adjacent inT to the polyhedraPg such that
g∈ Γf. By intersecting each suchPg with a small codimensionh + 1 sphere
centred inp and contained in the codimensionh subspace orthogonal tof, we
get some spherical polytopeQg of dimensionn−h− 1< n. (The spherical
polytopeQt is usually called thespherical linkoff.)
Byconstruction Qe⊂Sn−h−1 isaCoxeterpolytopeandthesubgroup Γf <
Isom(Sn−h−1) is generated by the reﬂections along its facets. By applying the
94 3. HYPERBOLIC MANIFOLDS
induction hypothesis onQe we deduce that the polytopesQg withg∈ Γf form
a tessellation ofSn−h−1, hence the polyhedraPg incident top form naturally
a hyperbolic ball locally nearp. ThereforeT is a hyperbolic manifold.
Proving that T is complete requires a bit of care ifPe has some ideal
vertexv. In that casev has a Euclidean link (obtained by intersectingPe with
a small horosphere) and we conclude by induction as above that the Euclidean
links of thePg incident tov in T glue to form a EuclideanRn−1, that is a
horosphere, so by intersecting eachPg with small horoballs we get a horoball
nearv, which is complete.
The hyperbolic spaceT is complete and connected, and we conclude as in
the proof of Proposition 3.4.6. □
A group generated by some reﬂections along hyperplanes is called areﬂec-
tion group. The following proposition shows that Coxeter polyhedra generate
all the interesting reﬂection groups.
Proposition 3.4.8. Every discrete reﬂection groupΓ is generated by the
reﬂections along the facets of some Coxeter polyhedron.
Proof. Consider the mirror hyperplanes of all the reﬂections inΓ. Since Γ
is discrete, these form a locally ﬁnite set and hence deﬁne a tessellation ofHn
onto whichΓ acts transitively. Pick one polyhedronP of the tessellation. The
reﬂections along the facets ofP generate Γ (exercise). □
Coxeter polyhedra are beautiful objects that can be used to construct
hyperbolic manifolds: every ﬁnite Coxeter polyhedronP generates a reﬂection
group Γ which contains, by Selberg’s Lemma, a torsion-free subgroupΓ′ of
some ﬁnite indexh. The quotient M = Hn/Γ′ is a hyperbolic manifold and
is tessellated intoh copies of P, so that Vol(M) = hVol(P ). By residual
ﬁniteness, there are plenty of such manifolds.
3.4.7. Coxeter graphs.If a Coxeter polyhedronP has a reasonable num-
ber of facets (for instance, ifP is a simplex), then one can study many of
its properties by looking at itsCoxeter graph, which is constructed as follows:
draw one node for each facet ofP, and for every pair of facets intersecting
with dihedral angleπ
a connect the corresponding nodes with an edge labeled
witha. One also uses thickened or dashed edges to denote non-incident faces
that do or do not intersect at some ideal vertex, respectively (these cases
cannot occur on simplexes). Given the abundance of right angles, one usually
omit the edges with label 2.
Exercise 3.4.9. LetP be a regular polytope or tessellation with Schläﬂi
symbol{a,b,...,z }. By quotientingP via all its isometries we get a Coxeter
simplex, called itscharacteristic simplex, whose Coxeter graph is
3.4. FUNDAMENTAL DOMAINS 95
Figure 3.16. A fundamental domain inR2 for the torus (left) and the
Klein bottle (centre): opposite sides should be identiﬁed as indicated by
the arrows. A fundamental domain inS2 for RP2 (right).
3.4.8. Flat tori. The isometry groupIsom(Rn) of Rn contains the trans-
lations subgroup that we identify withRn. The integer translations Γ = Zn
form a discrete subgroup that acts freely onRn, therefore the quotientRn/Γ
is a ﬂat manifold. It is naturally diﬀeomorphic to then-dimensional torus:
Rn/Zn = (R/Z)n∼=S1×... ×S1
| {z }
n
.
Exercise 3.4.10. For every p ∈ Rn the Dirichlet domain D(p) is a n-
dimensional unit cube centred atp.
The ﬂatn-torus may be seen as the unitn-cube with its opposite facets
identiﬁed by translations. The two-dimensional case is shown in Figure 3.16-
(left): by identifying the opposite sides of a square we get a torus.
The n-torus possesses a continuous family of non-isometric ﬂat metrics.
A lattice Γ< Rn is a discrete subgroup isomorphic toZn which spans Rn as
a vector space. We seeΓ as a group of translations.
Exercise 3.4.11. For every latticeΓ, the ﬂat manifoldRn/Γ is diﬀeomor-
phic to then-torus. A fundamental domain is the parallelotope spanned byn
generators of Γ.
A Dirichlet domain forΓ is almost never a parallelotope! In thehexagonal
torus R2/Γ the groupΓ is the equilateral lattice generated by the translations
(1, 0),
( 1
2,
√
3
2
)
and the Dirichlet domain of any point is a regular hexagon. Orientable ﬂat
manifolds are easily classiﬁed (up to diﬀeomorphism) in dimension two.
Proposition 3.4.12. Every closed ﬂat orientable surface is a torus.
Proof. A closed ﬂat surfaceS is isometric to R2/Γ for some discrete
group Γ of orientation-preserving isometries acting freely. Every ﬁxed-point-
free orientation-preserving isometry of R2 is a translation (exercise), hence
Γ< R2. If Γ has rank one thenS is not compact, henceΓ is a lattice andS
is a torus. □
96 3. HYPERBOLIC MANIFOLDS
Flat manifolds more complicated than tori can be constructed by consid-
ering also non-translational isometries ofRn, which exist forn> 3 and also
forn = 2 in the non-orientable setting. For instance, in dimension two we ﬁnd
the Klein bottleby taking Γ as the group generated by the isometries:
τ : (x,y )↦→ (x + 1,y ), η : (x,y )↦→ (1−x,y + 1).
A fundamental domain for the Klein bottle is shown in Figure 3.16-(centre).
Every subgroup Γ′ < Γ furnishes another ﬂat manifoldR2/Γ′ that covers
the Klein bottle. For instance, the subgroups⟨τ⟩ and⟨η⟩ generated respec-
tively byτ andη are both isomorphic toZ but provide two diﬀerent coverings:
the manifold R2/⟨τ⟩ is an inﬁnite cylinder whileR2/⟨η⟩ is an inﬁnite Möbius
strip.
The subgroup Γ′ generated by the translationsτ and η2 is isomorphic to
Z2 and has index 2 inΓ. The Klein bottle is doubly covered by the ﬂat torus
H2/Γ′. A fundamental domain forΓ′ is a rectangle with vertices(0, 0), (1, 0),
(0, 2), (1, 2).
We have seen that the Klein bottle is covered by a torus. In fact, we will
see in Section 4.4 thatevery closed ﬂatn-manifold is covered by a ﬂatn-torus.
Exercise 3.4.13. A squareQ⊂ R2 is a Coxeter polygon and determines
a reﬂection groupΓ. What is the minimum index of a torsion-free subgroup
Γ′< Γ? Which topological surfacesR2/Γ′ do we get?
3.4.9. Real projective spaces.We now exhibit some elliptic manifolds.
Every elliptic manifold is covered bySn and is hence compact and has ﬁnite
fundamental group (because coverings between compact manifolds have ﬁnite
degree).
An important example is the real projective spaceRPn =Sn/Γ where Γ is
the order-two group generated by the antipodal mapι(x) =−x.
Exercise 3.4.14. For everyp∈Sn, the Dirichlet domainD(p) of Γ is the
hemisphere centred atp.
The two-dimensional case is shown in Figure 3.16-(right). The only elliptic
surfaces areS2 and RP2 in virtue of the following.
Proposition 3.4.15.In even dimensionn the only elliptic manifolds areSn
and RPn.
Proof. Let M = Sn/Γ be an elliptic manifold. Every matrix in SO(n +
1) has an eigenvalue +1 because n is even (exercise) and hence acts inSn
with a ﬁxed point. ThereforeΓ contains no non-trivial orientation-preserving
isometries, and since these form a group of index at most two, eitherΓ is
trivial or is generated by an orientation-reversing ﬁxed-point free involution in
O(n + 1), and−I is the only such element (exercise). □
