---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-002-21-6d-a1-20-theory-on-3-manifolds-t6d-and-t6dirr
section_title: "6d A1 (2,0) theory on 3-manifolds : T6d and T6dirred"
section_number: 2.1
pages: 6-10
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
irred
We deﬁne
T 6d[M, K] = (Twisted compactiﬁcation of 6d (2,0) A1 theory on M
with a regular co-dimension two defect along K ⊂M) .
(2.6)
T 6d
irred[M, K] = (The low energy limit of T 6d[M, K]
on a particular point PSCFT on the moduli space of vacua) .
(2.7)
– 5 –
As a simpler set-up, we can also consider the case when the defect is absent. In that case, the
resulting 3d theory is denoted as T 6d[M] and T 6d
irred[M], respectively. For the T 6d
irred[M, K]
to be deﬁned, we assume that N = M\K is a hyperbolic knot complement.
The reason that we consider T 6d
irred[M, K] is as follows. The moduli space of vacua of
T 6d[M, K] in general contains several diﬀerent connected components. Then, we have to
decide which point of the moduli space we consider before taking the low energy limit. The
typical distances between diﬀerent components of the moduli space are of the order of the
compactiﬁcation scale on M, which set the cutoﬀscale of the low energy eﬀective 3d theory.
Therefore, we cannot expect that there is a single eﬀective 3d theory which describes the
entire moduli space of vacua. Only after specifying a point on the moduli space, we can
obtain a low energy eﬀective ﬁeld theory which describes the physics near that point.2
In other words, T 6d[M, K] is not a genuine 3d theory, but should be considered more
appropriately as the 6d theory compactiﬁed on M. However, we will be sometimes sloppy
and call it a 3d theory in this paper.
In T 6d
irred[M, K], we pick up a point and take the low energy limit. The low energy limit
may be described by a 3d SCFT (which can be empty or a topological theory). Below we
will specify which point on the moduli space of vacua we take, by using reduction to 5d
SYM.
T 6d on R2×S1 via 5d SYM
The structure of the moduli space of vacua becomes simpler
if we compactify the 3d spacetime to R2 ×S1. This is because we can use the 5 dimensional
maximally supersymmetric Yang-Mills (5d SYM) theory description. The set-up is3
6d N = (2, 0) on R2 × S1 × M

+
5d N = 2 SYM on R2 × M
/ theory T 6d[M] on R2 × S1
(2.8)
The bosonic components of the 5d SYM theory are gauge ﬁelds AI (I = 0, · · · , 4) and scalar
ﬁelds φk (k = 0, · · · , 4). After compactiﬁcation on M, the supersymmetry is deﬁned on R2,
and we split these ﬁelds as
(AI=0,1,2,3,4, φk=1,2,3,4,5) →(Aµ=0,1, φk=0,1) ⊕(Ai := Ai + iφi)i=2,3,4
(2.9)
From the point of view of the super-algebra on R2, the V = (Aµ=0,1, φk=0,1) is the vector
multiplet and Ai = Ai +iφi (i = 2, 3, 4) are twisted chiral ﬁelds. The reason that we regard
2 A simple example which illustrates the point is the T 2 compactiﬁcation of the 6d N = (2, 0) A1 theory
on T 2. The moduli space of this theory is [R5 × S1]/Z2, where S1 comes from the integral of the 2-form
ﬁeld on T 2. On the other hand, the moduli space of 4d N = 4 SYM is R6/Z2. Only after picking a point
on [R5 × S1]/Z2 and taking the low energy limit, the 6d N = (2, 0) theory on T 2 becomes the 4d N = 4
SYM. In this case the moduli space is connected, but still there is no single 4d eﬀective theory describing
the whole moduli space of vacua.
3On general grounds, one may only expect that 5d SYM describes the moduli space only in the limit
of very small radius of S1. However, somewhat miraculously, it is believed that 5d SYM describes even a
ﬁnite radius of S1.
– 6 –
A as twisted chiral ﬁelds rather than chiral ﬁelds is that the relation between 5d SYM and
T 6d[M] is a kind of mirror symmetry analogous to the case of 4d class S theories.
The twisted superpotential is given by complex Chern-Simons action as
f
WYM =
1
g2
YM
CS[A] :=
1
g2
YM
Z
M
1
2Tr

AdA + 2
3A3

