---
doc_id: arxiv-1202.5547v1
doc_title: "Markov property and Khovanov-Rozansky homology: Coxeter Case"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 1202.5547v1 (1).pdf
source_sha256: 1268c0834b6c9206
toc_source: inferred
doc_brief: "Markov property and Khovanov-Rozansky homology: Coxeter Case — In [2] Khovanov gave a construction of Khovanov-Rozansky homology, new triple-graded link invariant, taking the Hochschild homology of"
---
arXiv:1202.5547v1  [math.RT]  24 Feb 2012
Markov property and Khovanov-Rozansky homology: Coxeter
Case.
Traﬁm LASY
July 8, 2018
Abstract
In [2] Khovanov gave a construction of Khovanov-Rozansky homology, new triple-graded link
invariant, taking the Hochschild homology of the terms in Rouquier complexes. Its bigraded Euler
characteristic provides the Markov trace of type An, which, in its turn, induces the well-known
HOMFLY polynomial. Gomi [1, (3.3)] has extended the deﬁnition of Markov trace on a Hecke algebra
to all Coxeter groups. One can see that Khovanov’s and Rouquier’s constructions can be directly
extended to these groups.
We give a detailed proof that the corresponding Euler characteristic
provides a Markov trace in the sense of Gomi for any Coxeter group.
Let (W, S) be a Coxeter system with |S| = n < ∞. Let V be the C-vector space with the basis {es}s∈S
carrying the geometric representation of W. Then we have a natural action of W on the symmetric
algebra R = S(V ∗), which will be regarded as the graded polynomial ring C[{xs}s∈S] with deg xs = 1.
Now we brieﬂy recall the notions of Rouquier complexes needed to give Khovanov’s construction of
Khovanov-Rozansky homology. Let BW = ⟨σs⟩s∈S be the corresponding to W braid group. For s ∈S
deﬁne the graded R-bimodule Bs = R ⊗Rs R, where Rs is the ring of polynomials invariant under s.
Graduation on Bs is induced by the graduation on R. To the braid generator σs (resp. σ−1
s ) Rouquier
associates cochain complexes of graded R-bimodules:
F(σs) : 0 →Bs
m
→R →0
resp.
F(σ−1
s ) : 0 →R
η→Bs(1) →0
where Bs(1) means the shift in the graduation by 1, m(a⊗b) = ab and η(a) = a⊗xs+axs ⊗1. Bimodules
Bs and Bs(1) are placed in cohomological degree 0. Rouquier [4, 9.] proves the following
Theorem 1 (Rouquier) Map σ±1
s
→F(σ±1
s )⊗R −induces a well-deﬁned action of the braid group BW
on the category of cochain complexes of graded R-bimodules up to homotopy.
The above theorem allows to deﬁne the Rouquier complex F(σ) of σ ∈BW as the image of the complex
0 →R →0 by the action of σ.
Recall that the Hochschild homology HH(R, M) of an R-bimodule M is deﬁned as the direct sum of
TorR⊗R
i
(R, M). For σ ∈BW Khovanov takes the Hochschild homology of each term in the Rouquier
complex F(σ) and gets a complex of bigraded spaces
. . .
HH(∂)
−−−−→HH(R, F j(σ))
HH(∂)
−−−−→HH(R, F j+1(σ))
HH(∂)
−−−−→. . .
The homology of the above complex is called Khovanov-Rozansky homology. When W is the symmetric
group Khovanov proves the following
1
Theorem 2 (Khovanov) The triple-graded dimension of Khovanov-Rozansky homology is an invariant
of oriented links. Its bigraded Euler characteristic provides the HOMFLY 2-variable polynomial.
Let HW := C(q)BW / ⟨(σs −q)(σs + 1)⟩be the Hecke algebra of W.
We will explain how the Euler
characteristic of Khovanov-Rozansky homology provides a trace function on HW . For σ ∈BW deﬁne an
element ⟨σ⟩V ∈C(q, t) as
⟨σ⟩V =
 1 −q
1 + tq
n
·
X
i,j,k
(−1)i dimC HHj(R, F i(σ))k · qk · tj,
where the index i corresponds to the cohomological grading of the Rouquier complex, j - to the Hochschild
homology grading and k - to the polynomial grading of R-modules HHj(R, F i(σ)). By linearity we get a
C(q)-linear map ⟨·⟩V : C(q)BW →C(q, t). The following proposition is well-known (see e.g. [3, (4.4.6)]):
Proposition 1 The map ⟨·⟩V has the following properties:
• ⟨1⟩V = 1 (Normalizing property)
• ⟨ab⟩V = ⟨ba⟩V for any a, b ∈C(q)BW (Trace property)
• For any a ∈C(q)BW and s ∈S we have ⟨aσs⟩V = q

