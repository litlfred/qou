---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-015-42-the-2-category-uqsln
section_title: "The 2-category UQ(sln)"
section_number: 4.2
pages: 22-27
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
[33]. For an elementary introduction to the categoriﬁcation of sl2 see [38].
4.2.1. Choice of scalars Q. Associated to the Cartan datum for sln we also ﬁx a choice of scalars Q
consisting of:
• tij for all i,j ∈I,
such that
• tii = 1 for all i ∈I and tij ∈ k × for i ⁄=j,
• tij =tji when aij = 0.
4.2.2. The deﬁnition. By a graded linear 2-category we mean a category enriched in grade d linear
categories, so that the hom spaces form graded linear categories , and the composition map is grading
preserving.
Given a ﬁxed choice of scalars Q we can deﬁne the following 2-category.
Deﬁnition 4.1. The 2-category UQ(sln) is the graded linear 2-category consisting of:
• objects λ for λ ∈X.
• 1-morphisms are formal direct sums of (shifts of) compositions of
1λ, 1λ+αiEi = 1λ+αi Ei1λ = Ei1λ, and 1λ−αi Fi = 1λ−αi Fi1λ = Fi1λ
for i ∈I and λ ∈X.
• 2-morphisms are k -vector spaces spanned by compositions of (decorated) tangle- like diagrams
illustrated below.
/d79/d79
•
λλ+αi
i
: Ei1λ → E i1λ⟨(αi,α i)⟩ /d15/d15
•
λλ−αi
i
: Fi1λ → F i1λ⟨(αi,α i)⟩
/d79/d79/d79/d79
i j
λ : EiEj1λ → E jEi1λ⟨−(αi,α j)⟩ /d15/d15/d15/d15i j
λ : FiFj1λ → F jFi1λ⟨−(αi,α j)⟩
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 23
/d23/d23 /d74/d74 i
λ
: 1λ → F iEi1λ⟨1 + (λ,α i)⟩ /d7/d7/d84/d84 i
λ
: 1λ → E iFi1λ⟨1 − (λ,α i)⟩
/d87/d87/d10/d10
i λ
: FiEi1λ → 1λ⟨1 + (λ,α i)⟩ /d71/d71 /d20/d20
i λ
: EiFi1λ → 1λ⟨1 − (λ,α i)⟩
Here we follow the grading conventions in [19] and [40] which are oppos ite to those from [33]. In this
2-category (and those throughout the paper) we read diagrams from right to left and bottom to top.
The identity 2-morphism of the 1-morphism Ei1λ is represented by an upward oriented line labeled by
i and the identity 2-morphism of Fi1λ is represented by a downward such line.
The 2-morphisms satisfy the following relations:
(1) The 1-morphisms Ei1λ and Fi1λ are biadjoint (up to a speciﬁed degree shift). These conditions
are expressed diagrammatically as
(4.10) /d79/d79 /d15/d15 /d79/d79
λ
λ +αi
= /d79/d79
λλ +αi
/d15/d15/d79/d79/d15/d15
λ +αi
λ
= /d15/d15
λ +αiλ
(4.11) /d79/d79/d15/d15/d79/d79
λ
λ +αi
= /d79/d79
λλ +αi
/d15/d15 /d79/d79 /d15/d15
λ +αi
λ
= /d15/d15
λ +αiλ
(2) The 2-morphisms are Q-cyclic with respect to this biadjoint structure.
(4.12) /d79/d79
/d15/d15
/d15/d15
λ +αi
λ
•
=
/d15/d15
•
λ λ +αi
= /d79/d79
/d15/d15
/d15/d15
λ +αi
λ
•
The Q-cyclic relations for crossings are given by
(4.13) /d15/d15/d15/d15i j
λ = t−1
ij
/d79/d79 /d15/d15
/d15/d15 /d79/d79 λ/d15/d15 /d79/d79
/d15/d15/d79/d79
j i
ji
= t−1
ji
/d79/d79/d15/d15
/d15/d15/d79/d79 λ /d15/d15/d79/d79
/d15/d15 /d79/d79
ij
i j
Sideways crossings can then be deﬁned utilizing the Q-cyclic condition by the equalities:
(4.14)
/d79/d79
/d15/d15j i
λ :=
/d79/d79
λ/d15/d15 /d79/d79
/d15/d15/d79/d79
i j
ij
= tij
/d15/d15
λ/d79/d79/d15/d15
/d79/d79 /d15/d15
ji
j i
(4.15) /d15/d15
/d79/d79
ij
λ :=
/d79/d79
λ/d15/d15/d79/d79
/d15/d15 /d79/d79
ji
j i
= tji
/d15/d15 λ
/d79/d79 /d15/d15
/d79/d79/d15/d15
i j
ij
where the second equality in (4.14) and (4.15) follow from (4.13).
24 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
(3) The E’s carry an action of the KLR algebra associated to Q. The KLR algebra R = RQ
associated to Q is deﬁned by ﬁnite k -linear combinations of braid–like diagrams in the plane,
where each strand is labeled by a vertex i ∈ I. Strands can intersect and can carry dots but
triple intersections are not allowed. Diagrams are considered up to p lanar isotopy that do not
change the combinatorial type of the diagram. We recall the local r elations:
i) If all strands are labeled by the same i ∈ I then the nilHecke algebra axioms (2.3) and
(2.4) hold.
ii) For i ⁄=j
(4.16) λ
/d79/d79/d79/d79
i j
=



