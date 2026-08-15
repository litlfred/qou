---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE CHUL-HEE LEE"
section_id: sec-003-22-two-models-of-hyperbolic-plane
section_title: "Two models of hyperbolic plane"
section_number: 2.2
pages: 5-6
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE CHUL-HEE LEE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
of the hyperbolic plane. One such model is the upper half-plane, denoted by H. This
consists of complex numbers z where the imaginary part is positive: H ={z∈ C :
Im(z)> 0}. This model of the hyperbolic plane carries a metric:
ds2 = dx2 +dy2
y2 ,
which yields a constant Gaussian curvature −1. The distance dH(z,z′) between two
points z and z′ is given by
coshdH(z,z′) = 1 + |z−z′|2
2 Imz Imz′.
Geodesics in H are represented as either vertical half-lines or semicircles that intersect
thex-axis perpendicularly. For any two distinct points in H, there is a unique geodesic
connecting them. The Laplacian is given by
−∆ =y2
 ∂2
∂x2 + ∂2
∂y2

.
The group PSL2(R) = SL2(R)/{±1} acts isometrically on H. The action is given by
z7→gz = az+b
cz+d, where g =±

a b
c d

∈ PSL2(R). A non-trivial element g of PSL2(R)
is called hyperbolic if | tr(g)|> 2. This is equivalent to g fixing two distinct points on
the boundary ∂H of the upper half-plane. The length ℓ(g) of a hyperbolic element g is
defined as:
ℓ(g) = 2 arcosh
| tr(g)|
2

.
6 CHUL-HEE LEE
The unit disk D provides another model for the hyperbolic plane. It is defined by
D ={z∈ C :|z|< 1}. In this model, the metric is expressed as:
ds2 = 4(dx2 +dy2)
(1−x2−y2)2
which results in a constant Gaussian curvature −1. An isometry that maps H onto D
is given by:
z7→ z−i
z +i,
which is also a conformal equivalence. The distance, denoted as dD(z,z′), between two
points z and z′ in the disk is
coshdD(z,z′) = 1 + 2|z−w|2
(1−|z|2)(1−|w|2).
The Laplacian in this setting reads
−∆ = (1−x2−y2)2
4
 ∂2
∂x2 + ∂2
∂y2

.
The group of orientation-preserving isometries of D is given by the group
PSU(1, 1) =

±

a b
b a

:a,b∈ C,|a|2−|b|2 = 1

.
The notion of hyperbolic elements for PSU(1 , 1) and their lengths can be defined in
the same way.
