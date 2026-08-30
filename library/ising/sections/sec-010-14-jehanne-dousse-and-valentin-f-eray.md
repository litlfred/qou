---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-010-14-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 14
pages: 14-16
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
In particular, in the domain of convergence of the cluster expansion, joint moments are nonzero. If a
clusterX has no vertex ofA in the interior of any of its contours, then ΨA
β (X) = Ψ∅
β(X). Such clusters
do not contribute to⟨σA⟩+
Λ;β,0. Therefore,
⟨σA⟩+
Λ;β,0 = exp

 ∑
X∼A:X⊆Λ
(ΨA
β (X)− Ψ∅
β(X))

,
where X∼A means that X contains at least one contour γ such that a point of A is in the interior
of γ. The series is absolutely convergent and we can let Λ ↑ Zd, obtaining the following proposition.
Proposition 3.8 (Equation (5.47) in [13]) . Forβ large enough,
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
for some set B and random variables (Yi)i∈B deﬁned on the same probability space with nonzero joint
moments,
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
, Q β,0(σ1,σ 2,σ 3) =
⟨σ1σ2σ3⟩+
β,0⟨σ1⟩+
β,0⟨σ2⟩+
β,0⟨σ3⟩+
β,0
⟨σ1σ2⟩+
β,0⟨σ1σ3⟩+
β,0⟨σ2σ3⟩+
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
By deﬁnition of Ψ, observe that, if I is as above, then Ψδ
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
[
(ΨI
β(X)− Ψβ(X))
∑
δ:
I⊆δ⊆(I∪(A\Int(X)))
(−1)|δ|
]
.
But the last sum is equal to 0 unless A is contained in Int(X), in which case it is (−1)|I|. Therefore
we obtain
logQ (σj;j∈A) =
∑
X:
A⊆Int(X)
∑
I⊆A:
I⁄=∅
(−1)|I|(ΨI
β(X)− Ψβ(X)).
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 15
Finally, there are 2r− 1 non-empty subsets of A, and|ΨI
β(X)|≤ Ψβ(X) :=|ϕ(X)|e−2β ∑r
j=1|γj| for all
X and I, thus
(3.7) |logQ (σj;j∈A)|≤
∑
X:
A⊆Int(X)
2(2r− 1)Ψβ(X).
We conclude by using a trick similar to Lemma 3.6. By [13, Equation (5.29)], if β≥ βlt
ce(d), for any
face f of anySi (i∈ Zd), we have the bound
∑
X:X∋f
Ψβ(X)≤ 1.
Thus if β≥ 2βlt
ce(d), ∑
X:X∋f
Ψβ(X)eβ|X|≤
∑
X:X∋f
Ψβ
2
(X)≤ 1.
So for any positive integer R,
(3.8)
∑
X:X∋f
|X|≥R
Ψβ(X)≤e−βR ∑
X:X∋f
Ψβ(X)eβ|X|≤e−βR.
Let us now turn back to Eq. (3.7). Every cluster X such that ϕ(X)⁄= 0 and A⊆ Int(X) satisﬁes
|X|≥ 2𝓁T (A). Moreover, if a cluster of size R has j1∈ A in its interior, then it contains at least a
face f which is at distance at most R of j1. There are at most CRd such points, for some constant
C =C(d), therefore
∑
X:
A⊆Int(X)
Ψβ(X)≤
∑
R≥2𝓁T (A)
CRd


∑
X:X∋f
|X|=R
Ψβ(X)


≤C
∑
R≥2𝓁T (A)
Rde−βR≤C
≤C′e−cβ𝓁T (A),
for β large enough, where C′ and c are some positive constants depending on the dimension d of the
ambient space. Thus by (3.7),
|logQ (σj;j∈A)|≤ C′
re−cβ𝓁T (A),
for some positive constant C′
r depending on r and d. Exponentiating completes the proof. □
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
where G is the weighted graph deﬁned on Zd such that for each e = (i,j ), one has we = e
−cβ‖i−j‖1
2 .
Indeed in that case M
(
G[A]
)
=e
−cβ𝓁′
T (A)
2 ≥e−cβ𝓁T (A); see the discussion in Section 2.2.
Then using [10, Proposition 5.8], we deduce that
|κβ,0 (σj;j∈A)| =
∏
j∈A
⟨σj⟩+
β,0×O (M
(
G[A]
)
).
The ﬁrst factor is trivially bounded by 1, while the second is bounded using Proposition 2.1:
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
