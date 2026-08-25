---
doc_id: arxiv-1208.2521v1
doc_title: "On q-analogues of the Fourier and Hankel transforms"
section_id: sec-008-4-a-q-analogue-of-grafs-addition-formula
section_title: "A q-analogue of Graf’s addition formula"
section_number: 4
pages: 10-12
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "On q-analogues of the Fourier and Hankel transforms — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
In this section we will generalize the considerations which led to the orthogonality
relations in Proposition 2.6. The resulting formula will tu rn out to be a q-analogue
of Graf’s addition formula and, at the same time, of the disco ntinuous integral
of Weber and Schafheitlin. In a ﬁnal remark we will point out t hat the Graf
type addition formula part can also be done for the q-Bessel functions of Jackson
and Ismail, by similar methods, which go back to Heine, the fo unding father of
q-hypergeometric series.
A formula more general than (2.9) can be derived by expanding the expression
(4.1) (xs− 1t; q)∞ (yt− 1; q)∞
(yt; q)∞ (xst− 1; q)∞
.
as a Laurent series in t (|sx| < |t| < |y|− 1) in two diﬀerent ways. On the one hand,
(4.1) can be expanded by twofold substitution of the q-binomial formula (cf. [6,
(1.3.2)]) as:
1φ 0(s− 1xy− 1; −; q, yt ) 1φ 0(s− 1yx− 1; −; q, xst − 1)
=
∞∑
k=0
∞∑
l=−∞
(s− 1yx− 1; q)k
(q; q)k
(s− 1xy− 1; q)l
(q; q)l
sk xk yl tl− k
=
∞∑
n=−∞
tn yn
∞∑
k=max{− n, 0}
(s− 1yx− 1; q)k
(q; q)k
(s− 1xy− 1; q)n+k
(q; q)n+k
(sxy)k,
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 11
where we substituted l = k+n. Since the inner sum in the last part can be expressed
in terms of a 2φ 1 series (depending on the sign of n), we obtain for |sx| < |t| < |y|− 1
the identity
(4.2)
(xs− 1t, yt − 1; q)∞
(yt, xst − 1; q)∞
=
∞∑
n=0
tn yn (s− 1xy− 1; q)n
(q; q)n
2φ 1
[ s− 1yx− 1, q ns− 1xy− 1
qn+1 ; q, sxy
]
+
− 1∑
n=−∞
tns− nx− n (s− 1yx− 1; q)− n
(q; q)− n
2φ 1
[ s− 1xy− 1, q − ns− 1yx− 1
q− n+1 ; q, sxy
]
.
We might have written (4.2) as a sum over n running from −∞ to ∞ with summand
given for all integer n by the left-hand side of (4.3) below, where, for n < 0, an
interpretation of the 2φ 1 similar to our convention in Remark 2.3 is used. Thus the
analogue of (2.6) becomes:
(4.3) tnyn (s− 1xy− 1, q 1+n; q)∞
(qns− 1xy− 1, q ; q)∞
2φ 1
[ s− 1yx− 1, q ns− 1xy− 1
q1+n ; q, sxy
]
= tns− nx− n (s− 1yx− 1, q 1− n; q)∞
(q− ns− 1yx− 1, q ; q)∞
2φ 1
[ s− 1xy− 1, q − ns− 1yx− 1
q1− n ; q, sxy
]
.
Here we should exclude the case that both 1 + n and n + q log(s− 1xy− 1) are non-
positive integers, or that both 1 − n and −n + q log(s− 1yx− 1) are non-positive
integers.
Note that (4.2) reduces to (2.7) in the special case x = 0 (and also, in view of
(2.6), for y = 0). Formula (4.2) is a q-analogue of (1.4) with z and t replaced by
2(y − s− 1x)1/ 2(y − sx)1/ 2 and t(y − s− 1x)1/ 2(y − sx)− 1/ 2, respectively.
On the other hand we expand (4.1) by twofold substitution of ( 2.7):
(4.4) (xs− 1t; q)∞ (yt− 1; q)∞
(yt; q)∞ (xst− 1; q)∞
=
∞∑
n=−∞
∞∑
k=−∞
tn sk
× yn+k (qn+k+1; q)∞
(q; q)∞
1φ 1(0; qn+k+1; q, y 2) xk (qk+1; q)∞
(q; q)∞
1φ 1(0; qk+1; q, x 2),
which generalizes (2.9). When we compare coeﬃcients of equa l powers of t in (4.2)
and (4.4), we obtain:
Proposition 4.1. For |sxy| < 1 we have
(4.5)
∞∑
k=−∞
sk yn+k (qn+k+1; q)∞
(q; q)∞
1φ 1(0; qn+k+1; q, y 2) xk (qk+1; q)∞
(q; q)∞
1φ 1(0; qk+1; q, x 2)
=







yn (s− 1xy− 1; q)n
(q; q)n
2φ 1
[ s− 1yx− 1, q ns− 1xy− 1
qn+1 ; q, sxy
]
if n ≥ 0,
s− nx− n (s− 1yx− 1; q)− n
(q; q)− n
2φ 1
[ s− 1xy− 1, q − ns− 1yx− 1
q− n+1 ; q, sxy
]
if n < 0.
