---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-022-123-lewins-dilogarithm-identity-related-with-x-1
section_title: "Lewin’s dilogarithm identity related with x = 1"
section_number: 1.2.3
pages: 20-22
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
2 (
√
13− 3).
In the paper [Le] based on the numerical calculations the fol lowing dilogarithm identity
was suggested
4L(x)−L(x2)− 2
3L(x3) + 1
6L(x6) = 7
6L(1). (1.22)
We are going to prove the accessibility of this identity. For this purpose let us set
a = x3
1 +x3, b = x
1 +x, c = −x
1−x, d = −1
1 +x.
Having in mind the fact that x satisﬁes the quadratic equation x2 + 3x− 1 = 0, one can
check
x3
1 +x3 = x2
2(1 +x), 2 + 4x +x2 =x−1, x (1 + 2x) = (1−x)2, (1 +x)2 = 2−x.
Now, using the duplication formula (1.7) and functional equ ation (1.4), one can check the
following relations
L(x2) = 2L(x)− 2L(a),
L(x2) = 2L(−x)− 2L(c),
L(x6) = 2L(x3)− 2L(a),
L
(1
2
)
+L(b2) = L(a) +L(x3) +L((1−x)2),
L(b2) = 2L(b)− 2L(c2),
L(c2) = 2L(c)− 2L(d),
L(d2) = 2L(d)− 2L
(−1
x
)
,
L((1−x)2) = 2L(d2)− 2L(x).
Dilogarithm identities 21
After elimination a,b,c,d from these relations, one can ﬁnd
L(x6) = 4L(x3)− 2L(x2)− 8L(x) + 8L(−x)− 8L
(−1
x
)
−L(1).
Finally, if we substitute this expression for L(x6) to the LHS of (1.22) and use (1.9) to
remove the terms with negative arguments, the result is
6LHS(1.22) =−16L(−1)−L(1) = 7L(1),
as it was stated.
1.2.4. Browkin’s dilogarithm identities.
Let x = 1
6 (
√
13− 1) and z = 1
6 (
√
13 + 1) be the roots of the quadratic equations
3x2 +x = 1 and 3 z2−z = 1 correspondently. In the paper [Bro2], p.261 the followin g
dilogarithm identities were suggested
L(x6)− 6L(x3) +L(x2) + 18L(x) = 8L(1), (1.23)
L(z6)− 3L(z3)− 6L(z2) + 9L(z) = 2L(1). (1.24)
The main aim of this section is to prove the accessibility of ( 1.23) and (1.24). Let us start
with a proof of the Browkin ﬁrst identity. It can be easily che cked by using the functional
equation (1.4) and relations
x3
1 +x3 = x
4(1 +x), 1−x +x2 = 4x2, 3x + 4 = x−2, 1−x3 = 2x2(x + 2)
that the following identities are valid
L(x6) = 2L(x3)− 2L
( x3
1 +x3
)
,
L(x) +L(x2) = L(x3) +L
( x
2(1 + 2x)
)
+L
( 1 +x
2(1 + 2x)
)
,
L
(1
2
)
+L
( x
1 + 2x
)
=L
( x
2(1 + 2x)
)
+L
( x2
1 +x
)
+L(x),
L
(1
2
)
+L
( 1 +x
1 + 2x
)
=L
( 1 +x
2(1 + 2x)
)
+L(x(1 +x)) +L(x2),
L
(1
4
)
+L
( x
1 +x
)
=L
( x
4(1 +x)
)
+L(x2) +L(x(1−x)),
L(x) +L
( x
1 +x
)
=L
( x2
1 +x
)
+L
( 1−x
2(1 +x)
)
+L
( 1
2(1 +x)
)
,
