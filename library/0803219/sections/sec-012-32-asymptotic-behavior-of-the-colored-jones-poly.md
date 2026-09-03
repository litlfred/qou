---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-012-32-asymptotic-behavior-of-the-colored-jones-poly
section_title: "Asymptotic behavior of the colored Jones polynomial. Now we con-"
section_number: 3.2
pages: 15-17
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
doc_brief: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS — In this paper we give an introduction to the volume conjectur e and its generalizations."
---
sider the colored Jones polynomial and its asymptotic behav ior.
As described above, Habiro and Lˆ e independently showed tha t for the ﬁgure-
eight knot E, JN (E; q) can be expressed in a single summation as follows:
(3.9) JN (E; q) =
N −1∑
k=0
k∏
j=1
(
q(N −j)/ 2 − q−(N −j)/ 2
)(
q(N +j)/ 2 − q−(N +j)/ 2
)
.
234 HITOSHI MURAKAMI
We put q := exp(θ/N ) and consider the asymptotic behavior of JN (E; exp(θ/N ))
for N → ∞ ﬁxing a complex parameter θ .
To state a formula describing the asymptotic behavior of JN (E; exp(θ/N )) we
prepare some functions. Put ϕ (θ ) := arccosh(cosh( θ ) − 1/ 2), where we choose
the branch of arccosh so that
arccosh(x) = log
(
x −
√
− 1
√
1 − x2
)
+ 2π
√
− 1.
We also choose the branch cut of log as ( −∞ , 0). Note that we use √ − 1
√
1 − x2
instead of
√
x2 − 1 to avoid the cut branch of the square root function, since la ter
we will assume that x is near 1 / 2. Let Li 2 be the dilogarithm function:
Li2(z) := −
∫ z
0
log(1 − w)
w dw =
∞∑
k=1
zk
k2
with the branch cut (1 , ∞ ).
Now we can prove the following four theorems about the asympt otic behavior
of the colored Jones polynomials of the ﬁgure-eight knot E.
(i). When θ is close to 2 π √ − 1.
Theorem 3.1 ([50]). Let θ be a complex number near 2π √ − 1. We also assume
that θ is not purely imaginary except for θ = 2π √ − 1. Then we have
θ lim
N →∞
log JN
(
E; exp(θ/N )
)
N = H(θ ),
where we put
H(θ ) := Li 2
(
e−ϕ (θ )−θ
)
− Li2
(
eϕ (θ )−θ
)
+ (θ − 2π
√
− 1)ϕ (θ ).
(ii). When θ is real and |θ |/greaterorequalslantarccosh(3/ 2).
Theorem 3.2 ([44, Theorem 8.1] (See also [46, Lemma 6.7])) . Let θ be a real
number with |θ |/greaterorequalslantarccosh(3/ 2). Then we have
θ lim
N →∞
log JN
(
E; exp(θ/N )
)
N = ˜H(θ ),
where we put
˜H(θ ) := Li 2
(
e− ˜ϕ (θ )−θ
)
− Li2
(
e ˜ϕ (θ )−θ
)
+ θ ˜ϕ (θ )
and ˜ϕ (θ ) is deﬁned as ϕ (θ ) by using the usual branch of arccosh so that arccosh(x) >
0 if |x|> 1.
Note that ˜H(θ ) = 0 if θ = ± arccosh(3/ 2).
(iii) When θ is close to 0.
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 235
Theorem 3.3 ([45],[11]). Let θ be a complex number with |2 cosh(θ ) − 2|< 1 and
Im(θ ) < π/ 3, then the sequence {JN
(
E; exp(θ/N )
)
}N =2, 3,... converges and
lim
N →∞
JN
(
E; exp(θ/N )
)
= 1
∆
(
E; exp(θ )
),
where ∆( E; t) is the Alexander polynomial of the ﬁgure-eight knot E.
Here we normalize the Alexander polynomial for a knot K so that ∆( K; 1) = 1
and that ∆( K; t−1) = ∆( K; t).
Note that in this case
lim
N →∞
log JN
(
E; exp(θ/N )
)
N = 0.
(iv). When θ = ± arccosh(3/ 2).
From (ii) we know that when θ = ± arccosh(3/ 2) then the colored Jones poly-
nomial does not grow exponentially. Since exp
(
± arccosh(3/ 2)
)
= (3 ±
√
5)/ 2 is
a zero of ∆( E; t), we cannot expect that the colored Jones polynomial conver ges.
In fact in this case we can prove that it grows polynomially.
Theorem 3.4 ([19, Theorem 1.1]) . We have
JN (E; exp(± arccosh(3/ 2)/N )) ∼
N →∞
Γ(1 / 3)
(
3 arccosh(3/ 2)
)2/ 3 N 2/ 3,
where Γ is the gamma function:
Γ( z) :=
∫ ∞
0
tz−1e−t dt.
