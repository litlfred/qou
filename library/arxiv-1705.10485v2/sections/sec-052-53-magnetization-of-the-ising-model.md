---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-052-53-magnetization-of-the-ising-model
section_title: "Magnetization of the Ising model"
section_number: 5.3
pages: 42-44
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
We consider here the nearest-neighbour Ising model on a ﬁnite subsetΛ of Zd with a quadratic
potential, i.e. for aspin conﬁgurationσ in{−1, +1}Λ, its energy is given by
HΛ
β,h(w) =−β
∑
i,j∈Λ
{i,j}∈EZd
σiσj −h
∑
i∈Λ
σi,
where EZd is the set of edges of the latticeZd and h and β are two real parameters withβ > 0. The
probabilityµβ,h,Λ[σ] of taking a conﬁgurationσ is then proportional toexp(−HΛ
β,h(σ)).
We now want to makeΛ grow to the whole latticeZd. It is well known that forh⁄= 0 orβ smaller than
a critical valueβc(d) (thus, at high temperature), there is a unique limiting probability measureµβ,h on
spin conﬁgurations onZd, seee.g. [FV16, Theorem 3.41]. In the following, we take parameters(β,h ) in
this domain of uniqueness and consider a random spin conﬁgurationσ, whose law isµβ,h.
In [DIS74], Duneau, Iagolnitzer and Souillard proved what they call thestrong cluster propertiesfor
spins in the Ising model forh⁄= 0 or suﬃciently smallβ. Their result is actually more general (it holds
for other models than the Ising model) but for simplicity, we stick to the Ising model here. Reformulated
with the terminology of the present article, we have:
Theorem 48 (Duneau,IagolnitzerandSouillard,1974). Fix the dimensiond≥ 1 andh⁄= 0, β >0.
Mod-φ convergence, II: Estimates on the speed of convergence 43
1. There existC = C(d,β,h ) and ε = ε(d,β,h ) < 1 such that under the probability measureµβ,h, the
family{σi, i∈ Zd} has aC-uniform weighted dependency graphG, where the weight of the edge{i,j}
in G is ε‖i−j‖1.
2. The same holds forh = 0 and β is suﬃciently small (i.e. β < β1(d), for someβ1(d) depending on
the dimension; this is sometimes refered to as the very high temperature regime).
Note that the maximal weighted degree of this graph is a constantC′ <∞.
We now consider the magnetization in a ﬁnite box∆ deﬁned asM∆ = ∑
i∈∆σi. We seeM∆ as
a sequence of random variables (indexed by the countably many ﬁnite subsets ofZd). Restricting the
uniform weighted dependency graph above to{σi, i∈ ∆}, each M∆ is the sum of random variables
with aC-uniform weighted dependency graph and maximal weighted degree at mostC′. Therefore, using
Proposition 44, we know thatM|∆| admits uniform bounds on cumulants with parameters(C′
2 ,|∆|,C ).
Moreover, since all spins are positively correlated by the FKG inequality (see [FV16, Section 3.6]), we
have, using translation invariance
Var(M∆)≥
∑
i∈∆
Var(σi) = Var(σ0)|∆|.
Note that Var(σ0) is independent of∆. With the notation of Section 4, this inequality ensures that~σ∆
is bounded from below by a constant. Applying Corollary 30, we get:
Proposition 49.Fix the dimensiond≥ 1 and parametersh⁄= 0, β >0. The exists a constantK =
K(d,β,h ) such that, for all subsets∆ of Zd, we have underµβ,h
dKol
(
M∆− E[M∆]√
Var(M∆)
,NR(0, 1)
)
≤ K√
|∆|
.
The same holds forh = 0 and β suﬃciently small (very high temperature).
Remark 50.In this remark, we discuss mod-Gaussian convergence in this setting. Consider a sequence
∆n of subsets ofZd, tending toZd in the Van Hove sense (i.e. the sequence is increasing with unionZd,
and the size of the boundary of∆n is asymptotic negligible, compared to the size of∆n itself). Then it
is known from [Ell85, Lemma 5.7.1] that
lim
n→∞
1
|∆| Var(M∆) =
∑
k∈Zd
Cov(σ0,σk),
and the right-hand side has a ﬁnite value~σ2(β,h ) for parameters (β,h ) for which Theorem 48 applies.
Similarly, we have
lim
n→∞
1
|∆|κ(3)(M∆) =
∑
k,l∈Zd
κ(σ0,σk,σl)<∞.
We callρ(β,h ) this quantity, and denoteL = ρ(β,h)
~σ3(β,h). Let us then consider the rescaled variables
Xn = M∆n− E[M∆n]
(Var(M∆n))1/3.
From [FMN16, Section 5] (withαn = Var(M∆) andβn = 1), we know thatXn converges in the complex
mod-Gaussian sense with parameterstn = (Var(M∆n))1/3 and limiting functionψ(z) = exp(Lz3
6 ). This
mod-Gaussian convergence takes place on the whole complex plane. Using the results of [FMN16], this
implies a normality zone for(M∆− E[M∆])/
√
Var(M∆) of sizeo(|∆|1/6), see Proposition 4.4.1 inloc.
cit.; and moderate deviation estimates at the edge of this normality zone, see Proposition 5.2.1.
Remark 51.Forh = 0 and β >βc(d) (low temperature regime), there is no weighted dependency graph
as above. Indeed, this would imply the analycity of the partition function in terms of the magnetic ﬁeld
44 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
h, and the latter is known not to be analytic ath = 0 for β > βc(d); see [MM91, Chapter 6, §5] for
details.
