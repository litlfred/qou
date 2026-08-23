---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-004-41-the-kashaev-invariant-and-its-descendants
section_title: "The Kashaev invariant and its descendants"
section_number: 4.1
pages: 7-9
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
saddle-point expansion of the state integral appeared originally in the asymptotic expansion
of the Kashaev invariant [Kas95]. In the case of the 4 1 knot, the Kashaev invariant is given
by
J(41)(q) =
∞∑
n=0
(q;q)n(q−1;q−1)n. (30)
The above expression can be evaluated when q is a root of unity. The Volume Conjecture
of Kashaev [Kas97] (and its extension to all orders [Guk05]) asserts that J(41)(e2πi/N) has an
asymptotic expansion for N large of the form
J(41)(e2πi/N)∼N 3/2 Φσ1
( 1
N
)
. (31)
We now explain a relation discovered in [GZc] between the formula for the Kashaev in-
variant (30) and the algebraic equation (7).
Following [GZc], we deﬁne the descendantsJ(41)
m (q) of the Kashaev invariant of the 41 knot
by
J(41)
m (q) =
∞∑
n=0
(q;q)n(q−1;q−1)nqmn, (m∈ Z ). (32)
Then, the sequence J(41)
m (q) is a solution to a linear q-diﬀerence equation
qm+1Jm(q) + (1− 2qm)Jm(q) +qm−1Jm−1(q) = 1, (m∈ Z ). (33)
8 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARI ˜NO
This can be seen as follows: let
an,m(q) = (q;q)n(q−1;q−1)nqmn (34)
denote the summand of (32). It follows that
an+1,m(q) = (1−q−n−1)(1−qn+1)an,m(q) (35a)
=qm(2−qn+1−q−n−1)an,m(q) (35b)
=qm(2−qan,m+1(q)−q−1an,m−1(q)). (35c)
Summing over n≥ 0 and taking into account the boundary term a0,m(q) = 1 on the left
hand side of the above equation concludes the proof of Equation (33).
Using the operators E and Q that act on sequences (ym) by
(Ey)m =ym+1, (Qy)m =qmym, EQ =qQE (36)
it follows that we can write (33) in the form
(Q(1−qE)(1−q−1E−1)−I)Jm(q) = 1. (37)
The homogeneous part of the above operator can be obtained by replacing x in the left hand
side of Equation (7) x byqE, and replacing the right hand side of Equation (7) by Q−1.
4.2. The q-series (G0
0,G 1
0) and their descendants. We now discuss an appearance of the
formal power series Φ(τ) in the radial asymptotics of some q-series, following [GZb].
By q-series we mean formal Laurent series in a variable q with integer coeﬃcients, i.e.,
elements of Z ((q)). All the q-series below will deﬁne holomorphic functions in the punctured
unit disk with (perhaps) a pole at the origin. We now recall how the radial asymptotics of
the q-series (G0
0,G 1
0) is given by Φ( τ). The ﬁrst series G0
0(q) was found quite by accident
to have radial asymptotics expressed in terms of the series Φ( τ) [GZb], whereas the second
series was found systematically by expressing the state integral invariant of the 4 1 knot in
terms of products of q-series and ˜q-series [GK17].
Below, we will use capital letters for q-series and small letters for the corresponding func-
tions on the upper half-plane, e.g., g0
m(τ) = G0
m(q) for q = e 2πiτ. In [GZb] it was observed
that we have an asymptotic expansion
( 1√τg0
0(τ)√τg 1
0(τ)
)
∼
(
1 −1
1 1
)
Φ(τ) (38)
to all orders in τ, as τ tends to 0 along a ray in the ﬁrst quadrant of the upper half-
plane. The above asymptotic expansion requires some explanation since on a ﬁxed ray in
the ﬁrst quadrant, Φσ1(τ) is exponentially larger than Φ σ2(τ). Nonetheless, the asymptotic
expansion (38) makes sense theoretically and computationally if we use a reﬁned optimal
truncation explained in detail in [GZc] and applied in [GZb]. The numerical computations
of [GZb] hinted that the matrix in Equation (38) is the constant term of a matrix of ˜q series.
Given the deﬁnition ofG0
0(q) andG1
0(q) from [GZb] and [GK17], it was relatively straight-
forward to add the variable qmn and arrive to formulas (13a) and (13b) which deﬁne the
descendants of the pair (G0
0(q),G 1
0(q)).
THE RESURGENT STRUCTURE OF QUANTUM KNOT INV ARIANTS 9
