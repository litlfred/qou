---
doc_id: arxiv-1104.0755v2
doc_title: "A connection formula between the Ramanujan function and the q-Airy function"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1104.0755v2.pdf
source_sha256: d2fbbea44598e8f4
doc_brief: "A connection formula between the Ramanujan function and the q-Airy function — We show a connection formula between two diﬀerent q-Airy func- tions."
---
In the study of the q-analysis, it is known that there exist several diﬀerent q-
special functions corresponding to a special function deﬁned by a diﬀerential
equation. For example, three types of q-Bessel functions are known. We
denote them J (1)
ν (x;q), J (2)
ν (x;q) and J (3)
ν (x;q) due to Ismail [6]. The ﬁrst
and the second one are called Jackson’s ﬁrst and second q-Bessel function
and the third one is called the Hahn-Exton q-Bessel function. Similarly, two
types of q-Airy functions are known. We denote them A q(x) and Ai q(x). The
ﬁrst one is called the Ramanujan function and the second one is called the
q-Airy function.
‡Graduate School of Information Science and Technology, Osaka U niversity, 1-1
Machikaneyama-machi, Toyonaka, 560-0043, Japan. E-mail: t-mo rita@cr.math.sci.osaka-
u.ac.jp
1
Three q-Bessel functions are given by
J (1)
ν (x;q) := (qν+1;q)∞
(q;q)∞
(x
2
) ν∑
n≥0
1
(qν+1;q)n
(
−x2
4
) n
,
J (2)
ν (x;q) := (qν+1;q)∞
(q;q)∞
(x
2
) ν∑
n≥0
qn2
(qν+1;q)n
(
−qνx2
4
) n
,
J (3)
ν (x;q) := (qν+1;q)∞
(q;q)∞
xν
∑
n≥0
q
n(n+1)
2
(qν+1;q)n
(
−x2) n
.
The Ramanujan function and the q-Airy function are deﬁned by
Aq(x) :=
∑
n≥0
qn2
(q;q)n
(−x)n,
Aiq(x) :=
∑
n≥0
1
(−q,q ;q)n
{
(−1)nq
n(n− 1)
2
}
(−x)n.
Here, (a;q)n and (a;q)∞ are the q-Pochhammer symbol deﬁned in sec-
tion two. According to [1] , the Ramanujan function A q(x) appears in the
third identity on p.57 of Ramanujan’s ”Lost notebook” [9] as follows ( with
x replaced by q):
Aq(−a) =
∑
n≥0
anqn2
(q;q)n
=
∏
n≥1
(
1 + aq2n−1
1 −qny1 −q2ny2 −q3ny3 − · · ·
)
where
y1 = 1
(1 −q)ψ 2(q),
y2 = 0,
y3 = q +q3
(1 −q)(1 −q2)(1 −q3)ψ 2(q) −
∑
n≥0
(2n+1)q2n+1
1−q2n+1
(1 −q)3ψ 6(q) ,
y4 =y1y3,
ψ (q) =
∑
n≥0
q
n(n+1)
2 = (q2;q2)∞
(q;q2)∞
.
2
Ismail has pointed out that the Ramanujan function is a q-analogue of
the Airy function [6]. We show more detail about these functions in se ction
three.
It is known that there exist a relation for the q-Bessel functions and the
q-Airy function. One is a relation between Jackson’s ﬁrst and second q-Bessel
function [4] :
J (2)
ν (x;q) =
(
−x2
4 ;q
)
∞
J (1)
ν (x;q). (1)
Another is a relation between the Hahn-Exton q-Bessel function and the
q-Airy function [8] :
J (3)
ν (x;q) = (−q;q)∞
(q;q)∞
xν Aiq(−qx2), (2)
where qν = −1.
Other relations are not known. The main result in this paper is a relatio n
between two q-Airy functions. It is not known any relation between the
Ramanujan function and the q-Airy function, but these two functions are
related by a connection formula and not by algebraic relation like (1) o r (2).
Connection problems of linear q-diﬀerence equations between the origin
and the inﬁnity are studied by G. D. Birkhoﬀ [2]. Watson gave a connec tion
formula for the basic hypergeometric equation 2ϕ 1 in 1910 [11]:
2ϕ 1 (a,b ;c;q,x ) = (b,c/a ;q)∞(ax,q/ax ;q)∞
(c,b/a ;q)∞(x,q/x ;q)∞
2ϕ 1 (a,aq/c ;aq/b ;q,cq/abx )
+ (a,c/b ;q)∞(bx,q/bx ;q)∞
(c,a/b ;q)∞(x,q/x ;q)∞
2ϕ 1 (b,bq/c ;bq/a ;q,cq/abx ).
Recently, C. Zhang has given some connection formulae of q-diﬀerence
equations of the conﬂuent type [12], [13] and [14]. Zhang gives a conn ection
formula of Jackson’s q-Bessel function J (1)
ν (x;q) [14]. In [14], Zhang intro-
duced the q-Borel transformation and the q-Laplace transformation which
are useful to study connection problems. In section four, we app ly Zhang’s
method to the q-Airy functions.
The connection formula of the q-Airy function gives a relation between
the Ramanujan function and the q-Airy function as follows:
3
Theorem For any x ∈ C∗,
Aq2
(
−q3
x2
)
= 1
(q, −1;q)∞
{
θ
(x
q
)
Aiq(−x) +θ
(
−x
q
)
Aiq(x)
}
.
Since our new relation shows an asymptotic behavior of the Ramanuj an func-
tion near the inﬁnity, it may be useful to study the Ramanujan func tion or
similar type q-series.
