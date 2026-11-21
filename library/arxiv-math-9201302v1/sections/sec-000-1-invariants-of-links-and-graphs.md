---
doc_id: arxiv-math-9201302v1
doc_title: "The Quantum G 2 Link Invariant"
section_id: sec-000-1-invariants-of-links-and-graphs
section_title: "Invariants of links and graphs"
section_number: 1
pages: 1-4
source_pdf: 9201302v1.pdf
source_sha256: 67987dd432f58488
toc_source: inferred
doc_brief: "The Quantum G_2 Link Invariant — We derive an inductive, combinatorial deﬁnition of a polynomial-valued regular isotopy invariant of links and tangled graphs."
---
The simplest known deﬁnition of the Jones polynomial is the Kauﬀman bracket [8], which in this paper will
be denoted by ⟨·⟩A1 and will be called the A1 bracket. The A1 bracket is given by the following recursive
rules:
|
〉A1 = −(q 1/2+q -1/2)|
〉A1
|
〉A1 = −q 1/4|
〉A1 − q -1/4|
〉A1
The goal of this part of the paper is to derive deﬁnitions of the following three variants of the Jones
polynomial:
Theorem 1.1. There is an invariant for regular isotopy of projections of links and tangled trivalent graphs
called ⟨·⟩G2 which is given by the following recursive rules:
|
〉G2 = a|
〉G2
|
〉G2 = 0
|
〉G2 = b|
〉G2
|
〉G2 = c|
〉G2
|
〉G2 = d1(|
〉G2 + |
〉G2) + d2(|
〉G2 + |
〉G2)
|
〉G2 = e1(|
〉G2 + |
〉G2 + |
〉G2 + |
〉G2 + |
〉G2) +
e2(|
〉G2 + |
〉G2 + |
〉G2 + |
〉G2 + |
〉G2)
|
〉G2 = f1|
〉G2 + g1|
〉G2 + f2|
〉G2 + g2|
〉G2
∗Supported by a National Science Foundation graduate fellowship in mathematics and a Sloan Foundation graduate fellowship
in mathematics.
1
where the coeﬃcients are deﬁned as:
a
=
q5 + q4 + q + 1 + q−1 + q−4 + q−5
b
=
−q3 −q2 −q −q−1 −q−2 −q−3
c
=
q2 + 1 + q−2
d1
=
−q −q−1
d2
=
q + 1 + q−1
e1
=
1
e2
=
−1
f1
=
1
1 + q−1
g1
=
1
1 + q
f2
=
q
1 + q−1
g2
=
q−1
1 + q ,
q is an indeterminate, and ⟨∅⟩G2 = 1.
Theorem 1.2. There is an invariant for regular isotopy of projections of links and tangled trivalent graphs
called ⟨·⟩A2 which is given by the following recursive rules:
|
〉A2 = (q+1+q -1)|
〉A2
|
〉A2 = (q 1/2−q -1/2)|
〉A2
|
〉A2 = |
〉A2 + |
〉A2
|
〉A2 = −q 1/6|
〉A2 + q -1/3|
〉A2
|
〉A2 = −q -1/6|
〉A2 + q 1/3|
〉A2
where q is an indeterminate and ⟨∅⟩A2 = 1.
Theorem 1.3. There is an invariant for regular isotopy of projections of links and tangled trivalent graphs
called ⟨·⟩C2 which is given by the following recursive rules:
|
〉C2 = −(q 2+q+q -1+q -2)|
〉C2
|
〉C2 = (q 3+q+1+q -1+q -3)|
〉C2
|
〉C2 = 0
|
〉C2 = −(q+2+q -1)|
〉C2
|
〉C2 = 0
|
〉C2 − |
〉C2 = |
〉C2 − |
〉C2
|
〉C2 = q 1/2+q -1/2
q -1/2
|
〉C2 + q 1/2+q -1/2
q 1/2
|
〉C2
|
〉C2 = q 1/2+q -1/2
q 1/2
|
〉C2 + q 1/2+q -1/2
q -1/2
|
〉C2
|
〉C2 = −q 1/2|
〉C2 − q 1/2+q -1/2
q -1
|
〉C2 − q 1/2+q -1/2
1
|
〉C2
|
〉C2 = q|
〉C2 + q -1|
〉C2 + q+2+q -1
1
|
〉C2
where q is an indeterminate and ⟨∅⟩C2 = 1. Part of the invariant can also be deﬁned by the recursive rules:
|
〉C2 = −(q 2+q+q -1+q -2)|
〉C2
|
〉C2 = (q 2+q+q -1+q -2)| 〉C2
|
〉C2 = −(q+2+q -1)|
〉C2 − (q 2+2q+2+2q -1+q -2)|
〉C2
|
〉C2 = −|
〉C2 − |
〉C2 − |
〉C2 − (q 2+q+3+q -1+q -2)|
〉C2
|
〉C2 = −q 1/2|
〉C2 − q -1/2|
〉C2 − q 1/2+q -1/2
1
|
〉C2
which are related to the ﬁrst set of rules by:
|
〉C2 = |
〉C2 − |
〉C2
These invariants are not new. In fact, all three invariants are special cases of the Reshetikhin-Turaev
invariants [11]. (It should be emphasized that these invariants are part of a wide literature of closely related
ideas. Two other inﬂuential papers are [2] and [16].) According to Reshetikhin and Turaev, for each simple
Lie algebra g, there exists an invariant RTg of appropriately colored tangled ribbon graphs. Each edge is
colored by an irreducible representation of g and each vertex should be colored by a tensor of a certain kind.
The invariants we deﬁne all satisfy ⟨G⟩g = RTg(G) if the graph is colored in a certain simple way. (By our
notation, the Kauﬀman bracket also satisﬁes this equation.) This connection will be explained in detail in
the second part of the paper.
In addition, the A2 bracket is essentially a specialization of the HOMFLY polynomial [3], because the
HOMFLY polynomial describes RTAn; and the C2 bracket is essentially a specialization of the Kauﬀman
polynomial, because the Kauﬀman polynomial [9]
describes RTBn, RTCn, and RTDn. By the relation B2 = C2, the C2 bracket encompasses a second
specialization of the Kauﬀman polynomial. (The Kauﬀman polynomial should not be confused with the
Kauﬀman bracket.) Thus, the most interesting case is the G2 bracket. The Reshetikhin-Turaev deﬁnition
in the G2 case is also cast in an explicit form in [10].
The author recently learned that many of the results presented here, in particular the deﬁnition of the
A2 and G2 brackets, were obtained independently by Francois Jaeger [5, 7, 6].
