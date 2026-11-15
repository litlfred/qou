---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "The non-Riemannian nature of perceptual color space"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
toc_source: inferred
doc_brief: "The non-Riemannian nature of perceptual color space — 7 sections: Front matter; Experiment; Analysis"
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
reasoning and only partly on experiment. However, experimental
evidence against a Euclidean color space was found, for example,
in the Nickerson index of fading (8). Since then, many authors
have argued that color perception is not Euclidean but rather,
Fig. 2.
Geodesics (shortest paths computed with the shooting method)
between the corners of the sRGB cube in CIE LAB with its non-Euclidean metric
ΔE∗
2000 (79) illustrate what has long been known for perceptual color spaces
in general, namely that in contrast to a Euclidean setting (e.g., ΔE∗
1976), the
geodesics do not form straight lines. In this paper, we go one step further
and show what CIE LAB does not capture: that in contrast to a Riemannian
setting, their lengths do not even coincide with the distances between their
endpoints.
†The concept line element, ds2 = g, is preferred in the literature over the concept of metric,
but they can be used interchangeably because each determines the other.
Riemannian (9–16), with experiments undertaken to determine
coefficients of a Riemannian metric describing the perceived
differences of colors (11, 17–21).
Lastly, the interested reader should review Wyszecki and Stiles
(1) for an introduction to color theory, Resnikoff (22) for an
excellent summary of the historical development of the idea of
color space, and Vos (23, 24) for superb visualizations of the
different line elements of color perception and a historical account
on their development.
The Principle of Diminishing Returns. The principle of dimin-
ishing returns in color refers to the phenomenon that large color
differences are underestimated by human perception, as shown in
Fig. 1. Even if a color B lies on the shortest path between A and
C, the sum of the perceived lengths of the two segments exceeds
the total perceived length:
ΔE(A, B) + ΔE(B, C) > ΔE(A, C).
[4]
Importantly, Eq. 4 holds even along geodesics, making it distinct
from and stronger than the triangle inequality. The term “dimin-
ishing returns” was coined by Judd (13). He defines the concept
of an ideal color space as “a tridimensional array of points, each
representing a color, so located that the length of the straight
line between any two points is proportional to the perceived
size of the difference” (25). In his papers, he collects evidence
from the literature that such an ideal color space cannot exist
[e.g., referring to the experiments of Nickerson and Stultz (8)
and MacAdam (20)]. The latter describes an experiment in which
observers judged the perceived distances between neighboring
colors in three concentric, equiluminous hexagons of different
sizes in CIE xyY. He then determined the coefficients, H1, gij ,
p ∈R, i, j ∈{1, 2}, of the weighted adaptation to a Riemannian
distance formula
¯H = H1(g11(Δx)2 + 2g12ΔxΔy + g22(Δy)2)
p
2
[5]
to best fit these perceived differences. He found that the exponent
p, which makes the formula non-Riemanninan if p̸ = 1, is gener-
ally smaller than 1, indicating diminishing returns.
At approximately the same time, Helm (26) conducted ex-
periments in which the observer estimated color distances and
ratios between colors of constant luminance and saturation while
varying hue. He then used multidimensional scaling (MDS) to
estimate the dimensionality of the underlying space (27). For the
ratio experiments, the result revealed a two-dimensional circle, but
for the distances, the dimensionality was 12. Helm (26) argued
that this was the consequence of the underestimation of large
distances. A logarithmic transformation of the distances in CIE
xyY resulted in the expected dimensionality of two and a strong
correlation to the outcome of the ratio experiments. In the context
of contrast constancy across frequencies of sinusoidal gratings,
Cannon (28) studied the relation between physical and perceived
contrast, with contrast defined as
(Lmax −Lmin)/(Lmax + Lmin),
[6]
where L is physical luminance. In suprathreshold conditions, he
found a power law with an exponent of ∼0.5 to be a good fit,
similar to the results of MacAdam (20). Despite these findings, the
topic remains controversial. Using MDS, many researchers have
found good agreement between color difference experiments and
an additive 3D Euclidean space (29–33). Exceptions are Ekman
(34), Helm (26), and Izmailov and Sokolov (35). The lattermost
found that color space can be embedded into a 3D spherical
submanifold of a four-dimensional Euclidean space in analogy to
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Fig. 3.
Thurstonian distance perception (58) of a triad modeled with (solid)
and without (dashed) additivity with an example scaling function f(Δψ) =
√Δψ. If additivity is assumed and the gray-shaded Gaussians are appropri-
ately centered, the diﬀerence between the means can be subtracted to give
the perceived diﬀerence between the standard and either test (shown as the
shaded green and orange triads). The diﬀerence between these means would
be the perceived diﬀerence of diﬀerences, which can be plotted on a Gaussian
centered at zero, as shown in Lower, to predict how often participants would
be incorrect. However, if diminishing returns should exist, the means of
the green and orange Gaussians should be scaled as demonstrated by the
dashed distributions in the second row. The eﬀect of the scaling function is
an increased rate of predicted incorrect responses by more than an order of
magnitude.
the setting in Fig. 3. They argue that the Euclidean distances CAB
between colors A and B in their high-dimensional embedding
spaces provide the perceived differences and are related to the
arclengths DAB of the geodesics on the manifolds via
CAB = 2 sin(DAB/2).
[7]
They explicitly note the principle of diminishing returns: “that
the integral of just noticeable differences between colors does
not coincide with direct estimations of the subjective differences
between the colors” (35).
Currently, there is no officially recognized color space that
models the lack of additivity resulting from diminishing returns
(36, 37). Summarizing existing literature, there is experimen-
tal evidence for diminishing returns (20, 26, 28, 35, 38, 39),
anecdotal evidence for the opposite [i.e., large color differences
are overestimated ΔE(A, B) + ΔE(B, C) < ΔE(A, C)] (40),
and an overwhelming number of papers arguing against both
(i.e., small differences add up to large ones along the shortest
path) (Eq. 1) (29–33, 40–43). Proponents of diminishing returns
suggest three forms; Helm (26) assumes a logarithmic function,
MacAdam (20) assumes a polynomial function, and Izmailov and
Sokolov (35) assume a sinusoidal function between just noticeable
and large perceived color differences.
The Contradiction between Diminishing Returns and the
Paradigm of Riemannian Color Space. The principle of dim-
inishing returns has long served as an argument against the
existence of a Euclidean color space that models perceived color
differences (13, 25, 44, 45). So far, however, it has not been used as
an argument to reject a Riemannian color space. A possible reason
might be that the idea of Riemannian geometry is thought of as
the union of all geometries, including straight and curved spaces,
instead of a specific geometry satisfying rigid axioms. However,
we know with certainty that MacAdam (14) was aware of the
possibility of color space not being Riemannian. He describes
that the principle of hue superimportance‡ as captured in the
Nickerson index of fading (8) is in violation of Riemannian
geometry in his work on Judd in 1979 (14). Most fascinatingly,
MacAdam (14) summarizes that “there was no strong evidence
that those conditions for representation by a Riemannian (non-
Euclidean) space are violated,” which indicates that his own
findings from 1963 about diminishing returns (20) seem not
to evoke skepticism of color space being Riemannian.
While arguments against a Euclidean color space are ubiquitous
(8, 13, 25, 46) [e.g., Ennis and Zaidi (47) find that color per-
ception is approximately an affine space], there are few instances
in the literature that question the Riemannian nature of color
space. Exceptions are Zeyen et al. (48), who suggest an interpo-
lation algorithm for color maps that works in non-Riemannian
geometry, and Griffin and Mylonas (49), who express doubt when
they develop a Riemannian categorical metric from the probability
