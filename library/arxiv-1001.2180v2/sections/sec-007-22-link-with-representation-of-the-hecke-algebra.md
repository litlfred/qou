---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-007-22-link-with-representation-of-the-hecke-algebra
section_title: "Link with representation of the Hecke algebras"
section_number: 2.2
pages: 7-7
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
in the abstract harmonic analysis of the Iwahori-Hecke alge bras Hn,q. Recall that if n ∈ /C6 and q is a
complex parameter, then Hn,q is the complex associative algebra with generators T1, T2, . . . , Tn−1 and
relations:
braid relations: ∀i, T iTi+1Ti = Ti+1TiTi+1;
commutation relations: ∀ |j − i| ≥ 2, T iTj = TjTi;
quadratic relations: ∀i, (Ti − q)(Ti + 1) = 0 .
We recover the symmetric group algebra /BV Sn for q = 1 . For any value of q, one can deﬁne an element
corresponding to a permutation σ ∈ Sn:
Tσ = Ti1 Ti2 · · · Tik ,
where σ = si1 si2 · · ·sik is a minimal decomposition of σ in elementary transpositions (thanks to Mat-
sumoto’s theorem, the result does not depend on which minima l decomposition we choose). It can be
shown that (Tσ)σ∈Sn forms a linear basis of Hn,q (see for example [ Mat99] or [ GP00]). Moreover, if
q ⁄= 0 is not a root of unity (in the following, we assume that we are i n this case, as q is a positive real
number), then Hn,q is a semi-simple algebra abstractly isomorphic to /BV Sn, and consequently has the
same theory of representations: the irreducible Hn,q-modules are parameterized by the partitions of size
n, and each q-Specht module Sλ(q) has dimension dim Sλ(q) = dim λ. We will denote by ς λ(q) the trace
of the simple module Sλ(q), and by χλ(q) the normalized character, so that ς λ(q) = (dim λ) χλ(q). Both
objects are central linear forms on Hn,q.
Let us consider the regular trace of the Iwahori-Hecke algeb ra:
τq(Tσ) =
{
1 if σ = id,
0 otherwise.
The decomposition of τq in the basis of normalized q-characters χλ(q) writes as (this corresponds to
[Str08, equation (16)]):
τq =
∑
λ∈Yn
Mn,q(λ) χλ(q) =
∑
λ∈Yn
Dλ(q)
{n!}q
ς λ(q).(1)
Of course, this characterizes the q-Plancherel measure. Therefore, if we consider the q-characters on a
ﬁxed element Tσ as a function of the indexing partition λ, its expectation under the q-Plancherel measure
is τq(Tσ), that is either 0 or 1. Using this, we will be able to compute expectations of obser vables of
diagrams.
Remark 1. We will prove in this article that we have in fact a concentrat ion of the q-characters around
the regular trace and compute explicitly their ﬂuctuations , see Corollary
13 and Remark 5.
