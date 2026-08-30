---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-007-3-cluster-expansions-and-bounds-on-joint-cumulan
section_title: "Cluster expansions and bounds on joint cumulants"
section_number: 3
pages: 8-10
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
The cluster expansion is a powerful tool in statistical mechanics, which consists in studying a system
in terms of macroscopic geometrical objects instead of considering its original microscopic components.
It was introduced in a work of Mayer and Montroll [28] studying molecular distribution and has since
been used in several other topics; for the Ising model, see for example [9] or Chapter 5 of [13]. In this
section, we will use the cluster expansion in three diﬀerent regimes of the Ising model to prove the
bounds on joint cumulants of Theorem 1.1. This will later be useful to apply the theory of weighted
dependency graphs. Theorem 1.1 is proved in Sections 3.1.2, 3.2.2 and 3.3, depending on the considered
regime.
Remark 3.1. In each section below, we use some classical notation for cluster expansion, such as Ξ, W,
X, . . . Note however that these quantities may have diﬀerent meanings in diﬀerent regimes. Since they
are only used for the proof of Theorem 1.1 and since the proofs in the diﬀerent regimes are independent
from each other, this should not create any diﬃculty.
3.1. At very high temperature, with a weak magnetic ﬁeld.
3.1.1. The cluster expansion of the (multivariate) moment generating function. Fix h1 > 0. For The-
orem 1.1, we will specialize h1 to the threshold value of the strong magnetic ﬁeld regime, but, in this
section, we work with an arbitrary value of h1. We consider the regime where |h|≤ h1 and β is
suﬃciently small (very high temperature and weak magnetic ﬁeld).
We ﬁx a ﬁnite domain Λ ⊂ Zd and let A ={x1,...,x r} be a set of points in Λ. We consider the
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
Λ;β,h
=
∑
ω∈ΩΛ exp
(∑r
j=1tjσxj(ω)
)
e−HΛ;β,h(ω)
ZΛ;β,h
.
To state the high temperature representation of this moment generating function, we need some
notation. Let us call ZA
Λ;β,h the numerator of the right-hand side. The denominator ZΛ;β,h is then
exactlyZ∅
Λ;β,h. For a subset E⊆E Zd, we denoteVo(E) the set of vertices in Zd that are incident to an
odd number of edges in E. As usual, we use ∆ for the symmetric diﬀerence operator on sets. Finally,
if E⊆E Zd and B⊆ Zd fulﬁll B∆Vo(E)⊆A, we deﬁne
W(E,B ) = (tanh β)|E|(tanh βh)|B| ∏
xj∈B∆Vo(E)
(tanh tj).
Lemma 3.2 (high temperature representation). We have
(3.1) ZA
Λ;β,h = (cosh β)|EΛ|(2 cosh βh)|Λ|


r∏
j=1
cosh(tj)

 ΞA
Λ;β,h,
where
ΞA
Λ;β,h =
∑
E⊆EΛ,B⊆Λ:
B∆Vo(E)⊆A
W(E,B ).
Proof: This proof is a straight-forward extension of the case A =∅ and h = 0, see e.g. [13, Eq.
(5.40)]. We write in short σi for σi(ω). Since every σi lies in{−1, +1}, we can write
exp(tjσxj) = cosh(tj) +σxj sinh(tj) = cosh(tj)
(
1 +σxj tanh(tj));
exp(βhσi) = cosh(βh)
(
1 +σi tanh(βh));
exp(βσiσj) = cosh(β)
(
1 +σiσj tanh(β)
)
.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 9
This gives the following expression for ZA
Λ;β,h:
ZA
Λ;β,h = (cosh β)|EΛ|(cosh βh)|Λ|


r∏
j=1
cosh(tj)


·
∑
ω∈ΩΛ


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
B⊆Λ
∏
i∈B
(σi tanh(βh))

·

∑
C⊆A
∏
xj∈C
(σxj tanh(tj))



.
Changing the order of summation we get
ZA
Λ;β,h = (cosh β)|EΛ|(cosh βh)|Λ|
( r∏
j=1
cosh(tj)
)
·

 ∑
E,B,C
tanh(β)|E| tanh(βh)|B|
( ∏
xj∈C
tanh(tj)
)
∑
ω∈ΩΛ
( ∏
{i,j}∈E
σiσj
∏
i∈B
σi
∏
xj∈C
σxj
)


,
where, as above, we sum over E⊆E Λ, B⊆ Λ and C⊆A. By an easy symmetry argument, the sum
in square brackets is zero unless all σi’s appear an even number of times, which corresponds to the
condition B∆Vo(E) =C. In this case, the sum is the number of spin conﬁgurations |ΩΛ| = 2|Λ|. This
ends the proof of the high temperature expansion. □
Pairs (E,B ) with E ⊆ EΛ and B ⊆ Λ can be considered as subgraphs of Λ, where the vertex
set V (E,B ) consists of B and of vertices incident to an edge of E and the edge-set is precisely E.
This graph has a unique decomposition (up to reordering) into s connected components, each again
being the graph of some ( Ei,Bi) (for 1 ≤ i≤ s). Clearly, if B∆Vo(E)⊆ A, then each ( Ei,Bi)
satisﬁes Bi∆Vo(Ei)⊆ A. Moreover, the weight function is multiplicative with respect to connected
components, i.e. W(E,B ) =∏
i W(Ei,Bi). Therefore using notation of [13],
ΞA
Λ;β,h = 1 +
∑
s≥1
1
s!
∑
(E1,B1),...,(Es,Bs)
connected
s∏
i=1
W(Ei,Bi)
∏
1≤i<j≤s
1
[
V (Ei,Bi)∩V (Ej,Bj) =∅
]
,
where 1[event] is the indicator function of the corresponding event. The last product in the above
display encodes the fact that connected components should not intersect. We set
ζ((E,B ), (E′,B′)) = 1
[
V (Ei,Bi)∩V (Ej,Bj) =∅
]
− 1,
as usual in cluster expansions.
To compute cumulants, we need an expansion of log
(⟨
exp
(∑r
j=1tjσxj
)⟩
Λ;β,h
)
and thus of
log(ΞA
Λ;β,h). Such an expansion will be given by the theory of cluster expansions, but we should
ﬁrst check some conditions ensuring convergence, e.g. the ones given in [13, Section 5.4]. For this, we
deﬁne
W(E,B ) = (tanh β)|E|| tanh βh||B|,
which dominates all functions W( E,B ) when the tj’s are complex parameters of moduli at most
tanh−1(1).
Lemma 3.3. There exists a constant βht
ce(d,h 1) such that the following holds for |h|≤ h1 and β <
βht
ce(d,h 1). For each ﬁxed pair (E⋆,B⋆) whereE⋆ and B⋆ are ﬁnite subsets of EZd and Zd respectively,
one has
S(E⋆,B⋆) :=
∑
E⊆EZd,B⊆Zd:
(E,B) connected
W(E,B )e|V (E,B)|⏐⏐ζ
[
(E,B ), (E⋆,B⋆)
]⏐⏐≤|V (E⋆,B⋆)|.
