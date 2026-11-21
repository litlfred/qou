---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-016-5-colored-jones-polynomials
section_title: "Colored Jones polynomials"
section_number: 5
pages: 18-20
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
of T .
Remark 4.6. There is an obvious one-to-one correspondence between bottom knots
and string knots (i.e., a string link consisting of just one arc component running from
the above to the bottom). A bottom knot and the corresponding string knot have
the same value of the universal invariant. Therefore, we have the result announced
in [17, Theorem 2.1], [19, Theorem 1.2], which is the string knot version of Theorem
4.5.
5. Colored Jones polynomials
In this section, we recall the deﬁnition of the colored Jones polynomials of framed
links.
5.1. Finite-dimensional representations of Uh. By a ﬁnite-dimensional repre-
sentation of Uh, we mean a left Uh-module which is free of ﬁnite rank as a Q[[h]]-
module.
It is well known that, for each n ≥0, there is exactly one irreducible ﬁnite-
dimensional representation Vn of rank n+1 up to isomorphism, which corresponds
to the (n + 1)-dimensional irreducible representation of sl2.
The structure of Vn is as follows. Let vn
0 ∈Vn denote a highest weight vector of
Vn, which is characterized by Evn
0 = 0, Hvn
0 = nvn
0 and Uhvn
0 = Vn. It is useful
to deﬁne the other basis elements by
vn
i = ˜F (i)vn
0
for i = 1, . . . , n.
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT
19
Then the action of Uq on Vn is given by
K±1vn
i = vn−2ivn
i ,
(5.1)
emvn
i = {n −i + m}q,mvn
i−m,
(5.2)
˜F (m)vn
i = q−mi
i + m
m

q
vn
i+m,
(5.3)
for i = 0, . . . , n and m ≥0, where we understand vn
i = 0 unless 0 ≤i ≤n.
5.2. Colored Jones polynomials. Let L = L1 ∪· · · ∪Lm be an m-component,
framed, oriented, ordered link, and let W1, . . . , Wm ≥0 be ﬁnite-dimensional
representations of Uh.
We consider each Wi as a color attached to the compo-
nent Li. Then the colored Jones polynomial JL(W1, . . . , Wm) of the colored link
(L; W1, . . . , Wm) is deﬁned as follows.
We choose a diagram of L which is obtained by pasting copies of the fundamental
tangles, as in the deﬁnition of the universal sl2 invariant in Section 4.2. To each
copy of a fundamental tangle in L, we associate a left Uh-module homomorphism.
To a vertical line contained in Li, we associate to the left Uh-module Wi if the line
is oriented downward, and the dual W ∗
i of Wi if the line is oriented upward. To a
positive crossing, we associate a braiding operator
ψW,W ′ : W ⊗W ′ →W ′ ⊗W,
x ⊗y 7→
X
βy ⊗αx,
where W (resp. W ′) are the left Uh-modules associated to the string which connects
the upper left corner and the lower right corner (resp. the upper right corner and
the lower left corner). To a negative crossing, we associate
ψ−1
W ′,W : W ⊗W ′ →W ′ ⊗W,
x ⊗y 7→
X
¯αy ⊗¯βx,
where W and W ′ are as above. To the last four tangles in Figure 4.3, we associate
the following operators
evW : W ∗⊗W →Q[[h]],
f ⊗x 7→f(x),
ev′
W : W ⊗W ∗→Q[[h]],
x ⊗f 7→f(κx),
coevW : Q[[h]] →W ⊗W ∗,
1 7→
X
i
xi ⊗xi,
coev′
W : Q[[h]] →W ∗⊗W,
1 7→
X
i
xi ⊗κ−1xi,
respectively, where W = Wi if Li is the component of L containing the fundamental
tangle, and where the xi are a basis of W and the xi ∈W ∗are the dual basis.
By tensoring and composing the operators, we obtain a left Uh-module homo-
morphism from Q[[h]] to Q[[h]], and we deﬁne JL(W1, . . . , Wm) to be the trace of
this homomorphism.
Note that “JL” alone denotes the universal sl2 invariant of L. The above deﬁni-
tion of JL(W1, . . . , Wn) is an abuse of notation, but it should not cause confusion.
It is well known that JL ∈qp/4Z[q, q−1] ⊂Z[q±1/4], where p ∈Z/4Z depends
only on the linking matrix of L and on n1, . . . , nm. The invariant is normalized
so that J∅() = 1, and JU(Vn) = [n + 1] for n ≥0, where U denotes the 0-framed
unknot.
