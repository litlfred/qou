---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-010-3-cluster-expansions-and-bounds-on-joint-cumulan
section_title: "Cluster expansions and bounds on joint cumulants"
section_number: 3
pages: 8-16
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
The cluster expansion is a powerful tool in statistical mechanics, which consists in studying a system
in terms of macroscopic geometrical objects instead of considering its original microscopic components.
It was introduced in a work of Mayer and Montroll [23] studying molecular distribution and has since
been used in several other topics; for the Ising model, see for example [7] or Chapter 5 of [10]. In this
section, we will use the cluster expansion in three diﬀerent regimes of the Ising model to prove the
bounds on joint cumulants of Theorem 1.1. This will later be useful to apply the theory of weighted
dependency graphs. Theorem 1.1 is proved in Sections 3.1.2, 3.2.2 and 3.3, depending on the considered
regime.
Remark 3.1. As already mentioned, cluster expansion is a key step to obtain bounds for cumulants
in each of the three regimes. Therefore we will use each time classical notation for cluster expansion,
such as Ξ, wt, . . . Note however that these quantities may have diﬀerent meanings in diﬀerent regimes.
Since they are only used for the proof of Theorem 1.1 and since the proofs in the diﬀerent regimes are
independent from each other, this should not create any diﬃculty.
3.1. At very high temperature, without magnetic ﬁeld.
3.1.1. The cluster expansion of the (multivariate) moment generating function. Let us start with the
regime where h = 0 and β is suﬃciently small (very high temperature).
Fix a ﬁnite domain Λ ⊂ Zd and let A ={x1,...,x r} be a set of points in Λ. We consider the
(multivariate) moment generating function
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
Λ;β,0
=
∑
ω∈ΩΛ exp
(∑r
j=1tjσxj(ω)
)
e−HΛ;β,0(ω)
ZΛ;β,0
.
Let us call ZA
Λ;β,0 the numerator of the right-hand side. The denominator ZΛ;β,0 is then exactly
Z∅
Λ;β,0. Let Eeven
A (resp. Eeven
Λ,A ) be the set of pairs ( E,B ), where E⊂E Zd (resp. E⊂E Λ) and B⊆A
are such that a vertex of Λ is incident to an odd number of edges in E if and only if it is in B. For
such a pair (E,B ), we denote wt(E,B ) = (tanh β)|E|∏
j∈B(tanh tj).
Lemma 3.2 (high temperature representation). We have
(3.1) ZA
Λ;β,0 = 2|Λ|(cosh β)|EΛ|


r∏
j=1
cosh(tj)

 ΞA
Λ;β,0,
where ΞA
Λ;β,0 =∑
(E,B)∈E even
Λ,A
wt(E,B ).
Proof: This proof is a straight-forward extension of the case A =∅, see e.g. [10, Eq. (5.40)]. We
write in short σi for σi(ω). Since σxj is in{−1, +1}, we can write
exp(tjσxj) = cosh(tj) +σxj sinh(tj) = cosh(tj)
(
1 +σxj tanh(tj));
exp(βσiσj) = cosh(β)
(
1 +σiσj tanh(β)
)
.
This gives the following expression for ZA
Λ;β,0:
ZA
Λ;β,0 = (cosh β)|EΛ|


r∏
j=1
cosh(tj)

 ∑
ω∈ΩΛ

∑
E⊆EΛ
∏
{i,j}∈E
(σiσj tanh(β))

·

∑
B⊆A
∏
xj∈B
(σxj tanh(tj))

