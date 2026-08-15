---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI"
section_id: sec-003-23-invariant
section_title: "Invariant"
section_number: 2.3
pages: 4-5
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
[36] to introduce a link invariant derived from a Yang-Baxter operat or.
Let V be an N -dimensional vector space over C, R an isomorphism from V⊗V to
itself, m an isomorphism from V to itself, and a and b non-zero complex numbers.
Deﬁnition 2.3. A quadruple ( R, µ, a, b) is called an enhanced Yang–Baxter oper-
ator if it satisﬁes the following:
(1) ( R⊗ IdV )(IdV⊗R)(R⊗ IdV ) = (Id V⊗R)(R⊗ IdV )(IdV⊗R),
(2) R(µ⊗ µ) = ( µ⊗ µ)R,
(3) Tr 2
(
R±1(IdV⊗µ)
)
= a±1b IdV .
Here Trk : End( V ⊗k)→ End(V ⊗(k−1)) is deﬁned by
Trk(f )(ei1⊗ei2···⊗ eik−1) :=
N −1∑
j1,j2,...,jk−1,j=0
f j1,j2,...,jk−1,j
i1,i2,...,ik−1,j (ej1⊗ej2⊗···⊗ ejk−1⊗ej),
where f∈ End(V ⊗k) is given by
f (ei1⊗ ei2⊗···⊗ eik ) =
N −1∑
j1,j2,...,jk=0
f j1,j2,...,jk
i1,i2,...,ik (ej1⊗ ej2⊗···⊗ ejk )
and{e0, e1, . . . , eN −1} is a basis of V .
Remark 2.4. The isomorphism R is often called an R-matrix, and the equation (1)
is known as the Yang–Baxter equation.
Given an n-braid β, we can construct a homomorphism Φ( β) : V ⊗n→ V ⊗n by
replacing a generator σi with Id ⊗(i−1)
V ⊗R⊗ Id⊗(n−i−1)
V , and its inverse σ−1
i with
Id⊗(i−1)
V ⊗R−1⊗ Id⊗(n−i−1)
V (Figure 7).
⇒
 , ⇒
Figure 7. Replace a generator with the R-matrix.
Example 2.5. For the braid σ1σ−1
2 σ1σ−1
2 the corresponding homomorphism is give
as follows (Figure 8):
Φ( σ1σ−1
2 σ1σ−1
2 ) = ( R⊗ IdV )(IdV⊗R−1)(R⊗ IdV )(IdV⊗R−1).
AN INTRODUCTION TO THE VOLUME CONJECTURE 5
Φ
− →
Figure 8. A braid and the corresponding homomorhism
