---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-010-31-existence-of-coends
section_title: "Existence of (co)ends"
section_number: 3.1
pages: 15-17
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
(co)ends exists. All these (co)ends will be used in subseque nt sections. We
shall use ideas from [ 25].
LetC be a tensor category, B be a right C-module category. Since our
deﬁnition of module category includes that the action is rig ht exact in each
variable, hypothesis of [ 9, Thm. 2.24] are fulﬁlled. This means that, there
exists an algebra A∈C such that
(3.8) B≃ AC
as module categories. Consider C as a right C-module category with the
regular action. We shall denote by Rex C(B,C) the category of right exact
C-module functors. The functor
Φ : Bop→ Rex C(B,C),
Φ(B)(D) = Hom (D,B )∗
is an equivalence of categories, since, under identiﬁcatio n ( 3.8), the functor
Φ is the composition of equivalences
(AC)op (−)∗
−−−→CA
R−→Rex C(AC,C).
Here R :CA→ Rex C(AC,C) is the functor given by R(V )(W ) = V⊗AW.
Let be (F,c )∈ Rex C(B,C). In particular, we have natural isomorphisms
cB,X :F (B⊳X )→F (B)⊗X,
for B∈B,X ∈C . Consider the functor
Bop×B→B ,
(D,B )↦→D⊳ ∗F (B).
This functor posses a C-prebalancing
(3.9) γV
B,D :D⊳ ∗F (B⊳V )→D⊳ ∗V⊗∗F (B),
γV
B,D = id D⊳ (φl
F (B),V )−1∗(c−1
B,V ).
Proposition 3.7. LetB be a right C-module category. For any right exact
C-module functor (F,c ) :B→C the coend
~C(F,c ) =
∮ B∈B
(B⊳ ∗F (B),γ )∈B,
exists. Moreover, the functor (F,c )↦→~C(F,c ) is a quasi-inverse of Φ .
16 LENTNER AND MOMBELLI
Proof. For any D∈B we have
Natm(Φ(D),F )≃
∮
B∈B
HomC(Φ(D)(B),F (B))
≃
∮
B∈B
HomC(HomB(B,D )∗,F (B))
≃
∮
B∈B
HomC(∗F (B), HomB(B,D ))
≃
∮
B∈B
HomB(B⊳ ∗F (B),D )
≃ HomB(
∮ B∈B
B⊳ ∗F (B),D )
= Hom Bop(D,
∮ B∈B
B⊳ ∗F (B)).
The ﬁrst isomorphism is Proposition 3.3 (ii), and the ﬁfth isomorphism is
Proposition 3.4. Observe that, to prove the existence of the fourth isomor-
phism, one has to check that the natural isomorphisms
HomC(∗F (B), HomB(B,D )≃ HomB(B⊳ ∗F (B),D )
commute with the respective prebalancings and then use Prop osition 3.3
(i). This calculation is left to the reader. This proves both , that the coend
~C(F,c ) exists and that the quasi-inverse of Φ is given by
¯Φ : Rex C(B,C)→B op,
¯Φ(F,c ) =
∮ B∈B
(B⊳ ∗F (B),γ ).
□
For a pair of module functors ( F,c ), ( ~F, ˜c) :B→C , the functor
Bop×B→C ,
(A,B )↦→~F (B)⊗∗F (A)
has a canonical prebalancing, given by
βX
A,B : ~F (B)⊗∗F (A⊳X )→ ~F (B⊳ ∗X)⊗∗F (A),
βX
A,B = (˜c−1
B,∗X⊗id )(id ~F (B)⊗(φl
F (A),X )−1∗(c−1
A,X )).
(3.10)
As a consequence of Lemma 3.5, one can apply ~F to the coend in Propo-
sition 3.7. Thus we get the next result.
Corollary 3.8. For any pair of right exact C-module functors F, ~F :B→C ,
the coend ∮ B∈B
( ~F (B)⊗∗F (B),β )∈B,
exists. □
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 17
