---
doc_id: arxiv-math-0209324v1
doc_title: "CYCLOTOMIC COMPLETIONS OF POL YNOMIAL RINGS KAZUO HABIRO"
section_id: sec-016-71-units-in-zqs-if-r-is-a-ring-and-s-mr-is-a-sub
section_title: "Units in Z[q]S. If R is a ring and S ⊂ MR is a subset consisting"
section_number: 7.1
pages: 14-15
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS KAZUO HABIRO — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which"
---
of monic polynomials with the constant terms being units in R, then the
element q is invertible in R[q]S. In particular, we have an explicit formula
for q−1∈ R[q]N as follows.
Proposition 7.1. For any ring R the element q∈ R[q]N is invertible with
the inverse
q−1 =
∑
n≥0
qn(q)n.
Proof. q ∑
n≥0 qn(q)n = ∑
n≥0 qn+1(q)n = ∑
n≥0(1− (1− qn+1))(q)n =∑
n≥0((q)n− (q)n+1) = ( q)0 = 1. □
For each subset S⊂ N the inclusion Z[q]⊂ Z[q, q −1] induces an isomor-
phism
Z[q]S≃ lim
←−f ∈Φ ∗
S
Z[q, q −1]/ (f ),
via which we will identify these two rings. If S⁄=∅, then, since ⋂
f ∈Φ ∗
S
(f ) =
(0) in Z[q, q −1], the natural homomorphism Z[q, q −1]→ Z[q]S is injective
and regarded as inclusion.
For a ring R let U (R) denote the (multiplicative) group of the units in R.
If S⁄=∅, then we have
U (Z[q, q −1])⊂ U (Z[q]N).
It is well known that U (Z[q, q −1]) ={±qi| i∈ Z}. If we regard Z[q]N and
the Z[q]⟨n⟩ as subrings of Z[q]⟨1⟩ = Z[[q− 1]] as in Corollary 4.3, then we
have
U (Z[q]N) =
⋂
n∈N
U (Z[q]⟨n⟩).
Conjecture 7.2. We have U (Z[q]N) ={±qi| i∈ Z}.
Remark 7.3. One might expect that Conjecture 7.2 would generalize to any
inﬁnite, Z-admissible subset S⊂ N, but this is not the case. For odd m≥ 3
consider the element γm = ∑ m−1
i=0 (−1)iqi∈ Z[q], which is known to deﬁne a
unit in the ring Z[q]/ (qn− 1) with ( n, 2m) = 1 and is called an “alternating
unit”, see [11]. For such n, it follows that there are u, v ∈ Z[q] such that
CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS 15
γmu = 1 + vΦ n(q). Since 1 + vΦ n(q) is a unit in Z[q]⟨n⟩, it follows that γm is
a unit in Z[q]⟨n⟩. Set S ={n∈ N| (n, 2m) = 1}. Then it is straightforward
to check that γm deﬁnes a unit in Z[q]S (hence also in Z[q]S′
for any S′⊂ S).
Consequently, we have U (Z[q]S) ⊊ {±qi| i∈ Z}.
