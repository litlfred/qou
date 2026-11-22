---
doc_id: arxiv-q-alg-9707006v1
doc_title: "Drinfeld twist for quantum su(2) in the adjoint representation"
section_id: sec-007-42-explicit-computation-of-fq
section_title: "Explicit computation of Fq"
section_number: 4.2
pages: 6-8
source_pdf: 9707006v1.pdf
source_sha256: b9513be9294f56d9
toc_source: inferred
doc_brief: "Drinfeld twist for quantum su(2) in the adjoint representation — We give a detailed description of the adjoint representation of Drinfeld’s twist element, as well as of its coproduct, for suq(2)."
---
Explicit computation of Fq
We start by computing Cq. We ﬁrst ﬁnd
∆(Cq)
=
X−X+ ⊗qH + X−q−H/2 ⊗qH/2X+
+q−H/2X+ ⊗X−qH/2 + q−H ⊗X−X+
+λ−2(q · qH ⊗qH + q−1q−H ⊗q−H −2 · 1 ⊗1)
(19)
and substituting from (11) we obtain
Cq = {[5/2]2,
 
[1/2]2 + q−1[2]2
[2]
[2]
[1/2]2 + q[2]2
!
,



[1/2]2 + q−2[2]
−q−1[2]
0
−q−1[2]
[1/2]2 + 2[2]
−q[2]
0
−q[2]
[1/2]2 + q2[2]


} . (20)
The corresponding 2 and 3-dimensional eigenvectors are
(1, −q−2)
[3/2]2
(1, q2)
[5/2]2
(q2, q, 1)
[1/2]2
(1, −λ, −1)
[3/2]2
(1, −q −q3, q4)
[5/2]2 ,
(21)
where, in the second column, we give the corresponding eigenvalue (Cq has eigenvalues of the form [j + 1/2]2, j =
0, 1, 2, . . .). It is now easy to construct Fq using (18). We ﬁnd
µFq = 1,
DFq =
√
2a
 
q2 + 1
−(q2 −1)
q2 −1
q2 + 1
!
(22)
as well as
TFq =
1
√
6ab



√
2q2a +
√
3qb + 1
√
2q2a −2
√
2q2a −
√
3qb + 1
√
2qa −
√
3(q2 −1)b −q(1 + q2)
√
2qa + 2q(1 + q2)
√
2qa +
√
3(q2 −1)b −q(1 + q2)
√
2a −
√
3qb + q4
√
2a −2q4
√
2a +
√
3qb + q4


,
(23)
where a ≡
p
1 + q4, b ≡
p
1 + q2 + q4. Recalling the discussion in section 2.2, regarding the properties of ρr
under the substitution q 7→q−1, we see that, with ∆(Cq) as in (19), Cq satisﬁes (Cq−1)12 = (Cq)21. It follows then
from (18) that the same relation holds for Fq.
The 2-dimensional subspace
DFq is an SO(2) matrix, even in q, corresponding to an angle of rotation θ(2)
q
given by
tan(θ(2)
q ) = q2 −1
q2 + 1 ,
(24)
counterclockwise in the (+0, 0+) or (0−, −0) plane. As q ranges in the interval (0, ∞), θ(2)
q
goes from −π
4 to
π
4 . Notice that although at the endpoints of the above interval in q, neither the quantum su(2) algebra nor the
adjoint representation (11) make sense, DFq retains nevertheless a well deﬁned value. Under q 7→q−1, the two
axes get interchanged and the angle of rotation changes sign.
As pointed out in [6], a more natural reference point in describing the rotation eﬀected by Fq, and one which
simpliﬁes the results, is the crystal limit q →0 (notice that the eigenvectors of Cq in (21), when normalized, tend
to the basis vectors in this limit). The matrix that connects the general value of q to this limit is Fq0 ≡FqF −1
0
.
We ﬁnd
DFq0 = 1
a
 
1
−q2
q2
1
!
,
(25)
with corresponding angle of rotation θ(2)
q0 given by tan(θ(2)
q0 ) = q2.
0
20
40
60
80
100
-8
-6
-4
-2
00
20
40
60
80
100
120
Figure 1: The curve TFq in the SO(3) manifold (−1 ≤q ≤1)
The 3-dimensional subspace
TFq is an SO(3) matrix - we denote by ˆnq the unit vector along the axis of the rotation represented by TFq and
by θ(3)
q
the angle of rotation (clockwise) around ˆnq (θ(3)
q
ranges in the interval [0, π)). Working in a basis where
one of the basis vectors is along ˆnq, and using the invariance of the trace of TFq under rotations, we ﬁnd
1 + 2 cos(θ(3)
q ) = Tr(TFq) ,
(26)
where, using (23),
Tr(TFq) =
1
√
6ab(
√
2(q2 + q + 1)a + 2
√
3qb + q4 + 2q3 + 2q + 1) .
(27)
Let αi, i = 1, 2, 3 denote the angles that ˆnq makes with the axes - a little geometry shows that
cos2(αi) = TFq ii −cos(θ(3)
q )
1 −cos(θ(3)
q )
.
(28)
Notice that TFq ii (no summation over i) is the angle that the i-th basis vector makes with its image under the
rotation. The correct signs for cos(αi) are obtained by examining the derivatives dFq/dq|q=0 and d2Fq/dq2|q=0.
Under q 7→q−1, the axes (+−) and (−+) get interchanged. As q ranges over the reals, TFq traces out a curve
in the SO(3) manifold (a ball of radius π with antipodal points on the surface identiﬁed). We have plotted this
curve (for the range −1 ≤q ≤1) in ﬁgure 1. The left - right axis is in the (+−)-direction while the vertical is
along (−+) (the axes are marked in degrees). The points of the curve are projected down to the (+−, 00)-plane
and back to the (+−, −+)-plane (at equal intervals in q) for clarity of presentation. To ﬁnd the value qs at which
the curve meets the surface of the ball, we substitute (27) in (26), set θ(3)
q
equal to π and solve for qs - the result is
qs = −1. The corresponding rotation matrix has (1, −1, 1) along the second diagonal as its only nonzero entries.
The curve starts (for q = −1) at the right part of the ﬁgure (upper edge of the ribbon), touching at that point the
(+−, −+)-plane on the diagonal (notice the anisotropic scaling of the axes) as well as the surface of the SO(3)
ball. At q = 1, TFq is the unit matrix, which corresponds to the origin of the ball. Notice that the tangent to
the curve at the origin is along the diagonal in the (+−, −+)-plane (the same holds at q = −1). The property
(Fq−1)12 = (Fq)21 reﬂects itself in the following symmetry of the curve: the points corresponding to q and q−1
are mapped into each other by central reﬂection and subsequent interchange of the (+−), (−+) axes (this allows
one to picture the missing segments −∞< q < −1 and 1 < q < ∞, which are omitted from ﬁgure 1 for clarity).
