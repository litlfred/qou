---
doc_id: arxiv-1202.5547v1
doc_title: "Markov property and Khovanov-Rozansky homology: Coxeter Case. Trafim LASY"
section_id: sec-000-abstract
section_title: "Abstract"
section_number: null
pages: 1-4
source_pdf: 1202.5547v1.pdf
source_sha256: 1268c0834b6c9206
doc_brief: "Markov property and Khovanov-Rozansky homology: Coxeter Case. Trafim LASY — In [2] Khovanov gave a construction of Khovanov-Rozansky ho mology, new triple-graded link invariant, taking the Hochschild"
---
In [2] Khovanov gave a construction of Khovanov-Rozansky ho mology, new triple-graded link
invariant, taking the Hochschild homology of the terms in Ro uquier complexes. Its bigraded Euler
characteristic provides the Markov trace of type An, which, in its turn, induces the well-known
HOMFLY polynomial. Gomi [1, (3.3)] has extended the deﬁniti on of Markov trace on a Hecke algebra
to all Coxeter groups. One can see that Khovanov’s and Rouqui er’s constructions can be directly
extended to these groups. We give a detailed proof that the co rresponding Euler characteristic
provides a Markov trace in the sense of Gomi for any Coxeter gr oup.
Let ( W, S ) be a Coxeter system with |S| = n < ∞. Let V be the C-vector space with the basis {es}s∈S
carrying the geometric representation of W . Then we have a natural action of W on the symmetric
algebra R = S(V ∗), which will be regarded as the graded polynomial ring C[{xs}s∈S] with deg xs = 1.
Now we brieﬂy recall the notions of Rouquier complexes needed to giv e Khovanov’s construction of
Khovanov-Rozansky homology. Let BW = ⟨σs⟩s∈S be the corresponding to W braid group. For s ∈ S
deﬁne the graded R-bimodule Bs = R ⊗Rs R, where Rs is the ring of polynomials invariant under s.
Graduation on Bs is induced by the graduation on R. To the braid generator σs (resp. σ −1
s ) Rouquier
associates cochain complexes of graded R-bimodules:
F (σs) : 0 → Bs
m
→ R → 0 resp. F (σ −1
s ) : 0 → R
η
→ Bs(1) → 0
where Bs(1) means the shift in the graduation by 1, m(a ⊗ b) = ab and η(a) = a ⊗ xs + axs ⊗ 1. Bimodules
Bs and Bs(1) are placed in cohomological degree 0. Rouquier [4, 9.] proves the following
Theorem 1 (Rouquier) Map σ ±1
s → F (σ ±1
s ) ⊗R − induces a well-deﬁned action of the braid group BW
on the category of cochain complexes of graded R-bimodules up to homotopy.
The above theorem allows to deﬁne the Rouquier complex F (σ ) of σ ∈ BW as the image of the complex
0 → R → 0 by the action of σ .
Recall that the Hochschild homology HH(R, M ) of an R-bimodule M is deﬁned as the direct sum of
TorR⊗R
i (R, M ). For σ ∈ BW Khovanov takes the Hochschild homology of each term in the Rouquie r
complex F (σ ) and gets a complex of bigraded spaces
. . .
HH(∂ )
− − − − →HH(R, F j(σ ))
HH(∂ )
− − − − →HH(R, F j+1(σ ))
HH(∂ )
− − − − →. . .
The homology of the above complex is called Khovanov-Rozansky homology. When W is the symmetric
group Khovanov proves the following
1
Theorem 2 (Khovanov) The triple-graded dimension of Khovanov-Rozansky homolog y is an invariant
of oriented links. Its bigraded Euler characteristic provi des the HOMFLY 2-variable polynomial.
Let HW := C(q)BW / ⟨(σs − q)(σs + 1)⟩ be the Hecke algebra of W . We will explain how the Euler
characteristic of Khovanov-Rozansky homology provides a trace function on HW . For σ ∈ BW deﬁne an
element ⟨σ ⟩V ∈ C(q, t ) as
⟨σ ⟩V =
( 1 − q
1 + tq
) n
·
∑
i,j,k
(−1)i dimC HHj(R, F i(σ ))k · qk · tj,
where the index i corresponds to the cohomological grading of the Rouquier complex , j - to the Hochschild
homology grading and k - to the polynomial grading of R-modules HH j(R, F i(σ )). By linearity we get a
C(q)-linear map ⟨·⟩V : C(q)BW → C(q, t ). The following proposition is well-known (see e.g. [3, (4.4.6)]):
Proposition 1 The map ⟨·⟩V has the following properties:
• ⟨ 1⟩V = 1 (Normalizing property)
• ⟨ ab⟩V = ⟨ba⟩V for any a, b ∈ C(q)BW (Trace property)
• For any a ∈ C(q)BW and s ∈ S we have ⟨aσs⟩V = q
⟨
aσ −1
s
⟩
V + (q − 1) ⟨a⟩V (Hecke property)
This proposition implies that the map ⟨·⟩V can be factorized through the Hecke algebra HW . It induces
a trace τkr on HW called Khovanov-Rozansky trace.
Let Ts be the image of σs in HW . Recall, that Gomi deﬁnes a Markov trace with a parameter
z ∈ C(q, t ) on HW as a C(q)-linear function τ with the properties
• τ(1) = 1, τ(ab) = τ(ba) for any a, b ∈ H W
• τ(hTs) = zτ(h) for any s ∈ S and any h from the parabolic subalgebra HW,S \{s} of HW generated
by the set {Ts′ }s′∈S\{s}. This property is called Markov property.
The result of this article is the following theorem:
Theorem 3 The trace τkr is a Markov trace with the parameter z = tq(q−1)
tq+1 .
Proof. The idea of the proof is based on the proof of [2, Th. 1] where Koszu l complexes are used. Let
e1, · · · , e n be any basis of the vector space V . We denote the dual e∗
i by xi ∈ R. We will use the following
notations:
Rn
x := C[x1, . . . , x n], R n
y := C[y1, . . . , y n], R n
z := C[z1, . . . , z n], R n
x,y,z := Rn
x ⊗C Rn
y ⊗C Rn
z ,
Rn
x,y := Rn
x ⊗C Rn
y , R n
x,z := Rn
x ⊗C Rn
z , R n
y,z := Rn
y ⊗C Rn
z .
The action of W on Rn
y , R n
z is exactly the same as on R = Rn
x and is directly induced on
Rn
x,y , R n
x,z , R n
y,z , R n
x,y,z .
Let A be a graded ring and a1, . . . a k some homogeneous elements in A. We denote by ( a1, . . . , a k)A
the corresponding Koszul complex which is deﬁned as the tensor product over A of small complexes
0 → A(− deg ai)
×ai
− →A → 0, where ×ai means the multiplication by ai.
2
F act 1 Let (a1, . . . , a k)A be a Koszul complex and λ ∈ A be an element such that λa i is homogeneous of
the same degree as aj for some i ⁄= j. Then we have the following isomorphism of complexes:
(a1, . . . , a i, . . . , a j . . . , a k)A ≃ (a1, . . . , a i, . . . , a j + λa i . . . , a k)A.
F act 2 Let A, B be some C-algebras, K • some complex of A ⊗C B-modules and L• a complex of A-
modules. Then there is the obvious isomorphism of complexes K • ⊗A L• ≃ K • ⊗A⊗B (L• ⊗C B).
Proposition 1, the deﬁnition and the C(q)-linearity of τkr imply that in order to prove the theorem it is
enough to show that ⟨bσ s⟩V = z⟨b⟩V for any s ∈ S and b being a product of some generators σt, t ⁄= s of
the braid group BW .
For a bigraded space M with ﬁnite-dimensional homogeneous components we denote its bigr aded
dimension by dimgr q,t M . For a ﬁnitely generated graded R-bimodule N we denote by ♠q,t (N ) the
bigraded dimension of its Hochschild homology dimgr q,t HH(R, N ) = ∑
j,k dimC HHj(R, N )k · qk · tj.
Recall that by deﬁnition
( 1 + tq
1 − q
) n
⟨bσ s⟩V =
∑
i
(−1)i♠q,t (F i(bσ s)) =
∑
i
(−1)i♠q,t (F i(b) ⊗R Bs) −
∑
i
(−1)i♠q,t (F i(b))
( 1 + tq
1 − q
) n
z⟨b⟩V = tq(q − 1)
tq + 1
∑
i
(−1)i♠q,t (F i(b)).
Thus it is enough to prove the following equality: ( tq + 1)♠q,t (Θ b ⊗R Bs) = ( tq2 + 1)♠q,t (Θ b),
where the bimodule Θ b is a tensor product over R of some Bt’s (t ⁄= s) since every F i(b) is a direct sum
of such bimodules.
Let us look at our vector space V . Since dim C V = n > n − 1 = |S \ {s}| there exists a vector v ∈ V ∗
invariant under the action of any s′ ∈ S, s ′ ⁄= s. We can assume that v = xn and x1, . . . , x n−1 ∈ V s.
Let ux = xn − wx (wx ∈ V ∗s) be an element of V ∗ dual to the root of s (vectors uy = yn − wy and
uz = zn − wz will be the corresponding copies of ux in Rn
y and Rn
z ).
Lemma 1 There is an isomorphism of Rn
x,y -modules Θ b ≃ Θ ′
b ⊗C C[xn], where Θ ′
b is some Rn−1
x,y -module,
yn acts on C[xn] by multiplication by xn.
Proof. Easy consequence from the fact that Θ b is a tensor product of some Bt’s. □
Proposition 2 Let ~Θ ′
b be a free Rn−1
x,y -resolution of Θ ′
b. Then the following complex Kb,s is a free Rn
x,y,z -
resolution of Θ b ⊗Rn
y Bs:
(
~Θ ′
b ⊗C C[xn, y n] ⊗C Rn
z
)
⊗Rnx,y,z (xn − yn, y 1 − z1, . . . , y n−1 − zn−1, u 2
y − u2
z)Rnx,y,z .
Proof. Indeed, the above complex is isomorphic to
[(
~Θ ′
b ⊗C C[xn, y n]
)
⊗Rnx,y (xn − yn)Rnx,y
]
⊗Rnx,y (y1 − z1, . . . , y n−1 − zn−1, u 2
y − u2
z)Rnx,y,z
≃
[
~Θ ′
b ⊗Rn−1
x,y
(xn − yn)Rnx,y
]
⊗Rny (y1 − z1, . . . , y n−1 − zn−1, u 2
y − u2
z)Rny,z
Since the complex ~Θ ′
b⊗Rn−1
x,y
(xn −yn)Rnx,yis isomorphic to ~Θ ′
b⊗C(xn −yn)C[xn,y n], it is a free Rn
x,y -resolution
of Θ b. At the same time the complex ( y1 − z1, . . . , y n−1 − zn−1, u 2
y − u2
z)Rn
y,z considered as a complex
3
of Rn
y -modules is homotopy equivalent to the free Rn
y -module Bs. This proves that their tensor product
over Rn
y is a free Rn
x,y,z -resolution of Θ b ⊗Rny Bs. □
In order to calculate HH( R, Θ b ⊗R Bs) we take the tensor product over Rn
x,z of Kb,s and the free Rn
x,z -
resolution of R represented by the Koszul complex ( x1 − z1, . . . , x n − zn)Rnx,z . This tensor product equals
Kb,s ⊗Rnx,y,z (x1 − z1, . . . , x n − zn)Rnx,y,z, which, in its turn, is equal to
(
~Θ ′
b ⊗C C[xn, y n] ⊗C Rn
z
)
⊗Rn
x,y,z (xn − yn, y 1 − z1, . . . , y n−1 − zn−1, u 2
y − u2
z, x 1 − z1, . . . , x n − zn)Rn
x,y,z
≃
(
~Θ ′
b ⊗C C[xn, y n] ⊗C Rn
z
)
⊗Rnx,y,z (xn − yn, y 1 − z1, . . . , y n−1 − zn−1, 0, x 1 − z1, . . . , x n − zn)Rnx,y,z,
where the element u2
y − u2
z = (yn − zn − wy + wz)(yn + zn − wy − wz) of homogeneous degree 2 was ”killed”
by elements xn − yn, x n − zn, y 1 − z1, . . . , y n−1 − zn−1. Denoting the homology of the complex
(
~Θ ′
b ⊗C C[xn, y n] ⊗C Rn
z
)
⊗Rnx,y,z (xn − yn, y 1 − z1, . . . , y n−1 − zn−1, x 1 − z1, . . . , x n − zn)Rnx,y,z
by H •
b,s (which is double-graded) we have ♠q,t (Θ b ⊗R Bs) = (1 + tq2)dimgrq,t H•
b,s .
The proof that ♠q,t (Θ b) = (1 + tq)dimgrq,t H•
b,s is completely analogous. First we make a formal note
that the complex Lb,s :
(
~Θ ′
b ⊗C C[xn, y n] ⊗C Rn
z
)
⊗Rnx,y,z (xn − yn, y 1 − z1, . . . , y n−1 − zn−1, y n − zn)Rnx,y,z
is a free Rn
x,y,z -resolution of Θ b. Then we take the tensor product over Rn
x,z of Lb,s and the Koszul
complex ( x1 − z1, . . . , x n − zn)Rnx,z. And we get
(
~Θ ′
b ⊗C C[xn, y n] ⊗C Rn
z
)
⊗Rnx,y,z (xn − yn, y 1 − z1, . . . , y n−1 − zn−1, y n − zn, x 1 − z1, . . . , x n − zn)Rnx,y,z
≃
(
~Θ ′
b ⊗C C[xn, y n] ⊗C Rn
z
)
⊗Rnx,y,z (xn − yn, y 1 − z1, . . . , y n−1 − zn−1, 0, x 1 − z1, . . . , x n − zn)Rnx,y,z,
where the element yn − zn of homogeneous degree 1 was ”killed” by elements xn − yn and xn − zn. This
ends the proof. □
Remark 1 Rapha¨ el Rouquier told me in private communication that he h as a ”categoriﬁed” version of
theorem 3 which will be published later.
