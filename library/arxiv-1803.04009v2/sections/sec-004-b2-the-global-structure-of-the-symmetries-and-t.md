---
doc_id: arxiv-1803.04009v2
doc_title: "Prepared for submission to JHEP IPMU-18-0045"
section_id: sec-004-b2-the-global-structure-of-the-symmetries-and-t
section_title: "B.2 The global structure of the symmetries and 't Hooft anomaly"
section_number: null
pages: 51-52
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
Now we study the global structure of the symmetriessu(2)H and su(2)C. We claim that
both of them areSO(3) type in the sense that all gauge invariant operators (in the absence
of background ﬁelds) are in representations ofSO(3) (i.e, integer spin representations of
su(2)). We denote them asSO(3)H and SO(3)C, respectively. However, we will also show
that there is a mixed ’t Hooft anomaly between these groupsSO(3)H and SO(3)C which
forbid gauging both of them asSO(3) groups. In other words, this anomaly implies that if
we gauge one of them asSO(3) gauge group, then the other symmetry becomesSU (2).
It is easy to see thatsu(2)H is of SO(3) type. The ﬁelds (Ei, ˜Ei) transform under
su(2)H. Now, the center −1 ∈ SU (2)H multiplies the (Ei, ˜Ei) by (−1), but this can
be cancelled by aU(1) gauge transformation. Therefore, the action of the center−1∈
SU (2)H to all gauge invariant operators is trivial. This shows that the symmetry which
acts faithfully to gauge invariant operators isSO(3)H.
By mirror symmetry, it is obvious that the symmetrysu(2)C must also be ofSO(3)
type. More direct way to see this is to notice that all monopole operators have integer
charges underu(1)C⊂ su(2)C. Thus, all operators are in integer spin representations of
su(2)C, meaning that it isSO(3)C.
However, there is a subtle mixed anomaly betweenSO(3)H andSO(3)C as we now see.
Including the gauge groupU(1), the operators are in representations of
U(1)×SU (2)H
Z2
=U(2). (B.5)
Then, gauge invariant operators are in representations ofSU (2)H/Z2 =SO(3)H. Now let
usconsideramonopolebackgroundoftheabove U(2)onS2 whichisobtainedbyembedding
aU(1) magnetic ﬂux intoU(2) as diag(+1, 0). This is separated into gauge and ﬂavor parts
as
diag(+1, 0) = diag(+1/2, +1/2) + diag(+1/2,−1/2). (B.6)
So, the gaugeU(1) has magnetic ﬂux+1/2onS2. TheSO(3)H also has nontrivial magnetic
ﬂuxdiag(+1/2,−1/2)which is measured by a nontrivial value of the second Stiefel-Whitney
classw2∈H2(X, Z2) of theSO(3)H bundle, whereX is the spacetime on which the theory
is placed. Roughly speaking, the Stiefel-Whitney classw2 is deﬁned such that half of it,
1
2w2 mod 1, is the fractional part of the magnetic ﬂux ofSO(3). The integer part is not
topological invariant in non-abelianSO(3) group. The topologically invariant magnetic
ﬂuxes are classiﬁed byπ1(SO(3)) = Z2.
The above argument implies the following. Suppose we gauge the groupSO(3)H as
an SO(3) gauge group. Then it is possible to consider a monopole operator ofSO(3)H
which has nontrivial Stiefel-Whitney class. However, for this monopole operator to make
sense, we also have to turn on a half-integral magnetic ﬂux of the gaugeU(1). Then, these
monopole operators have half-integral charges under the topologicalu(1)C and hence they
are in half-integer spin representations of the Coulomb branch symmetrysu(2)C. Therefore,
by gaugingSO(3)H, the symmetrysu(2)C becomes SU (2)C. This fact forbids to gauge
– 50 –
both of thesu(2)H andsu(2)C symmetries asSO(3) type symmetries, and this means there
is an anomaly.
More formally, the anomaly is shown as follows [56]. (See also [57–64] where nontrivial
mixture of the center of gauge and ﬂavor symmetries lead to ’t Hooft anomalies.) Let
f =da be the ﬁeld strength of theU(1) gauge ﬁeld,F =dA +A2 be the ﬁeld strength of
the mixed gauge-ﬂavor symmetryU(2) = [U(1)×SU (2)H]/Z2, andB be the gauge ﬁeld of
u(1)C. Then, the coupling of the backgroundB and F in the Lagrangian is given by
∫
X
i
2πB∧f = i
4π
∫
X
B∧ trF. (B.7)
where X is a 3-manifold in which ourT [SU (2)] theory lives. To make the deﬁnition man-
ifestly gauge invariant, we consider a 4-manifoldY whose boundary isX, ∂Y = X, and
deﬁne the above coupling as
i
4π
∫
Y
G∧ trF (B.8)
where G = dB. However, this depends on the extension of the manifold and the gauge
ﬁeld fromX toY. Choose another extensionY′. Then glueY andY′ together along their
common boundary to make a closed manifoldZ. Then we get
i
4π
∫
Y
G∧ trF− i
4π
∫
Y′
G∧ trF = i
4π
∫
Z
G∧ trF. (B.9)
This shows the dependence on the extension. Now, letw2(SO(3)H) and w2(SO(3)C) be
the Stiefel-Whitney classes ofSO(3)H and SO(3)C, respectively. We have
1
2G =πw2(SO(3)C) mod 2 π, (B.10)
1
2 trF =πw2(SO(3)H) mod 2 π (B.11)
and hence
i
4π
∫
Z
G∧ trF =iπ
∫
Z
w2(SO(3)C)w2(SO(3)H) mod 2 πi. (B.12)
This represents the anomaly. The anomaly polynomial is1
2w2(SO(3)C)w2(SO(3)H).
