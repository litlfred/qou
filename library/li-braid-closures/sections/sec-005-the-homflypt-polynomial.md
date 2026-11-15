---
doc_id: li-braid-closures
doc_title: "Knot polynomials on braid closures"
section_id: sec-005-the-homflypt-polynomial
section_title: "The HOMFLYPT polynomial"
section_number: null
pages: 6-8
source_pdf: Li-braid-closures.pdf
source_sha256: f7410e7be5bc187e
toc_source: outline
doc_brief: "Knot polynomials on braid closures — We explore properties of the Jones and Alexander polynomials of braid closures of braids of index 3."
---
The HOMFLYPT polynomial
In [1, Section 6], Jones proposed a multivariable polynomial link invariant XL(q, Λ), which
reduces to the Jones polynomial under the specialization q = Λ = t and to the Alexander
polynomial under the specialization q =
1
Λ = t. We recall the key definitions organized
in [4].
Definition 2.16 ([6, Theorem 1.1]). Let λ ⊢n be a partition. The Ocneanu weight corre-
sponding to λ is the product
Ωλ =
Y
b∈λ
qr(b)w −qc(b)z
1 −qh(b)
,
where z = −1−q
1−Λq and w = 1 −q + z.
Definition 2.17. Let e: Bn →Z denote the braid exponent, the additive homomorphism
where e(σi) = 1 for all i.
Definition 2.18 ([1, Definition 6.1]). For a braid α ∈Bn, the HOMFLYPT polynomial
under Jones normalization is the product
Xˆα(q, Λ) :=

−
1 −Λq
√
Λ(1 −q)
n−1
(
√
Λ)e(α) X
λ⊢n
Ωλχλ(α).
This two-variable polynomial Xˆα(q, Λ) is a link invariant. The sum P
λ⊢n Ωλχλ(α) is some-
times referred to as the Ocneanu trace.
6
Remark. The HOMFLYPT polynomial often admits the much more common normalization
PL(a, z), related to the Jones normalization by XL(q, Λ) = PL((Λq)−1/2, q1/2 −q−1/2).
Ocneanu originally calculated the eponymous weights, but this work has been lost. A
reproof of the validity of these weights was given by Geck [6].
Example 2.19 ([4, Example A.10]). Under the Jones specialization q = Λ = t, the weights
Ωλ simplify drastically, as shown in [4]. Specifically, Ωλ = 0 if λ has more than two columns,
and the braid closure of any α ∈Bn has Jones polynomial
Vˆα(t) = (−1)n−1(
√
t)e(α)−n+1
t + 1
⌊n/2⌋
X
k=0
 n−k
X
i=k
ti
!
χ(n−k,k)⊤(α).
When n = 3, this simplifies to
Vˆα(t) = (
√
t)e(α)−2((t2 + 1)χ(1,1,1)(α) + tχ(2,1)(α)).
Example 2.20 ([1, Section 7]). Under the Alexander specialization q =
1
Λ = t, the sim-
plification of the weights is less clear as it seems like z = −1−q
1−Λq will exhibit a singularity.
However, it turns out that such singularities are removable due to the factor of (1 −Λq)n−1
in Definition 2.18.
Let µi be the hook-type partition made up of one row of i squares and one column of
n −i squares beneath. As computed in [1, Equation 7.2], we find that
∆α(t) =
(−1)n(t −1)
(
√
t)e(α)−n+1(tn −1)
n
X
i=1
(−1)iχµi(α).
When n = 3, this implies that
∆ˆα(t) = χ(1,1,1)(α) −χ(2,1)(α) + χ(3)(α)
(
√
t)e(α)−2(t2 + t + 1)
.
Remark. If we substitute t = ζn = e2πi/n into Example 2.20 above, the denominator vanishes,
implying that the numerator must vanish too. In particular, we must have
n
X
i=1
(−1)iχµi(α) = 0
at t = ζn. If we apply the KZ functor to the exact sequence proven due to the BGG resolution
in [7], we expect an exact sequence of ζn-Specht modules on hook-shape partitions.
7
