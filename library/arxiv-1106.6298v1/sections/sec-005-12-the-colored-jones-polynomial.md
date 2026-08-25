---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS"
section_id: sec-005-12-the-colored-jones-polynomial
section_title: "The colored Jones polynomial"
section_number: 1.2
pages: 6-7
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariant s."
---
ordered components and V1, . . . , Vm are ﬁnite-dimensional modules over a ribbon Hopf
algebra. Then one can deﬁne the quantum invariant JL(V1, . . . , Vm) through the machinery
of quantum link invariant theory, see [21]. The quantized enveloping algebra Uh(sl2) of
sl2 is a ribbon algebra, and for each positive integer n there is a unique Uh(sl2)-module
of dimension n. The quantum link invariant JL(n1, . . . , nm), where nj stands for the nj-
dimensional Uh(sl2)-module, is usually called the colored Jones polynomial, with the nj’s
being the colors. When all the colors are 2, JL(2, . . . ,2) is the usual Jones polynomial,
which can be deﬁned using skein relation.
One can construct the colored Jones polynomial without the quant um group theory
by ﬁrst deﬁning the Jones polynomial through the skein relation, an d then deﬁning the
colored Jones polynomial by using cablings, see e.g. [10, 11].
Let us recall here a few well–known formulas. For the unknot U with 0 framing one
has
(1) JU (n) = [ n]
Moreover, JL is multiplicative with respect to the disjoint union. If L1 is obtained from
L by increasing the framing of the ith component by 1, then
(2) JL1(n1, . . . , nm) = q(n2
i−1)/ 4JL(n1, . . . , nm).
If all the colors ni are odd, then JL(n1, . . . , nm) ∈ Z[q±1].
1.3. Kirby moves. By Kirby theorem, any link invariant which does not change under
Kirby moves is an invariant of a 3–manifold given by surgery on that link . Let us ﬁrst
recall what the Kirby moves are.
K1–Move (handle slide): For some i ⁄= j, replace the ith component Li with L′
i, a
band connected sum of Li with a push oﬀ of Lj (deﬁned by the framing), with b′
i =
bi + bj + 2lk(Li, Lj).
K2–Move (blow up): Add (or delete) a split unknotted component with framing ±1.
These two moves are equivalent to the one Fenn–Rourke move deﬁn ed as follows:
UNIFIED 3–MANIFOLD INV ARIANTS 7
FR–Move Locally the following two pictures are interchangeable
twistε
...
ε......
    strandsm
where ε ∈ { 1, −1} and the closed component has framing ε. Note that K2–Move corre-
sponds to the case when m = 0.
The main idea of the construction of the WRT invariants is to make the colored Jones
polynomial invariant under Kirby moves by averaging over all colors. To make this precise,
we have to choose the quantum parameter q to be a root of unity, otherwise the sum would
be inﬁnite.
