---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-046
section_title: "Page 46"
section_number: null
pages: 46-46
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Theorem 10.2 ([Bi1, Th. 1.3]). Fix an arbitrary A > 1. For any partition ρ and
any λ ∈Y(A),
χλ
ρ∪1n−|ρ|
dim λ
= n−|ρ|−ℓ(ρ)
2
Y
j≥1
ef mj(ρ)
j+1
[¯λ( · )] + O

n−|ρ|−ℓ(ρ)
2
−1
,
(10.1)
where n = |λ| is assumed to be ≥|ρ|. Here the estimate of the remainder term
depends only on A and ρ, and is uniform on λ provided that λ ranges over Y(A).
Comments. 1) All terms in (10.1) do not depend on m1(ρ). Indeed, this is evident
for ρ ∪1n−|ρ| and |ρ| −ℓ(ρ). On the other hand ef2(¯λ( · )) = 1, so that the factor
corresponding to j = 1 equals 1.
2) As pointed out by Biane, formula (10.1) implies that if {λ} is a sequence
of diagrams in Y(A) such that n = |λ| →∞and ¯λ( · ) uniformly converges to a
continual diagram ω ∈D0 then
χλ
ρ∪1n−|ρ|
dim λ
∼C n−|ρ|−ℓ(ρ)
2
,
C =
Y
j≥1
ef mj(ρ)
j+1
[ω].
(10.2)
Note that in some cases the constant C can vanish, which implies a faster decay of
the character values: this happens, for instance, when ω = Ωand ρ is nontrivial
(i.e. distinct from (1r)), because efk[Ω] = 0 for any k ≥3.
3) In this result, the assumption that λ ranges over a set of the form Y(A) plays
a key role. When this assumption is dropped, quite a diﬀerent estimate for the
left–hand side of (10.1) holds, see Roichman’s paper [Ro].
4) Biane [Bi2] obtained further results in this direction.
We shall give an alternative proof of this Biane’s theorem. Our argument seems
to be rather simple and transparent.
Proof of Theorem 10.2. Multiply both sides of (10.1) by
n↓|ρ| = n|ρ| (1 + O(n−1)).
Then, by Deﬁnition 4.1, (10.1) is transformed to
p#
ρ (λ) = n
|ρ|+ℓ(ρ)
2
Y
j≥1
ef mj(ρ)
j+1
[¯λ( · )] + O

n
|ρ|+ℓ(ρ)
2
−1
,
(10.3)
Expand p#
ρ into the sum of its weight homogeneous components:
p#
ρ =
|ρ|+ℓ(ρ)
X
j=0
F (j)
ρ
,
wt(F (j)
ρ ) = |ρ| + ℓ(ρ) −j,
(10.4)
so that F (0)
ρ
is the top weight component. By Proposition 4.9,
F (0)
ρ
=
Y
j≥1
(the top weight component of p#
j )mj(ρ) .
46
