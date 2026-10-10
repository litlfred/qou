---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-025-26-turning-c-categories-with-tensor-structures-int
section_title: "Turning C*-categories with tensor structures into tensor C*-categories, II"
section_number: 26
pages: 163-166
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
26. Turning C
∗
-categories with tensor structures into tensor
C
∗
-categories, II
Let A be a discrete weak quasi bialgebra with a pre-C
∗
-algebra structure and let Ω ∈
M(A⊗A) be a given partially invertible operator with domain ∆(I). We develop a criterion
that will be useful in Sect. 28, 30, 32 to verify the axioms of a positive Ω-involution.
Let ρ ∈ Reph(A) be a ∗-representation. Since the coproduct is not coassociative in
general, there are different tensor powers of ρ each given order n ≥ 3, but they are all
equivalent.
Definition 26.1. A representation ρ is called generating if ρn(a) = 0 for all n implies
a = 0, where ρn denotes the choice of an n-th tensor power of ρ.
It suffices to check the generating condition on a choice of a n-th tensor power of ρ for
each n.
Let σ and τ be f.d. ∗-preserving representations of A on Hlbert spaces. As for the case of
Ω-involutive weak-quasi bialgebras, we may define the sesquilinear form induced by Ω on
the tensor product space and consider the ρ⊗σ as a representation on this space, except we
do not know whether it is a Hilbert space ∗-representation. Let ρ be a generating Hilbert

164 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
space ∗-representation. We may consider the full subcategory Cρ of Rep(A) with objects
the various tensor powers ρn of ρ on sesquilinear spaces. This is a tensor category. We
may determine the Hermitian form of ρn with an inductive procedure, as follows. Let Ωn
be the element of A⊗n defining this form via (ξ, η) = (ξ, Ωnη)p, where (ξ, η)p denotes the
untwisted n-th tensor power of the original Hermitian form of ρ on V
⊗n
ρ
. Let ∆n : A → A⊗n
denote the homomorphism defining the A-action on the space of ρn. Writing
ρn = ρr⊗ρs, with r + s = n, r, s < n,
we have that
Ωn = Ωr ⊗ Ωs∆r ⊗ ∆s(Ω), ∆n = ∆r ⊗ ∆s ◦ ∆,
where Ω1 = I, Ω2 = Ω, ∆1 = 1, ∆2 = ∆.
Assume for a moment that Ω is an Ω-involution. Then we inductively get the following
relations, extending (11.1)–(11.3).
Ωn = Ω∗
n
, (26.1)
Ω
−1
n Ωn = ∆n(I), ΩnΩ
−1
n = ∆n(I)
∗
, (26.2)
∆n(a)
∗Ωn = Ωn∆n(a∗
), a ∈ A. (26.3)
We next go back to the original situation, then we only know that the above relations
holds under the image of ρn if we already know that ρn is a ∗-representation.
Theorem 26.2. Let A be a discrete pre-C
∗
-algebra equipped with the structure of a weak
quasi-bialgebra, and let ρ be a generating C
∗
-representation of A. Let Ω ∈ M(A ⊗ A) be
a partially invertible element with domain ∆(I) and such that for every irreducible C
∗
-
representation σ,
σ ⊗ ρ(Ω), ρ ⊗ σ(Ω), (26.4)
are positive on the full tensor product space, that σ⊗ρ and ρ⊗σ are C
∗
-representations
w.r.t. the Ω-twisted inner product and that
σ ⊗ ρ ⊗ ρ(I ⊗ Ω1 ⊗ ∆(Ω)), and ρ ⊗ ρ ⊗ σ(Ω ⊗ I∆ ⊗ 1(Ω)) (26.5)
are positive as well. Moreover, assume that the associativity morphisms
σ ⊗ ρ ⊗ ρ(Φ), ρ ⊗ ρ ⊗ σ(Φ)
are unitary with respect to the Ω-twisted inner products. Then Ω is a positive element of
M(A ⊗ A) and in this way A becomes a unitary discrete weak quasi bialgebra and Ω is
uniquely determined by the operators σ ⊗ ρ(Ω) for every irreducible σ.
Proof. It follows from the first relation in (26.4) that σ ⊗ ρ ⊗ ρ(Ω ⊗ I∆ ⊗ 1(Ω)) is positive.
It also follows that Ω ⊗ I∆ ⊗ 1(Ω) and I ⊗ Ω1 ⊗ ∆(Ω) are positive on Vρ ⊗ Vσ ⊗ Vρ
and Vρ ⊗ Vρ ⊗ Vσ. Every associativity morphism αρ
r,ρs,ρt = ρ
r ⊗ ρs ⊗ ρt
(Φ) of the full
subcategory Cρ of Rep(A) with objects parenthisized tensor powers of ρ can be written as
a composition of tensor products with identity of morphisms of the form αρ
r,ρ,ρ, αρ,ρr,ρ,
αρ,ρ,ρr . By complete reducibility of representations and naturality, our assumptions imply
unitarity of the first and the last, and the pentagon equation implies unitarity of the middle

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 165
one. It follows that the associators imply that αρ
rρsρt are unitary. We next show that every
ρn is a C
∗
-representation for the choice iteratively defined by ρn+1 = ρn⊗ρ. Assuming that
a fixed ρn is so, we decompose ρn into pairwise orthogonal irreducible components σ. Since
Vσ ⊗ Vρ is invariant under σ ⊗ ρ(Ω), ρn ⊗ ρ(Ω) is positive on Vρn ⊗ V as well, hence it is a
positive element of the C
∗
-algebra ρn(A) ⊗ ρ(A). We may thus find an element S ∈ A ⊗ A
such that ρn ⊗ ρ(S) is selfadjoint and ρn ⊗ ρ(Ω) = ρn ⊗ ρ(S)
2
. On the other hand, the
Hermitian form of ρn+1 is defined by the action of the operator ρ
⊗n+1[Ωn+1] on V⊗n+1
ρ with
Ωn+1 = Ωn ⊗ I∆n ⊗ 1(Ω). It follows that
ρ
⊗n+1[Ωn+1] = ρ⊗n
[Ωn] ⊗ Iρn ⊗ ρ(Ω) =
ρ
⊗n
[Ωn] ⊗ Iρn ⊗ ρ(S)
2 = ρ⊗n+1[Ωn ⊗ I∆n ⊗ 1(S)2
] =
ρ
⊗n+1[∆n ⊗ 1(S)∗Ωn ⊗ I∆n ⊗ 1(S)] =
ρ
⊗n+1[∆n ⊗ 1(S)]∗
ρ
⊗n
[Ωn] ⊗ Iρ⊗n+1[∆n ⊗ 1(S)]
and this is a positive operator by positivity of ρ
⊗n
[Ωn]. We consider the C
∗
-representation
τ = ⊕nρn, which is faithful as ρ is generating. We are left to show that τ ⊗τ [Ω] is a positive
operator in this representation, since it will then be a positive element of τ (A)⊗τ (A), and
therefore Ω positive in A ⊗ A. To this aim, we observe that the action of τ ⊗ τ [Ω] on the
subspace Vρr⊗Vρsis given by that of ρ
⊗n
(Ω′
n
), where n = r+s and Ω′
n = Ωr⊗Ωs∆r⊗∆s(Ω).
Thanks to unitarity of the associativity morphisms and an inductive argument we see that
ρ
⊗n
(Ω′
n
) = ρ
⊗n
(ΦnΩnΦ
∗
n
) for suitable associativity morphisms Φn. It follows that τ ⊗ τ (Ω)
is positive, hence Ω is positive in M(A ⊗ A). Therefore Cρ is a unitary tensor category
with unitary structure defined by Ω. Now the axioms of the Ω-involution on A follow.
□
The above theorem will be useful in the construction of the main examples of Sect. 32.
Remark 26.3. For example, if A is a finite dimensional C
∗
-algebra A =
L
r Mnr
(C)
and ρ is generating, every ρr⊗ρ is unitarily equivalent to an orthogonal direct sum of the
projection C
∗
-representations ρs : A → Mns(C) and their opposites ρ−s by Prop. 12.10.
By the previous theorem, verification of positivity of Ω reduces to the question of whether
the negative forms ρ−s can be ruled out for this subclass of fusion tensor products.
We conclude the section with a further discussion on C
∗
-transportability. In comparison
with Sect. 15, the following discussion gives a direct method to transport the tensor
structure from C to C
+ that will be useful in Sect. 28, 30, 32. We note however that
this method is already implicit in our main results Theorem 15.7 and 15.8. Let us assume
codition a). It is not difficult to see, using a quasi-inverse of F, that when C has a weak
dimension function there always is a faithful weak quasi-tensor functor G : C → Hilb such
that GF is a ∗-functor. Recall from Remark 12.11 that there are examples for which the
tensor structure of C is not transportable to C
+ and in these cases we have a functor G
which does not take the associativity morphisms to unitary morphisms. On the other hand,
it follows from Theorem 15.7 that when the tensor structure of C is C
∗
-transportable to
C
+ then we may find G taking the associativity morphisms to unitary morphisms. The
following proposition shows that the converse holds.

