---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3–manifolds with geodesic boundary"
section_id: sec-014-3-dehn-filling
section_title: "Dehn filling"
section_number: 3
pages: 18-20
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
toc_source: outline
---
Dehn ﬁlling
Once the smoothness of Ω(T ) at x0 is established, one can prove Thurston’s hyperbolic
Dehn ﬁlling Theorem just by following the strategy described in [12]. At this stage, this
argument applies only to those hyperbolic manifolds with geodesic boundary which
admit a good geodesic triangulation (but see Conjecture 1.2). The following result is
taken from [12].
Algebraic & Geometric Topology 6 (2006)
Deforming hyperbolic 3–manifolds with boundary
453
Lemma 3.1 Let j ∈{1, . . . , k}. Then there exists a complex number τj with non-zero
imaginary part such that if {yn}n∈N ⊂Ω(T ) is a sequence with limn→∞yn = x0 and
uj(yn)̸ = 0 for every n ∈N, then limn→∞vj(yn)/uj(yn) = τj.
3.1
Thurston’s hyperbolic Dehn ﬁlling Theorem
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
