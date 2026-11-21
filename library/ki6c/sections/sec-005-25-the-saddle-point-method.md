---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-005-25-the-saddle-point-method
section_title: "The saddle point method"
section_number: 2.5
pages: 11-12
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
The saddle point method
In this section, we review a proposition obtained from the saddle point method.
Proposition 2.6 (see [20]). Let A be a non-singular symmetric complex 3×3 matrix, and
let ψ(z1, z2, z3) and r(z1, z2, z3) be holomorphic functions of the forms,
ψ(z1, z2, z3) = zTA z + r(z1, z2, z3),
r(z1, z2, z3) = ∑
i,j,k bijkzizjzk + ∑
i,j,k,l cijklzizjzkzl + · · · ,
(26)
deﬁned in a neighborhood of 0 ∈C3. The restriction of the domain
{
(z1, z2, z3) ∈C3 

 Re ψ(z1, z2, z3) < 0
}
(27)
to a neighborhood of 0 ∈C3 is homotopy equivalent to S2. Let D be an oriented 3-ball
embedded in C3 such that ∂D is included in the domain (27) whose inclusion is homotopic
to a homotopy equivalence to the above S2 in the domain (27). Then,
∫
D
eN ψ(z1,z2,z3)dz1 dz2 dz3 =
π3/2
N 3/2√
det(−A)
(
1 +
d
∑
i=1
λi
N i + O
(
1
N d+1
))
,
11
for any d, where we choose the sign of
√
det(−A) as explained in [20], and λi’s are con-
stants presented by using coeﬃcients of the expansion of ψ(z1, z2, z3); such presentations
are obtained by formally expanding the following formula,
1 +
∞
∑
i=1
λi
N i = exp
(
N r
( ∂
∂w1
,
∂
∂w2
,
∂
∂w3
))
exp
(
−1
4N


w1
w2
w3


T
A−1


w1
w2
w3


)

w1=w2=w3=0
.
For a proof of the proposition, see [20].
Remark 2.7. As mentioned in [20, Remark 3.6], we can extend Proposition 2.6 to the
case where ψ(z1, z2, z3) depends on N in such a way that ψ(z1, z2, z3) is of the form
ψ(z1, z2, z3) = ψ0(z1, z2, z3) + ψ1(z1, z2, z3) 1
N + ψ2(z1, z2, z3) 1
N 2
+ · · · + ψm(z1, z2, z3) 1
N m + rm(z1, z2, z3)
1
N m+1 ,
where ψi(z1, z2, z3)’s are holomorphic functions independent of N, and we assume that
ψ0(z1, z2, z3) satisﬁes the assumption of the proposition and |rm(z1, z2, z3)| is bounded by
a constant which is independent of N.
3
The 61 knot
In this section, we show Theorem 1.1 for the 61 knot. We give a proof of the theorem in
Section 3.1, using lemmas shown in Section 3.2–3.5.
