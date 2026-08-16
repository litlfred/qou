---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-033-52-the-bipyramid
section_title: "The bipyramid"
section_number: 5.2
pages: 44-46
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
To ﬁnd the moduli space for the bipyramid theory, let us work in the equatorial polarization
Πeq, as discussed in Section 2 and Section 4.2. We closely follow the notation in those
sections. We can start with the decomposition into two tetrahedra, and use the Lagrangian
description ( 4.14) of TM,Πeq as Nf = 1 SQED, with a shift V → V −VX1/2, to obtain a
twisted superpotential
~W(X1,X 2;σ) = Li2(eσ) + Li2(e−σ+X1) + 1
2σ2 + (X2−iπ)σ. (5.18)
Here we have extended the symplectic transformation ( 4.12) with an aﬃne shift by −iπ for
the twisted mass X2. By requiring ∂~W/∂σ = 0 (because σ is the vev of a dynamical ﬁeld),
and setting P1 =∂~W/∂X1 and ∂~W/∂X2, it is straightforward to derive the moduli space
M(param)
SUSY (TM,Πeq) : p1 + p2
x1
− 1 = 0, p 2 + p1
x2
− 1 = 0. (5.19)
– 43 –
This is the same as the Lagrangian LM appearing in ( 2.23). An easier way to derive ( 5.19)
would be to begin with the product of moduli spaces for two tetrahedra
r′′ +r−1− 1 = 0, s ′ +s′′−1− 1 = 0, (5.20)
and simply apply the aﬃne Sp(4, Z) transformation r→ x1
p2
, r′′→p1, s2→p2, s1→− p1
x2p2
.
Equivalently, we can take the decomposition of the bipyramid into three tetrahedra, and
the corresponding XYZ model. The twisted superpotential corresponding to the Lagrangian
(4.11) is
~Weﬀ(X1,X 2,C ) = Li2(e−X1) + Li2(e−X2) + Li2(eC−X1−X2) +iπ(X1 +X2−C). (5.21)
Note that, according to the shifts in the symplectic transformation (4.7), we have turned on a
half-integral theta angle for the combination Σ X1 + ΣX2− ΣC. Setting P1 =∂~W/∂X1, P2 =
∂~W/∂X2, Γ =∂~W/∂C and exponentiating, we ﬁnd equations
γp1 + 1
x1
− 1 = 0, γp 2 + 1
x2
− 1 = 0, −γx1x2
c + x1x2
c − 1 = 0. (5.22)
Now, however, the (ordinary) cubic superpotential of the XYZ model tells us that we must
set the twisted mass C = 0 (modulo 2 πi), or c = eC = 1. By appending this to equations
(5.22) and eliminating γ, we then obtain
(x1− 1)
(
p1 + p2
x1
− 1
)
= 0, (x2− 1)
(
p2 + p1
x2
− 1
)
= 0. (5.23)
These are equivalent to (5.19) as long asx1⁄= 1 andx2⁄= 1. We recall, however, thatx1,2 = 1
(or X1,2 = 0) are precisely the analogues of the singular points in moduli space discussed
below ( 5.8). There, either supersymmetry is broken or new Higgs branches of dynamical
vacua open up. Away from this singular locus, equations ( 5.23) reduce to ( 5.19).
6. S3
b partition functions
In the previous section, the correspondence (M, Π) ↔ TM,Π was tested by comparing moduli
spaces attached to each side of the correspondence. A more reﬁned test could be obtained
by associating certain functions to each side. For example, on the gauge theory side one can
associate either an equivariant partition function or an index (an analog of the elliptic genus)
to the 3dN = 2 theory TM, by analogy with what was done in [ 3] or [41, 42] in the context
of 4dN = 2 gauge theory. Then, these functions are expected to match the corresponding
topological invariants of M.
In this section, we discuss one such test based on comparing the partition function of
the 3d N = 2 theory TM,Π on a squashed three-sphere (or “ellipsoid”) S3
b with the SL(2)
Chern-Simons partition function of the 3-manifold M:
ZSL(2)
CS (M) = ZS3
b
(TM,Π), (6.1)
– 44 –
where the squashing parameter b is related to the Chern-Simons coupling coupling strength
ℏ as
ℏ = 2πib2. (6.2)
This relation is a direct generalization of the AGT correspondence [ 3] to three dimensions.
In fact, it is fully consistent with the AGT correspondence, which corresponds to taking
M = R×C to be a product of the “time” direction and a Riemann surface C (possibly with
punctures), through a somewhat lengthy chain of correspondences [ 43], [35], reviewed e.g. in
[44]
Various aspects of partition functions in SL(2) Chern-Simons theory are discussed in
[8, 9, 45, 12]. Given a 3-manifold M with boundary phase space P∂M , as deﬁned here in
Section 2, Chern-Simons theory should promote P∂M to a Hilbert space
P∂M ↝ H∂M , (6.3)
and the partition function ZSL(2)
CS (M) can be thought of as a distinguished wavefunction
inH∂M . In particular, ZSL(2)
CS (M;X1,X 2,... ) is a function of half the coordinates on P∂M ,
the “positions” in a given polarization Π. An aﬃne Sp(2N, Z) change of polarization acts
on ZSL(2)
CS (M;X1,X 2,... ) in the standard Weil representation [ 46, 47]; for example, S-type
elements act as Fourier transform, and T -type elements act as multiplication by quadratic
exponentials∼ exp X2
i
2ℏ .
Similarly, theS3
b partition function ofTM,Π depends on the twisted massesmO of various
chiral operators that transform underU(1) ﬂavor symmetries. These real masses are naturally
complexiﬁed by the R-charge, due to the background curvature of the ellipsoid [48, 5]. Indeed,
if we describe S3
b geometrically as
b2|z1|2 +b−2|z2|2 = 1, z 1,z 2∈C , (6.4)
then ZS3
b
(TM,Π) depends holomorphically on the combinations ˜ mO ≡ mO + iQ
