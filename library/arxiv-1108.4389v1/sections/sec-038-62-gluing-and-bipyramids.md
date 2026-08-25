---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-038-62-gluing-and-bipyramids
section_title: "Gluing and bipyramids"
section_number: 6.2
pages: 48-50
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
In Section 3.3, we derived ST -invariance of the tetrahedron theory T1≃T ∆,ΠZ by starting
withN = 4 mirror symmetry, translating to N = 2 mirror symmetry for the XYZ model
and SQED with Nf = 1, and and then reducing further to the theories T1 and ST◦T 1 via
– 47 –
a mass deformation. It is somewhat instructive to now do the same at the level of partition
functions. In the process, we will see how gluing of partition functions should work.
Let’s begin with the partition function of a hypermultiplet, with (complex) vector twisted
mass denoted by x and axial twisted mass by y:
ZS3
b
( hypermultiplet ) = sb
(iQ
2 −x−y
)
sb
(iQ
2 +x−y
)
. (6.15)
TheN = 2 R-charge and axial charge are a linear combination of the Cartan generators of
the SU (2)H×SU (2)C R-charges of the N = 4 theory. We are using a convention where in
theN = 2 language the R-symmetry of chiral multiplets in the standard hypermultiplet is
absorbed in their axial twisted massy. Then the scalar ﬁeld in the vectormultiplet has “bare”
R-charge 2, and axial charge−2, i.e. complex twisted mass iQ− 2y. This is also required for
the basic superpotential coupling required by an N = 4 gauging.
Hence if we add a full N = 4 gauge multiplet to gauge the ﬂavor symmetry, the chiral
multiplet in it contributes a sb(2y−iQ/2). The partition function is
sb(2y−iQ/2)
∫
sb(iQ/2−x−y)sb(iQ/2 +x−y)e−2iπzxdx. (6.16)
The basicN = 4 mirror symmetry should match this to the partition function of a twisted
hypermultiplet, i.e. a hypermultiplet with the opposite axial charge [ 28]. The chiral ﬁelds in
a twisted hypermutliplet have “bare” R-charge 1 and axial charge −1, i.e. complex twisted
mass iQ
2 −y. Hence we should replace y with iQ
2 −y in (6.15) and write the basic N = 4
mirror symmetry relation as
sb(2y−iQ/2)
∫
sb(iQ/2−x−y)sb(iQ/2 +x−y)e−2iπzxdx =sb(y−z)sb(y +z) (6.17)
As a check, we are supposed to obtain either the partition functions of N = 2 SQED with
Nf = 1 ﬂavor or the partition function of the XYZ model by acting with S or with F on the
above relation. If we act with S, i.e. with the Fourier transform, we get
sb(2y−iQ/2)sb(iQ/2−x−y)sb(iQ/2 +x−y) =
∫
sb(y−z)sb(y +z)e−2iπzxdx. (6.18)
The left-hand side is the partition function of the XYZ model. The real masses of the three
chiral ﬁelds add to zero, and the R-charges to 2, as it should be to allow the superpotential
interactionW = µu˜u, cf. Section 3.3. Equation ( 6.18) happens to be another well known
identity for quantum dilogarithm functions [ 51, 52].
Now, if we redeﬁne x→ x−y, z→ z +y− iQ
2 , and take y to be large and positive
in ( 6.17), we replicate the mass deformation that reduces us to the theory T1 ≃ T∆,ΠZ.
Expression (6.17) becomes
∫
dxe−iπx
(
x+2(z−iQ
2 )
)
eb
(iQ
2 −x
)
=eb
(iQ
2 −z
)
, (6.19)
– 48 –
which is precisely ( 6.14), expressing the mirror symmetry σ◦T 1≃T 1.
We could also add Chern-Simons terms on both sides of ( 6.18) in order to reproduce the
exact partition function of the bipyramid theory, as discussed in Section 4.2. Namely, we ﬁnd
an identity
eiπ(iQ) ˜m3eb
(iQ
2 − ˜m1
)
eb
(iQ
2 − ˜m2
)
eb
(iQ
2 − ˜m3
)⏐⏐⏐
˜m3=iQ− ˜m1− ˜m2
(6.20)
=
∫
dσe−iπσ2−2πiσ
(
˜m2−iQ
2
)
eb
(iQ
2 +σ
)
eb
(iQ
2 −σ + ˜m1
)
The two sides correspond to the theories of three and two tetrahedra, respectively, both in the
equatorial polarization Πeq, with external edge positions X1 = 2πb ˜m1 andX2 = 2πb ˜m2. For
the left-hand side, the superpotential W =OC =φZφWφY (4.10) implements the constraint
˜m1 + ˜m2 + ˜m3 =iQ.
More generally, the rules for constructing theoriesTM,Π in Section 4 lead to the following
rules for calculating the corresponding ellipsoid partition functions:
1) Multiply together partition functions ZS3
b
(T∆i,Πi; ˜mZi) = eb
(iQ
2 − ˜mZi
)
, one for each
tetrahedron in the triangulation of M.
2) Act with Sp(2N, Z) in the Weil representation (i.e. by generalizing the quadratic expo-
nentials and Fourier transforms of ( 6.12)–(6.13)), to transform to the polarization ˜Π in
which all internal edges are “positions.”
3) Set the complex masses ˜mI now associated to internal edges equal to iQ.
We note that the specialization in Step 3 is the only consequence of adding a superpotential
W =∑
IOI to the theory TM,Π. Indeed, such a superpotential sets the real masses of the OI
to zero and the R-charges equal to 2. Otherwise, the ellipsoid partition function is completely
independent of superpotential terms, and cares only about gauge and matter content.
These rules for constructing ZS3
b
(TM,Π) are identical to the rules presented in [ 12] for
building the SL(2) Chern-Simons partition function of M. One can see even subtle quantum
eﬀects matching in the two descriptions. For example, in quantum Chern-Simons theory, the
classical internal edge constraintsCI = 2πi become corrected toCI = 2πi+ℏ, and this follows
immediately from the dictionary (6.5) between edge parameters and complexiﬁed masses ˜mI.
