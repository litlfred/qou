---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-024-64-localized-shocks
section_title: "Localized shocks"
section_number: 6.4
pages: 39-42
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Another generalization is to localize the precursor operators in the transverse space.
In the context of scrambling these geometries were introduced in [26] and studied
extensively in [7]. The D = 2 + 1 case for a single localized precursor was also studied
in purely two-dimensional CFT terms in [53]. Such a state is given by
e−iHLtLe−iHRtRWx(tw)|TFD⟩, (6.20)
where as usual Wx(tw) =eiHLtwWxe−iHLtw, and Wx is a simple thermal scale operator
localized on the boundary at spatial position x. In this case, the time fold of the
38
Figure 12: Kruskal diagram of a geometry perturbed by four shock waves. The blue
lines show the boundary of W, the shocks are drawn with double black lines, and the
stars show their collisions. The intersection of W and the Einstein-Rosen bridge is
colored blue, green, and gray. The dominant contribution to the action is given by the
ﬁve blue and green regions labeled II . The gray “postcollision” regions have negligible
action.
operator insertion is position dependent. This is shown in Fig. 13 for the state Eq. 6.20
with tL = tR = 0. This also means that the strength of the shock wave dual to the
operator insertion has a position dependent strength h(x)∼ e
2π
β (|tw|−t∗−µ|x|), where µ
is a positive constant and |x| is the transverse distance from the shock. For more
information, see [7].
There are a few interesting diﬀerences in the complexity growth of the localized
one-shock state and the spherically symmetric one-shock state. The early |tw| com-
plexity growth is no longer linear in tw. This is because the operator can grow in
spatial directions as well as the N 2 “matrix” directions, so the switchback eﬀect now
includes cancellations in the transverse space. A tensor network for a single localized
precursor is shown in Fig. 14. The precursor will grow ballistically with characteristic
velocityvB, which is known as the butterﬂy velocity [7,26]. This velocity can be com-
puted holographically for Einstein gravity, and for high temperatures is given by the
dimension dependent formula [7,26]
vB =
√
D− 1
2(D− 2). (6.21)
This spatial growth means that the tensor network Fig. 14 has the geometry of two
solid cones. By considering the point (as a function of transverse coordinate x) where
39
t
tw -|x|/vB
t
|x|
t=tw -|x|/vB
t=tw
Figure 13: A time fold for the state Eq. 6.20 with tL =tR = 0. The length of the fold
is dependent on position. The minimal tensor network for the state is given by ﬁbering
the time fold over the transverse space.
the boundary of W moves oﬀ the singularity (e.g. the point h(x) = v0 in Fig. 8) as
a way of deﬁning the geometry of the Wheeler-DeWitt patch, we ﬁnd an exact match
between the geometry of the tensor network shown in Fig. 14 and the geometry of W
inside the Einstein-Rosen bridge.
On the other hand, if the spatial topology of the ﬁeld theory is still compact,
the precursor will eventually run out of room to grow. Once this saturation occurs,
the growth with |tw| will transition to being linear. However, in this case there is an
additional delay in the growth as compared to Eq. 6.14 related to the size of the spatial
boundary and time it takes for the operator to saturate. (Se, e.g. the caption in Fig. 11
in [7].)
The spatially compact boundary situation is slightly complicated by the fact that
the shock will collide with itself on the other side of the transverse sphere. Instead,
let us consider the planar-AdS black hole geometry. Since the strength of the shock
is position dependent, the action in W is no longer simply linear in tw. Let us match
this action to the volume of the tensor network describing the state. Let m be the
energy density, L the inﬁnite length of a transverse direction, and M = mLD−2 the
total energy. Using the techniques of §6.1, it’s not hard to show that the total action
is
A = 2M(tL +tR) + 4mvD−2
B (|tw|− t∗−tR)D−1
(D− 1)(D− 2) , (6.22)
which is consistent with both the result from CV-duality and the tensor network pre-
dictions of [7]. In particular, with tL =tR = 0, the second term is exactly the volume
of the two solid D− 1-dimensional cones shown in Fig. 14.
40
tw
x
Figure 14: A tensor network for the operator Wx(tw) = eiHLtwWxe−iHLtw. The red
represents the evolution e−iHLtw, the black dot represents the local insertion Wx, and
the green represents the reverse evolution eiHLtw. Left: naive tensor network before
cancellation. Right: tensor network after cancellations outside the inﬂuence of the
insertion Wx.
One can also consider states perturbed by multiple localized precursors
e−iHLtLe−iHRtRWxn(tn)...W x1(t1)|TFD⟩. (6.23)
The analysis is annoyingly complicated and does not provide any additional insight into
the complexity equals action conjecture. Instead, we will simply state that all of the
results from CV-duality from [7] carry over. We can construct the tensor network by
ﬁbering the time fold for the state over the transverse directions [7]. As mentioned, we
can determine the geometry ofW by considering the point (as a function of transverse
coordinate x) where the boundary of W moves oﬀ the singularity. This lets us ﬁnd
an exact match between the geometry of the tensor network that constructs the state
Eq. 6.23 and the geometry of W inside the Einstein-Rosen bridge.
