---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-037-a2-formal-completions
section_title: "A.2. Formal completions"
section_number: null
pages: 37-38
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
associate a Poisson subalgebra
C∆ [T] =
⨁
Z(γ)∈∆ ⊔{0}
C· xγ⊂ C[T]. (43)
We will now introduce a natural completion of this algebra.
Deﬁne the height of an element a = ∑
γ aγ· xγ to be
H(a) = inf{|Z(γ)| : γ∈ Γ such that aγ⁄= 0}.
Note that since ∆ is acute, we have
|Z(γ1 + γ2)|≥ min(|Z(γ1)|,|Z(γ2)|),
whenever γi∈ Γ satisfy Z(γi)∈ ∆. It follows that
H(a· b)≥ max(H(a), H(b)), H ({a, b})≥ max(H(a), H(b)).
38 TOM BRIDGELAND
In particular, for any N > 0, the subspace
C∆ [T]≥N⊂ C∆ [T]
consisting of elements of height ≥ N is a Poisson ideal. We can therefore consider the inverse limit
of the quotient Poisson algebras as N→∞ :
C∆ [[T]] = lim←−N
C∆ [T]<N , C∆ [T]<N = C∆ [T]/C∆ [T]≥N .
The resulting completion C∆ [[T]] can be identiﬁed with the set of formal sums
∑
Z(γ)∈∆
aγ· xγ, (44)
such that for any N > 0 there are only ﬁnitely many terms with |Z(γ)| < N . We deﬁne the height
of such an element to be the minimum value of |Z(γ)| occurring.
