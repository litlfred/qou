---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-013-4-the-cyclotomic-function-of-a-knot-is-q--holono
section_title: "The cyclotomic function of a knot is q--holonomic"
section_number: 4
pages: 15-16
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
Habiro [15] proved that the colored Jones polynomial (of sl2) can be rearranged
in the following convenient form, known as the cyclotomic expansion of the
colored Jones polynomial: For every 0–framed knot K, there exists a function
CK : Z>0 →Z[q±1]
such that
JK(n) =
∞
X
k=1
CK(k)S(n, k),
where
S(n, k) := {n + k −1}2k−1/(v −v−1) =
Qn+k−1
n−k+1 (vi −v−i)
v −v−1
.
Note that S(n, k) does not depend on the knot K. Note that J is determined
from C and vice-versa by an upper diagonal matrix, thus C takes values in
Q(q). The diﬃcult part of Habiro’s result is CK takes values in Z[q±]. The
integrality of the cyclotomic function is a crucial ingredient in the study of
integrality properties of 3–manifold invariants, [15].
Theorem 4 The cyclotomic function CK : N →Z[q±] of every knot K is
q–holonomic.
Proof Habiro showed that CK(n) is the quantum invariant of the knot K with
color
P ′′(n) :=
Qn−1
i=1 (V (2) −v2i−1 −v1−2i)
{2n −1}2n−2
,
Geometry & Topology, Volume 9 (2005)
1268
Stavros Garoufalidis and Thang T Q Lˆe
where V (n) is the unique n–dimensional simple sl2–module, and (retaining
Habiro’s notation with a shift n →n −1) P ′′(n) is considered as an element
of the ring of sl2–modules over Q(v).
Using induction one can easily prove that
P ′′(n) =
n
X
k=1
R(n, k)V (k),
where R(k, n) is given by
R(n, k) = (−1)n−k
{2k}
{2n −1}![2n]

2n
n −k

.
We learned this formula from Habiro [15] and Masbaum [25]. Since
CK(n) =
X
k
R(n, k)JK(k)
and R(n, k) is q–proper hypergeometric and thus q–holonomic in both variables
n and k, it follows that CK is q–holonomic.
