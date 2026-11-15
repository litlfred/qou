---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-010-51-proof-of-theorem-51
section_title: "Proof of Theorem 5.1"
section_number: 5.1
pages: 20-23
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
toc_source: outline
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect(X), we are"
---
5.1. Proof of Theorem 5.1. The entire section is dedicated to the proof of Theorem 5.1. In
particular we assume the hypothesis and notation in its statement.
It is easy to see that FibX ,C is a stack (not necessarily in groupoids) for the fpqc topology on
Aﬀ/R. To avoid problems with disjoint unions we can assume that X is a Zariski stack.
Given a ﬁnite subset J of C denote by IJ the set of f : J →N extending to a function of I. In
other words a function f : J →N belongs to IJ if and only if there exists a point s: Spec L →X
such that f(E) = rk s∗E for all E ∈J. Given f : J →N we denote by Xf the open locus of X
where rk E = f(E) for all E ∈J and set GLf = Q
E∈J GLf(E). Notice that X = F
f∈IJ Xf and,
since X is quasi-compact, IJ is ﬁnite. The sheaves (E|Xf )E∈J induces a map Xf −→B GLf = Bf
and thus a map
ωJ : X −→
G
f∈IJ
Bf = BJ
For all E ∈J there is a locally free sheaf HE,J on BJ such that (HE,J)|Bf is the canonical locally
free sheaf of rank f(E) pullback from B GLf(E). By construction ω∗
JHE,J ≃E. Set DJ for the
subcategory of Vect(BJ) consisting of all sheaves G such that ω∗
JG ∈C. This is a monoidal
subcategory with duals. Finally when J = {E} we will replace J by E in the subscripts.
The idea now is to prove that DJ generates QCoh(Bj),so that PDJ : BJ −→FibBJ,DJ is an
equivalence of stacks by 3.2. Using this, any time we will have a monoidal functor Γ: C →Vect(A)
in FibX ,C(A), we can compose it via the pullback ω∗
J : DJ →C and deduce that Γ ◦ω∗
J ≃s∗for
some s: Spec A →BJ.
Lemma 5.3. The category DJ generates QCoh(BJ) and, in particular, PBJ : BJ →FibBJ,DJ is
an equivalence.
Proof. By hypothesis DJ contains HE,J and therefore H∨
E,J for E ∈J. Moreover if R is not a
Q-algebra then DJ contains also Symn HE,J and therefore (Symn HE,J)∨for n ∈N and E ∈J.
So everything follows from 1.16 and 3.2.
□
Lemma 5.4. The stack FibX ,C is ﬁbered in groupoids.
Proof. If Γ, Γ′ ∈FibX ,C(A), δ: Γ −→Γ′ is a morphism and E ∈C then δE : ΓE −→Γ′
E is
an isomorphism because Γ ◦ω∗
E
δ◦ω∗
E
−−−→Γ′ ◦ω∗
E is a morphism in the groupoid FibBE,DE(A) ≃
BE(A).
□
Lemma 5.5. Let t be any of the following operations of sheaves t = −∨, Symm, Λm and E ∈C
be such that t(E) ∈C. Then Gt(E) ≃t(GE) on FibX ,C. In particular for any Γ ∈FibX ,C(A) we
get an isomorphism Γt(E) ≃t(ΓE) by testing the previous isomorphism in Γ.
Proof. Consider J = {E} ⊆C. The functor ωE : X −→BE induces ω∗
E : DE −→C and a functor
δ: FibX ,C −→FibBE,DE ≃BE. In other words there is a canonical isomorphism
δ(Γ)∗
|DE ≃Γ ◦ω∗
E : DE →Vect A for Γ ∈FibX ,C(A)
Since t(E) ≃ω∗
Et(HE,{E}) ∈C we have t(HE,{E}) ∈DE. So we have isomorphisms
Gt(E)(Γ) = Γt(E) ≃(Γ ◦ω∗
E)t(HE,{E}) ≃δ(Γ)∗t(HE,{E}) ≃t(δ(Γ)∗HE,{E}) ≃t(ΓE) ≃t(GE)(Γ)
natural in Γ ∈FibX ,C and thus that Gt(E) ≃t(GE).
□
Proposition 5.6. We have Fibf
X ,C̸ = ∅if and only if f ∈I.
Proof. For the if part, if f ∈I there exists s: Spec L −→X such that rk s∗E = f(E) for all
E ∈C. Thus s∗
|C ∈Fibf
X ,C(L). Conversely we must show that, if L is an algebraically closed ﬁeld
and Γ ∈FibX ,C(L), then rk Γ∗: C −→N belongs to I.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
21
Given a ﬁnite subset J ⊆C consider [Γ ◦ω∗
J : DJ →Vect(L)] ∈FibBJ,DJ(L) ≃BJ(L), so
that there exists a map Spec L
s
−→BJ such that Γ ◦ω∗
J ≃s∗
|DJ. The map s has image in some
component Bf with f ∈IJ. In particular if E ∈J we have
rk ΓE = rk Γω∗
JHE,J = rk(s∗(HE,J)|Bf ) = f(E)
This shows that for all ﬁnite subsets J ⊆C we have that fJ = (rk Γ∗)|J belongs to IJ. By
construction XfJ is a non-empty (open and) closed substack of X. Since XfJ ⊆XfJ′ if J′ ⊆J
and X is quasi-compact it follows that T
J XfJ̸ = ∅and thus that rk Γ∗∈I.
□
Lemma 5.7. With notations from 1.2 we have that D(E) = D(GE) and Q(E) = Q(GE). In
particular D(G∗: C →Vect(FibX ,C)) = D(C →Vect(X)).
Proof. We have to show that ranks(E) = ranks(GE).
Since P∗
CGE ≃E we have ranks(E) ⊆
ranks(GE). For the converse, let n ∈ranks(GE) and ξ : Spec L →FibX ,C be a point such that
ξ∗GE has rank n.
Let Γ ∈FibX ,C(L) be the monoidal functor corresponding to ξ, so that
ξ∗GE = ΓE, and set f = rk Γ: C →N, so that f(E) = n. Since Γ ∈Fibf
X ,C̸ = ∅, by 5.6 we have
f ∈I. By deﬁnition of f there exists t: Spec Ω→X such that f(G) = rk t∗G for all G ∈C. In
particular f(E) = n = rk t∗E. By deﬁnition it follows that n ∈ranks(E).
□
We set D(C) = D(G∗: C →Vect(FibX ,C)) = D(C →Vect(X)). Since X is quasi-compact, by
1.10 we have that D(C) = Spec S is aﬃne. By abuse of notation we denote by Q(E) = Q(GE) the
pullback along D(C) →D(E) = D(GE) of the vector bundle denoted by the same symbol. By
the above lemma there is a map FibX ,C →D(C). We deﬁne the (pseudo)-functor Ω: Aﬀ/S →
(categories) by
Ω(A) = {R-linear and strong monoidal functors Γ: C →Vect(A) with ﬁxed ΓE ≃Q(E) ⊗S S}
Lemma 5.8. The functor Ωis an aﬃne scheme and Fr(G∗: C →Vect(FibX ,C)) is the locus in
Ωof functors Γ which are right exact, that is Γ ∈FibX ,C.
Proof. By deﬁnition Fr(G∗: C →Vect(FibX ,C))(A) is the groupoid of ξ ∈FibX ,C(A) together with
isomorphisms ξ∗GE ≃Q(E) ⊗S A. Since objects ξ correspond to R-linear and strong monoidal
functors Γ: C →Vect(A) which are right exact and ξ∗GE ≃ΓE, the second part of the statement
is clear.
For the ﬁrst one, notice that, since the Q(E) are vector bundles on D(C), the sheaves
HomD(C)(Q(E), Q(E′)), IsoD(C)(Q(E) ⊗Q(E′), Q(E ⊗E′)), Iso(OS, Q(OX ))
are all aﬃne schemes for E, E′ ∈C. In particular
Ω= (
Y
E→E′
HomD(C)(Q(E), Q(E′))) × (
Y
E,E′
IsoD(C)(Q(E) ⊗Q(E′), Q(E ⊗E′))) × (Iso(OS, Q(OX )))
where the product is taken over D(C), is a very big aﬃne scheme and Ωis a subfunctor of
Ω= Spec T .
Set Q(E) ⊗S T = Q(E)T . By construction there are maps Q(E)T →Q(E′)T for any map
E →E′ in C, isomorphisms Q(E)T ⊗Q(E′)T →Q(E ⊗E′)T for all E, E′ ∈C and an isomorphism
OΩ→Q(OX )T . We have that Ωis the locus in Ωwhere the association E 7→Q(E)T deﬁnes an
R-linear strong monoidal functor. All these condition can be expressed by the vanishing of a map
of vector bundles, which are closed relations. For example the locus where the association Q(−)T
is symmetric is the locus where the diﬀerence between Q(E)T ⊗Q(E′)T →Q(E⊗E′)T →Q(E′⊗E)
and Q(E)T ⊗Q(E′)T →Q(E′)T ⊗Q(E)T →Q(E′ ⊗E′)T vanishes.
In conclusion Ωis a closed subscheme of Ωand it is therefore aﬃne.
□
We now assume the notation from 5.1, 2). In particular we set G = Q
E GL(Q(E)) →D(C).
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
22
Lemma 5.9. The functor FibX ,C →B G is pseudo-aﬃne and, in particular, Fr(G∗: C →
Vect(FibX ,C)) is pseudo-aﬃne. If moreover the hypothesis of 5.1, 5) are met then the previ-
ous map and space are quasi-aﬃne.
Proof. By 2.5 and 2.6 it is enough to prove that U = Fr(G∗: C →Vect(FibX ,C)) is pseudo-aﬃne.
We are going to use 5.8. Set Ω= Spec B and denote by Γ: C →Vect(B) the tautological R-linear
and strong monoidal functor. Given a ﬁnite test sequence T in C the sequence of maps ΓT is a
complex of free B-modules and denote by ΩT the locus in Ωwhere this complex is exact. By
4.1 the locus ΩT is a quasi-compact open subset of Ω. Moreover U is the intersection of all the
ΩT for all ﬁnite test sequences T . The fact that U is pseudo-aﬃne follows from 4.2. In the
hypothesis of 5.1, 5) only ﬁnitely many test sequences are needed and therefore U is a ﬁnite
intersection of the ΩT , hence it is quasi-aﬃne.
□
Set D = {GE}E∈C ⊆Vect(FibX ,C) and let C′ be the subcategory of Vect B G obtained by taking
tensor products of the sheaves considered in 1.16 with respect to the map C →Vect(D(C)),
E 7→Q(E). By 1.16 the category C′ generates QCoh(B G). Set also ω: FibX ,C →B G.
Lemma 5.10. We have ω∗C′ ⊆D and, in particular, D generates QCoh(FibX ,C).
Proof. The second statement follows from the ﬁrst using 2.4 and the fact that ω is pseudo-
aﬃne. For the ﬁrst, denote by FE the tautological sheaves deﬁned over B G as in 1.16. By
construction ω∗FE ≃GE.
Using 5.5 we have GE∨≃(GE)∨≃g∗(FE)∨and, if Symn E ∈C,
GSymn E ≃Symn GE ≃g∗(Symn FE) over FibX ,C, which concludes the proof.
□
We now deal with the case of Fibf
X ,C for f ∈I. The map Spec R →D(C) deﬁned in 5.1, 4) is
a ﬂat closed immersion thanks to 1.11. Moreover it is easy to check that G ×D(C) R = GLf and
therefore (BD(C) G) ×D(C) R = B GLf. Moreover by construction Fibf
X ,C is the locus of FibX ,C
where all the GE have rank f(E). Hence Fibf
X ,C = FibX ,C ×D(C) R. Taking into account 2.4 we
obtain:
Proposition 5.11. Claims in Theorem 5.1, 4) hold.
It remains to show Theorem 5.1, 5). So we assume its hypothesis. We have already shown that
U = Fr(G∗: C →Vect(FibX ,C)) is quasi-aﬃne in 5.9. For T ⊆C set GT = Q
E∈T GL(Q(E)) →
D(C). In particular G = GC = GJ × GC−J and B G = B GJ × B GC−J. Consider the Cartesian
diagram
U
D(C)
U ′
B GC−J
D(C)
FibX ,C
B G
B GJ
α
Lemma 5.12. The map U →U ′ has a section and, in particular, U ′ is a closed subscheme of
U, hence quasi-aﬃne.
Proof. We need to show that the torsor U ′ →B GC−J is trivial. For this, it is enough to show
that U ′ →B G is trivial. This last map is given by the collection (α∗GE)E∈C and therefore we
must show that all those sheaves are free.
Let S ⊆C be the subset of E such that α∗GE is free. By construction J ⊆S. On the other
hand in 5.5 we have seen that if E ∈C is such that t(E) ∈C then Gt(E) ≃t(GE) for any of
the following operations of sheaves t = −∨, Symm, Λm. In particular α∗Gt(E) ≃t(α∗GE) and
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION
23
therefore E ∈S implies t(E) ∈S. By a direct check it is also clear that GE⊗E′ ≃GE ⊗GE′ for
E, E′ ∈C and, if E ⊕E′ ∈C, that GE⊕E′ ≃GE ⊕GE′. Thus S is closed under tensor product and,
when it makes sense, under direct sum.
Using the ﬁst condition on C we can conclude that S = C. Since U →U ′ is a GC−J-torsor
and therefore aﬃne, the existence of a section tell us that U ′ is a closed subscheme of U and
therefore is quasi-aﬃne.
□
As a consequence of the previous result we have that FibX ,C ≃[U ′/GJ] with U ′ quasi-aﬃne.
We want to show that FibX ,C ≃[V/ GLn] for some quasi-aﬃne scheme V . Since J is ﬁnite, there
is a ﬁnite decomposition of D(C) = ⊔iDi into open and closed subsets such that Q(E)|Ui has
constant rank for E ∈J. In particular we have that (GJ)|Ui is a ﬁnite product of GLm’s. The
following lemma concludes the proof of Theorem 5.1, 5) and therefore of Theorem 5.1 itself.
Lemma 5.13. Let m1, . . . , mh ∈N and n > m1 + · · · + mh. Then there is an injective map
G = GLm1 × · · · × GLmh →GLn
over Z such that B G →B GLn is quasi-aﬃne. In particular for any quasi-aﬃne scheme U with
an action of G one can write
[U/G] ≃[V/ GLn]
for some quasi-aﬃne scheme V with an action of GLn.
Proof. The last claim follows from the ﬁrst because [U/G] →B G →B GLn would be quasi-aﬃne
because composition of quasi-aﬃne maps.
Consider as G →GLn the map sending matrices M1, . . . , Mh to the n × n matrix having
the Mj on the diagonal and 1 in the remaining spots of the diagonal. The corresponding map
B G →B GLn, in terms of vector bundles, is induced by H = (L
i Fi)⊕On−m, where m = P
i mi
and Fi is the rank mi tautological vector bundle given by B G →B Gi. Denote by h: W →B G
the corresponding GLn-torsor.
We have to show that W is quasi-aﬃne and, since W is an
algebraic space, it is enough to show that it is pseudo-aﬃne thanks to 2.8.
It is enough to
show that the sheaves over B G coming from B GLn, whose category we denote by Dn, generates
QCoh(B G): h∗Dn are made of free sheaves and, since h is aﬃne, it generates QCoh(W) thanks
to 2.4,.
We have H = Fi ⊕Qi. In particular there is a surjective map H →Fi. Moreover, since
Symq(H) = (Symq FE) ⊕Ki, there is also a surjective map Dn ∋(Symm H)∨→(Symm Fi)∨. It
follows that the sheaves Fi, (Symq Fi)∨for q ∈N are generated by Dn, which therefore generates
QCoh(B G) thanks to 1.16.
□
