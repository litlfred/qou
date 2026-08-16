---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-012-72-sortings-and-the-jones-polynomial
section_title: "Sortings and the Jones polynomial"
section_number: 7.2
pages: 13-14
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
colored Jones function in terms of them.
Deﬁnition 7.6. Fix a ﬂow f of GK and a natural number n. Let P = (C, v) be an n-sorting of f . We say
that P is admissible if
• For every two edges e, e′∈ Fr such that ve = ve′ and e ends in vertex i and e′ ends in vertex j and
j≥ i, there exists an l, i≤ l < j such that e⁄∈Cl.
We denote by ACn(f ) the set of all admissible n-sortings of f , and by Sn(GK, f) the set of all lifts of f to
admissible subgraphs of G(n)
K .
The next lemma explains the notion of admissible sortings.
Lemma 7.7. There is a bijection Φ fromACn(f ) toSn(GK, f) such that β(Φ( P )) = b(P ). Moreover, if
P∈AC n(f ) and π is the projection to GK then for each e∈ EK, the ﬁxed total order on F (e) agrees with
the total order (π−1(e),≺) introduced in Deﬁnition 6.5.
Proof. Let P = (C, v), C = (C1, . . . , Cr), and P∈AC n(f ). In order to deﬁne Φ( P ) we will deﬁne the image
Φ( P, e) for each e∈ F .
First we determine the ends of the lifts of the red edges as follows: if e∈ Fr then we let t(Φ( P, e)) = at(e)
v(e)+1.
Next we determine the blue edges of Φ( P ) as follows: if 1 ≤ i≤ r then we let
{s(Φ( P, e))| e∈ F (eb
i )} ={ai
ve+1| e∈ Ci}.
This determines the beginnings of the blue edges, and hence also the ends of the blue edges.
It remains to specify the beginnings of the lifts of the red edges. Sin ce P is admissible, observe that for
each 1≤ i≤ r, there are exactly f (er
i ) vertices ai
j of indegree 1 in current Φ( P ). Hence it remains to make
each of them starting vertex of exactly one edge Φ( P, e), e∈ F (ei
r). This is uniquely determined by the
’moreover’ part of the Lemma. This ﬁnishes the deﬁnition of Φ. The e quality for the weights follows easily,
and the moreover part of the Lemma directly from the deﬁnition of Φ . To ﬁnish the proof we ﬁnd the inverse
to Φ.
Let c∈S n(GK , f). We construct Φ −1(c) = ( C(c), v(c)) as follows: Let e be an edge of GK. There is an
order preserving bijection between the ﬁxed total ordering ( F (e), <) and ( π−1(e),≺). If e′ is an edge of c
then we let e′
F be the corresponding edge of F .
First let e′ be a red edge of c. We let v(c)e′
F
= j where t(e′) = ai
j+1. Hence v(c) encodes the ends of the
red edges of c.
Next we deﬁne a predecessor p(e) for each edge e of c. If e red then p(e) = e. If e blue then p(e) is the
red edge of c which terminates in the starting vertex of the longest blue path of c whose last edge is e. Note
that p(e) always exists and is unique since c is admissible.
Finally for 1 ≤ i≤ r let Ci ={p(e)F ; e edge of c that terminates in some ai
j that is a starting vertex of a
blue edge of c}. This ﬁnishes the construction of Φ −1. □
Theorem 8. We have:
Jn(K)(t) = tδ(K,n) ∑
f ∈F (GK)
tδ(f ) ∑
P ∈ACn(f )
texc(P )b(P ),
where exc(P ) = exc(Φ( P ))− exc(f ).
Proof. We have:
Jn(K)(t) = tδ(K,n) ∑
c∈Sn(GK )
tδ(c)β(c)
= tδ(K,n) ∑
f ∈F (GK)
tδ(f ) ∑
c∈Sn(GK ,f )
texc(c)−exc(f )β(c)
= tδ(K,n) ∑
f ∈F (GK)
tδ(f ) ∑
P ∈ACn(f )
texc(P )b(P )
□
13
