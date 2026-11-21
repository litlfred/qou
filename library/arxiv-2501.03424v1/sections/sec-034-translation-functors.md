---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-034-translation-functors
section_title: "Translation functors"
section_number: null
pages: 14-15
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
Translation functors
Fixing the decomposition of g = n+ ⊕h ⊕n−, the weight lattice P ⊂h∗, root system3 R±,
simple roots Π, and the Weyl group W, we consider the W-action on h∗, given by
w · λ = w(λ + ρ) −ρ,
for w ∈W, λ ∈h∗, ρ = 1
2
P
α∈R+ α. Then O has the decomposition
O =
M
λ∈h∗/W
Oλ,
with simple objects {L(w·λ) | w ∈W} in each Oλ.
4.2.1
Let λ ∈h∗. Deﬁne
ιλ : Oλ֒ →O, πλ : O ։ Oλ
as the inclusion and projection, respectively, associated with Oλ. Let λ, µ ∈h∗be compatible
(λ −µ is integral). Let η be the unique dominant integral weight in W(λ−µ) Let Vη be the ﬁnite
dimensional irreducible representation of highest weight η. The translation functor T µ
λ is the exact
(by composition) functor
T µ
λ := πµ ◦(V ⊗(−)) ◦ιλ : Oλ →Oµ.
3it is important to clarify that what we mean by R± will always be a root system. Any use of R without a plus or
minus subscript will be the symmetric algebra associated to our construction of Soergel (bi)modules, unless explicitly
stated otherwise.
14
