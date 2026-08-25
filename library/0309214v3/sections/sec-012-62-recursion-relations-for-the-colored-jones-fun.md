---
doc_id: 0309214v3
doc_title: "The colored Jones function is q-holonomic"
section_id: sec-012-62-recursion-relations-for-the-colored-jones-fun
section_title: "Recursion relations for the colored Jones function of the figure 8 knot"
section_number: 6.2
pages: 22-24
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
doc_brief: "The colored Jones function is q-holonomic — A function of several variables is called holonomic if, roug hly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many l inear"
---
ﬁgure 8 knot
The Mathematica package qMultiSum.m can compute recursion relations for
q –multisums. Using this, we can compute equally easily the re cursion relation
for the colored Jones function. Due to the length of the outpu t, we illustrate
this by computing the recursion relation for the colored Jon es function of the
Figure 8 knot. Recall from Equation (2) for p = −1 and from the fact that
c(−1, n) = 1 that the colored Jones function of the ﬁgure 8 knot is give n by:
JK(−1)(n) =
∞∑
k=0
qnk(q−n−1; q−1)k(q−n+1; q)k. (3)
In computer talk,
In[6]:= qZeil[q^(n k) qfac[q^(-n-1),q^(-1),k] qfac[q^(- n+1),q,k],
{k,0,Infinity},n,2]
-1 - n n 2 n
q (q + q ) (-q + q )
Out[6]= SUM[n] == ---------------------------- -
n
-1 + q
-2 + n -1 + 2 n
(1 - q ) (1 - q ) SUM[-2 + n]
> ----------------------------------------- +
n -3 + 2 n
(1 - q ) (1 - q )
-2 - 2 n -1 + n 2 -1 + n
> (q (1 - q ) (1 + q )
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1275
4 4 n 3 + n 1 + 2 n 3 + 2 n 1 + 3 n
> (q + q - q - q - q - q ) SUM[-1 + n])/
n -3 + 2 n
> ((1 - q ) (1 - q ))
This is a second order inhomogeneous recursion relation for the colored Jones
function. A third order homogeneous relation may be obtaine d by:
In[7]:= MakeHomRec[%, SUM[n]]
2 + n 3 n
q (-q + q ) SUM[-3 + n]
Out[7]= ----------------------------- -
2 n 5 2 n
(q + q ) (-q + q )
-2 - n 2 n 8 4 n 6 + n 7 + n 3 + 2 n
> (q (q - q ) (q + q - 2 q + q - q +
4 + 2 n 5 + 2 n 1 + 3 n 2 + 3 n
> q - q + q - 2 q ) SUM[-2 + n]) /
n 5 2 n
> ((q + q ) (q - q )) +
-1 - n n 4 4 n 2 + n 3 + n 1 + 2 n
> (q (-q + q ) (q + q + q - 2 q - q +
2 + 2 n 3 + 2 n 1 + 3 n 2 + 3 n
> q - q - 2 q + q ) SUM[-1 + n]) /
1 + n n
2 n 2 n q (-1 + q ) SUM[n]
> ((q + q ) (-q + q )) + ----------------------- == 0
n 2 n
(q + q ) (q - q )
Of course, we can clear denominators and write the above recu rsion relation
using the q –Weyl algebra A. Let us end with a matching the theoretical bound
for the recursion relation from Section 5 with the computer c alculated bound
from this section. Using Theorem 5, it follows that the summa nd satisﬁes a
recursion relation of order J ⋆ = 1 2 +12 = 2. This implies that the colored Jones
function of the Figure 8 knot satisﬁes an inhomogeneous rela tion of degree 2 as
was found above. The program also conﬁrms that the colored Jo nes function
Geometry & Topology, Volume 9 (2005)
1276 Stavros Garoufalidis and Thang T Q Lˆ e
of the Figure 8 knot does not satisfy an inhomogeneous relati on of order less
than 2.
