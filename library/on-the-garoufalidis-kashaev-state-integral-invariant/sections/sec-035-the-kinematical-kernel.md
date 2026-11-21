---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT"
section_id: sec-035-the-kinematical-kernel
section_title: "The Kinematical Kernel"
section_number: null
pages: 41-42
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
toc_source: outline
doc_brief: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT — 67 sections: Front matter; ACKNOWLEDGMENTS; ABSTRACT"
---
The Kinematical Kernel
The combinatorial coherence of the triangulation is enforced via the kinematical
kernel, which incorporates the gluing relations among face variables.
Local Kernel
For each tetrahedron T ∈X3, with vertices labeled 0 < 1 < 2 < 3, we define the
local kernel:
KT(x, z) := ⟨x0; zT⟩sgn(T) · δA(x0 −x1 + x2) · δA(x2 −x3 + zT),
(4.1)
where:
• xi ∈A are the state variables assigned to the faces opposite vertex i,
• sgn(T) ∈{±1} encodes the orientation of T,
• δA denotes the Dirac measure on A.
Global Kernel
The kinematical kernel aggregates these local constraints:
32
KX(y, z) :=
Z
AX2
δA(∂X)2(x|(∂X)2 −y) ·
Y
T∈X3
KT(x, z)dx.
(4.2)
The result is a kernel depending on both the internal gluings and the boundary
data.
