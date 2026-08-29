---
doc_id: arxiv-1007.2335v1
doc_title: "Hopf solitons in the Nicole model"
section_id: sec-001-3-initial-conditions
section_title: "Initial conditions"
section_number: 3
pages: 6-7
source_pdf: 1007.2335v1.pdf
source_sha256: a55d544d1740523f
doc_brief: "Hopf solitons in the Nicole model — The Nicole model is a conformal ﬁeld theory in three-dimensi onal space."
---
Initial conditions, for a range of values of Q, need to be provided for the volume-preserving
ﬂow algorithm discussed in the previous section. We use the approac h introduced in [6],
which is brieﬂy reviewed in this section.
To construct an initial ﬁeld the spatial coordinates ( x1, x 2, x 3) ∈ R3 are ﬁrst mapped to
the unit three-sphere via a degree one spherically equivariant map. Explicitly, introduce the
complex coordinates Z1, Z 0 (on the unit three-sphere |Z1|2 + |Z0|2 = 1) as
(Z1, Z 0) =
(
(x1 + ix2) sin g
r , cos g + isin g
r x3
)
, (3.1)
where the proﬁle function g(r) is a monotonically decreasing function of the radius r, with
boundary conditions g(0) = π and g(∞) = 0 .
The initial condition is obtained by taking the stereographic project ion of φ to be a
rational function of Z1 and Z0. The simplest example is to take
φ 1 + iφ 2
1 + φ 3
= Z1
Z0
, (3.2)
which has Q = 1 and is identical to the exact solution (2.3) if the proﬁle function is t aken
to be g = tan − 1(2rλ/ (r2 − λ 2)).
Other choices of rational functions and proﬁle functions do not giv e exact solutions but
do provide suitable initial conditions for the numerical simulation.
An obvious generalization of (3.2) is given by
φ 1 + iφ 2
1 + φ 3
= Z n
1
Z m
0
. (3.3)
This is an axially symmetric ﬁeld with Hopf charge Q = nm. As discussed later, under
volume-preserving ﬂow this initial condition yields the solution of type An,m , obtained pre-
viously using toroidal coordinates [10].
Initial ﬁelds that are not axially symmetric and include knots and links c an be obtained
from less symmetric rational maps. For full details see [6] but some e xamples that are used
in this paper include the ( a, b )-torus knot (here a, b are coprime positive integers with a > b )
φ 1 + iφ 2
1 + φ 3
= Z α
1 Z β
0
Z a
1 + Z b
0
, (3.4)
where α is a positive integer and β is a non-negative integer. The Hopf charge of this ﬁeld
is Q = αb + βa. The position of this ﬁeld is an ( a, b )-torus knot and we denote a ﬁeld of this
type by Ka,b . Of particular relevance will be the simplest torus knot, the trefoil k not, which
corresponds to ( a, b ) = (3 , 2) and can be obtained with Q = 7 from the choice α = 2 and
β = 1.
In all the conﬁgurations discussed above, the position curve cont ains only a single com-
ponent. However, Hopf solitons also exist in which the position curve contains disconnected
6
components that are linked. In the simplest case there are just tw o components and such a
linked conﬁguration will be denoted by the type Lα,β
p,q , where p and q denote the Hopf charges
of the two components if each is taken in isolation, and α and β are the additional contri-
butions to the Hopf charge due the linking of each of the component s with the other. The
total Hopf charge is therefore Q = p + q + α + β. Initial ﬁelds of this type can be constructed
using a rational map in which the denominator is reducible. As an examp le, the ﬁeld
φ 1 + iφ 2
1 + φ 3
= Z n+1
1
Z 2
1 − Z 2
0
, (3.5)
is of the type L1, 1
n,n . It consists of two Hopf solitons that are each of the topological ty pe An, 1
and are linked once to create a ﬁeld with Hopf charge Q = 2n + 2.
The construction described in this section is easily applied to the situa tion of a ﬁnite
simulation region Ω by replacing the proﬁle function boundary conditio n g(∞) = 0 by the
condition that g = 0 on the boundary ∂Ω .
