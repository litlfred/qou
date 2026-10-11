---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "The non-Riemannian nature of perceptual color space"
section_id: sec-003-limitations-and-mitigations
section_title: "Limitations and Mitigations"
section_number: null
pages: 6-7
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
toc_source: inferred
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
6 of 10
https://doi.org/10.1073/pnas.2119753119
pnas.org
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
