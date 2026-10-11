---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "The non-Riemannian nature of perceptual color space"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
toc_source: inferred
---
RESEARCH ARTICLE
PSYCHOLOGICAL AND COGNITIVE SCIENCEMS
The non-Riemannian nature of perceptual color space
Roxana Bujacka,1
, Emily Tetia,b, Jonah Millera, Elektra Caﬀreya,c, and Terece L. Turtona
Edited by Brian Wandell, Stanford University, Stanford, CA; received October 28, 2021; accepted March 13, 2022
The scientific community generally agrees on the theory, introduced by Riemann and
furthered by Helmholtz and Schr¨odinger, that perceived color space is not Euclidean
but rather, a three-dimensional Riemannian space. We show that the principle of
diminishing returns applies to human color perception. This means that large color
differences cannot be derived by adding a series of small steps, and therefore, perceptual
color space cannot be described by a Riemannian geometry. This finding is inconsistent
with the current approaches to modeling perceptual color space. Therefore, the assumed
shape of color space requires a paradigm shift. Consequences of this apply to color
metrics that are currently used in image and video processing, color mapping, and the
paint and textile industries. These metrics are valid only for small differences. Rethinking
them outside of a Riemannian setting could provide a path to extending them to large
differences. This finding further hints at the existence of a second-order Weber–Fechner
law describing perceived differences.
color space | Riemann | cognition | metric | diminishing returns
Color spaces are specific organizations of colors. Since humans have three cones to perceive
color, color spaces are usually three-dimensional (3D). Color spaces can be directly
related to the three cones: red, green, and blue, such as CIE RGB. However, most color
spaces are mathematical constructs or models, such as CIE XYZ and CIE L*A*B*, with
transformation formulas* converting one to another (1). Apart from assigning a unique
coordinate to each color and arranging them in a sensible way, perceptual color spaces
arrange colors in a way that the distance between two colors reflects how differently
humans perceive them.
Background and Theory
We show how the principle of diminishing returns contradicts the paradigm of a
Riemannian color space, illustrated in Figs. 1 and 2. The key idea is that for a space to
be Riemannian, distances ΔE between stimuli A, B, C along a geodesic must satisfy
additivity: that is,
ΔE(A, B) + ΔE(B, C) = ΔE(A, C),
[1]
while diminishing returns require the strict inequality of this relation (Eq. 4).
Riemannian Geometry and Color. In his visionary lecture where he introduced a geome-
try that generalizes the notions of angle, curvature, and length to curved spaces, Riemann
(2) himself suggested that color forms a multidimensional manifold. This was probably
the largest step toward mathematical modeling of color since its description by means
of a vector space by Grassmann (3), which was rigorously formalized by Krantz (4). A
Riemannian manifold is a smooth manifold M with a metric g smoothly varying over M
that defines an inner product on the tangent space at point p ∈M . For a fixed basis in 3D,
we can express the metric at each point p as a matrix gp ∈R3×3 and the inner product of
two vectors u, v ∈R3 at p as
< u, v >p= uTgpv.
[2]
In this setting, the length of a curve γ : [t0, t1] ⊂R →M ,
L(γ) =
 t1
t0
|γ′(t)|γ(t) dt =
 t1
t0
dγ(t)
dt
, dγ(t)
dt

γ(t)
dt,
[3]
will be of central importance. The path between two points A, B that minimizes the
length is called a geodesic, and its length is the distance Δ(A, B) between these two
points, illustrated in Fig. 2.
*The transformation sometimes depends on additional parameters: for example, the white point.
Significance
For over 100 y, the scientiﬁc
community has adhered to a
paradigm, introduced by Riemann
and furthered by Helmholtz and
Schrodinger, where perceptual
color space is a three-dimensional
Riemannian space. This implies
that the distance between two
colors is the length of the shortest
path that connects them. We
show that a Riemannian metric
overestimates the perception of
large color diﬀerences because
large color diﬀerences are
perceived as less than the sum of
small diﬀerences. This eﬀect,
called diminishing returns, cannot
exist in a Riemannian geometry.
Consequently, we need to adapt
how we model color diﬀerences,
as the current standard, ΔE,
recognized by the International
Commission for Weights and
Measures, does not account for
diminishing returns in color
diﬀerence perception.
Author aﬃliations: aComputer, Computational, and Sta-
tistical Sciences Division, Los Alamos National Labora-
tory, Los Alamos, NM 87545; bDepartment of Psychology,
Florida Atlantic University, Boca Raton, FL 33431; and
cDepartment of Computer Science, University of New
Mexico, Albuquerque, NM 87106
Author contributions: R.B. designed research; E.C. and
T.L.T. performed research; E.T. analyzed data; J.M. pro-
vided mathematical theory; E.C. provided assistance with
experiments; and R.B., E.T., J.M., and T.L.T. wrote the
paper.
The authors declare no competing interest.
This article is a PNAS Direct Submission.
Copyright © 2022 the Author(s). Published by PNAS.
This
article
is
distributed
under
Creative Commons
Attribution-NonCommercial-NoDerivatives
License
4.0
(CC BY-NC-ND).
1To whom correspondence may be addressed. Email:
bujack@lanl.gov.
Published April 29, 2022.
PNAS
2022
Vol. 119
No. 18
e2119753119
https://doi.org/10.1073/pnas.2119753119
1 of 10
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Fig. 1.
Diminishing returns imply that large color diﬀerences appear less
than the sum of their parts. This image is a purely ﬁgurative illustration of how
this phenomenon could potentially occur, even though this speciﬁc geometry
is not suggested in this paper. If an isoluminant plane through color space
(Upper) would, for example, have the shape of a curved two-dimensional
submanifold embedded in a 3D space (Lower), then the 3D Euclidean metric
would produce the inequality of diminishing returns.
von Helmholtz (5) was the first to describe the distance between
colors by means of a line element† in a Riemannian manifold. He
defines the shortest path in a color space to be the path for which
the sum of its just noticeable differences is minimal. He bases his
line element on the Weber–Fechner law (6).
Schr¨odinger (7) also assumes that color perception is Rie-
mannian, but Schr¨odinger (7) strictly rejects Helmholtz’s line
element because it produces surfaces of isoluminance that are not
orthogonal to the direction of intensity increase and suggests an
alternative one.
These works are based primarily on geometry and mathematical