aσ−1
s

V + (q −1) ⟨a⟩V (Hecke property)
This proposition implies that the map ⟨·⟩V can be factorized through the Hecke algebra HW . It induces
a trace τkr on HW called Khovanov-Rozansky trace.
Let Ts be the image of σs in HW .
Recall, that Gomi deﬁnes a Markov trace with a parameter
z ∈C(q, t) on HW as a C(q)-linear function τ with the properties
• τ(1) = 1, τ(ab) = τ(ba) for any a, b ∈HW
• τ(hTs) = zτ(h) for any s ∈S and any h from the parabolic subalgebra HW,S\{s} of HW generated
by the set {Ts′}s′∈S\{s}. This property is called Markov property.
The result of this article is the following theorem:
Theorem 3 The trace τkr is a Markov trace with the parameter z = tq(q−1)
tq+1 .
Proof. The idea of the proof is based on the proof of [2, Th. 1] where Koszul complexes are used. Let
e1, · · · , en be any basis of the vector space V . We denote the dual e∗
i by xi ∈R. We will use the following
notations:
Rn
x := C[x1, . . . , xn],
Rn
y := C[y1, . . . , yn],
Rn
z := C[z1, . . . , zn],
Rn
x,y,z := Rn
x ⊗C Rn
y ⊗C Rn
z ,
Rn
x,y := Rn
x ⊗C Rn
y,
Rn
x,z := Rn
x ⊗C Rn
z ,
Rn
y,z := Rn
y ⊗C Rn
z .
The action of W
on Rn
y, Rn
z
is exactly the same as on R
=
Rn
x and is directly induced on
Rn
x,y, Rn
x,z, Rn
y,z, Rn
x,y,z.
Let A be a graded ring and a1, . . . ak some homogeneous elements in A. We denote by (a1, . . . , ak)A
the corresponding Koszul complex which is deﬁned as the tensor product over A of small complexes
0 →A(−deg ai)
×ai
−→A →0,
where ×ai means the multiplication by ai.
2
Fact 1 Let (a1, . . . , ak)A be a Koszul complex and λ ∈A be an element such that λai is homogeneous of
the same degree as aj for some i̸ = j. Then we have the following isomorphism of complexes:
(a1, . . . , ai, . . . , aj . . . , ak)A ≃(a1, . . . , ai, . . . , aj + λai . . . , ak)A.
Fact 2 Let A, B be some C-algebras, K• some complex of A ⊗C B-modules and L• a complex of A-
modules. Then there is the obvious isomorphism of complexes K• ⊗A L• ≃K• ⊗A⊗B (L• ⊗C B).
Proposition 1, the deﬁnition and the C(q)-linearity of τkr imply that in order to prove the theorem it is
enough to show that ⟨bσs⟩V = z⟨b⟩V for any s ∈S and b being a product of some generators σt, t̸ = s of
the braid group BW .
For a bigraded space M with ﬁnite-dimensional homogeneous components we denote its bigraded
dimension by dimgrq,tM.
For a ﬁnitely generated graded R-bimodule N we denote by ♠q,t(N) the
bigraded dimension of its Hochschild homology dimgrq,tHH(R, N) = P
j,k dimC HHj(R, N)k · qk · tj.
Recall that by deﬁnition
1 + tq
1 −q
n
⟨bσs⟩V =
X
i
(−1)i♠q,t(F i(bσs)) =
X
i
(−1)i♠q,t(F i(b) ⊗R Bs) −
X
i
(−1)i♠q,t(F i(b))
1 + tq
1 −q
n
z⟨b⟩V = tq(q −1)
tq + 1
X
i
(−1)i♠q,t(F i(b)).
Thus it is enough to prove the following equality: (tq + 1)♠q,t(Θb ⊗R Bs) = (tq2 + 1)♠q,t(Θb),
where the bimodule Θb is a tensor product over R of some Bt’s (t̸ = s) since every F i(b) is a direct sum
of such bimodules.
Let us look at our vector space V . Since dimC V = n > n −1 = |S \ {s}| there exists a vector v ∈V ∗
invariant under the action of any s′ ∈S, s′̸ = s. We can assume that v = xn and x1, . . . , xn−1 ∈V s.
Let ux = xn −wx (wx ∈V ∗s) be an element of V ∗dual to the root of s (vectors uy = yn −wy and
uz = zn −wz will be the corresponding copies of ux in Rn
y and Rn
z ).
Lemma 1 There is an isomorphism of Rn
x,y-modules Θb ≃Θ′
b ⊗C C[xn], where Θ′
b is some Rn−1
x,y -module,
yn acts on C[xn] by multiplication by xn.
Proof. Easy consequence from the fact that Θb is a tensor product of some Bt’s. □
Proposition 2 Let f
Θ′
b be a free Rn−1
x,y -resolution of Θ′
b. Then the following complex Kb,s is a free Rn
x,y,z-
resolution of Θb ⊗Rn
y Bs:

