---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-003-1-b-is-a-qv-basis-of-u-called-the-canonical
section_title: "(B) is a Q(v)-basis of U −, called the canonical"
section_number: 1
pages: 4-5
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
basis.
Lusztig’s theorem provides us with a parametrization of B, dependent on i. If b ∈ B, we write
ϕ i(b) = c, where c ∈ Nk satisﬁes b ≡F c
i mod vL. Note that ϕ i is a bijection.
Given any pair i, j ∈ χ n, Lusztig deﬁnes in [9, §2.6] a function Rj
i = ϕ jϕ −1
i : Nk → Nk, which
he shows is piecewise-linear. He further shows that its regi ons of linearity are signiﬁcant for the
canonical basis, in the sense that elements b of the canonical basis with ϕ i(b) in the same region of
linearity of Rj
i often have similar form.
Kashiwara’s approach
Let ~Ei and ~Fi be the Kashiwara operators on U − as deﬁned in [7, §3.5]. Let A ⊆ Q(v) be the
subring of elements regular at v = 0, and let L′ be the A-lattice spanned by the set S of arbitrary
products ~Fj1
~Fj2 · · · ~Fjm · 1 in U −. The following results were proved by Kashiwara in [7].
Theorem 2.2 (Kashiwara)
(i) Let π ′ : L′ → L ′/v L′ be the natural projection, and let B′ = π ′(S). Then B′ is a Q-basis of
L′/v L′ (the crystal basis).
(ii) The operators ~Ei and ~Fi each preserve L′ and thus act on L′/v L′. They satisfy ~Ei(B′) ⊆B′∪{0}
and ~Fi(B′) ⊆B′. For b,b ′ ∈B′ we have ~Fib =b′ if and only if ~Eib′ =b.
(iii) For each b ∈B′, there is a unique element ˜b ∈ L ′ ∩
L′ such that π ′(˜b) = b. The set of elements
{˜b : b ∈B′} forms a basis of U −, the global crystal basis of U −.
It was shown by Lusztig [10, 2.3] that the global crystal basi s of Kashiwara coincides with the
canonical basis. There is a parametrization of B arising from Kashiwara’s approach, again de-
pendent on i ∈ χ n. Let i = (i1,i 2,... ,i k) and b ∈ B. Let a1 be maximal such that ~Ea1
i1b ⁄≡0
mod vL′; let a2 be maximal such that ~Ea2
i2
~Ea1
i1b ⁄≡0 mod vL′, and so on, so that ak is maximal
such that ~Eak
ik
~Eak−1
ik−1 · · · ~Ea2
i2
~Ea1
i1b ⁄≡0 mod vL′. We write ψ i(b) = a = (a1,a 2,... ,a k) and we have
4
1
2
3
4
1 3 2 1 3 2
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . ........................................................ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . .
134
13
3
Figure 1: The Chamber Diagram of (1 , 3, 2, 1, 3, 2).
b ≡ ~F a1
i1
~F a2
i2 · · · ~F ak
ik · 1 mod vL′. This is the crystal string of b — see [3, §2], [15, §2] and [8]. The
map ψ i is injective (see [15, §2.5]). Its image is a cone, which we shall call the string cone associ-
ated to i, Yi =ψ i(B). We deﬁne a function which compares Kashiwara’s approach w ith Lusztig’s
approach. For i, j ∈χ n, let Sj
i =ϕ jψ −1
i : Yi → Nk.
