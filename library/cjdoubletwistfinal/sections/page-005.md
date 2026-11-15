---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
THE COLORED JONES POLYNOMIAL FOR DOUBLE TWIST KNOTS
5
and
Um,p(x; q) =
X
n≥0
n=nm≥nm−1≥···≥n1≥0
n=sp≥sp−1≥···≥s1≥0
(−xq)n(−x−1q)nqn
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
.
(1.16)
Note that if ζN is any Nth root of unity, we have
Fm,p(ζN) = JN(K(−m,−p); ζN)
(1.17)
and
Um,p(−1; ζN) = JN(K(m,p); ζN).
(1.18)
The base case F1,1(q) is q times the Kontsevich-Zagier series,
F(q) :=
X
n≥0
(q)n,
(1.19)
one of the foundational examples of Zagier’s quantum modular forms [31, 32], while
U1,1(x; q) = q−1U(x; q),
(1.20)
where U(x; q) is the generating function for strongly unimodal sequences [4],
U(x; q) :=
∞
X
n=0
(−xq)n(−x−1q)nqn+1.
(1.21)
For this reason, we call the series Fm,p(q) the generalized Kontsevich-Zagier functions for double
twist knots and the Um,p(x; q) the generalized U-functions for double twist knots. Note that
while Um,p(x; q) is well-deﬁned for |q| < 1 and for q a root of unity when x = −1, the generalized
Kontsevich-Zagier functions Fm,p(q) are only deﬁned at roots of unity.
The original Kontsevich-Zagier series F(q) and the generating function for strongly unimodal
sequences U(x; q) when x = −1 are dual at roots of unity via
F(ζ−1
N ) = U(−1; ζN).
(1.22)
This was ﬁrst shown by Bryson, Ono, Pitman and Rhoades [4]. It also follows at once from
(1.4) and the case m = p = 1 of (1.17) and (1.18), which was ﬁrst observed in [18]. Using (1.4)
and the general case of (1.17) and (1.18), we immediately have the following generalization of
(1.22).
Corollary 1.3. If ζN is any Nth root of unity, then we have
Fm,p(ζN) = Um,p(−1; ζ−1
N ).
(1.23)
Next we turn our attention to (1.12) and (1.2). Motivated by these expressions, we deﬁne
Fm,p(q) and Um,p(x; q) by
Fm,p(q) =
X
n2mp≥···≥n1≥0
(q)n2mp(−1)n2mpq−(
n2mp+1
2
)
Y
1≤i<j≤2mp
m∤i
q∆i,j,mninj
×
2p−1
Y
i=1
(−1)nmiq(nmi+1
2
)
2mp−1
Y
i=1
qβi,mni

ni+1
ni

(1.24)