.
Changing the order of summation we should evaluate, for E⊆E Λ and B⊆A, the quantity
∑
ω∈ΩΛ
∏
{i,j}∈E
(σiσj)
∏
xj∈B
(σxj).
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 9
By an easy symmetry argument, this sum is zero unless all σi’s appear an even number of times,
which corresponds to the condition ( E,B )∈E even
Λ,A . In this latter case, the sum is the number of spin
conﬁgurations|ΩΛ| = 2|Λ|. This ends the proof of the high temperature expansion. □
Pairs (E,B ) inEeven
Λ,A can be considered as subgraphs of Λ, where the vertices are all vertices incident
to an edge of E and the edge-set is precisely E (vertices in B must be adjacent to at least one edge
in E). This graph has a unique decomposition (up to reordering) into r connected components, each
again being the graph of some (Ei,Bi) (for 1≤i≤r). Notice that the weight function is multiplicative
with respect to connected components, i.e. wt(E,B ) = ∏
i wt(Ei,Bi). Therefore using notation of
[10],
ΞA
Λ;β,0 = 1 +
∑
r≥1
1
r!
∑
(E1,B1),...,(Er,Br)
connected
r∏
i=1
wt(Ei,Bi)
∏
1≤i<j≤r
δ
[
(Ei,Bi), (Ej,Bj)
]
,
where δ
[
(Ei,Bi), (Ej,Bj)
]
= 1 if the graphs corresponding to ( Ei,Bi) and (Ej,Bj) do not share a
vertex, and 0 otherwise (this factor encodes the fact that connected components should not intersect).
We setζ((E,B ), (E′,B′)) =δ
[
(E,B ), (E′,B′)
]
− 1 as usual for cluster expansions.
To compute cumulants, we need an expansion of log
(⟨
exp
(
i∑r
j=1tjσxj
)⟩
Λ;β,0
)
and thus of
log(ΞA
Λ;β,0). Such an expansion will be given by cluster expansion, but we should ﬁrst check some con-
ditions ensuring convergence, e.g. the ones given in [10, Section 5.4]. We let wt(E,B ) = (tanh β)|E|,
which dominates all functions wt( E,B ) when the tj’s are complex parameters of moduli at most
tanh−1(1).
Lemma 3.3. For (E,B )∈E even
Λ,A , let a(E;B) =|V (E,B )|, that is the number of vertices in the graph
associated to (E,B ). Then, there exists a constant βht
ce(d) such that the following holds for β <βht
ce(d):
(1) for any Λ⊂ Z, we have
∑
(E,B)∈E even
Λ,A
|wt(E,B )|ea(E,B) <∞;
(2) for each ﬁxed pair (E⋆,B⋆) whereE⋆ is a ﬁnite subset of EZd and B⋆⊆A, one has
S(E⋆,B⋆) :=
∑
(E,B)∈Eeven
A
(E,B) connected
|wt(E,B )|ea(E,B)|ζ
[
(E,B ), (E⋆,B⋆)
]
|≤ a(E⋆,B⋆).
Remark 3.4. To prove the convergence of cluster expansion, it is actually enough to prove a weaker
version of Item (2), where ( E⋆,B⋆) is necessarily in Eeven
Λ,A and the sum only runs on ( E,B )∈E even
Λ,A .
The stronger version stated here will nevertheless be useful in the proof of Lemma 3.6 below and is
proved in the same way, which explains our choice.
Proof: The ﬁrst condition is trivial since the set Eeven
Λ,A is ﬁnite. Let us consider the second one. By
deﬁnition, ζ
[
(E,B ), (E⋆,B⋆)
]
=−1 if (E,B ) and (E⋆,B⋆) share a vertex and 0 otherwise. Thus
S(E⋆,B⋆)≤
∑
v∈V (E⋆,B⋆)


∑
E⊂EZd,B⊂Zd s.t. (E,B) connected
and v∈V (E,B)
|wt(E,B )|e|V (E,B)|

.
A simple translation argument shows that the quantity between brackets is independent of v so that
S(E⋆,B⋆)≤|V (E⋆,B⋆)|


∑
E⊂EZd,B⊂Zd s.t. (E,B) connected
and 0∈V (E,B)
|wt(E,B )|e|V (E,B)|

.
Note that (E,B ) connected implies in particular that B is included in the vertex set of the graph
associated to E. Therefore the sum can be simpliﬁed as a sum only over E by paying a factor
10 JEHANNE DOUSSE AND VALENTIN F ´ERAY
2|V (E,B)|. Moreover connectedness implies |V (E,B )|≤| E| + 1. Thus we get:
S(E⋆,B⋆)≤|V (E⋆,B⋆)|


∑
E⊂EZd connected
s.t. 0∈V (E)
2|E|+1 (tanh β)|E|e|E|+1

.
The summand depends only on the size k ofE. From [10, Lemma 3.59], the number of connected sets
E⊂E Zd containing 0 of size k is bounded from above by (2d)2k, so that
S(E⋆,B⋆)≤|V (E⋆,B⋆)|

∑
k≥1
(2d)2k 2k+1 (tanh β)kek+1

