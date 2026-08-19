---
doc_id: arxiv-math-0506456v1
doc_title: "Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publishing Company ASYMPTOTICS OF THE QUANTUM INV ARIANTS FOR SURGERIES ON THE FIGURE 8 KNOT JØRGEN ELLEGAARD ANDERS"
section_id: sec-033-3-if-s2-1-then-λ11su-1-if-and
section_title: "If s2 ⁄= 1 then λ11(s,u ) = ±1 if and"
section_number: 3
pages: 33-35
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
only if λ12(s,u ) = 0. Therefore ρ(s,u)(λ) is diagonalizable (or diagonal) if and only
if s2 ⁄= 1. In case s2 ⁄= 1 and λ12(s,u ) ⁄= 0 we have
λ12(s,u )
λ11(s,u ) −λ11(s,u )−1 = 1
s2 − 1 = s−1
s −s−1.
We conclude that if s2 ⁄= 1, then C2 has a basis consisting of a set of common
eigenvectors for the matrices ρ(s,u)(µ) and ρ(s,u)(λ), namely u1 = (1, 0) and u2 =
(−1/(s2 − 1), 1). If we let ˜ ρ(s,u) : π → SL(2, C) be the representation ˜ρ(s,u)(γ) =
U −1ρ(s,u)(γ)U , where U ∈ SL(2, C) with jth column uj, we therefore have
˜ρ(s,u)(x) = diag
(
s,s −1)
, ˜ρ(s,u)(λ) = diag
(
λ11(s,u ),λ 11(s,u )−1)
. (5.63)
In particular, ρ(s,u) :π → SL(2, C),s2 ⁄= 1, extends to a representation of π1(Mp/q)
if and only if
s−p =λ11(s,u )q. (5.64)
Recall here that ρ(s,u) andρ(s−1,u) are equivalent for (s,u ) ∈ ˜N \ ˜N0, cf. Corollary 1.
But as noted above λ11(s−1,u ) = λ11(s,u )−1 in accordance with (5.64). For ( s,u ) ∈
˜N0 we have λ11(s,u ) = 1 and |s| ⁄= 1, so ρ(s,u) extends to a representation of
π1(Mp/q) if and only if p = 0.
A direct check shows that ifs2 = 1 then ρ(s,u) does not extend to a representation
of π1(Mp/q) for any rational number p/q. In fact, if s = ±1, then
ρ(s,u)(µ)p = (±1)|p|
( 1 p
0 1
)
and
ρ(s,u)(λ)q =
(
−
(
1 εi2
√
3
0 1
)) q
= (−1)|q|
(
1 εi2q
√
3
0 1
)
for a ε ∈ {− 1, 1}. On the other hand, since λ11(s,u ) = −1, we have that (5.64)
is satisﬁed if s = 1 and q is even or s = −1 and both p and q are odd. For the
following we note that if s2 = 1 then u2 +u + 1 = φ(1,u ) = 0 so u is not real.
We are mostly interested in the SU(2)–representations of π. Let in the following
Mnab be the set of conjugacy classes of nonabelian SU(2)–representa tions of π.
Proposition 2. Let (s,u ) ∈ ˜N . The representation ρ(s,u) : π → SL(2, C) is
SL(2, C)–equivalent to a representation π → SU(2) if and only if |s| = 1 and u
34 Asymptotics of the quantum invariants for the ﬁgure 8 knot
is real. If we write s = e2πiθ, θ ∈] − 1/2, 1/2], then u ∈ {u±}, where u± = u±(θ)
are the two solutions to φ(e4πiθ,u ) = 0, i.e.
u±(θ) = cos(4πθ) − 3
2 ±
√
cos2(4πθ) − cos(4πθ) − 3
4.
Sinceu is real we have θ ∈ [−1/3, −1/6] ∪ [1/6, 1/3]. The representation ρ(e2πiθ ,uε ),
θ ∈ [−1/3, −1/6] ∪ [1/6, 1/3] and ε ∈ {±} , is SL(2 , C)–equivalent to a SU(2)–
representation ¯ρθ,ε which satisﬁes
¯ρθ,ε(µ) = diag
(
e2πiθ,e −2πiθ)
, ¯ρθ,ε(λ) = diag(Lε,L −1
ε ),
whereµ andλ are the elements of π corresponding to the meridian and the preferred
longitude of K, and
L± =L±(θ) = λ11
(
e2πiθ,u ±
)
= −1 +e−4πiθ − 2e4πiθ +e8πiθ +u±
(
e−4πiθ −e4πiθ)
.
We note that ¯ρ−θ,ε and ¯ρθ,ε are SU(2)–equivalent. In particular, the space Mnab
can be parametrized by the two arcs (e2πiθ,u +(θ)),θ ∈ [1/6, 1/3], and (e2πiθ,u −(θ)),
θ ∈ [1/6, 1/3]. These two arcs only coincide at the endpoints, so topologically Mnab
is a circle.
This proposition follows from [28, Proposition 4], see also [18, Proposit ion 5.4].
For a more geometric argument determining the topological type of Mnab, see [19].
Forθ ∈ [−1/3, −1/6] ∪ [1/6, 1/3] and ε ∈ {±} , the representation ¯ρθ,ε extends
to a representation of π1(Mp/q) if and only if
¯ρθ,ε(µ)p ¯ρθ,ε(λ)q = 1,
i.e. if and only if
e−2πipθ =Lε(θ)q. (5.65)
From this (use e.g. (5.69)) we see that
Corollary 2. Letp/q ∈ Q be arbitrary. The moduli space of irreducible ﬂat SU(2)–
connections on Mp/q is a ﬁnite set.
Let us end this section by ﬁnding the abelian SU(2)–representation s ofπ1(Mp/q)
(up to equivalence). Therefore, let θ ∈] − 1/2, 1/2] and let ρθ be the assignment
ρθ(µ) = diag(e2πiθ,e −2πiθ).
By (5.57) this assignment extends to an abelian SU(2)–representa tion of π for
any θ ∈] − 1/2, 1/2] by letting ρθ(y) = ρθ(x). Moreover, any abelian SU(2)–
representation of π is SU(2)–equivalent to ρθ for some θ ∈] − 1/2, 1/2]. For any
θ ∈] − 1/2, 1/2] we have ρθ(λ) = 1, and ρθ extends to a representation of π1(Mp/q)
if and only if ρθ(µ)p = 1, i.e. if and only if pθ ∈ Z. If A =
( 0 −1
1 0
)
then
Aρθ(µ)A−1 =ρ−θ(µ) so we can assume that θ ∈ [0, 1/2]. Note, moreover, that two
matrices diag(eiφ,e −iφ) and diag(eiψ,e −iψ), φ,ψ ∈] −π,π ], are conjugate in SU(2)
if and only if φ =ψ or φ = −ψ. We conclude
Asymptotics of the quantum invariants for the ﬁgure 8 knot 35
Proposition 3. Forp ⁄= 0 the set of conjugacy classes of abelian SU(2)–represen-
tations of π1(Mp/q) is given by
{
[ρj/|p|]
⏐
⏐
⏐
⏐j = 0, 1,...,
[ |p|
2
] }
,
where [ |p|/2] is the integer part of |p|/2. For p = 0 the set of conjugacy classes of
abelian SU(2)–representations of π1(Mp/q) is given by
{
[ρθ]
⏐
⏐
⏐
⏐θ ∈ [0, 1
2 ]
}
,
so topologically this set is a closed interval.