tij
/d79/d79/d79/d79
i j
if (αi,α j) = 0,
tij
/d79/d79/d79/d79
•
i j
+ tji
/d79/d79/d79/d79
•
i j
if (αi,α j) ⁄= 0,
iii) For i ⁄=j the dot sliding relations
(4.17)
/d79/d79
•
/d79/d79
i j
=
/d79/d79
•
/d79/d79
i j
/d79/d79/d79/d79
•
i j
=
/d79/d79/d79/d79
•i j
hold.
iv) Unless i =k and (αi,α j)< 0 the relation
(4.18)
/d79/d79/d79/d79 /d79/d79
λ
i j k
=
/d79/d79/d79/d79/d79/d79
λ
i j k
holds. Otherwise, ( αi,α j) = −1 and
(4.19)
/d79/d79/d79/d79 /d79/d79
λ
i j k
−
/d79/d79/d79/d79/d79/d79
λ
i j i
= tij
/d79/d79/d79/d79 /d79/d79
i j i
(4) When i ⁄=j one has the mixed relations relating EiFj and FjEi:
(4.20) /d79/d79/d15/d15
/d15/d15
/d79/d79
λ
i j
= tji /d15/d15/d79/d79 λ
i j
/d15/d15
/d15/d15
/d79/d79
/d79/d79
λ
i j
= tij /d79/d79/d15/d15 λ
i j
(5) Negative degree bubbles are zero. That is, for all m ∈ /CI
+ one has
(4.21)
i
/d15/d15/d77/d77
•
m
λ
= 0 if m<λ i − 1,
i /d81/d81/d15/d15
•
m
λ
= 0 if m< −λi − 1.
On the other hand, a dotted bubble of degree zero is just the ident ity 2-morphism:
i
/d15/d15/d77/d77
•
λi−1
λ
= Id 1λ for λi ≥ 1,
i /d81/d81/d15/d15
•
−λi−1
λ
= Id 1λ for λi ≤ −1.
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 25
(6) For any i ∈ I one has the extended sl2-relations. In order to describe certain extended sl2
relations it is convenient to use a shorthand notation from [37] calle d fake bubbles. These are
diagrams for dotted bubbles where the labels of the number of dots is negative, but the total
degree of the dotted bubble taken with these negative dots is still p ositive. They allow us to
write these extended sl2 relations more uniformly (i.e. independent on whether the weight λi
is positive or negative).
• Degree zero fake bubbles are equal to the identity 2-morphisms
i
/d15/d15/d77/d77
•
λi−1
λ
= Id 1λ if λi ≤ 0,
i /d81/d81/d15/d15
•
−λi−1
λ
= Id 1λ if λi ≥ 0.
• Higher degree fake bubbles for λi < 0 are deﬁned inductively as
(4.22)
i
/d15/d15/d77/d77
•
λi−1+j
λ
=



−
∑
a+b=j
b≥1
/d77/d77
•
λi−1+a
/d15/d15
•
−λ−1+b
λ
if 0 ≤j <−λi + 1
0 if j <0.
• Higher degree fake bubbles for λi > 0 are deﬁned inductively as
(4.23)
i /d81/d81/d15/d15
•
−λi−1+j
λ
=



−
∑
a+b=j
a≥1
/d77/d77
•
λi−1+a
/d15/d15
•
−λ−1+b
λ
if 0 ≤j <λi + 1
0 if j <0.
These equations arise from the homogeneous terms in t of the ‘inﬁnite Grassmannian’ equation


i /d81/d81/d15/d15
•−λi−1
λ
+
i /d81/d81/d15/d15
•−λi−1+1
λ
t + · · · +
i /d81/d81/d15/d15
•−λi−1+α
λ
tα + · · ·




i /d15/d15/d77/d77
•λi−1
λ
+
i /d15/d15/d77/d77
•λi−1+1
λ
t + · · · +
i /d15/d15/d77/d77
•λi−1+α
λ
tα + · · ·

 = Id 1λ.
