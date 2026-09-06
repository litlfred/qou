---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-013-the-gravitational-machine-is-hyperbolic
section_title: "The gravitational machine is hyperbolic"
section_number: null
pages: 52-58
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
In this section, we prove one of the important results of this paper: that the gravita-
tional machine maps hyperbolic manifolds to hyperbolic manifolds. This will follow
from a rather nice interaction between topology and the conditions imposed on the
statistical ensemble. It will turn out that the conditions a), b) and c) on the gluing
are precisely what is topologically needed to stay in the class of hyperbolic manifolds.
The following section is somewhat mathematical, but central to our argument, which
is why it is included in the main text. The reader that trusts us on this point can
however jump to section 4.4.
The proof proceeds by induction. Namely, supposeM∈Mis hyperbolic. Then
we will prove that after applying any of the moves 1-3, the resulting manifold fMis
also hyperbolic. Since our initial set of manifolds was the set of handlebodies (which
are hyperbolic), we conclude thatMonly contains hyperbolic manifolds.
Thurston’s theorem.To prove the induction step, we will examine the homotopy
groups of the manifolds produced by the gravitational machine. The main workhorse
in the proof is Thurston’s hyperbolization theorem, which gives a topological criterion
that decides whether a topological 3-manifold admits a hyperbolic structure. More
precisely, it can be stated as [45]:
The interior of a compact 3-manifoldMwith nonempty boundary has a
hyperbolic structure if and only ifMis prime, homotopically atoroidal
and not homeomorphic to(T 2×[0,1])/Z 2.
Let us clarify the terminology used in this theorem. Assuming that the closure of
Miscompactis a relatively weak finiteness condition, ensuring that the hyperbolic
manifold is not too wild, for example it does not have infinitely many boundary
components. Aprimemanifold is a manifold that cannot be written as a non-trivial
connected sum, meaning thatM=M 1#M2 implies thatM 1 = S3 orM 2 = S3. Prime
is implied and essentially equivalent to beingirreducible, which is the condition that
the second homotopy group is trivial,π 2(M) = 0. 30 Thus we will in the following
30The only manifold that is prime, but not irreducible is S 2×S 1, which is not hyperbolic.
– 52 –
replace prime by irreducible.Homotopically atoroidalmeans that every map ofT 2
toMwhich acts injectively on the fundamental groups is homotopic to∂M. This
condition is equivalent to the condition that any subgroup ofπ 1(M) isomorphic to
Z×Zis conjugate to a subgroup ofπ 1(∂M). We will in the following take atoroidal
to mean homotopically atoroidal. 31
We also need the notion of anincompressible surface. These are surfacesS⊂M
whose fundamental group injects into the fundamental group of the 3-manifold. An
incompressible surface is calledboundary parallelif it can be isotoped into a boundary
component ofM; otherwise, it is calledessential. Thurston’s hyperbolization theo-
rem implies that hyperbolic 3-manifolds do not contain essential tori. Connecting to
the 3d gravity vocabulary, we note that a regular neighborhood of an essential torus
is topologically a torus wormholeT 2×I, showing that any bulk topology containing
a torus wormhole is automatically off-shell.
As an example of the above criteria, consider the complement in S 3 of the fol-
lowing handlebody-knot (to be discussed in section 5.3), called5 4 in table 1:
.(4.33)
The handlebody-knot (in red) has a complement in S 3 with a genus-2 boundary, but
it is not atoroidal. In the figure above, the essential torus is highlighted in gray.
Thus, by Thurston’s theorem the5 4-complement does not carry a hyperbolic metric.
Proving hyperbolicity.We now come back to the proof that the gravitational
machine does not map out of the space of hyperbolic 3-manifolds. Since we only
cut and paste manifolds one-by-one, the procedure does not change the compactness
properties ofM. Taking the disconnected union of manifolds (move 1) as well as
performing crossing transformations (move 2) do not map us out of hyperbolicity.
For the latter statement, we use Mostow rigidity [92] which ensures that a hyperbolic
31In the literature, there are two similar but distinct notions of atoroidal 3-manifolds: homotopi-
cally atoroidal and geometrically atoroidal. A manifold is geometrically atoroidal if everyembedded
torus with injectiveπ 1 inMis isotopic to a component of∂M. In contrast, a manifold is homotopi-
cally atoroidal if everyimmersedtorus, including those with self-intersections, with injectiveπ 1 is
homotopic to a component of∂M. The definition of homotopically atoroidal implies geometrically
atoroidal, but the converse does not hold. There are irreducible geometrically atoroidal 3-manifolds
Mthat satisfyZ×Z⊂π 1(M), where theZ×Zfactor is carried by an immersed torus that cannot
be homotoped to∂M. Notable examples include Σ 0,3×S1 (the product of a 3-punctured sphere
with S1), and the complement in S 3 of any torus knot. See e.g. [91] for more details.
– 53 –
structure in the bulk either exists forallboundary moduli or for none of them. In
particular, in the canonical picture crossing transformations act on the boundary
moduli, which do not affect hyperbolicity of the bulk manifold.
Moreover, the non-hyperbolic exceptional manifold (T 2×[0,1])/Z 2 is not gen-
erated by the machine. TheZ 2 quotient flips the interval and corresponds to the
covering transformation ofT 2 such thatT 2/Z2 is a Klein bottle. This exceptional
manifold does have a genus-1 boundary, but it is not one of the PSL(2,Z) family
of Euclidean black holes, and these are the only manifolds the machine generates at
genus 1. This follows directly from conditions b) and c). Namely, at genus 1, there
is a single Wilson line, so self-gluing is not permitted. The only available operation
is the cylinder surgery of two BTZ black holes,M 1 andM 2. This either produces
again a single BTZ black hole (for the trivial Dehn filling) or it introduces parallel
rings, which are not allowed by condition b).
Thus, it only remains to prove that the cylinder surgery operation, i.e. move 3,
keepsMirreducible and atoroidal. For irreducibility, we will use a simple geometric
argument known as the innermost/outermost curve argument. Our proof that the
manifold stays atoroidal is entirely group-theoretic and requires some input from
geometric group theory that we review in appendix B. By induction, it will follow
that any manifold produced by the gravitational machine is hyperbolic.
Irreducible.LetMbe the manifold before gluing and fM=M# P1∼P2 the manifold
after gluing. For the irreducibility part of the proof, it doesn’t matter whether we
are gluing two disconnected components ofMor the same component to itself. As
the induction hypothesis, we assume thatMis hyperbolic.
Recall that to define cylinder surgery, we had to excise the interiors of a pair of
2-punctured spheres inM. This does not change the homotopy groups ofM. Thus,
we will not distinguish betweenMandMwith the balls removed. In particular, we
will write∂M= Σ∪Σ 0,2⊔Σ0,2, where Σ is the original boundary ofMand Σ 0,2⊔Σ0,2
is the disjoint union of two 2-punctured spheres. In fM, these 2-punctured spheres
get identified. We will only use the Ω-loop condition a), which says that neither
m1 norm 2 is contractible inM. It also implies that a powerm n
i forn∈Z\{0}
is not contractible. Otherwise,π 1(M) would have torsion, which is impossible for
hyperbolic manifolds. In other words, the inclusionπ 1(Σ0,2),→π 1(M) is an injection,
for both of the boundary components Σ 0,2.
As a proof by contradiction, suppose thatπ 2(fM)̸= 0. Choose a non-trivial
element inπ 2(fM), which can be represented by an embedded 2-sphereS. 32 W.l.o.g.,
assume thatSintersects the 2-punctured sphere Σ 0,2 transversely in a number of
curvesCi, withi= 1,...,n. We choose the representative and the non-trivial element
inπ 2(fM) such that the number of connected componentsnof the intersection is
32For this one formally uses the sphere theorem of 3-manifolds, saying that any element ofπ 2(M)
may always be represented as a properly embedded sphere.
– 54 –
M1 M2 M1 M2 M2M1
S S
S1
S2
Ci
Ci
Figure 7. Pinching the innermost curve leads to two surfaces with fewer intersections
with the boundary∂M 1 =∂M 2.
minimal. Thisncannot be zero since thenSwould lie entirely inM. But since
π2(M) = 0 by hypothesis (for any connected component ofM), this implies thatS
is null-homotopic inMand thus in fM, contradicting non-triviality ofSinπ 2(fM).
Now choose an innermost curve of the intersection, i.e. aC i that bounds a disk
onS. Then [C i] cannot be a non-trivial element ofπ 1(Σ0,2). For if it were, the disk
would define a null-homotopy of [Ci] in one of the connected components ofM, thus
contradicting the injectivity assumption of the mapsπ 1(Σ0,2),−→π 1(M). ThusC i
has to be a contractible curve on Σ 0,2. SinceC i is contractible on Σ 0,2 and doesn’t
contain any other intersection curves in its interior, we can isotope it to a point.
This pinches the 2-sphereSalong the curveC i and we obtain two 2-spheresS 1 and
S2 connected at a single point. If we separate them, at least one of the 2-spheres
still defines a non-trivial element ofπ 2(fM) by the definition ofπ 2. See figure 7 for
an illustration of this procedure. Say [S 1] is non-trivial. However, the number of
intersections with Σ 0,2 ofS 1 is at mostn−1 since we removed the curveC i. This
contradicts the assumption that we chosenminimal. Thus we have arrived at a
contradiction and conclude thatπ 2(fM) = 0.
Computingπ 1.Next, we want to show that the gluing move 3 also preserves the
fact that the manifoldMis atoroidal. This can be checked by computingπ 1(fM).
The computation differs depending on whether we glue disconnected components or
the same connected component to itself.
For gluing two disconnected componentsM 1#P1∼P2M2, this is a standard appli-
cation of the Seifert-Van-Kampen theorem. Before gluing, we haveM=M 1⊔M 2,
withM 1∩M 2∼= Σ0,2 with fundamental groupπ 1(Σ0,2)∼= Z. The theorem tells us
– 55 –
that after gluing, the fundamental group has the form of an amalgamated product,
π1(fM) =π 1(M1)∗ Zπ1(M2).(4.34)
Let us recall what amalgamation means. Suppose, fori= 1,2, thatπ 1(Mi) is gener-
ated by a setS i with some relationsR i, i.e. has the presentationπ 1(Mi) =⟨S i|Ri⟩.
Then the free productπ 1(M1)∗π 1(M2) has the presentation⟨S 1, S2|R 1, R2⟩, so
we are not imposing any further relations than the ones already present in the two
factors. In particular, we are not imposing that generators inS 1 andS 2 commute
(which would be the case in the direct product). With amalgamation, denoted by
the subscript∗ H, we are additionally identifying a joint subgroupHinπ 1(Mi), in
this caseπ 1(Σ0,2), i.e. we are adding the additional relationsι 1(g) =ι 2(g) for allgin
the subgroup, whereι i :H ,→π 1(Mi) are the inclusions. In our case, we hence add
the additional relationm 1 =m 2.33
When writing the amalgamated product (4.34), we used the fact thatZis natu-
rally a subgroup ofπ 1(M1) andπ 1(M2), i.e. that the inclusion is injective according
to a). The amalgamated product can be viewed as a group-theoretic analogue of the
cylinder surgery, where we ‘glue’ two groups along a common subgroup.
In case that we are performing a self-gluing fM=M# P1∼P2, a similar presenta-
tion of the fundamental group exists. LetMbe the original manifold before gluing.
Letm 1 andm 2 be (based) loops around the two Wilson lines that are to be identified,
so that the fundamental group ofMhas the presentation:
π1(M) =

