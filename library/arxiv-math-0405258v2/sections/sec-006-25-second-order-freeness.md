---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-006-25-second-order-freeness
section_title: "Second order freeness"
section_number: 2.5
pages: 7-10
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
of second order freeness which is intended to capture the struct ure
of the ﬂuctuation functionals for random matrices arising in the limit
N → ∞, in the same way as the usual freeness captures the structure
of the expectation of the trace in the limit. We recall the relevant
notations and deﬁnitions.
8 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
Deﬁnition 2.3. A second order non-commutative probability space (A,
ϕ1, ϕ2) consists of a unital algebra A, a tracial linear functional
ϕ1 : A → C with ϕ(1) = 1
and a bilinear functional
ϕ2 : A × A → C,
which is tracial in both arguments and which satisﬁes
ϕ2(a, 1) = 0 = ϕ2(1, b) for all a, b ∈ A.
Notation 2.4. Let unital subalgebras A1, . . . ,Ar ⊂ A be given.
1) We say that a tuple ( a1, . . . , an) ( n ≥ 1) of elements from A is
cyclically alternating if, for each k, we have an i(k) ∈ { 1, . . . , r} such
that ak ∈ A i(k) and, if n ≥ 2, we have i(k) ⁄= i(k+1) for all k = 1, . . . , n.
We count indices in a cyclic way modulo n, i.e., for k = n the above
means i(n) ⁄= i(1). Note that for n = 1, we do not impose any condition
on neighbours.
2) We say that a tuple ( a1, . . . , an) of elements from A is centered if we
have
ϕ1(ak) = 0 for all k = 1, . . . , n.
Deﬁnition 2.5. Let ( A, ϕ1, ϕ2) be a second order non-commutative
probability space. We say that unital subalgebras A1, . . . ,Ar ⊂ A are
free with respect to (ϕ1, ϕ2) or free of second order , if they are free (in
the usual sense [VDN]) with respect to ϕ1 and if the following condition
for ϕ2 is satisﬁed. Whenever we have, for n, m ≥ 1, tuples ( a1, . . . , an)
and ( bm, . . . , b1) from A such that both are centered and cyclically
alternating then we have
(1) If n ⁄= m, then
ϕ2(a1 · · · an, bm · · ·b1) = 0 .
(2) If n = m = 1 and a ∈ A i, b ∈ A j, with i ⁄= j, then
ϕ2(a, b) = 0 .
(3) If n = m ≥ 2, then
ϕ2(a1 · · ·an, bn · · · b1) =
n−1∑
k=0
ϕ1(a1b1+k) · ϕ1(a2b2+k) · · · ϕ1(anbn+k).
For a visualization of this formula, one should think of two concentric
circles with the a’s on one of them and the b’s on the other. However,
whereas on one circle we have a clockwise orientation of the points, o n
the other circle the orientation is counter-clockwise. Thus, in orde r to
FLUCTUATIONS OF UNITARY RANDOM MATRICES 9
match up these points modulo a rotation of the circles, we have to pa ir
the indices as in the sum above.
Recall that in the combinatorial description of freeness [NSp], the
extension of ϕ1 to a multiplicative function on non-crossing partitions
plays a fundamental role. In the same way, second order freenes s will
rely on a suitable extension of ϕ2.
Notation 2.6. Let ( A, ϕ1, ϕ2) be a second order non-commutative
probability space. Then we extend the deﬁnition of ϕ1 and ϕ2 as fol-
lows:
ϕ1 :
∞⋃
n=1
(
Sn × An) → C
(π, a1, . . . , an) ↦→ϕ1(π)[a1, . . . , an]
is, for a cycle π = (i1, i2, . . . , ir), given by
ϕ1(π)[a1, . . . , an] := ϕ1(ai1ai2ai3 · · · air )
and extended to general π ∈ Sn by multiplicativity
ϕ1(π1 × π2)[a1, . . . , an] = ϕ1(π1)[a1, . . . , an] · ϕ1(π2)[a1, . . . , an].
In a similar way,
ϕ2 :
∞⋃
m,n=1
(
Sm × Sn × Am × An) → C
(π1, π2, a1, . . . , am, b1, . . . , bm) ↦→ϕ2(π1, π2)[a1, . . . , am; b1, . . . , bn]
is deﬁned, for two cycles π1 = ( i1, i2, . . . , ip) and π2 = ( j1, j2, . . . , jr),
by
ϕ2(π1, π2)[a1, . . . , am; b1, . . . , bn] := ϕ2(ai1ai2 · · · aip, bj1bj2 · · · bjr )
and extended to the general situation by the derivation property
(4) ϕ2(π1 × π2, π3)[a1, . . . , am; b1, . . . , bn]
= ϕ2(π1, π3)[a1, . . . , am; b1, . . . , bn] · ϕ1(π2)[a1, . . . , am, b1, . . . , bn]
+ ϕ2(π2, π3)[a1, . . . , am; b1, . . . , bn] · ϕ1(π1)[a1, . . . , am, b1, . . . , bn].
and
(5) ϕ2(π1, π2 × π3)[a1, . . . , am; b1, . . . , bn]
= ϕ2(π1, π2)[a1, . . . , am; b1, . . . , bn] · ϕ1(π3)[a1, . . . , am, b1, . . . , bn]
+ ϕ2(π1, π3)[a1, . . . , am; b1, . . . , bn] · ϕ1(π2)[a1, . . . , am, b1, . . . , bn].
10 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
Remark 2.7. Let ( Ai)i∈I be a family of unital subalgebras of the sec-
ond order probability space ( A, ϕ1, ϕ2) which are free of second order.
Suppose that for each i we have ( Bi,j)j∈Ki a family of unital subal-
gebras of Ai which are free of second order. By [VDN, Prop. 2.5.5
(iii)] ( Bi,j)j∈∪iKi are free of ﬁrst order. We leave as an exercise for the
reader to show that the proof of [VDN] can be adapted to show tha t
(Bi,j)j∈∪iKi are free of second order.
