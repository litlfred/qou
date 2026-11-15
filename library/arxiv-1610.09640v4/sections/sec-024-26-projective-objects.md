---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-024-26-projective-objects
section_title: "Projective Objects"
section_number: 2.6
pages: 46-47
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
A splitting of an epimorphism ψ : M →M ′′ in M is a morphism α : M ′′ →M
s.t. ψ ◦α = idM ′′. A splitting of a monomorphism φ : M ′ →M is a morphism
β : M →M ′ s.t. β ◦φ = idM ′. A splitting of a short exact sequence
(2.6.1)
0 →M ′
φ−→M
ψ−→M ′′ →0
is a splitting of the epimorphism ψ, or equivalently a splitting of the monomorphism
φ. The short exact sequence is said to be split if it has some splitting.
Exercise 2.6.2. Show how to get from a splitting of φ to a splitting of ψ, and vice
versa. Show how any of those gives rise to an isomorphism M ∼= M ′ ⊕M ′′.
Deﬁnition 2.6.3. An object P ∈M is called a projective object if for every mor-
phism γ : P →N and every epimorphism ψ : M ↠N, there exists a morphism
˜γ : P →N such that ψ ◦˜γ = γ.
46
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
This is described in the following commutative diagram in M :
P
γ

˜γ
{
M
ψ
/ / N
Proposition 2.6.4. The following conditions are equivalent for P ∈M :
(i) P is projective.
(ii) The additive functor HomM(P, −) : M →Ab is exact.
(iii) Every short exact sequence (2.6.1) with M ′′ = P is split.
Proof. Exercise.
□
Deﬁnition 2.6.5. We say M has enough projectives if every M ∈M admits an
epimorphism P →M from a projective object P.
Exercise 2.6.6. Let A be a ring.
(1) Prove that an A-module P is projective iﬀit is a direct summand of a free
module; i.e. P ⊕P ′ ∼= Q for some module P ′ and free module Q.
(2) Prove that the category Mod A has enough projectives.
Exercise 2.6.7. Let M be the category of ﬁnite abelian groups. Prove that the
only projective object in M is 0. So M does not have enough projectives. (Hint:
use Proposition 2.6.4.)
Example 2.6.8. Consider the scheme X := P1
K, the projective line over a ﬁeld K,
with structure sheaf OX. The category Coh OX of coherent OX-modules is abelian
(it is a full abelian subcategory of Mod OX, cf. Example 2.3.19). One can show
that the only projective object of Coh OX is 0, but this is quite involved.
Let us only indicate why the sheaf OX is not a projective object of Coh OX.
Denote by t0, t1 the homogeneous coordinates of X. These belong to Γ(X, OX(1)),
so each determines a homomorphism of sheaves tj : OX(i) →OX(i + 1). We get a
sequence
(2.6.9)
0 →OX(−2)
[ t0 t1 ]
−−−−→OX(−1)⊕2
 −t1
t0

−−−−→OX →0
in Coh OX, which is known to be exact. It is also known that Γ(X, OX) = K and
Γ(X, OX(−1)) = 0. Therefore the sequence (2.6.9) is not split.
