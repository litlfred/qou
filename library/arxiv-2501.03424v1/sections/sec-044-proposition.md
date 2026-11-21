---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-044-proposition
section_title: "Proposition"
section_number: null
pages: 18-20
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
4.5.2
Proposition
2 Let g be a complex semisimple Lie algebra. Then Soergel’s conjecture for the geometric repre-
sentation of its Weyl group W implies the Kazhdan-Lusztig conjecture for g.
Proof: We will begin by induction on Bruhat order. We have
Prid = Mid,
which implies that [Prid] = id = bid|v=1. Let x > id in Bruhat order. Choose s ∈S such that
xs < s, and take x = ws, where w < x. Then
ΘsPrw ≃Prx ⊕
M
z<x
Pr⊕mz
z
for multiplicities mz ≥0. In the Grothendieck group, we obtain by induction
[Prx] = [ΘsPrw] −
X
z<x
mz[Prz] = [Prw](1 + s) −
X
z<x
mz[Prz]
= bwbs −
X
mzbz|v=1.
Applying V to ΘsPrw, we get
BwBs ≃Bx ⊕
M
z<x
Bz
⊕mz,
and since Soergel modules decompose the same as Soergel bimodules,
BwBs ≃Bx ⊕
M
z<x
B⊕mz
z
.
18
Taking characters and invoking Soergel’s conjecture, we get
bx = bwbs −
X
z<x
mzbz.
Then by the equality
[Prw](1 + s) −
X
z<x
mz[Prz] = bwbs −
X
mzbz|v=1,
we get [Prx] = bx|v=1, which is the equivalent form of the Kazhdan-Lusztig conjecture.
19
