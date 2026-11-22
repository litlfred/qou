---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-001
section_title: "Page 1"
section_number: null
pages: 1-1
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER
SERIES FOR DOUBLE TWIST KNOTS
JEREMY LOVEJOY AND ROBERT OSBURN
In memory of Toshie Takata
Abstract. Using a result of Takata, we prove a formula for the colored Jones polynomial of the
double twist knots K(−m,−p) and K(−m,p) where m and p are positive integers. In the (−m, −p)
case, this leads to new families of q-hypergeometric series generalizing the Kontsevich-Zagier
series. Comparing with the cyclotomic expansion of the colored Jones polynomials of K(m,p)
gives a generalization of a duality at roots of unity between the Kontsevich-Zagier function and
the generating function for strongly unimodal sequences.
1. Introduction
Let K be a knot and JN(K; q) be the usual Nth colored Jones polynomial, normalized to be
1 for the unknot. It is often useful to determine a q-hypergeometric expression for JN(K; q),
and such expressions have been computed for a variety of knots (e.g., [13, 14, 15, 21, 24, 30]).
These have applications to the AJ conjecture [14], the generalized Volume conjecture [11, 16],
the computation of WRT invariants [3, 17] and quantum modular and mock modular forms
[6, 9, 18, 19, 32].
Consider the family of double twist knots K(m,p), where 2m and 2p are nonzero integers
denoting the number of half-twists in each respective region of Figure 1.
Positive integers
correspond to right-handed half-twists and negative integers correspond to left-handed half-
twists.
Using ideas of Habiro [13] and Masbaum [24], Lauridsen [20, Section 6] gave the cyclotomic
expansion of JN(K(m,p); q) for all nonzero m and p (cf. [7, 30]). For example, when m and p are
positive integers we have
JN(K(m,p); q) =
X
n≥0
n=nm≥nm−1≥···≥n1≥0
n=sp≥sp−1≥···≥s1≥0
(q1+N)n(q1−N)nqn
m−1
Y
i=1
qn2
i +ni

ni+1
ni
 p−1
Y
j=1
qs2
j+sj

sj+1
sj

(1.1)
Date: April 13, 2021.
2010 Mathematics Subject Classiﬁcation. 57M27.
Key words and phrases. double twist knots, colored Jones polynomial, duality.
1
