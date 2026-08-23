---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-032-1-such-groups-are-denoted-2bridge-kmot-groups-by
section_title: "Such groups are denoted 2–bridge kmot groups by Riley since the y generalize"
section_number: 1
pages: 30-33
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
the 2–bridge knot groups. Following Riley we say that a representat ion ψ : G →
SL(2, C) is aﬃne when the image of ψ ﬁxes exactly one point in CP1 and not aﬃne
when this image has no ﬁxed points. We note that if ψ is nonabelian then ψ is aﬃne
if and only if ψ(x) and ψ(y) have a common eigenvector, and ψ is not aﬃne if these
two matrices have no common eigenvector. Let H be some subgroup of SL(2 , C).
Then we will say that two representations ψ1,ψ 2 :G → SL(2, C) are H–equivalent
if they are conjugate to each other by a matrix in H, i.e. if there exists a matrix
U ∈H such that ψ2(γ) = Uψ 1(γ)U −1 for all γ ∈G. In particular, we will say that
ψ1 and ψ2 are equivalent if they are SL(2 , C)–equivalent. For ( t,u ) ∈ C∗ × C we
put
C0(t) =
( t 1
0 1
)
, D 0(t,u ) =
( t 0
−tu 1
)
,
Asymptotics of the quantum invariants for the ﬁgure 8 knot 31
C1(t) =
( t 1
0 t−1
)
, D 1(t,u ) =
( t 0
−u t −1
)
,
C2(t) =
(
t t −1
0 t−1
)
, D 2(t,u ) =
(
t 0
−tu t −1
)
.
We note that Cν (t) and Dν(t,u ) are elements of SL(2 , C), ν = 1, 2. If s is a square
root of t and V (s) = diag(s,s −1) then
V (s)C2(t)V (s)−1 =C1(t), V (s)D2(t,u )V (s)−1 =D1(t,u ), (5.58)
and
C0(t) = sC2(s), D 0(t,u ) = sD2(s,u ). (5.59)
LetWν (t,u ) denote the matrix obtained by replacing x andy by respectively Cν(t)
and Dν(t,u ) in the expression for w, and let
φ(t,u ) = W11 + (1 −t)W12,
where W = W (t,u ) = W0(t,u ). We let ρ(t,u) be the assignment x ↦→C2(t),
y ↦→D2(t,u ). We have the following SL(2 , C) version of [28, Theorem 1].
Theorem 5. Let (s,u ) ∈ C∗ × C. None of the assignments ρ(s,u) extend to an
abelian SL(2, C)–representation ofG. The assignment ρ(s,u) extends to a nonabelian
representationρ(s,u) :G → SL(2, C) if and only if
φ(s2,u ) = 0. (5.60)
Conversely, if ψ :G → SL(2, C) is a nonabelian representation, then there exists a
pair (s,u ) ∈ C∗ × C satisfying (5.60) such that ψ and ρ(s,u) are equivalent. When
ψ is aﬃne this pair is unique, and when ψ is not aﬃne the pair ( s,u ) can only be
replaced by (s−1,u ).
Proof. The theorem follows by results of [28], [29]. The assignment ρ(s,u) extends to
a SL(2, C)–representation of G if and only if W2(s,u )C2(s,u ) = D2(s,u )W2(s,u ).
The matrices C2(s) and D2(s,u ) commute if and only if s = ±1 and u = 0, and
since C2(±1) = ±C2(1) is diﬀerent from D2(±1, 0) = ±D2(1, 0) we have that the
assignment ρ(±1,0) does not extend to a SL(2 , C)–representation of G. (We note
that if W =W (1, 0) then W21 = 0 since the matrices C0(1),D 0(1, 0) = I and their
inverses are upper triangular. But we also have that φ(1, 0) = 0 would imply that
W11 = 0 contradicting the fact that W is invertible. Therefore φ(1, 0) ⁄= 0.)
Let σ = ∑ α−1
j=1 εj. Then sσW2(s,u ) = W (s2,u ). By (the proof of) [28, The-
orem 1] we have W (s2,u )C0(s2) = D0(s2,u )W (s2,u ) if and only if φ(s2,u ) = 0,
so by (5.59) we ﬁnd that ρ(s,u) extends to a (necessarily nonabelian) SL(2 , C)–
representation of G if and only if φ(s2,u ) = 0.
If ψ :G → SL(2, C) is an arbitrary nonabelian representation it follows by [29,
Lemma 7] and (5.58) that there exists a pair ( s,u ) ∈ C∗ × C (necessarily satisfying
(5.60)) such that ψ andρ(s,u) are equivalent. By the above any such pair is diﬀerent
from ( ±1, 0) and by [29, Lemma 8] and (5.58) we then get the ﬁnal statement o f
the theorem.
32 Asymptotics of the quantum invariants for the ﬁgure 8 knot
If (s,u ) ∈ C∗ × C with φ(s2,u ) = 0 then ρ(s,u) is aﬃne if and only if C2(s)
and D2(s,u ) have a common eigenvector. But this happens exactly when u = 0 or
u = (s −s−1)2.
Let us now restrict to the case where G is the ﬁgure 8 knot group π. Then
φ(t,u ) = u2 +
(
3 − (t +t−1)
)
(u + 1) (5.61)
so in particularφ(s2, 0) = 3 −s2−s−2 = 0 if and only if s4−3s2+1 = 0 i.e. if and only
if s =µ1
√
(3 +µ2
√
5)/2 for some µ1,µ 2 ∈ {±1}. If u = (s −s−1)2 =s2 +s−2 − 2
thenφ(s2,u ) = u2 + (3 −u − 2)(u + 1) =u2 + 1 −u2 = 1, so we conclude that ρ(s,u)
is aﬃne if and only if u = 0 and s4 − 3s2 + 1 = 0. Let
N = Hom(π, SL(2, C))/SL(2, C)
be the space of conjugacy classes of SL(2 , C)–representations of π and let Nnab be
the subset consisting of classes represented by nonabelian SL(2 , C)–representations.
Moreover, let
˜N = { (s,u ) ∈ C∗ × C |φ(s2,u ) = 0 }, (5.62)
and let Φ : ˜N → N be the map which maps ( s,u ) to the class represented by ρ(s,u).
We have shown
Corollary 1. The image of Φ is Nnab. If we let
˜N0 = { (µ1
√
(3 +µ2
√
5)/2, 0) |µ1,µ 2 ∈ {±1} }
then Φ | ˜N0 : ˜N0 → N is injective and Φ −1(Φ(s,u )) = {(s,u ), (s−1,u )} for any
(s,u ) ∈ ˜N \ ˜N0.
Recall that Mp/q denotes the closed oriented 3–manifold obtained by surgery on
S3 along the ﬁgure 8 knot with rational surgery coeﬃcient p/q. The representation
ρ(s,u), (s,u ) ∈ ˜N , extends to a SL(2 , C)–representation of π1(Mp/q) if and only if
ρ(s,u)(µ)pρ(s,u)(λ)q = 1.
To analyze this criterion it is an advantage to diagonalize ρ(s,u)(λ). Assume in
the following that ( s,u ) ∈ ˜N . By a rather long but completely elementary and
straightforward calculation we ﬁnd that
ρ(s,u)(λ) =
( λ11(s,u ) λ12(s,u )
0 λ11(s−1,u )
)
,
where
λ11(s,u ) = −1 +s−2 − 2s2 +s4 +u(s−2 −s2)
and λ12(s,u ) = 2u(1 −u) if s2 = 1 and
λ12(s,u ) = λ11(s,u ) −λ11(s−1,u )
s2 − 1
Asymptotics of the quantum invariants for the ﬁgure 8 knot 33
for s2 ⁄= 1. We note that λ11(s−1,u ) = λ11(s,u )−1.
In general, if A =
(
α β
0 α−1
)
∈ SL(2, C), then A can be diagonalized if and
only if A is not parabolic, i.e. if and only if tr( A) ⁄= ±2 or equivalently if and only
ifα ⁄= ±1 (except, of course, if β = 0). If α ⁄= ±1 then (1, 0) is an eigenvector with
eigenvalueα and (−β/(α −α−1), 1) is an eigenvector with eigenvalue α−1. If s2 = 1
then λ11(s,u ) = −1 and λ12(s,u ) = ±i2
√
