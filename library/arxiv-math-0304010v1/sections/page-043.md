---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-043
section_title: "Page 43"
section_number: null
pages: 43-43
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
is a Gaussian random variable. In particular, setting ϕ(x) = uk(x) we get, by the
orthogonality relation (7.5),
⟨uk, ∆⟩=
ξk+1
√
k + 1 ,
k = 1, 2, . . . .
Informally, the result of Theorem 7.1 can be stated as follows: for the random
Plancherel diagram λ ∈Yn ,
¯λ(x) ∼Ω(x) +
2
√n ∆(x),
n →∞,
(9.2)
where ¯λ(x) was introduced in Deﬁnition 2.3, and ∆(x) is given by (9.1)
Next, consider the random series
b∆(x) =
∞
X
k=3
√
k −1ξk−1tk(x)
2π
√
4 −x2
,
−2 < x < 2.
(9.3)
Here ξ2, ξ3, . . . are as above and t3, t4, . . . are modiﬁed Chebyshev’s polynomials
of the ﬁrst kind (see (8.5), (8.6)).
The series (9.3) correctly deﬁnes a general-
ized Gaussian process on the same space F′ = (C∞(R))′ of compactly supported
distributions. For any test function ϕ ∈C∞(R),
⟨ϕ, b∆⟩=
Z 2
−2
ϕ(x)b∆(x)dx =
∞
X
k=3
√
k −1ξk−1
2π
Z 2
−2
ϕ(x)uk(x)
√
4 −x2 dx
is a Gaussian random variable. In particular, setting ϕ(x) = tk(x) we get, by the
orthogonality relation (8.7),
⟨tk, b∆⟩=
√
k −1ξk−1 ,
k = 3, 4, . . . .
Informally, the result of Theorem 8.6 can be stated as follows: for the random
Plancherel diagram λ ∈Yn ,
bλ(x) ∼µs-c(x) +
1
√n
b∆(x),
n →∞,
(9.4)
where the transition measure bλ (see Deﬁnition 8.5) is viewed as a generalized func-
tion, and b∆(x) is given by (9.3).
Let us compare these results with the central limit theorem for the Gaussian
unitary ensemble. Consider the space HN of N × N complex Hermitian matrices,
and equip it with the Gaussian measure
GaussN(dX) =
 N
2π
N2/2
exp

−N
2 tr(X2)

Leb(dX),
(9.5)
where X ranges over HN and Leb denotes the Lebesgue measure on HN ≃RN2.
43
