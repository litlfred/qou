---
doc_id: arxiv-math-0403224v1
doc_title: "Difference equation of the colored Jones polynomial for torus knot"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 0403224v1.pdf
source_sha256: c25ccba77da375ad
toc_source: undetermined
doc_brief: "Difference equation of the colored Jones polynomial for torus knot — 7 sections: Page 1; Page 2; Page 3"
---
DIFFERENCE EQUATION OF THE COLORED JONES POLYNOMIAL FOR TORUS KNOT5
Hereafter we use a standard notation of the q-product and the q-binomial
coeﬃcient (see e.g. Ref. 1);
(x)n = (x; q)n =
n
Y
k=1
(1 −x qk−1)
"
n
m
#
q
=
(q)n
(q)n−m (q)m
Theorem 8 ( [9]). Let the function H2,2m+1(x) be deﬁned by
H2,2m+1(x) =
∞
X
km≥···≥k2≥k1≥0
(x)km+1 xkm

m−1
Y
i=1
qki(ki+1) x2ki
"
ki+1
ki
#
q

(11)
for |q| < 1 and |x| < 1. Then we have
H2,2m+1(x) =
∞
X
n=0
χ8m+4(n) q
n2−(2m−1)2
8(2m+1) x
n−(2m−1)
2
(12)
and it satisﬁes
H2,2m+1(x) = 1 −q x2 −q2m x2m+1 H2,2m+1(q x)
(13)
For m = 1 case, see also Ref. 1 [Chap. 2, p. 29] and Ref. 22.
With an expression (11), we can take a limit x →q−N; an inﬁnite sum
terminates into a ﬁnite sum due to (q−N)k = 0 for k > N. Comparing eq. (8)
with eq. (13) we obtain the colored Jones polynomial for the torus knot
T2,2m+1 as follows;
Proposition 9. The N-colored Jones polynomial for the torus knot T2,2m+1
is given by
JT2,2m+1(N) = qm(1−N)
∞
X
km≥···≥k2≥k1≥0
(q1−N)km q−Nkm

m−1
Y
i=1
qki(ki+1−2N)
"
ki+1
ki
#
q

(14)
We see that the colored Jones polynomial for the trefoil m = 1 coincides
with results in Refs. 8,13. It should be remarked that in Ref. 15 constructed
was the colored Jones polynomial for the twist knot, which gives a diﬀerent
expression of the colored Jones polynomial for the trefoil. By applying a
twisting formula given in Ref. 15, we have another expression of the colored
Jones polynomial in the form of cyclotomic expansion in a sense of Ref. 8
as follows;
