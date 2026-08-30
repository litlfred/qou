---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-020-64-hopf-algebras-in-c-constructed-from-a-coend
section_title: "Hopf algebras in C constructed from a coend"
section_number: 6.4
pages: 35-44
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
monoidalC-module category, and the functor ( F,c,ξ ) :B→C is a monoidal
module functor, one can endow the coalgebra C =C(F ) with a Hopf algebra
structure. In this Section, we shall explain the constructi on of the product
and antipode on C(F ). The new hypothesis needed to construct such Hopf
algebra is that C posses a braiding.
To construct the product m : C(F )⊗C(F )→ C(F ) we shall use ideas
from [ 19]. In few words, we shall construct some natural module trans for-
mationF⊗F→C(F )⊗F⊗F and use Lemma 6.1 to ﬁnd m :C(F )⊗C(F )→
C(F ).
36 LENTNER AND MOMBELLI
Lemma 6.8. LetC be a braided tensor category, B be a monoidal C-module
category, and a monoidal module functor (F,c,ξ ) : B→C . Let us denote
dB,V the following natural isomorphism
dB,V : ∗F (B⊳V )→ ∗V⊗∗F (B),
dB,V =
(
φl
F (B),V
) −1∗(c−1
B,V ).
Then, for any B∈B , V ∈C , we have
(6.27) dB,∗V ⊗V = (φl
∗V,V⊗id )(id ∗V⊗dB,∗V )dB⊳∗V,V,
Proof. It follows by a straightforward calculation, using ( 2.18). □
Recall, from Proposition 5.9, the functors
H, ~H :B ⊠CB→C ,
determined by
H(A ⊠B) = F (A⊗B), ~H(A ⊠B) = F (A)⊗F (B),
for anyA,B∈B . Recall also that, we are denoting by πB :F (B)⊗∗F (B)→
C(F ) the dinatural transformations, and the associated left C(F )-coaction
ρB =ψC
F (B),F (B)(πB).
Remark 6.9. In the caseC = vect k, the following Proposition is trivial, since
it only says that some natural transformation is additive. I n the general
case, where C is arbitrary, it is far from obvious, and it is a crucial step
towards the reconstruction of the product in C(F ). Its proof will highlight
the importance of all required axioms.
For later use, π has to satisfy Equation ( 3.5), using prebalancing ( 6.1).
This means that
(6.28)
πB⊳V =πB
(
id F (B)⊗∗F (id B⊳ coevV ∗)
)(
id F (B)⊗d−1
B⊳V,V ∗
)(
cB,V⊗id ∗F (B⊳V )
)
.
Proposition 6.10. LetC be a braided tensor category, B be a monoidal
C-module category, and (F,c,ξ ) :B→C be a monoidal module functor. The
natural transformation µ : ~H→C(F )⊗ ~H determined by the composition
~H(A,B )
ξA,B
−−−→H(A,B )
ρA⊗B
−−−→C(F )⊗H(A,B )
id ⊗ξ−1
A,B
−−−−−−→C(F )⊗ ~H(A,B )
is a natural module transformation. That is µ∈ Natm( ~H,C (F )⊗ ~H).
Proof. It follows from Proposition 5.9 that ξ is a natural module transfor-
mation. Once it has been established that the diagram
(6.29) H(A,B⊳V )
eA,B,V
/d15/d15
ρA⊗B⊳V /d47/d47C(F )⊗H(A,B⊳V )
id C(F )⊗eA,B,V
/d15/d15
H(A,B )⊗V
ρA⊗B ⊗id V/d47/d47C(F )⊗H(A,B )⊗V.
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 37
is commutative, the proof will follow. Recall, from the proo f of Proposition
5.9 that
eA,B,V :F (A⊗(B⊳V ))→F (A⊗B)⊗V,
eA,B,V =cA⊗B,VF (l−1
A⊗B,V (id A⊗lB,V ))
We shall also keep the notation
ηA,B,V :A⊗(B⊳V )→ (A⊗B)⊳V,
ηA,B,V =l−1
A⊗B,V (id A⊗lB,V ).
Using the deﬁnition of ρA, one can see that diagram ( 6.29) amounts to
(id C(F )⊗eA,B,V )(πA⊗B⊳V⊗id F (A⊗B⊳V ))(id F (A⊗B⊳V )⊗coevF (A⊗B⊳V )) =
= (πA⊗B⊗id F (A⊗B)⊗V )(id F (A⊗B)⊗coevF (A⊗B)⊗id V )eA,B,V
(6.30)
Using the dinaturality of π, one can see that the left hand side of ( 6.30) is
equal to
=
(
π(A⊗B)⊳V (F (ηB,V )⊗∗F (η−1
A,B,V ))⊗eA,B,V
)
(id F (A⊗B⊳V )⊗coevF (A⊗B⊳V ))
=
(
π(A⊗B)⊳V⊗cA⊗B,V
)(
F (ηA,B,V )⊗coevF ((A⊗B)⊳V )
)
=
(
π(A⊗B)⊳V⊗id
)(
F (ηA,B,V )⊗id⊗cA⊗B,V
)(
id⊗coevF ((A⊗B)⊳V )
)
=
(
π(A⊗B)⊳V⊗id
)(
F (ηA,B,V )⊗id⊗cA⊗B,V
)(
id⊗d−1
A⊗B,V⊗c−1
A⊗B,V
)
(id F (A⊗B⊳V )⊗∗V ⊗coevA⊗B ⊗id V
)(id F (A⊗B⊳V )⊗coevV )
=
(
π(A⊗B)⊳V⊗id
)(
F (ηA,B,V )⊗d−1
A⊗B,V⊗id F (A⊗B)⊗V
)
(id F (A⊗B⊳V )⊗∗V⊗coevA⊗B⊗id V )(id F (A⊗B⊳V )⊗coevV )
= (πA⊗B⊗id F (A⊗B)⊗V )(id F (A⊗B)⊗coevF (A⊗B)⊗id V )eA,B,V
The second equality follows from the deﬁnition of eA,B,V and ( 2.3), the
fourth follows from ( 2.21). The last equation follows by using ( 6.28) and
(6.27). □
Theorem 6.11. Assume (C,σ ) is a braided tensor category,B is a monoidal
right C-module category, and (F,c,ξ ) : B → Cis an exact and faithful
monoidal module functor with monoidal structure
ξA,B :F (A)⊗F (B)→F (A⊗B).
The relative coend coalgebra C(F ) from Theorem 6.7 has an algebra struc-
ture, with unit u = π1 and product m : C(F )⊗C(F )→ C(F ) determined
by
(m⊗id )(πA⊗πB⊗id F (A)⊗F (B))(id⊗σF (A),F (B)⊗∗F (B)⊗id F (B))
(id F (A)⊗coevF (A)⊗id F (B)⊗coevF (B)) = (id C(F )⊗ξ−1
A,B)ρA⊗BξA,B,(6.31)
38 LENTNER AND MOMBELLI
for any A,B ∈B . The object C(F ) becomes a bialgebra in C. Moreover,
the equivalence of C-module categories ˆF :B→ C(F )C is an equivalence of
tensor categories.
Proof. Recall from Lemma 6.3 that, if f : C⊗CC→C is the forgetful functor,
thenC(f ) = C⊗C and the dinatural transformations of this coend are given
by
λ(W,ρ) :W⊗∗W→C⊗C,
λ(W,ρ) = ¯ψC⊗C
W,W (ρ).
Since the functor F :B →C factorizes as F = f◦ ˆF , then the functor
~H =⊗◦ (F ⊠F ) :B ⊠CB→C factorizes as
B ⊠CB
~H /d47/d47
ˆF ⊠ ˆF
/d15/d15
C
CC ⊠C CC
⊗
/d15/d15
C⊗CC
f
/d62/d62⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤
Using Lemma 3.6, since ˆF is an equivalence of right C-module categories, it
follows that
C( ~H) =
∮ X∈B⊠CB
~H(X)⊗∗ ~H(X) = C(F )⊗C(F ).
Lemma 3.6 also explains how to compute dinatural transformations of t his
coend. If πX : ~H(X)⊗∗ ~H(X)→C(F )⊗C(F ),X∈B ⊠CB, are the dinatural
transformations associated to this coend, then
πA⊠B =λ(F (A)⊗F (B),ρ) =
(
id C(F )⊗C(F )⊗evD
)(
id C⊗σF (A),C⊗id F (B)⊗∗D
)
(
πA⊗id F (A)⊗πB⊗id
)
(id F (A)⊗coevF (A)⊗id F (B)⊗coevF (B)⊗id ∗D),
for any A,B ∈ B. Here D = F (A)⊗F (B). Here ρ : F (A)⊗F (B) →
C(F )⊗F (A)⊗F (B) is the comodule structure of the tensor product accord-
ing to formula ( 4.6). It follows from Lemma 6.1 that there is an isomorphism
ω : Hom C(C(F )⊗C(F ),C (F ))→ Natm( ~H,C (F )⊗ ~H),
ω(g)X = (g⊗id ~H(X))ψC(F )⊗C(F )
~H(X), ~H(X) (πX ).
Since, by Proposition 6.10, (id C(F )⊗ξ−1
A,B)ρA⊗BξA,B is a natural module
transformation, that is
(id C(F )⊗ξ−1
A,B)ρA⊗BξA,B∈Natm( ~H,C (F )⊗ ~H),
then there exists a morphism m :C(F )⊗C(F )→C(F ) such that
ω(m)A⊠B = (id C(F )⊗ξ−1
A,B)ρA⊗BξA,B.
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 39
Using the rigidity axioms, the naturality of σ and the formula for πA⊠B, this
equation implies ( 6.31). Using ( 6.31), follows that
m◦ (m⊗id ) =m◦ (id⊗m),
m◦ (u⊗id ) = id = m◦ (id⊗u).
It follows also from ( 6.31) that ξ is a comodule morphism, giving the
functor ˆF structure of monoidal functor. □
Deﬁnition 6.12. For any monoidal module functor F :B→C we shall
denote by
H(F ) =
∮ B∈B
F (B)⊗∗F (B)∈C
the bialgebra with product given by Theorem ( 6.11) and coproduct ( 6.3).
Remark 6.13. In Theorem 6.11, some hypothesis on the functor F :B→C
are superﬂuous. It follows from [ 8, Corollaire 2.10] that, if F is right exact
then it is exact and faithful.
Let (H, ∆ ,m ) be a bialgebra in C. In the next results, we shall be devoted
to prove that the bialgebra reconstructed in Theorem 6.11, from the forgetful
functor f : HC→C , coincides with the original bialgebra H.
In Lemma 6.3 we already proved that the reconstructed coalgebra coin-
cides with H. Moreover, if ( W,ρ W )∈ HC, then we have deﬁned dinatural
transformations
πW :W⊗∗W→H,
πW = ¯ψH
W,W (ρW ) = (id H⊗evW )(ρW⊗id ∗W ).
See ( 2.8) for the deﬁnition of isomorphisms ¯ψ. In order to see that, the
reconstructed multiplication coincides with the product o f H, we only need
to prove that the original product m satisﬁes diagram ( 6.31). This will be
done in the next Proposition.
Proposition 6.14. Let (H, ∆ ,m ) be a bialgebra inC. Using dinatural trans-
formations πW :W⊗∗W→H, πW = ¯ψH
W,W (ρW ), we have that equation
m(πV⊗πW⊗id V ⊗W )(id V ⊗∗V⊗σV,W ⊗∗W⊗id W )(id⊗coevV⊗id⊗coevW ) =
=ρV ⊗W.
holds for any pair (V,ρ V ), (W,ρ W )∈ HC.
Proof. It follows using the naturality of σ and ( 4.6). □
40 LENTNER AND MOMBELLI
6.5. The antipode of H(F ). In the next results we shall construct an
antipode S :H(F )→H(F ), making the bialgebra H(F ) a Hopf algebra in
C.
Lemma 6.15. Let (C,σ ) be a braided tensor category, and B be a monoidal
rightC-module category. Let (F,c ) :B→C be an exact and faithful monoidal
module functor. For any B∈B , V ∈C there are natural isomorphisms
(6.32) tB,V : ∗(B⊳V )→ ∗B⊳ ∗V
such that the diagram
(6.33) ∗F (B⊳V )
∗(c−1
B,V )
/d15/d15
F (tB,V ) /d47/d47F (∗B⊳ ∗V )
c∗B,∗ V
/d15/d15
∗(F (B)⊗V )
σ∗V,∗F (B)(φl
F (B),V )−1
/d47/d47F (∗B)⊗∗V,
is commutative.
Proof. We shall freely use the fact that F (∗B) = ∗F (B), for any B∈B .
Since we are under the same hypothesis as Theorem 6.7, the functor F :
B→ HC is full. Since F (∗B⊳ ∗V ) is a left H-comodule, and the composition
h =c−1
∗B,∗Vσ∗V,F (B)(φl
F (B),V )−1∗(c−1
B,V ) : ∗F (B⊳V )→F (∗B⊳ ∗V ),
is an isomorphism, we can endow ∗F (B⊳V ) with someH-comodule structure
such that, h is a H-comodule map. Fullness of F implies that, there exist
some tB,V such that F (tB,V ) = h. □
We shall use the same notation as in previous sections. We den ote by
πA :F (A)⊗∗F (A)→H(F ) =
∮ B∈B
F (B)⊗∗F (B)
the dinatural transformations of the relative coend H(F ). Also, recall from
Proposition 6.4, that for any A∈B we have that (F (A),ρ A) is a left H(F )-
comodule, with structure given by
ρA =ψH(F )
F (A),F (A)(πA) = (πA⊗id F (A))(id F (A)⊗coevF (A)).
Henceforth, for simplicity, we shall denote H =H(F ).
Lemma 6.16. Let (C,σ ) be a braided tensor category, and B be a monoidal
rightC-module category. For any B∈B , V ∈C , let us recall morphisms
dB,V , deﬁned in Lemma 6.8, as
dB,V : ∗F (B⊳V )→ ∗V⊗∗F (B),
dB,V =
(
φl
F (B),V
) −1∗(c−1
B,V ).
Then, for any B∈B , V ∈C , we have
(6.34) ( σ−1
∗V,H⊗id ∗F (B))(id H⊗dB,V )ρ∗(B⊳V ) = (id ∗V⊗ρ∗B)dB,V.
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 41
Proof. Using Lemma 6.15, there are natural isomorphisms tB,V : ∗(B⊳V )→
∗B⊳ ∗V such that
(6.35) c∗B,∗VF (tB,V ) = σ∗V,F (B)dB,V.
The naturality of φl and c implies that
(6.36) F (∗(id B⊳ coevV )) = ( ∗(coevV )⊗id ∗F (B))dB,∗V ⊗V,
for any B∈B , V ∈C . Using the dinaturality of π we obtain that
(6.37) π∗(B⊳V ) =π∗B⊳∗V
(
F (tB,V )⊗∗F (t−1
B,V )
)
,
for any B∈B , V ∈C . Also, dinatural transformations π satisfy ( 3.5), this
implies that, for any B∈B , V∈C , we have
πB⊳∗V =πB
(
id F (B)⊗F (∗(id B⊳ coevV ))
)(
id F (B)⊗d−1
B⊳∗V,V
)
(
cB,∗V⊗id ∗F (B⊳∗V )
)
.
(6.38)
Next, when it is not absolutely necessary, as a space saving m easure, we
shall write the identities id , without using subscripts. Us ing the deﬁnition
or ρ we obtain that
(σ−1
∗V,H⊗id ∗F (B))(id H⊗dB,V )ρ∗(B⊳V )d−1
B,V
is equal to
= (σ−1
∗V,H⊗id ∗F (B))(id H⊗dB,V )(π∗(B⊳V )⊗id )(id⊗coev∗F (B⊳V ))d−1
B,V
= (σ−1
∗V,H⊗id ∗F (B))(π∗B⊳∗V⊗dB,V )(F (tB,V )⊗∗F (t−1
B,V )⊗id )
(id⊗coev∗F (B⊳V ))d−1
B,V
= (σ−1
∗V,H⊗id ∗F (B))(π∗B⊳∗V⊗dB,V )(F (tB,V )⊗id ∗F (∗B⊳∗V )⊗F (t−1
B,V ))
(id⊗coevF (∗B⊳∗V ))d−1
B,V
= (σ−1
∗V,H⊗id ∗F (B))(π∗B⊗id )(id⊗F (∗(id ∗B⊳ coevV ))⊗id )(id⊗d∗B⊳∗V,V⊗id )
(c∗B,∗V⊗id )
(
F (tB,V )d−1
B,V⊗id ∗F (∗B⊳∗V )⊗dB,VF (t−1
B,V )
)
(id⊗d−1
∗B,∗V⊗c−1
∗B,∗V )
(id⊗coev∗F (B)⊗id ∗V )(id ∗F (B⊳V )⊗coev∗V )
= (σ−1
∗V,H⊗id ∗F (B))(π∗B⊗id )(id⊗(∗(coevV )⊗id ∗B))dB,∗V ⊗V⊗id )
(id⊗d∗B⊳∗V,V⊗id )
(
c∗B,∗VF (tB,V )d−1
B,V⊗id ∗F (∗B⊳∗V )⊗dB,VF (t−1
B,V )c−1
∗B,∗V
)
(id⊗d−1
∗B,∗V⊗id )(id⊗coev∗F (B)⊗id ∗V )(id ∗F (B⊳V )⊗coev∗V )
= (id ∗V⊗π∗B⊗id )(σ−1
∗V,F (∗B)⊗∗F (∗B)⊗id )(id⊗ev∗V⊗id ∗F (∗B)⊗∗V ⊗∗F (B))
(σ∗V,∗F (B)⊗id ∗∗V ⊗∗F (∗B)⊗σ∗V,∗F (B))(id ∗V ⊗∗F (B)⊗∗∗V⊗coev∗F (B)⊗id ∗V )
(id⊗coev∗V )
= (id ∗V⊗ρ∗B).
The second equality follows from ( 6.37), the third equality follows from ( 2.3),
the fourth one follows from ( 6.38), the ﬁfth equality follows from ( 6.36). The
42 LENTNER AND MOMBELLI
sixth equality follows by using ( 2.6) and ( 6.35), and the last equality follows
by using the rigidity axioms and ( 4.1). □
Recall that, sometimes we are denoting H =H(F ).
Theorem 6.17. LetC be a tensor category, and B be a monoidal right C-
module category. Let (F,c ) :B→C be an exact and faithful monoidal module
functor. There exists a map S : H(F )→ H(F ), such that, it corresponds,
under isomorphism
ω : Hom C(H(F ),V )→ Natm(F,V⊗F )
presented in (6.2), to the natural module transformation α :F→H(F )⊗F,
αB = (evF (B)⊗id H(F )⊗F (B))(id F (B)⊗σ−1
∗F (B),H(F )⊗id F (B))
(id F (B)⊗ρ∗B⊗id F (B))(id F (B)⊗coevF (B)).
That is ω(S) = α.
Proof. We only need to prove that, indeed, α is a module natural transfor-
mation, that is
(id H⊗cB,V )αB⊳V = (αB⊗id V )cB,V,
for any B∈B , V ∈C . Equations ( 2.20) and ( 2.21) implies that
evF (B⊳V ) = ev F (B)
(
id⊗evV⊗id
)(
cB,V⊗dB,V
)
,
coevF (B⊳V ) =
(
d−1
B,V⊗c−1
B,V
)(
id⊗coevF (B)⊗id
)
coevV
(6.39)
Using the deﬁnition of α we obtain that (id H⊗cB,V )αB⊳Vc−1
B,V is equal to
= (ev F (B⊳V )⊗id H⊗F (B)⊗V ))(id F (B⊳V )⊗σ−1
∗F (B⊳V ),H⊗cB,V )
(id F (B⊳V )⊗ρ∗(B⊳V )⊗id F (B⊳V ))(id F (B⊳V )⊗coevF (B⊳V ))c−1
B,V
= (ev F (B)⊗id H⊗F (B)⊗V ))
(
id⊗evV⊗id ∗F (B)⊗H⊗F (B)⊗V
)
(id F (B)⊗V⊗σ−1
∗V ⊗∗F (B),H⊗id F (B)⊗V )
(
cB,V⊗id H⊗dB,V⊗cB,V
)
(id F (B⊳V )⊗ρ∗(B⊳V )⊗id F (B⊳V ))
(
id F (B⊳V )⊗d−1
B,V⊗c−1
B,V
)
(
id F (B⊳V )⊗∗V⊗coevF (B)⊗id V
)
(id F (B⊳V )⊗coevV )c−1
B,V
= (ev F (B)⊗id H⊗F (B)⊗V ))
(
id⊗evV⊗id ∗F (B)⊗H⊗F (B)⊗V
)
(id⊗σ−1
∗F (B),H⊗id )(id⊗σ−1
∗V,H⊗id )
(
id⊗(id H⊗dB,V )ρ∗(B⊳V )d−1
B,V⊗id
)
(
id F (B⊳V )⊗∗V⊗coevF (B)⊗id V
)
(id F (B⊳V )⊗coevV )
=αB⊗id V.
The second equality follows from ( 6.39) and the naturality of σ, the third
equality follows by ( 4.1). The last equality follows from ( 6.34) and rigidity
axioms. □
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 43
Remark 6.18. The above result is the most sensitive statement to prove in
order to prove the existence of the antipode for H(F ). In the case C = vect k,
the isomorphism
ω : Hom C(H(F ),V )→ Nat (F,V⊗F )
lands in the space of all natural transformations. So, in that case, there is
nothing to prove, and the existence of S is guaranteed by the fact that ω is
an isomorphism.
Corollary 6.19. The bialgebra H(F ), from Deﬁnition 6.12, is actually a
Hopf algebra. The antipode S :H(F )→H(F ) is determined as the unique
morphism such that
(6.40) F (B)⊗∗F (B)
νB
/d15/d15
πB /d47/d47H(F )
S
/d15/d15
F (B)⊗∗F (B)⊗H
evF (B)⊗id H(F )/d47/d47H(F ),
is commutative. Here
νB = (id F (B)⊗σ−1
∗F (B),H(F ))(id F (B)⊗π∗B⊗id ∗F (B))(id F (B)⊗∗F (B)⊗coev∗F (B)).
Proof. Taking the map S : H(F )→ H(F ) deﬁned in Theorem 6.17, and
using the deﬁnition of α, one can prove that S satisﬁes Diagram ( 6.40).
Axioms
m◦ (id H⊗S)◦ ∆ = u◦ε,
m◦ (S⊗id H )◦ ∆ = u◦ε,
follow from ( 6.40) by a lengthy, but straightforward, computation. □
Remark 6.20. A version of the Hopf algebra H(F ) has been previously con-
sidered in the work of Lyubashenko [ 13], [ 14], when F is some ﬁber functor
and in [ 15], [ 16], when F is the identity functor. See also the work of P.
Schauenburg [22], whereC is the category of ﬁnite dimensional vector spaces.
However, there are new ingredients in our deﬁnition. We requ ire that B is
actually a monoidal C-module category, and the functor F is a monoidal
module functor. The use of the relative coend is another new feature of our
construction.
Let (H, ∆ ,m,S ) be a Hopf algebra in C. In the next Proposition we
shall see that the reconstructed antipode given in Theorem 6.17, out of the
forgetful functor f : HC→C , coincides with the original antipode S :H→
H.
Proposition 6.21. Let (H, ∆ ,m,S ) be a Hopf algebra in C. Using the
identiﬁcation H = H(f ) proven in Lemma 6.3, the reconstructed antipode
obtained in Corollary 6.19 coincides with the antipode S of H.
44 LENTNER AND MOMBELLI
Proof. Let us denote by ˆS : H→ H the map reconstructed in Proposition
6.19. For any V∈C , recall the isomorphism ( 6.2)
ω : Hom C(H(f ),V )→ Natm(f,V⊗f ),
ω(g)(W,ρW ) = (g⊗id W )ψH
W,W (πW ),
for any (W,ρ W )∈ HC. Corollary 6.17 implies that, if α : f→ H⊗f is the
module natural transformation deﬁned as
α(W,ρW ) = (ev W⊗id H⊗W )(id W⊗σ−1
∗W,H⊗id W )
(id W⊗ρ∗W⊗id W )(id W⊗coevW ),
for any (W,ρ W )∈ HC, then
ω( ˆS) = α.
Using formula ( 4.7) for ρ∗W we get that
α(W,ρW ) = (S⊗id W )ρW =ω(S)(W,ρW ),
for any (W,ρ W )∈ HC. Whence S = ˆS. □
