---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-020-43-geodesic-spectrum-isometry-groups-and-finite
section_title: "Geodesic spectrum, isometry groups, and finite covers"
section_number: 4.3
pages: 131-136
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
Rn−1/ΓX and the mapΓX =π1(X)→π1(N) = Γ is injective since it sends a
Euclidean isometry to a corresponding parabolic isometry. IfX is geodesic, it
lifts to a hyperplane in∂C, which is simply connected: henceπ1(X)→π1(N)
is injective.
A homotopically non-trivial closed curveγ⊂ X determines a conjugacy
class of hyperbolic or parabolic transformations inΓ. Every element in this
class preserves a unique boundary hyperplane or a point at inﬁnity ofC that
projects back toX, so the conjugacy class determinesX. Therefore distinct
boundary components contain diﬀerent conjugacy classes. □
Wenotethataﬁnite-volumehyperbolicmanifold M mayhavenon-compact
geodesic boundary: an ideal polygon inH2 is a simple example.
4.3. Geodesic spectrum, isometry groups, and ﬁnite covers
We now study the geodesic spectrum and the isometry group of hyperbolic
manifolds. The geodesic spectrum ofM is the set of the lengths of all the
closedgeodesicsin M. Weprovethataﬁnite-volume M hasadiscretegeodesic
spectrum (with ﬁnite multiplicities) and a ﬁnite isometry group.
Then we turn to ﬁnite covers and derive some geometric consequences
from the residually ﬁniteness of fundamental groups.
We are almost exclusively interested in ﬁnite-volume hyperbolic manifolds.
The general strategy when proving something about ﬁnite-volume hyperbolic
manifolds is the following: we ﬁrst suppose that the manifold is compact for
simplicity, and then we adapt the proof to the non-compact case by looking
at what happens to the cusps.
4.3.1. Geodesic spectrum. We start by proving the following.
Proposition 4.3.1.LetM be a ﬁnite-volume complete hyperbolic manifold.
For everyL> 0 there are ﬁnitely many closed geodesics inM shorter thanL.
Proof. Supposethatthereareinﬁnitelymanyclosedgeodesicsshorterthan
L. We know thatM decomposes into a compact part and a ﬁnite union of
truncated cusps. The compact part has ﬁnite diameterD.
Every closed geodesic intersects the compact part because a cusp contains
no closed geodesic. Therefore we can ﬁx a basepointx0∈ M and connect
x0 to these inﬁnitely many geodesics of length<L with arcs shorter thanD.
We use these arcs to freely homotope the geodesics into loops based atx0 of
length<L + 2D, and lift the loops to arcs inHn starting from some basepoint
˜x0∈ Hn.
If two such arcs end at the same point, the corresponding closed geodesics
inM are freely homotopic: this is excluded by Proposition 4.1.13, hence these
endpoints are all distinct. The orbit of˜x0 now contains inﬁnitely many points
in the ballB(˜x0,L + 2D), a contradiction because the orbit is discrete. □
124 4. THICK-THIN DECOMPOSITION
The lengths of the closed geodesics inM form a discrete subset ofRcalled
the geodesic spectrumofM. Let𝓁1(M)> 0 be the minimum of the spectrum
ofM: ashortest closed geodesicinM is a closed geodesic of shortest length
𝓁1(M). It is not necessarily unique (not even if considered up to orientation
reversal), but there are ﬁnitely many of them.
Proposition 4.3.2. IfM is a closed hyperbolic manifold, then
injM = 1
2·𝓁1(M)
and every shortest closed geodesic is simple.
Proof. Thelengthofaclosedgeodesicistheminimumdisplacementofthe
corresponding hyperbolic transformation, so Corollary 4.1.2 gives the equality.
Let nowγ be a shortest closed geodesic. Consider Proposition 4.1.10: ifγ
wraps multiple times along a curveη, thenη is shorter thanγ, a contradiction.
If γ self-intersects transversely at some pointp, we can splitγ naturally as
γ1∗γ2 in π1(M,p ), where bothγ1 and γ2 are shorter thanγ. Either γ1 or
γ2 is non-trivial inπ1(M,p ) and is hence hyperbolic, but it has length smaller
than𝓁1(M): this contradicts Corollary 4.1.15. □
Remark 4.3.3. A shortest geodesic may be non-simple whenM has cusps!
By doubling an ideal triangle along its boundary we construct a hyperbolic
surface called thethrice-punctured spherewhich has three cusps and contains
various closed geodesics, none of which is simple. See Chapter 6.
4.3.2. Isometry group. We now study the isometry groupIsom(M) of a
hyperbolic manifoldM. Recall that thenormaliser N(H) of a subgroupH<G
is the set of elementsg∈G such thatgH =Hg. It is the biggest subgroup
of G containing H as a normal subgroup. The isometry groupIsom(M) has
an algebraic representation.
Proposition 4.3.4. Let M = Hn/Γ be a complete hyperbolic manifold.
There is a natural isomorphism
Isom(M)∼=N(Γ)/Γ.
Proof. Every isometryϕ:M→M lifts to an isometry˜ϕ
Hn ˜ϕ //
π

