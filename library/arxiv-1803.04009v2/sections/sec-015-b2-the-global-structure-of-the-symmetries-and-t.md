---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-015-b2-the-global-structure-of-the-symmetries-and-t
section_title: "B.2 The global structure of the symmetries and 't Hooft anomaly"
section_number: null
pages: 51-52
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
The global structure of the symmetries and ’t Hooft anomaly
Now we study the global structure of the symmetries su(2)H and su(2)C. We claim that
both of them are SO(3) type in the sense that all gauge invariant operators (in the absence
of background ﬁelds) are in representations of SO(3) (i.e, integer spin representations of
su(2)). We denote them as SO(3)H and SO(3)C, respectively. However, we will also show
that there is a mixed ’t Hooft anomaly between these groups SO(3)H and SO(3)C which
forbid gauging both of them as SO(3) groups. In other words, this anomaly implies that if
we gauge one of them as SO(3) gauge group, then the other symmetry becomes SU(2).
It is easy to see that su(2)H is of SO(3) type. The ﬁelds (Ei, ˜Ei) transform under
su(2)H.
Now, the center −1 ∈SU(2)H multiplies the (Ei, ˜Ei) by (−1), but this can
be cancelled by a U(1) gauge transformation. Therefore, the action of the center −1 ∈
SU(2)H to all gauge invariant operators is trivial. This shows that the symmetry which
acts faithfully to gauge invariant operators is SO(3)H.
By mirror symmetry, it is obvious that the symmetry su(2)C must also be of SO(3)
type. More direct way to see this is to notice that all monopole operators have integer
charges under u(1)C ⊂su(2)C. Thus, all operators are in integer spin representations of
su(2)C, meaning that it is SO(3)C.
However, there is a subtle mixed anomaly between SO(3)H and SO(3)C as we now see.
Including the gauge group U(1), the operators are in representations of
U(1) × SU(2)H
Z2
= U(2).
(B.5)
Then, gauge invariant operators are in representations of SU(2)H/Z2 = SO(3)H. Now let
us consider a monopole background of the above U(2) on S2 which is obtained by embedding
a U(1) magnetic ﬂux into U(2) as diag(+1, 0). This is separated into gauge and ﬂavor parts
as
diag(+1, 0) = diag(+1/2, +1/2) + diag(+1/2, −1/2).
(B.6)
So, the gauge U(1) has magnetic ﬂux +1/2 on S2. The SO(3)H also has nontrivial magnetic
ﬂux diag(+1/2, −1/2) which is measured by a nontrivial value of the second Stiefel-Whitney
class w2 ∈H2(X, Z2) of the SO(3)H bundle, where X is the spacetime on which the theory
is placed. Roughly speaking, the Stiefel-Whitney class w2 is deﬁned such that half of it,
1
2w2 mod 1, is the fractional part of the magnetic ﬂux of SO(3). The integer part is not
topological invariant in non-abelian SO(3) group. The topologically invariant magnetic
ﬂuxes are classiﬁed by π1(SO(3)) = Z2.
The above argument implies the following. Suppose we gauge the group SO(3)H as
an SO(3) gauge group. Then it is possible to consider a monopole operator of SO(3)H
which has nontrivial Stiefel-Whitney class. However, for this monopole operator to make
sense, we also have to turn on a half-integral magnetic ﬂux of the gauge U(1). Then, these
monopole operators have half-integral charges under the topological u(1)C and hence they
are in half-integer spin representations of the Coulomb branch symmetry su(2)C. Therefore,
by gauging SO(3)H, the symmetry su(2)C becomes SU(2)C. This fact forbids to gauge
– 50 –
both of the su(2)H and su(2)C symmetries as SO(3) type symmetries, and this means there
is an anomaly.
More formally, the anomaly is shown as follows [56]. (See also [57–64] where nontrivial
mixture of the center of gauge and ﬂavor symmetries lead to ’t Hooft anomalies.)
Let
f = da be the ﬁeld strength of the U(1) gauge ﬁeld, F = dA + A2 be the ﬁeld strength of
the mixed gauge-ﬂavor symmetry U(2) = [U(1) × SU(2)H]/Z2, and B be the gauge ﬁeld of
u(1)C. Then, the coupling of the background B and F in the Lagrangian is given by
Z
X
i
2πB ∧f = i
4π
Z
X
B ∧tr F.
(B.7)
where X is a 3-manifold in which our T[SU(2)] theory lives. To make the deﬁnition man-
ifestly gauge invariant, we consider a 4-manifold Y whose boundary is X, ∂Y = X, and
deﬁne the above coupling as
i
4π
Z
Y
G ∧tr F
(B.8)
where G = dB. However, this depends on the extension of the manifold and the gauge
ﬁeld from X to Y . Choose another extension Y ′. Then glue Y and Y ′ together along their
common boundary to make a closed manifold Z. Then we get
i
4π
Z
Y
G ∧tr F −i
4π
Z
Y ′ G ∧tr F = i
4π
Z
Z
G ∧tr F.
(B.9)
This shows the dependence on the extension. Now, let w2(SO(3)H) and w2(SO(3)C) be
the Stiefel-Whitney classes of SO(3)H and SO(3)C, respectively. We have
1
2G = πw2(SO(3)C)
mod 2π,
(B.10)
1
2 tr F = πw2(SO(3)H)
mod 2π
(B.11)
and hence
i
4π
Z
Z
G ∧tr F = iπ
Z
Z
w2(SO(3)C)w2(SO(3)H)
mod 2πi.
(B.12)
This represents the anomaly. The anomaly polynomial is 1
2w2(SO(3)C)w2(SO(3)H).
