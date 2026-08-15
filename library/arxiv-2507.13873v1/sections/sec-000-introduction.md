---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography Andreas Belaey,∗ Thomas G. Mertens,† Jacopo Papalini,‡"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-4
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
doc_brief: "Probing the singularity at the holographic screen via q-holography Andreas Belaey,∗ Thomas G. Mertens,† Jacopo Papalini,‡ — We study the emergence ofq-deformed spacetime in a lower-dimensional"
---
2 Correlation functions on the quantum disk 3
2.1 q-Correlation functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Quantum hyperbolic disk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 A candidate bulk description for q-holography 10
3.1 Definition and classical structure of sinh dilaton gravity . . . . . . . . . . . . 11
3.2 Probe regime of sinh dilaton gravity . . . . . . . . . . . . . . . . . . . . . . . 14
4 Concluding remarks 20
A Corepresentations of (quasi)-primary operators 23
B Dilaton gravity models 27
B.1 Holographic counterterm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
B.2 Sinh dilaton gravity quantization . . . . . . . . . . . . . . . . . . . . . . . . 30
C Useful manipulations involving Ramanujan’s formula 33
1 Introduction
Going beyond the conventional AdS/CFT paradigm [1] is of considerable interest; primarily
because we do not live in an AdS universe, but also because it allows us to distill lessons
on holography in the more general context. Within the context of holography and string
theory, some important examples have been e.g. [2, 3, 4, 5]. To achieve further progress
towards this goal, especially when aiming for quantized gravity, exactly solvable models
serve as powerful benchmarks. In this light, lower-dimensional dilaton gravity models have
attracted significant attention in the past years. This was sparked by studies on Jackiw-
Teitelboim (JT) gravity [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], its direct relation
with microscopic SYK models [19, 20], its lessons on spacetime wormhole physics [21], and
its universality for describing the black hole throat for a near-extremal higher-dimensional
black hole (see e.g. [22, 23]). JT gravity is but one example of a solvable 2d dilaton gravity
model. Indeed, the 2d sinh dilaton gravity model was discovered to be structurally very
promising as well, since it is merely the old Liouville gravity models after a field redefinition
[24, 25, 26, 27, 28, 29]. Relatedly, within the double-scaling regime of the original SYK
1
model [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
52, 53, 54, 55, 56, 57, 58], the sine dilaton gravity model has been proposed to describe a
holographic dual in [59, 60, 61].1 Both of these models have in common that the holographic
boundary is not of the conventional asymptotic AdS type. In fact, for sinh dilaton gravity,
one readily shows (as we will review later on), that the Ricci scalar of the bulk geometry
actually blows up at the holographic screen!
The fact that this model has a curvature singularity exactly where one wants to position
the holographic screen presents us simultaneously with a puzzle and an opportunity. The
puzzle here is that the holographic boundary is usually at a location in spacetime where
gravitational fluctuations are negligible. However, a classical curvature singularity does not
seem like a stable anchoring region where one can trust classical gravity. From this, one can
expect that there can be a difference between on the one hand the near-boundary limit of
the model, and on the other hand the semi-classicalℏ→ 0 limit where we turn off gravity
quantum fluctuations. In ordinary AdS/CFT, these two regimes give the same answer close
to the boundary. But here we will have to be more careful, see Fig. 1 for a visualization of
the general puzzle studied in this work.
?
Figure 1: Left: Visualization of quantum gravitational fluctuations being suppressed close to the
holographic boundary in an AdS box. Right: Fluctuations are not obviously suppressed for the
case where the near-boundary region contains a classical curvature divergence.
It is of considerable interest currently to have a better understanding of quantum gravity
inthecasewherewedo not haveaboundarywheregravitationalfluctuationsaresuppressed,
such as happens in cosmological models along the lines of [64, 65, 66] and [67, 68, 69, 70].
Hence, one can view our current investigation as following a similar goal.
Generically, studying singularities in quantum gravity is hard, since the cosmic cen-
sorship hypothesis teaches us that they are classically hidden behind black hole horizons.
1Sine dilaton gravity has been defined and studied in [62] in a different quantization scheme, leading to
a continuum model instead which was utilized as a toy model for cosmology in [63].
2
Piercing through the horizon in quantum gravity is very difficult to do in a controlled envi-
ronment, with only a handful of (important!) examples [71, 72, 73, 74]. Since the singularity
here is not cloaked behind a horizon, we have the opportunity to learn more on how the
quantum dilaton gravity model at hand deals with it. This work can be viewed as a first
characterization of this singularity.
We will characterize the near-boundary behavior of sinh dilaton gravity in terms of non-
commutative geometry based on the quantum hyperbolic disk, which is aq-deformation of
the ordinary hyperbolic disk. To that end, we will in this work first investigate precisely
what we would expect from aq-deformation of the holographic dictionary by solving the
q-Ward identities, building upon earlier work [75, 76, 49] and extending to our range ofq.
Afterwards, we return to the specific dilaton gravity model at hand and match it to our
general predictions. Investigatingq-holography is an important goal in its own right.
For the related sine dilaton gravity model, a proposal was made for the holographic
screen to be in a complexified direction of the geometry [59], matching with where the
screen is in the analytically continued sinh dilaton gravity model. In this case, this is where
the SYK fermions live, and we have a precise link with the underlying microscopic system.
As it is good practice to isolate the different issues and treat the difficulties one at a time, we
study in this work the sinh dilaton gravity case (which is simpler), leaving a more detailed
investigation for the sine dilaton gravity and DSSYK case to future work.
The remainder of this paper is organized as follows. In section 2 , we review and
generalize the bootstrap argument of finding the q-CFT two-point function from global
conformal q-invariance. Section 3 defines the bulk gravitational model we will study here.
We take the probe regime of the boundary two-point function and match it precisely onto
the bootstrapped formula of section 2. We comment on various routes for the future in
the concluding section 4 . The appendices contain various supplementary material. In
particular, Appendix B contains an in-depth discussion on 2d dilaton gravity models, the
holographic counterterms, and the quantization of sinh dilaton gravity.Appendices A
and C contain technical details on the relevant representations and on some mathematical
manipulations withq-functions.
