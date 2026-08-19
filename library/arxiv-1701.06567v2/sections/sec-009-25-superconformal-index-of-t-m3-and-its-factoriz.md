---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-009-25-superconformal-index-of-t-m3-and-its-factoriz
section_title: "Superconformal index of T [M3] and its factorization"
section_number: 2.5
pages: 18-19
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Although the new invariantsˆZa(q) and their categoriﬁcationHa[M3] have a direct connection
to the WRT invariant via (2.6), from the viewpoint of 3dN = 2 theoryT [M3;SU (2)], it is not
the most natural or simplest object to consider. The main reason is that, in principle, there
are inﬁnitely many possible boundary conditions that could be considered. 18 Identifying the
correct subset that appears in ( 2.16) may be subtle, yet possible, as we shall see in concrete
examples.
The more natural object is the superconformal index of T [M3] or, equivalently, the par-
tition function on S2×S1 with a certain supersymmetry preserving background:
I(q) ≡ TrHS2(−1)FqR/2+J3 = ZT [M3](S2×qS1) (2.31)
16A framed gauged transformation acts trivially at a chosen point on M3.
17A closely related U(1)-equivariant rather than G-equivariant regularization of complex Chern-Simons
partition function was used [54] for 3-manifolds of the form M3 = S1× Σ. As expected, this equivariant
localization does help to see contributions of both abelian and non-abelian ﬂat connections in the same partition
function.
18If we understand the boundary condition as a coupling of the 3d theory to a 2d theory living on the
boundary, then the inﬁnite number of possibilities can be seen, for example, from the fact that we can always
introduce a 2d theory decoupled from the bulk.
– 17 –
whereHS2 is the space of BPS states of 3dN = 2 SCFTT [M3] or, equivalently,Q-cohomology
of all physical local operators, F is the fermion number, R is the generator of the U(1)R R-
symmetry and J3 is the Cartan generator of the SO(3) isometry of S2. By construction, this
index has the desired integrality property 19 and can be categoriﬁed,
HS2 =
⨁
i,j
Hi,j
S2, I(q) =
∑
i,j∈Z
qi(−1)j dimHi,j
S2 ∈ Z[[q]]. (2.32)
Another advantage ofHS2 compared toHD2 is that it has a natural ring structure which is
given by multiplication of BPS operators. One of the statements of 3d/3d correspondence
is that the partition function ZT [M3](S2×q S1) computes the partition function of complex
Chern-Simons onM3 with real part of the “level” being 0 and analytically continued imaginary
part∝ τ ≡ logq/(2πi). Motivated by the topological/anti-topological fusion [23] and its
recent 3d incarnation [24–26,55], we would like to make the following conjecture:
Conjecture 2.2 For ˆZa(q) as in Conjecture 2.1, the following holds
I(q) =
∑
a∈ TorH1(M3,Z)/Z2
|Wa|ˆZa(q)ˆZa(q−1) ∈ Z[[q]] (2.33)
where ˆZa(1/q) is an apropriate extension 20 of ˆZa(q) to the region|q|> 1.
