---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-017-36-orbifolds
section_title: "Orbifolds"
section_number: 3.6
pages: 109-117
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Exercise 3.5.8. The metric spaceX/Γ is the completion ofX/Γ and is
homeomorphic to Rn.
The image of˜S along the quotientπ :X→X/Γ is a copy of˜S and should
now be interpreted as a singularity with cone angleθ. Whenθ = 2kπ for some
integerk the mapπ :X→ Hn factors as
X
π1
−→X/Γ
π2
−→ Hn.
When k =±1 the mapπ2 is an isometry. We introduce the following deﬁni-
tion.
Deﬁnition 3.5.9. Ahyperbolic manifoldM with cone angles is a metric
space with charts in someX/Γ and transition maps that are isometries.
The term “isometries” should be interpreted in the strongest sense: the
transition maps send singular points to singular points, and outside of the
singular points these are isometries of Riemannian manifolds.
The points inM that are mapped along charts to some singular set form
a hyperbolic codimension-two submanifold inM with some cone angleθ, and
diﬀerent components may have diﬀerent cone angles. Points with cone angle
2π may be considered as ordinary points, while points with cone angle diﬀerent
from 2π are singular and form thesingular locusofM.
The singular locus ofM is a geodesic codimension-two manifold, and its
complement is an ordinary hyperbolic manifold, whose metric completion isM.
Flat and spherical manifolds with cone angles are deﬁned in the same way.
3.5.6. Examples. The following simple construction is already a source
of many two-dimensional examples: letP be any polygon inH2, R2, or S2,
with some inner anglesα1,...,α k. By doublingP along its edges we get a
topological sphere withk cone points of angles2α1,..., 2αk < 2π. This is a
hyperbolic, ﬂat, or spherical surface with cone angles.
Another simple but maybe more intriguing construction is the following:
pick any polyhedron P in H3, R3, or S3. The faces of P are (hyperbolic,
ﬂat, or elliptic) polygons that glue isometrically along the edges: hence∂P is
a topological sphere with a natural structure of (hyperbolic, ﬂat, or elliptic)
manifold with cone angles at the vertices.
Toconstructexamplesindimensionthreeweneedabitmoreworkbecause
polyhedra have more strata. Non-compact examples are easier to build: let
P⊂ H3 be any ideal hyperbolic polyhedron, with somek edges with dihedral
angles α1,...,α k; the double ofP is naturally a hyperbolic cone manifold
where the edges form the singular locus with cone angles2α1,..., 2αk.
3.6. Orbifolds
An orbifold is an object locally modelled on ﬁnite quotients ofRn. It
naturally arises when we quotient a Riemannian manifold by a discrete group
102 3. HYPERBOLIC MANIFOLDS
V1 V2
V3
O
w
1
w
2 w
3
c
21
c
32
Figure 3.18. An orbifoldO with three local modelsO =U1⊃U2⊃U3.
The group Γ1 = Z2× Z2 acts onV1 by reﬂections on the two coordinate
axis, the groupΓ2 = Z2 acts onV2 by reﬂection on the horizontal axis, the
group Γ3 is trivial.
of isometries that may not act freely. Orbifolds behave like manifolds on many
aspects.
3.6.1. Deﬁnition.Let Γ< O(n) be a ﬁnite group of linear isometries and
V ⊂ Rn be a Γ-invariant open set. The resulting map
ϕ:V −→V/ Γ
is called alocal orbifold model. For instance, we may pickV =B(0,r ).
We now generalise manifolds by allowing local orbifold models in the atlas.
Deﬁnition 3.6.1. LetO be a Hausdorﬀ paracompact topological space.
An orbifold atlas on O is an open covering{Ui}i∈I of O, closed by ﬁnite
intersections and equipped with local orbifold models
ϕi :Vi−→Vi/Γi =Ui.
The local models are connected by some appropriate transition functions: for
every inclusionUi⊂Uj there is an injective homomorphism
fij : Γi ↪→ Γj
and aΓi-equivariant smooth embeddingψij :Vi ↪→Vj compatible with the local
models, that is
ϕj◦ψij =ϕi.
Two such atlases are equivalent if the are contained in some bigger atlas.
The spaceO equipped with an orbifold atlas is anorbifold of dimensionn. See
an example in Figure 3.18.
3.6. ORBIFOLDS 103
Remark 3.6.2. We think at the mapsψij andfij as deﬁned only up to the
action of Γj (which acts onψij by composition and onfij by conjugation). In
particular, ifUi⊂Uj⊂Uk thenwecan verifythatthe equalities ψik =ψjk◦ψij
andfik =fjk◦fij hold only up to this ambiguity. See Figure 3.18.
The isotropy group Γp of a pointp∈ O is the stabiliser of any lift ofp
in any local modelV with respect to the action ofΓ. By deﬁnitionΓp is a
ﬁnite subgroup ofO(n). A pointp is regular if its isotropy group is trivial, and
singular otherwise.
Example 3.6.3. The isotropy groupOp in the orbifoldO from Figure 3.18
is Z2× Z2 at the origin,Z2 at the axis, and trivial elsewhere.
Proposition 3.6.4. The regular points in an orbifold form a dense subset.
Proof. On a local modelV → V/ Γ, a singular point is the image of the
ﬁxed point locus of some element inΓ, which is in turn a proper subspace.□
An orbifold islocally orientedif all the ﬁnite groupsΓ lie inSO(n), and it is
oriented if, inaddition, allthetransitionmaps ψij areorientation-preserving. In
a locally oriented orbifold reﬂections are not admitted and hence the singular
locus has codimension> 2. An open subset of an orbifold is naturally an
orbifold.
3.6.2. Examples. Orbifolds are natural objects and there are plenty of
nice examples around.
Example 3.6.5. A diﬀerentiable manifold is an orbifold whose points are
all regular. A diﬀerentiable manifold with boundary may be interpreted as an
orbifold whose boundary points have the local structure of typeRn/Γ where
Γ = Z2 is generated by a reﬂection along a hyperplane. The boundary should
be interpreted as amirror.
Exercise3.6.6. Constructanorbifoldstructureonthetriangleassuggested
by Figure 3.19.
Example 3.6.7. LetΓ< O(n) be ﬁnite andV ⊂ Rn a Γ-invariant open set.
The quotientV/ Γ has an orbifold structure, deﬁned by the unique local model
V →V/ Γ.
We generalise the last example.
Proposition 3.6.8. If M a Riemannian manifold and Γ < Isom(M) is a
discrete subgroup, the quotientM/Γ has a natural orbifold structure.
Proof. Take a pointp∈ M/Γ and ˜p∈ M a lift. Since Γ is discrete, the
stabiliser Γ˜p of ˜p is ﬁnite and there is ar >0 such that exp˜p(Br (0)) =Br (˜p)
andg(Br (˜p)) intersectsBr (˜p) for someg∈ Γ if and only ifg∈ Γ˜p.
104 3. HYPERBOLIC MANIFOLDS
Figure 3.19. An orbifold structure on the triangle constructed using the
local models from Figure 3.18. The isotropy group is Z2× Z2 at the
vertices, Z2 at the edges, and trivial in the interior.
The ball Br (˜p) is clearly Γ˜p-invariant. The group Γ˜p acts linearly and
orthogonally onBr (0) and we get an orbifold local model
Br (0)−→Br (0)/Γ˜p
∼=Br (˜p)/Γ˜p =Up
where the diﬀeomorphism is induced by the exponential map. We have con-
structed an orbifold local modelUp aroundp. We extend the covering{Up}
thus obtained by adding all the non-empty intersections. □
This is the richest source of nice examples. The quotient mapM→M/Γ
is a covering, in an appropriate sense that we now explain.
3.6.3. Coverings. Let Γ′ < Γ < O(n) be ﬁnite groups andV ⊂ Rn a
Γ-invariant open set. The natural map
ϕ:V/ Γ′↦−→V/ Γ
between the two orbifolds is alocal covering.
Deﬁnition 3.6.9. A continuous mapp : ˜O → O between orbifolds is a
covering if every pointp∈O has a neighbourhoodU with p−1(U) =⊔i∈IUi
and every restrictionp|Ui :Ui→U is a local covering.
The following is the main source of examples.
Example 3.6.10. LetM be a Riemannian manifold andΓ′< Γ< Isom(M)
be discrete groups. The natural mapM/Γ′→M/Γ is an orbifold covering.
Deﬁnition 3.6.11 (The good, the bad, and the very good). An orbifold is
good if it is covered by a manifold, and it isbad otherwise. It isvery goodif
it is ﬁnitely covered by a manifold.
3.6.4. Hyperbolic, ﬂat, and elliptic orbifolds.We deﬁne ahyperbolic,
ﬂat, or elliptic orbifold to be an orbifold whose local models are isometric
quotients of balls inHn, Rn, orSn, and whose transition functions are also
isometries.
The quotient of a hyperbolic, ﬂat, or spherical manifold by a discrete group
of isometries is naturally a hyperbolic, ﬂat, or elliptic orbifold.
3.6. ORBIFOLDS 105
a b
c
a b
c
Figure3.20. Theindex-twoorientation-preserving Γor(a,b,c )◁Γ(a,b,c )
deﬁnes an index-two orbifold coveringO→ ∆, whereO is a 2-sphere with
three singular points and∆ a triangle.
Example 3.6.12. The triangle groupΓ(a,b,c ) introduced in Section 3.4.5
isadiscretegroupofisometriesof S2, R2, orH2. Itdeﬁnesatriangularorbifold
∆, whichishyperbolic, ﬂat, orelliptic, accordingtowhether1
a + 1
b + 1
c issmaller,
equal, or bigger than 1. The isotropy groups are the dihedralD2a,D 2b, and
D2c at the vertices,Z2 at the edges, and trivial elsewhere.
The index-two subgroupΓor(a,b,c )◁ Γ(a,b,c ) consisting of orientation-
preserving isometries is sometimes called avon Dyck group. It deﬁnes an ori-
entable orbifoldO that double-covers∆. The orbifoldO is a topological sphere
with three singular points with rotation isotopy groupsZ/aZ, Z/bZ, Z/cZ. See
Figure 3.20.
Exercise 3.6.13. Show that the following is a presentation forΓor(a,b,c ):
⟨r,s,t |ra,sb,tc,rst ⟩.
The tripler,s,t of generators is intrinsically determined in the group up to
simultaneous conjugation or inversion. Diﬀerent unordered triples (a,b,c )
produce non-isomorphic Von Dyck groupsΓor(a,b,c ).
Hints. The groupΓ(a,b,c ) preserves the tessellationT of H2, R2, orS2
into triangles with angles π
a, π
b, π
c, so its ﬁnite-order elements are rotations
along some vertices ofT. Three rotationsr,s,t that satisfyrst = 1 are of
some very special kind. □
Example 3.6.14. More generally, every hyperbolic (or ﬂat, elliptic) Coxeter
polyhedron is a hyperbolic (or ﬂat, elliptic) orbifold.
Example 3.6.15. Quotient the ﬂat torusT = R2/Z2 by theelliptic invo-
lution (x,y )↦→ (−x,−y ). This isometry ofT has four ﬁxed points and the
quotient ﬂat orbifold is a sphere with four singular points, see Figure 3.21.
There are also many interesting non-compact orbifolds.
Example 3.6.16. A fundamental domain forPSL2(Z) was shown in Figure
3.15. By gluing its sides according to the action we see quite easily that
the hyperbolic orbifoldH2/PSL2(Z) is non-compact and contains two rotational
points of order 2 and 3, see Figure 3.22.
106 3. HYPERBOLIC MANIFOLDS
Figure 3.21. The elliptic involution quotients the torus to a sphere with
four singular points. The ﬁxed points and their images are drawn in red.
We show both a planar (left) and spacial (right) picture.
Figure 3.22. The hyperbolic orbifoldH2/PSL2(Z) is obtained by mirroring
the sides of a triangle with inner anglesπ
3, π
2, and zero (left). The orbifold
is topologically a punctured sphere with two singular points with rotational
isotropy Z2 and Z3 (right).
Exercise 3.6.17. The 1-dimensional compact orbifolds areS1 and the seg-
ment [0, 1]with mirrored endpoints. Show that there are coveringsS1→ [0, 1]
of degree 2, and also coverings[0, 1]→ [0, 1] of any positive degree.
When O = X/Γ and X is a simply connected manifold, we say thatΓ is
the fundamental group of O. It is also possible to deﬁne the fundamental
group for a generic orbifold using the appropriate orbi-notions of paths and
homotopies.
3.6.5. Conemanifolds. Hyperbolic(ﬂat, elliptic)conemanifoldsandorb-
ifolds are diﬀerent objects, but they have a wide common intersection.
A hyperbolic (ﬂat, elliptic) orbifoldO whose isotropy groupsOp are either
trivial or generated by a 2π
p -rotation along a codimension-two subspace is
naturally a hyperbolic (ﬂat, elliptic) cone manifold with cone angles2π
p . The
singular set may consist of various connected components and the natural
numberp depends on the component.
3.6. ORBIFOLDS 107
Conversely, every hyperbolic (ﬂat, elliptic) manifold with cone angles that
divide 2π can be given a natural hyperbolic (ﬂat, elliptic) orbifold structure
whose singular set consists of rotational points only. Moreover, we can easily
prove that it is a good one:
Proposition 3.6.18. Every hyperbolic (ﬂat, elliptic) manifoldM with cone
angles that divide2π is a good hyperbolic (ﬂat, elliptic) orbifold. IfM is com-
plete, thenM = Hn/Γ (Rn/Γ,Sn/Γ) for some discrete groupΓ of isometries.
Proof. We consider for simplicity only the hyperbolic case. We must prove
thatM is orbifold-covered by a hyperbolic manifold.
The singular setS ⊂ M decomposes into connected componentsS =
⊔iSi, each with a cone angle2π
pi
for some integerpi> 2. The complement
M′ =M\S is a non-complete hyperbolic manifold and as such it is equipped
with a developing mapD : ˜M′→ Hn and a holonomyρ:π1(M′)→ Isom(Hn).
We pick a loopµi around each component Si of S and note that by
deﬁnitionρ(µi ) is an elliptic isometry that rotatesHn around a codimension-
two subspace by the angle2π
pi
. In particularρ(µi ) has orderpi.
We consider the regular coveringN→M′ corresponding to the subgroup
kerρ and giveN the hyperbolic structure induced byM′. The completionN
of N is a hyperbolic manifold that orbifold-coversM: since ρ(µi ) has order
preciselypi, the added singular points inN have cone angle2π and are hence
ordinary.
If M is complete, then N also is and hence N = Hn/Γ′. We deﬁne
Γ < Isom(Hn) to be the group generated by Γ′ and any lifts of the deck
transformations ofN→M, and we getM = Hn/Γ. □
Corollary 3.6.19.IfM is complete and has ﬁnitely generated fundamental
group, then it is very good.
Proof. We know thatM = Hn/Γ and we apply Selberg’s Lemma. □
Summing up, complete hyperbolic cone manifolds with angles that divide
2π can be promoted to good orbifolds and hence to quotientsHn/Γ. We will
encounter many examples in dimensions two and three later on.
3.6.6. References. All the material presented here is standard and intro-
duced in various books, like Benedetti – Petronio [4] and Ratcliﬀe [49]. A
beautiful introduction to regular polytopes is Coxeter’s 1963 book [14], while
the reader interested in Coxeter polytopes may consult Vinberg’s survey [59].
The theory of orbifolds and cone manifolds presented here is quite limited:
togetmorebackground, thereadermayconsultThurston’snotes[ 56, Chapter
13] for the orbifolds, and McMullen’s paper [40] for the cone manifolds.
CHAPTER 4
Thick-thin decomposition
A peculiar aspect of hyperbolic geometry is the existence of complete hy-
perbolic manifolds that have ﬁnite volume but are not compact. These mani-
folds behave like the compact ones in many aspects, but are sometimes easier
to construct. They arise naturally when we study hyperbolic surfaces, and are
a fundamental constituent of Thurston’s geometrisation of three-manifolds.
We prove here a structure theorem for all such manifolds. The theorem
says that every ﬁnite-volume complete hyperbolic manifold can be decomposed
into two domains: a thick part which is compact and has injectivity radius
bounded from below, and athin part that consists of cusps. A cusp is a
(truncated) hyperbolic manifold of typeN× [0, +∞), where every section
N×t has a ﬂat metric that shrinks exponentially witht.
The core of this theorem is a lemma about discrete subgroups of Lie
groups called theMargulis Lemma. We will apply this lemma also to the other
geometries and prove Bierbach’s Theorem, that states that every compact ﬂat
manifold is covered by a torus.
Throughout the discussion we will also study some general aspects of
ﬁnite-volume complete hyperbolic manifolds, concerning in particular closed
geodesics, isometry groups, and ﬁnite covers.
