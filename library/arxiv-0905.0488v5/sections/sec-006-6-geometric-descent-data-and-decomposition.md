---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-006-6-geometric-descent-data-and-decomposition
section_title: "Geometric Descent Data and Decomposition"
section_number: 6
pages: 28-33
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
In this section we study the decomposition of twisted objects on open coverings.
Given a setK and p∈N, we let
(6.1) ∆ p(K) :={(k0,...,kp)|ki∈K}.
The collection{∆ p(K)}p∈N is a simplicial set. Recall that for an open covering
U ={Uk}k∈K of a topological spaceX, and fork = (k0,...,kp)∈∆ p(K), we
write Uk =Uk0∩···∩Ukp.
Let{Gj}j∈J be a collection of crossed groupoids indexed by some setJ. Their
product is the crossed groupoid ∏
j∈JGj, with set of objects Ob(∏
j∈JGj) :=∏
j∈J Ob(Gj) etc.
The notion of stack of crossed groupoids
P = (P1, P2, AdP1↷P2, D)
on a topological spaceX was introduced in Deﬁnition 1.11. We will make frequent
use of the functor of stacksIG : P1→Grp(X), and the natural transformation
ig : IG⇒AdP1, from Proposition 1.13.
Deﬁnition 6.2.Let P be a stack of crossed groupoids on a topological spaceX,
and letU ={Uk}k∈K be an open covering ofX. For anyp∈N deﬁne the crossed
groupoid
Cp(U, P) :=
∏
k∈∆ p(K)
P(Uk).
The restriction morphisms restV/U induce a morphism of crossed groupoids
Cp(U, P)→Cq(U, P) for anyα: p→q in ∆ . In this way we obtain a cosim-
plicial crossed groupoidC(U, P) ={Cp(U, P)}p∈N, which we refer to as theČech
cosimplicial crossed groupoidassociated to P andU.
The set of combinatorial descent dataDesc(G) in a cosimplicial crossed groupoid
G was deﬁned in Deﬁnition 5.2.
Deﬁnition 6.3.Let P be a stack of crossed groupoids on a topological spaceX,
and letU ={Uk}k∈K be an open covering ofX. A geometric descent datumfor
(U, P) is an element of the setDesc(C(U, P)).
Given d,d′∈Desc(C(U, P)), a gauge transformationf : d→d′is a gauge
transformation of combinatorial descent data, in the sense of Deﬁnition 5.3. Passing
to gauge equivalence classes we get the setDesc(C(U, P)).
Here is an explicit interpretation of geometric descent data, gotten by unraveling
the deﬁnitions. A descent datumd∈Desc(C(U, P)) is actually a collection
(6.4) d =
(
{Ak0}k0∈K,{gk0,k1}k0,k1∈K,{ak0,k1,k2}k0,k1,k2∈K
{
,
whereAk0 ∈Ob(P(Uk0)), gk0,k1 :Ak0|Uk0,k1 →Ak1|Uk0,k1 is an isomorphism in
P1(Uk0,k1), andak0,k1,k2∈Γ
(
Uk0,k1,k2, IG(Ak0)
{
. Conditions (i-ii) of Deﬁnition 5.2
say that
(6.5) g−1
k0,k2
◦gk1,k2◦gk0,k1 = ig(ak0,k1,k2)
TWISTED DEFORMATION QUANTIZATION 29
Figure 4. Geometric descent datum on an open covering
{Uk}k∈K of a topological space.
as automorphisms ofAk0|Uk0,k1,k2 in P1(Uk0,k1,k2), and
(6.6) a−1
k0,k1,k3
·ak0,k2,k3·ak0,k1,k2 = IG(g−1
k0,k1
)(ak1,k2,k3)
in the groupΓ
(
Uk0,...,k3, IG(Ak0)
{
. See Figure 4 for an illustration.
Given another descent datumd′=
(
{A′
k0},{g′
k0,k1},{a′
k0,k1,k2}
{
, a gauge trans-
formationf :d→d′is actually a collection
(6.7) f =
(
{fk0},{bk0,k1}
{
,
where fk0 : Ak0 → A′
k0 is an isomorphism in P1(Uk0), and bk0,k1 ∈
Γ(Uk0,k1, IG(Ak0)). Conditions (i-ii) of Deﬁnition 5.3 say that
(6.8) g′
k0,k1 =fk1◦gk0,k1◦ig(bk0,k1)◦f−1
k0
as isomorphismsA′
k0|Uk0,k1→A′
k1|Uk0,k1, and
(6.9) a′
k0,k1,k2 = IG(fk0)
(
b−1
k0,k2
·ak0,k1,k2·IG(g−1
k0,k1
)(bk1,k2)·bk0,k1
{
in the groupIG(A′
k0|Uk0,k1,k2 ).
Remark 6.10. The similarity between our notion of geometric descent data and
the usual notion of descent data for gerbes (cf. [Gi, Section IV.3.5] or [Br, Section
5]) is no coincidence. Indeed, as shown in Example 4.7, gerbes are an instance of
twisted objects. Likewise for gauge transformations between descent data.
In [Ko2], geometric descent data, forP = Assoc(R,X ), is called acombinatorial
description of algebroids. Note that in the paper [BGNT1] the authors refer to a
geometric descent datum as a “stack”.
Deﬁnition6.11.Let G beagerbeon X, andletU ={Uk}k∈K beanopencovering
of X. A trivialization datumof G onU is a collections =
(
{ik0},{sk0,k1}
{
, where
ik0∈Ob(G(Uk0)) and sk0,k1∈G(Uk0,k1)(ik0,ik1).
Consider a twisted object(G, A, cp) of the stack of crossed groupoidsP, and a
trivialization datums =
(
{ik0},{sk0,k1}
{
of the gauge gerbeG on the open covering
30 AMNON YEKUTIELI
U. Deﬁne
(6.12)
Ak0 := A(ik0)∈Ob(P(Uk0)),
gk0,k1 := A(sk0,k1)∈P1(Uk0,k1)(ik0,ik1),
ak0,k1,k2 := cp(s−1
k0,k2
◦sk1,k2◦sk0,k1)∈Γ(Uk0,k1,k2, IG(Ak0)).
The resulting collection of elements, arranged as in (6.4), is denoted bydec(A,s).
Lemma 6.13. Let (G, A, cp) be a twisted object ofP, and lets be a trivialization
datum for G onU.
(1) The collection dec(A,s) is a geometric descent datum for(U, P).
(2) Let (G′, A′, cp′) be another another twisted object ofP, which is twisted
gauge equivalent to (G, A, cp), and lets′be a trivialization datum forG′
onU. Assume that the groupoidsG(Uk) are connected for allk∈K. Then
the descent datadec(A,s) and dec(A′,s′) are gauge equivalent.
Proof. (1) This is a simple calculation.
(2) First assume that (G′, A′, cp′) = ( G, A, cp), but s′=
(
{i′
k0},{s′
k0,k1}
{
is a
diﬀerent descent datum. Since the groupoidsG(Uk) are connected, we can ﬁnd
elementstk∈G(Uk)(ik,i′
k). Deﬁnefk := A(tk), which is an isomorphismAk→A′
k
in P1, and
bk0,k1 := cp(s−1
k0,k1
◦t−1
k1
◦s′
k0,k1◦tk0)∈Γ(Uk0,k1, IG(Ak0)).
A calculation shows that the collectionf, with notation as in (6.7), is a gauge
transformation dec(A,s)→dec(A′,s′).
Now consider a twisted gauge transformation (Φ gau, Φ rep) : ( G, A, cp) →
(G′, A′, cp′). Since Φ gau : G →G′is an equivalence of gerbes, it follows that
the groupoids G′(Uk) are all connected. So, by the previous paragraph, we don’t
care which trivialization datum we use forG′. Let us deﬁnes′to bei′
k := Φ gau(ik)
and s′
k0,k1 := Φ gau(sk0,k1). Take fk := Φ rep :Ak →A′
k and bk0,k1 := 1. The
resulting collectionf is a gauge transformationdec(A,s)→dec(A′,s′). □
Deﬁnition 6.14.Let G be a gerbe on a topological spaceX, and letU ={Uk}k∈K
be an open covering ofX. We say thatU totally trivializes G if for everyp∈{0, 1}
andk∈∆ p(K) the groupoid G(Uk) is nonempty and connected.
Deﬁnition 6.15.Let P be a stack of crossed groupoids on a topological spaceX,
and letU be an open covering ofX.
(1) Let (G, A, cp) be a twisted object ofP. We say thatU totally trivializes
(G, A, cp) if it totally trivializes the gauge gerbeG.
(2) We say thatU totally trivializesP if it totally trivializes all twisted objects
of P.
Remark 6.16. In general there is no reason to expect that totally trivializing
open coverings should exist. If we were to work with hypercoverings, then such a
diﬃculty would not arise; but then the combinatorics would be more complicated.
Cf. [Br, Section 5].
We shall see in Corollary 7.4 that for the stacks with inner gauge groups
AssDef(R,OX) and PoisDef(R,OX) there do exist totally trivializing open cover-
ings.
Proposition 6.17.LetU be an open covering ofX that totally trivializes the stack
of crossed groupoidsP. Then there is a function
dec : TwOb(P)→Desc(C(U, P))
called decomposition, which is represented bydec(A,s) for any representativeA∈
TwOb(P) and any trivialization datums for A onU.
TWISTED DEFORMATION QUANTIZATION 31
Proof. Take any twisted object (G, A, cp). Since the groupoids G(Uk0) are
nonempty, and the groupoidsG(Uk0,k1) are connected, we can ﬁnd a trivialization
datum s. By Lemma 6.13(1) we get a geometric descent datumdec(A,s). Since
the groupoids G(Uk0) are connected, by Lemma 6.13(2) this gives a well-deﬁned
function on equivalence classes. □
Recall that a reﬁnement ofU is an open coveringU′={U′
k}k∈K′ofX, together
with a functionρ:K′→K, such thatU′
k⊂Uρ(k) for everyk∈K′. Sometimes we
say thatρ:U′→U is a reﬁnement. Given such a reﬁnement, there is a function
(6.18) ρ∗: Desc(C(U, P))→Desc(C(U′, P)).
The formula is obvious: sayd =
(
{Ak}k∈K,...
{
; then ρ∗(d) =
(
{A′
k}k∈K′,...
{
,
whereA′
k :=Aρ(k)|U′
k
, etc. It is easy to see that this function preserves the equiv-
alence relation. Thus Desc(C(U, P)) is contravariant with respect to reﬁnements
U′→U.
Proposition 6.19. Let U and U′be open coverings ofX that totally trivialize
the stack of crossed groupoidsP, and letρ: U→U′be a reﬁnement. Then the
diagram
TwOb(P) dec //
dec ))
Desc(C(U, P))
ρ∗

Desc(C(U′, P))
is commutative.
Proof. This is immediate from the construction; cf. proof of Lemma 6.13(2).□
In the rest of this section we will show how to glue twisted objects from descent
data. This construction will be inverse to the decomposition operation. But before
attempting to glue twisted objects, we have to understand how to pass from descent
data to connected groupoids.
Let K be some nonempty set. By groupoid descent datumindexed by K we
mean a collectiond =
(
{Gk0},{φk0,k1},{ak0,k1,k2}
{
, wherek0,k 1,k 2∈K, Gk0 is
a group,φk0,k1 : Gk0→Gk1 is a group isomorphism, andak0,k1,k2∈Gk0. These
satisfy conditions (6.5) and (6.6), with the obvious modiﬁcations in notation (e.g.
φk0,k1 instead ofgk0,k1).
Suppose d and d′are groupoid descent data indexed byK. A gauge transfor-
mation f : d→d′is a collectionf =
(
{ψk0},{bk0,k1}
{
of group isomorphisms
ψk0 :Gk0→G′
k1, and of elementsbk0,k1∈Gk0. The conditions are the translations
of formulas (6.8) and (6.9) to the present context.
A trivialization datum for a connected groupoidG is a collections ={sk0,k1}
of elements sk0,k1 ∈G(k0,k 1), indexed by the set K := Ob(G). We call the
pair (G,s) a trivialized groupoid. By isomorphism of trivialized groupoids F :
(G,s)→(G′,s′) we mean an isomorphism of groupoidsF : G→G′such that
F (sk0,k1) = s′
F(k0),F(k1). Just like in Lemma 6.13(1), to any trivialized groupoid
(G,s) there is a corresponding groupoid descent datumdec(G,s).
Lemma 6.20. Letd be a groupoid descent datum indexed by a nonempty setK.
(1) There is a connected groupoidG, with trivialization datum s, such that
dec(G,s) = d. The trivialized groupoid (G,s) is unique up to a unique
isomorphism. We writeglu(d) :=G.
(2) Letd′be another groupoid descent datum indexed byK, and letf :d→
d′be a gauge transformation. We describef as in (6.7). Then there is
32 AMNON YEKUTIELI
a unique isomorphism of groupoids glu(f) : glu( d)→glu(d′) such that
glu(f)(sk0,k1·bk0,k1) =s′
k0,k1.
Proof. (1) This seems to be known (cf. [Ko2, Appendix A1]), but here is a sketch
anyhow. Write d as in (6.4). For any k0,k 1 ∈K we take G(k0,k 1) to be the
Gk1-Gk0-bitorsor with basissk0,k1, such thatsk0,k1·a = φk0,k1(a)·sk0,k1 for any
a∈Gk0. The composition◦in G is speciﬁed by its value on the basis elements:
sk1,k2◦sk0,k1 :=sk0,k2·ak0,k2,k2.
(2) A direct calculation. □
Lemma 6.21. There is a function
glu : Desc(C(U, P))→TwOb(P)
having these properties:
(i) Ifd,d′∈Desc(C(U, P)) are gauge equivalent, thenglu(d) and glu(d′) are
twisted gauge equivalent.
(ii) For anyd∈Desc(C(U, P)) the twisted object (G, A, cp) := glu(d) has a
trivialization datums such that dec(A,s) =d.
(iii) Let (G, A, cp) be a twisted object ofP, with trivialization datums, and let
d := dec(A,s). Then glu(d) is twisted gauge equivalent to(G, A, cp).
Proof. Take anyd∈Desc(C(U, P)), which we describe as in (6.4). For a nonempty
open setV ⊂X let K(V ) :={k∈K|V ⊂Uk}. Consider the collection
IG(d,V ) :=
(
{Γ(V, IG(Ak0))},{IG(gk0,k1)},{ak0,k1,k2}
{
in which k0,k 1,k 2 ∈K(V ). So IG(d,V ) is a groupoid descent datum indexed
by the set K(V ). If K(V ) ⁄= ∅, then by Lemma 6.20(1) there is a nonempty
connected groupoid G(V ) := glu(IG(d,V )). If If K(V ) = ∅we let G(V ) be the
empty groupoid. ForV = Uk there is a distinguished objectk∈Ob(G(Uk)), and
forV =Uk0,k1 there is a distinguished isomorphismsk0,k1 :k0→k1 in the groupoid
G(Uk0,k1). Also there is a tautological group isomorphism cp : G(V )(k0,k 0)→
Γ(V, IG(Ak0)) for k0∈K(V ).
If V′⊂V then K(V ) ⊂K(V′). By construction of the groupoids glu(−)
there is an induced morphism of groupoidsG(V )→G(V′), which on the automor-
phism groups ofk0∈K(V ) it is the restriction homomorphismΓ(V, IG(Ak0))→
Γ(V′, IG(Ak0)). In this way we obtain a presheaf of groupoidsG on X, which is
a separated prestack (the isomorphism presheaves are sheaves). The group iso-
morphisms cp above induce an isomorphism of sheaves of groupscp : G(k0,k 0)→
IG(Ak0) on Uk0.
Let ˜G be the stackiﬁcation ofG; so ˜G is a gerbe onX, and there is a weak
equivalence of prestacksF : G→˜G. Note that ˜G is equipped with a trivialization
datums =
(
{ik0},{sk0,k1}
{
onU, whereik0 :=F (k0)∈Ob(˜G(Uk0)).
For anyV ⊂X open there is a morphism of groupoidsA(V ) : G(V )→P1(V ),
namely A(V )(k0) := Ak0 for k0∈K(V ) = Ob( G(V )), and A(V )(sk0,k1·a) :=
gk0,k1◦ig(a) for a∈G(V )(k0,k 0) = Γ(V, IG(Ak0)). Note thatig(a) is an automor-
phism ofAk0|V, andgk0,k1 :Ak0|V →Ak1|V is an isomorphism, all in the stack of
groupoids P1. It is a direct calculation to check thatA(V ) respects compositions,
so it is indeed a morphism of groupoids. AsV varies we get a morphism of prestacks
A : G→P1. This induces a morphism of stacks˜A : ˜G→P1.
Take a local objecti of ˜G which is not a local object ofG. This new local object
i is created by gluing a collection of local objects ofG using local isomorphisms in
G. The same gluing operation also determines an isomorphism of sheaves of groups
˜ cp :˜G(i,i )→IG( ˜A (i)). We thus get a twisted objectglu(d) = ( ˜G, ˜A, ˜ cp). By
TWISTED DEFORMATION QUANTIZATION 33
construction we see that the descent datumdec(glu(d),s) equalsd, so property (ii)
holds.
Suppose d′is another normalized descent datum, andf : d→d′is a gauge
transformation, described like in (6.7). Let’s writeglu(d′) = (˜G
′
, ˜A
′
, ˜ cp′). Lemma
6.20(2) implies that for every open setV there’s an induced isomorphism of group-
oids G(V )→G′(V ). Hence we get an equivalence of prestacks of groupoidsΦ gau :
G→G′. Next there is an isomorphismΦ rep : A→A′◦Φ gau of functors of prestacks
G→G′, which for an indexk0∈K is Φ rep :=fk0 :Ak0→A′
k0. The stackiﬁcation
extends these to an equivalence of gerbesΦ gau : ˜G→˜G
′
and an isomorphism of
functors of stacks Φ rep : ˜A→˜A
′
◦Φ gau. We obtain a twisted gauge equivalence
(Φ gau, Φ rep) : glu(d)→glu(d′) between these twisted objects; so property (i) holds.
Finally take any twisted object (G, A, cp) of P and a trivialization datums.
The step-by-step construction ofglu(d) = (˜G, ˜A, ˜ cp)shows that it is twisted gauge
equivalent to(G, A, cp). We see that property (iii) holds. □
Theorem 6.22(Decomposition). LetX be a topological space,U an open covering
of X, and P a stack of crossed groupoids onX. Assume thatU totally trivializes
P. Then the function
dec : TwOb(P)→Desc(C(U, P))
from Proposition6.17 is bijective.
Proof. By property (i) Lemma 6.21 there is a well-deﬁned function
glu : Desc(C(U, P))→TwOb(P).
Properties (ii-iii) of the lemma say thatglu is the inverse ofdec. □
We end this section with a simple example.
Example 6.23. LetA0 ∈Ob(P(X)). Consider the open covering U ={U0},
with U0 := X. Take g0,0 := 1 and a0,0,0 := 1. Then
(
{A0},{g0,0},{a0,0,0}
{
is
a geometric descent datum. From Theorem 6.22 we get a twisted objectA, and
A0 is a global object ofA. We refer toA as the twisted object generated byA0.
Conversely, any twisted objectA which is not really twisted arises in this way (up
to twisted gauge equivalence).
