---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-012-32-a-multisum-formula-for-the-colored-jones-func
section_title: "A multisum formula for the colored Jones function of a knot"
section_number: 3.2
pages: 13-15
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
A multisum formula for the colored Jones function of a
knot
In this section we will give explicit multisum formulas for the sl2–colored Jones
function of a knot. The calculation here is computerized in Section 6.
Consider a word w = σǫ1
i1 . . . σǫc
ic of length m written in the standard generators
σ1, . . . , σs−1 of the braid group Bm with m strands, where ǫi = ±1 for all i.
w gives rise to a braid β ∈Bm, and we assume that the closure of β is a knot
K. Let K′ denote long knot which is the closure of all but the ﬁrst strand of β.
A coloring of K′ is a tuple k = (k1, . . . , kc) of angle variables placed at the
crossings of K′.
Lemma 3.6 There is a unique way to extend a coloring k of K′ to a coloring
of the crossings and part-arcs of K′ such that
• around each crossing the following consistency relations are satisﬁed:
a
b+k
a−k
b
k
b
a+k
b−k
a
k
• The color of the lower-left incoming part-arc is 0.
Geometry & Topology, Volume 9 (2005)
1266
Stavros Garoufalidis and Thang T Q Lˆe
Moreover, the labels of the part-arcs are linear forms on k.
Proof Start walking along the long knot starting at the incoming part-arc.
At the ﬁrst crossing, whether over or under, the label of the outgoing part-arc
is determined by the label of the ending part-arc and the angle variable of the
crossing. Thus, we know the label of the outgoing part-arc of the ﬁrst crossing.
Keep going. Since K′ is topologically an interval, the result follows.
For an example, see Figure 1.
w = σ3
1
β =
K′ =
0
k
k
k
k
k
0
0
0
0
0
Figure 1: A word w, the corresponding braid β, its long closure K′, and a coloring of
K′
Fix a coloring of K′ determined by a vector k. Let bi(k) for i = 1, . . . , m
denote the labels of the top part-arcs of β. Let xj(k) and yj(k) denote the
labeling of the left and right incoming part-arcs at the ith crossing of K′ for
j = 1, . . . , c. According to Lemma 3.6, bi(k), xj(k) and yj(k) are linear forms
on k.
It is easy to see that
tr′
q(β) =
X
k≥0
Fw(n, k)
where
Fw(n, k) :=
m
Y
i=2
v
n
2 −bi(k)
c
Y
j=1
fsgn(ǫi)(n, n; xj(k), yj(k)).
is a q–proper hypergeometric function. Remark 3.5 then implies that
Proposition 3.7 The colored Jones function of a long knot K′ is a multisum
of a q–proper hypergeometric function:
JK′(n) =
X
k≥0
Fw(n, k).
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q–holonomic
1267
Remark 3.8 If a long knot K′ is presented by a planar projection D with c
crossings (which is not necessarily the closure of a braid), then similar to the
above there is a q–proper hypergeometric function FD(n, k) of c + 1 variables
such that JK′(n) = P
k≥0 FD(n, k).
Of course, FD depends on the planar
projection.
Occasionally, some of the summation variables can be ignored.
This is the case for the right hand-trefoil (where the multisum reduces to a
single sum) and the ﬁgure eight (where it reduces to a double sum).
D Bar-Natan has kindly provided us with a computerized version of Proposition
3.7, [1].
4
