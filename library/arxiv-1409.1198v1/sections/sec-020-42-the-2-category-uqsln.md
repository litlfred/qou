---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-020-42-the-2-category-uqsln
section_title: "The 2-category UQ(sln)"
section_number: 4.2
pages: 22-27
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
[33]. For an elementary introduction to the categoriﬁcation of sl2 see [38].
4.2.1. Choice of scalars Q. Associated to the Cartan datum for sln we also ﬁx a choice of scalars Q
consisting of:
• tij for all i, j ∈I,
such that
• tii = 1 for all i ∈I and tij ∈k× for i̸ = j,
• tij = tji when aij = 0.
4.2.2. The deﬁnition. By a graded linear 2-category we mean a category enriched in graded linear
categories, so that the hom spaces form graded linear categories, and the composition map is grading
preserving.
Given a ﬁxed choice of scalars Q we can deﬁne the following 2-category.
Deﬁnition 4.1. The 2-category UQ(sln) is the graded linear 2-category consisting of:
• objects λ for λ ∈X.
• 1-morphisms are formal direct sums of (shifts of) compositions of
1λ,
1λ+αiEi = 1λ+αiEi1λ = Ei1λ,
and
1λ−αiFi = 1λ−αiFi1λ = Fi1λ
for i ∈I and λ ∈X.
• 2-morphisms are k-vector spaces spanned by compositions of (decorated) tangle-like diagrams
illustrated below.
O
•
λ
λ+αi
i
: Ei1λ →Ei1λ⟨(αi, αi)⟩

•
λ
λ−αi
i
: Fi1λ →Fi1λ⟨(αi, αi)⟩
O
O
i
j
λ : EiEj1λ →EjEi1λ⟨−(αi, αj)⟩


i
j
λ : FiFj1λ →FjFi1λ⟨−(αi, αj)⟩
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR
23

J i
λ
: 1λ →FiEi1λ⟨1 + (λ, αi)⟩

T
i
λ
: 1λ →EiFi1λ⟨1 −(λ, αi)⟩
W

i
λ : FiEi1λ →1λ⟨1 + (λ, αi)⟩
G

i
λ : EiFi1λ →1λ⟨1 −(λ, αi)⟩
Here we follow the grading conventions in [19] and [40] which are opposite to those from [33]. In this
2-category (and those throughout the paper) we read diagrams from right to left and bottom to top.
The identity 2-morphism of the 1-morphism Ei1λ is represented by an upward oriented line labeled by
i and the identity 2-morphism of Fi1λ is represented by a downward such line.
The 2-morphisms satisfy the following relations:
(1) The 1-morphisms Ei1λ and Fi1λ are biadjoint (up to a speciﬁed degree shift). These conditions
are expressed diagrammatically as
(4.10)
O

O
λ
λ + αi
=
O
λ
λ + αi

O

λ + αi
λ
=

λ + αi
λ
(4.11)
O

O
λ
λ + αi
=
O
λ
λ + αi

O

λ + αi
λ
=

λ + αi
λ
(2) The 2-morphisms are Q-cyclic with respect to this biadjoint structure.
(4.12)
O


λ + αi
λ
•
=

•
λ
λ + αi
=
O


λ + αi
λ
•
The Q-cyclic relations for crossings are given by
(4.13)


i
j
λ
=
t−1
ij
O


O λ

O

O
j
i
j
i
=
t−1
ji
O


O
λ 
O

O
i
j
i
j
Sideways crossings can then be deﬁned utilizing the Q-cyclic condition by the equalities:
(4.14)
O

j
i
λ
:=
O
λ

O

O
i
j
i
j
=
tij

λ
O

O

j
i
j
i
(4.15)

O
i
j
λ
:=
O
λ

O

O
j
i
j
i
=
tji

λ
O

O

i
j
i
j
where the second equality in (4.14) and (4.15) follow from (4.13).
24
ANNA BELIAKOVA, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LAUDA
(3) The E’s carry an action of the KLR algebra associated to Q.
The KLR algebra R = RQ
associated to Q is deﬁned by ﬁnite k-linear combinations of braid–like diagrams in the plane,
where each strand is labeled by a vertex i ∈I. Strands can intersect and can carry dots but
triple intersections are not allowed. Diagrams are considered up to planar isotopy that do not
change the combinatorial type of the diagram. We recall the local relations:
i) If all strands are labeled by the same i ∈I then the nilHecke algebra axioms (2.3) and
(2.4) hold.
ii) For i̸ = j
(4.16)
λ
O
O
i
j
=



















tij
O
O
i
j
if (αi, αj) = 0,
tij
O
O
•
i
j
+ tji
O
O
•
i
j
if (αi, αj)̸ = 0,
iii) For i̸ = j the dot sliding relations
(4.17)
O
•
O
i
j
=
O
•
O
i
j
O
O
•
i
j
=
O
O
•
i
j
hold.
iv) Unless i = k and (αi, αj) < 0 the relation
(4.18)
O
O
O
λ
i
j
k
=
O
O
O
λ
i
j
k
holds. Otherwise, (αi, αj) = −1 and
(4.19)
O
O
O
λ
i
j
k
−
O
O
O
λ
i
j
i
=
tij
O
O
O
i
j
i
(4) When i̸ = j one has the mixed relations relating EiFj and FjEi:
(4.20)
O


O
λ
i
j
=
tji

O
λ
i
j


O
O
λ
i
j
=
tij
O

λ
i
j
(5) Negative degree bubbles are zero. That is, for all m ∈
Z+ one has
(4.21)
i

M
•
m
λ
= 0
if m < λi −1,
i
Q

