---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-013-52-examples
section_title: "Examples"
section_number: 5.2
pages: 25-26
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
λ
on the character variety Xirr
λ (Π(K)) for the following four examples: the trefoil knot 3 1 =
J(2, 2), 52 = J(2, 4), the ﬁgure eight knot 4 1 = J(2,−2), and 6 1 = J(2,−4) respectively.
The computer program for the computation is written on the free computer algebra system
Maxima [Sa06].
(1) For the trefoil knot 3 1 = J(2, 2), the Riley polynomial is given by
φJ(2,2)(s, u) =−1 + s + s−1− u.
The computation of the non–abelian Reidemeister torsion fo r J(2, 2) is expressed
as follows.
TJ(2,2)
λ (ρ√
s,u) = τ0
s + s−1− 2
(
−3(s + s−1− 2)
)
=−3τ0.
This coincides with the inverse of the result [Dub06, Subsec tion 6.1] (see Re-
mark 12).
(2) For 5 2 = J(2, 4), the Riley polynomial is given by
φJ(2,4)(s, u) =−3 + 2(s + s−1) +
(
−4 + 3(s + s−1)− (s + s−1)2)
u
+
(
−3 + 2(s + s−1)
)
u2− u3.
25
The non–abelian Reidemeister torsion for 52 = J(2, 4) is expressed as follows.
TJ(2,4)
λ (ρ√s,u) = τ0
s + s−1− 2 [−2 + 21(s + s−1)− 10(s + s−1)2
+{−2 + 15(s + s−1)− 17(s + s−1)2 + 5(s + s−1)3}u
+{6 + 7(s + s−1)− 5(s + s−1)2}u2]
= τ0
(
−10(s + s−1) + 1 +
(
5(s + s−1)2− 7(s + s−1) + 1
)
u
+
(
−5(s + s−1)− 3
)
u2)
.
(3) For the ﬁgure eight knot 4 1 = J(2,−2), the Riley polynomial is given by
φJ(2,−2)(s, u) = (3− s− s−1)(u + 1) + u2.
The computation of the non–abelian Reidemeister torsion for J(2,−2) is expressed
as follows.
TJ(2,−2)
λ (ρ√s,u) = τ0
s + s−1− 2
(
−2(s + s−1) + 1
)(
s + s−1− 2
)
= τ0
(
−2(s + s−1) + 1
)
.
This coincides with the inverse of the result [Dub06, Subsec tion 6.3] (see Re-
mark 12) in which the torsion is expressed as±√17 + 4Iλ.
Since the longitude λ is equal to [y, x−1][x, y−1], one has
Iλ =−2− (s + s−1) + s2 + s−2.
Thus, up to sign, we have
√
17 + 4Iλ = 2(s + s−1)− 1.
(4) For 6 1 = J(2,−4), the Riley polynomial is given by
φJ(2,−4)(s, u) = 5− 2(s + s−1) +
(
12 + (s + s−1)2− 7(s + s−1)
)
u+
(
11 + (s + s−1)2− 6(s + s−1)
)
u2 +
(
5− 2(s + s−1)
)
u3 + u4.
The non–abelian Reidemeister torsion for J(2,−4) is expressed as follows.
TJ(2,−4)
λ (ρ√s,u)
= τ0
s + s−1− 2[−14− 13(s + s−1) + 26(s + s−1)2− 8(s + s−1)3
+{−8− 34(s + s−1) + 49(s + s−1)2− 23(s + s−1)3 + 4(s + s−1)4}u
+{−2− 31(s + s−1) + 32(s + s−1)2− 8(s + s−1)3}u2
+{2− 9(s + s−1) + 4(s + s−1)2}u3]
= τ0
[(
−8(s + s−1)2 + 10(s + s−1) + 7
)
+
(
4(s + s−1)3− 15(s + s−1)2 + 19(s + s−1) + 4
)
u
+
(
−8(s + s−1)2 + 16(s + s−1) + 1
)
u2 +
(
4(s + s−1)− 1
)
u3]
.
