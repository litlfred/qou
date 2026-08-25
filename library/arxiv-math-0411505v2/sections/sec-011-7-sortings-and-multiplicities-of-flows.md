---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-011-7-sortings-and-multiplicities-of-flows
section_title: "Sortings and multiplicities of flows"
section_number: 7
pages: 12-13
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
7.1. Sortings. In this section we introduce one of our key tools, which is a categoriﬁ cation of multiplicities
of the ﬂows on GK . Let f be a ﬂow on GK. If e is an edge of GK then we let F (e)⊂ F be the set of f (e)
copies of e; we choose an arbitrary total order on each F (e).
Let F =∪e∈EK F (e) and let Fr⊂ F consists of the union of F (e), e red. Further let F +
r denote the subset
of Fr consisting of the red edges which leave a vertex with + sign, and we let f +
r =|F +
r|. Analogously we
deﬁne F −
r , . . ..
Deﬁnition 7.1. Fix a ﬂow f on GK . A sorting C of f is a function
C : Vertices(GK )→ 2Fr
such that
• C1 is a collection of red edges that terminate in vertex 1, of cardinality f (eb
1).
• For each 2≤ i≤ r, Ci⊆ Ci−1∪{ e∈ Fr; e terminates in vertex i} of f (eb
i ) elements.
LetC(f ) denote the set of all sortings of f .
Lemma 7.2. Every ﬂow f has mult(f ) sortings.
Proof. Use that mult( f, r) = 1, {e∈ Fr; e terminates in vertex 1} ={e∈ F ; e terminates in vertex 1} and
for each 2 ≤ i < r ,∑ f (e) : e terminates at vertex i equals|Ci−1∪{ e∈ Fr; e terminates in vertex i}|. □
Deﬁnition 7.3. We deﬁneI(f, n) ={0, . . . , n− 1}Fr . If v∈I (f, n) then we deﬁne f −
r (v) =∑
e∈F −
r
ve and
we deﬁne f +
r (v) analogously.
Deﬁnition 7.4. (a) Fix a ﬂow f on GK and a natural number n. An n-sorting of f is a pair P = ( C, v)
where C∈C (f ) and v∈I (f, n).
(b) If P = (C, v) is an n-sorting of f then we deﬁne its weight b(P ) to be
b(P ) = tn(f −
w −f +
w )(1− t)f −
r tf −
r (v)(1− t−1)f +
r t−(f +
r )(n−1)+f +
r (v).
(c) LetCn(f ) denote the set of all n-sortings of f .
The following lemma states that the n-sortings of f categorify multiplicities and weights of ﬂows.
Lemma 7.5. For every ﬂow f on GK and every n we have
β(f )|t→tn mult(f ) =
∑
P ∈Cn(f )
b(P ).
Proof. It follows by Lemma 7.2 that
∑
P ∈C(f,n)
b(P ) = mult( f )tn(f −
b −f +
b )(1− t)f −
r (1− t−1)f +
r

 ∑
v∈I(f,n)
tf −
r (v)t−(f +
r )(n−1)+f +
r (v)

 =
by a simple rearrangement
mult(f )tn(f −
b −f +
b )

(1− t)f −
r
∑
v∈I(f,n)
tf −
r (v)



(1− t−1)f +
r
∑
v∈I(f,n)
t−(f +
r )(n−1)+f +
r (v)

 =
by a geometric series summation
β(f )|t→tn mult(f ).
□
12
