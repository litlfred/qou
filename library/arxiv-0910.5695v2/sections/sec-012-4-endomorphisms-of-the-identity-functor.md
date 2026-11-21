---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-012-4-endomorphisms-of-the-identity-functor
section_title: "Endomorphisms of the identity functor"
section_number: 4
pages: 23-23
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
Deﬁnition 4.1. Let Ωr,d ∈FSd denote the sum of all r-cycles in Sd.
Since Ωr,d is in the center of FSd, the action of Ωr,d on V ⊗n
d
gives an element
of EndSd(V ⊗n
n(d) denote the unique element of FPn(d) with f(Cr
The ﬁrst goal of this section is to deﬁne elements of FPn(t) for arbitrary t ∈F
which agree with the deﬁnition of Cr
n(t) when t is a suﬃciently large integer. We are
able to do this because, as we will show, Cr
The following proposition records the properties of the (λ, d) grid marking which
will be useful for determining the roots of Pλ.
(1) If
appears in the ith row, then k = |λ| + λi −i.
(2) If
appears in the ith column, then d −k is the hook length of the row 0,
column i box in λ(d).
Proof. (1) If
appears in the ith row, then
must be in column µi + 1. Hence
k is the number of up/right moves it takes to get from the lower left corner to the
upper right corner in a (|λ| −i) × (λi + 1) grid. The result follows.
(2) Let ci denote the number of boxes in the ith column of λ. Notice there are
ci boxes below, and d−|λ|−i boxes to the right of the row 0, column i box in λ(d).
Hence the hook length of that box is d −|λ| −i + ci + 1. On the other hand, if
appears in the ith column, then
must be in row ci. Hence k is the number of
up/right moves it takes to get from the lower left corner to the upper right corner
in a (|λ| −ci) × i grid. Thus k = |λ| −ci + i −1.
□
Using Proposition 3.31, we can determine all the roots of the polynomial Pλ.
Proposition 3.32. Pλ is a degree |λ| polynomial with |λ| distinct, integer roots
given by |λ| + λi −i for each i = 1, . . . , |λ|.
Proof. Suppose d is an integer with d > 2|λ|. It follows from Deﬁnition 3.26 that
the roots of Pλ are exactly the integers 0 ≤k < d such that d −k is not a hook
length of a box in the top row of λ(d). By Proposition 3.31(2), those are exactly
the values of k for which
appears in the (λ, d) grid marking. The result now
follows from Proposition 3.31(1).
□
In this section we study endomorphisms of the identity functor on Rep0(St; F)
constructed using certain central elements in group algebras of symmetric groups.
These endomorphisms of the identity functor will play a key role in describing the
blocks in Rep(St; F). This role is analogous to the role the Casimir element plays
in Lie theory.
