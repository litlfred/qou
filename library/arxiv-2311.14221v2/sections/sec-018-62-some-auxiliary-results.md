---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-018-62-some-auxiliary-results
section_title: "Some auxiliary results"
section_number: 6.2
pages: 30-32
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
nical results that will be used later. In particular, these r esults will be used
in the proof of our main result Theorem 6.7.
LetB be a right C-module category, and ( F,c ) : B →C be a module
functor. To make calculations easier, we shall assume that t he associativity
of theC-module categoryB is trivial. Recall the relative coend
(6.8) ~C(F,c ) = ~C =
∮ B∈B
B⊳ ∗F (B)∈B,
presented in Proposition 3.7. Let us denote by
λB :B⊳ ∗F (B)→ ~C(F,c ),
the associated dinatural transformations. Analogous to th e deﬁnition of ∆,
given in ( 6.3), we shall deﬁne a map
(6.9) δ : ~C(F,c )→ ~C(F,c )⊳C (F,c ).
Lemma 6.5. There exists a unique morphism δ : ~C(F,c )→ ~C(F,c )⊳C (F,c )
such that
(6.10) B⊳ ∗F (B)
id ⊳(coevF (B)⊗id )
/d15/d15
λB /d47/d47 ~C
δ
/d15/d15
B⊳ ∗F (B)⊗F (B)⊗∗F (B)
λB ⊳ πB /d47/d47 ~C⊳C.
Proof. Let us denote dB,V the following natural isomorphism
dB,V : ∗F (B⊳V )→ ∗V⊗∗F (B),
dB,V =
(
φl
F (B),V
) −1∗(c−1
B,V ).
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 31
Recall from Equation ( 3.9), that the prebalancing used in the coend ~C(F,c )
is given by
γV
B,D :D⊳ ∗F (B⊳V )→D⊳ ∗V⊗∗F (B),
γV
B,D = id D⊳d B,V.
Using that c satisﬁes ( 2.18), it is not diﬃcult to prove that
(6.11) dB,∗V ⊗V = (φl
∗V,V⊗id )(id ∗V⊗dB,∗V )dB⊳∗V,V,
for any B∈B , V ∈C . The naturality of φl and c implies that
(6.12) F (∗(id B⊳ coevV )) = ( ∗(coevV )⊗id ∗F (B))dB,∗V ⊗V,
for any B∈B , V ∈C . Whence, using ( 2.6), it follows that
(6.13) F (∗(id B⊳ coevV ))d−1
B⊳∗V,V = (ev ∗V )⊗id ∗F (B))(id ∗V⊗dB,∗V ).
In this case, if A∈B , a dinatural transformation νB : B ⊳∗F (B)→ A
satisﬁes Equation ( 3.5) if and only if
(6.14) νB
(
id B⊳F (∗(id B⊳ coevV )
)
=νB⊳∗VγV
B⊳∗V,B.
Using that dinatural transformations λ and π both satisfy ( 3.5) and using
(6.13), it follows that dinatural transformation
(λB⊳ πB)(id B⊳ (coevF (B)⊗id ∗F (B))
also satisﬁes ( 6.14). Now, existence of the map δ : ~C(F,c )→ ~C(F,c )⊳
C(F,c ) satisfying ( 6.10) follows from the universal property of the relative
coend. □
For any A,B∈B and V∈C , deﬁne
~ψV
B,A : Hom B(B⊳ ∗V,A )→ HomB(B,A⊳V ),
~ψV
B,A(f ) = (f ⊳id V )(id B⊳ coevV ).
(6.15)
Compare with natural isomorphisms given in ( 2.7). For any B∈B , deﬁne
also
(6.16) ~ρB = ~ψF (B)
B, ~C (λB) : B→ ~C⊳F (B).
One could check that, using Lemma 3.5, whenever F is right exact,
F ( ~C) = C. The dinatural transformations of F ( ~C) is given by F (λB).
In particular, this implies that
(6.17) c ~C,F (B)F (~ρB) = ρB,
for any B∈B . Using deﬁnition of ∆ : C→C⊗C given by diagramm ( 6.2),
one can see that
(6.18) c ~C,CF (δ) = F (∆) .
If h1,h 2 :C⊗F (B)→C⊗C⊗F (B) are deﬁned as
h1 = id C⊗ρB, h 2 = ∆⊗id F (B),
32 LENTNER AND MOMBELLI
then, it is a standard result that, the kernel of the diﬀerence h1−h2 is ρB.
Using the above, we have the following:
Proposition 6.6. Assume that the module functor (F,c ) :B→C is faithful
and exact. The map ~ρB : B→ ~C ⊳F(B) is the kernel of the diﬀerence of
morphisms
~C⊳F (B)
~h1 /d47/d47
~h2
/d47/d47 ~C⊳ (C⊗F (B)),
where ~h1 = id ~C ⊳ρ B and ~h2 =δ⊳ id F (B).
Proof. Note that, we are using that F is right exact so that F ( ~C) = C. See
Lemma 3.5. Using ( 6.17), ( 6.18) and the naturality of c one can prove that
c ~C,C ⊗F (B)F (~h1− ~h2) = (h1−h2)c ~C,F (B).
This implies that F (~ρB) = ker F (~h1− ~h2) = F (ker ~h1− ~h2), since F is also
left exact. The result follows, since F is faithful. □
