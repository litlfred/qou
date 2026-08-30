---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-017-51-explicit-equations-for-pivotal-structures
section_title: "Explicit equations for pivotal structures"
section_number: 5.1
pages: 26-27
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
In Section 3.5 we showed that, by using the pairing convention, every fusion
category over C comes equipped with a canonical monoidal endofunctorT : C→
C, the pivotal endofunctor, whose underlying functor is simply the identity, with
the pivotal operators Ti
jk supplying the coherence isomorphisms.
On the other hand, a pivotal structure on a fusion category is usually deﬁned
(see eg. [9, 2]) by making choices of right duals ( V∗,ηV,ϵV ) for every object V
as in Section 3.6, giving rise to a monoidal double dual functor ∗∗ : C→ C,
and then declaring that a pivotal structure is a monoidal natural isomorphism
γ : id⇒∗∗ . In Section 3.6 we showed that there is a canonical monoidal natural
isomorphismT ∼=∗∗. Thus, to avoid ﬁxing choices of duals, in this paper we
adopt the following cleaner deﬁnition.
Deﬁnition 5.1. A pivotal structure on a fusion category over C is a monoidal
natural isomorphism γ : id⇒T , whereT is the canonical pivotal endofunctor
of the category.
For an alternative formulation in terms of even-handed structures, see [3].
Under this deﬁnition, quantum dimensions are deﬁned as follows.
Deﬁnition 5.2. Letγ be a pivotal structure on a fusion category. The quantum
dimension of an object V with respect to γ is deﬁned as
dimγ(V ) =
where the pairing convention has been used. The pivotal structureγ is spherical
when dimγ(V ) = dimγ(V∗) for all objects V .
The following is clear.
Lemma 5.3. The quantum dimension of a simple object Xi with respect to a
pivotal structure γ computes as dimγ(Xi) = γidi wheredi is the fusion dimen-
sion of Xi.
Under these conventions, we have the following.
Theorem 5.4. A pivotal structure on fusion category C with representative
simple objects Xi, i∈I corresponds to a collection of numbers γi∈U(1), i∈I
satisfying
γjγk id =γiTi
jk whenever Xi is a summand of Xj⊗Xk (32)
where the Ti
jk are the pivotal operators of the fusion category. Moreover, the
pivotal structure is spherical precisely when γi =±1 for all i∈I.
Proof. By Lemma 3.23, γ is uniquely determined by its components γi = γXi
on the representative simple objects Xi. The coherence equation for being a
monoidal natural isomorphism reduces to the scalars γi ∈ C× obeying (32).
Given a solution to (32), the collection {±γi} forms a ﬁnite subgroup of C×
and hence γi∈ U(1). Since T 1
11 = id from Lemma 3.16, we have γ1 = 1, and
26
similarly since T 1
ii∗ = id, we have γi = γi∗ for all i∈ I. From Lemma 5.3,
if γ is spherical, then γidi∗ = γi∗di∗ whence γi = γi∗ since di∗ = di. Hence
γi =±1.
Corollary 5.5 (cf. [9, Prop 8.23]) . A pseudo-unitary fusion category admits a
canonical spherical structure.
Proof. Follows from Corollary 3.22.
Deﬁnition 5.6. We say that a fusion category C over C is orientable if the
pivotal symbols ϵi
jk,α do not depend on α, that is, Ti
jk = ϵi
jk id for some signs
ϵi
jk =±1.
Clearly we have the following.
Lemma 5.7. If a fusion category is not orientable, then it does not admit a
pivotal structure.
Recall from Theorem 4.17 that the pivotal operators can be expressed in
terms of the apex associator monodromy operators.
Proposition 5.8. If the apex associator monodromyAijk = id for all i,j,k ∈I,
then the fusion category admits a canonical spherical structure.
Proof. If Aijk = id, then from Theorem 4.17,
Ti
jk =pipjpk id
where the pi =±1 are the pivotal indicators. Hence setting γi = pi will solve
(32).
