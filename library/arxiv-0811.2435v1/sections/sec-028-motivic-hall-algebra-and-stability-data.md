---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-028-motivic-hall-algebra-and-stability-data
section_title: "Motivic Hall algebra and stability data"
section_number: null
pages: 84-92
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
In this section the ﬁeld k can have arbitrary characteristic.
LetC be an ind-constructible triangulated A∞-category over a ﬁeld k. We
are going to describe a motivic generalization of the derive d Hall algebras
from [70].
As usual, we have a constructible countable decomposition Ob(C) =
⊔i∈IYi with group GL(Ni) acting on Yi. Let us consider a Mot(Spec(k))-
module⊕iMotst(Yi,GL (Ni)) (see section 4.2) and extend it by adding neg-
ative powers Ln,n < 0 of the motive of the aﬃne line L. We denote the
resulting Mot(Spec(k))-module by H(C). We understand elements of H(C)
as measures (and not as functions), because in the deﬁnition of the produ ct
we will use the pushforward maps.
We would like to makeH(C) into an associative algebra, called the motivic
Hall algebra . We need some preparations for that. First we observe that
if [πi : Zi → Ob(C)],i = 1, 2 are two elements 19 of H(C) then one has a
18In fact we would like to say that G is “ind-constructible” in some sense. A suﬃcient,
but not necessary condition would be the existence of an ind- constructible functor G′ from
C×C op to P erf(P1
k) such that G is isomorphic to the composition of G′ and the restriction
functor P erf(P1
k)→ P erf(A1
k).
19Here we consider for simplicity the case when the groups acti ng on Z1, Z 2 are trivial,
the generalization to the case of non-trivial groups is stra ightforward.
84
constructible set tot((π1×π2)∗(EXT 1)) which is the total space of the pull-
back of the ind-constructible bundle EXT 1 over Ob(C)×Ob(C). Then the
mapCone (see Section 3.1) after the shift [1] maps the total space to Ob(C).
For any N∈ Z we introduce the “truncated” Euler characteristic
(E,F )≤N :=
∑
i≤N
(−1)i dim Exti(E,F ) .
In the future we will use the notation ( E,F )i for dim Ext i(E,F ), hence
(E,F )≤N =∑
i≤N (−1)i(E,F )i.
With the pair [πi :Yi→Xi],i = 1, 2 as above we can associate a collection
of constructible sets
Wn =
{
(y1,y 2,α )|yi∈Yi,α∈ Ext1(π2(y2),π 1(y1)), (π2(y2),π 1(y1))≤0 =n
}
,
where n∈ Z is arbitrary. Clearly
[tot((π1×π2)∗(EXT 1))→Ob(C)] =
∑
n∈Z
[Wn→Ob(C)] .
We deﬁne the product
[Y1→Ob(C)]· [Y2→Ob(C)] =
∑
n∈Z
[Wn→Ob(C)]L−n ,
where the map Wn→Ob(C) is given by the formula
(y1,y 2,α )↦→Cone(α :π2(y2)[−1]→π1(y1)) .
Proposition 10 The above formula makes H(C) into an associative algebra.
Proof. We are going to prove the result for the “delta functions”
νE = [pt→Ob(C)],pt↦→E ,
where E is an object of C(
k). The case of equivariant families is similar. In
other words, we would like to prove that
(νE1·νE2)·νE3 =νE1· (νE2·νE3) .
Replacing the category by its minimal model we may replace in all consid-
erations Hom• by Ext•. Let us also remark that an element α∈ Ext1(E,F )
85
deﬁnes an extension Eα which we can interpret as a deformation of the ob-
ject E⊕F (the trivial extension). Therefore for any object G the group
Ext•(G,Eα) is equal to the cohomology of the complex (Ext •(G,E⊕F ),dα),
where dα is the operator of multiplication (up to a sign) by α.
Notice that
νE1·νE2 = L−(E2,E1)≤0[Ext1(E2,E 1)→Ob(C)] := L−(E2,E1)≤0
∫
α∈Ext1(E2,E1)
νEα ,
where Eα is the object corresponding to the extension α, i.e.
Eα =Cone(α :E2[−1]→E1) .
It follows that
(νE1·νE2)·νE3 = L−(E2,E1)≤0
∫
α∈Ext1(E2,E1),β∈Ext1(E3,Eα )
L−(E3,Eα )≤0νEβ .
We observe that
(E3,Eα)≤0 = (E3,E 2⊕E1)≤0−lα = (E3,E 2)≤0 + (E3,E 1)≤0−lα ,
where the “error term” lα /greaterorequalslant0 can be computed in terms of the linear map
dα. Therefore one can write
(νE1·νE2)·νE3 = L−(E2,E1)≤0−(E3,E1)≤0−(E3,E2)≤0
∫
α∈Ext1(E2,E1),β∈Ext1(E3,Eα )
LlανEβ .
One can write a similar expression for νE1· (νE2·νE3). In this case the
“error term” will be denoted by rα instead of lα.
Notice that the diﬀerential
dα : Ext 0(E3,E 2)⊕ Ext0(E3,E 1)→ Ext1(E3,E 1)⊕ Ext1(E3,E 2)
satisﬁes the property that the only non-trivial component i s the map αR :
Ext0(E3,E 2)→ Ext1(E3,E 1). Here we denote by αR the linear operator of
multiplication by α∈ Ext1(E2,E 1) from the right. We will use the same
convention for the linear operator αR : Ext 1(E3,E 2)→ Ext2(E3,E 1). Hence
we see that
dim Ext1(E3,Eα) = dim Ker
(
αR : Ext 1(E3,E 2)→ Ext2(E3,E 1)
)
+
86
+ dim Coker
(
αR : Ext 0(E3,E 2)→ Ext1(E3,E 1)
)
.
Let us now consider the constructible set
X1,2,3 ={(α,γ,δ )∈ Ext1(E2,E 1)⊕ Ext1(E3,E 2)⊕ Ext1(E3,E 1)|α◦γ = 0}.
Notice that a triple (α,γ,δ )∈X1,2,3 deﬁnes the deformation of the object
E1⊕E2⊕E3 preserving the ﬁltration
E1⊂E1⊕E2⊂E1⊕E2⊕E3 .
More precisely, the triple gives rise to a twisted complex, w hich is deﬁned
by the corresponding to ( α,γ,δ ) solution to the Maurer-Cartan equation
(strictly upper-triangular matrix acting on E1⊕E2⊕E3). The latter obser-
vation means that there is an ind-constructible map X1,2,3→ Ob(C) which
assigns to a point ( α,γ,δ ) the corresponding twisted complex.
Let us now ﬁx α∈ Ext1(E2,E 1) and consider the ind-constructible subset
Xα
1,2,3⊂ X1,2,3 which consists of the triples with ﬁxed α. There is a natu-
ral projection ( α,γ,δ )↦→(γ,δ ), which gives rise to the constructible map
Xα
1,2,3→ Ext1(E3,Eα). This is a constructible aﬃne bundle with the ﬁbers
isomorphic to Im( αR : Ext 0(E3,E 2) → Ext1(E3,E 1)). Also, one can see
directly that the dimension of the latter space is
lα = (E3,E 2⊕E1)≤0− (E3,Eα)≤0 .
Hence we have the following identity in H(C):
∫
α∈Ext1(E2,E1),β∈Ext1(E3,Eα )
Llα νEβ = [X1,2,3→Ob(C)] .
Therefore,
(νE1·νE2)·νE3 = L−(E2,E1)≤0−(E3,E1)≤0−(E3,E2)≤0· [X1,2,3→Ob(C)] .
Similar considerations show that
νE1· (νE2·νE3) = L−(E2,E1)≤0−(E3,E1)≤0−(E3,E2)≤0· [X1,2,3→Ob(C)] .
This proves the associativity of the product in H(C). ■
For a constructible stability structure onC with an ind-constructible class
map cl : K0(C)→ Γ, a central charge Z : Γ → C, a strict sector V ⊂ R2
87
and a branch Log of the logarithm function on V we have the category
CV :=CV,Log deﬁned in Section 3.4. Hence we have the completion
ˆH(CV ) :=
∏
γ∈(Γ∩C(V,Z,Q))∪{0}
H(CV∩ cl−1(γ)) .
Then we have an invertible element AHall
V ∈ ˆH(CV ) such that
AHall
V := 1 +··· =
∑
i∈I
1(Ob(CV )∩Yi,GL(Ni)) ,
where 1S is the identity function (see 4.2) but interpreted as a count ing
measure20. In short, element AHall
V is given by the counting measure restricted
toCV . The summand 1 comes from zero object.
Proposition 11 Elements AHall
V satisfy the Factorization Property:
AHall
V =AHall
V1 ·AHall
V2
for a strict sector V =V1⊔V2 (decomposition in the clockwise order).
Proof. The proof follows from the following observations:
1) For anyEi∈Ob(CVi(
k)),i = 1, 2 one has (E2,E 1)≤0 = dim Ext0(E2,E 1)
because Exti(E2,E 1) = 0 for i< 0.
2) The set {[E] ∈ Iso(CV (k))} is in one-to-one correspondence with
the set of isomorphisms classes of the triples ( E1,E 2,α ) such that Ei ∈
Ob(CVi(k)),i = 1, 2 and α∈ Ext1(E2,E 1) (the map between the sets assigns
to the triple the extension Eα).
3) The automorphism group of the triple ( E1,E 2,α ) is the stabilizer of α
for the natural action of the group Aut( E2)× Aut(E1) on the vector space
Ext1(E2,E 1).
4) There is an exact sequence of groups
1→ Ext0(E2,E 1)→ Aut(Eα)→ Aut(E1,E 2,α )→ 1
In order to apply these observations one uses the fact that an object
E ∈ CV (k) contains a unique subobject E1 ∈ Ob(CV1(k)) such that the
quotient object E2 belongs toCV2(k), and then the factor L−(E2,E1)≤0 cancels
the ratio between the stabilizer of α and the automorphism group of the
extension Eα. ■
20The same is true if one uses the language of higher stacks beca use for any E ∈
Ob(C(V ))(k) one has Ext <0(E, E ) = 0.
88
Corollary 3 Let us endow H(C) with an automorphism η given by the shift
functor [1]. Then the collection (AHall
V ) gives rise to a symmetric stability data
on H(C) considered as a graded Lie algebra (see Deﬁnition 2 and Remar k 8
in Section 2.2). Moreover we obtain a local homeomorphism Stab(C, cl)→
Stab(H(C)).
The above considerations can be illustrated in the case of ﬁn ite ﬁelds.
Namely, let us assume that C is a triangulated category over a ﬁnite ﬁeld
Fq. We deﬁne the Hall algebra H(C) as an associative unital algebra over
Q, which is a Q-vector space spanned by isomorphism classes [ E] of objects
E∈Ob(C). The multiplication is given by the formula
[E]· [F ] = q−(F,E )≤0
∑
α∈Ext1(F,E )
[Eα] ,
where Eα is the extension corresponding to α∈ Ext1(F,E ).
We deﬁne a stability condition onC in the same way as in the Introduction
(or Section 3.4) without imposing any constructibility con dition (since we
do not assume that our category is ind-constructible). Insi de of the set
Stab(C) of stability conditions on C we consider a subset Stab0(C) consisting
of such stability conditions that the set {E ∈ Css
γ| Arg(E) = ϕ} is ﬁnite
for any γ ∈ Γ,ϕ ∈ [0, 2π). This property is analogous to the one in the
ind-constructible setting which says that Css
γ is a constructible set. Then
for any strict sector V and a choice of the branch Log we have an element
AHall
V ∈ ˆH(CV ) given by
AHall
V = 1 +··· =
∑
[E]∈Iso(CV )
[E]
# Aut(E) .
Similarly to the motivic case the collection of elements ( AHall
V ) satisﬁes the
Factorization property. Hence it deﬁnes a stability data on the space H(C)
considered as a graded Lie algebra.
The relationship of our version of Hall algebra to the To¨ en d erived Hall
algebra from [70] is described in the following proposition .
Proposition 12 There is a homomorphism of rings H(C)→HTo (C), where
HTo (C) is the derived Hall algebra over Fq deﬁned by To¨ en in [70] (see also
[76]), such that
[π :Y→Ob(C)]↦→
∑
y∈Y (Fq)
[π(y)]# Aut(y)(Fq)q(y,y)<0 .
89
Moreover, for any strict sector V the above homomorphism admits a natural
extension to the completed Hall algebras such that the eleme ntAHall
V ∈ ˆH(CV )
is mapped to the element of the completed Hall algebra ˆHTo (CV ) given by∑
[x]∈Iso(CV )[x].
Proof. Straightforward. ■
In fact, in the To¨ en version of the Hall algebra the factoriz ation property
AHall
V =AHall
V1 AHall
V2
is essentially trivial. The reason is that the structure con stants in ˆHTo (CV ) for
the elements of the basis corresponding to objects in a heart of a t-structure
are the usual one, i.e. they count the number of 2-step ﬁltrat ions of a given
object with given isomorphism classes of the associate grad ed factors. The
factorization property means that any object in CV has a unique subobject
inCV1 with quotient in CV2.
Remark 21 One can try to go even further in an attempt to “categorify”
the motivic Hall algebra. Here one has to assume that objects ofC form not
just an ind-constructible stack, but a higher stack of local ly ﬁnite type in the
sense of To¨ en and Vezzosi (see [72]). The corresponding cat egory will be the
monoidal category of motivic sheaves on Ob(C). The motivic Hall algebra
is the K0-ring of this category. In the case of the non-commutative va riety
endowed with polarization one can deﬁne (for any strict sect orV ) the subcat-
egoryFV of “motivic sheaves with central charges in V ”. Nevertheless, the
Factorization Property could fail since the object AHall
V can be non-isomorphic
to the object AHall
V1 ⊗AHall
V2 (but their images in K0 coincide).
Finally, we explain how to rephrase the factorization prope rty in terms
of t-structures, without the use of stability conditions. Here we understand
a t-structure α on a small triangulated category C as a pair of strictly full
subcategories (i.e. a pair of sets of equivalence classes of objects)
C−,α, C+,α⊆C
such that for any E−∈C−,α, E+∈C +,α we have Ext≤0(E−,E +) = 0, and
any object E∈C can be represented (uniquely) as an extension
τ−,α(E)→E→τ+,α(E), τ±,α(E)∈C±,α .
90
Any stability condition onC deﬁnes two t-structuresαl,αr such thatC−,αl
(resp.C−,αr ) consists of extensions of semistable objects E with Arg(E) /greaterorequalslant0
(resp. with Arg( E) > 0). These two t-structures do not change under the
action of the group
{( a11 0
a21 a22
)⏐
⏐ a11,a 22> 0
}
⊂ ~GL+(2, R)
of transformations preserving the upper half-plane. In par ticularly, we see
that while a connected component in the Stab(C) is a real 2 n-dimensional
manifold for n := rank(Γ), the set of corresponding t-structures is at most
(n− 1)-dimensional.
Introduce an order on the set of t-structures by
α1≤α2 ⇐⇒ C−,α1⊆C−,α2 ⇐⇒ C+,α1⊇C +,α2 .
The shift functor acts on t-structures, and α[1]≤α for any t-structure α.
Let nowC be an ind-constructible category endowed with an ind-constructible
homomorphism cl : K0(C(
k))→ Γ and α1,α 2 are two ind-constructible t-
structures. We say
α1≤constr α2
iﬀ
• α1≤α2≤α1[−1] ,
• ∀γ∈ Γ C+,α1∩C−,α2∩cl−1(γ) is constructible,
• the cone generated by {γ∈ Γ|C +,α1∩C−,α2∩cl−1(γ)⁄= 0} is strict.
If α1≤constr α2 then we deﬁne an element Aα1,α2 of an appropriately com-
pleted Hall algebra as the sum of the “counting measure” over the objects
inC+,α1∩C−,α2. Obviously, elements AV (for an open, or a closed, or a
semi-open strict sector V ) are of the form Aα1,α2 for appropriate t-structures
α1,α 2. The factorization property generalizes to
Aα1,α3 =Aα1,α2·Aα2,α3
if α1≤constr α2, α2≤constr α3, α1≤constr α3.
Notice that in the case of stability conditions the element AV is preserved
under the action of a subgroup of ~GL+(2, R) conjugated to the group of
positive diagonal matrices. This action on Stab(C)/Aut(C) has a good chance
to be ergodic, as indicates a similar example with the moduli spaces of curves
with abelian diﬀerentials (see a review [78]).
91
