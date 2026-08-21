---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-010-4-regularized-distribution-relations
section_title: "Regularized distribution relations"
section_number: 4
pages: 10-12
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
It is well-known that multiple polylogs satisfy the followi ng distribution formula
(cf. [26, Prop. 2.25]):
Lis1,...,sn (x1, . . . , xn) = ds1+···+sn−n ∑
yd
j =xj ,1≤j≤n
Lis1,...,sn (y1, . . . , yn), (14)
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm V alues 11
for all positive integer d. When s1 = 1 one has to exclude the divergent case
x1 = 1. We call these ﬁnite distribution relations (FDT). Racinet further
considers the regularized version of these relations, whic h we now recall brieﬂy.
Fix an embedding µ N֒→C and denote by Γ its image. Deﬁne two sets of
words
X := XΓ = {xσ : σ ∈ Γ ∪ {0}}, and Y := YΓ = {xn−1
0 xσ : n ∈ N, σ ∈ Γ }.
Then one may consider the coproduct ∆ of Q⟨X⟩deﬁned by ∆ xσ = 1 ⊗ xσ +
xσ ⊗ 1 for all σ ∈ Γ ∪ {0}. For every path γ ∈ P1(C) − ({0, ∞} ∪ Γ) Racinet
deﬁnes the group-like element Iγ ∈ C⟨ ⟨X⟩ ⟩by
Iγ :=
∑
p∈N,σ1,...,σp∈Γ ∪{0}
Iγ(σ1, . . . , σp)xσ1 · · ·xσp ,
where Iγ(σ1, . . . , σp) is the iterated integral
∫
γ ω(σ1) · · ·ω(σp) with
ω(σ)(t) =
{
σ dt/(1 − σt), if σ ⁄= 0;
dt/t, if σ = 0.
(One has to correct the obvious typo in the displayed formula just before Prop.
2.8 in [26] by changing aj to αj.) This Iγ is essentially the same element
denoted by dch in [17]. Note that Q⟨Y⟩is the sub-algebra of Q⟨X⟩generated
by words not ending with x0. Let πY : Q⟨X⟩ → Q⟨Y⟩ be the projection. As
x0 is a primitive element one quickly deduces that ( Q⟨Y⟩, ∆) has a graded
co-algebra structure.
Let Q⟨X⟩cv be the sub-algebra of Q⟨X⟩not beginning with x1 and not ending
with x0. Let πcv : Q⟨X⟩ →Q⟨X⟩cv be the projection. Passing to the limit one
gets:
Proposition 4.1. ([26, Prop.2.11]) The series Icv := lim a→0+,b→1− πcv(I[a,b])
is group-like in (C⟨ ⟨X⟩ ⟩cv, ∆) .
Remark 4.2. The algebras A, A0 and A1 in §2 are essentially equal to Q⟨X⟩,
Q⟨X⟩cv and Q⟨Y⟩, respectively, after setting a = x0 and bj = xµ j .
Let I be the unique group-like element in ( C⟨ ⟨X⟩ ⟩, ∆) whose coeﬃcients of x0
and x1 are 0 such that πcv(I) = Icv. In order to do the numerical computation
one needs to determine explicitly the coeﬃcients for I. Put
I =
∑
p∈N,,σ1,...,σp∈Γ ∪{0}
C(σ1, . . . , σp)xσ1 · · ·xσp . (15)
Proposition 4.3. Let p, m and n be three non-negative integers. If p > 0 then
Documenta Mathematica 15 (2010) 1–34
