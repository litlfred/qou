---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-012-42-integrals
section_title: "Integrals"
section_number: 4.2
pages: 15-16
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
generalization of that of an integral in a usual Hopf algebra [M].
Deﬁnition 4.7 ([BNSz]). A left integral in A is an element ℓ ∈A such that
(13) hℓ =εt(h)ℓ, (rh =rεs(h)) for all h ∈A.
The space of left integrals in A is a left ideal of A of dimension equal to dimk(At).
Any left integral λ inA∗ satisﬁes the following invariance property :
(14) g(1)λ(hg(2)) = S(h(1))λ(h(2)g), g,h ∈A.
In what follows we use the Sweedler arrows ⇀ and ↼ for the dual actions :
(15) h⇀φ (g) = φ(gh) and φ↼h (g) = φ(hg).
for all g, h∈A,φ ∈A∗.
Recall that a functional φ ∈ A∗ is non-degenerate if φ ◦m is a non-degenerate
bilinear form on A. Equivalently,φ is non-degenerate if the linear map h ↦→(h⇀φ )
is injective. An integral (left or right) in a weak Hopf algebra A is called non-
degenerate if it deﬁnes a non-degenerate functional on A∗. A left integral ℓ is called
normalized if εt(ℓ) = 1.
16 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
It was shown by P. Vecsernyes [V] that a ﬁnite dimensional weak Hop f algebra
always possesses a non-degenerate left integral. In particular, a ﬁnite dimensional
weak Hopf algebra is a Frobenius algebra (this extends the well-know n result of
Larson and Sweedler for usual Hopf algebras).
Maschke’s theorem for weak Hopf algebras, proved in [BNSz, 3.13], s tates that
a weak Hopf algebra A is semisimple if and only if A is separable, and if and only
if there exists a normalized left integral in A. In particular, every semisimple weak
Hopf algebra is ﬁnite dimensional.
For a ﬁnite dimensional A there is a useful notion of duality between non-
degenerate left integrals in A and A∗ [BNSz, 3.18]. If ℓ is a non-degenerate left
integral in A then there exists a unique λ ∈ A∗ such that λ ⇀ ℓ= 1. This λ
is a non-degenerate left integral in A∗. Moreover, ℓ ⇀ λ = ǫ. Such a pair of
non-degenerate integrals (ℓ, λ) is called a pair of dual integrals.
An invertible elementg ∈A is called group-like if ∆( g) = (g ⊗g)∆(1) = ∆(1)( g ⊗
g) [N, Deﬁnition 4.1]. Group-like elements of A form a group G(A) under multipli-
cation. This group has a normal subgroup G0(A) := G(Amin) of trivial group-like
elements. If A is ﬁnite dimensional, the quotient group ~G(A) = G(A)/G0(A) is
ﬁnite. It was shown in [N] that if A is ﬁnite dimensional and ℓ ∈ A and λ ∈ A∗
is a dual pair of left integrals, then there exist group-like elements α ∈G(A∗) and
a ∈ G(A), called distinguished group-like elements, whose classes in ~G(A∗) and
~G(A) do not depend on the choice of ℓ and λ, such that
(16) S(ℓ) = α⇀ℓ and S(λ) = a⇀λ.
(Note that α and a themselves depend on the choice of ℓ and λ).
The following result is crucial for this paper. It is an analogue of Radf ord’s
formula for usual Hopf algebras.
Theorem 4.8. [N, Theorem 5.13] One has
(17) S4(h) = a−1(α⇀h↼α −1)a.
for all h ∈A.
A weak Hopf algebra A is said to be unimodular if it contains a non-degenerate
2-sided integral; equivalently, A is unimodular if the coset of α in G(A∗) is trivial.
A semisimple weak Hopf algebra is automatically unimodular [BNSz].