Hn
π

M ϕ
//M
such that ˜ϕΓ = Γ ˜ϕ: hence ˜ϕ∈N(Γ). The lift is uniquely determined up to
left- or right-multiplication by elements inΓ, hence we get a homomorphism
Isom(M)→N(Γ)/Γ
4.3. GEODESIC SPECTRUM, ISOMETRY GROUPS, AND FINITE COVERS 125
which is clearly surjective (every element inN(Γ) determines an isometry) and
injective (if ˜ϕ∈ Γ thenϕ = id). □
Recall that thecentraliser of H < Gis the set of elementsg∈ G such
thatgh =hg for allh. It is a subgroup ofG.
Exercise4.3.5. Let M = Hn/Γ beaﬁnite-volumehyperbolicmanifold. The
centralizer of Γ in Isom(Hn) is trivial.
4.3.3. Outerautomorphismgroup. Theautomorphismgroup ofagroup
G is the groupAut(G) of all the isomorphismsG→G. The inner automor-
phisms are those isomorphisms of typeg↦→hgh−1 for someh∈G, and they
form a normal subgroupInt(G)◁ Aut(G). The quotient
Out(G) = Aut(G)/Int(G)
is called theouter automorphism groupofG.
If x0,x 1 are two points in a path-connected topological spaceX there
is a non-canonical isomorphismπ1(X,x 0) → π1(X,x 1), unique only up to
post-composing with an inner automorphism. Therefore there is acanonical
isomorphism Out(π1(X,x 0))→ Out(π1(X,x 1)). Hence Out(π1(X)) depends
very mildly on the basepoint.
The group Homeo(X) of all homeomorphisms ofX does not act directly
onπ1(X) because of the inner-automorphism ambiguity, but we get a natural
homomorphism
Homeo(X)−→Out(π1(X))
which is neither injective nor surjective in general. We note that homotopic
self-homeomorphisms give rise to the same element inOut(π1(X)).
4.3.4. Finite isometry groups.We turn back to hyperbolic manifolds.
Proposition 4.3.6. If M is a ﬁnite-volume complete hyperbolic manifold,
the natural map
Isom(M)−→Out(π1(M))
is injective.
Proof. SetM = Hn/Γ, identify Γ withπ1(M) and Isom(M) withN(Γ)/Γ.
With these identiﬁcations the map
N(Γ)/Γ−→Out(Γ)
is just the conjugacy action that sendsh∈ N(Γ) to the automorphismg↦→
h−1gh of Γ. This is an inner automorphism if and only if there is af∈ Γ such
that h−1gh = f−1gf for allg∈ Γ, that is ifhf−1 commutes withg for all
g∈ Γ. Exercise 4.3.5 givesh =f∈ Γ and hence the map is injective. □
Corollary 4.3.7. Let M be a ﬁnite-volume complete hyperbolic manifold.
Distinct isometries ofM are not homotopic.
126 4. THICK-THIN DECOMPOSITION
This is a quite strong fact, from which we deduce the following.
Corollary 4.3.8. The isometry group of every ﬁnite-volume complete hy-
perbolic manifoldM is ﬁnite.
Proof. Weknowthat M isdiﬀeomorphictotheinteriorofsomecompact N
havingk> 0boundarycomponents. LetC1,...,C k⊂M bedisjointtruncated
cusps, all of the same small volumeV > 0. Every isometry ofM permutes
these truncated cusps and ﬁxes their complementC =M\ int(C1∪... ∪Ck).
The set C is compact and preserved by the Lie groupIsom(M), which
is hence compact. To show that it is ﬁnite it suﬃces to prove that it is
discrete. Suppose that a sequence of isometriesϕi converges to the identity:
we will deduce thatϕi is homotopic toid for suﬃciently large values ofi, a
contradiction.
For anyε> 0 there is aϕi that moves all points ofC at distance<ε . If
ε> 0 is suﬃciently small, the isometryϕi preserves eachCi, it restricts to an
isometry of the ﬂat torusXi = ∂Ci and its extension toCi is just a smaller
rescaling ofϕi|Xi at every ﬂat torus leaf in the cusp.
Let alsoε >0 be suﬃciently small, so thatε <injxM for everyx∈ C.
We getd(x,ϕi (x))< injxM for allx∈C, and sinceϕi acts on eachCi just
by rescaling its action onXi, we get the same inequality for everyx∈M.
For every x ∈ M there is a unique geodesic γx of length d(x,ϕi (x))
connecting x and ϕi (x). The geodesicsγx vary continuously withx and we
can use them to deﬁne a homotopy betweenϕi and id: a contradiction. □
The ﬁniteness of the isometry groups is peculiar to the hyperbolic world:
we will see in Remark 7.1.3 that the isometry group of a ﬂat torus is inﬁnite.
4.3.5. Finite covers. LetM = Hn/Γ be a complete ﬁnite-volume hyper-
bolic manifold. How many ﬁnite covers˜M→M are there aboveM? Quite a
lot, thanks to the following.
Proposition 4.3.9. The fundamental groupπ1(M) of a complete ﬁnite-
volume hyperbolic manifoldM is residually ﬁnite.
Proof. The groupπ1(M) is ﬁnitely generated (actually, ﬁnitely presented)
becauseM is homeomorphic to the interior of a compact manifold with bound-
ary, so Proposition 3.1.15 applies. □
This algebraic fact has some nice geometric consequences. Recall that
𝓁1(M) is the length of the shortest closed geodesic inM.
Corollary 4.3.10. For everyL > 0 there is a ﬁnite cover˜M → M with
𝓁1( ˜M)>L .
Proof. There are ﬁnitely many hyperbolic elementsa1,...,a k ∈ π1(M)
such that every closed geodesic inM of length< Lis freely homotopic to
4.3. GEODESIC SPECTRUM, ISOMETRY GROUPS, AND FINITE COVERS 127
some of these. By residually ﬁniteness there is a ﬁnite-index normalH◁π 1(M)
that does not contain any of the elementsa1,...,a k, and hence none of their
conjugates.
Theﬁnite-indexH determinesaﬁnitecover π : ˜M→M withπ∗(π1( ˜M)) =
H. A closed geodesic in˜M cannot be shorter thanL because its image inM
would be freely homotopic to one ofa1,...,a k. □
Corollary 4.3.11. If M is a closed hyperbolic manifold, for everyR > 0
there is a ﬁnite cover˜M→M with inj ˜M >R.
We can summarise this by saying that every closed hyperbolic manifold has
arbitrarily fat ﬁnite covers.
4.3.6. Subgroup separability.The geometric consequences of residually
ﬁniteness are quite remarkable: we now introduce a stronger algebraic notion
that will lead to more geometric applications.
LetG be a group. A subgroupH<G is separable if the intersection of all
the ﬁnite-index subgroups ofG containing H is H itself. In other words, for
every non-trivial elementa∈G\H, there is a ﬁnite-index subgroupG′ < G
that containsH but nota and hence “separates”H froma.
By deﬁnition, the trivial subgroup{e} inG is separable if and only ifG is
residually ﬁnite. Note that, for generalH<G , we cannot require the subgroup
G′ to be normal inG, becauseH itself may not be normal inG, as opposite
to{e}. The following proposition furnishes some interesting examples.
Proposition 4.3.12.Every maximal abelian subgroupH in a residually ﬁnite
groupG is separable.
Proof. More generally, we suppose thatH is maximal with respect to some
word relationf (h1,...,h n) = e. (In our case,f (h1,h 2) = [h1,h 2].) Since G
is residually ﬁnite, there is a sequenceNi◁G of ﬁnite-index normal subgroups
with∩Ni ={e}.
We show thatH =∩iHNi, and we conclude sinceHNi > Ni has ﬁnite
index inG. We haveH⊂∩ iHNi. We now show that the elements of∩iHNi
satisfyf =e, and by maximality ofH we getH =∩iHNi.
For everyNi and h1,...,h n∈ H, we havef (h1Ni,...,h nNi )⊂ Ni since
its projection inG/Ni is trivial. Therefore∩if (HNi,...,HN i ) ={e} and the
elements of∩iHNi satisfyf =e. □
Corollary4.3.13. LetM beacompleteﬁnite-volumehyperbolic n-manifold.
The following subgroups are separable:
• the subgroup⟨ϕ⟩ = Z generated by a primitive hyperbolic transfor-
mationϕ;
• the subgroupπ1(T ) generated by a(n− 1)-torus cusp sectionT.
Proof. Both subgroups are maximal abelian, see Section 4.2.1. □
128 4. THICK-THIN DECOMPOSITION
We deduce a couple of geometric consequences from this algebraic fact.
Corollary4.3.14. LetM beacompleteﬁnite-volumehyperbolic n-manifold.
Every closed geodesicγ in M lifts to a closed geodesic in some ﬁnite covers
ofM of arbitrarily large degree.
Proof. We haveM = Hn/Γ. The closed geodesicγ is obtained by project-
ing the axisl of a primitive hyperbolic elementϕ∈ Γ. Since⟨ϕ⟩ is separable,
there are subgroupsH<π 1(M) of arbitrarily large index that contain⟨ϕ⟩. □
We have discovered in particular that there are many closed hyperbolic
manifolds of bounded injectivity radius with arbitrarily large volume. We can
also use separability to promote some primitive closed geodesics to simple ones
on some ﬁnite coverings.
Corollary4.3.15. LetM beacompleteﬁnite-volumehyperbolic n-manifold.
Every primitive closed geodesicγ inM lifts to a simple closed geodesic in some
ﬁnite cover ofM.
Proof. We haveM = Hn/Γ. The closed geodesicγ is obtained by pro-
jecting the axisl of a primitive hyperbolic elementϕ∈ Γ. If γ is not simple,
it self-intersects ink > 0 points, which lift tok transverse intersections be-
tweenl and some translatesϕ1(l),...,ϕ k(l), for someϕi∈ Γ. Therefore the
elementsψ∈ Γ such thatψ(l) intersectsl transversely are those of the form
ψ =ϕhϕiϕl for somei = 1,...,k andh,l ∈ Z.
Since⟨ϕ⟩ is separable, there is a ﬁnite-indexH <Γ with ϕ1,...,ϕ k⁄∈H
and⟨ϕ⟩⊂ H. Noϕhϕiϕl lies inH, hence for everyψ∈H the linesl andψ(l)
coincide or are disjoint. The linel projects to a simple geodesic inHn/H. □
Concerning cusps, we deduce analogously the following.
Corollary 4.3.16.LetM be a complete ﬁnite-volume hyperbolicn-manifold
and T ⊂ M be a (n− 1)-torus cusp section. The cusp sectionT lifts to a
cusp section in some ﬁnite covers ofM with arbitrarily large degree.
Proof. The subgroup π1(T ) is separable, so there are subgroupsH <
π1(M) of arbitrarily large ﬁnite degree containing it. □
