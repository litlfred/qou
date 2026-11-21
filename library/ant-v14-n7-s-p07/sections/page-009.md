---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over finite fields"
section_id: page-009
section_title: "Page 9"
section_number: null
pages: 9-9
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
toc_source: undetermined
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 16 sections: Page 1; Page 2; Page 3"
---
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds
1903
Proof. Write δ for the quantity |Qn,q|−1|Qa,ℓ
n,q| to be bounded.
Since ma( f ) is the number of nonzero elements of a vector space over Z/ℓZ, it is at least ℓ−1 if it is
greater than 0. In particular,
|Qn,q|−1 X
f ∈Qn,q
ma( f ) ≥|Qn,q|−1(ℓ−1)|Qa,ℓ
n,q| = (ℓ−1)δ
By Proposition 2.1, we now have
(ℓ−1)δ < 1 + Cℓq−1/2
for all sufﬁciently large n, q, which yields the desired result by taking C′
ℓ= Cℓ/(ℓ−1).
□
So far, we have used the results of [Ellenberg et al. 2016] as they appear in that paper. However, for
the present application, it is useful to compute explicit values Cℓ, Qℓfor which Corollary 2.6 holds. We
do so by going back to the main body of [loc. cit.] and working out explicit bounds for quantities that are
given in [loc. cit., (7.8.1)] only as unspeciﬁed constants.
Proposition 2.7. Corollary 2.6 holds with C′
ℓ= 2(ℓ−1)−1(4ℓ)138 and Qℓ= 4 · (4ℓ)156.
Proof. By the proof of Corollary 2.6, we may take C′
ℓto be Cℓ/(ℓ−1), where Cℓis the constant appearing
in the statement of Proposition 2.1. Moreover, we may take Cℓto be 2KℓBℓand Qℓto be 4B2
ℓ, where
Bℓ, Kℓare the constants appearing in the proof of Proposition 2.1 controlling the exponential growth of
the Betti numbers of the relevant Hurwitz space. We now explain how to bound Bℓexplicitly.
In [Ellenberg et al. 2016, 7.8.1], the bound
dim Hi
ét((Xa
n)Fq; Qλ) ≤Kℓ(Bℓ)i
arises from two facts. First, there is a stability theorem [loc. cit., 6.2], which tells us in this context that
dim Hi
ét((Xa
n)Fq; Qλ) = dim Hi
ét((Xa
n+D)Fq; Qλ)
(2.8)
for all n > Ai + B, where A, B, and D are constants we shall specify. Second, there is an absolute bound
[loc. cit., 2.5] which tells us that
dim Hi
ét((Xa
n)Fq; Qλ) ≤(4ℓ)n.
These two facts together imply that
dim Hi
ét((Xa
n)Fq; Qλ) ≤(4ℓ)Ai+B+D
so we may take Bℓ= (4ℓ)A and Kℓ= (4ℓ)B+D. It remains to compute A, B, and D.
The key object of computation is the ring R deﬁned in [Ellenberg et al. 2016, Section 3]. This ring is
deﬁned for any ﬁnite group G and any conjugacy-closed subset of G; we will consider here just the case
relevant to us, which is that where G is the dihedral group of order 2ℓand c is the class of involutions
in G. The set of n-tuples of involutions (τ1, . . . , τn) ∈Gn carries a natural action of the n-strand braid