.
Forβ small enough, sayβ <βht
ce(d), the sum is smaller than 1 and the second inequality is fulﬁlled. □
We can now state the cluster expansion of log(Ξ A
Λ;β,0). In this context, a cluster is a multiset
X ={(E1,B 1),..., (Er,Br)} of elements of Eeven
Λ,A . The multiplicity of ( E,B ) in the multiset X is
denotednX(E,B ). The support X is the union of the vertex-sets V (Ei,Bi). We say that two clusters
intersect if ζ
[
(E,B ), (E⋆,B⋆)
]
=−1 i.e. if they share a vertex.
Proposition 3.5. Forβ <βht
ce(d), We have the following expansion:
(3.2) log(Ξ A
Λ;β,0) =
∑
X:X⊂Λ
Ψβ(X),
where for a cluster X ={(E1,B 1),..., (Er,Br)},
Ψβ(X) :=

 ∏
(E,B)∈E even
Λ,A
1
nX(E,B )!

 φ((E1,B 1),..., (Er,Br))
( r∏
i=1
wt(Ei,Bi)
)
,
where
φ((E1,B 1),..., (Er,Br)) =
∑
G⊂Gr connected

 ∏
{i,j}∈G
ζ
[
(Ei,Bi), (Ej,Bj)
]

,
and Gr denotes the complete graph on r vertices. The convergence of the series in Eq. (3.2) holds in
the sense of locally uniform convergence of analytic functions in the complex parameters t1, . . . ,tr for
|t1|,..., |tr|≤ tanh−1(1).
Proof: This follows from the general theory of cluster expansions, see e.g. [10, Chapter 5]. For the
analyticity in the parameters, see speciﬁcally [10, Section 5.5]. □
Notice that the functionalφ((E1,B 1),..., (Er,Br)) depends only on which pairs (Ei,Ej) intersect and
vanishes if X can be split into two mutually non-intersecting subsets.
3.1.2. Bounds on joint cumulants. Recall that A ={x1,...,x r} is a set of points in the ﬁnite domain
Λ. The joint cumulant κΛ;β,0(σx1,...,σ xr) is the coeﬃcient of t1...t r in
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
Λ,β,0
= logZA
Λ;β,0− logZ∅
Λ;β,0
=|Λ| log 2 +|EΛ| log(cosh β) +
r∑
j=1
log(cos tj) + log ΞA
Λ;β,0− logZ∅
Λ;β,0.
Only the summand log ΞA
Λ;β,0 contributes to the coeﬃcient oft1...t r. Therefore, using Proposition 3.5,
we have
(3.3) κΛ;β,0(σx1,...,σ xr) = [t1...t r]
∑
X:X⊂Λ
Ψβ(X) =
∑
X:X⊂Λ
[t1...t r]Ψβ(X).
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 11
The exchange of inﬁnite sum and coeﬃcient extraction is valid since we have uniform convergence of
analytic functions on a neighborhood of 0. A cluster X ={(E1,B 1),..., (Er,Br)} contributes to the
coeﬃcient of t1...t r only if A =B1⨄···⨄ Br⊆X. Then
[t1...t r]Ψβ(X) =

 ∏
(E,B)∈Eeven
Λ,A
1
nX(E,B )!

 ϕ((E1,B 1),..., (Er,Br)) (tanhβ)e(X)
