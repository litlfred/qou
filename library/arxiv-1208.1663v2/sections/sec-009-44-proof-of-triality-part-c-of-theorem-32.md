---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers"
section_id: sec-009-44-proof-of-triality-part-c-of-theorem-32
section_title: "Proof of triality: part (c) of Theorem 3.2"
section_number: 4.4
pages: 12-13
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES STAVROS GAROUFALIDIS With an appendix by Sander Zwegers — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of"
---
Theorem 3.2. Equation (3.2) concerns the following Z/3-action on V .
Deﬁnition 4.2. Consider the action f↦→Sf on a function f : Z2−→ Z((q1/2)) given by:
(4.3) Sf (m,e ) = (−q
1
2 )−ef(e,−e−m).
Proposition 4.3. (a) We have: S3 =Id.
(b) If f∈V , then Sf =f, and of course, also S2f =f.
Part (c) of Theorem 3.2 follows from part (b) of the above proposition.
Proof. (of Proposition 4.3) Part (a) is elementary. For part (b), assume that f satisﬁes
Equation (3.1a) for all ( m,e ). Replace ( m,e ) by (e,−1−e−m) in (3.1a) and we obtain
that
(4.4) −f(e,−1−e−m) +q−e
2f(e,−e−m) +q− 1
2−e
2−m
2f(1 +e,−1−e−m) = 0.
Now, replace f bySf in the left hand side of Equation (3.1a), and compute that the result
is given by
(−1)e+1
(
−f(e,−1−e−m) +q−e
2f(e,−e−m) +q− 1
2−e
2−m
2f(1 +e,−1−e−m)
)
The above vanishes from Equation (4.4).
Likewise, assume that f satisﬁes Equation (3.1b) for all (m,e ). Replace (m,e ) by (e, 1−
e−m) in (3.1b) and we obtain that
(4.5) q
1
2−e
2−m
2f(−1 +e, 1−e−m) +q−e
2f(e,−e−m)−f(e, 1−e−m) = 0
Now, replace f bySf in the left hand side of Equation (3.1b), and compute that the result
is given by
(−1)e+1
(
q
1
2−e
2−m
2f(−1 +e, 1−e−m) +q−e
2f(e,−e−m)−f(e, 1−e−m)
)
It follows that if f ∈ V , then the above vanishes from Equation (4.5). In other words, if
f∈V then Sf∈V . To conclude that f =Sf , it suﬃces to show (by part (a) of Theorem
3.2) that f(0, 0) = (Sf )(0, 0). If f(0, 0) =A, f(0, 1) =B, using Remark 3.4 we have:
(Sf )(0, 0) =f(0, 0) =A (Sf )(0, 1) =f(0, 1) +q− 1
2f(1,−1) =B +q− 1
2 (−Bq
1
2 ) = 0.
This concludes the proof of Proposition 4.3. □
THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES 13
4.5. I∆ is a tetrahedron index. Observe that by its deﬁnition,
I∆(m,e ) =
∑
e∈Z
S(m,e,n )
is given by a one-dimensional sum of a properq-hypergeometric term ([27, 21])
S(m,e,n ) = (−1)nq
1
2n(n+1)−(n+ 1
2e)m
(q)n(q)n+e
.
It follows by [27] thatI∆(m,e ) isq-holonomic in both variablesm ande. Moreover, recursion
relations for I∆(m,e ) can be found by the creative telescoping method of [27]. For instance,
S satisﬁes the recursion
(4.6) q
e
2S(m− 1,e,n ) +q−m
2S(m,e− 1,n )−S(m,e,n ) = 0
which implies thatI∆ satisﬁes Equation (3.1b). To prove Equation (4.6), divide byS(m,e,n )
and use the fact that
q
e
2
S(m− 1,e,n )
S(m,e,n ) =qe+n q−m
2
S(m,e− 1,n )
S(m,e,n ) = 1−qe+n.
The proof of Equation (3.1a) is similar. For an alternative proof, using the quantum dilog-
arithm, see Section B.
