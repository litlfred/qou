---
doc_id: arxiv-math-0404010v1
doc_title: "YANG–BAXTER OPERATORS ARISING FROM ALGEBRA STRUCTURES AND THE ALEXANDER POLYNOMIAL OF KNOTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0404010v1.pdf
source_sha256: a9522d4bec3ce6fb
toc_source: outline
doc_brief: "YANG–BAXTER OPERATORS ARISING FROM ALGEBRA STRUCTURES AND THE ALEXANDER POLYNOMIAL OF KNOTS — In this paper, we consider the problem of constructing knot invariants from Yang–Baxter operators"
---
The Yang–Baxter equation and its solutions, the Yang–Baxter operators, ﬁrst ap-
peared in theoretical physics and statistical mechanics. Later, this equation has emerged
in other ﬁelds of mathematics such as quantum group theory. Some references on this
topic are [5, 7].
The Yang–Baxter equation also plays an important role in knot theory. Indeed, Tu-
raev has described in [12] a general scheme to derive an invariant of oriented links from a
Yang–Baxter operator, provided this one can be “enhanced”. The Jones polynomial [4]
and its two–variable extensions, namely the Homﬂypt polynomial [2, 10] and the Kauﬀ-
man polynomial [6], can be obtained in that way by “enhancing” some Yang–Baxter
operators obtained in [3]. Those solutions of the Yang–Baxter equation are associated
to simple Lie algebras and their fundamental representations. The Alexander polyno-
mial can be derived from a Yang–Baxter operator as well, using a slight modiﬁcation of
Turaev’s construction [8].
More recently, D˘asc˘alescu and Nichita have shown in [1] how to associate a Yang–
Baxter operator to any algebra structure over a vector space, using the associativity
of the multiplication. This method to produce solutions to the Yang–Baxter equation,
initiated in [9], is quite simple.
In this paper, we consider the problem of applying Turaev’s method to Yang–Baxter
operators derived from algebra structures. In general, ﬁnding the enhancements of a
given Yang–Baxter operator can be diﬃcult or lengthy. In the case of Yang–Baxter
operators associated to algebra structures, the simplicity of their deﬁnition makes the
search for enhancements an easy task. We do this here in full generality. We conclude
from this computation that the only invariant which can be obtained from those Yang–
Baxter operators is the Alexander polynomial of knots. Thus, in a way, the Alexander
polynomial is the knot invariant corresponding to the axioms of (unitary associative)
algebras. Note that specializations of the Homﬂypt polynomial had to be expected from
those Yang–Baxter operators since they have degree 2 minimal polynomials.
The paper is organized as follows. In §2, we recall how to associate to any (unitary
associative) algebra a Yang–Baxter operator. Next, in §3, we review Turaev’s proce-
dure to derive a knot invariant from a Yang–Baxter operator as soon as this one can be
Date: January, 2004.
1
2
G. MASSUYEAU AND F. F. NICHITA
enhanced. Following Murakami [8], we recall how this method can be improved in the
case when the Yang–Baxter operator satisﬁes a certain redundancy property. The fact
that their minimal polynomials are quadratic implies that the Yang–Baxter operators
associated to algebra structures are redundant (Proposition 3.6). In §4, we compute
the enhancements of the Yang–Baxter operator associated to a given algebra structure.
Finally, we conclude from this calculation that Turaev’s procedure, as modiﬁed by Mu-
rakami, invariably produces from any of those enhancements the Alexander polynomial
of knots (Theorem 4.3).
Throughout the paper, we shall use the following conventions and notations. The
letter k will denote a ﬁxed ﬁeld with characteristic char(k)̸ = 2. For a k–vector space V
and an integer n ≥1, we denote by V ⊗n the n–times tensor product V ⊗· · · ⊗V over
k. The identity map V →V will be denoted by IdV , or simply by Id when the space
V is clear from the context. If V is ﬁnite–dimensional with basis e = (e1, . . . , ed) and if
f : V ⊗n →V ⊗n is a k–linear map, we denote by f j1···jn
i1···in the matrix element of f with
respect to the basis e⊗n:
f (ei1 ⊗· · · ⊗ein) =
X
1≤j1,...,jn≤d
f j1···jn
i1···in · ej1 ⊗· · · ⊗ejn.
