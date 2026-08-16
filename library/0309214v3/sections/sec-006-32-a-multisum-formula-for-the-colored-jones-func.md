---
doc_id: 0309214v3
doc_title: "School of Mathematics, Georgia Institute of Technology"
section_id: sec-006-32-a-multisum-formula-for-the-colored-jones-func
section_title: "A multisum formula for the colored Jones function of a knot"
section_number: 3.2
pages: 13-16
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
doc_brief: "The colored Jones function is q–holonomic Stavros Garoufalidis Thang T Q L ˆ — A function of several variables is called holonomic if, roug hly speaking, it is determined from ﬁnitely many of its"
---
knot
In this section we will give explicit multisum formulas for t he sl2 –colored Jones
function of a knot. The calculation here is computerized in S ection 6.
Consider a word w = σǫ1
i1 . . . σǫc
ic of length m written in the standard generators
σ1, . . . , σs−1 of the braid group Bm with m strands, where ǫi = ±1 for all i.
w gives rise to a braid β ∈ Bm , and we assume that the closure of β is a knot
K. Let K′ denote long knot which is the closure of all but the ﬁrst strand of β .
A coloring of K′ is a tuple k = ( k1, . . . , kc) of angle variables placed at the
crossings of K′ .
Lemma 3.6 There is a unique way to extend a coloring k of K′ to a coloring
of the crossings and part-arcs of K′ such that
• around each crossing the following consistency relations a re satisﬁed:
a
b+k a−k
b
k
b
a+kb−k
a
k
• The color of the lower-left incoming part-arc is 0.
Geometry & Topology, Volume 9 (2005)
1266 Stavros Garoufalidis and Thang T Q Lˆ e
Moreover, the labels of the part-arcs are linear forms on k.
Proof Start walking along the long knot starting at the incoming pa rt-arc.
At the ﬁrst crossing, whether over or under, the label of the o utgoing part-arc
is determined by the label of the ending part-arc and the angl e variable of the
crossing. Thus, we know the label of the outgoing part-arc of the ﬁrst crossing.
Keep going. Since K′ is topologically an interval, the result follows.
For an example, see Figure 1.
w = σ3
1 β = K′ =
0k
k
k
k
k0
0
0
0
0
Figure 1: A word w , the corresponding braid β , its long closure K′ , and a coloring of
K′
Fix a coloring of K′ determined by a vector k. Let bi(k) for i = 1 , . . . , m
denote the labels of the top part-arcs of β . Let xj(k) and yj(k) denote the
labeling of the left and right incoming part-arcs at the ith crossing of K′ for
j = 1, . . . , c. According to Lemma 3.6, bi(k), xj (k) and yj(k) are linear forms
on k.
It is easy to see that
tr′
q(β) =
∑
k≥0
Fw(n, k)
where
Fw(n, k) :=
m∏
i=2
v
n
2 −bi(k)
c∏
j=1
fsgn(ǫi)(n, n; xj(k), yj(k)).
is a q –proper hypergeometric function. Remark 3.5 then implies t hat
Proposition 3.7 The colored Jones function of a long knot K′ is a multisum
of a q –proper hypergeometric function:
JK′(n) =
∑
k≥0
Fw(n, k).
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1267
Remark 3.8 If a long knot K′ is presented by a planar projection D with c
crossings (which is not necessarily the closure of a braid), then similar to the
above there is a q –proper hypergeometric function FD(n, k) of c + 1 variables
such that JK′(n) = ∑
k≥0 FD(n, k). Of course, FD depends on the planar
projection. Occasionally, some of the summation variables can be ignored.
This is the case for the right hand-trefoil (where the multis um reduces to a
single sum) and the ﬁgure eight (where it reduces to a double s um).
D Bar-Natan has kindly provided us with a computerized versi on of Proposition
3.7, [1].
4 The cyclotomic function of a knot is q–holonomic
Habiro [15] proved that the colored Jones polynomial (of sl2 ) can be rearranged
in the following convenient form, known as the cyclotomic expansion of the
colored Jones polynomial: For every 0–framed knot K, there exists a function
CK : Z>0 → Z[q±1]
such that JK(n) =
∞∑
k=1
CK(k)S(n, k),
where S(n, k) := {n + k − 1}2k−1/(v − v−1) =
∏ n+k−1
n−k+1 (vi − v−i)
v − v−1 .
Note that S(n, k) does not depend on the knot K. Note that J is determined
from C and vice-versa by an upper diagonal matrix, thus C takes values in
Q(q). The diﬃcult part of Habiro’s result is CK takes values in Z[q±]. The
integrality of the cyclotomic function is a crucial ingredi ent in the study of
integrality properties of 3–manifold invariants, [15].
Theorem 4 The cyclotomic function CK : N → Z[q±] of every knot K is
q –holonomic.
Proof Habiro showed that CK(n) is the quantum invariant of the knot K with
color
P ′′(n) :=
∏ n−1
i=1 (V (2) − v2i−1 − v1−2i)
{2n − 1}2n−2
,
Geometry & Topology, Volume 9 (2005)
1268 Stavros Garoufalidis and Thang T Q Lˆ e
where V (n) is the unique n–dimensional simple sl2 –module, and (retaining
Habiro’s notation with a shift n → n − 1) P ′′(n) is considered as an element
of the ring of sl2 –modules over Q(v).
Using induction one can easily prove that
P ′′(n) =
n∑
k=1
R(n, k)V (k),
where R(k, n) is given by
R(n, k) = ( −1)n−k {2k}
{2n − 1}![2n]
[ 2n
n − k
]
.
We learned this formula from Habiro [15] and Masbaum [25]. Si nce
CK(n) =
∑
k
R(n, k)JK(k)
and R(n, k) is q –proper hypergeometric and thus q –holonomic in both variables
n and k , it follows that CK is q –holonomic.
