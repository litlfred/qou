---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-002-12-the-generalized-volume-conjecture
section_title: "The generalized volume conjecture"
section_number: 1.2
pages: 4-5
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
Volume Conjecture; the latter connects two very diﬀerent appro aches to knot theory, namely Topological
Quantum Field Theory and Riemannian (mostly Hyperbolic) Geometry.
Conjecture 1.7. [
Kas97, MM01] For every hyperbolic knot K in S3 we have:
lim
n→∞
log |fK,n (2πi)|
n = 1
2π vol(ρ2πi ),
where vol( ρ2πi ) is the hyperbolic volume of the the knot complement S3 − K.
In other words, the sequence fK,n (2πi) of complex numbers grows exponentially with respect to n, and
the exponential growth-rate is proportional to the volume of a hy perbolic knot.
One can deﬁne the volume function vol( ρ) of every representation ρ : π1(S3 \ K) → SL2(2, C), see
[Dun99, CCG+94, Thu77], and vol( ρ2πi ) is exactly the value of this volume function with ρ2πi being the
discrete faithful representation of the knot group.
The idea of the Generalized Volume Conjecture (formulated in part b y Gukov in [Guk05]) is that we should
use other representations of the knot complement in SL(2 , C). For α nearby 2πi, in a small neighborhood of
ρ2πi there is a unique (up to conjugation) representation
ρα : π1(S3 − K) − →SL(2, C)
which satisﬁes
(7) ρα (meridian) =
(
eα ⋆
0 e−α
)
.
Alas, there is an additional diﬃculty. Namely, when α/(2πi) is rational, we should distinguish two cases:
α/(2πi) = 1 or α/(2πi) ⁄= 1. The Generalized Volume Conjecture for α suﬃciently close to 2 πi may now be
stated as follows.
Conjecture 1.8. If α/(2πi) ∈ (R − Q) ∪ {1} is suﬃciently close to 1 then
(8) lim
n→∞
log |fK,n (α)|
n = cα vol(ρα ),
and if α/(2πi) ∈ Q − {1}, then
lim sup
n→∞
log |fK,n (α)|
n = cα vol(ρα ),
lim inf
n→∞
log |fK,n (α)|
n = 0 ,
where cα ⁄= 0 are some nonzero constants.
The distinction of α/(2πi) being rational or not is a bit with odds with the notion of hyperbolic Dehn
surgery developed by Thurston in [ Thu77]. When α/(2πi) is a rational number, the hyperbolic Dehn surgery
theorem associates an orbifold ﬁlling to the knot complement whose v olume is vol( ρα ). Orbifolds are mild
generalizations of manifolds. On the other hand, when α/(2πi) is irrational, hyperbolic Dehn surgery asso-
ciates a space which is topologically a 1-point compactiﬁcation of the k not complement, with volume vol( ρα ).
In the following, we will refer to the parameter α in the Generalized Volume Conjecture as the angle , making
contact with standard terminology from hyperbolic geometry.
There are two rather independent parts in the Volume Conjecture :
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 5
(a) To show that the limit exists in ( 8),
(b) To identify the limit with the volume of the corresponding Dehn ﬁlling .
At the moment, the Generalized Volume Conjecture is known only for the 4 1 knot and certain values of
α; see Murakami, [ Mur04].
One may further ask what happens to the Generalized Volume Conje cture when the angle α is small.
For α = 0, it is natural to deﬁne ρ0 to be the trivial representation. Then for α small enough, there is a
unique (up to conjugation) abelian SL2(C) representation ρα that satisﬁes ( 7). Abelian representations have
0 volume (see eg, [ CCG+94]). On the other hand, for small enough α, we have ∆ K(eα ) ∼ ∆ K (1) = 1. Thus
Theorem 1.3 implies that
Theorem 1.9. For every knot K there exists an open neighborhood UK of 0 ∈ C, such that for α ∈ UK, we
have:
lim
n→∞
log |fK,n (α)|
n = 0 = vol( ρα ).
In other words, Theorem 1.3 settles the Generalized Volume Conjecture for small complex angles .
1.3. The Generalized V olume Conjecture near 2πi. Our next result states that the volume conjecture
can only be barely true.
Theorem 1.10. (Proof in Section
9) For every knot K and every ﬁxed integer m ⁄= 0
lim
n→∞
1
n log |JK,n +m(exp(2πi/n))| = 0.
It follows that the double-scaling limit
lim
n,k
1
n log |JK,n (exp(2πi/k))|
when n, k → ∞ and n/k → 1 does not exist, or equals to 0; with the latter case in contradiction with the
Volume Conjecture. Our next result conﬁrms the strange behavio r in the Generalized Volume Conjecture
when α/(2πi) is rational, not equal to 1.
Theorem 1.11. (Proof in Section 9) For every knot K there exist a neighborhood VK of 1 ∈ C such that
when α/(2πi) ∈ VK is rational and not equal to 1, then
lim inf
n→∞
|fK,n (α)|
n = 0.
