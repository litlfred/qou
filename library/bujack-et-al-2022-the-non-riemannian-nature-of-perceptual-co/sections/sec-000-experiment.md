---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "The non-Riemannian nature of perceptual color space"
section_id: sec-000-experiment
section_title: "Experiment"
section_number: null
pages: 2-4
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
toc_source: inferred
---
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
2 of 10
https://doi.org/10.1073/pnas.2119753119
pnas.org
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
distributions of a crowdsourced color-naming experiment.
Yet, the principle of diminishing returns contradicts the pre-
vailing paradigm of a Riemannian color space. Assume that color
space is Riemannian and that γ is a geodesic between the colors
A = γ(t0) and C = γ(t2) containing the point B = γ(t1) with
t0 < t1 < t2. Then, the part of γ between A and B, γ1 = γ|t0,t1,
is a geodesic, as is the part between B and C.§ Therefore, the dis-
tances between the three points in a Riemannian setting coincide
with the lengths of the curve segments, and the contradiction with
the principle of diminishing returns, Eq. 4, follows immediately
from the additivity of integration boundaries via
Δ(A, C)
Eq. 3
=
 t2
t0
|γ′(t)|γ(t) dt
=
 t1
t0
|γ′(t)|γ(t) dt +
 t2
t1
|γ′(t)|γ(t) dt
Eq. 3
= Δ(A, B) + Δ(B, C).
[8]
In the remainder of this paper, we show that diminishing returns
do exist in human color perception, and we provide an estimate
of the shape through experiments on the neutral axis, which we
assume to be a geodesic. This, in turn, proves that the current
paradigm of Riemannian color space is incorrect.
Please note that it is sufficient to show one place in color space
where additivity is violated to prove that the whole space is not
Riemannian. We conduct our experiments on the neutral axis
because it is the location with the highest probability of being a
geodesic based on existing experiments and standards (36). We
do not rule out that there are loci somewhere in color space that
locally have a Riemannian structure, but the full 3D color space
itself is not Riemannian if the neutral axis is not.
Experiment
Ramsay (30) suggests that the principle of diminishing returns
or its opposite may have been spuriously identified by other
‡Hue superimportance refers to the phenomenon that an isoluminant circle centered at
gray has a circumference about π times its radius (8, 25). In our understanding of the
subject, hue superimportance can actually be modeled in a Riemannian space.
§If there was a shorter connection, γ′
1, connecting A and B, then replacing γ′
1 with γ1 in γ
would be shorter than γ, contradicting that it is a geodesic.
PNAS
2022
Vol. 119
No. 18
e2119753119
https://doi.org/10.1073/pnas.2119753119
3 of 10
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
researchers (daringly including his PhD advisor, Helm) because
of experimental procedures (successive intervals, paired compar-
isons) ill suited to the task. Indeed, open-ended and criterion-
dependent tasks give less accurate measures of similarity because
of individual factors (50) and the difficulty of the task (51). In
particular, humans are not good at judging questions of the type
“How big is the difference?” that form the basis for many large
difference experiments (31, 34, 35).
Instead, we use a more reliable two-alternative forced choice
(2AFC) task, where the participant simply answers the following
question: “Which is more different?” Specifically, we use a triad
arrangement of stimuli with the reference in the middle and one
test on either side. Each of 320 triads covering the neutral axis
was judged by at least 250 different participants in a crowdsourced
study on Amazon Mechanical Turk (MTurk) (52).¶
Because of its reliability, this task has been previously used to
