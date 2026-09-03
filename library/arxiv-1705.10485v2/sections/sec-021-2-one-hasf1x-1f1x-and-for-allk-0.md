---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-021-2-one-hasf1x-1f1x-and-for-allk-0
section_title: "One hasf1(x) = 1−f1(−x), and for allK≥ 0,"
section_number: 2
pages: 15-16
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
f1(K) =
∫ ∞
0
ρ(K +y)dy≤ 32
πK 3 ;
∫ ∞
0
f1(u−K)du≤K +
∫ ∞
w=0
min
(
1, 32
πw 3
)
dw =K + 3
3
√
3
π.
Proof. The derivative offa,ε is
∂(fa,ε)(x) =∂(1(−∞,a]∗ρε)(x) =
(
∂(1(−∞,a])∗ρε
)
(x)
= (−δa∗ρε) (x) =−ρε(x−a),
so it is indeed inT0(R), and non-positive. Its Fourier transform is supported by[− 1
ε, 1
ε], and‖∂fa,ε‖L1 =∫
Rρε(x)dx = 1. Then,
lim
x→+∞
fa,ε(x) = lim
x→+∞
f1
(x−a
ε
)
= lim
y→+∞
f1(y),
so limx→+∞fa,ε(x) = 0.Sincebydeﬁnition f1(y) =
∫∞
y ρ(u)du,thesymmetryrelation f1(x) = 1−f1(−x)
follows fromρ even; it implies the other limit statementlimx→−∞fa,ε(x) = 1. The inequalities in part
ii) are immediate consequences of those of Lemma 17. ⊓ ⊔
Let us now state a result which converts estimates on smooth test distributions into estimates of
Kolmogorov distances. It already appeared in [MN15, Lemma 16], and is inspired by [Tao12, p. 87] and
[Fel71, Chapter XVI, §3, Lemma 1]:
Theorem 19.Let X and Y be two random variables with cumulative distribution functionsFX(a) =
P[X≤a] and FY (a) = P[Y ≤a]. Assume that for someε> 0 and B >0,
sup
a∈R
|E[fa,ε(X)]− E[fa,ε(Y )]|≤ Bε.
We also suppose thatY has a density w.r.t. Lebesgue measure that is bounded bym. Then, for every
λ> 0,
dKol(X,Y ) = sup
a∈R
|FX(a)−FY (a)|
≤ (1 +λ)
(
B + m
3√π
(
4
3
√
1 + 1
λ + 3
3√
3
))
ε.
The choice of the parameterλ allows one to optimize constants according to the reference law ofY and
to the value ofB. A general bound is obtained by choosingλ = 1
2; this gives after some simpliﬁcations
