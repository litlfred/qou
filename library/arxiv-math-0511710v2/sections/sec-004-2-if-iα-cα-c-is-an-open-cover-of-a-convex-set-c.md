---
doc_id: arxiv-math-0511710v2
doc_title: "Higher gauge theory"
section_id: sec-004-2-if-iα-cα-c-is-an-open-cover-of-a-convex-set-c
section_title: "If iα : Cα → C is an open cover of a convex set C by convex subsets Cα ,"
section_number: 2
pages: 9-27
source_pdf: 0511710v2.pdf
source_sha256: f88f50d459080490
doc_brief: "Higher gauge theory — Just as gauge theory describes the parallel transport of poi nt particles using connections on bundles, higher gauge theory describe s the parallel transport of 1-dimensional"
---
and φ: C → X has the property that φ ◦ iα is a plot in X for all α, then φ
is a plot in X.
3. Every map from a point to X is a plot in X.
Deﬁnition 5. A smooth map from the smooth space X to the smooth space
Y is a map f : X → Y such that for every plot φ in X, φ ◦ f is a plot in Y .
In highbrow lingo, this says that smooth spaces are sheaves o n the category
whose objects are convex sets and whose morphisms are smooth maps, equipped
with the Grothendieck topology where a cover is an open cover in the usual sense.
However, smooth spaces are not arbitrary sheaves of this sor t, but precisely those
9
for which two plots with domain C agree whenever they agree when pulled back
along every smooth map from a point to C.
Using this, it is straightforward to check that there is a cat egory C ∞ whose
objects are smooth spaces and whose morphisms are smooth map s. Moreover
this category is cartesian closed, and it has arbitrary limi ts and colimits. It also
has other nice properties:
• Every ﬁnite-dimensional smooth manifold (possibly with bo undary) is a
smooth space; smooth maps between these are precisely those that are
smooth in the usual sense.
• Every smooth space can be given the strongest topology in whi ch all plots
are continuous; smooth maps are then automatically continu ous.
• Every subset of a smooth space is a smooth space.
• We can form a quotient of a smooth space X by any equivalence relation,
and the result is again a smooth space.
• We can deﬁne vector ﬁelds and diﬀerential forms on smooth spa ces, with
many of the usual properties.
With the notion of smooth space in hand, we can make the follow ing deﬁni-
tions:
Deﬁnition 6. Let C∞ be the category whose objects are smooth spaces and
whose morphisms are smooth maps. Then the objects, morphism s and 2-morphisms
of C∞Cat are called smooth 2-spaces , smooth maps , and smooth 2-maps ,
respectively.
Writing down the above deﬁnitions is quick and easy. It takes longer to
understand them and apply them to higher gauge theory. For th is we must
unpack them and look at examples.
To get examples of Lie 2-groups, we can use ‘Lie crossed modul es’. A Lie
crossed module is a quadruple ( G, H, t, α) where G and H are Lie groups,
t: H → G is a Lie group homomorphism and α is a smooth action of G as
automorphisms of H such that t is equivariant:
t(α(g)(h)) = g t(h) g−1
and satisﬁes the so-called ‘Peiﬀer identity’:
α(t(h))(h′) = hh′h−1.
We obtain a Lie crossed module from a Lie 2-group G as follows:
• G is the Lie group of objects of G, Ob( G),
• H is the subgroup of Mor( G) consisting of morphisms with source equal
to 1 ∈ G:
10
• t: H → G is the homomorphism sending each morphism in H to its target,
• α is the action of G as automorphisms of H deﬁned using conjugation in
Mor(G) as follows: α(g)h = 1 gh1g−1.
Conversely, we can reconstruct any Lie 2-group from its Lie c rossed module. In
fact, the 2-category of Lie 2-groups is biequivalent to that of Lie crossed modules
[12]. This gives various examples:
Example 7. Given any abelian group H, there is a Lie crossed module where
G is the trivial group and t, α are trivial. This gives a Lie 2-group G with one
object and H as the group of morphisms. Lie 2-groups of this sort are impor tant
in the theory of abelian gerbes.
Example 8. Given any Lie group H, there is a Lie crossed module with G =
Aut(H), t: H → G the homomorphism assigning to each element of H the cor-
responding inner automorphism, and the obvious action of G as automorphisms
of H. We call the corresponding Lie 2-group the automorphism 2-group of
H, and denote it by AU T (H). This sort of 2-group is important in the theory
of nonabelian gerbes.
We use the term ‘automorphism 2-group’ because AU T (H) really is the
2-group of symmetries of H. Lie groups form a 2-category, any object in a
2-category has a 2-group of symmetries, and the 2-group of sy mmetries of H is
naturally a Lie 2-group, which is none other than AU T (H). See [12] for details.
Example 9. Suppose that 1 →֒→H
t
− →G → 1 is a central extension of the
Lie group G by the Lie group H. Then there is a Lie crossed module with this
choice of t: H → G. To construct α we pick any section s, that is, any function
s: G → H with t(s(g)) = g, and deﬁne
α(g)h = s(g)hs(g)−1.
Since A lies in the center of H, α independent of the choice of s. We do not
need a global smooth section s to show α(g) depends smoothly on g; it suﬃces
that there exist a local smooth section in a neighborhood of e ach g ∈ G.
It is easy to generalize this idea to inﬁnite-dimensional ca ses if we work not
with Lie groups but smooth groups : that is, groups in the category of smooth
spaces. The basic theory of smooth groups, smooth 2-groups a nd smooth crossed
modules works just like the ﬁnite-dimensional case, but wit h the category of
smooth spaces replacing Diﬀ. In particular, every smooth gr oup G has a Lie
algebra g.
Given a connected and simply-connected compact simple Lie g roup G, the
loop group Ω G is a smooth group. For each ‘level’ k ∈ Z, this group has a
central extension
1 → U(1)֒→ˆΩ kG
t
− →Ω G → 1
11
as explained by Pressley and Segal [36]. The above diagram li ves in the category
of smooth groups, and there exist local smooth sections for t: ˆΩ kG → Ω G, so we
obtain a smooth crossed module (Ω G, ˆΩ kG, t, α) with α given as above. This in
turn gives an smooth 2-group which we call the level-k loop 2-group of G,
LkG.
It has recently been shown [14] that LkG ﬁts into an exact sequence of
smooth 2-groups:
1 → L k֒P kG − →G → 1
where the middle term, the level-k path 2-group of G, has very interesting
properties. In particular, when k = ±1, the geometric realization of the nerve of
PkG is a topological group that can also be obtained by killing th e 3rd homotopy
group of G. When G = Spin( n), this topological group goes by the name of
String(n), since it plays a role in deﬁning spinors on loop space [37]. The group
String(n) also shows up in Stolz and Teichner’s work on elliptic cohom ology,
which involves a notion of parallel transport over surfaces [38]. So, we expect
that PkG will be an especially interesting structure 2-group for app lications of
2-bundles to string theory.
To deﬁne the holonomy of a connection, we need smooth groups w ith an
extra property: namely, that for every smooth function f : [0, 1] → g there is a
unique smooth function g: [0, 1] → G solving the diﬀerential equation
d
dt g(t) = f (t)g(t)
with g(0) = 1. We call such smooth groups exponentiable. Similarly, we call a
smooth 2-group G exponentiable if its crossed module ( G, H, t, α) has both G
and H exponentiable. In particular, every Lie group and thus ever y Lie 2-group
is exponentiable. The smooth groups Ω G and ˆΩ kG are also exponentiable, as
are the 2-groups LkG and PkG. So, for the convenience of stating theorems in
a simple way, we henceforth implicitly assume all smooth groups and 2-gro ups
under discussion are exponentiable . We only really need this in Theorems 21
and 23.
Finally, here are some easy examples of smooth 2-spaces:
Example 10. Any smooth space can be seen as a smooth 2-space with only
identity morphisms.
Example 11. Any smooth group (for example a Lie group) can be seen as a
smooth 2-space with only one object.
Example 12. Given a smooth space M , there is a smooth 2-space P1(M ), the
path groupoid of M , such that:
• the objects of P1(M ) are points of M ,
12
• the morphisms of P1(M ) are thin homotopy classes of smooth paths
γ: [0, 1] → M such that γ(s) is constant near s = 0 and s = 1.
Here a thin homotopy between smooth paths γ1, γ2: [0, 1] → M is a smooth
map H: [0, 1]2 → M such that:
• H(s, 0) = γ1(s) and H(s, 1) = γ2(s),
• H(s, t) is independent of t near t = 0 and near t = 1,
• H(s, t) is constant near s = 0 and near s = 1,
• the rank of the diﬀerential dH(s, t) is < 2 for all s, t ∈ [0, 1].
The last condition is what makes the homotopy ‘thin’: it guar antees that the
homotopy sweeps out a surface of vanishing area.
To see how P1(M ) becomes a 2-space, ﬁrst note that the space of smooth
maps γ: [0, 1] → M becomes a smooth space in a natural way, as does the sub-
space satisfying the constancy conditions near t = 0, 1, and ﬁnally the quotient of
this subspace by the thin homotopy relation. This guarantee s that Mor( P1(M ))
is a smooth space. Clearly Ob( P1(M )) = M is a smooth space as well. One can
check that P1(M ) becomes a smooth 2-space with usual composition of paths
giving the composition of morphisms.
In fact, P1(M ) is not just a smooth 2-space: it is also a groupoid. The
inverse of [ γ] is just [ γ], where γ is obtained by reversing the orientation of the
path γ:
γ(s) = γ(1 − s).
Moreover, the map sending any morphism to its inverse is smoo th. Thus P1(M )
is a smooth groupoid : a 2-space where every morphism is invertible and the
map sending every morphism to its inverse is smooth.
3 2-Bundles
In diﬀerential geometry an ordinary bundle consists of two s mooth spaces, the
total space E and the base space B, together with a projection map
E
p
− →B .
To categorify the theory of bundles, we start by replacing sm ooth spaces by
smooth 2-spaces:
Deﬁnition 13. A 2-bundle consists of
• a smooth 2-space E (the total 2-space ),
• a smooth 2-space B (the base 2-space ),
• a smooth map p: E → B (the projection).
13
In gauge theory we are interested in locally trivial 2-bundles. Ordinarily, a
locally trivial bundle with ﬁber F is a bundle E
p
− →B together with an open
cover Ui of B, such that the restriction of E to any of the Ui is equipped with
an isomorphism to the trivial bundle Ui × F → Ui. To categorify this, we would
need to deﬁne a ‘2-cover’ of the base 2-space B. This is actually a rather tricky
issue, since forming the ‘union’ of 2-spaces requires knowi ng how to compose
a morphism in one 2-space with a morphism in another. While th is issue can
be addressed, we prefer to avoid it here by assuming that B is just an ordinary
smooth space, regarded as a smooth 2-space with only identit y morphisms.
We can now state the deﬁnition of a locally trivial 2-bundle. First note that
we can restrict a 2-bundle E
p
− →B to any subspace U ⊆ B to obtain a 2-bundle
which we denote by E|U
p
− →U . Then:
Deﬁnition 14. Given a smooth 2-space F , we deﬁne a locally trivial 2-
bundle with ﬁber F to be a 2-bundle E
p
− →B and an open cover {Ui} of the
base space B equipped with equivalences
E|Ui
ti
− →Ui × F
called local trivializations such that these diagrams:
E|Ui
p
/d26/d26/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52
ti /d47/d47 Ui × F
/d4/d4/d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10
Ui
commute for all i ∈ I.
Readers wise in the ways of categoriﬁcation [39] may ask why w e did not require
that these diagrams commute up to natural isomorphism . The reason is that
Ui, as an ordinary space, has only identity morphisms when we re gard it as a
2-space. Thus, for this diagram to commute up to natural isom orphism, it must
commute ‘on the nose’.
Readers less wise in the ways of categoriﬁcation may ﬁnd the a bove deﬁnition
painfully abstract. So, let us translate it into data that sp ecify how to build a
locally trivial 2-bundle from trivial ones over the patches Ui. For this, we need
to extract transition functions from the local trivializations.
So, suppose E
p
− →B is a locally trivial 2-bundle with ﬁber F . This means
that B is equipped with an open cover U and for each open set Ui in the cover
we have a local trivialization
ti: E|Ui → Ui × F
14
which is an equivalence. This means that ti is equipped with a speciﬁed map
¯ti: Ui × F → E|Ui
together with invertible 2-maps
τi: ¯titi ⇒ 1
¯τi: ti¯ti ⇒ 1
In particular, this means that ¯ti is also an equivalence.
Now consider a double intersection Uij = Ui ∩ Uj. The composite of equiv-
alences is again an equivalence, so we get an autoequivalence
tj ¯ti: Uij × F → Uij × F
that is, an equivalence from this 2-space to itself. By the co mmutative diagram
in Def. 14, this autoequivalence must act trivially on the Uij factor, so
tj ¯ti(x, f) = ( x, f gij(x))
for some smooth function gij from Uij to the smooth space of autoequivalences
of the ﬁber F . Note that we write these autoequivalences as acting on F from
the right, as customary in the theory of bundles. We call the f unctions gij
transition functions , since they are just categoriﬁed versions of the usual
transition functions for locally trivial bundles.
In fact, for any smooth 2-space F there is a smooth 2-space AU T (F ) whose
objects are autoequivalences of F and whose morphisms are invertible 2-maps
between these. The transition functions are maps
gij: Uij → Ob(AU T (F )).
The 2-space AU T (F ) is a kind of 2-group, with composition of autoequivalences
giving the product. However, is not the sort of 2-group we hav e been considering
here, because it does not have ‘strict inverses’: the group l aws involving inverses
do not hold as equations, but only up to speciﬁed isomorphism s that satisfy
coherence laws of their own. So, AU T (F ) is a ‘coherent’ smooth 2-group in the
sense of Baez and Lauda [12].
Next, consider a triple intersection Uijk = Ui ∩ Uj ∩ Uk. In an ordinary
locally trivial bundle the transition functions satisfy th e equation gijgjk = gik,
but in a locally trivial 2-bundle this holds only up to isomorphism . In other
words, there is a smooth map
hijk : Uijk → Mor(AU T (F ))
such that for any x ∈ Uijk ,
hijk (x): gij(x)gjk (x)
∼
− →gik(x).
To see this, note that there is an invertible 2-map
tkτj ¯ti : tk¯tjtj ¯ti ⇒ tk¯ti
15
deﬁned by horizontally composing τj with tk on the left and ¯ti on the right.
Since
tk¯tjtj ¯ti(x, f) = ( x, f gij(x)gjk (x))
while
tk¯ti(x, f) = ( x, f gik(x))
we have
tkτj ¯ti(x, f): (x, f gij(x)gjk (x)) → (x, f gik(x)).
Since this morphism must be the identity on the ﬁrst factor, w e have
tkτj ¯ti(x, f) = (1 x, f hijk (x))
where hijk (x): gij(x)gjk (x) → gik(x) depends smoothly on x.
Similarly, in a locally trivial bundle we have gii = 1, but in a locally trivial
2-bundle there is a smooth map
ki: Ui → Mor(AU T (F ))
such that for any x ∈ Ui,
ki(x): gii(x) → 1.
To see this, recall that there is an invertible 2-map
¯τi: ti¯ti ⇒ 1.
Since
ti¯ti(x, f) = ( x, f gii(x))
we have
¯τi(x, f): (x, f gii(x)) → (x, f),
and since this morphism must be the identity on the ﬁrst facto r, we have
¯τi(x, f) = (1 x, f ki(x))
where ki(x): gii(x) → 1 depends smoothly on x.
In short, the transition functions gij for a locally trivial 2-bundle satisfy the
usual cocycle conditions up to speciﬁed isomorphisms hijk and ki, which we call
higher transition functions . These, in turn, satisfy some cocycle conditions
of their own:
Theorem 15. Suppose E
p
− →B is a locally trivial 2-bundle, and deﬁne the
transition functions gij, hijk , and ki as above. Then:
16
• h makes this diagram, called the associative law , commute for any x ∈
Uijkl :
gij(x) gkl(x) glm(x)
gil(x) glm(x) gij(x) gjm(x)
gim(x)
gij (x) hjkl (x)
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63
hijk (x) gkl(x)
/d127/d127/d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127
hijl (x)
/d127/d127/d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127
hikl(x)
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63
• k makes these diagrams, called the left and right unit laws , commute
for any x ∈ Uij:
gii(x) gij(x) 1 gij(x)
gij(x)
ki(x) gij (x) /d47/d47
=
/d15/d15
hiij (x)
/d37/d37/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75 gij(x) 1 gij(x) gjj (x)
gij(x)
gij (x) kj (x)/d111/d111
=
/d15/d15
hijj (x)
/d121/d121/d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115
Proof. Checking that these diagrams commute is a straightforward c omputation
using the deﬁnitions of g, h, and k in terms of t, ¯t, τ and ¯τ . ✷
The associative law and unit laws are analogous to those whic h hold in a
monoid. They also have simplicial interpretations. In a loc ally trivial bundle,
the transition functions give a commuting triangle for any t riple intersection:
gij gjk
gik
In a locally trivial 2-bundle, such triangles commute only u p to isomorphism:
17
gij gjk
gik
hijk
However, the associative law says that for each quadruple in tersection, this
tetrahedron commutes:
gij gjk
gik
gil gkl
gjl
hijk
hikl
hjklhijl
We can also visualize the left and right unit laws simplicial ly, but they involve
degenerate tetrahedra:
gijgij
gijgij
gijgij
gijgij
giigii ki
1 1 =
hiij
=
gjjgjjkj
11 hijj
18
We are now almost in a position to deﬁne G-2-bundles for any smooth 2-
group G; we only need to understand how a 2-group can ‘act’ on a 2-spac e. For
simplicity we only consider the case of a strict action:
Deﬁnition 16. A (strict) action of a smooth 2-group G on a smooth 2-space
F is a smooth homomorphism
α: G → AU T (F ),
that is, a smooth map that preserves products and inverses.
Note in particular that every smooth 2-group has an action on itself via right
multiplication.
Deﬁnition 17. For any smooth 2-group G, we say a locally trivial 2-bundle
E → M has G as its structure 2-group when the transition functions gij,
hijk , and ki factor through an action G → AU T (F ). In this case we also say P
is a G-2-bundle. If furthermore F = G and G acts on F by right multiplication,
we say P is a principal G-2-bundle.
For a principal G-2-bundle we can think of the transition functions as taking
values in the groups Ob( G) and Mor( G). The reader familiar with gerbes will
note that these functions, satisfying the equations they do , reduce to the usual
sort of cocycle deﬁning an abelian gerbe when ki = 1 and G has the special
form described in Example 7. Similarly, they reduce to a cocy cle deﬁning a
nonabelian gerbe when ki = 1 and G has the form described in Example 8.
Thus there is a close relation between principal 2-bundles a nd gerbes, much like
that between principal bundles and sheaves of groups.
The equation ki = 1 arises because gerbes are often deﬁned using ˇCech
cocycles that are antisymmetric in the indices i, j, k, . . . ,in the sense that group-
valued functions go to their inverses upon an odd permutatio n of these indices.
Thus in this context gii = 1, and one implicitly assumes ki = 1. In fact, Bartels
[17] has shown that every G-2-bundle is equivalent to one with ki = 1. To state
this result, he ﬁrst needed to deﬁne a 2-category of G-2-bundles. This 2-category
is equivalent to the 2-category of abelian or nonabelian ger bes when G has one
of the two special forms mentioned above.
4 2-Connections
For a trivial bundle, the holonomy of a connection assigns el ements of the struc-
ture group to paths in space. Similarly, a 2-connection assi gns objects and mor-
phisms of the structure 2-group to paths and surfaces in spac e. To make this
precise we need the notion of a ‘path 2-groupoid’.
We described the path groupoid of a smooth space M in Example 12. This
has points of M as objects:
• x
19
and thin homotopy classes of paths in M as morphisms:
x •
γ
/d39/d39 • y
The path 2-groupoid also has 2-morphisms, which are thin hom otopy classes of
2-dimensional surfaces like this:
x •
γ 1
/d39/d39
γ 2
/d55/d55 • yΣ
/d11/d19
We call these ‘bigons’:
Deﬁnition 18. Given a smooth space M , a parametrized bigon in M is a
smooth map
Σ: [0 , 1]2 → M
which is constant near s = 0, constant near s = 1, independent of t near t = 0,
and independent of t near t = 1. We call Σ( ·, 0) the source of the parametrized
bigon Σ , and Σ( ·, 1) the target. If Σ is a parametrized bigon with source γ1
and target γ2, we write Σ: γ1 → γ2.
Deﬁnition 19. Suppose Σ: γ1 → γ2 and Σ ′: γ′
1 → γ′
2 are parametrized bigons
in a smooth space M . A thin homotopy between Σ and Σ ′ is a smooth map
H: [0, 1]3 → M
with the following properties:
• H(s, t, 0) = Σ( s, t) and H(s, t, 1) = Σ ′(s, t),
• H(s, t, u) is independent of u near u = 0 and near u = 1,
• For some thin homotopy F1 from γ1 to γ′
1, H(s, t, u) = F1(s, u) for t near
0, and for some thin homotopy F2 from γ2 to γ′
2, H(s, t, u) = F2(s, u) for
t near 1,
• H(s, t, u) is constant for s = 0 and near s = 1,
• H does not sweep out any volume: the rank of the diﬀerential dH(s, t, u)
is < 3 for all s, t, u ∈ [0, 1].
We say two parametrized bigons Σ , Σ ′ lie in the same thin homotopy class if
the pair (Σ , Σ ′) lies in the closure of the thin homotopy equivalence relatio n. A
bigon is a thin homotopy class [Σ] of parametrized bigons.
Deﬁnition 20. The path 2-groupoid P2(M ) of a smooth space M is the
2-category in which:
20
• objects are points x ∈ M :
• x
• morphisms are thin homotopy classes of paths γ in M that are constant
near s = 0 and s = 1:
x
[γ ]
/d37/d37 y
• 2-morphisms are bigons in M
x
[γ 1]
/d37/d37
[γ 2]
/d57/d57[Σ]
/d11/d19 y
and whose composition operations are deﬁned as:
• x
[γ 1]
/d37/d37 y
[γ 2]
/d37/d37 z = x
[γ 1◦γ 2]
/d37/d37 z
where
(γ1 ◦ γ2)(s) :=
{
γ1(2s) for 0 ≤ s ≤ 1/2
γ2(2s − 1) for 1/2 ≤ s ≤ 1
• x
[γ 1]
/d27/d27[γ 2] /d47/d47
[Σ 1]
/d11/d19
[γ 3]
/d67/d67
[Σ 2]
/d11/d19
y = x
[γ 1]
/d37/d37
[γ 3]
/d57/d57[Σ 1Σ 2]
/d11/d19 y
where
(Σ 1Σ 2)(s, t) :=
{
Σ 1(s, 2t) for 0 ≤ t ≤ 1/2
Σ 2(s, 2t − 1) for 1/2 ≤ t ≤ 1
• x
[γ 1]
/d37/d37
γ ′
1
/d57/d57[Σ 1]
/d11/d19 y
[γ 2]
/d37/d37
[γ ′
2]
/d57/d57[Σ 2]
/d11/d19 z = x
[γ 1◦γ 2]
/d37/d37
[γ ′
1◦γ ′
2]
/d57/d57[Σ 1◦Σ 2]
/d11/d19 z
where
(Σ 1 ◦ Σ 2)(s, t) :=
{ Σ 1(2s, t) for 0 ≤ s ≤ 1/2
Σ 2(2s − 1, t) for 1/2 ≤ s ≤ 1
21
One can check that these operations are well-deﬁned, where f or vertical com-
position we must choose suitable representatives of the big ons being composed.
One can also check that P2(M ) is indeed a 2-category. Furthermore, the ob-
jects, morphisms and 2-morphisms in P2(M ) all form smooth spaces, by an
elaboration of the ideas in Example 12, and all the 2-categor y operations are
then smooth maps. We thus say P2(M ) is a smooth 2-category : that is, a
2-category in C ∞. Indeed, the usual deﬁnitions [40] of 2-category, 2-functo r,
pseudonatural transformation, and modiﬁcation can all be i nternalized in C ∞,
and we use these ‘smooth’ notions in what follows. Furthermo re, both mor-
phisms and 2-morphisms in P2(M ) have strict inverses, and the operations of
taking inverses are smooth, so we say P2(M ) is a smooth 2-groupoid .
We obtain the notion of ‘2-connection’ by categorifying the concept of con-
nection. The following result suggests a strategy for doing this:
Theorem 21. For any smooth group G and smooth space B, suppose E → B
is a principal G-bundle equipped with local trivializations over open sets {Ui}i∈I
covering B. Let gij be the transition functions. Then there is a one-to-one
correspondence between connections on E and data of the following sort:
• for each i ∈ I a smooth map between smooth 2-spaces:
holi: P1(Ui) → G
called the local holonomy functor , from the path groupoid of Ui to the
group G regarded as a smooth 2-space with a single object •,
such that:
• for each i, j ∈ I, the transition function gij deﬁnes a smooth natural
isomorphism:
holi|Uij
gij
− →holj|Uij
called the transition natural isomorphism . In other words, this dia-
gram commutes:
gij(x)
gij(y)
holi(γ) hol j(γ)
for any path γ: x → y in Uij.
22
Proof. See Baez and Schreiber [23]. ✷
In addition, it is worth noting that whenever we have a connec tion, for each
i, j, k ∈ I this triangle commutes:
gij gjk
gikholi
holj
holk
The idea behind the above result is that:
• The local holonomy functors hol i are speciﬁed by 1-forms
Ai ∈ Ω 1(Ui, g) .
• The transition natural isomorphisms gij are speciﬁed by smooth functions
gij: Uij → G ,
satisfying the equation
Ai = gijAj g−1
ij + gijdg−1
ij
on Uij.
• The commuting triangle for the triple intersection Uijk is equivalent to
the equation
gijgjk = gik
on Uijk.
Categorifying all this, we make the following deﬁnition:
Deﬁnition 22. For any smooth 2-group G, suppose that E → B is a principal
G-2-bundle equipped with local trivializations over open se ts {Ui}i∈I covering
B, and let the transition functions gij, hijk and ki be given as in Theorem 15.
Suppose for simplicity that ki = 1. Then a 2-connection on E consists of the
following data:
• for each i ∈ I a smooth 2-functor
holi : P2(Ui) → G
x
γ
/d37/d37
η
/d57/d57Σ
/d11/d19
y ↦→ •
holi(γ )
/d37/d37
holi(η )
/d57/d57holi(Σ)
/d11/d19
•
called the local holonomy 2-functor , from the path 2-groupoid P2(Ui)
to the 2-group G regarded as a smooth 2-category with a single object •,
23
such that:
• For each i, j a pseudonatural isomorphism:
gij: holi|P(Ui∩Uj ) → holj|P(Ui∩Uj )
extending the transition function gij. In other words, for each path γ: x →
y in Ui ∩ Uj a morphism in G:
gij(x)
gij(y)
holi(γ) hol j(γ)gij(γ)
depending smoothly on γ, such that this diagram commutes:
holi(γ)
holi(η )holi(Σ)
gij(η )
gij(γ)
gij(x)
gij(y)
holj(γ)
holj(η )holj(Σ)
for any bigon Σ: γ ⇒ η in Uij,
• for each i, j, k ∈ I the transition function hijk deﬁnes a modiﬁcation:
holi
holj
holk
gij gjk
gik
hijk
24
In other words, this diagram commutes:
holk(γ) holi(γ)
holj(γ )
gik(y)
gik(x)
gij(y)
gij(x)
gjk(y)
gjk(x)
hijk(y)
hijk(x)
gik(γ)
gij(γ )
gjk(γ )
for any bigon Σ: γ ⇒ η in Uijk .
In addition, it is worth noting that whenever we have a 2-conn ection, for each
i, j, k, l ∈ I this tetrahedron commutes:
gij gjk
gik
gil gkl
gjl
holi holk
holj
holl
hijk
hikl
hjklhijl
In analogy to the situation for ordinary connections on bund les, one would
like to obtain 2-connections from Lie-algebra-valued diﬀe rential forms. This is
25
our next result. In what follows, ( G, H, t, α) will be the smooth crossed module
corresponding to the smooth 2-group G. We think of the transition function gij
as taking values in Ob( G) = G, and think of hijk as taking values in H. Actually
hijk takes values in Mor( G) ∼
= G ⋉ H, but its G component is determined by its
source, so only its H component is interesting. In these terms, the fact that
hijk (x): gij(x)gjk (x)
∼
− →gik(x)
translates into the equation
gij(x) gjk (x) t(hijk ) = gik(x),
and the associative law of Theorem 15 (i.e. the above tetrahe dron) becomes a
cocycle condition familiar from the theory of nonabelian ge rbes:
hijk hikl = α(gij)(hjkl ) hijl .
Theorem 23. For any smooth 2-group G and smooth space B, suppose that
E → B is a principal G-2-bundle equipped with local trivializations over open
sets {Ui}i∈I covering B, with the transition functions gij, hijk and ki given as in
Theorem 15. Suppose for simplicity that ki = 1 . Let (G, H, t, α) be the smooth
crossed module corresponding to G, and let (g, h, dt, dα) be the corresponding
diﬀerential crossed module. Then there is a one-to-one corr espondence between
2-connections on E and Lie-algebra-valued diﬀerential forms (Ai, Bi, aij) satis-
fying certain equations, as follows:
• The local holonomy 2-functor holi is speciﬁed by diﬀerential forms
Ai ∈ Ω 1(Ui, g)
Bi ∈ Ω 2(Ui, h)
satisfying
FAi + dt(Bi) = 0 ,
where FAi = dAi + Ai ∧ Ai is the curvature 2-form of Ai.
• The transition pseudonatural isomorphism holi
gij
− →holj is speciﬁed by the
transition functions gij together with diﬀerential forms
aij ∈ Ω 1(Uij, h)
satisfying the equations:
Ai = gijAjg−1
ij + gijdg−1
ij − dt(aij)
Bi = α(gij)(Bj) + kij
on Uij, where
kij = daij + aij ∧ aij + dα(Ai) ∧ aij .
26
• The modiﬁcation gij ◦ gjk
hijk
− →gik is speciﬁed by the transition functions
hijk . For this, the diﬀerential forms aij are required to satisfy the equation:
aij + α(gij)ajk = hijk aikh−1
ijk + (dhijk )h−1
ijk + dα(Ai)(hijk ) h−1
ijk
on Uijk .
Proof. See Baez and Schreiber [23]. The ‘vanishing fake curvature’ condition
FAi + dt(Bi) = 0 is necessary for the holonomy 2-functor to preserve the
source and target of 2-morphisms. It also guarantees that th e holonomy over a
parametrized bigon is invariant under thin homotopies. ✷
The reader familiar with gerbes will recognize that Lie-alg ebra-valued dif-
ferential forms of the above sort give a connection on an abelian gerbe when
G is of the special form described in Example 7. Similarly, the y give rise to a
connection with vanishing fake curvature on a nonabelian ge rbe when G is of the
form described in Example 8.
The vanishing fake curvature condition is a strong one. As Br een has em-
phasized, it implies that the h-valued ‘curvature’ 3-form H = dB + dα(A) ∧ B
actually takes values in the kernel of dt, which is an abelian ideal of h. So,
the existence of well-behaved holonomies forces a 2-connec tion to be somewhat
abelian in nature.
