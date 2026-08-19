---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Steklov Mathematical Institute"
section_id: sec-006-2-lx-ly-lxy-l
section_title: "L(x) +L(y) = L(xy) +L"
section_number: 2
pages: 6-8
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "DILOGARITHM IDENTITIES ANATOL N. KIRILLOV — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
(x(1−y)
1−xy
)
+L
(y(1−x)
1−xy
)
, (1.4)
where 0<x, y < 1.
Theorem B (Cf. [Ro], Section 4) Let f (x) be a function of class C3((0, 1)) which
satisﬁes the relations (1.3) and (1.4). Then we have
f (x) = L(x).
Dilogarithm identities 7
1.1.3. Single–valued dilogarithm.
We continue the function L(x) to all real axis R = R1∪{±∞} by the following rules
L(x) = π2
3 −L(x−1), if x> 1,
L(x) = L
( 1
1−x
)
− π2
6 , if x< 0, (1.5)
L(0) = 0, L (1) = π2
6 , L (+∞) = π2
3 , L (−∞) =−π2
6 .
Important remark. The continuation of Rogers’ dilogarithm function construc ted
in this way satisﬁes the functional equation (1.3), but does not satisfy in general the
ﬁve-term relation (1.4). Namely, one can check LHS(1 .4)− RHS(1.4) = 0, except the
case x < 0, y < 0 and xy > 1. In the latter case LHS(1 .4)− RHS(1.4) = −π2. So,
proving accessibility of a dilogarithm identity we must rem ember about an existence of the
exceptional cases. We leave a checking of exceptional cases to a reader.
In the last part of this section we are going to show that (1.3) is a corollary of (1.4).
Namely, let us take x = a
1−b and y = b
1−a in (1.4). It is clear that a = x(1−y)
1−xy ,
b = y(1−x)
1−xy and the ﬁve-term relation (1.4) is reduced to the so–called A bel equation
(see e.g. [Le])
L
( a
1−b
)
+L
( b
1−a
)
=L
( a
1−b· b
1−a
)
+L(a) +L(b). (1.6)
From (1.6), with 1 −a for b, we obtain
L(a) +L(1−a) = L(1),
as it was claimed. If in (1.4) we take x =y, we get the Abel duplication formula
L(x2) = 2L(x)− 2L
( x
1 +x
)
. (1.7)
From (1.6), with −a for b, and using (1.7), we obtain
L(a2) +L
( −a2
1−a2
)
= 0
and consequently,
L(a) +L(−a) = 1
2L(a2). (1.8)
Finally, if in (1.6) we take a− 1
a for b, we get
L(a2) +L(a−2) = 2L(1);
L(−a2) +L
(−1
a2
)
=−L(1). (1.9)