≤Cr 1[X is connected] (tanhβ)e(X),
wheree(X) =|E1| +··· +|Er| and 1[event] is the indicator function of the corresponding event. Back
to Eq. (3.3), we get
|κΛ;β,0(σx1,...,σ xr)|≤
∑
X:X⊂Λ,X connected,
and A⊆X
Cr(tanhβ)e(X).
Taking the limit Λ↑ Zd, we get a similar upper bound for the cumulant κβ,0(σx1,...,σ xr) under the
probability measure µβ,0 corresponding to the whole lattice Zd:
(3.4) |κβ,0(σx1,...,σ xr)|≤
∑
X connected
s.t. A⊆X
Cr(tanhβ)e(X).
The key point in the above formula is that any connected cluster X withA⊆X fulﬁllse(X)≥𝓁T (A).
We now need the following lemma, whose proof is inspired by the end of the proof of Theorem 5.27 in
[10].
Lemma 3.6. There exist constants βht
jc (d) > 0 and ε > 0 such that, for β≤ βht
jc (d), we have the
following inequality: ∑
X connected
s.t. x1∈Xande(X)≥R
(tanhβ)e(X)≤εR.
Proof: The proof involves diﬀerent values of the inverse temperature β so that we will here make
explicit the dependency of the weight in β: we write wtβ(E,B ) instead of wt(E,B ). We ﬁrst prove
that for β′≤βht
jc (d), we have
(3.5)
∑
X connected
s.t. x1∈X
(tanhβ′)e(X) =
∑
X connected
s.t. x1∈X
r∏
i=1
wtβ′(Ei,Bi)≤ 1.
This uses the same argument as in [10, Eq. (5.31)]:
∑
X connected
s.t. x1∈X
r∏
i=1
wtβ′(Ei,Bi)≤
∑
r≥1
r
∑
(E1,B1) connected
s.t. x1∈V (E1,B1)
∑
(E2,B2),...,(Er,Br)
r∏
i=1
wtβ′(Ei,Bi)
≤
∑
(E1,B1) connected
s.t. x1∈V (E1,B1)
wtβ′(E1,B 1)e|a(E1,B1)|≤a(∅,{x1}) = 1,
where we used Lemma 3.3 and [10, Theorem 5.4]. This proves (3.5).
Let us ﬁx a value β′ as above. There exists a constant ε< 1 such that for β small enough, we have
tanhβ <ε tanhβ′. We can now write
∑
X connected
s.t. x1∈Xand e(X)≥R
(tanhβ)e(X)≤εR ∑
X connected
s.t. x1∈Xand e(X)≥R
(tanhβ′)e(X)≤εR,
where the last inequality uses (3.5). This ends the proof of the lemma. □
12 JEHANNE DOUSSE AND VALENTIN F ´ERAY
Combining Eq. (3.4) and Lemma 3.6, we get the desired bound: for β≤βht
jc (d),
|κβ,0(σx1,...,σ xr)|≤ Crε𝓁T (A).
3.2. At very low temperature, without magnetic ﬁeld.
3.2.1. The cluster expansion of the partition function. We now turn to the regime without magnetic
ﬁeld (h = 0) and very low temperature (β large). Intuitively, in that case, the spin conﬁgurations with
fewer pairs of neighbours having opposite spins appear with higher probability. To emphasize the role
of these pairs, we rewrite the Hamiltonian as follows:
Hη
Λ;β,h(ω) =−β|Eη
Λ|− β
∑
{i,j}∈Eη
Λ
(σi(ω)σj(ω)− 1).
The only non-zero terms in the sum are those where two neighbours i and j have opposite spins. Let
us consider a ﬁnite subset Λ ⊂ Zd with + boundary condition. A typical spin conﬁguration will then
look as a sea of +’s with some islands of −’s. Therefore the interesting macroscopic components for
the cluster expansion in that case are the frontiers between the areas of +’s and those of −’s, which
are called contours. Let us deﬁne them more rigorously.
Given ω∈ Ω+
Λ, let Λ−(ω) denote the set of lattice points i where σi(ω) =−1. For each i∈ Zd we
deﬁneSi :=i + [−1
2 , 1
2]d to be the unit cube of Rd centred at i. Now let
M(ω) :=
⋃
i∈Λ−(ω)
Si,
and consider the set of maximal connected components of the boundary of M(ω), which we denote
Γ′(ω) ={γ1,...,γ r}.
Each of theγi’s is a contour ofω. Contours are connected sets of (d−1)-dimensional faces of the cubes
Si. We denote by |γi| the number of such faces in γi. Let Γ Λ :={γ∈ Γ′(ω) :ω∈ Ω+
Λ} denote the set
of all possible contours in Λ. Finally, a collection of contours Γ′⊂ ΓΛ is said to be admissible if there
exists a spin conﬁguration ω∈ Ω+
Λ such that Γ′(ω) = Γ′.
Thus when Λ is simply connected (which we will assume from now on in this paper), the partition
function can be rewritten as
Z+
Λ;β,0 =eβ|E+
Λ|Ξ+
Λ;β,0,
where
Ξ+
Λ;β,0 :=
∑
Γ′⊂ΓΛadmissible
∏
γ∈Γ′
e−2β|γ|.
The cluster expansion is an expression for log Ξ+
Λ;β,0 as an absolutely convergent series. In this case,
a cluster is a collection X ={γ1,...,γ r} of contours such that for every two contours γi andγj, there
is a “path” of faces of contours of X connecting γi and γj. Note that X is actually a multiset, and
denote bynX(γ) the number of copies ofγ appearing inX and byX the support ofX, ieX =∪γ∈Xγ.
In the following we write X⊆ Λ to say that X⊆∪ i∈ΛSi as subsets of Rd.
In can be shown (see e.g. [10, Chapter 5]) that the cluster expansion converges for β large enough.
Proposition 3.7. There exists βlt
ce(d) such that for all β >βlt
ce(d),
log Ξ+
Λ;β,0 =
∑
X:X⊆Λ
Ψβ(X),
where for a cluster X ={γ1,...,γ r},
Ψβ(X) :=