166 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Proposition 26.4. Let F : C
+ → C satisfy a) and assume that C admits a weak dimension
function. Let G : C → Hilb be a faithful functor such that G
+ = GF is a ∗
-functor and the
morphisms G(αρ,σ,τ ) are unitary. Then every weak quasi-tensor structure on G induces the
structure of a tensor C
∗
-category on C
+ s.t. F is a tensor equivalence (C∗
-transportability).
Proof. Let (F, G) be a weak quasi-tensor structure for G, thus F G = 1 and also G∗F
∗ = 1.
The functors G, G
+ correspond to the forgetful functors of a compatible triple as in Def.
15.3. We consider the corresponding weak quasi bialgebra (A, ∆, Φ) with A = Nat0(G).
The linear equivalence F : C
+ → C induces an algebra isomorphism A → A+ = Nat0(G+),
η → ηF( ). Since G
+ is a ∗
-functor, A+ is a C
∗
-algebra. By Theorem 15.7 we only need
to make A+ into a unitary weak quasi-bialgebra. We introduce the structure similarly to
the case of the Tannakian theorems 7.6, 13.5. We denote by x, y, z, . . . the irreducible
representations of A+ and define
F˜
x.y := FF(x),F(y)
: G(F(x)) ⊗ G(F(y)) → G(F(x) ⊗ F(y))
G˜
x.y := GF(x),F(y)
: G(F(x) ⊗ F(y)) → G(F(x)) ⊗ G(F(y)).
This suffices to make A+ into a weak quasi-bialgebra by
∆( ˜ ηF( ))x,y = G˜
x,yηF(x)⊗F(y)F˜
x,y,
Φ˜
x,y,z = ΦF(x),F(y),F(z) =
1 ⊗ G˜
y,z ◦ GF(x),F(y)⊗F(z) ◦ G(αF(x),F(y),F(z)) ◦ FF(x)⊗F(y),F(z) ◦ F˜x,y ⊗ 1.
We introduce an Ω-involution on A+ by Ω = F˜∗F˜, Ω−1 = G˜G˜∗. In this more general
setting the only non-trivial verification is axiom (11.5) which reduces to
G(αF(x),F(y),F(z))
∗ = G(α
−1
F(x),F(y),F(z)
)
and holds by assumption. □
