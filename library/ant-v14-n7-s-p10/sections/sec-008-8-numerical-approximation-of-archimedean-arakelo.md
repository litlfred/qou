---
doc_id: ant-v14-n7-s-p10
doc_title: "Abelian extensions in dynamical Galois theory"
section_id: sec-008-8-numerical-approximation-of-archimedean-arakelo
section_title: "Numerical approximation of Archimedean Arakelov–Zhang integrals"
section_number: 8
pages: 15-17
source_pdf: ant-v14-n7-s-p10.pdf
source_sha256: 8d3e47aa779ad9c7
doc_brief: "Abelian extensions in dynamical Galois theory — 11 sections: Introduction; Some algebraic lemmas; Ramiﬁcation and postcritically inﬁ"
---
In this section we prove a result which may be of use in numerically approximating the value of the
Archimedean part of the Arakelov–Zhang pairing⟨x2+ c, x2⟩.
Given a polynomialφ(x)∈ C[x] of degree 2, we may express the corresponding canonical local height
function as
λφ(x)= lim
n→+∞
1
2n log(1+|φn(x)|2)1/2. (15)
Note that, compared to (10), we have replaced log+|·| with log(1+|·| 2)1/2; this choice gives differentiable
approximations toλφ(x), but in the limit it deﬁnes precisely the same Archimedean local height function
as in (10).
Next deﬁne
B(φ)= sup
x∈C
|log(1+|φ(x)|2)1/2− 2 log(1+| x|2)1/2|. (16)
The signiﬁcance of this constant follows from a standard telescoping series argument [Silverman 2007,
Theorem 3.20], which shows that for each n≥ 1 we have
⏐⏐⏐⏐λφ(x)− 1
2n log(1+|φn(x)|2)1/2
⏐⏐⏐⏐≤ B(φ)
2n . (17)
Proposition 18. Letφ(x)= x2+ c for c∈ C, let N≥ 1 and M≥ 1 be integers, and letµM denote the set
of M-th roots of unity in C. Then
⏐⏐⏐⏐
∫ 1
0
λφ(e2πit) dt− 1
M
∑
ζ∈µM
1
2N log(1+|φ N(ζ)|2)1/2
⏐⏐⏐⏐≤ B(φ)
2N +πT N
M (18)
where T=(1+√1+ 4|c|)/2.
Proof. Using (17) we obtain
⏐⏐⏐⏐
∫ 1
0
λφ(e2πit) dt−
∫ 1
0
fN(t) dt
⏐⏐⏐⏐≤ B(φ)
2N (19)
where
fN: R/Z→ R fN(t)= 1
2N log(1+|φ N(e2πit)|2)1/2.
If f: R/Z→ R is continuously differentiable and M≥ 1, then
⏐⏐⏐⏐
1
M
M∑
m=1
f(m/M)−
∫ 1
0
f(t) dt
⏐⏐⏐⏐≤‖ f′‖∞
2M , (20)
1996 Jesse Andrews and Clayton Petsche
where‖g‖∞= sup{|g(t)|| t∈ R/Z}. This inequality can be veriﬁed using an elementary Riemann sum
argument, together with the mean-value theorem estimate | f(m/M)− f(t)|≤‖ f′‖∞/2M whenever
t∈[ m/M− 1/(2M), m/M+ 1/(2M)].
We are going to show that‖ f′
N‖∞≤ 2πT N , and so applying (20) with f= fN , and combining with
(19), we obtain (18).
It remains only to prove‖ f′
N‖∞≤ 2πT N . Given any polynomial F(x)∈ C[x], an application of the
multivariable chain rule gives, for t∈ R,
⏐⏐⏐⏐
d
dt log(1+| F(e2πit)|2)1/2
⏐⏐⏐⏐≤ 2π|F(e2πit)||F′(e2πit)|
1+| F(e2πit)|2 . (21)
The choice of T in terms of c was made so that T 2− T−| c|= 0, which can be used to show that
|x|> T⇒|φ(x)|>|x|2/T > T (22)
for all x∈ C. Indeed,|φ(x)|≥| x|2−| c| and therefore
|φ(x)|
|x|2 ≥ 1−|c|
|x|2 > 1−|c|
T 2= 1
T.
Using an iteration of the inequality (22), we claim that for each x∈ C, we have
|xφ(x)φ2(x)··· φ N(x)|≤ T N(1+|φ N(x)|2). (23)
Indeed, if|φn(x)|≤ T for all n= 0, 1, 2,..., N−1, the bound is trivial. Otherwise, let 0≤ n0≤ N−1 be
the smallest n for which|φn(x)|> T . Using (22) we have|φn(x)|< T 1/2|φn+1(x)|1/2 for all n0≤n≤ N−1.
Thus, letting m0= N− n0, we have
|xφ(x)φ2(x)··· φ N(x)|≤ T n0|φn0(x)||φn0+1(x)|···| φ N(x)|
< T n0T 1/2|φn0+1(x)|1/2+1|φn0+2(x)|···| φ N(x)|
< T n0T 1/2T 1/4+1/2|φn0+2(x)|1/4+1/2+1|φn0+3(x)|···| φ N(x)|
...
< T n0T 1/2T 1/4+1/2··· T 1/2m0+···+1/2|φ N(x)|1/2m0+···+1/2+1
< T N(1+|φ N(x)|2).
Usingφ′(x)= 2x and the chain rule we have
(φ N)′(x)=φ′(φ N−1(x))φ′(φ N−2(x))··· φ′(φ(x))φ′(x)= 2Nφ N−1(x)φ N−2(x)··· φ(x)x, (24)
and applying (23) we obtain
|φ N(x)||(φ N)′(x)|= 2N|φ N(x)φ N−1(x)φ N−2(x)··· φ(x)x|≤ 2N T N(1+|φ N(x)|2). (25)
Finally, taking F(x)=φ N(x) in (21) and using the bound (25) we conclude‖ f′
N‖∞≤ 2πT N , completing
the proof. □
Abelian extensions in dynamical Galois theory 1997
We conclude with an explanation of how to use Proposition 18 to obtain the numerical calculation (14)
of⟨x2−1, x2⟩ to the speciﬁed precision. Since both φ(x)= x2−1 andψ(x)= x2 are monic with integer
coefﬁcients, the non-Archimedean contributions in (12) vanish, and since the Archimedean canonical
measureµφ,∞ is the normalized Haar measure supported on the unit circle of C, we have
⟨φ,ψ⟩=
∫ 1
0
λφ,∞(e2πit) dt. (26)
We approximate this integral using Proposition 18 with φ(x)= x2− 1. Clearly T=(1+
√
5)/2, and
we will show that B(φ)=(log 5)/2, which according to the deﬁnition (16) is equivalent to checking that
sup
x∈C
⏐⏐⏐⏐log 1+| x2− 1|2
(1+| x|2)2
⏐⏐⏐⏐= log 5. (27)
To establish (27) is to prove both of the inequalities
1
5(1+| x|2)2≤ 1+| x2− 1|2≤ 5(1+| x|2)2 (28)
and to prove that at least one of them is sharp. The second inequality (with the stronger constant 2 in
place of 5) is easily checked using only the triangle inequality. For the second inequality, we see using
the triangle inequality that 1+| x2− 1|2≥| x|4− 2|x|2+ 2, with equality when x is real; we complete the
proof by noting that(r 4− 2r 2+ 2)/(1+ r 2)2 is minimized at r=
√
3
2 with minimum value 1
5.
Using Proposition 18 with M= 224 and N= 13, we have
∫ 1
0
λφ,∞(e2πit) dt= 1
238
∑
ζ∈µ224
log(1+|φ13(ζ)|2)+θ (29)
where|θ|≤ (log 5)/214+π((1+
√
5)/2)13/224= 0.000195... . Finally, one may perform the calculation
1
238
∑
ζ∈µ224
log(1+|φ13(ζ)|2)= 0.16772223... (30)
using any implementation of arbitrary precision ﬂoating-point arithmetic; speciﬁcally we used the
RealField() package in Sage [2016] in a computation taking about three hours. It follows from (26), (29),
(30), and the bound on θ that (14) is accurate to the indicated precision.
It was pointed out to us by an anonymous referee that, if one only wants to check that ⟨x2− 1, x2⟩<
(log 2)/4 but without giving an explicit numerical approximation for ⟨x2− 1, x2⟩, then one could get
away with the smaller parameters N= 9 and M= 216, resulting in a much faster calculation.
