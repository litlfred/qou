---
doc_id: arxiv-q-alg-9707006v1
doc_title: "Drinfeld twist for quantum su(2) in the adjoint representation"
section_id: sec-003-22-the-reduced-basis
section_title: "The reduced basis"
section_number: 2.2
pages: 3-4
source_pdf: 9707006v1.pdf
source_sha256: b9513be9294f56d9
toc_source: inferred
doc_brief: "Drinfeld twist for quantum su(2) in the adjoint representation — We give a detailed description of the adjoint representation of Drinfeld’s twist element, as well as of its coproduct, for suq(2)."
---
The reduced basis
To simplify subsequent calculations we chose to work in a reduced basis, in which the representation (denoted ρr)
consists of 1 and 3-dimensional blocks. The transition is eﬀected by conjugation with the matrix A, i.e. (x ∈Uq)
ρf(x) = Aρr(x)A−1
(8)
with A being given by
A =





q3
0
γ−1
0
0
1
0
0
0
0
0
q−1
q
0
−γ−1
0




.
(9)
This amounts to switching to the generators
c = q3x1 + qx2 ,
x0 = γ−1(x1 −x2)
in favor of x1, x2 as well as rescaling x−by q (the order chosen is {c, x+, x0, x−}). The generator c is central and
provides therefore an 1-dimensional representation for the algebra, given by the counit (notice that this coincides
with the classical limit). Omitting the 1-dimensional block, the reduced representation is given explicitly by
ρr(X+)=



0
−q−1/2γ
0
0
0
q−1/2γ
0
0
0


, ρr(qH/2)=



q
0
0
0
1
0
0
0
q−1


, ρr(X−)=



0
0
0
−q−1/2γ
0
0
0
q−1/2γ
0


,
(11)
where γ ≡
p
1 + q2. The rescaling of x−mentioned above guarantees that ρr(X+)T = ρr(X−), as in the classical
case.
It is also worth pointing out that, under the substitution q 7→q−1, ρr(X±) go into themselves while
ρr(qH) 7→ρr(qH)−1. We introduce now, for later use, the quantum casimir Cq, given by
Cq = X−X+ + λ−2(qH+1 + q−(H+1) −2) .
(12)
Its value in ρr is [3/2]2 where [x] ≡qx−q−x
q−q−1 . Notice that limq→1 Cq = Cc +1/4, where Cc is the familiar undeformed
casimir of su(2).
