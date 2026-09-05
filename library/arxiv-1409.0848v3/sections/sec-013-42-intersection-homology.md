---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-013-42-intersection-homology
section_title: "Intersection homology"
section_number: 4.2
pages: 43-51
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
Recall from [AFT] that the underlying space of a n-dimensional stratiﬁed space X∈ Snglrn has a
canonical ﬁltration by the union of its strata X0⊂ X1⊂ ... ⊂ Xn = X where each Xi /integerdivideXi−1 is
a smooth i-dimensional manifold. As such, the deﬁnition of Goresky & MacPher son’s intersection
homology [GM1] applies verbatim. Namely, we restrict to stratiﬁed sp acesX have no codimension-1
strata, Xn−1 =Xn−2 and for which the n-dimensional open stratum Xn /integerdivideXn−1 is nonempty.
For the deﬁnition below we use jth-stratum functor (−)j : Snglrn→ Snglr≤j which assigns to
stratiﬁed space X the maximal substratiﬁed space Xj whose strata are of dimension less than j + 1.
Deﬁnition 4.4. Denote the left ideal Bscps
n → Bscn spanned by those basics U for which Un−1 =
Un−2. Deﬁne the category of pseudomanifolds as Snglrps
n = Mﬂd(Bscps
n ) – its objects are those
n-dimensional stratiﬁed spaces for which Xn−1 =Xn−2.
Continuing, choose a perversity function p, i.e., a mapping p :{2, 3,...,n }→ Z≥0 such that
p(2) = 0 and for each i > 2 either p(i) = p(i− 1) or p(i) = p(i− 1) + 1. Recall the following
deﬁnition.
Deﬁnition 4.5 ([GM1]). Aj-simplexg : ∆ j→X isp-allowable if, for every i the following bound
on the dimensions of intersections holds:
dim
(
g(∆ j)∩Xi
)
≤i +j−n +p(n−i) .
A singular chain φ∈ Cj(X) is p-allowable if both |φ| is p-allowable and|∂φ| is p-allowable.
This gives the following deﬁnition of Goresky–MacPherson, of inters ection homology with per-
versityp.
43
Deﬁnition 4.6 ([GM1]). The intersection homology IpC∗(X) of X∈ Snglrps
n is the complex of all
p-allowable singular chains.
The condition of a simplex being p-allowable is clearly preserved by embeddings of stratiﬁed
spaces: if f :X→Y is a morphism in Snglrps
n and g : ∆ j→X is p-allowable, then f◦g : ∆ j→Y
is p-allowable. Further, being p-allowable varies continuously in families of embeddings. That is,
there is a natural commutative diagram:
Snglrn(X,Y ) /d47/d47
/d15/d15
Map(X,Y )
/d15/d15
Map
(
IpC∗(X), IpC∗(Y )
) /d47/d47 Map
(
C∗(X), C∗(Y )
)
Consequently, intersection homology is deﬁned on the ∞-category Snglrps
n ofn-dimensional pseudo-
manifolds. Obviously IpC∗(X⊔Y )∼= IpC∗(X)⊕ IpC∗(Y ). We have the following:
Proposition 4.7. The intersection homology functor
IpC∗ : Snglrps
n −→ Ch
deﬁnes a homology theory in H(Snglrps
n, Ch⊕).
The proof is exactly that intersection homology satisﬁes excision, o r has a version of the Mayer-
Vietoris sequence for certain gluings.
Proof. Let X∼=X−∪R×V X+ be a collar-gluing. Then
IpC∗(R×V )
/d15/d15
/d47/d47 IpC∗(X+)
/d15/d15
IpC∗(X−) /d47/d47 IpC∗(X)
is a pushout diagram in the ∞-category of chain complexes. I.e., the natural map
IpC∗(X−)⊕IpC∗(R×V ) IpC∗(X+)→ IpC∗(X) is a quasi-isomorphism. □
4.3. Link homology theories and Diskfr
d⊂n-algebras
We now consider one of the simplest, but more interesting, classes o fn-dimensional stratiﬁed spaces
– that of n-manifolds together with a distinguished properly embedded d-dimensional submanifold.
While we specialize to this class of stratiﬁed spaces, the techniques f or their analysis are typical of
techniques that can be used for far more general classes.
Recall from [AFT] the ∞-category Mﬂdfr
d⊂n whose objects are framed n-manifolds M with a
properly embedded d-dimensional submanifold L⊂ M together with a splitting of the framing
along this submanifold, and the full ∞-subcategory Diskfr
d⊂n⊂ Mﬂdfr
d⊂n generated under disjoint
union by the two objects Rn :=U n
∅−1 and ( Rd⊂ Rn) := U n
Sn−d−1 with their standard framings.
4.3.1. Explicating Diskfr
d⊂n-algebras
Fix a symmetric monoidal ∞-category V which is⊗-sifted cocomplete. Recall from the discussion
of the push-forward and Corollary 2.29 the map of ∞-categories
∫
Y : AlgDiskfr
n
(V)→ AlgDiskfr
d+1
(V)
deﬁned for any framed ( n−d− 1)-manifold Y .
Proposition 4.8. There is a pullback diagram:
44
AlgDiskfr
d⊂n
(V)
/d15/d15
AlgDiskfr
d+1
( ∫
Sn−d−1
A , HC∗
Dfr
d
(B)
)
/d111/d111
/d15/d15
AlgDiskfr
n
(V)× AlgDiskfr
d
(V) {(A,B )}/d111/d111
That is, the space of compatible Diskfr
d⊂n-algebra structures on the pair (A,B ) is equivalent to the
space of Diskfr
d+1-algebra maps from
∫
Sn−d−1A to the Hochschild cohomology HC∗
Dfr
d
(B); the datum
of a Diskfr
d⊂n-algebra is equivalent to that of a triple ( A,B,α ), where A is a Diskfr
n-algebra, B is a
Diskfr
d -algebra, and α is a map of Diskfr
d+1-algebras
α :
∫
Sn−d−1
A−→ HC∗
Dfr
d
(B)
– this is an Sn−d−1 parametrized family of central Diskfr
d -algebra actions of A on B. In essence,
Proposition 4.8 is a parametrized version of the higher Deligne conjec ture, and in the proof we will
rely on the original version of the higher Deligne conjecture (prove d in§5.3 of [Lu2]).
Proof. The∞-category Diskfr
d⊂n has a natural ﬁltration by the number of components which are
isomorphic to the stratiﬁed space ( Rd⊂ Rn):
Diskfr
n = (Diskfr
d⊂n)≤0→ (Diskfr
d⊂n)≤1→... → colim
i
(Diskfr
d⊂n)≤i≃ Diskfr
d⊂n
Consider the second step in this ﬁltration, the full subcategory ( Diskfr
d⊂n)≤1 of Diskfr
d⊂n whose objects
contain at most one connected component equivalent to ( Rd⊂ Rn).
Disjoint union endows ( Diskfr
d⊂n)≤1 with a partially deﬁned symmetric monoidal structure. This
partially deﬁned symmetric monoidal structure can be articulated a s follows. Consider the pullback
(Diskfr,⊔
d⊂n)≤1 := ( Diskfr
d⊂n)≤1×Diskfr
d⊂n
Diskfr,⊔
d⊂n where here we are using the map from the right
factor ⊔ : Diskfr,⊔
d⊂n → Diskfr
d⊂n. The coCartesian ﬁbration Diskfr,⊔
d⊂n → Fin∗ restricts to a map
(Diskfr,⊔
d⊂n)≤1→ Fin∗ which is an inner ﬁbration and for each edge f in Fin∗ with a lift ~J+ of its
source in ( Diskfr,⊔
d⊂n)≤1 there is either a coCartesian edge over f with source ~J+ or the simplicial set
of morphisms over f with source ~J+ is empty. In this way, by a symmetric monoidal functor from
(Diskfr,⊔
d⊂n)≤1 over Fin∗ it is meant a map over Fin∗ which sends coCartesian edges to coCartesian
edges.
It is immediate that such a symmetric monoidal functor F is equivalent to the data of a Diskfr
n-
algebra F (Rn) and a Diskfr
n−d-F (Rn)-module given by F (Rd⊂ Rn). Extending such a symmetric
monoidal functorF to Diskfr
d⊂n is thus equivalent to giving a Diskfr
d -algebra structure on F (Rd⊂ Rn)
compatible with the Diskfr
n−d-F (Rn)-module. That is, the following is a triple of pullback squares
of∞-categories
AlgDiskfr
d⊂n
(V)
/d15/d15
AlgDiskfr
d
(
Mod
Diskfr
n−d
A (V)
)/d111/d111
/d15/d15
Fun⊗(
(Diskfr
d⊂n)≤1, V
)
/d15/d15
Mod
Diskfr
n−d
A (V)/d111/d111
/d15/d15
AlgDiskfr
n
(V) {A} ./d111/d111
45
Using the equivalence Mod
Diskfr
n−d
A (V)≃ Mod∫
Sn−d−1 A(V) of [Fr], we can then apply the higher
Deligne conjecture to describe an object of the ∞-category
AlgDiskfr
d
(
Mod
Diskfr
n−d
A (V)
)
≃ AlgDiskfr
d
(
Mod∫
Sn−d−1 A(V)
)
.
That is, to upgrade a Diskfr
d -algebra B to the structure of a Diskfr
d -algebra in
∫
Sn−d−1A-modules
is equivalent to giving a Diskfr
d+1-algebra map α :
∫
Sn−d−1A→ HC∗
Dfr
d
(B) to the Dfr
d -Hochschild
cohomology of B. □
4.3.2. Hochschild cohomology in spaces
We now specialize our discussion of Diskfr
d⊂n-algebras to the case where V = S× is the ∞-category
of spaces with Cartesian product, but any ∞-topos would do just as well. In this case, the Dfr
n-
Hochschild cohomology of an n-fold loop space has a very clear alternate description which is given
below.
Proposition 4.9. Let Z = (Z,∗) be a based space which is n-connective. In a standard way, the
n-fold based loop space Ω nZ is a Diskfr
n-algebra. There is a canonical equivalence of Diskfr
n+1-algebras
in spaces
HC∗
Dfrn
(Ω nZ)≃ Ω n Aut(Z)
between the Dfr
n-Hochschild cohomology space of Ω nZ and the n-fold loops, based at the identity map,
of the space of homotopy automorphisms of Z.
Proof. In what follows, all mapping spaces will be regarded as based spaces , based at either the
identity map or at the constant map at the base point of the target argument – the context will
make it clear which of these choices is the appropriate one.
There are equivalences
ModDiskfr
n
Ω nZ (S)≃ Mod∫
Sn−1 Ω nZ (S)≃ ModΩ ZSn−1 (S)≃ S/ZSn−1
sending the object Ω nZ with its natural Diskfr
n-Ω nZ-module self-action to the space Z with the
natural inclusion of constant maps Z→Z Sn−1
. Thus, to describe the mapping space
HC∗
Dfrn
(Ω nZ)≃ ModDiskfr
n
Ω nZ (Ω nZ, Ω nZ)
it suﬃces to calculate the equivalent mapping space Map/ZSn−1 (Z,Z ). By deﬁnition, there is the
(homotopy) pullback square of spaces
Map/ZSn−1 (Z,Z ) /d47/d47
/d15/d15
∗
/d15/d15
Map(Z,Z ) /d47/d47 Map(Z,Z Sn−1
) .
Choose a base point p ∈ Sn−1. The restriction of the evaluation map ev∗
p : Map(Z,Z ) →
Map(Z,Z Sn−1
) is a map of based spaces. Thus, the pullback diagram above factor izes as the
(homotopy) pullback diagrams
Map/ZSn−1 (Z,Z ) /d47/d47
/d15/d15
∗
/d15/d15
Map(Z,Z )Sn
/d47/d47
/d15/d15
Map(Z,Z )
/d15/d15
Map(Z,Z ) /d47/d47 Map(Z,Z Sn−1)
46
where the space of maps from the suspension Sn = ΣSn−1 to Map(Z,Z ) is realized as the homotopy
pullback of the two diagonal maps Map(Z,Z )→ Map(Z,Z )Sn−1
; this is a consequence of the fact
that the functor Map(−,Z ) sends homotopy colimits to homotopy limits, applied to the homotopy
colimit colim(∗← Sn−1→∗ )≃Sn.
Applying the adjunction between products and mapping spaces, we obtain that the Hochschild
cohomology space Map/ZSn−1 (Z,Z ) is the homotopy ﬁber of the map Map
(
Sn, Map(Z,Z )
)
→
Map(Z,Z ) over the identity map of Z, which recovers exactly the deﬁnition of the based map-
ping space Map∗
(
Sn, Map(Z,Z )
)
≃ Map∗
(
Sn, Aut(Z)
)
, where the last equivalence follows by virtue
of Sn being connected.
□
Corollary 4.10. LetZ andW be pointed spaces. Suppose Z isn-connective andW isd-connective.
A Diskfr
d⊂n-algebra structure on the pair (Ω nZ, Ω dW ) is equivalent to the data of a pointed map of
spaces
Z Sn−d−1
−→ BAut(W ) .
Proof. Proposition 4.8 informs us that giving the structure of a Diskfr
d⊂n-algebra on (Ω nZ, Ω dW ) is
equivalent to deﬁning a Diskfr
d+1-algebra map
∫
Sn−d−1
Ω nZ−→ HC∗
Dfr
d
(Ω dW ) .
By way of nonabelian Poincar´ e duality (Theorem 3.18), the factoriz ation homology
∫
Sn−d−1 Ω nZ is
equivalent as Diskfr
d+1-algebras to the mapping space Ω d+1Z Sn−d−1
. Proposition 4.9 gives that the
Hochschild cohomology HC∗
Dfr
d
(Ω dW ) is equivalent to the space of maps to Ω d Aut(W ).
Finally, a ( d + 1)-fold loop map Ω d+1Z Sn−d−1
→ Ω d Aut(W ) is equivalent to a pointed map
between their (d + 1)-fold deloopings. The ( d + 1)-fold delooping of Ω d+1Z Sn−d−1
isZ Sn−d−1
, since
Z isn-connective; the (d + 1)-fold delooping of Ω d Aut(W ) is τ≥d+1BAut(W ), the d-connective cover
of BAut(W ). However, since Z Sn−d−1
is already (d + 1)-connective, the space of maps from it into
τ≥d+1BAut(W ) is homotopy equivalent to the space of maps into BAut(W ). □
4.3.3. F reeDiskfr
d⊂n-algebras
Fix a symmetric monoidal ∞-category V whose underlying ∞-category is presentable and whose
monoidal structure distributes over colimits in each variable. We ana lyze the factorization homol-
ogy theory resulting from one of the simplest classes of Diskfr
d⊂n-algebras, that of freely generated
Diskfr
d⊂n-algebras. That is, there is a forgetful functor
(4.3.1) AlgDiskfr
d⊂n
(V)→ V× V ,
given by evaluating on the objects Rn and ( Rd ⊂ Rn), and this functor admits a left adjoint
Freed⊂n. To accommodate more examples, we modify (4.3.1). Consider the ma ximal sub-Kan
complex E⊂ Dd⊂n. E is a coproduct EndDd⊂n(Rn) ∐ EndDd⊂n (Rd⊂ Rn)≃ O(n) ∐ O(d⊂n), here
O(d⊂n) := O(n−d)×O(d). There results a map of ∞-categories E→ Dd⊂n→ Diskd⊂n→ Disk⊔
d⊂n,
restriction along which gives the map of ∞-categories
AlgDiskd⊂n(V)→ Map(E, V)≃ VO(n)× VO(d⊂n)
to the ∞-category of pairs ( P,Q ) consisting of an O(n)-object in V and an O(d⊂ n)-object in V.
We will denote the left adjoint to this map as FreeE. Denote the inclusion as δ : V× V→ Map(E, V)
as the pairs ( P,Q ) whose respective actions are trivial.
ForX a Dd⊂n-manifold (not necessarily framed) deﬁne
∫
X Free(P,Q)
d⊂n :=
∫
X Freeδ(P,Q)
E . When X is
framed (i.e., is a Dfr
d⊂n-manifold) the lefthand side of this expression has already been fur nished with
meaning as the factorization homology of X with coeﬃcients in the free Diskfr
d⊂n-algebra generated
47
by (P,Q ). The following lemma ensures that the two meanings agree. Recall t he forgetful map
Diskfr,⊔
d⊂n→ Disk⊔
d⊂n.
Lemma 4.11. Let (P,Q ) be a pair of objects of V. Then the universal arrow
Free(P,Q)
d⊂n
≃
− →
(
Freeδ(P,Q)
E
)
| Diskfr,⊔
d⊂n
is an equivalence.
Proof. Denote the pullback ∞-category Efr = E×Dd⊂n Dfr
d⊂n. Like E, Efr⊂ Dfr
d⊂n is the maximal
sub-Kan complex (=∞-groupoid). The projection Efr→ E is a Kan ﬁbration with ﬁbers O(n) or
O(d⊂ n), depending on the component of the base. As so, the inclusion of t he two objects with
their standard framings {Rn} ∐{Rd⊂ Rn}
≃
− →Efr is an equivalence of Kan complexes. Therefore
Map(Efr, V)
≃
− →V× V.
Let us explain the following diagram of ∞-categories
AlgDiskd⊂n(V)
ρ /d47/d47
ρ
/d29/d29
Map(E, V)
ρ
/d2/d2
FreeE
/d6/d6
AlgDiskfr
d⊂n
(V) ρ
/d47/d47
RKan
/d79/d79
Map(Efr, V) .
RKan
/d79/d79
Freed⊂n
/d92/d92
Each leg of the square is an adjunction. All maps labeled by ρ are the evident restrictions. The
maps denoted as RKan are computed as point-wise right Kan extension. (That is, RKan(A) :U↦→
limU→U ′A(U ′) where this limit is taking place in V and is indexed by the appropriate over category.
We emphasize that, unlike the case for left extensions, this point-w ise right Kan extension agrees
with operadic right Kan extension.) As so, the straight square of rig ht adjoints commutes. It follows
that the outer square of left adjoints also commutes.
The right downward map is equivalent to that which assigns to a pair of objects (P,Q ) with
respective actions of O(n) and O(d⊂n), the pair ( P,Q ). The map δ : V× V→ VO(n)× VO(d⊂n) is
a section to this right downward map ρ. We have established the string of canonical equivalences
Freed⊂n≃ Freed⊂n◦
(
ρ◦δ
)
=
(
Freed⊂n◦ρ
)
◦δ≃
(
ρ◦ FreeE
)
◦δ .
This completes the proof.
□
In order to formulate our main result, we ﬁrst give the following deﬁn ition.
Deﬁnition 4.12. ForM a topological space and P an object of V, the conﬁguration object of points
in M labeled by P is
ConfP (M ) =
∐
j≥0
Conf j(M )⊗
Σ j
P ⊗j∈ V
where Confj(M )⊂M ×j is the conﬁguration space of j ordered and distinct points in M .
For the remainder of the section, assume that the monoidal struc ture of V distributes over small
colimits.
48
Proposition 4.13. Let (P,Q ) be a pair of objects of V. Let (L⊂M ) be a Dd⊂n-manifold, i.e., a
smoothn-manifold and a properly embedded d-submanifold. There is a natural equivalence∫
(L⊂M)
Free(P,Q)
d⊂n ≃ Conf P (M /integerdivideL)⊗ ConfQ(L)
between the factorization homology of (L⊂M ) with coeﬃcients in the Diskd⊂n-algebra freely gen-
erated by (P,Q ) and the tensor product of the conﬁgurations objects of the li nk complement M /integerdivideL
and the link L labeled by P and Q, respectively.
We make some remarks before proceeding with the proof of this res ult.
Remark 4.14. We see from this result with ( d ⊂ n) = (3 , 1) that factorization homology in
particular distinguish knots whose knot complements have distinct h omotopy types. For instance,
the unknot, whose knot group is Z, and the trefoil knot, whose knot group is presented by ⟨x,y|x2 =
y3⟩, give rise to diﬀerent factorization homologies.
Remark 4.15. Specializing to the case where the link L is empty, we obtain the equivalence∫
M FreeP
n≃ Conf P (M ). Consequently, factorization homology is not a homotopy invarian t of M , in
as much as the homotopy types of the conﬁguration spaces Conf j(M ) are sensitive to the homeo-
morphism (or, at least, the simple homotopy) type of M , see [LS]. This is in contrast to the case in
which the Diskfr
n-algebraA comes from an n-fold loop space on an n-connective space, in which case
nonabelian Poincar´ e duality (Theorem 3.18) implies that factorizatio n homology with such coeﬃ-
cients is a proper homotopy invariant. However, note that the fac torization homology
∫
M FreeP
n is
independent of the framing on M ; this is a consequence of the fact that the Diskfr
n-algebra structure
on FreeP
n can be enhanced to a Diskn-algebra.
Recall the maps of symmetric monoidal ∞-categories Diskfr,⊔
n → Diskfr,⊔
d⊂n and Diskfr,⊔
d → Diskfr,⊔
d⊂n
indicated by the assignments Rn↦→Rn and Rd↦→(Rd⊂ Rn), respectively. The following lemma
describes the free Diskfr
d⊂n-algebras in terms of free Diskfr
n-algebras and free Diskfr
d -algebras.
Lemma 4.16. Let (P,Q ) be a pair of objects of V. Then the universal arrows to the restrictions
FreeP
n
≃
− →
(
Free(P,Q)
d⊂n
)
| Diskfr,⊔
n
& FreeQ
d⊗
∫
Sn−d−1×Rd+1
FreeP
n
≃
− →
(
Free(P,Q)
d⊂n
)
| Diskfr,⊔
d
are equivalences.
Proof. Recall from the proof of Proposition 4.8 that a Diskfr
d⊂n-algebra structure A on (An,A d),
whereAn is a Diskfr
n-algebra and Ad is a Diskfr
d -algebra, is equivalent to the structure of a Diskfr
n−d-
An-module structure on Ad in the ∞-category AlgDiskfr
d
(V). The forgetful functor factors as the
forgetful functors
AlgDiskfr
d⊂n
(V)−→ AlgDiskfr
n
(V)× AlgDiskfr
d
(V)−→ V× V
and thus, passing to the left adjoints, we can write the free algebr a A on a pair ( P,Q ) as the
composite of the two left adjoints, which gives the free Diskfr
n-algebra on P and the free Diskfr
n−d-
module on the free Diskfr
d -algebra on Q; the latter is calculated by tensoring with the factorization
homology
∫
Sn−d−1×Rd+1 FreeP
n , which is a special case of the equivalence between Diskfr
j -R-modules
and left modules for ∫
Sj−1R, see Proposition 3.16 of [Fr], applied to R = FreeP
n and j =n−d.
□
Proof of Proposition 4.13. Recall the construction of the ∞-operad E∐
inert – it is the free ∞-operad
on E. That is, the map
Fun⊗(E∐
inert, V)
≃
− →Fun(E, V)≃ VO(n)× VO(d⊂n) ,
induced by restriction along the inclusion of the underlying ∞-category E→ E∐
inert, is an equivalence
of Kan complexes – here we are using exponential notation for simplic ial sets of maps. Explicitly,
a vertex of E∐
inert is a pair of ﬁnite sets ( Jn,J d) while an edge is the data of a pair of based maps
49
(Jn)+
a
− →(J ′
n)+ and (Jd)+
b
− →(J ′
d)+ which are inert, which is to say, the ﬁbers over non-base
points a−1(j′) and b−1(j′′) are each singletons, together with a pair of elements α∈ O(n)J ′
n and
β∈ O(d⊂n)J ′
d. We will denote a typical object of E∐
inert as E = (Jn,J d).
The the standard inclusion E→ Mﬂdd⊂n then induces the map of ∞-operads E∐
inert
i
− →Mﬂd⊔
d⊂n
whose value on vertices is
i : (Jn,J d)↦→
( ⨆
Jn
Rn)
⊔
( ⨆
Jd
(Rd⊂ Rd)
)
.
Likewise, let ( O(n)
~P
− →V , O(d⊂ n)
~Q
− →V) be a pair ( P,Q ) of objects in V each equipped with
actions of O(n) and O(d⊂ n), respectively. These data then determine the solid diagram of ∞-
operads
E∐
inert
(P •,Q•)
/d43/d43❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲
i
/d15/d15
Mﬂd⊔
d⊂n
Free( ~P , ~Q)
E /d47/d47 V
in where the value of ( P •,Q •) on (Jn,J d) is canonically equivalent to P ⊗Jn⊗Q⊗Jd as a
(
O(n)Jn×
O(d ⊂ n)Jd
)
-objects. The ﬁller Free( ~P , ~Q)
ǫ is the desired free construction, and is computed as
operadic left Kan extension. Explicitly, for X∈ Mﬂdd⊂n, the value
(4.3.2) Free( ~P , ~Q)
E (X) = colim
E
act
− − →X
(P •,Q •)(E) = colim
(Jn,Jd)
act
− − →X
P ⊗Jn⊗Q⊗Jd
where the colimit is over the ∞-category E∐
X := E∐
inert×Mﬂd⊔
d⊂n
(
(Mﬂd⊔
d⊂n)act
)
/X of active morphisms
in Mﬂd⊔
d⊂n from the image under i of E∐
inert to the object X.
We will now compute the colimit in (4.3.2). By construction, the projec tion E∐
X → E∐
inert is a
right ﬁbration whose ﬁber over E is the Kan complex Mﬂdd⊂n(i(E),X ). Consider the subcategory
of isomorphisms E∐
iso⊂ E∐
inert – it is isomorphic to the category of pairs of ﬁnite sets and pairs of
bijections among them. Denote G = E∐
iso×E∐
inert
E∐
X . Because the inclusion E∐
iso⊂ E∐
inert is ﬁnal, so is
the inclusion G⊂ E∐
X . So the colimit (4.3.2) is canonically equivalent to the colimit of the compo site
G ⊂ E∐
X
(P •,Q•)
−−−−−→V. Because E∐
iso is a coproduct of ∞-groupoids (Kan complexes) indexed by
isomorphism classes of its objects, then G is a coproduct of ∞-groupoids indexed by isomorphism
classes of objects of E∐
iso. As so, the colimit (4.3.2) breaks up as a coproduct over isomorphism
classes of objects of E∐
iso.
We will now understand the [ E]th summand of this colimit. Choose a representative E =
(Jn,J d) ∈ E∐
iso of this isomorphism class. We point out that the Kan complex of Aut(E) ﬁts
into a Kan ﬁbration sequence O(n)Jn× O(d⊂ n)Jd→ Aut(E)→ Σ Jn× Σ Jd. Consider the right
ﬁbration ( E∐
iso)/E→ E∐
iso whose ﬁber over E′ is the Kan complex Iso(E′,E ) which is a torsor for the
Kan complex Aut(E) is E′ if isomorphic to E and is empty otherwise. Denote the resulting right
ﬁbration GE = ( E∐
iso)/E×E∐
iso
G −→ G whose ﬁbers are either a torsor for Aut(E) or empty. The
composite GE→ G⊂ E∐
X
(P •,Q•)
−−−−−→V is canonically equivalent to the constant map at P ⊗Jn⊗Q⊗Jd.
It follows from the deﬁnition of the tensor over spaces structure , that the colimit of this composite
is (
Mﬂdd⊂n
(
i(Jn,J d),X
) )
⊗
(
P ⊗Jn⊗Q⊗Jd
)
.
We conclude from this discussion that the colimit of the composite G⊂ E∐
X
(P •,Q•)
−−−−−→V is
(4.3.3)
∐
[(Jn,Jd)]
(
Mﬂdd⊂n
(
i(Jn,J d),X
) )
⊗Aut(Jn,Jd)
(
P ⊗Jn⊗Q⊗Jd
)
.
50
We make expression (4.3.3) more explicit for the case that ( ~P, ~Q) = δ(P,Q ) is a pair of objects
with trivial group actions. As so, the map G ⊂ E∐
X
(P •,Q•)
−−−−−→V factors through the projection
G→ E∐
iso→ (Fin∗)iso the groupoid of ﬁnite sets and bijections – we denote this groupoid a s Σ.
Recall that the Dd⊂n-manifold X = (L⊂M ) is the data of a framed n-manifold M , a properly
embedded smooth submanifold L, and a splitting of the framing along L. Evaluation at the origins
of i(Jn,J d) =
( ⨆
Jn Rn)
⊔
( ⨆
Jd
(Rd⊂ Rn)
)
gives a map
Mﬂdd⊂n
(
(
⨆
Jn
Rn)⊔ (
⨆
Jd
(
Rd⊂ Rn)
)
, (L⊂M )
)
−→ Conf Jn(M /integerdivideL)× Conf Jd(L) .
This map is evidently natural among morphisms among the variable ( Jn,J d)∈ G where the action
of G on the righthand side factors through the projection G→ Σ. There results a Σ-equivariant map
(
Mﬂdd⊂n
(
i(Jn,J d), (L⊂M )
) )
/O(n)Jn ×O(d⊂n)Jd
∼
−→ Conf Jn(M /integerdivideL)× Conf Jd(L) ;
and for standard reasons it is an equivalence of Kan complexes. We c onclude that
Freeδ(P,Q)
E (L⊂M )
≃
− →Conf P (M /integerdivideL)⊗ Conf Q(L) .
Finally, the formula
Freeδ(P,Q)
E (L⊂M ) =
∫
(L⊂M)
Freeδ(P,Q)
E
is a formal consequence of commuting left Kan extensions (here we are using the same notation
for Freeδ(P,Q)
E and its restriction to Disk⊔
d⊂n). With Lemma 4.11, this completes the proof of the
proposition.
□
Remark 4.17. The methods employed here in §4.3.3 have been intentionally presented to accom-
modate much greater generality. For instance, with appropriate m odiﬁcations of the statements,
the role of Dd⊂n (or its framed version) could be replaced by any category of basics B. Likewise,
the maximal sub-Kan complex E⊂ Dd⊂n could be replaced by any map E→ B of∞-categories.
