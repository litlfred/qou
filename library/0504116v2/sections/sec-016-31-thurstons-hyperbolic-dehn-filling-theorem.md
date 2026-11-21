---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3–manifolds with geodesic boundary"
section_id: sec-016-31-thurstons-hyperbolic-dehn-filling-theorem
section_title: "Thurston's hyperbolic Dehn filling Theorem"
section_number: 3.1
pages: 19-20
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
toc_source: outline
doc_brief: "On deformations of hyperbolic 3-manifolds with geodesic boundary (Frigerio, AGT 6 (2006) 435–457) — the solution variety of consistency equations for a geometric partially truncated triangulation…"
---
Let U be a sufﬁciently small neighbourhood of x0 in Ω(T ) and let x ∈U. For
j = 1, . . . , k, we deﬁne the j–Dehn ﬁlling coefﬁcient (pj(x), qj(x)) ∈R2 ∪{∞} as
follows: if uj(x) = 0, then (pj(x), qj(x)) = ∞; otherwise, pj(x), qj(x) are the unique real
solutions of the equation
pj(x)uj(x) + qj(x)vj(x) = 2πi.
(Existence and uniqueness of such solutions near x0 can be easily deduced from
Theorem 2.2 and Lemma 3.1.)
Let us set
d = (d1, . . . , dk): U →
kY
i=1
S2,
dj(x) = (pj(x), qj(x)) ∈S2 = R2 ∪{∞}.
As a consequence of Theorem 2.2 and Lemma 3.1 we have the following:
Theorem 3.2 If U is small enough, the map d deﬁnes a diffeomorphism onto an open
neighbourhood of (∞, . . . , ∞) in S2 × · · · × S2.
For x ∈Ω(T ) we denote by N(x) the hyperbolic structure induced on N by x, and by
bN(x) the metric completion of N(x). Recall that a preferred basis µi, λi of H1(Ti; Z) is
ﬁxed for every i = 1, . . . , k. We also set
IΩ(T )
=
{x ∈U ⊂Ω(T ) : each Dehn ﬁlling coefﬁcient corresponding to x
is equal either to ∞or to a pair of coprime integers}.
Theorem 3.3 If U is sufﬁciently small and x belongs to IΩ(T ) ∩U, then bN(x) admits
a complete ﬁnite-volume smooth hyperbolic structure which is obtained by adding to
N(x) a closed geodesic at any cusp with non-inﬁnite Dehn ﬁlling coefﬁcient. From a
topological point of view, bN(x) is obtained by Dehn ﬁlling the ith cusp of N along the
slope pi(x)µi + qi(x)λi if (pi(x), qi(x))̸ = ∞, and by leaving the ith cusp of N unﬁlled
if (pi(x), qi(x)) = ∞, i = 1, . . . , k.
Proof See eg, Thurston [15], Neumann–Zagier [12], Benedetti–Petronio [1], Frige-
rio [5].
Algebraic & Geometric Topology 6 (2006)
454
Roberto Frigerio
The following proposition will prove useful in the last subsection.
Proposition 3.4 Let X be any smooth manifold and let g: Ω(T ) →X be a smooth
map. Suppose that there exists a small neighbourhood U of x0 in Ω(T ) such that for
all x, x′ ∈U ∩IΩ(T ) with d(x) = −d(x′) we have g(x) = g(x′). Then dgx0 = 0.
Proof Since d : U →Qk
i=1 S2 deﬁnes a chart around x0, it is sufﬁcient to observe
that U ∩IΩ(T ) accumulates to x0 along any direction in Tx0Ω(T ).
