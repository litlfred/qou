---
doc_id: arxiv-math-0203003v2
doc_title: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in represe"
section_id: sec-001-1-representations-of-quantum-dynamical-r-matrice
section_title: "Representations of Quantum Dynamical R-Matrices with Spe c-"
section_number: 1
pages: 2-4
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
doc_brief: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in representation the ory in t"
---
tral Parameters
Let a be a ﬁnite dimensional abelian Lie algebra over C, V be a ﬁnite dimensional semisimple
a-module, and γ ∈ C∗. The quantum dynamical Yang-Baxter equation with spectral parameter
and step γ is
R12(u1 −u2,λ −γh(3))R13(u1 −u3,λ )R23(u2 −u3,λ −γh(1))
=R23(u2 −u3,λ )R13(u1 −u3,λ −γh(2))R12(u1 −u2,λ ) (1.1)
with respect to a meromorphic function R : C × a∗ → Enda(V ⊗V ). The notation h(i) means that,
for example, R12(u1 −u2,λ −γh(3))(v1 ⊗v2 ⊗v3) =
(
R(u1 −u2,λ −γµ )(v1 ⊗v2)
)
⊗v3 if v3 has
weight µ . A function R is called a quantum dynamical R-matrix if it is a generically invertible
solution of (1.1).
Given a quantum dynamical R-matrix R : C × a∗ → Enda(V ⊗V ), we denote by Repf(R) the
category of meromorphic ﬁnite dimensional representation s of R. This category was ﬁrst deﬁned in
[Fe94a, Fe94b]. It consists of pairs ( W,L W ) where W is a semisimple ﬁnite dimensional a-module
and LW is a meromorphic function
LW : C × a∗ → Enda(V ⊗W )
2
such that LW (u,λ ) is (generically) invertible and satisﬁes
R12(u1 −u2,λ −γh(3))L13
W (u1 −u3,λ )L23
W (u2 −u3,λ −γh(1))
=L23
W (u2 −u3,λ )L13
W (u1 −u3,λ −γh(2))R12(u1 −u2,λ ) (1.2)
in End a(V ⊗V ⊗W ). If ( W,L W ) and (U,L U ) are two representations, a morphism between them
is a meromorphic function f : a∗ → Homa(W,U ) such that
(
1 ⊗f (λ)
)
LW (u,λ ) = LU (u,λ )
(
1 ⊗f (λ −γh(1))
)
(1.3)
Thus, the category Repf(R) is linear over the ﬁeld MV of meromorphic functions on a∗ periodic
under the lattice spanned by the weights of V .
Example 1.1. Let R : C × a∗ → Enda(V ⊗V ) be a quantum dynamical R-matrix.
1. Let W be any vector space and let a act trivially on W . Then ( W, 1), where 1 denotes the
constant function 1 ∈ Enda(V ⊗W ), is a representation of R called the trivial representation
associated to W .
2. (V,R ) is a representation of R called the basic representation.
3. If ( W,L W ) is a representation of R, f : a∗ → Enda(W ) is generically invertible and Lf
W =(
1 ⊗f (λ)−1)
LW (u,λ )
(
1 ⊗f (λ −γh(1))
)
then (W,L f
W ) is also a representation. It is clear that
f provides an isomorphism from ( W,L f
W ) to (W,L W ).
Example 1.2. Let a be an abelian n-dimensional Lie algebra and V be a semisimple n-dimensional
a-module whose weights form a basis for a∗ (in other words, a is the usual Cartan subalgebra of
gln acting naturally on V = Cn). Quantum dynamical R-matrices for such a and V are said to be
of gln type [EV98, EV99]. They have the form
R(u,λ ) =
∑
m,l
α m,l (u,λ )Em,m ⊗El,l +
∑
m⁄=l
βm,l (u,λ )El,m ⊗Em,l
The main example is the elliptic quantum dynamical R-matrix found by Felder [Fe94a, Fe94b]
Rell
τ,γ (u,λ ) =
∑
m
Em,m ⊗Em,m +
∑
m⁄=l
α (u,λ m,l )Em,m ⊗El,l +β (u,λ m,l )El,m ⊗Em,l
with
α (u,λ ) = ϑ 1(λ +γ;τ)
ϑ 1(λ;τ)
ϑ 1(u;τ)
ϑ 1(u −γ;τ) β (u,λ ) = ϑ 1(γ;τ)
ϑ 1(λ;τ)
ϑ 1(u −λ;τ)
ϑ 1(u −γ;τ)
whereλ m,l =λ m −λ l, and ϑ 1 is the standard ﬁrst theta function. Felder also proposed to associate
toRell
τ,γ an elliptic quantum group Eτ,γ/ 2(gln), whose category of ﬁnite dimensional representations
is Repf(Rell
τ,γ ).
LetR : C × a∗ → Enda(V ⊗V ) be a quantum dynamical R-matrix. The category Repf(R) can
be endowed with a tensor product functor given by ( W,L W ) ⊙ (U,L U ) = (W ⊗U,L W ⊙U ) where
LW ⊙U (u,λ ) = L12
W (u,λ −γh(3))L13
U (u,λ )
on objects and
f ⊙g(λ) = f (λ −γh(2)) ⊗g(λ)
on morphisms. One easily checks that the ﬁrst formula deﬁnes a representation, and the second one
a morphism of representations. Thus, ⊙ is a bifunctor. Moreover, it is easy to see that it deﬁnes a
structure of a tensor category on Repf(R), with unit object being the trivial representation ( C, 1).
3
