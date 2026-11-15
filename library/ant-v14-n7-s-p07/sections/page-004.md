---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over finite fields"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
toc_source: undetermined
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 16 sections: Page 1; Page 2; Page 3"
---
1898
Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
is nonvanishing mod 2 at s = 1
2. For the similar Theorem 1.7, the ℓis again the order of the Dirichlet
character in question.
2. Main theorem and proof
2A. Setup and notations. Throughout the paper, Fq is a ﬁnite ﬁeld of odd characteristic p. Let Qn,q be
the set of squarefree polynomials over Fq of degree n. For each f ∈Qn,q, write J f for the Jacobian of
the hyperelliptic curve
y2 = f (x)
and Pf (x) ∈Z[x] for the characteristic polynomial of geometric Frobenius acting on the ℓ-adic Tate
module of J f . Let ℓbe a prime not equal to the characteristic of Fq and let a be an element of (Z/ℓZ)∗.
The elements R of J f [ℓ](Fq) which satisfy
Frobq ·R = aR
form a ﬁnite-dimensional vector space over Z/ℓZ and we denote by ma( f ) the number of nonzero
elements of this vector space. Note that m1( f ) is just the number of Fq-rational nontrivial ℓ-torsion points
of J f . Let Qa,ℓ
n,q be the set of squarefree polynomials f over Fq of degree n such that ma( f ) is greater
than 0.
Let α be a q-Weil number of weight 1 with minimal polynomial gα(x) ∈Z[x]. Namely, it is an
algebraic integer whose absolute values under all complex embeddings equal √q. Let Qα
n,q be the subset
of Qn,q deﬁned by { f ∈Qn,q | Pf (α−1) = 0}. With notation introduced as above, if gα(a) = 0 mod ℓ,
then |Qα
n,q| ≤|Qa,ℓ
n,q|.
2B. Rational points on twisted Hurwitz spaces over ﬁnite ﬁelds. Our main tool will be the following
result about the average size of the subspace of Jac(C)[ℓ](Fq) on which Frobenius acts by some speciﬁed
scalar a, as C ranges over hyperelliptic curves over Fq. More precisely, we study the variation as we range
over y2 = f (x) with f ranging over squarefree polynomials in Fq[x]; this amounts to the same, since each
isomorphism class of hyperelliptic curves is represented in this form the same number of times (assuming,
of course, that the isomorphism classes are weighted inversely to the number of automorphisms they
possess.)
Proposition 2.1. Let a ∈(Z/ℓZ)×. With notation as in Section 2A, there exist constants Cℓ, Nℓ, Qℓonly
depending on ℓsuch that

P
f ∈Qn,q ma( f )
|Qn,q|
−1
 ≤Cℓq−1/2
for all n ≥Nℓand q ≥Qℓ.
Remark 2.2. While this paper was in proof, we learned that Proposition 2.1 follows from the proof of
Theorem 1.1 of [Lipnowski and Tsimerman 2019], which is in fact more general, and the arguments used
are essentially the same as those here. We have left the proof of Proposition 2.1 in the present paper
