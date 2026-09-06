---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-009-33-some-features-of-transport-2-functors
section_title: "Some Features of Transport 2-Functors"
section_number: 3.3
pages: 18-22
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
In this section we provide several features of transport 2-func tors.
3.3.1 Operations on T ransport 2-F unctors
It is straightforward to see that transport 2-functors allow a list of natural operations.
(i) Pullbacks: Let f :M /d47/d47 N be a smooth map. The pullback f ∗tra of any transport 2-functor
on N is a transport 2-functor on M .
(ii) Tensor products : Let ⊗ : T ×T /d47/d47 T be a monoidal structure on a 2-category T . For
transport 2-functors tra 1, tra2 : P2(M ) /d47/d47 T with Gr-structure, the pointwise tensor product
tra1 ⊗ tra2 : P2(M ) /d47/d47 T is again a transport 2-functor with Gr-structure, and makes the
2-category Trans2
Gr(M,T ) a monoidal 2-category.
(iii) Change of the target 2-category : Let T and T ′ be two target 2-categories equipped with 2-
functors i : Gr /d47/d47 T and i′ : Gr /d47/d47 T ′, and let F :T /d47/d47 T ′ be a 2-functor together with a
pseudonatural equivalence
ρ :F ◦i /d47/d47 i′.
If tra : P2(M ) /d47/d47 T is a transport 2-functor with Gr-structure, F ◦ tra is also a transport
2-functor with Gr-structure. In particular, this is the case for i′ :=F ◦i and ρ = id.
(iv) Change of the structure 2-groupoid : Let tra : P2(M ) /d47/d47 T be a transport 2-functor with
Gr-structure, for a 2-functor i : Gr /d47/d47 T which is a composition
Gr F /d47/d47 Gr′ i′
/d47/d47T
in which F is a smooth 2-functor. Then, tra is also a transport 2-functor wit h Gr ′-structure,
since for any local i-trivialization (triv,t ) of tra we have a local i′-trivialization (F ◦ triv,t ).
3.3.2 Structure Lie 2-Groups
We describe some examples of Lie 2-groupoids and outline the role of t he corresponding transport
2-functors. First we recall the following generalization of a Lie grou p.
Deﬁnition 3.3.1. A Lie 2-group is a strict monoidal Lie category (G, ⊠, I) together with a smooth
– 18 –
functor inv : G /d47/d47 G such that
X ⊠inv(X) = I =inv(X) ⊠X and f ⊠inv(f ) = id I =inv(f ) ⊠f
for all objects X and all morphisms f in G.
The strict monoidal category ( G, ⊠, I) deﬁnes a strict 2-category BG with a single object [SW,
Example A.2]. The additional functor inv assures that BG is a strict 2- groupoid. All our examples in
Section 4 discuss transport 2-functors with BG-structure, for G a Lie 2-group.
Lie 2-groups can be obtained from the following structure.
Deﬁnition 3.3.2. A smooth crossed module is a quadruple (G,H,t,α ) of Lie groups G and H, of a
Lie group homomorphism t :H /d47/d47 G, and of a smooth left action α :G ×H /d47/d47 H by Lie group
homomorphisms such that
a) t(α(g,h )) = gt(h)g−1 for all g ∈ G and h ∈ H.
b) α(t(h),x ) = hxh−1 for all h,x ∈ H.
The construction of a Lie 2-group G = G(G,H,t,α ) from a given smooth crossed module (G,H,t,α )
can be found in the Appendix of [SW11]. We shall explicitly describe the c orresponding Lie 2-groupoid
BG. It has one object denoted ∗ . A 1-morphism is a group element g ∈ G, the identity 1-morphism
is the neutral element, and the composition of 1-morphisms is the mu ltiplication, g2 ◦g1 :=g2g1. The
2-morphisms are pairs ( g,h ) ∈ G ×H, considered as 2-morphisms
∗
g
/d27/d27
g′
/d67/d67h
/d11/d19
∗
with g′ :=t(h)g. The vertical composition is
∗ g′ /d47/d47
g
/d25/d25
g′′
/d69/d69
h
/d11/d19
h′
/d11/d19
∗ = ∗
g
/d27/d27
g′′
/d67/d67h′h
/d11/d19
∗
with g′ =t(h)g and g′′ =t(h′)g′ =t(h′h)g, and the horizontal composition is
∗
g1
/d27/d27
g′
1
/d67/d67h1
/d11/d19
∗
g2
/d27/d27
g′
2
/d67/d67h2
/d11/d19
∗ = ∗
g2g1
/d29/d29
g′
2g′
1
/d65/d65h2α(g2,h 1)
/d11/d19
∗.
– 19 –
Summarizing, one can go from smooth crossed modules to Lie 2-grou ps, and then to Lie 2-groupoids.
Example 3.3.3.
(i) Let A be an abelian Lie group. A smooth crossed module is deﬁned by G = {1} and H := A.
This ﬁxes the maps to t(a) := 1 and α(1,a ) := a. Notice that axiom b) is satisﬁed because A is
abelian. The associated Lie 2-group is denoted by BA. Transport 2-functors with BBA-structure
play the role of abelian gerbes with connection ; see Section 4.2.
(ii) Let G be a Lie group. A smooth crossed module is deﬁned by H :=G,t = id and α(g,h ) :=ghg −1.
The associated Lie 2-group is denoted by EG. This notation is devoted to the fact that the
geometric realization of the nerve of the category EG yields the universalG-bundleEG. Transport
2-functors with BEG-structure arise as the curvature of transport functors; see Section 3.4.
(iii) Let H be a connected Lie group, so that the group of Lie group automorp hisms of H is again a
Lie group G := Aut(H). The deﬁnitions t(h)(x) := hxh−1 and α(ϕ,h ) := ϕ(h) yield a smooth
crossed module whose associated Lie 2-group is denoted by AUT(H), it is called the automorphism
2-group of H. Transport 2-functors with BAUT(H)-structure play the role non-abelian gerbes
with connection ; see Section 4.3.
(iv) Let
1 /d47/d47N t /d47/d47H
p /d47/d47G /d47/d47 1
be an exact sequence of Lie groups, not necessarily central. Ther e is a canonical action α of H
on N deﬁned by requiring
t(α(h,n )) = ht(n)h−1.
This deﬁnes a smooth crossed module, whose associated Lie 2-grou p we denote by N. Transport
2-functors with BN-structure correspond to (non-abelian) lifting gerbes . They generalize the
abelian lifting gerbes [Bry93, Mur96] for central extensions to arb itrary short exact sequences of
Lie groups.
3.3.3 T ransgression to Loop Spaces
Transport 2-functors on a smooth manifold M induce interesting structure on the loop space LM .
This comes from the fact that there is a canonical smooth functor
ℓ : P1(LM ) /d47/d47 Λ P2(M )
expressing that a point in LM is just a particular path in M , and that a path in LM is just a particular
bigon in M [SW11, Section 4.2]. If tra : P2(M ) /d47/d47 T is a transport 2-functor, then the composition
of ℓ with
Λtra : Λ P2(M ) /d47/d47 Λ traT
yields a functor
Ttra := Λtra ◦ℓ : P1(LM ) /d47/d47 Λ traT
that we call the transgression of tra to the loop space . In order abbreviate the discussion of the functor
Ttra we make three simplifying assumptions:
(i) We restrict our attention to the based loop space Ω M (for some ﬁxed base point) and identify
Ttra with its pullback along the embedding ι : ΩM /d47/d47 LM .
– 20 –
(ii) We assume that there exists a surjective submersion π :Y /d47/d47 M for which tra admits smooth
local trivializations and for which Ω π : ΩY /d47/d47 ΩM is also a surjective submersion.
(iii) We assume that the target 2-category T is strict, so that Λ T is the target category of the functor
Ttra.
Proposition 3.3.4. Let tra : P2(M ) /d47/d47 T be a transport 2-functor with Gr-structure satisfying (ii)
and (iii). Then,
Ttra : P1(ΩM ) /d47/d47 ΛT
is a transport functor with ΛGr -structure.
Proof. Let t :π∗tra /d47/d47 trivi be a π-locali-trivialization of tra for π a surjective submersion satisfying
(ii). A local trivialization ˜t of Ttra is given by
P1(ΩY )
ℓ
/d15/d15
(Ωπ)∗ /d47/d47 P1(ΩM )
ℓ
/d15/d15
Λ P2(Y )
Λtriv
/d15/d15
π∗ /d47/d47 Λ P2(M )
Λt rrrrrrrr
/d116/d124 rrrrrrrr Λtra
/d15/d15
ΛGr Λi
/d47/d47 ΛT
in which the upper subdiagram is commutative on the nose. If g :π∗
1trivi /d47/d47 π∗
2trivi is the pseudona-
tural transformation in the smooth descent object Ex π(tra,t, triv), and ˜g is the natural transformation
in the descent object Ex π(Ttra, ˜t,ℓ ∗Λtriv) associated to the above trivialization, we ﬁnd ˜ g = ℓ∗Λg.
Since F (g) is a transport 2-functor with ΛGr-structure, it has smooth Wilso n lines [SW09]: for a
ﬁxed point α ∈ Y [2] there exists a smooth natural transformation g′ :π∗
1ℓ∗Λtriv /d47/d47 π∗
2ℓ∗Λtriv with
g =i(g′). This shows that ˜g factors through a smooth natural transformation ℓ∗Λg′, so that Ttra is a
transport functor. □
Having in mind that transport functors correspond to ﬁbre bundle s with connection, Proposition
3.3.4 shows that transport 2-functors on a manifold M naturally induce ﬁbre bundles with connection
on the loop space Ω M . In general, these are so-called groupoid bundles [MM03, SW09], who se structure
groupoid is ΛGr. However, in the abelian case, i.e. Gr = BBA for an abelian Lie group A, we have
ΛGr ∼= BA (see Lemma 4.2.3 below), so that the transgression Ttra is – via Theorem 2.4.2 – a principal
A-bundle with connection over Ω M . This ﬁts well into Brylinski’s picture of transgression [Bry93].
3.3.4 Curving and Curvature
Suppose tra : P2(M ) /d47/d47 T is a transport 2-functor with BG-structure, for G some Lie 2-group coming
from a smooth crossed module (G,H,t,α ). Since such 2-functors are supposed to describe (non-abelian)
gerbes with connection, we want to identify a 3-form curvature . Just as for (non-abelian) principal
bundles, this curvature is only locally deﬁned.
First we need the following fact: if g and h denote the Lie algebras of the Lie groups G and H,
respectively, there is a bijection
{ Smooth 2-functors
F : P2(X) → B G
}
∼=
{ Pairs (A,B ) ∈ Ω 1(X, g) × Ω 2(X, h)
satisfying t∗(B) = dA + [A ∧A]
}
, (3.3.1)
– 21 –
where t∗ : h /d47/d47 g is the diﬀerential of t. This bijection is the lowest level of an equivalence of
2-categories that we will review in more detail in Section 4.1; see Theo rem 4.1.1.
Deﬁnition 3.3.5. Let tra : P2(M ) /d47/d47 T be a transport functor with BG-structure over M , let
π : Y /d47/d47 M be a surjective submersion, and let (t, triv) be a π-local trivialization with smooth
descent data.
(i) The diﬀerential forms A ∈ Ω 1(Y, g) and B ∈ Ω 2(Y, h) that correspond to the smooth 2-functor
triv under the above bijection, are called the 1-curving and the 2-curving of tra.
(ii) The 3-form
curv(tra) = dB +α∗(A ∧B) ∈ Ω 3(Y, h),
whereα∗ : g × h /d47/d47 h is the diﬀerential of the action α :G ×H /d47/d47 H of the crossed module,
is called the curvature of tra.
We recall that we called a 2-functor tra : P2(M ) /d47/d47 T ﬂat if it factors through the projection
P2(M ) /d47/d47 Π 2(M ) of thin homotopy classes of bigons to homotopy classes. The next proposition
shows that this notion of ﬂatness is equivalent to the vanishing of th e curvature.
Proposition 3.3.6. Suppose that the 2-functor i : BG /d47/d47 T is injective on 2-morphisms. A trans-
port 2-functor tra : P2(M ) /d47/d47 T with BG-structure is ﬂat if and only if its local curvature 3-form
curv(tra) ∈ Ω 3(Y, h) with respect to any smooth local trivialization vanishes.
Proof. We proceed in two parts. (a): curv(tra) vanishes if and on ly if triv is a ﬂat 2-functor, and
(b): tra is ﬂat if and only if triv is ﬂat. The claim (a) follows from Lemma A .11 in [SW11]. To see
(b) consider two bigons Σ 1 : γ /d43/d51 γ′ and Σ 2 :γ /d43/d51 γ′ in Y which are smoothly homotopic so that
they deﬁne the same element in Π 2(Y ). Suppose tra is ﬂat and let Σ := Σ −1
2 • Σ 1. Axiom (T2) for the
trivialization t is then
t(y) ◦π∗tra(γ)
t(γ) /d43/d51
idt(y)◦π∗tra(Σ)
/d11/d19
trivi(γ) ◦t(x)
trivi(Σ) ◦idt(x)
/d11/d19
t(y) ◦π∗tra(γ)
t(γ)
/d43/d51 trivi(γ) ◦t(x)
and since π∗tra(Σ) = id by assumption it follows that triv i(Σ) = id, i.e. triv is ﬂat. Conversely,
assume that triv is ﬂat. The latter diagram shows that tra is then ﬂa t on all bigons in the image of
π∗. This is actually enough: let h : [0, 1]3 /d47/d47 M be a smooth homotopy between two bigons Σ 1 and
Σ 2 which are not in the image of π∗. Like explained in Appendix A.3 of [SW11] the cube [0 , 1]3 can be
decomposed into small cubes such that h restricts to smooth homotopies between small bigons that
bound these cubes. The decomposition can be chosen so small that each of these bigons is contained
in the image of π∗, so that tra assigns the same value to the source and the target b igon of each small
cube. By 2-functorality of tra, this infers tra(Σ 1) = tra(Σ 2). □
