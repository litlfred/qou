---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-004-2-the-zeta-function-of-a-graph-and-the-quantum-m
section_title: "The zeta function of a graph and the quantum MacMahon Master Theorem"
section_number: 2
pages: 4-5
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
One of main ingredients in our result is combinatorics of non-negative integer ﬂows on digraphs. They
appear in an expression of the zeta function.
Let us recall what is the zeta function of a digraph. We will consider d igraphs (that is, graphs with
oriented edges) with weights on their edges.
Let G = ( V, E) be a digraph with vertex set V and directed edges E⊂ V × V , and let B = ( βe)e∈E
be a weight matrix for the edges of G. For edge e we denote by s(e), t(e) the starting and terminal vertex
of e. Bass-Ihara-Selberg deﬁned a zeta function of a graph in analogy with number theory and dynamical
systems, where the analogue of a prime number is a nonperiodic cycle . Let us deﬁne the latter.
A pointed walk on a digraph is a sequence ( e1, . . . , ek) of edges such that the end of one coincides with
the beginning of the next; we say that it is pointed at the beginning of e1, which is also called a base point.
A pointed closed walk is a path whose beginning and end vertex coincide. Two pointed closed walks are
equivalent if they diﬀer on the choice of base point only. By a cycle we will mean an equivalence class
of pointed closed walks. A cycle c is periodic if c = dn for some closed walk d and some integer n > 1.
Otherwise, it is called nonperiodic. Let P(G) denote the set of nonperiodic cycles of a digraph G. Using the
weight function, we may deﬁne the weight β(c) of a cycle c by β(c) =∏
e∈c β(e).
With the above preliminaries, Bass-Ihara-Selberg [B] deﬁne
Deﬁnition 2.1. The zeta function ζ(G, B) of a weighted digraph ( G, B) is deﬁned by:
ζ(G, B) =
∏
c∈P(G)
1
1− β(c) .
It follows by deﬁnition that
ζ(G, B) =
∑
c multisubsets of P(G)
β(c)
The actual deﬁnition of Bass-Ihara-Selberg uses more special we ights for the edges (each edge is given the
same weight), and is used to digraphs which are doubles (in the sense of replacing an unoriented edge by a
pair of oppositely oriented edges) of undirected graphs.
Foata-Zeilberger proved that the zeta function is a rational func tion, and in fact given by the inverse of
a determinant. Moreover, the zeta function is given by a sum over ﬂ ows.
Deﬁnition 2.2. A ﬂow f on a digraph G is a function f : Edges(G)−→ N of the edges of G that satisﬁes
the (Kirkhoﬀ) conservation law ∑
e begins at v
f (e) =
∑
e ends at v
f (e)
at all vertices v of G. Let f (v) denote this quantity and let F (G) denote the set of ﬂows of a digraph G.
4
If β is a weight function on the set of edges of G and f is a ﬂow on G, then
• the weight β(f ) of f is given by β(f ) =∏
e β(e)f (e), where β(e) is the weight of the edge e.
• The multiplicity at a vertex v with outgoing edges e1, e2, . . . is given by mult v(f ) =
(f (e1)+f (e2)+...
f (e1),f (e2),...
)
,
and the multiplicity of f is given by mult( f ) =∏
v multv(f ).
• If A is a subset of edges then we let f (A) =∑
e∈A f (e).
Let us summarize Foata-Zeilberger’s theorem [FZ, Theorem 1.1] her e. For the sake of completeness we
include its proof in Appendix A.
Theorem 3. If (G, B) is a weighted digraph, then
ζ(G, B) = 1
det(I− B)(1)
=
∑
f ∈F (G)
β(f ) mult(f ).(2)
Remark 2.3. For r = 1, the above Theorem states that
1
1− x =
∞∑
n=0
xn
where x = b11. Thus, Theorem 3 is a version of the geometric series summation.
Another formula for the inverse of a determinant, the MacMahon M aster Theorem, has been mentioned
in the introduction. We will need its quantum version, proved in [GLZ].
In r-dimensional quantum algebra we have r indeterminates xi (1≤ i≤ r), satisfying the commutation
relations xj xi = qxixj for all 1 ≤ i < j ≤ r. Further we are given a right-quantum matrix A. We assume
that the indeterminates of A commute with the xi’s. The following theorem has been proven recently in
[GLZ].
Theorem 4. Let A be a right-quantum matrix of size r. For 1≤ i≤ r let Xi = ∑ r
j=1 aijxj, and for
any vector (m1, . . . , mr) of non-negative integers let GA(m1, . . . , mr) be the coeﬃcient of xm1
1 xm2
2 . . . xmr
r in∏ r
i=1 X mi
i . Then
∞∑
m1,...,mr=0
GA(m1, . . . , mr) = 1 /Ferm(A).