∏
γ∈ΓΛ
1
nX(γ)!

φ(γ1,...,γ r)e−2β ∑r
i=1|γi|,
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 13
where
φ(γ1,...,γ r) =
∑
G⊆Grconnected
∏
{i,j}∈G
ζ(γi,γj),
ζ(γi,γj) :=
{
0 if γi∩γj =∅,
−1 otherwise,
and Gr denotes the complete graph on r vertices.
3.2.2. Bounds on joint cumulants. This cluster expansion can be used to compute expectations and
therefore deduce some bounds on joint cumulants.
Let A⊆ Λ and let us deﬁne σA :=∏
i∈Aσi. Its expectation is given by
⟨σA⟩+
Λ;β,0 =
∑
ω∈Ω+
Λ
σA(ω)e−HΛ;β,0(ω)
Z+
Λ;β,0
.
For any spin conﬁguration ω∈ Ω+
Λ and any contour γ∈ Γ′(ω), let us deﬁne the interior of γ (written
Int(γ)) as the set of points of Λ which would have spin −1 if γ was the only contour of ω. We also
write Int(X) :=⋃
γ∈X Int(γ). Thus for any ω∈ Ω+
Λ and any i∈ Λ,
σi(ω) = (−1)|{γ∈Γ′(ω):i∈Int(γ)}|,
and thus
σA(ω) = (−1)
∑
i∈A|{γ∈Γ′(ω):i∈Int(γ)}|
= (−1)
∑
γ∈Γ′(ω)|{i∈A:i∈Int(γ)}|.
Therefore one can write
⟨σA⟩+
Λ;β,0 =
Ξ+,A
Λ;β,0
Ξ+
Λ;β,0
,
where
Ξ+,A
Λ;β,0 :=
∑
Γ′⊆ΓΛadmissible
∏
γ∈Γ′
(−1)|{i∈A:i∈Int(γ)}|e−2β|γ|.
The cluster expansion converges, which means that we have an analogue of Proposition 3.7 for Ξ +,A
Λ;β,0,
and thus⟨σA⟩+
Λ;β,0 can be expressed as
⟨σA⟩+
Λ;β,0 = exp

 ∑
X:X⊆Λ
ΨA
β (X)−
∑
X:X⊆Λ
Ψβ(X)

,
where for a cluster X ={γ1,...,γ r},
ΨA
β (X) :=

∏
γ∈ΓΛ
1
nX(γ)!



 ∑
G⊆Grconnected
ζ(γi,γj)


× (−1)
∑r
j=1|{i∈A:i∈Int(γj)}|e−2β ∑r
j=1|γj|.
For all clusters X such that no vertex of A is in the interior of any of its contours, the exponent of
(−1) in the deﬁnition of Ψ A
β (X) is always 0 and thus ΨA
β (X) = Ψβ(X). Therefore we obtain
⟨σA⟩+
Λ;β,0 = exp

 ∑
X∼A:X⊆Λ
(ΨA
β (X)− Ψβ(X))

,
where X∼A means that X contains at least one contour γ such that a point of A is in the interior
of γ. The series is absolutely convergent and we can let Λ ↑ Zd, obtaining the following proposition.
14 JEHANNE DOUSSE AND VALENTIN F ´ERAY
Proposition 3.8 (Equation (5.49) in [10]) . Forβ large enough,
⟨σA⟩+
β,0 = exp
(∑
X∼A
(ΨA
β (X)− Ψβ(X))
)
.
We now want to ﬁnd estimates on the joint cumulants of the variables {σi :i∈A}, for all A⊂ Zd
ﬁnite. But in this case, it is easier to estimate ﬁrst another quantity related to cumulants. We deﬁne,
for some set B and random variables (Yi)i∈B deﬁned on the same probability space,
Q (Yj;j∈B) :=
∏
δ⊆B
δ⁄=∅
⟨∏
j∈δ
Yj
⟩(−1)|δ|
.
For example,
Qβ,0(σ1,σ 2) =
⟨σ1σ2⟩+
β,0
⟨σ1⟩+
β,0⟨σ2⟩+
β,0
.
We show a bound on the quantities Qβ,0 (σj;j∈A) for all ﬁnite A⊂ Zd.
Lemma 3.9. LetA be a ﬁnite subset of Zd of size r. Then for β large enough,
|Qβ,0 (σj;j∈A)− 1|≤ Cre−cβ𝓁T (A),
wherec =c(d) and Cr are positive constants depending respectively on d and r.
Proof: Using Proposition 3.8, we have
logQ (σj;j∈A) =
∑
δ⊆A,δ⁄=∅
(−1)|δ|∑
X∼δ
(Ψδ
β(X)− Ψβ(X)).
Recall that X∼δ means that at least one point of δ is in the interior of a contour in X. We split the
second sum depending on the exact subset I⊆δ of points that are in the interior of a contour in X.
By deﬁnition of Ψ observe, if I is as above, Ψδ
β(X) = ΨI
β(X). Therefore
logQ (σj;j∈A) =
∑
δ⊆A,δ⁄=∅
(−1)|δ|∑
I⊆δ:
I⁄=∅
∑
X:
Int(X)∩δ=I
(ΨI
β(X)− Ψβ(X))
=
∑
I⊆A:
I⁄=∅
∑
X:
I⊆Int(X)
(ΨI
β(X)− Ψβ(X))
∑
δ:
I⊆δ⊆(I∪(A\Int(X)))
(−1)|δ|.
But the last sum is equal to 0 unless A is contained in Int(X). Therefore we obtain
logQ (σj;j∈A) =
∑
X:
A⊆Int(X)
∑
I⊆A:
I⁄=∅
(−1)|I|(ΨI
β(X)− Ψβ(X)).
Finally, there are 2r− 1 non-empty subsets of A, and|ΨI
β(X)|≤| Ψβ(X)| for all X and I, thus
(3.6) |logQ (σj;j∈A)|≤
∑
X:
A⊆Int(X)
2(2r− 1)|Ψβ(X)|.
We conclude by using a trick similar to Lemma 3.6. By [10, Equation (5.31)], if β≥ βlt
ce(d), for any
vertexv∈ Zd, we have the bound ∑
X:X∋v
|Ψβ(X)|≤ 1.
Thus if β≥ 2βlt
ce(d), ∑
X:X∋v
⏐⏐⏐Ψβ(X)eβ|X|
⏐⏐⏐≤
∑
X:X∋v
⏐⏐⏐Ψβ
2
(X)
⏐⏐⏐≤ 1.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 15
So for any positive integer R,
(3.7)
∑
X:X∋v
|X|≥R
|Ψβ(X)|≤ e−βR ∑
X:X∋v
⏐⏐⏐Ψβ(X)eβ|X|
⏐⏐⏐≤e−βR.
Let us now turn back to Eq. (3.6). Every cluster X such that A⊆ Int(X) satisﬁes |X|≥ 2𝓁T (A).
Moreover, if a cluster of size R has j1∈A in its interior, then it contains at least a point v which is
at distance at most R of j1. There are at most CRd such points, therefore
∑
X:
A⊆Int(X)
|Ψβ(X)|≤
∑
R≥2𝓁T (A)
CRd


∑
X:X∋v
|X|=R
|Ψβ(X)|


≤C
∑
R≥2𝓁T (A)
Rde−βR
≤C′e−cβ𝓁T (A),
for β large enough, where C′ and c are some positive constants (and c depends on the dimension d of
the ambiant space). Thus by (3.6),
|logQ (σj;j∈A)|≤ C′
re−cβ𝓁T (A),
for some positive constant C′
r depending on r. Exponentiating completes the proof. □
Now we can convert this estimate into the desired bound on joint cumulants.
Proposition 3.10. LetA be a ﬁnite subset of Zd of size r. Then, for β large enough,
|κβ,0 (σj;j∈A)|≤ Dre
−cβ𝓁T (A)
2 ,
wherec =c(d) is given by Lemma 3.9 and Dr is a positive constant depending on r.
Proof: By Lemma 3.9,
Qβ,0 (σj;j∈A) = 1 +O(M
(
G[A]
)
),
where G is the weighted graph deﬁned on Zd such that for each e = (i,j ), we =e
−cβ‖i−j‖1
2 . Indeed in
that caseM
(
G[A]
)
=e
−cβ𝓁′
T (A)
2 ≥e−cβ𝓁T (A); see the discussion in Section 2.3.
Then using Proposition 5.8 of [8], we deduce that
|κβ,0 (σj;j∈A)| =
∏
j∈A
⟨σj⟩+
β,0×O (M
(
G[A]
)
).
But for all j∈A, we have⟨σj⟩+
β,0≤ 1, and for β large enough,⟨σj⟩+
β,0 > 0. Hence
0<
∏
j∈A
⟨σj⟩+
β,0≤ 1.
Moreover by Proposition 2.2,
M
(
G[A]
)
=e
−cdβ𝓁′
T (A)
2 ≤e
−cdβ𝓁T (A)
2 .
Thus|κβ,0 (σj;j∈A)|≤ Dre
−cdβ𝓁T (A)
2 , as claimed. □
16 JEHANNE DOUSSE AND VALENTIN F ´ERAY
3.3. With a strong magnetic ﬁeld. The last regime we consider is the Ising model with a strong
magnetic ﬁeld, i.e. h is bigger than some value h1 > 0 (h1 is to be determined later). The case of
negativeh (smaller than−h1 < 0) is obviously symmetric.
In this regime, there is also a well-known cluster expansion for the partition function [10, Section
5.7]. Let us present it brieﬂy.
Fix Λ ⊂ Zd and consider the Ising model on Λ with + boundary conditions. We ﬁrst write its
partition function in a suitable form. For a subset Λ − of Λ, we denote
δeΛ− ={{i,j}∈E b
Λ, i∈ Λ−, j /∈ Λ−}.
Deﬁne also wt(Λ−) = exp(−2β|δeΛ−|− 2h|Λ−|). Then we have:
Lemma 3.11 (strong magnetic ﬁeld representation). With the above notation,
Z+
Λ,β,h = exp
(
β|Eb
Λ| +h|Λ|
)

 ∑
Λ−⊆Λ
wt(Λ−)

.
Proof: The proof is not diﬃcult and can be found, e.g., in [10, Section 5.7]. It is important to
note that the sum over Λ −⊆ Λ corresponds to the sum over spin conﬁgurations in the deﬁnition of
the partition function: the correspondence simply associates with a spin conﬁguration the set Λ − of
positions of its minus spins. □
Let A be a subset of Λ. It is straightforward to modify the argument to ﬁnd a similar expression for
the numerators of⟨σA⟩ (as in Section 3.2) or of
⟨
exp
(∑
i∈Atiσi
)⟩
(as in Section 3.1).
∑
ω∈ΩΛ
σA(ω)e−H+
Λ;β,h(ω) = exp
(
β|Eb
Λ| +h|Λ|
)

 ∑
Λ−⊆Λ
(−1)|A∩Λ−| wt(Λ−)

.(3.8)
∑
ω∈ΩΛ
exp
(∑
i∈A
tiσi
)
=e exp
(
β|Eb
Λ| +h|Λ| +
∑
i∈A
ti
)
 ∑
Λ−⊆Λ
[ ∏
i∈A∩Λ−
exp(−2ti)
]
wt(Λ−)

.(3.9)
A set Λ−⊆ Λ can be seen as a subgraph of the lattice Zd. As such, it admits a unique decomposition
as disjoint union of its connected components Λ − = S1⊔S2⊔···⊔ Sr. The weight wt behaves
multiplicatively with respect to this decomposition wt(Λ −) = ∏r
i=1 wt(Si); the same is true for the
modiﬁed weights (−1)|A∩Λ−| wt(Λ−) and
[∏
i∈A∩Λ− exp(−2ti)
]
wt(Λ−) which appear in Eqs. (3.8)
and (3.9) above. This enables us to use the technique of cluster expansion.
The convergence of this cluster expansion is proved for the partition function in [10, Section 5.7].
The argument can be directly adapted to get a cluster expansion of the expression in Eqs. (3.8)
and (3.9) above. The same reasoning as in Section 3.1 or in Section 3.2 leads to similar bounds on
joint cumulants, which proves Theorem 1.1 in the strong magnetic ﬁeld regime.