f
Θ′
b ⊗C C[xn, yn] ⊗C Rn
z

⊗Rn
x,y,z (xn −yn, y1 −z1, . . . , yn−1 −zn−1, u2
y −u2
z)Rn
x,y,z.
Proof. Indeed, the above complex is isomorphic to
h
f
Θ′
b ⊗C C[xn, yn]

⊗Rn
x,y (xn −yn)Rn
x,y
i
⊗Rn
x,y (y1 −z1, . . . , yn−1 −zn−1, u2
y −u2
z)Rn
x,y,z
≃
h
f
Θ′
b ⊗Rn−1
x,y (xn −yn)Rn
x,y
i
⊗Rn
y (y1 −z1, . . . , yn−1 −zn−1, u2
y −u2
z)Rn
y,z
Since the complex f
Θ′
b⊗Rn−1
x,y (xn−yn)Rn
x,yis isomorphic to f
Θ′
b⊗C(xn−yn)C[xn,yn], it is a free Rn
x,y-resolution
of Θb. At the same time the complex (y1 −z1, . . . , yn−1 −zn−1, u2
y −u2
z)Rn
y,z considered as a complex
3
of Rn
y-modules is homotopy equivalent to the free Rn
y-module Bs. This proves that their tensor product
over Rn
y is a free Rn
x,y,z-resolution of Θb ⊗Rn
y Bs. □
In order to calculate HH(R, Θb ⊗R Bs) we take the tensor product over Rn
x,z of Kb,s and the free Rn
x,z-
resolution of R represented by the Koszul complex (x1 −z1, . . . , xn −zn)Rn
x,z. This tensor product equals
Kb,s ⊗Rn
x,y,z (x1 −z1, . . . , xn −zn)Rn
x,y,z,
which, in its turn, is equal to

f
Θ′
b ⊗C C[xn, yn] ⊗C Rn
z

⊗Rn
x,y,z (xn −yn, y1 −z1, . . . , yn−1 −zn−1, u2
y −u2
z, x1 −z1, . . . , xn −zn)Rn
x,y,z
≃

f
Θ′
b ⊗C C[xn, yn] ⊗C Rn
z

⊗Rn
x,y,z (xn −yn, y1 −z1, . . . , yn−1 −zn−1, 0, x1 −z1, . . . , xn −zn)Rn
x,y,z,
where the element u2
y −u2
z = (yn −zn −wy +wz)(yn +zn −wy −wz) of homogeneous degree 2 was ”killed”
by elements xn −yn, xn −zn, y1 −z1, . . . , yn−1 −zn−1. Denoting the homology of the complex

f
Θ′
b ⊗C C[xn, yn] ⊗C Rn
z

⊗Rn
x,y,z (xn −yn, y1 −z1, . . . , yn−1 −zn−1, x1 −z1, . . . , xn −zn)Rn
x,y,z
by H•
b,s (which is double-graded) we have ♠q,t(Θb ⊗R Bs) = (1 + tq2)dimgrq,tH•
b,s.
The proof that ♠q,t(Θb) = (1 + tq)dimgrq,tH•
b,s is completely analogous. First we make a formal note
that the complex Lb,s:

f
Θ′
b ⊗C C[xn, yn] ⊗C Rn
z

⊗Rn
x,y,z (xn −yn, y1 −z1, . . . , yn−1 −zn−1, yn −zn)Rn
x,y,z
is a free Rn
x,y,z-resolution of Θb. Then we take the tensor product over Rn
x,z of Lb,s and the Koszul
complex (x1 −z1, . . . , xn −zn)Rn
x,z. And we get

f
Θ′
b ⊗C C[xn, yn] ⊗C Rn
z

⊗Rn
x,y,z (xn −yn, y1 −z1, . . . , yn−1 −zn−1, yn −zn, x1 −z1, . . . , xn −zn)Rn
x,y,z
≃

f
Θ′
b ⊗C C[xn, yn] ⊗C Rn
z

⊗Rn
x,y,z (xn −yn, y1 −z1, . . . , yn−1 −zn−1, 0, x1 −z1, . . . , xn −zn)Rn
x,y,z,
where the element yn −zn of homogeneous degree 1 was ”killed” by elements xn −yn and xn −zn. This
ends the proof. □
Remark 1 Rapha¨el Rouquier told me in private communication that he has a ”categoriﬁed” version of
theorem 3 which will be published later.
