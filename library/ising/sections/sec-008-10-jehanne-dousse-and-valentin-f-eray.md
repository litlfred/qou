---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-008-10-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 10
pages: 10-12
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
Remark 3.4. To prove the convergence of cluster expansion, it is actually enough to prove a weaker
version of this lemma, where E⋆ andB⋆ fulﬁlB⋆∆Vo(E⋆)⊆A and where the sum only runs over pairs
(E,B ) with the additional conditions E⊆E Λ,B⊆ Λ and B∆Vo(E)⊆A. The stronger version stated
here will be useful in the proof of Lemma 3.6 below.
Proof: By deﬁnition, ζ
[
(E,B ), (E⋆,B⋆)
]
=−1 if (E,B ) and (E⋆,B⋆) share a vertex and 0 otherwise.
Thus
S(E⋆,B⋆)≤
∑
v∈V (E⋆,B⋆)


∑
E⊂EZd,B⊂Zd s.t. (E,B) connected
and v∈V (E,B)
W(E,B )e|V (E,B)|

.
A simple translation argument shows that the quantity in the brackets is independent of v, so that
S(E⋆,B⋆)≤|V (E⋆,B⋆)|


∑
E⊂EZd,B⊂Zd s.t. (E,B) connected
and 0∈V (E,B)
W(E,B )e|V (E,B)|

.
Note that (E,B ) connected implies in particular that B is included in the vertex set of the graph
associated to E. For such pair ( E,B ), we therefore have W(E,B ) ≤ (tanh β)|E|(tanh βh)|V (E)|.
Moreover, for a givenE, the number of corresponding sets B is 2|V (E)|. Finally, connectedness implies
|V (E,B )| =|V (E)|≤| E| + 1. Thus we get:
S(E⋆,B⋆)≤|V (E⋆,B⋆)|


∑
E⊂EZd connected
s.t. 0∈V (E)
2|E|+1 (tanh β)|E|| tanh βh||E|+1e|E|+1

.
The summand depends only on the size k ofE. From [13, Lemma 3.59], the number of connected sets
E⊂E Zd containing 0 of size k is bounded from above by (2d)2k, so that
S(E⋆,B⋆)≤|V (E⋆,B⋆)|

∑
k≥1
(2d)2k (tanh β)k (2e| tanβh|)k+1

.
Forβ small enough, uniformly on h with|h|≤ h1, sayβ <βht
ce(d,h 1), the sum is smaller than 1, which
proves the lemma. □
We can now state the cluster expansion of log(ΞA
Λ;β,h). In the remaining part of Section 3.1, we
write X to represent a list (( Ei,Bi))1≤i≤s of pairs of subsets of EZd and Zd, where each ( Ei,Bi)
should correspond to a connected graph and satisfy Bi∆Vo(Ei)⊆A. Such a list is called an (ordered)
cluster. We also write |X| = s for its length, W( X) =∏s
i=1 W(Ei,Bi) for its weight and lastly
X =⋃s
i=1V (Ei,Bi) for its support.
Proposition 3.5. Forβ <βht
ce(d,h 1) and|h|≤ h1, we have the following expansion:
(3.2) log(Ξ A
Λ;β,h) =
∑
X
ϕ(X) W(X),
where the sum runs over clusters X of all lengths s≥ 1,
ϕ(X) =ϕ((E1,B 1),..., (Es,Bs)) = 1
s!
∑
G⊆Gs connected

 ∏
{i,j}∈G
ζ
[
(Ei,Bi), (Ej,Bj)
]

,
and Gs denotes the complete graph on s vertices. The convergence of the series in Eq. (3.2) holds in
the sense of locally uniform convergence of analytic functions in the complex parameters t1, . . . ,tr for
|t1|,..., |tr|≤ tanh−1(1).
Proof: This follows from Lemma 3.3 and the general theory of cluster expansions, see e.g. [13, Chapter
5]. For the analyticity in the parameters, see speciﬁcally [13, Section 5.5]. □
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 11
3.1.2. Bounds on joint cumulants. Recall that A ={x1,...,x r} is a set of points in the ﬁnite domain
Λ. The joint cumulant κΛ;β,h(σx1,...,σ xr) is the coeﬃcient of t1...t r in
log
⟨
exp


r∑
j=1
tjσxj


⟩
Λ,β,h
= logZA
Λ;β,h− logZ∅
Λ;β,h
=|Λ| log(2 cosh βh) +|EΛ| log(cosh β) +
r∑
j=1
log(cos tj) + log ΞA
Λ;β,h− logZ∅
Λ;β,h.
Only the summand log ΞA
Λ;β,h contributes to the coeﬃcient of t1...t r. Using Proposition 3.5, we have
(3.3) κΛ;β,h(σx1,...,σ xr) = [t1...t r]
∑
X:X⊆Λ
ϕ(X) W(X) =
∑
X:X⊆Λ
ϕ(X) [t1...t r] W(X).
The exchange of inﬁnite sum and coeﬃcient extraction is valid since we have uniform convergence of
analytic functions on a neighborhood of 0. A cluster X contributes to the coeﬃcient of t1...t r only if
(3.4) ( B1∆Vo(E1))⨄···⨄ (Bs∆Vo(Es)) =A.
In particular, we should have A⊆X. When (3.4) is fulﬁlled, since [ ti] tanh(ti) = 1, we have
[t1...t r] W(X) = (tanhβ)e(X)(tanhβh)b(X),
where e(X) =|E1| +··· +|Es| and b(X) =|B1| +··· +|Bs|. Back to Eq. (3.3), we get
⏐⏐κΛ;β,h(σx1,...,σ xr)
⏐⏐≤
∑
X:
A⊆X⊆Λ
|ϕ(X)| (tanhβ)e(X)| tanhβh|b(X).
Taking the limit Λ↑ Zd, we get a similar upper bound for the cumulant κβ,h(σx1,...,σ xr) under the
probability measure µβ,h corresponding to the whole lattice Zd:
⏐⏐κβ,h(σx1,...,σ xr)
⏐⏐≤
∑
X:
A⊆X
|ϕ(X)| (tanhβ)e(X)| tanhβh|b(X).
But, by deﬁnition, ϕ(X) = 0 unless the graph corresponding to ( ⋃s
i=1Ei,⋃s
i=1Vi) is connected.
Together with the condition A⊆X, this forces e(X)≥𝓁T (A). Hence, we can write
(3.5)
⏐⏐κβ,h(σx1,...,σ xr)
⏐⏐≤
∑
X:
x1∈X,e (X)≥𝓁T (A)
|ϕ(X)| (tanhβ)e(X)| tanhβh|b(X).
We now bound the right-hand side in the following lemma, whose proof is inspired by the end of the
proof of Theorem 5.16 in [13].
Lemma 3.6. Fix h1 > 0. Then there exist constants βht
jc (d,h 1) > 0 and ε >0 such that, for (β,h )
with β≤βht
jc (d) and|h|≤ h1, we have the following inequality:
∑
X: x1∈Xand e(X)≥R
|ϕ(X)| (tanhβ)e(X)| tanhβh|b(X)≤εR.
Proof: The proof involves diﬀerent values of the parameter ( β,h ) so that we will here make explicit
the dependency of the weight in (β,h ): we write W(β,h)(E,B ) instead of W(E,B ). We ﬁrst prove the
following inequality: for β′ <β ht
ce(d,h 1), we have
(3.6)
∑
X: x1∈X
|ϕ(X)| (tanhβ′)e(X)(tanhβ′h1)b(X) =
∑
X: x1∈X
|ϕ(X)|
r∏
i=1
W(β′,h1)(Ei,Bi)≤ 1.
