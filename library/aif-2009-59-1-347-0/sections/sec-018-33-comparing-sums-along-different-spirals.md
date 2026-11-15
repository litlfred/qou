---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-018-33-comparing-sums-along-different-spirals
section_title: "Comparing sums along different spirals"
section_number: 3.3
pages: 34-35
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
Notice that if λqZ = µqZ, i.e. if λ and µ are two complex numbers
congruent modulo q, the two discrete sums E[λ]
q
and E[µ]
q
coincide. On the
other side, if λqZ̸ = µqZ these sums are trivially distinct, since the sets
of their poles are distinct. This simple remark underlines a fundamental
diﬀerence between the continuous and the discrete summations. In fact,
when we make the direction d vary we are actually constructing an analytic
continuation of Ed
q on eC∗, while when we make λqZ vary, we obtain a whole
family of distinct meromorphic solution of x2dqy + y = x. This implies
that the “discrete Stokes phenomenon” for the discrete summation has
a diﬀerent nature from the classical diﬀerential Stokes phenomenon. It is
described in the following theorem:
Theorem 3.13. — For λ, µ ∈C∗\ (1 −p)qZ we have:
E[λ]
q
−E[µ]
q
= K(λ, µ, x)
ep( q
x)
,
where:
K(λ, µ, x) = C
θp(−λ
µ)θp( 1−p
x )θp( (1−p)λµ
x
)
θp( (1−p)λ
x
)θp( (1−p)µ
x
)
,
where C is a constant depending only on q.
Proof. — The function E[λ]
q (x) −E[µ]
q (x) being solution of the homoge-
neous equation x2dqy = −y, has the form
E[λ]
q
−E[µ]
q
= K(λ, µ, x)
ep( q
x)
,
where K(λ, µ, x) is q-invariant function in each variable (x, λ, µ).
We want a more precise description of K(λ, µ, x). Notice that E[λ]
q
−E[µ]
q
has only two spirals of simple poles: −(1 −p)λpZ and −(1 −p)µpZ. Since
TOME 59 (2009), FASCICULE 1
380
Lucia DI VIZIO & Changgui ZHANG
any q-invariant uniform function can be written as a quotient of Theta
functions, we obtain:
K(λ, µ, x) =
C(λ, µ)θ( α
x )θ( β
x)
θ( (1−p)λ
x
)θ( (1−p)µ
x
)
,
where αβ = (1 −p)2λµ. Moreover the factor eq(−q/x) in
K(λ, µ, x) = eq(−q/x)(E[λ]
q
−E[µ]
q ),
implies that K(λ, µ, x) has a spiral of simple zeros at (1 −p)pZ, which
implies that we can chose either α or β equal to −(1 −p). We conclude
that {α, β} = {−(1 −p), −(1 −p)λµ}.
We have to calculate C(λ, µ). The poles of K(λ, µ, x) with respect to the
variable λ forms two spirals: −
x
1−ppZ and −pZ, hence:
C(λ, µ) =
θ(−λ
µ)
θ(λ) C(µ).
A similar argument shows that C(µ) = C/θ(pµ).
□
Remark 3.14. —
One can express the constant C in terms of q-series.
For instance, setting x = 1 and letting λ →µ = 1 in K(λ, µ, x), we can
express C as a value of a derivative.
