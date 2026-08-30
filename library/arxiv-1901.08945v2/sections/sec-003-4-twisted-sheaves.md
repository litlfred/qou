---
doc_id: arxiv-1901.08945v2
doc_title: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES"
section_id: sec-003-4-twisted-sheaves
section_title: "Twisted sheaves"
section_number: 4
pages: 16-20
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
doc_brief: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group decomposes accordi ng to the char- acters of"
---
In this section, ∆ will denote a diagonalizable group scheme (over Spe c Z) with
character group A := Hom Spec Z(∆ , Gm). Recall that A is a ﬁnitely generated
abelian group. We will usually use multiplicative notation for A, except when we
identify it with something like the additive group of Z.
LetS be an algebraic stack. By a ∆-gerbe on S we mean a ∆ S-gerbe on S. Fix a
∆-gerbe α :X →S. Note that X is isomorphic to B ∆ S locally on S. In particular,
X is an algebraic stack, and it is reasonable to talk about quasi-cohere nt sheaves
on X.
Remark 4.1. Let α : X → S be a ∆-gerbe. Note that the structure morphism
α is smooth and surjective. Indeed, this is true for any algebraic ger be [ Ber17,
Proposition A.2]. Moreover, assume that Y is a ∆ ′-gerbe over S and let ρ : X →Y
be a morphism over S with induced morphism ϕ : ∆ S → ∆ ′
S on bands. Then
ρ factors as X → X × B ∆ ′ → ϕ∗X ∼= Y by Construction 3.8 combined with
Proposition 3.9. Note that the ﬁrst morphism in the factorization is a ∆ ′-torsor
DECOMPOSITIONS 17
and that the second morphism is a gerbe banded by ∆. In particular, the morphism
ρ is faithfully ﬂat. See also Remark 5.3 for cohomological properties of ρ.
Deﬁnition 4.2. Let F be an object in Mod( Xfppf, OX ), and let χ : ∆ S → Gm,S
be a character. Note that ∆ X acts on F from the right via the inertial action ( 3.1)
and the banding (see Deﬁnition 3.4) of X, and that Gm acts on F from the left via
the inclusion Gm,X ⊂ OX . We deﬁne the χ-homogeneous subsheaf Fχ of F by
(4.1) Fχ = {s ∈ F | s ·γ =χ(γ)s for all γ ∈ ∆ X }.
An object F of Mod(Xfppf, OX ) is called χ-homogeneous or homogeneous of degree
χ provided that F = Fχ , and we denote the full subcategory of χ-homogeneous
objects in Qcoh(Xfppf, OX ) by Qcohχ (Xfppf, OX ).
Remark 4.3. Note that the expression ( 4.1) does not make sense in the lisse–´ etale
topos unless ∆ X is smooth over X. When we talk about homogeneous sheaves
in Qcoh(Xlis-´ et, OX ), we implicitly transport the subcategory Qcoh χ (Xfppf, OX ) ⊂
Qcoh(Xfppf, OX ) to a subcategory Qcoh χ (Xlis-´ et, OX ) ⊂ Qcoh(Xlis-´ et, OX ) under
the equivalence obtained by restriction. We will usually simply write Qco hχ (X) for
any of these subcategories.
Deﬁnition 4.4 (Twisted sheaves). Letα :X →S be a Gm-gerbe and let id : Gm →
Gm be the identity character. An α-twisted quasi-coherent sheaf on S is sim-
ply an object of Qcoh id(X). We will often use the notation Qcoh α (S) instead
of Qcoh id(X).
Remark 4.5. Since the category Qcoh α (S), up to equivalence, obviously depends
only on the class of α in H 2(Sfppf, Gm), we will sometimes abuse notation and write
Qcohα (S) even if α is just a cohomology class in H 2(Sfppf, Gm).
Remark 4.6. Twisted sheaves may also be described using 2-cocycles. This ap-
proach was taken by C˘ ald˘ araru in [C˘ al00, Deﬁnition 1.2.1]. That his deﬁnition
is essentially equivalent to the deﬁnition above was proved by Lieblich in [Lie04,
Proposition 2.1.3.11].
We now give a precise formulation of the well-known fact that any qua si-coherent
sheaf on a suitable gerbe decomposes into its homogeneous subshe aves (c.f. [ Lie04,
Proposition 2.2.1.6]).
Theorem 4.7. Let S be an algebraic stack and let α : X → S be a gerbe banded
by a diagonalizable group ∆ . Then Qcohχ (X) is a Serre subcategory (see [SP19,
Tag 02MO]) of Qcoh(X) for any character χ of ∆ S, and taking the coproduct gives
an equivalence
(4.2)
∏
χ ∈A
Qcohχ (X)
∼
− →Qcoh(X), (Fχ )χ ↦→
⨁
χ ∈A
Fχ,
of abelian categories, where A denotes the character group of ∆ .
Furthermore, assume that Fχ and Gψ are quasi-coherent OX -modules which are
homogeneous for ∆ S-characters χ and ψ, respectively. Then the quasi-coherent
OX -modules
(4.3) Fχ ⊗ Gψ, Hom(Gψ, Fχ )
areχψ- and χψ−1-homogeneous, respectively.
Proof. Throughout the proof, we work with sheaves in Xfppf , which we view as the
topos of sheaves on the site of aﬃne schemes over X. Fix a quasi-coherent sheaf F
of OX -modules.
Letx be an object of X lying over an aﬃne scheme Spec A. Then F (x) is an A-
module with an A-linear right action of the group ∆( A) := ∆(Spec A) coming from
18 DANIEL BERGH AND OLAF M. SCHN ¨URER
the inertial action via the banding. Given a morphism f : y →x in X lying over a
morphism Spec ϕ : Spec B → SpecA, the corresponding morphism F (f ) : F (x) →
F (y) is equivariant with respect to ∆( A) → ∆( B). Moreover, since F is quasi-
coherent, it induces an isomorphism B ⊗ϕ,A F (x)
∼
− → F(y) of B-modules.
By restricting F to SpecA alongx : Spec A →X (see [SP19, Tag 06W9]), we see
that the A-module F (x) can be viewed as a right representation of the diagonaliz-
ableA-group scheme ∆ SpecA in the sense of [ Jan87, I.2.7]. Hence it decomposes as
F (x) = ⨁
χ ∈A F (x)χ by [ Jan87, I.2.11].
If the object x varies, all these decompositions are compatible and combine
into the decomposition F = ⨁
χ ∈A Fχ where Fχ is the χ-homogeneous subsheaf
of F . This shows that the functor ( 4.2) is essentially surjective. Similarly, we
get a decomposition of morphisms between pairs of quasi-coherent modules (cf.
[Jan87, I.2.11]), which shows that ( 4.2) is fully faithful. Moreover, any ∆ S-character
χ clearly gives an exact functor F ↦→ Fχ . In particular, Qcoh χ (X) is a Serre
subcategory of Qcoh(X).
The statement that the tensor product of a χ-homogeneous quasi-coherent mod-
ule with a ψ-homogeneous quasi-coherent module is ( χ +ψ)-homogeneous is ob-
vious, and the corresponding claim for the internal Hom-functor is then a formal
consequence. □
Remark 4.8. Note that the canonical morphism ⨁
χ ∈A Fχ → ∏
χ ∈A Fχ is an iso-
morphism even if the character group A is not ﬁnite. Here the product is taken in
Qcoh(X). This is a simple consequence of the equivalence ( 4.2) in Theorem 4.7.
Proposition 4.9. LetS be an algebraic stack and α :X →S a gerbe banded by a
diagonalizable group ∆ . Let f : T → S be a morphism of algebraic stacks, and let
g :Y →X denote the base change of f along α. Then the functors
g∗ : Qcoh(X) → Qcoh(Y ), g ∗ : Qcoh(Y ) → Qcoh(X)
respect the decompositions of Qcoh(X) and Qcoh(Y ) into homogeneous objects given
in Theorem 4.7.
Proof. As a formal consequence of adjunction, it is enough to verify that one of
the functors g∗ and g∗ preserves the decomposition. The functor g∗ is obtained by
restriction of the functor g∗ : Mod(Sfppf, OS) → Mod(Tfppf, OT ), which in turn is
just given by restriction of the topos Sfppf . In this setting the statement is obvious
from the deﬁnition of a homogeneous sheaf (see Deﬁnition 4.2). □
Proposition 4.10. LetX andX ′ be gerbes over S banded by diagonalizable groups
∆ and ∆ ′, respectively, and let ρ : X → X ′ be a morphism over S with induced
morphism ϕ : ∆ S → ∆ ′
S on the bands. Fix a character χ′ : ∆ ′
S → Gm,S , and let
χ = χ′ ◦ϕ. Then the pull-back functor ρ∗ takes χ′-homogeneous objects to χ-
homogeneous objects and induces an equivalence
(4.4) ρ∗ : Qcohχ ′ (X ′)
∼
− →Qcohχ (X)
of categories. In particular, if X ′ =S thenρ∗ : Qcoh(S) → Qcoh(X) is fully faithful
with essential image consisting of those objects that are ho mogeneous for the trivial
character.
Proof. By a similar argument as in the proof of Proposition 4.9, we see that ρ∗
takes χ′-homogeneous objects to χ-homogeneous objects. First we note that the
special case in the last sentence in the statement of the propositio n follows directly
from Proposition 3.2.
In the general case, we consider the ﬁber product X ×SX ′ and its projections p
andq toX andX ′. Note that X ×SX ′ is a ∆ × ∆ ′-gerbe over S and that p andq
induce the projections to ∆ respectively ∆ ′ on the bands.
DECOMPOSITIONS 19
The projection p is a gerbe banded by the kernel of the projection ∆ × ∆ ′ →
∆, which is isomorphic to ∆ ′. In particular, p∗ is fully faithful with essential
image consisting of sheaves on which this kernel acts trivially. Similar s tatements
hold for q. Hence it follows from the decomposition in Theorem 4.7 that we get
equivalences
p∗ : Qcohχ (X) ⇄ Qcoh(χ,e ′)(X ×SX ′/S) :p∗,(4.5)
q∗ : Qcohχ ′ (X ′) ⇄ Qcoh(e,χ ′)(X ×SX ′/S) :q∗,(4.6)
where e and e′ denote the trivial characters of ∆ and ∆ ′, respectively.
Note that the gerbe p has a trivialization τ = (id,ρ ). In particular, there exists
a line bundle L on X ×SX ′ such that
(a) L is χ′-homogeneous with respect to the decomposition induced by p;
(b) τ ∗L ∼= OX .
Since L is a line bundle, it must also be homogeneous for some character ( ψ,ψ ′)
of (∆ × ∆ ′)S with respect to the gerbe X ×S X ′ → S. By (a), we have ψ′ =
χ′. Furthermore, since τ induces the morphism (id ,ϕ ) on bands, we have τ ∗L ∈
Qcohψχ (X). This forces ψ = χ−1 by (b), so L ∈ Qcoh(χ −1,χ ′)(X ×S X ′/S). In
particular, it follows from the equivalences ( 4.5) and ( 4.6) and the statement about
the monoidal structure in Theorem 4.7 that we get an equivalence
p∗(L∨ ⊗q∗(−)) : Qcohχ ′ (X ′)
∼
− →Qcohχ (X).
Furthermore, the restriction of the natural transformation
p∗(L∨ ⊗q∗(−)) ∼=τ ∗p∗p∗(L∨ ⊗q∗(−)) →
τ ∗(L∨ ⊗q∗(−)) ∼=τ ∗(L∨) ⊗τ ∗q∗(−) ∼=ρ∗
to Qcohχ ′ (X ′) is an isomorphism, which concludes the proof. □
Now the following corollaries are easy consequences of Theorem 4.7, Proposi-
tion 4.9 and Proposition 4.10.
Corollary 4.11. LetS be an algebraic stacks and let α :X →S be a gerbe banded
by ∆ , and choose a character χ : ∆ S → Gm,S . Then we have an equivalence
(4.7) Qcoh χ ∗α (S) ∼= Qcohχ (X)
of categories, where χ∗α is deﬁned as in Construction 3.8. In the particular case
when ∆ = Gm, this gives the equivalence
(4.8) Qcoh α d (S) ∼= Qcohd(X)
for any d ∈ Z, where αd is deﬁned as in Construction 3.10.
Proof. The equivalence ( 4.7) is the special case of Proposition 4.10 where we take
ρ to be X →χ∗X as in Construction 3.8. The equivalence ( 4.8) is the special case
of ( 4.7), where we take χ =pn as in Construction 3.10. □
Corollary 4.12. LetS be an algebraic stack and let α : X →S and β :Y →S be
Gm-gerbes. Then the tensor product and the internal Hom-funct or on Qcoh(X×SY )
induce functors
⊗ : Qcohα (S) × Qcohβ (S) → Qcohαβ (S),
Hom : Qcohα (S)op × Qcohβ (S) → Qcohα −1β (S).
Furthermore, if f : T → S is an arbitrary morphism of algebraic stacks, then we
get an induced pair of adjoint functors
f ∗ : Qcohα (S) → Qcohf ∗α (T ), f ∗ : Qcohf ∗α (T ) → Qcohα (S).
Recall our conventions regarding f∗ and Hom from Notation 1.8.
20 DANIEL BERGH AND OLAF M. SCHN ¨URER
Proof. The product X ×S Y has the structure of a Gm × Gm-gerbe such that the
projections on the factors X and Y induce the projections on the factors on the
bands. By applying Proposition 4.10 to the two projections Gm × Gm → Gm, we
get equivalences
Qcohα (S) ∼= Qcoh(1, 0)(X ×SY ), Qcohβ (S) ∼= Qcoh(0, 1)(X ×SY ),
where we have identiﬁed the character group of Gm with Z. By applying Proposi-
tion 4.10 to the multiplication and inversion maps given in Construction 3.10, we
obtain the equivalences
Qcohαβ (S) ∼= Qcoh(1, 1)(X ×SY ), Qcohα −1β (S) ∼= Qcoh(−1, 1)(X ×SY ),
respectively. Now the functors ⊗ and Hom are obtained from the monoidal struc-
ture of Qcoh(X ×SY ) described in Theorem 4.7. The statement about the functors
f ∗ and f∗ is an obvious consequence of Proposition 4.9. □