S,m 1,m 2|R

(4.35)
for some relationsR. Thenπ 1(fM) takes the form of a so-called HNN extension [93].
This means thatπ 1(fM) is obtained by adding a new generatorttogether with the
relationm 2 =tm 1t−1, i.e.
π1(fM) =

S,m 1,m 2,t|R, m 2 =tm 1t−1

.(4.36)
The generatortis usually called the stable letter. Geometrically, it corresponds to
the loop through the ‘wormhole’ Σ 0,2×I, while the self-gluing identifiesm 1 with the
conjugated looptm 2t−1 that also runs through the wormhole. Notice that the choice
ofm 1 andm 2 is only well-defined up to conjugation, but the resulting groups are
isomorphic.34
In writing down the HNN extension (4.36), we again made use of the injectivity
of the inclusions ofπ 1(Σ0,2) inπ 1(fM). More generally, the HNN extension identifies
33In the above constructions, we have to choose a basepoint. We choose a basepoint forπ1(Mi,xi)
in the respective boundaryx i∈Σ 0,2⊂M i, so thatx 1 andx 2 get identified after identifying the
two boundaries.
34This can be derived using the groupoid version of the Seifert-van-Kampen theorem. For a more
down-to-earth explanation, see [94, chapter 5].
– 56 –
two isomorphic subgroupsHandH ′ ofπ 1(M), usually denoted byπ 1(M)∗H∼H′.
Thus it provides the group-theoretic analogue of the self-gluingM# P1∼P2. More
details on the underlying geometric group theory can be found in appendix B.
Malnormality.We now establish two further properties of the amalgamated prod-
uct and the HNN extension in our case, which will let us conclude that they do not
haveZ×Zsubgroups. Let us writeG i =π 1(Mi) in the disconnected case and
G1 =π 1(M) in the connected case, and letH i =⟨m i⟩∼= Z,i= 1,2 for the joint
isomorphic subgroups that we are identifying. W.l.o.g., we can assume thatm 1 is
primitive by condition b). For the case of a connected gluing, the condition c) that
a Wilson line cannot be glued to itself states that
H1∩gH 2g−1 ={1},for allg∈G 1.(4.37)
We next claim thatH 1⊂G 1 is amalnormalsubgroup in both the disconnected and
the connected case. This means that
H1∩gH 1g−1 ={1},for allg∈G 1\H 1.(4.38)
To show this, assume thatgmk
1g−1 =m ℓ
1 fork, ℓ∈Z\{0}. Sincem 1 is primitive, the
left-hand side is ak-th power of a primitive element and the right-hand side is anℓ-th
power of a primitive element. Thus, they can only be equal if|k|=|ℓ|. Furthermore,
sincem 1 is primitive, we only have to analyzegm 1g−1 =m 1 andgm 1g−1 =m−1
1 . In
either case, [m 1,g 2] = 1. SinceG 1 does not haveZ×Zsubgroups by the induction
hypothesis,m 1 andg 2 have to lie in the same infinite cyclic subgroup, which is
necessarily generated bym 1, since it is primitive. Thusg 2 =m n
1 for somen. Since
m1 is again primitive, it follows thatnhas to be even and since the group is torsion-
free we can take the square root of the relation to conclude thatg∈H 1 =⟨m 1⟩.
This establishes (4.38).
Atoroidal.We can now finish the argument quickly by using geometric group the-
ory [95]. We give some more mathematical background on this theory in appendix B.
Let us first treat the amalgamated product case, where we have the following the-
orem [96]. 35 Consider an amalgamated productG=G 1∗H G2. Assume thatHis
malnormal inG 1. Letg∈G. Then the centralizerC(g) inGis either infinite cyclic
orC(g) is conjugate toG 1 orG 2.
We set everything up such that we can apply the theorem. Centralizers inG1 and
G2 are all infinite cyclic groups (sinceG i does not have torsion orZ×Zsubgroups).
Thus, in both possibilities in the above theorem, the centralizer is an infinite cyclic
group. ThusGdoes not haveZ×Zsubgroups.
35We will actually need a small generalization that is for example explained in [97]. In [96], it is
assumed thatHis malnormal inG 1 andG 2. We explain the derivation of this more general version
in appendix B.
– 57 –
We have a similar theorem for the HNN extension. Consider an HNN extension
G=G 1∗H1∼H2. It states: ifH 1 does not intersect any of the conjugates ofH 2 and
is malnormal inG 1, then the centralizerC(g) ofg∈Gis either infinite cyclic or
C(g) is conjugate toG 1. The assumptions of this theorem are guaranteed by (4.37)
and (4.38). SinceG 1 does not haveZ×Zsubgroups by the induction hypothesis, it
follows that alsoGdoes not haveZ×Zsubgroups.
Thus in both gluing types, we do not getZ×Zsubgroups ofπ 1(fM), and hence
fMis homotopically atoroidal. Using Thurston’s theorem, this concludes our proof
that the operations of the machine preserve hyperbolicity.
