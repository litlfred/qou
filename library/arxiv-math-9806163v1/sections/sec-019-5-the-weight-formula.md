---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana"
section_id: sec-019-5-the-weight-formula
section_title: "The Weight Formula"
section_number: 5
pages: 16-18
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
In this section we deﬁne for every pair of partitions, ( α, β), a rational function in q and Q,
W(α,β )(q, Q). We will show that this function is a weight for the Markov trace deﬁ ned by
Geck and Lambropolou [GL] for the Hecke algebra of type B. If we denote the weights by
ω(α,β ) then the Markov trace, tr, can be written as follows:
tr(x) =
∑
(α,β )⊢n
ω(α,β )χ(α,β )(x), (11)
where x ∈ Hn(q, Q) and χ(α,β ) is the character (the usual trace) of the irreducible represen-
tation of Hn(q, Q) indexed by ( α, β).
First we deﬁne a rational function in q and Q for any arbitrary double partition ( α, β)
such that l(α) ≤ r1 and l(β) ≤ r2. If l(α) = s < r 1 then αi = 0 for i = s + 1, . . . r1, similarly
for β. Let r = r1 + r2.
W(α,β )(q, Q) = qn(α )+n(β )( 1 − q
1 − qr )|α |+|β | ∏
1≤i<j≤r1
1 − qα i−α j +j−i
1 − qj−i
∏
1≤i<j≤r2
1 − qβ i−β j+j−i
1 − qj−i
×
r1∏
i=1
r2∏
j=1
Qqα i−i + qβ j−j
Qq−i + q−j (12)
Notice that this function can be expressed as a product of Schur f unctions
W(α,β )(q, Q) = qr1|β | sα (1, q, . . . , qr1−1)sβ (1, q, . . . , qr2−1)
s[1](1, q, . . . , qr1+r2−1)|α |+|β |
r1∏
i=1
r2∏
j=1
(1 + Qqα i−β j+j−i)
(1 + Qqj−i) .
(13)
Recall that sα (1, q, . . . , qr1−1) = ∏
1≤i<j≤r1
1−qα i−α j +j−i
1−qj−i is the symmetric Schur function de-
ﬁned in Section 1, see equation (1).
Observation: Let 1 − r1 ≤ s ≤ r2 − 1. Assume that q is not a root of unity and Q ⁄= −q−s.
Then W(α,β )(q, Q) is an analytic rational function.
The rectangular Young diagram with r rows which has m boxes in the ﬁrst r1 rows and
0 boxes in the remaining rows, i.e. [ mr1], has Schur function given by
s[mr1 ],r (q) =
qmr1(r1−1)/ 2 ∏ r1
i=1
∏ r2
j=1
1−qm+r1+j−i
1−qr1+j−i
s[1](1, q, . . . , qr−1)mr1
.
We are going to assume that for ﬁxed integer n and m, r1 ∈ N, we have m > n and r1 > n.
Then for any double partition of n, ( α, β), we have µ = [m + α1, . . . , m + αr1, β1, . . . , βr2] is
Weights of Markov Traces on Hecke Algebras 17
a partition of n + mr1. Then by equation (3) from Section 1 we have the following equation
sµ,r (q)
s[mr1 ],r (q) = qr1|β | sα (1, q, . . . , qr1−1)sβ (1, q, . . . qr2−1)
s[1](1, q, . . . , qr)|α |+|β |
r1∏
i=1
r2∏
j=1
1 − qm+r1+α i−β j+j−i
1 − qm+r1+j−i .
Observe that we have the following equality:
sµ,r (q)
s[mr1 ],r (q) = W(α,β )(q, −qr1+m). (14)
Notice that W(α,β )(q, −qr1+m) is well-deﬁned since r1 + m > r 1, and as we observed before
W(α,β )(q, Q) is undeﬁned for Q = −q−s where 1 − r1 < s < r 2 − 1. So W(α,β )(q, −qr1+m) is
an analytic rational function.
Lemma 5.1
W(α,β )(q, Q) =
∑
(α,β )⊂(γ,η )
W(γ,η )(q, Q)
where (α, β) ⊂ (γ, η) means that (γ, η) is obtained by adding one box to (α, β).
Proof: Assume µ = [m + α1, . . . , m + αr1, β1, . . . , βr2]. By the Littlewood-Richardson rule
for Schur functions (see [M]) we have the following:
s[1],r sµ,r =
∑
µ ⊂ν,
|ν |=|µ |+1
sν,r
where s[1],r (q) = 1. Now divide both sides of this equation by s[mr1 ],r (q) and we get by
equation (14).
W(α,β )(q, −qr1+m) =
∑
(α,β )⊂(γ,η )
W(γ,η )(q, −qr1+m). (15)
Since W(α,β )(q, Q) is an analytic rational function and the above equation holds for all Q =
−qr1+m, thus we have that
W(α,β )(q, Q) =
∑
(α,β )⊂(γ,η )
W(γ,η )(q, Q). (16)
holds for all values of Q.□
In [W1] Wenzl showed that the weights of the Markov trace (with pa rameter z = qr (1−q)
(1−qr))
on the Hecke algebra of type A are given by the symmetric Schur function sµ,r (q) as described
in Section 1.
