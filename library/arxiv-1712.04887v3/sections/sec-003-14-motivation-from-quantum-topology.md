---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K-THEORY"
section_id: sec-003-14-motivation-from-quantum-topology
section_title: "Motivation from quantum topology"
section_number: 1.4
pages: 6-8
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "BLOCH GROUPS, ALGEBRAICK-THEORY — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F (e2πi/n), well-deﬁned up to n-th"
---
anywhere else in this paper — we discuss the empirical discoveries that led us to conjecture
the results presented here. A much more detailed discussion of these ideas and of the
experimental results can be found in [13] (Introduction, Sections 1, 5 and 9, and Appendix).
The story has its origin in Quantum Topology and one of its most prized problems, the
Volume Conjecture of Kashaev, which relates the Jones polynomial of a hyperbolic knot with
hyperbolic geometry. More precisely, the Volume Conjecture [16] asserts that the Kashaev
invariant⟨K⟩N of a hyperbolic knot (which is equal to the value of the N-th colored Jones
polynomial ate2πi/N [23]) grows exponentially at a rate proportional to the hyperbolic volume
V(K) of the knot:
lim
N
1
N log|⟨K⟩| = V(K)
2π . (16)
A reﬁnement of the Volume Conjecture asserts the existence of an asymptotic expansion
⟨K⟩N ∼ N 3/2ˆΦK(2πi/N), ˆΦK(h) =ev(K)/hΦK(h) (17)
to all orders in 1/N asN→∞ , wherev(K) =iV(K)+CS(K)∈ C/4π2Z is the complexiﬁed
volume of K and ΦK(h) is a power series which satisﬁes µδ(K)1/2ΦK(h)∈ FK[[h]] where
FK is the trace ﬁeld of the hyperbolic knot, µ is some eighth root of unity, and δ(K) is a
non-zero number inFK related to the Ray-Singer torsion ofK. For instance, for the simplest
hyperbolic (ﬁgure-eight) knot, whose trace ﬁeld is F41 = Q(√−3), the ﬁrst few terms of the
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 7
series Φ41(h) are given by
Φ41(h) = 1
4√
3
(
1 + 11
72√−3h− 697
31104h2− 724351
33592320√−3h3 +···
)
.
In [38], the third author observed that if we extend the Kashaev invariant to a function
J(K) : Q/Z→ Q by Galois equivariance (i.e., by setting J(K)(a/N) :=σ−a
(
⟨K⟩N
)
forN >0
and (a,N ) = 1), then (17) can be improved to
JK(−1/X) ∼ X3/2 JK(X)ˆΦK(2πi/X), (18)
to all orders in 1 /X as X→∞ in Q with bounded denominator (note that JK(X) = 1 if
X =N∈ N), and more generally that for any
(a b
c d
)
∈ SL(2, Z) we have
JK
(aX +b
cX +d
)
∼ (cX +d)3/2 JK(X)ev(K)(X+d/c) ΦK
a/c
( 2πi
cX +d
)
(19)
to all orders in 1 /X as X→∞ in Q with bounded denominator, where Φ K
α (h)∈ Q[[h]]
(α∈ Q) is a power series depending only on α∈ Q/Z. This conjectural modular property
led to the concept of a quantum modular form [38], and its more recent development, that
of a holomorphic quantum modular form [13, 11]. Experiments for various knots and various
values of α suggested that the power series Φ K
α is the product of a number κα∈ Q with a
power series having coeﬃcients in the cyclotomic extension FK(e2πiα) of the trace ﬁeld of
the knot. The story that led to the present paper was then the striking empirical discovery
that the quotient of κα byκ0 was always the product of a root of unity and the c-th root of
an S-unit ϵK
α in FK(e2πiα) with S independent of α, where c is the denominator of α, and
furthermore that this unit, which is well-deﬁned only up tocth powers, transforms according
to Equation (6). For example, numerical computations given in [38] for the 41 knot andc = 5
suggested that εK
α in this case equals (ζ4 + 1)/ζ(ζ− 1)2 with ζ =e2πi(α−1/3)∈F41(e2πiα) =
Q(e2πi/15).
On the other hand, it is well known that a hyperbolic knot (and more generally, a complete,
ﬁnite-volume hyperbolic 3-manifold) gives an element ξK in the Bloch group B(FK), or
equivalently of the third K-group K3(F ), which determines (via the regulator map) the
complexiﬁed volume ofK, and this led to the guess that the units appearing in the quantum
modularity conjecture might depend only onξK. Moving away from hyperbolic manifolds and
of quantum topology, these observations prompted the third author to ask the ﬁrst author
during an Oberwolfach meeting (in July 2011) whether he could suggest a construction of
a map cζ as in Theorem 1.5. The answer was positive, but of course with no proof that
the units coming from the Kashaev invariant and the units given by cζ were connected,
leading to an initial two-author version of the current paper with an abstract saying that
we conjectured that a number that could not be deﬁned was equal to a number that could
not be computed! In the following years, the number of authors increased by one and it was
discovered that the asymptotic expansions of Nahm sums at roots of unity also involved a
unit with very similar properties, which together with Nahm’s construction of an element
of the Bloch group associated canonically to any Nahm sum suggested the existence of a
map Rζ as in Theorem 1.2 as well as of the map cζ in algebraic K-theory. The map Rζ has
the fortunate property of being well-deﬁned and computable.Eventually we found complete
8 FRANK CALEGARI, STA VROS GAROUF ALIDIS, AND DON ZAGIER
constructions of both maps, as explained in the current paper. But the basic disclaimer of
the old abstract remains true: the quantum modular conjecture is still open, so that we
cannot rigorously prove even the existence of the units εK
α . There is, however, a conjectural
description of the power series Φ K
α occurring in (19), as given by Tudor Dimofte and the
second author [5, 6], and these can be related to the map Rζ, as discussed in Section 7
of [13], so in conjunction with the extensive numerical computations of the putative units
coming from the quantum modular conjecture described in the appendix of that paper we
can conjecture with a fair degree of conviction that these numbers do indeed always coincide.
