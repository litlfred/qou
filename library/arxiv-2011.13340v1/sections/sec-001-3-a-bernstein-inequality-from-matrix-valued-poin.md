---
doc_id: arxiv-2011.13340v1
doc_title: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions*"
section_id: sec-001-3-a-bernstein-inequality-from-matrix-valued-poin
section_title: "A Bernstein Inequality from Matrix valued Poincare inequalities"
section_number: 3
pages: 10-15
source_pdf: 2011.13340v1.pdf
source_sha256: e73876ed2c923608
doc_brief: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions* — The Entropy method provides a powerful framework for provin g scalar concentration in- equalities by establishing functional"
---
In this section we show how to use Matrix valued Poincare inequ alities to obtain matrix Bernstein
style inequalities.
We will need a well-known monotonicity property of the trace exponential [Tro15]
Lemma 3.1. For any monotone function f , for any Hermitian matrices A and H such that A ≼H, then
Tr
[
f (A)
]
⩽ Tr
[
f (H)
]
The next lemma characterizes Jensen’s inequality for matri ces. The ﬁrst statement about
operator Jensen’s inequality for matrices can be found in [ Tro15], while the Jensen inequality for
the trace of a convex function is from [ HP03]
Lemma 3.2. Given a decomposition of the identity of the form
n∑
i=1
K∗
i Ki = I and an operator convex function
f , we have for any set of Hermitian matrices A 1, . . . ,An,
f
( n∑
i
K∗
i AiKi
)
≼
n∑
i
K∗
i f (Ai)Ki
For any convex function, we also have
T r
[
f
( n∑
i
K∗
i AiKi
) ]
⩽ T r
[n∑
i=1
K∗
i f ((Ai)Ki
]
10
Finally , we will need the following matrix identities which we will use to establish a mean
value theorem for the Dirichlet form.
Fact 3.3. [Eqn 5.35 in [ Bha07]] Given any positive semi-deﬁnite A, B, any Hermitian X and any unitarily
invariant norm ‖ · ‖, we have
‖‖‖‖‖
1∫
0
AtXB1−tdt
‖‖‖‖‖⩽ 1
2 ‖AX + XB‖
Fact 3.4. [Eqn 6.42 in [ Bha07]] For any Hermitian X, Y, we have
eX − eY =
1∫
0
etX(X − Y)e(1−t)Ydt
Lemma 3.5. Given random Hermitian matrices X and Y, we have
T r
[
E[(eX − eY)2]
] p
⩽ 1
2 E
[
‖X − Y‖2pT r[e2pX + e2pY]
]
Proof. We have
T r
[
E[(eX − eY)2]
] p
⩽ E
[
T r
[
(eX − eY)2p]
(using Lemma 3.2)
= E
[
T r
[
1∫
0
etX(X − Y)e(1−t)Y] 2p]
(from Fact 3.4)
= E
[‖‖‖‖‖
1∫
0
etX(X − Y)e(1−t)Y
‖‖‖‖‖
2p
2p
]
⩽ E
[(1
2
‖‖‖eX(X − Y) + (X − Y)eY‖‖‖2p
) 2p]
(using Fact 3.3)
⩽ E
[1
22p
( ‖‖‖eX(X − Y)
‖‖‖2p +
‖‖‖(X − Y)eY‖‖‖2p
) 2p]
(using triangle inequality)
⩽ E
[1
2
( ‖‖‖eX(X − Y)
‖‖‖
2p
2p +
‖‖‖(X − Y)eY‖‖‖
2p
2p
)]
(using (a + b)p ⩽ 2p−1(ap + bp) )
⩽ 1
2 E
[
‖X − Y‖2p(
‖eX‖2p
2p + ‖eY‖2p
2p
)
= 1
2 E
[
‖X − Y‖2pT r
[
e2pX + e2pY] ]
□
We now use this lemma to derive an upper bound on the trace powe r of the Dirichlet form.
11
Lemma 3.6. Given a reversible Markov Chain with transition matrix P ∈ RΩ×Ω and stationary measure
π ∈ RΩ, any function F : Ω→ Sd, we have
T r
[
E(eF, eF)
] p
⩽ v(F)2pT r[Ex∼π[e2pF(x)]]
where v(F) = max
x,y∈Ω
x∼y
‖F(x) − F(y)‖
Proof. Consider the trace power of the Dirchlet form,
T r
[
E(eF, eF)
] p
= T r
[∑
x∈Ω
πx
∑
y∈Ω
Pxy
(
eF(x) − eF(y)) 2] p
⩽
∑
x∈Ω
πxT r
[∑
y∈Ω
Pxy
(
eF(x) − eF(y)) 2] p
(using Lemma 3.2)
⩽ 1
2
∑
x∈Ω
πx
∑
y∈Ω
Pxy
(
‖F(x) − F(y)‖2pT r
[
e2pF(x) + e2pF(y)])]
(using Lemma 3.5 with X = F(x) and Y = F(y) )
⩽ v(F)2p
2
∑
x,y∈Ω
πxPxyT r[e2pF(x) + e2pF(y)]
⩽ v(F)2p
∑
x∈Ω
πxT r[e2pF(x)] (using reversibility of P)
= v(F)2pT r[Ex∼π[e2pF(x)]]
□
We are ﬁnally ready to use our Matrix valued Poincare inequalit y to prove our matrix concen-
tration inequality . A standard method to prove matrix concentration uses the exponential moment
generating function (mgf) which we state next.
Proposition 3.7. [Matrix Laplace T ransform Method [T ro15]] Let X ∈ Hd be a random matrix with trace
mgf m(θ) = T r[eθ(X−E[X])]. For every t ∈ R,
Pr[‖X − E[X]‖/greaterorequalslantt] ⩽ 2 inf
θ>0
e−θt+log(m(θ))
Hence, to get our concentration inequality , we just need to g et a bound on the moment gener-
ating function.
Theorem 3.8. Given a reversible Markov Chain with transition matrix P ∈ RΩ×Ω and its stationary
distribution π ∈ RΩ, any function F : Ω → Sd such that it satisﬁes the Matrix valued Poincare inequality
with constant λ, we have
Prx∼π[‖F(x) − Ey∼π[F(y)]‖/greaterorequalslantt] ⩽ 2de−t2/4(v(F)2/λ+tv(F)/
√
λ)
where v(F) = max
x,y∈Ω
x∼y
‖F(x) − F(y)‖
12
Proof. For notational convenience, we will write λ as the inverse of the actual λ value. Hence,
our Poincare inequality now looks like V ar[F] ≼λE[F, F]To use Proposition 3.7, we need an upper
bound on the mgf. The statement we want to prove, via inductio n, is
(1 − λv(F)2Sk)T r
[
E[eF(x)]
]
⩽ T r[E[eF(x)/2k
]]2k
(3.1)
where λv(F)2 ⩽ 1 and Sk =
k∑
i=1
1/2i which tends to 1 as k → ∞ . Assuming the induction
hypothesis, consider the RHS where n = 2k
T r[E[eF(x)/n]]n = T r[
∑
x∈Ω
πx(1 + F(x)/n + (F(x)/n)2/2! + . . .)]n
= T r[(1 + E[F(x)]/n)n] → T r[eE[F(x)]]
where the second inequality follows as we can ignore the seco nd order terms and beyond for
n → ∞. Now notice that for any β > 0, we have v(βF) = βv(F). Now taking θF in place of F and the
requirement of λv(θF)2 ⩽ 1 translates to θ2λv(F)2 ⩽ 1, we plug this into Equation 3.1, to get
T r
[
Ex∼π[eθF(x)]
]
⩽ T r[eθEx∼π[F(x)]]
1 − θ2λv(F)2 (3.2)
Now, using Equation3.2 with F being F−E[F] which is zero mean and noticing thatv(F−E[F]) = v(F),
we get that
T r
[
Ex∼π[eθF(x)]
]
⩽ d
1 − θ2λv(F)2 (3.3)
Now, in the RHS for Proposition 3.7, we have
2 inf
θ>0
e−θt+log m(θ) ⩽ 2 inf
θ2λv(F)2⩽ 1
e−θt+log m(θ)
= 2d inf
θ2λv(F)2⩽ 1
e−θt−log(1−θ2λv(F)2)
⩽ 2d inf
θ2λv(F)2⩽ 1
e
−θt+λv(F)2θ2+ λ2v(F)4θ4
2(1−λv(F)2θ2)
Diﬀerentiating w.r.t θ and setting to zero, we get that the probability is upper boun ded by
2de−t2/4(λv(F)2)+t
√
λv(F)) and we would be done.
Now, it just remains to prove the induction statement. Our pr oof proceeds by a doubling trick
to transform the variance of eF to the exponential moment generating function. We ﬁrst prove the
base case. Consider k = 1 and consider the function f = F/2. Using the matrix valued Poincare
inequality on ef, we have
V ar(ef) = λE(ef, ef)
=⇒ E[e2f] ≼(E[ef])2 + E(ef, ef)
E[eF] ≼(E[ef])2 + E(ef, ef)
13
Taking trace on both sides, we have
T r[E[eF]] ⩽ T r[(E[eF/2])2] + T r[E(eF/2, eF/2)]
⩽ T r[(E[eF/2])2] + v(F/2)2T r[Ex∼π[eF]] (using Lemma 3.6)
= T r[(E[eF/2])2] + v(F)2
4 T r[Ex∼π[eF]]
⩽ T r[(E[eF/2])2] + λv(F)2S1
2 T r[Ex∼π[eF]] (using λ /greaterorequalslant1 and S1 = 1/2 )
(
1 − λv(F)2S1
2
)
T r[E[eF]] ⩽ T r[(E[eF/2])2]
which establishes our base case. Now assume the induction hy pothesis for k-1 and consider the
function f = F/2k. Denote vk = v(F/2k) = v(F)/2k Using the matrix valued Poincare inequality on ef
and taking trace to the power p = 2k−1, we get,
T r
[
E[eF/2k−1
]
] 2k−1
⩽ T r
[
(E[eF/2k
])2 + λE(eF/2k
, eF/2k
)
] 2k−1
= T r
[
(1 − λv2
k) (E[eF/2k
])2
(1 − λv2
k) + λv2
k)(E(eF/2k
, eF/2k
)/v2
k)
] 2k−1
⩽
T r
[
E[eF/2k
]
] 2k
(1 − λvk)2k−1−1 + λv2
kT r
[
(E(eF/2k
, eF/2k
)/v2
k)
] 2k−1
(using Jensen’s inequality as λv2
k ⩽ 1 )
⩽
T r
[
E[eF/2k
]
] 2k
(1 − λv2
k)2k−1−1 + λv2
k T r[Ex∼π[eF]] (using Lemma 3.6)
Now using the induction hypothesis, we can lower bound the LH S above to get,
(1 − λv(F)2Sk−1)T r[Ex∼π[eF]] ⩽
T r
[
E[eF/2k
]
] 2k
(1 − λv2
k)2k−1−1 + λv2
kT r[Ex∼π[eF]]
(1 − λv(F)2Sk−1 − λv2
k )T r[Ex∼π[eF]] ⩽
T r
[
E[eF/2k
]
] 2k
(1 − λv2
k)2k−1−1
T r
[
E[eF/2k
]
] 2k
/greaterorequalslant(1 − λv(F)2Sk−1 − λv2
k)(1 − λv2
k)2k−1−1T r[Ex∼π[eF]]
/greaterorequalslant(1 − λv(F)2Sk−1 − λv2
k)(1 − λ(2k−1 − 1)v2
k)T r[Ex∼π[eF]]
/greaterorequalslant(1 − λv(F)2Sk−1 − λ2k−1v2
k)T r[Ex∼π[eF]]
/greaterorequalslant(1 − λv(F)2Sk−1 − λ2k−1v(F)2/22k)T r[Ex∼π[eF]]
/greaterorequalslant(1 − λv(F)2Sk)T r[Ex∼π[eF]]
where the fourth inequality follows from (1 − x)n /greaterorequalslant(1 − nx) and the last line follows as 2 k−1/22k =
1/2k+1 ⩽ 1/2k □
14
Proof. [of Theorem 1.1] Since our function F is L-Lipshitz, we know that v(F) ⩽ 2L as the Hamming
distance between any pair of connected states in the Markov Ch ain is 2. Hence, using Theorem
3.8 and the fact that λ /greaterorequalslant1/2k (from 2.1), we are done. □
4 Comparison with [ KS18]
We ﬁrst state the main result of [ KS18] below.
Theorem 4.1. Suppose (x1, . . . ,xn) ∈ { 0, 1}n is a random subset whose distribution is a k-homogenous
strong Rayleigh distribution. Given a collection of PSD matri ces A 1, . . . ,An ∈ Rd×d s.t. for all e ∈ [n] we
have ‖Ae‖⩽ 1 and ‖E[∑
e xeAe]‖⩽ µ. Then for any ε > 0,
Pr[‖
∑
e
xeAe − E[
∑
e
xeAe]‖/greaterorequalslantεµ] ⩽ de−ε2µ/(log k+ε)Θ(1)
Compared to our Theorem 1.1, immediate di ﬀerences is that our theorem can handle any
symmetric matrix valued Lipshitz function rather than just sums of random matrices associated
to each element. Furthermore, [ KS18] require their matrices to be PSD whereas we just require the
matrices to be symmetric. Finally , in the special case of sum s of PSD matrices. While Theorem
4.1 is concerned with multiplicative errors whereas we are conc erned with additive errors, we can
take t = εµ and plugging this into Theorem 1.1, noticing that sums of spectral norm 1 random
matrices have Θ(1) Lipshitz constant and ignoring constants in both bounds we get that our bound
is better when
ε2µ
log(k) + ε ⩽ ε2µ2
k + εµ
√
k
k + εµ
√
k ⩽ µ log k + εµ
Now assuming ε ⩽ 1√
k , we get that the above equation is approximately
µ /greaterorequalslantk/(log(k))
Also notice that in this case, µ ⩽ k but it is conceivable that µ = Θ(k) when there is no strong
relation between the underlying strong Rayleigh measure an d the matrices for each element. So
our bound is better when such a condition is satisﬁed and we are looking for small error of the
form ε ⩽ 1/
√
k. If one could establish a Matrix valued modiﬁed log-Sobolev an d a Matrix Herbst
argument, the
√
kε term in our bound will not appear which would allow us to get ri d of the
ε ⩽ 1/
√
k condition and just require µ /greaterorequalslantk/ log(k). However, we are not aware of any strategy to
get multiplicative bounds even in the scalar concentration settings using log-Sobolev or any other
functional inequalities.
