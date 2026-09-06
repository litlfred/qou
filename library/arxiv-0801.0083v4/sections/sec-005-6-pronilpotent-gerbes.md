---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI"
section_id: sec-005-6-pronilpotent-gerbes
section_title: "Pronilpotent Gerbes"
section_number: 6
pages: 29-36
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
doc_brief: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI — W e introduce the notion of central extension of gerbes on a to po- logical space X."
---
Let X be a topological space. Recall that given an inverse system {Gp}p∈N of
sheaves of groups on X, its inverse limit is the sheaf of groups lim ←p Gp whose
group of sections on an open set U is
Γ(U, lim←p Gp) = lim←p Γ(U, Gp).
Deﬁnition 6.1. Let G be a sheaf of groups on X.
(1) A normal ﬁltration of G is a descending sequence {Np}p∈N of sheaves of
normal subgroups of G.
(2) A central ﬁltration of G is a normal ﬁltration {Np}p∈N, such that N0 = G,⋂
p Np = 1, and for every p the extension of sheaves of groups
1 → N p/ Np+1 → G/ Np+1 → G/ Np → 1
is central.
(3) Let {Np}p∈N be a normal ﬁltration of G. We say that G is complete with
respect to this ﬁltration if the canonical homomorphism of s heaves of groups
G → lim←p G/ Np
is an isomorphism.
(4) If G is complete with respect to some central ﬁltration, then we c all it a
pronilpotent sheaf of groups .
Note that when {Np}p∈N is a central ﬁltration, then each Np/ Np+1 is a sheaf of
abelian groups.
Deﬁnition 6.2. Let G be a sheaf of groups on X, with central ﬁltration {Np}p∈N.
An open set U ⊂X is called acyclic with respect to {Np}p∈N if the following two
conditions hold.
(i) For every p ≥ 0 and i> 0 the sheaf cohomology group H i(U, Np/ Np+1) is
trivial.
(ii) For every q ≥p ≥ 0 the canonical group homomorphism
Γ(U, Np) → Γ(U, Np/ Nq)
is surjective.
Lemma 6.3. Let {Np}p∈N be a central ﬁltration of the sheaf of groups G. Suppose
that G is complete with respect to the ﬁltration {Np}p∈N, and the open set U ⊂X
is acyclic with respect to {Np}p∈N. Let G := Γ(U, G) and Np := Γ(U, Np). Then G
is complete with respect to the ﬁltration {Np}p∈N.
Proof. Condition (ii) of Deﬁnition 6.2, combined with Proposition 5.6(1), say that
for every p there is an exact sequence of groups
1 →Np →G → Γ(U, G/ Np) → 1.
Now use Deﬁnition 6.1(3). □
30 AMNON YEKUTIELI
In the situation above the ﬁltration {Np}p∈N of G is separated. Therefore it
deﬁnes a metric topology on G, say by letting Np ·g = g ·Np be the ball of
radius 2−p around the point g ∈ G (cf. [CA, Section III.5]). The condition that
G ∼= lim←p G/N p translates to G being a complete metric space.
Deﬁnition 6.4. Let G be a sheaf of groups on X, with central ﬁltration {Np}p∈N.
(1) A collection U = {Uk}k∈K of open sets of X is called acyclic with respect
to {Np}p∈N if every ﬁnite intersection Uk0,...,k m is acyclic with respect to
{Np}p∈N, in the sense of Deﬁnition 6.2.
(2) We say that there are enough acyclic coverings with respect to {Np}p∈N if
every open covering U of an open set U ⊂X admits a reﬁnement U′ which
is acyclic with respect to {Np}p∈N.
Now we move to gerbes. Let G be a gerbe on X. The notion of normal sub-
groupoid N ⊂ G was introduced in Deﬁnition 3.6.
Deﬁnition 6.5. Let G be a gerbe on X.
(1) A normal ﬁltration of G is a descending sequence {N p}p∈N of normal sub-
groupoids of G.
(2) A central ﬁltration of G is a normal ﬁltration {N p}p∈N, such that for every
local object i of G, the ﬁltration {N p(i,i )}p∈N of the sheaf of groups G(i,i )
is central.
(3) Let {N p}p∈N be a normal ﬁltration of G. We say that G is complete with
respect to this ﬁltration if for every local object i of G, the sheaf G(i,i ) is
complete with respect to the ﬁltration {N p(i,i )}p∈N.
(4) If G is complete with respect to some central ﬁltration, then we c all it a
pronilpotent gerbe.
Proposition 6.6. Suppose {N p}p∈N is a central ﬁltration of the gerbe G. Then
for every p there is a central extension of gerbes
(6.7) 1 → N p/ N p+1 → G/ N p+1
F
− →G/ N p → 1.
Proof. Use Theorem 3.13. □
Observe that N p/ N p+1 is a central subgroupoid of the gerbe G/ N p+1; so
N p/ N p+1 can be regarded as a sheaf of abelian groups on X. See Proposition
3.19.
Deﬁnition 6.8. Let G be a gerbe on X, with central ﬁltration {N p}p∈N. An open
setU ⊂X is called acyclic with respect to {N p}p∈N if the following two condition
hold:
(i) The groupoid G(U ) is nonempty.
(ii) For every i ∈ Ob G(U ), the set U is acyclic with respect to the central
ﬁltration {N p(i,i )}p∈N of the sheaf of groups G(i,i ).
Deﬁnition 6.9. Let G be a gerbe on X, with central ﬁltration {N p}p∈N.
(1) A collection U = {Uk}k∈K of open sets of X is called acyclic with respect
to {N p}p∈N if every ﬁnite intersection Uk0,...,k m is acyclic with respect to
{N p}p∈N.
(2) We say that there are enough acyclic coverings with respect to {N p}p∈N if
every open covering U of an open set U admits a reﬁnement U′ which is
acyclic with respect to {N p}p∈N.
CENTRAL EXTENSIONS OF GERBES 31
Suppose G is a gerbe, complete with respect to a central ﬁltration {N p}p∈N. Let
U be an open set of X which is acyclic with respect to {N p}p∈N, and let i be an
object of the groupoid G(U ). By Lemma 6.3 the group G(U )(i,i ) is complete with
respect to the ﬁltration {N p(U )(i,i )}p∈N; so G(U )(i,i ) is a complete metric space.
Now let j be another object of G(U ), and suppose G(U )(i,j ) ⁄= ∅. Then the set
G(U )(i,j ) is a G(U )(j,j )-G(U )(i,i )-bitorsor. One can introduce a metric topology
on this set, by letting
g ◦ N p(U )(i,i ) = N p(U )(j,j ) ◦g
be the ball of radius 2−p aroundg ∈ G(U )(i,j ). For any such g the functionh ↦→g·h
is an isomorphism of metric spaces G(U )(i,i )
≃
− →G(U )(i,j ); and hence G(U )(i,j )
is complete.
Theorem 6.10. Let G be a gerbe on the topological space X, and let {N p}p∈N be
a central ﬁltration on it. Assume that G is complete with respect to {N p}p∈N, and
that there are enough acyclic coverings with respect to {N p}p∈N. Let U be some
open set of X.
(1) If H1(U, N p/ N p+1) = 1 for every p ≥ 0, then the groupoid G(U ) is con-
nected.
(2) If H2(U, N p/ N p+1) = 1 for every p ≥ 0, then the groupoid G(U ) is
nonempty.
Proof. (1) This is very similar to Theorem 4.6. Given i,j ∈ Ob G(U ), we must
show that G(U )(i,j ) ⁄= ∅.
Since G is locally connected, we can ﬁnd an open covering U = {Uk}k∈K of
U such that G(Uk)(i,j ) ⁄= ∅ for any k ∈ K. By reﬁning U , we can assume that
it is acyclic with respect to {N p}p∈N. For each k ∈ K let us choose an element
gk;0 ∈ G(Uk)(i,j ). We are going to construct new elements gk;p ∈ G(Uk)(i,j ), for
all k ∈K and p ∈ N, satisfying these conditions:
(a) gk;p+1 ∈gk;p ◦ N p(Uk)(i,i ).
(b) g−1
k1;p ◦gk0;p ∈ N p(Uk0,k 1)(i,i ) for any k0,k 1 ∈K.
The construction is by recursion on p.
Forp = 0 the elements gk;0 are already given. So let p ≥ 0, and assume that
we have elements gk;p′ for p′ ≤ p, satisfying conditions (a)-(b). Let us denote by
¯gk;p ∈ (G/ N p+1)(Uk)(i,j ) the image of gk;p, and deﬁne
¯gk0,k 1;p := ¯g−1
k1;p ◦ ¯gk0;p ∈ (G/ N p+1)(Uk0,k 1 )(i,i )
fork0,k 1 ∈K. Consider the central extension of gerbes (6.7). By conditi on (b) we
haveF (¯gk0,k 1;p) = 1; so
¯gk0,k 1;p ∈ (N p/ N p+1)(Uk0,k 1 )(i,i ).
We get a Čech 1-cocycle c := {¯gk0,k 1;p}k0,k 1∈K with values in the sheaf N p/ N p+1.
According to the assumptions and Proposition 5.5(1), we hav e
ˇH1(U, N p/ N p+1) ∼= H1(U, N p/ N p+1) = 1.
Hence there is a 0-cochain b = { ¯fk}k∈K such that c = d(b), where d is the Čech
coboundary. By condition (ii) of Deﬁnition 6.2 the homomorp hism
N p(Uk)(i,i ) → (N p/ N p+1)(Uk)(i,i )
32 AMNON YEKUTIELI
is surjective, so we can lift ¯fk to an element fk ∈ N p(Uk)(i). Let us deﬁne
gk;p+1 :=gk;p ·f−1
k .
Then conditions (a)-(b) are satisﬁed.
We know that the set G(Uk)(i,j ) is a complete metric space. Condition (a) says
that {gk;p}p∈N is a Cauchy sequence. Let
gk := lim
p→∞
gk;p ∈ G(Uk)(i,j ).
Condition (b) now says that {gk}k∈K is a 1-cocycle. By descent for morphisms
there is an element g ∈ G(U )(i,j ) such that g|Uk =gk.
(2) This is like Theorem 4.17. Since G is locally nonempty, there is an open covering
U = {Uk}k∈K of U such that all the groupoids G(Uk) are nonempty. By reﬁning
U we may assume it is acyclic with respect to {N p}p∈N. Let’s choose some ik ∈
Ob G(Uk). For any k0,k 1 ∈K, and any p ∈ N, we have H 1(Uk0,k 1, N p/ N p+1) = 1.
According to part (1) of the theorem, applied to the open set Uk0,k 1 , the groupoid
G(Uk0,k 1 ) is connected. Let us choose some element gk0,k 1;0 ∈ G(Uk0,k 1)(ik0,i k1 ).
Using recursion on p we shall construct elements gk0,k 1;p ∈ G(Uk0,k 1 )(ik0,i k1)
satisfying these conditions:
(a) gk0,k 1;p+1 ∈gk0,k 1;p ◦ N p(Uk0,k 1)(ik0,i k0).
(b) g−1
k0,k 2;p ◦gk1,k 2;p ◦gk0,k 1;p ∈ N p(Uk0,k 1,k 2 )(ik0,i k0) for any k0,k 1,k 2 ∈K.
Forp = 0 the elements gk0,k 1;0 are already given. So let p ≥ 0, and assume that
we have elements gk0,k 1;p′ for p′ ≤ p, satisfying conditions (a)-(b). Let us denote
by
¯gk0,k 1;p ∈ (G/ N p+1)(Uk0,k 1 )(ik0,i k1)
the image of gk0,k 1;p, and deﬁne
¯gk0,k 1,k 2;p := ¯g−1
k0,k 2;p ◦ ¯gk1,k 2;p ◦ ¯gk0,k 1;p ∈ (G/ N p+1)(Uk0,k 1,k 2 )(ik0,i k0).
Consider the central extension of gerbes (6.7). By conditio n (b) we have
F (¯gk0,k 1,k 2;p) = 1; so
¯gk0,k 1,k 2;p ∈ (N p/ N p+1)(Uk0,k 1,k 2)(ik0,i k0 ).
Lemma 4.11 says that c := {¯gk0,k 1,k 2;p} is a Čech 2-cocycle.
According to the assumptions and Proposition 5.5(1), we hav e
ˇH2(U, N p/ N p+1) ∼= H2(U, N p/ N p+1) = 1.
Hence there is a 1-cochain b = { ¯fk0,k 1} such that c = d(b). As before, we can lift
¯fk0,k 1 to an element fk0,k 1 ∈ N p(Uk0,k 1)(ik0,i k0). Let us deﬁne
gk0,k 1;p+1 :=gk0,k 1;p ◦f−1
k0,k 1.
Then conditions (a)-(b) are satisﬁed.
As in the proof of part (1), let
gk0,k 1 := lim
p→∞
gk0,k 1;p ∈ G(Uk0,k 1 )(ik0,i k1).
Condition (b) says that {gk0.k 1}k0,k 1∈K is a 2-cocycle. By descent for objects there
is an object i ∈ Ob G(U ). □
CENTRAL EXTENSIONS OF GERBES 33
7. F ake Global Objects of Gerbes
In this section X is some topological space. We will study a gerbe G onX, with
center Z( G), and the central extension of gerbes
(7.1) 1 → Z(G) → G
F
− →G/ Z(G) → 1.
Deﬁnition 7.2. An object i ∈ Ob
(
G/ Z(G)
)
(X) is called a fake global object of G.
When we need to emphasize that i ∈ Ob G(X), as opposed to being in
Ob
(
G/ Z(G)
)
(X), we will say that i is a true global object of G.
Note that some fake global objects i of G will lift to true global objects of G,
whereas other won’t; this is determined by the vanishing of t he obstruction class
cl2
F (i) ∈ ˇH2(
X, Z(G)
)
for the central extension of gerbes (7.1), if this obstructi on class is deﬁned.
Here is an easy example of a fake global object that does not li ft.
Example 7.3. SupposeX is an algebraic variety over a ﬁeld, with H 2(X, OX ) ⁄= 0.
Choose a nonzero cohomology class c ∈ H2(X, OX ). There is an abelian gerbe G
corresponding to c, and it has no global objects. (This construction is standar d; cf.
Example 7.7 below.) Indeed, here the gerbe G/ Z(G) is equivalent to the gerbe I
from Example 2.3, and hence it has one global object (up to iso morphism), say j.
We have a central extension of gerbes
1 → O X → G
F
− →G/ Z(G) → 1,
and the obstruction class to lifting j to an object of G(X) is cl 2
F (j) = c. We see
thatj is a fake global object of G, which does not lift to a true global object of G.
Remark 7.4. The reason we are interested in fake global objects has to do w ith
twisted deformations. Let K be a ﬁeld of characteristic 0, and consider the ring of
formal power series K[[ℏ]] in the variable ℏ. Let ( X, OX ) be a ringed space over
K, as in Examples 5.2-5.4. As explained in [Ye], a twisted (Poi sson or associative)
K[[ℏ]]-deformation A of OX is made up of many locally deﬁned sheaves of (Poisson
or associative) K[[ℏ]]-algebras Ai, that are glued together by isomorphisms Ad( g) :
Ai
≃
− → Aj, called gauge equivalences . The indices i,j,... are local objects of the
gauge gerbe G of A, and the isomorphisms g are local sections of the bitorsors
G(i,j ). The group G(i,i ), for a local object i, is by deﬁnition exp( ℏAi), where
Ai is viewed as a pronilpotent K[[ℏ]]-linear Lie algebra, with Lie bracket being
either its Poisson bracket or the commutator of the associat ive multiplication. The
deformations Ai, for i ∈ Ob G(X), are called global deformations belonging to A.
In case such global deformations do not exist (i.e. the gerbe G is nontrivial), then
we say A is really twisted. Note that the gerbe G is pronilpotent.
Now consider a global deformation A of the following sort: there is an open cov-
ering X = ⋃
k∈KUk, objects ik ∈ Ob G(Uk), and gauge equivalences hk : A|Uk
≃
− →
Aik , such that
hk1 ◦h−1
k0
= Ad(gk0,k 1)
for some gk0,k 1 ∈ G(Uk)(i,i ). So as gauge equivalences Aik0
≃
− → Aik2 we have the
equality
Ad(gk0,k 2 ) = Ad(gk1,k 2) ◦ Ad(gk0,k 1 ).
34 AMNON YEKUTIELI
The local isomorphisms g in the center Z( G(i,i )) are precisely those such that the
gauge equivalences Ad(g) are trivial. Hence, going to the extension of gerbes (7.1),
we have
F (gk0,k 2 ) = F (gk1,k 2 ) ◦F (gk0,k 1 )
in the gerbe G/ Z(G). This implies that the global deformation A corresponds to
an object j ∈ Ob
(
G/ Z(G)
)
(X), i.e. to a fake global object of G. Therefore we call
it a global deformation falsely belonging to A. Observe that the obstruction class
cl2
F (j) ∈ ˇH2(X, Z(G)) is represented by the cocycle
gk0,k 1,k 2 :=g−1
k0,k 2 ◦gk1,k 2 ◦gk0,k 1.
If cl 2
F (j) ⁄= 1 then the deformation A does not truly belong to A.
Next a result.
Proposition 7.5. Let G be a gerbe on X, and assume there are enough Z(G)-
acyclic open coverings. Let ¯G := G/ Z(G).
(1) If ˇH2(X, Z(G)) = 1 , then the canonical morphism of groupoids G(X) →
¯G(X) is essentially surjective on objects. In particular any fak e global object
of G lifts to a true global object.
(2) If moreover ˇH1(X, Z(G)) = 1 , then G(X) → ¯G(X) is bijective on isomor-
phism classes of objects.
Proof. By Theorem 5.11 the obstruction classes cl 1
F (h) and cl 2
F (j) are all deﬁned.
Assertion (1) is a consequence of Theorem 4.17, and assertio n (2) is a consequence
of Theorem 4.6. □
Example 7.6. Let K be a smooth algebraic variety over a ﬁeld K of character-
istic 0. Suppose A is a twisted (Poisson or associative) K[[ℏ]]-deformation of OX
which is symplectic. This means that the ﬁrst order bracket {−, −}A on OX is
nondegenerate (cf. [Ye]). It follows that the center of the g auge gerbe G is iso-
morphic (canonically) to the constant sheaf K[[ℏ]]. Now in the Zariski topology
constant sheaves have no higher cohomologies; and hence Pro position 7.5 applies.
So there are as many global deformations falsely belonging t o A there are global
deformations truly belonging to A in this case.
Example 7.7. Let K be a smooth algebraic variety over a ﬁeld K of characteristic
0, and assume there is a nonzero class c ∈ H2(X, OX ). Then there is a twisted
associative K[[ℏ]]-deformation A of OX , which is commutative (i.e. each of the
local deformations Ai belonging to A is commutative). See [Ye, Example 6.17] for
this construction. The gauge gerbe here is abelian: G ∼= exp(ℏOX [[ℏ]]). We ﬁlter
it by N p := exp(ℏp+1OX [[ℏ]]). For p = 0 we have a central extension of gerbes
1 → O X
ℏ
− →G/ N 1 → G/ N 0 → 1,
and for the unique (up to isomorphism) global object j of the gerbe G/ N 0, the
obstruction class is cl 2(j) = c (same as in Example 7.3). Hence Ob( G/ N 1) = ∅,
implying that Ob G(X) = ∅, so A is really twisted.
One of the reasons for introducing the obstruction classes c l2
F (j) is to address
the following question.
CENTRAL EXTENSIONS OF GERBES 35
Question 7.8. Does there exist an algebraic variety X, and a symplectic twisted
K[[ℏ]]-deformation A of OX , that is really twisted? We expect the answer to be
positive. Indeed, we think this happens when X is any abelian surface, and we take
any nonzero Poisson bracket on OX , and let A be its canonical quantization (as in
[Ye, Theorem 0.1]), which is a twisted associative K[[ℏ]]-deformation of OX .
Example 7.9. LetX be a complex analytic manifold, and denote by OX the sheaf
of holomorphic functions. Let A be a symplectic (Poisson or associative) twisted
C[[ℏ]]-deformation of OX . Then the gauge gerbe G has a central ﬁltration, with
N p(i) = exp( ℏp+1Ai) for a local object i. And the center of G is
exp(ℏC[[ℏ]]) = exp
( ∏ ∞
m=1
Cℏm)
⊂ G.
We put on ¯G := G/ Z(G) the induced ﬁltration { ¯N p}p∈N. Deﬁne a normal sub-
groupoid
Mp := N p+1 · exp
( ∏ p
m=1
Cℏm)
⊂ G.
Then for every p ≥ 0 there is a morphism of central extensions of gerbes
1 /d47/d47OX /d47/d47
/d15/d15
G/ Mp /d47/d47
/d15/d15
¯G/ ¯Mp /d47/d47
=
/d15/d15
1
1 /d47/d47OX/ C /d47/d47¯G/ ¯N p+1
Ep /d47/d47¯G/ ¯N p /d47/d471.
We do not know if there are enough acyclic open coverings for t he sheaf OX/ C;
but according to Proposition 5.13, for any j ∈ Ob( ¯G/ ¯N p)(X) the obstruction class
cl2
En (j) ∈ ˇH2(X, OX/ C) exists, and moreover it comes from ˇH2(X, OX ).
Now assume that the homomorphism
(7.10) H 2(X, C) → H2(X, OX )
is surjective. This happens when X is the analytiﬁcation of a projective algebraic
variety (cf. [NT, Section 5]). Then cl 2
En(j) = 1 for all p. Presumably Theorem 6.10
can be reﬁned to work with vanishing of obstruction classes ( rather than vanishing
of the whole cohomology groups). This would imply that fake g lobal deformations
exist here.
Example 7.11. Suppose X is a smooth projective algebraic variety over C (with
the Zariski topology), and let Xan be the corresponding complex analytic manifold.
Let A be a symplectic (Poisson or associative) twisted C[[ℏ]]-deformation of OX .
There is an induced deformation Aan of OXan . As in Example 7.6, there are as many
global deformations truly belonging to A as there are global deformations falsely
belonging to it. By the GAGA principle we have H p(X, OX ) = H p(Xan, OXan ) for
all p, and therefore there as many global deformations truly belo nging to A as
there are global deformations truly belonging to Aan. In particular, there might be
none (see Question 7.8). On the other hand, by Hodge Theory th e homomorphism
(7.10) is surjective here (cf. [BK, Section 1.2]), and there fore (under the caveat of
reﬁning Theorem 6.10) there is always some global deformati on falsely belonging
to Aan.
36 AMNON YEKUTIELI
