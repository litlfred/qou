---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-019-63-reconstruction-results
section_title: "Reconstruction results"
section_number: 6.3
pages: 32-35
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
results and is a generalization of [ 22, Thm. 2.2.8].
Theorem 6.7. LetC be a tensor category, and B be a right C-module cat-
egory. Let (F,c ) : B → Cbe an exact and faithful module functor. Let
C =
∮ B∈BF (B)⊗∗F (B)∈C be the relative coend coalgebra introduced in
Proposition 6.2 and consider its category of comodules CC. Then the functor
F factorizes into an equivalence of C-module categories ˆF :B ∼−→ CC and
the forgetful functor f : CC→C :
(6.19) B
ˆF /d47/d47
F /d31/d31❄❄❄❄❄❄❄❄
CC
f/d126/d126⑥⑥⑥⑥⑥⑥⑥⑥
C.
Proof. Recall that we denote by
πA :F (A)⊗∗F (A)→
∮ B∈B
F (B)⊗∗F (B)
the dinatural transformations of the relative coend C(F ). The deﬁnition of
the functor ˆF :B→ CC was given in Proposition 6.4. Since F is faithful, ˆF
is also faithful. We need to prove that ˆF is essentially surjective and full.
Let us prove ﬁrst that ˆF is essentially surjective. Take ( M,ρ )∈ CC. We
endowedC⊗M structure of left C-comodule via ∆, then ρ :M→C⊗M is
actually a morphism in CC. We begin with the observation that, ( M,ρ ) is
the kernel (in CC) of the diﬀerence of morphisms
C⊗M
∆ ⊗id /d47/d47
id ⊗ρ
/d47/d47C⊗C⊗M.
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 33
Recall from Proposition 6.4 that, for any A∈B , the object F (A) has a left
H-comodule structure given by ρA =ψC
F (A),F (A)(πA). Hence, for any V∈C ,
the object F (A)⊗V has a left comodule structure given by ρA⊗id V . The
next Claim will be crucial for the proof. To prove this claim, it is essential
that the dinatural maps π satisfy equation ( 3.5).
Claim 6.1. For any A∈B ,V∈C , morphisms cA,V :F (A⊳V )→F (A)⊗V
areC-comodule maps.
Proof of Claim. We need to prove that
(ψH
F (A),F (A)(πA)⊗id V )cA,V = (id H⊗cA,V )ψH
F (A⊳V ),F (A⊳V )(πA⊳V )
This equation is equivalent to
(6.20)
(πA⊗id F (A)⊗V )(id⊗coevF (A)⊗id V )cA,V = (πA⊳V⊗cA,V )(id⊗coevF (A⊳V )).
Since π satisﬁes equation ( 3.5), it follows that
πA⊳V =πA(id F (A)⊗∗(F (id A⊳ coevV ∗)))
(
βV ∗
A⊳V,A
) −1.
Using the description of the prebalancing β given in ( 3.10), we obtain that
πA⊳V =πA(id F (A)⊗∗(cA⊳V,V ∗F (id A⊳ coevV ∗)))(id⊗φl
F (A⊳V ),V ∗)
(cA,V⊗id ∗F (A⊳V )).
(6.21)
It follows from the naturality of c that
cA,V ⊗V ∗F (id A⊳ coevV ∗) = (id F (A)⊗coevV ∗ ).
Using Equation ( 2.18), it follows that
cA⊳V,V ∗F (id A⊳ coevV ∗) = (c−1
A,V⊗id V ∗ )(id F (A)⊗coevV ∗).
Whence
πA⊳V =πA(id F (A)⊗∗(id F (A)⊗coevV ∗))(id F (A)⊗∗(c−1
A,V⊗id V ∗))
(id F (A)⊗φl
F (A⊳V ),V ∗ )(cA,V⊗id ∗F (A⊳V ))
=πA(id F (A)⊗∗(id F (A)⊗coevV ∗))(id F (A)⊗φl
V ∗,F (A)⊗V )
(cA,V⊗∗(c−1
A,V )).
(6.22)
The second equality follows from the naturality of φl. It follows by a tedious,
but straightforward, computation that
( ∗(id F (A)⊗coevV ∗)⊗id F (A)⊗V
)(
φl
V ∗,F (A)⊗V⊗id F (A)⊗V
)
(
id V⊗coevF (A)⊗V
)
= coev F (A)⊗id V
(6.23)
34 LENTNER AND MOMBELLI
Let us prove now equation ( 6.20). The right hand side of ( 6.20) is equal to
= (πA⊳V⊗id F (A)⊗V )(id⊗cA,V )(id F (A⊳V )⊗coevF (A⊳V ))
=
(
πA⊗id F (A)⊗V
)(
id F (A)⊗∗(id F (A)⊗coevV ∗)⊗id F (A)⊗V
)
(
id F (A)⊗φl
V ∗,F (A)⊗V⊗id F (A)⊗V
)(
cA,V⊗∗(c−1
A,V )⊗id F (A)⊗V
)
(id⊗cA,V )(id F (A⊳V )⊗coevF (A⊳V ))
=
(
πA⊗id F (A)⊗V
)(
id F (A)⊗∗(id F (A)⊗coevV ∗)⊗id F (A)⊗V
)
(
id F (A)⊗φl
V ∗,F (A)⊗V⊗id F (A)⊗V
)(
cA,V⊗coevF (A)⊗V
)
= (πA⊗id F (A)⊗V )(id F (A)⊗coevF (A)⊗id V )cA,V.
The second equality follows from Equation ( 6.22), the third equality follows
from ( 2.3), and the last equality follows from ( 6.23). This ﬁnishes the proof
of the Claim. □
From this Claim follows that, natural isomorphisms c endow the functor
ˆF with structure of module functor. Let
~C = ~C(F,c ) =
∮ B∈B
B⊳ ∗F (B)∈B
be the object deﬁned in Proposition 3.7, together with themap
δ : ~C→ ~C⊳C,
presented in Diagram ( 6.10). Since F ( ~C) = C, it also follows from Claim
6.1 that, there are C-comodule isomorphisms
F ( ~C⊳M )≃C⊗M,
F ( ~C⊳ (C⊗M ))≃C⊗C⊗M.
Hence (M,ρ ) is the kernel of the diﬀerence of morphisms
F ( ~C⊳M )
F (h1)/d47/d47
F (h2)
/d47/d47F ( ~C⊳ (C⊗M )),
whereh1 =δ⊳ id M,h 2 = id ~C⊳ρ . Since F is left exact (M,ρ )≃F (ker(h1−
h2)). This proves that ˆF is essentially surjective.
Let us prove now that ˆF is full. Take A,B ∈B and f :F (A)→F (B) a
C-comodule morphism. We have a commutative diagram
(6.24) F (A)
f
/d15/d15
ρA
/d47/d47C⊗F (A)
id H ⊗f
/d15/d15
F (B)
ρB
/d47/d47C⊗F (B).
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 35
This implies that, we have a commutative diagram
0 /d47/d47F (A)
ρA /d47/d47
f
/d15/d15
C⊗F (A)
hA
1 −hA
2 /d47/d47
id ⊗f
/d15/d15
C⊗(C⊗F (A))
id ⊗f
/d15/d15
0 /d47/d47F (B)
ρB /d47/d47C⊗F (B)
hB
1 −hB
2 /d47/d47C⊗(C⊗F (B)).
(6.25)
WherehA
1 = id H⊗ρA,h A
2 = ∆⊗id F (A). Note that, by the universal property
of the kernel, the map f :F (A)→F (B) is the unique morphism ﬁtting in
this diagram. Deﬁne
~C = ~C(F,c ) =
∮ B∈B
B⊳ ∗F (B)∈B.
See Proposition 3.7 for the deﬁnition of this coend. Using Proposition 6.6,
for any B∈B , we have an exact sequence
0→B
~ρB
−−−→~C⊳F (B)
~h−−−−→~C⊳ (C⊗F (B)),
where ~hB = id ~C⊳ρ B−δ⊳ id F (B). For the deﬁnition of δ and ~ρB see ( 6.9),
(6.10). Since f is a comodule morphism, by the universal property of the
kernel, there exists a unique morphism η that ﬁts into the diagram
0 /d47/d47A
~ρA /d47/d47
η
/d15/d15
~C⊳F (A)
~hA /d47/d47
id ⊳f
/d15/d15
~C⊳ (C⊗F (A))
id ⊳(id ⊗f )
/d15/d15
0 /d47/d47B
~ρB /d47/d47 ~C⊳F (B)
~hB /d47/d47 ~C⊳ (C⊗F (B)).
(6.26)
Applying F to this diagram we obtain diagram ( 6.25). By the uniqueness
of f , we get that F (η) = f , proving that ˆF is full. □
