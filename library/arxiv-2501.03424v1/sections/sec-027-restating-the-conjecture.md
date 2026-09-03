---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner"
section_id: sec-027-restating-the-conjecture
section_title: "Restating the conjecture"
section_number: null
pages: 18-20
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials ethan eugene wynner — This paper presents an exposition of Soergel bimodules, the categ oriﬁcation of Hecke alge- bras, and their applications to"
---
The Kazhdan-Lusztig conjecture states that for a complex semis imple Lie algebra g, and any
x, y in the Weyl group W,
[My : Lx] = hy,x (1)
where hy,x (1) is the value of the Kazhdan-Lusztig polynomial hy,x (v) at v = 1. By Bernstein-
Gelfand-Gelfand reciprocity6.5, the Kazhdan-Lusztig conjectur e is equivalent to stating
(Prx : My) = hy,x (1).
Using the correspondence [O0]≃ Z[W ] in the Grothendieck group, this means that we equivalently
have
[Prx] = bx|v=1,
where bx|v=1 is the specialization at v = 1 of the Kazhdan-Lusztig basis element bx∈H . Recall
ﬁnally that Soergel’s conjecture is true if for every x∈ W,
χ(Bx) = bx.
We now move to our ﬁnal proposition.
4.5.2 Proposition
2 Let g be a complex semisimple Lie algebra. Then Soergel’s conject ure for the geometric repre-
sentation of its Weyl group W implies the Kazhdan-Lusztig conjecture for g.
Proof: We will begin by induction on Bruhat order. We have
Prid = Mid,
which implies that [Pr id] = id = bid|v=1. Let x > id in Bruhat order. Choose s∈ S such that
xs < s, and take x = ws, where w < x. Then
Θ sPrw≃ Prx⊕
⨁
z<x
Pr⊕mz
z
for multiplicities mz≥ 0. In the Grothendieck group, we obtain by induction
[Prx] = [Θ sPrw]−
∑
z<x
mz[Prz] = [Pr w](1 + s)−
∑
z<x
mz[Prz]
= bwbs−
∑
mzbz|v=1.
Applying V to Θ sPrw, we get
BwBs≃ Bx⊕
⨁
z<x
Bz
⊕mz
,
and since Soergel modules decompose the same as Soergel bimodule s,
BwBs≃ Bx⊕
⨁
z<x
B⊕mz
z .
18
Taking characters and invoking Soergel’s conjecture, we get
bx = bwbs−
∑
z<x
mzbz.
Then by the equality
[Prw](1 + s)−
∑
z<x
mz[Prz] = bwbs−
∑
mzbz|v=1,
we get [Pr x] = bx|v=1, which is the equivalent form of the Kazhdan-Lusztig conjecture.
19