.
(2.10)
where g2
YM is the gauge coupling of 5d SYM which is related to the radius R of S1 as
1
g2
YM
=
1
8π2R.
(2.11)
This is the results in [6–8] in the limit S2 →R2. This twisted superpotential corresponds
to the twisted superpotential obtained in DGG’s construction discussed in Sec. 2.2
The regular co-dimension two defect along a knot K ⊂M can be realized as coupling
the 3d T[SU(2)] theory [21] to the ﬁelds of 5d SYM [24–28].
The theory T[SU(2)] is
reviewed in Appendix B.1.
This is a 3d N = 4 SCFT given by U(1) vector multiplet
coupled two fundamental hypermultiplets (Ea, ˜Ea)a=1,2. The theory has su(2)H × su(2)C
ﬂavor symmetry and let
eµ := holomorphic moment map operator of su(2)C ,
eν := holomorphic moment map operator of su(2)H .
(2.12)
Then the twisted superpotential coupling of the T[SU(2)] and the 5d SYM is given by
f
WYM-defect =
Z
K
tr(eνA).
(2.13)
This means that we integrate the one-form tr(eνAi)dyi over K.4
We can also include (complexiﬁed) mass terms to the defect as
f
Wmass =
Z
K
ds tr(meµ)
(2.14)
where ds is the line element on K, and m is the mass. The mass of defect is related to the
eigenvalues of eν:
Eigenvalues of eν = {m, −m} .
(2.15)
See [28] for detailed explanations of the coupling of 5d SYM to T[SU(2)] in the context of
4d class S theories. The analysis there may be extended to the 3d/3d case, but we do not
perform a detailed analysis.
4 The gauge invariance is preserved as follows. The supersymmetry is considered in the two dimensional
space R2, and hence the direction along the knot K is considered as a kind of “internal manifold”. Let t be
the coordinate along K. Then, the kinetic term along this direction comes not from the Kahler potential,
but from the twisted superpotential as f
W ⊃˜E∂tE. This term combines with (2.13) to form a covariant
derivative ˜E(∂t + A)E, where we have used eµ ∼E ˜E (see Appendix B.1).
– 7 –
By solving F-term equations for the twisted superpotenal in (2.10) and (2.13), a part
of the moduli space of vacua5 on R2 × S1 with mass parameter m is given by
Mvacua(T 6d[M, K] on R2 × S1)
= {A : dA + A ∧A = eνδ(K), eigenvalues of eν = {m, −m}}/G .
(2.16)
where δ(K) is the delta function localized on K, and G is the group of PSL(2, C) gauge
transformations on M. This is the space of ﬂat connections of the complexiﬁeld gauge
group PSL(2, C) with the holonomy eeν around K.
ρhol(A) := (PSL(2, C) holonomy matrix along A-cycle) = eeν .
(2.17)
Notice that the eigenvalues of eeν are determined by the mass parameter m.
Now we can specify the point PSCFT on the moduli space of vacua which is taken in
the deﬁnition (2.7). First, let us consider more generally. For simplicity we assume that the
moduli space of vacua on R3, Mvacua(T 6d[M, K] on R3), is a discrete set. Let us take an
arbitary point P ∈Mvacua(T 6d[M, K] on R3 ). Then, if we compactify the theory on S1
with a radius which is large enough compared to potential barriers between diﬀerent points
on Mvacua(T 6d[M, K] on R3), then the point P goes to a subset M(P) of the moduli space
of vacua on R2 × S1 denoted as Mvacua(T 6d[M, K] on R2 × S1),
P →M(P) ⊂Mvacua(T 6d[M, K] on R2 × S1).
(2.18)
This M(P) need not be a single point, but may have several points whose number is related
to the Witten index of the 3d eﬀective theory on P. Because of the supersymmetry, the
condition that the radius of S1 is large may be dropped since there is no phase transition
under change of the radius.
The explicit forms of Mvacua(T 6d[M, K] on R3) and M(P) are not known and they are
deﬁned just by the abstract ﬁeld theoretical considerations as above. However, later we will
propose how M(PSCFT) may be given concretely in terms of ﬂat PSL(2, C) connections.
To consider a superconformal point, we set the mass m to be zero. Then the point
PSCFT is deﬁned as follows.
After compactiﬁcation on S1, the moduli space of vacua
of the theory on PSCFT becomes a subset M(PSCFT) of the moduli space of vacua on
R2 × S1.
Then, the point PSCFT is deﬁned by the condition that M(PSCFT) contains
the connection Ahyp ∈Mvacua(T 6d[M, K] on R2 × S1) which is determined by the unique
complete hyperbolic metric on N = M\K. More explicitly, using the spin-connection ω
and dreibein e of the complete hyperbolic metric, the ﬂat connection can be expressed as
Ahyp = ω −ie .
(2.19)
This ﬂat connection has the greatest value of Im(CS[Aα]) among all ﬂat connections Aα
with parabolic boundary holonomy and is conjectured to be the only vacua contributing
5When the connection A is reducible, we can turn on the expectation values of the vector multiplets
V = (Aµ=0,1, φk=0,1). These branches are very important in 4d class S theories [28, 29]. However, in the 3d
theories considered in this paper, we only consider points on the moduli space on which A is irreducible.
Therefore, we can neglect those branches.
– 8 –
to a squashed 3-sphere partition function [30] of T 6d
irred[M, K].
Refer to [13, 31–34] for
discussions on the conjecture from various respects, state-integral model of the complex
CS theory, holographic principal and resurgent analysis. To other physical quantities of
T 6d
irred[M, K] such as superconformal index, on the other hand, other ﬂat connections in
M(PSCFT) may contributes.
Now we give a conjecture about how M(PSCFT) is given concretely in terms of ﬂat
connections. First we consider the case where a knot K exists. For this purpose, we deﬁne
M(PSCFT) even for nonzero mass m by continuity from m = 0. Namely, M(PSCFT) is
just the set of vacua of the 3d eﬀective theory near PSCFT with mass m. We make the
dependence on m explicit by writing it as M(PSCFT, m). We also deﬁne χ(N) as
χ(N) =
[
m
{A : dA + A ∧A = eνδ(K), eigenvalues of eν = {m, −m}}/G
(2.20)
This means that we consider all ﬂat connections with varying holonomy around the knot.
Then we propose
[
m
M(PSCFT, m) = {the connected component of χ(N) containing Ahyp}
:= χ0(N) .
(2.21)
In [35], the component is called Dehn surgery component. Another way of representing the
above equation is M(PSCFT, m) = χ0(N) ∩{eigenvalues of ν = {m, −m}}.
Next, consider the case where there is no knot on M.
If the closed 3-manifold is
represented by a Dehn ﬁlling operation on a hyperbolic knot complement N = M\K for
some K along a boundary cycle A,
M = NA
(2.22)
we propose that the M(PSCFT) is given by
M(PSCFT) of the closed manifold M
= χ0(N) ∩{ρhol(A) = 1}
(2.23)
The deﬁnition of the right hand side contains a knot K, but we assume that it is independent
of the choice K ⊂M. Notice that ρhol(A) = 1 is stronger than m = 0, since we could have
a nonzero upper-right component of ν even if its eigenvalues are zero.
2.2
