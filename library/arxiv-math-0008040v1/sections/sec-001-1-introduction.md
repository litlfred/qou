---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
Let U = Uq(g) be the quantum group associated to a semisimple Lie algebra g of rank n. The
negative part U − of U has a canonical basis B with favourable properties (see Kashiwara [7] and
Lusztig [11, §14.4.6]). For example, via action on highest weight vectors it gives rise to bases for
all the ﬁnite-dimensional irreducible highest weight U -modules.
Let W be the Weyl group of g, with Coxeter generators s1,s 2,... ,s n, and let w0 be the element
of maximal length in W . Let i be a reduced expression for w0, i.e. w0 = si1si2 · · ·sik is reduced.
Lusztig obtains a parametrization of the canonical basis B for each such reduced expression i, via
a correspondence between a basis of PBW-type associated to i and the canonical basis. This gives
a bijection ϕ i : B → Nk, where N = {0, 1, 2,... }.
Kashiwara, in his approach to the canonical basis (which he c alls the global crystal basis), deﬁnes
certain root operators ~Fi on the canonical basis (see [7, §3.5]) which lead to a parametrization of
the canonical basis for each reduced expression i by a certain subset Yi of Nk. This gives a bijection
ψ i : B →Yi. The subset Yi is called the string cone.
There is no simple way to express the elements of B in terms of the natural generators F1,F 2,... ,F n
ofU −. This has been done for all of B only in types A1,A 2,A 3 andB2 (see [9, §3.4], [12, §13], [20]
and [19]) and appears to become arbitrarily complicated in g eneral.
A monomial F (a1)
i1 F (a2)
i2 · · ·F (ak)
ik
, where F (a)
i = F a
i / [a]!, is said to be tight if it belongs to B.
1
Lusztig [12] described a method which in low rank cases leads to the construction of tight monomials.
He deﬁned, for each reduced expression i of w0, a certain cone Ci in Nk which we shall call the
Lusztig cone. Let
Mi = {F (a1)
i1 F (a2)
i2 · · ·F (ak)
ik : a ∈Ci}
be the set of monomials obtained from elements of Ci. Lusztig showed that, in types A1,A 2 and
A3, Mi ⊆ B. The author [14] has extended this to type A4. However, counter-examples of Xi [21]
and Reineke [18] show that this fails for higher rank.
Instead, one can consider monomials in Kashiwara’s operato rs ~Fi. Deﬁne, for a reduced expression
i for w0,
Bi = {b ∈ B : b ≡ ~F a1
i1
~F a2
i2 · · · ~F ak
ik
· 1, a ∈Ci}.
It has been shown by Premat [16] that Ci ⊆ Yi, so we have Bi = ψ −1
i (Ci). Then it is known
that Bi =Mi in types A1,A 2,A 3 (using Lusztig’s work [12] and direct calculation); it will be seen
in [6] that this is also true in type A4. This breaks down in higher ranks because of the above
counter-examples. Thus Bi can be regarded as a generalisation of Mi for higher ranks, and it is
likely that canonical basis elements in Bi will have a common form.
Furthermore, the cones Ci play a role with respect to various reparametrization funct ions of the
canonical basis. Let i, j be reduced expressions for w0. There is a reparametrization function,
Rj
i = ϕ jϕ −1
i : Nk → Nk (see [9, §2]); a reparametrization function T j
i = ψ jψ −1
i : Yi → Yj (see [3,
§§2.6, 2.7] and also the remark at the end of Section 2 of [15]). W e also deﬁne a reparametrization
function Sj
i = ϕ jψ −1
i : Yi → Nk linking the approaches of Lusztig and Kashiwara. The functi ons
Rj
i and T j
i are known to be piecewise-linear, and it follows that Sj
i is also piecewise-linear. These
functions are very diﬃcult to understand; they have recentl y been described by Zelevinsky in [4],
but their regions of linearity are only known in types A1–A5, B2, C3, D4 and G2 (see [5] and
references therein).
Suppose now that g is of type An. In [13], it was shown that Ci could be expressed as the set of
nonnegative integral combinations of a certain set of k spanning vectors, vj(i),j = 1,... ,n ,vP (i),
P a partial quiver of type An associated to i (as described in [13]). A partial quiver of type An is
a quiver of type An with some directed edges replaced by undirected edges in suc h a way that the
subgraph of directed edges is connected.
If an element a = (a1,a 2,... ,a k) ∈ Ci is written a = (aα )α ∈Φ + , where Φ + is the set of positive
roots of g and aα =aj where α is the jth root in the ordering on Φ + induced by i, then the vj(i)
and the vP (i) do not depend on i and are described in [13]. These vectors have also been studi ed by
B´ edard [1] in terms of the representation theory of quivers. Here we show that if a = (a1,a 2,... ,a k)
is one of these vectors then the corresponding monomial of Ka shiwara’s operators ~F a1
i1
~F a2
i2 · · · ~F ak
ik · 1
can be described using a remarkable rectangle combinatoric s.
For j = 1, 2,... ,n and P a partial quiver associated to i, let bj(i) = ψ −1
i (vj(i)) and bP (i) =
ψ −1
i (vP (i)) be the corresponding canonical basis elements. We will sh ow that these elements are
independent of the reduced expression i. Thus the canonical basis elements arising in this way for
at least one reduced expression i can be labelled bj, j = 1, 2,... ,n , bP , P a partial quiver of type
An.
The following conjecture, which will be shown in type A4 in [6], suggests that these elements are
important in understanding the canonical basis. For a reduc ed expression j forw0, let cj(j) = φ j(bj)
2
and let cP (j) = φ j(bP ) be the parametrizations of these canonical basis elements arising from
Lusztig’s approach.
Conjecture 1.1 (Carter and Marsh)
Let i be a reduced expression for w0 and let k = (1 , 3, 5,... 2, 4, 6,... ) and
k′ = (2 , 4, 6,... , 1, 3, 5,... ), the opposite reduced expressions for w0 arising in [9]. Then the
vectorscj(k), j = 1, 2,... ,n , cP (k), P a partial quiver associated with i as above form a simplicial
region of linearity Xi of Lusztig’s piecewise-linear function Rk′
k . Furthermore, all such simplicial
regions arise in this way, and the map i ↦→Xi from the graph of commutation classes of reduced
expressions for w0 (with edges given by the long braid relation) to the graph of s implicial regions of
linearity of R (with edges given by adjacency) is a graph isomorphism.
In this paper we shall use the above rectangle combinatorics to calculate the vectors cj(j), cP (j)
for the reduced expression j = (n,n − 1,n,n − 2,n − 1,n,... , 1, 2,... ,n ) for w0. This will be used
in a future paper of Carter in order to calculate the vectors cj(k), cP (k), and thus the conjectural
simplicial regions of linearity of Rk′
k . It is also possible that the above conjecture is true for any
pair of opposite reduced expressions k, k′ forw0; in particular for j and its opposite j′, i.e. that the
vectorscj(j) and cj
P span simplicial regions of linearity of Rj′
j .
