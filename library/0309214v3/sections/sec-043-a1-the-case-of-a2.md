---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-043-a1-the-case-of-a2
section_title: "A.1 The case of A2"
section_number: null
pages: 37-38
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
The case of A2
There are two fundamental roots denoted by α and β. The set of positive roots
is {α, β, α+β}. The reduced representations of the longest element of the Weyl
group are w = s1s2s1 and w′ = s2s1s2, where s1 = sα and s2 = sβ .
The total ordering (see Section 7.1.4) of the set of positive roots corresponding
to w and w′ are, respectively:
(γ1, γ2, γ3)
=
(α, α + β, β)
(γ1′, γ2′, γ3′)
=
(β, α + β, α).
Notice that γi′ = γ3−i for i = 1, . . . , 3.
The PBW basis of U−(see Section 7.1.5) corresponding to w and w′ are,
respectively:
{f m
3 f n
2 f p
1 | m, n, p ∈N},
{f m
3′ f n
2′f p
1′ | m, n, p ∈N},
where
(f3, f2, f1)
=
(Fβ, Tα(Fβ) = −v[Fβ, Fα]q = FβFα −vFαFβ, Fα)
(f3′, f2′, f1′)
=
(Fα, Tβ(Fα) = FαFβ −vFβFα, Fβ).
From explicit formulas of [23, section 5] it follows that:
Lemma A.1 The structure constants of U−, in the basis of w, is q–holonomic.
Let us deﬁne a scalar product (·, ·) on U−such that the PBW basis of w is an
orthonormal basis. Since
f m′
3′ f n′
2′ f p′
1′ =
X
m,n,p
(f m′
3′ f n′
2′ f p′
1′ , f m
3 f n
2 f n
1 )f m
3 f n
2 f p
1
Geometry & Topology, Volume 9 (2005)
1290
Stavros Garoufalidis and Thang T Q Lˆe
Proposition 7.3 is equivalent to showing that
(f m′
3′ f n′
2′ f p′
1′ , f m
3 f n
2 f n
1 )
is q–holonomic in all variables m, n, p, m′, n′, p′.
Since multiplication is q–holonomic in the PBW basis of w (see Lemma A.1),
it suﬃces to show that
(f k
i′, f m
3 f n
2 f n
1 )
is q–holonomic in k, m, n, p for each i = 1, 2, 3. This is clear for i = 1 or i = 3,
since f1′ = f3 and f3′ = f1. As for f2′ , an easy induction shows that
f n
2′ = (−v)−n
∞
X
k=0
v−k(k−3)/2(v −v−1)k
 n
k

f k
3 f n−k
2
f k
1 .
and the statement also holds true for i = 2. This proves Proposition 7.3 for
A2.
