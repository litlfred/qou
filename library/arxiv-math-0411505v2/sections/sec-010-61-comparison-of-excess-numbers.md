---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-010-61-comparison-of-excess-numbers
section_title: "Comparison of excess numbers"
section_number: 6.1
pages: 11-12
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
K , let f be the corresponding
ﬂow in GK, to which c projects, under the projection
π : G(n)
K → GK .
In this section, we compare exc( f ) (in Deﬁnition 4.1) with exc( c).
As we will see, the two excess numbers do not agree. In this section we will determine their diﬀerence.
We begin by introducing a partial ordering ≺ on the set of edges of G(n)
K . We warn the reader that this
ordering is diﬀerent from the ordering <v of the edges of GK entering vertex v, introduced in Deﬁnition 4.1.
Deﬁnition 6.5. Consider two edges e and e′ of G(n)
K which start at the vertices ai
j and ai′
j′ of G(n)
K . We say
that e≺ e′ if
• e, e′ end at the same vertex v and π(e) <v π(e′) in GK, or
• i = i′ and sign( i) = + and j < j ′, or
• i = i′ and sign( i) =− and j′ < j
Recall that c∈S n(GK ) ( c admissible) if and only if c is a collection of vertex disjoint directed cycles of
G(n)
K . Hence the ordering on the edges of c deﬁned in Deﬁnition 6.5 induces a total ordering on each π−1(e),
e edge of GK.
This total ordering may be seen from the cabling of the knot in the sa me way as the ordering <v of
Deﬁnition 4.1 may be seen from the knot: if we travel along an arc ai
j, we see one by one the arcs corresponding
to the starting vertices of edges of π−1(e), where e is an edge of GK . This agrees with the total ordering on
π−1(e) induced by ≺; see Figure before 6.2.
Deﬁnition 6.6. Consider two edges e and e′ of G(n)
K which end at the vertices ai
j and ai′
j′ of G(n)
K .
X(e, e′) =

































1 if e, e′ = red , e ′≺ e, sign(s(e)) = + , j < j ′
1 if e = red, e ′ = blue,
π(e), π(e′) do not start at the same vertex ,
e′≺ e, sign(s(e)) = + , j < j ′
1 if e, e′ = red , e ′≺ e, sign(s(e)) =−, j ′ < j
1 if e = red, e ′ = blue,
π(e), π(e′) do not start at the same vertex ,
e′≺ e, sign(s(e)) =−, j ′ < j
0 otherwise
Y (e, e′) =





1 if e = red, e ′ = blue,
π(e), π(e′) start at the same vertex , e ≺ e′
0 otherwise
Lemma 6.7. Let c be an admissible subgraph of G(n)
K . Denote by f the ﬂow on GK which is the projection
of c to GK. Then
exc(c) = exc( f ) +
∑
e
sign(s(e))
(∑
e′
X(e, e′) + Y (e, e′)
)
where the summations of e and e′ are over the set of edges of c and s(e) denotes the starting vertex of e.
Proof. Consider a crossing v of K, and the corresponding n2 crossings of K n. We count the contribution to
exc(c) of pairs ( e, e′) of edges of c such that
• e projects to eb
v (the blue edge that starts at v), and e′ does not project to er
v (the red edge that
starts at v). This gives exc( f ).
• e projects to er
v, and e′ does not project to eb
v. This gives the X-term in the formula.
• e projects to er
v, and e′ projects to eb
v. This gives the Y -term in the formula.
□
11
