---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-002-2-multiplicities-in-pivotal-categories
section_title: "Multiplicities in pivotal categories"
section_number: 2
pages: 5-8
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
Forn≥ 1 objects X1,...,X n of a monoidal category C, one can consider the
“set of multiplicities” Hom C(1,X 1⊗···⊗ Xn). We show that if C is pivotal, then
this set essentially depends only on the cyclic order of the objects X1,...,X n.
2.1. Permutation maps. For objects X,Y of a pivotal category C, let
σX,Y : Hom C(1,X⊗Y )→ HomC(1,Y ⊗X)
be the map deﬁned as follows: for any α∈ HomC(1,X⊗Y ),
(3) σX,Y (α) = (ev X⊗ idY ⊗X )(idX ∗⊗α⊗ idX )~coevX =
PSfrag replacements
X
α
Y
.
It is easy to check that the maps {σX,Y}X,Y ∈Ob(C) are natural in the sense that
(g⊗f )σX,Y (α) = σX ′,Y ′ ((f⊗g)α)
for any morphisms f :X→X ′,g :Y →Y ′, and α : 1→X⊗Y inC. The following
lemma shows that the maps {σX,Y}X,Y behave as permutations.
Lemma 2.1. For all X,Y,Z ∈ Ob(C),
(a) σX,Y is an isomorphism and σ−1
X,Y =σY,X ;
(b) σX,1 =σ1,X = id HomC (1,X);
(c) σX⊗Y,Z =σY,Z ⊗XσX,Y ⊗Z and σX,Y ⊗Z =σZ⊗X,Y σX⊗Y,Z .
6 V. TURAEV AND A. VIRELIZIER
Proof. Claims (b) and (c) are direct consequences of the monoidality of the duality
functor (Cop,⊗op)→ (C,⊗) deﬁned by X↦→X ∗ and f↦→f ∗. From (b) and (c),
we obtain σY,XσX,Y =σX⊗Y,1 = id HomC(1,X⊗Y ), hence (a). □
It is easy to deduce from Claim (a) of this lemma that
(4) σX,Y (α) = (id Y ⊗X⊗ ~evY )(idY⊗α⊗ idY ∗ )coevY =
PSfrag replacements
X
α
Y
.
2.2. Symmetrized sets of multiplicities. A signed object of a pivotal categoryC
is a pair (X,ε ) where X∈ Ob(C) and ε∈{ +,−}. Given a signed object ( X,ε ), set
X ε =X if ε = + and X ε =X ∗ if ε =−.
A cyclicC- set is a triple (E,c : E→ Ob(C),ε :E→{ +,−}), whereE is a totally
cyclically ordered ﬁnite set. In other words, a cyclic C- set is a totally cyclically
ordered ﬁnite set whose elements are labeled by signed objects of C. For shortness,
we will sometimes write E for (E,c,ε ).
A cyclicC- setE = (E,c,ε ) determines a set H(E) as follows. For e∈E, set
Ze =c(e1)ε(e1)⊗···⊗ c(en)ε(en)∈ Ob(C) and He = Hom C(1,Z e),
wheree =e1<e 2<··· <e n are the elements of E ordered starting from e via the
given cyclic order (here n = #E is the number of elements of E). For e,f ∈E, we
deﬁne a map pe,f :He→Hf as follows. We have f =ek for k∈{ 1,...,n }. Set
X =c(e1)ε(e1)⊗···⊗ c(ek−1)ε(ek−1) and Y =c(ek)ε(ek)⊗···⊗ c(en)ε(en).
Clearly,Ze =X⊗Y andZf =Y⊗X. The map pe,f carries a morphism α : 1→Ze
toσX,Y (α) : 1→Zf . Lemma 2.1 implies that ( He,p e,f )e,f ∈E is a projective system
of sets and bijections. The projective limit H(E) = lim←−He depends only on E. It is
equipped with a system of bijections τ ={τe : H(E)→He}e∈E, called the universal
cone. The bijections τe :H(E)→He are called cone bijections.
An isomorphism of cyclic C- setsφ : E→E′ is a bijection preserving the cyclic
order and commuting with the maps to Ob( C) and {+,−}. Such a φ induces a
bijection H(φ) :H(E)→H(E′) in the obvious way.
2.3. Symmetrized multiplicity modules. LetC be a pivotal k-category. Clearly,
for any cyclic C- setE, the set H(E) is a k-module (called the symmetrized multi-
plicity module ), and the cone bijections and the maps H(φ) as above are k-isomor-
phisms. We now study duality for these modules.
For a tuple S = ((X1,ε 1),..., (Xn,ε n)) of signed objects of C with n≥ 1, set
(5) XS =X ε1
1 ⊗···⊗ X εn
n .
and S∗ = (Xn,−εn),..., (X1,−ε1). The tuple S determines a cyclic C- set ES =
{1, 2,...,n }, where 1 < 2 <··· < n <1 and the label of each e∈ ES is (Xe,ε e).
By deﬁnition, the k-module H(S) = H(ES) is preserved under cyclic permutations
of S and is isomorphic to Hom C(1,X S) through the cone isomorphism τ1.
If S and T are two tuples of signed objects of C, then ST is the tuple obtained
by their concatenation. Clearly, XST = XS⊗XT , (ST )∗ = T ∗S∗, and S∗∗ = S.
The following recursive formulas deﬁne a morphism Ev S : XS∗⊗XS→ 1:
Ev(X,+) = ev X, Ev(X,−) = ~evX, and Ev ST = Ev T (idXT ∗⊗ EvS⊗ idXT )
for any S,T . The morphism Ev S induces a k-bilinear evaluation form
(6) ωS : Hom C(1,X S∗ )⊗ HomC(1,X S)→ EndC(1) = k
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 7
by ωS(α⊗β) = Ev S(α⊗β) for all α∈ HomC(1,X S∗ ) and β∈ HomC(1,X S). For
example:
ω(X,−),(Y,+)(α⊗β) =
PSfrag replacements
X Y
α β
.
As an exercise, the reader may verify that ωS(α⊗β) = ωS∗ (β⊗α) for all α andβ.
Lemma 2.2. IfC is spherical, then ωT S
(
σXT ∗ ,XS∗⊗σXS ,XT
)
=ωST for all tuples
S, T of signed objects of C.
Proof. Letα∈ HomC(1,X (ST )∗ ) = Hom C(1,X T ∗⊗XS∗) and β∈ HomC(1,X ST ) =
HomC(1,X S⊗XT ). By the pivotality of C,
PSfrag replacements EvT = Ev T ∗ =
PSfrag replacements
EvTXT
XT ∗
.
Using these equalities, Formulas (3), (4), and the sphericity of C, we obtain
PSfrag replacements
EvT
EvT ∗
EvS
α β
=
PSfrag replacements
EvT
EvT ∗ EvS
α β =
PSfrag replacements
EvT
EvT ∗ EvS
α β
=
PSfrag replacements
EvT
EvT ∗
EvS
α β
.
Here the left-hand side represents ωT S
(
σXT ∗ ,XS∗ (α)⊗σXS ,XT (β)
)
and the right-
hand side represents ωST (α⊗β). Hence these two expressions are equal. □
By Lemma 2.2, for spherical C, the form (6) is compatible with cyclic permuta-
tions of S and induces a well deﬁned pairing H(S∗)⊗H(S)→ k also denoted ωS.
The dual of a cyclic C- set (E,c,ε ) is the cyclic C- set (Eop,c,−ε), where Eop
is E with opposite cyclic order. Enumerating the elements of E in their cyclic
order, we can identify E with ES for a tuple S of signed objects of C. Then
Eop = ES∗ . If C is spherical, then the pairing ωS : H(S∗)⊗H(S)→ k induces
a pairing ωE : H(Eop)⊗ H(E) → k. More generally, a duality between cyclic
C- setsE and E′ is an isomorphism of cyclic C- setsφ : Eop→E′. Such φ induces
a k-isomorphism H(φ) :H(Eop)→H(E′) and a pairing
(7) ωE◦ (H(φ)−1⊗ id) :H(E′)⊗H(E)→ k.
2.4. Non-degeneracy. Given two k-modulesM andN , one calls a k-bilinear form
ω : M⊗N→ k non-degenerate if there is a k-linear map Ω : k→N⊗M such that
(idN⊗ω)(Ω⊗ idN ) = id N and (ω⊗ idM )(idM⊗ Ω) = id M . If such Ω exists, then
it is unique, and Ω(1) ∈ N⊗M is the inverse of ω. The dual k-homomorphism
Ω ⋆ : M ⋆⊗N ⋆→ k is called the contraction induced by ω. Here M ⋆ = Hom k(M, k).
A pivotal k-categoryC is non-degenerate if for any X∈ Ob(C), the form ωX =
ω(X,+) : Hom C(1,X ∗)⊗ HomC(1,X )→ k (carrying α⊗β to ev X (α⊗β)) is non-
degenerate.
Lemma 2.3. IfC is non-degenerate, then the form (6) is non-degenerate for all S
and the form (7) is non-degenerate for all E,E ′,φ .
Proof. Let{ψX : X→ X ∗∗}X∈Ob(C) be the isomorphisms deﬁned in Remark 1.5.
ForS = ((X1,ε 1),..., (Xn,ε n)), set
ψS =ψ(X1,ε1)⊗···⊗ ψ(Xn,εn) : XS→ (XS∗ )∗,
where ψ(X,+) = ψX and ψ(X,−) = id X ∗ for any X ∈ Ob(C). One veriﬁes that
EvS = ev XS (ψS∗⊗ idXS ) and therefore ωS(α⊗β) = ωXS (ψS∗ (α)⊗β). Since the
formωXS is non-degenerate and ψS∗ is an isomorphism, ωS is non-degenerate. □
8 V. TURAEV AND A. VIRELIZIER
