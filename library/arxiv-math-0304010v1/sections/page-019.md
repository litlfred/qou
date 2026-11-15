---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-019
section_title: "Page 19"
section_number: null
pages: 19-19
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Then, as is readily seen,
1
k eak = bk + Yk(b2, . . . , bk−1),
k = 2, 3, . . .,
(3.8)
where, likewise, Yk is a polynomial of total weight ≤k, with the convention that
wt(bj) = j.
Moreover, the top weight homogeneous component of Yk depends only on the
top weight homogeneous components of X2, . . ., Xk.
Now let us set
eak = epk ,
bk = p#
k−1 ,
k = 2, 3, . . .,
eA(t) =
∞
X
j=2
eaj
j tj,
A(t) = exp eA(t),
B(u) = 1 +
∞
X
j=2
bjuj.
By Proposition 3.5, we have
bk = −
1
k −1 [tk]{A−(k−1)(t)} + . . . ,
k = 2, 3, . . .,
where dots mean terms of lower weight. By (3.6), these relations are of the form
(3.7). Therefore, to evaluate the inverse relations (3.8) up to lower weight terms,
we may use formula (iv) of Proposition 3.6. This yields
eak = [uk]{Bk(u)} + . . . ,
k = 2, 3, . . .,
which is exactly (3.6).
□
§4. The basis {p#
ρ } and filtrations in A
In this section we review some results of [KO] and [IK].
Deﬁnition 4.1. To any partition ρ we assign a function p#
ρ on Y as follows. Let
r = |ρ|, let λ ∈Y, and denote n = |λ|. Then
p#
ρ (λ) =



n↓r ·
χλ
ρ∪1n−r
dim λ ,
n ≥r,
0,
n < r,
where ρ ∪1n−r = (ρ, 1, . . ., 1) ∈Yn.
When ρ consists of a single part, ρ = (r), then this reduces to Deﬁnition 3.1.
Given a partition ρ, we shall denote by mi = mi(ρ) the multiplicity of i in ρ:
mi(ρ) = Card{j | ρj = i},
i = 1, 2, . . . .
By ℓ(ρ) we denote the number of nonzero parts of ρ (the length of ρ). We have
ℓ(ρ) = P mi(ρ).
Similarly to the conventional notation for the algebra Λ, we set
pρ = pρ1 . . . pρℓ(ρ) =
Y
i
pmi(ρ)
i
.
The elements pρ form a homogeneous (in the canonical grading) basis in the algebra
A. Note that deg pρ = |ρ|.
The next result generalizes Proposition 3.3 (ﬁrst claim) and Proposition 3.4. It
was ﬁrst announced in [VeK2].
19
