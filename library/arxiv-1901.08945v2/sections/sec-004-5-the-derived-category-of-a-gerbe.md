---
doc_id: arxiv-1901.08945v2
doc_title: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES"
section_id: sec-004-5-the-derived-category-of-a-gerbe
section_title: "The derived category of a gerbe"
section_number: 5
pages: 20-24
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
doc_brief: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group decomposes accordi ng to the char- acters of"
---
In this section we generalize some of the results by C˘ ald˘ araru [C˘ al00, Chapter 2]
and Lieblich [ Lie04, Section 2.2.4] on the basic structure of derived categories of
gerbes and twisted sheaves. Throughout the section, we let α : X →S be a gerbe
banded by a diagonalizable group ∆ with character group A.
Deﬁnition 5.1. Given a character χ : ∆ S → Gm,S , we say that an object F in
Dqc(X) is χ-homogeneous if it has χ-homogeneous cohomology. We denote the full
subcategory of χ-homogeneous objects in D qc(X) by D qc,χ (X).
Consider the special case ∆ = Gm and let id : Gm → Gm be the identity charac-
ter. An object in D qc, id(X) is called an α-twisted complex on S. We often use the
notation D qc,α (S) instead of D qc, id(X) employing a similar abuse of notation as in
Remark 4.5 if α is just a cohomology class in H 2(Sfppf, Gm).
We state the following lemma for convenient reference. See Remark 5.10 for
sharper results.
Lemma 5.2. Let S be an aﬃne scheme and let α : X → S be a trivial ∆ -gerbe,
where ∆ is a diagonalizable group. Then the obvious functor
(5.1) D(Qcoh( X))
∼
− →Dqc(X)
is a monoidal equivalence and induces equivalences
(5.2) D(Qcoh χ (X))
∼
− →Dqc,χ (X)
for each character χ of ∆ . Moreover, let T be an aﬃne scheme and let β :X ′ →T
be a trivial ∆ ′-gerbe, where ∆ ′ is a diagonalizable group. Assume that we have a
morphism ρ : X →X ′ of algebraic stacks. Then the squares
(5.3) D(Qcoh( X ′)) ∼ /d47/d47
Lρ ∗
/d15/d15
Dqc(X ′)
ρ ∗
/d15/d15
D(Qcoh(X)) ∼ /d47/d47 Dqc(X),
D(Qcoh(X ′)) ∼ /d47/d47 Dqc(X ′)
D(Qcoh(X)) ∼ /d47/d47
Rρ ∗
/d79/d79
Dqc(X)
ρ ∗
/d79/d79
commute up to natural equivalence.
Proof. The equivalence ( 5.1) is a special case of [ Lie04, Proposition 2.2.4.6], and
the equivalences ( 5.2) are then immediate from Theorem 4.7. The fact that the
equivalence ( 5.1) is monoidal follows from the fact that any complex in Qcoh( X)
admits a resolution by an h-ﬂat complex in Qcoh( X) which is also h-ﬂat as a
complex in Mod(Xlis-´ et, OX ). This can be seen by using a homotopy limit argument
(see [SP19, Tag 06XX]), using that any object in Qcoh( X) is a quotient of a locally
DECOMPOSITIONS 21
free sheaf and the fact that coproducts in Mod( Xlis-´ et, OX ) are exact and preserve
Qcoh(X).
The functor α∗ : Qcoh(X) → Qcoh(S) is exact, since this operation corresponds
to taking invariants and ∆ is diagonalizable. This well-known fact also ea sily follows
from the last sentence of Proposition 4.10 together with the decomposition in The-
orem 4.7. Hence the equivalence ( 5.1) shows that X has cohomological dimension
zero.
Note that ρ induces a morphism S → T on the coarse spaces, so ρ factors as
X →X ′ ×T S →X ′ where the ﬁrst morphism is a morphism of gerbes over S, and
the second morphism is aﬃne. Furthermore, the ﬁrst morphism fac tors as an aﬃne
morphism followed by a ∆-gerbe by Remark 4.1. Hence also ρ has cohomological
dimension zero, as this property is stable under composition and can be checked
after a faithfully ﬂat base change by [ HR17, Lemma 2.2]). In particular, ρ is
concentrated, so it follows from [ HNR18, Corollary 2.2] that the right hand square
(5.3) commutes. Hence also the left hand square commutes by adjunct ion. □
Remark 5.3. Let ρ : X → Y be a morphism of gerbes banded by diagonalizable
groups over an algebraic stack S as in Remark 4.1. Then the last part of the proof
shows that ρ is concentrated of cohomological dimension zero, as these proper ties
can be checked locally on S (see [ HR17, Lemma 2.2 and Lemma 2.5]).
The next theorem is the main structure theorem for the derived ca tegory of
a ∆-gerbe and the derived analog of Theorem 4.7. It is a generalization of the
observation in [ Lie04, Section 2.2.4] that the derived category splits according to
characters in certain situations.
Theorem 5.4. Let S be an algebraic stack and α : X → S a gerbe banded by a
diagonalizable group ∆ . Then Dqc,χ (X) is a triangulated subcategory of Dqc(X) for
each ∆ S-characterχ, and taking the coproduct gives an equivalence
(5.4)
∏
χ ∈A
Dqc,χ (X)
∼
− →Dqc(X), (Fχ )χ ∈A ↦→
⨁
χ ∈A
Fχ,
of triangulated categories, where A denotes the character group of ∆ .
Furthermore, assume that Fχ and Gψ are objects in Dqc(X) which are homoge-
neous for ∆ S-charactersχ and ψ, respectively. Then the objects
(5.5) Fχ ⊗ Gψ, Hom(Gψ, Fχ )
areχψ- and χψ−1-homogeneous, respectively.
Proof. By Theorem 4.7, the category Qcohχ (X) is a Serre subcategory of Qcoh( X).
It follows that D qc,χ (X) is a strictly full triangulated subcategory of D qc(X) by
[SP19, Tag 07B4, Tag 06UQ].
Recall that we work with sheaves on the lisse–´ etale sites overX andS. Note that
we get a morphism Xlis-´ et→Slis-´ etof topoi, by [ SP19, Tag 07AT], sinceα is smooth
(see Remark 4.1). In particular, there is no need to work with hypercoverings to
deﬁne pull-backs as in [ Ols07].
LetE be a subset of the set A of characters of ∆, and let Qcoh E(X) denote the
full subcategory of Qcoh( X) of objects which are direct sums of χ-homogeneous
objects for χ ∈E. Let F be the complement of E inA. It follows from Theorem 4.7
that (QcohE(X), QcohF (X)) is a torsion pair in Qcoh( X) and that both Qcoh E(X)
and QcohF (X) are abelian subcategories of Qcoh( X).
Let E and F be objects of Qcoh E(X) and QcohF (X), respectively. We will show
that
(5.6) Ext n
OX (E, F ) ∼= Hn(RΓ RHomOX (E, F ))
22 DANIEL BERGH AND OLAF M. SCHN ¨URER
vanishes for each n. Since RΓ RHomOX (E, F ) ∼= RΓ Rα∗RHomOX (E, F ), this fol-
lows if we prove that Rα∗RHomOX (E, F ) vanishes. The n-th cohomology sheaf of
Rα∗RHomOX (E, F ) is easily seen to be the sheaf of OS-modules associated to the
presheaf
(U →S) ↦→Extn
OXU
(E|XU, F |XU )
where U is a scheme and U → S is smooth. It is therefore enough to verify the
vanishing of ( 5.6) when S is aﬃne and the gerbe α : X →S is trivial. But in this
situation the functor ( 5.1) is an equivalence by Lemma 5.2, so we get the desired
vanishing from Lemma 2.5.(d) or, more easily, from Theorem 4.7.
All direct and inverse truncation systems in D qc(X) are eﬀective by Proposi-
tions 2.16 and 2.20. Hence the hypotheses of Theorem 2.22 are satisﬁed, so we get
a semi-orthogonal decomposition
(5.7) D qc(X) = ⟨Dqc,F (X), Dqc,E (X)⟩,
where D qc,E denotes the full subcategory of D qc(X) of objects with cohomology in
QcohE(X) and similarly for D qc,F (X).
We are now ready to prove that the functor ( 5.4) is an equivalence. First note
that it is well deﬁned since D qc(X) has arbitrary coproducts. Let χ ∈ A and set
E = {χ},F =A − {χ}. Then Hom Dqc(X)(Fχ, G) vanishes whenever Fχ ∈ Dqc,χ (X)
and G ∈ Dqc,F by the semi-orthogonal decomposition ( 5.7). Since D qc,χ (X) is a
full subcategory of D qc(X), it follows that the functor ( 5.4) is fully faithful.
Now let F be any object of D qc(X). Then the semi-orthogonal decomposi-
tion ( 5.7) gives a triangle
Fχ → F → F F → Σ Fχ
with Fχ ∈ Dqc,χ (X) and FF ∈ Dqc,F (X), respectively. By Remark 2.21 and The-
orem 4.7, the morphism Fχ → F induces an isomorphism H n(Fχ ) → Hn(F )χ for
eachn. It follows that the canonical map ⨁
χ ∈A Fχ → F induces an isomorphism
on cohomology and therefore is an isomorphism in D qc(X). Hence the functor ( 5.4)
is essentially surjective and therefore an equivalence.
Finally, we prove the statements about the monoidal structure. I t is enough
to prove the statement about the tensor product, since the sta tement about the
internal hom follows formally from the adjointness property. The q uestion whether
Fχ ⊗L
OX Gψ is χψ-homogeneous can be veriﬁed locally on S. Indeed, this follows
from Proposition 4.9, since cohomology of a complex commutes with pull-back
along a ﬂat map (see [ HR17, Equation 1.9]), and the pull-back functor along a
faithfully ﬂat map is conservative. Hence we may assume that S is aﬃne and that
the gerbe α : X →S is trivial. Now the statement follows from the underived case
described in Theorem 4.7 by the monoidal decomposition preserving equivalence
(5.1) in Lemma 5.2. □
Remark 5.5. Similarly as in Remark 4.8, the canonical morphism ⨁
χ ∈A Fχ →∏
χ ∈A Fχ is an isomorphism even if the character group A is not ﬁnite.
The following two propositions are the derived analogs of Proposition 4.9 and
4.10.
Proposition 5.6. Let S be an algebraic stack and α : X → S a gerbe banded by
a diagonalizable group ∆ . Let f : T → S be a morphism of algebraic stacks, and
let g : Y →X denote the canonical morphism from the pull-back Y of X along f .
Then the functors
g∗ : D qc(X) → Dqc(Y ), g ∗ : D qc(Y ) → Dqc(X)
respect the decompositions of Dqc(X) and Dqc(Y ) into homogeneous components
given in Theorem 5.4.
DECOMPOSITIONS 23
Proof. As a formal consequence of adjunction, it is enough to verify that the pull-
backg∗ respects the decomposition. By a similar reduction argument as in th e last
paragraph of the proof of Theorem 5.4, we reduce to the case when S and T are
aﬃne and the gerbes are trivial. Now the result follows from the unde rived setting
in Proposition 4.9 and the commutative diagram ( 5.3) in Lemma 5.2. □
Proposition 5.7. LetX and X ′ be gerbes over S banded by diagonalizable groups
∆ and ∆ ′, respectively, and let ρ : X → X ′ be a morphism over S with induced
morphism ϕ : ∆ S → ∆ ′
S on the bands. Fix a character χ′ : ∆ ′
S → Gm,S , and let
χ = χ′ ◦ϕ. Then the pull-back functor ρ∗ takes χ′-homogeneous objects to χ-
homogeneous objects and induces an equivalence
(5.8) ρ∗ : D qc,χ ′ (X ′)
∼
− →Dqc,χ (X)
of triangulated categories. In particular, if X ′ = S then ρ∗ : D qc(S) → Dqc(X) is
fully faithful with essential image consisting of those obj ects that are homogeneous
for the trivial character.
Proof. Since ρ is ﬂat (see Remark 4.1), the pull-back ρ∗ commutes with taking
cohomology (see [ HR17, Equation (1.9)]). In particular, the ﬁrst statement follows
from the underived case, which is given by Proposition 4.10.
Let us ﬁrst consider the special case X ′ = S. By Remark 5.3, the morphism ρ
is concentrated, so the push-forward ρ∗ respects ﬂat base change by [ HR17, The-
orem 2.6(4)]. Hence the statement can be veriﬁed locally. In particu lar, we may
assume that the gerbes are trivial and that S is aﬃne. Hence we may use the
equivalences in Lemma 5.2. Since ρ∗ and ρ∗ are exact, the statement follows from
the underived case, which is Proposition 4.10.
For the general case, we proceed exactly as in the proof of Propo sition 4.10 on
the level of derived categories. □
Similarly as in the underived case, we get the following corollaries.
Corollary 5.8. LetS be an algebraic stacks and let α :X →S be a gerbe banded
by ∆ , and choose a character χ : ∆ S → Gm,S . Then we have an equivalence
Dqc,χ ∗α (S) ∼= Dqc,χ (X)
of categories, where χ∗α is deﬁned as in Construction 3.8. In the particular case
when ∆ = Gm, this gives the equivalence
Dqc,α d (S) ∼= Dqc,d (X)
for any d ∈ Z, where αd is deﬁned as in Construction 3.10.
Proof. This is proven similarly as Corollary 4.11 by using Proposition 5.7 instead
of Proposition 4.10. □
Corollary 5.9 (cf. [ C˘ al00, Theorem 2.2.4]) . Let S be an algebraic stack and let
α :X →S and β :Y →S be Gm-gerbes. Then the tensor product and the internal
Hom-functor on Dqc(X ×SY ) induce triangulated functors
⊗ : D qc,α (S) × Dqc,β (S) → Dqc,αβ (S),
Hom : D qc,α (S)op × Dqc,β (S) → Dqc,α −1β (S).
Furthermore, if f : T → S is an arbitrary morphism of algebraic stacks, then we
get an induced pair of adjoint functors
f ∗ : D qc,α (S) → Dqc,f ∗α (T ), f ∗ : D qc,f ∗α (T ) → Dqc,α (S).
Proof. This is proven similarly as Corollary 4.12 by using Theorem 5.4, Proposi-
tion 5.6 and Proposition 5.7 instead of Theorem 4.7, Proposition 4.9 and Proposi-
tion 4.10. □
24 DANIEL BERGH AND OLAF M. SCHN ¨URER
We conclude the section with two remarks regarding alternative app roaches for
proving Theorem 5.4.
Remark 5.10. Note that Theorem 5.4 is trivial whenever the functor ( 5.1) is a
monoidal equivalence. By Lieblich [ Lie04, Proposition 2.2.4.6], the functor ( 5.1) is
an equivalence whenever S is a quasi-compact, separated scheme. More generally,
it follows from the work by Hall, Neeman and Rydh [ HNR18, Theorem 1.2] that
(5.1) is an equivalence whenever S is an algebraic space which is either noetherian
or quasi-compact with aﬃne diagonal. The aforementioned theorem applies since
in this case, the category D qc(X) is compactly generated by |A| objects by [ HR17,
Theorem 6.9] applied to the presheaf ( T → S) ↦→Dqc(XT ) of triangulated cate-
gories. Since we are not going to use this result, we leave the details o f verifying
the hypotheses of the cited theorem to the reader (cf. [ HR17, Example 9.2]). We
do not know whether the equivalence ( 5.1) is monoidal in this generality.
Finally, it should be emphasized that there certainly are interesting c ases when
(5.1) is not an equivalence. For instance, consider the Gm-gerbe in Example 3.7.(a).
The functor ( 5.1) is not an equivalence for X = B GL n if n ≥ 2 by [ HNR18,
Theorem 1.3], so Theorem 5.4 seems to be non-trivial even in this basic case.
Remark 5.11. Theorem 5.4 would be trivial if the category Mod( Xlis-´ et, OX ) ad-
mitted a decomposition similar to the one for Qcoh( X) described in Theorem 4.7.
We do not know whether this is the case, but we suspect it is not.
In [ SGA3i, Expos´ e 1, Proposition 4.7.2], it is stated that the category of (no t
necessarily quasi-coherent) sheaves of G − OS-modules on the small Zariski site is
equivalent to the category of sheaves of A-comodules for any aﬃne group scheme
G = Spec S A over a scheme S. If this were true, then it should be possible to
adapt the proof to our situation and to get a decomposition of Mod( Xlis-´ et, OX ).
However, we suspect that the previously cited proposition might be wrong, since
it uses [ SGA3i, Expos´ e 1, Proposition 4.6.4] which in turn uses the fact that the
canonical morphism
(5.9) F ⊗S A → α∗α∗F
is an isomorphism whenever F is quasi-coherent and α : X = Spec S A → S is
aﬃne. But this is certainly not true in general if we drop the condition that F be
quasi-coherent.
Let for example S be a scheme with an open subscheme U such that the inclusion
j : U →S is aﬃne and quasi-compact and F = j!OU is not quasi-coherent. Then
the canonical morphism j!OU ∼= F ⊗j∗OU →j∗j∗F ∼=j∗OU is not an isomorphism
because j∗OU is quasi-coherent. Let G := S ⊔U be the disjoint union. Then
α : G → S is in the obvious way an aﬃne ´ etale group scheme over S. In this
case A = α∗OG = OS ⊕j∗OU and the morphism ( 5.9) is not an isomorphism for
F =j!OU .
