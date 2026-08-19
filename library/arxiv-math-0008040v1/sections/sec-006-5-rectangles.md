---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh"
section_id: sec-006-5-rectangles
section_title: "Rectangles"
section_number: 5
pages: 9-10
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh — Let U be the quantum group associated to a Lie algebra g of type An."
---
We therefore have:
Theorem 4.4 Let i ∈ χ n. For j = 1, 2,... ,n and P a partial quiver associated to i, let bj(i) =
ψ −1
i (vj(i)) and bP (i) = ψ −1
i (vP (i)) be the corresponding canonical basis elements. Then these
elements are independent of the reduced expression i. Thus the canonical basis elements arising in
this way for at least one reduced expression i can be labelled bj, j = 1, 2,... ,n , bP , P a partial
quiver of type An.
5 Rectangles
The above provides us with a description of the spanning vect ors of a Lusztig cone as multisets
of positive roots. We would also like a description of the mon omial of Kashiwara operators corre-
sponding to such a vector. We will use this in the next section to calculate Lusztig parametrizations
cj(j),cP (j) of the canonical basis elements arising in Theorem 4.4. We s hall show that these mono-
mials can be described by a remarkable ‘rectangle combinato rics’ (invented by R. W. Carter) which
we shall now describe.
Deﬁnition 5.1 LetP be a partial quiver, and Y a component of P . Let a =a(Y ) and let b =b(Y )
(see Theorem 3.1). We deﬁne the rectangleρ(Y ) of Y , as follows. If Y is of type L, then ρ(Y ) is as
in the left hand diagram in Figure 3; if Y is of type R then ρ(Y ) is as in the right hand diagram
in Figure 3. We also deﬁne, for j = 1, 2,... ,n , ρ(j) to be the type L rectangle with a = j and
b =j + 1 (for these values of a and b, both diagrams in Figure 3 coincide).
In each case, the rectangle is ﬁlled in with numbers in diagon al rows, with the numbers along a
diagonal row from top right to bottom left increasing by 1 at e ach step and similarly from top left to
bottom right. We deﬁne the diagram D(P ) of P in the following way. Go through the components
Y of P one by one, from left to right. Fit the corresponding rectang les ρ(Y ) together, so that if
a component of type L is followed by one of type R, the rectangles share leftmost corners, and if
one of type R is followed by one of type L, they share rightmost corners. In each case, it is easy
to see that the overlapping numbers agree. We associate a mul tiplicity m(s) to each position in
9
ρ(L − −−) =
4
3
2
1
................................................................................................................................................................. ......................................... ................................................................................................................................................................. .........................................
L1
ρ(−R − −) =
4
3
2
5
4
3
......................................................................................................................... ................................................................................. ......................................................................................................................... .................................................................................R1
ρ(− −L−) = 2
1
3
2
4
3
................................................................................. ......................................................................................................................... ................................................................................. .........................................................................................................................
L2
Figure 4: Examples of the rectangles ρ(Y ).
D(LRL−) =
4
3
2
1
................................................................................................................................................................. ......................................... ................................................................................................................................................................. .........................................
5
4
3
......................................................................................................................... ................................................................................. ......................................................................................................................... .................................................................................
2
1
................................................................................. ......................................................................................................................... ................................................................................. .........................................................................................................................
L1
R1
L2
Figure 5: The diagram D(LRL−).
D(P ) where a number s is placed; if t is the number of rectangles ρ(Y ) that s lies in, then m(s)
is deﬁned to be ⌈t/ 2⌉. We label each rectangle with the corresponding component Y of P ; on the
left hand corner if Y is of type R, and on the right hand corner if Y is of type L. We deﬁne, for
j = 1, 2,... ,n , D(j) to be the diagram ρ(j), with each position given multiplicity 1.
Example
We consider the case when n = 5 and P =LRL−. Then P has three components, L1 =L − −−,
R1 = −R − − and L2 = − −L−. The diagrams ρ(Y ) are as in Figure 4.
We put them together, so that the 4 in ρ(L − −−) matches the leftmost 4 in ρ(−R − −) and so that
the rightmost 3 in ρ(−R − −) matches the rightmost 3 in ρ(− −L−), to get the complete diagram
D(LRL−); see Figure 5. The numbers 2 and 3 in the middle of the diagram each have multiplicity
2.
Deﬁnition 5.2 Suppose P is a partial quiver or P =j for some j ∈ [1,n ]. We deﬁne a diagonal
row of D(P ) to be a diagonal row of numbers in D(P ) running from top left to bottom right.
Such a diagram D(P ) deﬁnes a sequence µ (P ) which is obtained by reading oﬀ the digits in the
diagonal rows in the diagram, starting with the bottom left r ow. Each digit is repeated according
to its multiplicity. In our example, µ (LRL−) = (4, 5, 2, 3, 3, 4, 1, 2, 2, 3, 1). There is a corresponding
monomialF (P ) in U −, obtained by replacing each digit, s, occurring with multiplicity m(s), by the
divided power F (m(s))
s . In our example, F (LRL−) = F4F5F2F (2)
