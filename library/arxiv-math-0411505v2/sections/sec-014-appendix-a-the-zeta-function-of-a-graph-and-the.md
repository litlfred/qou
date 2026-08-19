---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-014-appendix-a-the-zeta-function-of-a-graph-and-the
section_title: "Appendix A. The zeta function of a graph and the Foata-Zeilberger formula"
section_number: null
pages: 15-16
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
A.1. The F oata-Zeilberger formula. In this section we translate key combinatorial results of Foata and
Zeilberger [FZ, Theorem 1.1] in the language of our paper, resulting in Theorem 3.
Consider the complete graph Kr with r vertices equipped with a weight martix B = ( bij) of size r with
independent commuting variables, and letR = Z[[bij]]. Let X ={x1, . . . , xr} denote an alphabet on r letters
and X ⋆ denote the set of words on X.
Recall the notion of a Lyndon word l∈ X, that is a word which is not a nontrivial power of another word,
and is strictly smaller than any of its cyclic rearrangements. It follow s by deﬁnition that
Lemma A.1. There is a 1-1 correspondence between the set of nonperiodic cycles in Kr and the set of
Lyndon words in X.
Given a nonempty word w = x1x2 . . . xm∈ X, Foata and Zeiberger deﬁne a function βcirc by
βcirc(w) = bx1,x2bx2,x3 . . . bxm−1,xmbxm,x1
and βcirc(w) = 1 if w is the empty word. Every word w∈ X has a unique factorization as
w = l1l2 . . . ln
where li are Lyndon words in nonincreasing order l1≥ l2≥···≥ ln. Using this, Foata and Zeilberger deﬁne
a map:
βdec : X ⋆−→R
by βdec(w) = βcirc(l1)βcirc(l2) . . . βcirc(ln) where ( l1, . . . , ln) is the unique factorization of w. For example, if
X ={1, 2, 3, 4, 5} and w = 34512421231242, then its factorization is given by ( l1, l2, l3) = (345 , 1242, 1231242)
and βdec(w) = b3
1,2b2
2,1b2,3b2
2,4b3,1b3,4b2
4,2b4,5b5,3.
Foata and Zeilberger deﬁne another map
βvert : X ⋆−→R
as follows: if w = x1x2 . . . xm is a word and ~w = ~x1~x2 . . .~xm is the rearrangement of the letters of w in
nondecreasing order, then they deﬁne
βvert(w) = b~x1,x1b~x2,x2 . . . b~xm,xm.
15
In [FZ, Theorem 1.1] they show that
1
det(I− B) =
∑
w∈X ⋆
βdec(w)(4)
=
∏
c∈P(Kr)
1
1− β(c)(5)
=
∑
w∈X ⋆
βvert(w)∈R(6)
Let us now translate (6). Write a word w and its rearrangement ~w as an array
Γ( w) =
[
~w
w
]
A rearrangement ~w of a word w is always of the form ~w = 1 n12n2 . . . rnr , and gives rise to a function
fw : Edges( Kr)−→ N on the edges of Kr deﬁned by fw((i, j)) is the number that the column vector
[ i
j
]
appears in Γ( w). Since ~w is a rearrangement of w, it follows that fw is a ﬂow. It follows from 4 that this
map X ⋆−→F (Kr) is onto, and it is easy to see that given an ﬂow γ on Kr, the preimage under this map
consists of mult( γ) words with the same βvert weight, equal to the weight of γ. This together with Equation
(6) implies that
(7) 1
det(I− B) =
∑
f ∈F (Kr)
β(f ) mult(f ).
This, together with a specialization of the variables imply Theorem 3.
