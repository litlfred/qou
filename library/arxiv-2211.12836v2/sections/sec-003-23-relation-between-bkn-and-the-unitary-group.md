---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-003-23-relation-between-bkn-and-the-unitary-group
section_title: "Relation between Bk,n and the unitary group"
section_number: 2.3
pages: 6-7
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
through the mapξn. This map can be transformed into a map, still denoted byξn, fromM≥0(Bk,n)
toMf(Tk), the space of ﬁnite Radon measures on Tk with the formula
ξn(µ) =
(2π
n
)k ∑
I∈Bk,n
µ(I)δξn(I).
As explained in the previous section, for µ ∈ M1(Bk,n) we have ∑
I∈Bk,nµh(I)µ(I) = 1 with
µh(I) = |V (ξn(I)|2
nk , so that
(3)
∫
Tk
|V (⃗ u)|2
(2π)k d [ξn(µ)] (⃗ u) = 1.
The latter equality is reminiscent of the spectral projection of conjugation invariant probability
measures on the unitary group U(k). Indeed, according to the Weyl integration formula [1, Section
4], the projection p :U(k)→Tk mappingU to the arguments of its eigenvalues sorted in decreasing
order (and taken in [0, 2π)) transforms the Haar measure µH on U(k) into the measure
dp⋆µH(⃗ u) =|V (⃗ u)|2
(2π)k d⃗ u
onTk, where p⋆ denotes the push-forward of µH throughp 1. For ⃗ u∈Tk, |V (⃗ u)|2
(2π)k is exactly the area
of the adjoint orbitO(⃗ u) of unitary matrices having eigenvalues
(
eiu1,...,e iuk
)
, see [1, Section 4.1,
Eq. (4.1.17)]. Hence, for any conjugation invariant probability measure ˜µ on U(k) with density f
with respect to µH (which means that f = ˜f◦p for some measurable function ˜f : Tk→ R), we
have
dp⋆˜µ(⃗ u) =|V (⃗ u)|2
(2π)k
˜f(⃗ u)d⃗ u,
onTk. In particular, ˜f(⃗ u)d⃗ usatisﬁes (3). Let us denote byM1(Tk) the closure in the weak topology
of the set of positive measurable functions ˜f onTk such that (3) is satisﬁed withd [ξn(µ)] (⃗ u) replaced
1We recall that p⋆µ(A) =µ(p−1(A)) for A measurable set of Tk.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 7
byf(⃗ u)d⃗ u. Note that the set of extreme points of the convex setM1(Tk) includes the weighted Dirac
masses (2π)k
|V (⃗ u)|2δ⃗ ufor elements⃗ uofTk with|V (⃗ u)|> 0. As a consequence, ξn [M1(Bk,n)]⊂M 1(Tk).
For any element µ ofM1(Tk), there exists a unique conjugation invariant probability measure
p⋆µ onU(k) (meaning that p⋆µ(UEU∗) =p⋆µ(E) for all U∈U(k) and E measurable set of U(k))
such that
p⋆ [p⋆µ] =µ,
so thatp⋆ yields an embedding ofM1(Tk) into the set of conjugation invariant probability measures
on U(k), see [1, Chapter 4]. Dirac masses on M1(Tk) correspond through p⋆ to Dirac masses on
orbitsO(⃗ u) = {U ∈ U(k), p(U) = ⃗ u) for ⃗ u∈ Tk. In particular, the set M1(Bk,n), which had
been seen previously as a discrete subset of M1(Tk), can now be considered through p⋆ as a set of
conjugation invariant probability measures on U(k).
The relation betweenBk,n andU(k) is actually much stronger. There exists a natural convolution
product∗ on the set of probability measures on U(k) which is characterized for µ,ν probability
measures on U(k) by the formula
∫
U(k)
f(U)d [µ∗ν] (U) =
∫
U(k)×U(k)
f(UV )dµ(U)⊗dµ(V )
for any continuous map f : U(k)→ R. Conjugating by p⋆ turns this product into a convolution
product, also denoted by ∗, on the set M1(Tk).
The set (M1(Bk,n),∗) can be seen as an-step discrete version of the space (M1(Tk),∗)), although
the former is not a subgroup of the latter. However, it has been proven in [18, Proposition 7.1]
that the convolution algebra (M1(Bk,n),∗) converges towards (M1(Tk,∗)) as n goes to inﬁnity in
some sense. Indeed, for λ,µ ∈ Tk which are decreasing, set λ(n) =
{⌊
nλi
2π
⌋}
1≤i≤k
for n≥ 1 and
similarly for µ(n), so that ξn(λ(n)) (resp. ξn(µ(n))) converges to λ (resp. µ) as n→∞ . Then,
λ(n),µ (n)∈Bk,n for n large enough and, as n→∞ ,
lim
n→∞
ξn
( eλ(n)
µh(λ(n))∗Bk,n
eµ(n)
µh(µ(n))
)
=δ(λ)∗Tkδ(µ) =p⋆(δO(λ)∗U(k)δO(µ)),
where we wrote∗F to specify that the convolution occurs in the group M1(F ).
