---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "The non-Riemannian nature of perceptual color space"
section_id: sec-003-limitations-and-mitigations
section_title: "Limitations and Mitigations"
section_number: null
pages: 6-8
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
toc_source: inferred
doc_brief: "The non-Riemannian nature of perceptual color space — 7 sections: Front matter; Experiment; Analysis"
---
There are two assumptions that we make throughout our work
that could limit the generality of our results. We discuss them here
and explain the design and verification choices that we made to
mitigate them.
Inﬂuence of the Background. The background can have a strong
influence on the way colors are perceived (63). We, therefore, keep
the background constant across all experiments.
The crispening effect causes colors in the vicinity of the back-
ground to appear more different from its neighbors than those
far away (64, 65). This effect could potentially interfere with the
measurement of diminishing returns. Sch¨onfelder’s law suggests
that the crispening effect is strongest at the exact location of the
background color (63). We chose the background to be dark blue,
approximately equivalent to that used by Krantz (54). By using a
hue, the background is not in the direct vicinity of any stimulus
presented, and the crispening effect is significantly reduced (62).
Still, even a small crispening effect could violate the assumption of
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Fig. 8.
Optimal diﬀerence scaling function f from Eq. 17 using the spline with
four control points. The shaded region indicates the middle 95% of all learned
models across test sets and bootstrapped training sets.
L∗being a reasonable proxy for a perceptual scale. We, therefore,
model the transform g from L∗to an actual perceptual scale
Ψ before estimating the effect of diminishing returns f. The
shape of our modeled g shows the expected compensation for
the crispening effect around the luminance of our background of
L∗= 20 (Fig. 7).
Apart from crispening, it has been observed that increments
in the lightness of the background can be perceived differently
than decrements (62, 66). To see if this effect could potentially
explain the measured nonadditivity, we performed experiments
around five different centers on the neutral axis, some closer and
Fig. 9.
Optimal diﬀerence scaling functions using the hypothesized func-
tions. The shaded region indicates the middle 95% of all learned models
across test sets and bootstrapped training sets.
some farther from the background and some involving stimuli
exclusively brighter than the background (L∗= 50, 60, 70).
We compared the increase in predictive power due to account-
ing for the size of the differences using the scaling function across
each center individually. At each center, there was a significant
increase in predictive power when using both the g and f trans-
formations compared with using only g alone, as seen in Fig. 6.
While there is less of an increase at the centers with increments
only (L∗= 50, 60, 70), the increase remains significant. This leads
us to the conclusion that the effect of diminishing returns is robust
to some degree against the influence of the background.
The Neutral Axis as a Geodesic. It is not trivial to verify whether
any given path through color space is a geodesic. We chose the
neutral axis because it is the one path on which all available data
agree that it is indeed a geodesic. For example, the neutral axis
is a geodesic in the commonly used color space CIE L*A*B* for
its 1976, 1994, and 2000 metrics. It is also a geodesic in the
Euclidean color spaces CIE CAM, CIE RGB, CIE XYZ, CIE
LUV, DIN99, Adobe RGB, and sRGB, where it is always a straight
line (the interested reader is directed to ref. 37 for a discussion of
the various color spaces). It is also a geodesic in the Euclidean
spaces CIE CAM, CIE RGB, CIE XYZ, CIE LUV, DIN99,
Adobe RGB, and sRGB, where it is always a straight line. It is
also a geodesic in Schr¨odinger’s theory of luminance, hue, and
saturation, in which he expects that paths of constant ratios of the
primaries form geodesics (7), and the theory that paths of constant
hue and saturation that differ only in luminance form geodesics,
even though these two theories do not generally agree everywhere
in color space because of the Bezold–Br¨ucke effect (1). Still, we
acknowledge that there is no guarantee that the neutral axis is
indeed perceived as a geodesic in our experiment. It is possible, for
example, that the background could change the path of a geodesic.
Our findings rely on these theories and models to hold at least
approximately.
Since the measured effect of diminishing returns was signifi-
cant, we expect a small deviation from a geodesic not to invalidate
our overall findings. The following Gedankenexperiment provides
a coarse estimate of how far from neutral the perception of the
grays would have to be so that the measured effect could be
explained through the triangle inequality instead of through di-
minishing returns. To this end, we chose one example of measured
perceived distances from our experiments. These three gray stimuli
are spaced with ΔL∗of 15, for which we measured perceived
distances of 1.36. For the ΔL∗distance of 30 between the two
outer stimuli, we measured a perceived distance of 2.06 (compare
with Fig. 8). Now, assume that this effect would be produced
because they do not lie on a geodesic but on an actual triangle.
The sides of the triangle depicted here (△) have the same ratio as
these measured perceived distances. We find a perturbation of the
perception of the neutral axis of this magnitude hard to imagine.
Example
To illustrate that the impact of changing from an additive to a
nonadditive metric can be significant, we use the simple example
of computing the mean of a black-and-white photograph. In a
non-Euclidean setting, the mean cannot be computed by adding
the values. Z´era¨ı and Triki (15) suggest the use of the intrinsic
mean ¯x ∈M of a set of points xi ∈M in a manifold M,
¯x = argminx∈M
n

i=1
ΔE(x, xi)2,
[19]
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Fig. 10.
Photograph of Bernhard Riemann used to illustrate the impact of
the non-Riemannianness for the computation of the intrinsic mean.
in the context of image quality measures in non-Euclidean color
spaces. Even though their work is intended for Riemannian spaces,
this formula does not require the assumption of additivity and
trivially generalizes to general metric spaces. We compute the
intrinsic mean of the photograph of Bernhard Riemann shown in
Fig. 10. The additive distance ΔL results in a mean of ¯xΔL = 42,
while the nonadditive formula generated by the highest likelihood
logarithmic curve from Eq. 18 with the parameters a = 5.34, b =
2.34 (Fig. 9) results in ¯xflog = 54.
