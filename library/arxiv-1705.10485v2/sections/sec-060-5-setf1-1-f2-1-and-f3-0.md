---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-060-5-setf1-1-f2-1-and-f3-0
section_title: "Setf(1) = 1, f(2) =−1 and f(3) = 0;"
section_number: 5
pages: 50-52
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
one hasπ(f) = 0, and one computes
E[f(X0)f(Xk)] = 1
5
( 2 + i
(−1− i)k + 2− i
(−1 + i)k
)
.
It follows thatΣ2(f) = 0, althoughf is non zero.
In the general case of an ergodic Markov chain, ﬁx an elementa of the state space X, and denote
τa≥ 1 the ﬁrst hitting time ofa by the Markov chain, which is almost surely ﬁnite and with expectation
1/π(a) when starting froma. Then, the asymptotic varianceΣ2(f) can be rewritten as
Σ2(f) =π(a) Ea


( τa∑
k=1
g(Xk)
)2
,
see [KS76, Chapter 4]. Therefore, a general condition in order to obtain the bound of Eq. (13) is:
Proposition 58.We have Σ2(f) > 0 if and only if there exists a cycle (x1,...,x n) in the graph of
transitions of the Markov chain such that the sum∑n
i=1g(xi) of the values ofg = f−π(f) along this
cycle is non-zero. In this case, the bound(13) holds.
The proposition explains readily why the irreducible aperiodic Markov chain
1 2
3
1
1/2
1/21
previously studied gives asymptotic variance0 to the functionf(1) = 1, f(2) =−1 and f(3) = 0: the
minimal cycles of the chains are(1, 2) and (1, 2, 3), and the sum of the values off along these cycles is
always 0.
Mod-φ convergence, II: Estimates on the speed of convergence 51
Another simple criterion to apply Theorem 55 to linear functionals of the empirical measure is:
Proposition 59.Suppose that the ergodic Markov chain is reversible:
π(x)P (x,y ) =π(y)P (y,x )
for anyx,y. Then, iff is a non-constant function,Σ2(f)> 0 and the bound(13) holds.
Proof. To say thatP is reversible is equivalent to the fact thatP is a symmetric operator of the Hilbert
space L2( 1
π ). In particular, P has only real eigenvalues. Besides, the restriction of the operatorI +
2∑∞
k=1Pk to the space of functionsf with π(f) = 0 is well deﬁned, and it is an auto-adjoint operator
on this space with eigenvalues
1 +λ2
1−λ2
,..., 1 +λM
1−λM
,
where λ2≥ λ3≥···≥ λM are the real eigenvalues ofP diﬀerent from1. The quantities above are all
positive, and larger than1−θP
1+θP
(this value being obtained ifλM =−θP). Therefore,
Σ2(f) =
⟨
f
⏐⏐⏐⏐⏐
(
I + 2
∞∑
k=1
Pk
)
f
⟩
L2(π)
≥ 1−θP
1 +θP
π(f2)> 0.
We then obtain
dKol
(
Sn− E[Sn]√
Var(Sn)
,NR(0, 1)
)
≤ 77
(
‖g‖∞
√
M√
π(g2)
)3(1 +θP
1−θP
)7
2 1√n
for n large enough. ⊓ ⊔
Remark 60.In this remark, we discuss mod-Gaussian convergence for linear statistics of Markov chains.
We use the above notation and assume thatΣ2(f) > 0. Consider the third cumulant ofSn. One can
easily prove that
ρ = 1
n lim
n→∞
κ3(Sn) =
∑
j,k∈Z
κ(f(X0,Xj,Xk)),
where (Xt)t∈Z is a bi-inﬁnite stationary Markov chain with transition matrixP. (The sum on the right-
hand side is ﬁnite, as consequence of Proposition 54). Let us callρ this limit. We then consider the
rescaled random variables
Xn =
( Sn− E[Sn]
(Var(Sn))1/3
)
n∈N
.
As for the magnetization in the Ising model, from [FMN16, Section 5] (withαn = Var(Sn) and βn = 1),
we know thatXn converges in the mod-Gaussian sense with parameterstn = (Var(Sn))1/3 and limit
ψ(z) = exp( Lz3
6 ), with L = ρ
Σ3(f). Again, this mod-Gaussian convergence takes place on the whole
complex plane and implies a normality zone forSn/
√
Var(Sn) of sizeo(n1/6), see Proposition 4.4.1 inloc.
cit.; we also have moderate deviation estimates at the edge of this normality zone, see Proposition 5.2.1.
This mod-Gaussian convergence could also have been proved by using an argument of the perturbation
theory of linear operators, for which we refer to [Kat80]. Indeed, the Laplace transform ofXn writes
explicitly as
E[ezXn] =π (Pz,f )n 1,
where 1 is the column vector with all its entries equal to1, π is the stationary measure of the process,
and Pz,f is the inﬁnitesimal modiﬁcation of the transition matrix deﬁned by
Pz,f (i,j ) =P (i,j ) e
z(f (j)−π(f ))
(V ar(Sn ))1/3
.
Forz inazoneofcontrolofsize O(n1/3),onecangiveaseriesexpansionoftheeigenvaluesandeigenvectors
ofPz,f, which allows one to recover the mod-Gaussian convergence. The theory of cumulants and weighted
dependency graphs allows one to bypass these diﬃcult analytic arguments.
52 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