•
m
λ
= 0
if m < −λi −1.
On the other hand, a dotted bubble of degree zero is just the identity 2-morphism:
i

M
•
λi−1
λ
= Id1λ
for λi ≥1,
i
Q

•
−λi−1
λ
= Id1λ
for λi ≤−1.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR
25
(6) For any i ∈I one has the extended sl2-relations. In order to describe certain extended sl2
relations it is convenient to use a shorthand notation from [37] called fake bubbles. These are
diagrams for dotted bubbles where the labels of the number of dots is negative, but the total
degree of the dotted bubble taken with these negative dots is still positive. They allow us to
write these extended sl2 relations more uniformly (i.e. independent on whether the weight λi
is positive or negative).
• Degree zero fake bubbles are equal to the identity 2-morphisms
i

M
•
λi−1
λ
= Id1λ
if λi ≤0,
i
Q

•
−λi−1
λ
= Id1λ
if λi ≥0.
• Higher degree fake bubbles for λi < 0 are deﬁned inductively as
(4.22)
i

M
•
λi−1+j
λ
=











−
P
a+b=j
b≥1
M
•
λi−1+a

•
−λ−1+b
λ
if 0 ≤j < −λi + 1
0
if j < 0.
• Higher degree fake bubbles for λi > 0 are deﬁned inductively as
(4.23)
i
Q

•
−λi−1+j
λ
=











−
P
a+b=j
a≥1
M
•
λi−1+a

•
−λ−1+b
λ
if 0 ≤j < λi + 1
0
if j < 0.
These equations arise from the homogeneous terms in t of the ‘inﬁnite Grassmannian’ equation


i
Q

•
−λi−1
λ
+
i
Q

•
−λi−1+1
λ
t + · · · +
i
Q

•
−λi−1+α
λ
tα + · · ·




i

M
•
λi−1
λ
+
i

M
•
λi−1+1
λ
t + · · · +
i

M
•
λi−1+α
λ
tα + · · ·

= Id1λ.
(4.24)
Now we can deﬁne the extended sl2 relations. Note that in [19] additional curl relations were
provided that can be derived from those above. Here we provide a minimal set of relations.
If λi > 0 then we have:
(4.25)
λ
K
L
R
V
i
=
0
i
i

O
λ
=
−


O
O
λ
i
i
(4.26)
i
i
O

λ
=
−
O


O
λ
i
i
+
X
f1+f2+f3
=λi−1
λ

N•
f3
	
O
•f1
i
Q

•
−λi−1+f2
i
i
If λi < 0 then we have:
(4.27)
λ
S
R
L
H
i
=
0
i
i
O

λ
=
−
O


O
λ
i
i
26
ANNA BELIAKOVA, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. LAUDA
(4.28)
i
i

O
λ
λ
=
−


O
O
λ
i
i
+
X
g1+g2+g3
=−λi−1
R
•
g3
I

•g1
i

M
•
λi−1+g2
i
i
λ
If λi = 0 then we have:
(4.29)
λ
K
L
R
V
i
=
−
λ
O
i
λ
S
R
L
H
i
=
λ
O
i
(4.30)
i
i
O

λ
=
−
O


O
l
i
i
i
i

O
λ
=
−


O
O
λ
i
i
While the deﬁnition above may seem quite involved, the relations above encode a great deal of
interesting combinatorics. In particular, the relations above imply that all of the equations between
generators in ˙U(sln) lift to explicit isomorphisms in UQ(sln). For more details see [33].
In what follows it is often convenient to introduce a shorthand notation
λ
i

M
•
♠+α
:=
λ
i

M
•
λi−1+α
λ
i
Q

•
♠+α
:=
λ
i
Q

•
−λi−1+α
for all λi. Note that as long as α ≥0 this notation makes sense even when ♠+ α < 0. These negative
values are the fake bubbles deﬁned above.
Exercise 17. Use the relations above to show that the following bubble slide equations
λ
O
j
i
Q

•
♠+α
=















































P
α
f=0
(α + 1 −f)
λ + αj
O
j
i
Q

•
♠+f
•α−f
if i = j
λ + αj
O
j
i
Q

•
♠+α
+
t−1
ij tji
λ + αj
O
j
i
Q

•
♠+α−1
•
if i · j = −1
λ + αj
O
j
i
Q

•
♠+α
if i · j = 0
(4.31)
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR
27
λ
O
j
i

M
•
♠+α
=







































P
α
f=0
(α + 1 −f)
λ
O
j
i

M
•
♠+f
•α−f
if i = j
t−1
ij tji
λ
O
j
i

M
•
♠+α−1
•
+
λ
O
j
i

M
•
♠+α
if i · j = −1
λ
O
j
i

M
•
♠+α
if i · j = 0
(4.32)
(4.33)
λ
O
j
i

M
•
♠+α
=

























λ + αi
O
j
i

M
•
♠+(α−2)
• 2
−2
λ + αi
O
j
i

M
•
♠+(α−1)
•
+
λ + αi
O
j
i

M
•
♠+α
if i = j
P
α
f=0
(−t−1
ij tji)f
λ + αj
O
j
i

M
•
♠+α−f
• f
if i · j = −1
(4.34)
λ + αj
O
j
i
Q

•
♠+α
=

























λ
O
j
i
Q

•
♠+(α−2)
• 2
−2
λ
O
j
i
Q

•
♠+(α−1)
•
+
λ
O
j
i
Q

•
(♠+α
if i = j
P
α
f=0
(−t−1
ij tji)f
λ
O
j
i
Q

•
♠+(α−f)
• f
if i · j = −1
hold in UQ(sln). Hint: see equations (6.8) and (6.9) of [19].