(4.24)
Now we can deﬁne the extended sl2 relations. Note that in [19] additional curl relations were
provided that can be derived from those above. Here we provide a m inimal set of relations.
If λi > 0 then we have:
(4.25)
λ/d75/d75
/d76/d76
/d82/d82
/d86/d86
i
= 0
i i
/d15/d15 /d79/d79 λ = − /d15/d15
/d15/d15
/d79/d79
/d79/d79
λ
i i
(4.26)
i i
/d79/d79 /d15/d15 λ = − /d79/d79/d15/d15
/d15/d15
/d79/d79
λ
i i
+
∑
f1+f2+f3
=λi−1
λ
/d15/d15/d78/d78•f3
/d9/d9/d79/d79
• f1
i /d81/d81/d15/d15
•
−λi−1+f2
i
i
If λi < 0 then we have:
(4.27)
λ /d83/d83
/d82/d82
/d76/d76
/d72/d72
i
= 0
i i
/d79/d79 /d15/d15 λ = − /d79/d79/d15/d15
/d15/d15
/d79/d79
λ
i i
26 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
(4.28)
i i
/d15/d15 /d79/d79 λλ = − /d15/d15
/d15/d15
/d79/d79
/d79/d79
λ
i i
+
∑
g1+g2+g3
=−λi−1 /d82/d82/d15/d15•g3
/d73/d73/d18/d18
•g1
i /d15/d15/d77/d77
•
λi−1+g2
i
i
λ
If λi = 0 then we have:
(4.29)
λ/d75/d75
/d76/d76
/d82/d82
/d86/d86
i
= −
λ
/d79/d79
i
λ /d83/d83
/d82/d82
/d76/d76
/d72/d72
i
=
λ
/d79/d79
i
(4.30)
i i
/d79/d79 /d15/d15 λ = − /d79/d79/d15/d15
/d15/d15
/d79/d79
l
i i i i
/d15/d15 /d79/d79 λ = − /d15/d15
/d15/d15
/d79/d79
/d79/d79
λ
i i
While the deﬁnition above may seem quite involved, the relations above encode a great deal of
interesting combinatorics. In particular, the relations above imply t hat all of the equations between
generators in ˙U(sln) lift to explicit isomorphisms in UQ(sln). For more details see [33].
In what follows it is often convenient to introduce a shorthand nota tion
λ
i
/d15/d15/d77/d77
•
♠+α
:=
λ
i
/d15/d15/d77/d77
•
λi−1+α
λ
i /d81/d81/d15/d15
•
♠+α
:=
λ
i /d81/d81/d15/d15
•
−λi−1+α
for all λi. Note that as long as α ≥ 0 this notation makes sense even when ♠ +α< 0. These negative
values are the fake bubbles deﬁned above.
Exercise 17. Use the relations above to show that the following bubble sli de equations
λ
/d79/d79
j
i /d81/d81/d15/d15
•
♠+α
=



∑α
f =0
(α + 1 −f )
λ +αj
/d79/d79
j
i /d81/d81/d15/d15
•
♠+f
•α−f
if i =j
λ +αj
/d79/d79
j
i /d81/d81/d15/d15
•
♠+α
+ t−1
ij tji
λ +αj
/d79/d79
j
i /d81/d81/d15/d15
•
♠+α−1
•
if i ·j = −1
λ +αj
/d79/d79
j
i /d81/d81/d15/d15
•
♠+α
if i ·j = 0
(4.31)
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 27
λ
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+α
=



∑α
f =0
(α + 1 −f )
λ
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+f
•α−f
if i =j
t−1
ij tji
λ
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+α−1
•
+
λ
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+α
if i ·j = −1
λ
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+α
if i ·j = 0
(4.32)
(4.33)
λ
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+α
=



λ +αi
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+(α−2)
• 2
− 2
λ +αi
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+(α−1)
•
+
λ +αi
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+α
if i =j
∑α
f =0
(−t−1
ij tji)f
λ +αj
/d79/d79
j
i
/d15/d15/d77/d77
•
♠+α−f
• f
if i ·j = −1
(4.34)
λ +αj
/d79/d79
j
i /d81/d81/d15/d15
•
♠+α
=



λ
/d79/d79
j
i /d81/d81/d15/d15
•
♠+(α−2)
• 2
− 2
λ
/d79/d79
j
i /d81/d81/d15/d15
•
♠+(α−1)
•
+
λ
/d79/d79
j
i /d81/d81/d15/d15
•
(♠+α
if i =j
∑α
f =0
(−t−1
ij tji)f
λ
/d79/d79
j
i /d81/d81/d15/d15
•
♠+(α−f )
• f
if i ·j = −1
hold in UQ(sln). Hint: see equations (6.8) and (6.9) of [19].
