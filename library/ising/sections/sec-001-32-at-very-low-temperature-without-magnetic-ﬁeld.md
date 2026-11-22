---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-001-32-at-very-low-temperature-without-magnetic-ﬁeld
section_title: "At very low temperature, without magnetic ﬁeld."
section_number: 3.2
pages: 12-16
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
toc_source: inferred
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
3.2.1. The cluster expansion of the partition function. We now turn to the regime without magnetic
ﬁeld (h = 0) and very low temperature (β large). Intuitively, in that case, the spin conﬁgurations with
fewer pairs of neighbours having opposite spins appear with higher probability. To emphasize the role
of these pairs, we rewrite the Hamiltonian as follows:
Hη
Λ;β,0(ω) = −β|Eη
Λ| −β
X
{i,j}∈Eη
Λ
(σi(ω)σj(ω) −1).
The only non-zero terms in the sum are those where two neighbours i and j have opposite spins. Let
us consider a ﬁnite subset Λ ⊂Zd with + boundary condition. A typical spin conﬁguration will then
look as a sea of +’s with some islands of −’s. Therefore the interesting macroscopic components for
the cluster expansion in that case are the frontiers between the areas of +’s and those of −’s, which
are called contours. Let us deﬁne them more rigorously.
Given ω ∈Ω+
Λ, let Λ−(ω) denote the set of lattice points i where σi(ω) = −1. For each i ∈Zd we
deﬁne Si := i + [ −1
2 , 1
2]d to be the unit cube of Rd centred at i. Now let
U(ω) :=
[
i∈Λ−(ω)
Si,
and consider the set of maximal connected components of the boundary of U(ω), which we denote
Γ′(ω) = {γ1, . . . , γr}.
Each of the γi’s is a contour of ω. Contours are connected sets of closed (d −1)-dimensional faces of
the cubes Si. We denote by |γi| the number of such faces in γi. Let ΓΛ := {γ ∈Γ′(ω) : ω ∈Ω+
Λ} denote
the set of all possible contours in Λ. Finally, a collection of contours Γ′ ⊂ΓΛ is said to be admissible
if there exists a spin conﬁguration ω ∈Ω+
Λ such that Γ′(ω) = Γ′.
We say that Λ is c-connected if Rd \S
i∈Λ Si is connected, which we will assume from now on in this
paper. Then, according to [13, eq (5.42)], the partition function can be rewritten as
Z+
Λ;β,0 = eβ|E+
Λ | Ξ+
Λ;β,0,
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL
13
where
Ξ+
Λ;β,0 :=
X
Γ′⊂ΓΛadmissible
Y
γ∈Γ′
e−2β|γ|.
The cluster expansion is an expression of log Ξ+
Λ;β,0 as an absolutely convergent series. In this case,
an (ordered) cluster is a list X = (γ1, . . . , γs) of contours. We denote by X the support of X, ie
X = ∪γ∈Xγ. In the following we write X ⊆Λ to say that X ⊆∪i∈ΛSi as subsets of Rd.
In can be shown (see e.g. [13, Chapter 5]) that the cluster expansion converges for β large enough.
Proposition 3.7. There exists βlt
ce(d) such that for all β > βlt
ce(d),
log Ξ+
Λ;β,0 =
X
X:X⊆Λ
ϕ(X) e−2β Ps
i=1 |γi|,
where
ϕ(γ1, . . . , γs) = 1
s!
X
G⊆Gsconnected
Y
{i,j}∈G
ζ(γi, γj),
ζ(γi, γj) :=
(
0 if γi ∩γj = ∅,
−1 otherwise,
and Gs denotes as above the complete graph on s vertices.
3.2.2. Bounds on joint cumulants. This cluster expansion can be used to compute expectations and
therefore deduce some bounds on joint cumulants.
Let A ⊆Λ and let us deﬁne σA := Q
i∈A σi. Its expectation is given by
⟨σA⟩+
Λ;β,0 =
X
ω∈Ω+
Λ
σA(ω)e−HΛ;β,0(ω)
Z+
Λ;β,0
.
For any spin conﬁguration ω ∈Ω+
Λ and any contour γ ∈Γ′(ω), let us deﬁne the interior of γ (written
Int(γ)) as the set of points of Λ which would have spin −1 if γ was the only contour of ω. We also
write Int(X) := S
γ∈X Int(γ) for any collection X of contours. Thus for any ω ∈Ω+
Λ and any i ∈Λ,
σi(ω) = (−1)|{γ∈Γ′(ω):i∈Int(γ)}|,
and thus
σA(ω) = (−1)
P
i∈A |{γ∈Γ′(ω):i∈Int(γ)}|
= (−1)
P
γ∈Γ′(ω) |{i∈A:i∈Int(γ)}|.
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
X
Γ′⊆ΓΛadmissible
Y
γ∈Γ′
(−1)|{i∈A:i∈Int(γ)}|e−2β|γ|.
The cluster expansion of log Ξ+,A
Λ;β,0 converges, which means that we have an analogue of Proposition
3.7 for Ξ+,A
Λ;β,0, replacing e−2β|γ| by (−1)|{i∈A:i∈Int(γ)}|e−2β|γ|. Thus ⟨σA⟩+
Λ;β,0 can be expressed as
⟨σA⟩+
Λ;β,0 = exp

X
X:X⊆Λ
ΨA
β (X) −
X
X:X⊆Λ
Ψ∅
β(X)

,
where for a cluster X = (γ1, . . . , γs),
ΨA
β (X) := ϕ(X) (−1)
Pr
j=1 |{i∈A:i∈Int(γj)}|e−2β Pr
j=1 |γj|.
14
JEHANNE DOUSSE AND VALENTIN F´ERAY
In particular, in the domain of convergence of the cluster expansion, joint moments are nonzero. If a
cluster X has no vertex of A in the interior of any of its contours, then ΨA
β (X) = Ψ∅
β(X). Such clusters
do not contribute to ⟨σA⟩+
Λ;β,0. Therefore,
⟨σA⟩+
Λ;β,0 = exp


X
X∼A:X⊆Λ
(ΨA
β (X) −Ψ∅
β(X))

,
where X ∼A means that X contains at least one contour γ such that a point of A is in the interior
of γ. The series is absolutely convergent and we can let Λ ↑Zd, obtaining the following proposition.
Proposition 3.8 (Equation (5.47) in [13]). For β large enough,
⟨σA⟩+
β,0 = exp
 X
X∼A
(ΨA
β (X) −Ψβ(X))
!
.
We now want to ﬁnd estimates on the joint cumulants of the variables {σi : i ∈A}, for all A ⊂Zd
ﬁnite. But in this case, it is easier to estimate ﬁrst another quantity related to cumulants. We deﬁne,
for some set B and random variables (Yi)i∈B deﬁned on the same probability space with nonzero joint
moments,
Q (Yj; j ∈B) :=
Y
δ⊆B
δ̸=∅
*Y
j∈δ
Y j
+(−1)|δ|
.
For example,
Qβ,0(σ1, σ2) =
⟨σ1σ2⟩+
β,0
⟨σ1⟩+
β,0⟨σ2⟩+
β,0
,
Qβ,0(σ1, σ2, σ3) =
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
We show a bound on the quantities Qβ,0 (σj; j ∈A) for all ﬁnite A ⊂Zd.
Lemma 3.9. Let A be a ﬁnite subset of Zd of size r. Then for β large enough,
|Qβ,0 (σj; j ∈A) −1| ≤Cre−cβℓT (A),
where c = c(d) and Cr are positive constants depending respectively on d and r.
Proof: Using Proposition 3.8, we have
log Q (σj; j ∈A) =
X
δ⊆A,δ̸=∅
(−1)|δ| X
X∼δ
(Ψδ
β(X) −Ψβ(X)).
Recall that X ∼δ means that at least one point of δ is in the interior of a contour in X. We split the
second sum depending on the exact subset I ⊆δ of points that are in the interior of a contour in X.
By deﬁnition of Ψ, observe that, if I is as above, then Ψδ
β(X) = ΨI
β(X). Therefore
log Q (σj; j ∈A) =
X
δ⊆A,δ̸=∅
(−1)|δ| X
I⊆δ:
I̸=∅
X
X:
Int(X)∩δ=I
(ΨI
β(X) −Ψβ(X))
=
X
I⊆A:
I̸=∅
X
X:
I⊆Int(X)
"
(ΨI
β(X) −Ψβ(X))
X
δ:
I⊆δ⊆(I∪(A\Int(X)))
(−1)|δ|
#
.
But the last sum is equal to 0 unless A is contained in Int(X), in which case it is (−1)|I|. Therefore
we obtain
log Q (σj; j ∈A) =
X
X:
A⊆Int(X)
X
I⊆A:
I̸=∅
(−1)|I|(ΨI
β(X) −Ψβ(X)).
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL
15
Finally, there are 2r −1 non-empty subsets of A, and |ΨI
β(X)| ≤Ψβ(X) := |ϕ(X)|e−2β Pr
j=1 |γj| for all
X and I, thus
(3.7)
|log Q (σj; j ∈A)| ≤
X
X:
A⊆Int(X)
2(2r −1)Ψβ(X).
We conclude by using a trick similar to Lemma 3.6. By [13, Equation (5.29)], if β ≥βlt
ce(d), for any
face f of any Si (i ∈Zd), we have the bound
X
X:X∋f
Ψβ(X) ≤1.
Thus if β ≥2βlt
ce(d),
X
X:X∋f
Ψβ(X)eβ|X| ≤
X
X:X∋f
Ψ β
2 (X) ≤1.
So for any positive integer R,
(3.8)
X
X:X∋f
|X|≥R
Ψβ(X) ≤e−βR
X
X:X∋f
Ψβ(X)eβ|X| ≤e−βR.
Let us now turn back to Eq. (3.7). Every cluster X such that ϕ(X)̸ = 0 and A ⊆Int(X) satisﬁes
|X| ≥2ℓT (A). Moreover, if a cluster of size R has j1 ∈A in its interior, then it contains at least a
face f which is at distance at most R of j1. There are at most CRd such points, for some constant
C = C(d), therefore
X
X:
A⊆Int(X)
Ψβ(X) ≤
X
R≥2ℓT (A)
CRd


X
X:X∋f
|X|=R
Ψβ(X)


≤C
X
R≥2ℓT (A)
Rde−βR ≤C
≤C′e−cβℓT (A),
for β large enough, where C′ and c are some positive constants depending on the dimension d of the
ambient space. Thus by (3.7),
|log Q (σj; j ∈A)| ≤C′
re−cβℓT (A),
for some positive constant C′
r depending on r and d. Exponentiating completes the proof.
□
Now we can convert this estimate into the desired bound on joint cumulants.
Proposition 3.10. Let A be a ﬁnite subset of Zd of size r. Then, for β large enough,
|κβ,0 (σj; j ∈A) | ≤Dre
−cβℓT (A)
2
,
where c = c(d) is given by Lemma 3.9 and Dr is a positive constant depending on r.
Proof: By Lemma 3.9,
Qβ,0 (σj; j ∈A) = 1 + O(M
 G[A]

),
where G is the weighted graph deﬁned on Zd such that for each e = (i, j), one has we = e
−cβ∥i−j∥1
2
.
Indeed in that case M
 G[A]

= e
−cβℓ′
T (A)
2
≥e−cβℓT (A); see the discussion in Section 2.2.
Then using [10, Proposition 5.8], we deduce that
|κβ,0 (σj; j ∈A) | =
Y
j∈A
⟨σj⟩+
β,0 × O(M
 G[A]

).
The ﬁrst factor is trivially bounded by 1, while the second is bounded using Proposition 2.1:
M
 G[A]

= e
−cdβℓ′
T (A)
2
≤e
−cdβℓT (A)
2
.
