---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-006-4-the-enhanced-arc-graph-and-the-jones-polynomia
section_title: "The enhanced arc-graph and the Jones polynomial"
section_number: 4
pages: 7-8
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
In order to express the Jones polynomial as a function of the arc g raph, we need to enhance the arc-graph
as follows.
Deﬁnition 4.1. (a) We introduce a linear order <v on the set of edges of GK terminating at vertex v as
follows. Recall that v corresponds to an arc av of K. If we travel on av along the orientation of K, we ’see’
one by one the arcs corresponding to starting vertices of red arc s entering v: this gives the linear order of
red arcs entering v. Finally there is at most one blue edge entering vertex v, and we make it less than all
the red edges entering v.
(b) If f is a ﬂow on GK, we deﬁne the rotation and excess number of f by:
(3) rot( f ) =
∑
e∈EK
f (e)rot(e), exc(f ) =
∑
v∈VK
sign(v)f (eb
v)
∑
e<v er
v
f (e), δ (f ) = exc( f )− rot(f ),
where VK and EK are the set of vertices and edges of GK, and rot( e) is deﬁned in Deﬁnition B.6.
LetS(G) denote the set of all subgraphs C of G such that each component of C is a directed cycle. Note
thatS(G) may be identiﬁed with a ﬁnite subset of F (G) since the characteristic function of C is a ﬂow.
The next theorem, due to Lin-Wang, expresses the Jones polynom ial of a knot projection K in terms of
the enhanced arc-graph of K. For the sake of completeness we include its proof in Appendix B.
Theorem 5. [L W]For every knot projection K we have:
J(K, t) = tδ(K) ∑
c∈S(GK )
tδ(c)β(c).
We now give a similar formula for the colored Jones function Jn of a knot. We will normalize the colored
Jones function so that it is the constant sequence {1} for the unknot, and Jn is the quantum group invariant
of knots that corresponds to the ( n + 1)-dimensional irreducible representation of sl2.
Recall the operation of cablingK(n) the knot projection K n times. Recall that a1, . . . , ar+1 are the arcs
ofK. Each al is in the cabling replaced by n2 arcs al
i,j, i, j = 1 , . . . , n, with the agreement that the ’long
arcs’ obtained by cabling arc ak will be ak
1j, j = 1, . . . , n and the ’small arcs’ obtained by cabling of crossing
k will be denoted by ak
ij for i = 2, . . . , n and j = 1, . . . , n. Note that all crossings which replace the original
crossing k have the same sign, equal to the sign of the crossing k. (see ﬁgure before Lemma 6.2).
We further let K (n) denote the link obtained from K(n) by deletion of the n special long arcs ar+1
1j ,
j = 1, . . . , n.
Theorem 6. For every knot K and every n∈ N, we have
Jn(K, t) = tδ(K,n) ∑
c∈S(GK(n) )
tδ(c)β(c)
where GK (n) is the arc graph of K (n).
Proof. Let Vn denote the ( n + 1)-dimensional irreducible representation of the quantum group Uq(sl2), and
let vn denote a highest weight vector of Vn. Then, there is an inclusion Vn−→⊗ nV1 that maps vn to a
nonzero multiple of ⊗nv1.
The result follows since cabling K corresponds to tensor product of representations and since ω(K(n)) =
n2ω(K) and rot( K (n)) = n rot(K). □
For an integer m, we denote by
(m)q = qm− 1
q− 1
the quantum integer m. This deﬁnes the quantum factorial and the quantum binomial coeﬃcients by
(m)q! = (1) q(2)q . . .(m)q
(m
n
)
q
= (m)q!
(n)q!(m− n)q!
7
for natural numbers m, n with n≤ m. We also deﬁne
multq(f ) =
∏
v
( f (v)
f (eb
v)
)
qsign(v)
.
Theorem 7. For every knot projection K we have:
Jn(K, t) = tδ(K,n) ∑
f ∈F (GK)
multt(f )tδ(f ) ∏
v∈VK
t−sign(v)nf (eb
v ) ∏
ered;t(e)=v
f (e)−1∏
j=0
(1− t−sign(s(e))(n−j−∑
e′<v e f (e))).
Remark 4.2. It simply follows that the contribution of a ﬂow f to the sum in Theorem 7 is non-zero only if
f (v)≤ n for each vertex v. Thus, in the above sum, only ﬁnitely many terms contribute. As a re sult, when
n = 1, Theorems 7 and 5 coincide.
