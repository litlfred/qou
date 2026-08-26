---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-018-24-the-non-degenerate-quotient-let-c-be-an-addit
section_title: "The non-degenerate quotient. Let C be an additive k-linear spher-"
section_number: 2.4
pages: 8-10
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect exampl es."
---
ical category with End(1) ≃ k. For any two objects X,Y in C there is a
bilinear pairing
Θ : Hom C(X,Y ) × HomC(Y,X ) → k, Θ(fg ) = tr L(fg ) = tr R(gf );
C is non-degenerate if Θ is, for any X,Y . By [BaW1, Theorem 2.9], see also
[T], any additive spherical category C gives rise a factor category C, with the
same objects 3 as C and morphisms HomC(X,Y ) := Hom C(X,Y )/J (X,Y ),
X,Y ∈ C , where
J (X,Y ) = {f ∈ HomC(X,Y ) : tr L(fg ) = 0, ∀g ∈ HomC(Y,X )}.(2.8)
The category C is an additive non-degenerate spherical category, but it is not
necessarily abelian, even if C is abelian. Clearly, the quantum dimensions in
RepH and RepH are the same. See [Kn] for a general formalism of tensor
ideals, that encompasses the construction above.
We now give more information on RepH following [BaW1, Proposition
3.8]. Let us ﬁrst point out some precisions on the terminolog y used in the
literature on additive categories, see e. g. [Har] and refer ences therein. We
shall stick to this terminology in what follows. Let C be an additive k-linear
category, where k is an arbitrary ﬁeld.
• C is semisimple if the algebras End(X) are semisimple for all X ∈ C .
• An object X is minimal if any monomorphism Y →X is either 0 or
an isomorphism; hence End(X) is a division algebra over k.
• C is completely reducible if every object is a direct sum of minimal
ones.
Beware that in more recent literature in topology (where it is assumed
that k = k), an object S is said to be simple when End(S) ≃ k; and ‘ C
is semisimple’ means that every object in C is a direct sum of simple ones.
For instance, if C = A- mod, A an algebra, then a minimal object in C is
just a a simple A-module; then End(S) ∼= k by the Schur Lemma. But it is
well-known that the converse is not true.
Example 2.5. Let H = k⟨x,g |x2,g 2 − 1,gx +xg⟩ be the Sweedler Hopf
algebra. H has two simple modules, both one dimensional, namely the tri vial
3This is a bit misleading, as non-isomorphic objects in C may became isomorphic in C.
FROM HOPF ALGEBRAS TO TENSOR CATEGORIES 9
V + and V −, where g acts as −1. Consider the non-trivial extension V ± ∈
Ext1
H(V −,V +), that is V ± = kv ⊕ kw with action
g ·v =v, g ·w = −w, x ·v =w, x ·w = 0.
Then V ± is not simple and EndH(V ±) ∼= k. It is easy to see that the
indecomposable H-modules are V +, V −, V ± and V ∓ := ( V ±)∗; hence
RepH ≃ Rep Z/2 by Step 2 of the proof of Theorem 2.7 below. Also,
notice that in RepH it is not true that all endomorphism algebras are
semisimple (just take the regular representation); and, re lated to this, that
HomH(V ∓,V ±) ⁄= 0.
However, the converse above is true when the category is semi simple.
Remark 2.6. [Har, 1.1, 1.3] Let C be a semisimple additivek-linear category,
where k is an arbitrary ﬁeld.
(a) If α :V →W is not zero, then there exists β,γ :W →V such that
βα ⁄= 0, αγ ⁄= 0. If HomC(V,W ) = 0 , then HomC(W,V ) = 0 .
(b) If V ∈ C and End(V ) is a division ring, then V is minimal.
(c) If V,W ∈ C are minimal and non-isomorphic, then HomC(V,W ) = 0 .
Proof. (a) Assume that HomC(W,V )α = 0. Set U =V ⊕W ; then EndCUα
is a nilpotent left ideal of EndCU , hence it is 0.
(b) Let W ⁄= 0 and f ∈ Hom(W,V ) be a monomorphism. Since f ⁄= 0 ,
Hom(V,W ) ⁄= 0 by (a). Since End(V ) is a division ring, the map f ◦ − :
Hom(V,W ) → End(V ) is surjective. Therefore there exists g ∈ Hom(V,W )
such that f ◦g = id V . On the other hand, the map End(W ) → Hom(W,V ),
˜h ↦→f ◦ ˜h is injective. Hence g ◦f = id W since f ◦ (g ◦f ) = f ◦ idW . Thus
W ≃V . (c) follows from (a) at once. □
If H is a spherical Hopf algebra, then we denote by IndecqH the set of
isomorphism classes of indecomposable ﬁnite-dimensional H-modules with
non-zero quantum dimension.
Theorem 2.7. [BaW1, 3.8] LetH be a spherical Hopf algebra with pivot ω.
Then the non-degenerate quotient RepH is a completely reducible spherical
tensor category, and Irr RepH is in bijective correspondence with IndecqH.
By Remark 2.6, ‘completely reducible’ becomes what is called semisimple
in the recent literature.
Proof. The crucial step is to show that RepH is semisimple.
Step 1. [BaW1, 3.7] The algebra EndRep H(X) is semisimple for any X in
RepH.
Indeed, the Jacobson radical J of EndH (X) is contained in J (X,X ). For,
if ϑ ∈J, then ϑω is nilpotent, hence trL(ϑ) = tr V (ϑω) = 0 .
As a consequence of Step 1 and Remark 2.6, X ∈ RepH is minimal if
and only if EndRep H(X) ≃ k, that is if and only if it is simple. Also,
HomRep H(S,T ) = 0 , for S,T ∈ RepH simple non-isomorphic.
